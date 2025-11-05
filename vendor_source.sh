#!/usr/bin/env bash
set -euo pipefail

# Change folder to correct name
cd HyprPanel-0a961ce8a959c521f41546af7f355e04adee5503

cat > .npmrc <<'EOF'
node-linker=hoisted
store-dir=.pnpm-store
cache-dir=.pnpm-cache
virtual-store-dir=.pnpm
EOF

pnpm install --lockfile-only
pnpm fetch
pnpm install --offline --frozen-lockfile

echo "Verifying @types/node metadata..."
jq -e '.versions."22.15.17"' .pnpm-cache/metadata-v1.3/registry.npmjs.org/@types/node.json > /dev/null && echo "OK"

ARCHIVE_NAME="hyprpanel-pnpm-offline-cache.tar.gz"
tar --mtime='2025-01-01' \
    --owner=0 --group=0 --numeric-owner \
    --dereference \
    -czf "../$ARCHIVE_NAME" \
    package.json \
    pnpm-lock.yaml \
    .npmrc \
    .pnpm-store \
    .pnpm-cache \
    .pnpm \
    node_modules

echo "Archive created: ../$ARCHIVE_NAME"
echo "Size: $(du -h ../$ARCHIVE_NAME | cut -f1)"
