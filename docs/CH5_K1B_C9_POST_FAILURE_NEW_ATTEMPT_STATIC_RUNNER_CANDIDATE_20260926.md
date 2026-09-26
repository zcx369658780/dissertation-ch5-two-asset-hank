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

## Repair2 独立候选（2026-09-26）

Repair1 提交 `0e71c8edfed120c5f117f2e16815748b280fa3a5` 经 GPT Work 独立判为 `REJECT__SEALED_INPUT_PATH_GAP_AND_EVIDENCE_AMBIGUITY__NO_SCIENCE`。Repair1 五份文件原始 SHA-256（wrapper、delegate、test、报告、收据）依次为 `D4F2A1BACA2838217950CC7468A5B27509B558A3BD3A6865A9ECB7B0E9E9CB01`、`44080FE05EEAD299F34DBD1FAB33EDCB3A0E77B04459402169F5ADD24EEBC84A`、`4D1FB993E00C04582865B74A9FFFF0EEDD7DEDAA58D5BEE3E47DD286D4B8DBE6`、`EB75C82E84A0BCDCEA0B46501BE53B5442AA890C4B98B13E9BB789ABB0150B1F`、`47540885CF338CC315DE4CC0519E81D8A03D6A1D8971778C49BC6487BDBC5901`。前文原候选的两次违规执行标志探测、三次 `7 passed` 均属原拒绝任务；Repair1 只有一次 `10 passed` 的只读测试。本段记录仅属 Repair2，不改变两个 REJECT 结论。

Repair2 在两份 runner 中为 C8 execution/entering manifest、readback、JSON、NPZ、comparison、terminal，以及 C9 partial manifest 和 `timing_failure.json` 增加完整路径 `lstat` 检查、普通文件判断及原始哈希核验。C8 目录扫描改为逐层检查后再递归，拒绝 reparse/junction 子目录。wrapper 的静态门、未来门和 delegate 加载前入口均先核验封存路径；delegate 的静态门、未来门、直接封存读取和源快照也先核验。五个受保护清单核验仍保留。未修改封存输入或经济、求解器代码。

只运行授权的惰性测试文件：首次 `31 passed, 1 failed`，失败是旧测试仍模拟 `Path.is_file()`，与新的 `lstat` 判断不一致；仅修正该测试后，允许的一次定向重跑为 `32 passed in 2.53s`。参数化测试覆盖五个 manifest 各自的哈希替换、缺失叶文件和 reparse 父组件；另覆盖 C8 JSON/NPZ、C9 timing failure 叶及父组件和新根父组件的只读模拟，检查静态/未来门拒绝且新根未创建。重跑后，源码检查发现直接加载 delegate 前仍需同一封存路径门，已补入 wrapper；按一次重跑预算未第三次运行测试，因此最终 wrapper 这两处新增前置门只有静态源码检查，未获最终版本的完整测试验证。未来真实执行、竞态和 Windows junction 行为仍须独立审查。

Repair2 本身的执行标志探测、模型/科学调用、新 C9/C10 尝试、重试、部分续跑和保护输出写入均为零；旧 `RUN001` 实际账本继续为 `CALL_LEDGER_UNRESOLVED`，完整旧 turn 扣账仅是治理额度。当前 wrapper/delegate/test 原始 SHA-256 分别为 `B7C276FF55EAB99B5894051B10753B62C040636FCC0271C2B2EA9B2BD678EB86`、`B890F16C515249F91BFD71DAE9797FB00A5E8AE7631F688E6DCAF79CB60BD794`、`38C1B5C51DAA345847F1E9E06F431892D6F0C43D5DC2BED6CF3642AAFEF552FC`。新输出根和 live 合同/执行采纳/任务仍不存在。结果资格 `FALSE`；提交后仅待 GPT Work 独立 ACCEPT/REJECT。

## Repair2 最终入口静态验证候选（2026-09-26）

本轮任务 `CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_FINAL_ENTRY_STATIC_VERIFICATION_20260926` 基线为 `bd0d04b741ec1f1d953d8b6331db4b055f3fa5e3`，其父提交 `d55e12d4af0e187efb68af727e16b78afec70942`，`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。基线跟踪文件与暂存区干净，仅有 C6-prime、C7、C8、C8-timing、C9-partial 五个受保护未跟踪输出根；五份清单哈希仍分别为 `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`、`413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`、`5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`、`5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`、`80BD0D42CB73B4E39B811E759505480542D5A73227014F30B732C34A8AC1FDC3`。新输出根、新 live 合同、执行采纳及执行任务均不存在。

仅在现有惰性测试文件加入两项 AST/source-order 检查，读取最终提交的 wrapper 字节并解析函数体。`load_delegate` 的 sealed-evidence、protected-manifest 与输出路径门位于 `committed_file`、模块 spec 创建和 `exec` 之前；`run_timed_action` 的同类门位于 `load_delegate`、`future_gate` 与时钟采样之前，并检查直接输出领取调用不会早于这些门。检查测试源码后，只运行一次 `python -m pytest -q tests/test_mp4c_k1b_turn9_post_failure_new_attempt_preflight.py -k final_committed`，结果 `2 passed, 32 deselected in 0.07s`。未运行更广测试，也未调用 `--execute`、`execute_once`、`run_timed_action`、`load_delegate` 或科学入口。新尝试、C10、重试、部分续跑、模型/科学调用和受保护输出写入均为零。

原候选 `REJECT__TASK_BOUNDARY_VIOLATION_AND_STATIC_GAPS__NO_SCIENCE`、Repair1 `REJECT__SEALED_INPUT_PATH_GAP_AND_EVIDENCE_AMBIGUITY__NO_SCIENCE`、Repair2 `REJECT__FINAL_ENTRY_GUARDS_UNTESTED__NO_SCIENCE` 仍是各自独立裁决。原候选两次违规 `--execute` 测试探测不能因本轮验证改列为合规。本轮只证明这两处最终源码的静态顺序，不能证明未来运行时行为、旧实际账本已核清、C9 完成或 Results 资格。旧 `C9_TIMED_RISK_RUN001` 已消耗，实际账本仍为 `CALL_LEDGER_UNRESOLVED`；完整旧 turn 仅作治理扣账。Results eligibility 为 `FALSE`。候选提交后等待 GPT Work 新一轮独立 ACCEPT/REJECT；任何新 C9 科学执行仍须 Owner 单独明确授权。

## 新尝试导入前身份修复候选（2026-09-26）

本轮任务 `CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_PREIMPORT_IDENTITY_REPAIR_20260926` 起点 HEAD 为 `a34d3d52e1f4b02f4c7df6f4b9774658c5373c14`、父提交 `5ecabfb06be9bd5cc54392ed5ea8eb102739629f`、`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。跟踪文件与暂存区干净，仅有五个受保护未跟踪输出根。C6-prime、C7、C8、C8-timing、C9-partial 清单原始 SHA-256 仍分别为 `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`、`413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`、`5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`、`5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`、`80BD0D42CB73B4E39B811E759505480542D5A73227014F30B732C34A8AC1FDC3`。新 C9 输出根、live 合同、Owner 执行采纳、执行任务和 runner-recognized ACCEPT 审查文件均不存在。

修复限定于两个审查缺口。`static_preflight` 现在按 `require_inactive` 分支：inactive 明确要求未来权威文件缺席并返回不可执行状态；active 不再把文件存在本身判为失败，而先调用不导入模块的完整提交权威身份门，缺失、未提交或不匹配时拒绝，仅对核验通过的链返回静态预检状态。wrapper 在执行 delegate 模块前、delegate 直接权威帮助函数在执行 wrapper 模块前，分别核验合同、当前任务与副本、GPT Work runner 审查、Owner 一次性采纳、双方 runner 提交哈希及其相互绑定。原封存证据、五份受保护清单与新输出路径门仍先于模块执行；导入后预算、来源和输出门保留。delegate 直接 CLI 保持关闭。本轮未修改方程、求解、冻结输入、预算映射、36,000 秒资源墙、调用记账或输出归属。

只新增解析源码的惰性测试，没有导入 runner 模块或调用任何执行函数。唯一授权命令 `python -m pytest -q tests/test_mp4c_k1b_turn9_post_failure_new_attempt_preflight.py -k repair3` 共运行两次：首次 `3 passed, 34 deselected in 0.09s`；补强对封存/保护/输出门先于提交身份检查的静态断言后，第二次 `3 passed, 34 deselected in 0.12s`。第二次后未改代码，也未运行第三次或更广测试。这些 AST 检查证明源码中两状态分支、权威检查及导入顺序，不能代替未来真实活动链、竞态或科学行为验证。

原候选 `REJECT__TASK_BOUNDARY_VIOLATION_AND_STATIC_GAPS__NO_SCIENCE`、Repair1 `REJECT__SEALED_INPUT_PATH_GAP_AND_EVIDENCE_AMBIGUITY__NO_SCIENCE`、Repair2 `REJECT__FINAL_ENTRY_GUARDS_UNTESTED__NO_SCIENCE`、有限入口顺序 `ACCEPT__FINAL_ENTRY_STATIC_ORDER_ONLY__NO_SCIENCE`，以及随后整体身份 `REJECT__ACTIVE_PREFLIGHT_AND_PREIMPORT_AUTHORITY_GAPS__NO_SCIENCE` 均保留原裁决范围。原候选两次违规 `--execute` 探测仍属违规。本轮 `--execute`、模型/科学调用、新 C9/C10 尝试、重试、部分续跑与受保护输出写入均为零。旧 `C9_TIMED_RISK_RUN001` 已消耗，实际账本仍为 `CALL_LEDGER_UNRESOLVED`；旧完整 turn 扣账仅为治理额度。Results eligibility 为 `FALSE`。候选提交后必须停下等待 GPT Work 独立 ACCEPT/REJECT；新 C9 科学尝试仍需 Owner 单独一次性授权。
