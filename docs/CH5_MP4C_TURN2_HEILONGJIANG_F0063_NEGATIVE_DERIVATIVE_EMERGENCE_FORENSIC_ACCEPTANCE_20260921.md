# Chapter 5 turn-2 黑龙江 F0063 negative liquid-derivative emergence forensic — Reviewer acceptance

Date: 2026-09-21

Verdict:

`ACCEPTED_PASS__F0063_NEGATIVE_LIQUID_SLOPE_IS_EXACT_CHECKPOINT2_TO_3_DIRECT_SOLVE_TRANSIENT__NO_ARTIFACT`

Accepted terminal:

`PASS__TURN2_HEILONGJIANG_F0063_NEGATIVE_DERIVATIVE_FORENSIC__EXACT_DIRECT_SOLVE_TRANSIENT_NONMONOTONICITY_CONFIRMED__NO_CODE_CHANGE`

Accepted classification:

`CHECKPOINT2_TO_3_ACCEPTED_DIRECT_SOLVE_EXACTLY_INTRODUCED_FIRST_NEGATIVE_LIQUID_SLOPES__NO_SERIALIZATION_OR_ARITHMETIC_INCONSISTENCY`

Results eligibility remains `FALSE`.

## Independent Git review

- baseline: `c50465673ad34613e17ec3a4fba265bc79ff2924`
- candidate: `892b3ca9a40bb97b2390dedcab5d7bcd99ca0c21`
- tree: `18a8a426fde5f6fb70885369a2f9fec6b54fb86c`
- ancestry: 1 ahead / 0 behind
- merge-base: exact baseline
- changed paths: 18
- production `src/ch5_two_asset_hank/**`: 0 changes
- CURRENT: 0 changes
- remote candidate SHA/tree: exact.

All changed paths are the authorized forensic report, validator/test and fresh evidence root.

Focused tests: 4/4 PASS.

## Accepted identity chain

The accepted run004 manifest remains exact:

`1C501CEF7740748805CF538A05ECF9D80938149CDDF31A3158091F665C45AD80`

For 黑龙江:

- native / checkpoint0 V:
  `7BEDB2FD4BA8DEA72095DE1F44FF6F12AF4B9008809501B7925CEC612CB0B575`
- checkpoint1:
  `74913F05A786569C62C6DD309F97B87F98AEDDC1474EB1AFAADE13D36E294E32`
- checkpoint2:
  `2C6D5FCBA2FDF64805CBE9AA9C6E414C395F1D3CB246F57278C7AD4BEEF4DEDA`
- checkpoint3:
  `1FA95217C9EEFDAA638F0CD07F00B59B053EB4A59E5670A0CED94852922DBFE7`.

Native V is bitwise identical to checkpoint0. Each persisted direct-update `next_value` is bitwise identical to the next checkpoint state. Checkpoint2 `next_value` exactly matches the checkpoint3 derivative-receipt V identity.

All independently reconstructed derivative-field hashes match the persisted checkpoint0/1/2/3 derivative receipts.

F0062 and F0063 reconstructed derivative values match the persisted cell JSON values exactly.

## Four-iterate liquid derivative census

Native/checkpoint0, checkpoint1 and checkpoint2 contain no nonpositive raw liquid derivative.

Interior-b sign counts:

| V state | (+,+) | (<=0,+) | (+,<=0) | (<=0,<=0) |
| --- | ---: | ---: | ---: | ---: |
| native/checkpoint0 | 720 | 0 | 0 | 0 |
| checkpoint1 | 720 | 0 | 0 | 0 |
| checkpoint2 | 720 | 0 | 0 | 0 |
| checkpoint3 | 716 | 2 | 2 | 0 |

All lower-b and upper-b boundary cells remain (+,+) at all four states.

Checkpoint3 contains exactly two distinct negative b-grid edges, represented four times in backward/forward derivative fields.

The first affected F-order flat is 62.

The most negative edge is:

`-0.0002428532863339202`

shared by F0062/F0063.

## Exact F0062/F0063 trajectory

Shared F0062→F0063 liquid slope:

- checkpoint0: `0.031046537549290782`
- checkpoint1: `0.021374596813396908`
- checkpoint2: `0.018363586699392222`
- checkpoint3: `-0.0002428532863339202`.

The value gap:

`V63-V62`

evolves:

- checkpoint0: `0.011438198044475545`
- checkpoint1: `0.007874851457567278`
- checkpoint2: `0.006765531941881342`
- checkpoint3: `-0.00008947226338618108`.

For update 2→3:

- V62 increment: `0.022404505693101928`
- V63 increment: `0.015549501487834405`
- gap change: `-0.006855004205267523`.

Thus the first mixed/nonpositive liquid derivative is introduced exactly by the accepted checkpoint2→3 update.

## Direct-solve attribution

For all three accepted direct updates, independently recomputed CSR residuals are bitwise identical to the saved residual arrays and all persisted identity hashes match.

Checkpoint2→3:

- residual infinity norm:
  `1.2961853812498703e-14`
- normwise backward error:
  `1.2447854827809075e-16`
- accepted bound:
  `1e-12`
- solver warnings: none.

Local persisted sparse-row reconstruction gives:

- row 62 implied V matches actual within `4.44e-16`;
- row 63 implied V matches actual exactly;
- neither matrix row couples across the F0062/F0063 shared b interface.

At checkpoint2 the selected consumed liquid drifts are:

- F0062: `g_b=-0.33805498098430536`
- F0063: `g_b=+0.2280802231505044`.

The selected transport therefore points away from the shared interface on both sides, so the accepted implicit equations independently update the two neighboring values and invert their ordering.

The negative slope is therefore not:

- a serialization mismatch;
- a hash/identity mismatch;
- a finite-difference implementation mismatch;
- a linear-solve accuracy failure.

It is an exact transient non-monotonicity of the accepted full implicit HJB update under the frozen checkpoint2 policy/operator.

## Scientific consequence

The selector remains correct to fail closed at checkpoint3 because q_b must be positive and the one-sided extrapolation route has already been rejected.

The unresolved issue has moved upstream from derivative selection to the nonlinear HJB update law.

The existing Owner convergence authority freezes:

- `Delta=1000`;
- full implicit update;
- no damping/relaxation;
- no adaptive Delta;
- no line search;
- no clipping/artificial diffusion.

Therefore any attempt to preserve positive liquid slopes across the nonlinear update is a new scientific/numerical-law question and cannot be implemented as a local engineering repair.

## Zero-science integrity

Accepted ledger:

- persisted NPZ loads: 19
- persisted JSON loads: 14
- independent derivative reconstructions: 15
- independent full CSR matvecs: 3
- independent local sparse rows: 2
- production derivative helper: 0
- production selector/root helper: 0
- HJB/direct update execution: 0
- new linear solves: 0
- D2/Q rebuild: 0
- KFE/SVD: 0
- aggregate/integration: 0
- turn2 replay/rerun: 0
- turn3: 0
- MATLAB: 0
- retry/tuning: 0
- scientific model calls: 0.

## Evidence integrity

Evidence root:

`reports/ch5_mp4c_turn2_heilongjiang_f0063_negative_derivative_emergence_forensic_20260921_run001/`

- manifest SHA-256:
  `086C6DE48DFF65A2B2B338CB01CFAAB201489575147E9145F73BF8E629B6D165`
- entries: 12
- bytes: 49,285
- independent readback: PASS
- bad paths: none.

## Reviewer decision

The forensic candidate is accepted.

No numerical repair is adopted.

A successor scientific design gate may now examine whether a monotonicity-preserving convex relaxation of the accepted implicit update can preserve the model's positive liquid marginal-value domain without changing the fixed-point equations.

No implementation or HJB rerun is authorized until that design is independently accepted and, if it changes the frozen iteration law, separately adopted by Owner.
