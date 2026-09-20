# Chapter 5 corrected Option-B terminal-KFE repair and run003 report

Date: 2026-09-20

## Terminal verdict

`FAIL__HJB_CONVERGED__TERMINAL_TOPOLOGY_OR_KFE_GATE`

The topology-persistence and exception-ledger repairs passed the zero-science gate. The one authorized fresh run003 then reached Beijing, reproduced HJB convergence at checkpoint 12, passed the structural topology and SVD rank/nullity gates, and stopped at the first stationary-mass scientific failure. No scientific retry was made.

The exact first failing object is:

`province_index=0 / 北京 / checkpoint=12 / terminal_kfe / stationary_mass / minimum_mass_within_allowance`.

The normalized null vector has minimum mass `-2.217909641958515e-12`, below the permitted arithmetic floor `-1.9184653865526386e-13`. The aggregate negative mass remains within its separate bound, but the frozen contract requires every check to pass. No clipping, absolute-value repair, second normalization, solver substitution, tolerance change, or retry was performed.

## Authority and execution freeze

- Fresh live-main baseline: `829cc10785b88b02700204243e49f694ec8cf54a`.
- Isolated branch: `codex/ch5-mp4c-optionb-terminal-kfe-repair-run003-20260920`.
- Execution-freeze commit: `cac4ae52`.
- Exact authorized pre-science changed paths: `nonlinear_continuation.py`, `optionb_initial_turn_integration.py`, and the focused integration test.
- Accepted initialization, source-native initialization, K1A, and C1 blobs matched.
- The 31-state initialization order matched exactly.
- Run001 and run002 sealed evidence and readback matched. Run002 actual SCC=1 versus sealed-ledger SCC=0 reconciliation was bound without modifying either predecessor.
- Pre/post run003 scientific-code hashes match exactly.

## Zero-science repairs

### Topology serialization

`analyze_exact_positive_topology(Q)` and its exact-positive graph/SCC algorithm remain unchanged and are still called exactly once. The returned in-memory topology continues to drive the existing scientific decisions.

Persistence now uses an explicit topology-specific projection. It retains edge count, component count/sizes, closed labels/members, closed-class count, transient count, and condensation nodes/edges. The CSR adjacency is represented by shape, nonzero count, and data/indices/indptr identities. Labels are represented by length and a deterministic little-endian int64 SHA-256. No generic scientific-object coercion and no second SCC are used.

### Exception-path ledger

The initial-turn driver accumulates province-local terminal-KFE counter deltas in a `try/finally`. Stubbed success and exception-after-increment tests show one accumulation on each path and no duplicate success accumulation. Serialization itself adds no scientific call.

### Gate results

- Focused tests: `18 passed`.
- Synthetic projection test SCC/SVD calls: `0/0`.
- Stubbed success/exception ledger tests: PASS.
- Run002 checkpoint-0 current-only diagnostics regressions: PASS.
- `py_compile`: PASS.
- `git diff --check`: PASS.
- Authority/blob/order, exact changed paths, run001/run002 lineage, and pre-science code freeze: PASS.

## Beijing HJB

- Source-native initializations: `1`.
- Labor roots: `800/800`.
- Policy maps / D2 assemblies: `13/13`; all reached D2 gates passed.
- Selector evaluations: `10,400`.
- Scalar selector roots: `4,148`.
- Interior-Z / interior-a / joint roots: `760 / 17 / 1`.
- Direct HJB updates / post-update evaluations: `12 / 12`.
- Solver: only `scipy.sparse.linalg.spsolve`.
- Maximum normwise backward error: `3.0832786979441453e-16`.
- Checkpoint 12 B: `1.292732587643286e-11`.
- Checkpoint 12 D: `1.2743897048750341e-08` using `||vec_F(V12-V11)||_inf`.
- Primary convergence: PASS.
- Final V SHA-256: `48396D52F13045B4F3370CA892C9989813BBEA8F0D45A577DD8C6D6EDE5ADA93`.
- Final Q artifact SHA-256: `E1F55D0B755CB83D4F6A3CB4FEFD6DBC8CD4F05C6D23FC5DE00302E16B74BF20`.

These values exactly reproduce the accepted run002 Beijing HJB result.

## Beijing terminal KFE

### Topology

- Exact-positive edges: `2316`.
- SCC decompositions: exactly `1`.
- Component count: `11`.
- Component sizes: one component of `400` states and ten components of `40` states.
- Closed communicating classes: exactly `1`.
- Closed-class size: `400`.
- Closed membership: F-order flat indices `200..399` and `600..799`.
- Transient states: `400`.
- Condensation edges: `10`, forming the recorded directed chain into the closed component.
- Labels SHA-256: `4D6A9A47469E183A1C56719C5D39B827F3B7796E885883070F4C3940F7A3C2D9`.
- Adjacency nonzeros: `2316`; CSR carrier identities are persisted in `topology_receipt.json`.

### Dense GESVD

- Calls: exactly `1`.
- Solver: full dense `scipy.linalg.svd`, driver `gesvd`.
- Rank / nullity: `799 / 1`.
- `sigma_max=19.4736601669653`.
- Second-smallest singular value: `2.2838705156609336e-06`.
- Smallest singular value: `3.0494145606360786e-16`.
- Frozen rank threshold: `3.735954297981181e-12`.
- Structural closed-class count equals numerical nullity: `1=1`.
- SVD rank/nullity gate: PASS.

### Stationary mass failure

Exactly one smallest right-singular vector, one global sign orientation, one mass normalization, and one `Q.T@p` were used.

- Stationarity residual infinity norm: `1.3682631416767066e-16`.
- Stationarity bound: `6.197427304868947e-13`.
- Normwise backward ratio: `4.235572839943202e-17`.
- `math.fsum(p)=1.0`.
- `omega*math.fsum(g)=1.0`.
- Minimum p: `-2.217909641958515e-12`.
- Minimum-entry allowance: `-1.9184653865526386e-13` — FAIL.
- Negative entries: `278`.
- Total negative mass: `1.0087680036243705e-11`.
- Total-negative-mass bound: `1.5347723092421108e-10` — PASS.

All other stationarity, source-free accounting, normalization, finiteness, total-negative-mass, no-clipping, and no-retry checks passed. Because the minimum-entry check failed, Beijing did not complete KFE and no stationary household aggregate was produced.

## 31-province and integration status

- Complete HJB+KFE household blocks: `0/31`.
- Beijing HJB: PASS; Beijing KFE: FAIL at stationary-mass nonnegativity.
- Provinces 1 through 30: not started under first-failure semantics.
- Corrected aggregates: `0`.
- `PreFrozenHouseholdOutputBatch`: not constructed.
- Source-faithful labor, K1A, C1, firms, monetary/fiscal batches, and raw-next-payoff: not reached.
- `raw_ra0_turn1_by_destination @ S_destination_origin`: unavailable.

## Exact run003 scientific ledger

| Object | Count |
|---|---:|
| Source-native initializations | 1 |
| Labor roots attempted / returned | 800 / 800 |
| Corrected policy maps / D2 assemblies | 13 / 13 |
| Selector evaluations | 10,400 |
| Scalar selector roots | 4,148 |
| Interior-Z / interior-a / joint roots | 760 / 17 / 1 |
| Direct HJB updates / checkpoint evaluations | 12 / 12 |
| SCC / dense GESVD / normalized candidate / `Q.T@p` | 1 / 1 / 1 / 1 |
| Aggregate evaluations / household batches | 0 / 0 |
| Source-faithful labor / K1A / C1 | 0 / 0 / 0 |
| Firm evaluations | 0 |
| Wage / monetary / fiscal / raw-next-payoff | 0 / 0 / 0 / 0 |
| Scientific retries / solver substitutions | 0 / 0 |
| Turn-2 household / second outer turn | 0 / 0 |
| K1B / K2 / adaptive controller | 0 / 0 / 0 |
| MATLAB / GE-annual-shock-IRF-welfare-Results | 0 / 0 |
| Payoff transformations or repair | 0 |

## Historical consumption

Run001 remains separate: one initialization, 800 labor roots, one policy/D2 map, 800 selector evaluations, 483 scalar selector roots including 206 interior-Z roots, and zero HJB/SCC/KFE/integration calls.

Run002 remains separate: one initialization, 800 labor roots, 13 policy/D2 maps, 10,400 selector evaluations, 4,148 scalar selector roots, 12 HJB updates, actual SCC `1`, and zero GESVD/mass/`Q.T@p`/integration calls. Its sealed SCC count remains `0` and its accepted reconciliation remains unchanged.

## Evidence and protected boundaries

- Evidence root: `reports/ch5_mp4c_corrected_optionb_initial_turn_31_province_household_kfe_k1a_c1_one_turn_integration_20260920_run003`.
- Sealed manifest SHA-256: `18D62A1E388E17D3D0A7001D22998B86389C946B7136D481FB7DE11777A3388B`.
- Manifest entries / bytes: `144 / 1,996,742`.
- Independent readback: PASS; bad paths `0`.
- Pre/post code freeze: exact match.
- Turn 2 was not run.
- CURRENT files were not modified.
- No successor was published.
- Main was not merged.
