#!/usr/bin/env bash
# Scaffold a new component file from the props template.
# Usage: ./scripts/scaffold.sh Button src/components/Button.tsx

set -euo pipefail

NAME="${1:?Component name required, e.g. Button}"
TARGET="${2:-src/components/${NAME}.tsx}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE="${SCRIPT_DIR}/../assets/component-props-template.ts"

if [[ ! -f "$TEMPLATE" ]]; then
  echo "Template not found: $TEMPLATE" >&2
  exit 1
fi

mkdir -p "$(dirname "$TARGET")"
sed "s/Button/${NAME}/g; s/button/${NAME,}/g" "$TEMPLATE" > "$TARGET"
echo "Created ${TARGET} from template. Customize props and styling before use."
