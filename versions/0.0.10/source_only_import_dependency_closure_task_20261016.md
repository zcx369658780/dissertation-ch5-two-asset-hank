# V010：SOURCE_ONLY 冻结模型 import 全传递依赖闭包与只读隔离装配设计（正式单轮任务）

**唯一新 ACTIVE 任务 ID：`V010_SOURCE_ONLY_IMPORT_DEPENDENCY_CLOSURE_AND_READONLY_ASSEMBLY_PLAN`**

**授权来源：**2026-10-16 Owner在Astra独立验收上一轮 PARTIAL_ENGINEERING_DIAGNOSTIC 后明确同意纯 SOURCE_ONLY 依赖闭包核查。Astra在本冻结单文档中限域确定资源与验收标准。**本任务在发行commit后只接受该固定commit/blob正文，不得用动态分支HEAD或这段聊天替代。**
**终态：**`WAIT_ASTRA_V010_SOURCE_ONLY_IMPORT_CLOSURE_REVIEW / STOP`。Codex不得自授科学/Windows工程运行PASS或发布Results。

## 0. 目标、冻结输入与审议前提

解决V010 ENGINEERING_ONLY Windows Stage B–E 真实runner在`load_runtime`处报告`LOADER_IMPORT_NOT_EVALUATED`的**静态源码依赖闭包缺口**；上一轮5真实Git child的identity/audit/Job/reap与68 synthetic PASS/1 NOT_EVALUATED不得因新静态分析被抹除或提升为FULL PASS。

- 仓库：`zcx369658780/dissertation-ch5-two-asset-hank`；GitHub治理分支`migration/astra-workflow-20261012`。
- 上一轮独立[主审](runner_io_windows_be_github_primary_review_20261016.md)：文件Blob `67c15e010c4a90b9773899cd699222d756fe5772`；上一工程review commit `9bcd61fc88ace3b8e2c1c07753c610e2e4b5c75e` / tree `b36531a20a3f99090f4650e10834a54d24cb6d14` / parent `7ec7eae170ae744b6c1b8321c434baf565e9ef7c`。
- 当前唯一模型代码固定commit `94de4501dec051b969bee9d852eba2d4591f30ef` / tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5` /唯一parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`；仅该Git原始对象的源码、索引、版本声明可作为模型身份。不得从main、治理branch、V008/V009候选或本机未认证copy混合引用。
- 模型源码Git树：`src`子tree `342d5709cefac1d61669a05a800672641f0f02cf`，`src/ch5_two_asset_hank`子tree `50aff40936c1c7232853eb0b3c32901f101bcae0`，`corrected_diagnostic` tree `e83a5ab436d050bcc8ac60114f3451c6154e1645`，`multi_province` tree `ecaee158decfc6dfe51c4e69789ec16d4d424bec`；Astra已独立通过非recursive Git tree端点看到这三个模块范围合计**70个.py文件（顶层18+纠错30+省际22）**，这只是候选全集而不是全部需要导入的结论。**不得依赖整个repo `recursive=1` 截断结果做完整树证明**。
- 冻结`pyproject.toml` Blob `5c778f7ccbbabfaf1046d4696cf843dc0adbb34c`，仅声明Python≥3.11、numpy≥2.0、scipy≥1.14，不证明Windows已安装版本、二进制兼容或import安全。
- 九份受监测源码按上一轮runner `NEEDED`及Stage A已签出正确Git Blob身份；初始入口来自上一轮脱敏runner源码 `versions/0.0.10/review_runner_io_windows_be_static_draft_20261016.txt` Blob `79b8e6b8eb9bd7138c3c23aa6a997a0bc1272d3e`，具体`load_runtime`调用的`from ch5_two_asset_hank.multi_province import mainline_household_runtime as runtime`以及`VerifiedFinder.find_spec/VerifiedLoader.exec_module/check_loaded`必须实际静态读原文本，不猜测。
- **已知缺失三份均为真实非空源码**：`src/ch5_two_asset_hank/__init__.py` Blob `d99cf2762787ed6999e63745903116f95fe02ab9`；`src/ch5_two_asset_hank/multi_province/__init__.py` Blob `58484859799b3fd3c79d33f93b5a26fa6d7c0193`；`src/ch5_two_asset_hank/corrected_diagnostic/__init__.py` Blob `c937c4aa4c6cf0ce4638e113d5d732f69b909923`。其顶层显式导入可涉及`hjb/kfe/contracts`、`household_adapter/annual/provenance/one_turn/steady_state`、`boundary/cost/saved_controls/panel/selector`等；**补齐这3份不保证import闭包已完整**。冻结科学plan blob `85138d8859d53295262fe13bf5bc277bca95ed3f`、人工fixture blob `40915658d93403cfc21b33a6b864b332b7857749`、单点manifest blob `c23d331bed34e5ca478324cdc05034609ecb91b7`不修改。

## 1. 许可与绝对禁止

本轮只能**读既有Git Blob/文本并写新的静态分析报告与计划**：允许PowerShell原生命令、已认证Git的`cat-file`/`ls-tree`/`show`/`rev-parse`等严格read-only方法，从已存在且独立的Stage A单分支模型clone中的Git对象数据库解析冻结commit；如该clone失效、对象不完整或标记与远端冻结不符即STOP，而**不能clone/fetch/pull/checkout/reset/clean/sparse-checkout set**或额外取得模型网络对象。允许核对GitHub固定commit的公开blob/tree，不能写远端模型branch。避免Git命令带可能修改index的默认锁；明确`GIT_OPTIONAL_LOCKS=0`等可信环境和结果exit检查。

本轮**Python/py/AST/import/py_compile/pytest/exec/eval/模型runner/科学函数/数值求解进程全部0**，Node或PowerShell亦不许通过二级子进程偷偷启动它们。PowerShell静态词法读源码可行，但解析不全、动态import、条件分支必须标`UNKNOWN`，不可宣称比文本可证的更多。禁止为了修通import修改runner/hook`VerifiedFinder`白名单、伪造`__init__`、建立synthetic package stub或加载任何冻结科学模块，不得阅读原真实C8/2017/2018/B3和V009坏数据。

禁止读写原受保护`D:\ProjectTemp\c5k1bturn56`以及其8个dirty tracked、staged/index、untracked/ignored、外部Git common-dir、全部旧失败证据根与其它项目。**Stage A独立模型clone仍然只读，包括它的worktree/index/.git/object store/config，不对其写入任何文件或复制为共享worktree**。读取其固定commit内部原Git blob允许；如存在任何共享`common-dir`或风险reparse，停止，不为“检查保护”实际stat旧根。V010模型数学、原MATLAB、参数、网格、阈值、行业/省份/人口、GovInv和所有科学输入不可修改。

## 2. 单轮具体审查流程

**A. 受界SOURCE_ONLY预置（先身份后内容）**。新独立scratch `D:\ProjectTemp\ch5_v010_source_only_import_closure_20261016_01`必须全新排他创建、无旧文件或reparse；记录Git.exe SHA/路径类别、模型cloneHEAD/tree/parent与独立common-dir，九个原Stage A源Git blob与三init真实Git对象存在，读路径核验与准确原任务发行commit/blob。失败立即`SOURCE_ONLY_FAIL_CLOSED / STOP`，无重试自动清理。读取对象时保留原blob SHA和字节数，禁止因PowerShell文本转码而重新宣称raw byte身份。

**B. 冻结模块全集inventory**。分别读上述Git子tree，形成模型内可静态装配的`module → repo_relative_path → Git_blob → byte_size → is_package`全域索引；包括三init、九受监测模块及其它被达成的相对/绝对包内import。非源项目文件与第三方依赖另列，不能算作冻结模型Git blob；若同名模块/路径alias、目录遍历、可疑Git mode/submodule/symlink、重复module名，STOP或UNKNOWN。明确检查`__init__`初始化自身带入的依赖，而非只有`mainline_household_runtime.py`的几行from。

**C. 真实导入入口的传递闭包**。以冻结runner的`load_runtime`实际`from ch5_two_asset_hank.multi_province import mainline_household_runtime`为根节点，按Python package parent `__init__`的导入顺序，将顶层`import`/`from`、多行括号、显式/相对import、`from . import xxx`、模块级conditional与`__all__`分别标注。对新发现的内部模块继续读固定Git blob，直到无新增**静态可解析**的导入边；每个节点记录`source_blob`、`imports`、`edge_type`（`IMPORT_TIME`、`FUNCTION_LOCAL`、`TYPE_CHECKING`、`MAIN_ONLY`、`CONDITIONAL`、`DYNAMIC_UNKNOWN`等）、被谁引入、是否在Stage A磁盘九文件签出白名单内。函数内科学`brentq`调用不可当import执行，也不可对有条件导入声称必然会运行；未知路径保留UNKNOWN。每个真实init内部导入的其它包也要递归。**若无法静态可靠解析原源码的括号、字符串/条件、通配/动态import，不能靠宽松正则宣称`FULL_IMPORT_CLOSURE_READY`，应以未知节点报PARTIAL并明确建议。**

**D. 执行风险与外部依赖门**。针对传递闭包中可能在模块import时执行的顶层非定义语句、全局变量赋值表达式、I/O、路径/环境/网络、subprocess、第三方初始化、动态import及`sys.modules`副作用逐项分类`PURE_DEFINITION`、`IMPORT_TIME_SIDE_EFFECT_RISK`、`UNRESOLVED`。只记录合法静态证据，不实际import；`numpy/scipy`的冻结项目最低版本作为依赖声明标注`RUNTIME_INSTALLATION_AND_ABI_UNVERIFIED`，不能推断Windows包存在。审查`VerifiedLoader.exec_module`之`compile(...,exec)`、`check_loaded`对九模块的严格要求，输出实际模块顺序、路径、必要认证对象和被hook拒绝的可能路径；不因`sys.setprofile` Python调用名守门就宣称所有import-time C/native行为安全。

**E. SOURCE_ONLY安全装配蓝图（**只写计划、不得执行**）**。设计**仅在未来另获Owner授权时**可在一个全新独立隔离目录内，从固定Git commit的原始blob恢复所有明确需要的.py文件字节，保持真实`__init__`、正确包层级、同SHA256/blob，不触原Stage A只读clone。明确谁在未来应执行raw byte校验、no pycache/原科学源码只读、第三方依赖可信安装验证、loader路径签名、Git identity与runner source-map的一致性、import-time side effect hard deny、产物预算/异常退出；本轮不创建该源码装配目录、不运行preflight、不生成Python源执行副本。若GitGate固定`root`要求`.git`/HEAD而计划目录只是纯源码树，需提出**身份校验与隔离源码根分离的最小工程设计建议**，禁止擅自放宽Git identity guard。任何引入替换的`__init__`或跳过包副作用的方案必须标为`NOT_SOURCE_FAITHFUL`并拒绝将其用于PASS。

**F. 独立分类和下个权限边界**。当静态internal graph每条import-time可解析边都指向固定Git blob、没有UNKNOWN/无法拒绝的顶层I/O风险、隔离装配蓝图和外部库验证门定义清楚，可报告`SOURCE_ONLY_IMPORT_GRAPH_CLOSURE_CANDIDATE_READY`；这仍然不是`IMPORT_RUNTIME_PASS`。若graph有未解析边、第三方安装未知或者包初始化存在风险，报告`SOURCE_ONLY_PARTIAL_IMPORT_CLOSURE_WITH_OPEN_GATES`，逐项给具体阻断路径与下一所需信息；只读身份/资源/保护失败报告`SOURCE_ONLY_FAIL_CLOSED`。所有分类均要求`ENGINEERING_RUNTIME_NOT_RUN`、`HA_SCIENCE_NOT_RUN`、`FULL_RUNNER_IO_CLOSURE=BLOCKED`、Results FALSE。

## 3. 一次性资源、发布与回执

- 新`Python/HA/pytest/AST/runner=0`；总task wall ≤**2小时**；读取冻结仓库内静态source对象 **≤90份文件、原始源码累计≤5MiB**（最多模型70.py＋必要固定meta，超过STOP而非扩大）；显式只读Git/PowerShell source身份调用**≤150次**（全部退出码和调用类型有证据、Git内部spawn若未监控标UNKNOWN）。新scratch中一切MD/JSON/报告/命令账/临时源文本副本**累计增量≤8MiB**，不允许写原任何clone；先做quota预约和最终/应急预算保留，不因失败清理超额证据。
- **无新模型clone、fetch、checkout、sparse写或模型分支网络取物**。GitHub非修改式connector读取冻结对象可用；用于单次审阅文档发布，允许一个全新不共享原对象的最小Git元数据工作区 **≤1GiB**，定向取得**本任务发行commit的审阅基线**，此取物不应夹带模型对象；所有发布网络/Git空间与SOURCE_ONLY读取独立计账。
- 仅允许一次**普通non-force** push到新`review/v010-source-only-import-closure-20261016`分支，必须从**本任务发行commit为唯一Parent**建立，先确认新branch不存在；失败即LOCAL_ONLY STOP，不修改全局Git config、不重试、不force、不写main/治理/旧review/模型分支。
- 发布**最多2份经过脱敏的GitHub review材料**：`versions/0.0.10/review_source_only_import_closure_result_20261016.md`（≤32KiB）；`versions/0.0.10/review_source_only_import_closure_manifest_20261016.json`（≤128KiB，含模块节点/导入边/分类/各blob/外部依赖/装配方案/资源账；不含原始绝对路径、私有stdout/stderr或源码全文）。若不安全，保留local-only原件STOP，不为push暴露秘密。远端回读commit/tree/sole parent/确切两文件blob及bytes。
- 私有真实Git/PowerShell回执若有本机路径等信息LOCAL_ONLY，Astra GitHub只能独立核Git源码身份和公开静态图，不能把Codex本地进程/保护回执假装Astra亲证。

**最终报告：`V010_SOURCE_ONLY_IMPORT_DEPENDENCY_CLOSURE_RESULT`。终态`WAIT_ASTRA_V010_SOURCE_ONLY_IMPORT_CLOSURE_REVIEW / STOP`。**

原V010冻结计划和数值合同、旧单点两次Python各1/1与首次存储超额、旧V010实现pytest4/6-driver1/4-HA1/26-selector1626-roots1642、上一轮B–E工程Python3/4/runner1/2剩余额度、A16 FAIL_CLOSED/window UNACCEPTED/C9 PAUSED/CALL_LEDGER UNRESOLVED、`model_activation=False`、`Results FALSE`、real C8 A-D REQUEST_ONLY、原8dirty/index/外common-dir与历史失败根、`V011 NOT_STARTED`全部保留；不恢复旧额度、不改公式。
