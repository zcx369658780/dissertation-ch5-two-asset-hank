# Chapter 5 两资产 HANK 当前状态
更新：2026-09-08。唯一活动仓库：zcx369658780/dissertation-ch5-two-asset-hank。
最新接受证据提交：9d76747f48858a3e9289de8f284fffbc49aaedce。本次Owner批准落地前live main为062cd3b715e9aed85e7c068063d6a099b2e30186；这些是检查点，不是假定未来main固定。

## 当前Owner批准与活动任务
状态：OWNER_APPROVED_CALL725_RAH_0P07_NATIVE_INIT_SENSITIVITY_ACTIVE。
Owner已明确批准独立单户rah=.07原生初始化敏感性诊断。活动任务：tasks/CH5_MP4C_CALL725_RAH_0P07_NATIVE_INIT_SENSITIVITY.md。
只复制已捕获安徽call725输入并将rah=.09改为float('0.07')，原工资本金税率等其他输入、网格、a_bar、helper和算法/HJB100步规则保持；对应HouseholdInputs.r_a从该字段绑定。按原生算法重新生成.07的V0/l0，不固定到.09数组。复用已接受.09失败基线，不重跑0.09或725调用前缀。
新预算：一次Python科学进程、一次原生初始化、最多800个原劳动根、一次HJB且最多100次直接求解、自然到达时一次原KFE及聚合。原HJB正常返回false仍按原adapter进入KFE；异常立即停止。科学进入后不重启，至多一次经证明零科学进入的外部启动重试；科学15分钟、全任务90分钟。精确允许路径/预算/检查以task为准。
发布不等于本地已执行，尚未收到本任务报告。此前“尚待Owner选择”的未来安排被此次明确批准取代；历史验收记录保留当时状态。
Owner继续保留原MATLAB算法及生产设置：不改ramax或其他生产校准，不改Zt/GovInv规则，不跑其他利率点、MATLAB、GE/年度或动态。D1–D3边界/生成算子/FOC修复target未采纳、未实施、暂缓。此次批准不是生产替换、因果已证、修正年度或Results接受。

## 最新可观测前缀证据
已接受OBSERVABLE_PREFIX_CAPTURE_COMPLETE / MATCHED_PREFIX_AND_FAILURE_REPRODUCED；tasks/CH5_MP4C_2018_ORIGINAL_PARAMETER_OBSERVABLE_PREFIX_REPLAY.md已完成，预算已消费。
报告与验收：docs/CH5_MP4C_2018_ORIGINAL_PARAMETER_OBSERVABLE_PREFIX_REPLAY_REPORT.md 和同前缀_ACCEPTANCE.md。
摘要：reports/2018_observable_prefix_replay_20260908/；外部根：D:\ProjectTemp\ch5-2018-observable-prefix-replay-20260908-001。
725个入口×11个连续字段=7975项，新旧最大误差全部0，类别/次序通过；历史725组HJB停止量和44项旧控制器标量比较通过。只支持已比较字段，未证明旧运行未保存的完整数组同一性。
第24轮安徽call725原生初始化HJB100步返回false，统计量.3038218386543494；原post-loop adapter进入KFE，复现faithful contaminated-row solve is non-finite。原始非有限KFE线性输出和前置HJB已保存；无有效KFE返回/该户aggregate，未进入call726。
24份完整31省共同入口、725个实际家户入口、724个家户返回、713个firm返回、23轮全国controller和713个逐省action。第24轮余19省有共同旧状态，但没有本轮家户返回/firm阶段。

## 对高收益率与调整机制的更新
安徽第22轮raw ra0=.21979491622969854，第23轮=.21906938941252802，严格超过.09；第23轮wt0=2.5772708754207905，超过1.3，实际截断ra=.09、wjt=1.3。家户读rah=.09，不直接读raw .219069。
第23轮rk=.244069389412528、delta=.025、截零后PIt=0、divrate=0，所以ra0=rk-delta；mt=.9943859584740543，Y/K=.317580620411841。这是同阶段代数归因，不是Zt/K/mt的因果比例。
安徽第5轮raw ra0约.53423，至第23轮约.21907，虽下降仍高于clip；所以存储ra持续.09不表示反馈从未执行。第23轮贵州决定全国maxKNratiogap=.04124871080231385，门打开；安徽Zt .7163967429125945→.6650485431957093，GovInv115261012.11434016→126787113.32577418。第22轮贵州导致门关闭与此不冲突。
第5–15轮全国31省ra都触上界；第23轮仍24省触上界、7省内部，工资19上界/5下界/7内部。不能将安徽的唯一异常推广为这些省都失败。
安徽外省比例0；turn23生成rah消费turn22旧ra，之后才有新firm和适应。call725的rah=.09具有明确滞后；GovInv/Zt调整不会即时改写已生成价格。第23轮模型私人资本供给份额.0008794002451333387（约.08794%），其余为GovInv；不擅补本地资本项。实际household Lt_prev与destination Lt_supply仍按源区分，不作单位/公式修正。
全部4278项firm代数身份核对报告通过。旧审计缺少raw和第23轮全国最大值的局限，由本次独立观测补充；旧报告保留当时PARTIAL_EVIDENCE，不倒填历史raw文件。

## 前缀预算、证据等级与工程限制
此前一次Python科学进程、科学耗时2874.297秒；另一次bootstrap CRLF身份失败在科学进入前，消耗其唯一允许的外部启动重试。同HEAD的隔离LF工作树恢复原字节身份，原checkout/全局设置保留；科学重启0。
native initialization/HJB/KFE各725；HJB直接求解19961、KFE直接求解725、KFE成功724；劳动根580000，其内brentq同为580000（嵌套不双算为不同家户初值）；residual4837970。one-turn23、firm713、controller23。MATLAB、独立诊断求解、其他年度/R-PLM/动态/IRF/Results0。原生产HJBmaxit100、原worker外层参数250与source默认500均未改。
Reviewer对前缀做L3提交/代码/报告审阅、L4最终15/15发布日志检查；未独立执行测试/模型、读取Windows完整capture或重新核验13800引用。外部manifest_02 SHA256：4C18B9AA14C23356594F1A0ECCBA346B3DB2AE668B7204A73D88A226B98B0146；13800文件引用/13696capture文件/8321索引条目是Builder回执。相应早期工程失败与manifest版本保留，非额外科学运行。历史环境并非全部版本可核验，旧capture-time hash gap不被追溯消除。
本次Reviewer仅发布Owner批准的任务，新增科学调用0，没有重做上述验收或Windows文件核验。

## 已完成的价格审计与年度口径
前置8ef4a2a6审计接受为PARTIAL_EVIDENCE；docs/CH5_MP4C_PROVINCE_PRICE_BOUNDARY_AND_ADAPTATION_AUDIT_{REPORT,ACCEPTANCE}.md。有效audit根后缀-002；-001错误旧firm Lt替代current household Lt及191项派生不匹配已排除，不是新模型发现。原审计新增科学调用0。
Owner-A成功终点403省年：工资上/下界225/120；旧runtime-cache465省年：18/400；两组ra触界及rah>.07均0。派生raw经clip核对通过，非raw runtime捕获。源码终止谓词不排除工资触界，终点统计不是中间求解的安全率定理。
旧protected runtime-cache Python2009–2023的15/15年、465省年历史接受，不是全部年份跨语言parity。Owner-A修正2009–2022共14年中13年PASS、2018失败；完整修正覆盖仍未接受。各来源/初始化不拼接。

## 不变的科学问题与历史证据
- 独立完全共同MAT初始化：MATLAB143步收敛、Python500未收敛，尾部约.00862；不同于原生初始化100步失败。
- 首轮25e5db97a0239d956d572359db5835cec945962f：53/53，V1最大差3.9968028886505635e-15；raw-vb40/40是保存阶段差异，非导数修复依据。
- 多轮dedd0f8e5fa894b83c8b20e522d66893e7b6b377及四状态b2d7a814039a585b696d8cc5079b8b9865017501：历史限定比较继续保留；M24/P24/M143_FINAL38/38，P32首差V1。
- 固定线性2ff3eb212ea9a0d101183f9ff49dd1043bb6b886：精确同M/RHS仍有求解路径差异及输入微差敏感性；ROW_POW2未普遍改善，P32极大policy/cost与sigma丢失仍开放。不得靠调容差/反复换solver寻求PASS。
- 边界规格15f51be9733b5043e738d3e522b97554e95902b9：14/14快照预算/捕获漂移一致但有上界向外漂移；M143_FINAL有18负非对角元及15泄漏；2,256异常行不是独立经济状态或全部bug。只接受证据/提案，target不实施。
- household特定fixture、MP0–MP3的历史限定接受保留，不升级所有经验输入。旧预算包括失败/未持久化调用，不能重置。

## 身份、本地保护与下一步
protected HJB SHA256：049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE；export blob：9e7dc9556a2b76811e78f89999abecc045886106。
原2018输入SHA256：F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0；隔离共同MAT：1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81；scalar binding：A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6。后两者不替代本次原生初始化。
工作目录D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001；原D:\ResearchCode\dissertation-ch5-two-asset-hank及70未跟踪文件、所有历史证据和LF工作树保留。docs-sync d2f3e6e7cc21fffe8807f577ec2262bb77afdc07已完成，不重开。
新任务分支codex/ch5-call725-rah-0p07-native-init-20260908；新证据根D:\ProjectTemp\ch5-call725-rah-0p07-native-init-20260908-001，已占用使用fresh suffix。
下一步执行本次已批准单户实验并分别报告HJB收敛、KFE返回/异常、算子/分布诊断。包含初始化响应，不是固定V0/l0的纯算子效应；KFE返回不等于HJB收敛，实验改善也不自动成为生产修改或年度接受。后续仍需解决数值有效性、修正年度覆盖、真正动态规格与稳健性。Results eligibility=FALSE。
