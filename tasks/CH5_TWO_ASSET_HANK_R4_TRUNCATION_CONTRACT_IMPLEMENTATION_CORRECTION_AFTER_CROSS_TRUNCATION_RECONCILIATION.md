# CH5_TWO_ASSET_HANK_R4_TRUNCATION_CONTRACT_IMPLEMENTATION_CORRECTION_AFTER_CROSS_TRUNCATION_RECONCILIATION

## Task

Correct the previously failed local R4 truncation-contract implementation using the accepted cross-truncation reconciliation, then validate the corrected implementation with focused regression tests and exactly one bounded 25/29 internal-HJB compatibility pair.

This task does **not** authorize a full frozen steady-state rerun, connectivity/KFE/aggregate acceptance, MATLAB parity, threshold tuning, calibration changes, or Results work.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Scientific authority

Accepted evidence:

- consumed-run baseline: `546b88be6316526682c5a02ef4671021d0f387c3`
- candidate-identity diagnostic: `524690c6ab82b0f42758c48c157406d53863d98e`
- first truncation-contract review: `7186204076189a65d89cc96c3ed4c132b9e49d86`
- failed implementation authority/base: `a150dccdbe7fc7af00ec992c65220dafba1b1594`
- cross-truncation reconciliation report: `60527e66df049decdfb6c711a8dc9b12ad195751`
- reconciliation classification:
  `CROSS_TRUNCATION_MACHINE_EQUIVALENCE_CONTRACT_WAS_OVERSTRICT__MOVE_MACHINE_EQUIVALENCE_INTRA_SOLVE`

The failed implementation was not published and is not accepted source. It may be reused only after exact fingerprint verification under this task.

## Required live read-back

Before any mutation, fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_SELECTOR_NEAR_TIE_CANONICALIZATION_AND_TRUNCATION_COMPATIBILITY_IMPLEMENTATION.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_CROSS_TRUNCATION_PHYSICAL_EQUIVALENCE_CONTRACT_RECONCILIATION.md`
- `docs/CH5_TWO_ASSET_HANK_R4_COMMON_CORE_CANDIDATE_IDENTITY_DIAGNOSTIC_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_ACCEPTANCE_CONTRACT_REVIEW_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_CROSS_TRUNCATION_PHYSICAL_EQUIVALENCE_CONTRACT_RECONCILIATION_REPORT.md`
- this task file
- current live versions of `src/ch5_two_asset_hank/contracts.py`, `policies.py`, `steady_state.py`, `diagnostics.py`

## Fresh workspace requirement

Use a new isolated clone/worktree rooted exactly at fresh live `origin/main`.

Record:

- live `origin/main` before work;
- fresh workspace root;
- branch/ref;
- clean pre-change `git status --short --untracked-files=all`.

Do not perform the implementation directly in the preserved failed workspace.

## Live-source continuity gate

Before copying the failed patch, verify that the live-main pre-change blobs for these files are still identical to their corresponding blobs at implementation-authority base `a150dccdbe7fc7af00ec992c65220dafba1b1594`:

- `src/ch5_two_asset_hank/contracts.py`
- `src/ch5_two_asset_hank/policies.py`
- `src/ch5_two_asset_hank/steady_state.py`

Also confirm no intervening live-main source change affects `src/ch5_two_asset_hank/diagnostics.py` or the frozen HJB/boundary/KKT logic relevant to this contract.

If source continuity fails, stop with:

`BLOCKED_R4_CORRECTION_LIVE_SOURCE_DRIFT`

## Preserved failed-patch identity gate

Read-only inspect:

`D:\ProjectTemp\ch5-r4-truncation-contract-implementation-20260829`

It MUST remain unmodified.

Require exact changed path set:

- `src/ch5_two_asset_hank/contracts.py`
- `src/ch5_two_asset_hank/policies.py`
- `src/ch5_two_asset_hank/steady_state.py`
- `tests/test_r4_truncation_acceptance_contract.py`
- `docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_CONTRACT_IMPLEMENTATION_REPORT.md`

Require exact preserved file identities:

- `src/ch5_two_asset_hank/contracts.py`
  - bytes: `5326`
  - SHA-256: `6234E1AE8FD13B9517A71DF1B56763D28F22F8906A30E12884E1CD94D0F14FEC`
- `src/ch5_two_asset_hank/policies.py`
  - bytes: `31381`
  - SHA-256: `46F04A68C36EDE81C3EF66C1F020C57050C03465BFC4A3BC568E0896F96EA922`
- `src/ch5_two_asset_hank/steady_state.py`
  - bytes: `15069`
  - SHA-256: `B9EA856B231B0DF20D5629D6612201E162EB2692F3E8F9434EE98ABCBFFA0109`
- `tests/test_r4_truncation_acceptance_contract.py`
  - bytes: `5426`
  - SHA-256: `4D5AABB359340A911A251A446369A6E92BC73C7F1A9E361A03F04ADE98C285AA`
- failed implementation report
  - bytes: `7489`
  - SHA-256: `CF2F21EEA7FD4FC2CC51CBD7FD5EE7A938ECC9DE025EE63294F9A301BBBC28A6`

Require the tracked three-file binary diff fingerprint:

`618E0EAFE5027F21ED3A263168DD74224F2AD403C5D6F5EC3B626EBE6FCDE11F`

If any identity differs, stop with:

`BLOCKED_R4_CORRECTION_FAILED_PATCH_IDENTITY_MISMATCH`

Do not reconstruct, approximate, or update the expected fingerprint.

## Patch reuse rule

After all identity gates pass, copy **only** these four implementation/test files from the preserved failed workspace into the fresh workspace, preserving bytes and relative paths:

- `src/ch5_two_asset_hank/contracts.py`
- `src/ch5_two_asset_hank/policies.py`
- `src/ch5_two_asset_hank/steady_state.py`
- `tests/test_r4_truncation_acceptance_contract.py`

Do **not** copy the old failed implementation report into the fresh workspace.

Immediately verify the four copied files match the preserved SHA-256/byte identities above.

### Frozen reused components

The reused `contracts.py` and `policies.py` implement diagnostic raw/canonical identity state and narrow intra-solve lower-`b` F/Z near-tie canonicalization.

Under this correction task, after copying:

- `contracts.py` MUST remain byte-identical to SHA-256 `6234E1...14FEC`;
- `policies.py` MUST remain byte-identical to SHA-256 `46F04A...EA922`.

If reconciliation would require changing either file, stop for new authority. This task assumes the scientific correction belongs to inter-truncation compatibility, not alias construction/canonicalization.

Only `steady_state.py` and `tests/test_r4_truncation_acceptance_contract.py` may be edited after the copy.

## Reconciled scientific contract

### A. Intra-solve alias proof

Retain the failed patch's narrow intra-solve active-lower-`b` F/Z alias proof and canonicalization.

Machine-scale equivalence remains valid **only within one fixed HJB solve**.

Retain exactly:

`tau_machine(x,y) = 16 * eps_float64 * max(1, abs(x), abs(y))`

and:

`tau_H = 16 * eps_float64 * max(1, abs(H_i), abs(H_j))`.

A qualifying alias still requires, within the same solve:

- active lower liquid boundary;
- same illiquid branch and transfer suffix/disposition;
- both candidates present/admissible/feasible/KKT-valid;
- both `abs(mu_b) <= 1e-12`;
- consumption, labor components, transfer, adjustment cost, `mu_a`, effective shadow machine-equivalent;
- same `mu_a` drift classification;
- near-tied Hamiltonians under `tau_H`;
- raw multiplier equality not required, but dual feasibility/complementarity/KKT/effective-shadow equivalence required;
- canonical representative uses liquid direction `Z`.

Do not broaden the alias class.

### B. Inter-truncation 25/29 compatibility

Across the two distinct converged HJB solutions, **do not** require `tau_machine` equality for consumption, labor, transfer, adjustment cost, `mu_a`, `mu_b`, or effective shadow prices.

Require instead:

1. Existing common-core normalized max-norm guards remain unchanged and terminal:
   - value <= `1e-3`;
   - consumption <= `1e-3`;
   - transfer <= `1e-3`;
   - labor <= `1e-3`.
2. Add the same existing `normalized_change` metric with the same frozen `1e-3` threshold for:
   - adjustment cost;
   - `mu_a`.
3. Canonical candidate IDs agree state by state.
4. If raw IDs differ, each solve independently proves the same narrow intra-solve alias class, including alias counterpart availability/admissibility and near-tie evidence.
5. Active boundary regime/feasibility and KKT validity remain compatible and valid; no KKT/complementarity failure may be hidden.
6. Compare `mu_b` by frozen drift classification under `1e-12`:
   - `Z` if `abs(mu_b) <= 1e-12`;
   - `F` if `mu_b > 1e-12`;
   - `B` if `mu_b < -1e-12`.
   The 25/29 classifications must agree state by state.
7. Raw multiplier equality is not required across truncations. Multiplier sign/KKT/complementarity failures remain terminal.
8. Effective shadow prices are machine-compared only inside each solve's alias proof; no cross-truncation machine-equality requirement is permitted.
9. Canonical-ID agreement alone is never sufficient: global normalized guards plus bilateral alias evidence for every raw-ID mismatch plus boundary/KKT/drift-classification validity must all pass.

Do not introduce a new state-specific tolerance.

## Frozen thresholds and economics

Do not change:

- `1e-12` drift/zero threshold;
- `1e-7` KKT threshold;
- `1e-3` truncation threshold;
- HJB residual/convergence thresholds;
- generator thresholds;
- grids;
- fixture;
- parameters;
- equations;
- FOCs;
- transfer mechanism/sign;
- adjustment-cost economics;
- boundary/KKT economics;
- generator/KFE/connectivity/recurrent-class/density/aggregate logic.

## Required test-first correction

Revise `tests/test_r4_truncation_acceptance_contract.py` before relying on integration evidence.

Required tests must demonstrate at minimum:

1. all positive/negative intra-solve alias/canonicalization tests from the failed patch remain passing;
2. candidate-order permutation determinism remains passing;
3. exact/near/outside-`tau_H` behavior remains correct;
4. nonzero `mu_b` cannot canonicalize to `Z`;
5. alias scope, availability, KKT, multiplier/effective-shadow negative cases remain fail-closed;
6. a cross-truncation difference larger than `tau_machine` but safely inside all normalized `1e-3` guards can pass when canonical IDs, bilateral alias evidence, boundary/KKT and drift classification all pass;
7. value normalized guard fails independently above `1e-3`;
8. consumption normalized guard fails independently above `1e-3`;
9. labor normalized guard fails independently above `1e-3`;
10. transfer normalized guard fails independently above `1e-3`;
11. adjustment-cost normalized guard fails independently above `1e-3`;
12. `mu_a` normalized guard fails independently above `1e-3`;
13. `mu_b` Z/F/B classification mismatch fails even if scalar normalized changes are small;
14. canonical-ID mismatch fails;
15. raw-ID mismatch without bilateral intra-solve alias availability/proof fails;
16. boundary/KKT incompatibility fails;
17. state-identifying audit/failure evidence remains available.

Do not weaken an existing negative test merely to obtain PASS.

## Authorized engineering checks

After correction:

- `python -m py_compile` on changed/copied Python/test files;
- targeted pytest for `tests/test_r4_truncation_acceptance_contract.py`;
- existing non-steady-state test set with `tests/test_r4_steady_state.py` explicitly excluded;
- `git diff --check`.

`tests/test_r4_steady_state.py` MUST NOT be executed.

## Exactly one bounded 25/29 validation pair

Only after all targeted/non-steady regression checks pass, authorize exactly one new bounded validation pair:

- one internal HJB solve on frozen 25-point `z=0.5:0.0625:2.0`;
- one internal HJB solve on frozen 29-point `z=0.5:0.0625:2.25`;
- common-core comparison only through the corrected truncation compatibility layer.

Do not call `run_frozen_r4_steady_state()`.

Do not proceed to:

- `_a_connectivity`;
- recurrent classes;
- left nullity;
- KFE;
- mass/density;
- `A_hh/B_hh`;
- any full steady-state acceptance stage.

The one-pair budget is consumed on first execution regardless of PASS/FAIL. No same-task rerun.

## Required bounded-pair evidence

Report:

- HJB solve count exactly 1+1;
- all six normalized common-core changes:
  - value;
  - consumption;
  - transfer;
  - labor;
  - adjustment cost;
  - `mu_a`;
- complete common-core raw-ID mismatch list;
- canonical IDs for every raw mismatch;
- bilateral alias availability/proof for every raw mismatch;
- `mu_b` 25/29 drift classifications for every raw mismatch and any classification mismatch anywhere in the common core;
- boundary/KKT compatibility evidence;
- explicit evidence for the four historically diagnosed states;
- any unexpected mismatch class.

If any unexpected mismatch cannot satisfy the exact reconciled contract, fail closed.

## Report authorization

Create exactly one new report:

`docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_CONTRACT_IMPLEMENTATION_CORRECTION_REPORT.md`

Do not publish the old failed report as current evidence.

The new report must include:

- authority/live identities;
- preserved failed-patch fingerprint verification;
- copied-file identity verification;
- files changed;
- exact correction design;
- confirmation that `contracts.py` and `policies.py` retained their preserved failed-patch hashes;
- tests/checks and results;
- bounded pair count/result;
- six normalized changes;
- complete raw/canonical mismatch evidence;
- drift classifications;
- forbidden-operation check;
- git status;
- recommended next gate.

## Failure rule

On any failure:

- stop;
- do not change thresholds;
- do not broaden aliasing;
- do not rerun the bounded pair;
- do not commit/push;
- preserve the workspace for read-only diagnosis.

## Commit/push authorization

If and only if all required tests/checks and the single bounded 25/29 pair PASS, and the only repository changes are exactly:

- `src/ch5_two_asset_hank/contracts.py`
- `src/ch5_two_asset_hank/policies.py`
- `src/ch5_two_asset_hank/steady_state.py`
- `tests/test_r4_truncation_acceptance_contract.py`
- `docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_CONTRACT_IMPLEMENTATION_CORRECTION_REPORT.md`

then:

- explicitly stage only those five paths;
- verify `contracts.py` and `policies.py` still match their frozen reused hashes;
- create exactly one commit;
- fresh-fetch remote before push;
- require remote main still equals the task's live/base commit;
- push fast-forward only;
- no merge/rebase/force-push.

Suggested commit subject:

`Correct R4 cross-truncation compatibility contract`

## Acceptance meaning

PASS means only:

`R4_TRUNCATION_CONTRACT_CORRECTED_AND_BOUNDED_25_29_COMPATIBILITY_VALIDATED__FULL_STEADY_STATE_NOT_RERUN`

It does not accept R4 steady state.

## Forbidden operations

Do not:

- modify `contracts.py` or `policies.py` beyond the exact preserved failed-patch bytes;
- change scientific/numerical thresholds;
- change grids, fixture, parameters, equations, FOCs, transfer, adjustment-cost economics, boundary/KKT economics;
- modify generator/KFE/connectivity/recurrent-class/density/aggregate logic;
- run `tests/test_r4_steady_state.py`;
- call `run_frozen_r4_steady_state()`;
- run full steady-state acceptance;
- proceed to connectivity/KFE/aggregates;
- run MATLAB;
- claim MATLAB-Python parity;
- implement AR(1), transition solver or IRF;
- write Results prose;
- merge/rebase/force-push.

## Final response requirements

Report:

- verdict;
- files read/written;
- live/base commit;
- source-continuity gate;
- failed-patch fingerprint gate;
- copy/reuse identity gate;
- exact correction summary;
- tests/checks executed;
- bounded 25/29 solve counts/result;
- six normalized changes;
- full mismatch/canonicalization/drift-classification evidence;
- forbidden-operation check;
- commit/push identity if published;
- git status;
- acceptance level;
- recommended next gate.

## Recommended next gate

If PASS and independently accepted at GitHub L3/L4 level:

`CH5_TWO_ASSET_HANK_R4_STEADY_STATE_RERUN_AFTER_CORRECTED_TRUNCATION_CONTRACT`

That future task may separately authorize exactly one new full frozen R4 steady-state run. It must remain fail-closed and must not combine MATLAB parity, AR(1), transition or IRF work.