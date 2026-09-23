# Evidence Contract

This directory is the lightweight entry point for new local-workflow evidence. Existing sealed evidence under `reports/` remains authoritative and is not moved or rewritten.

## Persist what supports the decision

Prefer raw terminal output or an exact failure excerpt, machine-readable JSON/NPZ receipts, focused test results, numerical summaries tied to input and source identities, first-failure forensic evidence, changed-path and manifest/readback receipts, and figures only when they materially improve review.

## Keep evidence bounded

- One task gets one clearly named evidence root.
- Record inputs, source/commit identity, call ledger, outcome, and stop reason.
- Preserve raw evidence; derive summaries without overwriting it.
- Do not duplicate the same facts across many Markdown reports.
- A short report or `CURRENT.md` pointer should link to the evidence root and its manifest.
- Reviewer checks the evidence needed for the decision; Reviewer need not reproduce every Builder computation.

## Integrity

- Manifests list relative path, bytes, and SHA-256.
- Readback recomputes hashes from disk and reports mismatches.
- Scientific calls made during readback must be zero.
- Never store credentials, private/raw purchased data, or unrelated project artifacts here.
- Never use evidence from `deep-learning-hank`.

## Naming

Use `EVIDENCE/<task_slug>_<YYYYMMDD>/`. Large or existing task packages may remain under `reports/<task_slug>_runNNN/`; link them from `CURRENT.md` rather than copying them.
