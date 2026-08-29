# CH5_TWO_ASSET_HANK_R4_CROSS_TRUNCATION_PHYSICAL_EQUIVALENCE_CONTRACT_RECONCILIATION

## Task

Perform a planning-only reconciliation of the R4 physical-policy equivalence contract after the bounded 25/29 implementation validation failed at `(a,b,z)=(1.0,0.0,0.5625)`.

Do not implement, rerun, tune, or accept the steady state.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Current authority state

Accepted GitHub evidence:

- consumed-run baseline: `546b88be6316526682c5a02ef4671021d0f387c3`
- candidate-identity diagnostic: `524690c6ab82b0f42758c48c157406d53863d98e`
- truncation-contract review: `7186204076189a65d89cc96c3ed4c132b9e49d86`
- implementation authority task commit: `a150dccdbe7fc7af00ec992c65220dafba1b1594`

The implementation task failed closed during its single authorized bounded 25/29 pair. No implementation commit or push was made. Therefore live GitHub main still contains the pre-implementation source; the failed implementation remains local-only evidence and is not accepted source.

## Critical reconciliation point

The earlier GitHub diagnostic already reported, at `(a,b,z)=(1.0,0.0,0.5625)` before selector canonicalization:

- labor 25: `0.9355985608237138`
- labor 29: `0.9355985608236972`
- absolute labor difference: `1.6653345369377348e-14`

The later contract defined:

`tau_machine(x,y) = 16 * eps_float64 * max(1, abs(x), abs(y))`

For those labor values the bound is approximately:

`3.552713678800501e-15`

Thus the pre-canonicalization cross-truncation labor difference was already about `4.6875` times the later machine-equivalence bound.

The same diagnostic state also reported cross-truncation differences in consumption, transfer and `mu_a` at approximately `1e-14` to `2e-14`, while the existing common-core normalized truncation changes remained around `1e-9`, well below the frozen `1e-3` truncation guard.

Therefore this review must not assume that the failed post-patch labor check proves an HJB iteration-path change. First determine whether the reviewed contract incorrectly applied a machine-precision equivalence requirement across two distinct truncation solves.

## Required live read-back

Fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_SELECTOR_NEAR_TIE_CANONICALIZATION_AND_TRUNCATION_COMPATIBILITY_IMPLEMENTATION.md`
- `docs/CH5_TWO_ASSET_HANK_R4_COMMON_CORE_CANDIDATE_IDENTITY_DIAGNOSTIC_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_ACCEPTANCE_CONTRACT_REVIEW_REPORT.md`
- `src/ch5_two_asset_hank/diagnostics.py`
- relevant frozen HJB/steady-state contract files needed to interpret the existing `normalized_change` guard.

## Local failed-implementation evidence

Read-only inspect the preserved failed implementation workspace if it still exists:

`D:\ProjectTemp\ch5-r4-truncation-contract-implementation-20260829`

Do not modify it.

Record:

- workspace root;
- HEAD/base commit;
- exact `git status --short --untracked-files=all`;
- exact changed path set;
- SHA-256 and byte count of each changed working-tree file;
- SHA-256 of a canonical textual `git diff --no-ext-diff --binary` capture if safely reproducible;
- SHA-256 and byte count of the local implementation report.

Expected changed path set from the failed task report is exactly:

- `src/ch5_two_asset_hank/contracts.py`
- `src/ch5_two_asset_hank/policies.py`
- `src/ch5_two_asset_hank/steady_state.py`
- `tests/test_r4_truncation_acceptance_contract.py`
- `docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_CONTRACT_IMPLEMENTATION_REPORT.md`

If the workspace is absent or the changed path set differs, report that limitation. Do not reconstruct or modify the patch.

## No numerical execution

Do not run:

- Python;
- pytest;
- HJB;
- KFE;
- fixture;
- MATLAB;
- any numerical diagnostic.

Use only existing GitHub evidence and read-only local failed-patch evidence.

## Core scientific distinction to review

Explicitly distinguish these two comparisons:

### A. Intra-solve representation equivalence

Within one fixed 25-point or 29-point HJB solution, compare two candidate representations such as `BF` versus `BZ` or `FF` versus `FZ` at the same state and using the same solved value/derivatives.

Determine whether machine-scale equivalence is appropriate here for:

- consumption;
- labor;
- transfer;
- adjustment cost;
- `mu_a`;
- effective shadow prices;
- Hamiltonian near ties;
- `mu_b` zero-band treatment;
- boundary/KKT validity.

### B. Inter-truncation solution compatibility

Compare the selected/canonical physical policy from the 25-point solution against the selected/canonical physical policy from the 29-point solution.

Determine whether requiring `tau_machine` across the two different converged HJB solutions is scientifically justified, given that:

- truncation changes the solved value function and derivatives;
- the frozen design already contains an explicit cross-truncation `normalized_change` guard;
- `normalized_change` is a max-absolute-difference divided by a common scale and therefore already bounds every array element;
- the observed accepted diagnostic differences were above `tau_machine` but far below the frozen `1e-3` guard.

## Required alternatives

Assess at least:

1. `KEEP_MACHINE_EQUIVALENCE_ACROSS_TRUNCATIONS`
   - retain `tau_machine` for 25-vs-29 physical controls;

2. `MOVE_MACHINE_EQUIVALENCE_TO_INTRA_SOLVE_ALIAS_ONLY`
   - use machine-scale equivalence only to prove `F/Z` are representation aliases inside each individual solve;
   - across 25/29, require canonical identity agreement plus the existing frozen truncation guards, boundary/KKT validity and availability evidence;

3. `DERIVE_SEPARATE_CROSS_TRUNCATION_STATEWISE_TOLERANCE`
   - define a new cross-grid state-level tolerance derived from pre-existing solver/truncation accuracy, not from the observed failure and not by tuning to obtain PASS;

4. another precisely justified fail-closed design.

Do not select a tolerance merely because it exceeds the observed difference.

## Required questions

The report must answer:

- Was the failed bounded pair expected from an internally inconsistent contract already contradicted by the pre-patch diagnostic evidence?
- Does existing `normalized_change` with the frozen `1e-3` threshold already provide statewise max-norm control/labor/transfer protection across truncations?
- Should cost and `mu_a` receive an explicit cross-truncation statewise guard if they are not already part of the existing normalized-change tuple?
- Should `mu_b` be compared by the frozen zero-band classification rather than machine equality across truncations?
- Should effective shadow prices be machine-equivalent only within an alias pair, while cross-truncation shadow prices are governed by the truncation contract?
- Is a second numerical one-shot evidence run scientifically necessary, or can the contract error be resolved from existing evidence without consuming another HJB pair?
- Does any evidence currently support the claim that canonicalization materially changed the HJB iteration path? If not, say so explicitly.

## Classification

Return exactly one primary classification:

- `CROSS_TRUNCATION_MACHINE_EQUIVALENCE_CONTRACT_WAS_OVERSTRICT__MOVE_MACHINE_EQUIVALENCE_INTRA_SOLVE`
- `KEEP_CROSS_TRUNCATION_MACHINE_EQUIVALENCE__POST_PATCH_EFFECT_NEEDS_DIAGNOSIS`
- `SEPARATE_CROSS_TRUNCATION_STATEWISE_TOLERANCE_REQUIRED`
- `CONTRACT_RECONCILIATION_BLOCKED`

## Output

Write exactly one new report:

`docs/CH5_TWO_ASSET_HANK_R4_CROSS_TRUNCATION_PHYSICAL_EQUIVALENCE_CONTRACT_RECONCILIATION_REPORT.md`

The report must include:

- verdict and primary classification;
- live GitHub identity;
- failed local patch identity/fingerprints if available;
- evidence table showing the old diagnostic differences versus `tau_machine` at the terminal state;
- intra-solve alias-equivalence decision;
- inter-truncation compatibility decision;
- any revised contract wording;
- whether a new numerical evidence pair is necessary;
- exact future implementation surface;
- regression-test implications;
- forbidden-operation check;
- recommended next gate.

## GitHub mutation authorization

Only the new reconciliation report may be created.

If and only if it is the sole repository change in the report workspace:

- explicitly stage only the report;
- commit once;
- fresh-fetch before push;
- fast-forward push to live `main` only if remote main has not moved.

Suggested commit subject:

`Reconcile R4 cross-truncation physical equivalence contract`

Do not publish the failed implementation patch in this task.

## Forbidden operations

Do not:

- modify the failed local implementation workspace;
- modify model source, tests, fixture, parameters, tolerances, equations, FOCs, boundary/KKT economics, generator or KFE;
- run Python, pytest, HJB, KFE, fixture, MATLAB or any solver;
- change `1e-12`, `1e-7`, `1e-3` in this task;
- infer that a broader tolerance is valid merely because it would pass the observed state;
- claim the implementation is accepted;
- rerun the bounded 25/29 pair;
- rerun the full steady state;
- proceed to connectivity/KFE/aggregates;
- claim MATLAB-Python parity;
- implement AR(1), transition or IRF;
- merge, rebase or force-push.

## Acceptance meaning

PASS means only that the failed implementation has been correctly interpreted and the physical-equivalence contract has been scientifically reconciled for a future implementation task.

It does not accept the failed patch or R4 steady state.
