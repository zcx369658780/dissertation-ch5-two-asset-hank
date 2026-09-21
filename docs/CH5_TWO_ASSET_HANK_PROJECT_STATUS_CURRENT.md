# Chapter 5 两资产 HANK 当前状态

更新：2026-09-21。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`.

状态：

`K1B_TURN4_FIRST_FAILURE_ACCEPTED__ANHUI_F0364_FORENSIC_ACTIVE`

Results eligibility=`FALSE`.

## Accepted K1B-active turn3

Candidate `1143cd8eb6e7722d7588107a0d69f68e8dd06df7` remains the latest complete K1B-active PASS.

Turn3 acceptance:

`docs/CH5_MP4C_K1B_TURN3_CORRECTED_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_ACCEPTANCE_20260921.md`.

## Accepted turn4 failed evidence

Candidate:

`cc8f1ba22aa2b010325dce6e6c282802f5157c10`

Acceptance:

`docs/CH5_MP4C_K1B_TURN4_ANHUI_F0364_FIRST_FAILURE_ACCEPTANCE_20260921.md`

Terminal:

`FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE`.

First failure:

- 安徽, province index 11
- checkpoint 4
- flat 364
- cell `v004_f0364_b004_a018_z000`
- cell SHA `F1170662F50FEB38BB6D26B233725B672B12397EA891C15CBBDC559DBA6DCB65`
- outcome `NO_ADMISSIBLE_POLICY`.

Reached before stop:

- HJB/KFE PASS: 11/31
- direct HJB updates: 140
- SCC / restricted GESVD / stationary / full-Q: 11 each
- relaxation alpha=1 / alpha=.5: 138 / 2
- retries / solver substitutions: 0 / 0.

The 31/31 gate failed. Therefore turn4 household batch, integration, C1, firms, completed-turn4 raw ra0, turn5 preparation and turn5 household were all not run.

Production source changes=0. CURRENT changes by Builder=0.

## Forensic issue

The exact 安徽 cell has a strict a-drift crossing on the backward-liquid negative-transfer branch.

Current selector source also contains a whole-mapped-interval positivity guard before the already accepted interior-a switching construction.

Because the current illiquid derivative interval crosses zero, the next task must determine whether that guard discards an otherwise valid positive branch-local q_b candidate under the existing Owner authority.

No defect classification or selector repair is yet accepted.

## Active task

`tasks/CH5_MP4C_K1B_TURN4_ANHUI_F0364_STRADDLING_ZERO_MAPPED_INTERVAL_FORENSIC_20260921.md`

This is zero-science only. It may read persisted evidence and perform deterministic scalar arithmetic. It may not call the production selector/HJB/KFE or modify production source.

K1B turn4 rerun, K2, full outer fixed point, GE, annual dynamics, shocks, IRFs, welfare and Results remain closed.
