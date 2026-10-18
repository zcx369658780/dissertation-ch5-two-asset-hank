# 第五章工作流 V1.9：URI、文件路径与转义文本分类器

日期：2026-10-18。V1.9只修订交付审查器的路径/URI/转义文本分类与测试顺序。V1.4资源真实性、V1.5不可变身份、V1.6保护路径边界、V1.7交付闭环和V1.8来源身份溯源继续有效。

## 1. 最新失败记录

Delivery V2 run_id=447f9775e1b5482f9e3add9344742017在发布前停止。审查器将URI `https://` 中的 `s:/` 误判为Windows盘符；唯一E1修复后，仍将JSON转义路径片段误判/未能分类。仅扫描17/491成员（16分类、1未决、474未审），ZIP完整安全结论UNKNOWN。fake-bare、SSH、fetch、push、远端回读均NOT_RUN。没有发布候选。不能由审查器误报推断源证据泄密或修改。

旧Delivery V2保持FAIL_CLOSED / STOP，不续跑、不修改、不复用已关闭预算。新任务仅修复分类器并使用合成语料，不读取/扫描旧ZIP，不生成新ZIP，不联网发布。

## 2. 类型先行，不使用裸正则作最终裁决

分类器必须区分语法上下文，至少输出以下类型：
- URI（有效scheme与URI语法）
- WINDOWS_DRIVE_PATH（例如 C:\\folder 或 C:/folder；必须在路径语境识别，不因任意文本出现 `s:/` 即认定）
- UNC_PATH（\\\\server\\share）
- JSON_ESCAPED_FRAGMENT（仅表示序列化文本中的转义片段；不能直接当成实际文件路径）
- CREDENTIAL_CANDIDATE（只标候选，不等于已泄露）
- ORDINARY_TEXT
- UNKNOWN

同一文本可有多段span分类，但不得把单个局部子串直接升级为整条记录的路径类别。必须保留原始字节/原始字符串offset与上下文。分类结果与安全结论分离：CREDENTIAL_CANDIDATE需要后续上下文/规则复核；UNKNOWN或不可解析格式阻止发布，但不能被报告为已证实泄露。

## 3. 解析规则

1. 先按容器格式解析（例如合法JSON必须由JSON parser解析），同时保留原始字节、解析后字符串与来源offset映射；禁止先做全局反斜杠替换。
2. URI判断使用明确的scheme/authority/path结构。URI的scheme冒号及后续斜杠不能因字符串模式 `letter + :/` 被判为盘符。URL内路径片段仍可按URI组件语境进一步分类，但不能把整条URL误判为本机文件路径。
3. Windows路径识别必须要求路径上下文与结构约束，例如盘符冒号后紧随斜杠/反斜杠，且该片段不是URI scheme位置。UNC必须满足双反斜杠和server/share结构。
4. JSON_ESCAPED_FRAGMENT只有在JSON token/字符串语境下成立。转义表示不自动等于实际路径，也不自动等于秘密。合法JSON解析失败时，保留原始内容并标记UNKNOWN/FORMAT_PARSE_ERROR，不用启发式反转义后继续发布。
5. 对文本中嵌入的绝对路径、用户名、内网地址和凭据仍需检查；V1.9不放宽脱敏要求。只允许将误报归类到正确类型，不允许忽略真实敏感数据。
6. 不执行任何被检查文件/归档内的代码或命令。路径解析不触碰真实文件系统，除非任务明确授权并且目标路径已通过保护门禁。
7. 分类器输出：原始样本ID、span起止、上下文类型、分类、置信/规则ID、是否需复核、decision、原因。未知或格式错误一律不发布。

## 4. 强制合成回归语料

至少包括：
- `https://example.test/a/b`与`ssh://host/path`不得误判为Windows盘符；
- `C:\\Users\\demo\\file.txt`、`D:/data/file.txt`识别为Windows路径；
- `\\\\server\\share\\file`识别为UNC；
- JSON字符串中双反斜杠转义片段，须区分原始JSON文本与解析后的字符串；
- 含URI、路径、JSON转义混合文本；
- 普通文本中的 `s:/` 不可仅凭局部模式判为盘符；
- 真实绝对路径、credential候选、格式错误JSON、嵌套归档元数据与UNKNOWN；
- Unicode、大小写、重复路径及路径穿越候选的分类；
- 对所有样本验证原始输入未被修改，offset映射稳定。

必须报告样本数、每类TP/FP/FN或适用的分类混淆表、负例、UNKNOWN数和失败用例。不得只报告“全部通过”而不列样本与断言。

## 5. 本任务权限与预算

TASK_ID=CH5_REVIEW_PATH_CLASSIFIER_V19_SYNTHETIC_ONLY_20261018
SCOPE=ENGINEERING_ONLY / SYNTHETIC_ONLY / NO_ARCHIVE_SCAN / NO_NETWORK / NO_RUNNER / NO_SCIENCE

只在既有已授权独立scratch规则通过后工作；如果保护身份不能核验，原样只读STOP。仅修改新scratch中的分类器和合成测试，不改旧源、原ZIP、manifest、回执或正式模型树。不得读取或扫描本轮旧ZIP的其余474个成员，不得执行ZIP安全审查，不得fake-bare，不得SSH/fetch/push，不得生成或发布review候选。

资源上限：工程后代≤96；Python启动≤24；同时活动Python≤4；跨进程活动线程≤32；主动工程时间≤90分钟；最多4批；新增非Git字节≤128MiB。每项限制创建前执行。科学调用0、测试仅合成语料、runner调用0、网络调用0。

E1语法/断言错误可在4批预算内修复，保留首次错误并重新运行合成测试；E2保护身份、资源账本、意外网络、真实数据/凭据暴露立即STOP。不得在本任务内扫描真实ZIP来“证明修复有效”。

## 6. 验收与终态

PASS只表示合成分类器在冻结测试语料中正确区分URI、Windows路径、UNC、JSON转义和敏感候选。它不表示原ZIP已通过安全审查，也不授权发布。

交付本地result.md、manifest.json、源与测试SHA索引；无需ZIP，因为本任务无真实归档输入且禁止网络发布。交付后STOP，等待Astra验收。旧Delivery V2仍FAIL_CLOSED；正式V010不变；model_activation=False；REAL_GE=False；Results=FALSE；V011=NOT_STARTED；FULL_RUNNER_IO_CLOSURE=BLOCKED。
