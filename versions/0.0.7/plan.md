# V0.0.7 M1 正式冻结：原C8历史证据锚与经济量纲/财政公式科学核查

冻结日期：2026-10-15（Asia/Shanghai）。
**版本状态：FROZEN__WAIT_CODEX_SOURCE_ONLY_UNIT_RECONCILIATION__REAL_READ_REQUEST_ONLY。**
**权限：本计划本身不是实施授权；Astra在GitHub回读后须另行明确签发限于SOURCE_ONLY文档/科研单位审查的授权。全部真实/受保护原件访问、哈希/解析、真实消费者/模型/科学测试仍0许可。**

## 0. 原Owner立版及版前审议

Owner在2026-10-14正式启动 V0.0.7；原版前DRAFT见历史commit `d21df7b8d785f36163d2ae2457c6fb6ffb163322`，plan blob `349e5c3af571e7a32875e3be50d2dd13f173e580`。Codex一次集中完成 `V0.0.7_M1_ORIGINAL_C8_PROVENANCE_UNIT_BRIDGE_AND_PROTECTED_READ_GATE_CONSOLIDATED_PROPOSAL`，报告通过Owner提供的当前会话文本交付，无新候选/真实读取/代码修改、SOURCE_ONLY计数属于CODEX_REPORTED。Astra独立读取GitHub历史 C8 报告、独立接受、commit/git-tree及Python经济式，并只读比对Owner提供的原MATLAB ZIP的相关文本（**上传的原版ZIP不等于历史C8执行代码认证；不上传ZIP或复制其原文到公开仓库**）。

**本版重点不同于V0.0.6**：不再做合成输入包装/测试；已发现可独立审查的原C8历史信任锚，并定位 `Lt_prev`、财政 `Govinc`、`AtTax` 与人口/劳动/货币尺度可能不相容的实质经济学疑点。优先获得可供Owner作科学采纳或证伪的逐式证据，不为多一个文档PASS重复SOURCE_ONLY冗余工作。

## 1. 已独立核实的历史证据及适用范围

- 历史 C8 runner 审核候选 `7b81628a8c54088117878c666995c665935a9617`；dispatch `7c88960f16ce0b7dd42bbb99b882334731895749`；独立接受执行候选 `63ac1ae972fe7f54dc59d2ed58764955088c57ce`。后两者Git root tree不同，但均包含同一个 `src` tree `00682b2e1a7ba23665f6e16f6acf48ad35874883`。
- 历史接受文档 `docs/CH5_K1B_TURN8_OUTER_R2_EXECUTION_INDEPENDENT_REVIEW_20260925.md` 及对应执行报告的 `HISTORICALLY_ACCEPTED` 限度：C8 manifest SHA256 `5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`；当时完整回读5,141成员，manifest自身第5,142个文件，成员总大小63,801,638 B（**非manifest文件长度**）；31省 terminal、31组 KFE mass和一次 integration；当时C8的39类attempted ledger已核；C6→C7 2/9、C7→C8 5/9，严格R2不满足，绝非固定点/GE/Results。此历史C8账本不能消除后续C9的CALL_LEDGER_UNRESOLVED。
- 原 entering-C8 JSON 固定历史 SHA256 `30EDAECEA59ABA03EFFD6C11530617BB7CF80FED175F58437F4DACA9E96D2F3A`；NPZ `E6B5D428C1070C6F9F6D9C450F7CDB0D4C2C54F0658074C9C75E60E8FDB743DB`。当前磁盘存在性/字节、省级五字段、原live batch identity、真实劳动/资本单位继续UNKNOWN。
- SOURCE_ONLY: `validators/multi_province/k1b_turn8_outer_r2/run.py` (load_bundle和C8专属caller)、`optionb_turn2_household_integration.py` (terminal writer)、`corrected_household_adapter.py` (原聚合)、`k1b_turn5_turn6_bounded_continuation/run.py` (五字段batch及S/C1/firm/wage)的历史对应关系有静态源码证据；历史关键源码blob与V0.0.6候选相同，**整棵src并非相同**，不能以当前代码替代原执行现场。

## 2. NEXT_BASELINE_ADOPTION及科研资产保护

**ADOPTED_FOR_V007_SOURCE_ONLY_DOC_CANDIDATE**：上版正式接受候选 `198b70f8b1c7b802bc2e18cb4bb0825bdb495b00`，Git tree `0c637893d92cafdf72a194b350b3bf7016894d5c`，单父 `cf74384f151427f0b7071ac0461cede6ad6cdf11`。原D盘模型树 `D:\ProjectTemp\c5k1bturn56`、HEAD `a1db8c114dec0ab69d69a5576e153a7f868cba0e`，据Codex只读Git关系相较V006候选0 left-only/4 right-only；但本地8 tracked dirty/旧unstaged资产、5,948 untracked和4,553 ignored及外置Git common-dir不可被覆盖。此次Codex只确认dirty路径/类型与staged=0，**未做dirty字节/hash和全index独立保护验证**，相关强保证仍UNKNOWN。旧 `main=dd90f41e0daa97cf55fcb2a7a233ee8cd64297ac` 与模型候选不同，绝不自动merge main。
- 若实施需落盘，只能在新的受控isolated candidate_view/候选分支基于准确accepted SHA及tree做文档改动；不得对原树 checkout/reset/clean/stash/merge、修改历史8 dirty、reparse追随、访问B3快照、扫其他项目/删除文件。不得覆盖冻结版计划。

## 3. 本版本长任务真正必须得到的科学结果（无新科学计算）

A. **原 C8 来源资格最终静态 crosswalk**：以已核历史独立锚为起点，正文只列尚未闭合的 producer/version→entering C8 JSON/NPZ→31省 terminal/c8 batch五字段→S/参数/距离→真实消费者链条。按 `INDEPENDENT_GITHUB_CODE`、`HISTORICALLY_ACCEPTED`、`CURRENT_BYTE_UNKNOWN`、`PROTECTED_BLOCKED` 分账。不要重复Codex前述逐文件流水账或任何真实读取。

B. **从原MATLAB到已接受Python的符号经济单位与财政核查**，明确检验而非改写：
1. 已知数据换算：2018 GDP/资本亿元→`MU_10WAN_YUAN`（×1000），人口万人→`NU_100_PERSONS`（×100）。在条件单位下 `Y/N` 的一个模型单位为每100人10万元、即1000元/人；源统计人均 `q=10000 G/P` 元/人，代码映射 `q=1000 (Y/N)` 只是**条件代数**，不能认证真实C8 household `At,Ct,wjt`。
2. 分别审计 `At=sum(a*p)`、`Bt`、`Ct`、`Lt=sum(z*l*p)`、`AtTax=At*rah-sum(a*r_a_eff*p)` 的分布均值角色与单人/代表人口/地区总量单位；`wealth_i=At_i*N_i`、`S[j,i]`列守恒只保证数字与方向，必要条件 `[At]=MU/NU`；完整资本、收益、时间桥仍UNKNOWN。
3. **高优先级疑点 #1**：原MATLAB `HANK_2ASSETS_HJB.m` 写 `results.Lt` 为家户劳动聚合；`HANK_firm.m` 使用 `results.Lt` 作上一期劳动。Python `firm.py` 的 `Lt_prev` 取household `Lt`，firm当前 `Lt` 为migration `Lt_supply`，两者一个可能按人口前、一个已按人口后；须判断是否还有其他历史归一化、期状态覆盖或定标证据。给出 `(Lt_prev-Lt)/Lt` 的真实角色对照与纯符号条件反例。不能未证就定性已发生真实运行bug或自行乘N。
4. **高优先级疑点 #2**：原MATLAB `HANK_firm.m` 与Python `firm.py` 源忠实 `Govinc=Corptax+Lt*tau+AtTax+GovInv*ra-Tt`，而 `tau` 在家庭/迁移工资公式充当比例税率。明确 `Lt*tau` 为何能否与货币项同量纲，何处需要工资/劳动单位桥；`AtTax` 原均值为何/如何在此转为地区财政流，`Tt` 是否同样为每人转移。区分源忠实、经济闭合和可能的未来科学修订，仅提出可检验的不同解释、反例、文献/原证所需对象和Owner真正新裁决，不编辑财政式。
5. 2017 observed→2018 target仅历史回溯，模型一期不等于一年；年度 `q` 对比构造按来源减目的，不把年度 GDP当工资；保留Owner人口/人均，不得 `N=P/3`；`current_price_methodologically_attributed` 已采纳、`direct_price_verified=False`、`price_verified=False`、release UNKNOWN、baseyear None。原 `ra0` 每模型期，禁止擅自年化/改单位；未证 `phi_l,alphal` 与wage尺度不能自填解释。
6. 原MATLAB来源文本若从项目中可安全取得（Git-tracked或Owner已直接提供的文本），只读、准确定位 `HANK_firm.m`、`HANK_2ASSETS_HJB.m`、`Lt_seperate.m`、`wage_caculate.m`、`HANK_mp_1turn.m`、`load_GDPdata.m`、`multi_prov_HANK_12sts.m` 等的变量定义。会话中Owner上传的原MATLAB ZIP可作为辅助文本证据，**不是原C8 execution SHA成员**，不得外传、重写或把它追认为当时运行字节。无法访问就按局限交付，而非私自扩大protected读取。

C. **最小受保护真实文件许可建议（仅REQUEST_ONLY）**：历史已经独立接受，不为再次验证“曾经执行了C8”强行重复读取5141个文件。采用候选分期：A=C8 `execution_artifact_manifest.json` 一文件；B= `preflight.json`、`turn8/household_batch_receipt.json`、entering-C8 JSON与NPZ四文件；C=最多精确31个 `stationary_aggregate_receipt.json`；D=可选1个固定距离CSV。完整37文件申请上限的源假设不代表必要或已授权；31省真正数值只在经过A/B且确有需求时C阶段另签。
- **已纠正预算算术**（按照Codex原候选每文件上限，未签发）：A 1文件≤1,048,576B；A+B 5文件≤3,538,944B；A+B+C 36文件≤4,046,848B；A+B+C+D 37文件≤4,112,384B。原SOURCE_ONLY报告阶段累计 A+B、A+B+C 各少列65,536B NPZ；full总额正确。不得按错误中间限额执行。
- 5141成员manifest的**自身文件大小UNKNOWN**，不能把成员总大小当manifest大小；1MiB是待审上限，不是实测可用长度。未来单独Owner决策前须采用经过独立审议的元数据/大小门或明确可证明充足的新cap；若届时cap不足则STOP，不能分段偷读、重试或静默扩额。勿在本轮对真实资产stat/hash/读/解析。
- 对每文件分列existence/stat、read byte、single-buffer SHA256、parse JSON/NPZ、字段提取的不同权利及1次尝试/retry0；相关实际大小、原件路径祖先、reparse/权限、进程token、输入输出及LOCAL_ONLY生存期、完整A16/window是否适用该**单次被动读取**的具体操作合同由Owner与独立保护审议另行裁决。被动读取不等于A16四类敌对mutation PASS，亦不得暗自豁免未证保护；本冻结真实访问0。
- 已有V0.0.3初始run004北京三文件属不同历史对象，不叠加或混同C8；B3副本不自动替代原件。即使37文件全核，也不能直接证明经济量纲、真实consumer、R2/GE、Results。

## 4. 本版受限文件与工程权限（待独立签发）

在准确V006代码基线的隔离文档候选中，仅可新建：
- `versions/0.0.7/execution.md`：历史/代码核对与准确工作账，原证/保护全部 UNKNOWN分账。
- `versions/0.0.7/provenance_unit_evidence.md`：原历史信任锚、原创单位/财政科学分析、必要条件/替代解释、阶段A-D owner-read REQUEST_ONLY，以及需Owner决定的具体经济疑点。
- `versions/0.0.7/acceptance_summary.json`：机读候选资格、全部blocked、precise commit/tree预算/科学调用0与local-only说明。

原计划 `versions/0.0.7/plan.md` 固定，不为PASS修改；除此之外任何源文件、测试、历史科学run、治理索引、Python工程模块、真实source-loader或输出资产均不得在实施候选变更。公开报告不得包含受保护原数据、ZIP原始程序全文或可复用私有路径细目；敏感回执保留 LOCAL_ONLY。

## 5. 资源、前置、停点与独立验收

拟签发的 SOURCE_ONLY 单次长任务预算：至多4小时；准确read-only Git tracked/已公开来源文本≤60文件且累计≤2MiB（优先重用Codex已审查结果，不为凑额度再检）；文本校核无需科学运行，**Python/import/pytest/MATLAB/solver/真实callbacks/数值重算全部0**；非模型Git候选隔离临时操作/存储≤128MiB，LOCAL_ONLY脱敏回执≤8MiB，GitHub公开文档≤2MiB，新增总≤138MiB；真实/受保护数据的stat、read、hash、parse、字段抽取预算一律0；不可取资源遥测记UNKNOWN。仅允许所列3个新增文档/JSON，其精确所有权与候选root的非reparse/原dirty保护先确认，任何代码越界、原件/保护碰触即STOP。

Codex一次集中实施并完成准确候选tree封存、源hash、diff、远端普通non-force push/readback，原main不合并；无法安全建隔离候选则停止/LOCAL_ONLY回报而非修改原工作树；无合成测试任务，且不重复V006 40项。
Astra最后按范围独立验收固定Git文件，Codex本地Git/脏树保护回执分账；只可能得到 `HISTORICAL_SOURCE_CROSSWALK_DOCUMENTARY_ACCEPTED` 与 `ECONOMIC_UNIT_CRITICAL_OBLIGATIONS_ACCEPTED`，真实SOURCE_AUTHENTICATED、ECONOMIC_UNITS_VERIFIED、原C8加载、GE/Results仍不得设真。不为获得完整闭环的表面结果添加新 synthetic 包装或混合阶段。

旧科学硬停不变：Option1条件回溯（家户/states/S/N/参数/distance冻结）、HJB/KFE/(b,a,z) F-order、质量聚合、K1 raw-ra0/lagged/S、C1、来源/目的税的已采纳算法，R2 2/9、5/9 miss；`A16 UNRESOLVED/FAIL_CLOSED`、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、旧data/science/consumer budget CLOSED、D3-real/D4-real未授权。任何科学修订、真实原件许可或K1B/C9/GE只允许通过后续明确Owner决定和独立准入，不能由本工程候选隐式升级。

停止条件：`WAIT_ASTRA_V007_SOURCE_ONLY_ECONOMIC_EVIDENCE_ACCEPTANCE / STOP`；V0.0.8 NOT_STARTED。
