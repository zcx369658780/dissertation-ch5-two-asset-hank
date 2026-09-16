# CH5 MP4C 2018 KFE D1-D3 V1 policy remap and Q1 recurrent-topology diagnostic

Date: 2026-09-16

Task: `CH5_MP4C_2018_KFE_D123_V1_POLICY_REMAP_AND_Q1_RECURRENT_TOPOLOGY_DIAGNOSTIC_20260916`

## Verdict

`PASS__V1_COMPLETE_POLICY_MAP__Q1_SINGLE_CLOSED_CLASS__Q0_TWO_SINKS_DO_NOT_PERSIST`

The accepted V1 was loaded once and remapped through the unchanged corrected
selector. All 800 cells returned durable `SELECTED_ADMISSIBLE` receipts. Q1
then passed the unchanged zero-tolerance D2 contract and its exact-positive
graph has one closed communicating class, with members
`[5,6,405,406]`.

The four Q0 recurrent coordinates all remain recurrent in Q1, but they no
longer form two separate exact-zero sinks. At flat 405 the V1 policy switches
from Z to a forward-liquid directional policy with `g_b>0`; at flat 6 it
switches from Z to a backward-liquid directional policy with `g_b<0`. These
two new liquid edges connect the former Q0 classes into one four-state closed
class. Flats 5 and 406 retain Z and exact zero asset drift.

This is a one-step policy/operator topology diagnostic. It is not HJB
convergence, a KFE stationary-mass result, a joint HJB-KFE fixed point,
economic equilibrium, production authority, or Results evidence.

## Authority and input binding

- fresh-fetched baseline: `83b25a428e9ee4c622690a43b55f17a2e6a7cf50`;
- accepted arrays artifact SHA-256:
  `28A27473A4C08CCD20550B9EDF1509BABB4D7D882A9429F7F54F55DE72083173`;
- accepted V1 field SHA-256:
  `5C410EBC329F08B37F941A783E7F2C84BFCDCB67C6E24118114BE8C55697F2E2`;
- V1 shape/order: `(20,20,2)`, F-order, b fastest;
- accepted grid field hashes, frozen call-725 scalars, productivity generator,
  selector, derivative adapter and D2 generator identities all passed
  preflight;
- the selector, D2 law, grid, calibration and accepted artifact were not
  modified.

## Complete policy map and Q1 D2

The fresh map completed 800/800 cells. It used 408 scalar roots, including
160 interior-Z roots; 40 selected policies used Z and 760 selected a
directional liquid branch. No retry occurred.

Q1 D2 was assembled exactly once after the complete map. All required checks
passed:

- minimum offdiagonal: `0.016508228132885275`;
- diagonal construction error: exactly `0.0`;
- `max_abs(Q1 @ 1)`: `2.220446049250313e-15`;
- prospective row-sum bound: `2.976424297233587e-14`;
- b-coordinate action violations: `0`;
- a-coordinate action violations: `0`;
- lower/upper b and a outward drift, rate and flux: exactly `0.0`;
- no clipping, tolerance tuning, edge repair or artificial diffusion.

Persisted Q1 artifact:

- path: `q1_generator.npz`;
- bytes: `23,773`;
- SHA-256:
  `5F96C2CFAAFB3EA7EF32943A892A9191FEDCC5DBC7AB28D066F5893D3F560D1E`.

## Q0 versus Q1 recurrent topology

| Metric | accepted Q0 | Q1 |
|---|---:|---:|
| exact-positive edges | 2,318 | 2,307 |
| SCC count | 400 | 155 |
| condensation edges | 759 | 289 |
| closed classes | 2 | 1 |
| closed membership | `[5,405]`, `[6,406]` | `[5,6,405,406]` |
| transient states | 796 | 796 |

Q1 SCC sizes are: 131 SCCs of size 2, 11 of size 4, and 13 of size 38.
All 155 SCCs and all 800 states can reach the single closed class. Therefore
the applicable reachability partition is one category, `C0`; an A/B basin
partition is no longer applicable. There are no asset-grid category
separatrices under this single downstream reachability category.

## Required prior-coordinate comparison

| flat | `(i_b,i_a,i_z)` | `(b,a,z)` | Q1 status | policy change | `g_b` | `g_a` | both zero? |
|---:|---|---|---|---|---:|---:|---|
| 5 | `(5,0,0)` | `(-0.1578947368421053,0,0.8)` | recurrent | no; Z remains | `0.0` | `0.0` | yes |
| 405 | `(5,0,1)` | `(-0.1578947368421053,0,1.3)` | recurrent | Z -> forward directional | `4.13792238700476` | `0.0` | no |
| 6 | `(6,0,0)` | `(0.2105263157894739,0,0.8)` | recurrent | Z -> backward directional | `-1.9752164611482765` | `0.0` | no |
| 406 | `(6,0,1)` | `(0.2105263157894739,0,1.3)` | recurrent | no; Z remains | `0.0` | `0.0` | yes |

Thus none of these coordinates becomes transient. The topology change occurs
because flats 405 and 6 cease to have simultaneous zero asset drift and add
oppositely directed liquid transitions across the adjacent b nodes.

## Single Q1 recurrent class: policies and complete outgoing rates

All four states retain active `lower_a`, transfer branch `zero_kink`,
`a=forward`, `g_a=0.0`, `d=-0.0`, `cost=0.0`, and the accepted lower-a
minimum-feasible-shadow marker.

### Flat 5: `(5,0,0)`, `(-0.1578947368421053,0,0.8)`

- branch: `INTERIOR_Z_ZERO_LIQUID_SWITCH`; derivatives `b=zero`, `a=forward`;
- `q_b=0.012500213882917608`, `q_a=0.011250192494625848`;
- `c=8.944195389902259`, `l=0.6929663884478887`;
- `g_b=0.0`, `g_a=0.0`;
- outgoing: `5 -> 405` productivity switch at `0.3333333333333333`;
- diagonal: `-0.3333333333333333`.

### Flat 405: `(5,0,1)`, `(-0.1578947368421053,0,1.3)`

- branch: directional; derivatives `b=forward`, `a=forward`;
- `q_b=0.008720537785666562`, `q_a=0.007848484007099905`;
- `c=10.70849321636963`, `l=0.7105718656598194`;
- `g_b=4.13792238700476`, `g_a=0.0`;
- outgoing: `405 -> 5` productivity switch at `0.3333333333333333` and
  `405 -> 406` positive-b transition at `11.231503621870056`;
- diagonal: `-11.56483695520339`.

### Flat 6: `(6,0,0)`, `(0.2105263157894739,0,0.8)`

- branch: directional; derivatives `b=backward`, `a=forward`;
- `q_b=0.009219646889686503`, `q_a=0.008297682200717853`;
- `c=10.414606273678`, `l=0.6520359466096006`;
- `g_b=-1.9752164611482765`, `g_a=0.0`;
- outgoing: `6 -> 5` negative-b transition at `5.361301823116747` and
  `6 -> 406` productivity switch at `0.3333333333333333`;
- diagonal: `-5.69463515645008`.

### Flat 406: `(6,0,1)`, `(0.2105263157894739,0,1.3)`

- branch: `INTERIOR_Z_ZERO_LIQUID_SWITCH`; derivatives `b=zero`, `a=forward`;
- `q_b=0.00545307214084189`, `q_a=0.004907764926757701`;
- `c=13.541893014759237`, `l=0.6468857778838657`;
- `g_b=0.0`, `g_a=0.0`;
- outgoing: `406 -> 6` productivity switch at `0.3333333333333333`;
- diagonal: `-0.3333333333333333`.

The complete 155-node condensation DAG, SCC membership, reachability sets,
four recurrent-state policy receipts and all recurrent outgoing rates are
persisted in `q1_topology.json`.

## Scientific ledger and verification

| Operation | Calls |
|---|---:|
| V1 artifact load | 1 |
| corrected policy map | 1 |
| real selector evaluations | 800 |
| scalar roots total | 408 |
| interior-Z roots | 160 |
| Q1 D2 assembly | 1 |
| graph audit | 1 |
| SCC decomposition | 1 |
| condensation/reachability | 1 |
| retries | 0 |
| HJB direct/nonlinear continuation, V2 | 0 |
| KFE/nullspace/SVD/eigen/stationary mass, `Q1.T @ p` | 0 |
| row replacement/pin/source RHS | 0 |
| MATLAB/downstream/Results | 0 |

- focused tests before execution: `23 passed`;
- task module/test `py_compile`: PASS;
- pre-execution `git diff --check`: PASS;
- scientific-code freeze readback: exact match;
- scientific run wall time: `10.0257714000763` seconds;
- sealed manifest: 808 entries, 14,117,850 bytes;
- `q1_topology.json` SHA-256:
  `4FDD25E33E2D1025849370391D43CE65F925859DAB4A4E97BDE28784D658E86D`;
- `q1_d2_receipt.json` SHA-256:
  `EDE6EED10F4558BA4D902CC3AA9FDED7E23D961D997C12DE8E3654DC2990085A`;
- sealed manifest SHA-256:
  `573FCF61220E5982EB4A6E78FAFC5D82310BAC7F7638D2D83B576B1420DDCF37`.

## Boundary

Q1 has a unique closed graph class after one accepted V1 remap, and the two
separate Q0 sinks do not persist. This does not authorize a stationary-mass
solve, further HJB iteration, V2, production replacement, paper Results, a
successor task, or an interpretation as economic equilibrium uniqueness.
