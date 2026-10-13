# V0.0.1 · Astra 实施授权（独立于冻结计划）

日期：2026-10-13（Asia/Shanghai）

## 正式裁决

**`ASTRA_APPROVED_EXECUTION__CH5_V0.0.1__SYNTHETIC_HOUSEHOLD_BRIDGE_ONLY`**

网页 Astra 已审议 Owner 手动启动第三阶段后的 `V0.0.1_EXECUTION_PROPOSAL_DRAFT`，批准在正式冻结计划的严格范围内由 Codex **一次性自主实施、正常 focused 测试、必要普通工程修复和集中候选交付**。

冻结计划**固定提交 SHA**：
`6c9a13bdf6a54913d8f16b5ec23fdda2a68f28e8`

冻结文件：
`versions/0.0.1/plan.md`（blob `065cfaf699db99f36d0fb05f037986ba22479298`）。

该固定 SHA 优先于此后动态文档分支 HEAD。本独立授权文档只开启冻结范围内的实施，不修改原计划目标与验收标准。

## 已批准的实现与资源

- 当前获批源码基线 commit：`a1db8c114dec0ab69d69a5576e153a7f868cba0e`；真实 worktree `D:\ProjectTemp\c5k1bturn56`，按 Codex 草案已报告但必须实施前 fresh-readback。代码基线不包含 dirty 工作区成果。
- 仅新增 `src/ch5_two_asset_hank/multi_province/synthetic_household_bridge.py` 与 `tests/test_v001_synthetic_household_bridge.py`；另允许仅新建 `versions/0.0.1/execution.md`，和 `EVIDENCE/ch5_v001_synthetic_household_bridge/` 中的受保护本地 candidate_view、合成 fixture、测试回执与清单。
- 测试只限合成内存输入的非科学 one-turn 及其原有依赖；不得运行真实 HA solver 或 KFE、31省资料消费者、旧科学 runner、C8/C9/C10。
- 资源限额：总墙钟不超过4小时、focused pytest 进程最多8次且每次120秒、单进程目标内存不超过2GiB、本版新增证据不超过10MiB、科学/真实数据调用 0。
- Codex 可在冻结计划内自主确定编码顺序、普通缺陷修复与 focused 测试，无中途微步骤审批。任何新增科学定义、受保护数据/权限、重要 guard、更改现有 dirty 文件/源码和超预算，停止并报告。
- 只允许从明确代码基线以**精确路径、独立临时 index**生成候选 `codex/ch5-v0.0.1-synthetic-household-bridge`，一次普通 non-force push，完成远端 readback；不得覆盖已有分支或修改 `main`、本地原分支/HEAD/index，也不得合并 `migration/astra-workflow-20261012` 文档树。公开仅两份新增源码/测试、脱敏 execution 报告；本地私有 EVIDENCE 不外传。
- 模型正式生产接线、科学接受、稳态、GE、Results 和部署依然**禁止**；合成测试通过只支持 `SYNTHETIC_ENGINEERING`。

## 交付与验收

Codex 完成候选后提交精确 commit/tree、候选视图模块路径、原始测试回执/脱敏摘要、代码差异、关键错误拒绝、资源账与所有未闭科学/保护状态，并停止于 `WAIT_ASTRA_FINAL_ACCEPTANCE`。Astra 再按上述冻结计划独立验收、集中返修原目标缺陷，记录最终结果与偏差复盘。

若生产模块原本不支持合成小省份、需要触及禁止文件或不能安全验证 candidate tree，Codex **不通过修改冻结条件绕过问题**，须保留原证据并集中报告 BLOCKED/PARTIAL。旧失败与关闭预算不可重启。

这不是生产发布许可。旧 Work 不参与实时管理。
