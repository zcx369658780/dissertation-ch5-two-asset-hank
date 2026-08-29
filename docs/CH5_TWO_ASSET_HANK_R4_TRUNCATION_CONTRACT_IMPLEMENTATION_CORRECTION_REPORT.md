# CH5 Two-Asset HANK R4 Truncation-Contract Implementation Correction

## Verdict

`PASS`

Acceptance level:

`R4_TRUNCATION_CONTRACT_CORRECTED_AND_BOUNDED_25_29_COMPATIBILITY_VALIDATED__FULL_STEADY_STATE_NOT_RERUN`

The reconciled correction passed the focused and non-steady-state regression gates
and the exactly-one bounded 25/29 internal-HJB compatibility pair. This does not
accept R4 steady state and does not establish downstream connectivity, KFE, density,
aggregate, or MATLAB parity evidence.

## Authority and workspace identity

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- Fresh-fetched live/base `origin/main`: `1ac35dbbf39720e0acea071f0dc86da39214a635`
- Fresh implementation workspace:
  `D:\ProjectTemp\ch5-r4-truncation-contract-correction-20260829`
- Initial branch/ref: `main`
- Initial status: clean
- Failed implementation authority/base:
  `a150dccdbe7fc7af00ec992c65220dafba1b1594`
- Reconciliation report commit:
  `60527e66df049decdfb6c711a8dc9b12ad195751`

## Files read

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_TRUNCATION_CONTRACT_IMPLEMENTATION_CORRECTION_AFTER_CROSS_TRUNCATION_RECONCILIATION.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_SELECTOR_NEAR_TIE_CANONICALIZATION_AND_TRUNCATION_COMPATIBILITY_IMPLEMENTATION.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_CROSS_TRUNCATION_PHYSICAL_EQUIVALENCE_CONTRACT_RECONCILIATION.md`
- `docs/CH5_TWO_ASSET_HANK_R4_COMMON_CORE_CANDIDATE_IDENTITY_DIAGNOSTIC_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_ACCEPTANCE_CONTRACT_REVIEW_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_CROSS_TRUNCATION_PHYSICAL_EQUIVALENCE_CONTRACT_RECONCILIATION_REPORT.md`
- current live `contracts.py`, `policies.py`, `steady_state.py`, `diagnostics.py`,
  HJB and relevant boundary/economics sources
- the preserved failed-patch files and failed implementation report

## Source continuity gate

The following live-main blobs were identical to implementation-authority base
`a150dccdbe7fc7af00ec992c65220dafba1b1594`:

| Path | Live/base Git blob |
|---|---|
| `src/ch5_two_asset_hank/contracts.py` | `4b373706e82f8d350e90ea3a1de8b51e4ec72275` |
| `src/ch5_two_asset_hank/policies.py` | `d739c6ae77d6c8ce42119e79bbd3817ab9365e0d` |
| `src/ch5_two_asset_hank/steady_state.py` | `7b804645e5a08fa6c688a98052729c594c9f2519` |
| `src/ch5_two_asset_hank/diagnostics.py` | `4ed47adbdbf04532bc876c95443cb1a5c92f42fd` |
| `src/ch5_two_asset_hank/hjb.py` | `8b3d67079f13dd5d905e8d472a134a3316b26579` |
| `src/ch5_two_asset_hank/boundaries.py` | `1822089050614cc0fe059096832ab7a57e11cdfa` |
| `src/ch5_two_asset_hank/economics.py` | `fa29c7fcb9ed9ce52657affbb5a94c3b24662bed` |

Result: `PASS`; no relevant intervening scientific-source drift.

## Preserved failed-patch fingerprint gate

Read-only workspace:
`D:\ProjectTemp\ch5-r4-truncation-contract-implementation-20260829`

- HEAD/base: `a150dccdbe7fc7af00ec992c65220dafba1b1594`
- Exact changed path set: PASS, five expected paths only
- Tracked three-file binary-diff SHA-256:
  `618E0EAFE5027F21ED3A263168DD74224F2AD403C5D6F5EC3B626EBE6FCDE11F`

| Preserved file | Bytes | SHA-256 |
|---|---:|---|
| `src/ch5_two_asset_hank/contracts.py` | 5326 | `6234E1AE8FD13B9517A71DF1B56763D28F22F8906A30E12884E1CD94D0F14FEC` |
| `src/ch5_two_asset_hank/policies.py` | 31381 | `46F04A68C36EDE81C3EF66C1F020C57050C03465BFC4A3BC568E0896F96EA922` |
| `src/ch5_two_asset_hank/steady_state.py` | 15069 | `B9EA856B231B0DF20D5629D6612201E162EB2692F3E8F9434EE98ABCBFFA0109` |
| `tests/test_r4_truncation_acceptance_contract.py` | 5426 | `4D5AABB359340A911A251A446369A6E92BC73C7F1A9E361A03F04ADE98C285AA` |
| failed implementation report | 7489 | `CF2F21EEA7FD4FC2CC51CBD7FD5EE7A938ECC9DE025EE63294F9A301BBBC28A6` |

Result: `PASS`. The preserved workspace was not modified.

## Copy/reuse identity gate

Exactly four authorized implementation/test files were copied. Immediately after
copy, all four matched the preserved bytes and SHA-256 values above. The old failed
report was not copied.

After correction:

- `contracts.py` remains 5326 bytes and SHA-256
  `6234E1AE8FD13B9517A71DF1B56763D28F22F8906A30E12884E1CD94D0F14FEC`;
- `policies.py` remains 31381 bytes and SHA-256
  `46F04A68C36EDE81C3EF66C1F020C57050C03465BFC4A3BC568E0896F96EA922`.

Neither frozen reused component was edited after copying.

## Files changed/written

- `src/ch5_two_asset_hank/contracts.py` — exact frozen reused bytes
- `src/ch5_two_asset_hank/policies.py` — exact frozen reused bytes
- `src/ch5_two_asset_hank/steady_state.py` — reused patch plus authorized correction
- `tests/test_r4_truncation_acceptance_contract.py` — reused tests plus correction regressions
- `docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_CONTRACT_IMPLEMENTATION_CORRECTION_REPORT.md`

No other path changed.

## Exact correction

The intra-solve selector contract in frozen `policies.py` is unchanged:

- `tau_machine = 16*eps_float64*max(1,abs(x),abs(y))` is used only to prove
  physical equivalence of already-admissible F/Z candidates within one fixed solve;
- `tau_H = 16*eps_float64*max(1,abs(H_i),abs(H_j))` remains the exact
  intra-solve Hamiltonian near-tie rule;
- aliasing remains limited to the precisely qualified active-lower-b F/Z class;
- canonical representative remains Z; raw candidate and multiplier evidence remain
  auditable.

The corrected inter-truncation layer:

1. removes cross-truncation machine comparisons for controls, cost, drifts and
   effective shadows;
2. retains normalized max-norm `<=1e-3` for value, consumption, transfer and labor;
3. adds the identical metric and threshold for adjustment cost and `mu_a`;
4. requires canonical IDs to agree at every common-core state;
5. requires bilateral availability and valid intra-solve Hamiltonian-gap/bound
   evidence whenever raw IDs differ;
6. requires KKT state residuals `<=1e-7` and boundary violations `<=1e-12`;
7. compares `mu_b` by frozen Z/F/B classification at `1e-12`;
8. preserves state-identifying fail-closed errors.

No new state-specific tolerance was introduced.

## Test-first and engineering checks

- First correction RED: cross-truncation consumption difference `1e-12` was rejected
  by the old machine-equivalence check.
- First correction GREEN: focused suite `17 passed`.
- Second correction RED: missing six-array normalized guard helper.
- Second correction GREEN and expanded regression suite: `27 passed in 0.64s`.
- Static compilation of copied/changed Python and test files: PASS.
- Final focused suite: `27 passed in 0.63s`.
- Full non-steady-state suite with `tests/test_r4_steady_state.py` explicitly ignored:
  `56 passed in 3.87s`.
- `git diff --check`: PASS.

Regression coverage includes retained intra-solve exact/near/outside tie,
permutation, nonzero drift, alias scope, availability, KKT, multiplier and effective
shadow behavior; cross-truncation machine-scale differences; all six independent
normalized guards; canonical mismatch; bilateral alias evidence; KKT/boundary
failures; and `mu_b` classification mismatch.

## Exactly-one bounded 25/29 validation pair

- 25-point internal HJB solve: exactly `1`
- 29-point internal HJB solve: exactly `1`
- `run_frozen_r4_steady_state()` calls: `0`
- pair result: `PASS`
- iterations: `34 / 34`
- HJB residual sup: `8.365197423643167e-10 / 8.372715853965929e-10`
- global KKT residual: `9.088497027490715e-15 / 9.423101212153411e-15`
- global boundary violation: `7.993605777301127e-15 / 8.43769498715119e-15`

All six common-core normalized changes:

| Quantity | Normalized change | Guard |
|---|---:|---:|
| value | `2.9348475455283523e-09` | `1e-3` |
| consumption | `2.165192411731261e-09` | `1e-3` |
| transfer | `1.92715998714732e-09` | `1e-3` |
| labor | `3.7659760021779296e-09` | `1e-3` |
| adjustment cost | `1.0345611728412862e-09` | `1e-3` |
| `mu_a` | `1.92715998714732e-09` | `1e-3` |

## Complete current raw/canonical mismatch evidence

The full 153-state common-core scan found exactly two raw-ID mismatches. There were
zero canonical-ID mismatches and zero `mu_b` classification mismatches anywhere.

### `(a,b,z)=(0.5,0.0,0.5)`, index `(1,0,0)`

- raw IDs: `BF / BZ`
- canonical IDs: `BZ / BZ`
- bilateral alias availability: `true / true`
- Hamiltonian gap/bound:
  - 25: `6.661338147750939e-16 / 4.0805675444274515e-15`
  - 29: `1.1102230246251565e-15 / 4.080567544427456e-15`
- `mu_b`: `-5.551115123125783e-16 / 2.1094237467877974e-15`
- drift classifications: `Z / Z`
- KKT state residual: `8.296975767380606e-16 / 4.7411290099317635e-15`
- consumption: `0.5338036710611048 / 0.5338036710611035`
- labor: `0.936673962931148 / 0.9366739629311504`
- transfer: `-0.07480216091979 / -0.07480216091979`
- adjustment cost: `0.009335471324259659 / 0.009335471324259659`
- `mu_a`: `-0.05480216091979 / -0.05480216091979`

### `(a,b,z)=(1.0,0.0,0.5625)`, index `(2,0,1)`

- raw IDs: `BF / BZ`
- canonical IDs: `BZ / BZ`
- bilateral alias availability: `true / true`
- Hamiltonian gap/bound:
  - 25: `1.1102230246251565e-15 / 3.5802429268395466e-15`
  - 29: `1.1102230246251565e-15 / 3.5802429268395544e-15`
- `mu_b`: `-3.219646771412954e-15 / 3.3306690738754696e-15`
- drift classifications: `Z / Z`
- KKT state residual: `3.737930640348919e-15 / 1.8142529359444556e-16`
- consumption: `0.601219394250434 / 0.6012193942504306`
- labor: `0.9355985608236953 / 0.9355985608237009`
- transfer: `-0.08246925563079 / -0.08246925563079`
- adjustment cost: `0.007524051843687794 / 0.007524051843687794`
- `mu_a`: `-0.042469255630789994 / -0.042469255630789994`

This second state is the terminal state from the failed implementation task. It now
passes under the reconciled cross-truncation contract without changing any threshold.

## Four historically diagnosed states

The prior pre-canonicalization diagnostic listed:

1. `(0.0,0.0,0.75)` — expected canonical `FZ`;
2. `(0.5,0.0,0.5625)` — expected canonical `BZ`;
3. `(1.0,0.0,0.5)` — expected canonical `BZ`;
4. `(1.0,0.0,0.5625)` — expected canonical `BZ`.

In the current pair, only state 4 remains in the cross-grid raw-mismatch list above.
States 1–3 produced no cross-grid raw-ID mismatch in the complete scan. The scan also
proved no canonical-ID mismatch and no `mu_b` classification mismatch at any of the
153 states, so all four historical states satisfy those two cross-grid requirements.
The one-pair script emitted detailed raw labels only for actual mismatches; it did not
emit the equal raw label for historical states 1–3. The pair was not rerun to add
non-terminal logging, in compliance with the exact-once rule.

The newly observed raw mismatch at `(0.5,0.0,0.5)` is within the exact authorized
alias class and independently passes bilateral availability, near-tie, canonical-ID,
boundary/KKT and Z-classification requirements. It is not an unexpected mismatch
class.

## Forbidden-operation check

- Preserved failed workspace modified: no.
- `contracts.py` or `policies.py` changed after exact reuse: no.
- Frozen thresholds, grids, fixture, parameters, equations, FOCs, transfer,
  adjustment-cost economics, boundary/KKT economics: unchanged.
- Generator/KFE/connectivity/recurrent-class/density/aggregate logic modified: no.
- `tests/test_r4_steady_state.py` run: no; explicitly excluded.
- `run_frozen_r4_steady_state()` called: no.
- Connectivity, recurrent classes, left nullity, KFE, mass/density, `A_hh/B_hh`:
  not run.
- MATLAB, parity, AR(1), transition, IRF, Results work: none.
- Bounded pair rerun: no.
- Merge, rebase, force-push: none.

## Recommended next gate

After independent GitHub L3/L4 acceptance, the recommended next gate is exactly:

`CH5_TWO_ASSET_HANK_R4_STEADY_STATE_RERUN_AFTER_CORRECTED_TRUNCATION_CONTRACT`

That future task may separately authorize exactly one full frozen R4 steady-state
run. It must remain fail closed and must not combine MATLAB parity, AR(1), transition,
IRF, threshold tuning, or Results work.
