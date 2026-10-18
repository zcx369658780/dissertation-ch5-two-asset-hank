# 第五章工作流 V1.6：保护路径边界与PATH_ALIAS分类

日期：2026-10-18。V1.6在V1.4资源门禁真实性与V1.5不可变任务身份规则之上，仅修订BOOTSTRAP 0的保护路径识别、别名解析与停止分类。其余V1.4/V1.5规则继续有效。

## 1. 最新失败事实

任务 TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V2_20261018 在BOOTSTRAP 0停止，run_id=1b1c3687d35c42b0a06ab581d4a39697。Codex报告保护枚举在路径 `D:\ProjectTemp\c5k1bturn56\EVIDENCE\ch5_revised_data_table_20260930\node_modules\pnpm\dist\node_modules\node-gyp\gyp\gyp_main.py` 触发 PATH_ALIAS，但检查器未返回实际最终路径。别名性质、最终路径及其是否触及受保护根均为UNKNOWN。没有创建scratch、文件、runner或测试；不据此推断模型源码损坏。

终态：FAIL_CLOSED_PROTECTED_PATH_IDENTITY / STOP。STOP本身正确；问题是保护路径枚举的范围和诊断粒度不足。

## 2. 保护路径核验必须以边界为中心

1. 先定义并核验有限的保护根清单：正式模型worktree根、外部Git common-dir、index文件、历史运行根、文档镜像根、备份根及本任务指定的独立scratch父目录。对每个根记录规范化路径、卷/设备标识、文件ID（可得时）、reparse/link属性和根身份SHA/元数据。
2. 禁止为验证根身份而递归枚举保护根内全部文件、包管理依赖、node_modules、pnpm store或其他无关后代。保护根的存在与身份检查，不等于必须对根下每个依赖文件做完整最终路径解析。
3. 只对本任务将要写入的具体目标路径、其父目录链，以及可能影响写入定向的reparse point/junction/symlink做逐段解析。对受保护根本身及其父链执行边界检查；不要把无关依赖文件当成候选写入目标。
4. `PATH_ALIAS`不是自动的安全违规结论。它是需诊断的解析状态。必须返回：原始输入路径、解析到失败的路径组件、可获得的规范化/最终路径、reparse tag/类型、目标路径是否在保护根内/外/无法判断、检查API与原始错误。若系统API无法提供最终路径，明确 `ALIAS_TARGET_UNKNOWN`，不可猜测。
5. 如果实际目标是任务明确禁止的保护根、跨卷或未授权位置，立即STOP。若PATH_ALIAS仅发生在只读枚举到的无关依赖文件，且本任务不访问、不写入该文件，则不得仅凭此项拒绝整个scratch；记录并排除该无关条目，继续验证真正的保护根与目标路径。若无法证明其无关，则STOP。
6. 不得以关闭链接检查、忽略reparse point、使用字符串前缀判断或简单换目录来规避保护。路径包含关系必须基于规范化路径边界/文件身份，不可用不安全的文本前缀。

## 3. BOOTSTRAP 0/1/2顺序

BOOTSTRAP 0只读核验：固定任务身份、治理状态、有限保护根清单、scratch父目录、具体目标路径与别名诊断能力。此阶段不创建文件。
BOOTSTRAP 1只在0通过后创建独占scratch目录，并通过目录句柄/文件ID及父子关系重新验证目标没有被重定向。
BOOTSTRAP 2只在1通过后写入首个工件。写入前仍需确认目标目录身份与保护根无交叉。

若任何必需保护根无法识别、实际目标是否位于保护区无法判断、路径被重定向到保护根或写前身份不一致，立即只读STOP。不要换路径重试。

## 4. 诊断失败分类

- TASK_RAW_IDENTITY：固定合同/发行元数据不一致；原文只读STOP。
- GOVERNANCE_STATE：CURRENT/TASK_CURRENT授权冲突；只读STOP。
- PROTECTED_ROOT_IDENTITY：正式worktree/index/common-dir/备份等必需保护根身份未知。
- PATH_ALIAS_TARGET_UNKNOWN：目标/父链存在别名，但最终目标及保护边界无法判断。
- PATH_ALIAS_UNRELATED_ENUMERATION：只读递归发现的无关依赖文件存在别名，不是本任务目标；记录排除理由，不自动升级为保护根故障。
- PROTECTED_TARGET_REDIRECTION：本任务具体写入目标被重定向到保护区或未授权位置；STOP。
- RESOURCE_GATE：运行期资源事实与约束不一致；E2 STOP。

每次报告必须列出原始路径、作用对象（保护根/目标父链/无关递归条目）、解析API、解析结果、保护边界判定和未运行步骤。不得把所有PATH_ALIAS一律归为同一错误。

## 5. 不可变合同与预算

V1.5关于固定合同原样读取、Git Blob与SHA256分离、启动Prompt不得重构合同、身份失败不得改文档重试的规则完全保留。路径诊断只读阶段不得写日志或创建工件；失败原始输出可保留在执行器工具回执中。

本政策不授权运行测试、runner或科学模型。先前adapter V2任务因保护路径诊断失败，保持FAIL_CLOSED_PROTECTED_PATH_IDENTITY，不续跑。正式V010不变；V011 NOT_STARTED；model_activation=False；REAL_GE=False；Results=FALSE；FULL_RUNNER_IO_CLOSURE=BLOCKED。
