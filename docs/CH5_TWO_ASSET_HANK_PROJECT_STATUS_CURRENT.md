# Chapter 5 两资产 HANK 当前状态
更新：2026-09-10。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`FIVE_TURN_KFE_ATTRIBUTION_ACCEPTED__SAME_FINITE_BOX_UPPER_B_LEAKAGE_AND_PINNING_MECHANISM_CONFIRMED__OWNER_BOUNDARY_DECISION_REQUIRED`。
最新接受候选：`ea4ac44fe3c65c506ff7fdfbdbf29d96078cc5c6`。
报告：`docs/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION_REPORT.md`。
Reviewer验收：`docs/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION_ACCEPTANCE.md`。
当前 active Builder task：无。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

## 2018数据层已闭合
- canonical workbook：`D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`，SHA256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`；私有本体不提交GitHub。
- 安徽2018四经普后修订现价GDP=`34010.9`亿元；POP=`6076`万人；PIM `K2018=1357314108.2013683`万元；alpha=`.772866243094144`；PLM vintage19/window2009–2018；same-year Zt约`.0006934644495858679`。
- PIM冻结：`K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`；资本为model-derived calibration object；2011投资统计定义断点保留。

## corrected-2018 已接受科学证据
- turn1–3完整执行并接受；turn3已真实观测corrected firm `ra=.02`通过native capital-allocation timing进入household composite return。
- 安徽`rah`: `.09 -> .0829892058879816 -> .0184420457528848`；turn3 source old-ra vector 31/31均`.02`。
- five-turn候选`9864129dd2e97bae97238ab9cc588aea48682d29`完整执行5 turns/155 updates，0 scientific retries，但被接受为KFE/distribution diagnostic blocker，不是PASS。
- turn4/5 returned densities 31/31均`DIAGNOSTIC_ONLY`；machine-scale negative density不是material blocker；material blockers是source-free stationarity residual与upper-b outward leakage。
- turn4/5全国upper-b positive leak cells各620；lower-b/lower-a/upper-a outward leak均0；max leak rate约2.2393。
- turn4首次native adaptation gate开启；turn4/5执行31省Zt adjustment与`LOW_RA_DECREASE_0P9` GovInv action。该controller行为不解决KFE blocker。

## 最新归因：同一 finite-box/pinning 机制已确认
候选`ea4ac44f...`在0 scientific/model/solver calls下，使用five-turn保存的operator/density/drift完成全国归因。

接受结论：
`SAME_FINITE_BOX_UPPER_B_LEAKAGE_AND_PINNING_MECHANISM_CONFIRMED`。

关键事实：
- turn4/5共62个省-轮对象：material source-free residual 62/62；positive upper-b escape 62/62；pin row约占全部residual L1 62/62。
- pin-row L1 share=`0.9999999999869693–0.9999999999982326`；max individual off-pin residual=`5.352822169074709e-15`，低于`128 eps≈2.842e-14`。
- signed residual-vs-escape identity和implicit-source-vs-escape balance均在约`10^-16`浮点误差内闭合；无additional material residual source。
- upper-b finite-box assembler省略outside-grid offdiagonal但保留对应diagonal rate；KFE使用post-loop operator转置、替换`k=295`方程、设置`rhs[k]=.007`并归一化。被丢弃的source-free equation在代数上等价于平衡upper-b escape的source。
- 这只是finite-box/pinning代数后果，不是源码显式的household entry/exit经济机制。
- corrected turn4/5与accepted call725 `rah=.07`属于同一post-loop KFE机制；flows规模不同但closure结构一致。
- HJB-loop operator仍是独立问题：turn4/5有19个negative offdiagonals；post-loop KFE operator为0。质量账本只使用后者。
- turn3资产塌缩与invalid-density/leakage机制时间上同时出现，但保存证据不能把leakage识别为唯一因果来源；C/L/A/B继续只是diagnostic quantities。

## 当前科学边界
当前没有active Builder task。禁止自动继续turn6+、new KFE solve、steady state、GE、annual、IRF、Results，也禁止直接实现production boundary/grid/source/pinning repair。

下一步必须先由Owner作finite-box/KFE closure科学决策。D1–D3继续是deferred redesign proposals，不因本次机制确认而自动采用。

## 会话交接
当前长会话到此收口。新会话必须fresh-read live main、`AGENTS.md`、规则索引、本状态、交接和最新attribution acceptance，再与Owner讨论boundary/KFE closure路线。任何新科学执行仍需先发布exact GitHub task；发布task时同一回复自动附Codex启动prompt。