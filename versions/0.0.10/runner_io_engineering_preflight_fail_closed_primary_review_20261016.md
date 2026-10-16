# V010 ENGINEERING_ONLY Windows preflight：阶段A Git对象可达性失败的Astra独立验收

**日期**：2026-10-16（北京时间）。
**审议终态**：`INDEPENDENT_GITHUB_DELIVERY_ACCEPTED__ENGINEERING_PREFLIGHT_FAIL_CLOSED_CONFIRMED__A_STAGE_GIT_REF_SCOPE_FAILURE__NO_RUNTIME_OR_SCIENCE_PASS`。
**裁决范围**：接受Codex遵守门禁而停止及脱敏材料的有限交付；**不**接受工程Windows preflight通过、不认证完整runner I/O、不追加Python或科学资源，不恢复同一个已STOP任务。
**下一停点**：`WAIT_OWNER_FRESH_A_STAGE_GIT_OBJECT_REACHABILITY_AUTHORITY / STOP`。目前**无新ACTIVE执行任务**。

## 一、精确GitHub证据及身份

固定Owner已批准工程任务 `V010_RUNNER_IO_ENGINEERING_ONLY_WINDOWS_PREFLIGHT` 的[发布commit](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/343c22132deb23ba6d913d70e132b43a00b95f1d)：`343c22132deb23ba6d913d70e132b43a00b95f1d`，任务blob `08fed792ee19329313dfc7402fa174035805a345`。先前GitHub治理HEAD（本审议写入前） `2f451b0a4871230ddd1b7673821abf8729f617b4`。

本轮[Codex候选](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/416cff6c00d2b865c3e9dda4088242d2b80969ce)：commit `416cff6c00d2b865c3e9dda4088242d2b80969ce`、tree `1d5bc390774d68ea619f6ad263c99d0090486b37`；Git原始commit对象唯一parent `343c22132deb23ba6d913d70e132b43a00b95f1d`。与任务发布提交compare结果1 ahead/0 behind，且仅新增下列三个原任务白名单文件，未修改/删除其他跟踪文件：
- `versions/0.0.10/review_runner_engineering_preflight_result_20261016.md`，Git blob `ce035e0c102c9de155c362e661bfd531e7d7a988`，4220 UTF-8字节。
- `versions/0.0.10/review_runner_engineering_preflight_manifest_20261016.json`，Git blob `6bd68abe36b89d33ce691bd47fb00e52a0c13b2b`，11573 UTF-8字节。
- `versions/0.0.10/review_runner_engineering_preflight_static_draft_20261016.txt`，Git blob `a6d7d4db82ece8ef26d6f01cbaa7a145d4ebb8a7`，1390 UTF-8字节。

三件都在对应单文件上限内、LF无BOM、末尾LF；公开文本按常见私有Windows路径/秘密token/PEM私钥/个人邮箱模式检查未发现明显命中，**不能据此证明所有敏感数据均不存在**。remote分支在本次核验时确指向 `416cff6c00d2b865c3e9dda4088242d2b80969ce`。单提交谱系只能证明Git最终图，不足以独立证明“恰一次普通nonforce push”；该细节按Codex本地回执分账。

## 二、失败性质：隔离clone漏取冻结模型分支

Codex在[报告](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/416cff6c00d2b865c3e9dda4088242d2b80969ce/versions/0.0.10/review_runner_engineering_preflight_result_20261016.md)和manifest明确记录：
1. 阶段A先 `git clone --no-checkout --single-branch --branch migration/astra-workflow-20261012`，仅取得治理分支范围；
2. 配置`core.autocrlf=false`与sparse-checkout src后，针对固定代码commit `94de4501dec051b969bee9d852eba2d4591f30ef`运行`checkout --detach`，报告exit 128、`unable to read tree`；
3. 未再fetch、未第二次clone、未调用Python、未进入AST/harness/真实runner/science；依赖失败即时STOP。

**独立远端补证**：通过GitHub raw Git Commit/Tree和branch-ref实际查询，已确认冻结模型commit `94de4501dec051b969bee9d852eba2d4591f30ef` 存在，其tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5` 确实存在且可读取；远端`refs/heads/codex/ch5-v010-matlab-first-20261015` 当前HEAD正是该准确commit。由此可排除“GitHub上该冻结对象消失”的判断。单分支治理clone遗漏模型分支可解释本地对象不足；**无法直接访问Windows本机object DB/原始完整stderr**，故将确切本地缺失形态保留为`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，不伪称远程重现。

**执行偏差/计划限制分账**：独立clone本身符合原保护方向；`--single-branch`选择治理分支却要checkout另一个历史代码分支，属于准备步骤ref/object覆盖不足，而非数学算法错误、HJB失败或真实数据问题。原任务并未要求“只能克隆治理分支”。该错误不能通过放宽runner安全检查、修改模型source或忽略exit code来解决。

## 三、用例、资源与尚无资格事项

已独立读取新的机读manifest并与上一轮`review_runner_io_offline_static_cases_20261016.json`对照：**69/69** ID相同且唯一（原24主例+新增22主例+23变体），全部`NOT_EVALUATED`，`PASS=0,FAIL=0`。这是用例执行状态，不是阶段A无故障：**阶段A实际FAIL**。

公开报告/manifest一致声称工程Python `0/4`、AST0、harness0、真实runner0/2、科学过程与HA及pytest等均0；准备阶段显式Git命令5次、回执exit顺序 `0,0,0,0,128`，Git内部子进程未instrument、真实runner Git child=0。这些**本地操作数值是Codex报告**，网页未获得D盘原回执，不能升级为独立进程实测。Owner转述本地回执SHA256 `C8E4DC9DCAB7BCE109811EFC6129861DD698C4CF73EE4D830BF3E8DD96062432`，本会话**未直接读取本地文件字节，SHA未独立重算**。

资源分别保留：manifest clone在STOP时报告497,022,015B、artifact写报告前8625B；Owner最后转述封存后clone497,029,770B/2GiB、工程artifact14,983,882B/16MiB。差别属于不同封存时点且仅本地回执支持；**不能把公开manifest中准备阶段8625B当成最终artifact总量**。全部新Python预算虽零消耗，但原任务已STOP，余额**不是自动跨任务继续或刷新科学许可**。

尚未验：AST语法、46+23运行案例、Popen真实Windows argv审计、真实Git child身份回执、磁盘九源原字节及loader、Job Object/timeout/reap、日志有界事务、watchdog、完整runner I/O。现有静态runner审议`STATIC_DESIGN_READY=CONDITIONAL_LIMITED_ACCEPT`仍有效，`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`ENGINEERING_RUNTIME_NOT_RUN`、`HA_SCIENCE_NOT_RUN`。

## 四、后继建议（本报告**不授权执行**）

如Owner批准**新独立阶段A对象可达性修复**，仅在可信的新隔离clone中，显式基于`codex/ch5-v010-matlab-first-20261015`获取模型分支（或经批准单独fetch此确切ref），先只读校验commit/tree/sole parent和九份源文件的Git blob、`.git`与原受保护common-dir完全不共享，再决定是否另行授权真实Windows runner。所有Git网络次数、scratch/clone新增字节、存储/时长必须在新授权中**重新说明**；旧已STOP预检预算不能偷作新预算，不能以“0/4未用”越过STOP。修复scope不得扩为Git所有分支抓取、碰旧dirty树或再次混合工程与科学HA启动。

**Owner前置决定待办**：是否允许单独A阶段Git对象可达性修复（无Python/科学），其结果独立审查后再决议工程-only preflight后续预算。不得凭本审议自动发新执行任务、重跑原checkout、补取旧clone对象或启动V011。

原科学冻结plan blob `85138d8859d53295262fe13bf5bc277bca95ed3f`、原单点input blob `c23d331bed34e5ca478324cdc05034609ecb91b7`、两次历史单点Python1/1耗尽、旧首次存储超额和旧V010算子/selector根账原样保留；`A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`model_activation=False`、`Results FALSE`、real C8 A–D REQUEST_ONLY、原8 dirty/index/staged/external common-dir/untracked/ignored与历史失败回执、`V011 NOT_STARTED`均不改。
