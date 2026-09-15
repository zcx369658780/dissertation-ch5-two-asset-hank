# Chapter 5 当前交接 — J160 first-turn local-basin interpolation diagnostic active

更新：2026-09-15。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC_ACTIVE`。

最新 accepted input-envelope candidate：`49ea4c12692c669701cdc7bcf8fd02267a068090`。
Acceptance：`docs/CH5_MP4C_K1_FIRST_TURN_PROVINCIAL_INPUT_OUTCOME_ENVELOPE_AUDIT_ACCEPTANCE.md`。
Freeze：`docs/CH5_MP4C_K1_J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC_FREEZE_CURRENT.md`。
Active task：`tasks/CH5_MP4C_K1_J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC.md`。
Results eligibility=`FALSE`。

Practical household grid remains `I=20,J=160,a=[0,100],b=[-2,20],h=1` for bounded diagnostics only. Finer-J/finer-I routes remain closed; do not extend maxit or introduce damping/relaxation/line search.

Accepted first-turn failures and successes overlap substantially in consumed `(ra, composite w)`: no single-variable threshold separates all outcomes, 2D boxes/hulls overlap, and the fixed k=3 graph is interleaved. Guard states also have no discriminating variation. This closes the simple safe-envelope / universal guard route.

Current exact task tests local numerical basin topology rather than calibration. Preregistered pairs: 山西↔河北, 重庆↔河北, 江西↔安徽, 贵州↔四川. Before science, each pair must prove exact equality of all consumed household inputs other than `ra` and composite `w`. Endpoints are reuse-only. For each authorized pair run only t=.25,.50,.75 interpolation probes in `(ra,w)`, with all other inputs fixed at their pair-common accepted values. Total new HJB exactly12, KFE=0, scientific retries=0. No adaptive bisection or extra synthetic points.

Synthetic probes are numerical diagnostics only; they are not feasible provincial equilibrium states, not outputs of upstream wage/return mappings, and not calibration targets. No boundary/HJB/mapping/parameter change is authorized in this task.

The corrected-2018 KFE finite-box/pinning blocker remains separate. Owner retains authority over structural changes, major calibration, causal interpretation and Results eligibility; ChatGPT Reviewer retains bounded local numerical/debug route authority.
