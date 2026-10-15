# 第五章 CURRENT：V010独立corrected HA单点科学诊断已获Owner授权并正式签发

日期：2026-10-15（Asia/Shanghai）。
**状态：V010_SINGLE_POINT_CORRECTED_HA_SCIENCE_TASK_ISSUED__WAIT_CODEX_ONE_ATTEMPT_RESULT**。

唯一当前有效任务：[V010 corrected HA 单点对照任务](versions/0.0.10/corrected_ha_price_probe_task_20261015.md)，任务ID`V010_CORRECTED_HA_SINGLE_PRICE_POINT_ONE_ATTEMPT`。**经Owner单独明确授权**，只允许固定代码候选`94de4501dec051b969bee9d852eba2d4591f30ef`/tree`205eab47c4e4f9c6292c2ead9947d94d1a7579a5`在隔离目录执行**新增1次**省级corrected HA科学尝试；不跑两省外层、响应或任何真实数据。

本次科学manifest `versions/0.0.10/corrected_ha_price_probe_v1.json` Blob `c23d331bed34e5ca478324cdc05034609ecb91b7`，科学freeze `corrected_ha_price_probe_freeze_20261015.md` Blob `24dd985c2497b5aebe5774af925b4c4b9e84be9e`，两者都固定于commit `81181490495f827aa0e15e6a6efb186e8addee67`、tree `846fd3f354d8f9d5d4978e15ad9ff78b71d2e451`。参数唯一`rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07`，其余完全来自原V010 manifest引用的`synthetic_fixture_v1.json`固定blob`40915658d93403cfc21b33a6b864b332b7857749`。实验不是两省GE或历史原MATLAB相同工资税口径复现；只有严格corrected HJB/KFE完成才能得到该点条件HA资格，失败如实STOP。

此前V010首个HA binding的`(.055,1.7085897434929322,.02)`报告checkpoint2 F25拒绝，12 candidate无可采纳；该失败原证SOURCE_ONLY已报告，与原code selector条件相容，根因未证明。历史成功价格集合`ra=.06/.0675/.07,w=13/15.5/18,rb=.02`是**MATLAB-faithful**旧算法（且部分KFE存在边界病态），不能自动当新算法PASS。 [交叉审议](versions/0.0.10/first_ha_price_domain_source_review_20261015.md)保留。

原V010冻结实施`plan.md`commit`bf091da33d59293f147d52c11580327d3ac2a85d`、blob`85138d8859d53295262fe13bf5bc277bca95ed3f`，旧两省fixture、原15路径代码候选及受保护工作树完全不改。以前Codex报告4/6 pytest、1/4 driver、1/26 HA、1626 selectors、1642 roots不被本授权重置；新增单点预算另列1/1不互借。

A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、真实C8 A–D REQUEST_ONLY、原8 dirty/index/common-dir及untracked/ignored保护、V011 NOT_STARTED、V1.2不变。新结果交回Astra独立验收，不自动启动下一试验。
