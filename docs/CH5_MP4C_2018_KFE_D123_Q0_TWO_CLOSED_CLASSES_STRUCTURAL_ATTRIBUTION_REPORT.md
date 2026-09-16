# CH5 MP4C 2018 KFE D1-D3 Q0 two-closed-class structural attribution

Date: 2026-09-16

Task: `CH5_MP4C_2018_KFE_D123_Q0_TWO_CLOSED_CLASSES_STRUCTURAL_ATTRIBUTION_20260916`

## Verdict

`ATTRIBUTED__TWO_RECURRENT_CLASSES_FROM_EXACT_ZERO_ASSET_DRIFT_SINKS`

Both closed communicating classes are exact asset-drift sinks on the lower-a
boundary.  At all four recurrent states, the selected interior-liquid Z policy
sets `g_b=0.0` exactly and the active lower-a / zero-kink multiplier branch
sets `g_a=0.0` exactly.  There are no positive asset-transition rates.  The
only positive outgoing Q0 rate is the accepted productivity-state switch
`z=0.8 <-> z=1.3` at rate `1/3`, which connects the two members inside each
size-2 closed class.

Thus closure is not produced by a nonzero drift cycling through another
directed asset topology.  Its immediate cause is exact zero consumed drift in
both asset dimensions.  The policy mechanism is jointly:

- `INTERIOR_LIQUID_Z_ZERO_DRIFT_SWITCH` for the liquid dimension;
- `lower_a` state constraint plus `zero_kink` transfer branch;
- `ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERVAL_CANONICAL_MIN` and
  `ACTIVE_EQUALITY_CANONICAL_ZERO` for the illiquid dimension.

This is a mixed policy-law origin for an exact-zero-drift sink, but the graph
closure itself is completely resolved by the exact zero asset rates.

## Git and object identity

- Fresh-fetched baseline: `1238de8ae77aade0a9967c92c7723a8a65f86085`.
- Branch:
  `codex/ch5-mp4c-2018-kfe-d123-q0-two-closed-classes-attribution-20260916`.
- Candidate SHA: reported by the immutable post-push remote readback; a commit
  cannot contain its own SHA without changing it.
- Q0 SHA-256:
  `093E1AF1ADFEEE5C50D3DD91EDDD678EBAC5BBA6C42E64DE73A63B82102AF1D5`.
- Q0 was not modified or reassembled.

Changed paths are exactly the task-local forensic script, this report, and the
four files in the structural-attribution evidence directory.  No selector,
generator, policy, grid, seed, calibration or production source changed.

## Closed class A — SCC label 0

Asset coordinate: `(i_b,i_a)=(5,0)`, `(b,a)=(-0.1578947368421053,0.0)`.

### State flat 5 — `(5,0,0)`, `z=0.8`

- receipt: `cell_0005.json`, SHA-256
  `7D6537B523FC96006E3B8CD310F2908D8090CE03D279D5E9330ED30E13E59730`;
- policy: `INTERIOR_Z_ZERO_LIQUID_SWITCH`;
- active constraints: `lower_a`;
- transfer branch: `zero_kink`;
- derivative branches: `a=forward`, `b=zero`;
- Z marker: `INTERIOR_LIQUID_Z_ZERO_DRIFT_SWITCH`;
- lower-a marker:
  `ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERVAL_CANONICAL_MIN`;
- `q_b=0.012500213882917605`;
- `q_a=0.011250192494625845`;
- `c=8.944195389902259`;
- `l=0.6929663884478887`;
- `d=-0.0`, `cost=0.0`;
- `g_b=0.0`, `g_a=0.0`.

Complete positive outgoing Q0 rates:

- flat `5 -> 405`, `(5,0,0) -> (5,0,1)`, productivity transition only,
  rate `0.3333333333333333`.

The row diagonal is `-0.3333333333333333`; positive outgoing-rate sum is
`0.3333333333333333`.  There are no asset outgoing rates.

### State flat 405 — `(5,0,1)`, `z=1.3`

- receipt: `cell_0405.json`, SHA-256
  `89807039258366104C85641B79D9B2559A2CD72D793E54414C53FB7AF98A00A3`;
- policy: `INTERIOR_Z_ZERO_LIQUID_SWITCH`;
- active constraints: `lower_a`;
- transfer branch: `zero_kink`;
- derivative branches: `a=forward`, `b=zero`;
- Z marker: `INTERIOR_LIQUID_Z_ZERO_DRIFT_SWITCH`;
- lower-a marker:
  `ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERVAL_CANONICAL_MIN`;
- `q_b=0.005463705846706049`;
- `q_a=0.004917335262035445`;
- `c=13.528708681221874`;
- `l=0.6471378718820484`;
- `d=-0.0`, `cost=0.0`;
- `g_b=0.0`, `g_a=0.0`.

Complete positive outgoing Q0 rates:

- flat `405 -> 5`, `(5,0,1) -> (5,0,0)`, productivity transition only,
  rate `0.3333333333333333`.

The row diagonal is `-0.3333333333333333`; positive outgoing-rate sum is
`0.3333333333333333`.  There are no asset outgoing rates.

## Closed class B — SCC label 6

Asset coordinate: `(i_b,i_a)=(6,0)`, `(b,a)=(0.2105263157894739,0.0)`.

### State flat 6 — `(6,0,0)`, `z=0.8`

- receipt: `cell_0006.json`, SHA-256
  `DF640A5A9D121D658F796231556AEBDB2762BFA7E922060978D3E5E8C34CC814`;
- policy: `INTERIOR_Z_ZERO_LIQUID_SWITCH`;
- active constraints: `lower_a`;
- transfer branch: `zero_kink`;
- derivative branches: `a=forward`, `b=zero`;
- Z marker: `INTERIOR_LIQUID_Z_ZERO_DRIFT_SWITCH`;
- lower-a marker:
  `ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERVAL_CANONICAL_MIN`;
- `q_b=0.012463405130485179`;
- `q_a=0.011217064617436661`;
- `c=8.957393306123056`;
- `l=0.6925577982332177`;
- `d=-0.0`, `cost=0.0`;
- `g_b=0.0`, `g_a=0.0`.

Complete positive outgoing Q0 rates:

- flat `6 -> 406`, `(6,0,0) -> (6,0,1)`, productivity transition only,
  rate `0.3333333333333333`.

The row diagonal is `-0.3333333333333333`; positive outgoing-rate sum is
`0.3333333333333333`.  There are no asset outgoing rates.

### State flat 406 — `(6,0,1)`, `z=1.3`

- receipt: `cell_0406.json`, SHA-256
  `62938AD9B607C5B38B1B8727F95C80D368F2CE2CC767FF4C135F12E134E8051D`;
- policy: `INTERIOR_Z_ZERO_LIQUID_SWITCH`;
- active constraints: `lower_a`;
- transfer branch: `zero_kink`;
- derivative branches: `a=forward`, `b=zero`;
- Z marker: `INTERIOR_LIQUID_Z_ZERO_DRIFT_SWITCH`;
- lower-a marker:
  `ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERVAL_CANONICAL_MIN`;
- `q_b=0.005453072140841891`;
- `q_a=0.004907764926757702`;
- `c=13.541893014759237`;
- `l=0.6468857778838657`;
- `d=-0.0`, `cost=0.0`;
- `g_b=0.0`, `g_a=0.0`.

Complete positive outgoing Q0 rates:

- flat `406 -> 6`, `(6,0,1) -> (6,0,0)`, productivity transition only,
  rate `0.3333333333333333`.

The row diagonal is `-0.3333333333333333`; positive outgoing-rate sum is
`0.3333333333333333`.  There are no asset outgoing rates.

## Closure mechanism

All four recurrent states are interior in b but located at the lower-a state
constraint.  Their persisted policy receipts show:

1. the two one-sided liquid drifts have a strict sign crossing;
2. the accepted Z branch selects the unique zero-liquid-drift shadow and stores
   `g_b=0.0` exactly;
3. the active lower-a equality uses the zero-kink multiplier intersection and
   stores `g_a=0.0` exactly;
4. `d=-0.0` and `cost=0.0` under the zero-kink transfer branch;
5. only the accepted two-way productivity generator remains active.

Therefore the recurrent classes are directly caused by the conjunction of Z,
zero-kink and the lower-a state constraint.  Neither upper/lower-b boundary
behavior nor a nonzero deterministic asset cycle is involved.  The fact that
two adjacent b nodes independently satisfy the same exact-zero policy
conditions creates two separate productivity pairs rather than one connected
asset class.

## Condensation DAG and reachability basins

The exact-positive graph reproduction is identical to the accepted result:

- 2,318 directed edges;
- 400 SCCs, all size 2;
- 759 condensation-DAG edges;
- two closed SCCs, labels 0 and 6;
- 796 transient states;
- SCC-label SHA-256:
  `63717388651FFCCB336F6D0D324D6E3B063276E4F4D3ADE726FD639A63494A76`.

Reachability partition:

| Category | SCCs | States |
|---|---:|---:|
| A only | 6 | 12 |
| B only | 280 | 560 |
| both A and B reachable | 114 | 228 |
| neither | 0 | 0 |

These are graph reachability classes only.  They are not probabilistic
absorption weights.

The complete 400-node condensation DAG, every node's successors, distances to
reachable closed classes, all 759 edges and all reachability labels are stored
in `structural_attribution.json`.

## Asset-grid separatrix and first directed split

The reachability partition has an exact rectangular form:

- at `a=0`, b indices `0..5` are A-only and b indices `6..19` are B-only;
- at every positive-a row (`i_a=1..19`), b indices `0..5` can reach both
  classes, while b indices `6..19` are B-only.

Consequently the 26 neighboring asset-grid category changes are:

- six a-direction pairs between `i_a=0` and `i_a=1` for `i_b=0..5`:
  A-only versus both-reachable;
- one b-direction pair at `a=0`, between `i_b=5` and `i_b=6`:
  A-only versus B-only;
- nineteen b-direction pairs at `i_a=1..19`, between `i_b=5` and `i_b=6`:
  both-reachable versus B-only.

The first immediate directed fork is SCC 21 at
`(i_b,i_a)=(5,1)`, `(b,a)=(-0.1578947368421053,0.5263157894736842)`.
It has successors SCC 0 (A-only) and SCC 20 (B-only); the shortest DAG
distances are one edge to A and two edges to B.  The complete attribution finds
24 such directed fork SCCs and persists all of them.  This identifies the
downstream reachability split without edge tolerances or graph repair.

## Existing V0/V1 diagnostic comparison

The accepted `failed_cell_diagnostics.json` contains V0/V1 comparisons only at
the historical coordinates `(19,19,0)`, `(19,19,1)` and `(19,18,0)`.  None of
the four recurrent coordinates `(5,0,0)`, `(5,0,1)`, `(6,0,0)`, `(6,0,1)`
matches those persisted diagnostics.  Therefore no exact-coordinate V0/V1
comparison is available.  No V1 selector or new derivative calculation was
performed.

## Runtime ledger and verification

| Operation | Calls |
|---|---:|
| accepted Q0 load | 1 |
| structural graph audit | 1 |
| SCC decomposition | 1 |
| condensation/reachability analysis | 1 |
| accepted cell receipt reads | 800 |
| SVD/GESVD/eigendecomposition/nullspace | 0 |
| stationary-mass construction | 0 |
| `Q0.T @ p` | 0 |
| row replacement/pin/source RHS | 0 |
| selector/root/policy map | 0 |
| D2 reassembly/HJB/V1 remap | 0 |
| MATLAB/downstream | 0 |
| retry/edge tolerance/graph repair/artificial diffusion | 0 |

- task-local script `py_compile`: PASS;
- `git diff --check`: PASS;
- task-local script SHA-256 before/after execution:
  `941A81A3354F8EB5ACE9905530BD4C8C9CF3E88EEFCC0ADF814987F93B553D9C`;
- code-freeze readback: exact match;
- wall time: `5.2991386000067` seconds;
- sealed evidence manifest: 3 entries, 360,238 bytes;
- `structural_attribution.json` SHA-256:
  `31167A91A51FED93B03FA2BB74A6C316BD95F3A04A1FAB7E0BF69E0A9C4AADD2`.

## Scientific boundary

The accepted Q0 has a structurally nonunique invariant stationary space because
it contains two exact-zero-asset-drift recurrent productivity pairs.  This is a
property of the accepted one-step V0 policy operator and its deterministic
upwind graph.

It must not be described as economic multiple equilibria, corrected HJB
fixed-point multiplicity, nonlinear HJB nonexistence, a stationary economic
equilibrium or Results evidence.  Results eligibility remains `FALSE`.

This task does not prescribe a repair or publish a successor.  Any decision to
alter the accepted Z law, zero-kink handling, boundary law, grid or subsequent
fixed-point route remains a fresh Reviewer/Owner scientific decision.
