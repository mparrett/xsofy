#!/usr/bin/env bash
# scripts/deploy.sh — publish to mparrett/xsofy:play
#
# Lifecycle:
#  - Local daily branch: experiment/mobile (full kruft, never pushed)
#  - Public deploy branch: play on mparrett/xsofy (curated history, force-pushed)
#
# Each run:
#  1. Rebuilds local lg from the let-go fork so native testing stays honest.
#  2. Updates mparrett/let-go:play to current experiment/js-bridge.
#  3. Clones experiment/mobile into a temp dir.
#  4. Filters history via git-filter-repo (allowlist below) — preserves every
#     commit's message + chronology, strips disallowed paths from every tree.
#     Commits that touched ONLY disallowed paths drop out.
#  5. Force-pushes the filtered history to mparrett/xsofy:play.
#  6. GitHub Actions deploys; live at https://mparrett.github.io/xsofy/ in ~1min.
#
# Caveats:
#  - SHAs on `play` will not match local SHAs (filter rewrites history).
#  - Commit messages on `play` are unchanged — write them so they describe
#    the *code change*, not bookkeeping in stripped paths.
#  - Adding a new top-level path that should ship requires editing the
#    allowlist below.

set -euo pipefail

LETGO="$HOME/projects-new/3p/let-go"
XSOFY="$HOME/projects-new/3p/xsofy"
SRC_BRANCH="experiment/mobile"
PUBLIC_REMOTE="https://github.com/mparrett/xsofy.git"
PUBLIC_BRANCH="play"

TMP="$(mktemp -d -t xsofy-deploy.XXXXXX)"
trap "rm -rf '$TMP'" EXIT

echo "==> rebuild local lg from let-go"
(cd "$LETGO" && go build -o ./lg .)

echo "==> push let-go experiment/js-bridge -> mparrett/let-go:play"
git -C "$LETGO" push fork experiment/js-bridge:play

echo "==> clone $SRC_BRANCH into $TMP/work"
git clone --branch "$SRC_BRANCH" --no-local "$XSOFY" "$TMP/work"

echo "==> filter history (allowlist)"
cd "$TMP/work"
git filter-repo \
    --path main.lg \
    --path xsofy/ \
    --path dev/shell.html \
    --path .github/workflows/deploy-pages.yml \
    --path LICENSE \
    --path .gitignore \
    --path README.md

echo "==> force-push filtered history to $PUBLIC_REMOTE:$PUBLIC_BRANCH"
git remote add origin "$PUBLIC_REMOTE"
git push -f origin "$SRC_BRANCH:$PUBLIC_BRANCH"

echo ""
echo "==> deploy triggered. watch: https://github.com/mparrett/xsofy/actions"
echo "==> live in ~1min:           https://mparrett.github.io/xsofy/"
