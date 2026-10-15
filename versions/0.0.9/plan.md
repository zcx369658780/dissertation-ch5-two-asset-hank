# V0.0.9 版前 DRAFT：从人工条件稳态走向真正两资产 corrected HANK 稳态与动态IRF闭合

日期：2026-10-15（Asia/Shanghai）
**状态：`OWNER_STARTED__V009_DRAFT__WAIT_CODEX_FULL_CORRECTED_HANK_STEADY_STATE_AND_DYNAMIC_CLOSURE_PROPOSAL__NO_SCIENCE_EXECUTION_OR_REAL_READ_AUTHORIZED`。**
**Authority：Owner已在2026-10-15授权继续研究与顺序进入后续版本；连续立版依据`docs/CH5_OWNER_CONTINUOUS_VERSION_DIRECTIVE_20261015.md`。当前只准`SOURCE_ONLY`集中科学/代码方案审查，不授权HJB/KFE/GE/IRF/真实原件或任何新模型执行。** 本DRAFT不是冻结计划。

## 1. 唯一科学目标与已取得基础

第一篇可投稿的中国多省份两资产HANK研究为目标，不再重复过去V006的carrier包装、V007的SOURCE_ONLY经济单位疑点汇总或V008的同类人工条件静态冲击实验。

V008由Astra独立核实并受限接受：新 CES 劳动—工资对偶/一次工资税/全国统一财政人工账、`reconciled_stationary.py`基于1/2/31个**人工省份**在**给定两资产和家庭离散分布**时求解n个工资及一个全国转移的条件均衡，数学经济残差最高约1.18e-12；单省四条条件冲击路径是外生AR(1)+每期静态块求解，共140期，可复算但`NOT_REAL_IRF`；动态Gate D准确`IRF_BLOCKED__NO_DYNAMIC_HANK_CLOSURE`。正式实现候选`d41d229b681e09b913c21deff7a057085b9bc419`、tree`88833acf90613380afa30ab8d6ee7e0297e98664`、唯一parent`d8bb49d86ea674ea4ff5e3fdf03929baa08a6514`，未合并`main`。V008原`pytest5/8、roots10/12、31省roots2/2、paths4/4`属**已关闭的V008科学/合成预算**，绝不自动转为V009额度。

V009目标是形成可实际进入**动态家户选择/资产分布/资本与债务出清**的独立corrected-model数值实施规格：
- 第一优先级：真正合成`(b,a,z)`两资产家庭最优化→stationary KFE概率分布→家户流动/非流动资产供应与私人/公共资本负债映射→双边劳动/工资与国民财政→完整**合成HANK稳态求解**，而非仅给定家庭财富与分布。
- 第二优先级：在完整稳态和经济动态方程已被独立审查后，构造正确的前瞻性动态转移/政策冲击IRF（至少一个严谨人工经济体的小规模验证），但本版尚无相应模型调用与科学成功承诺。不得为了图形把每期条件静态解充当IRF。
- 不自动把人工结果升级为历史2018数据、完整现实31省HANK/论文反事实/D3-D4/Results。

## 2. 版前Codex唯一科学集中提案

交付名：`V0.0.9_M2_FULL_CORRECTED_TWO_ASSET_HANK_STEADY_STATE_AND_DYNAMIC_CLOSURE_PROPOSAL`。
一次性SOURCE_ONLY只读核查：
1. 固定GitHub治理分支与V008已接受候选实际tree/parent/main、原D盘worktree、Git common-dir、8 tracked dirty和未跟踪资产的**已知保护历史**，不重扫untracked/ignored、不hash受保护科学产物、不checkout/merge；
2. 新`src/ch5_two_asset_hank/multi_province/reconciled_*.py`六个实现与相应测试；已接受`src/ch5_two_asset_hank/corrected_diagnostic`中的原HJB、policy/selector/derivatives、KFE unique-closed-class（及`src/ch5_two_asset_hank/hjb.py/kfe.py/steady_state.py`）作为**源码可复用性审查**，不能直接运行旧HJB/KFE/科学runner或改既有已接受法则；
3. 用户博士论文第五章和原MATLAB的必要预算、两资产调整、家户/资本/财政公式只作可能含bug的辅助文本；优先独立经济学推导与Owner已采纳corrected CES、税、统一政府、人口人均合同；
4. 建立一个**完整理论未知量/方程、边界与数值资格矩阵**：`u(c), labor CES eta/kappa`；b,a,KKT及转换成本、财产权与状态漂移；`z`生成与网格；资产收益`rah,rb`、债券发行人/借贷spread中介；`HJB(steady)`/policy/`Q.`/`KFE Q^T mu=0`及分布矩、地区资本与劳动、定价/markup或NKPC稳态、统一财政工具、资源约束与货币名义锚；省份资金份额`S[j,i]`与旧lagged回报语义；明确模型期和统计年，哪些能由已采纳科学合同提供，哪些**必须Owner新选择**；
5. 给出完整动态`backward HJB + forward KFE`、国民资本/公共资产/政府债券转移、企业定价/通胀、中央货币财政规则、初/末稳态、冲击生成与多期市场出清的最小**研究方法路线**；比较纯前瞻完美预见路径、sequence-space方法能否与两资产连续时间框架适配，明确可能的边界缺口，不能仅讲软件接口；
6. 设计第一项真正可完成的**V009实施长任务**：优先合成两资产HANK stationary end-to-end，若动态完整性与资源已证再建议本版后续数值门；给出≤适当文件数的精确代码白名单（新模块优先，旧科研代码若需科学修订必须另独立采纳）、算法/网格/oracles、极小1省→2省→31省先后风险与受界资源预算、失败终态、最终验收证据资格；不以任意新增大规模求解器调用替代审议。
7. 对`AtTax`的政府/中介/资源成本归属、`b`是否为政府债券、`clip/raw/used`、`sigma`费用去向、公共资本投资现金流、零/非零稳态通胀、折旧`0.0025 vs0.025`等未正式采纳项，列出至少一套**科学一致、明确标成`PROPOSED_OWNER_CHOICE`**的最小研究基线及替代方案；未选时保持UNKNOWN/BLOCKED，禁止自行改原C8科学合同。

## 3. 当前允许/禁止与版前上限

允许：已公开精确Git-tracked源码、科学历史接受、研究知识库与Owner直接提供的PDF/`.m`文本**只读**；本地项目QMD/Basic Memory如确实连通可做有界只读检索并说明来源，不能从网页记忆代替C8证据。最多90份精确源码/研究合同、累计代码文本≤4MiB、≤4小时SOURCE_ONLY调查；超额/无法核的只记录阻断。此版只读Git命令及已授权的非模型文档检索不构成科学实验预算。

**新增权限**：Codex收到任务后，应从固定GitHub治理HEAD只读核对`docs/CH5_OWNER_CONTINUOUS_VERSION_DIRECTIVE_20261015.md`、`docs/CH5_ASTRA_WORKFLOW_CURRENT.md`和`docs/knowledge/CH5_WEB_KNOWLEDGE_CURRENT.md`。对Owner要求“Codex同步文档”，允许在经核实非reparse的**独立新文档镜像**中保存只读下载/复制的上述三份新治理材料及CURRENT/版本登记，最多8MiB，逐文件记录Git blob和原内容摘要；**不覆盖原D盘8个tracked dirty、AGENTS.md、CURRENT.md、index或其他本地证据**，不写入未核QMD/Basic Memory。若无法安全建立镜像，`DOC_SYNC_BLOCKED`并报告，不阻止纯SOURCE_ONLY科学提案。没有从此获得GitHub额外push、原repo fetch/pull或真实数据权限。

禁止：新科研Python/import/pytest/MATLAB/HJB/KFE、科学root/路径/GE/IRF/生产消费者、任何真实2017/2018/C8 JSON/NPZ/MAT/CSV/receipts的stat/read/hash/parse、访问C盘B3、A16/G0/敌对实验、修改原模型/外部common-dir、原文件clean/reset/stash/checkout、发布新科学代码或push候选、升级冻结科学法则或恢复任何已耗预算；以上执行额度全0。原本地dirty内容/目录体积未经本轮核验继续UNKNOWN。

版本研究方法与证据分账：`SOURCE_ONLY`方案通过 ≠ household/HJB/KFE/资产市场执行资格 ≠ synthetic HANK steady ≠ real 31 province steady ≠ dynamic HANK IRF ≠ policy Results。

## 4. 唯一回报、Owner停点与下轮触发

Codex应一次性向Owner当前聊天回传：Git/科学基线身份、经济闭合方程表、现有HJB/KFE可复用性风险、完整合成HANK稳态实施建议、独立动态IRF方法/终端与预算、需要Owner真正决定的关键经济条款（集中最多3项）、Codex文档同步结果、实际调用/未证/0 science账。**不创建实现候选或自动运行实验。**

`WAIT_ASTRA_V009_FULL_HANK_SCIENTIFIC_CLOSURE_PROPOSAL_REVIEW / STOP`。

Astra将依据Owner本次**连续立版委托**在收到报告时主动集中审议；若只是此前已采纳经济法则与源码科学范畴，决定冻结计划并另行明确授权；若必须做新的重要经济制度/数据/科学调用预算/工作流变更，按长期停点向Owner一次性报告、等待明确选择。特别是**工作流本身**变更需先停止并让Codex按授权同步文档。没有任何条件允许自行跳过科学/保护门。`V0.0.10 NOT_STARTED`。
