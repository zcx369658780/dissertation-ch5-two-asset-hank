# CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_SHARED_INPUT_NUMERICAL_PARITY

## Task

Execute the bounded shared-input MATLAB–Python numerical parity protocol for the two-asset heterogeneous-agent household block.

This is the hard numerical gate before any AR(1), transition, IRF, calibration-extension, or Results work.

Execute P1 -> P2 -> P3 -> P4 in order. Stop fail-closed at the first material mismatch. Do not repair, tune, broaden tolerances, or continue to later stages after a terminal parity failure.

This task does **not** itself grant final Owner parity acceptance. A complete PASS means only that P1–P4 numerical evidence is ready for independent review and explicit Owner P5 acceptance.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Scientific authority

Accepted structural-closure evidence:

- Owner/helper audit commit: `13348e595bc2aefb7610b49cac3dfa9e97fb02fb`
- Structural classification: `OWNER_STRUCTURAL_PARITY_CLOSED__NUMERICAL_PARITY_REQUIRED`
- Accepted Python implementation baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`
- Accepted Python R4 steady-state evidence: `8931eacf4e9f503b9ab12b75399f098177196dfb`

Accepted MATLAB identities:

- `HANK_2ASSETS_HJB.m`
  - SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_cost.m`
  - SHA-256 `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `HANK3_FOC.m`
  - SHA-256 `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`

Accepted O1 decision:

`O1_MATLAB_LEGACY_LIMITATION_NOT_TO_INHERIT`

The MATLAB cost uses `max(a,a_bar)`, while the MATLAB low-`a` transfer FOC uses bare `a`. Therefore direct MATLAB/Python FOC equality is required only for `a>=a_bar`; for `a<a_bar`, MATLAB must reproduce its frozen legacy formula and Python must reproduce the accepted dissertation/Python `max(a,a_bar)` formula. The known low-`a` difference is an authorized legacy counterexample, not a parity failure.

O2–O12 are Owner `ACCEPT` as frozen in the structural-closure report.

## Hard route

The required route remains:

`accepted Python R4 -> structural parity closed -> P1–P4 numerical parity -> independent review -> Owner P5 acceptance -> only then dynamic extension`

Do not create, issue, or execute any AR(1), transition, or IRF task from this gate.

## Required live GitHub read-back

Fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_ACCEPTANCE_AND_MATLAB_PYTHON_HA_PARITY_PREP_REPORT.md`
- accepted Python source needed for P1–P4, including at minimum:
  - `src/ch5_two_asset_hank/contracts.py`
  - `src/ch5_two_asset_hank/economics.py`
  - `src/ch5_two_asset_hank/derivatives.py`
  - `src/ch5_two_asset_hank/boundaries.py`
  - `src/ch5_two_asset_hank/policies.py`
  - `src/ch5_two_asset_hank/generator.py`
  - `src/ch5_two_asset_hank/indexing.py`
  - `src/ch5_two_asset_hank/kfe_contract.py`
  - `src/ch5_two_asset_hank/kfe.py`
  - relevant accepted R4 policy/truncation tests used only as case authority, not as an execution substitute.

## Source-identity gates

Before any numerical execution:

1. verify that live Python scientific/test source is unchanged from `7a2388a2ba89073e307f05a909570e8c40a4be13` except later task/report-only commits;
2. verify exact MATLAB source identities at:
   `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`;
3. require all three MATLAB SHA-256 values above to match exactly;
4. record MATLAB executable path and version;
5. record Python executable path and version.

If MATLAB is unavailable, stop with:

`BLOCKED_HA_NUMERICAL_PARITY_MATLAB_EXECUTABLE_UNAVAILABLE`

Do not substitute GNU Octave or another MATLAB tree.

If source identity differs, stop with:

`BLOCKED_HA_NUMERICAL_PARITY_SOURCE_IDENTITY_DRIFT`

A source/environment block does not authorize source repair in this task.

## Workspace and artifact isolation

Use a fresh isolated Git workspace rooted at live `origin/main`.

Create parity harnesses and raw numerical artifacts only under a separate temporary root, for example:

`D:\ProjectTemp\ch5-ha-shared-input-numerical-parity-20260829`

Do not write harnesses into the repository or the designated MATLAB source tree.

Do not modify any accepted MATLAB or Python source/test file.

Before scientific execution, freeze and hash:

- the shared-input manifest;
- MATLAB harness source(s);
- Python harness source(s);
- comparison/orchestration source(s).

Record SHA-256 and bytes for every harness/manifest. After the first scientific stage begins, none of these files may change. If a harness defect is discovered after stage execution begins, stop and request a new task; do not edit and rerun in the same gate.

## Frozen common parameter authority

Use the accepted R4 primitive values where the object is shared:

- `rho = 0.05`
- `gamma_c = 1.0`
- `phi = 1.0`
- `chi_0 = 0.05`
- `chi_1 = 1.0`
- `a_bar = 0.5`
- `r_a = 0.04`
- `r_b = 0.03`
- `tau = 0.0`
- scalar embedded wage `w = 1.0`
- scalar embedded migration cost `sigma = 0.0`
- scalar embedded labor weight `1.0`

The scalar labor case is the common embedded MATLAB object for parity; it does not replace the accepted Python vector labor contract.

## Pre-authorized numerical tolerances

No tolerance may be changed after execution starts.

### Cross-language floating-expression tolerance

For quantities that represent the same pointwise formula or the same finite arithmetic construction, define:

`eps64 = IEEE float64 machine epsilon`

`tau_fp(x,y) = 128 * eps64 * max(1, abs(x), abs(y))`

For vectors/matrices use:

`tau_fp_array(A,B) = 128 * eps64 * max(1, max(abs(A)), max(abs(B)))`

and require maximum absolute mapped difference `<= tau_fp_array`.

The factor 128 is a pre-execution cross-language roundoff envelope for MATLAB/Python evaluation-order differences. It is machine-scale, not an economic tolerance. If it fails, do not widen it.

### Existing economic/numerical contracts retained

- zero/drift classification threshold: `1e-12`
- KKT validity threshold: `1e-7`
- generator validity threshold: `1e-11`
- stationary KFE residual/normalization threshold: `1e-10`

For shared generator matrix parity require:

`max_abs(G_M_mapped - G_P) <= 1e-11 * max(1, max_abs(G_M_mapped), max_abs(G_P))`

For shared stationary-mass parity require:

`max_abs(g_M_mapped - g_P) <= 1e-10`

For shared `A_hh/B_hh` parity require:

`abs(X_M - X_P) <= 1e-10 * max(1, abs(X_M), abs(X_P))`

These are fixed before execution and may not be tuned to observed results.

## Shared orientation adapter

Freeze one explicit state permutation before execution:

- MATLAB logical order: `[b,a,z]`, MATLAB column-major / `b` fastest;
- Python logical order: `(a,b,z)`, canonical `a` fastest.

The manifest must contain the exact forward and inverse index permutation used for all P2–P4 mapped comparisons.

Round-trip permutation identity must be exact before P1 starts.

## P1 — static primitives and pointwise economic formulas

### Fixed case grid

Use the following deterministic cases:

- `a in {0.0, 0.25, 0.5, 1.0}`
- `b in {0.0, 2.5, 5.0}`
- `z in {0.5, 0.75, 1.0, 1.5}`
- `v_b in {0.75, 1.0, 1.5}`
- `q in {-0.20, 0.0, 0.20}` with `v_a = v_b*(1+q)`

Use the full Cartesian set unless a formula is undefined for a scientifically explicit reason; any omitted case must be named before execution in the manifest.

### MATLAB execution

Use the actual designated `HANK3_cost.m` and `HANK3_FOC.m` helpers for adjustment cost and transfer FOC.

For consumption, scalar labor, budget components, and drifts that are coded inline in `HANK_2ASSETS_HJB.m`, the MATLAB harness may evaluate the exact line-equivalent expressions, with each expression line-referenced to the designated main file. Do not alter the formula to make it resemble Python.

### Python execution

Call the accepted production functions in `economics.py` wherever available. Do not restate the Python formulas in the harness as the primary result when the production function can be called directly.

### P1 required comparisons

For `a >= a_bar`:

- adjustment cost;
- transfer FOC/control;
- consumption FOC;
- scalar labor FOC;
- `mu_a`;
- `mu_b` and each shared budget component;

must match within `tau_fp`, after symbol adapters.

For `a < a_bar`:

- MATLAB cost must still match Python/accepted analytic cost within `tau_fp`;
- MATLAB transfer FOC must match the frozen bare-`a` legacy analytic formula within `tau_fp`;
- Python transfer FOC must match the accepted `max(a,a_bar)` analytic formula within `tau_fp`;
- for nonzero-transfer cases, the two FOCs are expected to differ materially and this must be demonstrated rather than hidden;
- downstream drift differences caused solely by this accepted low-`a` legacy FOC are evidence of O1 redesign and are not direct parity failures.

Boundary/KKT classifications must obey the accepted Python contract where MATLAB exposes comparable state-constraint quantities; KKT residual validity remains `<=1e-7`.

P1 terminal failure means any unexpected mismatch in a materially comparable primitive, sign convention, formula, or adapter.

If P1 fails, do not execute P2–P4.

## P2 — local policy-selection / HJB candidate parity

### Case manifest

Before execution freeze at least these ten case classes using explicit shared derivative inputs:

1. interior forward/forward comparable branch;
2. interior backward/backward comparable branch;
3. liquid zero-drift comparable case;
4. lower-`a` active state;
5. lower-`b` active state;
6. interior `mu_a=0` crossing candidate;
7. upper-`a` / lower-`b` corner;
8. upper-`a` / interior-`b` zero-liquid-drift corner;
9. dual-upper corner;
10. qualified lower-`b` F/Z near-tie representation case.

Use accepted existing Python regression fixtures as case authority where they already provide deterministic derivative/state values. If a MATLAB-comparable case needs a new explicit derivative tuple, freeze it in the manifest before P1 execution and do not alter it after seeing results.

### P2 comparison rule

For cases where MATLAB and Python implement the same candidate/economic object, compare within `tau_fp`:

- directional derivatives;
- consumption;
- scalar labor;
- transfer;
- adjustment cost;
- `mu_a`, `mu_b`;
- flow utility;
- candidate Hamiltonian;
- direction/admissibility classification after adapter.

Boundary feasibility classifications must agree exactly. Comparable KKT validity must pass the accepted thresholds.

For accepted Python redesigns missing or incomplete in MATLAB — including interior `mu_a=0`, explicit upper/corner closure, full multiplier audit, and F/Z canonicalization — do **not** require a nonexistent MATLAB candidate to match. Instead:

- show the MATLAB omission/legacy behavior directly from the designated code/harness result;
- numerically verify the Python candidate against the accepted analytic drift/boundary/KKT conditions;
- require every redesign case to satisfy its accepted zero-drift/KKT/boundary contracts;
- record it as `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION`.

Qualitative similarity is insufficient where both implementations expose the same quantitative candidate.

If P2 fails materially, do not execute P3–P4.

## P3 — shared finite-grid generator parity

P3 is a deliberately shared mathematical object. It does **not** replace either production productivity process.

### Shared finite grid

Use:

- `a = [0.0, 0.5, 1.0]`
- `b = [0.0, 2.5, 5.0]`
- parity-only `z = [0.75, 1.25]`

### Frozen shared asset drifts

For each `(i_a,i_b,i_z)` use:

`mu_a`:

- lower `a` (`i_a=0`): `+0.020 + 0.005*i_z`
- interior `a` (`i_a=1`): `+0.015` when `i_z=0`, `-0.015` when `i_z=1`
- upper `a` (`i_a=2`): `-0.020 - 0.005*i_z`

`mu_b`:

- lower `b` (`i_b=0`): `+0.030`
- interior `b` (`i_b=1`): `+0.020` when `i_z=0`, `-0.020` when `i_z=1`
- upper `b` (`i_b=2`): `-0.030`

These arrays are parity fixtures only. They are not calibration or dissertation Results.

### Asset generator comparison

Python must use the accepted production asset-generator construction (calling the existing internal asset-generator helper is permitted for parity diagnostics).

MATLAB harness must implement the exact designated directional-rate construction used by the main source for the asset components, without importing Python conventions except through the explicit index adapter.

After mapping orientation, compare:

- every nonzero asset-transition destination;
- every off-diagonal rate;
- every diagonal rate;
- `G_a`, `G_b` full matrices;
- component row sums;
- off-diagonal signs.

Require the frozen generator parity tolerance above and individual generator validity `<=1e-11`.

### Common productivity component for P3/P4 only

To create one common finite mathematical operator for stationary parity, define the external two-state Markov generator:

`Q_common = [[-0.4, 0.4], [0.3, -0.3]]`

This is **not** a replacement for MATLAB's production `la_mat` or Python's reflected diffusion. It is a parity adapter object authorized only for P3/P4 mathematical generator/KFE comparison.

Construct the total common backward generator in both harnesses from the already-verified asset components plus `Q_common`, using each language's native orientation and the frozen permutation adapter.

Require mapped total-generator parity under the frozen generator tolerance.

If P3 fails, do not execute P4.

## P4 — KFE / stationary-distribution / aggregate parity

Use only the P3-accepted common finite backward generator.

### Common measure

Treat the P4 parity object as a finite-state **probability mass** object:

- normalization is `sum(g)=1`;
- use unit positive cell weights for the parity KFE input;
- density is not the primary comparison object;
- `A_hh` and `B_hh` are expectations under the same normalized mass.

This finite-state parity measure does not replace the accepted Python production mass/density contract or MATLAB production quadrature convention.

### Python

Use the accepted production KFE input/solver on the common backward generator through `make_kfe_input` and `solve_stationary_kfe` where compatible. Do not reconstruct a different Python stationary algorithm in the harness when the accepted solver can consume the common generator.

### MATLAB

Use the designated mathematical `G'` forward relation and a parity harness implementing the legacy pinned-row linear solve/normalization on the same common mapped generator. Compare the resulting mathematical stationary object, not row-pinning details.

### Required P4 evidence

For both languages report:

- backward row-sum/off-diagonal validity;
- forward operator equals mapped transpose;
- stationary residual `||G^T g||_inf`;
- normalization error;
- minimum mass and negative-mass count;
- mapped stationary mass vector;
- `A_hh`;
- `B_hh`.

Require:

- each stationary residual and normalization error `<=1e-10`;
- no mass below `-1e-12`;
- mapped mass max absolute difference `<=1e-10`;
- aggregate parity under the frozen `1e-10` scaled rule.

If the common generator is not uniquely stationary, that is a parity-fixture design failure and this task must stop; do not tune the drift arrays or `Q_common` after execution.

## Call budgets and fail-closed execution

P1–P4 are separately bounded scientific stages.

For each stage:

- one MATLAB scientific harness invocation maximum;
- one Python scientific harness invocation maximum;
- one deterministic comparison pass maximum.

A single process may execute multiple cases within its stage.

Once a stage begins evaluating its frozen scientific cases, its execution budget is consumed. Do not rerun that stage after PASS or FAIL.

If a source/environment/harness problem prevents scientific case evaluation before the stage begins, report a named BLOCKED state. Do not silently edit a frozen harness after scientific execution begins.

At the first material parity failure, stop all later P stages.

## Raw evidence preservation

For every reached stage preserve outside the repository:

- exact input manifest slice;
- raw MATLAB output;
- raw Python output;
- mapped/canonical comparison output;
- stdout/stderr or command transcript sufficient to establish execution count;
- SHA-256 and bytes of every artifact.

The repository report must summarize all reached evidence and include the hashes/paths. Do not commit large raw numerical artifacts unless a later task explicitly authorizes it.

## Required classification

Return exactly one primary task classification:

- `MATLAB_PYTHON_TWO_ASSET_HA_NUMERICAL_PARITY_EVIDENCE_COMPLETE__OWNER_ACCEPTANCE_PENDING`
- `MATLAB_PYTHON_TWO_ASSET_HA_P1_FAIL_CLOSED`
- `MATLAB_PYTHON_TWO_ASSET_HA_P2_FAIL_CLOSED`
- `MATLAB_PYTHON_TWO_ASSET_HA_P3_FAIL_CLOSED`
- `MATLAB_PYTHON_TWO_ASSET_HA_P4_FAIL_CLOSED`
- `MATLAB_PYTHON_TWO_ASSET_HA_NUMERICAL_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT`

Do **not** issue final `MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION` from this task.

## Report authorization

Write exactly one repository report:

`docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_SHARED_INPUT_NUMERICAL_PARITY_REPORT.md`

Whether PASS, FAIL_CLOSED, or BLOCKED, the report must contain:

- live GitHub identity;
- Python/MATLAB source identities;
- MATLAB/Python executable identities;
- frozen harness/manifest hashes;
- exact tolerances;
- stage execution counts;
- full P1 result table, including low-`a` legacy counterexamples if reached;
- full P2 case table and redesign classifications if reached;
- P3 orientation permutation and matrix parity diagnostics if reached;
- P4 stationary/KFE/aggregate diagnostics if reached;
- raw artifact inventory with SHA-256/bytes;
- first terminal mismatch/block if any;
- forbidden-operation check;
- final task classification;
- recommended next gate.

## Report-only GitHub mutation

No MATLAB source, Python source/test, fixture, parameter file, or existing report may be modified.

If the new report is the only repository change:

- stage only that report;
- create one commit;
- fresh-fetch before push;
- fast-forward push to live `main` only if remote main has not moved;
- no merge, rebase, reset, or force-push.

Suggested commit subject:

`Record MATLAB Python shared-input HA numerical parity`

## Forbidden operations

Do not:

- modify designated MATLAB source/helpers;
- modify accepted Python source/tests;
- change the O1–O12 Owner decisions;
- change any frozen parity input/tolerance after scientific execution begins;
- replace MATLAB with Octave;
- tune a case to obtain PASS;
- treat the known low-`a` MATLAB FOC legacy difference as a reason to make Python imitate it;
- claim final Owner parity acceptance;
- enter AR(1), transition, IRF, calibration extension, or Results work;
- merge, rebase, reset, or force-push.

## Acceptance meaning

A complete P1–P4 PASS means:

`MATLAB_PYTHON_TWO_ASSET_HA_NUMERICAL_PARITY_EVIDENCE_COMPLETE__OWNER_ACCEPTANCE_PENDING`

It establishes that all materially comparable shared-input HA objects passed the pre-authorized numerical criteria and all intentional redesign/non-comparability cases behaved as frozen by Owner authority.

It does **not** by itself unlock dynamics.

## Recommended next gate

If P1–P4 complete:

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P5_OWNER_FINAL_ACCEPTANCE`

That gate must independently review the numerical report and obtain explicit Owner acceptance before issuing:

`MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`

If any stage fails, the next gate must be a stage-specific diagnostic only; no dynamics may be authorized.
