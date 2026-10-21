# 第五章：强制交付、分层验收与终审后清理

更新：2026-10-19；本次Owner批准验收提效方案。既有冻结任务、失败回执和关闭预算不追溯改变。本条款覆盖未来DOC_ONLY、工程、合成和科学任务的交付与验收组织，不修改科学合同。

## 1. 发单不得缺项或冲突
必须填实：候选对象/来源身份、规范路径、有限保护根与唯一scratch、必要验收内容、REVIEW_BRANCH、FIXED_PARENT、TEMP_PATH、文件白名单、大小上限、独立DELIVERY预算、E1恢复范围、成功发布次数、原字节通道、终态回执通道、清理责任。
执行期离线不覆盖交付联网。不得一边要求上传一边全程NO_NETWORK；LOCAL_ONLY须另有Owner明确批准。基础读取、路径或身份字段不一致由Planner在发行前解决，不让Codex猜测；失败读取不证明源文件被修改。

## 2. Codex自动交付实际证据
安全条件满足时必须自动上传result.md、manifest.json、evidence_sanitized.zip，不以本地路径或Owner搬运为正常终点。必要源码、fixtures、逐项结果和首错须有可审阅内容，不能只交摘要或哈希索引。公开每项内容均须有安全审查，raw_private和凭据不得直接打包。
result写明本轮变化、验收定位、执行结果和已知问题；manifest以相对路径登记载荷、长度、SHA256、来源/派生关系及critical_evidence。ZIP内同一原件只放一次，历史不变件可引用已接受的固定身份，但本轮必需原件不得遗漏。完整原件留存与是否重点语义阅读分开。
manifest不要求自身最终哈希；候选commit/tree、manifest哈希和发布后计数写入包外最终回执。FINAL_RECEIPT及控制器退出后事件必须有明确原字节通道；未发生或未知就如实记录，不从摘要重建。

## 3. Astra验收读取策略
按当前工作流五步执行。固定commit后精确读取目录和三文件，不获取root recursive tree。一次成功获取后复用原字节缓存；成熟标准库批量完成全部成员的长度/CRC/SHA及清单检查。原字节不可获取时标REVIEW_PENDING_IO，不用Git Blob ID或URL代替计算证明。
完整性是机器全量检查，语义审阅按本轮变化和风险聚焦；隐私门不因聚焦而豁免。已有足够证据确认缺陷时可CHANGES_REQUIRED并列出未完成项，无需继续无关全包审查。完整PASS必须完成当前合同全部必需项。
验收工具故障记REVIEW_TOOL_ERROR或REVIEW_PENDING_IO，不算候选缺陷。独立Windows内核UNKNOWN不当作0，也不为消除无关历史UNKNOWN自动运行测试。

## 4. 停止、恢复与状态
普通参数/语法/确定性误报在新任务已冻结的E1预算内修复并保留首错。平台/认证拒绝、实际保护区风险、真来源失配、资源失控或隐私风险为硬门，不绕过。读失败不自动授权重推、重跑或新任务。来源commit与已关闭预算保持不变。
主裁决为PASS、CHANGES_REQUIRED、REVIEW_PENDING_IO；机器记录另列artifact_integrity、implementation_review、privacy_review、delivery、cleanup、not_completed，不能用一项通过覆盖其他未查项。
普通工程验收5—10分钟为软目标。记录四阶段耗时，不因超时强判失败；及时报告阻塞，拒绝无边界读取与临时开发校验器。

## 5. 终审后必须删除
责任人Astra。终审PASS或CHANGES_REQUIRED后，先永久归档结论与证据身份并回读，再核review HEAD未被无关写入改变，以普通non-force提交删除本任务当前tree白名单文件并回读缺失。验收PENDING时不得先删；不扩大删除范围，不改写历史，不替Codex重新推送。
没有候选记NOT_APPLICABLE_NO_CANDIDATE。清理失败记TEMP_CLEANUP_PENDING。operations_closed可表示退修终审及清理结束，不代表acceptance_pass；只有必需验收、交付核验、归档回读、清理均满足才允许完整成功。删除当前tree不抹除历史，所以发布前脱敏不能省略。

## 6. 同步
GitHub治理、本地Codex入口、Project Sources三个平面独立核验。签发后附单一代码框启动Prompt；它只导航固定合同，不重组正文。此次规则落实与DOC_ONLY同步不授权HTTP代码修复、旧491成员ZIP读取、分类器重跑或任何科学运行。


## 2026-10-21 · Owner重申自动GitHub临时ZIP交付与审阅取证分账（明确执行口径）

- **Codex执行交付是硬要求**：每张已授权可公开证据的长任务都必须在合同/参数/启动Prompt中明写固定 `REVIEW_BRANCH`、`FIXED_PARENT`、`TEMP_PATH`，并由Codex自动上传该**GitHub独立review分支临时目录**的三份原件 `result.md`、`manifest.json`、`evidence_sanitized.zip`。候选commit/tree/三文件Git Blob、大小/哈希和远端完整字节回读必须提供；只打印本地路径不算发布完成。违反安全/权限/限额时如实STOP，不能绕过门禁。旧独立review树不许因新单被清理。
- **交付与独立验证是不同状态**：Codex已完成GitHub自动上传、远端commit与原字节自检，不等于Astra在其独立运行环境完成ZIP全部成员SHA/CRC语义/隐私检查；反过来，Astra无法从连接器Base64把ZIP送进标准库，只能记`REVIEW_PENDING_IO`，**不能误写成Codex没有上传**、要求Codex重复推送或扩建发布器。
- Astra优先按固定commit/path直接从GitHub原字节受支持通道验收；工具不能提供可运行标准库的完整原字节时，保留既有remote候选并暂停清理。仅作为**经Owner自愿选择的例外兜底**，可由Owner把同一候选ZIP原件上传到会话，必须先核其Git原生blob身份后再复算。不能把Owner手动中转改成常态工作流，不能要求为纯取证障碍重跑Codex或重签任务。
- 终审PASS或CHANGES_REQUIRED归档回读后仅用普通non-force精确删除当前review分支当前树三文件、逐文件404及diff回读；Git历史不会被删除，因此脱敏门仍是发行前硬门。PENDING时不删。
