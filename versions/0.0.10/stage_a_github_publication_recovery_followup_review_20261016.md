# V010 Stage A：GitHub补推成功的Astra独立远端审议补遗

日期：2026-10-16（北京时间）。
**补充验收终态**：`STAGE_A_GITHUB_DELIVERY_VERIFIED__TWO_FILES_BYTE_IDENTICAL_TO_UPLOADED__DOCUMENTARY_LIMITED_ACCEPT_RETAINED`。
**覆盖范围**：仅更新GitHub review候选发布身份和两原件远端一致性；不推翻此前本地失败记录，不补认证Windows本机SSH443、进程、独立Git common-dir或源磁盘执行过程。
**原独立限域验收**：[stage_a_git_reachability_uploaded_primary_review_20261016.md](stage_a_git_reachability_uploaded_primary_review_20261016.md)（blob `6fdd38b2c12902d2c55e65c9ea5fa083833fcba2`），认定九源码远端哈希/大小独立复算9/9，结论 `STAGE_A_DOCUMENTARY_LIMITED_ACCEPT`。本补遗增补此前未到位的GitHub候选，不追改该时点的历史事实。

## 1. 真实GitHub Commit、Tree、sole parent及改动白名单

Astra通过GitHub connector现场读取：
- 目标ref `refs/heads/review/v010-stage-a-model-ref-reachability-20261016` 实际指向commit `d84cc76b19cbb81e097f502348b5073633fbda6e`；
- 原始commit `d84cc76b19cbb81e097f502348b5073633fbda6e` 的tree为 `5a03f952ba471352a685b327e79a33176e8bd7b6`，**唯一parent**是本轮Stage A任务发行commit `68530b3f121952b4382d08dc9ff964c7f6c7ab75`；
- 与发行commit compare：1 ahead，0 behind，恰好新增以下两份原任务白名单文件；没有其他tracked paths的添加、修改或删除：
  1. `versions/0.0.10/review_stage_a_model_ref_reachability_result_20261016.md`，Git blob `eb574370d367fc6f333b3dfc82e58e4bd1bf98a2`；
  2. `versions/0.0.10/review_stage_a_model_ref_reachability_manifest_20261016.json`，Git blob `12a7e2c9fb8dd63cc1e15445875ba2369ed5cbc9`。

固定候选Commit链接：https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/d84cc76b19cbb81e097f502348b5073633fbda6e 。

## 2. 两文件独立字节级复算及与此前上传物一致性

此前用户已在ChatGPT上传这两份脱敏源文件，Astra亲自计算其SHA256；本次又从**固定GitHub候选commit**实际fetch_file读取UTF-8原文，按UTF-8编码原始字节、使用独立SHA256实现（由`abc`及空串标准向量验证）再次计算，并与原上传字节哈希对照，结果：
- MD结果文件：**6190字节**，Git SHA1 blob `eb574370d367fc6f333b3dfc82e58e4bd1bf98a2`，SHA256 `A1DFCAA8FAEA7A1A257D119A54F2AFBA4911FDC705B5B589B08239316F5C26F8`；与此前上传文件**原字节等同（SHA256+长度一致）**。
- JSON manifest文件：**15107字节**，Git SHA1 blob `12a7e2c9fb8dd63cc1e15445875ba2369ed5cbc9`，SHA256 `C6593C9C1B1B0DD8FB84A52D3D93C242F01311F359A0F574E43FE9357CE66ABC`；与此前上传文件**原字节等同（SHA256+长度一致）**。
- 远端两文件UTF-8、仅LF无CR，满足每份发布大小限制；manifest九源记录此前已经与固定模型`94de4501dec051b969bee9d852eba2d4591f30ef`远端9份文件的全部SHA256、bytes复算一致，Stage A记录19个命令收据，其中前14条Stage A exit0；这些历史审议内容不因发布变化而被重写。

**结果：`GITHUB_REVIEW_DELIVERY=VERIFIED`、`LOCAL_ONLY_SAFE_PUBLICATION_BLOCKED=RESOLVED_BY_SEPARATE_PUBLICATION_RECOVERY`。** 先前首次push exit128保留为历史失败；新SSH443连接、服务器识别用户`zcx369658780`、全局Git配置未更改、这次push频次等均只有Codex的本地口述及其本地receipt可证明，网页GitHub最终对象本身不能反推认证方式、总push次数或原始本地环境配置。

## 3. 科学与工程资格和资源边界

Stage A已结束；在“冻结Git对象和上传/远端九源哈希证明、两文件GitHub一致性”范围给予 `STAGE_A_DOCUMENTARY_LIMITED_ACCEPT_WITH_GITHUB_DELIVERY`。**并未亲临Windows模型clone进行OS级独立鉴证**，也没有执行Python/AST/pytest/工程runner、HA/HJB/KFE、GE/IRF、真实C8；绝对不等于 `FULL_RUNNER_IO_CLOSURE=PASS` 或科学采纳。

Codex此前Stage A一次clone、模型网络2/2、显式Git14条全exit0、0Python/0HA以及最终资源账均属上传报告/本地回执证据等级；未重新运行或新造。原V010两次单点恢复各Python1/1、第一次存储超额、工程preflight checkout128、原8dirty/index/common-dir及旧失败回执保存不变。V010正式原计划blob`85138d8859d53295262fe13bf5bc277bca95ed3f`不追改；A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、真实C8 A–D REQUEST_ONLY、V011 NOT_STARTED。

下一步按Owner本轮“补上GitHub验收，然后继续”的指示，可以**另立一份独立ENGINEERING_ONLY Windows runner预检任务**，采用新的单独工程预算且零科学调用；这不来自旧阶段A/上次工程STOP任务未耗余额，也不允许跳过Windows audit argv、Job回收、hook来源和真正九源loader认证。此补遗本身不启动任何进程、HA或V011。
