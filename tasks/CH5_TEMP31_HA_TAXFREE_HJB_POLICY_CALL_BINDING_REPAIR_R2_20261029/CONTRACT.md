# TEMP31 HJB→policy未绑定函数名：严格最小隔离修复 R2

TASK_ID=CH5_TEMP31_HA_TAXFREE_HJB_POLICY_CALL_BINDING_REPAIR_R2_20261029
STATUS=ISSUED_AWAITING_OWNER_TRANSFER
OWNER_APPROVAL=2026-10-29__FIX_ONE_CONFIRMED_UNBOUND_HJB_POLICY_CALL__BOUNDED_AST_REGRESSION
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=95ba40447bdffdae6ac312acee31ac98b0ddd8bf
TASK_PUBLICATION_COMMIT=EXACT_FULL_40_HEX_TO_BE_PROVIDED_BY_GPT_AFTER_PUBLICATION
EXPECTED_REMOTE_GOVERNANCE_HEAD=TASK_PUBLICATION_COMMIT__STRICT_EQUALITY
TASK_CONTRACT_PATH=tasks/CH5_TEMP31_HA_TAXFREE_HJB_POLICY_CALL_BINDING_REPAIR_R2_20261029/CONTRACT.md
SOURCE_COMMIT=10ee7973713c547faa581388aa97fbfd898809de
SOURCE_ROOT_TREE=301340d8521e645275466602159343527344390a
FIXED_PARENT=10ee7973713c547faa581388aa97fbfd898809de
CANDIDATE_BRANCH=codex/ch5-temp31-hjb-policy-call-target-repair-20261029-r2
PREVIOUS_TASK=CH5_TEMP31_HA_TAU_REMOVAL_NUMERICAL_BOOTSTRAP19_ISOLATED_R1_20261029
PREVIOUS_INDEPENDENT_REVIEW=docs/CH5_TEMP31_HA_BOOTSTRAP19_TAU_REMOVAL_R1_INDEPENDENT_ABC_REVIEW_20261029.md
PREVIOUS_REVIEW_VERDICT=CHANGES_REQUIRED__UNBOUND_HJB_POLICY_CALL_AT_LINE105
NEW_GIT_REPOSITORIES=0
SOURCE_FETCH_BUDGET=0
SCIENCE_BUDGET=0
ACTUAL_HA_HJB_KFE_GE_IRF_CALLS=0
SYNTHETIC_STATIC_TEST_COMMANDS=2_MAX
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 0. 冻结缺陷与唯一修复目的

GPT已从SOURCE_COMMIT固定GitHub原始文件独立复核：
- src/ch5_two_asset_hank/temp31_netwage_hjb.py（Git Blob fdbde69f6fde448300a9e52f5e67636409272ec8）第14行已导入 select_temp31_netwage_local_policy。
- 同文件第105行却调用 select_matlab_faithful_local_policy，该符号未在此新HJB模块中导入、定义、赋值或显式建立别名。
- src/ch5_two_asset_hank/temp31_netwage_policy.py（Git Blob d90eb4ba627d4c702062116c2a4ffadac0f43d86）第57行实际定义的是 select_temp31_netwage_local_policy。
- 上轮16/16 AST/标量测试有界通过，但没有验证**实际调用节点的符号是否绑定到已经导入并定义的新版函数**；因此完整HJB消费链存在确定的潜在 NameError，不得因既有绿色结果忽视。
- R1独立审阅在治理分支commit 95ba40447bdffdae6ac312acee31ac98b0ddd8bf固定裁决：delivery PASS、首轮19及六处税楔代数 PASS_BOUNDED、implementation CHANGES_REQUIRED、真实HA未执行。

**本任务唯一实现改动**：将 temp31_netwage_hjb.py 的第105行实际调用标识符由 select_matlab_faithful_local_policy 替换成已导入/确有定义的 select_temp31_netwage_local_policy。只允许这一处Python语义更改；不改变参数列表、顺序、变量、网格、边界、HJB operator、数值算法、收敛条件或原先去税表达式。禁止借此“修复”其他可能的模型问题。若发现第二个独立缺陷，只记录证据与gap，STOP越界部分，不顺手修改。

## 1. 强制第一步：安全、最新治理和固定候选来源

1. 只复用R3/R4/R5/R1已获安全批准的独立Git库，先只读确认Git对象库、当前refs、干净候选创建区域、历史R3/R4/R5/R1分支与证据安全、无锁或未跟踪文件覆盖风险。禁止第二Git库、旧shallow.lock隔离库、P3受保护科研树、WASM/reparse、D盘历史目录、强制reset/clean/删除/修复旧Git引用。前置不明即STOP。
2. GPT本R2合同发布后通过Owner转交指令提供准确40位 TASK_PUBLICATION_COMMIT。通过当前已授权**普通SSH**进行一次有界远端治理HEAD观察，必须严格等于该发布commit；发布commit的唯一直接parent须严格等于 GOVERNANCE_PARENT=95ba40447bdffdae6ac312acee31ac98b0ddd8bf，其diff**只新增本R2合同**。不能要求远端HEAD等于SOURCE_COMMIT或仅做祖先检测。若有瞬时传输失败，可在同一授权SSH通道一次有界技术重试并如实记录；权限/安全拒绝不得重试、换账号/密钥/协议绕过。治理发布对象未在本地可标LOCAL_OBJECT_ABSENT，不能猜SHA。
3. **Codex先同步核验最新固定候选代码**：R2唯一允许的代码基线=上一R1最终未合并候选 SOURCE_COMMIT=10ee7973713c547faa581388aa97fbfd898809de，root tree=301340d8521e645275466602159343527344390a，并核验原HJB Blob fdbde69f6fde448300a9e52f5e67636409272ec8、新policy Blob d90eb4ba627d4c702062116c2a4ffadac0f43d86、既有R1测试Blob fe3432d2c54ab7cd1b1583a16adfb49621535653 的Git对象和可获取的真实字节SHA-256。不得从治理分支、main或旧R4作为代码父提交，不能静默更新到更晚分支。所有必要源对象应在原隔离库内；本任务**不授权额外SSH fetch、raw下载、全量unshallow或补充仓库**。源对象缺失则STOP。
4. 从FIXED_PARENT创建一条独立R2候选分支，保留历史候选、R1已交付30份文件及所有终审报告原字节。R2合同位于治理发布commit，不存在于候选父提交属于正常状态。

## 2. 极小代码白名单与源码证据

仅允许修改：
- src/ch5_two_asset_hank/temp31_netwage_hjb.py —— **只替换一处调用符号，精确保留其他全部源码字节**。必须用git diff --check、逐行diff、修改前后原字节SHA-256/Git Blob报告证明单一名称变更。

仅允许新增：
- tests/test_temp31_hjb_policy_call_binding_r2.py —— 专用纯静态AST/符号绑定测试，可自带命令行phase选择，不能导入/调用HA求解器。
- tasks/CH5_TEMP31_HA_TAXFREE_HJB_POLICY_CALL_BINDING_REPAIR_R2_20261029/ —— 本R2任务必要报告、真实测试证据、原字节身份、manifest和seal。

禁止修改既有R1测试、旧源、R4/R5新源、正式生产、matlab_faithful_hjb/policy/economics、HouseholdInputs、ORACLE_SHA、数据和任务历史。无需为新验证器增加单独validator文件；推荐用新增tests脚本本身承载定向测试入口。不允许修改__init__.py、包路径或新增别名让旧调用“偶然可以解析”；修复必须直接落在第105行调用目标。

## 3. 测试预算与反例

最多**两次显式无HA静态/合成测试命令调用**，优先一次旧代码预期红灯及一次修改后绿色：
- 第一次：新测试脚本针对尚未修复的R1 HJB旧调用，实际AST解析导入语句、调用节点和policy真实函数定义，预期**返回exit≠0、有定位到未绑定 select_matlab_faithful_local_policy 的明确断言失败**。事前写下测试预期；如果无法证明测试真正会捕获此缺陷，STOP，不伪造红灯。
- 第二次：修复单一调用标识符后，预期通过：(a)实际HJB调用节点指向 select_temp31_netwage_local_policy；(b) import的目标与真实policy def一致；(c)恢复成旧名的错误注入必须使测试失败；(d)函数调用参数、HJB除调用名以外的AST、已净工资表达式及历史源码身份均保持；(e)第105行没有任何残留未绑定旧名。建议覆盖HJB→policy→economics的新依赖符号静态闭包，但不能将静态闭包冒充真实运行时模块依赖/HA结果。
- 两次实际命令的exit、stdout/stderr原始字节、预声明与回执、必要的确切shell命令和Git对象归档；不得以失败检测的内部单元测试代替真正第一轮红灯，也不得以只检查import存在作为通过条件。
- Python AST解析/纯文本比较/标量断言允许；**实际调用初始化/root/policy/HJB/KFE/GE/IRF预算均为0**。不运行真实数值网格、稳态、校准或31省实验；不加载整个suite/生产runner，不安装依赖。若测试自身技术故障与两次预算冲突，STOP不扩大命令次数。
- 不触碰Owner批准的首轮数值工资19、工作地tau_j、六处去税源码的数学形式、真实经济税率或财政机制。任务是修复HJB调用链，不是再次作工资科学裁决。

## 4. 交付、双阶段push及独立审阅

候选只含一个源文件精确改动、新测试文件、本任务必要证据。至少提交：
- result.md（实际终态/COMPLETED/BLOCKED/NOT_COMPLETED/NEXT_ACTION）
- source_identity.json（治理发布及固定源码commit/parent/tree/blob/bytes/SHA256）
- call_binding_before_after.md（完整原符号位置、导入/定义/调用AST关系、单一源码diff证明、已修/未修边界）
- synthetic_test_evidence.md（两次命令、预声明、真实stdout/stderr/exit、反例检测范围）
- gap_register.md（真实HA/网格/收敛/财政/经验来源仍待Owner授权）
- privacy_report.md
- manifest.json（各交付path原字节bytes、SHA-256、Git Blob，manifest自身单独核验）
- DELIVERY_FINAL_RECEIPT.json（payload及seal阶段commit/parent/tree，逐路径远端readback及STOP）
- evidence/（必要测试原始日志及非敏感精准回执）

普通已授权SSH按小批次顺序push：阶段1为源码/测试/evidence/非自引用manifest，远端逐path读回；阶段2为seal最终回执，核验固定候选完整commit/parent/root tree及Blob/bytes/SHA256。代码不产生真正HA数值输出。只报告可见真实远端证据，不暴露私人绝对路径和凭据；遇GitHub/SSH安全拒绝、保护门或证据不符即STOP，不切换协议/凭据绕过、不创建别的仓库。不自动Issue/PR/merge/cleanup/next task。

随后Codex立即STOP。GPT从最终固定候选分A固定身份/来源与交付→B真实diff、AST与反例检测→C artifact/source/numeric/implementation/science/privacy/actual_terminal/delivery/cleanup/not_completed 分层裁决。修复成功至多说明**HJB源码调用目标绑定纠正**，不等于完整HA runtime/linkage、数学政策方程、数值收敛或正式生产接线已经PASS。

## 5. 状态与既有科研约束

ACTIVE_TASK=ISSUED_AWAITING_OWNER_TRANSFER
PREVIOUS_REVIEW_VERDICT=CHANGES_REQUIRED
FIX_REQUIRED_001=HJB_LINE105_UNBOUND_OLD_POLICY_CALL
PREVIOUS_BOOTSTRAP19=OWNER_APPROVED_NUMERICAL_GUESS_ONLY
REAL_WAGE_TAX_TAU_J=RETAINED_OUTSIDE_HA
PROTECTION_BASELINE=BLOCKED
FORMAL_SOURCE_FREEZE=FALSE
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE
FULL_RUNNER_IO_CLOSURE=BLOCKED
AUTO_NEXT=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
