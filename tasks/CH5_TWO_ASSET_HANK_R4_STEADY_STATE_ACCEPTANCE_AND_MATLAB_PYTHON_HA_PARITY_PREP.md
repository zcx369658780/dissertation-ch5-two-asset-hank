# CH5_TWO_ASSET_HANK_R4_STEADY_STATE_ACCEPTANCE_AND_MATLAB_PYTHON_HA_PARITY_PREP

## Task

Freeze the independently accepted Python R4 steady-state evidence and prepare an owner-facing MATLAB–Python two-asset HA parity review package.

This is a **read-only scientific parity-preparation gate**. It does not authorize model repair, source modification, MATLAB execution, Python numerical execution, AR(1), transition dynamics, IRFs, calibration changes, or Results claims.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Reviewer acceptance state

The full frozen R4 steady-state run under the corrected truncation contract is independently accepted for the purpose of entering MATLAB–Python HA parity review.

Accepted execution evidence commit:

`8931eacf4e9f503b9ab12b75399f098177196dfb`

Accepted implementation baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

Accepted Python steady-state classification:

`R4_PYTHON_FROZEN_STEADY_STATE_ACCEPTED_FOR_MATLAB_PYTHON_HA_PARITY_REVIEW`

This acceptance means only that the frozen synthetic Python R4 household steady-state fixture passed all authorized HJB/truncation, connectivity, recurrent-class, KFE, mass/density, and aggregate gates.

It is **not**:

- MATLAB–Python parity;
- dissertation calibration acceptance;
- empirical validation;
- Results acceptance;
- authorization for AR(1), transition, or IRF work.

## Required live GitHub read-back

Fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_RERUN_AFTER_CORRECTED_TRUNCATION_CONTRACT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_RERUN_AFTER_CORRECTED_TRUNCATION_CONTRACT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_CONTRACT_IMPLEMENTATION_CORRECTION_REPORT.md`
- current Python HA implementation files needed for the mapping, including at minimum:
  - `src/ch5_two_asset_hank/contracts.py`
  - `src/ch5_two_asset_hank/economics.py`
  - `src/ch5_two_asset_hank/derivatives.py`
  - `src/ch5_two_asset_hank/boundaries.py`
  - `src/ch5_two_asset_hank/policies.py`
  - `src/ch5_two_asset_hank/generator.py`
  - `src/ch5_two_asset_hank/hjb.py`
  - `src/ch5_two_asset_hank/kfe_contract.py`
  - `src/ch5_two_asset_hank/kfe.py`
  - `src/ch5_two_asset_hank/productivity.py`
  - `src/ch5_two_asset_hank/indexing.py`
  - `src/ch5_two_asset_hank/steady_state.py`

Verify that live model source is unchanged from the accepted implementation baseline except for later task/report-only commits. If scientific source drift is found, stop with:

`BLOCKED_PARITY_PREP_PYTHON_SOURCE_DRIFT`

## Python acceptance evidence to freeze in the report

Record the accepted R4 evidence without rerunning anything:

- primary/buffer HJB residuals;
- KKT residuals;
- generator row sums/off-diagonal validity;
- all six common-core normalized changes;
- canonical/raw candidate evidence and `mu_b` classification compatibility;
- upward/downward endogenous `a` edges;
- closed recurrent class count/support;
- left nullity;
- stationary KFE residual;
- normalization/minimum mass/negative-mass count;
- mass-density consistency;
- exact synthetic `A_hh` and `B_hh`.

Use only the accepted GitHub report. Do not rerun Python.

## MATLAB scientific source

Read-only inspect the owner-designated MATLAB household source:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m`

Do not modify or execute it.

Record:

- existence;
- exact resolved path;
- size in bytes;
- SHA-256;
- line count;
- whether it is a regular file and not an unexpected link/reparse indirection.

If the exact path is absent, do not substitute another MATLAB file automatically. Report:

`BLOCKED_PARITY_PREP_MATLAB_AUTHORITY_NOT_FOUND`

and stop before making any parity claim.

If an existing project provenance record supplies an expected MATLAB SHA-256, compare against it. If no complete expected hash is available in live authority, report the freshly computed hash as `CURRENT_READ_ONLY_MATLAB_IDENTITY` rather than inventing provenance.

## Dissertation/equation authority

Parity review is triangular, not MATLAB-as-oracle:

`dissertation/equation authority ↔ MATLAB implementation ↔ accepted Python reconstruction`.

Use only equation/specification authority that can be identified from existing project records or owner-designated dissertation source. Do not infer missing dissertation equations from MATLAB code.

If the dissertation source or a complete equation-authority record cannot be located in this task, do **not** block the code-to-code mapping. Instead mark each affected row:

`DISSERTATION_AUTHORITY_PENDING_OWNER_REVIEW`

and identify exactly which equation/reference is needed for final scientific parity.

## No numerical execution

Do not run:

- MATLAB;
- Python;
- pytest;
- HJB;
- generator/KFE solvers;
- the frozen fixture;
- any calibration or experiment.

This gate is source reading, mapping, and review preparation only.

## Required MATLAB–Python structural mapping

Prepare a line-referenced side-by-side map. For each item record:

- economic/numerical object;
- dissertation authority/reference if available;
- MATLAB file/line range;
- Python file/line range;
- MATLAB formulation;
- Python formulation;
- parity classification;
- whether owner review is required;
- exact unresolved question if any.

Cover at minimum:

1. state vector and economic meanings of the two assets and productivity state;
2. grid orientation, tensor shape, flattening/index order;
3. household budget identities;
4. consumption FOC;
5. labor FOC and province/region labor treatment;
6. transfer/rebalancing control `d` and sign convention;
7. adjustment-cost function and the `m(a)` scaling convention;
8. illiquid drift `mu_a`;
9. liquid drift `mu_b`;
10. productivity diffusion law and support/boundary treatment;
11. forward/backward directional derivatives;
12. upwind candidate construction;
13. zero-drift candidate construction;
14. lower-`a` boundary state constraint/KKT;
15. lower-`b` borrowing-boundary state constraint/KKT;
16. computational upper-`a` and upper-`b` no-outflow treatment;
17. corner cases, including upper-a/lower-b and dual-upper handling;
18. Hamiltonian comparison and deterministic candidate selection;
19. generator component construction `G_a`, `G_b`, `G_z`;
20. generator row-sum/off-diagonal conventions;
21. productivity operator discretization;
22. KFE forward operator and transpose relationship;
23. stationary-distribution normalization;
24. mass versus density representation and quadrature weights;
25. household aggregate definitions for illiquid and liquid assets;
26. any MATLAB assumptions, shortcuts, or legacy numerical behavior intentionally not inherited by Python.

## Required classification vocabulary

Use exactly one primary classification for every mapped item:

- `STRUCTURAL_MATCH`
- `ECONOMICALLY_EQUIVALENT_DIFFERENT_NUMERICS`
- `AUTHORIZED_PYTHON_REDESIGN`
- `MATLAB_LEGACY_LIMITATION_NOT_TO_INHERIT`
- `POTENTIAL_MATERIAL_MISMATCH_REQUIRES_OWNER_REVIEW`
- `DISSERTATION_AUTHORITY_PENDING_OWNER_REVIEW`

Do not force MATLAB and Python to match line-by-line.

A Python difference that was deliberately introduced to satisfy dissertation/economic authority must not be labeled a parity failure merely because MATLAB implemented an older or incomplete numerical contract.

## Required focus on previously known redesign-sensitive areas

The report must explicitly isolate and explain any MATLAB–Python difference involving:

- adjustment-cost scaling for low `a`;
- lower-bound KKT/state-constraint treatment;
- productivity diffusion/boundary discretization;
- interior zero-illiquid-drift candidates;
- upper-bound state-constraint candidates;
- lower-`b` F/Z representation/canonicalization;
- generator/KFE transpose construction.

For each, state whether the Python behavior is:

- required by accepted scientific authority;
- a numerical stabilization only;
- an unresolved parity question.

## Owner-facing parity checklist

Create a compact manual-review table for the Owner, ordered by scientific importance.

For each checkpoint provide:

- checkpoint ID;
- what the Owner should compare;
- exact MATLAB line(s);
- exact Python file/line(s);
- expected relationship;
- proposed reviewer classification;
- Owner decision field: `ACCEPT / REJECT / NEEDS_DISCUSSION`.

The checklist should be usable without requiring the Owner to read the entire codebase.

## Numerical parity preparation, not execution

Prepare a proposed later numerical-parity protocol, but do not run it.

It must define what a later shared-input comparison should export from both MATLAB and Python, including at minimum:

- common grids and parameter mapping;
- value function;
- consumption;
- labor;
- transfer `d`;
- `mu_a` and `mu_b`;
- boundary/KKT diagnostics;
- generator summaries and selected rows/states;
- stationary distribution if both implementations support the same frozen object;
- `A_hh` and `B_hh`.

For every proposed numerical comparison distinguish:

- exact identity expected;
- tolerance-based numerical equivalence expected;
- directional/sign/qualitative equivalence only;
- intentionally non-comparable because Python is an authorized redesign.

Do not invent numerical tolerances in this prep task. Mark tolerance-setting as a future parity-authority decision unless an existing accepted tolerance already applies to the same object.

## R4 acceptance classification

The report must return one R4 acceptance classification:

- `R4_PYTHON_STEADY_STATE_ACCEPTED_FOR_PARITY_REVIEW`
- `R4_PYTHON_STEADY_STATE_ACCEPTANCE_BLOCKED_BY_EVIDENCE_GAP`

Given an accepted R4 classification, return one parity-prep classification:

- `MATLAB_PYTHON_HA_STRUCTURAL_PARITY_REVIEW_READY_FOR_OWNER`
- `MATLAB_PYTHON_HA_PARITY_PREP_BLOCKED_MATLAB_SOURCE`
- `MATLAB_PYTHON_HA_PARITY_PREP_PARTIAL_DISSERTATION_AUTHORITY_PENDING`
- `MATLAB_PYTHON_HA_PARITY_PREP_BLOCKED_OTHER`

Do **not** return a final MATLAB–Python parity PASS/FAIL in this task.

## Report authorization

Write exactly one new report:

`docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_ACCEPTANCE_AND_MATLAB_PYTHON_HA_PARITY_PREP_REPORT.md`

The report must include:

- live GitHub identity;
- independent R4 acceptance summary;
- accepted Python evidence table;
- MATLAB source identity;
- dissertation/equation authority status;
- complete structural mapping table;
- redesign-sensitive comparison section;
- owner-facing parity checklist;
- proposed future numerical parity protocol;
- R4 acceptance classification;
- parity-prep classification;
- forbidden-operation check;
- recommended next gate.

## Commit/push authorization

Only the new report may be added.

If and only if the report is the sole repository change:

- explicitly stage only the report;
- create one commit;
- fresh-fetch remote before push;
- fast-forward push to live `main` only if remote main has not moved;
- no merge, rebase, reset, or force-push.

Suggested commit subject:

`Prepare MATLAB Python HA parity review after R4 acceptance`

## Forbidden operations

Do not:

- modify MATLAB;
- modify Python source/tests;
- modify fixture, parameters, grids, tolerances, equations, FOCs, boundary/KKT economics, generator, or KFE;
- execute MATLAB or Python numerical code;
- create a new calibration;
- repair either implementation;
- claim final MATLAB–Python parity;
- claim dissertation Results;
- implement AR(1), transition solver, or IRF;
- merge, rebase, reset, or force-push.

## Acceptance meaning

A PASS means the Python R4 steady-state evidence is frozen as accepted for parity review and the Owner receives an auditable MATLAB–Python structural/numerical parity review package.

AR(1), transition, and IRF work remain blocked until the Owner completes the parity review and a later parity gate records the decision.

## Recommended next gate

If the parity package is ready for Owner review:

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW`

That future gate should record the Owner's module-by-module decisions before any numerical parity execution or transition/AR(1) work.
