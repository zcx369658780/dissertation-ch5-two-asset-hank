# 第五章 V1.3：本地工程快速通道与分级独立验收
**2026-10-18长期证据传输扩展：** [Owner批准新任务GitHub临时MD＋脱敏ZIP](CH5_OWNER_REVIEW_MD_ZIP_TEMP_EXCHANGE_POLICY_20261018.md)。后续固定新任务可白名单`evidence_sanitized.zip`，须逐条清单/递归内嵌压缩包审查，原RAW/私人路径不得因临时上传而公开；Codex SSH+独立bare及Astra正式归档后清remote temp文件不变。**这里只变证据交付协议，不改变E1/E2/E3门、旧科学和网络预算。**


**Owner批准日期：2026-10-17。**
**工作流状态：OWNER_APPROVED__GITHUB_PUBLISHED__LOCAL_CODEX_SYNC_PENDING。**
**适用范围：**本项目此后新签发的任务、Codex本地工程执行与Astra工程验收；既有冻结任务与历史失败原件不追改。
**唯一学科主线：**修正原MATLAB两资产HANK/多省顺序方法并以Python复现，推进博士第五章成果。V1.3不提供新的模型、真实数据、HJB/KFE、GE、IRF或Results权限。

## 1. V1.3替代的低效习惯

过去多次把JSON类型误拒、sourceIndex空值、普通脚本和证据封存缺陷各自变成新的不可续任务，造成“每次运行先为证据工具补证”的循环。又将一次工程验收拆成正式长主审、CURRENT、TASK_CURRENT、目录、版本、科学决策、长期知识和路线图逐个提交，出现多次远端写入/读回及重复的旧ACTIVE。

V1.3明确恢复原V1.2原则：**Codex对已经冻结授权的普通工程范围有自主修复权；Astra集中验收；GitHub不是工程微步骤中转站**。不提高真实科学、保护文件、网络发布与敏感数据操作的权限。

## 2. 三档门禁（执行中一次判断，严格分账）

| 类型 | 示例 | 新处理 |
|---|---|---|
| E1普通工程可恢复 | JSON日期解析差异、非关键schema字段、manifest生成器bug、白名单内脚本和合成测试错误 | **在同一新任务**的明确工程修复额度内定位、修复、复测，保留初次失败；无需再让Owner审批一次微任务。 |
| E2关键工程硬门 | 首次写入前路径身份未验、文件身份或原字节不可确认、同用户重解析/alias、source执行绑定不可信、资源上限或stdout失控 | 立即暂停受影响链并FAIL_CLOSED；**不得**事后补造前置证据。在任务写明的备用动作已独立授权时方可走备用动作；否则STOP并报告，不借其他领域预算。 |
| E3科学/安全/外部硬门 | 经济方程或数值阈值修改、未授权HJB/KFE/真实数据、敏感内容公开、GitHub超许可提交、原保护工作树写入/强推 | 无条件STOP，Owner须给新批准及准确冻结任务。 |

普通工程是否属于E1必须由**当次冻结任务事先划定具体路径、操作、测试及总预算**；不允许依赖通用V1.3文字重开以前停止的次数。E2/E3守门不因“用户科研无保密需求”而省略源文件及备份防误写。

## 3. 第一次写入前的安全顺序（Codex不得反过来执行）

**BOOTSTRAP 0：只读可信启动。** 使用已认证、可直接在受信任PowerShell/OS中调用的既有读操作；禁止在待创建目标scratch写启动脚本、第一次日志、错误回执、下载文件或Git对象。记录可信父目录的身份、请求创建的目标及目标不存在、保护根不相交、路径祖先无reparse/junction/UNC/device/ADS/硬链接/同名别名等本次风险门；未知FAIL_CLOSED。需要公开报错时仅向受控终端输出匿名失败状态。

**BOOTSTRAP 1：创建新独立scratch。** BOOTSTRAP0真正PASS才允许创建唯一新的目录；创建后、**写入第一个文件前**重新读回新目录及可信父目录身份，确认与preflight相同。严禁将已写过的失败scratch删除/重建以冒充“首次写前已检查”。

**BOOTSTRAP 2：再启动执行器。** 上述两道身份门有前后只读证据后，才允许写最小manifest/脚本/first receipt。所有执行、异常和最后seal都写在已认证scratch；不覆盖历史原件。Codex可在新工程任务中实现一个可复用的只读preflight工具，但**本次V1.3纯文档同步不授权在原模型树或旧scratch实验该工具**。

**静态首发条件**：只有新任务明确允许工程失败自行修复时，才允许把合法普通修复汇入当前运行；写前顺序违规不是普通修复，不可回溯擦除。

## 4. 一份简洁证据合同代替多层自证明

新run开始即生成`run_id`和最小可信`sourceIndex`（可为空/UNKNOWN但不得虚构），记录冻结task SHA/blob、source/current commit/tree或明确LOCAL_ONLY、文件整体SHA256、相关字段schema、可读边界与声明来源、每次调用实际次数/bytes/time、first/final各自原始字节SHA256以及不可变单向链接。

- first必须是**真实可留存的原文件字节**，不能仅嵌入final的快照或first hash；否则标`SEAL_CHAIN_UNVERIFIABLE`。
- 防自引用：manifest只列其他证据文件的hash，自身hash放在传输结果/远端readback。
- 既有历史缺失原raw、旧run_id、历史代码hash或PS版本，永久标`UNKNOWN / UNVERIFIABLE`，不得因新测试或新seal回填旧run。
- `RAW_EXACT`与`SANITIZED_DERIVATIVE`分别分账；投影文件即使远端可核，也不能替代未上传的本机raw。秘密、token、SSH私钥、原argv及私人路径禁止公开。
- **普通工程交付最小集**：task/ref、真实结果与首个失败、case总/通过/失败/UNKNOWN、资源实际消耗、保护事项、first/final或合理的LOCAL_ONLY说明、最终STOP；不要自动为每次失败生成长报告矩阵。

## 5. 分级验收与文档更新次数控制

**E1快速验收**：读固定任务与一份简短脱敏交付，必要时回读GitHub真实候选；只给一次结论，通常更新`CURRENT.md`和`TASK_CURRENT.md`中的最新状态即可。仅有本机摘要时只能判`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，不得假称Astra在Windows重跑。一次早停如无科学决定，不强制生成独立长篇主审，也不逐次修改七份治理文件。

**E2重要工程里程碑**：集中审查原证哈希及精确提交身份，形成一份正式主审；按需要更新version register和总目录，使用GitHub批量树提交或尽可能少的顺序变更、一次对比与抽样回读；不能为减少步骤跳过必要核验。

**E3科学/数据/论文Results**：维持原完整数学、数值、经济性与来源审查，单独验证HJB双门、KFE、税/人口单位、模型校准、31省GE与GDP目标、冲击和Results。工程PASS不授科学资格。新科学决定才更新`SCIENTIFIC_DECISIONS.md`；长期知识在里程碑而非每次微失败更新。

最新`ACTIVE_TASK`只以`CURRENT.md`、`TASK_CURRENT.md`**顶部一处简短状态**为准；旧历史ACTIVE应留在旧commit/正式审查，而非不断将全套旧段粘到动态索引。不得删除Git历史来获得干净视图。

## 6. GitHub交换、预算与Owner停点

GitHub用于版本合同、必要独立review、备份，而不承担每个普通json/脚本错误的审批传输。Owner已批准在另行明确冻结的任务中，Codex使用现有SSH Key+ssh.github.com:443在新独占bare对象仓对remote-only _review_tmp白名单进行最多明确次数的非force发布，Astra先永久审议后再清理远端白名单临时副本。**V1.3文件本身不授权任何push**，更不准把 _review_tmp 写入任何已有本地工作树/index。秘密须在上传前过滤，Git历史不可视为删除。

新工程任务应给一个有用的总时间/尝试/体积预算与普通修复回旋空间，预留异常收尾；避免对每个普通脚本行另发一张不可续签的“2次PS”任务。科学solver/数据/发布预算仍独立冻结、失败计费、STOP关闭，永不跨任务结转。不得要求新增VM或第三套备份；用户已认可物理独立C/D SSD既有备份+GitHub，并承担可信工作站非OS沙箱的残余风险。

## 7. 生效、一次Codex本地文档同步与未完成事项

Owner已批准升级V1.3。GitHub正式发布后，Codex只需**一次**在已认证的独立本地文档镜像读取当前V1.3规则、CURRENT/TASK_CURRENT、知识入口并回报SHA/来源/保护状态；该次同步不得触原8dirty/index/common-dir或启动模型。同步完成之前状态明确为`LOCAL_CODEX_SYNC_PENDING`，不得声称本机AGENTS和ChatGPT项目Sources已自动改动。

下一独立工程任务建议一次完成“先写前Preflight，再准备安全时间戳证据交换”，而不是再次拆成多个微任务；必须另行固定安全白名单和发布次数。原V010 scientific plan、代码候选、A16/window/C9/CALL_LEDGER、真实C8限制、corrected HA单点未测试、model_activation=False、Results FALSE、V011 NOT_STARTED全保持。

**V1.3不是旧任务的追溯授权，也不等于本轮新源脚本/工程运行器已经安装或通过测试。**
