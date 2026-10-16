# V010_IMPORT_GUARD_DEPENDENCY_GATE_SOURCE_ONLY_DESIGN_RESULT

**SOURCE_ONLY_GUARD_DESIGN_PARTIAL_WITH_OPEN_GATES**；待 Astra 独立验收。不是 IMPORT_GUARD_DESIGN_COMPLETE、Windows runtime PASS 或科学 PASS。

固定任务 commit `79f82934184292e7d021cbef8d4322c02c9cc0bc`，tree `80a18652013613f883d4d8b48a87cb2a36c882f7`，blob `1bdb77a12d4494cae3052ba52392125a94bf0413`。实际读取任务全文、当前 CURRENT/TASK_CURRENT、上一 SOURCE_ONLY 独立主审、临时交换协议和 V1.2 工作流；精确 blobs 见 manifest.frozen_inputs。

## 结论、可信输入和证据限度

仅只读复用前轮两份已脱敏 MD/JSON，字节数15502/102135、SHA256与固定任务完全匹配；没有重新打开前轮私有 receipt、日志、raw capture 或发布对象库。JSON schema、70节点、1056 edge records及1049 unique tuples匹配；7个重复记录不改变42个入口词法候选。沿用20 UNRESOLVED、14 IMPORT_TIME_SIDE_EFFECT_RISK、8 PURE_DEFINITION，逐项保留原标签，不能把纯定义标签升为安全证明。

本轮从现有 Stage A 独立只读 clone 的固定 Git 对象重新认证42候选原字节和pyproject：43对象/518536B；另只读固定GitHub runner脱敏文本58055B，共44对象/576591B。4个只读Git child exit0，身份、独立common-dir及原blob SHA1 header/raw SHA256吻合。没有重扫70源码、取得模型网络对象、物化新源码根或改任何模型/guard。模型固定 commit `94de4501dec051b969bee9d852eba2d4591f30ef`、tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`、sole parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e` 不变。

重点结论：多数原“默认值/注解未解析”标记可具体解释为None、布尔、数字、字符串、预定义常量，或嵌套函数定义；**这只收窄局部风险，不证明完整Python语义链**。39个非init候选声明future annotations，三init主要执行eager imports与字面量exports；延后普通注解求值不证明dataclass/后续introspection没有行为。三真实非空init及其源序不可替换。

35个external名字已逐项分类：STDLIB_BY_NAME_ONLY、THIRD_PARTY_NATIVE_ABI_UNKNOWN、OUT_OF_SCOPE_REPO_NAMESPACE_UNKNOWN，另单列__future__编译指令。标准库名字不证明没被shadow；numpy/scipy的C/native初始化不能标PURE。`exports`与validators命名空间在本入口候选外，未递归取得，不能算已安装第三方或隐含许可。入口外动态helper的compile/exec/sys.modules路径仍禁止。

## 双根绑定：最小接口与不可放宽项

现runner `GitGate.root`同时用于Git cwd和`VerifiedFinder.root`读源。其4个身份命令分别为HEAD、HEAD tree、唯一parent、common-dir，第5个是固定commit的source inventory。本设计保留这五个真实child及原nonce/audit/Job/reap证据要求，仅把**未来**源码读取根分离；纯源码目录永不充当Git cwd。

伪接口为合同文字，不是可执行新runner：

|接口|结果与前置|
|---|---|
|VerifyGitIdentity(identity root, Git hash, fresh nonce)|四个真实有界child；全部身份及回收证据满足才可推进|
|ReadFrozenSourceInventory(identity session, fixed commit)|第五个真实child；只取冻结tree/path/blob/mode|
|SealBinding(proofs, source manifest, runtime image, policy, nonce/expiry)|受信任发行者签名或认证只读传递的一次性capsule；不能由普通布尔值自证|
|OpenBoundSource(capsule, module, source root handle)|同一最终文件handle的不可变原字节buffer、volume/fileID、路径身份|
|ExecuteApprovedImport(capsule, buffer, loader)|仅未来新授权可调用；LOADING成功返回才转EXECUTED|
|VerifyNineAndSeal(actual modules, handles, end readback)|九模块真实loader/spec/sys.modules/路径/字节一致；只生成证据，不自行验收|

绑定manifest至少含：固定任务/模型commit-tree-parent、五个Git真实child证明摘要、每个module→相对path→mode100644→blob SHA1 header→bytes→SHA256、三init身份/顺序、root volume/fileID/retained handles、runtime/stdlib/wheel/PYD/DLL及policy摘要、no-pycache、session nonce/expiry、start/end readback。签名的issuer、密钥可信分发和防重放机制仍须独立设计评审；哈希只能证明字节一致，不能单独证明授权或安全。

源根必须未来全新排他、位于项目/保护根之外且无symlink/reparse；不得共享common-dir/objects、hardlink/alternates或复制原工作树。拒绝ADS、UNC/device、相对逃逸、drive/case/8.3别名、保留名和模块映射冲突。**路径规范化+先查后开不足以抵御TOCTOU**：受信任broker应持有root/祖先handle，OS禁止不可信方替换目录，最终打开同一volume/fileID并审reparse，读同一handle、hash后compile同一buffer，再读回。句柄相对打开及共享模式的可行实现未在本轮认证；不能声称PowerShell chain或readonly属性已实现这些保障。只读属性、同用户可改ACL或可写父目录均不足。

no-pycache由受控启动参数、loader不走bytecode缓存和OS源写入拒绝共同约束。实际module.__file__/__path__/spec.origin、loader和spec.loader、sys.modules对象须绑定新源根；不以历史NEEDED/磁盘存在代替加载。现finder.loaded在exec前记项，未来状态设计必须区分LOADING/EXECUTED，异常不得伪作加载成功；九源必须全部实际成功绑定，不得为了凑九源再主动导入未审路径。

状态链：UNINITIALIZED → GIT_IDENTITY_VERIFIED → INVENTORY_AUTHENTICATED → SEMANTICS_REVIEWED → RUNTIME_IMAGE_VERIFIED → OS_ISOLATION_VERIFIED → BINDING_SEALED → SOURCE_HANDLE_AUTHENTICATED → IMPORT_LOADING → IMPORT_EXECUTED → NINE_LOADER_BOUND → END_READBACK_SEALED → WAIT_INDEPENDENT_REVIEW。每次推进要求全部前门证据和未来新权限；UNKNOWN不推进，身份变化、unexpected import、超额、timeout、deny失败统一FAIL_CLOSED。失败回执保留最后状态、限定错误码/相对对象、expected/actual hash、真实PID/audit/Job/回收及输出预约，不自动重试。

## IMPORT_GUARD：定义期执行与科学调用分开

源码读取、compile/exec是不同动作，本轮只做前者。未来loader要compile原字节；dataclasses标准库也可能通过代码生成产生方法。因此不能用“全局禁exec”之后再为通过import随意开洞；应认证固定loader、精确runtime及经审查的dataclass生成来源/类字段合同，禁止只凭函数名或`<string>`文件名豁免。property/classmethod包装不等于运行属性/方法体；`field(default_factory=dict)`当前创建字段元数据，factory在实例化时才运行。

只有已审明确的元数据构造可能进入未来定义期允许集合：AcceptedHAPublicAPI、六个DataArtifactProvenance及字符串/摘要验证。它们不等于构造GridSpec/HAInputs或真实省际输入。provenance.__post_init__的object.__setattr__不授予真实数据文件访问；字符串中的solver symbol不是动态import授权。Path全局构造不等于读取历史报告；MAIN_ONLY main不等于import调用。所有科学函数、数据loader、seal_json/报告writer、数值验证、property数值体仍禁止执行。

原profile只对`event=='call'`和有限co_name列表守门；不能涵盖别名、其它科学入口、C/native I/O/计算或运行时生成代码。原audit open/rename/subprocess等事件和Job正常退出正向证据也不是OS沙箱。必须同时有完整定义期语义审查、精确源/库身份、OS native约束；任何一个欠证继续STOP。不能把原68 synthetic PASS或69案例数量当本门运行证据。

## 第三方与Windows native门

冻结pyproject blob `5c778f7ccbbabfaf1046d4696cf843dc0adbb34c`仅给Python≥3.11、numpy≥2.0、scipy≥1.14、构建setuptools≥68。未来必须固定精确解释器版本/位数/build、exe/stdlib/发行物和PYD/DLL hash、可信来源及离线锁定依赖；setuptools属构建声明，不自动成为本入口运行必需。wheel RECORD也不是独立可信签名或完整native传递图。

未来启动应隔离site/user-site/bytecode和环境注入，逐项审适用的._pth、pyvenv.cfg、.pth、sitecustomize/usercustomize、PYTHONPATH/PYTHONHOME、sys.path、DLL search/cwd/PATH；没有观察到一个hook不证明历史全部hook可枚举。需审numpy/scipy/BLAS/LAPACK/OpenMP/runtime DLL、PE与delay-load和系统库、动态LoadLibrary；native依赖和初始化I/O的闭包目前UNKNOWN。没有pip/install/import或系统健康探针运行。

**建议供未来评审的首选隔离目标**是一次性Windows VM：无host共享目录/驱动器/剪贴板/凭据、无网络设备，输入只通过认证只读介质，输出经有限受控通道。没有声称本机现有此设施。Windows Sandbox/AppContainer/restricted token/ACL/firewall/WDAC可作备选，但必须分别证明实际read/write/network/DLL/process限制；名称或配置意图不是生效证据。Job限制与kill-on-close只管进程资源/生命周期，不能替代隔离。

这里有必须独立裁决的架构接点：原Stage A Git root在host，不能为了VM执行把它共享挂载进去或复制.git冒充同根。可评审的方案是host受信任identity broker执行原五个真实child，把新鲜签名一次性capsule和认证raw source传到guest；guest源码根无.git。**这改变现runner的进程/信任布局，必须独立审查child audit/nonce/proof如何保持，不能把历史或跨guest声明当原进程亲证。** 若坚持Git children与loader同地而无法安全保留原根，或无法证明broker传递可信，继续STOP。

OS拒绝模型访问真实/protected host数据、未批准file/registry/environment写、网络、子进程和image外DLL；库若确需cache/config/temp只能在明确受界guest路径，不能放开用户目录或整盘。日志/ETW/ProcMon等观察不能替代执行限制。高权限host/hypervisor及可信image是需要Owner接受的TCB假设，负例测试也不能证明对所有攻击绝对安全。当前保持 **IMPORT_GUARD_OS_NATIVE_ISOLATION_UNRESOLVED / STOP**。

## 最小后继顺序与审议分歧点

|门|当前资格|未来放行证据|
|---|---|---|
|H0 固定70身份/42风险队列|上轮documentary limited accept；本轮42原字节认证|仅复用证据，不提升为runtime|
|H1 全定义期语义链|UNKNOWN|42逐项、别名/from属性、dataclass生成及external初始化可解释；不重扫70凑结论|
|H2 双根/broker合同|设计草案|独立接受handle防替换、nonce/发行者及五child新鲜证据布局|
|H3 精确runtime与OS隔离|UNRESOLVED|Owner选隔离机制，可信image与有效限制独立审查|
|H4 非模型OS负例/N13/kill-reap|NOT_RUN|新进程/elapsed/RSS/artifact预算；真实活跃child及后代kill、timeout、reader join、PID回执；N13不可用外部timeout替代|
|H5 dependency-only初始化|NOT_RUN|H1–H4接受后另获运行许可；零model/data/science|
|H6 物化与真实九源loader|NOT_AUTHORIZED|再获明确预算，原字节/句柄/start-end绑定；首失败停，无补import凑数|
|H7 HA/Results/V011|CLOSED|工程接受不产生科学权限；另行Owner决策|

本轮不提虚构的新进程次数或预填预算；未来必须重新冻结进程数量、wall/RSS/输出和故障回收上限。Owner需决定OS隔离/host-guest信任布局及未来工程资源；普通静态默认值解释不需要每项重复征询。原数学、经济参数、GovInv 0.9/1.1、税扣一次、same-S/lagged ra0、迁移/劳动/原lagged-NKPC与科学输入均未修改。

## 实际资源与交付约定

新增源44份/576591B≤55/4MiB，只读Git4次≤120且均exit0；Git内部spawn未监控，UNKNOWN。前两脱敏输入另117637B。Python/py/AST/pytest/model import/runner/HA/HJB/KFE/selector/roots/GE/IRF/MATLAB/真实数据均0；源码装配、模型网络、clone/fetch/checkout、原模型/guard修改均0。新scratch非Git产物≤8MiB、wall≤2h，保留1MiB final/emergency预算；最终字节/耗时及clone index/config前后核对由独立LOCAL_ONLY DELIVERY_RECEIPT封存，不伪作Astra亲证。

一处新报告整理脚本曾因PowerShell数组tuple展平导致null索引exit1；已保存本轮失败记录，在许可的静态文档整理范围内修正聚合，重整exit0，没有执行源表达式或继续任何失败下游发布。该错误不改变冻结源码，也不触及前轮失败原件。

仅通过GitHub Git Objects API发布本报告与manifest，临时路径只出现在远端独立review分支Git tree：`_review_tmp/ch5/v010-import-guard-design-20261016/`；本机只有项目外非Git scratch中的平铺MD/JSON，没有创建该临时目录、本地Git仓库、index、checkout、git add、共享对象或.gitignore变更。唯一branch `review/ch5-temp-v010-import-guard-design-20261016`；唯一parent必须固定任务commit；ref创建最多一次nonforce。若API失败，LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED / STOP，不补推或重试旧候选。

本报告和manifest为PRE_REF_PUBLICATION材料，不能包含未来enclosing commit/tree自引用；远端ref/commit/tree/sole-parent/精确两路径/blob/UTF8原字节SHA256由提交后单独回执核实。Astra先永久治理归档并回读，之后才在该远端review分支删除两临时文件、回读cleanup commit；不会清理本机原项目，Git历史仍可能保留旧字节。

旧SOURCE_ONLY write-tree exit128及push0证据未修复/续推；B–E Python3/4、runner1/2余额STOP；旧driver1/4、HA1/26、pytest4/6、selector1626、roots1642及两次单点Python各1/1、首次存储超额9965206B保留。保护树、8dirty/index/staged/untracked/ignored/外common-dir及历史失败原证不进入。本轮Stage A仅只读。A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、real C8 A–D REQUEST_ONLY、FULL_RUNNER_IO_CLOSURE BLOCKED、V011 NOT_STARTED全部保持。

## 42节点逐项风险队列

以下保留原词法标签；每条source blob/raw SHA256/字节数、定位行、owner_decision_needed及guard_requirement完整列于manifest.risks_for_all_42。每项都已记录静态处置，仍不证明运行链安全。

|node|原标签|模块（共同前缀ch5_two_asset_hank）|静态证据与处置|
|---|---|---|---|
|0|PURE_DEFINITION|(root)|Real root init eagerly imports contracts,hjb,kfe,kfe_contract (lines3-6); literal __all__. Prior PURE_DEFINITION label is not an inert-package claim.|
|1|UNRESOLVED|boundaries|Defaults at63/99 are False for upper-face flags; dataclass at13. Solver expressions below definitions are function-local.|
|2|SIDE_EFFECT_RISK|contracts|Dataclasses22,53,78,107,130,140 and property wrappers44,48 execute definition machinery. GridSpec/EconomicParams __post_init__ numerical checks run on instantiation, not merely class definition.|
|3|SIDE_EFFECT_RISK|derivatives|DerivativeBundle dataclass12; differentiation operations in function bodies. Decorator implementation remains runtime-dependent.|
|4|PURE_DEFINITION|diagnostics|Function definitions/imports; diagnostics numerical bodies remain forbidden to call. Prior pure label cannot certify numpy/scipy initialization.|
|5|PURE_DEFINITION|economics|Function definitions/imports; utility/economic calculations remain function-local and uncalled.|
|6|PURE_DEFINITION|generator|Function definitions/imports; generator assembly is function-local and forbidden. Imports transitively execute other modules.|
|7|UNRESOLVED|hjb|solve_hjb43 default numerics=None; HJBNumerics dataclass19. HJBNumerics() at50 and iterative/numpy operations are inside solve_hjb, not default evaluation.|
|8|PURE_DEFINITION|indexing|Index helpers are definitions; no new top-level constructor flagged. Functions and external initialization not executed.|
|9|UNRESOLVED|kfe|solve_stationary_kfe72 defaults are numeric literals 1e-11,1e-10,1e-12; dataclasses16,30. Sparse solve is function-local and denied.|
|10|SIDE_EFFECT_RISK|kfe_contract|KFEInput dataclass13 and imports; input construction/validation and solver invocation are distinct from definition.|
|15|UNRESOLVED|policies|Header195 default active_b_upper=False; policy calculations and controls remain function-local; no solver invocation inferred from default.|
|16|UNRESOLVED|productivity|productivity_diagnostics56 default tolerance=1e-11; dataclass13. Generator and sparse arithmetic below are function body.|
|18|PURE_DEFINITION|corrected_diagnostic|Real corrected init eagerly imports boundary,contracts,cost,generator,saved_controls,panel,selector; literal __all__. Prior pure label is not absence of eager effects.|
|21|UNRESOLVED|corrected_diagnostic.boundary|assess/require definitions91/120 default tolerance=0.0; dataclasses12,22. Property wrappers33,38 do not call method bodies at definition.|
|29|SIDE_EFFECT_RISK|corrected_diagnostic.contracts|CorrectedDiagnosticGrid dataclass27 and property wrappers44,48; __post_init__35-42 invokes numerical validators only upon construction.|
|30|UNRESOLVED|corrected_diagnostic.cost|check_transfer_kkt76 default tolerance=0.0; dataclasses9,16. Cost/KKT numerical bodies are not import execution.|
|31|UNRESOLVED|corrected_diagnostic.generator|assemble_consumed_drift_generator57 default z_generator=None; dataclass14. Operator assembly remains forbidden function body.|
|33|UNRESOLVED|corrected_diagnostic.nonlinear_continuation|Definitions87/1685 default None;345 tolerance references CYCLE_TOLERANCE numeric assignment49. Path constructors58,61,64,67 do not read reports. Main guard1696-1697 is MAIN_ONLY.|
|34|UNRESOLVED|corrected_diagnostic.option_a_step|main1094 argv=None; dataclasses53,61; Path38 is construction, not read. main execution and input loaders remain forbidden.|
|37|SIDE_EFFECT_RISK|corrected_diagnostic.panel|BoundPanelCell dataclass34; scipy.io.loadmat import is library initialization, not a MAT-file read. Binding/loading function bodies denied.|
|38|UNRESOLVED|corrected_diagnostic.q0_kfe_validation|Defaults60/478/748 are None,123 is literal dtype string; dataclass66. Path45,48 is construction; resource import181 is function-local. Native/Job helpers must not be called.|
|39|UNRESOLVED|corrected_diagnostic.q1_kfe_validation|Defaults110 is literal dtype string,377/652 None; dataclass59. Path41,44 construction. Finalize and preflight functions perform I/O only if called, which is denied.|
|44|SIDE_EFFECT_RISK|corrected_diagnostic.saved_controls|Dataclasses16,25; loadmat is imported as symbol. Actual saved-control I/O remains uncalled; library native startup unproved.|
|45|UNRESOLVED|corrected_diagnostic.selector|Definitions30/466/596/666 have literal64,False,None and status string defaults. Dataclass class body279-281,288 calls field(default_factory=dict): field metadata now, factory delayed until instance creation. Scientific selector/root bodies forbidden.|
|46|UNRESOLVED|corrected_diagnostic.v1_q1_topology|state_index88 default SHAPE refers literal tuple45; main830 argv=None. Paths46,49 construct objects; topology math and main remain uncalled.|
|48|PURE_DEFINITION|multi_province|Real multi init explicitly imports household_adapter,provenance,annual,one_turn,migration_labor,government_assets,province_contracts,steady_state; must preserve source order and effects.|
|49|SIDE_EFFECT_RISK|multi_province.annual|Global regex compile27; dataclasses60,136,163,198,283,506 and property/classmethod wrappers. Workbook/XML/ZIP loaders and numerical transformation476-477 are function-local, not imports.|
|51|UNRESOLVED|multi_province.capital_allocation|Helper14 default n=None; dataclasses25,50. np.array validation/capital allocation is function-local and not permitted during import.|
|54|SIDE_EFFECT_RISK|multi_province.corrected_household_adapter|Dataclasses37,94,103; aggregation and conditioned household calls are function-local. Corrected contracts/generator imports still require authenticated chain.|
|55|UNRESOLVED|multi_province.firm|evaluate_firm44 default mainline=False; FirmResult dataclass20. Firm calculations are forbidden function-body execution.|
|56|SIDE_EFFECT_RISK|multi_province.fiscal_diagnostics|FiscalDiagnostics dataclass10; diagnostics body uncalled. No certification of external initialization from this label.|
|57|UNRESOLVED|multi_province.government_assets|Nested readonly137 default dtype=float is builtin lookup when its enclosing function reaches def, not at module import; dataclasses26,43. Batch construction and numpy calls remain function-local.|
|58|SIDE_EFFECT_RISK|multi_province.household_adapter|AcceptedHAPublicAPI instance27 is metadata only; MappingProxyType43,69 constructs mappings; solver names are strings. Dataclasses20,95,185,228. No dynamic import follows merely from a string.|
|60|SIDE_EFFECT_RISK|multi_province.mainline_household_runtime|HAInputs dataclass54; imports scipy.linalg,sparse,optimize.brentq,sparse.csgraph,spsolve. seal_json46-51 writes only when called, and household solving remains forbidden.|
|62|UNRESOLVED|multi_province.migration_labor|Helper14 default n=None; dataclasses35,76,218; property wrappers290-327. Reconstruction math is function-local, not executed by property creation.|
|63|SIDE_EFFECT_RISK|multi_province.monetary|MonetaryResult dataclass9; monetary calculation body uncalled. Frozen NKPC mathematics untouched.|
|64|UNRESOLVED|multi_province.one_turn|Helper47 default n=None; dataclasses58,96,134,164. One-turn functions and local imports remain forbidden; generator continuation363 is not top-level for.|
|65|SIDE_EFFECT_RISK|multi_province.provenance|Dataclasses9,75; six metadata instances37,43,49,55,61,67 execute __post_init__24-33 string/digest validation and object.__setattr__. No workbook open in this constructor; original data names/digests withheld.|
|66|SIDE_EFFECT_RISK|multi_province.province_contracts|Dataclasses18,38,58,80,114; construction can trigger validation. Declaring them is not instantiating actual provincial data.|
|68|UNRESOLVED|multi_province.steady_state|mainline_outer_diagnostics303 default reg_threshold=1e-9; dataclasses42,53,83,130. All outer iteration calculations remain uncalled.|
|69|PURE_DEFINITION|multi_province.wage|Wage functions/imports only in current risk inventory; numerical body not run. Pure label does not authorize import or calls.|

**WAIT_ASTRA_V010_IMPORT_GUARD_DESIGN_REVIEW / STOP**
