---
name: full-stop
description: "Use when explicitly asked to run full-stop or prepare a merge-ready PR without merging. Complete, prove, review, file, and babysit the change, then hand it back open and unmerged. Ordinary emphatic 'full stop' is not a workflow request."
---

# Full stop

Read [runtime compatibility](references/runtime.md). This workflow requires sibling `sol-loop`, `file-pr`, `babysit-pr`, and `leaving-pr-comments`, not `full-send`.

## Grant and boundary

When explicitly invoked as a workflow, complete the user's goal through an open, merge-ready PR. This covers branch creation, relevant verification, commits, pushes, review fixes, and updates to this task's PR. Rebase the task branch only as permitted by the host and repository, using an explicit `--force-with-lease` against the previously observed head when rewriting it.

**Never merge, enable auto-merge, enter a merge queue, push to the default branch, bypass protection, or delegate those actions.** Testing follows existing host and repository instructions. Production changes, data deletion, unrelated changes, and closing PRs need their own authorization.

Before work, check whether the PR already has auto-merge or queue membership. Disable auto-merge and remove it from the queue for this task; report those changes. Confirm again before every push and at handoff. If you cannot prevent automatic merging, stop and report the blocker.

## Finish and prove

1. Read the request and later corrections. Inspect the actual state, base, surrounding architecture and callers. Preserve unrelated changes; create a task branch if on the default branch. Choose the smallest change that solves the underlying problem.
2. Complete the implementation and verify observable behavior. Reproduce a bug before and after when practical. Run relevant repository checks. For UI or runtime changes, exercise the real surface when permitted. Add focused behavior coverage where it earns its cost. Record checks that failed before the change or could not run.
3. Read and run `sol-loop` for GPT Sol 6.1 review. Respect its budget. Verify findings yourself, fix real in-scope issues, and prove each behavior fix. No approval on an old behavior diff counts for a new one. If the required model or proof is unavailable, report the blocker rather than silently skipping review.
4. Fetch the actual base and update the branch when needed. If rebase or conflict resolution changes behavior, repeat the relevant proof and review. Use `file-pr` to open or update a real PR with the problem, resulting behavior, and a short proof summary. Link it through the host immediately after creation or push to an existing PR.
5. Use `babysit-pr` to handle CI and real review findings. Use `leaving-pr-comments` for authorized replies. Dismiss unsupported claims with a concrete reason. Recheck behavior changes before pushing. Keep changes within the original goal.

## Wait and hand off

In T3 handle actionable work, call `watch_pull_request`, and end the turn to await events. Do not poll or run another watcher. On a wake, inspect the current head and gate again. Only the parent owns the watch. Outside T3 use the permitted watcher from `babysit-pr`.

Before handoff, fetch the base and read the live PR. Readiness requires:

- Proof and review cover the final behavior diff and current head.
- Required checks pass; relevant review bots have finished and their findings are resolved or dismissed with evidence.
- No human review still requests changes.
- The PR is up to date and mergeable; newer overlapping base changes have been verified.
- The PR is open, not a draft, and cannot merge automatically.

Report **ready to merge**, **waiting for required approval**, or **blocked**, with the actual reason. Include the PR link, final head, proof, review outcome and remaining limits. State that it is open and unmerged. If someone else merged or closed it, report the observed state instead of claiming readiness.

In T3 unwatch before a final handoff or a question. Use the host's question tool only when the goal, an authorization boundary, or an unresolvable blocker needs the user. If no answer is available, leave the PR open and unmerged and explain the blocker.
