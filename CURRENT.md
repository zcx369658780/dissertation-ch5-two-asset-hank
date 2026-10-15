# 第五章 CURRENT：V009正确停于未取得稳态；V010自动开启只读失败机理取证

日期：2026-10-15（Asia/Shanghai）
**最新状态：`V010_OWNER_CONTINUATION_DRAFT__WAIT_CODEX_V009_NEWTON_TRIAL_AND_ZERO_PRIVATE_CAPITAL_FORENSIC__ZERO_SCIENCE_CALLS`。**
**V009终裁：`CLOSED__LIMITED_ACCEPT__V009_PHI_B_CODE_AND_REPORTED_SCIENCE_STOP_ONLY__NO_SYNTHETIC_HANK_STEADY_STATE__WITH_OBSERVATIONS`。**

Owner采纳φ人均GDP方案B，补充合同及原V009冻结仍有效；新代码候选 [`e25f8e22490dddf57568e14aec2819d52603a78f`](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/e25f8e22490dddf57568e14aec2819d52603a78f)，tree `4b161428470e4bc8070ed4ec4010a0ea08f9695a`，唯一parent `d41d229b681e09b913c21deff7a057085b9bc419`，仅13白名单新增，未main merge。Astra独立读GitHub候选源码/测试及PRE_SEAL机器摘要，确认HJB/KFE算法、有限差分宏观Newton、φ固定外生逻辑与本轮STOP路径，正式[ V009有限科学验收](versions/0.0.9/acceptance.md) / [复盘](versions/0.0.9/retrospective.md)。

**科学结果不是完整HANK稳态**：Codex本地回执报告5个价格点household HJB同checkpoint最大B约3.373e−11、D约3.372e−8且终端KFE唯一34状态闭类/rank33/nullity1/最大stationarity1.388e−16，然而`At=0`而private资本非退化失败，初始宏观5项残差显著非零。第六次宏观eval在flat179(b上界=2,a=2.1053,z=.8)遇`NO_ADMISSIBLE_POLICY`，该评估按GitHub代码顺序是初始点+4有限差分后的**首个未被接受的完整Newton试探**；用户报告当时HJB B69/D36、尚无KFE，无法认证整个经济无稳态。**由于1省φ=1，失败不反证两省富裕目的地φ=.9/反向1.1机制。**

V009代码工程/正确停点有限CLOSED，真正1省HANK稳态FALSE，2省NOT_RUN，动态IRF BLOCKED。Codex报告pytest7/8、science drivers2/4、1省宏观2/2耗尽（整体2/4）、household7/176、HJB55、policy/Q62、selector48783和root21222。所有终端五价点科学数值与保护属于`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，网页未访问D盘`FINAL_DELIVERY_PHI_B.json`或重跑；无GitHub CI PASS。旧版本任何余量不跨版本重开。

按[Owner连续版前立版指令](docs/CH5_OWNER_CONTINUOUS_VERSION_DIRECTIVE_20261015.md)已经**直接进入**[V010 DRAFT](versions/0.0.10/plan.md)：只读新V009合成证据，重点区分`a=0`的零私有资本吸收闭类机制与宏观Newton首个不可行试探不回溯；Codex不运行科学模型/真实数据或改代码。形成集中可信科学取证后，Astra决定是否需要Owner新算法/经济方程/科学预算许可。没有工作流变更。

原2018/C8 A–D真实文件仍REQUEST_ONLY、A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE。V0.0.11 NOT_STARTED，main/旧D盘8dirty/untracked/ignored/外部common-dir/B3不动。
