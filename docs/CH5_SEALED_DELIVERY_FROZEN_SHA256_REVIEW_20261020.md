# CH5封存交付任务 · 冻结SHA256身份缺陷终审

日期：2026-10-20；审查者：GPT/Astra科学顾问。范围：仅冻结参数、同一live治理状态、review ref，不读取根recursive tree、不重跑代码或测试。

## 任务及原始事实

- TASK_ID：CH5_PUBLISHER_HTTP_FIX_SEALED_DELIVERY_ONLY_20261020
- Codex run_id：ddecec03fe034fcf877f9a896761fdab
- 原Codex终态：DELIVERY_BLOCKED；实际阶段FROZEN_SOURCE_IDENTITY_GATE
- 外部完成事件：Owner提供chunk_id=42e699、exit_code=0；仅表示回执封存，不是执行/交付成功
- Owner提供最终回执声明：2532 bytes、SHA256 7746633dab8a62444c29e9df747d801e4e174412087e55efd234b412736b7997；本终审未独立复算该Base64整段原字节，不宣称已认证该回执SHA
- 任务发行提交34f454337fc808241bf8bf7a119bc5f1571b2e39；固定issue commit 45f80d8ec78d22c289fa2b15e7a75325f3794942
- frozen contract blob 0842e1d687dd7ed5964a71c8fcda73ef8074b71d；frozen parameters blob f48e5034717b225e3ca015ce2f3ed1340be73c0d
- 2026-10-20本轮读取治理分支live HEAD仍为发行commit，CURRENT/TASK_CURRENT明确本任务唯一ACTIVE，ISSUE_MANIFEST固定issue commit一致。
- 对review/ch5-publisher-http-fix-sealed-delivery-20261020进行精确ref GET：404 Not Found。未见远端候选。

## 可独立确认的明确发行缺陷

读取固定发行HEAD下tasks/CH5_PUBLISHER_HTTP_FIX_SEALED_DELIVERY_ONLY_20261020/TASK_PARAMETERS.json并用JSON解析后检查sealed_files：
1. result.md，长度声明611 bytes，sha256字段为63个十六进制字符，非64；
2. manifest.json，长度声明4564 bytes，sha256字段为63个十六进制字符，非64；
3. evidence_sanitized.zip，长度声明38378 bytes，sha256字段为63个十六进制字符，非64。

已独立验证三条SHA长度均为63且不能匹配正则^[0-9a-f]{64}$。故合同中的冻结原字节认证根本无法执行。根因归属：Planner/任务发行元数据质量门漏检；**不是Codex实现缺陷、不是GitHub 403、也不是封存ZIP本身出错的证据**。不能猜测缺失的十六进制字符，也不修改历史合同。

## 分层终审

MAIN_REVIEW=CHANGES_REQUIRED_INVALID_FROZEN_SHA256_ISSUANCE
CODEX_ORIGINAL_TERMINAL=DELIVERY_BLOCKED
ISSUANCE_DEFECT_OWNER=PLANNER
CODEX_GUARD_RESPONSE=APPROPRIATE_HARD_STOP_SELF_REPORTED
artifact_integrity=NOT_COMPLETED_SOURCE_BYTES_NOT_READ
implementation_review=NOT_COMPLETED_NO_NEW_IMPLEMENTATION_TASK
privacy_review=NOT_COMPLETED_PACKAGE_NOT_READ
delivery=NOT_STARTED_IDENTITY_GATE
cleanup=NOT_APPLICABLE_NO_CANDIDATE
not_completed=BOOTSTRAP_0_1_2;SEALED_THREE_BYTES;ZIP_14_MEMBERS;PRIVACY;DELIVERY_ENVELOPES;HTTP_PREFLIGHT;SSH_FETCH_PUSH;REMOTE_BYTES_REVIEW

Codex报告：sealed_files read=0，scratch未创建，HTTP preflight未执行，SSH/fetch/push全部0，代码修改/测试重跑/科学调用全部0；先出现本机CreateProcess OS error 206（命令行过长）并缩短只读调用修复，这个E1不构成封存身份失败原因。本轮未独立观察Codex本机进程和保护路径，OS kernel UNKNOWN不能当0。

### 时间记录
fetch_seconds=UNKNOWN；integrity_seconds=UNKNOWN；semantic_seconds=UNKNOWN；archive_cleanup_seconds=UNKNOWN。此次无需整包下载或后续语义重审即可据确定性不合法来源合同退修。

## 后续原则
- 此错误任务CLOSED，不重置/续用旧预算；不要求Codex重跑此冻结合同或重推任何候选。
- 需要新的、明确签发的修订/新任务：先从信任的本地封存三份原字节独立计算完整64位SHA256、校对长度/ZIP清单/隐私，再把**实际正确的完整哈希**冻结到新合同；发行前机器检查所有哈希长度、格式、bytes、任务路径与manifest一致。不可凭63位前缀猜补最后一位。
- 重新签发前保持WAIT_OWNER_CORRECTED_SOURCE_IDENTITY_AUTHORIZATION；新的交付任务须另有正常的远端/保护/资源预算。不因Planner失误对Codex计一次实现失败。
- HA历史黑箱，正式V010/v0.0.10；model_activation=False；REAL_GE=False；Results=FALSE；V011=NOT_STARTED；FULL_RUNNER_IO_CLOSURE=BLOCKED。
