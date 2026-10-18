# CH5 CURRENT · V1.8 source identity provenance; delivery recovery V2 issued

**PREVIOUS_DELIVERY_TASK=TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_20261018**
**PREVIOUS_RUN=6568ae4f4d134f3b9459e47d983f2acc**
**PREVIOUS_RESULT=FAIL_CLOSED / STOP**
**PREVIOUS_STOP=SOURCE_FINAL_RECEIPT_IDENTITY**
**ACTIVE_TASK=TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_V2_20261018**
**TASK_SCOPE=DELIVERY_ONLY / ZERO_SCIENCE / NO_TEST_RERUN / NO_RUNNER**
**TASK_STATUS=ISSUED_NOT_STARTED**
**TASK_ISSUE_COMMIT=454453dcdc56d62da11d2fbb0a603aa1e015c9e4**
**TASK_BLOB=ff17fbd3f672ba35e58c60d882da634be294ae7b**
**TASK_PATH=tasks/TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_V2_20261018.md**
**WORKFLOW_V1_8=docs/CH5_ASTRA_WORKFLOW_V1_8_SOURCE_IDENTITY_PROVENANCE_20261018.md**

## Latest delivery failure
The predecessor stopped before ZIP audit/fake-bare/network because a 65-character receipt SHA was manually copied into a local validator. That expected value was not in the predecessor contract. This does not prove source evidence changed. Do not resume the predecessor or alter its receipt.

## V1.8 rule
Expected source identities must be frozen in the current task contract or an explicitly authoritative source index. Do not add manual hashes from chat as gates. Validate hash format/length, report expected value and its source separately from actual bytes, and distinguish VALIDATOR_EXPECTATION_DEFECT from SOURCE_IDENTITY_MISMATCH. The corrected receipt identity for the new task is explicitly frozen in its contract.

## Active task
The new V2 delivery-only task handles existing run 33f2b49ddc274e868956f6480d5f3a3a only. It may audit/sanitize/publish/read back the three allowlisted files under its unique remote review branch/path. No tests, Windows smoke, Python, runner or model/science calls. Prior delivery budget is closed; use only this new task's budget.

**ACTIVE_RESEARCH_TASK=NONE; ACTIVE_SCIENCE_TASK=NONE**
**model_activation=False; REAL_GE=False; Results=FALSE; V011=NOT_STARTED**
**FULL_RUNNER_IO_CLOSURE=BLOCKED**
**NEXT=CODEX_EXECUTE_TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_V2_20261018**
**FINAL_STOP=WAIT_ASTRA_INDEPENDENT_REVIEW_AND_PERMANENT_ARCHIVE**
