# V010 E0 Launcher UInt32 与临时 Git mktree 发布器：限域工程集中修复

**唯一任务ID：V010_E0_LAUNCHER_UINT32_AND_TEMP_MKTREE_CORRECTION**
**版本：V0.0.10，ENGINEERING_ONLY / E0_AND_GIT_PUBLICATION_ONLY；日期：2026-10-16（北京时间）。**
**Owner新会话指令：完成正式GitHub交接后直接签发下一任务。** 本任务是新的、仅限E0与Git发布器的工程授权，不是对旧任务的重试许可，也不开放新的Python或科学求解。Codex在下述预算内集中实施、验证并交付；不逐微步请示普通修复。
**本任务正式发行commit及任务Git Blob以发行后的TASK_CURRENT.md记载为准。** 不在本文件预填未来自引用SHA；签发后不可追改。本次结果停止于 `WAIT_ASTRA_V010_E0_LAUNCHER_MKTREE_CORRECTION_REVIEW / STOP`。

## 一、固定依据与上一轮失败

- 唯一仓库：`zcx369658780/dissertation-ch5-two-asset-hank`；治理分支：`migration/astra-workflow-20261012`。读取动态 `docs/DOC_INDEX_CURRENT.md`、`CURRENT.md`、`TASK_CURRENT.md`、V1.2工作流、Owner风险/SSH/Loader决定、远端临时审阅协议；冻结本任务后始终按固定发行commit读取任务正文。
- 上一已STOP任务 `V010_ENGINEERING_ONLY_TRUSTED_LOADER_INTEGRATION_PREFLIGHT`：发行commit `01129efd5220683d415bd1486f23f6ecd068cb53`，任务Blob `1e6757fd235fd96d8b08130ca3fefb3b602c413c`；本会话前正式独立审议 `versions/0.0.10/trusted_loader_e0_fail_closed_local_only_primary_review_20261016.md`，Blob `d9d5a3ea38fcff89633ce09fdf0d97d9e9e61293`。旧任务报告E0阶段Launcher UInt32转换失败，source_assembly_root保护门未建立；独立SSH443发布基线据报成功，但新bare脚本写出空行，`git mktree` exit128、candidate0、push0，结果LOCAL_ONLY。旧Python0/6、runner0/2已随STOP关闭，不结转。
- 旧本机回执 `DELIVERY_RECEIPT.json` Owner转述SHA256 `C0BE33821FCB956483F8E894A8762F9D0D24139C8377D4A1B544BA73332056F8`；因原本地字节未给Astra，E0细节及70源物化只能标 `CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，不能冒充独立核验。
- 冻结V010模型：commit `94de4501dec051b969bee9d852eba2d4591f30ef`、tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`、唯一parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`；原70份.py（三非空init），均只读。科学plan：commit `bf091da33d59293f147d52c11580327d3ac2a85d`、blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；合成fixture blob `40915658d93403cfc21b33a6b864b332b7857749`，单点HA manifest blob `c23d331bed34e5ca478324cdc05034609ecb91b7`；皆不可追改。
- 现行技术选择：Owner已接受 `TRUSTED_WORKSTATION_ENGINEERING_CONTAINMENT`、两个独立Git/source身份根、raw Git Blob VerifiedLoader、现有C盘独立SSD备份+GitHub双重备份、不强制新VM或第三备份；Codex使用原SSH key/SSH-over-443，不改global/system Git配置、不使用PAT；该选择**不等于**OS native沙箱PASS。

## 二、新独占scratch及可读写白名单

唯一新独立scratch：`D:\ProjectTemp\ch5_v010_e0_launcher_mktree_20261016_01`。在创建前按字面路径、reparse/祖先路径、磁盘/保护根与共用Git object检测；与任何旧失败目录、模型工作树、C盘备份或真实数据根重合/重解析立即STOP。所有新增脚本、测试/回执、装配源仅写在此新scratch；不能覆盖旧失败原件。

可精确只读：前一失败目录中的 `result.md` 与 `DELIVERY_RECEIPT.json`（只限这两文件，合计读≤2MiB；过大则保留UNKNOWN）；前次工程Launcher/发布器**已知准确源文件**的小段只读文本；独立Stage A只读 `git_identity_root` 的固定Git对象及70源码原始字节；本仓已冻结GitHub计划、任务、主审与协议。禁止扫旧错误日志、旧科研树、C8/2017/2018/B3、V009失败数组、无关项目。原 `D:\ProjectTemp\c5k1bturn56` 的8 dirty tracked、staged/index、untracked/ignored、外部common-dir绝不写/清理/stash/reset/checkout；C盘备份不动。

## 三、Codex集中修复目标，依赖门失败立即停

**A. UInt32真实根因及修复。** 从旧回执和精确PowerShell源码提取发生转换失败的实际参数名、原始类型、允许区间、触发调用点和错误信息；若回执没有这些字段，必须标UNKNOWN，不能猜测实际触发值。仅修新scratch里的Launcher/封装，不改原冻结模型或旧回执。严格区分 null、负值、越界（大于UInt32上限）、非法字符串、浮点或非整值，显式受界验证后才做UInt32强类型转换；禁止吞异常、环绕、截断、无条件clamp、扩大安全阈值、把失败当PASS。静态正反用例须覆盖原可用类型、最小/最大合法值及典型非法值，并保存每例预期和实际PowerShell检查结果。

**B. E0 source root安全门的窄域再验证。** 在全新scratch允许按固定commit raw bytes重新物化70份原源码（完全不执行任何.py），逐件保持Git Blob SHA1/size、SHA256、相对路径及三份真实非空init，来源只读身份根；修过的Launcher可执行至E0防替换/写入排他门，最多两次受界E0级PowerShell试验。检查目录祖先reparse、UNC/ADS/hardlink/symlink、意外写入/源变动、排他手段实际效果、begin/end hash和受信任工作站假设；记录具体机制与不能防御同用户恶意替换的TOCTOU残余。**readonly attribute、口头声明、hash仅静态存在不等于OS级写排他PASS**。若既定可信工作站边界内也无法有效验证写入/替换保护，报告 `SOURCE_ROOT_OS_WRITE_EXCLUSIVITY_UNKNOWN / E0_FAIL_CLOSED` 并停止后继E0依赖步骤；不得放宽安全检查。绝不从E0跨入AST/model import/VerifiedLoader/runner。

**C. Git mktree脚本修复与隔离构树。** 在新项目外**独占bare对象库**（无worktree、无项目index/checkout、不共享.git/common-dir/alternates）修复旧发布器产生空行的源逻辑。生成树条目必须逐条匹配 `<mode> SP <type> SP <object-id> TAB <path> LF`，禁止空白行、重复或越界路径、错误mode/type/缺失blob、输入内嵌换行与不受控引号；分别静态检查 UTF-8/LF 与PowerShell字节处理，正确区分最终一个LF与额外空记录。至多2次在新bare上对非模型/非私有的合成tree样例做真实`git mktree`工程校验，严格核exit code、stdout object ID、tree只含预计条目。之后校完整固定任务parent commit/tree/所需blob在独立bare可达，再准备审阅candidate。不能把`mktree` exit0偷换成已push或已验证GitHub，也不能补推上次失败分支。
- 仅当全部前置成功、脱敏通过，才准新任务的一次GitHub临时发布（见第五节）。若E0失败但mktree本身修复成功，报告分门结果；是否发表本轮安全脱敏的诊断性结果，以发布链已通过自己的前置检查为准，**不得将E0失败隐瞒成成功**。
- 禁止改变原SSH配置、补PAT/秘钥；严格host-key。任何新object/write仅位于新bare，不对Stage A身份根或模型旧Git对象写。

**D. 固定结果语义。** 分开列 `LAUNCHER_UINT32_CAUSE`、`LAUNCHER_CORRECTION_STATUS`、`SOURCE_ROOT_E0_PROTECTION_STATUS`、`MKTREE_GENERATOR_STATUS`、`TEMP_GITHUB_PUBLICATION_STATUS`；每项取PASS/FAIL_CLOSED/NOT_EVALUATED/UNKNOWN且说明证据种类。只有实际E0门成功可标 `E0_ENGINEERING_GUARD_PASS_WITH_TRUST_LIMIT`；Git mktree只过合成测试不称发布PASS。永不据此声称 `CANONICAL_IMPORT_AUTHENTICATED`、`FULL_RUNNER_IO_CLOSURE_PASS`、`HA_SCIENCE_PASS`、`RESULTS_PASS`。

## 四、本任务独立新增、不可结转的明确预算

- **Python进程0，py/pytest/py_compile/AST执行0，模型import0，VerifiedLoader0，真实runner0，HA/HJB/KFE/selector/scalar roots/GE/IRF/MATLAB/真实C8调用0。** 不允许旧任务的6工程Python余额恢复，不允许试跑corrected HA单点。
- 只允许PowerShell文本编辑/类型验证、E0纯PowerShell启动器门（≤2次）、新bare非模型`git mktree`验证（≤2次）、冻结Git只读/必要发布操作；全部不运行任何Python。新Git只读调用≤100，模型clone/fetch/checkout=0；发布用新bare为获取完整**本任务发行基线**最多一次SSH完整fetch（若本地完整对象已可独立证明也可不fetch），仅新review ref一次nonforce push，失败STOP不重试。不得用残缺blob:none基线猜想对象齐全。
- 总墙钟≤2.5小时；新scratch**非Git物理增量≤16MiB**（含新70文件、脚本、日志、回执及失败transaction，最终/应急回执需先预留≥1MiB）；独占bare Git元数据≤1.5GiB（单独计账，绝非无限配额）。无模型网络/软件安装、无额外科学或工程进程申请。每一实际试验在调用前写入新外部ledger；失败保留实际费用，不重置旧账。
- 一旦任一硬界/保护/身份/写前预算或新脚本依赖失败，先STOP保留新失败原证；只在上述明确允许的普通工程修复额度内继续修当前任务，不可修改本任务冻结合同扩大权限。

## 五、脱敏GitHub远端临时审阅：仅本次专属许可

沿用Owner `docs/CH5_TEMP_SANITIZED_REVIEW_EXCHANGE_20261016.md`；本次确切远端review分支：
`review/ch5-temp-v010-e0-launcher-mktree-20261016`
远端临时目录仅限remote candidate tree：
`_review_tmp/ch5/v010-e0-launcher-mktree-20261016/`
**这条目录绝不可在本地任何科研/模型/治理工作树、Git index/staging或旧目录创建/checkout/git add。** 本地仅新scratch平铺原始脱敏候选文件，以新独占bare Git对象构造远端路径。

唯一允许远端三个文件（经脱敏与字节/密钥/path扫描后）：
1. `result.md` ≤32KiB：双失败分门原因、修复和实际E0/mktree试验回执摘要、严格未通过/未运行项与所有历史预算保留。
2. `manifest.json` ≤128KiB：本任务冻结模型/git身份、每项校验真实计数/exit/哈希/资源、70源码仅身份表、脱敏状态；未有真实数据。
3. `correction_draft.txt` ≤96KiB：两脚本限域修改的非可执行脱敏文本/最小差异和静态正反例，不包含本地绝对路径、用户标识、Secrets、原日志或完整未审计模型源。

单一candidate commit的**唯一parent必须是本任务正式发行commit（见发行后的TASK_CURRENT）**，从完整Git parent tree只添加以上三个路径，无其他变更。review branch必须事先不存在、白名单/size/tree/UTF8/LF检查成功，再用现有SSH Key/443严格host-key方式**最多一次普通non-force push**并核远端HEAD/tree/parent/三个Blob SHA1及原文件SHA256。失败标`LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED`，无candidate/push时准确报告，不跳过、不追加retry/fetch、不强推、不写治理/main/model树。本新分支不是补推上次旧失败分支。Astra收到后先验收、正式治理归档且回读，再依Owner协议仅清理新临时目录的三个远端文件；旧Git历史永不改写。

## 六、保护与终点

科学主线不动：corrected两资产HA→多省顺序单轮→原GovInv收益率边界控制0.9/1.1与Zt有界校准→冻结GDP目标≤1%另验→原lagged-NKPC递推；目的地工资税一次、家庭人均/省总量、三劳动账、same-S及前完整轮raw-ra0、phi_max=0.3、20×20×2、HJB/KFE原硬门均不动。旧V008/V009辅助Newton/CES/Bt=Bgov不能回主线。原单点`rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07`仍**完全UNTESTED**。
`A16 FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER UNRESOLVED`、`model_activation=False`、`Results FALSE`、`real C8 A–D REQUEST_ONLY`、`FULL_RUNNER_IO_CLOSURE=BLOCKED`、`V011 NOT_STARTED`不变。所有旧科学进程/首次GBK超额/Windows argv与历史E0 LOCAL_ONLY保留。
**最终报告ID：`V010_E0_LAUNCHER_UINT32_TEMP_MKTREE_CORRECTION_RESULT`。最终停止：`WAIT_ASTRA_V010_E0_LAUNCHER_MKTREE_CORRECTION_REVIEW / STOP`。本轮绝不启动新Python import；之后若要工程Python preflight，必须Owner另行明确批准专用进程预算，若要HA科学进程更需独立许可。**
