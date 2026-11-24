# Working in this repository

Read the README and relevant documentation before changing code. This repository starts as an OpenMettle component template; do not assume that a service or installer already exists.

- Keep changes focused on the requested behavior and explain material trade-offs.
- Keep site-specific values, credentials and private data outside tracked files.
- Preserve upstream licenses, copyright notices and provenance.
- Clearly distinguish implemented behavior from plans and unverified assumptions.
- Prefer validation and dry-run behavior for infrastructure changes. Do not apply to a live cluster, erase storage or publish a release without task authorization.
- Run `python3 scripts/check_repository.py` and the component-specific checks relevant to the change. Report checks not run and why.
- Add meaningful tests for changed behavior; do not describe repository hygiene checks as application coverage.
- Update user-facing documentation when configuration, operation or recovery changes.
- Never invent benchmark results, supported hardware, working commands or compatibility guarantees.

## Ticket and sprint coordination

[Project 1](https://github.com/orgs/OpenMettle/projects/1) and the [delivery tracker](https://github.com/OpenMettle/openmettle-core/issues/1) are the live work index. This policy applies to every ticket, including delegated work.

- **Accountability:** the main (coordinating) agent owns task selection, scope control and tracker reconciliation. Delegating work does not transfer these duties.
- **Check before work:** before implementing or delegating, after resuming or recovering context, and before starting another ticket, fetch the live issue, its Project 1 fields and the relevant sprint record. Check the acceptance criteria, dependencies, recent relevant comments and existing PRs. Then briefly state the selected issue, its sprint or goal and the bounded scope.
- **Scope:** give each subagent an explicit assignment and the evidence it must return. Record unrelated discoveries and out-of-scope review findings as follow-up issues in Project 1, in an appropriate sprint or the backlog. Preserve agreed priorities, historical sprint assignments and capacity decisions. Follow explicit user-directed scope changes and record them on the sprint record.
- **Tracking updates:** when work starts, reaches review or is handed off, reconcile the owning issue, its Project 1 status and the relevant sprint record. Record PR links, the verification actually run, remaining gaps and next steps. Read each update back to confirm that it persisted.
- **Completion:** close an issue or set it to Done only when its full acceptance criteria and any applicable owner gates are met. Keep partial increments and unfinished parent issues open.
- **Access failures:** if a tracker read or write fails, report it and list the outstanding updates. Continue only clearly authorized work. Do not guess missing state or claim that synchronization succeeded.
