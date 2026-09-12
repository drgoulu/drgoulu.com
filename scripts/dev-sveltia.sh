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
  kill $(jobs -p) 2>/dev/null || true
  exit 0
}
trap cleanup SIGINT SIGTERM EXIT

# 1. Lancer le serveur Vite de Sveltia CMS en arrière-plan
(cd "$SVELTIA_DIR" && pnpm dev) &

# Petit délai pour laisser Vite démarrer
sleep 1

# 2. Lancer le serveur Hugo
(cd "$SITE_DIR" && hugo server --disableFastRender)
