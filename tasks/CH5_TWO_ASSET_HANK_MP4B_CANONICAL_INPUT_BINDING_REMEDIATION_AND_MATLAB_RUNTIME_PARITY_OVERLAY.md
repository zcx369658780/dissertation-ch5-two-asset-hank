# CH5_TWO_ASSET_HANK_MP4B_CANONICAL_INPUT_BINDING_REMEDIATION_AND_MATLAB_RUNTIME_PARITY_OVERLAY

Date: 2026-09-01

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / validation-input binding remediator

Owner: final scientific authority

## 1. Authority basis and L3 decision

Accepted predecessor execution:

`MP4B_L3_READ_ONLY_SOURCE_BINDING_CENSUS_AND_EARLY_HOUSEHOLD_OUTPUT_ATTRIBUTION_PASS`

Execution commit:

`a7ee476dbe16e8dfc71cebc9216ad92fd28c5ab0`

Accepted predecessor markers/classifications:

- `MP4B_INITIAL_ZT_BINDING_CENSUS_REPRESENTATION_DIVERGENCES_LOCALIZED`
- `MP4B_CANONICAL_INITIAL_ZT_SOURCE_RECOMPUTATION_AUTHORIZED`
- `MP4B_TURN1_BEIJING_HOUSEHOLD_INPUT_REPRESENTATION_DIFFERENCE_LOCALIZED`
- `MP4B_TURN1_BEIJING_HOUSEHOLD_OUTPUT_NONBITWISE_BUT_WITHIN_ACCEPTED_PARITY_ENVELOPE`

The 31-province census establishes:

- `24/31` MATLAB-cache `IND_Zt` values are bitwise identical to canonical `initialized_zt`;
- `7/31` differ only in binary64 representation: five by `1 ULP`, two by `2 ULP`;
- canonical `initialized_zt` reproduces the protected source-order formula for `31/31` provinces;
- the MAT cache is an accepted derived runtime representation, not primary scientific authority.

Earlier MP4A2 authority also froze:

- `MP4A2_2009_PRIMARY_SOURCE_CANONICAL_INPUT_ACCEPTED`;
- `MP4A2_2009_RUNTIME_REPRESENTATION_COMPATIBILITY_ACCEPTED`;
- `MP4A2_MAT_CACHE_COMPATIBILITY_REPRESENTATION_ACCEPTED_FOR_2009_RUNTIME_ONLY`;
- `OWNER_DERIVED_MAT_CALIBRATION_CACHE_NOT_PRIMARY_SCIENTIFIC_AUTHORITY`.

Therefore the L3 decision is:

> Do **not** mutate or downgrade the primary-source canonical JSON. Instead create an explicit validation-only dual-binding contract: primary-source canonical values remain the scientific input authority; a separately named MATLAB-runtime parity overlay may replace only `initialized_zt` with the exact derived cache binary64 values when the explicit objective is bitwise same-runtime-input MATLAB/Python parity.

This is a mechanical provenance/validation remediation under the Owner's standing L3 delegation. It introduces no new economic equation, parameter, grid, solver algorithm, controller rule, parity tolerance, shock design, or Results claim.

## 2. Required live continuity

Required execution-start predecessor:

`a7ee476dbe16e8dfc71cebc9216ad92fd28c5ab0`

At execution start:

1. fresh-fetch `origin/main`;
2. require this exact task live on `main` as the direct child of `a7ee476dbe16e8dfc71cebc9216ad92fd28c5ab0`;
3. require clean worktree, `HEAD == origin/main`, ahead/behind `0/0`;
4. read completely:
   - `AGENTS.md`;
   - `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
   - `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`;
   - `project_rules/PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md`;
   - predecessor source-binding census task/report;
   - MP4A2 canonical-input preparation report at commit `85772bc6920db58cd6ec38bf8e1d7a5d593e12fc`;
   - post-trace initial-Zt provenance report;
   - accepted Beijing same-input household parity report;
   - current validation driver/input-binding code and tests.

Any authority or immutable-identity failure => stop before mutation and report BLOCKED.

## 3. Hard zero-model-execution budget

All scientific/model execution counts are exactly zero:

- MATLAB processes / `checkcode`: `0`;
- MATLAB stationary/HJB/KFE/household/firm/controller: `0`;
- Python stationary/HJB/KFE/household/MP2/MP3: `0`;
- comparator replay / `compare_terminal`: `0`;
- standalone household replay: `0`;
- other year / annual batch: `0`;
- shocks/AR1/transition/dynamics/IRF: `0`;
- historical R5 / Results: `0`.

Allowed work is source inspection, hashing, standard-library-only input construction, validator/helper/test implementation, focused non-scientific tests, and external no-overwrite artifacts.

## 4. Immutable input authorities

Primary canonical corrected-2009 input:

`D:\ProjectTemp\ch5-mp4a2-2009-input-binding-20260830-001\calendar_2009_primary_premodel_input.json`

SHA-256:

`507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`

This file is immutable and MUST NOT be edited, overwritten, regenerated in place, or relabeled as cache-authoritative.

MATLAB derived runtime cache:

`数据估计结果_1000_100_0.mat`

Accepted SHA-256:

`923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A`

Its role remains derived/non-primary runtime representation only.

Require the predecessor census/audit artifacts and SHA-256 identities from the accepted report, especially the 31-province initial-Zt census and audit manifest.

## 5. Dual-binding scientific/validation contract

Freeze two explicit and non-interchangeable modes.

### Mode A — primary-source scientific canonical

Canonical label:

`PRIMARY_SOURCE_CANONICAL`

Rules:

- all values come from the accepted canonical JSON;
- `initialized_zt` is the protected source-order recomputation already accepted for 31/31 provinces;
- canonical SHA remains `507D1259...CDAD48`;
- this is the default scientific/provenance authority;
- no cache value may silently override it.

### Mode B — MATLAB historical runtime parity overlay

Canonical label:

`MATLAB_CACHE_RUNTIME_PARITY_OVERLAY`

Rules:

- start from the exact immutable canonical JSON object;
- preserve every field except `initialized_zt` bitwise/structurally identical to Mode A;
- replace only `initialized_zt` with exact binary64 values read from the accepted MATLAB runtime cache field actually consumed by `mpHANK_equilibrium_2000`;
- preserve province order exactly;
- bind and persist both canonical SHA and cache SHA;
- explicitly record per-province canonical/cache decimal, hex, ULP distance, and replacement boolean;
- expected census must be exactly `24` identical + `7` differing, with the accepted ULP pattern `5×1 ULP + 2×2 ULP`;
- fail closed if any other field differs, any province order differs, any ULP pattern changes, or either immutable SHA differs;
- never call this overlay the primary scientific input.

This overlay exists only to answer the forensic parity question:

> What happens when Python consumes the same historical runtime `initialized_zt` binary64 representation as the protected MATLAB stationary execution?

## 6. Implementation boundary

Preferred implementation is validation-only under `validators/multi_province/` plus focused tests under `tests/`.

A production scientific module under `src/ch5_two_asset_hank/` MUST NOT be modified unless the task becomes BLOCKED and L3/Owner separately authorizes a broader change.

The implementation MAY:

- add one explicit validation helper/data class for the two binding modes;
- add one explicit runtime-parity overlay constructor;
- add focused tests;
- if strictly necessary, make the minimum validation-entry wiring change so a future separately authorized Python parity runner can receive an explicitly constructed overlay object.

The implementation MUST NOT:

- mutate canonical JSON;
- mutate MAT cache;
- change household equations or solver code;
- change multi-province MP2/MP3 scientific code;
- change controller logic or thresholds;
- change accepted comparator tolerances;
- silently make cache overlay the default;
- allow stringly-typed or implicit fallback between the two modes.

## 7. Required fail-closed tests

Without invoking any model, test at minimum:

1. canonical SHA exact-match gate;
2. cache SHA exact-match gate;
3. province order exact-match gate;
4. canonical Mode A reproduces existing canonical object byte-for-byte/field-for-field;
5. Mode B changes only `initialized_zt`;
6. exact 31-province cache/canonical census `24 equal / 7 differ`;
7. exact ULP pattern `5×1 / 2×2`;
8. all seven changed values exactly equal accepted cache binary64 hex values;
9. all 24 unchanged values stay bitwise identical;
10. any changed non-`initialized_zt` field fails closed;
11. province permutation fails closed;
12. wrong cache/canonical SHA fails closed;
13. missing explicit mode fails closed;
14. default/scientific mode remains `PRIMARY_SOURCE_CANONICAL`;
15. no scientific/model module call occurs.

## 8. External no-overwrite package

Create one fresh root under:

`D:\ProjectTemp\ch5-mp4b-canonical-binding-remediation-20260901-001`

If it exists, use the next deterministic fresh suffix. Never overwrite/delete prior artifacts.

Persist at minimum:

- `binding_contract.json`;
- `matlab_cache_runtime_overlay.json`;
- `initial_zt_31province_hex_ulp_table.json`;
- `canonical_vs_overlay_field_identity.json`;
- `focused_test_results.json`;
- `remediation_manifest.json`.

The overlay artifact remains external; do not commit the 31-value derived runtime cache vector as project data.

## 9. Required terminal classifications

PASS terminal:

`MP4B_CANONICAL_INPUT_BINDING_REMEDIATION_AND_MATLAB_RUNTIME_PARITY_OVERLAY_PASS`

Required PASS markers:

- `MP4B_PRIMARY_SOURCE_CANONICAL_BINDING_PRESERVED`
- `MP4B_DUAL_INPUT_AUTHORITY_CONTRACT_FROZEN`
- `MP4B_MATLAB_CACHE_RUNTIME_PARITY_OVERLAY_PREPARED`
- `MP4B_CACHE_OVERLAY_VALIDATION_ONLY_NO_SCIENTIFIC_DEFAULT_CHANGE`

BLOCKED terminal:

`MP4B_CANONICAL_INPUT_BINDING_REMEDIATION_AND_MATLAB_RUNTIME_PARITY_OVERLAY_BLOCKED`

Use BLOCKED for unresolved provenance, identity, implementation-boundary, or fail-closed-test failure. Do not widen scope.

## 10. Scientific interpretation boundary

This task cannot establish:

- corrected-2009 MATLAB/Python stationary parity;
- causality from initial-Zt ULP differences to later reset/controller differences;
- that cache values are scientifically superior to canonical recomputation;
- that MATLAB or Python is wrong;
- any Results or policy conclusion.

It only creates an explicit testable separation between primary-source science input and historical-runtime parity input.

## 11. Repository change boundary

Required report:

`docs/CH5_TWO_ASSET_HANK_MP4B_CANONICAL_INPUT_BINDING_REMEDIATION_AND_MATLAB_RUNTIME_PARITY_OVERLAY_REPORT.md`

Allowed repository mutation:

- narrowly scoped validation helper/wiring under `validators/multi_province/` if required;
- focused tests under `tests/`;
- the required report;
- no production scientific code under `src/`;
- no canonical data or MAT/cache files;
- no project rules;
- no prior reports/tasks.

## 12. Closeout

Report:

- exact verdict and markers;
- live continuity;
- immutable identities;
- dual-binding contract;
- exact changed paths and why each is validation-only;
- complete 31-province overlay census and ULP pattern;
- focused fail-closed test results;
- zero-model ledger;
- forbidden-operation audit;
- external artifact sizes/SHA-256;
- `git diff --check` PASS on actual staged content;
- exactly one execution commit;
- non-force push;
- fresh GitHub read-back of all changed paths;
- `HEAD == origin/main`;
- ahead/behind `0/0`;
- clean worktree;
- exactly one recommended next gate.

If PASS, the recommended next gate should be a separately authorized **Python-only corrected-2009 one-shot under `MATLAB_CACHE_RUNTIME_PARITY_OVERLAY`**, compared read-only against the already admissible instrumented MATLAB chronology. That future run must not rerun MATLAB and must retain a finite one-shot budget.
