#!/usr/bin/env bash
# ==============================================================================
# publish.sh - Synchronisation du dossier public/ avec l'hébergement Infomaniak
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Chargement du fichier de configuration des secrets s'il existe
# (Ce fichier est listé dans .gitignore pour ne pas être versionné)
SECRETS_FILE=""
if [ -f "$SCRIPT_DIR/.env.deploy" ]; then
  SECRETS_FILE="$SCRIPT_DIR/.env.deploy"
elif [ -f "$SCRIPT_DIR/.env" ]; then
  SECRETS_FILE="$SCRIPT_DIR/.env"
elif [ -f "$SCRIPT_DIR/publish.secrets" ]; then
  SECRETS_FILE="$SCRIPT_DIR/publish.secrets"
fi

if [ -n "$SECRETS_FILE" ]; then
  # shellcheck source=/dev/null
  set -a
  source "$SECRETS_FILE"
  set +a
fi

# Variables de connexion (depuis le fichier de secrets ou l'environnement)
REMOTE_USER="${INFOMANIAK_USER:-}"
REMOTE_HOST="${INFOMANIAK_HOST:-}"
REMOTE_PORT="${INFOMANIAK_PORT:-22}"
TARGET_DIR="${INFOMANIAK_TARGET_DIR:-}"
SOURCE_DIR="${SOURCE_DIR:-$SCRIPT_DIR/public/}"

DRY_RUN=false
DO_BUILD=false

usage() {
  cat <<EOF
Usage: $(basename "$0") [OPTIONS]

Synchronise le dossier public/ de drgoulu.com avec le serveur Infomaniak via rsync SSH.
Les paramètres de connexion sont lus depuis le fichier .env.deploy (non versionné).

Options:
  -n, --dry-run     Effectue une simulation sans modifier les fichiers distants
  -b, --build       Recompile le site Hugo et régénère l'index de recherche avant l'envoi
  -h, --help        Affiche cette aide et quitte

Fichier de configuration requis (.env.deploy) :
  INFOMANIAK_USER="utilisateur_ssh"
  INFOMANIAK_HOST="serveur.infomaniak.com"
  INFOMANIAK_PORT="22"
  INFOMANIAK_TARGET_DIR="web/hugo/"
EOF
  exit 0
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -n|--dry-run)
      DRY_RUN=true
      shift
      ;;
    -b|--build)
      DO_BUILD=true
      shift
      ;;
    -h|--help)
      usage
      ;;
    *)
      echo "Option inconnue : $1" >&2
      echo "Utilisez --help pour voir les options disponibles." >&2
      exit 1
      ;;
  esac
done

# 1. Vérification des identifiants requis
if [ -z "$REMOTE_USER" ] || [ -z "$REMOTE_HOST" ] || [ -z "$TARGET_DIR" ]; then
  echo "❌ Erreur : Identifiants Infomaniak manquants." >&2
  echo "Veuillez créer ou renseigner le fichier '.env.deploy' à la racine du projet :" >&2
  echo "  cp .env.deploy.example .env.deploy" >&2
  echo "Puis éditez-le avec vos paramètres de connexion." >&2
  exit 1
fi

# S'assurer que les chemins se terminent par un slash pour rsync
[[ "${TARGET_DIR}" != */ ]] && TARGET_DIR="${TARGET_DIR}/"
[[ "${SOURCE_DIR}" != */ ]] && SOURCE_DIR="${SOURCE_DIR}/"

# 2. Compilation préalable si demandée
if [ "$DO_BUILD" = true ]; then
  echo "🔨 Compilation du site avec Hugo..."
  HUGO_ENVIRONMENT=production hugo --gc --minify -b "https://drgoulu.com/"
  if command -v pnpm &>/dev/null && [ -f "package.json" ]; then
    echo "🔍 Indexation Pagefind..."
    pnpm run pagefind
  fi
fi

# 3. Vérification du dossier source
if [ ! -d "$SOURCE_DIR" ] || [ -z "$(ls -A "$SOURCE_DIR" 2>/dev/null)" ]; then
  echo "❌ Erreur : Le dossier source '$SOURCE_DIR' est vide ou introuvable." >&2
  echo "Veuillez d'abord générer le site avec 'hugo' ou exécuter '$(basename "$0") --build'." >&2
  exit 1
fi

# 4. Préparation des arguments rsync
RSYNC_FLAGS=(
  -avz
  --delete
  --human-readable
  --progress
  --exclude='/.git*'
  -e "ssh -p ${REMOTE_PORT}"
)

if [ "$DRY_RUN" = true ]; then
  RSYNC_FLAGS+=(--dry-run)
  echo "🔍 [SIMULATION] Mode dry-run activé (aucun fichier ne sera modifié sur le serveur)."
fi

echo "🚀 Synchronisation vers Infomaniak :"
echo "   Source       : ${SOURCE_DIR}"
echo "   Destination  : ${REMOTE_USER}@${REMOTE_HOST}:${TARGET_DIR}"
echo "------------------------------------------------------------"

rsync "${RSYNC_FLAGS[@]}" "${SOURCE_DIR}" "${REMOTE_USER}@${REMOTE_HOST}:${TARGET_DIR}"

echo "------------------------------------------------------------"
if [ "$DRY_RUN" = true ]; then
  echo "✅ Simulation terminée avec succès."
else
  echo "✅ Synchronisation terminée avec succès !"
fi
