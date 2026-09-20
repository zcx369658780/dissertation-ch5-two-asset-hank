# Chapter 5 两资产 HANK 当前状态

更新：2026-09-20。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`CORRECTED_HOUSEHOLD_FIXED_POINT_AND_AGGREGATE_INTERFACE_ACCEPTED__OWNER_PAYOFF_RETURN_FREEZE_REQUIRED__OUTER_RUNTIME_BLOCKED`

Results eligibility=`FALSE`。

## Accepted corrected household closure

Accepted checkpoint 11 provides:

- HJB primary convergence PASS;
- exact same-Q11 source-free unique invariant mass PASS;
- exact stationary aggregate/interface binding PASS.

Latest aggregate-adapter candidate accepted:

`5830285db591c448cacffd8a7b28635bbcef2f54`.

Acceptance:

`docs/CH5_MP4C_2018_CORRECTED_HOUSEHOLD_FIXED_POINT_AGGREGATE_AND_ADAPTER_BINDING_ACCEPTANCE_20260920.md`.

Accepted corrected fixed-point aggregates:

- Ct `11.72504598498222`
- Lt `0.6881256647265093`
- At `9.210552290174773`
- Bt `1.6622560718337767`
- total assets `10.87280836200855`
- AtTax `0.05117497248083413`.

The opt-in corrected household adapter is accepted. Existing default household/one-turn/stationary route remains unchanged.

## Current scientific gate

There is no active Builder task.

The controlling Owner gate is:

`docs/CH5_MP4C_K1A_PAYOFF_RETURN_OWNER_DECISION_GATE_20260920.md`.

The accepted payoff audit still finds:

- clipped/used `ra` = transitional source-faithful bridge only;
- raw `ra0` = source-consistent payoff candidate;
- period / numeraire / final payoff interpretation unresolved.

No runtime payoff-law change, K1B execution or corrected-household outer trajectory may begin until Owner explicitly adopts the payoff-return contract.

K1A geography benchmark `beta_distance=2`, K1/C1 accounting, lagged timing and source-faithful labor sequencing remain accepted.

Production default, market clearing, GE, annual dynamics, IRFs, welfare and Results remain closed.
