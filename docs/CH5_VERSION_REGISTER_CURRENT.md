# 第五章路线图与版本登记

## 2026-10-13 当前：V0.0.3 由 Owner 启动版前规划，等待 Codex（未冻结）

`DRAFT__WAIT_CODEX_EXECUTION_PROPOSAL__NO_IMPLEMENTATION_AUTHORIZED`。Owner 已明确启动 V0.0.3；Astra 已发布 [V0.0.3 corrected producer 联合身份与安全读取草案](../versions/0.0.3/plan.md)。Codex **仅只读**编制执行方案；暂无冻结计划、独立实施许可、模型/tests 或真实 protected 文件读取权。V0.0.1 与 V0.0.2 均按原限定资格 ACCEPT/CLOSED；V0.0.2 固定候选 `8f5457947492eef552f4261f8630c6c886af9fa5` 仅为建议下一版代码/文档来源基线，`NEXT_BASELINE_ADOPTION=UNDECIDED`，原工作树与 main 不作自动合并。

本版针对真实 corrected producer 的 policy/mass/Q/checkpoint/收益/省份联合身份合同与 Owner 最小受保护读取申请包，**不再叠加模拟 seal**。旧 `C9 PAUSED`、A16 `FAIL_CLOSED`、`CALL_LEDGER_UNRESOLVED`、`Results FALSE`、人口/人均决策及所有旧数据/科学 0 新许可均保持。V0.0.4 NOT_STARTED。


## V1.2 后续交付与证据登记补充（2026-10-13，规范性说明）

本节为 V0.0.2 复盘后的**长期治理规则**，补充 V1.1 登记要求，不改变 V0.0.1 / V0.0.2 冻结计划、实施授权、已有执行报告、验收和复盘原件。**V0.0.3 是否启动仍以最近状态与 Owner 指令为准**，本段不构成派单。

后续版本的原登记字段继续有效；执行交付另外分开记录：①前置依赖命令是否 fail-fast，以及发生失败后实际继续/停止的路径；②新文本记录的 UTF-8/LF 与最终 Git 差异检查情况，编码/显示错误单独分账；③ `PRE_FINAL` 公开摘要与**终端候选 tree/commit** 的身份、最终运行进程/退出码、私有或可发布交付回执 SHA 的区别（不得自引用候选哈希）；④首次及其后每次 focused 测试的可测资源记录与不可测 `UNKNOWN`，禁止追填缺失历史值；⑤候选基线是否已经包含前版被接受的代码，与 `main` 是否合并仍单独证实。

以上是**每版本依实际复杂程度提交的简明证据项**，不新增固定测试次数、额外审批角色、额外候选推送或强制第三方验收。实际独立阅读 GitHub 源码/commit/测试设计与本地执行方报告的 raw receipts 必须区别；存在无法获取的原始终端回执时，按证据限制验收，不把测试摘要哈希冒充独立重跑。具体流程详见 [V1.2工作流](CH5_ASTRA_WORKFLOW_CURRENT.md)。


## 2026-10-13 当前：V0.0.2 最终有限接受并关闭

**终态 `CLOSED__ACCEPT__SOURCE_CONTRACT_AND_SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`。** Astra 依据不可追改冻结计划 `4b11c46823e7cdabc12de8b8036cc5efc2380c52` / blob `43171bc6b841695845e7576d7feaa3135b88c588` 与实施授权 `3ed139aee7563a7033fa02fb933c3b49f24bd6b1` 对 Codex 候选作了 GitHub 独立静态审查。候选 commit `8f5457947492eef552f4261f8630c6c886af9fa5`、tree `af2a6a3d85f7525d480ad7da1916eaa25bf349b1`、唯一 parent `3260ec393dd4d53d6aab6c34d7c0442f09aa79f4`，分支 `codex/ch5-v0.0.2-household-source-contract`，只新增五个已授权源码/测试/证据路径；候选不合并 main。

- 正式冻结：[V0.0.2 计划](../versions/0.0.2/plan.md)；[独立授权](../versions/0.0.2/authorization.md)；[Astra 验收](../versions/0.0.2/acceptance.md)；[版本复盘](../versions/0.0.2/retrospective.md)。执行文件仅存在候选代码提交： [crosswalk](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/8f5457947492eef552f4261f8630c6c886af9fa5/versions/0.0.2/source_crosswalk.md) / [execution](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/8f5457947492eef552f4261f8630c6c886af9fa5/versions/0.0.2/execution.md) / [public JSON summary](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/8f5457947492eef552f4261f8630c6c886af9fa5/versions/0.0.2/acceptance_summary.json)。
- Codex 集中报告精确树测试 `62 passed, exit0`、总 focused 进程 `6/12`、含保守起始计费时间 `2810.44/10800s`、本版存储 `26,887,236/176,422,912B`；这些运行/原 checkout 完整保全为 `CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，网页独立只核 GitHub 代码、测试和公开报告，不冒称亲自重跑/读取本机原始 JUnit。
- 公开摘要在最终准确树测试前封存，未内含最终测试/提交身份；第六次运行及两项最终私有 receipt SHA 由 Codex/Owner 额外交付。run01/02 RSS UNKNOWN、CRLF/GBK/UTF-8 与第5次中间树误续测等真实偏差见验收和复盘。
- 本版只是内部 simulated digest/seal 与合成 typed contract，通过不证明外部 REAL 源身份、protected asset 联合真实性、真正家户运行或经济单位；`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `FAIL_CLOSED`、`model_activation=False`、`Results FALSE`、旧 CLOSED 预算、人口/人均与不 `N=P/3` 均保持。
- `NEXT_BASELINE_ADOPTION` 对 **V0.0.2** 已固定从 `3260ec393dd4d53d6aab6c34d7c0442f09aa79f4` 采用；**V0.0.3** 尚未启动且尚未选定代码基线。接受候选不等于已合并 main 或未来一定采用该候选；Owner 以后明确启动新版本后才另行决定。

## 2026-10-13 V0.0.2 冻结及授权状态（历史，非现行）

- **状态**：`FROZEN__ASTRA_APPROVED_EXECUTION__WAIT_CODEX_IMPLEMENTATION`。Owner 已启动 V0.0.2 版前规划，Codex 提交完整 `V0.0.2_EXECUTION_PROPOSAL_DRAFT`，Astra 审议后选择窄合成 source-boundary，完成冻结和独立实施授权。此状态仅说明可以启动受限工程，**尚无实施、测试或候选的通过证据**。
- **正式不可追改计划**：[V0.0.2 plan](../versions/0.0.2/plan.md)，固定 freeze SHA `4b11c46823e7cdabc12de8b8036cc5efc2380c52`，plan blob `43171bc6b841695845e7576d7feaa3135b88c588`。版前草稿存于历史固定提交 `5cfe41fd0a66877565accca3c8e7dc9a71fa35ee`，不是现行执行合同。
- **独立实施许可**：[V0.0.2 authorization](../versions/0.0.2/authorization.md)，固定提交 `3ed139aee7563a7033fa02fb933c3b49f24bd6b1`；裁决 `ASTRA_APPROVED_EXECUTION__CH5_V0.0.2__SYNTHETIC_SOURCE_CONTRACT_ONLY`。
- **代码基线** `NEXT_BASELINE_ADOPTION=ADOPTED_FROM_EXACT_SHA`：前一版合成工程已接受的 commit `3260ec393dd4d53d6aab6c34d7c0442f09aa79f4`，tree `39e7a91ca473ba770bd65518607c3f78f4b9fe24`。仅作为本版本精确新候选树起点，**不合并 main、不移动原本地分支/HEAD/index**；远端目前不得假称 main 已包含。
- **文件/分层预算**：仅新增来源 metadata 工程模块与 focused 测试，以及 `versions/0.0.2/source_crosswalk.md`、`execution.md`、`acceptance_summary.json`；候选分支 `codex/ch5-v0.0.2-household-source-contract`。工程上限3小时、最多12次 focused pytest/次<=120秒、目标单进程1GiB。新增存储128MiB Git 操作 +32MiB isolated candidate_view/fixture +8MiB LOCAL_ONLY回执 +256KiB公开脱敏报告，合计<=168.25MiB。**真实科学/受保护数据/旧任务预算 0**。
- **科学资格上限**：仅 `SOURCE_CONTRACT_AND_SYNTHETIC_ENGINEERING`；真实 producer、真实数据/31省、HJB/KFE、C8/C9/C10、GE、Results、生产均非本版目标且不授权。只有明示 `SYNTHETIC/NOT_REAL_SOURCE` 准入，模拟 seal/hash 不能证明真实性。人口/人均保留、户均封存、不 `N=P/3`。旧 `C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `FAIL_CLOSED`、`model_activation=False`、`Results FALSE` 与 CLOSED 预算不变。
- **候选执行与终态**：Codex 版本内无实时监督自主管理合成工程，在冻结标准内修复与集中交付；仅正常 non-force push 受限候选一次并准确 readback。执行报告/最终候选 SHA/tree、Astra acceptance/retrospective 均 **NOT_YET_AVAILABLE**；收到候选后独立审议，不预先接受、不自动启 V0.0.3。

## 2026-10-13 V0.0.2 版前 DRAFT 记录（历史，不能用作执行授权）

Owner 已确认 V0.0.1 的收尾完成，并于本轮**手动要求开始下一版本规划**。Astra 草案：[V0.0.2 来源契约与输入准入计划](../versions/0.0.2/plan.md)。当前 `DRAFT__WAIT_CODEX_EXECUTION_PROPOSAL__NO_IMPLEMENTATION_AUTHORIZED`；Codex 仅可对已授权源码做有限只读核查并交一份执行方案草稿。版本尚未冻结、未颁布独立实施许可、没有新模型运行或新测试授权。

V0.0.1 `CLOSED__ACCEPT__SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`；其 accepted candidate SHA `3260ec393dd4d53d6aab6c34d7c0442f09aa79f4` 与原代码基线、`main` 均须分开记录。`NEXT_BASELINE_ADOPTION=UNDECIDED`，候选默认不合并、不切换、不等于正式下一版代码基线。Owner 未采纳新的真实科学/数据执行许可，C9/Results/A16/ledger/未知经济单位照旧。


## V1.1 后续版本登记约定（2026-10-13，规范性说明）

本规则在 V0.0.1 `CLOSED__ACCEPT__SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS` 后生效，**不重写该版的冻结计划、验收、复盘或历史版本登记**；新版本未启动。与旧记录中“待创建”的时态冲突时，优先按上方最近状态判读。

每个新版本由 Owner 明确启动；至少登记：版本 ID/状态及 Owner 启动出处、Astra 草案与 Codex 执行方案、**正式冻结计划的不可变 SHA/blob**、授权 SHA/边界、模型代码基线 commit/tree、真实模型 worktree/remote、候选 commit/tree 与分支、允许的变更路径、明确独立的工程/科学/数据/操作性存储/脱敏证据预算、测试与证据资格、执行报告和原始本地回执身份、Astra 独立验收、复盘及终态。没有必要的资源上限可写 NOT_APPLICABLE，不为形式主义机械复制旧预算。

**增加独立字段 `NEXT_BASELINE_ADOPTION`**：`UNDECIDED` / `ADOPTED_FROM_EXACT_SHA` / `NOT_ADOPTED`，含依据和固定 commit；候选接受不自动意味着进入 `main` 或下一版代码基线。可分开登记 `MERGED_TO_MAIN` 的实际 Git 证明，缺失则 `NOT_MERGED/UNKNOWN`。文档分支与代码分支分离时，执行报告必须链接其**真实存在的固定候选 commit**，不能使用指向文档分支而不存在文件的相对路径。

集中交付至少含实际代码与 Git 可核身份、简短脱敏测试/资源/保护摘要及私有原始回执的哈希和访问界限；Astra 在验收中显式区分 `INDEPENDENTLY_VERIFIED_GITHUB_CODE`、`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`、`UNKNOWN`。失败、Owner 限定例外及预算使用如实累积记录，冻结计划不事后重写。详见 [V1.1工作流](CH5_ASTRA_WORKFLOW_CURRENT.md)。


## 2026-10-13 现行：V0.0.1 最终接受并关闭

- **状态：`CLOSED__ACCEPT__SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`**。Astra 已独立核对 Github 固定候选身份、三文件增量、源码/测试与执行报告，接受合成工程范围，保留本地原始回执未直接复核的局限。
- 正式冻结计划（绝不追改）：[V0.0.1 plan](../versions/0.0.1/plan.md)，冻结提交 `6c9a13bdf6a54913d8f16b5ec23fdda2a68f28e8`，blob `065cfaf699db99f36d0fb05f037986ba22479298`。
- 独立实施授权：[authorization](../versions/0.0.1/authorization.md)，提交 `837b99dff12f1b263fd7f4b80c43e19cf4efaa48`。
- Codex 代码候选：[3260ec393dd4d53d6aab6c34d7c0442f09aa79f4](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/3260ec393dd4d53d6aab6c34d7c0442f09aa79f4)，tree `39e7a91ca473ba770bd65518607c3f78f4b9fe24`，分支 `codex/ch5-v0.0.1-synthetic-household-bridge`，与原代码基线 `a1db8c114dec0ab69d69a5576e153a7f868cba0e` 直接相邻；仅新增合成源码、测试与脱敏 execution。
- Astra 最终结果：[独立验收](../versions/0.0.1/acceptance.md)；[偏差复盘](../versions/0.0.1/retrospective.md)；[执行报告](../versions/0.0.1/execution.md) **仅存在于独立候选分支**，此处应读固定候选链接：https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/3260ec393dd4d53d6aab6c34d7c0442f09aa79f4/versions/0.0.1/execution.md 。勿将相对路径误认文档分支中已拥有该文件。
- Codex 报告 candidate_view 42/42 通过、4/8 focused 进程、最终新 EVIDENCE≈1.87MiB、墙钟≈21分钟；网页独立核查源码/42例静态设计及 Git SHA，但未直接复跑 Windows 私有 raw receipts。初始临时 Git index 超10MiB证据配额真实失败，后获 Owner 受限运维修正后恢复，未追改冻结科学/工程标准；记录于验收/复盘。
- 本版**不支持** HJB/KFE/31省来源真实性、经济劳动单位、真实生产 callback、K1B/GE/收敛、Results、发布。旧 `C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、Objective A16 `FAIL_CLOSED`、`model_activation=False`、`Results FALSE`、旧预算和人口/人均决定保持；生产未接受。
- **下一版 NOT_STARTED、没有 ISSUED、没有自动派单。** 后续路线由 Owner 新指令另行启动版前协商。候选 branch 不自动 merge main。当前本地脏工作区及未跟踪资产不由本网页验收追认其字节完整性。

## 2026-10-13 V0.0.1 立版与实施记录（历史）

- **版本 `0.0.1`：`FROZEN__ASTRA_APPROVED_EXECUTION__WAIT_CODEX_IMPLEMENTATION`。** Owner 启动第三阶段；Codex 已提交 `V0.0.1_EXECUTION_PROPOSAL_DRAFT`，Astra 审议后批准其纯合成工程方案。
- **不可修改的正式冻结计划**：[V0.0.1 plan](../versions/0.0.1/plan.md)；冻结提交 `6c9a13bdf6a54913d8f16b5ec23fdda2a68f28e8`，plan blob `065cfaf699db99f36d0fb05f037986ba22479298`。
- **独立实施许可**：[authorization](../versions/0.0.1/authorization.md)；发布提交 `837b99dff12f1b263fd7f4b80c43e19cf4efaa48`，其中含 `ASTRA_APPROVED_EXECUTION__CH5_V0.0.1__SYNTHETIC_HOUSEHOLD_BRIDGE_ONLY`。
- 代码基线截点 `a1db8c114dec0ab69d69a5576e153a7f868cba0e`，本地既有 dirty/untracked/ignored 不包含在该 SHA，Codex 启动前须 fresh-readback 与保护。
- 本版本仅准新的显式合成模块/测试、受控 isolated candidate_view、专属本地 EVIDENCE、脱敏执行报告；focused 工程预算 <=4小时、<=8个测试进程/每个<=120秒、目标<=2GiB、证据<=10MiB；真实科学/模型与受保护数据运行预算 0。
- Codex 在冻结边界内自主实施、调试和聚焦验证，集中发布一次候选供 Astra 最终独立验收。当前**仅为授权就绪**，尚无实际实施或通过证据；`execution.md`、`acceptance.md`、`retrospective.md` 仍待产生。
- 不更改旧 C9 PAUSED、CALL_LEDGER_UNRESOLVED、A16 FAIL_CLOSED、Results FALSE、劳动单位 UNKNOWN、既有经济法则、已关闭预算。**本登记不覆盖 plan 冻结原件。**

## 2026-10-12 第二阶段迁移记录（历史截点）
迁移后首版：**尚未制定，等待第三阶段**。Owner手动启动；本轮没有新版本号、批准、执行或通过记录。

## 路线图入口
历史[两资产路线图](CH5_TWO_ASSET_HANK_ROADMAP_CURRENT.md)及[Python重建路线图](DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md)保留现有内容和证据级别，不能由旧“下一步”直接启动。未来路线更新不能改原冻结版本。
当前优先未闭问题：真实solver来源绑定、聚合/frozen实际调用、frozen→batch构造、callback装配、量纲/人口分母/时点及科学运行与环境/保护。它们是问题清单，不是第三阶段执行计划。

## 后续登记约定
Owner确立版本后，在此登记：版本标识及阶段、正式计划路径和冻结依据（批准来源及固定提交）、代码基线与候选SHA、实际执行报告、独立验收、复盘位置和终态。
可采用`versions/<Owner确立的版本标识>/plan.md`、`execution.md`、`acceptance.md`、`retrospective.md`；这些是命名约定，目前全部待创建，不是现存链接。草稿仅版前协商。冻结计划不可事后改目标；修复批次针对原目标内缺陷，新增需求入未来版。

## 历史登记与固定证据
- 历史K1B等冻结版本：原件/原状态不重写。已有[科学合同账固定快照](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/a1db8c114dec0ab69d69a5576e153a7f868cba0e/SCIENTIFIC_DECISIONS.md)与[双边资本网络冻结稿固定快照](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/a1db8c114dec0ab69d69a5576e153a7f868cba0e/docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md)。
- 上述SHA是本地提交已存在于远端备份分支的文件快照，不是各合同首次冻结提交或全部验收基线的追认。逐版本原冻结/代码/验收commit尚未从完整历史逐一核出，记UNKNOWN，不补造。
- 最新接受为scripts/tools metadata门ACCEPT/CLOSED；末binding SOURCE_ONLY门NOT_ACCEPTED/CLOSED，见[近期账快照](knowledge/published/CH5_WORK_ACCEPTANCE_LEDGER_MANUAL_HANDOFF_20261011_140603Z.md)。这些旧stage不是迁移后新版本。
- 各历史执行/复盘资料未全量覆盖，若需要立版必须按具体问题核原件。备份≠验收，自测≠最终验收，验收≠发布。

## 第二阶段执行端交接（不登记为新版本）

[Codex实时交接](CH5_ASTRA_CODEX_EXECUTION_HANDOFF_CURRENT.md)及[Owner手工启动Prompt](CH5_ASTRA_CODEX_NEW_SESSION_PROMPT_CURRENT.md)补充本地封存状态。发布基线3ec76075c90f823ed83ca6e0a8c385a61f79ef85；本次文档提交以发布回执及分支fresh-fetch为准。本地代码HEAD不移动；迁移后首版NOT_STARTED，等待Owner第三阶段。交接文件准备完成不等于新会话已实际接收。
