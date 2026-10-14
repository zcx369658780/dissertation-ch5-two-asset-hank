# V0.0.6 独立最终验收：固定 C8 联合来源—三轴—双消费者合成合同

2026-10-14（Asia/Shanghai）

**终态：CLOSED__ACCEPT__SOURCE_ONLY_IMPLEMENTATION_AND_SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS**

本验收只接受冻结合同内的 SOURCE_ONLY 联合工程和隔离合成测试；不认证 original C8 真正原件、历史执行身份、经济量纲、real observed/consumer、Objective A/window、K1B固定点/GE或Results。未改变任何已采纳的 HJB/KFE、raw-ra0、lagged timing、S、C1和人口/人均科学合同。原 V0.0.5 仍保持有限关闭。

## 1. 正式不可追改权威

- Owner启动 V0.0.6：既有治理提交 `8b6fec04690aae05d2b3eeeffb2d2a981f5ce605`。
- Astra正式冻结：commit `4857d9222580b491676cdf75951527eb06d16b49`，`versions/0.0.6/plan.md` blob `5c96485f9b70c4c4033675134768b1ff4fe2d188`。独立会话授权为 `ASTRA_APPROVED_EXECUTION__CH5_V0.0.6__SOURCE_ONLY_AND_SYNTHETIC_JOINT_BINDING_ONLY`；不能把冻结计划文件自身当作授权。
- 唯一可采纳代码基线 `cf74384f151427f0b7071ac0461cede6ad6cdf11`，tree `372c693ca3dccea716ae8caef382f513e5a2316e`；本版候选 `198b70f8b1c7b802bc2e18cb4bb0825bdb495b00`，tree `0c637893d92cafdf72a194b350b3bf7016894d5c`，唯一 parent 等于基线。GitHub compare 1 ahead / 0 behind，8个文件全部在冻结白名单，未合并 main。
- 候选分支 `codex/ch5-v0.0.6-fixed-c8-joint-synthetic`，GitHub branches-where-head 回读确认当时远端该分支 HEAD 指向候选。主分支不同，不能假定下一版自动采用候选。

## 2. Astra独立读过的GitHub对象和验收结果

证据等级：`INDEPENDENTLY_VERIFIED_GITHUB_CODE`。
- 新 `fixed_c8_source_contract.py` 使用 existing ArchiveDeclaration / InputDeclaration、五字段 Ct/Lt/At/Bt/AtTax 的 synthetic roles、2017/2018 回溯时点和价格归属未验证状态，明确 `source_authenticated/runtime_authorized/model_activation/results=False`；历史 producer 路径是 documented crosswalk，不是本版执行 pin。
- 新 `fixed_c8_joint_preparation.py` 实际实现一次性 `JointPreparation`、before-consumer 检查、对原状态/五字段/params/S/迁移wedge的不可混同快照与 signed-zero 比特比较、年度master和31省三轴/terminal checkpoint 联合比对；普通工程身份和引用检查不是 hostile protection seal。
- 修改 `integration.py` 在 V0.0.6 synthetic C8 接入 `joint.begin`，在 labor、middle、wage 周围做 `recheck`，完成或异常路径调用 `close`；只准 SyntheticSpies 和已准备的 synthetic middle，observed/production 仍拒绝，`model_activation=False`。
- 三份新增 V006 测试静态源码包含40个可收集的测试实例（参数化展开），覆盖五字段、布尔/非有限拒绝、跨轴/阶段/source/price/人口声明冲突、S方向及F字节哈希、负零、同年度master、old/new wages、origin/destination tax、frozen S/C1、失败后禁止后继、一次尝试关闭和显式受界模块加载。
- 代码仅改变8个允许路径：上述两个新增工程模块、`integration.py`、三份新增tests、`versions/0.0.6/execution.md` 和 `versions/0.0.6/acceptance_summary.json`。其余已冻结或受保护科学源码未在提交diff中变化。
- GitHub 候选树和原 V0.0.3 基线的 commit/tree/parent 核实；没有 GitHub Actions 可替代本地最终测试的 PASS（无CI statuses不能冒充FAIL，也不能冒充独立PASS）。

## 3. Codex本地运行、预算及证据限制

证据等级：`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，不是Astra在Windows独立复跑：
- pytest 开发进程1为35 passed、开发2为40 passed；最终封存 commit 的隔离 `final_view` 为40 passed、exit0，累计3/6个进程、失败0，最终约0.984秒/峰值约43.54MiB。Astra没有亲自读取LOCAL_ONLY完整 stdout/stderr/JUnit 或执行final_view。
- Codex报告新增存储保守计费约16.63MiB、计时采样1,142秒，均在已报的8h/290MiB限额内；瞬时Git pack峰值无连续实测，属于 `UNKNOWN`，不得称全阶段资源峰值独立认证。
- Codex报告原工作树HEAD/index/8个dirty文件哈希及5,948 untracked、4,553 ignored路径清单保持；网页没有读取D盘或C盘B3副本，故原工作树保全仅限本地回执等级。
- 公开 `execution.md` / `acceptance_summary.json` 特意为 `PRE_FINAL/PRE_SEAL`；最终 commit/tree/tests 存在于用户交付的外部 LOCAL_ONLY 回执。没有把报告自身的未来SHA假填为最终验证；不要求为自引用追加候选提交。

## 4. 受界通过项与保留缺口

**接受**：
- 完整五字段及 model0/annual1/external-ID 按全名join的合成联合输入合同；
- 静态documented C8 producer→terminal writer→mass selector 的来源映射，与真正运行独立分账；
- 同一个已准备annual master 在两个 synthetic 边界传递，年度phi正确定义为来源q减目的q；合成oracle检查旧目的省工资+来源税的migration与新目的省工资+目的税的wage；
- frozen S 目的行来源列、资本数量和独立合成 prior raw-ra0收益方向oracle、C1残差与firm先后关系；
- 一次性准备、失败拒绝以及签名/输入生命周期检查在合成边界确实实现。

**未接受/未证明**：
- 历史 original C8 的独立受信原件锚、实际producer执行版本、JSON/NPZ/receipts内容和31省运行联合身份；
- household At/Lt、人口NU、资本MU、迁移/firm劳动、工资与一个模型期的实际经济单位相容；
- 真实source-loader/observed与真实migration/C1/firm/wage消费者、资产保护 A16/window 和任何科学模型；
- 九分量K1B R2严格固定点、GE、policy Results或投稿级数值证据。

Codex提出的37文件/总4,112,384B后续精确读取申请，只记录为 **REQUEST_ONLY**。文件存在性、可信历史锚、保护准入与Owner新的逐对象、字段、次数、字节和操作授权均待定；绝不因本版CLOSED自动执行。

## 5. 终裁与版本保护

**CLOSED__ACCEPT__SOURCE_ONLY_IMPLEMENTATION_AND_SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS**

本版正常关闭、无需重复执行本版合成测试或制作多余“验收修复”微版本。下一版代码基线 `NEXT_BASELINE_ADOPTION` 仍须由下一次Owner立版后的独立决策确定；本版候选接受 ≠ main merge。V0.0.7 NOT_STARTED。

保留 `A16 UNRESOLVED/FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、`model_activation=False`、`Results FALSE`，旧真实 science/data/consumer 预算仍 CLOSED、D3-real/D4-real 未授权。真实科研M1尚未完成，继续遵循投稿成果优先策略和CH5_WORKFLOW_V1.2。
