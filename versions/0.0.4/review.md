# V0.0.4 Astra 版前独立审议：Owner 决策待定，保护未闭合

2026-10-13（Asia/Shanghai）

**裁决：`REVIEWED__OWNER_DECISION_REQUIRED__PROTECTION_BLOCKED__NO_READ__NOT_FROZEN`。**

这是版前审议文件，**不是**正式冻结计划、独立实施许可、模型测试任务、Windows 安全验证授权或受保护真实数据读取许可。原版前 `versions/0.0.4/plan.md` 继续保留 DRAFT，固定提交 `f5abef37cf7aa5b22c0b918782cc9a28daf60e5a` / blob `cda85bf01687b6e0fce9fffcfc57b5038f6358af`，不追改。本次只处理 Codex `V0.0.4_EXECUTION_PROPOSAL_DRAFT` 后的 Astra 审议和 Owner 待决事项。

## I. 科学/证据审核与结论

Astra 通过 GitHub 核验了原版前草案、V1.2 工作流、V0.0.3 固定[来源合同](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/cf74384f151427f0b7071ac0461cede6ad6cdf11/versions/0.0.3/producer_source_contract.md)与[读取申请](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/cf74384f151427f0b7071ac0461cede6ad6cdf11/versions/0.0.3/owner_read_request.md)，及历史[run004 31省完成初始 turn 的接受原件](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/8f5457947492eef552f4261f8630c6c886af9fa5/docs/CH5_MP4C_CORRECTED_INITIAL_TURN_FULL_CLOSURE_ACCEPTANCE_20260920.md)。历史 HJB/KFE/aggregate 31/31、integration-only replay 等只在原固定实验范围 `HISTORICAL_ACCEPTED`；不能证明北京当前原文件、子哈希或现有权限的有效性。checkpoint-11 固定 fixture、北京 checkpoint-12 方法诊断和 run004 初始运行不混配。

Codex 报告本轮模型 worktree `D:\ProjectTemp\c5k1bturn56`，原代码 HEAD `a1db8c114dec0ab69d69a5576e153a7f868cba0e`、index 哈希稳定、tracked dirty8、untracked5947、ignored4553、staged0。没有写入、没有受保护文件 stat/open/read/hash/探测、没有测试或科学调用。**这些是 `CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，网页未访问本机原 index、进程历史或受保护目录进行独立复测。** 同时 Codex 本轮 fresh host/projectId 确认 `UNKNOWN`，不能将前次 app 成员资格当作当前保证。

Astra 赞同 `PROTECTION_BLOCKED/NO_READ`：目前 Objective A16 `UNRESOLVED/FAIL_CLOSED`、window `UNACCEPTED` 的历史状态未变。按 Codex 的受界保护文件阅读，同一用户/获 ACL 权限的普通进程、父目录 `DELETE_CHILD`、祖先目录/junction/reparse 替换和句柄保护生命周期都属于可能相关的威胁；当前 principal/SID/token、实际可保证的窗口、祖先 ACL 与访问工具未知。**`resolve → stat → open` 和单次 checksum 不能独立证明抗竞态/合法权限**；本轮网页未亲自取得 Windows 安全证明，无法将保护由 FAIL_CLOSED 升级为 PASS。不得借启动版本、普通计划审议或替换工具/会话绕过保护。

## II. D1–D4：Owner 必须集中决定的范围（当前尚未决定）

- **D1 科学对象**：是否原则选择历史 run004 初始北京三份元数据，仅作为一次小规模**历史成员一致性**验证候选；接受原件和历史 manifest SHA 是拟核可信锚，不等于对本地当前资产认证。若选择也**不授权读取**。
- **D2 保护威胁模型**：建议完整保留现有 A16/window 风险边界（含同用户普通进程、祖先目录替换、重解析/junction、父目录 DELETE_CHILD 和读句柄生命周期）。任何缩小范围是新的明确 Owner 科学/保护风险决定，不能沉默豁免。
- **D3 具体工具/身份/预读探测/读权限**：未来须独立指定 principal/SID/token、访问工具及可证抗竞态设计、精确路径/祖先/ACL/句柄探测对象/次数和有效期、数据文件的 open/read/size/hash/parse 次数/上限、失败即停与零重试。在这些条件及 Owner 许可未通过前**连真实保护路径的 stat/exists/ACL/reparse probe 都为0**。
- **D4 生命周期与对外公开**：未来若允许，建议原文件字节只留受控内存快照并明确关闭/销毁，原始日志/ACL/机器细节 `LOCAL_ONLY`；Owner 决定原始回执访问者/保存期限、准确允许外发的非敏感匹配/缺口字段。既有本地历史资料及完整 manifest 不上传。

当前 `D1–D4=OWNER_DECISION_REQUIRED`。Owner 可先作 D1/D2 原则选择，随后另行获得 D3/D4 的准确可证安全方案，仍**不等于本版已有任何真实读取授权**。

## III. 仅用于未来讨论的三文件名单（REQUEST_ONLY）

历史源码推导根 `R=D:\ProjectTemp\c5k1bturn56\reports\ch5_mp4c_corrected_optionb_initial_turn_unique_closed_class_kfe_20260920_run004`：

1. `R\sealed_manifest.json`：候选1次、最多2MiB，历史 SHA-256 `CF70E7D6A62A35F461D1A75B28F8F502B2CBDD2D94ED5D9DDFA099D821CC5EC6`；
2. `R\household\p00_北京\province_terminal_receipt.json`：候选1次、最多64KiB；
3. `R\household\p00_北京\native_initialization_receipt.json`：候选1次、最多64KiB。

**合计候选3次尝试/2.125MiB（2,228,224 bytes）/重试0；不是已批准预算。** 要另行冻结 pre-read stat/ACL/祖先/句柄 probe 的对象及调用上限，不能藏在三次正文读取中。历史封存 manifest 的4353成员、61,650,777 total member bytes不在申请范围，禁止运行旧全量 verifier、扫描/散列其它成员。

即使未来真正获批且通过，也最多形成单个历史北京元数据内容/成员一致性受界证明，不能升级到 policy C/l、Q/p/g、完整进入状态、经济单位、真实数值收敛、31省当前可用或 Results/生产。

## IV. 版前终态与后续门

**`WAIT_OWNER_DECISION__NO_READ__V0.0.4_NOT_FROZEN`。** 不签发 `ASTRA_APPROVED_EXECUTION`，不创建工程候选、不运行测试、不读取/探测真实资产；不为避免版本阻塞再生成重复合同。Codex 推荐 `cf74384f151427f0b7071ac0461cede6ad6cdf11` / tree `372c693ca3dccea716ae8caef382f513e5a2316e` 作为未来候选基线，仍 `NEXT_BASELINE_ADOPTION=UNDECIDED`，不合并 main、不移动原 checkout。

如果 Owner 选择 D1/D2，则先审议是否存在**独立且符合全部安全威胁条件**的保护实现路径，不能预设纯 Python 是足够的。若保护不可证，保持 `PROTECTION_BLOCKED/NO_READ`；不能自动缩小既有威胁模型。本文件不是保护可行性 PASS。

V0.0.1–V0.0.3 各自 `CLOSED/ACCEPT_WITH_OBSERVATIONS`；`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、A16 `FAIL_CLOSED`、window `UNACCEPTED`、`model_activation=False`、`Results FALSE`、旧 CLOSED 预算、人口/人均保留与不 `N=P/3` 不变。V0.0.5 NOT_STARTED。
