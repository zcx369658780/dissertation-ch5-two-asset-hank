# 发布器诊断修复：远端存在确认与回读实现定向终审

日期：2026-10-19。
任务：CH5_PUBLISHER_DIAGNOSTICS_AND_DELIVERY_REPAIR_20261019
修订：SECURITY_REVIEWED_20261019
run_id：f6466e1e2f674dc38c25a1614f15812e

## 1. 裁决与范围

TERMINAL_REVIEW=CHANGES_REQUIRED_REMOTE_READBACK_IMPLEMENTATION
ORIGINAL_CODEX_STATUS=DELIVERY_BLOCKED
REMOTE_CANDIDATE_PRESENCE=CONFIRMED
FULL_DELIVERY_ACCEPTANCE=NOT_GRANTED

这是针对已确认阻断问题作出的终审退修，不是全包通过，也不是要求Owner重传或Codex盲目重推。保留原回执DELIVERY_BLOCKED与UNKNOWN_INCOMPLETE；Astra补充远端存在和源码证据，不覆盖历史原件。当前任务停止、预算不延续，没有签发后继。

本轮没有重跑发布器、测试、fake-bare、SSH或push，没有运行模型。12组本地通过记录保留为历史证据，不被描述为Astra复跑。

## 2. 远端独立确认

实际读取指定review ref、候选commit及精确目录：
- review/ch5-publisher-diagnostics-20261019指向42ac4f1c76ece94e5ada633f66daa7efddc1512d。
- tree=1aead7b7ff2e4b8823b986218a5dad1f1074881c。
- 唯一parent=09b0986415dbfc85db0d28199194ad4f817cc292，与合同一致。
- commit diff只有_review_tmp/ch5/publisher-diagnostics-20261019/下三条新增文件。

GitHub目录/对象元数据：
|文件|GitHub字节数|Git Blob|
|---|---:|---|
|result.md|232|c62a915f2092022ecff86e511087431e6439f9d5|
|manifest.json|29718|e03cc5f48e5a38b42a13f9f106cae978e33a0678|
|evidence_sanitized.zip|60626|039b44f02a4fccaacbc4fb7a3a926f25f87f725f|

因此，本轮不是候选未上传。远端对象存在可以独立确认，但不能与完整字节/实现验收混为一谈。

## 3. 实际字节检查与明确未完成项

Owner提供的最终回执Base64经Python标准库解码、json解析及hashlib计算：2059字节，SHA256=00e3df31e90984b5b33e8b0f9220a2576a382a1c1380f2dd8c6a5ecf0b6d1d2b，Git Blob=7eee1a65cb8f082e24f33e5fbb14c48478cc417d，无重复JSON键；原字节归档于docs/evidence/publisher-f6466e1e/FINAL_RECEIPT.json。

远端result.md由Base64原字节独立计算：232字节，SHA256=f39b0eeb5a6a54950aed793d91665c081551eedaa3cc50187bf40c448faff84e，Git Blob匹配。

连接器取得ZIP Base64。Astra将选定前段传入标准库base64/zlib/struct，按ZIP本地文件头读取完整成员，核对长度、CRC与清单中的SHA256。用于本次定向源码终审的六份完整成员如下：
|成员|字节|独立SHA256|
|---|---:|---|
|src/ch5_evidence_publisher.py|35057|bc6a0af991d239b84ef543f46be2fec767a177a3cd2d78d4f3948a86ac624782|
|tests/test_publisher.py|5951|e2cd746d82066c5319d13a60fcb2e948b5c84d23de75943cf0080603089ed1cc|
|tests/helper.py|1112|98a0f9687b04fa317b11ff1fd1e7bc5550ee24a541bf073fbf2d6f87652ad68c|
|publisher_lock.json|1573|10273e6d25003b45f36dc332e1a95616616e36302c5b19dd48ae304e77a1bc7c|
|qualification/test_results.json|1306|7eeea80f71074c2256b4ff5297bacae82021659e296251c42ae386f0a0194772|
|qualification/fake-bare-proof.json|904|d29a6d4e50727ee1ed50148a46a4bd37862d6c34cf929009817b6811c314a530|

三份实现/测试源码与publisher_lock的sources哈希一致。test_results中12条记录均为PASS。fake-bare-proof记录三文件二进制核验、唯一parent和保留sentinel/history的清理；这份回执的原字节通过核对，其运行事实不是Astra重演。

重要限制：没有完成整个60626字节ZIP在分析环境中的独立SHA256复算，没有完成manifest原字节SHA256复算，也没有完成全部158项逐成员检查或全包隐私审核。manifest登记ZIP SHA256=a327fb8a2faee4f4c52863e32d04532a8f61321d50fba4b02a641229fafdcb8c，此值在本轮仅是远端清单声明，不得表述为Astra独立计算值。取得Base64响应不等于完成全部计算。定向终审已发现足以退修的源码问题，因此本裁决不授予整体交付PASS；其余检查记NOT_COMPLETED，不能升级为通过。

## 4. 已确认的实现问题及因果限制

依据上述35057字节最终源码（未执行）：

A. readback第517—534行先读取ref、commit，随后第524行附近调用：
entries = self._http('/git/trees/' + tree + '?recursive=1')['tree']
然后才按本次temp_path筛选。也就是说，为核验三份文件，先递归获取整个仓库根目录树。该范围过大是源码可直接确认的设计问题。代码也未检查GitHub tree响应的truncated标志。

B. _http第503—515行对响应调用response.read(16 * 1024 * 1024 + 1)，成功后才解析JSON。出现IncompleteRead时没有在这里持久化请求步骤、实际请求路径、响应状态/长度、已接收分段及完整/不完整状态。main第574—605行保存repr(exc)，保存异常文字不等于保存HTTP部分响应。这是HTTP诊断覆盖缺口，不是对已改进的子进程stdout/stderr留存的否定。

C. tests/test_publisher.py中T10调用本地selftest；selftest第416—456行从fake bare仓用Git cat-file/ls-tree取回数据，再调用共用_verify。12组测试和HTTP API响应接收并非同一覆盖范围，没有对真实readback传输层的截断/大响应/精确子树读取作相应模拟。故12/12与真实HTTP回读失败并不矛盾。

原回执记录IncompleteRead(2228224 bytes read)及IncompleteRead(12910592 bytes read)。这些现象与全仓库大响应路径相符，但回执没有明确失败请求URL和完整traceback；不能宣称已经证明唯一网络根因、GitHub故障或本机网络损坏。不能以stderr旧128的根因解释本次失败。

## 5. 后续最小修复方向（不是新执行授权）

只针对当前源码的HTTP读取/核验接口：通过固定commit的精确目录/三文件，或逐层非递归Git tree查询定位目标，避免root recursive=1；逐步验证目标文件Blob/bytes/SHA，保留对目录额外文件和父提交的核验。保留已验证的本地日志和fake-bare功能，不再重新设计分类器、HA或资源门禁。

在现有私有/公开分离机制内增加HTTP请求阶段、相对URL、状态、响应长度及有界partial bytes留存；中断标INCOMPLETE，不能把部分响应解析或报告为完整文件。只读重试必须固定同一候选/同一文件并遵守新的独立预算；已有候选不得盲目重推。

为该获取层补充小型合成HTTP响应测试（正常小目录、根树截断标志、传输IncompleteRead、逐文件哈希异常及ref已存在不重推）；是否重新运行具体旧测试由下一合同明确，不能追溯重开本轮预算。

## 6. 资源和其他边界

原回执工程74、交付22是保守启动预留（含一个模拟日志打开拒绝）；Python启动16和2。不能将96预留称为96个内核确认进程。独立内核累计UNKNOWN，不推断必然超额，也不当作0。

push_attempts=1、push_exit=0、push_reaped=true来自原回执；远端候选存在现有独立佐证。successes=0可保留为本地完整回读成功计数，不据此否定已经存在的GitHub对象。外部完成事件chunk_id=1e70c2、exit_code=0是Owner提供的工具事件摘要，未获得外部事件原件的独立认证。上一1495字节prior_receipt仅有身份，不重建其正文。

本次没有旧491成员ZIP读取，没有分类器/adapter/HA重跑。正式V010与HA黑箱不改；model_activation=False；REAL_GE=False；Results=FALSE；V011=NOT_STARTED；FULL_RUNNER_IO_CLOSURE=BLOCKED。

## 7. 终审归档后的清理

本裁决为终审退修而非PENDING验收，不宣称完整证据包已通过。按Owner强制规则，永久归档并回读本记录后，Astra须核对review HEAD仍为42ac4f1c76ece94e5ada633f66daa7efddc1512d，再以单一普通non-force commit删除指定temp_path下result.md、manifest.json、evidence_sanitized.zip三件；回读确认缺失。不得删除其他分支或改写历史。旧候选与源码证据仍保留在Git历史。

清理实际执行前：TEMP_CLEANUP_PENDING。清理完成不把本轮DELIVERY_BLOCKED改为PASS，不满足完整交付验收的字段仍保持未通过。ACTIVE_TASK=NONE；NEXT=WAIT_OWNER_NEXT_TASK。
