# CH5 Two-Asset HANK R4 Cross-Truncation Physical-Equivalence Contract Reconciliation

## Verdict

`PASS`

Primary classification:

`CROSS_TRUNCATION_MACHINE_EQUIVALENCE_CONTRACT_WAS_OVERSTRICT__MOVE_MACHINE_EQUIVALENCE_INTRA_SOLVE`

Acceptance meaning:

`R4_CROSS_TRUNCATION_PHYSICAL_EQUIVALENCE_CONTRACT_RECONCILED__FAILED_PATCH_AND_STEADY_STATE_NOT_ACCEPTED`

The failed bounded pair was expected under an internally inconsistent contract. The
pre-patch GitHub diagnostic already contained cross-truncation policy differences
larger than the subsequently imposed `tau_machine`, while the established
cross-truncation normalized max-norm guards passed by roughly six orders of
magnitude. No evidence supports the claim that selector canonicalization materially
changed the HJB iteration path.

## Live GitHub and workspace identity

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- Fresh-fetched live `origin/main`: `58257f5be143fb65a88d54440a13338bf3426710`
- Report workspace: `D:\ProjectTemp\ch5-r4-cross-truncation-contract-reconciliation-20260829`
- Report workspace initial branch/status: `main`, clean
- Consumed-run baseline: `546b88be6316526682c5a02ef4671021d0f387c3`
- Candidate-identity diagnostic commit: `524690c6ab82b0f42758c48c157406d53863d98e`
- Truncation-contract review commit: `7186204076189a65d89cc96c3ed4c132b9e49d86`
- Failed implementation authority/base: `a150dccdbe7fc7af00ec992c65220dafba1b1594`

Files read from live GitHub authority included:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_CROSS_TRUNCATION_PHYSICAL_EQUIVALENCE_CONTRACT_RECONCILIATION.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_SELECTOR_NEAR_TIE_CANONICALIZATION_AND_TRUNCATION_COMPATIBILITY_IMPLEMENTATION.md`
- `docs/CH5_TWO_ASSET_HANK_R4_COMMON_CORE_CANDIDATE_IDENTITY_DIAGNOSTIC_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_ACCEPTANCE_CONTRACT_REVIEW_REPORT.md`
- `src/ch5_two_asset_hank/diagnostics.py`
- `src/ch5_two_asset_hank/steady_state.py`
- `src/ch5_two_asset_hank/hjb.py`

The only file written is this report.

## Preserved failed implementation identity

- Root: `D:\ProjectTemp\ch5-r4-truncation-contract-implementation-20260829`
- HEAD/base and local `origin/main`: `a150dccdbe7fc7af00ec992c65220dafba1b1594`
- Read-only inspection performed; no file in this workspace was modified.

Exact status:

```text
 M src/ch5_two_asset_hank/contracts.py
 M src/ch5_two_asset_hank/policies.py
 M src/ch5_two_asset_hank/steady_state.py
?? docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_CONTRACT_IMPLEMENTATION_REPORT.md
?? tests/test_r4_truncation_acceptance_contract.py
```

The changed path set is exactly the five expected paths. File fingerprints are:

| Path | Bytes | SHA-256 |
|---|---:|---|
| `src/ch5_two_asset_hank/contracts.py` | 5326 | `6234E1AE8FD13B9517A71DF1B56763D28F22F8906A30E12884E1CD94D0F14FEC` |
| `src/ch5_two_asset_hank/policies.py` | 31381 | `46F04A68C36EDE81C3EF66C1F020C57050C03465BFC4A3BC568E0896F96EA922` |
| `src/ch5_two_asset_hank/steady_state.py` | 15069 | `B9EA856B231B0DF20D5629D6612201E162EB2692F3E8F9434EE98ABCBFFA0109` |
| `tests/test_r4_truncation_acceptance_contract.py` | 5426 | `4D5AABB359340A911A251A446369A6E92BC73C7F1A9E361A03F04ADE98C285AA` |
| `docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_CONTRACT_IMPLEMENTATION_REPORT.md` | 7489 | `CF2F21EEA7FD4FC2CC51CBD7FD5EE7A938ECC9DE025EE63294F9A301BBBC28A6` |

SHA-256 of the canonical stdout capture from
`git diff --no-ext-diff --binary` for the three tracked modifications:

`618E0EAFE5027F21ED3A263168DD74224F2AD403C5D6F5EC3B626EBE6FCDE11F`

The two untracked files are not included by ordinary `git diff`; their separate
file hashes and byte counts above complete the failed-patch identity.

## Evidence contradiction at the terminal state

State: `(a,b,z)=(1.0,0.0,0.5625)`, diagnostic index `(2,0,1)`.

For quantities whose magnitudes are below one,
`tau_machine=16*eps_float64=3.552713678800501e-15`. The shadow-price bound scales
with its approximately `1.6633` magnitude and is approximately `5.91e-15`.

| Quantity | 25-point diagnostic | 29-point diagnostic | Absolute difference | Later `tau_machine` result |
|---|---:|---:|---:|---|
| consumption | `0.6012193942504221` | `0.6012193942504329` | about `1.08e-14` | FAIL, about `3.0x` bound |
| labor | `0.9355985608237138` | `0.9355985608236972` | `1.6653345369377348e-14` | FAIL, exactly `4.6875x` bound |
| transfer | `-0.08246925563077` | `-0.08246925563079` | about `2.00e-14` | FAIL, about `5.6x` bound |
| adjustment cost | `0.007524051843685145` | `0.007524051843687794` | about `2.65e-15` | PASS |
| `mu_a` | `-0.042469255630769996` | `-0.042469255630789994` | about `2.00e-14` | FAIL, about `5.6x` bound |
| `mu_b` | `1.7763568394002505e-15` | `-9.992007221626409e-16` | about `2.78e-15` | both independently in frozen zero band |
| effective shadow `c^(-gamma_c)` | `1.6632863303532692` | `1.6632863303532393` | about `3.00e-14` | FAIL, about `5.1x` scaled bound |

These values were recorded before canonicalization existed. The later bounded-pair
failure at the same state therefore does not establish a post-patch iteration-path
effect. It reproduces a failure already implied by applying the later inter-grid
machine rule to the older diagnostic evidence.

The existing complete common-core normalized changes were:

| Array | Normalized change | Frozen guard |
|---|---:|---:|
| value | `2.934849005663455e-09` | `1e-3` |
| consumption | `2.1651891433372274e-09` | `1e-3` |
| transfer | `1.92715998714732e-09` | `1e-3` |
| labor | `3.76597996000552e-09` | `1e-3` |

`normalized_change` is the maximum absolute array difference divided by one common
scale. Consequently, passing it bounds every common-core element of that array; it
is not merely an average or aggregate test.

## Decision A: intra-solve F/Z representation equivalence

Machine equivalence remains scientifically appropriate inside one fixed HJB solve.
Here `F` and `Z` candidates use the same solved value and derivative state, so the
question is whether two already-constructed candidates are duplicate numerical
representations of one physical policy, not whether two independently solved
truncations coincide.

The retained intra-solve contract is:

1. active lower liquid boundary only;
2. same illiquid branch and transfer suffix/disposition;
3. both candidates present, admissible and boundary-feasible;
4. both KKT/complementarity systems valid under `1e-7`;
5. both `abs(mu_b)<=1e-12`;
6. consumption, labor components, transfer, adjustment cost, `mu_a`, and effective
   shadow are equivalent under
   `16*eps_float64*max(1,abs(x),abs(y))`;
7. `mu_a` direction classification agrees;
8. Hamiltonians satisfy
   `abs(H_i-H_j)<=16*eps_float64*max(1,abs(H_i),abs(H_j))`;
9. raw `lambda_b` equality is not required, but dual feasibility,
   complementarity, effective shadow, and KKT validity are required;
10. only then is the existing Z candidate the canonical representative.

This rule must not broaden F/Z aliasing.

## Decision B: inter-truncation solved-policy compatibility

Machine equality is rejected across 25- and 29-point converged solutions. Changing
the outer truncation changes the solved value function and derivatives, so small but
non-machine-identical controls are expected even when truncation stability is strong.

The inter-truncation contract should require:

1. the existing normalized common-core guards for value, consumption, transfer and
   labor, all using the unchanged `1e-3` threshold, run first and remain terminal;
2. canonical candidate IDs agree state by state;
3. if raw IDs differ, each solve independently proves the narrow intra-solve alias,
   including candidate availability, near-tie evidence and KKT/boundary validity;
4. active boundary regimes and economically meaningful drift classifications agree;
5. `mu_b` is compared by the frozen `1e-12` zero/F/B classification, not by
   cross-grid machine equality;
6. raw multiplier equality is not required, while sign, complementarity and KKT
   failures remain terminal;
7. effective shadow prices are machine-equivalent only within each solve's alias
   pair; across truncations they are governed by the truncation contract rather than
   `tau_machine`.

Canonical-ID agreement alone is not sufficient: it must be paired with the existing
global max-norm policy guards and bilateral proof that any raw-ID mismatch is only an
intra-solve alias representation.

## Additional cross-truncation guards

Adjustment cost and `mu_a` are physical-policy outputs but are absent from the
current normalized-change tuple. A future implementation should add explicit
`normalized_change` guards for their common-core arrays using the same already-frozen
`1e-3` threshold and the same max-norm definition. This is a symmetric extension of
the pre-existing truncation metric to omitted physical arrays, not a tolerance fitted
to the observed failure.

No new state-specific tolerance is justified. `DERIVE_SEPARATE_CROSS_TRUNCATION_STATEWISE_TOLERANCE`
is rejected because the global normalized max-norm already supplies statewise array
control. `KEEP_MACHINE_EQUIVALENCE_ACROSS_TRUNCATIONS` is rejected because existing
accepted evidence contradicts it. A new looser scalar threshold chosen to clear this
state would be post-hoc tuning.

## Revised contract wording

> Use `tau_machine` and `tau_H` only within each fixed solve to establish that two
> already-admissible active-lower-b F/Z candidates are duplicate representations of
> one physical policy. Across the 25- and 29-point converged solutions, do not require
> machine equality of controls, drifts or effective shadows. Require the unchanged
> `1e-3` normalized max-norm guards for value, consumption, labor and transfer, and
> extend the same pre-existing metric and threshold to adjustment cost and `mu_a`.
> Require canonical-ID agreement, bilateral intra-solve alias availability and proof
> for every raw-ID mismatch, matching boundary/KKT validity, and matching drift
> classifications, with `mu_b` evaluated under the frozen `1e-12` zero band. Any
> failure remains state-identifying and terminal.

## Numerical evidence decision

Another numerical pair is not necessary to reconcile the scientific contract. The
logical contradiction is fully established by existing pre-patch GitHub evidence.
No existing evidence proves that canonicalization changed the HJB iteration path.

A later implementation task may separately authorize one bounded 25/29 validation
pair after correcting the contract, because implementation verification is distinct
from contract reconciliation. That future authorization is not granted here.

## Future implementation surface and regressions

A separately authorized implementation gate should use only:

- `src/ch5_two_asset_hank/policies.py`: retain narrow intra-solve canonicalization;
- `src/ch5_two_asset_hank/contracts.py`: retain immutable raw/canonical and alias
  audit evidence only if necessary;
- `src/ch5_two_asset_hank/steady_state.py`: remove inter-truncation `tau_machine`
  checks, retain existing guards, and add cost/`mu_a` normalized guards;
- `tests/test_r4_truncation_acceptance_contract.py`: revise tests to separate
  intra-solve machine alias proof from inter-truncation max-norm compatibility;
- existing R4 tests only if explicitly named by that future task;
- one new implementation report only if explicitly authorized.

Mandatory regression implications:

- retain all positive and negative intra-solve alias tests, including permutation,
  exact/near tie, nonzero drift, scope, availability, KKT and multiplier cases;
- prove cross-truncation differences above `tau_machine` may pass only when all
  normalized guards, canonical identity, bilateral alias, boundary/KKT and drift
  classification checks pass;
- prove each value/control/cost/`mu_a` normalized guard fails independently above
  `1e-3`;
- prove `mu_b` zero/F/B classification mismatches fail;
- prove missing alias availability, canonical-ID differences, boundary/KKT failures
  and non-near-tie intra-solve pairs remain terminal;
- preserve raw/canonical IDs and state-identifying failure evidence.

The failed local patch must not be published or treated as accepted source by this
planning task.

## Forbidden-operation check

- Python, pytest, HJB, KFE, fixture, MATLAB, and numerical diagnostics run: none.
- Failed implementation workspace modified: no.
- Model source, tests, fixture, parameters, tolerances, equations, FOCs,
  boundary/KKT economics, generator or KFE modified: no.
- Bounded pair or full steady state rerun: no.
- Connectivity, recurrent classes, left nullity, KFE, mass/density or aggregates:
  not entered.
- Claim that canonicalization changed the HJB iteration path: not made; unsupported.
- Merge, rebase, reset or force-push: none.
- Repository write: this report only.

## Recommended next gate

After independent GitHub L3/L4 acceptance of this reconciliation, publish a narrow
implementation-correction task that reuses the preserved failed patch by exact
fingerprint, moves `tau_machine` to intra-solve alias proof only, adds cost and `mu_a`
normalized guards, requires fail-closed regression separation, and may authorize one
new bounded 25/29 validation pair. It must not authorize the full frozen steady-state
fixture, downstream connectivity/KFE/aggregates, MATLAB parity, or any threshold
tuning.
