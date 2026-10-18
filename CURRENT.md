# CH5 CURRENT · V1.7交付闭环规则；V3既有证据补交任务已签发

**PREVIOUS_ENGINEERING_TASK=TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_20261018**
**PREVIOUS_ENGINEERING_RESULT=PASS_BOUNDED_ADAPTER_INTEGRATION_LOCAL**
**PREVIOUS_RUN=33f2b49ddc274e868956f6480d5f3a3a**
**PREVIOUS_INDEPENDENT_ACCEPTANCE=PENDING**
**ACTIVE_TASK=TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_20261018**
**TASK_SCOPE=DELIVERY_ONLY / ZERO_SCIENCE / NO_TEST_RERUN / NO_RUNNER**
**TASK_STATUS=ISSUED_NOT_STARTED**
**TASK_ISSUE_COMMIT=98d9705e7219b23a344fb33052dbe41fe8fdf6f2**
**TASK_BLOB=c409bf77eae018a6ff7db6cb821bb9410fe85ffe**
**TASK_PATH=tasks/TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_20261018.md**
**WORKFLOW_V1_7=docs/CH5_ASTRA_WORKFLOW_V1_7_DELIVERY_CLOSURE_20261018.md**

## Current decision

The V3 engineering contract prohibited network publication, so its evidence was not pushed. This was contract-compliant but left the long-term delivery workflow incomplete. Do not rewrite or resume that contract. A new zero-science delivery-only task has now been issued with a separate fixed delivery budget.

## V1.7 hard rules

SCIENCE_BUDGET, ENGINEERING_BUDGET and DELIVERY_BUDGET are independent and must be frozen separately. Any task requiring Astra independent review must specify the review branch, fixed parent, exact remote temp path, file allowlist, size limits, fake-bare preflight, publish/readback/cleanup budgets, and STOP conditions at issuance. If the task prohibits network publication, it cannot also be expected to use GitHub temp exchange; issue a new delivery-only contract rather than changing old authority.

Only sanitized result.md, manifest.json and evidence_sanitized.zip may be published under the task's remote-only _review_tmp path. Review all ZIP members and nested archives; preserve raw/private evidence locally. Astra must read back actual ZIP bytes and recompute SHA256/length; if bytes cannot be independently read, mark BINARY_NOT_INDEPENDENTLY_READABLE. Permanently archive and read back the verdict before deleting only allowlisted files from the remote review branch current tree. Git deletion never erases history.

## Active task

`TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_20261018` only publishes and verifies existing evidence for run `33f2b49ddc274e868956f6480d5f3a3a`. No tests, Windows smoke, Python, runner, model or scientific calls may be rerun. One successful ordinary non-force publication maximum; no PAT, force push, protected worktree/index writes or extra fetches.

**ACTIVE_RESEARCH_TASK=NONE; ACTIVE_SCIENCE_TASK=NONE**
**model_activation=False; REAL_GE=False; Results=FALSE; V011=NOT_STARTED**
**FULL_RUNNER_IO_CLOSURE=BLOCKED**
**NEXT=CODEX_EXECUTE_TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_20261018**
**FINAL_STOP=WAIT_ASTRA_INDEPENDENT_REVIEW_AND_PERMANENT_ARCHIVE**
