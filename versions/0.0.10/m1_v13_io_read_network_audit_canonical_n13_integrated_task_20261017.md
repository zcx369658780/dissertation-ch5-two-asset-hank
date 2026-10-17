# V010 M1 · V1.3 IO_READ_CLOSURE、NETWORK_DISABLED、canonical import 与 N13 集中工程闭环

**唯一任务ID：** V010_M1_V13_IO_READ_NETWORK_AUDIT_CANONICAL_N13_INTEGRATED_REPAIR
**版本：** V010/V0.0.10；**类型：** ENGINEERING_ONLY_IMPORT_AND_RUNNER_IO；非科学求解。
**新Owner授权：**2026-10-17，在上一项M1 import/runner部分验收并正式STOP后，同意继续一张集中工程任务：定位IO_READ_CLOSURE、NETWORK_DISABLED实际拒绝原因，工程修复后验证canonical/九模块身份，并按条件验证N13。此授权不复活旧任务、不改变经济学合同、不自动开放科学HA。
**交付ID：** V010_M1_V13_IO_NETWORK_CANONICAL_N13_INTEGRATED_RESULT
**终态：** WAIT_ASTRA_V010_M1_IO_NETWORK_N13_ENGINEERING_REVIEW / STOP
**冻结机制：**任务第一次GitHub发行Commit和Git Blob由随后TASK_CURRENT登记，发行后不得追改本文件。Codex只能从**固定发行Commit**读取此文，不凭聊天摘要执行。

## 0. 固定权威、前轮事实与本轮成功标准

仓库 `zcx369658780/dissertation-ch5-two-asset-hank`，治理分支 `migration/astra-workflow-20261012`（不是main）。先核发行任务Blob、CURRENT/TASK_CURRENT、docs/DOC_INDEX_CURRENT.md、docs/CH5_ASTRA_WORKFLOW_V1_3_20261017.md、Owner Loader技术决定及remote-only GitHub审阅协议。发现状态冲突或冻结身份不匹配即STOP。

上一冻结任务：`V010_M1_V13_VERIFIED_IMPORT_RUNNER_INTEGRATED_PREFLIGHT`，发行Commit `1f379141cc8c7cf84a4c798f31f8b21dd3eedc7e` / Blob `f914da78fdce9b6c41fc29f68743c70f8ae83ffc`；正式主审 `versions/0.0.10/m1_v13_verified_import_runner_local_only_partial_review_20261017.md`，Blob `1854241be531177dbda256191bcbbbdeb72ca25e`。该主审只限 `PARTIAL_ENGINEERING_DIAGNOSTIC/LOCAL_ONLY`：Codex报告70冻结模型源码和三个非空init原字节装配、双根Loader局部修正、两次真实runner各5 Git child/Job/PIPE/reap局部结果；**import**分别被 `IO_READ_CLOSURE`、`NETWORK_DISABLED`拒绝。首次被拒目标、network audit事件子类型、退出前模块表 UNKNOWN；N13未执行（合成适配器提前异常）；上一首次runner变体仅留hash、无源码原字节，不能推断当时执行字节；目标review分支实际404，fetch/push=0。上一工程Python4/6、旧Stage A Git24、PS29、126非Git文件1,720,053B、终态receipt SHA256 `4BE31B06959200677C6D42F86EAF0FD43E8244F5750780A1B7CC23FB1E5BC636`均为Codex本机报告，网页未取得原raw；**旧Python剩余2次等所有旧余额已STOP，绝不结转**。旧first、含用时计算错误的原final、仅修正时间的关联final及终态receipt必须保留为不同字节实体，不能在新任务下改写。

**验收目标按门分账**：(A)找到首个实际IO拒绝动作和network拒绝的审计event类型/发生位置分类，证明是否真的有网络企图，而不是根据标签猜测；(B)在不放松安全合同下令canonical import-only至少一次真实通过并准确记录加载模块身份，九个原监测模块如需显式import必须另标签记录；(C)至少一次真runner I/O import-only有界完整通过且N13 dummy活进程超时/回收负例在安全条件下验证；(D)可选远端脱敏证据独立交付。结果允许PARTIAL/FAIL_CLOSED，**不能把A/B/C某一门通过当全部PASS**。

原科学V010冻结plan Commit `bf091da33d59293f147d52c11580327d3ac2a85d` / Blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；模型Commit `94de4501dec051b969bee9d852eba2d4591f30ef` / Tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5` / sole parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`。70份`src/ch5_two_asset_hank`原始.py及3非空`__init__.py`不可更改。HA/HJB/KFE、selector/scalar roots、真实C8/2017/2018/B3、双省/31省GE、GovInv/Zt稳态、经济冲击/IRF/论文Results均**0次运行许可**，corrected HA单点 `rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07`仍UNTESTED。

## 1. E0：新scratch与旧原证精确只读

**唯一新可写工程根：** `D:\ProjectTemp\ch5_v010_m1_v13_io_network_n13_20261017_01`。先在原有可信PowerShell/Windows终端进行**零写入**父路径及目标不存在/保护根交叠/无reparse、junction、UNC、ADS、device、alias等V1.3 BOOTSTRAP0身份检查；如不成立终端匿名STOP，绝不先向待验目标写脚本、日志或receipt。BOOTSTRAP0通过才创建根，**在写第一个字节之前**重新核新根及父目录身份，真PASS才写first/run_id/sourceIndex、后续脚本；不可删除或重建已失败旧scratch以冒充新根。

旧上一轮工程根 `D:\ProjectTemp\ch5_v010_m1_v13_import_runner_20261017_01` **只读**。仅允许从上次可信receipt/manifest已有准确相对索引及任务证据引用中读最少工程结果、原runner代码变体（**只在真实字节存在且whole-file SHA256实核时**）、双根Loader/IO audit方案、原First/原Final/关联Final的必要匿名字段。为避免空sourceIndex阻断，允许对此**唯一旧根一次depth=0非递归直接子项元数据盘点≤32项**，然后仅依身份锚点按白名单选内容，不泛目录/全文递归扫描；旧文件不同件数≤16、**全部实际重复读取字节累计≤3MiB**，每件读前后hash/大小/非reparse核验；若原变体确无字节，记`RUNNER_VARIANT_EXECUTED_BYTES_UNVERIFIABLE`，不得由hash虚构源码，也不可把它当本轮可执行起点。旧原件、C备份、原历史工作树/index/common-dir绝不触写。

优先从本轮固定Git模型Commit的真实Git blob及已获本机身份验证的原Stage A只读Git对象重组70份原raw源到**新**source_assembly_root；可以把上一任务old assembly作为只读cache候选，但必须每份raw与固定Git身份逐一重核才可复制到新根，不能直接从旧可写目录import或用旧无原字节runner变体。新根及70源运行前后完整SHA1/SHA256/size/mode核验；Git identity root仍为独立只读Stage A clone，所有五真实Git child的参数/nonce/bounded stdout/stderr保持合同，不随意改全局Git环境。

## 2. E1：先补“拒绝事件”可观测性，而不是关守门

在新scratch新建**安全匿名audit/IO回执**，记录每次阻断的`audit_event_class`、`event_subtype`、`deny_rule_id`、`first_denied_action`、`authorized_source_category`（仅固定模型包/已认证Python stdlib/已认证现有NumPy或SciPy/native依赖/项目外工程dummy/其它或UNKNOWN）、source模块标识的安全相对路径或hash、允许表/deny来源、PID/退出/发生阶段。不得把原argv、用户绝对路径、实际host/port、密钥、完整traceback或未经脱敏原source lines打印进外发材料；无法安全定位时用匿名hash+UNKNOWN，不能猜测。

`IO_READ_CLOSURE`必须先辨识**真实首次被拒对象**属于已认证源码、stdlib、只允许工程的第三方依赖还是未经授权的真实数据/保护根/动态路径。如果确为冻结可认的依赖读取，允许在本轮工程scratch修复**过窄的分类器、source-root映射或白名单构造逻辑**，条件是该目标路径/文件与Git固定byte identity或受信任解释器/依赖实际hash一致且对应原已准许工程import来源；不能无证据增加任意root/通配路径。若指向保护根、未批准文件、未知DLL或数据，则保留DENY并E2 STOP。

`NETWORK_DISABLED`先记录**哪个审计event subtype和哪个来源组件**触发，区分安全模拟误分类、导入时初始化可能的socket创建/配置/连接企图与实际网络访问；如果只是audit分类器错误，允许在本轮scope内修事件到风险分类映射并在纯dummy负例验证**真正socket/network动作仍DENY**。如果确认存在实际外联企图或来源不能证明安全，保留network deny并STOP后续canonical import；严禁为了取得PASS关闭network guard或做一次“有网再试”。**前次仅有NETWORK_DISABLED标签不能用作已经联网事实**。

同时修复合成适配器提前异常（限本次新scratch，保留原失败），为N13提供完全独立于模型包的无网络dummy进程负例；不得改原模型代码。原双根VerifiedFinder/VerifiedLoader须在`exec_module`真正成功后才记EXECUTED，失败记LOADING_FAILED；任何退出前的`sys.modules`源集合与`module.__file__/__path__/spec.origin/loader`只在实际可观测时记录，不能用预计九模块冒充真实加载表。

## 3. E2：仅在真实IO与network guard已经安全证明后验证

采用Owner既定可信工作站非提权、受界Python `-I -B -S -X utf8`或实证等效安全模式，已认证stdlib/NumPy/SciPy/native路径和真实Windows Job/audit/双PIPE/PID/reader/reap，禁pip/未知环境/未授权网络及写入保护根。采用源身份认证的runner源**全文件原字节**，不得重用上一丢失raw的runner变体。当E1已证安全后：
- 实际仅import冻结的canonical入口 `from ch5_two_asset_hank.multi_province import mainline_household_runtime`，不给任何模型函数参数、不调用`solve_conditioned_household`或其它scientific API。
- 只在另行明确记录`EXPLICIT_NINE_ALLOWLIST_IMPORT_ONLY`标签的受界工程进程中可额外import原九份已核冻结模块，canonical自然加载名单、显式追加名单严格分账；凡新的动态依赖source hash不能认证或import-time科学/数据/网络操作出现即STOP。
- 至少一次真实Windows runner的**import-only** I/O smoke（含准确5个Git只读child、Job、PID、双PIPE、reader join、timeout/reap、source byte before/after），才可由Codex报告候选工程通过。不能把前次两个runner正常退出等同本次完整认证。
- N13 dummy活子进程超时/kill/reap/reader退出，必须独立于模型计算；允许在E0身份门及工程dummy安全门通过后提前做**一个**这样的受界负例，即使canonical import未通过也可记录独立N13结果。若适配器再次异常，记N13 NOT_EVALUATED和首次失败，不造PASS。

日志只用有界匿名来源ID/分类与各进程exit/wall/资源；无论PASS/PARTIAL，模型HA/HJB/KFE/selector/root/GE/IRF调用数严格为0（无法核证就UNKNOWN/STOP），`model_activation=False`持续。

## 4. V1.3本轮一次性工程预算与止损

**本任务独立新预算，旧所有STOP剩余额（包括上一Python未用2次）永久不得继承**。
- 总wall≤**180分钟**；工程Python及衍生Python合计**最多8个进程**（受界static/dummy verifier≤2、匿名拒绝源probe≤2、canonical/显式九模块import≤2、runner import-only≤2），每Python进程外部wall≤180s。N13如果使用Python dummy必须计入这8个；另允许非Python惰性dummy child≤1（每次PID/Job计费，最长90s）。同一任务中E1普通错误可修改并在余额内最多3轮focused工程回归；不能通过隐蔽子进程重置分类额度。
- 新scratch非Git文件（含重装70源、新runner源码、匿名诊断、原始first/final、失败及emergency预留≥2MiB）累计**≤32MiB**；独立bare Git对象库如可选E3进入≤2GiB另列。已存在只读Stage A Git操作≤**100**次；真实runner每次最多5条Git child且全部单独计数；日志每进程stdout+stderr合计≤256KiB，异常超过上限立即FAIL_CLOSED；RSS尽可能在外部取证，未知记UNKNOWN。须事先证明本轮所有资源与收尾额度可用。
- E1仅限新scratch中受界小错误（日志schema、loader/path分类、runner adapter、dummy test）自主修复；E2写前路径、来源SHA、未知读/未授权动态访问、预算超限必须STOP受影响链；E3真实数据/旧保护根、科学求解、实际外联、修改原数学/容差、秘密公布须无条件STOP。只观察不代表可放行，不能将网络guard从DENY改为ALLOW来得PASS。
- Python模型import可以执行包初始化代码，但只准Owner已接受的TRUSTED_WORKSTATION_ENGINEERING_CONTAINMENT，**不**宣称OS_NATIVE_SECURITY_SANDBOX_VERIFIED。若无法证明读取源合法或import有危险副作用，宁可局部诊断STOP也不得继续。所有已报告的上一E0 70份hash与runner尝试都属本机报告，本轮重新认证是必要工程input，不算科学“重跑”。
- 所有旧B/S/L20旧first原字节/run_id缺失、旧timestamp25项24预期+1 SPEC_UNRESOLVED、旧sanitizer DENIED、历史ledger偏差保留，**旧25/17/20 tests=0新执行**。任何本轮新first/final分别保留可取原字节、相同run_id、不可逆hash链接；如果原final的wall记录出错，只追加受别名标识的修正副本，不覆盖原final、不反算历史修复。

## 5. E3 可选独立GitHub审阅（工程结果先于运输判定）

只有新scratch前置身份与源保护/脱敏门全部合法时，才允许将本轮**已有**工程诊断结果做一次远端独立review；如SSH或网络预检失败，保留本地前两门证据的等级并记`PUBLICATION_LOCAL_ONLY`，不额外重试同ref、不能让上传失败伪装本地工程失败，也不能宣告Astra远端独立PASS。

唯一远端review分支：`review/ch5-temp-v010-m1-io-network-n13-20261017`。
唯一远端树新增前缀：`_review_tmp/ch5/v010-m1-io-network-n13-20261017/`。
**仅5个 UTF-8/LF 严格脱敏非可执行文件**：
`result.md`≤32KiB；`manifest.json`≤128KiB；`io_network_audit.json`≤128KiB；`import_modules.json`≤128KiB；`n13_runner.json`≤96KiB。
Candidate唯一sole parent必须为**本任务发行Commit**，原parent tree其它路径0改动；review分支发布前核不存在，不污染model/main/治理树。远端`_review_tmp`**不得在本机任何模型/研究/治理工作树/index/scratch中创建目录**，本地只允许独立scratch的平铺候选文件和不共享对象的`git --bare`元数据仓，无checkout/worktree/alternates/hardlink。用Owner原SSH Key到`ssh.github.com:443`严格host key，不求PAT/新令牌、不更改global/system配置、不上传原argv/source/raw logs/用户路径/hostname/port/token/实际研究数据。manifest列其他4份文件hash/size与raw-vs-derivative来源等级，自己SHA256外置交付防循环；源本机raw声明不能冒充远端已认证字节。

脱敏结构化扫描至少1次、至多2次（第一次失败只修投影不得放宽DENY）；**SSH精确ls-remote≤1、完整固定parent fetch≤1、普通nonforce push≤1、远端ref readback≤1**；Git hash-object≤5、mktree≤10、commit-tree≤1，extra read-only Git objects探针≤40，任何失败不给重试额度。整个remote tree只能增以上5个经scanner PASS文件。必要parent缺blob/object closure则LOCAL_ONLY STOP E3，不借主模型clone/fetch。Codex只报告候选Await-Astra，不自授科学或完整工程PASS。

## 6. 交付与永久冻结保护

最终只交一份**≤5KiB安全摘要**，逐门给(E0 prewrite+固定源，E1首次拒绝IO目标和network事件分类，E2 canonical自然模块和明确九模块/runner/真实五child，N13真实或NOT_EVALUATED，E3候选/LOCAL_ONLY)状态、实际进程/资源账、front-first/final/raw SHA+run_id及必要派生层、首次错误与E1修复记录、拒绝规则（不含敏感值）、上版未闭UNKNOWN保持及条件后续目标。若E3成功报candidateSHA/tree/唯一parent和5份远端GitBlob/SHA256/大小；未发布则不假设remote evidence或Astra原raw验。

**必须保持：**原`D:\ProjectTemp\c5k1bturn56`8dirty/index/staged/untracked/ignored及外Git common-dir、全部旧失败scratch、C盘物理独立SSD原备份、真实C8/2017/2018/B3/V009原件不可写/清理。学科主线为原MATLAB corrected两资产HA/HJB/KFE→多省手动有界顺序→GovInv收益界乘0.9/1.1及Zt→冻结后GDP每省≤1%独立核→原lagged-NKPC；目的地工资税一次、same-S/前完整轮raw ra0、家庭人均/省财政量纲/三劳动账、phi_max=.3和20×20×2原阈值不变。

**FULL_RUNNER_IO_CLOSURE=BLOCKED直至后续独立工程核准；model_activation=False；Results FALSE；V011 NOT_STARTED；A16 FAIL_CLOSED；window UNACCEPTED；C9 PAUSED；CALL_LEDGER UNRESOLVED；real C8 A–D REQUEST_ONLY。** 实际科学HA必须未来Owner另批准，即便工程全PASS也不能自动开始。
