# V010 runner guard / I/O 离线集成：GitHub 脱敏候选独立静态审议

**审议日期**：2026-10-16（北京时间）；**性质**：独立GitHub源码/静态数据核验，非Windows runtime或科学运行。
**裁决**：`V010_RUNNER_IO_GITHUB_DELIVERY_INDEPENDENT_STATIC_REVIEW_COMPLETE__LIMITED_STATIC_DESIGN_ACCEPT__FULL_RUNNER_IO_BLOCKED__NO_RUNTIME_AUTHORITY`。
**四项分账**：
- `STATIC_DESIGN_READY = CONDITIONAL_LIMITED_ACCEPT`（明确限于未执行文本结构和机读静态定义）。
- `FULL_RUNNER_IO_CLOSURE = BLOCKED / NOT_ESTABLISHED`（不能由静态防护意图推断Windows实测或全I/O有效）。
- `ENGINEERING_RUNTIME_NOT_RUN = TRUE`。
- `HA_SCIENCE_NOT_RUN = TRUE`。无GE、正式IRF、Results资格；`V011 NOT_STARTED`。

## 1. 权威与Git谱系：连接器实际回读

唯一原ACTIVE任务仍为`V010_RUNNER_GUARD_IO_OFFLINE_INTEGRATION_AND_SANITIZED_GITHUB_HANDOFF`，任务发布commit `50fece7d51bbcbb7e4384b0a5a8833b81dcbf76b`、tree `c79f874a1ea60f3a880114fd5d80b0861e6ca21e`、任务blob `0070437d83eccaaf4a1c38838e9ce2b1a2fb5634`；本审议**不重复下发任务、不产生新执行许可**。

审议前治理branch `migration/astra-workflow-20261012` HEAD为交接commit `0d59fde4131d8b3d7551eac7f6918f127374c340`，tree `3cbfd353780a737baadc2d890cb20230e6c09514`，原交接文档blob `3200af36532af51b92f90828d3ddf5645701fbb6`。这是固定恢复锚点，不应由本报告追改。

GitHub review分支 `review/v010-runner-io-offline-20261016` 已存在；独立核原始Git commit对象：candidate `c207e866cf70d9d5ae6fb245f43cabfdeac1d32b`、tree `b4ba5b7939653a0cdb8524fa82743d9634d79083`、**sole parent `50fece7d51bbcbb7e4384b0a5a8833b81dcbf76b`**。同task发行commit比较 `ahead=1,behind=0`；仅增加以下三个Git文件，原tracked文件没有修改/删除：
1. `versions/0.0.10/review_runner_io_offline_result_20261016.md`，Git blob `73daf247c2a6bcf44e9ca65dcbc0af893e72ec55`，UTF-8 8425B（不超过30KiB）。
2. `versions/0.0.10/review_runner_io_offline_static_draft_20261016.txt`，Git blob `dac0cf74364843f7e0f8b5cbebdbb3481a4ff329`，31373B；独立UTF-8 SHA-256 `3FF7B5D6FBEF57CE851C327EA5C6E6CA8200C852A3C1629586F3AC584FACFF11`，与报告一致。
3. `versions/0.0.10/review_runner_io_offline_static_cases_20261016.json`，Git blob `8d221ad63471427223b81087121b0067f649b23f`，188210B；独立UTF-8 SHA-256 `5B7D1B661FFF84F5844B15AE5104307B0FDEA0A23F70B809FBAC7A29E351A1CC`，与报告一致。

三件合计UTF-8字节228008B。均已核为UTF-8/LF、无BOM、以LF终结。对三份公开文件作静态正则筛查，未发现明确私有Windows用户绝对路径、原D盘保护目录、标准GitHub/OpenAI token式密钥、PEM私钥或个人邮箱；该检查只证明**指定模式未命中**，不能代替本地原证或证明所有秘密绝无外泄。1 ahead/0 behind及单提交**不能独立证明非force push次数恰为1**，只能证明最终Git谱系满足单父白名单结构。

## 2. 独立静态内容审查

候选TXT是643行的**未执行非可执行发布文件**，含 `GitGate.verify` 对四条身份真实有界child结果的比对与exit/reap/audit条件、`VerifiedFinder.disk/check_loaded` 的原磁盘字节Git Blob认证、`bounded_child` 的双管道预算/timeout/Windows Job清理草案、单一 `sys.addaudithook` 注册点、`Writer` 的写前字节计账/排他事务/final及emergency预算/日志reservation和watchdog退出路径。草案声明无自动入口；本轮**未导入、未编译、未运行、未进行Windows审计事件验证**。

此外以固定模型代码commit `94de4501dec051b969bee9d852eba2d4591f30ef` 实际fetch_file，逐一核候选 `NEEDED` 中9份 `src/ch5_two_asset_hank/` Python源文件的Git Blob值，**9/9与草案所列一致**。这仅证明GitHub的固定commit源码身份，不证明Windows本机将来加载的文件或实际`__file__`已经验过。固定V010科学plan blob `85138d8859d53295262fe13bf5bc277bca95ed3f`、原fixture blob `40915658d93403cfc21b33a6b864b332b7857749`、单点manifest blob `c23d331bed34e5ca478324cdc05034609ecb91b7`并未改变。

JSON已独立解析：46个唯一主ID（A01–A08 8个、D01–D16 16个、N01–N22 22个）、另有23个`variant_cases`静态replace变体，主例必需键存在且所有`expected.source_anchor`能在TXT里找到对应字面标识。每个主例标注`runtime_execution=NOT_RUN`、`runtime_pass=false`；23个变体亦为NOT_RUN。字面锚点/JSON结构审查**不是逐例运行，也不是证明全部ALLOW/DENY与Python/Windows实际一致**；原24例从旧本地JSON映射的真实性、PowerShell历史过程仅Codex回执支持。

## 3. 保留阻断项与等级

- **HOOK来源/叠加**：新草案只检查自己设置的 `sys._v010_offline_hook_installed`，不能枚举或证明进程中不存在其他预装 `sys.addaudithook`。N09标识了该风险，但预装其他hook不设置此标志时仍无法从本静态草案证明排除。须以未来全新受控解释器、可信启动过程及工程实测核证；不得把“单一注册点”当作“全进程仅一个hook”的已证事实。
- **未来科学权限真绑定不足**：`one_ha` 中 `new_science_authorization_blob`目前只检查为长度40的字符串，未与未来Owner明确批准的固定SHA/科学输入与额度作权威匹配。此字段**不是科学许可**。即使工程preflight后来完成，`ONE_HA`依旧保持未获授权，未来科学门须另行建立并独立核验。
- **范围/OS边界**：Hook聚焦若干Python审计事件与显式文件/子进程路径，不能证实覆盖所有原生I/O、网络/扩展库/并发替换；草案明确依赖可信Windows、可信Git/Python、独占新root且无恶意替换。这不是OS沙箱，也不是A16安全解除证明。
- **未经过runtime**：Job Object API布局/分配、Windows真实argv审计形态、stdout/stderr对抗超限、timeout/reap、拒绝分支、路径别名、异常封存、日志最终预留、源码实际载入等均**尚无运行回执**。TXT也没有本轮AST/Python语法独立验收，不能假装已经执行。
- **本地证据边界**：Codex所报0 Python/0 HA、独立scratch≤5文件/2MiB、读文件≤12件/5MiB、≤3小时、原dirty/index/common-dir未访问以及非force仅一次push，GitHub端不能完全复验，归类`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`或`UNKNOWN`，不是Astra亲历；旧actual Windows argv仍未由旧receipt保存。

上述发现不自动否定静态设计的方向价值，但足以令`FULL_RUNNER_IO_CLOSURE`维持BLOCKED，更不构成科学数值或工程运行PASS。

## 4. 审议后任务/资源/保护

**最新任务身份不变**，现在状态为`CODEX_DELIVERY_RECEIVED__INDEPENDENT_STATIC_LIMITED_ACCEPT__NO_RUNTIME_AUTHORITY__WAIT_OWNER_ENGINEERING_GATE_DECISION`；这不是新任务签发或科学候选升级。可在Owner另行决定时讨论**独立ENGINEERING_ONLY Windows preflight**的精确一次性许可、合格条件、运行前可信解释器与bootstrap日志/进程账；不能在本报告中默认执行。预检之后是否允许独立`ONE_HA`，还必须再次单独经Owner批准及绑定真实许可。若要修静态缺口，亦不追改冻结V010计划。

原V010实施预算Codex报告：pytest 4/6、science driver 1/4、HA 1/26、selector cells 1626、scalar roots 1642，继续记账。原两次单点preflight各Python1/1消耗、HA均0；首次GBK异常产物43,519,638B超旧32MiB 9,965,206B，第二次Windows argv审计误拒产物117,446B在96MiB内；原单点 `rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07` corrected HA仍从未执行。不得回滚/重置/覆盖。

`A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`model_activation=False`、`Results FALSE`、`real C8 A-D REQUEST_ONLY`、原8 dirty tracked/index/staged/untracked/ignored/外Git common-dir保护、`V011 NOT_STARTED`不变。GitHub同步不证明本机QMD/Basic Memory已更新。

**最终停点：`WAIT_OWNER_V010_ENGINEERING_ONLY_PREFLIGHT_DECISION / STOP`。**
