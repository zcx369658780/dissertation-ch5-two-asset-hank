# V010 Windows runner Stage B–E：Astra GitHub独立验收（PARTIAL工程诊断）

更新：2026-10-16（Asia/Shanghai）。
**独立分类**：`PARTIAL_ENGINEERING_DIAGNOSTIC_CONFIRMED__BOUNDED_WINDOWS_GIT_IO_POSITIVE_EVIDENCE__LOADER_IMPORT_BLOCKED__FULL_RUNNER_IO_NOT_ACCEPTED`。
**验收范围**：GitHub候选身份、三文件完整交付、JSON对照与源码静态审阅可独立认证；Windows本地执行事件依Codex脱敏回执及Manifest，**不**宣称Astra亲自执行Windows进程、Python、真实子进程或磁盘保护检查。
**当前权限/停点**：`ACTIVE_TASK=NONE`；`WAIT_OWNER_V010_ENGINEERING_SOURCE_IMPORT_CLOSURE_AUTHORITY / STOP`。原任务已交付并STOP，剩余工程Python1/4与runner1/2不得自行结转或重启，HA/HJB/KFE/selector/root/GE/IRF/真实数据调用新许可仍0。

## 1. 候选GitHub身份及脱敏白名单

本次冻结任务 `V010_RUNNER_IO_WINDOWS_ENGINEERING_STAGE_B_E_PREFLIGHT` 发行commit `7ec7eae170ae744b6c1b8321c434baf565e9ef7c`、tree `41da24010c732866988360bd1c01107a4e88f20c`、blob `72f3b503ce5f468b8f80c2cb9cb16497a4b5b75f`。Codex[脱敏候选commit](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/9bcd61fc88ace3b8e2c1c07753c610e2e4b5c75e) `9bcd61fc88ace3b8e2c1c07753c610e2e4b5c75e`、Git tree `b36531a20a3f99090f4650e10834a54d24cb6d14`、**唯一parent准确等于任务发行commit**。远端`review/v010-runner-io-windows-engineering-b-e-20261016` HEAD正确；与发行commit比较`ahead=1, behind=0`，仅新增三份允许文件：
- `versions/0.0.10/review_runner_io_windows_be_result_20261016.md`，Blob `f6f62fd4b50c94638efcf95ee4f019e8b10d8a84`，6675 UTF-8字节。
- `versions/0.0.10/review_runner_io_windows_be_manifest_20261016.json`，Blob `9256f0c81a445c02b32d97cfea93937dbe9edc71`，35285 UTF-8字节。
- `versions/0.0.10/review_runner_io_windows_be_static_draft_20261016.txt`，Blob `79b8e6b8eb9bd7138c3c23aa6a997a0bc1272d3e`，58055 UTF-8字节，**NON-EXECUTABLE SANITIZED ENGINEERING SOURCE BUNDLE**。
三文件均在各自30/96/96KiB公开上限内，UTF-8、LF无BOM、有final LF；不把文档当可直接运行的Python交付，也不把单Git commit拓扑冒充“确实只进行一次nonforce push”的本地进程证明。未读取私有本机`DELIVERY_RECEIPT.json`原字节。

## 2. 69 cases和进程/Child证据的独立结构检查

已从上一轮固定`review_runner_io_offline_static_cases_20261016.json`交叉比较本轮Manifest `B2.cases`：46个主ID+23变体=69个唯一ID，**全部ID准确一致**，没有缺项或额外替换。分类`PASS=68`、`FAIL=0`、`NOT_EVALUATED=1 (N13)`。68条均标`SYNTHETIC_ENGINEERING_ONLY`，不能冒充真实Windows正向证据。另有`SCIENCE_MODE_HARD_DENY`和`TERMINAL_RESERVE_EXHAUSTION`两条附加合成测试报告PASS。N13本轮没触发旧6600秒进程内watchdog故障，外部180秒host timeout用于限期但真正超时/强制kill仍未实测。

Manifest里恰好3条工程Python进程记录（B1 AST：PID46952，B2 harness：44328，runner：29572），三项exit=0且运行wall均小于180秒；AST峰值RSS写`UNKNOWN`，没有伪填0。B1结构检查46+23和唯一project hook注册点；B2执行记录合成68/69；真实runner仅1次，exit0但内部状态`ENGINEERING_ONLY_PARTIAL`，不等于全部验收合格。以上PID/时间/执行事实来自Codex本地receipt清单，不是Astra本机观察。

真实Windows Child部分提供4身份+1固定commit源码inventory共5个nonce，Manifest恰有5个audit event，nonce集合一一相同且无重复。5个child字段均包含`exit_code=0`、`job_assigned=true`、`reaped=true`、`readers_joined=true`、`audit_consumed=true`、`streams_complete=true`、`timeout=false`、`stderr_bytes=0`；五次Windows Popen审计报告均为4参数、`argv_type=str`且与`list2cmdline`预期吻合。输出大小分别为41/41/41/72/7702字节，均在身份4KiB和inventory1MiB白名单以内；子进程PID`NOT_CAPTURED`、Git内部spawn`UNKNOWN`，不能臆造。无异常timeout现场时不能证明Job杀死活跃子进程及后代回收能力，只有正常退出Job分配/回收的本地正向证据。

Writer正常UTF8写入和一次人工注入rename失败后事务保留/计费+应急/final封存由报告和静态runner给出相符记载，但不能外推覆盖所有磁盘故障。Hook`HOOK_PROVENANCE_BOUNDED`通过`-I -S -B -X utf8`受控环境与自家注册点论证；Python历史其它hook不可枚举，不能证明全进程绝对只有一个hook，也不等于OS沙箱/A16解除。

## 3. 原模型源码身份、loader实际阻断和潜在传递依赖

冻结模型commit `94de4501dec051b969bee9d852eba2d4591f30ef` / tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5` /唯一parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`未变。Manifest九份`model.nine_disk_binding`的路径、git_blob、raw_sha256、bytes与先前Stage A用户上传及Astra从固定GitHub源独立复算的9/9一致；本轮Windows实际磁盘读写仍是Codex回执，报告称启动前/runner内/运行后多次交叉核验九源。

**硬阻断**：Stage A为了范围保护只sparse签出九份源码，实际clone缺少三个Git已有的包初始化模块：
`src/ch5_two_asset_hank/__init__.py`（冻结Git Blob `d99cf2762787ed6999e63745903116f95fe02ab9`，579B）、
`src/ch5_two_asset_hank/multi_province/__init__.py`（`58484859799b3fd3c79d33f93b5a26fa6d7c0193`，4274B）、
`src/ch5_two_asset_hank/corrected_diagnostic/__init__.py`（`c937c4aa4c6cf0ce4638e113d5d732f69b909923`，1947B）。
Astra已直接从固定模型commit读取并核对这些文件在GitHub确实存在。当前受控runner`load_runtime`在发现三文件缺失时，**先写`LOADER_IMPORT_NOT_EVALUATED`并返回**，不进行模型import或`__file__`/loader检查；原任务不允许修改Stage A clone、追加fetch/checkout，Codex据此STOP合理。

**额外静态风险（不能误简化为仅补三个文件）**：三个`__init__.py`不为空，包含`contracts/hjb/kfe`、`household_adapter/provenance/annual/one_turn/steady_state`和`boundary/cost/saved_controls/panel/selector`等import；九份源码自身亦有其它transitive imports。当前`VerifiedFinder.find_spec`按固定Git tree提供模块spec，`VerifiedLoader.disk`要求每份真正被导入的Python源码均在磁盘、Git Blob精确认证。即便补齐三份初始化模块，仍可能缺失**其传递依赖文件及合法第三方包**。下一授权必须先做`SOURCE_ONLY`全量导入依赖闭包/冻结Git Blob inventory与最小只读隔离装配方案，再申请工程Python，否则再浪费进程的风险可预见。本轮没有证明导入闭包完整，也没有运行一次真正的model import。不得通过伪造空init、放宽Finder或在原Stage A只读clone里写文件来救PASS。

## 4. 资源、保护和历史状态分账

Codex本地最终回执由Owner口述SHA256 `8CE3D65D046753CF92D01238BE09A816A87FB7C5D6960C67F3D89DA7DB157D62`；原D盘receipt本会话未访问或独立重算。报告内运行前/发布前Manifest快照`nonGitBytes=419764B / 33554432B`、`publicationGitBytes=497072677B / 1073741824B`、`elapsedSeconds=1175.931...`；Owner最终报告`artifacts=503758B/32MiB`、`publicationGit=512047316B/1GiB`，分别属不同封存时点，无明显自相矛盾，但最终数据仍需本地原证支持，不升级独立现场计量。
- 新工程Python报告`3/4`、真实runner`1/2`，自STOP后剩余额度不可转入未来任务。新模型clone/fetch=0；保护树/8dirty/index/staged/untracked/ignored/外Git common-dir/历史失败根无访问或改写均为Codex报告级。
- V010原科学/实施账pytest4/6、science driver1/4、HA1/26、selector1626、scalar roots1642及两笔单点Python各1/1且HA0、首次产物43519638B超32MiB 9965206B**原样保留**。本轮真实HA/HJB/KFE/selector/root/GE/IRF/pytest/真实C8全部报告0、未从工程进程授权中产生科学计算权限。
- V010科学计划冻结commit `bf091da33d59293f147d52c11580327d3ac2a85d`、blob `85138d8859d53295262fe13bf5bc277bca95ed3f`，不因工程预检成功部分而追改。模型研究主线修原MATLAB两资产HA→多省顺序→原GovInv收益边界×0.9/1.1与Zt→GDP独立1%目标→原lagged-NKPC递推，家庭人均/省总量、目的地税扣一次、same-S/lagged raw ra0保持。
- `A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`model_activation=False`、`Results FALSE`、`real C8 A-D REQUEST_ONLY`、`V011 NOT_STARTED`均不变。

## 5. Astra终审裁决、下一许可

**认可**三份GitHub候选交付及其parent/tree/blob身份，`PARTIAL_ENGINEERING_DIAGNOSTIC`和五Git child正向证据的受界价值；未观察的OS负例、N13及loader import继续分别标`NOT_EVALUATED`。**拒绝**`FULL_RUNNER_IO_CLOSURE=PASS`、`ENGINEERING_RUNTIME_PREFLIGHT_FULL_ACCEPT`与任何HA/论文Results推断。原任务完成交付后STOP、无继续执行中的ACTIVE。

**建议下一个最小风险门**：`OWNER_DECISION_REQUIRED__V010_SOURCE_ONLY_IMPORT_DEPENDENCY_CLOSURE`，在新独立scratch中、不写只读Stage A clone、先0 Python/HA，静态列齐从九源、三个真实init及其传递模块的冻结Git Blob、入口loader约束与依赖包，产生有界装配/验收计划；通过后才申请新`ENGINEERING_ONLY` Windows真实loader/异常timeout补证预算，科学HA再另授权。本报告**不是**自动签发下一任务，不自作新fetch/clone/修改。
