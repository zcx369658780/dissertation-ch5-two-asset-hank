# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：zcx369658780/dissertation-ch5-two-asset-hank。
最新接受候选：e3176e9352b4f7e155c91891a4cabdd517e9e232；审阅前live main：f455bdb8904f92a027bf6dc4437c75d900835bbb。均为检查点，必须fresh读取未来main。

## 当前结论、执行配置与活动任务
状态：RAH_0P07_SENSITIVITY_ACCEPTED__ZERO_SOLVE_KFE_MASS_BALANCE_ACTIVE。
已接受独立单户.07敏感性实验：HJB_CONVERGED_AND_KFE_RETURNED；Reviewer marker为CALL725_RAH_0P07_SENSITIVITY_ACCEPTED__STATIONARITY_BLOCKER_REMAINS。这不是有效稳态分布、MODEL_PASS、生产修复、年度覆盖或Results验收。
活动任务：tasks/CH5_MP4C_CALL725_RAH_0P07_KFE_MASS_BALANCE_ATTRIBUTION.md。使用现有有限密度和原矩阵，定位被替换方程残差，核对密度加权upper-b概率流与归一化分布的质量收支。新初始化/根/直接或迭代求解/HJB/KFE/评价器/模型及MATLAB调用全部0；不重复.07或.09实验，也不重新观测725次前缀。发布尚未收到该新任务报告，不代表本地运行。
Codex默认gpt-5.6-sol / medium；Reviewer负责整体规划和验收，任务可指定有理由的局部模型例外。该设置是Owner偏好，不是已核验本地model/provider事实；预算与标准不随模型变化。
Owner继续保留原MATLAB算法、a_bar、生产ramax及其余生产设置。D1–D3边界/生成算子/FOC target未采纳、未实施；.07只用于已完成诊断副本。当前不授权任何矩阵/边界修复、参数扫描或GE恢复。

## 最新.07实验事实
报告及验收：docs/CH5_MP4C_CALL725_RAH_0P07_NATIVE_INIT_SENSITIVITY_{REPORT,ACCEPTANCE}.md。
摘要：reports/call725_rah_0p07_sensitivity_20260908/。有效外部根D:\ProjectTemp\ch5-call725-rah-0p07-native-init-20260908-002。
完整state仅rah变为float('0.07')，mapped输入仅r_a变化；carried ra=.09、ramax=.09保留。工资16.82014806560587、rb=.02、rb_gap=.07、tau=.05、Tt=.1、rho=.05、gamma=2、phi=5、chi0=.1、chi1=2、a_bar=1e-6及原20x20x2网格/Delta1000/crit1e-7/maxit100/原求解器保持；从原始捕获对象绑定，非聊天数字重建。
.09原生初始化基线只读复用：HJB100 false/statistic .3038218386543494，KFE raw非有限，无有效density/aggregate。新.09调用0。
.07按原生算法一次重建V0/l0：HJB26步收敛、statistic8.867440115523095e-11；原KFE/聚合返回。C10.292627721151788，有效z加权L.6800557026886584，A7.300066770790965，B4.69218565897191，A+B11.992252429762875，质量.9999999999999999。全部为诊断积分，不是已接受稳态经济量。
局部受控结果支持包含原生初始化响应在内的收益率敏感性，不分离初值与后续算子效应、不证明唯一致因/普适.07安全率/应改ramax。尚无额外非线性固定点评价。

## 仍然明确不通过的有效性
最后HJB迭代算子21个负非对角元，最小-4.0056579039558065；行和最大绝对值.005241251210036213。post-loop KFE算子负非对角元0，但行和最大绝对值4.00987105374827。两者不能互换。
post-loop由保存drift重建29个upper-b外向rate单元，最大4.00987105374827、未加权总和34.068684700799736；其余面计数0。row-sum+leak最大误差2.942091015256665e-15。这个未加权rate总和不是概率质量损失；新任务才做密度加权账本。
contaminated-row原始线性残差2.054563116860031e-17、尺度比5.10588263142955e-17。未修改转置稳态残差3.4540415243199343、分母23.043925230125268、比值.14988946066377937。后者不是人口/质量流失百分比；不同方程残差不能互相替代。
密度160个精确负值，最小-1.5082603896975325e-16，带权负质量-1.0402057506525602e-16；保留符号但不把这些舍入量级负值与O(1)稳态残差混为同等问题。有限与归一不意味着原稳态方程成立。pin行是否对应补偿边界流失的隐含源尚待新账本核对，不能提前当作已证结论。

## 最新预算与验收范围
新.07一次Python科学进程/初始化；800劳动根及嵌套800brentq，残差评估6654；HJB1次/26更新求解，KFE1次/1直接求解，聚合1次。科学耗时报告2.938秒；无科学重启或启动重试。MATLAB/firm/GE/年度/其他省年/IRF/额外诊断solve0。
首个预检目录-001因index绑定路径停止、科学进入0；-002验证外部index与Git副本同字节后完成。早期合成映射键array解码错误及失败日志保留，未通过重跑科学掩盖。source_runtime LF和保护源不改。
Reviewer：L3提交/源码/报告审阅、L4发布12/12日志检查；未独立执行这些测试/模型、直接读Windows数组、重算全部诊断或重验80引用/39个Git输出LF。部分测试是简单合成样例，非完整wrapper集成测试。
manifest SHA256 F1C59EE5D937AABB8F5A3CE01A24456F53E9C90D26F710E3BE6F357C375CE459；Builder回执80引用、21科学文件、12阶段。新验收不制造独立复算声明。

## 前缀、上游价格和年度证据保留
9d76747f48858a3e9289de8f284fffbc49aaedce的原参数观测前缀已接受：725入口*11字段=7975项误差0，24份完整31省共同入口，713firm返回、23controller记录；原call725 KFE异常复现。仅已比较对象匹配，旧未保存数组/历史环境同一性和旧capture-time raw-hash gap不被追溯修复。
安徽turn22/23 raw ra0=.21979491622969854/.21906938941252802，turn23 wt0=2.5772708754207905，clip为.09/1.3。turn23 rk=.244069389412528、delta=.025、PIt/divrate0，mt=.9943859584740543、Y/K=.317580620411841；高raw来自该时点资本租金而非正利润分红。家户实际读.09，不是.219。
反馈实际执行，raw从turn5约.53423下降但仍高于clip。turn22贵州令全国门关闭；turn23贵州决定maxgap=.04124871080231385、门开，安徽Zt .7163967429125945→.6650485431957093，GovInv115261012.11434016→126787113.32577418。安徽外省权重0，turn23组合使用turn22旧ra，调整不即时回写已形成rah。turn23私人资本份额.0008794002451333387；不补本地项/改单位。第5–15轮31省ra都在上界，第23轮仍24省；不推论所有省都失败。
前缀预算HJB/KFE各725、HJB求解19961、KFE成功724、劳动根580000、one-turn23、firm713；其一次零进入CRLF启动失败与唯一重试仍计原账本。manifest_02 SHA2564C18B9AA14C23356594F1A0ECCBA346B3DB2AE668B7204A73D88A226B98B0146，外部13800引用回读为Builder证据，不是本次重复核验。
8ef4a2a6价格审计按当时PARTIAL_EVIDENCE保留，错误-001旧firm Lt替代current household Lt已排除，有效-002。旧runtime-cache2009–2023 Python15/15年、465省年历史限定接受；Owner-A2009–2022为13/14年PASS、2018失败。成功端点工资上/下界分别18/400与225/120；端点ra触界及rah>.07均0，不是中间路径安全定理。

## 更早科学边界及锚点
首轮25e5db97为53/53，raw-vb40/40由保存阶段不同解释。多轮dedd0f8/四状态b2d7a814和固定线性2ff3eb2均保留原范围；完全共同MAT初始化下MATLAB143收敛、Python500不收敛，与原生初始化.09/.07不同。P32巨大transfer/cost和sigma丢失未被本次修复；ROW_POW2不普遍改善，不反复换solver/调容差求PASS。
15f51be9边界规格：14/14快照预算/捕获漂移一致但有上界向外；M143_FINAL18负非对角元/15泄漏；2256异常快照行不全是独立状态或bug。D1–D3只是未采纳提案，不因新诊断自动实施。household特定fixture及MP0–MP3限定历史接受不升级为所有经验参数有效。

## 身份与后续
HJB保护SHA256049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE；export blob9e7dc9556a2b76811e78f89999abecc045886106。原年度input F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0；共同MAT1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81和scalar binding A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6不能替代原生初始化。
工作目录D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001；原D:\ResearchCode checkout、70未跟踪文件及所有旧证据/LF工作树保留，禁止reset/clean/stash/强覆。docs-sync d2f3e6e7已完成不重开。当前新证据根由active task指定，与完成的.07 -002分开。
后续：已存有限密度的残差/边界质量账本→有证据的最小科学决定与新任务→数值有效性及修正2018→年度覆盖→真正动态规格/集成/稳健性。MATLAB顺序比较静态不等于真正IRF。Results eligibility=FALSE。
