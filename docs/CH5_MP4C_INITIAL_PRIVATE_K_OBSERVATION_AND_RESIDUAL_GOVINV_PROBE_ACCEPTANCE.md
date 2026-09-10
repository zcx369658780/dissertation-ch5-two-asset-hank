# Chapter 5 MP4C initial private-K observation and residual-GovInv probe — Reviewer acceptance

Date: 2026-09-11

Reviewer verdict:

`INITIAL_PRIVATE_K_RESIDUAL_GOVINV_PROBE_ACCEPTED__G1_ACCOUNTING_VALIDATED_UNDER_DIAGNOSTIC_BETA1__SUCCESSOR_RUNTIME_INTEGRATION_AUTHORIZED`

Accepted candidate: `8df20bef54618487664ae16ea4dfe5639750cc3b`.

## Acceptance basis

The candidate is exactly one commit ahead of the authorized baseline `67172ba4cc761cdbbe2716dccc85b78c88b408e3`. The implementation respects the bounded one-pass contract: 31 household observations, 31 HJB returns, 31 KFE returns, 31 aggregates, and exactly one existing At-only capital allocation. Migration, normalized migration, firm, wage, GovInv controller, outer turn, steady state, MATLAB, GE, annual, IRF, and Results calls remain zero.

The probe reuses the accepted corrected-2018 runtime validator before science. Finite nonconverged HJB returns remain `HJB_NONCONVERGED_DIAGNOSTIC_ONLY`; all KFE returns remain `DIAGNOSTIC_ONLY`; `beta_a=1` remains `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`. Thus numerical observability of private K is not promoted to household/KFE/bridge scientific acceptance.

The G0/G1 accounting helper is pure and does not mutate runtime state. Under the observed beta=1 private capital vector, all 31 provinces satisfy private K below Track-A Ktarget. Therefore the candidate residual rule

`GovInv0_G1 = max(Ktarget - Kt_supply_initial, 0)`

makes initial accounting firm capital equal Track-A Ktarget in all 31 provinces, while historical G0 mechanically adds the positive private-K vector on top of the full target. National G0 overshoot equals the national observed private K exactly.

The reported private-K/target distribution is accepted as diagnostic evidence: min/median/mean/max `0.0009496604680542149 / 0.003209990990658578 / 0.005053897862873359 / 0.03486516202709419`. The beta-star distribution is also accepted only as bridge-sensitivity geometry, not as an estimate of `beta_a`.

For Anhui, the accepted receipt is internally consistent: private K `218901.27196706057 MU`, target `70182433.35888097 MU`, G0 ratio `1.003119032234857`, G1 residual GovInv `69963532.08691391 MU`, and G1 total-K ratio `1`.

## Scientific interpretation

This evidence is sufficient to authorize a separately named diagnostic successor initialization route using G1 under the still-diagnostic `beta_a=1` contract. It does not establish production GovInv calibration, public-capital identification, KFE/HJB validity, or Results eligibility.

Initialization and the historical return-bound GovInv controller remain separate objects. The next integration must change only initialization first and keep the controller frozen, so any trajectory effect is attributable.

## Boundary

Results eligibility remains `FALSE`. No production steady-state acceptance is granted. Any outer trajectory requires a new exact GitHub task and bounded scientific-call budget.
