# V0.0.2 · Astra 最终独立验收

日期：2026-10-13（Asia/Shanghai）

**最终裁决：`CLOSED__ACCEPT__SOURCE_CONTRACT_AND_SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`**

## 1. 不可变权威和交付身份

- 冻结标准：[`versions/0.0.2/plan.md`](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/4b11c46823e7cdabc12de8b8036cc5efc2380c52/versions/0.0.2/plan.md)，freeze commit `4b11c46823e7cdabc12de8b8036cc5efc2380c52`，plan blob `43171bc6b841695845e7576d7feaa3135b88c588`；本轮不修改该原件，也不因结果调整 G1–G4/A–G 标准。
- 实施授权：[`authorization.md`](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/3ed139aee7563a7033fa02fb933c3b49f24bd6b1/versions/0.0.2/authorization.md)，固定提交 `3ed139aee7563a7033fa02fb933c3b49f24bd6b1`。
- 获批单父代码基线：`3260ec393dd4d53d6aab6c34d7c0442f09aa79f4`（V0.0.1 accepted candidate）。
- 实际候选：[commit `8f5457947492eef552f4261f8630c6c886af9fa5`](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/8f5457947492eef552f4261f8630c6c886af9fa5)；tree `af2a6a3d85f7525d480ad7da1916eaa25bf349b1`；唯一 parent `3260ec393dd4d53d6aab6c34d7c0442f09aa79f4`；候选分支 `codex/ch5-v0.0.2-household-source-contract`。
- Codex 文件：[source_crosswalk.md](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/8f5457947492eef552f4261f8630c6c886af9fa5/versions/0.0.2/source_crosswalk.md)、[execution.md](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/8f5457947492eef552f4261f8630c6c886af9fa5/versions/0.0.2/execution.md)、[acceptance_summary.json](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/8f5457947492eef552f4261f8630c6c886af9fa5/versions/0.0.2/acceptance_summary.json)。
- 许可范围与科学结果分离：本次接受**仅限 typed 模拟来源契约与 synthetic aggregate/frozen/batch 工程验证**，绝非真实来源认证、历史受保护资产许可、RUNTIME_REAL、数值收敛、科学有效、GE、Results、生产或一般隔离安全证明。

## 2. Astra 实际独立核验与证据分账

**INDEPENDENTLY_VERIFIED_GITHUB_CODE：**
1. GitHub Git-commit 元数据的 candidate tree 精确为 `af2a6a3d85f7525d480ad7da1916eaa25bf349b1`、唯一父提交 `3260ec393dd4d53d6aab6c34d7c0442f09aa79f4`；基线→候选恰好 ahead1/behind0；远端候选分支 HEAD 与此 SHA 相同。
2. 只有冻结允许的五个新增路径：`src/ch5_two_asset_hank/multi_province/household_source_contract.py`（204行）、`tests/test_v002_household_source_contract.py`（250行）、`versions/0.0.2/source_crosswalk.md`（132行）、`execution.md`（162行）、`acceptance_summary.json`（188行）；无既有模型源码、V0.0.1、冻结合同或生产默认文件的候选修改。
3. Astra 打开并检查新增模块、完整新测试、crosswalk、公开执行报告与 JSON 摘要；source blob `be63550e6adef05edc15ddfcd618577e72ab7fde`、test blob `9724362c7412c879a0872d8266b1fa2403b7903a` 等 GitHub 身份与候选一致。
4. 源代码 `admit_synthetic_household_record` 在任何转化/aggregate 之前强制 `SYNTHETIC/NOT_REAL_SOURCE`，核对独立请求声明的 simulation identity、严格字段集合、每字段身份/角色/sha256 与模拟 manifest 摘要、`(b,a,z)`/F-order；随后调用原 `CorrectedHouseholdAggregateInputs` 和 V0.0.1 `SyntheticHouseholdRecord`，拒绝未验证真实来源。 `assess_source_contract` 的评估结果**不能**跳过后续准入重检。模块未引入真实 loader、solver 或 production export。
5. 完整测试代码包含62个参数展开测试实例：确有单个两省合成集成测试显式调用实际 corrected aggregate、`frozen_output()` 和原 `build_synthetic_household_batch`，用三处非零质量格点的独立标量 oracle 比较 Ct/Lt/At/Bt/AtTax，测试原数组改变不影响 admitted snapshot，验证非合成/身份/期次/轴序/质量/收益角色的拒绝。测试还明确展示自洽但重新封存的转置可改变 Ct（5.6→4.7），防止自签名等同真实认证。
6. `source_crosswalk.md` 逐字段区分 MATLAB-faithful 与 corrected checkpoint 来源路线，说明 population/clock/price/real producer/closed asset 身份未知；公开执行记录保留测试前置失败及操作修复，不用 CODEX PASS 冒充 Astra 最终裁决。

**CODEX_REPORTED_WITH_LOCAL_RECEIPTS：**
最终精确 candidate tree 的 focused pytest `62 passed, exit 0`、总进程 `6/12`、运行前后71个导出 blob 匹配及实际模块来源属 candidate_view；第6次最终 UTC `2026-10-13T04:10:26.970483Z` 至 `04:10:27.833350Z`、用户交付计时0.875秒/峰值43,102,208B；最高已测峰值43,687,936B，前两次峰值 UNKNOWN。包括前置保守计时的墙钟界 `2810.44/10800秒`；本版新建存储 `26,887,236 / 176,422,912字节`。这些**并非** Astra 在网页环境直接运行/原始回执复算的结果。

最终本地测试回执 SHA-256（Codex/Owner 提供）：`7e39c2914e335ae49e6cfefa1b3d1b8cb0d487dbce41096596ce578d30e9a6d8`；最终原回执集合 manifest SHA-256：`13f5f38dd7037237c8b616d361d7b23c8581d72df4cb64af381eab31c1122520`。原 receipt、私有保护哈希、全部导出视图和完整 stdout/stderr/JUnit 仍 LOCAL_ONLY；不能仅凭这些字符串声称 Astra 已独立复算。

**UNKNOWN/NOT_VERIFIED：** 真实 source seals、联合政策/质量/Q/checkpoint 的资产认证，真实生产 callback、劳动力人口/效率/工时量纲、价格/年份/日历、真实31省科学运行、C9 收敛、经济/论文 Results、安全环境完整性。本机未跟踪/ignored 资产的逐字节内容没有被 Astra 独立核验。

## 3. 按冻结 A–G 逐项验收

| 冻结标准 | 判定 | 证据上限 |
|---|---|---|
| A / G1 逐字段 producer→consumer crosswalk | **PASS** | 静态源码/版本和历史 ACCEPTED 严格分账，不赋予真实运行资格 |
| B / G2 typed 模拟来源准入 | **PASS** | 非合成标签在本次新入口 fail closed；模拟 seal/digest 仅为自陈一致性 |
| C / G3 合成集成与 oracle、准入不升级 | **PASS WITH EVIDENCE QUALIFICATION** | 实际源码和62个测试定义可独立审阅；最终运行通过与 candidate_view 绑定依赖 Codex 本地回执 |
| D / G4 证据、资源、保护 | **PASS WITH OBSERVATIONS** | 分层预算报送在限内；完整本地原始收据未独立打开；前两次 RSS 未测量不补造 |
| E 科学防冒认 | **PASS** | 只证明 SOURCE_CONTRACT_AND_SYNTHETIC_ENGINEERING；真实 solver/source/data/单位依然 BLOCKED |
| F 精确 Git 候选与集中发布 | **PASS（远端身份）** | GitHub commit/tree/parent/五文件核实；单次 non-force push、原本地 index/dirty 未损属 Codex 回执 |
| G 异常/部分接受处理 | **PASS WITH OBSERVATIONS** | 失败和修正保存；无证据表明科学权限或冻结标准被擅自扩大 |

## 4. 明确保留的观察项与不接受的夸大

1. **公开的 `acceptance_summary.json` 是 post-seal final-tree 运行前封存的摘要。** 其状态仍含 `WAIT_FINAL_TREE_VALIDATION`，并记录前五次进程。不可将其自身称为包含最终第6次、最终 SHA/tree 和全部本地结果的完整原始执行回执；第6次由后续外部交付与 LOCAL_ONLY `delivery.json` 补足，网页未取得原件。自引用 commit SHA 无法安全写入自身，这种分离属明确披露的证据结构，并非事后改 summary。
2. **资源缺口：** run01/run02 的进程峰值未采集，记 `UNKNOWN`，只能说后续测得峰值低于目标，不能声称所有六次峰值均有实测。
3. **流程/工程偏差：** 记录了 test-first import RED；CRLF 导致 Git whitespace check 失败、GBK 输出/UTF-8读取错误；PowerShell 未阻断失败后的依赖命令导致第5次在**中间树**执行。该次计入 `6/12` 累积预算；最后第6次才据执行端报告绑定最终树。不能用第5次 PASS 为最终候选作证。
4. 模拟 manifest/field digest 没有独立信任锚，payload 与自报 metadata 可以协同改写、相同形状误映射可以自洽；本版的 `admitted=True` 只在**显式合成内存**范围成立，不等于“已经认证真实数据来源”，也不提供完整文件系统安全沙箱。
5. 原 checkout 的 HEAD/index、八个 tracked dirty 文件及 5405 untracked、4553 ignored 路径 Codex 报告保持；网页不能直接重算。既有未跟踪文件正文未做全量内容核查，保全资格不可升级。

## 5. 版本终态与后续边界

**`CLOSED__ACCEPT__SOURCE_CONTRACT_AND_SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`。**

候选继续在独立分支，不合并 `main`、不自动作为未来版本代码基线；下一版 `NOT_STARTED` 且无 ISSUED / 自动授权。Codex 不再对 V0.0.2 追加测试或修改。后续若需要真实来源/受保护数据/参数、科学求解或 producer 身份认证，须新版本版前协商和 Owner 特定许可。

`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `UNRESOLVED/FAIL_CLOSED`、`model_activation=False`、`Results FALSE`、旧 CLOSED 预算全部保持；人口/人均方向保持、户均封存，不使用 `N=P/3`。劳动量纲/人口分母/实际价格年份/时点与真实来源继续 `UNKNOWN`。
