# CH5 TEMP V010 — 价格输入来源审查与共享账本可靠性先验验证（合并长任务）

TASK_ID=CH5_TEMP_V010_PRICE_ATTRIBUTION_LEDGER_PRECONDITION_20261021
REVISION=ISSUED_20261021_R1
SCOPE=SOURCE_ONLY_ECONOMIC_FORENSIC_PLUS_ISOLATED_NO_HA_LEDGER_TEST
OWNER_AUTHORIZATION=2026-10-21明确同意将阶段A与B合并为一张受界长任务单
SCIENCE_CALL_BUDGET=0

## 1. 科研定位与不可改变边界
- **阶段A**严格只读历史报告和指定不可变GitHub源码，梳理MATLAB-faithful HA外部的宏观收益/工资/财政价格流、单位与时序；只能做已有源码的代数oracle与少量无HA纯公式复算，不能执行生产模型。
- **阶段B**在独立scratch内以Python标准库编写新的纯合成journal/ledger小测试（不运行、不import、不覆盖生产ledger），观察Append→原子checkpoint→reader→E2共享STOP机制与WinError5故障注入。单次长任务在E1内可自行修复普通工程脚本/fixture，保留首错。
- **本合同不执行阶段C**：不重启原100轮、A0/A1/A2/A3、不授权任何新HA/HJB/KFE/GE/IRF调用、V011启动或正式V010数学变更。旧任务预算全部CLOSED_NO_CARRY_FORWARD。阶段B即使合成PASS，也只证明参考实现/模拟保护机制在此次环境可用，**不代表原2026-10-18生产ledger已修复或真实Windows WinError5根因已证明**。
- 正式V010/v0.0.10与MATLAB-faithful HA黑箱不可擅改，Bellman仅TEMP观察不提升为新硬门。历史2009年31省稳态parity仅其受界case有效；研究Results/REAL_GE仍FALSE。

## 2. 冻结身份和来源裁剪
治理仓库zcx369658780/dissertation-ch5-two-asset-hank，治理branch migration/astra-workflow-20261012，正式动态入口CURRENT.md、TASK_CURRENT.md、docs/DOC_INDEX_CURRENT.md，同一live快照校验本TASK_ID授权。该合同通过后发ISSUE_MANIFEST关联固定issue commit；历史parent用于本轮独立review的创建而非要求live HEAD等于其值。
冻结精确资料位置/Blob/Commit统一在TASK_PARAMETERS：
(A) 六份已接受历史科研报告/回归简报/正式V010冻结计划，均从固定治理commit a48137c03cebaa4c5e4090a7880ae170a1bb1aca读；
(B) 五份最相关宏观源码（firm/wage/steady_state/capital_network/one_turn），仅从固定模型commit 94de4501dec051b969bee9d852eba2d4591f30ef按Git Blob只读；
(C) 原2026-10-18 TEMP 2×2实验合同从固定commit 2c855f616efbca05c29d4069a44e3c6651070b44只读，合同是历史参考、并非执行许可。
仅上述12个精确Git文件为任务研究输入；其他repo代码默认不打开，不读任何整仓库递归树、不下载历史910/278/491/158成员ZIP、不查旧本地privates/密钥/真实数据/真实2017/2018。非意图源、blob不一致、Git权限/IO失败STOP_SOURCE_INTAKE；普通重试只限同路径/commit一次。
历史100轮静态数字**来自已接受的独立审查报告**，不冒充本轮对run/trajectory.jsonl原始100行复核。来源与信用等级必须列明：REVIEW_ACCEPTED_STATIC_FACT / CODE_STATIC_ORACLE / HISTORICAL_CODEX_REPORTED / HYPOTHESIS / NOT_OBSERVED。
保护基线和本机身份从参数指定的有限可信父链与Git locator/index获取；BOOTSTRAP0仅只读并确认新scratch不存在，BOOTSTRAP1独占创建，BOOTSTRAP2首次日志写前重新确认，绝不写受保护正式worktree/index、原研究目录或其它项目。本任务Python标准库/Git现有程序，不安装软件、不改代理/凭据/系统配置。

## 3. 阶段A：经济学因果链SOURCE_ONLY
必须以正确来源、时序、单位与实际消费点逐项追踪至少这些变量：
raw ra0、企业clip ra_used、lagged score raw、S[j,i]、同一S下资本数量与rah、企业raw wt0和used wjt、目的地tau、税楔sigma、w_eff进入HA前是否可能被prepare_mainline_household_states重绑定、企业补偿和财政WageTax/GovInv/Zt。
明确下一轮资本回报/当前企业报价/税前工资与税后家庭收入是否同单位、同价格对象；不能在“变量值不同”与“模型bug”之间跳跃。检查原MATLAB vs V010 source 的历史已知区别，列出原模型与当前TEMP采用的各自逻辑。
需提供：价格生产/消费方向图、逐变量(生产文件/字段→转换公式→轮次→消费文件/字段)矩阵、为何会clip/未clip的公式链、100轮事实与静态同状态替代工资的证据等级、可能的合成尺度异常/控制器门条件/原单位问题排序及每个可证伪条件。
允许调用新scratch内**只做代数验证**的Python脚本(不import生产HA/runner，不请求旧轨迹)，作为恒等式/输入约束oracle；不能把同状态代数反事实称为新价格桥收敛结果。若某消费点的真实原代码（如TEMP私有桥或prepare调用）不在授权五文件内，只记SOURCE_NOT_AVAILABLE/NEEDS_OWNER_E3_SOURCE_SCOPE，不能补猜、读取未经授权的本地ZIP或擅改程序。
输出price_lineage.md、price_source_matrix.json、claims_and_hypotheses.md、静态来源哈希/行号与缺证点清单。

## 4. 阶段B：共享ledger无HA合成资格门
只在新scratch/synthetic_ledger创建安全参考脚本与synthetic fixture，不复制真实journal、旧WinError诊断ZIP或原科学driver。使用Python stdlib可在Windows适度合成读写进程但只控制自己创建的child，禁止对系统/其它进程通用PID扫杀。
最少6组聚焦测试：①单写者事件seq/previousSHA链与checkpoint一致；②append后在checkpoint前可恢复的单步故障，保留原头及恢复语义，不把缺失checkpoint当正常完成；③Windows只读者在目标checkpoint持有句柄时的os.replace行为，捕捉是否真的WinError5，不允许事后虚构必现；④明确注入PermissionError/WinError5及残留current.next处理，首错持久化，真实seq/head不倒退；⑤A1出现E2后能在合成A2/A3下一模拟HA入口前传播STOP，禁止把失败任务继续计费成成功；⑥任务自有子进程计费/确认reap和私有/公开证据分离。
每组保留输入、断言、stdout/stderr脱敏摘要、实际原始私有证据、安全停点、负例与平台依赖。负例中预期拒绝不算任务E1；无法可靠复现WinError5必须写NOT_REPRODUCED，不得伪装生产修复。合成失败而修脚本允许在本任务3个E1批次中自行修复；但如果需要修改生产ledger源码/桥/runner则STOP_SCOPE_REQUIRED，不能借研究任务越权。
阶段B最后给出足够具体的“下一次生产账本单写者+sharing+checkpoint+STOP真实接口验证”建议，指出哪些属于模拟通过、哪些必须在真实原2026-10-18生产ledger源码与受控Windows句柄下才能认证。即使所有模拟测试PASS，终态最多SIMULATED_LEDGER_GATE_PASS__PRODUCTION_UNVERIFIED，不得自动启动A1/A2/A3。
源历史事件A1 11条而checkpoint seq9、A2/A3各25条，E2 STOP传播延迟，是历史已接受证据，不是本轮新增采集；缺少运行原件不将其升级为本轮机核。

## 5. 资源预算、E1/E2与STOP
采用TASK_PARAMETERS数值；本任务总墙钟上限7200秒，stage A/B工程独立账，Python starts全局受界，只有预定自有helper才能启动/终止；kernel OS子孙真实不可观测记UNKNOWN而非0。额外本地非Git文件≤64MiB、Git对象≤1GiB，总GET≤48，工程与交付分期计数，至少保留180秒封存。无旧任务额度借用。任何真实受保护写入、敏感外泄、平台拒绝、真实资源门失守或要求超出固定白名单为E2/E3，立即停止安全封存，不通过新登录或重建权限绕过。
不得安装软件、克隆全仓库、调用正式模型/旧测试/家计数、模型伪HA模拟、未经授权科研数据。
先验验收原则：阶段A允许SUPPORTED_SOURCE_ONLY/INCOMPLETE_SOURCE；阶段B允许SYNTHETIC_PASS/CONDITIONAL/FAIL_CLOSED，不能因为B PASS宣称真实WinError5根因已经锁定。若A资料不足以完成全部变量，仍应输出充分已知部分与缺口，除涉及身份、隐私或硬门冲突不得无谓提前重签任务。

## 6. GitHub独立证据交付、审查和本任务停止
新任务自己的脱敏结果通过现有已授权精确Git Data API，或在发行前权限能力缺失且无策略拒绝的条件下使用合同批准的受界SSH。权限拒绝、401/403/429、认证问题硬停不切换方式绕过；固定review_branch=`review/ch5-temp-price-ledger-precondition-20261021`，固定parent=a48137c03cebaa4c5e4090a7880ae170a1bb1aca，temp_path=`_review_tmp/ch5/temp-price-ledger-precondition-20261021/`，仅新增result.md、manifest.json、evidence_sanitized.zip三件；普通非强制唯一候选，不能修改治理/main、已有待审HTTP证据review分支，也不能用root recursive=1或全仓库clone。ZIP必须包含新阶段A/B可实际读的关键文档、合成源码/fixtures/测试原件及安全资源、首错，逐成员脱敏/索引SHA/CRC/路径检查；不把hash-only列表冒充脚本。
Codex在本任务安全发布后精确回读真实raw bytes(含ZIP全部成员标准库复验)，最终返完整原始JSON回执Base64、实际字节长度/SHA256、新run_id、候选commit/tree/唯一parent、计数与真实终态和独立外部exit事件；URL/blob ID/退出0不足以证明交付。
Astra待终审后依当前五步：完整原件机器验真、聚焦经济学静态结论/合成测试实际源码与隐私→PASS/CHANGES_REQUIRED/REVIEW_PENDING_IO→先永久归档回读再精确非强制清理；PENDING保留。**前一尚未独立验收的HTTP候选1579e7f1d7a1975c322dd6ae9af1776e88e83e7c必须继续保留，不在本任务中触碰/清理。**
预期停点WAIT_ASTRA_TEMP_PRICE_LEDGER_PRECONDITION_REVIEW，具体真实停机以回执为准。成功结果只是A/B先验科研诊断，不是稳态、经济政策或Results获得通过。
