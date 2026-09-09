# Chapter 5 两资产 HANK 当前状态
更新：2026-09-10。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`CORRECTED_2018_FIVE_TURN_DIAGNOSTIC_BLOCKER_ACCEPTED__KFE_ATTRIBUTION_ACTIVE`。
最新接受科学候选：`9864129dd2e97bae97238ab9cc588aea48682d29`。
Five-turn报告：`docs/CH5_MP4C_2018_CORRECTED_INPUT_FIVE_TURN_PREFIX_REPORT.md`。
Reviewer验收：`docs/CH5_MP4C_2018_CORRECTED_INPUT_FIVE_TURN_PREFIX_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION.md`。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

## 2018数据层已闭合
- canonical workbook：`D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`；SHA-256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`；私有本体不提交GitHub。
- 安徽2018修订后现价GDP官方公布值=`34010.9`亿元；保护workbook `34010.91`仅在官方0.1亿元精度下匹配。
- 安徽2018常住人口=`6076`万人。
- PIM资本冻结并闭合：`K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`；安徽`K2018=1357314108.2013683`万元；资本为model-derived calibration object；2011投资统计定义断点保留。
- PLM rolling 10-year；2018 vintage19/window2009–2018；same-year Zt；安徽alpha=`.772866243094144`。

## 已接受 corrected-2018 科学前缀
### Turn 1–3
- turn1/turn2/turn3 均已完整31省执行并接受；turn3首次真实观测corrected firm `ra=.02`通过native capital-allocation timing进入household composite return。
- 安徽 `rah`: `.09 -> .0829892058879816 -> .0184420457528848`。
- 安徽 firm raw `ra0`: `-.02496997113112164 -> -.024968505109415375 -> -.024968792977977675`；used `ra=.02`。
- turn3 source old-ra vector 31/31均为`.02`，source SHA-256=`79EBB857CF8A7AD90E3418F9B2A6D2E5D294FFFB6E25C3A71BD0FC77B0A256D8`。

### Five-turn bounded prefix
候选`9864129d...`完整执行turn1–5 / 155 province updates，科学重试0；turn1–3前序复现mismatch均0。

Reviewer marker：
`CORRECTED_2018_FIVE_TURN_DIAGNOSTIC_BLOCKER_ACCEPTED__KFE_SOURCE_FREE_STATIONARITY_AND_UPPER_B_LEAKAGE_BLOCK_PREFIX_INTERPRETATION`

接受事实：
- turn4/5 returned density：31/31均`DIAGNOSTIC_ONLY`；KFE returned不等于source-free stationary validity。
- negative density weighted mass仅机器精度量级，不是material blocker。
- material blockers：source-free stationarity residual + upper-b outward leakage。
- turn4/5全国upper-b positive leak cells各620；lower-b/lower-a/upper-a leakage均0；max upper-b leak rate约2.2393。
- 安徽A+B：turn2 `11.978258156033768` -> turn3 `1.8919618910437164` -> turn4 `1.8927517068346027` -> turn5 `1.8926686768743746`。这些只可称diagnostic quantities。
- turn4首次native adaptation gate开启；turn4/5均执行31次Zt adjustment和31次`LOW_RA_DECREASE_0P9` GovInv action。该controller行为不解决KFE blocker。
- 不授权turn6+、steady state、GE、annual、MATLAB、IRF或Results。

## 当前 active task：five-turn KFE leakage attribution
`tasks/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION.md`

任务严格为ZERO-SCIENCE-CALL post-processing。只读取five-turn已保存的operator/density/drift和当前冻结源码，判断turn4/5 blocker是否与已接受call725 `rah=.07`归因中的同一机制一致：finite-box upper-b outward leakage + row replacement/pinning dropped source-free equation + algebraic implicit balancing source。

必须全国量化turn4/5：pin-row residual concentration、off-pin residual、四面boundary leak、density-weighted escape、signed residual-vs-escape identity、implicit-source-vs-escape balance，并与call725机制对照。若saved artifacts不足，不得重跑科学模型。

所有scientific/model calls必须为0。不得实现boundary/grid/source/pinning repair；D1–D3仍是deferred redesign proposals。

## 验收后的科学分叉
- 若`SAME_FINITE_BOX_UPPER_B_LEAKAGE_AND_PINNING_MECHANISM_CONFIRMED`：先进入Owner boundary/KFE closure科学决策，不直接继续trajectory或steady state。
- 若partial/distinct：先定位additional residual source，再决定设计路线。
- 不论归因PASS与否，Results eligibility保持FALSE。

## 会话交接
当前会话已很长。Owner要求：当前attribution任务返回后，Reviewer先验收、必要时合并候选并同步CURRENT文档，然后立即生成完整新会话交接prompt。以后每次发布exact task时，同一回复自动附Codex启动prompt。