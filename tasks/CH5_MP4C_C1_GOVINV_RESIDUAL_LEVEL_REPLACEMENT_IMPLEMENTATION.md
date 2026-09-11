# Chapter 5 MP4C C1 GovInv residual level-replacement implementation

Date: 2026-09-11

Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Implement, as a separately named diagnostic successor controller component, the Owner-frozen interpretation of `GovInv` as unobserved government/public productive assets that close the gap between observed province productive-capital target and model-implied private productive capital.

The frozen diagnostic rule is:

`GovInv_next_j = max(Ktarget_j - Kprivate_current_j, 0)`.

This task is **zero-science implementation only**. Do not run a trajectory, steady state, HJB, KFE, firm, migration, wage, or controller runtime.

## 2. Required authority

Fresh-read live `origin/main`, then read at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- current status/handoff/roadmap;
- `docs/CH5_MP4C_GOVINV_CONTROLLER_REDESIGN_FORENSIC_AND_SPEC.md`;
- `docs/CH5_MP4C_GOVINV_CONTROLLER_REDESIGN_FORENSIC_AND_SPEC_ACCEPTANCE.md`;
- accepted G1 initialization probe/report/acceptance;
- accepted G1 isolated 25-turn diagnostic/report/acceptance;
- accepted corrected-2018 runtime binding authority;
- current controller/adaptation and capital-allocation sources;
- protected MATLAB `HANK_mp_1eq.m`, `HANK_mp_1turn.m`, `HANK_firm.m` if locally accessible, read-only.

## 3. Owner-frozen economic interpretation

`GovInv` represents government/public productive assets. The motivation is that estimated total productive capital `Kt` materially exceeds household/private illiquid assets `At`, while province-level government productive asset stocks are not directly observed with sufficient reliability. Historically `GovInv` was therefore made endogenous and adjusted by a clipped-return heuristic.

For this successor route, the government/public asset stock is defined residually against the accepted capital target:

`GovInv = max(Ktarget - Kprivate, 0)`.

This is **not** an arbitrary balancing stock and **not** a gain tuned for convergence.

## 4. No lambda_K parameter

Do not expose or select `lambda_K` in this task.

Although the forensic wrote generic C1 as

`GovInv_next=max(GovInv + lambda_K*(Ktarget-(Kprivate+GovInv)),0)`,

the Owner clarification freezes the next diagnostic component to the direct residual level replacement:

`GovInv_next=max(Ktarget-Kprivate_current,0)`.

This is algebraically equivalent to one-step `lambda_K=1` replacement but must not be described as an estimated or calibrated gain.

## 5. Input/output contract

Implement a pure deterministic helper with explicit fields at least:

Inputs per province:

- `Ktarget_MU`;
- `Kprivate_current_MU`.

Outputs per province:

- `GovInv_residual_MU`;
- `firm_K_accounting_MU = Kprivate + GovInv_residual`;
- `firm_K_over_target`;
- `private_at_or_above_target`;
- `residual_floor_binding`;
- `capital_gap_before_MU`;
- `capital_gap_after_MU`.

Required behavior:

- if `0 <= Kprivate < Ktarget`, then `GovInv=Ktarget-Kprivate` and total accounting K equals Ktarget;
- if `Kprivate >= Ktarget`, then `GovInv=0` and any private-capital overshoot remains explicit;
- negative/nonfinite private capital or nonpositive/nonfinite target fails closed.

## 6. Preserve historical C0

Do not modify or delete the historical source-faithful C0 controller path.

The new component must be separately named, for example:

`residual_government_asset_level`

or another unambiguous name.

The existing clipped-return controller remains available for source parity/history.

## 7. State semantics

The successor component defines a **level**, not a multiplicative adjustment action.

Do not produce labels such as `HIGH_RA_INCREASE_1P1`.

Use labels that expose residual-government-asset semantics, e.g.:

- `RESIDUAL_PUBLIC_ASSET_POSITIVE`;
- `RESIDUAL_PUBLIC_ASSET_ZERO_PRIVATE_AT_OR_ABOVE_TARGET`.

Do not silently modify `ra`, `rah`, `Zt`, wages, labor, Ktarget, private K, or KN references.

## 8. Static replay on accepted G1 ledger

Using accepted G1 25-turn province ledger only, with **zero model calls**, compute for every province-turn:

`GovInv_C1_residual = max(Ktarget - Kprivate, 0)`

and compare against recorded historical C0 GovInv.

Report:

- how many rows C1 would put exactly at accounting Ktarget;
- how many rows private K is already at/above Ktarget;
- C0 vs C1 GovInv level difference;
- C0 vs C1 accounting total-K/target;
- how much of the accepted late-window overshoot would disappear mechanically under C1 accounting.

This is static counterfactual accounting only. Do not claim a dynamic trajectory result.

## 9. Mandatory tests

At minimum test:

1. `Kprivate=0` -> `GovInv=Ktarget`.
2. `0<Kprivate<Ktarget` -> exact residual closure.
3. `Kprivate=Ktarget` -> `GovInv=0`.
4. `Kprivate>Ktarget` -> `GovInv=0`, overshoot retained.
5. vectorized 31-province behavior.
6. units and shape preservation.
7. nonfinite/negative inputs fail closed.
8. historical C0 path unchanged.
9. no `lambda_K`, damping, hysteresis, or `ra_target` introduced.
10. no model/scientific calls.

## 10. Forbidden scope

Do not:

- run HJB/KFE/household;
- run firm;
- run migration or normalized migration;
- run wage;
- run outer turn/trajectory/steady state;
- modify G1 initialization observation logic;
- modify C0;
- activate normalized labor;
- alter HJB/KFE/bounds/grids/solvers;
- select damping/hysteresis;
- introduce return-target control;
- run GE/annual/IRF/Results.

## 11. Required outputs

At minimum:

- production-adjacent but unconnected pure residual-public-asset helper/source;
- focused tests;
- `docs/CH5_MP4C_C1_GOVINV_RESIDUAL_LEVEL_REPLACEMENT_IMPLEMENTATION_REPORT.md`;
- `reports/mp4c_c1_govinv_residual_level_replacement_20260911/static_g1_replay.csv`;
- `.../static_replay_summary.json`;
- `.../api_contract.json`;
- `.../legacy_c0_unchanged_receipt.json`;
- `.../zero_scientific_call_ledger.json`;
- source/hash receipt;
- focused test receipt;
- manifest/readback.

## 12. Report must answer

1. Is the C1 helper algebraically exact for residual government/public assets?
2. Does it preserve private-capital overshoot rather than hiding it when `Kprivate>=Ktarget`?
3. On accepted G1 history, how much of late K overshoot is mechanically attributable to the historical C0 GovInv level rather than private K?
4. Does the implementation introduce any tuning coefficient? It must answer no.
5. Is the helper ready for a separately authorized bounded trajectory integration test?

## 13. Allowed verdicts

- `C1_GOVINV_RESIDUAL_LEVEL_REPLACEMENT_PASS__PURE_PUBLIC_ASSET_RESIDUAL_IMPLEMENTED_AND_STATICALLY_VALIDATED`
- `C1_GOVINV_RESIDUAL_LEVEL_REPLACEMENT_PARTIAL__PURE_HELPER_VALID_BUT_STATIC_REPLAY_INCOMPLETE`
- `C1_GOVINV_RESIDUAL_LEVEL_REPLACEMENT_BLOCKED__CAPITAL_ACCOUNTING_CONTRACT_AMBIGUOUS`

PASS does not authorize runtime activation or steady-state acceptance.

## 14. Git boundary

Use dedicated branch/worktree.

- no force push;
- no reset/clean/stash;
- explicit staging only;
- commit and non-force push;
- do not merge main;
- do not publish successor scientific task;
- Results eligibility remains `FALSE`.

Return to Reviewer with verdict, branch, candidate SHA, files changed, focused tests, static replay summary, legacy-C0 unchanged evidence, zero-call ledger, and report path.
