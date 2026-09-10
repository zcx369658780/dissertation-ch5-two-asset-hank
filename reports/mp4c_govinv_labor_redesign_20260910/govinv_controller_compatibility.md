# GovInv controller compatibility: static source audit

## Scope

This is a zero-science source reading.  No model, solver, MATLAB, Python runtime, or trajectory was invoked.  The observed-prefix statements below are restricted to the accepted 25-turn ledger; they neither estimate a new controller nor freeze a parameter.

## Recovered source order

1. `HANK_mp_1eq.m:8` first obtains one completed `HANK_mp_1turn` result.
2. Within that turn, `HANK_mp_1turn.m:31-36` constructs `Kt_supply` from the household-produced `At*N` and cross-province allocation; `HANK_mp_1turn.m:46` then calls the firm block.
3. `HANK_firm.m:14` forms firm capital as `Kt = Kt_supply + GovInv`.  It computes the **raw** asset return `ra0` at line 54, then clips it to `ra` at the grid maximum/minimum or retains it at lines 57-65.  The stored field is `results.ra` (`HANK_firm.m:84`), so the outer controller observes the clipped value, not the raw magnitude beyond a boundary.
4. After the turn, `HANK_mp_1eq.m:31-38` computes the `KNratio/tKNratio` gap and records whether clipped `ra` is exactly at a bound.  Full local convergence requires the KN and Y gaps, all HJB convergence flags, and no clipped `ra` endpoint (`HANK_mp_1eq.m:42`).
5. Only after non-convergence, only when `maxKNratiogap < 0.1`, and only for a steady-state call does the update block run (`HANK_mp_1eq.m:47`).  For each province it first updates `Zt` when the Y target error exceeds 1 percent (`:49-50`), then tests the **clipped** `results.ra`: below `ramin + 0.02` multiplies `GovInv` by `0.9`; above `ramax - 0.02` multiplies it by `1.1` (`:52-55`).
6. The reference `tKNratio` is updated only after that controller block as `0.6*current_KNratio + 0.4*previous_tKNratio` (`HANK_mp_1eq.m:60-62`).  Thus the next pass sees the post-update state and the smoothed KN reference; the current pass's gate precedes both the current-pass controller action and the reference refresh.

## Compatibility implications

- The source action is a return-bound response, not a capital-target residual controller.  It does not compare `Kt_supply + GovInv` with `Ktarget`.
- Because `ra0` is clipped before the outer test, the controller retains endpoint direction but not the degree by which raw return exceeded a bound.  A future redesign that needs raw-return magnitude needs explicit authority and a source-level contract; it cannot infer that magnitude from `results.ra`.
- `Zt` adjustment is ordered before the return-triggered GovInv action inside the same gated loop.  These are coupled state updates: a new initialization must be evaluated for compatibility with that sequence rather than treated as a replacement for it.
- The accepted ledger shows the frozen controller did not reduce the observed capital gap: turns 20-25 had zero GovInv decreases, increase counts `22, 0, 21, 0, 16, 0`, and median GovInv/target rose from `2.143588810000001` to `2.8531167061100016`.  This is bounded diagnostic evidence, not a calibration target.

## Future integration options (not selected and no parameters frozen)

1. **Initialization-only separation.**  Select an externally identified initialization contract, retain the source controller unchanged, and separately authorize a bounded evaluation of the resulting path.  This preserves source mechanics but does not presume the controller will correct a new capital accounting start.
2. **Retain trigger, later study damping.**  Preserve the clipped-return trigger and the existing Zt/KN ordering, while a separate future controller task considers an explicitly governed under-relaxation/damping rule.  Its functional form and any coefficient require future authority; neither is set here.
3. **Two-decision architecture.**  Freeze neither control law nor initialization now: first resolve the economic public/private capital definition and its observation point, then decide in a separate task whether a capital-target controller is warranted.  This avoids using controller performance to identify the initial public-capital level.

## Boundary

`GovInv0=Ktarget` is a source-faithful historical start, but the accepted prefix establishes that it mechanically adds positive private supply and therefore is not evidence for an economically identified public-capital level.  Residual initialization is structurally compatible with the firm identity only after `Kt_supply_initial` is independently defined.  No production rule, controller alteration, HJB/KFE change, parameter choice, or scientific call is authorized by this note.
