import { copyFile, lstat, mkdir, readFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const out = path.join(root, 'dist');
const names = JSON.parse(await readFile(path.join(root, 'static-assets.json'), 'utf8'));
if (!Array.isArray(names) || new Set(names).size !== names.length ||
    names.some((name) => !/^[a-z0-9-]+\.(html|css|js)$/.test(name)) ||
    !['index.html', 'site.js', 'style.css'].every((name) => names.includes(name))) {
  throw new Error('静态资源白名单格式错误或缺少必需入口。');
}

const items = await readdir(root, { withFileTypes: true });
const unknown = items.filter((item) => item.name.endsWith('.html') && !names.includes(item.name));
if (unknown.length) throw new Error(`存在未批准发布的HTML：${unknown.map((item) => item.name).join('、')}`);
for (const name of names) {
  const info = await lstat(path.join(root, name));
  if (!info.isFile() || info.isSymbolicLink()) throw new Error(`静态资源不是普通文件：${name}`);
}

let outInfo;
try { outInfo = await lstat(out); } catch (error) { if (error.code !== 'ENOENT') throw error; }
if (outInfo && (!outInfo.isDirectory() || outInfo.isSymbolicLink())) {
  throw new Error('dist必须是项目内普通目录，不能使用符号链接。');
}
const existing = outInfo ? await readdir(out, { withFileTypes: true }) : [];
for (const item of existing) {
  if (!item.isFile() || item.isSymbolicLink() || !names.includes(item.name)) {
    throw new Error(`dist存在未受管内容，未作更改，请先检查：${item.name}`);
  }
}

// 所有输入与输出边界通过后，只复制白名单文件，不删除任何未知内容。
if (!outInfo) await mkdir(out);
for (const name of names) await copyFile(path.join(root, name), path.join(out, name));
console.log(`构建完成：${names.filter((name) => name.endsWith('.html')).length}个HTML页面、2个共享资源 → dist/`);
console.log('未包含.workbuddy、outputs、Git信息、ZIP、环境文件或维护脚本。');
