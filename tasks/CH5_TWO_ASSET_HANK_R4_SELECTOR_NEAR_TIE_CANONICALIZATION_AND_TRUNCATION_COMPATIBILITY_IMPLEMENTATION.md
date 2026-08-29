# CH5_TWO_ASSET_HANK_R4_SELECTOR_NEAR_TIE_CANONICALIZATION_AND_TRUNCATION_COMPATIBILITY_IMPLEMENTATION

## Task

Implement the reviewed R4 truncation-acceptance contract narrowly and test-first:

1. deterministic selector near-tie canonicalization for qualifying active lower-`b` `F/Z` aliases; and
2. state-level physical-policy compatibility for the frozen 25-vs-29 common-core truncation comparison.

This task implements the accepted numerical contract only. It does not authorize a full steady-state rerun, connectivity/KFE/aggregate acceptance, MATLAB parity, calibration changes, or Results work.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Scientific authority

Accepted contract-review evidence:

- review commit: `7186204076189a65d89cc96c3ed4c132b9e49d86`
- review classification: `REQUIRE_SELECTOR_NEAR_TIE_CANONICALIZATION_AND_PHYSICAL_EQUIVALENCE`
- consumed-run implementation/evidence baseline: `546b88be6316526682c5a02ef4671021d0f387c3`
- diagnosed blocker: `TRUNCATION_SENSITIVITY_NEAR_TIE_OR_IDENTIFIER_ONLY`
- consumed failure interpretation: `NUMERICAL_ACCEPTANCE_CONTRACT_FAILURE__NOT_SCIENTIFIC_MODEL_FAILURE`

The implementation MUST preserve the accepted economic model and all frozen numerical thresholds.

## Required live read-back

Before any mutation, fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_TRUNCATION_ACCEPTANCE_CONTRACT_REVIEW.md`
- `docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_ACCEPTANCE_CONTRACT_REVIEW_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_COMMON_CORE_CANDIDATE_IDENTITY_DIAGNOSTIC_REPORT.md`
- `src/ch5_two_asset_hank/policies.py`
- `src/ch5_two_asset_hank/steady_state.py`
- `src/ch5_two_asset_hank/contracts.py`
- relevant existing R4 tests.

## Workspace and source-identity gate

Use a fresh isolated clone/worktree rooted at live `origin/main`.

Before editing:

- record live `origin/main`;
- record workspace root and branch/ref;
- require clean `git status --short --untracked-files=all`;
- verify that the pre-change blobs for the model source inherited from the consumed baseline remain unchanged relative to commit `546b88be6316526682c5a02ef4671021d0f387c3` for at least:
  - `src/ch5_two_asset_hank/policies.py`
  - `src/ch5_two_asset_hank/steady_state.py`
  - `src/ch5_two_asset_hank/contracts.py`
  - `src/ch5_two_asset_hank/boundaries.py`
  - `src/ch5_two_asset_hank/economics.py`
  - `src/ch5_two_asset_hank/hjb.py`

If any inherited scientific source has drifted from the consumed baseline before this task, stop with:

`BLOCKED_R4_TRUNCATION_IMPLEMENTATION_SOURCE_DRIFT`

Do not merge, rebase, or choose a newer implementation automatically.

## Frozen numerical/scientific contract

Do not change:

- drift/zero tolerance `1e-12`;
- KKT tolerance `1e-7`;
- common-core scalar truncation guard `1e-3`;
- HJB residual/convergence tolerances;
- generator tolerances;
- state grids;
- fixture values;
- parameters;
- equations;
- transfer mechanism or sign;
- FOCs;
- adjustment cost;
- boundary/KKT economics;
- candidate construction or admissibility rules except the final near-tie canonical representative selection described below;
- generator/KFE/connectivity/recurrent-class/density/aggregate logic.

The Hamiltonian near-tie threshold is fixed by the accepted review:

`tau_H = 16 * eps_float64 * max(1, abs(H_i), abs(H_j))`

and near tie means:

`abs(H_i - H_j) <= tau_H`.

For scalar/vector physical quantities use the reviewed machine-equivalence rule:

`tau_machine(x,y) = 16 * eps_float64 * max(1, abs(x), abs(y))`.

No broader tolerance may be substituted.

## Authorized implementation surface

Existing source files that MAY be modified:

1. `src/ch5_two_asset_hank/policies.py`
2. `src/ch5_two_asset_hank/steady_state.py`
3. `src/ch5_two_asset_hank/contracts.py` only if strictly necessary to carry immutable audit evidence described below.

Tests that MAY be created or modified:

4. `tests/test_r4_truncation_acceptance_contract.py` — preferred new focused test file.
5. `tests/test_r4_policy_fixture_resolution.py` — only if an existing selector regression must be updated or extended.
6. `tests/test_r4_steady_state.py` — source may be changed only if strictly necessary to reflect the reviewed compatibility contract, but this test file MUST NOT be executed in this task.

One report MAY be created:

7. `docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_CONTRACT_IMPLEMENTATION_REPORT.md`

No other path may be modified without stopping for new authority.

## Required audit representation

The future selector and truncation comparison must preserve enough immutable state-level evidence to distinguish raw selection representation from canonical physical identity.

If `contracts.py` is changed, additions MUST be diagnostic-only and MUST NOT change economic parameter meanings.

At minimum, each selected state must make it possible to audit:

- raw selected candidate ID before alias canonicalization;
- canonical candidate ID after canonicalization;
- whether a qualifying lower-`b` alias counterpart was actually available/admissible in that solve.

A minimal immutable representation such as `raw_candidate_id` plus a boolean qualifying-alias-availability field is acceptable if it fully supports the fail-closed cross-grid contract. Equivalent diagnostic-only design is permitted if equally auditable.

The existing `candidate_id` exposed to downstream selector/generator logic SHOULD represent the deterministic canonical ID after this patch.

Do not store mutable candidate lists in the scientific contract merely for convenience.

## Selector near-tie canonicalization

Implement a pure deterministic selection/canonicalization step in `policies.py` before final candidate selection.

A lower-liquid-boundary `F/Z` alias class may be considered only if ALL conditions hold:

1. current state is at active lower `b`;
2. candidates share the same illiquid direction/branch;
3. candidates have the same transfer suffix and transfer-zero/sign disposition under the frozen thresholds;
4. IDs differ only by liquid `F` versus `Z` representation;
5. both candidates are already constructed and admissible under existing production logic;
6. both are boundary-feasible;
7. KKT/complementarity validity remains within the existing `1e-7` contract;
8. both independently satisfy `abs(mu_b) <= 1e-12`;
9. consumption, every labor component, transfer, adjustment cost, `mu_a`, and effective shadow price are machine-equivalent under `tau_machine`;
10. `mu_a` has the same economically meaningful direction classification;
11. Hamiltonians satisfy the exact `tau_H` near-tie rule.

Do NOT require raw `lambda_b` equality inside a qualifying alias class. Raw multiplier differences are permitted only when both candidates satisfy the same active lower-boundary primal/dual feasibility, complementarity and KKT contract and the effective shadow policy is machine-equivalent.

Within a qualifying class:

- canonicalize liquid direction to `Z` when `abs(mu_b) <= 1e-12`;
- preserve illiquid direction and transfer suffix exactly;
- if more than one canonical `Z` representative remains, apply existing zero-transfer-first and then lexical-ID ordering;
- retain auditable raw-selection identity/evidence.

Outside a qualifying class:

- preserve the existing larger-Hamiltonian deterministic selection behavior;
- a candidate with `abs(mu_b) > 1e-12` MUST retain an economically meaningful `F/B` direction;
- no aliasing across illiquid directions, transfer suffixes, upper-boundary states, interior liquid states, or different availability/admissibility regimes.

Candidate construction, root finding, controls, FOCs, boundary checks and KKT equations MUST NOT be altered to manufacture equivalence.

## State-level 25/29 truncation compatibility

Replace the unconditional raw `candidate_id` array equality in `steady_state.py` with a fail-closed state-level compatibility check consistent with the accepted review.

Existing global normalized-change guards for value, consumption, transfer and labor remain unchanged and run first.

For each common-core state:

### Case 1: canonical IDs agree

Candidate-identity layer may pass, while all existing HJB/KKT/generator/boundary guards remain in force.

### Case 2: raw IDs differ

The state may pass only if BOTH solves prove the same narrow qualifying active lower-`b` alias class and state-level physical compatibility. Require at minimum:

- alias counterpart availability/admissibility evidence is present on both sides;
- raw IDs differ only by the allowed liquid `F/Z` representation with identical illiquid branch and transfer disposition;
- canonical IDs agree;
- both `abs(mu_b) <= 1e-12`;
- consumption, labor components, transfer, cost, `mu_a`, and effective shadow prices satisfy `tau_machine`;
- `mu_a` direction classification agrees;
- boundary active set/feasibility agree;
- KKT state/component validity remains within existing contracts;
- near-tied Hamiltonian/equivalence evidence satisfies the reviewed `tau_H` rule.

If any item fails, raise `SteadyStateValidationError` with state-identifying evidence. Do not silently summarize or waive the mismatch.

Do not turn raw multiplier equality into an acceptance requirement, but ensure multiplier sign/KKT/complementarity/shadow-policy failures remain terminal.

## Required test-first regression suite

Implement focused tests before relying on the integration check.

The new/updated tests MUST cover at least:

1. observed four-state regression for the diagnosed `FF/FZ` and `BF/BZ` cases;
2. candidate-order permutation determinism;
3. exact Hamiltonian tie canonicalization;
4. near tie at/below `tau_H` canonicalization;
5. outside-near-tie protection where the larger Hamiltonian wins;
6. nonzero liquid drift protection: `abs(mu_b) > 1e-12` cannot canonicalize to `Z`;
7. material-control difference fails even with near-tied Hamiltonians;
8. boundary active-set/feasibility difference fails;
9. KKT/complementarity/effective-shadow failure fails;
10. multiplier representation is permitted only with physical/shadow/KKT equivalence;
11. genuine candidate availability/admissibility switch fails;
12. alias-scope protection for different illiquid direction, transfer suffix, upper-`b`, or interior-`b` states;
13. existing HJB/KKT/generator and `1e-3` truncation guards remain present and terminal;
14. state-level mismatch diagnostics expose raw/canonical IDs and relevant equivalence evidence.

Tests must not weaken an existing test merely to obtain PASS.

## Authorized checks

Allowed after implementation:

### A. Static/targeted engineering checks

- `python -m py_compile` on changed Python/test files;
- targeted pytest for `tests/test_r4_truncation_acceptance_contract.py`;
- targeted pytest for `tests/test_r4_policy_fixture_resolution.py` if that file changed;
- the existing non-steady-state test set may be run with `tests/test_r4_steady_state.py` explicitly excluded.

`tests/test_r4_steady_state.py` MUST NOT be executed.

### B. Exactly one bounded 25/29 integration compatibility pair

After targeted tests pass, authorize exactly one bounded pair using the existing internal HJB solve path:

- one 25-point solve on frozen `z=0.5:0.0625:2.0`;
- one 29-point solve on frozen `z=0.5:0.0625:2.25`;
- common-core comparison only through the revised truncation compatibility layer.

This bounded pair is engineering/scientific-contract validation for the patch. It is NOT a full R4 steady-state fixture rerun and does NOT replenish the consumed one-run budget.

For this bounded pair:

- do not call `run_frozen_r4_steady_state()`;
- do not proceed to `_a_connectivity`;
- do not compute recurrent classes or left nullity;
- do not solve KFE;
- do not compute mass/density or `A_hh/B_hh`;
- do not run any downstream steady-state acceptance stage.

The integration evidence MUST explicitly report the four previously diagnosed states, their raw IDs, canonical IDs, alias-availability evidence, controls/drifts, Hamiltonian gaps/bounds, and PASS/FAIL under the new contract.

If any unexpected additional raw-ID mismatch appears, report it and fail closed unless it independently satisfies the exact same reviewed alias contract. Do not broaden the implementation in this task.

## Failure rules

Stop without same-task scientific redesign if:

- source identity preflight fails;
- implementation requires touching a non-authorized source file;
- a mandatory negative regression cannot be made fail closed without changing the reviewed contract;
- any existing unrelated non-steady regression fails because of the patch;
- the bounded 25/29 pair reveals a material policy, boundary, KKT, availability, or non-near-tie difference;
- new unexpected mismatch classes require a broader rule;
- preserving audit evidence requires changing economic meanings rather than diagnostic fields.

Do not tune thresholds or fixture values after observing results.

## Report requirements

Create:

`docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_CONTRACT_IMPLEMENTATION_REPORT.md`

Report:

- verdict;
- live/base commit and pre-change blob verification;
- files read/written;
- exact implementation design;
- whether `contracts.py` changed and why;
- raw versus canonical candidate representation;
- exact `tau_H` and `tau_machine` implementation;
- multiplier handling;
- tests executed and results;
- bounded 25/29 integration execution count;
- complete common-core raw-ID mismatch list;
- four-state canonicalization evidence;
- any unexpected mismatches;
- confirmation that downstream connectivity/KFE/aggregates were not run;
- forbidden-operation check;
- git status;
- recommended next gate.

## Commit/push authorization

If and only if:

- all required tests/checks pass;
- bounded integration compatibility passes;
- only authorized source/test paths plus the new report changed;
- no downstream steady-state work was executed;

then:

- explicitly stage only changed authorized paths;
- create exactly one commit;
- fresh-fetch remote before push;
- push fast-forward to live `main` only if remote main has not moved;
- no merge, rebase or force-push.

Suggested commit subject:

`Canonicalize R4 lower-b near ties and truncation compatibility`

## Forbidden operations

Do not:

- change grids, fixture, parameters, equations, FOCs, transfer mechanism, adjustment cost, boundary economics or KKT definitions;
- change `1e-12`, `1e-7`, `1e-3` or HJB/generator tolerances;
- modify generator/KFE/connectivity/recurrent-class/density/aggregate code;
- call `run_frozen_r4_steady_state()`;
- run `tests/test_r4_steady_state.py`;
- claim that the consumed fixture now passes;
- proceed to connectivity, recurrent classes, left nullity, KFE, mass/density or aggregates;
- run MATLAB;
- claim MATLAB-Python parity;
- implement AR(1), transition solver or IRF;
- write Results prose;
- merge/rebase/force-push;
- broaden `F/Z` equivalence beyond the reviewed lower-`b` contract.

## Acceptance meaning

A PASS means only:

`R4_TRUNCATION_CONTRACT_IMPLEMENTED_AND_BOUNDED_25_29_COMPATIBILITY_VALIDATED__FULL_STEADY_STATE_NOT_RERUN`

It does not accept R4 steady state.

## Final response requirements

Report:

- verdict;
- files read/written;
- live/base commit;
- pre-change source-blob verification;
- implementation summary;
- exact raw/canonical audit representation;
- tests/checks executed;
- bounded 25/29 pair count and result;
- complete common-core mismatch/canonicalization evidence;
- forbidden-operation check;
- commit/push identity if published;
- git status;
- acceptance level;
- recommended next gate.

## Recommended next gate

If PASS and independently accepted at GitHub L3/L4 level:

`CH5_TWO_ASSET_HANK_R4_STEADY_STATE_RERUN_AFTER_TRUNCATION_CONTRACT_IMPLEMENTATION`

That future task may separately authorize one new full frozen R4 steady-state run under the revised, accepted contract. It must remain fail-closed and must not combine MATLAB parity or AR(1)/transition work.