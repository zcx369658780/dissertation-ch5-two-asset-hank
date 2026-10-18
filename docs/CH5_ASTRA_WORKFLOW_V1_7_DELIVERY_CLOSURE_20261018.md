# 第五章工作流 V1.7：交付预算闭环与已完成证据补交

日期：2026-10-18。V1.7只修订任务签发、工程停止后的独立交付和远端证据交换；V1.4资源真实性、V1.5不可变任务身份、V1.6保护路径边界以及科学/模型禁令继续有效。

## 1. 本轮缺口与裁决

TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_20261018 的本地工程结果为 `PASS_BOUNDED_ADAPTER_INTEGRATION_LOCAL`，但其固定合同明确禁止Git fetch/push、网络发布和review清理。因此没有发布远端临时材料并非该合同下的违规；真正的流程缺陷是签发任务时未同时满足长期“MD＋manifest＋脱敏ZIP远端交换”要求，也未预留独立交付预算。不得追溯修改原合同、重开原任务预算或伪造远端验收状态。

## 2. 新任务的双预算与明确发布条款

每张需Astra独立验收的任务，在签发时必须把下列预算分开固定：
- `SCIENCE_BUDGET`：HA/HJB/KFE/selector/root/GE/IRF等科学调用。
- `ENGINEERING_BUDGET`：本任务允许的实现、测试、进程、时间与批次。
- `DELIVERY_BUDGET`：脱敏、manifest生成、发布器预检、GitHub发布、远端原字节回读、永久归档和临时清理。
任一预算关闭不得自动打开另一预算。科学/工程任务STOP后，只有当合同预先允许且有独立DELIVERY预算时，才可执行已完成证据的交付；若原合同禁止网络发布，必须签发全新、零科学、限域delivery-only合同。不得把delivery-only变相用于续跑测试、模型或runner。

每张新任务必须明确填写：
`DELIVERY=GITHUB_TEMP_REVIEW_MD_ZIP_FIRST`（适用时）
`TEMP_PATH=_review_tmp/ch5/<task-id>/`
`REVIEW_BRANCH`、`FIXED_PARENT`、文件白名单、各文件上限、最大发布次数、SSH/网络预算、清理预算和失败STOP。
需交付ZIP时，白名单默认 `result.md`、`manifest.json`、`evidence_sanitized.zip`。在任务签发前核对该任务已有的限制；禁止发布与合同冲突时，不得仅靠本长期规则覆盖固定合同。

## 3. 交付验证与修复规则

- 在真实发布前，必须使用任务外独占、非共享、无checkout的fake bare remote做发布器端到端预检；精确核验argv token、blob/tree/commit、普通推送、远端读取二进制字节和清理tree。该预检不能接触受保护worktree/index，也不算真实GitHub发布。
- 预先固定普通E1恢复预算。参数token、路径引用、脚本语法等本地可确定性错误可在预算内修复；必须保留首次失败，不得把E1伪装成从未发生。认证/权限失败、固定父对象不匹配、敏感内容无法脱敏、保护路径不确定、越白名单或预算超限为STOP；不强推、不扩大范围。
- ZIP发布前逐成员核验并检查嵌套归档、路径穿越、重复大小写路径、链接、压缩炸弹、凭据、绝对本机路径及非授权真实数据。保留RAW原件本地及原始SHA/长度；manifest分别登记RAW与SANITIZED派生件，绝不以派生哈希冒充RAW哈希。不可解析或无法确认脱敏时，不发布ZIP。
- Astra必须从固定远端ref/commit/tree读取result、manifest及ZIP真实字节；对ZIP重算SHA256/长度并逐成员比对。若二进制字节不可读，标记 `BINARY_NOT_INDEPENDENTLY_READABLE`，不能宣称ZIP独立验收通过。
- 顺序不可变：先永久归档独立验收结论及必要哈希，并回读治理分支；然后仅对指定临时分支当前tree中的白名单文件执行普通非强制清理commit，再回读确认。清理失败标记 `TEMP_CLEANUP_PENDING`，不得扩大删除范围。Git删除不抹除历史commit。
- `_review_tmp/ch5/<task-id>/`只能存在于远端review tree，绝不在本地科研/模型/治理worktree或index中创建。Codex使用既有SSH Key/443，不新增PAT、不修改global/system Git配置、不记录凭据。

## 4. 当前适用范围

本V1.7是前瞻性流程规则，不追溯打开任何已关闭任务的网络预算。当前唯一后续delivery-only任务为 `TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_V3_GITHUB_DELIVERY_20261018`；其范围只允许交付既有本地证据，不得重跑静态/合成/Windows测试，不得运行模型或runner。原V3工程结果、历史V2失败与所有原始收据保持不变。

正式科学状态保持：V010不变；V011 NOT_STARTED；model_activation=False；REAL_GE=False；Results=FALSE；FULL_RUNNER_IO_CLOSURE=BLOCKED。
