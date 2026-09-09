# Chapter 5 MP4C corrected-2018 single-turn validation — Reviewer acceptance

Date: 2026-09-09.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Accepted candidate: `90ee5b29f3be070d9f8f28c9614e1b59fe798462`.

## Verdict

Reviewer marker: `CORRECTED_2018_SINGLE_TURN_ACCEPTED__FULL_ORDERED_TURN_PASS__TURN2_PROPAGATION_REQUIRED_BEFORE_LONGER_PREFIX`.

Accept the candidate verdict `CORRECTED_2018_SINGLE_TURN_PASS__FULL_ORDERED_TURN_COMPLETED`.

## Accepted findings

1. The canonical workbook identity was bound to SHA-256 `AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`, and the corrected 2018 V2 annual contract was used without legacy fallback.
2. Exactly one ordered 31-province turn completed. All 31 native household initializations, HJB solves, KFE solves, aggregates, firm calls and province updates returned; no scientific retry occurred.
3. Every HJB converged in 64 updates; total HJB direct solves were 1,984. All 31 KFE direct solves returned.
4. Anhui corrected first-turn firm raw return was `-0.02496997113112164`; the used firm rate clipped to the lower bound `0.02`, not the upper bound `0.09`. Raw wage was `2.5721358283733027`, clipped to `1.3`.
5. Anhui household entered turn 1 with carried `rah=0.09`. This is not contradictory to the current-turn firm `ra=0.02`: the household rate is an entering/lagged state and the current firm return cannot rewrite the same-turn household call.
6. Across all 31 provinces, firm rates clipped lower in 31 cases and upper in 0 cases. Wage clipping was lower in 5 and upper in 22 cases. Maximum `nk_gap=204296.40029802968` at Shandong, so the adaptation gate was not open; no Zt or GovInv adjustment occurred.
7. The saved-old comparison is accepted only as `DESCRIPTIVE_INPUT_CORRECTION_EFFECT_ONLY`. It must not be used to claim that the old turn-23/call725 high-return pathology has been eliminated, because this new evidence covers only turn 1.
8. Scientific calls and actual call counts were properly recorded, including 24,800 labor roots, 24,800 brentq calls, 31 HJB calls, 1,984 HJB direct solves, 31 KFE solves, one controller call, and zero MATLAB/second-turn/steady-state/GE/annual/IRF/Results calls.

## Scientific interpretation

This pass establishes that the corrected 2018 data contract produces a fully executable first turn and that the first-turn firm return is on the low-rate side rather than the old late-prefix high-rate side. It does **not** establish steady-state convergence, long-prefix stability, KFE global admissibility, or elimination of the old call725 pathology.

The highest-value next observation is turn 2, because turn 1 still feeds households the carried `rah=0.09` while the corrected current firm produces `ra=0.02`. Turn 2 is therefore the first point at which the corrected firm-rate state can propagate into subsequent household inputs under the native one-turn law.

## Next route

Authorize a bounded two-turn propagation task only. Reuse/validate the accepted turn-1 identity and execute a fresh source-faithful two-turn corrected-2018 trajectory with no scientific retries. Capture turn-by-turn household `rah`, firm `ra0/ra`, wage, HJB/KFE status, gaps, and controller actions, with special focus on Anhui. Do not proceed to turn 3 or steady state in the same task.

Results eligibility = FALSE.
