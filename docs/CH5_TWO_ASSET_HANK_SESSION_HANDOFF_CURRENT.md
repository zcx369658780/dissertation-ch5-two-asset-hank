# Chapter 5 当前交接 — Option A first-cell fail-closed accepted / lower-a zero-kink multiplier repair active

更新：2026-09-16。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
状态：`OPTION_A_FIRST_CELL_FAIL_CLOSED_ACCEPTED__LOWER_A_ZERO_KINK_MULTIPLIER_REPAIR_REEXECUTION_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Governance

Owner is final scientific authority; ChatGPT is L3 Reviewer/scientific-route authority; Codex is bounded Builder. GitHub live `main` is repository-state authority. `deep-learning-hank` is a separate project.

## Accepted state

D1/D2/D3 remain Owner-adopted only for a separate corrected diagnostic target. Historical derivative failures are already attributed and closed. Owner selected Option A `hjb100_initialization.mat:v0` for the first corrected one-step diagnostic.

The first Option-A full-map attempt is now accepted only as fail-closed evidence. It stopped at Cell `(0,0,0)` before D2/HJB.

Reviewer found one concrete selector omission: at active lower-`a`, `a=0`, zero transfer, the frozen selector fixes `q_a=p_a` although the accepted lower-face KKT law allows `q_a=p_a+lambda_a`, `lambda_a>=0`. The D3 zero-kink interval must be intersected with this multiplier domain. At Cell 0 the intersection is nonempty, so the observed failure is not evidence that Option A lacks an admissible policy.

## Active task

`tasks/CH5_MP4C_2018_KFE_D123_LOWER_A_ZERO_KINK_MULTIPLIER_REPAIR_AND_OPTION_A_REEXECUTION_20260916.md`

Builder may repair only the active lower-a zero-kink multiplier branch, using a deterministic minimum feasible shadow from the legal intersection. No generic projection, no slack-face repair, no upper-a/nonzero-transfer change, no seed/grid/calibration/tolerance/D2 change.

After focused synthetic preflight and scientific-code freeze, rerun the same Option-A full-map experiment from Cell 0 with a fresh budget. Ceiling: <=800 selector evaluations, <=264 roots, D2<=1 only after complete 800-cell PASS, direct HJB solve<=1 only after D2 PASS, retries=0. First failed cell stops.

KFE/MATLAB/outer/firm/wage-return/GE/annual/shock/IRF/Results remain zero. Production replacement remains unauthorized.
