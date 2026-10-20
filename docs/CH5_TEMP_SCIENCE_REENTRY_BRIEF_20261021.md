# CH5 · TEMP科学主线恢复准备简报（2026-10-21）

STATUS=OWNER_APPROVED_RESEARCH_DIRECTION__PLANNING_ONLY
SCIENCE_EXECUTION_AUTHORIZED=FALSE
FORMAL_VERSION=V010/v0.0.10
MODEL_ACTIVATION=False
REAL_GE=False
RESULTS=FALSE
V011=NOT_STARTED
FULL_RUNNER_IO_CLOSURE=BLOCKED

## 研究方向与来源范围

Owner 2026-10-21同意结束发布器工具链循环、回到博士论文第五章科学主线。此处只依据现有已归档历史实验及冻结方法，确定优先研究问题和下一任务设计，不创造新的经济方程或科学运行额度。
主来源：
- `docs/CH5_SESSION_HANDOFF_20261018_AFTER_TEMP_HA_PRICE_BRIDGE_AND_GITHUB_ZIP_CLOSEOUT.md`
- `docs/CH5_TEMP_V010_BLACKBOX_100_ROUNDS_INDEPENDENT_REVIEW_20261018.md`
- `docs/CH5_TEMP_PRICE_BRIDGE_FACTORIAL_E2_LEDGER_TERMINAL_REVIEW_20261018.md`
- `versions/0.0.10/plan.md`（正式冻结，未经E3绝不改写）

## 事实基础（不可从历史接受推演未运行的结果）

1. 2009年31省MATLAB/Python稳态一致性仅在受界历史案例中接受，不能推断TEMP双省、其它年度、真实GE/IRF通过。
2. TEMP中MATLAB-faithful两资产HA黑箱，单个实验每ARM外层最多100轮（可早停），保留原HJB/D和KFE实际终态。Bellman残差只作TEMP观察，不将其新设正式V010硬门。
3. 合成两省100轮完整历史：末轮max KN gap 0.1075218256230952、max Y跨轮gap 0.012719310966908814、HA converged 0/2；两个省的`ra_used`与工资边界100/100轮触发。不是稳态、非数学上不可收敛定理。
4. 末轮两省企业端raw `ra0`约0.3846/0.4272，firm端used资本收益边界0.09，家庭`rah`约0.389/0.419，家庭净工资`wt0`约6.948/7.029，同状态firm`wjt`静态净工资约2.038/2.019。**存在显著传递差异**，但并未证明bug或改价后必收敛。
5. 价格桥A0 raw ra0+raw wt0沿用旧100轮，A1 used ra+raw wt0、A2 raw ra0+clipped wjt、A3 used ra+clipped wjt原先得到0/2/2完整轮，缺少共同完整样本，绝无可采纳因子效应结论。前实验E2硬停来自共享journal写入WinError5，且主控停止传播延迟；并非HA价格机制的科学失败证明。

## 目前优先解决的科学问题

问题一：家庭收入/资产价格输入与企业用价是否同尺度、同轮、同经济含义？用前次100轮固定轨迹和合同审阅`raw ra0`、`ra_used`、`rah`、`wt0`、`wjt`、`S`、税楔及边界裁切位置，先构建**不调用HA**的价格账与来源矩阵图。每个价记录来源、时点、单位、进入HA前实际值，不能仅由变量名推断等价。
问题二：厂商收益/工资触界是宏观约束造成的反馈可观测现象，还是某个单位/参数/读写路径失配？在Owner批准前，不调整`ra cap`、工资clip、GovInv/Zt、资本权重、劳动效用或者HA内部算法来换取PASS。
问题三：前次共享账本必须先证明单写者journal、append/checkpoint原子替换和E2 STOP对并发读者安全；WinError5共享删除句柄是假设而非既定根因。**不调用HA**的精确合成压力复现和快速停止测试，是后续科学实验的前置工程可靠性门，而非再建通用发布器。

## 推荐下一次单张受界科研任务（此文非签发/执行许可）

题目：TEMP V010 MACRO PRICE INPUT ATTRIBUTION AND LEDGER PRECONDITION
阶段A（只读科学诊断）：沿用已通过独立审议的100轮报告与固定MATLAB-faithful黑箱身份，只读取在新任务中明确列出的安全来源文件；建立价格输入/收益截断/单位时点影响链及可证伪的假设清单，保存SOURCE_ONLY结论。若原轨迹原字节仍仅保留私有，不得凭旧摘要自行伪造逐轮值。
阶段B（不运行HA的工程资格）：仅针对已定位的WinError5 checkpoint与共享STOP延迟做有限、可记录首错、带合成读写争用的测试，排除共享journal断裂。必须明确守住受保护工作树，不改主求解器。
阶段C（需要Owner另行批准真实科研预算后才可执行）：若A/B通过，再在隔离scratch中重做TEMP 2×2价格桥；A0仅复用历史不重跑，A1/A2/A3逐ARM先小轮资格观察，再按冻结每ARM最多100轮的新预算及硬停止。资本S继续前完整轮raw ra0排序、GovInv0.9/1.1、Zt/财政/劳动单次税楔和HA黑箱都不变；Bellman只作TEMP观察。要求价格实际进入HA前后同输入回读，防止prepare_mainline_household_states覆盖掉实验桥。
阶段D：只有对照同输入并都达到可比轮数时才比较价格桥机制，报告边界频率、KN/Y gaps、HA真实converged率、跨省结果；不能宣称稳态或政策Results。若无条件成立，保持TEMP受限观察并E3请Owner判断是否单独提出宏观约束简化方案。

## 管理和停止

- 当前**可以开展研究规划、来源差异/方程梳理**，不能自动启动Codex科学调用、HA/KFE/GE/IRF、旧100轮续跑，旧科学预算没有余额。
- 独立交付 review 候选`1579e7f1d7a1975c322dd6ae9af1776e88e83e7c`仍为REVIEW_PENDING_IO；原始ZIP尚未完成独立机器全成员核验与语义审阅，须保留远端三件，不提前清理。
- 下一步科学执行须Owner核准精确来源、同一长期任务总预算、HA调用次数、停止条件、原件隐私与验收；新的科学意见不从此brief自动变更正式V010合同。
