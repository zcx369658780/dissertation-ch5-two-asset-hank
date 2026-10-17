# V010 CP2_F25 selector机制取证与条件式修复（唯一版本长任务）

**TASK_ID：V010_CP2F25_SELECTOR_MECHANISM_AND_CONDITIONAL_REPAIR_LONG_TASK**
**交付ID：V010_CP2F25_MECHANISM_REPAIR_LONG_RESULT**
**版本：V010 / v0.0.10；V011 NOT_STARTED。**
**Owner授权来源：2026-10-17「可以，我同意你的建议继续V010，先修复」。**
**生命周期：F源证取证→R同数学合同条件式实现修复→D受界单格诊断→集中STOP交Astra。**
**任务发行Commit/Git Blob由紧接本任务发行的CURRENT/TASK_CURRENT精确固定；任务原文一经发行不追改。**
**终态：WAIT_ASTRA_V010_CP2F25_MECHANISM_REPAIR_REVIEW / STOP。**

## 0. 定位与不变权威

这是前一长任务科学FAIL_CLOSED后**新签的一张**独立V010机制修复长任务，绝非将旧STOP/旧26次HA余额重新开放，也不按每一个普通程序bug拆微任务。

- 治理repo：zcx369658780/dissertation-ch5-two-asset-hank；权威branch：migration/astra-workflow-20261012。上一M1终审固定Commit：14fcd57591295cfa62b8ced52d70646d7719e254；独立主审Blob：c5873368f2d011280066fbc7b4dbeef5e91ffdd0。上一任务发行Commit 54454066859692a0f481cfa44de8df8dc298ce03、Blob 5d87753b4a3ac972f37f1ac59722b464efd11bd9；其ACTIVE_TASK已为NONE，科学结论已STOP，旧预算关闭。
- 数学最高约束：冻结V010 plan Commit bf091da33d59293f147d52c11580327d3ac2a85d / Blob 85138d8859d53295262fe13bf5bc277bca95ed3f（**原数学、输入和数值门不变**）。冻结模型Commit 94de4501dec051b969bee9d852eba2d4591f30ef / Tree 205eab47c4e4f9c6292c2ead9947d94d1a7579a5（70个Python源码、3个真实非空init），fixture Git Blob 40915658d93403cfc21b33a6b864b332b7857749，原字节SHA256 BC002D71430D5472F8C5C62543F07A845F2D6BF564CB5BB92E6DD8142AC50252。
- **本轮调查的实际算法执行视图**是上一M1上传ZIP里的 final_view_v2（含已回读的B0两路径工程补丁），其LOCAL_EXECUTION_VIEW_ONLY Commit bb5eae2dfb84c9d73b6644f97148eb244b4cf4fa、Tree 6243e58b7acc36f868f057022267a6b78428ea92 **不是**已经上传GitHub的完整模型候选。其B0_TWO_PATH_PORTABLE.patch SHA256 B89161B09445B53E4541C070578D64FC6EB39AB341E9C1BEA20A9C7093E5C76B；严禁把本机候选误称远端主分支或擅自覆写原仓。
- Owner私有历史ZIP：D:\ProjectTemp\ch5_v010_m1_science_bridge_20261017_01\CH5_V010_M1_LONG_RESULT_20261017.zip，1,877,576B、SHA256 D76207C452496737D4A9DCA159A197826E9053A7298383AD003A6BEB30AD2E8B。内有425份原始/派生身份分明的证据，不扫描其根目录其他未知对象。核心失败原件 science_driver_01/HA_01_binding/first_failed_cell.json，22,390B、SHA256 E01A5E5137424C238F8090903D21970910A2CC1562103FC2C78FB16E0487CEC3。
- 上一科学事实不得改写：SYN_A首次HA，CP2/F-order flat25、b=-0.1578947368421053、a=0.5263157894736842、z=0.8，12候选全部inadmissible、selected=null，HA1、maps3（800/800/26）、HJB更新2、roots1642、selector cells1626、KFE0。无完成的HJB双门或KFE；B2/B3/B4均未运行；FULL_RUNNER_IO_CLOSURE=BLOCKED；model_activation=False、REAL_GE=False、Results FALSE。

**本次立即授权仅限源码/冻结证据取证、非求解数学oracle、受界单格selector诊断及严格等价的程序实现修复。新的完整HA/HJB迭代、KFE、跨省outer、GE、IRF及现实C8科学调用预算全部为0。** 是否投入下一轮真实HA，由Astra审议修复证据后请Owner再作阶段决策；本任务不能偷换为新的synthetic HA实验。

## 1. F阶段：先锁定具体机制（绝不靠放宽门）

从精确原件构造两份分账的只读参照：（a）原冻结selector与原数学规范；（b）上一B1实际执行视图中使CP2_F25失败的原源码、HJB历史V0/更新与完整十二候选原件。逐字节验证来源，不从日后Git HEAD替代固定模型身份。冻结网格20×20×2、F-order b-fast、Delta=1000、原V0输入与SHA保持。

非求解/只读静态检查至少覆盖：
1. **十二候选逐一映射**：转换negative/zero_kink/positive、b/a backward/forward/zero、候选创建与丢弃前置、可行域、g_b/g_a、q_b/q_a、transfer KKT、完整rejection reasons、Hamiltonian/D2源门；记录每个可能漏入的分支/活动集，而非只抄NO_ADMISSIBLE_POLICY。
2. **流动与非流动双轴守门**：冻结F25 p_b_backward=0.5460198582796224、p_b_forward=0.41906757997286065；p_a_backward=0.5436727408844979、p_a_forward=0.40495349203417863。以原FOC、资产转移律和direction/upwind定义**独立推导**漂移、零漂移约束、单位及浮点区间；不能把g_b正/负时使用的单侧导数倒置当作修复。
3. **严格筛查联合零漂移**：重点复核 corrected_diagnostic/selector.py 中 _interior_z_candidate、_interior_a_switching_candidate、_joint_switching_candidate 和 select_constrained_policy 的joint_contexts生成及最终fallback之间是否存在**比冻结D3/已采纳合同更强的误筛**。分别判断（i）原合同是否有满足g_b=g_a=0、q_b>0、q_a在合法导数区间、原KKT和边界条件的候选；（ii）若有，哪个源码前置误拒；（iii）若不存在，不得以新增政策或删KKT约束救活格点。
4. **数值与真实逻辑分账**：第三策略映射的局部overflow Warning只是线索，不是假定根因；检验原root bracket/根唯一性、零漂移精确残差、负ratio内点与先前F0364验收、所有已接受D1/D2/D3边界和KKT。若只能推测代码bug、不能证明冻结法则下确有被遗漏的合法候选或纯控制流错误，归类UNRESOLVED/MATHEMATICAL_GAP并STOP，不做猜测式patch。

F阶段交付最小证据为：原函数行号/固定Git blob、F25候选矩阵、独立代数/浮点oracle、从数学条件到代码筛选的对应表、唯一根因候选及其反例/证明、原本无解可能性的替代假设。**缺证明时不为PASS编造解。**

## 2. R阶段：只在能证明原合同等价的情况下修复代码

Owner本次「先修复」只新增一个**任务内、独立候选视图**的特定代码修改许可：src/ch5_two_asset_hank/corrected_diagnostic/selector.py 中经取证证明与**已接受数学合同等价**的候选枚举/分支守门/错误筛选实现修复。这是前一15路径白名单以外的**本新任务限域例外**，**不追改原冻结plan**，也不等于Owner接受新的经济/数学法则；如果需要改变已采纳的D1/D2/D3约束、KKT定义或数值门，立即E3 STOP，请Owner另决策。

**候选工程路径白名单仅2条：**
- src/ch5_two_asset_hank/corrected_diagnostic/selector.py（只修经证明的实现缺陷，最小局部diff）。
- tests/test_v010_cp2f25_selector_mechanism.py（唯一新增focused回归测试；包含成功/拒绝/边界/原历史正反例）。

必要测试辅助脚本、pure math proof/trace仅放独立scratch（不进入源树）。原本B0已生成的 mainline_household_runtime.py 和 v010_mainline_validation.py 补丁视图**保持原字节只读**；corrected_diagnostic/cost.py、option_a_step.py、generator.py、其他数学模块、原MATLAB和全部现有测试文件不在本次可写白名单。若发现错误其实位于白名单之外、或需要实质新数学规则→STOP，一次提交机制报告，不能暗中增加第3路径。

禁止：按CP2_F25硬编码成功、强行selected、丢弃inadmissible reasons、移除单轴/联合strict crossing、允许非法q_b/负质量、改成本/消费/劳动效用方程、放松KKT/arithmetic tolerance、改变F-order/网格/Delta、换合成输入/Owner未测试价格、clip或增加Newton/fsolve；不能从人工局部成功推出所有省HA已合格。

代码修复须有**先于变更的原数学oracle**和修复后的反事实、负例及旧F0364/D3/边界回归，并证明不再错误接受原本应被拒绝的候选。普通E1脚本与测试错误可在本任务总预算内自行更正，保存首错，不再逐项申请微任务；E2身份/账本/首写、E3数学/保护/额度越权立刻STOP。

## 3. D阶段：单格数值诊断与独立验收前STOP

非求解静态测试可正常运行；允许**明确计费、真实调用的pure single-cell selector-only diagnostics**（并非HJB/HA/KFE），仅限冻结F25及基于同一定义构造的邻近正反/边界synthetic cells、历史已接受F0364及D1/D2/D3回归。这类调用不得被报告为「科学求解调用0」：须列selector诊断次数、其内部root数、PASS/FAIL，且与未来真实HA预算完全隔离。

硬计费上限：selector-only diagnostic evaluations ≤64、其内部scalar-root ≤2048；不得使用该额度计算800格全域policy-map或伪造完整HJB。若诊断通过，仅能判为「MATH_PRESERVING_SELECTOR_IMPLEMENTATION_REPAIR_CANDIDATE_READY_FOR_ASTRA_REVIEW」，**不**自动释放真实HA及第二次绑定。

最低回归要求：
- 旧F25原件精确重放（修复前NO_ADMISSIBLE_POLICY，若不同则身份/执行口径不符→STOP）；修后如判通过，输出被选候选所有方向/漂移/KKT/根残差/两个资产的合法证明、拒绝的其他候选全列表，绝不只有selected=True。
- 以前accepted的F0364负ratio切换、联合开/关根合法性、lower/upper资产边界、KKT损坏负例、无根情形依旧FAIL_CLOSED；保证变化限于数学上证实的遗漏分支。
- 静态源码diff与每个单格测试的源码hash、测试输入hash、执行器/Python/NumPy/SciPy版本、全部科学调用实际计数封存；若因算术/警告、新NO_ADMISSIBLE_POLICY、原回归失败，STOP如实记录。所有测试输入仍仅synthetic，真实省数据0。

## 4. 新任务资源、隔离与第一次写入

**新计费账**：独立run_id和single-writer ledger，旧M1 STOP的剩余次数全部0不可迁入。墙钟≤6小时（从本任务首次被许可写/运行开始；暂停不豁免真实执行耗时）；工程Python/AST/stub/测试子进程总数≤24，其中focused pytest启动≤8（计入24），每个测试子进程≤600秒；单格selector诊断最多64次/2048 scalar roots；**完整HA/HJB/KFE/policy-map/outer/GE/IRF真实模型driver全为0**。受界旧证唯一归档ZIP及其定名成员只读（累计读取≤64MiB），新增非Git artifacts≤64MiB，非合作模型Git写入0，内存采样目标≤512MiB，未知记录UNKNOWN；预算溢出FAIL_CLOSED而不是重命名一次运行。至少预留证据封存/交付空间。

**唯一建议scratch**：D:\ProjectTemp\ch5_v010_cp2f25_repair_20261017_01；仅当原路径第一次写入前身份门拒绝且无任何本轮写入时，才可在已单独认证的全新 _02 备选，严禁失败后删除/复用旧目录。开始前严格按V1.3 BOOTSTRAP0可信只读父路径/保护根/alias/reparse/UNC/device/ADS身份→BOOTSTRAP1新目录创建后首文件前二次回读→BOOTSTRAP2才允许写工具/first receipt；路径未知直接STOP。不可回填首次写入证明。

**保护清单**：D:\ProjectTemp\c5k1bturn56（8 dirty及index/staged/untracked/ignored、外external Git common-dir）、原M1 scratch和425证据、C盘物理SSD备份、原仓/model源码、真实C8/2017/2018/B3/V009及全部历史FAIL/UNKNOWN文件一律不写/checkout/clean/stash/reset/merge/worktree attach/共享Git对象。旧模型/新候选只可从已验证源字节在新独立scratch中物化；不得强制新增VM、第三备份、global/system Git配置、联网pip。受信任Windows工作站≠已独立认证native OS sandbox。原模型/论文/现实数据模型激活始终FALSE。

## 5. GitHub-first脱敏审阅与一次性交付

本轮正常审阅改回Owner批准的**GitHub临时路径优先**，不必每轮让Owner搬运小型脱敏MD/JSON。具体冻结：
- 独立远端ref（首次发布前必须确认不存在）：review/ch5-temp-v010-cp2f25-selector-mechanism-20261017
- **仅远端Git Tree**中的路径：_review_tmp/ch5/v010-cp2f25-selector-mechanism-20261017/
- 白名单：result.md≤32KiB，manifest.json≤128KiB；若发生源码修复，可追加**同次发布**的 repair.patch≤64KiB（UTF-8 LF、非执行）。原始failure cell和敏感完整raw不得未经审核上传。
- 新review提交应恰以本任务正式**发行commit**为唯一parent，并只新增上述白名单最多3件；Codex只能用Owner现有SSH Key、ssh.github.com:443，在原项目树外独立无工作树/无共享对象的bare Git对象库准备并最多一次普通nonforce push；首次身份/provenance/readback/认证缺失、SSH失败或发布越权即LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED，**不得重试扩大网络预算、改PAT/全局config**。禁止在本地项目树/index创建_review_tmp，GitHub仓main/治理/模型候选不得由Codex更改。
- Codex先匿名化Windows路径、秘密、日志原argv/环境，再生成白名单。可在独立scratch保存一份私人raw evidence ZIP（≤上述artifact预算）交Owner手动上传作为fallback或E3独立审查需要；网上公开sanitized digest不可替代未上传原raw。
- Astra后续从精确remote commit取全部脱敏文件、验证唯一parent/Blob/SHA、必要时要求Owner提供私人ZIP，**先永久归档正式科学审议并远端readback、后仅清指定白名单temp文件及回读**。不删整个历史或其他分支；Git删除不抹Git历史。

## 6. 终态与Owner集中审议

只交**一次** V010_CP2F25_MECHANISM_REPAIR_LONG_RESULT，最低字段：任务发行Commit/Blob、原冻结plan/model/tree/fixture身份、旧第一失败原始引用、数学候选覆盖/联合切换证明、源码diff白名单、原反例/修后单格诊断正反案例、首/终原始证据hash、Python/test/selector-only/root次数、资源/保护/UNKNOWN、远端review精确Commit/Tree或LOCAL_ONLY、每阶段PASS/FAIL/NOT_RUN及最早STOP。不要用冗长中间报告或把每次普通脚本错误上交审批。

可接受终态分档：
- **FIX_PROVEN_LOCAL_SELECTOR_ONLY__WAIT_ASTRA_INDEPENDENT_REVIEW**：原法则下确认具体实现漏项，最小patch与单格回归支持；不是HA PASS。
- **NO_MATH_PRESERVING_REPAIR_PROVEN__STOP**：原法则下无可接受候选/机制未确定/白名单外错误；不伪造修复。
- **E2_E3_OR_BUDGET_FAIL_CLOSED__STOP**：任一权限/前置守门/资源越权，完整保留首错。

交付后**立即STOP**：WAIT_ASTRA_V010_CP2F25_MECHANISM_REPAIR_REVIEW / STOP。Astra集中审议后由Owner决定是否为下一张V010科学验证任务另给新HA预算；**本任务本身没有完整HA科学授权，不允许擅自启动第二次绑定、B2稳态、B3目标或B4短动态。**

未变的原V010经济合同包括目的地工资税一次、phi[j,i]方向、same-S数量与上一完整轮raw-ra0、家庭人均/人口/财政总量桥、GovInv×0.9/1.1及Zt独立GDP≤1%冻结核验、tKN平滑、lagged-NKPC；HA双门B≤1e-8且D≤1e-7，后向误差≤1e-12，halving0..52，唯一闭类source-free KFE。原A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、FULL_RUNNER_IO_CLOSURE=BLOCKED，model_activation=False、Results FALSE、V011 NOT_STARTED均持续。
