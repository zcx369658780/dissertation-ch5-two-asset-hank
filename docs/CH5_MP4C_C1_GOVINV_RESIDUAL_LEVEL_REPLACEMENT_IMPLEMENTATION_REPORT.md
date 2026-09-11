# Chapter 5 MP4C C1 GovInv residual level-replacement implementation report

Date: 2026-09-11

Builder verdict:

`C1_GOVINV_RESIDUAL_LEVEL_REPLACEMENT_PASS__PURE_PUBLIC_ASSET_RESIDUAL_IMPLEMENTED_AND_STATICALLY_VALIDATED`

## Result and scope

A separately named pure helper now defines government/public productive assets as the direct nonnegative residual between accepted productive-capital target and current model-implied private productive capital. It is exported as `residual_government_asset_level` for one province and `residual_government_asset_levels` for the exact 31-province axis. It is not connected to the active steady-state runtime or historical C0 controller.

The helper contains no tuning coefficient or return signal. It does not mutate private K, Ktarget, return, productivity, wages, labor, or KN references. Nonpositive/nonfinite targets, negative/nonfinite private capital, vector shape mismatch, and province-order mismatch fail closed. Outputs preserve the explicit `MU_10WAN_YUAN` contract and distinguish `RESIDUAL_PUBLIC_ASSET_POSITIVE` from `RESIDUAL_PUBLIC_ASSET_ZERO_PRIVATE_AT_OR_ABOVE_TARGET`.

No HJB, KFE, household, firm, migration, normalized migration, wage, controller-runtime, outer-turn, trajectory, steady-state, root/Brent, MATLAB-runtime, GE, annual, IRF, or Results call was made. `Results eligibility=FALSE`.

## Static accepted-G1 replay

The accepted 25-turn ledger supplied all 775 province-turn rows; no model was rerun. C1 places 775/775 rows exactly at accounting Ktarget. Private K reaches or exceeds Ktarget in 0/775 rows, so no floor binds and no private-only overshoot remains in this saved path.

For turns 20-25 (186 pooled observations), historical C0 total-K/target min/median/mean/max is `1.3257022041568054 / 2.353363495591088 / 2.2653870930586595 / 2.8512142917573127`. Static C1 accounting is exactly `1 / 1 / 1 / 1`.

Late-window historical C0 GovInv/target min/median/mean/max is `1.3144349634860897 / 2.3503561274071445 / 2.2607692059229105 / 2.8503483106194247`; static C1 GovInv/target is `0.9674211387143388 / 0.9970813617599386 / 0.9953821128642512 / 0.9991512192299407`. Private-K/target remains `0.0008487807700594351 / 0.0029186382400614363 / 0.00461788713574891 / 0.032578861285661315`.

Thus the accepted late median moves mechanically from `2.353363495591088` to `1.0`: `1.353363495591088` target multiples, or 100% of the historical median overshoot above one, disappear in the static accounting replacement. Across pooled late province-turns, historical positive overshoot totals `19963597940.767487 MU`; C1 mechanically removes `19963597940.767487 MU`, with `0.0 MU` remaining private-only overshoot. These pooled sums are province-turn accounting totals, not a national stock or a dynamic effect.

Requested all-sample and five-turn-window distributions are in `static_replay_summary.json`; every row is in `static_g1_replay.csv`.

## Historical C0 preservation

`src/ch5_two_asset_hank/multi_province/steady_state.py` remains byte-identical to the accepted baseline, SHA-256 `B8897FDEF9CC59A2811561A18CB0FADF059A158AD8E5F3661BD10A5734D264AA`. Its clipped-return `0.9/1.1` logic remains available. The new helper is additive and unconnected.

## Required answers

1. **Is the helper algebraically exact?** Yes. Below target, residual public assets equal target minus private capital and accounting firm K is exactly target; at or above target the public component is zero.
2. **Does it preserve private overshoot?** Yes. It never creates negative government assets, so private K above target remains explicit in total accounting K and in the negative post-replacement capital gap.
3. **How much late overshoot is attributable to historical GovInv level?** In the saved turns 20-25 path, private K is below target in all 186 rows and remaining private-only overshoot is zero. The full positive C0 overshoot—`19963597940.767487 MU` as a pooled province-turn amount—is mechanically removed by the static C1 replacement. This is not a causal trajectory estimate.
4. **Is any tuning coefficient introduced?** No. The rule is a direct level definition with only Ktarget and current private K inputs.
5. **Is it ready for bounded trajectory integration?** Engineering evidence is sufficient to present the pure helper for Reviewer acceptance and a later separately authorized integration task. Runtime activation and dynamic stability remain untested and unauthorized.

## Evidence and stop

Focused tests cover scalar branches, exact 31-province vectors, units, immutable shapes, invalid inputs, province order, absence of tuning/return-target fields, C0 source identity, complete static replay, and the zero-call ledger. PASS is implementation evidence only. No successor task is published; the next gate is independent ChatGPT Reviewer fresh-fetch ACCEPT/REJECT.
