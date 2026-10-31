# Python 科研主线与会话治理规则（Owner批准，2026-10-31）

STATUS=OWNER_APPROVED_CURRENT
EFFECTIVE=2026-10-31
RESEARCH_MAINLINE=PYTHON_MULTI_PROVINCE_HANK
MATLAB_ROLE=HISTORICAL_REFERENCE_ONLY
MATLAB_EXECUTION_PREREQUISITE=FALSE
AUTO_NEXT=FALSE
MODEL_AUTHORIZATION=PER_TASK_OWNER_APPROVAL_REQUIRED

## 1. 科研主线裁决

博士论文第五章多省份 HANK 的后续主动开发、数值诊断和科学验证，以 Python 实现为唯一主线。MATLAB 原版程序仅作为历史来源、数学结构/原始实现参照及历史证据；MATLAB 可执行文件身份、安装、启动、运行和 MATLAB–Python 全量 parity 不构成 Python 科研工作的前置条件。

不得因 Python 出现数值问题而自动转回 MATLAB 可执行环境验证。只有 Owner 针对一个明确、不可由 Python 证据回答的数学/历史实现争议另行批准时，才可开展有界 MATLAB 只读或执行任务。

## 2. 原版错误与 Python successor

MATLAB 原版是历史来源，不是无条件正确的科学 oracle。Python 复现过程中已经识别并修正的原版错误不得为追求逐字/逐算子 parity 而重新引入。

必须区分：
- historical/source-faithful reference：记录原版实际公式和程序行为；
- corrected Python successor：记录经明确科学推导、Owner决策或已接受任务批准的修正；
- numerical evidence：证明特定输入、网格、参数和预算下的数值行为；
- formal Results：须经过单独的科学验收，不由程序运行、收敛或工程 PASS 自动推出。

不得把未记录的修正推断为已批准；数学机制、经济口径、参数、网格、边界、求解器、容差和校准的实质变化仍须明确 Owner 决策及任务合同。

## 3. 当前 Python 数值工作方式

后续优先从 Python 最近一次真实数值实验及其原始 result、输入快照、源码身份、日志和诊断文件恢复。助手的会话总结、表格转述或聊天文字不能替代原始实验报告。

对每个实验分别记录：
- HJB 是否收敛及残差/策略/边界诊断；
- KFE 是否仅成功执行，还是通过原始生成矩阵的严格驻定、质量、非负性、闭类和质量守恒检查；
- 资产边界质量、上/下界流量及分布敏感性；
- 价格点、参数、网格、输入身份、算法版本与预算；
- 失败、未认证和 UNKNOWN 项。

不能将“求解器返回”“分布归一化”“价格点可运行”升级为经济稳态或严格驻定。未取得原始报告时，数值结论标记为SECONDARY_SUMMARY_ONLY / NOT_INDEPENDENTLY_VERIFIED。

## 4. MATLAB 历史任务处理

R8–R12 及其 STOP/PENDING、合同、原始证据、隐私门和独立审阅报告全部保留为不可覆盖的历史审计记录。R12 正式终态仍为：
STOP__R12_SOURCE_PRIVACY_OR_DELIVERY_BLOCKED

R13 离线恢复建议截至本规则生效时未获授权。不得自动读取 LOCAL_ONLY 矩阵/源码、修复或重跑比较器、放宽隐私断言、重启 MATLAB 或签发 R13。历史 STOP 不因路线调整而解除。

不删除 GitHub 历史 MATLAB 源码、实验、任务证据或论文原件；它们可能是来源与可追溯性证据。项目 Sources 可以不再附带重复的大型 MATLAB ZIP、博士论文 PDF/TeX ZIP，因为 Codex 本地工作区保有原件；移出 Project Sources 不等于删除 GitHub 或本地原件。

## 5. 会话与项目记忆治理

每个新会话采用增量恢复，不复述完整项目历史。启动顺序：
1. 读取精简 Project Source 的入口/当前状态；
2. 读取本任务明确引用的 GitHub 固定任务、commit、原始结果；
3. 只读取解决当前问题所需的数学推导、源码和历史决策；
4. 不扫描全部 docs、tasks、experiments 或历史会话。

每个专题会话聚焦一个可判定的科研问题。交接只包含：当前问题、固定代码/任务/结果身份、已证实结论、未知/阻塞、Owner权限、下一允许动作。避免重复粘贴博士论文、完整路线图和历史审计摘要。

Project Source 只保留少量入口规则与状态摘要；原始科研证据和完整审计仍在 GitHub 仓库按固定 commit 管理。助手不得把会话总结当作新的科研事实。

## 6. 当前状态与权限

本规则只改变研究优先级和知识/会话组织方式，不授权任何模型运行或正式源修改。

在 Owner 另行批准具体任务前，保持：
FORMAL_SOURCE_FREEZE=FALSE
V010=UNCHANGED
V011=NOT_STARTED
Results=FALSE
model_activation=FALSE
REAL_GE=FALSE
FULL_RUNNER_IO_CLOSURE=BLOCKED
STRICT_KFE_STATIONARITY=FALSE
AUTO_NEXT=FALSE

当前无活动执行任务。下一步应先恢复并核验 Python 最近数值实验的原始证据，再由 Owner 与顾问讨论数值诊断优先级；本规则本身不签发下一任务。

## 7. 与其他治理文件的关系

本规则是 2026-10-31 Owner 对科研主线与会话组织的最新专项裁决。GitHub 固定提交、人工逐任务、独立审阅、隐私、来源和交付流程继续遵循仓库中最新 Owner 批准的治理权威；如历史文件出现 MATLAB 优先或 MATLAB parity 前置措辞，以本规则对科研路线的专项裁决为准。科研权限仍以每项任务的明确授权为准。
