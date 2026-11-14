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
