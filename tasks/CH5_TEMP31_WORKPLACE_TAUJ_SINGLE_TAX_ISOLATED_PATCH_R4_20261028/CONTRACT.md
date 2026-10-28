# TEMP31 工作地 tau_j 与单次扣税：复用R3隔离库、按需辅助源码的隔离补丁 R4

TASK_ID=CH5_TEMP31_WORKPLACE_TAUJ_SINGLE_TAX_ISOLATED_PATCH_R4_20261028
STATUS=OWNER_AUTHORIZED_ISSUED_AWAITING_TRANSFER
OWNER_APPROVAL=2026-10-28__REUSE_R3_SAFE_REPO__GPT_AUX_SOURCE_READ_ONLY__ISOLATED_TAUJ_SINGLE_TAX_PATCH
REPOSITORY=zcx369658780/dissertation-ch5-two-asset-hank
GOVERNANCE_BRANCH=migration/astra-workflow-20261012
GOVERNANCE_PARENT=db8ec2d14c09b422bff9d8df493ca69172029222
TASK_PUBLICATION_COMMIT=SUPPLIED_EXACTLY_BY_GPT_IN_OWNER_HANDOFF_AFTER_COMMIT
EXPECTED_REMOTE_GOVERNANCE_HEAD=TASK_PUBLICATION_COMMIT__STRICT_EQUALITY
TASK_CONTRACT_PATH=tasks/CH5_TEMP31_WORKPLACE_TAUJ_SINGLE_TAX_ISOLATED_PATCH_R4_20261028/CONTRACT.md
CANDIDATE_BRANCH=codex/ch5-temp31-worksite-tauj-single-tax-isolated-20261028-r4
FIXED_PARENT=5e4ec0ae4c310b8071b6aef68642fd0ffd862478
SOURCE_COMMIT=5e4ec0ae4c310b8071b6aef68642fd0ffd862478
SOURCE_ROOT_TREE=R3_EXECUTOR_REPORTED_e636e09a2542deb29f386a26f5456e2b517f7911__MUST_LOCAL_REVALIDATE
R3_BASE_BRANCH=codex/ch5-temp31-worksite-tauj-single-tax-isolated-20261028-r3
NEW_GIT_REPOS_ALLOWED=0
OLD_ISOLATED_REPO_LOCK_ACTIONS=0
SUPPLEMENTAL_SOURCE_GIT_FETCH_ALLOWED=0
TEST_BUDGET=2_BOUNDED_NO_HA_SYNTHETIC_INVOCATIONS
SCIENCE_BUDGET=0
HA_HJB_KFE_GE_IRF=0
MODEL_CALLS=0
STEADY_STATE_IRF_CALIBRATION=0
FORMAL_SOURCE_WRITES=0
PRODUCTION_WIRING=0
V010_CHANGES=0
V011_ACTIVATION=0
AUTO_ISSUE=FALSE
AUTO_PR=FALSE
AUTO_MERGE=FALSE
AUTO_CLEANUP=FALSE
AUTO_NEXT=FALSE

## 0. 单张任务的经济学目标与历史状态

Owner正式批准：来源省i家户在发放工资的目的地省j工作，适用**目的地工资税 tau_j**；同一笔劳动收入**只扣税一次**。本任务沿用R2/R3批准的隔离实现和两次无HA合成测试预算；不改变税归属、财政税基、劳动单位或正式生产算法，不运行真实模型。

R3 Codex回执：新独立仓库已建立、固定十份源码Git Blob/原始bytes/SHA256均本地认证、R3工作分支指向SOURCE_COMMIT=5e4ec0ae4c310b8071b6aef68642fd0ffd862478，root tree据回执为e636e09a2542deb29f386a26f5456e2b517f7911；无patch、无测试、无远端候选。额外辅助源码mp4b_python_empirical.py经普通SSH获取报bad revision / did not send all necessary objects，按合同STOP。**R3证据目前仅Codex报告及未上传的本地原始文件，GPT未独立复算十份原字节。** R3旧预算已关闭；R4为新一次Owner授权，不自动恢复R3任务或续用R3预算。

GPT现已从SOURCE_COMMIT经GitHub固定文件连接器只读确认五份辅助源码及下列Git Blob（这不等于Codex本地有其Git对象，不能当作本地源码认证）：
- validators/multi_province/mp4b_python_empirical.py: b1710ae3c5d8d7baf96e85c932d777fa5f3b908c；重点行171–183初始化、337–350 HA调用
- src/ch5_two_asset_hank/contracts.py: c746b616bec38531a7d96da81a54e2899d8aba53；HouseholdInputs行79–104
- src/ch5_two_asset_hank/matlab_faithful_hjb.py: e06f9871b361c8e1c8df7aab5c43c2dbd3b09b50；HJB边界行89–103
- src/ch5_two_asset_hank/matlab_faithful_policy.py: 2021db630f3057026ffc37d375a43aaddbccec48；effective net wage行119–155
- validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py: 0033baee136c0328e80ffb8b794a88d4405c976c；适配器行15–40

若这些辅助模块在本地对象库缺失，**不得**把GitHub可读冒充本地存在，也**不得**自动fetch/checkout/copy GitHub对象、下载raw、扩大仓库或换协议。仅可利用本合同已经列出的可核对的静态接口事实，实施**独立纯函数/纯数组隔离接口**；任何运行/导入必需缺失模块的步骤，按受影响范围STOP并登记；若导致所有获准实现不可进行，则完整STOP。不得凭缺失源码臆造算法细节。

## 1. 强制第一步：复用、核验并对齐最新固定源码（不重新建立仓库）

1. **先作非跟随只读工作区安全预检**：仅识别R3创建的那个已授权安全隔离库，核对实际Git dir、refs、object store、HEAD、固定commit、root tree、候选分支及R3原有STOP证据的存在性和保护边界。禁止访问旧R2有shallow.lock的隔离库、P3科研工作树、WASM/reparse目标及D盘历史版本；不清理/更改它们。若无法确认所选库就是R3安全库或存在锁/可疑链接/私人保护差异，STOP。NEW_GIT_REPOS_ALLOWED=0，禁止第二个库、shared/reference clone、alternates、worktree穿越或复制.git。
2. **先校验最新任务与远端身份**：由GPT在Owner转交指令给出发布后的完整40位TASK_PUBLICATION_COMMIT；用现有获准SSH read-only查询远端治理HEAD，必须严格等于该R4发布SHA。任务发布提交必须具有唯一直接parent=db8ec2d14c09b422bff9d8df493ca69172029222，对该parent的diff**仅新增本R4合同**。不可把SOURCE_COMMIT当治理HEAD，不可用祖先关系替代严格相等。若发布commit的Git对象在本地缺失，可用已获授权的只读SSH远端观察及GPT固定提交审阅作为独立远端证据，明示LOCAL_COMMIT_OBJECT=ABSENT；不得因此强制在本地获取发布commit对象，也不能据此推断完整本地Git对象。
3. **与最新冻结科研代码对齐**：R4的SOURCE_COMMIT和FIXED_PARENT均为5e4ec0ae4c310b8071b6aef68642fd0ffd862478（R3已经验证过的固定源码），不是R4任务发布commit或最新main。以R3保留的source_identity原始回执和当前**实际可读**的源文件进行只读核对；确认SOURCE_COMMIT的Git身份、root tree（R3报告值e636e09a2542deb29f386a26f5456e2b517f7911需本地重新确认）、十份固定源Blob和已有bytes/SHA256证据均与原冻结一致。可复用R3经过校验的原始认证记录，不需重复无意义的批量重算、无界fetch或模型实验。若实际代码未齐备、Git对象缺失或R3原始证据不能认证，STOP对应修改，不得以Codex摘要代替所需原字节。**Codex必须先核对最新远端治理提交与最新已冻结源码一致性，之后方可修改；不得对受保护正式树执行git pull/reset。**
4. 仅在安全和身份门通过后，从FIXED_PARENT本地创建一个**新的R4候选分支**，保留R3分支和已保存STOP证据，确保不会覆盖未跟踪文件或历史目录。候选父为5e4ec0ae4c310b8071b6aef68642fd0ffd862478，即使它不包含R4合同也是正常状态；记录new branch创建前后状态。若分支冲突或未跟踪文件覆盖风险，STOP，不clean/reset/rm。仅在R4候选安全工作区写入允许的修改。**R3已经报告的本地身份结果只可标EXECUTOR_REPORTED_RECHECKED，不提升为GPT_INDEPENDENT_PASS。**

### R3已核验十份源路径及预期Git Blob（不可改写历史）
1. src/ch5_two_asset_hank/multi_province/wage.py — 48001b2e4ca64d81dda6174255f6ccf130e07004
2. src/ch5_two_asset_hank/multi_province/migration_labor.py — e6fd216aeda40b9b477c0f0e16332e6366b66900
3. src/ch5_two_asset_hank/multi_province/one_turn.py — 621c8e2dfaf5f55eda39c9b9bffb22cd52ee451f
4. src/ch5_two_asset_hank/multi_province/firm.py — 1f7d37247e2d712fc0477a9f562dce81d1b367ce
5. src/ch5_two_asset_hank/multi_province/fiscal_diagnostics.py — c24bbda9ea88c1581eeed6d734062b30d13def2f
6. src/ch5_two_asset_hank/multi_province/stationary_runtime.py — 8717cfa759948bd1ad3c8cd788f8f4736f250598
7. src/ch5_two_asset_hank/multi_province/steady_state.py — 5c5b56e6a2eb82fab4e80eb7b8e5bbbf97f08c22
8. validators/multi_province/mp4c_python_annual_empirical.py — d2e74cb8b491489053dcde525cd4d83cb4bd0b3a
9. validators/multi_province/mp4c_python_annual_production.py — 7473e04418744d745000afb21d84588273cc5bca
10. validators/multi_province/mp4c_run_full_annual_batch.py — 599202c39a358b78c4115dcb1e5886021f388389

## 2. 隔离代码补丁：必须经济学可证伪、可保留历史基线

A. **目的地征税与双边劳动**：为TEMP31新增具名纯函数/隔离wrapper，双边矩阵行=destination j、列=origin i。工作地税率始终取tax_by_destination[j]，即wjt[j]*(1-tau_j-sigma[j,i])/phi[j,i]。覆盖历史source-like双边数量重构与origin-preserving-normalized候选的公式语义，原消费幂次、工资幂次、人口乘子只出现一次、按origin列归一化及destination行求和保持算法不变；清楚区分normalized路线并未接生产。不得直接修改既有reconstruct_migration_labor、reconstruct_origin_preserving_normalized_migration_labor或其公共业务语义以致旧MATLAB-faithful行为变化。若无需触及旧文件，尽量用temp31_worksite_tax.py新增函数与测试。

B. **已净综合工资→HA**：当前wage.py综合工资已经内含目的地tau_j及sigma_ji；现行HA初始化和HJB对state['w']再应用(1-tau_i)，源码存在双重税楔路径。R4仅新增独立纯数据适配合同：输入明确标记NET_COMPOSITE_AFTER_DESTINATION_TAU_AND_MIGRATION_WEDGE，输出可审的净工资及等价单一类别HA输入语义（如tau_for_HA=0、sigma_for_HA=0），使初始化与HouseholdInputs使用同一个净工资合同。需有非对称人工测试证明有效工资=原净综合工资，不再次乘(1-tau_i)或扣sigma。**禁止实际调用或编辑HJB、KFE、历史HA初始化、shared HouseholdInputs、matlab_faithful_policy、正式annual production入口**；若调用缺失模块是实际运行必需，STOP受影响测试。首轮state['w']可能是默认初始化值，不得声称其已被证明是NET_COMPOSITE。

C. **财政仅条件诊断**：只比较当前firm.py Govinc中Lt*tau与条件性tau_j*wjt_j*L_j，记录Lt_mat是否已含N_i、z_i，有效劳动与人口/就业口径、工资clip与税基、sigma作为私人迁移楔子不计税收入、按目的地财政归集的未决问题。**不得修改firm.py、fiscal_diagnostics.py或正式财政算法**。

D. **白名单写入**：仅允许：
- src/ch5_two_asset_hank/multi_province/temp31_worksite_tax.py（新建：纯函数隔离实现、明确数据语义）
- src/ch5_two_asset_hank/multi_province/migration_labor.py（确有必要时只加具名TEMP31独立wrapper，不改历史函数）
- src/ch5_two_asset_hank/multi_province/one_turn.py（确有必要时仅加未接线TEMP31具名接口，旧入口保持）
- validators/multi_province/temp31_worksite_tax_isolated.py（新建：纯合成验证，不调用生产）
- tests/test_temp31_worksite_tax_isolated.py（新建：纯合成定向测试）
- tasks/CH5_TEMP31_WORKPLACE_TAUJ_SINGLE_TAX_ISOLATED_PATCH_R4_20261028/（本任务报告、清单与精简证据）
不写入其余任何代码、.git之外的旧证据、现有历史任务、R3停止报告、科学原件、正式V010/生产worker或D盘。必要的候选.git元数据只允许在已认证R3**新隔离库**里发生。不扩大到真实数学模型修改。

## 3. 合成测试与停止预算

仅允许最多2次定向、显式、无HA/HJB/KFE的测试**命令调用**。两省非对称tau_0!=tau_1、wjt_0!=wjt_1及非对称sigma，核验用目的地tau_j而非原籍tau_i，至少一个错误旧路径会产生可观测不同结果；测试自身/跨省、交换省次序、destination-row/origin-column、phi>0、税后幂底>=0、tau=0/sigma=0边界。source-like路径需核对destination行和，normalized路径需核对每origin列归一化且N_i及家户劳动质量只乘一次。另一组验证NET_COMPOSITE进入HA纯适配数据后不再被应用(1-tau_i)或sigma，错误注入非零二次tau必须检测失败；但**不得真正调用HA/HJB/KFE或把纯数据测试PASS写成正式科学PASS**。

若因缺失辅助源码、依赖或不完整浅仓库而无法运行某些测试，允许收口静态纯函数补丁和剩余gap（前提是前置安全、源码身份与涉及代码字节均已核验）；不得下载raw/获取Git对象、pip install、打开科学保护树或改测试含义绕过。测试未跑须明确NOT_EXECUTED；不能为通过次数而换成与验收问题无关的检查。测试任一实质失败需修复白名单内隔离缺陷并在剩余额度内定向复检；超预算则STOP留证。科学预算和真实模型调用永远为0。

TEST_BUDGET=2_BOUNDED_NO_HA_SYNTHETIC_INVOCATIONS
TEST_INVOCATION_FAILURE_RETRY_MAX=1_ONLY_TOOL_TRANSIENT_WITHIN_2_TOTAL
GIT_REMOTE_HEAD_READ_MAX=1_BOUNDED
SUPPLEMENTAL_SOURCE_GIT_FETCH_ALLOWED=0
NEW_GIT_REPOS_ALLOWED=0
HA_HJB_KFE_GE_IRF=0
REAL_GE=FALSE
Results=FALSE

## 4. 证据、分批次交付与独立验收

交付R4候选分支只提交**本任务相关最小文件**。报告至少包括：
- result.md（实际终态、完成/阻塞/未完成、下一行动）
- source_identity.json（R4发布commit与治理父、R3固定源commit与tree、十份源路径Blob与复用的R3实际bytes/SHA记录、缺失辅助对象逐项状态、隔离库审查）
- auxiliary_static_review.md（GPT固定Git Blob与准确行号、Codex本地对象有/无、静态事实与未知分开）
- code_diff_and_callpath.md（旧版语义未变、隔离实现事实、行号、未接生产证明）
- synthetic_test_evidence.md（最多两次测试命令、预期和实际、错误注入、未运行项）
- tax_contract_and_fiscal_gaps.md（tau_j及单次扣税批准、税基/单位/首轮工资待决）
- gap_register.md、privacy_report.md
- manifest.json（每载荷path、bytes、SHA-256、Git Blob、provenance、purpose；不制造循环自哈希）
- DELIVERY_FINAL_RECEIPT.json（固定候选commit、parent、root tree、精确远端读回状态、预算/STOP）
任何本地私人绝对路径、锁敏感信息、原始工资微观数据或凭据不得上传；必要脱敏应保留来源及转换记录。

普通授权SSH，小提交**顺序分批推送**：第一阶段最小代码/证据/非自引用manifest，逐文件远端readback；第二阶段seal及回执。不得推送全部历史库、创建第二仓库、借GitHub对象API/HTTP/新SSH Key绕过传输异常，或把远端已有候选误判为新成功。网络卡顿可记录阶段诊断，只有合同允许的原路径瞬时故障1次受界技术重试；权限/安全拒绝立即STOP。失败可保留未推送本地隔离patch及报告，但不宣称DELIVERY_PASS。

GPT之后按独立A（固定commit/parent/tree/path/Blob/bytes/SHA）→B（diff、数学、数值测试、历史行为、科学缺口）→C（artifact_integrity/source_identity/numeric_review/implementation_review/scientific_review/privacy_review/actual_terminal/delivery/cleanup/not_completed）三阶段审阅。无远端候选则远端审阅NOT_STARTED，不从Codex回执推测PASS。Codex完成交付即STOP；不自动Issue、PR、merge、cleanup或下一任务。

## 5. 不可更改的保护与当前状态

PREVIOUS_TASK=CH5_TEMP31_WORKPLACE_TAUJ_SINGLE_TAX_ISOLATED_PATCH_R3_20261028
PREVIOUS_TERMINAL=STOP__ADDITIONAL_ALLOWED_SOURCE_OBJECT_FETCH_FAILED__PINNED_TEN_SOURCE_IDENTITIES_VERIFIED__NO_PATCH_NO_TEST_NO_PUSH__STOPPED
ACTIVE_TASK=ISSUED_AWAITING_OWNER_TRANSFER
PROTECTION_BASELINE=BLOCKED
TRUSTED_NEW_STATUS_BASELINE=NOT_APPROVED
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
