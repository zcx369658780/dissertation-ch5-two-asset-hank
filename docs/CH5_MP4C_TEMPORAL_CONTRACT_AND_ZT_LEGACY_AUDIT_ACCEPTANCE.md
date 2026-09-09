# Chapter 5 MP4C 年度时间合同与 Zt legacy 审计 — Reviewer 验收

Date: 2026-09-09.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Accepted candidate: `deb2d56560ce85590b9e19d34b4d28ea6b084e27`.

## Verdict

Reviewer marker: `TEMPORAL_CONTRACT_AUDIT_ACCEPTED__ROLLING_10Y_PLM_FROZEN__LEVEL_INDEX_DEFECT_CONFIRMED__ZT_2020_ANCHOR_LIKELY_LEGACY`.

接受候选中的源码/数据发现、`steady_year = 2008 + ii`、同年水平量应使用一基 `ii+9` 行、固定2020 `Zt` 缺少已发现经济依据、以及旧cache与较新PLM workbook存在身份不一致等证据。

但是，候选报告中“Owner 已冻结从2000开始不断扩展的 expanding window，因此现有PLM artifact必须重建”这一科学解释不予接受。Owner在验收后明确裁决：PLM应使用滚动10年窗（rolling 10-year window），理由是过旧样本会干扰不断发展的生产力估计。该裁决也与现有PLM artifact的固定10期布局及源码“前10年的数据估计本年alpha”注释一致。

因此正式时间合同冻结为：

- `steady_year = 2008 + ii`；
- 稳态同年 GDP/CAP/POP 水平量行 = `ii + 9`（MATLAB一基）；
- PLM估计器保持不变；
- PLM样本窗 = 截至 `steady_year` 的最近10个年度：`steady_year-9 : steady_year`；
- ii=1 / 2009 使用 2000–2009；
- ii=10 / 2018 使用 2009–2018；
- ii=15 / 2023 使用 2014–2023；
- 不要求把现有PLM artifact改成从2000起始的扩展窗，也不因本次审计切换估计方法。

## Accepted findings

1. `multi_prov_HANK_12sts(ii,pp)` 的输出/稳态年度语义与 `ii+2008` 一致，但当前初始化器仍用 `data_year=ii` 读取工作簿水平量，导致 ii=10/2018 实际消费row10/2009。该 `level_row` 缺陷属于 confirmed defect。
2. `data_MAT{ii}` / PLM vintage end-year 与2009–2023稳态序列对齐；现有固定10期PLM布局与Owner新冻结的 rolling-10-year 合同一致。因此不再把“需要重建 expanding-window PLM artifact”视为 blocker。
3. `load_GDPdata.m` 对所有年度固定用row21/calendar2020构造 `Zt`，现有源码审计未找到base-year、normalization或经济锚定依据。接受 `LIKELY_LEGACY_FIXED_YEAR_ANCHOR`，但不升级为 `PROVEN_BUG`。
4. 年度一致性候选为：在保持现有PLM alpha vintage不变的前提下，`Zt`公式使用与稳态同年的 `level_row=ii+9` GDP/CAP/POP。
5. ii15/industry4 cache alpha=`0.967775174774325` 与较新PLM workbook vintage24 value=`1.0219847778591` 不一致。旧cache缺少版本身份，后续修复必须显式版本化并记录PLM workbook/source身份，不能静默混用。
6. 2022–2023六个负资本/复数log单元仍是独立数据质量 blocker；年份合同修复不能掩盖这些问题。

## What this does not authorize

本验收不执行生产patch，不重建cache，不重跑2009/2018稳态，不修改PLM估计器，不调整GovInv/alpha收敛速度，不继续扩大bmax，不运行多省份/GE/Results。

## Next route

下一步可进入一个有界实现任务：仅实现年度水平量 `ii+9`、同年Zt、cache/metadata版本合同和必要的静态/合成检查；在第一次科学模型运行之前，仍需处理2018所用官方数据核验与cache身份，并明确2022–2023负资本不进入本次2018小规模验证范围。

Results eligibility = FALSE.
