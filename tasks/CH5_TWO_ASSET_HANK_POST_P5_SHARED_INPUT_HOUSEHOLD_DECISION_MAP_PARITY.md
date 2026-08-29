# CH5_TWO_ASSET_HANK_POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_MAP_PARITY

Date: 2026-08-29

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

After P5 Owner acceptance, perform one supplementary MATLAB-Python validation focused specifically on **household decisions** under the now-closed accepted economic equations.

This task answers:

> when MATLAB and Python are given the same household state/shadow inputs and MATLAB is evaluated under the accepted corrected equations rather than known legacy limitations, do they produce the same household controls, drifts, directions and local policy decisions?

This is not a new P5 gate and does not revoke the accepted marker:

`MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`

However, the Owner has voluntarily held actual dynamic execution under:

`DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`

A material contradiction found here must stop downstream dynamics and return to Owner/reviewer diagnosis.

## 2. Live authority and accepted state

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main`;
3. record live start SHA;
4. read `docs/CH5_TWO_ASSET_HANK_P5_OWNER_FINAL_ACCEPTANCE_DECISION.md`;
5. verify accepted Python scientific/test continuity from baseline `7a2388a2ba89073e307f05a909570e8c40a4be13` with:

`git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`

It must be empty before scientific execution.

## 3. Required reads

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_P5_OWNER_FINAL_ACCEPTANCE_DECISION.md`
- `docs/CH5_TWO_ASSET_HANK_P5_ACCEPTANCE_DESIGN_REVISION_AND_EVIDENCE_SUFFICIENCY_REVIEW_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_SHARED_INPUT_NUMERICAL_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P2_PYTHON_HARNESS_API_ARITY_CORRECTION_AND_COMPLETION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_HJB_DEPENDENCY_CLOSURE_AND_PYTHON_FUNCTIONAL_COVERAGE_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_ILLIQUID_RETURN_TAPER_AUTHORITY_RESOLUTION_AND_NUMERICAL_SCOPE_REVIEW_REPORT.md`
- accepted Python `economics.py`, `boundaries.py`, `policies.py`, `contracts.py`
- designated MATLAB `HANK3_cost.m`, production `HANK3_FOC.m`, `lab_solve2.m`, and accepted O1 test-only FOC helper.

Do not rerun or reopen P3/P4 or R4.

## 4. Frozen scientific authority for this task

The common economic object is fixed as follows.

### 4.1 Illiquid drift

Use the accepted dissertation law:

`mu_a = r_a * a + d`

Do not use the legacy MATLAB `raah/Rah` taper in any decision comparison.

### 4.2 Adjustment technology

Use:

`m(a)=max(a,a_bar)`

`chi(d,a)=chi0*abs(d)+(chi1/2)*d^2/m(a)`

The MATLAB decision evaluator must therefore use the already accepted O1 test-only FOC behavior rather than the production bare-`a` low-asset FOC.

Accepted O1 SHA-256:

`B28E73F439CB3DD40B2A6C00BE5D3E56FD7C4254DF468B4E2C0DCCED06DB7315`

### 4.3 Labor curvature mapping

Use:

`Python phi = 1 / MATLAB frisch_l`

### 4.4 Common budget scope

For direct MATLAB-Python decision comparisons use only currently common-supported fields:

- `Tt=0`
- `rb_gap=0`
- `fixcost=0`
- `fixcost2=0`
- `foreign=0`
- zero migration cost unless the frozen Python vector test explicitly embeds the scalar zero-migration case.

Do not add a transfer-income or borrowing-spread adapter.

### 4.5 Numerical tolerances

Reuse the accepted P1/P2 tolerances without widening:

- floating comparison: `128*eps64*max(1,abs(x),abs(y))` and array analogue;
- drift/zero classification: `1e-12`;
- KKT: `1e-7`.

No new tolerance may be invented after observing results.

## 5. Protected identities

Re-verify before execution:

- `HANK_2ASSETS_HJB.m` SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_cost.m` SHA-256 `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- production `HANK3_FOC.m` SHA-256 `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`
- `lab_solve2.m` SHA-256 `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`
- accepted O1 test-only helper SHA-256 `B28E73F439CB3DD40B2A6C00BE5D3E56FD7C4254DF468B4E2C0DCCED06DB7315`

No MATLAB or Python production source may be modified.

## 6. Pre-execution freeze

Before the first scientific call, create a fresh no-overwrite external artifact root and freeze/hash/read back:

- complete manifest for D1/D2/D3;
- MATLAB harnesses;
- Python harnesses;
- comparison harnesses;
- source/helper identity manifest;
- exact run order and call budget.

All scientific cases must be frozen before the first scientific call. No case may be added, removed or edited after execution begins.

## 7. D1 — corrected P1 full decision-primitive map

Purpose: rerun the exact accepted 432-case P1 Cartesian decision primitive set, but replace the known legacy low-`a` MATLAB FOC with the accepted O1 corrected MATLAB helper.

Reuse the exact P1 case manifest from the accepted predecessor evidence if available and identity-valid:

- predecessor artifact root: `D:\ProjectTemp\ch5-ha-shared-input-numerical-parity-20260829`
- predecessor manifest SHA-256: `3D2A35A7118CFEE479C05C1339AB247D78F5A71BBA044779AAB678D59E72D449`

The case set is exactly:

`4 a × 3 b × 4 z × 3 v_b × 3 q = 432`

Do not change states, ordering, calibration or shadow inputs from accepted P1.

The only scientific comparison change from old P1 is that the MATLAB decision side uses the accepted O1 low-`a` transfer FOC and the accepted scalar-`r_a` drift.

For every case export and compare:

- consumption `c`;
- scalar labor `l`;
- labor income;
- transfer `d`;
- adjustment cost;
- `mu_a`;
- `mu_b`;
- utility;
- local Hamiltonian `u + v_a*mu_a + v_b*mu_b`;
- transfer sign/disposition;
- `mu_a` and `mu_b` direction classes under `1e-12`.

Expected contract:

- there are no longer authorized low-`a` decision mismatches in D1;
- all 432 cases are materially common under the accepted corrected equation;
- every compared scalar must satisfy the frozen floating bound and every direction/sign class must agree exactly.

If any D1 material mismatch occurs, stop before D2/D3 and classify a material decision contradiction.

Execution budget D1:

- MATLAB scientific harness: 1
- Python scientific harness: 1
- comparison: 1
- no rerun.

## 8. D2 — corrected 10-case local household policy map

Purpose: revisit the accepted ten P2 local policy cases, now using an **independent MATLAB accepted-equation reference evaluator** for all ten cases rather than treating cases 4-10 as unavailable in legacy MATLAB.

Reuse the exact ten frozen P2 case definitions and ordering from accepted P2 evidence. Do not invent new cases in D2.

### MATLAB D2 evaluator rules

The D2 MATLAB harness is test-only external evidence, not production source and not a new production adapter.

It must:

- be written independently in MATLAB from the frozen dissertation/O1/KKT equations and P2 case definitions;
- use accepted O1 `max(a,a_bar)` transfer scaling;
- use constant `r_a` in `mu_a`;
- use `HANK3_cost.m` domestic branch for cost where applicable;
- use the accepted labor/consumption FOCs;
- implement the accepted lower/upper state constraints and multiplier/KKT equations needed by the ten cases;
- solve required zero-drift roots numerically from the frozen equations rather than hard-coding the expected Python outputs;
- not import, execute, translate, scrape or embed Python result values as MATLAB answers.

Static source review must confirm that expected result numbers are not hard-coded.

### D2 compared outputs

For all ten cases compare where defined by the accepted common equation:

- `c`
- `l`
- `d`
- adjustment cost
- `mu_a`
- `mu_b`
- utility
- Hamiltonian
- `a` direction
- `b` direction
- `lambda_a`
- `lambda_b`
- maximum KKT residual
- boundary-feasibility result.

All ten cases must now be treated as common accepted-equation decision cases. No case may be passed merely because production MATLAB lacks an explicit KKT audit.

Frozen thresholds remain drift `1e-12`, KKT `1e-7`, floating bound above.

If any D2 material mismatch occurs, stop before D3.

Execution budget D2:

- MATLAB accepted-equation evaluator: 1
- Python production evaluator: 1
- comparison: 1
- no rerun.

## 9. D3 — gamma-2 / native-like common decision map

Purpose: confirm that parity is not an artifact of the gamma-1 / phi-1 synthetic P1/P2 calibration and explicitly exercise the dissertation/native labor-curvature regime.

Freeze exactly this common-supported calibration:

- `rho=0.05`
- `gamma_c/ga=2`
- Python `phi=5`
- MATLAB `frisch_l=0.2`
- labor weight / `alphal=1`
- `chi0=0.1`
- `chi1=2`
- `a_bar=1e-6`
- `r_a/rah=0.04`
- `r_b/rb=0.02`
- `w=13.084227346448168`
- `tau=0.05`
- migration cost `0`
- `Tt=0`
- `rb_gap=0`
- `fixcost=fixcost2=0`
- `foreign=0`.

Freeze the exact Cartesian mesh:

- `a = [0, 5e-7, 1e-6, 1.0, 10.0]`
- `b = [-2.0, 0.0, 2.5, 5.0]`
- `z = [0.8, 1.3]`
- `v_b = [0.5, 1.0, 2.0]`
- `q = [-0.2, 0.0, 0.2]`, where `v_a = v_b*(1+q)`.

Total D3 cases:

`5 × 4 × 2 × 3 × 3 = 360`.

Use the same outputs and comparison rules as D1.

The MATLAB side must use O1 and constant `r_a`; the Python side must use accepted production economics.

Execution budget D3:

- MATLAB scientific harness: 1
- Python scientific harness: 1
- comparison: 1
- no rerun.

## 10. Total execution budget and order

Order is strict:

1. D1 MATLAB
2. D1 Python
3. D1 compare
4. D2 MATLAB
5. D2 Python
6. D2 compare
7. D3 MATLAB
8. D3 Python
9. D3 compare

Stop fail-closed at the first material scientific mismatch or post-start harness failure.

Maximum model/decision harness calls:

- MATLAB: 3
- Python: 3
- comparison: 3

No HJB iteration, generator construction, KFE/stationary solve, R4 steady state, AR(1), transition or IRF is authorized.

## 11. Required terminal classifications

Use exactly one.

### Full supplementary PASS

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_PASS__DYNAMIC_HOLD_MAY_ADVANCE_TO_ASSET_TAIL_GATE`

Use only if D1, D2 and D3 all pass completely.

Meaning:

- the corrected/common MATLAB accepted-equation evaluator and Python production give the same household decisions within frozen tolerances across the three decision maps;
- P5 remains accepted;
- the Owner-requested household-decision hold is satisfied;
- actual dynamics should still wait for the separately recommended upper-`a` asset-tail assurance gate.

### Material mismatch

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_FAIL_MATERIAL_MISMATCH__DYNAMIC_HOLD_CONTINUES`

Use if any common accepted-equation decision differs beyond the frozen criteria.

Report the smallest failing case and field. Do not tune, patch or rerun.

P5 is not automatically erased by this classification, but dynamics must remain on hold pending Owner/reviewer contradiction review.

### Source/environment/harness blocker

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

Use if execution cannot reach a valid comparison for non-scientific reasons. No rerun unless a later task authorizes it.

## 12. Required diagnostics

For each D-stage report:

- exact case count entered and completed;
- execution counts;
- manifest/harness/output SHA-256 identities;
- maximum absolute difference by compared scalar field;
- worst-case case ID/state/input for each field;
- count of direction/sign mismatches;
- D2 maximum KKT residual in both implementations;
- D2 boundary-feasibility mismatch count;
- complete failure list, which must be empty for PASS.

For D1 specifically report low-`a` subset statistics separately to prove the old O1 gap is actually closed under the accepted corrected evaluator.

For D3 separately report gamma-2/phi-5 labor and transfer maxima.

## 13. Repository output

Write only:

`docs/CH5_TWO_ASSET_HANK_POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_MAP_PARITY_REPORT.md`

All harnesses, manifests and raw outputs remain in a fresh external no-overwrite artifact root.

The report may be committed/pushed to `main` only if repository scope is otherwise clean. Explicitly stage only the report; do not use `git add .` or `git add -A`.

## 14. Explicit prohibitions

Do not:

- modify Python production source/tests;
- modify MATLAB production source/helpers/cache;
- add the MATLAB taper to Python;
- use production bare-`a` FOC as the corrected D1/D2/D3 oracle;
- add `Tt` or `rb_gap` to Python;
- add a new production adapter;
- change P1/P2 case values;
- tune cases after observing results;
- widen tolerances;
- rerun a failed scientific stage;
- run full MATLAB `HANK_2ASSETS_HJB`;
- run Python HJB/KFE/steady state;
- rerun P3/P4/R4;
- enter asset-tail, AR(1), transition, IRF, calibration extension, dynamics or Results in this task;
- revoke or reissue P5 acceptance automatically.

## 15. Recommended next gate

If PASS, recommend only:

`CH5_TWO_ASSET_HANK_POST_P5_UPPER_A_ASSET_TAIL_ROBUSTNESS_ASSURANCE`

before actual dynamics/calibration execution.

If FAIL, recommend the smallest contradiction-review gate centered on the first failing household-decision field/case.

If BLOCKED, recommend only the smallest harness/source correction gate required to complete this exact frozen experiment.
