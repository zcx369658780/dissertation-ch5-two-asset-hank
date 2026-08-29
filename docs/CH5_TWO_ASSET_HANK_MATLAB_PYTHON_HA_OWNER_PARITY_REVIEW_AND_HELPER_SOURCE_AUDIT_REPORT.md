# CH5 Two-Asset HANK MATLAB–Python HA Owner Parity Review and Helper-Source Audit

## Classification

- O1 classification: `O1_MATLAB_LEGACY_LIMITATION_NOT_TO_INHERIT`
- Structural closure: `OWNER_STRUCTURAL_PARITY_CLOSED__NUMERICAL_PARITY_REQUIRED`

This closes the source/equation structural review only. It does **not** return a final numerical MATLAB–Python parity PASS/FAIL and does not authorize dynamic extension.

## Live GitHub and Python source identity

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- Fresh-fetched live/base `origin/main`: `dfda905c9f656107e201f22b037d2a186fb1c6df`
- Fresh isolated workspace: `D:\ProjectTemp\ch5-ha-owner-parity-helper-audit-20260829`
- Accepted Python implementation baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`
- Accepted R4 execution evidence: `8931eacf4e9f503b9ab12b75399f098177196dfb`
- `git diff 7a2388a2ba89073e307f05a909570e8c40a4be13..dfda905c9f656107e201f22b037d2a186fb1c6df -- src tests`: empty

Source continuity result: `PASS`. No accepted Python scientific or test source drift exists.

## Files read

- `tasks/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT.md`
- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_ACCEPTANCE_AND_MATLAB_PYTHON_HA_PARITY_PREP_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_RERUN_AFTER_CORRECTED_TRUNCATION_CONTRACT_REPORT.md`
- `src/ch5_two_asset_hank/economics.py`
- `src/ch5_two_asset_hank/boundaries.py`
- `src/ch5_two_asset_hank/policies.py`
- `src/ch5_two_asset_hank/contracts.py`
- `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m`
- `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK3_cost.m`
- `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK3_FOC.m`

## File written

- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`

## MATLAB source identities

All three are regular files with `Archive` attribute, no `LinkType`, no target, and no reparse/link indirection.

| Role | Exact path | SHA-256 | Bytes | Lines | Function signature |
|---|---|---|---:|---:|---|
| main | `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | 12227 | 427 | `function results = HANK_2ASSETS_HJB(param, grid, num, CHIh, results, show_result)` |
| cost helper | `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` | 691 | 25 | `function eq = HANK3_cost(results,paramchi,d,a,foreign)` |
| FOC helper | `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` | 565 | 22 | `function d = HANK3_FOC(results,paramchi,pa,pb,a,foreign)` |

The two exact helper names each had exactly one match inside the designated MATLAB source tree. No similarly named helper from another project/date tree was used.

## O1 helper formulas and line-referenced comparison

### MATLAB adjustment cost

`HANK3_cost.m:2–8` loads `chi0`, `chi1`, fixed-cost fields, and `a_bar`. For the domestic branch actually requested by `HANK_2ASSETS_HJB.m:137–140,148–149,263,352–353` with `foreign=0`, `HANK3_cost.m:21–22` defines:

`chi(d,a) = chi0*abs(d) + (chi1/2)*d^2*(max(a,a_bar))^(-1)`.

This is an exact structural match to the accepted contract

`m(a)=max(a,a_bar)`,

`chi(d,a)=chi_0*abs(d)+(chi_1/2)*d^2/m(a)`,

and to `economics.py:10–13`.

The foreign branch is outside the current domestic two-asset HA comparison. For completeness, `HANK3_cost.m:15–19` applies a price conversion, adds `fixcost`, folds `fixcost2` into `chi0`, and still uses `max(a,a_bar)`.

### MATLAB transfer FOC

`HANK3_FOC.m:2–10` loads the same adjustment parameters and `a_bar`. However, the domestic formula at `HANK3_FOC.m:18–19` is:

`d = [min(pa/pb - 1 + chi0,0) + max(pa/pb - 1 - chi0,0)] * a / chi1`.

Thus its scale is bare `a`, not `max(a,a_bar)`. The foreign branch at `HANK3_FOC.m:12–17` also multiplies by bare `a` after price/fixed-cost adjustments.

The accepted Python FOC at `economics.py:16–21` instead defines:

`q = v_a/v_b - 1`,

`d = max(a,a_bar) * [min(q+chi_0,0)+max(q-chi_0,0)] / chi_1`.

For `a >= a_bar`, the domestic MATLAB and Python formulas agree after the symbol adapter `pa=v_a`, `pb=v_b`. For `a < a_bar`, they materially differ: MATLAB shrinks the control scale with `a` and gives zero transfer at `a=0`, while the accepted cost derivative requires the frozen scale `m(a)=a_bar`.

### Accepted shadow-price/KKT relation

The Python relation is internally consistent with the accepted cost:

- positive `d`: `shadow_a = shadow_b*(1+chi_0+chi_1*d/m(a))`;
- negative `d`: `shadow_a = shadow_b*(1-chi_0+chi_1*d/m(a))`;
- zero `d`: `shadow_a-shadow_b` lies in the `±shadow_b*chi_0` subgradient interval.

References: `boundaries.py:85–96,146–153`. The same `m(a)=max(a,a_bar)` is used by multiplier recovery and residual audit. `economics.py:59–65` then uses the selected control in `mu_b=r_b b+labor_income-d-chi-c` and `mu_a=r_a a+d`.

The main MATLAB drifts have the same signs at `HANK_2ASSETS_HJB.m:263–264`, but its low-`a` FOC helper is not the derivative of its own `HANK3_cost.m:22` cost formula.

### Exact O1 decision

`O1_MATLAB_LEGACY_LIMITATION_NOT_TO_INHERIT`

Reason: MATLAB cost and accepted Python cost match, but the MATLAB transfer FOC omits `max(a,a_bar)` below `a_bar`. The task explicitly establishes the accepted dissertation/Python contract and directs that this low-`a` MATLAB difference be treated as a legacy limitation, not as grounds to reject Python. No source is modified to manufacture a match.

For future parity, O1 is split deliberately:

- at `a >= a_bar`, cost and FOC are materially comparable under an adapter;
- at `a < a_bar`, the MATLAB FOC is a controlled legacy counterexample and Python must be validated against the accepted equation, not forced to reproduce MATLAB.

## Contradiction audit against accepted parity-prep report

The helper evidence resolves the previously open O1 question. It does not directly contradict O2–O12:

- O7 budget/drift signs remain aligned; the issue is the low-`a` magnitude selected by the MATLAB FOC, not the drift sign convention.
- O3 boundary/KKT acceptance is reinforced because Python uses one common scale in cost, FOC, multiplier recovery, and KKT residuals.
- No helper formula concerns productivity, interior zero-drift construction, upper corners, F/Z canonicalization, generators, stationary normalization, mass/density, or the line-90 initialization expression.

Therefore O2–O12 remain frozen as Owner `ACCEPT` exactly as directed.

## Final O1–O12 Owner structural decision table

| Checkpoint | MATLAB reference | Python reference | Equation-authority status | Reviewer classification | Owner decision | Later numerical comparison | Intentional non-comparability reason |
|---|---|---|---|---|---|---|---|
| O1 low-`a` cost/FOC | `HANK3_cost.m:21–22`; `HANK3_FOC.m:18–19`; main 137–149,263 | `economics.py:10–21`; `boundaries.py:85–96,146–153` | accepted contract explicitly freezes `m(a)=max(a,a_bar)` | `O1_MATLAB_LEGACY_LIMITATION_NOT_TO_INHERIT` | `ACCEPT` | yes: exact/near for `a>=a_bar`; controlled redesign test below | MATLAB bare-`a` FOC is not the oracle for `a<a_bar` |
| O2 productivity law/support/boundary | main 16–20,64–66 | `productivity.py:27–53` | accepted reflected-diffusion redesign | `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION` | `ACCEPT` | only after common special case | two-state switch and reflected diffusion are different objects |
| O3 lower-a/lower-b constraints/KKT | main 117–154 | `boundaries.py:21–42,63–156`; `policies.py:514–553` | accepted R4 KKT/state-constraint contract | `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION` | `ACCEPT` | yes, where MATLAB exposes quantities | MATLAB lacks full multiplier/residual audit |
| O4 interior `mu_a=0` crossing | main 141–154 | `policies.py:195–258,675–727` | accepted R4 redesign | `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION` | `ACCEPT` | controlled special cases | explicit Python candidate is absent in legacy MATLAB |
| O5 upper/corner closures | main 143–153,194–195 | `policies.py:261–443,554–674` | accepted R4 boundary redesign | `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION` | `ACCEPT` | controlled special cases | legacy MATLAB has incomplete/hard-coded closures |
| O6 lower-b F/Z near tie | main 131–154 | `policies.py:28–104,728–754`; `steady_state.py:76–154` | accepted narrow canonicalization contract | `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION` | `ACCEPT` | compare physical controls/drift class | MATLAB has no raw/canonical candidate audit |
| O7 budget/drift signs | main 263–264,352–353 | `economics.py:49–65` | accepted equation route | `EXACT_OR_NEAR_NUMERICAL_MATCH_REQUIRED` | `ACCEPT` | yes | none once primitives are shared |
| O8 multi-province labor | main 103–112,127–136 | `contracts.py:79–104`; `economics.py:30–46` | accepted vector generalization | `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION` | `ACCEPT` | scalar embedded case plus vector Python tests | legacy MATLAB call is one-province scalar |
| O9 generator/KFE transpose | main 155–239,333–340 | `generator.py:13–57`; `kfe_contract.py:35–41`; `kfe.py:44–46` | accepted operator contract | `ECONOMIC_EQUIVALENCE_UNDER_ADAPTER_REQUIRED` | `ACCEPT` | yes | orientation/index adapter required |
| O10 stationary uniqueness/normalization | main 337–345 | `kfe.py:49–132` | accepted uniqueness redesign | `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION` | `ACCEPT` | compare mathematical stationary object | arbitrary MATLAB pin-row detail is not authoritative |
| O11 mass/density/aggregates | main 341–351,387–389 | `kfe.py:115–141`; `steady_state.py:241–248` | accepted mass/density contract | `ECONOMIC_EQUIVALENCE_UNDER_ADAPTER_REQUIRED` | `ACCEPT` | yes after common measure | current finite-state/continuous-measure objects differ |
| O12 line-90 initialization | main 81,90,111–113 | `economics.py:59–65`; accepted initialization contract | legacy initialization not inherited | `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION` | `ACCEPT` | no literal equality required | `Rah.*raah` is frozen as legacy initialization behavior |

No row is changed to `NEEDS_DISCUSSION` because no direct contradiction was found.

## Meaning and exact final HA parity acceptance

The future Owner may declare

`MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`

only if all of the following are recorded in one auditable gate:

1. every materially comparable P1–P4 object passes its pre-authorized exact/near criterion;
2. every orientation, indexing, parameter, and measure adapter is explicit and independently checked;
3. every authorized redesign is validated against its accepted dissertation/equation contract with controlled special cases, rather than against MATLAB as oracle;
4. all intended non-comparabilities are confined to the O1–O12 accepted redesign set and have evidence showing the legacy limitation or differing object;
5. no unresolved material mismatch, missing source identity, unexplained sign difference, generator violation, KFE residual failure, or aggregate inconsistency remains;
6. the Owner explicitly accepts the complete P1–P4 evidence.

Qualitative similarity alone cannot pass an object where an exact quantitative shared-input comparison is available. R4 Python steady-state acceptance alone is insufficient.

## P1–P5 future shared-input numerical parity protocol — not executed

### Common controls for P1–P4

- Use a new isolated workspace rooted at the then-live accepted Python commit.
- Re-verify all MATLAB identities above and all Python scientific blobs.
- Freeze a manifest before execution: shared parameter names/values, units, grids, state list, `[b,a,z] ↔ [a,b,z]` adapter, labor scalar/vector adapter, mass/density adapter, outputs, comparison category, tolerance authority, and call budgets.
- Do not invent tolerances during execution. A predecessor task must authorize them per object.
- Execute each block once in order; stop fail-closed at the first material mismatch; do not tune or repair in the same task.
- Preserve raw outputs and transformed adapter outputs separately.

### P1. Static economic primitives / pointwise formulas

Frozen states must span `a=0`, `0<a<a_bar`, `a=a_bar`, interior `a>a_bar`, lower/upper `b`, interior `b`, and multiple `z`; frozen derivative/shadow pairs must cover positive, negative, and zero transfer regimes.

Export and compare:

- `m(a)`, adjustment cost, cost derivative/subgradient;
- consumption FOC and labor FOC;
- transfer FOC/control;
- `mu_a`, `mu_b` and each budget component;
- boundary feasibility and all available KKT multipliers/residual components.

Categories:

- cost formula and all primitives with identical representation: `EXACT_OR_NEAR_NUMERICAL_MATCH_REQUIRED`;
- MATLAB/Python symbol/vector adapters: `ECONOMIC_EQUIVALENCE_UNDER_ADAPTER_REQUIRED`;
- low-`a` MATLAB FOC: `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION`; demonstrate the legacy bare-`a` result and separately verify Python against the accepted `m(a)` equation;
- any object lacking a common definition: `NOT_COMPARABLE_UNTIL_COMMON_OBJECT_DEFINED` and blocks advancement until defined.

P1 passes only if all comparable primitives pass and the low-`a` redesign evidence matches the accepted analytic equation exactly/within authorized floating evaluation rules.

### P2. One-step policy selection / local HJB objects

Feed both implementations identical value slices or explicit forward/backward derivative arrays after orientation mapping. The case manifest must include interior F/B choices, liquid zero drift, interior illiquid zero drift, lower-a, lower-b, upper-a/lower-b, upper-a/interior-b, dual-upper, and qualified lower-b F/Z near ties.

Export:

- forward/backward derivatives and validity;
- every available candidate's derivative pair, controls, adjustment cost, drifts, utility, Hamiltonian and admissibility;
- selected raw/canonical identity or MATLAB directional indicators;
- boundary/KKT evidence;
- deterministic tie/selection audit.

Requirements:

- derivative/control/Hamiltonian objects with the same candidate: `EXACT_OR_NEAR_NUMERICAL_MATCH_REQUIRED` under authorized tolerance;
- layout and label mapping: `ECONOMIC_EQUIVALENCE_UNDER_ADAPTER_REQUIRED`;
- Python-only zero/corner/KKT/canonicalization cases: `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION`, proved with analytic constraints and controlled MATLAB omission/legacy behavior;
- no qualitative-only substitution where both codes expose the same quantitative candidate.

P2 cannot begin if P1 fails.

### P3. Generator parity

Freeze a deliberately shared finite grid and one common policy/drift array. First compare only asset components, then add a productivity component only after a common productivity special case is explicitly defined.

Export:

- index maps and selected interior/boundary flat indices;
- every nonzero entry of selected `G_a`/MATLAB illiquid-transition rows and `G_b`/MATLAB liquid-transition rows;
- row sums, diagonal, off-diagonals, neighbor destinations and rates;
- common productivity component if defined;
- total backward generator and component sum identity.

Requirements:

- asset rates after index adapter: `ECONOMIC_EQUIVALENCE_UNDER_ADAPTER_REQUIRED`, with exact/near numeric rates required;
- row sums and off-diagonal sign contract: `EXACT_OR_NEAR_NUMERICAL_MATCH_REQUIRED`;
- current two-state versus reflected-diffusion productivity: `NOT_COMPARABLE_UNTIL_COMMON_OBJECT_DEFINED`;
- a frozen common special case may move productivity to exact/near comparison, but cannot silently replace either accepted production object.

P3 cannot begin if P2 fails.

### P4. KFE and stationary distribution parity

Use only the P3-accepted common finite backward generator. Compare the mathematical stationary object, not MATLAB's arbitrary pinned row.

Export:

- proof/read-back that forward operator is the mapped transpose of backward `G`;
- stationary mass vector before and after orientation mapping;
- `||G^T g||`, normalization, minimum/negative mass diagnostics;
- common cell/measure weights, density if defined;
- `A_hh`, `B_hh` from the same states, mass and measure.

Requirements:

- transpose, residual, normalization, mass and aggregates: `EXACT_OR_NEAR_NUMERICAL_MATCH_REQUIRED` under pre-authorized tolerances;
- orientation/measure conversion: `ECONOMIC_EQUIVALENCE_UNDER_ADAPTER_REQUIRED`;
- arbitrary pinned-row implementation details: intentionally non-comparable, provided both solve the same unique stationary object;
- if no common generator/measure exists, classification remains `NOT_COMPARABLE_UNTIL_COMMON_OBJECT_DEFINED` and P4 cannot pass.

P4 cannot begin if P3 fails.

### P5. Full HA block Owner acceptance

Assemble one manifest linking every O1–O12 decision to P1–P4 evidence, including exact source hashes, inputs, adapters, authorized tolerances, raw outputs, comparison results, redesign proofs, and terminal status.

P5 may issue `MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION` only under the six acceptance conditions above. Otherwise it must return fail-closed or a named blocked state and must not authorize AR(1), transition, IRF, calibration, or Results work.

## Forbidden-operation check

- MATLAB executed or modified: no
- Python, pytest, HJB, KFE, fixture or shared-input experiment executed: no
- Python source/tests modified: no
- Parameters, tolerances, equations or policy contracts changed: no
- Helpers substituted from another source tree: no
- Numerical parity claimed: no
- AR(1), transition, IRF, calibration or Results work entered: no
- Merge, rebase, reset or force-push: no

## Required next gate

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_SHARED_INPUT_NUMERICAL_PARITY`

That future gate must execute P1–P4 in bounded order, stop fail-closed on the first material mismatch, and require explicit Owner P5 acceptance before any dynamic extension.
