# CH5 MP4C 2018 KFE D1-D3 interior Z switching repair and Option A reexecution

Date: 2026-09-16

Task: `CH5_MP4C_2018_KFE_D123_INTERIOR_Z_SWITCHING_REPAIR_AND_OPTION_A_REEXECUTION_20260916`

## Verdict

`PASS__OPTION_A_COMPLETE_800_CELL_CORRECTED_POLICY_MAP__D2_PASS__ONE_DIRECT_HJB_STEP_COMPLETED`

The Owner-adopted corrected-target interior zero-liquid `Z` switching law was
implemented generically under the frozen D1+D2+D3 contract.  A fresh Option A
execution then completed all 800 F-order cells with durable
`SELECTED_ADMISSIBLE` receipts.  D2 was assembled exactly once only after the
complete-map gate and passed all frozen invariants.  One sparse direct HJB solve
was then performed and passed the finite/residual evidence checks.

There was no retry, second policy map, selector evaluation on `V1`, nonlinear
continuation, KFE, MATLAB or downstream model call.  Results eligibility remains
`FALSE`.

## Git identity and changed paths

- Fresh-fetched baseline: `c2e3c257a1e508acf9f567a3d672ca4c751dc770`.
- Branch:
  `codex/ch5-mp4c-2018-kfe-d123-interior-z-switching-repair-option-a-reexecution-20260916`.
- Scientific-code Git HEAD before selector call 1 was the baseline above; the
  exact uncommitted implementation is bound by the pre-execution per-file hashes.
- Candidate SHA convention: the final candidate SHA is returned after commit,
  non-force push and remote readback because a commit cannot embed its own SHA.

Changed implementation/test paths:

- `src/ch5_two_asset_hank/corrected_diagnostic/selector.py`
- `src/ch5_two_asset_hank/corrected_diagnostic/option_a_step.py`
- `tests/test_mp4c_2018_kfe_d123_interior_z_switching.py`

Generated evidence is under:

`reports/ch5_mp4c_2018_kfe_d123_interior_z_switching_option_a_reexecution_20260916/`

No source-faithful/production path, seed, grid, calibration, D2 generator,
boundary contract, adjustment-cost law or Results material changed.

## Authority and frozen inputs

Startup authority was read from the fresh baseline in the task-prescribed order,
including the Owner adoption, accepted Cell 5 algebraic attribution, accepted
lower-a repair, accepted corrected selector/Option-A driver/D2 generator and the
exact seed-grid-scalar provenance.

The live readback matched the accepted identities:

| Object | Identity |
|---|---|
| Option A seed container | 13,362 bytes; SHA-256 `1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81` |
| `v0` field | shape `(20,20,2)`; F-order little-endian float64 SHA-256 `564B95B818713477691389903C3CFF72B5A7F991B924D52FBEB23D5A3675D665` |
| Scalar binding | 2,732 bytes; SHA-256 `A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6` |
| Liquid grid | SHA-256 `A3FF663C18A2088A75B0E76C8ADA982EAF6D33ACFECB8DAA17C6D7DDE0533A76` |
| Illiquid grid | SHA-256 `AE3A3A789FBC0DC9900B8153DEC717264C74AAB6FDA356C21C0EB22EEAC52567` |
| Productivity grid | SHA-256 `A35F6FAB6E4564C6F4B1962A2ADE64E477F808432F747ABC7ACCF5E70B0B39B7` |

The exact Option A scalars, switch matrix, `(b,a,z)=(20,20,2)` grid, F-order
mapping and direct-step equation remained unchanged.

## Implemented Z contract

At an interior liquid node, each existing a-side active-set / derivative-branch /
transfer-regime combination first retains its raw backward and forward liquid
candidates.  A `Z` root is invoked only when both raw liquid shadows are finite
and positive and the prospective endpoint evidence gives the strict crossing
`g_b^B > bound_B` and `g_b^F < -bound_F`.  Endpoint zero or direction-consistent
cases do not invoke a root.

Each eligible combination receives at most one counted root procedure, confined
to the closed interval between the two positive raw shadows.  The procedure uses
a fixed 513-point log-domain uniqueness screen and at most one Brent solve; it
has no widening, retry, optimizer, averaging, interpolation, floor, cap or
clipping path.  Absent, nonunique, nonfinite, nonpositive and out-of-interval
results reject fail-closed.

For a finite root the selector recomputes `c,l,d,cost,g_b,g_a,utility`, the a-side
shadow/multiplier/KKT objects and Hamiltonian from the root.  A raw root residual
inside the prospective arithmetic bound is represented as consumed `g_b=0.0`
with marker `INTERIOR_LIQUID_Z_ZERO_DRIFT_SWITCH`.  The Z candidate then passes
the same domain, face, complementarity, transfer-KKT, finite, deduplication and
Hamiltonian comparison as B/F.  Liquid boundary nodes never use Z.

The lower-a zero-kink canonical-minimum repair is reused unchanged.  Slack,
upper-a and nonzero-transfer laws are not altered.  The D2 strict zero-tolerance
outward-face contract is unchanged.

## Focused preflight and freeze

All preflight work completed before real selector call 1:

- 42 focused/synthetic tests passed;
- strict crossing, no crossing, endpoint zero, nonpositive endpoint, liquid
  faces, nonunique root, root-function failure, out-of-interval result, root-
  recomputed controls and no-average behavior were covered;
- existing lower-a repair, Option A derivative/F-order adapter, receipt-ordering,
  corrected D1-D3 contract and tiny-panel tests passed;
- `py_compile` passed for the complete corrected-diagnostic Python namespace;
- `git diff --check` passed;
- D2 generator, boundary, cost and contracts were byte-unchanged from baseline;
- exact input/grid/hash/F-order checks passed.

The synthetic Cell 5 preflight used zero selector evaluations and one separately
reported synthetic Z-root invocation.  It reproduced

`q_b*=0.012500213882917605`

with `ROOT_CONVERGED` and confirmed

`0.012481806039037598 < q_b* < 0.02256028269097067`.

Before real call 1, the driver persisted hashes for the full corrected-diagnostic
namespace and all changed/relevant focused tests.  Post-execution readback gives
`matches_pre_execution_freeze=true`.  No scientific code or test was modified
after the freeze.

## Fresh 800-cell policy map

All 800 expected `cell_0000.json` through `cell_0799.json` receipts are present.
Every receipt reports `SELECTED_ADMISSIBLE`; no cell failed and no receipt was
reused from a prior run.

Map-level Z evidence:

| Measure | Value |
|---|---:|
| Z root invocations / persisted Z candidates | 206 |
| Z root status `ROOT_CONVERGED` | 206 |
| Selected Z policies | 42 |
| Z candidates at liquid faces | 0 |
| Z residual-bound violations | 0 |
| Maximum `abs(raw residual) / arithmetic bound` | `0.00675481957145365` |

Cell 5 selected the repaired active lower-a / zero-kink / liquid-Z policy:

- `q_b=0.012500213882917605`;
- bracket `[0.012481806039037598, 0.02256028269097067]`;
- endpoint drifts: forward `-0.009203423814039269`, backward
  `3.3967923469887262`;
- `q_a=0.011250192494625845` and
  `lambda_a=0.011250192494627533`;
- `c=8.944195389902259`, `l=0.6929663884478887`, `d=-0.0`,
  `cost=0.0`, consumed `g_b=0.0`, `g_a=0.0`;
- marker `INTERIOR_LIQUID_Z_ZERO_DRIFT_SWITCH` plus unchanged marker
  `ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERVAL_CANONICAL_MIN`.

The complete Cell 5 receipt is `cell_0005.json`, 35,309 bytes, SHA-256
`7D6537B523FC96006E3B8CD310F2908D8090CE03D279D5E9330ED30E13E59730`.

## D2 gate

D2 was assembled exactly once after all 800 cells passed.  Its receipt status is
`PASS`:

- minimum off-diagonal `0.2642984748447064`;
- diagonal construction error exactly `0.0`;
- `max_abs(Q*1)=3.552713678800501e-15` against prospective bound
  `5.222144858126786e-14`;
- b-coordinate and a-coordinate action checks both passed with zero violations;
- D2 artifact SHA-256
  `093E1AF1ADFEEE5C50D3DD91EDDD678EBAC5BBA6C42E64DE73A63B82102AF1D5`.

No outward face drift was repaired by tolerance.

## One direct HJB step

The single authorized solve used `scipy.sparse.linalg.spsolve` and returned
`PASS`:

- matrix shape `(800,800)`, `nnz=3118`;
- residual infinity norm `2.5875135367670055e-14`;
- normwise backward error `1.9727855630325988e-16`;
- `V1` SHA-256
  `5C410EBC329F08B37F941A783E7F2C84BFCDCB67C6E24118114BE8C55697F2E2`;
- arrays artifact SHA-256
  `28A27473A4C08CCD20550B9EDF1509BABB4D7D882A9429F7F54F55DE72083173`.

Without a second selector map, the persisted raw `V1` derivatives at historical
coordinates are:

| Historical cell | `(b,a,z)` index | `V1` | `p_b^B=p_b^F` | `p_a^B` | `p_a^F` |
|---:|---|---:|---:|---:|---:|
| 4 | `(19,19,0)` | `-2.1155832159789054` | `0.005935217957511304` | `0.0037577531744710183` | `0.0037577531744710183` |
| 8 | `(19,19,1)` | `-2.078051337405182` | `0.0036696751939198735` | `0.003101868441400142` | `0.003101868441400142` |
| 10 | `(19,18,0)` | `-2.1175609808075744` | `0.0059795435449576375` | `0.0038223546736416113` | `0.0037577531744710183` |

These are raw diagnostics only; no `V1` selector evaluation was performed.

## Scientific-call ledger

| Operation | Calls |
|---|---:|
| corrected policy maps | 1 |
| real selector evaluations | 800 |
| scalar root invocations, total | 442 |
| interior-Z roots | 206 |
| D2 assemblies | 1 |
| sparse direct HJB solves | 1 |
| selector evaluations on `V1` | 0 |
| nonlinear continuation | 0 |
| adverse-numerics retries | 0 |
| KFE / MATLAB / outer / firm / wage-return | 0 |
| GE / annual / shock / IRF / Results | 0 |

All ceilings were respected: selectors `800/800`, total roots `442/3144`,
interior-Z roots `206/2880`, D2 `1/1`, direct solves `1/1`.

## Evidence closure and interpretation boundary

The sealed manifest contains 810 entries totaling 13,963,843 bytes.  It covers
preflight, pre-execution freeze, 800 durable cell receipts, D2 artifacts and
receipt, direct-step artifacts and receipt, raw historical-coordinate diagnostics,
execution summary/ledger and post-freeze verification.

This result establishes one complete corrected Option A policy map, one passing
consumed-drift D2 assembly and one finite direct linear HJB step under the exact
frozen inputs.  It is not nonlinear HJB convergence, a corrected fixed point,
KFE admissibility, stationary equilibrium, production readiness, recalibration or
Results authority.  Results eligibility remains `FALSE`.

This Builder does not merge `main` and does not publish a successor task.  The
next gate, if any, is independent review of this candidate and its sealed
evidence.
