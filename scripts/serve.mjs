import { createServer } from 'node:http';
import { lstat, readFile, realpath } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const project = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const root = process.argv.includes('--dist') ? path.join(project, 'dist') : project;
const rootInfo = await lstat(root);
if (!rootInfo.isDirectory() || rootInfo.isSymbolicLink()) throw new Error('预览目录须为普通项目目录。');
const realRoot = await realpath(root);
const allowed = new Set(JSON.parse(await readFile(path.join(project, 'static-assets.json'), 'utf8')));
const port = Number(process.env.PORT || 3000);
if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error('PORT须为1至65535的整数。');
const types = { '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8', '.js': 'text/javascript; charset=utf-8' };

const server = createServer(async (req, res) => {
  try {
    const pathname = decodeURIComponent(new URL(req.url, 'http://127.0.0.1').pathname);
    const name = pathname === '/' ? 'index.html' : pathname.slice(1);
    // 预览与构建使用同一静态范围，避免公开项目资料或系统文件。
    if (name.includes('/') || name.includes('\\') || name.startsWith('.') || !allowed.has(name)) {
      res.writeHead(404); res.end('页面不存在'); return;
    }
    if (req.method !== 'GET' && req.method !== 'HEAD') {
      res.writeHead(405, { Allow: 'GET, HEAD' }); res.end(); return;
    }
    const target = path.join(root, name);
    const info = await lstat(target);
    const resolved = await realpath(target);
    if (!info.isFile() || info.isSymbolicLink() || path.dirname(resolved) !== realRoot) {
      res.writeHead(404); res.end('页面不存在'); return;
    }
    const body = await readFile(resolved);
    res.writeHead(200, {
      'Content-Type': types[path.extname(name)],
      'Content-Length': body.length,
      'X-Content-Type-Options': 'nosniff',
      'Referrer-Policy': 'strict-origin-when-cross-origin',
      'Cache-Control': 'no-cache'
    });
    res.end(req.method === 'HEAD' ? undefined : body);
  } catch (error) {
    res.writeHead(error.code === 'ENOENT' || error instanceof URIError ? 404 : 500);
    res.end('无法读取页面');
  }
});
server.on('error', (error) => { console.error(`预览启动失败：${error.message}`); process.exitCode = 1; });
server.listen(port, '127.0.0.1', () => {
  console.log(`岚翎百科 ${process.argv.includes('--dist') ? '构建结果' : '源码'}预览：http://127.0.0.1:${port}`);
  console.log('按Ctrl+C停止。');
});
