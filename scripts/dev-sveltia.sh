#!/usr/bin/env bash
set -e

# Détermination des chemins
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SVELTIA_DIR="$(cd "$SITE_DIR/../sveltia-cms" 2>/dev/null && pwd || true)"

if [ -z "$SVELTIA_DIR" ] || [ ! -d "$SVELTIA_DIR" ]; then
  echo "❌ Erreur : Le dossier sveltia-cms est introuvable à côté de drgoulu.com"
  exit 1
fi

echo "=========================================================="
echo "🚀 Lancement du développement local Sveltia CMS + Hugo"
echo "   - Sveltia CMS : http://localhost:5173"
echo "   - Site Hugo   : http://localhost:1313/admin/"
echo "=========================================================="
echo "Appuyez sur Ctrl+C pour arrêter les deux serveurs."
echo ""

# Arrêter tous les serveurs quand l'utilisateur fait Ctrl+C
cleanup() {
  echo -e "\n🛑 Arrêt des serveurs en cours..."
  rm -f "$SITE_DIR/content/admin-preview.md" 2>/dev/null || true
  kill $(jobs -p) 2>/dev/null || true
  exit 0
}
trap cleanup SIGINT SIGTERM EXIT

# Créer le fichier d'aperçu temporaire avant le démarrage de Hugo pour qu'il soit routé immédiatement
if [ ! -f "$SITE_DIR/content/admin-preview.md" ]; then
  cat << 'EOF' > "$SITE_DIR/content/admin-preview.md"
---
title: Aperçu du brouillon
slug: admin-preview
date: '2026-09-13'
draft: false
build:
  list: never
  render: always
---
EOF
fi

# 1. Vérifier si un build initial ou Pagefind est nécessaire
FORCE_PAGEFIND=false
if [ "$1" = "--pagefind" ] || [ "$1" = "-p" ]; then
  FORCE_PAGEFIND=true
fi

if [ "$FORCE_PAGEFIND" = true ] || [ ! -f "$SITE_DIR/static/pagefind/pagefind.js" ]; then
  echo "🔍 Construction du site et indexation Pagefind pour la recherche locale..."
  (cd "$SITE_DIR" && hugo --environment sveltia --cleanDestinationDir --buildFuture && pnpm exec pagefind --site public --output-path static/pagefind)
elif [ ! -f "$SITE_DIR/public/admin/index.html" ]; then
  echo "📦 Aucun build existant détecté dans public/. Compilation initiale de Hugo..."
  (cd "$SITE_DIR" && hugo --environment sveltia --buildFuture --disableKinds=RSS,sitemap,taxonomy,term)
else
  echo "⚡ Site déjà compilé dans public/ et index Pagefind présent. Démarrage immédiat !"
fi

# 2. Lancer le serveur Vite de Sveltia CMS en arrière-plan
echo "🚀 Lancement de Sveltia CMS (Vite)..."
(cd "$SVELTIA_DIR" && VITE_SITE_URL="http://localhost:1313" HUGO_CONTENT_DIR="$SITE_DIR/content" ./node_modules/.bin/vite) &

# 3. Lancer le serveur HTTP local (port 1313) avec surveillance des changements de content/
node "$SCRIPT_DIR/dev-server.mjs"


