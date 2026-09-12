# Chapter 5 MP4C K1 annual HJB G1 vs G2 price-guard continuation diagnostic acceptance

Date: 2026-09-12.

Reviewer verdict:

`ANNUAL_K1A_G1_VS_G2_PRICE_GUARD_CONTINUATION_DIAGNOSTIC_ACCEPTED__G2_REDUCES_RETURN_SATURATION_BUT_DEGRADES_HJB_CONVERGENCE_AND_AMPLIFIES_CONTROL_STRESS__DO_NOT_EXTEND_G2_OR_ENTER_G3__FOCUSED_HA_HJB_MECHANISM_DIAGNOSTIC_REQUIRED`

Accepted candidate:

`ab6b19022d920a8929a2ee66cc5511be6f602557`

## Scope accepted

The candidate is accepted as the bounded 5-turn continuation comparison authorized by `CH5_MP4C_K1_ANNUAL_HJB_G1_VS_G2_PRICE_GUARD_CONTINUATION_DIAGNOSTIC`. Relative to baseline `b5ba365d0e21329d81828c466fcc7010a429aa09`, it changes only task-bounded runner/finalizer/tests/report/compact evidence. No production scientific equation, annual calibration, capital-network formula, HJB/KFE equation, boundary/KKT law, C1, labor science, grid, tolerance, solver semantics, K1B/K2 or Results authority is changed.

## Accepted evidence

1. G1 and G2 both completed the authorized 5/5 turns with zero scientific retries, no NaN/Inf hard stop, no provenance failure, no same-turn return feedback, and accepted K1/C1 accounting closure.
2. Turn 1 is exactly equivalent. The treatment difference begins only at turn 2 through the HJB-interface return guard.
3. G1 remains fully upper-saturated over treatment turns: `124/124` return hits and no unsaturated province-turns.
4. G2 materially reduces return saturation to `84/124` upper hits and restores `40/124` unsaturated province-turns; HJB-consumed return variation reappears with distinct counts `14,10,10,10` over turns 2-5.
5. Despite restoring variation, G2 worsens treatment HJB convergence from G1 `18/124` to G2 `6/124`, with G2 turn 5 at `0/31` converged. Therefore relaxed return variation is not currently numerically admissible as an automatic longer-horizon scaffold.
6. Several G2 control/drift extrema increase sharply. In particular, turn-2 adjustment-cost/illiquid-drift extrema rise from roughly `6.52e12` under G1 to `1.92e14` under G2, and liquid-drift/transfer extrema from roughly `6.68e6` to `4.27e7`. The pattern is not uniform across every turn, but it is sufficient to reject a monotone-stability claim.
7. The wage safeguard remains highly binding while held fixed: G1 `112/124` and G2 `109/124` treatment province-turn wage hits. This confirms that wage-bound usage must remain a first-class numerical diagnostic, but this task does not authorize wage-bound relaxation.
8. Same-S quantity/payoff identity, own-prior return provenance, source-faithful labor, capital conservation and C1 accounting remain accepted in this bounded comparison.
9. All KFE results remain `DIAGNOSTIC_ONLY`; finite-box upper-b leakage and MATLAB-style pinning remain independent blockers.

## Route decision

Do not run longer G2 and do not enter G3/G4. G2 demonstrates that merely widening the return safeguard restores heterogeneity but moves the HA/HJB block into a substantially less convergent and more stressed regime. The next gate is therefore a focused HA/HJB mechanism diagnostic using the already persisted G1/G2 evidence before any further continuation step.

The diagnostic must determine where the G1->G2 convergence loss and control/drift amplification arise: which provinces, turns, grid cells, policy branches, value derivatives, transfer-FOC states and boundary/interior regimes change when the return cap widens. It must also distinguish return-guard effects from the still-binding legacy wage safeguard.

No G3, wage relaxation, longer-horizon provisional steady-state run, K1B, K2, KFE upgrade or Results upgrade is authorized by this acceptance.

Results eligibility remains `FALSE`.
