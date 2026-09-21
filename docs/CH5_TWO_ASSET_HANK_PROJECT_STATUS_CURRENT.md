# Chapter 5 两资产 HANK 当前状态

更新：2026-09-21。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`.

状态：

`K1B_TURN3_ACTIVATION_SAFETY_ACCEPTED__K1B_TURN3_RUNTIME_ACTIVE`

Results eligibility=`FALSE`.

## Latest accepted corrected runtime prefix

Turn2 runtime candidate:

`45e2e1f0f50c8e681d13e4e22fba4b50a90c8aad`

Turn2 acceptance:

`docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_FRESH_TURN2_RUN005_ACCEPTANCE_20260921.md`

Accepted facts remain:

- 31/31 turn2 household HJB/KFE PASS;
- 380 direct HJB updates;
- six one-halving monotonicity-preserving relaxation events;
- exactly one K1A/C1 integration PASS;
- national private-capital residual 0;
- completed-turn2 raw ra0 SHA `B3B50A6F0A3876904582DE05354C2DF76A71524FB53E41D4170109B8FCEB8951`.

## Latest accepted K1B activation safety gate

Candidate:

`1c2157c1ee381f1bbc21bcebaa0233784e41a5c5`

Acceptance:

`docs/CH5_MP4C_K1B_TURN3_LAGGED_RAW_RA0_ATTRACTIVENESS_ACTIVATION_SAFETY_GATE_ACCEPTANCE_20260921.md`

Accepted frozen turn3 K1B objects:

- population-z-score ddof=0 mean/std = `0.5151713619509639 / 0.18665369395010123`;
- z-score SHA `E152FE1C33634F2127D2B535638FA2725687650496140641F0FC6D6A4C02B564`;
- turn3 K1B share-plan SHA `4C3AB67F1982AEB3B707D07C53BB98C5BA54C835234DFEDE45A96B09BC5E3AB6`;
- turn3 K1B household payoff SHA `CEEFE34C16BA0DFDE9FA0C5590DFBB89084475BD88A8496EC18FEEBA7CB674D2`;
- K1A/K1B home shares bitwise identical;
- 900 foreign share cells change;
- scale-only national private-capital residual = 0;
- production source changes = 0;
- all scientific calls = 0.

The exact turn3 input candidate changes no non-`rah` state field relative to accepted run005 and remains household-not-run evidence.

## Active task

`tasks/CH5_MP4C_K1B_TURN3_CORRECTED_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_20260921.md`

The task authorizes exactly one corrected K1B-active turn3:

1. 31-province household HJB/KFE under the accepted relaxation/KFE laws;
2. if and only if 31/31 pass, exactly one integration using source-faithful labor and the exact frozen turn3 `S_K1B`;
3. C1 residual GovInv and one firm batch;
4. deterministic construction of the lagged K1B turn4 share/payoff candidate;
5. STOP before turn4 household.

K2, full outer fixed point, GE, annual dynamics, shocks, IRFs, welfare and Results remain closed.
