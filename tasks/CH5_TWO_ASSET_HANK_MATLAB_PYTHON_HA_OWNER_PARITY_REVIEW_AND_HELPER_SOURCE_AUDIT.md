# CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT

## Task

Close the remaining structural/equation-authority gap for the two-asset HA block before any MATLAB–Python numerical parity execution.

This task has two purposes only:

1. read-only audit of the MATLAB helper functions needed to resolve O1 adjustment-cost / transfer-FOC parity; and
2. freeze the Owner's current module-by-module structural parity decisions for O1–O12.

This task does **not** authorize MATLAB execution, Python numerical execution, source modification, a numerical parity run, AR(1), transition dynamics, IRFs, calibration changes, or Results claims.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Hard project route

The heterogeneous-agent household block is the core algorithmic foundation of the project.

The Owner requires MATLAB–Python HA parity to be resolved before any AR(1), transition, IRF, or downstream dynamic-model work.

No later task may treat R4 Python steady-state PASS alone as sufficient for transition work.

The required route is:

`accepted Python R4 steady state -> Owner structural parity closure -> shared-input MATLAB–Python numerical HA parity -> Owner parity acceptance -> only then AR(1)/transition/IRF authority`

## Required live GitHub read-back

Fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_ACCEPTANCE_AND_MATLAB_PYTHON_HA_PARITY_PREP_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_RERUN_AFTER_CORRECTED_TRUNCATION_CONTRACT_REPORT.md`
- current accepted Python HA source needed for O1 and structural parity, including at minimum:
  - `src/ch5_two_asset_hank/economics.py`
  - `src/ch5_two_asset_hank/boundaries.py`
  - `src/ch5_two_asset_hank/policies.py`
  - `src/ch5_two_asset_hank/contracts.py`

Verify that accepted Python scientific source remains unchanged from implementation baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

If scientific source drift exists, stop with:

`BLOCKED_OWNER_PARITY_REVIEW_PYTHON_SOURCE_DRIFT`

## Owner decisions already given in chat

The Owner explicitly agreed to continue under the principle that the HA module must be fully validated before downstream dynamics.

Freeze the current Owner decision state as follows unless helper-source evidence creates a direct contradiction:

- O2 Productivity law/support/boundary: `ACCEPT`
- O3 Lower-a/lower-b state constraints and KKT: `ACCEPT`
- O4 Interior `mu_a=0` crossing candidate: `ACCEPT`
- O5 Upper-a/lower-b and dual-upper closures: `ACCEPT`
- O6 Lower-b F/Z near-tie representation/canonicalization: `ACCEPT`
- O7 Budget and drift signs: `ACCEPT`
- O8 Multi-province labor aggregation: `ACCEPT`
- O9 Generator components and KFE transpose: `ACCEPT`
- O10 Stationary uniqueness/normalization redesign: `ACCEPT`
- O11 Mass/density/aggregate conventions: `ACCEPT`
- O12 MATLAB line-90 initialization expression as legacy initialization behavior not to inherit: `ACCEPT`

O1 remains unresolved pending exact MATLAB helper-source audit.

These ACCEPT decisions mean the reviewed Python behavior is accepted relative to the current dissertation/equation-authority route; they do not mean MATLAB and Python must be line-by-line identical.

## O1 MATLAB helper-source audit

Read-only inspect the exact MATLAB source directory containing the designated main file:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Primary designated main source:

`HANK_2ASSETS_HJB.m`

Find only exact helper filenames referenced by that source or by the helper bodies themselves. At minimum search for:

- `HANK3_cost.m`
- `HANK3_FOC.m`

If either exact file is absent, do not silently substitute a similarly named file from another project/date tree. Report the absence and stop O1 closure with:

`O1_MATLAB_HELPER_AUTHORITY_INCOMPLETE`

If present, for each helper record:

- exact resolved path;
- SHA-256;
- bytes;
- line count;
- regular-file/link identity;
- full function signature;
- every formula that affects adjustment cost, transfer FOC, low-a scaling, shadow-price relation, or asset drifts;
- exact line references.

Follow helper calls only when necessary to resolve O1, and only inside the same designated MATLAB source tree unless the Owner has already designated another exact source. Do not execute any helper.

## O1 scientific comparison

Compare MATLAB helper formulas against the accepted Python/dissertation contract:

`m(a) = max(a, a_bar)`

`chi(d,a) = chi_0*abs(d) + (chi_1/2)*d^2/m(a)`

and the corresponding transfer FOC / KKT shadow-price scaling used by accepted Python source.

Determine exactly one O1 classification:

- `O1_STRUCTURAL_MATCH`
- `O1_ECONOMICALLY_EQUIVALENT_DIFFERENT_NUMERICS`
- `O1_MATLAB_LEGACY_LIMITATION_NOT_TO_INHERIT`
- `O1_POTENTIAL_MATERIAL_MISMATCH_REQUIRES_OWNER_REVIEW`
- `O1_MATLAB_HELPER_AUTHORITY_INCOMPLETE`

Do not change Python or MATLAB to manufacture a match.

If MATLAB differs for `a < a_bar` but the accepted dissertation/Python authority requires `max(a,a_bar)`, classify the MATLAB formula as a legacy limitation rather than automatically rejecting Python.

## Structural parity closure

Produce a final O1–O12 Owner decision table with:

- checkpoint;
- MATLAB line/helper reference;
- Python reference;
- dissertation/equation authority status;
- reviewer classification;
- Owner decision;
- whether numerical parity comparison is required later;
- exact reason if an item is intentionally non-comparable numerically.

For O2–O12 preserve the Owner ACCEPT state above unless direct newly read source evidence contradicts the existing parity-prep report. If a contradiction is found, mark only the affected row `NEEDS_DISCUSSION` and explain it; do not silently overturn an Owner decision.

## Meaning of "HA parity"

The final HA parity gate must prove the same **economic household block and accepted numerical contract**, not literal source-code identity.

The final numerical parity protocol must distinguish:

1. `EXACT_OR_NEAR_NUMERICAL_MATCH_REQUIRED`
   - same economic object and same numerical representation can be placed on shared inputs;

2. `ECONOMIC_EQUIVALENCE_UNDER_ADAPTER_REQUIRED`
   - same economic object but orientation/measure/index adapters are required;

3. `AUTHORIZED_REDESIGN_VALIDATED_AGAINST_DISSERTATION`
   - MATLAB legacy implementation is not the target numerical oracle; parity is judged against dissertation/equation authority plus controlled special-case tests;

4. `NOT_COMPARABLE_UNTIL_COMMON_OBJECT_DEFINED`
   - e.g. two-state MATLAB productivity versus continuous reflected Python diffusion without a shared special case.

A future parity PASS must not be issued merely because signs or qualitative shapes look similar where exact quantitative comparison is scientifically available.

## Required future numerical-parity plan

Without executing anything, define the exact next numerical-parity gate needed to validate the complete HA core.

The plan must specify shared-input comparison blocks in this order:

### P1. Static economic primitives / pointwise formulas

Compare at a frozen set of interior and boundary states:

- adjustment cost;
- consumption FOC;
- labor FOC;
- transfer FOC;
- `mu_a`;
- `mu_b`;
- boundary admissibility/KKT quantities where MATLAB exposes them.

### P2. One-step policy-selection / HJB local objects

Compare shared-state derivative inputs and outputs:

- forward/backward derivatives;
- candidate controls;
- Hamiltonians;
- selected directions/candidates;
- zero-drift and corner cases.

For authorized Python redesigns missing in MATLAB, define controlled cases that demonstrate the MATLAB omission/legacy behavior and the dissertation-consistent Python behavior rather than demanding identical output.

### P3. Generator parity

On a deliberately shared finite grid/object, compare:

- `G_a` / asset-transition rows;
- `G_b` rows;
- productivity component only where a common productivity special case is defined;
- total backward generator row sums/off-diagonals;
- indexing/orientation adapters.

### P4. KFE / stationary distribution parity

Only after P3 mapping is valid, compare:

- forward operator transpose relation;
- stationary residual;
- normalized mass under a common finite-state object;
- aggregates `A_hh`, `B_hh` under the same measure.

Do not require MATLAB arbitrary pin-row implementation details to match Python; compare the mathematical stationary object.

### P5. Full HA block acceptance

Define the conditions under which the Owner may finally declare:

`MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`

That final classification must require all materially comparable P1–P4 objects to pass, all authorized redesigns to be explicitly justified against dissertation authority, and no unresolved material mismatch.

## No numerical execution

Do not run:

- MATLAB;
- Python;
- pytest;
- HJB;
- KFE;
- fixture;
- shared-input experiments.

This is source/equation audit and parity-authority preparation only.

## Output

Write exactly one report:

`docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`

The report must contain:

- live GitHub/source identity;
- MATLAB main/helper identities;
- O1 helper formulas with line references;
- O1 classification;
- final O1–O12 Owner decision table;
- any contradiction found relative to the parity-prep report;
- exact definition of final HA parity acceptance;
- P1–P5 future numerical parity protocol;
- required next gate;
- forbidden-operation check.

## Classification

Return one structural-closure classification:

- `OWNER_STRUCTURAL_PARITY_CLOSED__NUMERICAL_PARITY_REQUIRED`
- `OWNER_STRUCTURAL_PARITY_PARTIAL_O1_HELPER_AUTHORITY_INCOMPLETE`
- `OWNER_STRUCTURAL_PARITY_BLOCKED_MATERIAL_MISMATCH`

Do **not** return final numerical parity PASS/FAIL.

## Commit/push authorization

Only the new report may be added.

If and only if the report is the sole repository change:

- explicitly stage only the report;
- create one commit;
- fresh-fetch remote before push;
- fast-forward push to live `main` only if remote main has not moved;
- no merge, rebase, reset, or force-push.

Suggested commit subject:

`Close HA structural parity decisions and audit MATLAB helpers`

## Forbidden operations

Do not:

- execute or modify MATLAB;
- execute or modify Python source/tests;
- tune parameters/tolerances;
- reinterpret a Python redesign as accepted solely because it differs from MATLAB;
- claim numerical parity;
- enter AR(1), transition, IRF, calibration, or Results work;
- merge, rebase, reset, or force-push.

## Recommended next gate

If classification is `OWNER_STRUCTURAL_PARITY_CLOSED__NUMERICAL_PARITY_REQUIRED`:

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_SHARED_INPUT_NUMERICAL_PARITY`

That future gate should execute P1–P4 in bounded stages, stop fail-closed on the first material mismatch, and require explicit Owner acceptance before any dynamic extension.
