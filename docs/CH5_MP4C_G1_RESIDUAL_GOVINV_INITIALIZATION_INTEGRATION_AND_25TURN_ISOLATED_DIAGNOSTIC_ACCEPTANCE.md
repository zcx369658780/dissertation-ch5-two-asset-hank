# Chapter 5 MP4C G1 residual-GovInv initialization integration and 25-turn isolated diagnostic — Reviewer acceptance

Date: 2026-09-11

Reviewer verdict:

`G1_RESIDUAL_GOVINV_25TURN_FAIL_ACCEPTED__INITIAL_ALIGNMENT_VALID__UNCHANGED_RETURN_BOUND_CONTROLLER_RECREATES_GOVINV_OVERSHOOT__CONTROLLER_REDESIGN_REQUIRED`

Candidate accepted: `54b6736b0507bee44f433832415507c0bfb170fa`.

## Acceptance rationale

The candidate executed the exact authorized experiment: a separately named G1 diagnostic route used one pre-turn initialization observation, one At-only capital allocation, and then exactly one 25-turn trajectory under the frozen corrected-2018 contract. The source-faithful labor route remained active; normalized labor was not activated. No second trajectory, second initialization pass, beta cell, parameter tuning, scientific retry, steady-state production run, GE, annual, IRF, or Results call occurred.

G1 succeeded at the narrow question it was designed to answer: under diagnostic `beta_a=1`, all 31 provinces had initial private capital below Track-A target and `GovInv0=max(Ktarget-Kt_supply_initial,0)` aligned initial accounting firm capital exactly to target, with maximum identity error zero. Turn-1 median total-K/target was 1.0 versus the accepted G0 value 1.0032099909906587, so the historical `Ktarget + private K` duplication was removed.

The 25-turn evidence then falsified the idea that initialization alone resolves the capital instability. The unchanged historical controller produced 0/289/486 GovInv decrease/increase/hold actions across the trajectory, identical to accepted G0 totals. In turns 20-25, pooled total-K/target min/median/max was 1.3257022041568054 / 2.353363495591088 / 2.8512142917573127; median GovInv/target was 2.3503561274071445, while median private-K/target was only 0.0029186382400614363. Thus the late capital overshoot is again overwhelmingly GovInv-driven and is recreated after the correct residual initialization.

The selected-turn raw-ra lower/interior/upper counts matched G0 exactly, supporting the interpretation that the current return-bound controller reacts in essentially the same way after G1. The accepted evidence therefore identifies the unchanged GovInv controller—not the G1 accounting initialization—as the dominant remaining capital-side mechanism in this bounded diagnostic prefix.

This is an accepted FAIL scientific result. `FAIL` means the tested controller did not preserve the G1 improvement; it is not an implementation rejection.

## Scientific boundaries

HJB/KFE validity blockers remain separate. The trajectory had 50 finite nonconverged-but-continued HJB province-turn observations and all 775 KFE returns remained `DIAGNOSTIC_ONLY`. The asset bridge remains `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`. The G1 initializer is accepted only as a diagnostic successor mechanism, not as production calibration authority.

The evidence does not identify a replacement controller law or damping coefficient. In particular, no new controller may be selected by minimizing this trajectory's errors, no coefficient may be fitted to make convergence pass, and no production claim follows.

`Results eligibility=FALSE`.

## Next gate

A separate zero-science controller redesign/forensic task is warranted before any new trajectory. It should compare the historical clipped-return ±10% multiplicative controller with capital-target/residual, rate-target, and staged/hybrid alternatives; recover exact source timing and gate semantics; and present Owner decision points without implementing or tuning a replacement controller.
