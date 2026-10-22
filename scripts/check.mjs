import assert from 'node:assert/strict';
import { lstat, readFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const items = await readdir(root, { withFileTypes: true });
const pages = items.filter((item) => item.isFile() && item.name.endsWith('.html')).map((item) => item.name).sort();
const manifest = JSON.parse(await readFile(path.join(root, 'static-assets.json'), 'utf8'));
assert(Array.isArray(manifest), '静态资源白名单须为数组');
assert.equal(new Set(manifest).size, manifest.length, '静态资源白名单重复');
assert(manifest.every((name) => /^[a-z0-9-]+\.(html|css|js)$/.test(name)), '静态资源白名单含不安全路径');
assert.deepEqual([...manifest].sort(), [...pages, 'style.css', 'site.js'].sort(), '根目录页面与资源白名单不一致');
for (const name of manifest) {
  const info = await lstat(path.join(root, name));
  assert(info.isFile() && !info.isSymbolicLink(), `${name}不是普通静态文件`);
}
const allowed = new Set(manifest);
const docs = new Map();
const anchors = new Map();
const decode = (value) => value.replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#39;/g, "'");

assert.equal(pages.length, 83, '当前版本应有83个HTML页面；新增页面时同步此检查。');
assert.equal(pages.filter((name) => name.startsWith('e-')).length, 66, '当前版本应有66个词条。');
assert.equal(pages.filter((name) => name.startsWith('category-')).length, 8, '应有8个主题栏目。');

for (const name of pages) {
  const text = await readFile(path.join(root, name), 'utf8');
  assert.match(text, /<!DOCTYPE html>/i, `${name}缺少文档声明`);
  assert.match(text, /<html\b[^>]*lang="zh-CN"/, `${name}缺少中文语言声明`);
  assert.match(text, /name="viewport"[^>]*width=device-width/, `${name}缺少移动视口声明`);
  assert.match(text, /<title>[^<]+<\/title>/, `${name}缺少标题`);
  assert(!/地球|现实生物|虚构谱系|虚构地域|人类世界|作者|小说叙事|漫画分镜/.test(text), `${name}含外部世界解释`);
  assert(!/(?:href|src)="(?:\/Users\/|[A-Za-z]:\\)/i.test(text), `${name}含本地绝对路径`);
  const ids = [...text.matchAll(/\bid="([^"]+)"/g)].map((match) => match[1]);
  assert.equal(new Set(ids).size, ids.length, `${name}有重复DOM标识`);
  docs.set(name, text);
  anchors.set(name, new Set(ids));
}

let linkCount = 0;
for (const [name, text] of docs) {
  // 当前生成器统一使用双引号；同时校验链接、脚本、样式及搜索表单入口。
  for (const match of text.matchAll(/\b(?:href|src|action)="([^"]+)"/g)) {
    const value = decode(match[1]);
    assert(!/^(?:javascript:|data:|file:)/i.test(value), `${name}含不允许的链接协议：${value}`);
    if (/^(?:https?:|mailto:)/i.test(value)) continue;
    const url = new URL(value, `https://local.test/${name}`);
    assert.equal(url.origin, 'https://local.test', `${name}包含未明确允许的外部链接`);
    const target = decodeURIComponent(url.pathname.slice(1)) || 'index.html';
    assert(allowed.has(target), `${name}引用缺失或非部署资源：${value}`);
    if (url.hash) {
      const anchor = decodeURIComponent(url.hash.slice(1));
      assert(anchors.get(target)?.has(anchor), `${name}引用缺失锚点：${value}`);
    }
    linkCount += 1;
  }
  if (name.startsWith('e-')) {
    for (const id of ['overview', 'connections', 'gaps', 'references']) {
      assert(anchors.get(name).has(id), `${name}缺少百科必需区域：${id}`);
    }
    assert.match(text, /<dl class="facts">/, `${name}缺少事实概要`);
  }
}

const getIndex = (name) => {
  const match = docs.get(name).match(/<script type="application\/json" id="search-data">([\s\S]*?)<\/script>/);
  assert(match, `${name}缺少全文索引`);
  return JSON.parse(match[1]);
};
const all = getIndex('all.html');
const search = getIndex('search.html');
assert.deepEqual(all, search, '全部词条和搜索页面全文索引不一致');
assert.equal(all.length, 66, '全文索引不完整');
assert.equal(new Set(all.map((entry) => entry.id)).size, 66, '全文索引重复');
for (const entry of all) {
  assert(docs.has(`e-${entry.id}.html`), `索引对应的词条缺失：${entry.id}`);
  assert(entry.text.length > 100, `全文索引正文不足：${entry.id}`);
  for (const key of ['dimensions', 'scenes', 'tags']) {
    assert(Array.isArray(entry[key]) && entry[key].length > 0, `索引分类不足：${entry.id}/${key}`);
  }
}
const city = docs.get('e-city-networks.html');
assert.match(city, /id="diagram-city"/, '双网城市缺少节点图');
assert.match(city, /id="diagram-city-section"/, '双网城市缺少剖面图');
assert.equal([...docs.get('atlas.html').matchAll(/<figure class="diagram"/g)].length, 16, '图解总览应包含16幅图解');
assert.match(await readFile(path.join(root, 'style.css'), 'utf8'), /@media\(max-width:640px\)/, '缺少移动布局');

const config = JSON.parse(await readFile(path.join(root, 'vercel.json'), 'utf8'));
assert.equal(config.framework, null);
assert.equal(config.buildCommand, 'npm run build');
assert.equal(config.installCommand, '');
assert.equal(config.outputDirectory, 'dist');
assert.equal(config.cleanUrls, false, '须保持现有.html路径');
assert(!config.rewrites, '多页静态站不应添加单页应用重写');
const pkg = JSON.parse(await readFile(path.join(root, 'package.json'), 'utf8'));
assert(!Object.keys(pkg.dependencies || {}).length && !Object.keys(pkg.devDependencies || {}).length, '当前项目应无第三方构建依赖');

for (const name of ['site.js', 'scripts/build.mjs', 'scripts/serve.mjs', 'scripts/check.mjs']) {
  const result = spawnSync(process.execPath, ['--check', path.join(root, name)], { encoding: 'utf8' });
  assert.equal(result.status, 0, `${name}语法错误：${result.stderr}`);
}
console.log(`校验通过：${pages.length}个页面、66个词条、16幅图解、${linkCount}个站内资源与锚点引用。`);
console.log('全文索引、移动布局、JavaScript语法与Vercel部署配置检查通过。');
