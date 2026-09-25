#!/usr/bin/env node

import http from 'http';
import fs from 'fs';
import path from 'path';
import { spawn } from 'child_process';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const SITE_DIR = path.resolve(__dirname, '..');
const PUBLIC_DIR = path.join(SITE_DIR, 'public');
const PORT = 1313;

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.yaml': 'text/yaml; charset=utf-8',
  '.yml': 'text/yaml; charset=utf-8',
  '.xml': 'application/xml; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.wasm': 'application/wasm',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
};

// 1. Serveur HTTP statique pour servir public/
const server = http.createServer((req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, HEAD, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', '*');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  let urlPath = decodeURIComponent(req.url.split('?')[0]);
  let filePath = path.join(PUBLIC_DIR, urlPath);

  // Sécurité anti-traversée de répertoire
  if (!filePath.startsWith(PUBLIC_DIR)) {
    res.writeHead(403);
    res.end('Forbidden');
    return;
  }

  // Si c'est un dossier, chercher index.html
  if (fs.existsSync(filePath) && fs.statSync(filePath).isDirectory()) {
    filePath = path.join(filePath, 'index.html');
  }

  if (!fs.existsSync(filePath) || !fs.statSync(filePath).isFile()) {
    if (fs.existsSync(filePath + '.html') && fs.statSync(filePath + '.html').isFile()) {
      filePath = filePath + '.html';
    } else {
      res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
      res.end('404 Not Found');
      return;
    }
  }

  const ext = path.extname(filePath).toLowerCase();
  const contentType = MIME_TYPES[ext] || 'application/octet-stream';

  res.writeHead(200, {
    'Content-Type': contentType,
    'Cache-Control': 'no-cache',
  });
  fs.createReadStream(filePath).pipe(res);
});

server.listen(PORT, '127.0.0.1', () => {
  console.log(`🌐 Serveur Hugo local actif sur http://localhost:${PORT} (servant public/)`);
});

// 2. Déclenchement de Hugo uniquement sur modification
let isBuilding = false;
let pendingBuild = false;
let debounceTimer = null;

function runHugoBuild(triggerFile = '') {
  if (isBuilding) {
    pendingBuild = true;
    return;
  }

  isBuilding = true;
  const startTime = Date.now();
  console.log(`\n📝 Changement détecté${triggerFile ? ` (${path.basename(triggerFile)})` : ''} : Recompilation Hugo en cours...`);

  const hugoArgs = [
    '--environment', 'sveltia',
    '--buildFuture',
    '--disableKinds=RSS,sitemap,taxonomy,term'
  ];

  const hugoProc = spawn('hugo', hugoArgs, { cwd: SITE_DIR, stdio: 'inherit' });

  hugoProc.on('close', (code) => {
    isBuilding = false;
    const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
    if (code === 0) {
      console.log(`✅ Site recompilé avec succès en ${elapsed}s.`);
    } else {
      console.error(`⚠️ Erreur de compilation Hugo (code ${code}).`);
    }

    if (pendingBuild) {
      pendingBuild = false;
      runHugoBuild();
    }
  });
}

function onFileChange(eventType, filename) {
  if (!filename) return;
  // Ignorer les fichiers cachés, temporaires ou swap
  if (filename.startsWith('.') || filename.endsWith('~') || filename.endsWith('.tmp')) return;

  clearTimeout(debounceTimer);
  const delay = filename.includes('admin-preview.md') ? 150 : 600;
  debounceTimer = setTimeout(() => {
    runHugoBuild(filename);
  }, delay);
}

// Surveillance récursive du dossier content/
const contentDir = path.join(SITE_DIR, 'content');
if (fs.existsSync(contentDir)) {
  fs.watch(contentDir, { recursive: true }, onFileChange);
  console.log(`👀 Surveillance active sur ${path.relative(SITE_DIR, contentDir)}/`);
}

// Gestion de l'arrêt
process.on('SIGINT', () => {
  server.close(() => process.exit(0));
});
process.on('SIGTERM', () => {
  server.close(() => process.exit(0));
});
