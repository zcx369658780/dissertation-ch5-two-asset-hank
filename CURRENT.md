# CH5 CURRENT · V1.9 synthetic path classifier task issued

**PREVIOUS_TASK=TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_V2_20261018**
**PREVIOUS_RUN=447f9775e1b5482f9e3add9344742017**
**PREVIOUS_RESULT=FAIL_CLOSED / STOP**
**PREVIOUS_STOP=PATH_CLASSIFIER_FALSE_POSITIVE_AND_UNRESOLVED_JSON_ESCAPE**
**ACTIVE_TASK=CH5_REVIEW_PATH_CLASSIFIER_V19_SYNTHETIC_ONLY_20261018**
**TASK_SCOPE=ENGINEERING_ONLY / SYNTHETIC_ONLY / NO_ARCHIVE_SCAN / NO_NETWORK / NO_RUNNER / NO_SCIENCE**
**TASK_STATUS=ISSUED_NOT_STARTED**
**TASK_ISSUE_COMMIT=fa923c6048d958eba772b8145f79cf1fa857ee42**
**TASK_BLOB=VERIFY_BY_READBACK**
**TASK_PATH=tasks/CH5_REVIEW_PATH_CLASSIFIER_V19_SYNTHETIC_ONLY_20261018.md**
**WORKFLOW_V1_9=docs/CH5_ASTRA_WORKFLOW_V1_9_REVIEW_PATH_CLASSIFIER_20261018.md**

## Previous failure
Delivery V2 stopped after scanning 17/491 members because `https://` was misclassified as a drive path and a JSON-escaped fragment remained unresolved. Complete ZIP safety is UNKNOWN; 474 members remain unreviewed. No fake-bare or network publication occurred. This is not proof of source modification or credential leakage. Predecessor remains closed and not resumable.

## Active task
Only build/fix the URI/path/JSON-escape classifier using synthetic fixtures. Do not read or scan the old ZIP, do not generate a ZIP, do not run fake-bare, SSH/fetch/push, adapter, runner, tests against real evidence, or scientific models. Local-only outputs only. This task does not authorize resuming Delivery V2.

**ACTIVE_RESEARCH_TASK=NONE; ACTIVE_SCIENCE_TASK=NONE**
**model_activation=False; REAL_GE=False; Results=FALSE; V011=NOT_STARTED**
**FULL_RUNNER_IO_CLOSURE=BLOCKED**
**NEXT=CODEX_EXECUTE_CH5_REVIEW_PATH_CLASSIFIER_V19_SYNTHETIC_ONLY_20261018**
**FINAL_STOP=WAIT_ASTRA_PATH_CLASSIFIER_V19_REVIEW**
