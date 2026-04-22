#!/usr/bin/env node
// Minimal Cloudflare Pages-style preview server for CI.
// Serves static files from repo root; for /path with no extension, tries /path.html.
// Used by auto-deploy.yml so Playwright tests run against the code about to deploy,
// not against stale production.

const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = process.cwd();
const PORT = process.env.PREVIEW_PORT ? Number(process.env.PREVIEW_PORT) : 8080;

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.webp': 'image/webp',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.txt': 'text/plain; charset=utf-8',
  '.xml': 'application/xml; charset=utf-8',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
};

function send(res, status, body, contentType) {
  res.writeHead(status, { 'Content-Type': contentType || 'text/plain; charset=utf-8' });
  res.end(body);
}

function serveFile(res, filePath) {
  fs.readFile(filePath, (err, data) => {
    if (err) return send(res, 404, 'Not Found');
    const ext = path.extname(filePath).toLowerCase();
    send(res, 200, data, MIME[ext] || 'application/octet-stream');
  });
}

const server = http.createServer((req, res) => {
  const urlPath = decodeURIComponent(req.url.split('?')[0]);
  // Resolve against ROOT, block path traversal
  const resolved = path.normalize(path.join(ROOT, urlPath));
  if (!resolved.startsWith(ROOT)) return send(res, 403, 'Forbidden');

  // 1. If path points to a file, serve it
  if (fs.existsSync(resolved) && fs.statSync(resolved).isFile()) {
    return serveFile(res, resolved);
  }
  // 2. If path is a directory, serve its index.html
  if (fs.existsSync(resolved) && fs.statSync(resolved).isDirectory()) {
    const idx = path.join(resolved, 'index.html');
    if (fs.existsSync(idx)) return serveFile(res, idx);
  }
  // 3. Cloudflare-Pages-style: /about → /about.html
  const withHtml = resolved.endsWith('.html') ? resolved : resolved + '.html';
  if (fs.existsSync(withHtml) && fs.statSync(withHtml).isFile()) {
    return serveFile(res, withHtml);
  }
  // 4. Fallback to 404.html
  const notFound = path.join(ROOT, '404.html');
  if (fs.existsSync(notFound)) {
    fs.readFile(notFound, (err, data) => {
      if (err) return send(res, 404, 'Not Found');
      res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8' });
      res.end(data);
    });
    return;
  }
  send(res, 404, 'Not Found');
});

server.listen(PORT, () => {
  console.log(`preview-server listening on http://localhost:${PORT} (root: ${ROOT})`);
});
