# CH5 MP4C turn-2 黑龙江 F0063 negative liquid-derivative emergence forensic

Date: 2026-09-21

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Baseline: `c50465673ad34613e17ec3a4fba265bc79ff2924`

## Terminal

`PASS__TURN2_HEILONGJIANG_F0063_NEGATIVE_DERIVATIVE_FORENSIC__EXACT_DIRECT_SOLVE_TRANSIENT_NONMONOTONICITY_CONFIRMED__NO_CODE_CHANGE`

Classification:

`CHECKPOINT2_TO_3_ACCEPTED_DIRECT_SOLVE_EXACTLY_INTRODUCED_FIRST_NEGATIVE_LIQUID_SLOPES__NO_SERIALIZATION_OR_ARITHMETIC_INCONSISTENCY`

The first negative raw liquid slope is created by the accepted checkpoint2-to-checkpoint3 implicit direct solve. It was absent from native/checkpoint0, checkpoint1 and checkpoint2. The persisted next-value, derivative receipt, residual and failed-cell receipts form one exact identity chain. No implementation repair is proposed.

## Identity chain

Accepted run004 manifest:

`1C501CEF7740748805CF538A05ECF9D80938149CDDF31A3158091F665C45AD80`

All relevant artifacts match their manifest entries. The value chain is:

| State | V SHA-256 |
|---|---|
| native / checkpoint0 | `7BEDB2FD4BA8DEA72095DE1F44FF6F12AF4B9008809501B7925CEC612CB0B575` |
| checkpoint1 | `74913F05A786569C62C6DD309F97B87F98AEDDC1474EB1AFAADE13D36E294E32` |
| checkpoint2 | `2C6D5FCBA2FDF64805CBE9AA9C6E414C395F1D3CB246F57278C7AD4BEEF4DEDA` |
| checkpoint3 | `1FA95217C9EEFDAA638F0CD07F00B59B053EB4A59E5670A0CED94852922DBFE7` |

Native V is bitwise identical to checkpoint0 V. Each checkpoint `n` direct-update `next_value` is bitwise identical to checkpoint `n+1` V. Checkpoint2 `next_value` equals the checkpoint3 derivative receipt's V identity.

The independently reconstructed four derivative-field hashes match every checkpoint0/1/2/3 derivative receipt exactly. Reconstructed F0062/F0063 derivatives also match the persisted cell JSON floating-point values exactly.

## Liquid derivative sign census

Native and checkpoint0 are the same state, so the table contains four unique V states.

### Interior liquid cells

| State | `(+,+)` | `(<=0,+)` | `(+,<=0)` | `(<=0,<=0)` | negative b-edges | first affected flat |
|---|---:|---:|---:|---:|---:|---:|
| native / checkpoint0 | 720 | 0 | 0 | 0 | 0 | none |
| checkpoint1 | 720 | 0 | 0 | 0 | 0 | none |
| checkpoint2 | 720 | 0 | 0 | 0 | 0 | none |
| checkpoint3 | 716 | 2 | 2 | 0 | 2 | 62 |

At every state, all 40 lower-b cells and all 40 upper-b cells are `(+,+)`.

Checkpoint3 minimums:

- minimum `p_b^B=-0.0002428532863339202` at flat 63, index `(3,3,0)`;
- minimum `p_b^F=-0.0002428532863339202` at flat 62, index `(2,3,0)`;
- maximum negative magnitude: `0.0002428532863339202`;
- negative derivative representations: 4, produced by 2 distinct negative grid edges.

The two negative edges are both between b indices 2 and 3:

- `a_index=3, z_index=0`: `-0.0002428532863339202`;
- `a_index=4, z_index=0`: `-0.00020081807822456922`.

## F0062/F0063 trajectory

The common slope between F0062 and F0063 evolves as follows:

| State | `V62` | `V63` | `V63-V62` | shared slope |
|---|---:|---:|---:|---:|
| checkpoint0 | `-3.0698905276020465` | `-3.058452329557571` | `0.011438198044475545` | `0.031046537549290782` |
| checkpoint1 | `-2.5615161279799237` | `-2.5536412765223564` | `0.007874851457567278` | `0.021374596813396908` |
| checkpoint2 | `-2.312540903990399` | `-2.3057753720485175` | `0.006765531941881342` | `0.018363586699392222` |
| checkpoint3 | `-2.290136398297297` | `-2.290225870560683` | `-0.00008947226338618108` | `-0.0002428532863339202` |

The gap narrows in the first two updates but remains positive. Update 2→3 changes it by `-0.006855004205267523` and flips its sign.

At checkpoint2:

- F0062 selected `q_b=0.01769496075403763`, `g_b=-0.33805498098430536`;
- F0063 selected `q_b=0.019060841477612046`, `g_b=0.2280802231505044`.

The persisted policies therefore point away from their shared b interface: row 62 uses the left b neighbor and row 63 uses the right b neighbor.

## Direct-solve attribution

For all three persisted updates:

- `next_value`, RHS and saved-residual hashes match their direct-solve receipts;
- independently recomputed CSR residual is bitwise identical to the saved residual;
- the recomputed scalar norms agree with receipts within the prospective 8-epsilon scaled arithmetic bound;
- each `next_value` is bitwise identical to the next checkpoint state.

For checkpoint2→3:

- residual infinity norm: `1.2961853812498703e-14`;
- denominator: `104.12921737761056` in the persisted receipt;
- normwise backward error: `1.2447854827809075e-16`;
- accepted inclusive bound: `1e-12`;
- warnings: none.

Local row reconstruction uses only the persisted CSR matrix, RHS and solution:

- row 62 residual: approximately `1.30e-15`;
- row 63 residual: approximately `-8.33e-16`;
- diagonal rearrangement reproduces V62 within `4.44e-16` and V63 exactly;
- neither row contains the other side of the F0062/F0063 interface.

Thus the accepted sparse equations themselves produce `V63<V62`. The negative slope is neither a serialization difference nor a derivative-reconstruction inconsistency. It is an exact transient non-monotonicity of the persisted accepted direct-solve iterate.

This attribution does not establish that the iteration law should change. Any damping, monotonicity preservation, matrix redesign, or other repair requires a separate scientific-design authority.

## Zero-science ledger

- persisted NPZ loads: 19
- persisted JSON loads: 14
- accepted artifact SHA-256 reads: 16
- independent derivative reconstructions: 15
- independent full CSR matvecs: 3
- independent local sparse-row attributions: 2
- production derivative helper, selector and root helper calls: all 0
- HJB/direct-update executions and new linear solves: 0
- D2/Q rebuild, KFE/SVD, aggregate/integration: all 0
- turn2 replay/rerun, turn3, MATLAB, retry/tuning and scientific model calls: all 0

Focused tests: `4 passed`.

## Evidence

Evidence root:

`reports/ch5_mp4c_turn2_heilongjiang_f0063_negative_derivative_emergence_forensic_20260921_run001/`

The root contains the artifact chain, exact derivative parity, full census, local trajectory, residual identity, sparse-row attribution, classification, ledger, focused test receipt, sealed manifest and independent readback.
