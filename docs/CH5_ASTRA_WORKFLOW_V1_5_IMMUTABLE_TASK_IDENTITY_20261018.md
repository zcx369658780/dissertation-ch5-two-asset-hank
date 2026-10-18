# 第五章工作流 V1.5：不可变任务身份与启动校验

日期：2026-10-18
性质：对V1.4启动身份、任务合同读取、任务重发和Codex启动Prompt的窄修订。V1.4其他科学、资源、STOP与三平面同步规则继续有效；冲突时本文件仅覆盖任务身份与启动校验部分。

## 1. 最新经验与正式结论

Adapter任务 TEMP_V010_RESOURCE_GATE_V3_ADAPTER_INTEGRATION_20261018 未进入BOOTSTRAP写阶段。Codex在构造校验文本时替换了正文内的历史V3 commit/blob引用，导致本地组装文本与固定合同Blob不一致。固定远端合同并未因此被证明有误。

本轮正确终态：FAIL_CLOSED_TASK_RAW_IDENTITY / STOP。BOOTSTRAP 0失败；BOOTSTRAP 1/2、测试、runner、科学均NOT_RUN；修改文件和新工件0。

这属于启动材料构造/身份验证流程缺陷。STOP行为正确，不得追责为“应该继续执行”。

## 2. 不可变合同原则

1. 固定合同是只读原件。不得通过文本替换、模板渲染、统一改写哈希或组装“校验版正文”来验证其身份。
2. 历史Commit/Blob/SHA、当前任务Commit/Blob/SHA、治理HEAD是不同语义的独立字段，不得全局替换或互相覆盖。
3. Git Blob SHA与文件SHA256算法不同，禁止把二者当作同一种哈希；长度与编码也必须使用明确的原始字节定义。
4. 验证必须直接针对从固定发行Commit读取的原始文件字节：
   - GitHub内容读取工具若只返回解码文本，不得宣称已获得Git原始blob字节；
   - 可核对路径、commit、返回Blob ID、编码文本的UTF-8长度/SHA256，但证据等级必须标为CONNECTOR_TEXT_VERIFIED；
   - 只有原始blob API/本地Git对象字节及其Git对象哈希可用时，才标RAW_GIT_OBJECT_VERIFIED；
   - 身份不匹配立即停止，不尝试修正文档。
5. 任务合同正文不得引用自己的发行Commit/Blob作为必需内容，以避免自引用循环。发行Commit、合同Blob、文件SHA256、长度统一放在CURRENT/TASK_CURRENT或独立发行清单中。
6. 历史V3身份应保持原样：commit 09e073ee69b34fc22dd5448a6a39156a0cd11775；blob f323a5855600b5dc4ef715a73533421dc09d1e99；run_id 49b82ce3c2554dbeb0aa2fb6b0b2f067。这些是历史基线，不得为新任务而替换。

## 3. 启动Prompt的生成规则

1. Codex启动Prompt是导航说明，不是合同原件；不得将Prompt重新拼成合同校验文本。
2. Prompt只引用固定任务ID、发行Commit、合同路径及合同Blob等独立元数据，并明确“完整合同直接读取，禁止重写或替换合同正文”。
3. 启动Prompt中不得复制整份合同后再做文本变换；不得用正则、sed、脚本或手动替换历史哈希以生成校验材料。
4. Prompt、CURRENT和TASK_CURRENT字段不一致时，Prompt服从当前治理状态并STOP；不得自行挑选“看起来最新”的值。
5. 若固定任务合同读取失败，可对同一固定Commit/路径做一次无副作用只读读取；仍失败即STOP。禁止改路径、改分支或改哈希猜测修复。
6. 启动身份核验必须是只读。BOOTSTRAP 0通过之前，不创建scratch、日志、脚本、测试夹具或其他文件。

## 4. 分层启动与失败分类

- TASK_RAW_IDENTITY：原始合同/发行元数据不一致。只读STOP，不创建工件。
- GOVERNANCE_STATE：CURRENT/TASK_CURRENT/合同授权冲突。只读STOP。
- PROTECTED_PATH_IDENTITY：保护根或目标scratch无法认证。只读STOP，不换路径。
- RESOURCE_GATE：运行期实际进程/线程/Job与预算不一致。E2 STOP。
- DELIVERY：只处理交付证据，不重跑科学或工程测试。

每次失败报告必须写明失败层、触发字段、预期值、实际值、证据来源和哪些步骤未运行。不得把身份错误修成另一个内容后沿用原任务ID；合同确需修改时发行全新任务，保留旧合同与失败证据。

## 5. 启动校验最小协议

启动阶段只允许：
1. 读取当前治理HEAD、CURRENT、TASK_CURRENT；
2. 从固定Commit/路径读取合同，保存读取工具原样输出，不改正文；
3. 比较任务ID、路径、Commit、Blob、长度、SHA和授权字段；Git Blob与SHA256分开验证；
4. 只生成内存中的差异报告；BOOTSTRAP 0未通过前不落盘；
5. 全部通过后才按V1.4既有规则执行BOOTSTRAP 0/1/2的后续步骤。

如果接口无法给出原始Git字节，只能对连接器文本做有限验证，并明确证据等级。不可为了追求更高证据等级而改写合同或绕过工具边界。

## 6. 当前科学与任务权限

本规则本身不授权运行任何模型、runner或测试。先前Adapter任务由于TASK_RAW_IDENTITY在BOOTSTRAP 0停止，记为 SUPERSEDED_NOT_STARTED，不续跑，不改写其历史记录。

新任务必须使用新TASK_ID、新发行提交和新合同路径。旧TEMP价格调参与旧ResourceGate V2失败继续FAIL_CLOSED；V3有界单子进程基线保留既有验收范围。

正式V010不变；V011 NOT_STARTED；model_activation=False；REAL_GE=False；Results=FALSE；FULL_RUNNER_IO_CLOSURE=BLOCKED，直至有独立证据支持改变。
