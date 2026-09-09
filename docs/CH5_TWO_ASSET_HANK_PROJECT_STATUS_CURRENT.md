# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：zcx369658780/dissertation-ch5-two-asset-hank。
最新接受候选：51ba55709dcec2ef82163f6f9f1766ba6ff90f32；审阅前live main：8cb763f2d31b850c7fb84e4ea1150e1cf8ef14f3。检查点不代表未来main不变。

## 当前结论与活动任务
状态：KFE_MASS_BALANCE_ACCEPTED__BOUNDARY_OR_TRUNCATION_DECISION_PENDING。
source_escape_interpretation=SUPPORTED只适用于保存有限箱算术；Reviewer marker为KFE_MASS_BALANCE_ATTRIBUTION_ACCEPTED__SOURCE_FREE_STATIONARITY_NOT_SATISFIED。原稳态方程仍不成立，没有MODEL_PASS、生产修复或Results资格。
当前active Builder任务：无。tasks/CH5_MP4C_CALL725_RAH_0P07_KFE_MASS_BALANCE_ATTRIBUTION.md已完成，不重跑账本、不继承其零调用预算。此前.07、.09和725次前缀均不重跑。
Codex默认gpt-5.6-sol / medium；Reviewer负责规划/验收，可在task中指定有理由的模型例外。本轮未暴露可验证实际模型标签，不将任务偏好当作已验证运行事实，不改provider/global配置，预算不随模型或会话重置。
Owner继续保留原MATLAB算法、a_bar、生产ramax及其他设置。D1–D3未采纳/未实施；没有授权经济source、改边界、扩网格或恢复GE。下一步建议与未批准范围见文末。

## 最新质量账本事实
报告及验收：docs/CH5_MP4C_CALL725_RAH_0P07_KFE_MASS_BALANCE_ATTRIBUTION_{REPORT,ACCEPTANCE}.md。
摘要：reports/call725_kfe_mass_balance_20260909/；外部根D:\ProjectTemp\ch5-call725-rah-0p07-kfe-mass-balance-20260909-001。
Q为post-loop KFE算子，T=Q.T，B为单行替换矩阵，x为raw，g为density，omega=db*da，p=omega*g。源对象/转置/F-order通过。g=x/saved_eta精确；eta=.017158160684824984与omega*sum(x)=.01715816068482498并非逐位一致，但通过原128-eps标准，不是容差放宽。
B只替换row295（MATLAB296），零基(15,14,0)，坐标(b,a,z)=(3.526315789473684,7.368421052631579,.8)。raw x[k]=.007只定标，不是概率流率；该pin是内点。
Tg的物质性残差集中于该行：r[k]=-3.4540415243199343，占残差L1的.99999999999999656；最大off-pin1.156193196738542e-15，off-pin绝对和1.2191973401434281e-14。不是错转置或展开次序解释了原残差。
upper-b密度加权流出dot(ell,p)=.6697587443279651，隐含平衡源-omega*r[k]同值；包含delta=Q*1+ell及off-pin修正后，两条质量恒等式误差均1.1102230246251565e-16，小于冻结2.842170943040401e-14。已支持的是Q.T*p+s*e_k约等于0，不是Q.T*p=0，也不是批准新的经济进入/退出法则。
29个upper-b外向格中20个有正流量，9个概率0；全部流出来自b=5。前3格占78.760811%，前10格占99.280428%。返回诊断密度在upper-b质量为.6758361975609537，非已接受真实家户分布。边界面在角点重叠，union另列。
160个精确负density仍保留，负质量约-1.04e-16；对逃逸贡献0，对dot(q,p)贡献约-1.07e-32，不能解释O(1)残差。.6697587是每模型时间单位概率质量流率，不是一期流失概率；.149889尺度比也不是人口流失率。
冻结export轴组装省略越界offdiagonal但保留对应diagonal rate，post-loop后转置并替换一行解释了此代数平衡。数值pin补源不能当成原经济设定。Qh未用于质量账本，其21负非对角元仍为独立问题。

## 本轮预算与证据范围
新增initializer/root/HJB/KFE/各类solve/policy/evaluator/assembler/selector/GE/年度/IRF/MATLAB全部0，scientific retry0；只有已有数组后处理和合成测试。
Reviewer为L3提交/代码/报告审阅、L4已发布10/10测试日志检查；未独立执行这些测试、读取Windows原始NPZ/MAT、重算全部800格或重验72引用。验收读ledger/analyze源码、质量JSON、源行映射及manifest回执，不把SUPPORTED字符串本身当作自动证明。
manifest E94F1810905B551EEC62CE066B0769DE0EB9EC2414481FDC73B63973A500C82C；Builder回执72引用/13前序科学文件/800格账本。早期eta精确断言与测试失败保留，最终使用的128-eps规则早已冻结。实际模型未核验。

## 前置.07敏感性与未通过的有效性
已接受e3176e9352b4f7e155c91891a4cabdd517e9e232，报告/验收docs/CH5_MP4C_CALL725_RAH_0P07_NATIVE_INIT_SENSITIVITY_{REPORT,ACCEPTANCE}.md。
有效原科学根D:\ProjectTemp\ch5-call725-rah-0p07-native-init-20260908-002；manifest F1C59EE5D937AABB8F5A3CE01A24456F53E9C90D26F710E3BE6F357C375CE459。仅state.rah变float('0.07')且mapped r_a改变；carried ra/ramax=.09，工资16.82014806560587、rb=.02、rb_gap=.07、tau=.05、Tt=.1、rho=.05、gamma2、phi5、chi0=.1、chi1=2、a_bar=1e-6、20x20x2网格/Delta1000/crit1e-7/maxit100与solver不变。按原生算法一次生成新V0/l0，.09初值仅作比较。
.09复用基线HJB100 false/statistic.3038218386543494、KFE非有限；新.09调用0。.07 HJB26收敛/statistic8.867440115523095e-11、KFE及聚合返回；支持包含原生初始化响应的局部收益率敏感性，不分离初值与后续价格效应，不证明普适.07安全率或应改ramax。
C10.292627721151788、有效z加权L.6800557026886584、A7.300066770790965、B4.69218565897191、A+B11.992252429762875、质量.9999999999999999均为诊断积分，不能带入GE当作已接受稳态。
Qh21负非对角元、min-4.0056579039558065；post-loop Q非对角无负值但row-sum最大4.00987105374827。小Bx-f残差2.054563116860031e-17及归一化不替代Tg残差3.4540415243199343；其尺度比.14988946066377937。原固定点评价未新增。
.07实际1进程/初始化、800劳动根及嵌套800brentq、HJB26直接求解/KFE1求解/聚合1；无科学重启或启动重试。其-001预检和早期解码失败保留。此前12/12日志与80引用/39 Git LF项为Builder证据，非本轮重复独立核验。

## 上游与历史科学事实
9d76747f原参数前缀：725入口*11字段=7975项零差，24份31省共同状态、713firm/23controller，安徽call725原KFE异常复现。仅已比较对象一致，不追溯修复旧capture-time hash gap/未保存数组/历史环境身份。
安徽turn22/23 raw ra0约.219795/.219069，turn23 wt0=2.5772708754207905，clip为.09/1.3；当时rk=.244069389412528减delta=.025解释ra0，分红0。turn23贵州决定maxgap=.04124871080231385并开门，安徽Zt下降/GovInv*1.1；raw下降仍高于clip不是没有调整。安徽外省权重0，turn23组合消费turn22旧ra；反馈不即时改写已生成rah。第23轮24省ra触上界，不推论全部失败。不补本地资本项、不改劳动/货币单位。
前缀旧预算HJB/KFE各725、HJB求解19961、劳动根580000、one-turn23；旧manifest_02为4C18B9AA14C23356594F1A0ECCBA346B3DB2AE668B7204A73D88A226B98B0146。本轮不重验其13800引用。
8ef4a2a6审计保留PARTIAL_EVIDENCE，错误audit-001已排除。旧runtime-cache2009–2023 Python15/15年465省年限定接受；Owner-A2009–2022为13/14年PASS、2018失败；终点工资上/下界分别18/400与225/120，端点ra触界与rah>.07均0，非路径安全定理。
首轮53/53/raw-vb阶段解释、多轮dedd0f8/四状态b2d7a814/固定线性2ff3eb2及边界规格15f51be9保留原范围。共同MAT初始化MATLAB143收敛/Python500未收敛与原生.09/.07不同；P32极大transfer/cost/sigma丢失、M14318负元/15泄漏与14/14上界冲突未被本轮修复。household特定fixture、MP0–MP3限定接受不升级全部经验参数有效。

## 下一科学选择：未批准、无执行任务
Reviewer不建议把数值pin解释为经济补人口机制。为尊重保留原算法/a_bar的Owner方向，建议先选择一次独立upper-b截断敏感性：候选b从[-2,5]20点扩至[-2,12]39点，数学间距7/19不变；a/z网格、rah=.07、其他价格/参数、初始化算法、helper、组装和pin公式、HJB100步均保留。生产网格/ramax不改，不采用.07密度热启动，不复算旧箱基线。
这不是已授权task。扩网格属于新的诊断输入选择，需Owner确认后才发布有限预算。原pin公式依赖状态数，因此该候选会自动从k295变k576；必须记录相应物理坐标，不宣称固定pin的纯边界效应。单次扩箱无法保证截断充分、消除Qh负率或恢复有效稳态，不以新source或调容差制造PASS。
如Owner选择直接修边界，则应明确数值/经济含义，不能默认同时批准D1–D3；已有规格不必重写。无实质选择前不增加重复审计/文档门禁。后续仍需原稳态有效性→2018/年度覆盖→真正动态规格/集成/稳健性；顺序比较静态不是IRF。Results eligibility=FALSE。

## 身份与本地保护
HJB SHA256049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE；export blob9e7dc9556a2b76811e78f89999abecc045886106。
原年度input F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0；共同MAT1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81与scalar A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6不能代替原生初始化。
工作目录D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001；原D:\ResearchCode checkout及70未跟踪文件、全部分支/证据/LF runtime保留，禁止reset/clean/stash/强覆。docs-sync已完成不重开。此次Reviewer发布没有启动本地模型。
