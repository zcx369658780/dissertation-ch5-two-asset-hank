# Chapter 5 两资产 HANK 当前状态

更新：2026-09-16。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`CELL5_ZERO_LIQUID_SWITCH_ATTRIBUTION_ACCEPTED__OWNER_INTERIOR_Z_LAW_DECISION_REQUIRED__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted checkpoints

Owner-adopted D1/D2/D3 corrected diagnostic bundle、isolated static implementation、historical ten-cell fail-closed selector evidence、failed-cell algebraic attribution、corrected-HJB one-step design/input binding、Option A seed adoption，以及 lower-a zero-kink multiplier repair均继续有效。Source-faithful/production paths remain frozen。

## Option A / Cell 5 checkpoint

Fresh Option A reexecution confirmed Cells 0–4 `SELECTED_ADMISSIBLE` after the lower-a zero-kink repair. The first later failure at Cell 5 `(5,0,0)` is now independently attributed by accepted candidate `fdfabfb8ba12fa52add525b68050de67c2d6369d`.

Accepted findings:
- backward liquid branch gives positive drift while forward branch gives negative drift;
- a unique positive zero-liquid shadow exists at `q_b*=0.01250021388291760706054915182349077777...`;
- it lies strictly between `p_b^F=0.012481806039037598` and `p_b^B=0.02256028269097067`;
- historical/source-faithful logic contains a genuine zero-liquid `I0`/`Z` precedent, and accepted Python HJB code contains an endogenous zero-liquid shadow candidate with Hamiltonian comparison;
- the separate corrected selector/budget does not explicitly inherit this branch and currently assumes interior-b cells consume zero scalar roots.

Therefore the current issue is an Owner-level corrected-target law decision, not a Builder implementation decision and not evidence of corrected-HJB/KFE/economic nonexistence.

Reviewer acceptance: `docs/CH5_MP4C_2018_KFE_D123_CELL5_LIQUID_DIRECTION_SWITCH_OWNER_DECISION_REQUIRED_ACCEPTANCE_20260916.md`。

## Owner decision gate

No scientific Builder task is active.

Owner must explicitly decide whether the corrected D1-D3 selector shall inherit the repository's historical/accepted interior zero-liquid `Z` switching law. If adopted, Reviewer must publish a fresh exact implementation/execution task with a new interior-root budget, eligibility conditions, Hamiltonian comparison contract and fail-closed rules before any Option-A rerun.

Until Owner decision: selector/root/policy-map/D2/HJB/KFE/MATLAB/outer/firm/wage-return/GE/annual/shock/IRF/Results calls remain unauthorized. Production replacement remains unauthorized.
