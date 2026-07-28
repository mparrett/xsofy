# This fork

`mparrett/xsofy` is a working fork of [`nooga/xsofy`](https://github.com/nooga/xsofy).
Upstream is where xsofy is developed and released. **This fork is where work
happens before it's worth proposing, and where playtest builds are hosted.**

The dividing line, set 2026-07-27:

> Upstream gets a branch when, and only when, we're opening a PR.
> Everything else — experiments, integration branches, playtest builds — lives here.

Before this, a playable URL required an upstream branch plus a PR plus a
maintainer applying a `deploy-preview` label, because Pages and the preview
workflow live upstream. That's how upstream accumulated 51 dead branches,
including two PRs titled "do not merge" opened purely to get a URL.

## Playtest builds

Publish any ref to a URL you can hand someone:

```
gh workflow run lab-deploy.yml --repo mparrett/xsofy \
  -f ref=<branch> -f name=<slug> -f action=deploy
```

→ **`https://mparrett.github.io/xsofy/lab/<slug>/`** (about 90 seconds)

Tear it down with `-f action=remove`. Or use the Actions tab: **Lab Deploy →
Run workflow**. `skip_smoke` publishes even if the boot gate fails, for when a
deliberately broken build is the thing you want to look at.

The ref has to exist *on this fork* — the workflow checks it out from here, not
from upstream. Each ref builds against **its own** `.let-go-version` and its own
`build-wasm` composite, so an experiment that moves the let-go pin is playtested
on the pin it moves to.

## Branch namespaces

| Prefix | What it is |
|---|---|
| `archive/*` | Retired upstream branches, preserved before deletion from `nooga/xsofy`. The largest namespace here (51). Restore one with `git push origin play/archive/<name>:refs/heads/<name>`. |
| `experiment/*`, `wt/*` | Spikes and worktree branches. Not proposed, may never be. |
| `ci/*` | Fork CI experiments (Pages publishing, preview plumbing). |
| `redecomp/*` | The 2026-07 mobile-stack re-cut rehearsal. Historical. |
| `main` | Mirrors upstream `main`, **plus one commit** — see below. |
| `gh-pages` | Published site. Four publishers write here; see below. |

## Two traps

**1. `main` deliberately sits ahead of upstream.** It carries fork-only
commits — currently `.github/workflows/lab-deploy.yml` and this file. The
workflow *has* to live here: `workflow_dispatch` only fires when the workflow
file is on the repository's default branch, so it can't go on a side branch.

Every fork-only commit here is a *new file that edits nothing*, which is
deliberate: it means a resync can never conflict.

```
git fetch origin
git rebase --onto origin/main <last-synced-upstream-sha> main
git push play --force-with-lease main
```

Resync by rebasing those commits. **Don't reset `main` to `origin/main`** —
that silently drops the lab deploy, and the workflow vanishes from the Actions
tab with no error to explain why.

**2. This fork must never run `deploy-pages.yml`.** That workflow hardcodes
`cname: xsofy.quest`, a domain owned by `nooga/xsofy`. Publishing it from here
collides with upstream's custom domain. It triggers on `push: tags: ['v*']`, so
**don't push a `v*` tag to this fork.** `lab-deploy.yml` sets no CNAME.

## gh-pages layout

Four publishers share the branch, so every one of them needs
`concurrency: group: gh-pages-publish` and `keep_files: true`, or they clobber
each other:

| Path | Written by |
|---|---|
| `/` | `deploy-pages.yml` — **do not run here** (see trap 2) |
| `/lab/<slug>/` | `lab-deploy.yml` — playtest builds |
| `/play/` | the older fork play bundle |
| `/pr-preview/pr-<N>/` | `pr-preview.yml` on fork PRs (self-label `deploy-preview`) |

Note the fork's Pages site is **not** production. Production is
`nooga/xsofy` → <https://xsofy.quest>.
