# CH5 MP4C 2018 KFE D1-D3 joint switching implementation and checkpoint-2 acceptance

Date: 2026-09-19

Reviewer verdict:

`PASS__JOINT_SWITCHING_IMPLEMENTATION_ACCEPTED__V2_MAP_COMPLETE__Q2_D2_PASS__CHECKPOINT2_NONCONVERGED__BOUNDED_NONLINEAR_CONTINUATION_AUTHORIZED`

## Accepted candidate

- baseline live main before task: `0033e61b7bfbb3080c1aeac43b66a78d669d4571`
- Builder candidate: `62d01dac0eb1e516386cf6336837b5a2ef4463e5`
- candidate tree: `98f21a0973cc24197c9368ba948268bdfd1064ba`
- candidate chain is exactly `2 ahead / 0 behind` baseline
- focused engineering gate: `64/64` passed
- source-faithful/production paths, D1/D2/D3 equations, grid, calibration, solver/tolerances and convergence law remain unchanged
- Results eligibility remains `FALSE`

## L3 acceptance of the adopted joint law implementation

The Owner-adopted simultaneous two-axis zero-drift switching law is implemented consistently with its scientific authority.

The exact cell185 joint candidate is accepted:

- `q_b=0.0118331456615342`
- `q_a=0.00852012060113076`
- `d_ZZ=-0.42626460578345887`
- raw `g_b=3.33066907387547e-16`, raw `g_a=0`
- canonical `g_b=g_a=0`
- transfer-KKT residual `0`
- D2 assembler admissible `true`
- selector outcome `SELECTED_ADMISSIBLE`.

The full accepted-V2 policy map completes all 800 cells. Joint policies are selected at flat indices `185` and `205`. One-axis interior-`a` behavior remains valid and is selected at flat indices `100`, `120`, and `140`. The implementation preserves one-axis liquid-`Z`, lower-`a` zero-kink and boundary laws.

## Accepted complete checkpoint 2

Accepted V2 field SHA-256:

`A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.

Accepted same-value checkpoint-2 identities:

- P2 identity: `EBCBABC0593EF163D2E7FA300F6FFEB6E3C187D232D4CCEA5D59AB7180CD1D95`
- u2 SHA-256: `C222F4B147F48EA177A28AAF289F3ED5EA76F531BC08201070DD63698BF98D73`
- Q2 artifact SHA-256: `346DBCDA13392DAF6897DC185767B0E7C5961AA76A9AAA686053AEDA33C02F9F`
- Q2 data/indices/indptr identities:
  - `3278FFDA5ABA29E8C8E7ECC84649DF7A787AD7BDA5E936657F585B65A9844BEB`
  - `6FF05054740279B563416E942AFEC958804FBD1AF63C660C9877D3175FB5B066`
  - `180A552000B935F15F1934266DE86FF9E3D7550005366AB92B312793648F0200`
- full checkpoint-2 identity: `71DC6975E814060A4F63961A736E6E9DDF766C51CE4672C3EF777E5E15B80C2C`
- checkpoint arrays artifact SHA-256:
  `F55C1A37BF16720AA1BC61DC4BA42A410BD9DCA5399A2C38EC19D2AE295B8612`.

D2 is accepted as PASS:

- minimum off-diagonal `1.5861421037712475e-08`
- diagonal construction error `0`
- `max(abs(Q2 @ 1))=1.7763568394002505e-15`
- zero outward closed-face violations.

The sealed evidence manifest has `816` verified entries, zero mismatch, SHA-256:

`B3CC70792E41E0EBDDE138057406C86D07063AD44959B595FA1B503B9D5AE2EA`.

## Nonlinear checkpoint-2 classification

The Owner primary convergence law is not satisfied:

- `B2=0.006582827785543588 > 1e-8`
- `D2=0.05439336697877817 > 1e-7`.

Therefore checkpoint 2 is complete and scientifically usable for continuation, but is not an HJB convergence candidate.

Policy/operator changes remain diagnostic only. The large Q2-Q1 difference does not override the primary law.

No exact cycle is established. Approximate period-2/3 windows are not yet available at checkpoint 2.

## Scientific ledger accepted

The scientific ledger is accepted exactly as persisted:

- accepted V1/V2/Q1 loads: `1/1/1`
- one V2 policy map: `1`
- selector evaluations: `800`
- total scalar roots: `383`
- liquid-`Z` roots: `157`
- one-axis interior-`a` roots: `2`
- joint roots: `2`
- Q2/D2 assemblies: `1`
- checkpoint-2 evaluations: `1`
- HJB solves / V2->V3 updates: `0/0`
- topology/KFE/SVD/eigen/nullspace/`Q.T@p`: `0`
- scientific retries / solver substitutions: `0/0`
- damping/relaxation/adaptive Delta/continuation: `0`
- MATLAB/production/GE/downstream/Results: `0`.

## Successor authority

No new economic/scientific law is required to continue from checkpoint 2.

The Owner-adopted nonlinear convergence law already authorizes continuation with fixed `Delta=1000`, direct-solve backward error `<=1e-12`, exact-cycle stopping and approximate period-2/3 stopping.

Reviewer therefore authorizes one bounded nonlinear continuation successor beginning from the exact accepted V2/P2/u2/Q2 checkpoint.

The successor may perform up to four new updates, `V2->V3->V4->V5->V6`, stopping immediately on:

- primary convergence;
- direct-solve accuracy failure;
- first policy-map/D2 failure;
- exact cycle;
- authorized approximate period-2/3 cycle;
- provenance/nonfinite failure.

This four-update horizon is intentionally sufficient to make the complete approximate period-2 window available and, if all checkpoints through 6 exist, the complete approximate period-3 window available.

No terminal KFE/topology work is authorized in the continuation task itself.
