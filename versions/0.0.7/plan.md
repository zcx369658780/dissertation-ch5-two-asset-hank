# V0.0.7 M1：真实C8历史证据、经济量纲与受保护来源准入闭环（版前DRAFT）

**2026-10-14（Asia/Shanghai），Owner已明确授权开始V0.0.7。**

**状态：`OWNER_STARTED__V007_DRAFT__WAIT_CODEX_CONSOLIDATED_SOURCE_ONLY_M1_EVIDENCE_PROPOSAL__NO_REAL_READ_OR_IMPLEMENTATION_AUTHORIZED`**

**注意：这是版前计划草案，不是科学/代码实施冻结、真实文件读取、数值或模型运行授权。** 先由Codex完成一份SOURCE_ONLY集中取证及正式实施方案，Astra独立审议后再冻结。冻结后工程许可与真实受保护原件读取许可分别签发；Owner这次授权“进入V0.0.7”不等于批准读取第37项文件或豁免Objective A。

## 1. 工作流及继承

继续 `CH5_WORKFLOW_V1.2`，不升级工作流、不增加审批角色/微任务/自动轮询。Owner负责重大经济和保护决策，Astra负责版前/冻结/单独授权与独立终验，Codex在允许的范围内自主完成一个长任务。草案调查无需反复逐命令审批，允许一次集中静态提案；正式科学或文件访问须按冻结合约审批。

V0.0.6已正式 `CLOSED__ACCEPT__SOURCE_ONLY_IMPLEMENTATION_AND_SYNTHETIC_ENGINEERING_ONLY__WITH_OBSERVATIONS`。固定代码候选 `198b70f8b1c7b802bc2e18cb4bb0825bdb495b00` / tree `0c637893d92cafdf72a194b350b3bf7016894d5c`；单父 `cf74384f151427f0b7071ac0461cede6ad6cdf11`，仅synthetic SOURCE_ONLY实现，不认证真实C8，未合并main。**本版代码基线暂定“建议继承V0.0.6已接受候选”，NEXT_BASELINE_ADOPTION仍为待Codex现行工作树/历史代码核查的PROPOSED，而非自动checkout/merge**。2026-10-14最新readback治理HEAD见 `CURRENT.md`，main当时为 `dd90f41e0daa97cf55fcb2a7a233ee8cd64297ac`，与治理分支和模型候选不同。

原模型worktree仍按本地上一轮回执为 `D:\ProjectTemp\c5k1bturn56`、旧HEAD `a1db8c114dec0ab69d69a5576e153a7f868cba0e`、外部Git common dir `D:\ResearchCode\dissertation-ch5-two-asset-hank\.git`。历史8个dirty tracked（含 `government_assets.py`、`middle_stage.py`）、5,948 untracked、4,553 ignored不得覆盖/清理/自动合并。C盘B3有限普通字节备份和V0.0.5有限关闭保持；不重启备份、A16敌对试验或G0微审计。

## 2. 唯一长版本科研目标

从V0.0.6已验证的**synthetic端到端合同**继续推进，不重复40项合成测试。重点是为首篇多省份两资产HANK投稿建立**原C8真实源证据可被独立识别、资产与劳动/人口量纲可审核、实际读取/认证权限可精确签发**的闭环路径。

集中覆盖三个相互连接的研究事实：

**A. 原C8身份/历史信任锚**。以已发表的接受文档及固定源码（不是私有原件）确认：C8实际执行的 runner/code版本、entering-C8 JSON states/参数/N/上一轮raw-ra0，frozen S、31省terminal aggregate和五字段 `mass_form`、writer/batch/checkpoint/stage/版本/摘要之间**哪里有受信锚、哪里只是历史locator**。确认C8完整九分量严格R2不通过而家户31省有限PASS的科学资格区别。不要把旧run004北京初始bootstrap、C8、C9归档或V0.0.6 synthetic carrier混成一个原件。

**B. 可审查的经济量纲表**。从原MATLAB科学源码、已接受Python聚合、2018输入/校准、政策/资本/劳动函数及既有文献证据逐符号构造单位和归一化检查：
- `Ct,Lt,At,Bt,AtTax` 的个人/模型质量权重及其量纲；
- `N`（原万人→`NU_100_PERSONS`）、2018地区GDP/资本（原亿元→`MU_10WAN_YUAN`）、`wealth_i = At_i * N_i`、`S[j,i]`、firm `Kt` 与 `GovInv=max(Ktarget-Kprivate,0)`；
- individual `l`、household `Lt=sum(z*l*p)`、迁移流/firm `Lt_supply`、生产 `Lt` 和 `Lt_prev`，区分人数、工时、效率劳动、代表性家庭质量；
- household/old firm/new firm工资、composite wage、`wjt`、来源税 `tau_i` vs 目的税 `tau_j`、`phi_l`、`alphal`、distance/migration wedge；
- 2017 observed→2018 target 仅历史回溯，2018原省GDP/人口属于不同作用；年度人口分母与资本的“模型一期” vs 历年统计期限；
- 价格只能记 `current_price_methodologically_attributed`，`direct_price_verified=False`、`price_verified=False`、release UNKNOWN、baseyear None；
- 对比代码换算与**经济认证**，未知处按UNKNOWN及条件等式列出所需证据，不因量纲标签、数值大小、README或旧回执声称已证。Owner已采纳人口/人均而非户均，不使用 `N=P/3`。

**C. 最小可签发的真实原证门**。复用V0.0.6 `execution.md` 的37文件/合计4,112,384B REQUEST_ONLY申请，以及V0.0.3北京历史三文件REQUEST_ONLY，但不简单合并或累加预算。先找独立历史信任锚/manifest绑定依据，再提出是否存在**更小的分阶段准入集合**（例如先manifest/输入bundle/批次摘要，后在可核锚基础上单一受限31省五字段集合），详细说明必要性与“读到会证明什么”；如果37项都有科学必要性，应解释独立原证对应。严格分列“可信锚确证”“文件存在性/字节哈希”“31省内容”“经济单位”“资产保护”“真实consumer”五个不同门。未获Owner实际数据/保护操作新授权前一项也不打开/解析/hash。

本版**预期有实质性可审查结论**：SOURCE_ONLY固定证据交叉表、经济量纲方程/UNKNOWN及证据缺口、真实输入分阶段精确准入/STOP设计；如经后续分别审批成功，才可能推进最小历史原证认证，而绝非C9或GE的复活。静态调查后由Astra审议冻结一个完整长任务，避免“再加一层只有声明的synthetic wrapper”。

## 3. 当前Codex可执行的版前工作（且仅此）

单份 concentrated `V0.0.7_M1_ORIGINAL_C8_PROVENANCE_UNIT_BRIDGE_AND_PROTECTED_READ_GATE_CONSOLIDATED_PROPOSAL`。

允许：
- 已公开的GitHub源码、历史采纳/来源/价格/人口/风险文档只读，以及本地**精确Git-tracked源/测试文本**的有界只读核查；
- `git rev-parse/log/show/diff/ls-tree/status --short` 只读，用于独立确认代码 ancestry/current dirty和V0.0.6候选是否可继承，避免无界status扫描或重算untracked/ignored；
- 合法的纯纸面维度/单位代数、合同和证据资格对照；
- 60份准确Git-tracked源码/测试文档、源码文本不超过2MiB、版前审阅约120分钟为上限，越界仅停止相关部分。已发布旧文档可以按需阅读，不为凑额度扩大调查。

禁止：Python/import/pytest/MATLAB/solver/consumer/actual source-loader、真实JSON/NPZ/MAT/CSV/受保护receipts的stat/读取/新哈希/解析、写入或创建任何候选文件/目录/commit/push、改变工作树/索引、访问B3/外部reparse目标、Windows A16攻击/备份或重新启动旧科学预算。原始公共代码中的旧真实数据路径只作 locator 记载，不作为访问许可。

具体SOURCE_ONLY审查：
1. 由历史接受/执行文档建立origin-C8 producer/version/checkpoint→31 terminals→五字段→S/参数的双向静态 crosswalk，标注SOURCE_ONLY、HISTORICALLY_ACCEPTED、UNKNOWN和BLOCKED。
2. 联合审查 household `At*N` 与MU/NU、工资税/来源—目的矩阵、资本/firm、日历/名义价格的完整dimension ledger，给出符号维度推导、冲突和可否闭合的明确判定。
3. 对37项REQUEST_ONLY先做一份精确表（不读取私有原件），提出最小首批与后续条件批次、每文件字段/字节/次数/零重试/允许操作、保护root/路径/输出生存期、独立锚、签发主体和A16/window前置，重点回答为何此访问不等于攻击性A16测试；若保护合同确实不足则提出可核的窄门，不宣称豁免。
4. 不把“计划有路径”写成“文件存在”，不把source静态一致写成“执行时原件确证”，不把完成读取写成真实consumer或模型认证。
5. 把V0.0.7实施时要做的文件改动、所需原件、测试类别（纯合成/metadata-only/真内容）、精确预算（真实独立给出）、验收与STOP一次集中提出。没有真实输入授权时应有可接受的最小文档/数量判定上限，不为获得PASS虚构事实。

## 4. 不可更改的科学法则与权限

原C8 Option1固定：已接受household outputs/entering states/S、N/params/distance， prospective只替换annual labor/wage系数，条件回溯对照不是完整新工资自洽GE。保留原 `(b,a,z)` 20×20×2 F-order、HJB `Delta=1000`/B,D门、唯一闭类KFE、质量聚合原式、K1 raw `ra0`/同S/lagged timing、`beta_distance=2`、`beta_return=0.5`、ddof0、C1残差、来源/目的税位置及原source-faithful labor。其他版本已经接受的科学定律也不重新裁决。

历史R2 2/9、5/9未过；`A16 UNRESOLVED/FAIL_CLOSED`、window UNACCEPTED、`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、`model_activation=False`、`Results FALSE`、旧数据与科学调用预算CLOSED，真实D3-real/D4-real未授权。

**本次Owner的V0.0.7启动决定不赋予真实37文件、北京三文件、C8/C9/K1B、GE、或任何受保护目录的新科学/读取预算。** 后续Owner实际授权必须逐对象/字段/次数/字节/操作/期限/安全条件明确签发，不能在静态提案中假定。

## 5. 唯一提案交付及停止

Codex一次直接向Owner交付，报告依次为：(i) Git代码基线与dirty保全、(ii) original-C8历史受信链及未证环节、(iii) 单位/资本/劳动/工资的维度证据矩阵、(iv) 37文件分阶段最小受保护申请与Owner独立决定、(v) 建议的完整V0.0.7正式实施长任务、资源/验收上限、(vi) 实际SOURCE_ONLY调用、读量、时间、零写入/零真实数据账。不要创建新GitHub文档/commit。没有足够证据的门逐项UNKNOWN，不能以新合成测试或保护试验替代。

终态：`WAIT_ASTRA_V007_CONSOLIDATED_M1_SCIENCE_AND_READ_GATE_REVIEW / STOP`。

完成后Astra集中审议、必要Owner重大保护裁决、一次正式冻结、分别独立实施/读取授权，然后Codex在冻结范围内实施，Astra集中验收。不自动启动V0.0.8。