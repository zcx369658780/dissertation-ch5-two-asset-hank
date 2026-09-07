# MP4C 省份价格边界与原自适应机制审计

2026-09-08，本地 bounded Builder；原算法和参数全部保留，D1–D3 target 暂缓。

**diagnostic_completion: PARTIAL_EVIDENCE**。本任务可用证据的提取、诊断、测试和报告已完成；失败路径未保存完整价格/控制器事件，不能补成完整轨迹。

**boundary_findings: OBSERVED_CONTACTS_AND_DERIVED_ANNUAL_RAW_EXCURSIONS**。
**high_rah_root_cause: SUPPORTED_LINK**，限定为安徽零外省投资权重下的滞后 ra→rah 传递关系；高价格造成不收敛的因果解释仍为 **NOT_ESTABLISHED**。

最重要的发现是：**原自适应机制执行过，不能归因为“完全没有调整”**。安徽第4轮降低国资，此后多次增加国资并调整 Zt；第22轮全国开关被贵州误差关闭，第23轮又发生调整，第24轮在安徽家户/KFE内异常退出，未进入本轮厂商和调整。安徽 call725 的 rah=.09 可追到第22轮厂商 ra=.09，但当时 ra0、mt 和本轮家户劳动未保存，不能确定原始超额收益率或完整厂商分解。

## 1. 当前 authority 与取证范围

- 实际工作目录：`D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001`。
- remote：`git@github.com:zcx369658780/dissertation-ch5-two-asset-hank.git`；启动工作区干净。
- fresh-fetch 有效 main：`c90bb26fb17f03dd9f45cea668d9e65a9ea22f43`；规则索引仍指定本 exact task。
- 分支：`codex/ch5-province-price-boundary-audit-20260908`。
- 正式任务：`tasks/CH5_MP4C_PROVINCE_PRICE_BOUNDARY_AND_ADAPTATION_AUDIT.md`。
- 有效证据根：`D:\ProjectTemp\ch5-province-price-boundary-audit-20260908-002`。

已读 AGENTS、索引、当前状态、任务、相关 workflow/safety/MATLAB/Python 规则、Reviewer 源码审阅及指定年度/失败报告。直接使用 D 盘保护根，没有假定 ChatGPT 附件路径存在，也未复制 zip。Reviewer 给出的7份相关保护 .m SHA256逐项一致；call725 运行的6个关键 Python blob 与当前文件一致。绑定 JSON SHA256 `A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6` 再次通过。未加载初始化 MAT 或家户 g/V 面板；沿用已认证初始化身份。

`source_map.json` 保存具体路径/行号/捕获运行 blob。旧 runtime-cache 年度 worker 在 `9944ddb` 的历史字节匹配其 run_manifest；当前 worker 增加 Owner-A 输入分支，不能把正常版本差异误报为历史证据破损。相关 firm、one_turn、输入适配器和 stationary_runtime 身份已对应核查，源代码均只读。

2018实际捕获运行是 `ch5-mp4c-2018-final-production-path-faithful-durable-execution-20260903-001`，PID67056。原8worker失败、observable retry和此捕获运行分别保留，不拼接轨迹。725行 ledger与定位 JSON匹配既有公布哈希。其 provenance 限制仍是 **CAPTURE_TIME_RAW_HASH_GAP_REMAINS__RETROSPECTIVE_CURRENT_FILE_INTEGRITY_CERTIFIED**；本轮读回不补造捕获时哈希。

## 2. 证据覆盖和口径

| 对象 | 实际覆盖 | 未保存/未观察 |
|---|---|---|
| Owner-A 原始2018批次 | 输入、run_manifest | 无终点、checkpoint或详细轨迹 |
| Observable single retry | receipt、stderr/stdout；KFE异常 | 无全国价格/调整轨迹，不与PID67056拼接 |
| PID67056捕获运行 | 725个家户入口；第1–23轮各31省，第24轮前12省至安徽；捕获 rah,w,Yt,Lt,Kt,Zt,GovInv 等 | ra0,ra,wt0,wjt,rk,mt,本轮家户Lt,At/Bt和控制器事件未保存 |
| 已完成轮次的状态差分 | 1–22轮各31省前后标量；第23轮12省前后标量 | 第23轮余19省，故其全国最大误差/决定省未知 |
| Owner-A成功终点 | 2009–2017及2019–2022，13年×31=403省年 | 2018终点缺失；其他年份中途接触时长未知 |
| 旧runtime-cache成功终点 | 2009–2023，15年×31=465省年 | 无完整中间轨迹，不与Owner-A视为相同输入 |
| Native MATLAB年度st | 消费的运行manifest未定位到；保护根顶层年度st清点为空 | 本轮没有native年度终点比较；Python checkpoint不是legacy st替身 |

全部年度终点及输入经过各年SUCCESS/checkpoint/run manifest绑定。只取小JSON，不打开checkpoint中的大数组。`consumed_inputs.json` 区分已有哈希匹配与本轮读取哈希。每条面板保留 regime、year、step、phase、两种省份索引和来源。

`call725_common_old_state_31.csv` 是明确的31省表：北京至安徽12省为捕获旧状态，福建至新疆19省在第24轮缺失；不能用第23轮的它们补齐同一快照。`province_coverage_and_spells.csv`、`contact_spells.csv` 给出各省观察分母。后续单家户 HJB 的1–500迭代没有当作新外层价格观察。

Owner-A对应修正CAP、指定滚动PLM结束年及GDP×1000/CAP×1000/POP×100；2018为rolling entry10、PLM vintage19、calendar row19。旧runtime-cache保持其各年binding和cache SHA，不升级为主源数据。用于输入数据工程的calibration_delta=.096不是厂商折旧；执行worker的厂商delta=.025，诊断使用后者。具体年/vintage、输入representation和原始量纲保存在年度面板。

## 3. 源码时序与判定规则

| 源码 | 本轮核对内容 |
|---|---|
| multi_prov_HANK_12sts.m:49–55,85–94,118–135 | 活动边界ra=[.02,.09]、wjt=[.8,1.3]；初始ra=rah=.09、wjt=.6、w=20；存在st时缓存绕过重新初始化 |
| mpHANK_equilibrium_2000.m:22–50 | 数据初值、GovInv和跨省比例；不能把初始Zt当作调整后的Zt |
| HANK_mp_1turn.m:15,29–40,45–52 | 同时旧状态家户→资本与旧ra生成rah→新厂商ra/wjt→综合w |
| HANK_firm.m:9–17,21–35,42–74 | Kt=Kt_supply+GovInv、Lt=Lt_supply；NKPC、利润floor、原始价格、clip及税额调整 |
| wage_caculate.m:7–11；HJB:26–31 | 跨目的省工资/税/迁移偏好聚合，家户读rah/w，不是ra/wjt |
| HANK_mp_1eq.m:14–22,31–60 | 触界计数、先收敛退出、全国gap开关、Zt/GovInv调整、tKN平滑 |
| Python one_turn.py:179–197 | 严格保留跨省资本表达式；firm Lt_prev取本轮household_lt，不能拿旧firm Lt替代 |
| annual_production.py:76–84,144–196 | 终点只输出20字段，FirmResult中的ra0/wt0未持久化；成功终点在调整前退出 |

有效高ra触发式 `ramax-.02` 的binary64为 `0.06999999999999999`（hex `0x1.1eb851eb851ebp-4`），低触发式 `ramin+.02` 为 `.04`。严格 `<`/`>`保留。全国 `maxKNratiogap<.1 AND steady_state==1` 是调整开关；不是单省自己的gap，也没有 `rah>.07` 这一原生条件。

面板同时给出原严格越界、精确接触、距上下界距离、128eps近界、near-inside及outside-by-roundoff；近界诊断不替代源条件。NaN/Inf/缺失不计入正常内部。初始化wjt=.6明确标为初始化，不当作厂商clip失效。没有从舍入日志推断binary64接触。

ra/ra0和wjt/wt0是厂商原生边界；rah对[.02,.09]只是描述参照，综合w完全没有套用[.8,1.3]。恰好等于边界本身不能证明raw严格越界。

## 4. 省份触界结果

| 输入组成功终点 | 分母 | ra上下界接触 | wjt上界 | wjt下界 | rah>.07 |
|---|---:|---:|---:|---:|---:|
| Owner-A修正口径 |403|0 / 0|225|120|0|
| 旧runtime-cache |465|0 / 0|18|400|0|

年度保存了mt,rk,Yt,Kt,Lt_supply,Zt，且成功退出发生在本轮调整前，因此可用同阶段标量重建raw。全部868省年重建的clip结果与保存ra/wjt在不变128eps比较下通过；由此得到的wt0严格上/下越界数分别等于表中的接触数。raw不是新增runtime捕获。ra0没有严格越界。两组年度均有大量工资接触，这符合原收敛条件不排除工资触界的事实，不撤销历史特定配置接受。

Owner-A上界接触最多：广东13/13年、江苏12/13，浙江/山东/河南/四川各11/13；下界持续者海南/西藏/青海/宁夏各13/13。旧runtime-cache上界主要广东6/15、江苏5/15、山东4/15；大量省份终点工资位于下界。完整31省×两组统计和年份列表见 `annual_province_coverage.csv`；逐年见 `annual_counts.csv`，不能把这些年度样本当作连续外层接触时长。

失败路径不具备可认证的逐省raw/capped厂商价格，因此对应接触/越界分母为0，明确缺失。捕获rah在非初始化入口的范围为[0.014424565870159915,.09]；低于厂商下界不构成rah原生边界违反。安徽是此输入唯一零外省权重省份，非初始化入口第2轮及第7–24轮rah=.09，第3–6轮rah=.02；第7–24轮有18个连续已观察上界参照接触，第24轮后未知。初始化第1轮接触单独统计。

原权重未归一化。对省i，rah权重和为

`1-r_i + r_i*sum_{j!=i}(r_j)/30`。

本2018输入权重和范围[0.7212282935079958,1]；所以即使所有厂商ra均受限，rah也可低于.02。第2轮31省rah由初始ra=.09按字面权重重建，31/31通过；第3轮以后缺少全国滞后ra，不伪造一般省份传递检验。安徽r_i=0，直接有rah=旧ra，无需解线性系统或归一化。

## 5. 自适应机制确实执行，且受全国开关限制

从每轮捕获后继状态的Kt/Lt重建KNratio，初始tKN=3，逐轮按源 `tKN_next=.6*KNratio+.4*tKN` 计算。Ygap使用相邻捕获Yt。此处Lt由firm写回，为Lt_supply；这与缺失的本轮household_lt不是同一对象。

| 已完成轮 | 全国maxKNratiogap | 决定省 | 调整门 |
|---:|---:|---|---|
|1|19.842075357095016|广东|关|
|2|.30787718279682275|西藏|关|
|3|.14187586624280568|广东|关|
|4|.05832661228030156|西藏|开|
|5|.1217541953566762|西藏|关|
|6|.08717418821744105|海南|开|
|7|.08941476241411839|海南|开|
|8|.1517827595686938|海南|关|
|9|.05302525856242446|海南|开|
|10|.11437413558448584|甘肃|关|
|11|.045388499860329556|吉林|开|
|12|.12327685575168079|贵州|关|
|13|.046260800192606144|贵州|开|
|14|.12116268152957499|贵州|关|
|15|.04250939823869704|贵州|开|
|16|.12000731417578381|贵州|关|
|17|.04483860609090007|贵州|开|
|18|.11978897055080262|贵州|关|
|19|.04630688166053876|贵州|开|
|20|.12158758987451845|贵州|关|
|21|.043503890509719145|山西|开|
|22|.11947876361194498|贵州|关|

这是 **DERIVED_EXPECTATION**，不是捕获的controller事件。1–22轮所有682组Zt前后变化与源条件一致；关闭门的372组GovInv均不变。开启门的310组中277次×1.1、31次×.9、2次不变。这些是 **CAPTURED_BEFORE_AFTER_STATES**，没有独立action事件；缺ra时只能由改变推断触发区间，不能声称逐项独立核验了ra阈值。

第23轮只有12省后态：11省GovInv×1.1、1省不变，11省Zt改变。结合已核对的唯一赋值路径，可以推断原调整块已启用，但全国max数值及决定省仍缺失，表中保留UNKNOWN_GATE数值状态而不填估计值。进入第24轮也证明第23轮没有先以收敛分支退出。第24轮有725号KFE异常，完整家户batch没有返回，所以未执行本轮one-turn厂商/控制器；正常返回的HJB nonconverged标志与这个异常不同。

安徽的关键捕获变化：

- 第4轮：GovInv从54313245.2543264减至48881920.728893764；Zt从.000641551386937363增至1.1943048929490467。此时Yt/Yt0=.0005371755493299598，Zt重置针对的是远低于目标的产出。
- 第6、7、9、11、13、15、17、19、21轮连续在各开启门时增加10%国资；第23轮再次增加10%。因此“机制未执行”不成立。
- 第22轮由贵州挡住全国门，安徽GovInv保持115261012.11434016、Zt保持.7163967429125945。
- 第23轮：GovInv增加到126787113.32577418，Zt调为.6650485431957093；这些值进入call725。它们不是生成该快照Yt/Kt时所用的值。

## 6. 安徽call725时点与价格上游

call725捕获输入：rah=.09、w=16.82014806560587、rb=.02、rb_gap=.07、tau=.05、Tt=.1。映射为外层24、第12省、0-based index11。

第23轮生成rah时读取的是进入第23轮携带的ra，即第22轮厂商ra。安徽外省比例恰为0，所以call725的rah=.09直接识别第22轮ra=.09。它是厂商上界接触，但没有第22轮ra0就不能区分严格超界clip或raw恰等于上界。第23轮GovInv×1.1又表明其新ra满足严格 `ra>ramax-.02`，不能据此指定新ra=.09。

第23轮厂商使用Zt=.7163967429125945、GovInv=115261012.11434016；保存Yt=36636882.21977386、Kt=115362461.89160682、Lt_supply=3210665.858026796，alpha=.772866243094144，N=438530，Kt0=54313245.2543264。由同阶段标量得到Y/K=.317580620411841、Kt_supply=101449.7772666663、Y/Y0=1.077209701821382。源生产函数重建通过。call725中的GovInv=126787113.32577418已经是调整后值，因此它大于保存Kt不表示同阶段Kt_supply为负。

失败路径不能完整计算rk/divrate/ra0：`one_turn.py`给firm的Lt_prev是当前家户劳动，而ledger只保存旧firm Lt；还缺少捕获的rk。不能以旧firm Lt替换，也不能从未来价格倒解缺失量。本轮初次后处理错误替换了该操作数，出现191项rah传递不匹配；相关尝试留在证据根`-001`，明确标为INVALID，不作为本报告价格证据。修正后raw路径字段全部缺失，未调整容差，未重跑模型。

成功同口径安徽终点对照（描述性，不是因果实验）：

| 口径/年 | ra | rah | 重建wt0 | wjt | Y/K |
|---|---:|---:|---:|---:|---:|
| Owner-A 2017 |.05741756420882064|.057417564208821|3.9422078841551627|1.3|.1472039750549909|
| Owner-A 2019 |.06075970595064213|.060759705950642395|1.6480982169542748|1.3|.10335598986444564|
| runtime-cache 2018，单独口径 |.04602939371229983|.04394482319701043|.4472095733444809|.8|.09383797662877025|

高Zt/高Y/K、资本相对不足、mt变化与组合传递是不同假说。当前可支持：Zt先因产出不足大幅重置，随后下降；GovInv显著上升但安徽仍有滞后高ra输入，全国门间歇关闭。不能从绝对Zt高低或跨年/跨口径差异给出因果占比，不能认定降低rah就能解决P32、算子缺陷或2018失败。

源资本供给只按 `sum(r_j*At_j*N_j)`排除自身后除30；没有加入不存在的本地留存项，也没有用At+Bt替换At*N。失败路径缺少At，只有同阶段Kt-GovInv派生的总供给；年度面板保存各省At*N和比例，未从它重新调用capital/one-turn例程。

## 7. 检查、产物及后续建议

13项相关合成测试：实际日志 **Ran 13 / 13 individual ok / OK**。覆盖严格/近界与非有限分类、初始化/对象隔离、滞后、字面组合权重、全国门/严格阈值、利润floor、缺步打断接触期，以及无生产模块/模型调用。原始日志字节base64和LF文本分别给SHA；无科学回归测试。

新增HJB/household/KFE、线性/root、one-turn、GE/annual、R/PLM、shock/IRF/Results、MATLAB进程、科学重试全部 **0**。两次运行均为保存标量后处理；第一份错误派生不删除，第二份为有效证据。没有修改生产、a_bar、ramax、Zt/GovInv或求解参数。原始文件、主checkout和未跟踪文件保留；没有Zotero、deep-learning-hank或全局配置改动。

发布路径仅本任务允许的validator目录、单个测试、报告及 `reports/province_price_boundary_audit_20260908/`。主要产物：31省call725表、725条旧状态价格面板、两组868省年终点面板、逐年/逐省统计、控制器时间线、同阶段分解、接触期表、source_map、consumed-input receipt、summary、ledger、测试日志和有限manifest。manifest排除自身及终端回执，外部文件按原字节，Git文本按LF身份核验。

建议Reviewer下一步先审阅这些时点和缺口：若确需判定2018各省ra0/wt0及mt原因，需要一份**明确另行授权**的观测方案，保存每轮全31省完整旧状态、当前household_lt、firm原始/截断价格、nk_gap/tKN与带时点的调整事件；重点覆盖22–24轮并在异常前落盘。当前没有足够保存数据补齐它们，也不能通过本任务再跑2018。任何rah敏感性试验必须单独由Owner选择目标与预算。D1–D3未实施，既有FAIL未改判，Results eligibility=FALSE。
