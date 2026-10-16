# V010 Stage A Git可达性：LOCAL_ONLY交付接收记录

日期：2026-10-16。性质：独立GitHub远端身份核验与Codex本地报告分账；不是本机原件独立验收。

**分类：CODEX_REPORTED_A_STAGE_OBJECT_REACHABILITY_VERIFIED__GITHUB_PUBLICATION_BLOCKED__INDEPENDENT_LOCAL_REVIEW_PENDING。**
**停点：WAIT_OWNER_SANITIZED_STAGE_A_FILES_FOR_INDEPENDENT_REVIEW / STOP。**

正式Stage A任务发行commit `68530b3f121952b4382d08dc9ff964c7f6c7ab75`，任务blob `3688674363aa8a0c45a7a322c9c2098baed62fae`，本轮已由Codex报告结束，不能重发或用旧预算继续。

## GitHub连接器实际核实

- 目标分支 `codex/ch5-v010-matlab-first-20261015` 仍指向commit `94de4501dec051b969bee9d852eba2d4591f30ef`。
- 该模型commit tree为 `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，唯一parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`。
- 冻结模型九份Python源码的**远端**Blob与正式任务列出的预期9/9一致。此结论不等于Windows本机磁盘raw bytes已获网页重算。
- 目标review分支 `review/v010-stage-a-model-ref-reachability-20261016` 查询404；Codex声明的本地候选 `d84cc76b19cbb81e097f502348b5073633fbda6e` 原始Git对象亦404。不得伪称GitHub交付成功。

## Codex本地报告（未独立验证）

Codex称一次正确模型branch clone、模型网络2/2、显式Git命令14条成功，九份源码实际磁盘Blob匹配，common-dir独立，Python/runner/科学调用0；Git工作区1,023,532,480B/2GiB，artifact 376,945B/16MiB，原受保护树与旧失败根未访问。据报告唯一一次push因认证不可用退出128后STOP，未重试；分类`LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED`。私有DELIVERY_RECEIPT.json的SHA-256由Owner提供：`56AD3D6F83782886D4E6E49FB0E37622B5E20EF8D94C739C62CF39B97D0`，**尚未读取原字节、未独立重算**。

当前ChatGPT没有读取Owner本机D盘的能力；对应脱敏MD/JSON未上传，故本地Git exit、磁盘哈希、common-dir、资源账、保护证据只属于`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，不认证`INDEPENDENT_LOCAL_STAGE_A_PASS`。

## 待审原件与安全边界

请Owner在对话上传：
1. `review_stage_a_model_ref_reachability_result_20261016.md`；
2. `review_stage_a_model_ref_reachability_manifest_20261016.json`。

私有DELIVERY_RECEIPT.json不要求未经脱敏原件；若审议还需可提供经确认的最小脱敏摘要。上传供审议**不是**授权补push或重新运行。

当前无可继续的ACTIVE执行任务；不得重试clone/fetch/push，不启动ENGINEERING_ONLY Windows runner B-E、不执行HA/HJB/KFE/selector/root/GE/IRF。完整runner I/O仍BLOCKED、单点corrected HA仍UNTESTED。原V010冻结科学合同及两次历史失败资源不变，A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、真实C8保护、原8dirty/index/common-dir、V011 NOT_STARTED继续有效。
