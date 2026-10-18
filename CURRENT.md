# CH5 CURRENT · Immutable identity V1.5; adapter integration reissued

**PREVIOUS_TASK=TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_20261018**
**PREVIOUS_TASK_RESULT=FAIL_CLOSED_TASK_RAW_IDENTITY / STOP**
**PREVIOUS_RUN= e2a4f335b534d43778a41c588386d9071**
**PREVIOUS_TASK_NOT_STARTED=TRUE**
**ACTIVE_TASK=TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V2_20261018**
**TASK_SCOPE=ENGINEERING_ONLY / NO_SCIENCE / NO_HA**
**TASK_STATUS=ISSUED_NOT_STARTED**
**TASK_ISSUE_COMMIT=22fbd1b1d42bb774f826d57bbca973965781f39e**
**TASK_BLOB=fedd822504bdc0547ab91c7250d9e256efbc18c3**
**TASK_PATH=experiments/TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V2_20261018/ENGINEERING_CONTRACT.md**
**WORKFLOW=docs/CH5_ASTRA_WORKFLOW_V1_5_IMMUTABLE_TASK_IDENTITY_20261018.md**

## Latest identity failure
Previous adapter task stopped at BOOTSTRAP 0 because Codex changed historical V3 references while assembling validation text. This is a local construction error, not evidence the fixed remote contract was wrong. No files or scratch were created, tests/runners/science/network were not run. Previous task is superseded, not resumed.

## Immutable startup rule
Read the contract from its fixed issue commit/path unchanged. Never template, regex-replace, normalize or reconstruct the contract for identity checking. Distinguish Git Blob SHA from file SHA256. If only decoded connector text is available, label CONNECTOR_TEXT_VERIFIED; don't claim raw Git object verification. Mismatch => read-only STOP; no path/branch/hash guessing.

## Current task boundary
Integrate the accepted bounded V3 single-child gate into the existing executor via a narrow adapter. Follow V1.5 identity rules and V1.4 resource/protection rules. Fresh scratch and BOOTSTRAP 0/1/2 required. Unsupported nested/arbitrary descendants remain blocked. Static/synthetic checks first; at most one real bounded Windows integration smoke after they pass. No science, no old TEMP resume, no Git fetch/push, no network publication or review cleanup.

**ACTIVE_RESEARCH_TASK=NONE; ACTIVE_SCIENCE_TASK=NONE**
**model_activation=False; REAL_GE=False; Results=FALSE; V011=NOT_STARTED**
**FULL_RUNNER_IO_CLOSURE=BLOCKED**
**NEXT=CODEX_EXECUTE_TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V2_20261018**
**FINAL_STOP=WAIT_ASTRA_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_REVIEW**
