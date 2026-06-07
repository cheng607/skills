#!/usr/bin/env bash
# Copy design token assets into a project.
# Usage: ./scripts/scaffold.sh [target-directory]

set -euo pipefail

TARGET="${1:-.}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ASSETS="${SCRIPT_DIR}/../assets"

mkdir -p "${TARGET}/styles" "${TARGET}/config"

cp "${ASSETS}/design-tokens-template.json" "${TARGET}/styles/design-tokens.json"
cp "${ASSETS}/tailwind-theme-template.js" "${TARGET}/config/tailwind.theme.js"

echo "Copied design tokens to ${TARGET}/styles/design-tokens.json"
echo "Copied Tailwind theme to ${TARGET}/config/tailwind.theme.js"
echo "Next: import tokens into CSS variables and merge tailwind.theme.js into tailwind.config.js"
