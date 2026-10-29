# Agent skills

Personal skill collection for soumyyy: a personal mode, investigation and learning skills from Lauren Tan (poteto)'s [pstack](https://github.com/cursor/plugins/tree/main/pstack), and PR workflows from Theo Browne's [tstack](https://github.com/t3dotgg/tstack).

## Included skills

- `soumya-mode`: invocation-only personal workflow for autonomous work with system context, evidence, and continuous improvement.

- `why`: investigate design rationale with cited historical evidence.
- `recall`: reconstruct project context and verify its current state.
- `reflect`: identify durable lessons and propose targeted skill improvements.
- `automate-me`: draft or revise a personal mode from demonstrated preferences.
- `teach`: explain how a system works and why it has its current shape.
- `technical-writing`: write and review technical documents and developer prose.
- `sharpen`: explicitly invoke `$sharpen` to deepen and rewrite a prompt using primary material, concrete methods, and independent verification. It does not execute the task.

## PR workflows from tstack

- `council`: two-member independent review with **GPT Sol 6.1 and Claude Opus 5.5**, up to three rounds by default. No third provider and no model substitutions.
- `sol-loop`: bounded review with **GPT Sol 6.1**, three rounds by default, with a finding ledger and focused rechecks.
- `modernize`: reassess an old PR against current product and architecture before rebasing; recommend modernize, rework, or close.
- `full-stop`: complete, prove, review, file, and babysit a PR, then leave it open and unmerged. It is self-contained and does not install `full-send`.

Supporting dependencies are included: `file-pr`, `babysit-pr` (with its upstream `pr-wait` script for non-T3 hosts), and `leaving-pr-comments`. In T3, PR monitoring uses the host watcher instead of the script. A caller can load these dependencies when running its workflow.

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

## Adaptation and provenance

`UPSTREAM.json` pins pstack; `TSTACK-UPSTREAM.json` pins tstack. Both record hashes of the original imported files before adaptation. Upstream supporting files are retained. Imported entrypoints link a runtime adapter that replaces Cursor-specific tools, hardcoded model selection, transcript paths, unavailable skill dependencies, and external-write assumptions with the current host's capabilities and authorization rules. Unsupported Cursor frontmatter was removed from pstack. Normal Codex skill discovery remains enabled for the imported skills; the personal mode and sharpen have implicit invocation disabled. The tstack workflows have their own narrow request triggers.

No chat history, credentials, or existing private skills are included. Invoke the personal mode explicitly with `$soumya-mode`. Its `agents/openai.yaml` disables implicit invocation. `automate-me` can revise it from future feedback.

The imported material is MIT licensed. See [LICENSE](LICENSE) for Lauren Tan’s copyright and [LICENSE.tstack](LICENSE.tstack) for Theo Browne’s copyright. Runtime adaptations are maintained in this repository.
