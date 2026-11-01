# Agent skills

Personal skill collection for soumyyy: investigation, learning, writing, code review, and PR workflows.

## Included skills

- `soumya-mode`: invocation-only personal workflow for autonomous work with system context, evidence, and continuous improvement.

- `why`: investigate design rationale with cited historical evidence.
- `recall`: reconstruct project context and verify its current state.
- `reflect`: identify durable lessons and propose targeted skill improvements.
- `automate-me`: draft or revise a personal mode from demonstrated preferences.
- `teach`: explain how a system works and why it has its current shape.
- `technical-writing`: write and review technical documents and developer prose.
- `demo`: end-to-end narrated vertical explainers with a 2D presenter, real speech timing, audio analysis and MP4 verification. Designed around the primary MacBook’s M3 chip and 8 GiB memory; Blender is optional, not required.
- `seo`: diagnose and improve organic-search visibility through evidence-backed crawl, indexing, metadata, content, structured-data and performance checks. Use `$seo`; ranking outcomes and external account actions remain separate from code fixes.
- `unslop`: audit and refine an existing screen’s visual design while preserving behavior, brand, data and accessibility. Use `$unslop` or ask to polish the UI; it does not handle prose cleanup.
- `sharpen`: explicitly invoke `$sharpen` to deepen and rewrite a prompt using primary material, concrete methods, and independent verification. It does not execute the task.

## PR workflows

- `council`: two-member independent review with **GPT Sol 6.1 and Claude Opus 5.5**, up to three rounds by default. No third provider and no model substitutions.
- `sol-loop`: bounded review with **GPT Sol 6.1**, three rounds by default, with a finding ledger and focused rechecks.
- `modernize`: reassess an old PR against current product and architecture before rebasing; recommend modernize, rework, or close.
- `full-stop`: complete, prove, review, file, and babysit a PR, then leave it open and unmerged. It is self-contained and does not install `full-send`.

Supporting dependencies are included: `file-pr`, `babysit-pr` (with its `pr-wait` script for non-T3 hosts), and `leaving-pr-comments`. In T3, PR monitoring uses the host watcher instead of the script. A caller can load these dependencies when running its workflow.

Invoke with `$council`, `$sol-loop`, `$modernize`, or `$full-stop`. An ordinary emphatic “full stop” is not a workflow request. These workflows do not grant general permission to merge or publish outside the requested task.

Both review skills resolve the exact named versions through the host catalog at invocation time. Codex and Claude providers were exposed during setup, but the catalog response did not list those model versions. No live model calls were run: if either requested version cannot be confirmed or launched, the skill reports the blocker instead of changing models. Supported reasoning settings go through the host's options schema.

## Install in Codex

With GitHub CLI authenticated for this private repository, clone it and install the skill folders:

```sh
gh repo clone soumyyy/agent-skills
cd agent-skills
python3 scripts/install.py
```

The installer copies to `$CODEX_HOME/skills`, defaulting to `~/.codex/skills`. It refuses to replace an existing skill with different contents. Skills become available on the next turn. Invoke by name, for example `$why` or `$teach`.

Edit the repository copies, then commit and push when ready. Installed copies do not sync automatically. To update an installed skill, back up or remove its old folder and rerun the installer.

## Install in Claude Code

```sh
python3 scripts/install.py --agent claude
```

This installs to `~/.claude/skills/`. Invoke `/demo`, `/reflect`, `/seo`, or another skill by name in a new Claude Code session. Existing differing skills and symlink destinations are never overwritten. Repeating the command is safe when the installed copies match.

The installer generates Claude-compatible entrypoints, mapping the personal mode and sharpen’s invocation-only policy to `disable-model-invocation: true`. Source skills and Codex installations remain unchanged. Generated entrypoints explain Claude paths, invocation and missing-capability handling. Tool access is session-specific: standalone Claude cannot run cross-provider council or Sol reviews without a harness exposing those exact models. Video workflows require the installed HyperFrames/media skills and their tools.

Use `--dest <directory>` for an isolated installation. Claude copies do not automatically sync; preserve any personal edits before replacing an older generated copy.

## Runtime and configuration

Skills use the current host’s tools, model catalog, and authorization rules. Runtime compatibility references explain how to run workflows in Codex and T3. The personal mode and sharpen require explicit invocation; other workflows use their documented request triggers.

No chat history or credentials are included. Use `$automate-me` to revise the personal mode from future feedback.

## License notices

Required license and copyright notices are retained in [LICENSE](LICENSE) and [LICENSE.third-party](LICENSE.third-party). The UI-polishing workflow has a separate [license notice](skills/unslop/NOTICE.md) and [CC BY 4.0 license](skills/unslop/LICENSE).
