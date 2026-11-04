# HA算法冻结合同 · 2026-11-04

STATUS=OWNER_HA_ALGORITHM_LOCK_ACTIVE__NO_NEW_RUN_GRANT
DECISION=CH5_TEMP31_HA_ALGORITHM_FREEZE_OWNER_DECISION_20261104.json
DECISION_SHA256=7975c4f35307b5fa61433c6ec5e38cad2a53b36ed334d167bdf05e720685fe3d
OWNER_EXACT_STATEMENT=好的我补充一下：KFE应该找matlab版本的方法稳态后重建算子再归一化。请你冻结此项（等同于HANK_2ASSETS_HJB.md的所有算法都冻结）请执行冻结后继续

## 冻结对象及身份

Owner所写`HANK_2ASSETS_HJB.md`在两处活动工作树及既定原件同名查找中未发现；本会话已认证的实际原件为`HANK_2ASSETS_HJB.m`，12227 bytes，SHA-256=`049136b769560040bc678f828f5d3ec5338ddcaa2090d6bed4e40732f56c3eae`。依上下文将其登记为本次算法引用，原始措辞同时保留；不伪造.md、不重命名或移动原件。

该原件所描述的HA全部算法均锁定：初始化方法、导数/FOC/政策/迎风与边界、隐式迭代、原有停止逻辑、后置算子重建、KFE固定行求解/归一化及汇总，不允许以工程调试名义改变。辅助方法即使未单列历史文件哈希，也不能借此绕过算法禁改。

实际Python运行基线为6a3d443840757f3f1e003cbd6554a0c43afa7eb8；本次不可变决定列出实际加载的11个科学模块的bytes/Blob/SHA-256，全部核验匹配并冻结。选定来源锚点仍56447829。未完整归档或认证整个MATLAB依赖树，也不把局部身份核验说成全跨语言等价。

## KFE方法及顺序锁定

**原HJB迭代结束并满足原收敛准入 → 使用按最终政策与预算总漂移重建并返回的原后置算子 → 原转置及固定行求解 → 按原网格权重归一化 → 原汇总。**

具体保持`post_convergence_operator.full`，不改用`operator.full`。保留原第floor(.37*N)行（Python索引减1）、rhs=.007、raw求解及`sum(raw)*db*da`归一化。不能补对角、剪裁漂移/密度、改固定行或归一化、重建另一算子替代原返回。

“稳态后”在此指进入KFE前已有原HJB收敛返回，不意味着先拥有严格KFE驻定证书。现有HJB函数在返回前已经计算post，外层再检查原converged才准入KFE；本冻结不移动代码位置或改变内部控制流。保留原HJB值函数变化量与原KFE系统残差，外部原驻定残差另列，不改名为其他接受指标。

## 已知差异不自动改回

前述对比报告已列明：既有Owner批准的外置a*r_a初始化与历史平方项初猜、净工资接线、历史迭代行和检查在选定Python缺失，以及已批准的外层失败即停逻辑。它们仍作为显式既存差异/决定保留，不从“冻结”自动推导恢复平方项、补历史检查、重扣税或完整逐步等价认证。若未来要求处理这些差异，需Owner明确具体口径；本轮不改算法来追求对齐。

## 冻结后可继续的工程

只允许在HA原调用返回后，由外层worker复制已有公开返回字段以补保存见证；不新增HA内部字段/钩子、不重算policy或求解器、不修改输入或返回对象、不换算子。算法和原结果均保持；既存资源、调用限额与停止保护不放宽。该工程继续不包含新科学进程。

允许的参数变化仍须具体清单和新的有限决定，HA grid原禁改规则保持；本次不开放容差/迭代控制/校准，也不借用初始化余7。当前科学运行累计5/5已用、零重试、S03未授权，启动门保持关闭。外层记录代码即使完成工程检查，也须新代码pins与新科学决定才能执行新诊断。

这是**HA算法约束冻结**，不是全项目正式来源/科学验收：FORMAL_SOURCE_FREEZE/consumer_ready/formal_ha_accepted/科学接受/Results/model_activation/REAL_GE保持FALSE，严格reference/thresholds保持null。原证据、历史dirty树、R12/R13/WASM及保护重绑定等边界保持，GitHub仍PENDING_SYNC。
