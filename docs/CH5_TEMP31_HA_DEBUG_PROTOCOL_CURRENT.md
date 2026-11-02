# TEMP31 单来源地HA诊断：本轮固定目标与判定口径 · 2026-11-02

STATUS=EXECUTION_PROTOCOL_FIXED__STRICT_SCIENTIFIC_ACCEPTANCE_UNBOUND
FROZEN_PLAN=CH5_TEMP31_S2_ATTEMPT3_FROZEN_DEBUG_PLAN_20261102.json
FROZEN_PLAN_SHA256=ad2fb2c11ba571d6aa3b65c0af9c622af23e054bb4d98a9a2541891455c44cd9
OWNER_DECISION=CH5_TEMP31_S2_OWNER_DECISION_20261102_03.json
OWNER_DECISION_SHA256=cad0a70b875bc41dd28dd95f25212f3648d002754242384b23c081747a66562e
FINAL_PINNED_PROPOSAL=CH5_TEMP31_S2_BOUNDED_OBSERVER_PROPOSAL_20261102.json
CODE_CANDIDATE=b26ee2d737cea77479b8632cf8d5395e472655eb
CODE_TREE=77bd328ee3f3fd30ec3df32843a25ad9f329afe5
CODE_PUBLICATION=LOCAL_ONLY_NOT_PUSHED

## 本轮目标与固定项

Owner明确同意先固定目标/输入/诊断并调试HA，说明50或100轮可判断。执行采用原max_iterations=100，50为若到达则观察的中途点；原HJB提前达到条件时正常返回，不强迫跑满50或100。只做合成A/index0首轮、原20×20×2网格、原价格/参数/输入和净19初猜，原a*r_a初始化及原核心源码不改。这里固定的是本轮工程执行协议，不是FORMAL_SOURCE_FREEZE或科学接受。

新1进程，含导入120秒、2GiB，初始化≤1、Python/native Brent各≤800，HJB≤1/线性求解≤100/policy≤80000；只有原HJB收敛且网格不变才KFE≤1及汇总≤1。失败即停、重试0；原2次S2授权保持关闭，本轮为新第3次累计尝试。旧初始化3/10余7、工资/补录各1/1关闭均不动。

## 预先固定的结果解释

| 可观察事件 | 本轮解释与下一阶段 |
|---|---|
| 原HJB返回converged=true且max(abs(value-old))<1e-7 | 原HJB自身迭代条件达到；同次原后置算子/网格检查后才允许KFE；不是严格HA接受 |
| 原HJB返回converged=false且达到100轮 | 本固定输入/控制下100轮未收敛；保留返回和原始变化量，停止于KFE前，不自动延长/换参数 |
| 超时/内存/域/来源/观察器或返回未知 | 工程/数值异常按实测原因分类；没有完整返回时不声称100轮不收敛，保留最后完整进度 |
| KFE与汇总返回 | 保留原污染系统残差，同时报告完整原算子A_post.T@g的无穷范数、密度有限性/最小值、质量、负质量及单位权重；不剪负值或重建算子 |
| 严格科学资格 | 适用合同引用与阈值仍null，保持CRITERIA_UNBOUND；本轮不填经验阈值，不将HJB变化量改称方程残差 |

质量沿db*da，对离散z求和；原人口缩放/劳动z权重保持其原位置。正式输入采纳、真实生产工资兼容及后轮接线独立处理，不从合成首轮诊断推定31省生产有效。

## 辅助计数的静态依据

原policy没有循环；可枚举工资验证入口为：直接require_netwage_inputs1次、新局部输入构造1次、劳动函数2次、资产漂移函数3次，共≤7次。另有HJB入口1次。原policy上限80000给出验证≤1+7×80000=560001。固定省序A/B、2×2机制矩阵，各嵌套生成器每次验证最多2×(2+1)=6次Python进入，因此HJB工资验证嵌套代码限额为3360006；同函数内其他生成器3或5次不超过此界。

只对HJB阶段该验证函数及其嵌套代码设置派生额度；其他辅助代码每阶段1000000与所有核心预算保持。观察器允许的最大绑定值也固定3360006，实际每个绑定仍单独检查。不同code/globals/phase、native对象/调用者、阶段顺序、失钩/超额拒绝及Owner门均保持。源码哈希固定可防止调用结构改变后沿用该推导；任何结构/身份不符停止。

## 进度记录与工程核验

进度只在每轮第一个policy格进入时读取确切原HJB父frame已有iteration/statistic，记录上一完整轮的变化量；不重算工资、值函数或残差。最后一轮以确切原HJB实际返回补齐；异常unwind独立记录，不当返回。超时可能只保留最近一个已完成轮，不能由“进入本轮”推断本轮已完成。

新增8项非科学夹具先出现真实缺失/上限失败，再实现并通过；相关33项限定回归通过，包括旧观察器、预算/失钩/身份拒绝、异常返回及子进程实际Job限额复核。只新增1个中性工程进程；该工程阶段科学模块导入/科学worker0。仅改4个工程源路径并新增1测试，旧593中589及原565路径保持，现594；原11科学源catalog、fixture、计划与环境摘要不变。

本轮固定计划、不可变Owner决定、预登记累计账本与最终pins均先于科研启动；运行结果和关闭状态以CURRENT及本轮结果报告为准。失败/成功原始文件均LOCAL_ONLY，不改旧决定/意图/原始证据。工程自审不是独立科学审查。

FORMAL_SOURCE_FREEZE/consumer_ready/formal_ha_accepted/科学接受/Results/model_activation/REAL_GE保持FALSE。R12 STOP、R13未授权、WASM六路径STOP、OWNER_BASELINE_REBIND未授权、16项义务及历史dirty树/index保持。无科学后继、分支清理、main合并、原件移动/删除或全局配置变更。


## 2026-11-03当前S01执行补充

最新Owner决定CH5_TEMP31_S2_OWNER_DECISION_20261103_04.json与固定输入CH5_TEMP31_S01_PRICE_INPUT_20261102.json允许唯一外部rah替换.09→.05，原P0协议作为控制保留；原11科学源、网格及其他输入/数值条件保持。执行结果见CH5_TEMP31_S01_PRICE_DIAGNOSTIC_RESULT_20261103.md：HJB25轮达到原条件，原KFE/汇总返回，原驻定残差3.618851426605556未获严格资格。当前CLOSED_COMPLETED_NO_RETRY、4/4用完、无预备点或新运行；严格引用/阈值null和全部科学/保护门保持。原计划/协议历史数字保留，最新代码ee15d70、41项工程检查，不把计算完成解释为FORMAL_SOURCE_FREEZE或Results。
