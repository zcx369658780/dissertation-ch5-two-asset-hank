# C9 失败后新尝试：零科学静态 runner 候选

**状态：待 GPT Work 独立 ACCEPT/REJECT；执行权关闭。** 本候选只新建一对隔离 runner、一份惰性测试、本报告与机器收据。未修改旧 wrapper/delegate、`src`、现有合同、Owner 文件、任务或五个受保护输出根。`C9_TIMED_RISK_RUN001` 已消耗，其实际账本仍为 `CALL_LEDGER_UNRESOLVED`。Results eligibility 为 `FALSE`。

## 候选身份与静态门

新 pair 固定候选 ID `C9_POST_FAILURE_NEW_ATTEMPT_001`、独占且当前不存在的根 `reports/ch5_k1b_turn9_post_failure_new_attempt_001`、命名空间 `C8_START_C9_POST_FAILURE_NEW_ATTEMPT_001_C10_PROSPECTIVE`。新 wrapper 的默认入口仅校验已采纳预算 JSON、Owner 采纳哈希、旧失败终态、五个受保护输入身份、冻结 C8 manifest/readback/JSON/NPZ 和新根不存在，返回 `BLOCKED__NEW_LIVE_AUTHORITY_ABSENT__PREPARATION_ONLY`。该静态状态不声称合同已激活。旧 `RUN001` 被显式拒绝；即使给出新 ID，`--execute` 在新 live 合同缺失时也于 delegate/模型导入及输出创建之前拒绝。本任务没有建立新 live 合同、runner 独立审查、Owner 执行采纳或逐字节任务副本。

新 wrapper/delegate 候选从已接受的旧 C9 经济和求解路径机械分离，保留九项载体、冻结 C8 来源、方程、网格、阈值、阻尼及零重试。delegate 的直接科学入口仍拒绝，科学路径必须经新 wrapper 的完整提交身份链。新 wrapper 的未来门要求新合同逐键绑定新 ID/根/命名空间、runner 与 delegate 原始哈希、39 类每 turn、5 项逐省、39 类新 C9 加未来 C10 累计、39 类旧完整 C9 治理扣账及生命周期治理上限、36,000 秒 C9-only 协作墙、冻结输入、独立审查、Owner 执行采纳和已提交且逐字节相同的任务。合同/任务/审查路径仅是将来的常量，当前均不存在。C10 没有执行路由或自动授权。

`BudgetGuard` 在原有入门前每类别/逐省/单 turn/累计保护之外，检查“旧完整 C9 治理扣账 + 新尝试计数”不超过已采纳生命周期治理图。扣账是**行政额度**，未写成旧实际调用；日志和失败记录仍显式标出 `old_actual_ledger=CALL_LEDGER_UNRESOLVED`。已修复的 `MeasuredGuard.reconcile(ledger, province=None)` 继续转发省参数。资源墙使用单调时钟，只在下一科学入口检查；在途调用不会由该检查强制中断，人工中断或未核清账本也不产生免费重试或部分续跑。保全首失败和部分证据的原有路径保留。

## 证据与检查

本候选绑定的 Owner 采纳文件原始 SHA-256 为 `C1D88891C08D7526996F72DE6F77AA6D0FA2C593BAD91017877C8B8A0A51573D`；已采纳提案 JSON 的历史原始 SHA-256 为 `66C2C028B07E2CB41FFBB05B643C6EF644291A0FC94C8DAF2FE888518D240460`。该 JSON 内的 `adopted=false` 是创建时状态，后续 Owner 文件单独赋予治理采纳；runner 不把历史字段自行改写。三张预算映射的规范哈希为 `F76B958C8D57CEAD22B61A497FCCFBF45143E1DC2AA07CCC656EBA6252464C20`、`FDA5A76D45B639FD0B793E6270D051255CCFC0F85E7E982A152A4AA7743D7028`、`3E2DF35B6D867A0680E1ABBBB778205982F1845139D775A63A9D4672B7D6CA3A`；生命周期图为 `D5C5D10AD030FFD2F12AA81FFFD8DBD5CF8655D4870452593C7AA3B5A224604C`。冻结 C8 manifest/readback/JSON/NPZ 原始哈希为 `40200B60729A5B4173E24661843980851F8610A9FA2186F7E411B7FE9E5CDC65`、`E428D105600D091979B526ADD6BF61E0FC294050B9FAB97FE8B87A29A1012F85`、`FBB18A5B8B4FD94F337510DBB4E62F94188C27863EED1F79FE2E1A71B5BC39AB`、`E7E6AF79864F67A28386ECF8BEB3B71C6080E9A6C6E64F4CBA8125E1C19D34DD`。

只读 AST 解析三份新代码文件通过。仅运行 `python -m pytest -q tests/test_mp4c_k1b_turn9_post_failure_new_attempt_preflight.py`，三轮均为 **7 passed**，最终测试只调用只读权威门、预算 guard 与默认静态入口。它验证旧 ID/缺失权威拒绝、输入与采纳图身份、新根未创建、尝试与逐省及零重试 guard、36,000 秒入口谓词、首失败分类及两参数 `reconcile` 转发。**测试过程偏离：**前两轮惰性测试曾以 `--execute` 参数调用新 wrapper 的 `main`；均在新合同缺失处拦截，未导入模型或创建输出根。这两轮不作为零执行边界的合规证明；最终第三轮改用只读 `future_gate`，为 7 passed、0 failed。没有旧或新模型科学调用。最终原始 SHA-256：新 wrapper `3A3EAF65B2BFDD073E1700F072016CC0FD877991BB8B07C2400EA7AC2AE60771`；新 delegate `FFFA102D4C5AEF78CCAA717F5EBAC46E6B3441B55A4668E9252CF0576258870E`；惰性测试 `6C074499C50BC0351B196098311F75A64760F07D981FDF195A4BBB22F44F29F4`。

这些静态测试不能证明未来 live 合同、完整 C9、实际调用账本或数值收敛。下一个门是 GPT Work 对**这五条路径**独立 ACCEPT/REJECT；之后才可能分别提出新合同和执行身份链的零科学任务。任何新的科学执行仍需单独 Owner 一次性决定与独立最终审查。旧失败部分 C9 不计 prospective 两次连续 pass，C10 与 Results 均保持关闭。

## Repair1 补充记录（2026-09-26）

前述原候选经独立 GPT Work 判为 `REJECT__TASK_BOUNDARY_VIOLATION_AND_STATIC_GAPS__NO_SCIENCE`。原五份未跟踪文件的原始 SHA-256（wrapper、delegate、test、本报告、收据）依次为 `3A3EAF65B2BFDD073E1700F072016CC0FD877991BB8B07C2400EA7AC2AE60771`、`FFFA102D4C5AEF78CCAA717F5EBAC46E6B3441B55A4668E9252CF0576258870E`、`6C074499C50BC0351B196098311F75A64760F07D981FDF195A4BBB22F44F29F4`、`0EB848C5BEBF0E150A0FD546D8D0648A92A76E5EE892C97A8EC98B4A75087A19`、`5AA0DF1BDB33815EC02A6E65523A9E719C6078A24AF2DD9CC69609328323DB16`。原任务两次以 `--execute` 调用 wrapper 的测试探测均违反边界，虽在缺失合同处拦截、未进入模型/科学或创建新根，仍不因本次通过测试而变为合规。

本次 Repair1 仅原地修补同五条路径。两份 runner 的静态前检和未来身份门均核验 C6-prime、C7、C8、C8-timing、C9-partial 五份精确 manifest；所有受保护路径组件使用 `lstat` 拒绝符号链接及 Windows reparse/junction，缺失或替换 manifest 均 fail closed。wrapper 的新根路径检查也改用相同规则；未来 `execute_once` 的缺失合同拒绝位于 delegate 加载及任何输出根领取之前。新增只读测试仅直接调用静态门/未来门并检查 AST，模拟缺失、替换与 reparse，不调用 `--execute`、`execute_once`、`run_timed_action` 或科学入口。

Repair1 定向命令 `python -m pytest -q tests/test_mp4c_k1b_turn9_post_failure_new_attempt_preflight.py`：`10 passed in 0.67s`，本次只运行一次。新 wrapper/delegate/test 原始 SHA-256 分别为 `D4F2A1BACA2838217950CC7468A5B27509B558A3BD3A6865A9ECB7B0E9E9CB01`、`44080FE05EEAD299F34DBD1FAB33EDCB3A0E77B04459402169F5ADD24EEBC84A`、`4D1FB993E00C04582865B74A9FFFF0EEDD7DEDAA58D5BEE3E47DD286D4B8DBE6`。本次执行标志探测、模型调用、科学调用、新 C9/C10 尝试、重试和部分续跑均为零；受保护输出写入为零，新根仍不存在。五个保护清单原始哈希复核通过。该记录只提交新的静态候选，仍待 GPT Work 独立 ACCEPT/REJECT；Results eligibility 为 `FALSE`。
