# V0.0.8：多省份HANK劳动时序与财政会计的跨来源科学审订（版前DRAFT）

**Owner 于2026-10-15明确同意继续下一科研版本，允许必要时查历史项目记忆/接受文档、自己原MATLAB源码及博士论文第五章；同时特别指出原MATLAB程序本身包含错误，不得作为正确答案。**

**当前状态：`OWNER_STARTED__V008_DRAFT__WAIT_CODEX_CROSS_SOURCE_ECONOMIC_THEORY_PROPOSAL__NO_MODEL_CHANGE_OR_REAL_READ_AUTHORIZED`。本文件仅为版前DRAFT和一次SOURCE_ONLY集中提案许可，不是冻结科研方案、科学方程修改授权、真实C8资产读取、模型测试或Results许可。**

## 1. 唯一科学目标和权威层级

以**第一篇可投稿、经济学自洽的多省份两资产HANK论文**为目标，集中解决V007定位的`Lt_prev`/目的省`Lt_supply`、工资税`Lt*tau`、`AtTax`、`Tt`、人口/货币与时间归一化问题。新版本必须提出可以判真伪的理论方程与最小后续科学修订方案，**不是再写一版相同的SOURCE_ONLY清单或套壳synthetic类型合同**。

证据权威须严格区分：
1. 数学恒等、家庭/企业最优化、资源和政府预算共同计价、一般均衡定义等**独立经济学推导**（应给出假设、量纲和可证伪条件）；
2. Owner明确采纳的既有科学合同，对**原有accepted runs的历史资格**保持权威，但允许本版提出另立未来模型科学修订的理由，不能追改既有验收；
3. 博士论文原文：研究意图/写出的式子/时间和数据口径的文本证据，**可能存在错误或内部矛盾**，不能自动胜过经济恒等；
4. 用户原MATLAB ZIP：过去实现行为的辅助证据，**可能含旧科学bug**，不等于历史C8执行时该源码版本，更不因MATLAB/Python一致而正确；
5. 已接受Python代码：现行软件行为/已接收历史运行的可核证事实，**不自动提供经济理论正确性**；
6. 2026年早期来源合同、数值parity与过去研究笔记：只说明原接受范围，不可把`2009 MATLAB-Python parity`误认为2018/C8完整经济单位/财政正确性。

本版提出改法属于DESIGN_ONLY。实际改变HJB/KFE、Lt/工资/财政/资本、校准和Results都须后续独立经济学Owner采纳、正式冻结、分级实现及验证授权。

## 2. 已由Astra当前会话核读的源线索（仅供Codex复核）

**Owner上传博士论文PDF《基于异质性新凯恩斯模型的中国经济区域均衡协调发展研究》**，按PDF物理页数定位，打印页码比物理页码少20：
- PDF p94–95（论文页74–75），公式(5-1)–(5-3)：31省跨地区供给、家户效用/预算、来源/目的工资税与劳动厌恶。p95(5-2)书面预算没有明确`Tt`，而原MATLAB/Python家庭预算实际有`Tt`。
- PDF p96（论文页76），公式(5-11)明确目的省总劳动 `L_i^s=Σ_j L_{ji} N_j`，其中`L_{ji}`由原省份家庭分布积分定义；资产业务也乘`N`。这与`Lt_seperate.m`乘人口一致，说明家户均值与firm劳动总量需要同量纲桥。
- PDF p97（论文页77），公式(5-16)的`GovInc/GovExp`写法，与MATLAB/Python的`Govinc=Corptax+Lt*tau+AtTax+GovInv*ra-Tt`、Python的`GovSurplus=sum(Govinc-Bt*rb*N)`并不完全一致。需准确转录数学式及核算每一项经济含义，**不能假定论文就是正确的预算约束**。
- PDF p99（论文页79），表5-1折旧率记`0.0025`，而Owner上传的`multi_prov_HANK_12sts.m`源码`param.delta=0.025`；PDF p101（论文页81）同处文本既先说31省、又说26省。此类明显版本/编辑冲突只列风险、优先检查是否影响当前经济模型，不允许因此修改已接受参数。
- PDF p100–101（论文页80–81）5.2.6/5.2.7称初期劳动人口用常住人口代理、HJB输出为家庭/户均再按总人数放大，**与后续Owner已采纳的人口/人均且不N=P/3的决定必须明确区分**；原文不构成重新采用户均政策的授权。

**Owner上传原MATLAB ZIP《多省份HANK_matlab原版程序.zip》**已有静态对照：
- `HANK_2ASSETS_HJB.m` L347/L397以概率密度积分产生`results.Lt`，`Tt`进入家户预算；
- `Lt_seperate.m` L6–15先求source→destination个人劳动再乘来源人口`N_i`；
- `HANK_mp_1turn.m` L14–26先家庭/迁移，再L44–46调用firm；
- `HANK_firm.m` L9读当前`Lt_supply`，L20–21读旧`Kt/Lt`，L35含`(Lt_1-Lt)/Lt`，L95为`Govinc`公式；
- `multi_prov_HANK_12sts.m` L69 `param.delta=0.025`、L81 GDP/人口缩放`1000/100`。
这些仅是当前上传ZIP源码事实，并非原历史C8实际运行字节。Codex可在合法可用范围内核读，不开放ZIP中任何`.mat`、真实C8 reports或无界文件查找。

**V007已接收Python证据**：`k1b_turn5_turn6_bounded_continuation/run.py` L289–295把保存的旧firm `Lt_prev`覆盖成当次household `Lt`，现`Lt`是migration destination supply；`firm.py`使用该量进入`mt`和后续工资/收益；`Tt`由household预算直接加并在firm地区财政直接减；`AtTax`为家户资产收益差均值。证据见固定 [V007候选经济来源报告](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/d8bb49d86ea674ea4ff5e3fdf03929baa08a6514/versions/0.0.7/provenance_unit_evidence.md)；其经济unit status未证，不自动判为已在现实数值运行中产生BUG。

## 3. Codex本轮单次SOURCE_ONLY集中科研调查授权

任务名：`V0.0.8_M1_LABOR_FISCAL_MODEL_CROSS_SOURCE_SCIENTIFIC_RECONCILIATION_PROPOSAL`。

允许按需只读：
- GitHub当前治理/科学采纳/历史接受/代码的精确SHA；先核`CURRENT.md`、`SCIENTIFIC_DECISIONS.md`、`CH5_WORKFLOW_V1.2`、V007最终验收、V007固定候选以及本DRAFT；
- 本项目既有project-level研究知识库、Obsidian/Zotero/QMD（如果实际存在、合法连接且只读），以`Lt_prev/上期firm labor`、`2009 MATLAB-Python parity mapping`、人口/人均、`Govinc/AtTax/Tt`和原研究公理为精确查找键。先读有接受身份的直接文件，不扫描其他项目/本机全盘；个人聊天记忆只有确实可见且带原证的部分才引用，**无法访问则记UNKNOWN**；
- 用户提供的**上述一份博士论文PDF、一份原MATLAB ZIP**的明确文本页/成员，若在Codex当地已能合法准确定位；PDF允许非模型只读文本/页面抽取，ZIP仅浏览`.m`文本，不执行MATLAB、不解出`.mat`缓存、不运行脚本，不将全文/用户私有源码上传GitHub；
- 本仓已发布确切Git-tracked Python/MATLAB说明及校准/财政来源文本。原历史C8受保护JSON/NPZ/CSV/receipts及B3备份仍不可stat/read/hash/parse/extract。

建议本轮最多90份准确Git-tracked源码/接受文档、代码正文≤4MiB、版前静态审议总时长≤4小时；两个Owner上传文件若可得，分别只读单一PDF（原约11MiB，封顶16MiB）和单一ZIP（原约1.6MiB，封顶3MiB），不计入代码正文配额但记录实际可得字节。PDF/ZIP不可达时先使用Astra当前已审线索提出未认证问题，明确`NOT_IN_CODEX_VIEW`，不要假装已亲自读。无界索引/危险路径遍历禁止。

**本轮禁止**任何科研Python/import/pytest/模型/MATLAB执行、HJB/KFE/31省consumer/旧tests、真实原件访问、代码/报告文件写入、Git commit/push/checkout/reset/clean/stash/pull、科学参数/经济式更改、Excel/.mat派生缓存研究或Windows A16/G0/B3实验。必要合法的只读PDF文本提取工具不属于科学模型调用；产生的临时工具副作用须在无保护安全临时区、可控且记账，不进入原repo/outputs。资源/工具不可证即限于已可读文本。

## 4. 必须独立推导与对照的科学问题

**L——劳动状态/时序/省份和归一化**：
- 定义省i来源家户`l_{ji}(a,b,z,t)`、质量均值`L^h_i=\int z\sum_j l_{ji}g_i`与目的j有效劳动`L^s_j=\sum_i N_i \int z l_{ji}g_i`。请验证源代码aggregate household Lt是否事实上等于这个`Σ_j`（原历史旧HJB可能仅有一维`l`，这是独立缺口，不能默认成立）。
- 指出`Lt_prev`究竟应该是经济期t−1的同一目的j firm supply、外层固定点迭代k−1的同一firm supply、还是当轮来源家户均值；分析原firm/NKPC表达为何要求时序/省份/单位同时一致；为至少两种理论自洽解释提供推导及可证伪的共同尺度条件。
- 分开定值`N`=现实人口代理、工作参与率、单位效率劳动、迁移目的矩阵与统计常住人口的角色；`N=P/3`已被Owner否决，不重新采用。严格区分零通胀/无迁移/等人口退化情形会遮蔽差异。
- 审核上一阶段历史`Lt_prev`映射修复/2009数值parity的**具体accepted范围**，不把MATLAB-Python数值一致等同于经济正确或当期C8模型版本。

**F——财政闭合、税基及货币同量纲**：
- 按每省家庭预算（含`Tt`和净工资）、企业利润/资本所得、金融资产和政府债务/国有资本出发，**独立推导**财政总量恒等式、工资税基`w^gross\times L^s\times \tau`是否含迁移楔子、AtTax为何可作为真实政府收入、`Tt`是否按人口支付及财政期的债务利息。区分`source-faithful`与`economic-consistent`，不能先假定应该怎样补N或乘w，必须列条件和记账定义。
- 同时核论文(5-2)、(5-11)、(5-16)，原MATLAB`HANK_firm.m`、`HANK_mp_1turn.m`以及Python`firm.py/fiscal_diagnostics.py`的**准确不同项**，判定哪些是论文漏项、实现变更或尚未解释的会计规则，给出最多三条完整备选理论规格及必要的Owner科学选择，不自动推广。
- 保持`AtTax=At*rah-sum(a*effective_r_a*p)`的历史数值公式和`raw_ra0`同S lagged不变，设计若未来经济学改造政府税/资产规模是新模型契约而非偷偷修改原聚合。

**D——定义/参数/经济期/科研成果条件**：
- 每人资产`[At]=MU/NU`与`At*N`，劳动总量、工资单位、`Tt`、`Bt*rb*N`必须同样验算；分析FOC效用系数如何与货币数值缩放共变。
- 论文表5-1 `delta=0.0025` vs ZIP`0.025`及当前Python、26 vs31、多年数据真实年份的冲突仅按范围与科学影响分级。禁止以旧MATLAB/论文字面数字覆盖既有接受校准。
- 年度`q`（observed2017/target2018）是历史回溯偏好系数；模型期`raw_ra0`和资本/财政收益不得年化，价格`current_price_methodologically_attributed`但`direct_price_verified=False`、`price_verified=False`、release UNKNOWN、baseyear None。
- 无需修改Option1固定C8 household/states/S/N/params/distance、HJB/KFE、C1、源忠实migration、origin/destination税索引、外层R2九分量停止历史结论；但可提出**未来单独的corrected-model研究支线**与旧 source-faithful branch的可复现比较路径，实施许可为0。

## 5. 唯一交付与后继独立门

向Owner当轮Codex会话交付**一次集中纯文本报告**，名称严格：
`V0.0.8_M1_LABOR_FISCAL_MODEL_CROSS_SOURCE_SCIENTIFIC_RECONCILIATION_PROPOSAL`。

报告需回答：
1. 完整项目Git身份、当前dirty保护、拟议下一代码基线以及历史C8与V006/V007真实提交的区分；
2. 博士论文/原MATLAB/已接受Python/过去memory与科学采纳文件**五源证据冲突表**，每一条都标明实际已读原文、精确公式页码/函数行号、证据强度与不可作的推论；
3. 劳动的来源/目的省、t−1 vs k−1、家庭均值到地区总量的数学推导及至少两套候选规范，逐项反例与可证伪标准；
4. 政府预算、工资税/AtTax/Tt、国有资本、利息、人口货币的完整恒等式与最多三套规范，可识别假设/不可识别部分/与已采纳科学合同的冲突；
5. 哪些**文本中可确证错误**，哪些只是经济期/numeraire/福利和人口口径未知，哪些真的必须由Owner选择新方程；不因为旧论文/代码一致就宣布正确；
6. 一份**实质修订优先**的V008正式长任务实施路线与验收oracle建议，明确安全的零科学可证验证优先、后续经济实验/真实资产访问单独权限，允许路径与资源建议；
7. 只列Owner真正必须裁决的1–3个科研选择（如果证据不足则说明等待哪个具体原件/定义）；不会请求重新采纳人口/人均、原Option1和已采纳K1/C1法则；
8. SOURCE_ONLY实际阅读/本地记忆检索/文本处理资源、失败与0受保护数据/0模型执行账。

V008版前终态：
`WAIT_ASTRA_V008_CROSS_SOURCE_SCIENTIFIC_REVIEW__NO_IMPLEMENTATION_AUTHORIZED / STOP`。

Astra审议后才正式冻结V008、独立签发可实施范围；实质科学方程修订需Owner特别采纳。真实C8 A–D仍REQUEST_ONLY（首A manifest自身文件大小UNKNOWN），A16 UNRESOLVED/FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、旧science/data/consumer预算CLOSED。V0.0.9 NOT_STARTED。
