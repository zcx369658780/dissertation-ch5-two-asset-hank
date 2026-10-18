# CH5 CURRENT · V1.6 path-boundary rules; adapter integration V3 issued

**PREVIOUS_TASK=TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V2_20261018**
**PREVIOUS_TASK_RESULT=FAIL_CLOSED_PROTECTED_PATH_IDENTITY / STOP**
**PREVIOUS_RUN=1b1c3687d35c42b0a06ab581d4a39697**
**ACTIVE_TASK=TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_20261018**
**TASK_SCOPE=ENGINEERING_ONLY / NO_SCIENCE / NO_HA**
**TASK_STATUS=ISSUED_NOT_STARTED**
**TASK_ISSUE_COMMIT=37271647c5818731231b6d95854174ca1dcef3ce**
**TASK_BLOB=489b636cba99a66ea40b85041f9bf87c7aaccfee**
**TASK_PATH=experiments/TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_20261018/ENGINEERING_CONTRACT.md**
**WORKFLOW_V1_6=docs/CH5_ASTRA_WORKFLOW_V1_6_PROTECTED_PATH_BOUNDARIES_20261018.md**

## Latest failure
Adapter V2 stopped at BOOTSTRAP 0 with PATH_ALIAS in a recursively enumerated dependency file. The checker did not return the final resolved path, so alias target and relation to protected roots remain UNKNOWN. This does not prove model source corruption. No scratch, files, tests, runners, science or network operations occurred.

## V1.6 rule
Protect finite declared root identities and the actual intended target/parent chain. Do not recursively enumerate all descendants of evidence roots to infer protection identity. If a PATH_ALIAS is encountered in an unrelated dependency file and it is demonstrably not the target, ancestor, or relevant protected root, record PATH_ALIAS_UNRELATED_ENUMERATION rather than automatically failing the task. If relevant target/boundary cannot be established, STOP. Never disable alias checks or change path to evade.

## Current task
Integrate accepted V3 single-child gate through a narrow ResourceGate adapter. Immutable contract identity rules from V1.5 remain active. BOOTSTRAP 0/1/2 required. Unsupported nested/arbitrary descendant topology remains blocked. Static/synthetic tests first; at most one real bounded Windows integration smoke after they pass. No science, no old TEMP resume, no Git fetch/push, no network publication or review cleanup.

**ACTIVE_RESEARCH_TASK=NONE; ACTIVE_SCIENCE_TASK=NONE**
**model_activation=False; REAL_GE=False; Results=FALSE; V011=NOT_STARTED**
**FULL_RUNNER_IO_CLOSURE=BLOCKED**
**NEXT=CODEX_EXECUTE_TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_20261018**
**FINAL_STOP=WAIT_ASTRA_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_REVIEW**
