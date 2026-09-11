# Reviewer Acceptance — C1 GovInv Residual Level Replacement

Date: 2026-09-11

Reviewer verdict:

`C1_GOVINV_RESIDUAL_LEVEL_REPLACEMENT_ACCEPTED__PURE_PUBLIC_ASSET_RESIDUAL_IMPLEMENTED__STATIC_G1_REPLAY_FULLY_CLOSES_HISTORICAL_GOVINV_OVERSHOOT__BOUNDED_RUNTIME_INTEGRATION_AUTHORIZED`

Accepted candidate:

`77c17f224c466720b4c7e67250513817f584d1f8`

## Reviewer finding

The candidate is accepted.

The implementation adds a separately named pure public-asset residual contract without modifying the historical C0 controller or connecting the new logic to active steady-state execution. The scalar and 31-province APIs implement exactly:

`GovInv = max(Ktarget - Kprivate_current, 0)`

with no gain, return target, damping, hysteresis, or other tuning parameter.

For private capital below target, accounting firm capital closes exactly to `Ktarget`. For private capital at or above target, the public-asset residual is floored at zero and the private-capital overshoot remains explicit. Invalid/nonfinite targets, negative/nonfinite private capital, province-order mismatch, and shape mismatch fail closed.

The Reviewer independently inspected `src/ch5_two_asset_hank/multi_province/government_assets.py` and confirmed that the contract is deterministic, stock-unit consistent, and unconnected to model runtimes.

## Static accepted-G1 replay

The accepted G1 25-turn ledger is used only as immutable historical input; no science is rerun.

The static C1 replacement closes 775/775 accepted province-turn observations exactly to Ktarget because private productive capital remains below target in all rows. In turns 20–25, the historical total-K/target median of `2.353363495591088` becomes exactly `1.0` under static residual replacement. The pooled historical late-window GovInv-driven positive overshoot amount `19,963,597,940.767487 MU` is mechanically removed in the static accounting replay, with `0 MU` remaining private-only overshoot in those saved observations.

This is accounting counterfactual evidence, not a dynamic stability result.

## Legacy authority preservation

The source-faithful/historical C0 controller remains byte-identical at the recorded SHA-256 and is not overwritten. The accepted C1 helper is additive and separately named. Production steady-state behavior remains unchanged at this gate.

## Scientific boundary

This acceptance means:

- the residual public-asset definition is algebraically and dimensionally accepted;
- no gain is required for the level definition;
- floor behavior for private capital at/above target is accepted;
- engineering/static evidence is sufficient to authorize a separately governed bounded runtime integration diagnostic.

It does **not** mean:

- the C1 dynamic path is stable;
- beta_a is identified;
- HJB/KFE are scientifically valid;
- normalized labor should be activated simultaneously;
- production steady state is accepted;
- Results are eligible.

`Results eligibility=FALSE`.
