# TASK_CURRENT：V010工程集成／旧封存链／合成mktree已交付、STOP

更新：2026-10-16（Asia/Shanghai）。
**ACTIVE_TASK=NONE**。
**LAST_TASK=V010_ENGINEERING_INTEGRATION_SEAL_CHAIN_SYNTHETIC_MKTREE_PREFLIGHT__DELIVERED__STOPPED**。
**REVIEW=[正式限域主审](versions/0.0.10/engineering_integration_seal_chain_synthetic_mktree_local_only_primary_review_20261016.md)；REVIEW_BLOB=32272533e9f4136883f536814919bddf2cb037d9**。
**CLASS=PARTIAL__LEGACY_SEAL_UNVERIFIABLE__NEW_SYNTHETIC_17_OF_17_CODEX_REPORTED__NEW_LOCAL_SEAL_CHAIN_REPORTED**。
**NEXT_GATE=WAIT_OWNER_FRESH_V010_SANITIZED_EVIDENCE_EXCHANGE_AND_REAL_ENGINEERING_GATE_AUTHORITY / STOP**。
**NEW_AUTHORITY=NONE__PS0__BARE_INIT0__GIT_IDENTITY0__MKTREE0__GIT_FETCH_PUSH0__PYTHON0__RUNNER0__HA0**。

上一[正式冻结任务](versions/0.0.10/engineering_integration_seal_chain_synthetic_mktree_task_20261016.md)发行Commit 34497613d7085cfeea39682aef15f983ef5030a9、任务Blob 6aa223b4c98391e051ebe4f7b8d358f88cf678bf，已交付 `V010_ENGINEERING_INTEGRATION_SEAL_CHAIN_SYNTHETIC_MKTREE_RESULT` 并停止。Codex本机报告旧最终receipt SHA256匹配，然而旧first seal只有结构化快照和hash引用，缺可核验的原字节，旧run_id亦未记录，所以旧封存链 **UNVERIFIABLE**；严禁新造旧原件或借新测试补造旧身份。新本轮实际first/final原字节、统一run_id、17个测试hash/单向链接据报成立，但网页Astra尚未实际读取本机原证，限`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`。

本轮本地集成17/17预期匹配（bare身份/结构化脱敏/匿名ledger），serializer自身拒绝额外空行，合成mktree正例2 entries、直接空行负例Git exit128；不能扩展成旧真实bare publish / GitHub / Windows Python / runner PASS。原真实扫描拒绝仍UNKNOWN且DENIED，历史台账偏差UNRESOLVED。

Codex自报PS测试批次1/2、bare init1/1、Git身份read-only4/6、hash-object2/2、mktree2/2、ls-tree1/1，旧文件读取43,787B、新非Git8份68,551B、bare保守1,049,165B/16条目；旧读取文件确切个数、wall及其它命令预算未知。最终receipt SHA256（Owner转述、未复算）：859398F7F4ABF2067AAF6613213290B9F027EE48D2A7E0EEA361BC0C5FDF5197。Python/VerifiedLoader/runner/模型科学与GitHub推送0。旧/本轮剩余全部随STOP关闭，不得结转；未来新工程、审阅发布及科学进程均须Owner新授权。本轮绝不触原冻结plan/模型、8dirty/index/common-dir/C备份、real C8，A16/window/C9/CALL_LEDGER、model_activation=False、Results FALSE、V011 NOT_STARTED照旧。