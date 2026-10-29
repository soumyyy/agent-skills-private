---
name: council
description: "Use when the user requests council or a council review. Obtain independent review from GPT Sol 6.1 and Claude Opus 5.5, reconcile evidence-backed findings, and bound follow-up rounds."
---

# Council

Read [runtime compatibility](references/runtime.md). The panel has exactly two members: **OpenAI GPT Sol 6.1** and **Anthropic Claude Opus 5.5**. Do not add Gemini or substitute a different version. This skill reviews; it does not independently authorize publishing or merging.

## Ground and resolve

State the user's goal, scope, base SHA, exact reviewed head, and relevant checks. Fix known in-scope issues and run covering checks before review. Preserve unrelated work. For a design question, give both reviewers the same requirements and constraints instead of inventing a diff.

In T3 call `orchestrator_capabilities` to resolve the requested versions to actual provider/model IDs and supported high reasoning options. Sol 6.1 may be exposed as `gpt-6.1-sol`; verify it. Resolve Opus 5.5 from the actual catalog, not a guessed slug. If either version cannot be confirmed or launched, report that blocker; do not claim a complete council. Outside T3 use a harness capable of those exact versions, otherwise report the limitation.

## Independent review

Start one read-only review delegate per member in parallel, with the same goal, repo, base/head, scoped diff command, untracked-file scope, checks and missing checks. Tell each to read surrounding callers, verify claims, preserve scope, and return:

- `APPROVE` or `CHANGES` on the specified head.
- Findings with stable IDs, severity, file and line, evidence, and the smallest fix.
- A score out of 10, only if the reviewer actually provides one.

Delegates must not edit, commit, push, post comments, spawn children, or watch PRs. Do not edit reviewed files while either review runs. Follow each delegate's returned continuation instructions; do not poll.

## Reconcile and recheck

Validate each claim against code or observed behavior. Fix real in-scope bugs with the smallest change. Reject unsupported or out-of-scope requests with evidence. Keep a ledger of findings, decisions, and reviewed heads. Agreement and scores are not substitutes for proof.

Default to at most **three full rounds**, unless the user requests another budget. After behavior changes, request fresh reviews from both members on the updated head; follow-up briefs include the original scope, ledger, previous findings and changed code. Recheck only changed behavior and outstanding findings. Nits or prose-only fixes do not require another round. Stop early when both approve the current behavior diff and no substantiated concern remains.

If disagreement persists after two evidence-backed exchanges on a finding, or the round budget ends, report both positions and the unresolved decision. A missing response, failed delegate, or exhausted budget is not approval. Cancel delegates that are no longer needed.

## Report

Give the reviewed head, actual model versions, round count, verdicts, accepted and declined findings with reasons, verification, and remaining gaps. Record scores only as returned; use `no score` otherwise. When updating a PR is authorized, put the review summary in its description rather than a filler comment. Link the PR through the host after updating it. If there is no authorized PR update, report in the conversation.
