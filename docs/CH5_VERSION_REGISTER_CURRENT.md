# 第五章版本登记（2026-10-16 V010工程集成已审、旧seal不可验证）

**VERSION=V010/V0.0.10；V011 NOT_STARTED；ACTIVE_TASK=NONE**。
**LAST_TASK=V010_ENGINEERING_INTEGRATION_SEAL_CHAIN_SYNTHETIC_MKTREE_PREFLIGHT__DELIVERED__STOPPED**。
**LATEST_REVIEW=PARTIAL__LEGACY_SEAL_UNVERIFIABLE__CURRENT_SYNTHETIC_INTEGRATION_17_OF_17_CODEX_REPORTED__CURRENT_SEAL_LOCAL_REPORTED**。
**REVIEW=[正式独立限域主审](../versions/0.0.10/engineering_integration_seal_chain_synthetic_mktree_local_only_primary_review_20261016.md)；REVIEW_BLOB=32272533e9f4136883f536814919bddf2cb037d9**。
**NEXT_GATE=WAIT_OWNER_FRESH_V010_SANITIZED_EVIDENCE_EXCHANGE_AND_REAL_ENGINEERING_GATE_AUTHORITY / STOP**。
**NEW_RUN_PERMISSION=NONE__PS0__BARE_INIT0__MKTREE0__GITHUB_FETCH_PUSH0__PYTHON0__RUNNER0__HA0**。
**FULL_RUNNER_IO_CLOSURE=BLOCKED；HA_SCIENCE_NOT_RUN；model_activation=False；Results FALSE**。

[固定冻结任务](../versions/0.0.10/engineering_integration_seal_chain_synthetic_mktree_task_20261016.md) issue Commit `34497613d7085cfeea39682aef15f983ef5030a9`、Blob `6aa223b4c98391e051ebe4f7b8d358f88cf678bf`已停止。Codex本机读取前一最终receipt哈希匹配，但旧first seal缺可还原原始字节、原run_id未记录，故`LEGACY_SEAL_CHAIN=UNVERIFIABLE`；不得根据现轮数据修补上轮20合成测试链。本轮另有新first/final原字节、同run_id、17项结果hash与单向链接（仅Codex本地回执级）；17/17本地集成报告预期匹配，合成mktree正例2精确tree entries、额外空行负例exit128，serializer自身DENY；不能宣称原GitHub发布链、真实runner或旧脱敏器已通过。上一原真实候选`PUBLICATION_DENIED`、原因UNKNOWN，历史原argv/源码中间台账偏差UNRESOLVED。

本轮Codex自报PS批次1/2、bare init1/1、Git身份4/6、hash-object2/2、mktree2/2、ls-tree1/1；前轮只读43,787B，新非Git8份68,551B，新bare全目录16条目/保守1,049,165B。wall、旧读文件数和其他Git meta count没有原始逐项证据可由Astra亲验。Owner提供新终版receipt SHA256 `859398F7F4ABF2067AAF6613213290B9F027EE48D2A7E0EEA361BC0C5FDF5197`，未实际取得字节复算。Python/runner/science/远端Git 0；所有旧/新余量STOP不结转。旧首次GBK超限及其它V010科学、Windows工程原账保留。

V010冻结科学plan Commit`bf091da33d59293f147d52c11580327d3ac2a85d`/Blob`85138d8859d53295262fe13bf5bc277bca95ed3f`及模型commit`94de4501dec051b969bee9d852eba2d4591f30ef`/Tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`不变。原MATLAB corrected HA/HJB/KFE→多省顺序→GovInv收益率边界×0.9/1.1与Zt→冻结GDP各省误差≤1%独立验证→原lagged-NKPC递推；目的地工资税只一次、same-S/前完整轮raw ra0、phi_max=.3、家庭人均/财政总量及三劳动账不变；原两省F-order25 NO_ADMISSIBLE_POLICY，corrected单点rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07仍UNTESTED。Owner现有C盘物理独立SSD备份+GitHub双备份、SSH Key/443及可信工作站技术取舍不变；原8dirty/index/staged/untracked/ignored、外Git common-dir、所有旧失败原证、C盘备份、真实C8/2017/2018/B3不得越界。**A16 FAIL_CLOSED；window UNACCEPTED；C9 PAUSED；CALL_LEDGER UNRESOLVED；real C8 A–D REQUEST_ONLY；V011 NOT_STARTED**。
