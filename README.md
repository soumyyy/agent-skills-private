# Agent skills

Personal skill collection for soumyyy, starting with six skills adapted from Lauren Tan (poteto)'s [pstack](https://github.com/cursor/plugins/tree/main/pstack).

## Included skills

- `why`: investigate design rationale with cited historical evidence.
- `recall`: reconstruct project context and verify its current state.
- `reflect`: identify durable lessons and propose targeted skill improvements.
- `automate-me`: draft or revise a personal mode from demonstrated preferences.
- `teach`: explain how a system works and why it has its current shape.
- `technical-writing`: write and review technical documents and developer prose.

## Install in Codex

With GitHub CLI authenticated for this private repository, clone it and install the six folders:

```sh
gh repo clone soumyyy/agent-skills
cd agent-skills
python3 scripts/install.py
```

The installer copies to `$CODEX_HOME/skills`, defaulting to `~/.codex/skills`. It refuses to replace an existing skill with different contents. Skills become available on the next turn. Invoke by name, for example `$why` or `$teach`.

Edit the repository copies, then commit and push when ready. Installed copies do not sync automatically. To update an installed skill, back up or remove its old folder and rerun the installer.

## Adaptation and provenance

`UPSTREAM.json` pins the source commit and hashes every original imported file. All upstream supporting references are retained. Each entrypoint links a runtime adapter that replaces Cursor-specific tools, hardcoded model selection, transcript paths, unavailable skill dependencies, and external-write assumptions with the current host's capabilities and authorization rules. Unsupported Cursor frontmatter was removed; normal Codex skill discovery remains enabled.

No chat history, credentials, or existing private skills are included. `automate-me` is installed as a workflow; a personal mode has not yet been generated.

The imported material is MIT licensed. See [LICENSE](LICENSE) for the upstream copyright and license.
