# Reviewer acceptance — C1 residual public-asset 25-turn contemporaneous integration

Date: 2026-09-11

Candidate: `b3183d1aa404922ee179359dc6fa43b411978090`

Reviewer verdict:

`C1_RESIDUAL_PUBLIC_ASSET_25TURN_ACCEPTED__CAPITAL_TARGET_HELD__GOVINV_OVERSHOOT_REMOVED__PRICE_NUMERAIRE_RAW_RA_UPPER_PRESSURE_IS_NEXT_DIRECT_NUMERICAL_BLOCKER`

## Acceptance basis

The candidate is one commit ahead of live baseline `ed38a9761f7911895df5314c99397bbfdd48b3c1` with no unrelated modifications. The new C1 route is separately named and inserts the already accepted residual-public-asset identity after current private productive-capital allocation and before firm evaluation. Historical source-faithful one-turn, C0 controller, firm, and capital-allocation implementations remain unchanged.

The run completed one initialization observation and exactly 25 outer turns with no scientific retry, second initialization, second trajectory, beta cell, steady-state production run, GE, annual, IRF, or Results call. C1 accounting assertions passed 775/775 province-turn rows; maximum absolute accounting residual was `1.4901161193847656e-08 MU`. Private productive capital never reached Ktarget, so the residual floor never bound.

Turns 20–25 pooled firm total-K/target was exactly `1/1/1` min/median/max. Thus the previously accepted two-to-three-times GovInv-driven capital overshoot is removed in the bounded dynamic path, not merely in static replay.

At the same time, turn-25 raw-ra lower/interior/upper counts are `0/1/30`, compared with `0/21/10` in both accepted C0 baselines. Therefore fixing the capital stock does not make the return signal more interior; it exposes a stronger raw-return/price-normalization tension. Pooled `rah` remains boundary-proximate rather than becoming decisively interior.

KN/Y/GDP numerical paths improve materially: turn-25 max KN gap is `2.0177068904558837e-09`, max Y/Yprev gap is `1.3322676295501878e-15`, and max GDP-level gap is `0.007556323724974279`. Zt adjustments occur only in turns 4, 6, and 7 and disappear in turns 20–25, so late instability is not primarily an active Zt-adjustment channel in this prefix.

HJB nonconvergence is confined to early turns; all household HJB returns converge from turn 6 onward. KFE remains independently `DIAGNOSTIC_ONLY` for 775/775 trajectory observations. These blockers remain distinct from the now-resolved GovInv capital-level overshoot.

## Scientific interpretation

Accepted conclusion: C1 is a successful bounded diagnostic integration of the Owner-defined residual government/public productive-asset stock. It removes the dominant GovInv-driven capital-level divergence mechanism under the current diagnostic beta bridge.

Not accepted: production steady state, beta-a identification, KFE validity, price/numeraire validity, wage/labor calibration, annual/GE/IRF/Results eligibility.

The next lowest-risk gate is a zero-science forensic of the firm price/numeraire and raw-ra upper-bound pressure under the accepted C1 path. The already accepted normalized-labor successor should remain inactive for that forensic so the source of the return-scale problem can be isolated before stacking labor normalization.

Results eligibility remains `FALSE`.
