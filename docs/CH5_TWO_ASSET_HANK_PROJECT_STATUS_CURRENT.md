# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：zcx369658780/dissertation-ch5-two-asset-hank。
最新接受候选：51ba55709dcec2ef82163f6f9f1766ba6ff90f32；验收整合后main检查点a9420502e0b3f307a216b58fffd1b0b67d47e8bf。检查点不代表未来main固定。

## 当前状态与Owner决定
状态：OWNER_APPROVED_SINGLE_HOUSEHOLD_B_DOMAIN_EXPANSION_ACTIVE。
Owner保留原MATLAB-faithful算法、a_bar、生产ramax及生产网格，不批准经济source或D1–D3修复。Owner明确允许对流动资产b范围做一次小规模验证，但要求不要直接跑多个省份。
活动任务：tasks/CH5_MP4C_CALL725_RAH_0P07_B_DOMAIN_EXPANSION_SINGLE_HOUSEHOLD.md。
Builder默认gpt-5.6-sol / medium；本任务无模型例外。

## 已接受的前置事实
1. 原2018安徽call725原参数路径：家户rah=.09时原生初始化HJB100步未收敛、KFE非有限；725入口与历史捕获匹配。上游raw ra0约.219被clip为.09，原Zt/GovInv反馈确实执行。
2. 独立单户只改rah .09→float('0.07')并按原生算法重新初始化后，HJB第26步满足原crit<1e-7，KFE/聚合返回。该结果只支持本地收益率+初始化链敏感性，不证明.07为普适安全率或应改生产ramax。
3. 返回的.07密度并非原source-free稳态：post-loop Q存在29个upper-b向外rate；Tg的物质性残差集中在被污染法替换的row295；density加权upper-b逃逸=.6697587443279651，并由该row的隐含源数值平衡。source_escape_interpretation=SUPPORTED只限保存有限箱代数，不批准进入/退出机制。
4. last-HJB iteration operator Qh仍有21个负非对角元，独立数值有效性问题未解除。C/L/A/B只作诊断积分，Results eligibility=FALSE。

## 新单户扩箱诊断的冻结范围
原Owner提供生产家户格点：I20，b∈[-2,5]；J20，a∈[0,10]；Nz2，z∈[.8,1.3]。论文与原程序均按格点法求HJB/KF；论文也明确提醒家户分布和HJB收敛对收益率/边界位置敏感，故扩箱仅作诊断，不直接替换生产校准。

新诊断只使用已接受的安徽call725 rah=.07经济输入，不跑其他省份。为避免把“扩范围”和“变分辨率”混合：保留已捕获前20个b节点字节不变，使用相同db=7/19数学间距追加19个上方节点，得到I39、上界约12；a/z/switch矩阵、rah=.07、全部其他价格/参数、a_bar、原生初始化、helper/组装、solver、Delta1000、crit1e-7、maxit100保持。

旧bmax5=.07结果只读复用，新基线求解0。新科学预算：1次原生初始化（最多1560劳动root和1560嵌套brentq）、1次HJB（最多100 updates/direct solves）、自然到达时1次原KFE/direct solve和1次aggregate。一个Python科学进程，科学开始后不重启。firm/one-turn/controller/GE/annual/其他省年/R-PLM/dynamic/IRF/Results/MATLAB全部0。

源KFE pin公式依赖state_count；扩到39x20x2=1560时预期k=floor(.37*1560)-1=576。该伴随变化必须记录物理坐标，KFE density/aggregate比较为次级、潜在pin依赖；不得称为固定pin的纯bmax因果效应。

## 新任务主要判据
- 输入/网格绑定：仅液体维度扩展；共同20个b节点及a/z完全一致。
- HJB：停止状态、statistic、Qh负非对角元及common-subgrid描述比较。
- post-loop Q：新upper-b面外向drift/rate、Q*1质量缺口；与旧b=5已接受诊断比较。
- KFE若返回：原Tg残差、污染系统残差、density-weighted boundary escape、pin/source账本、b<=5质量、b>5 tail质量及新top-face质量；不裁剪负density。
- 仅当原source-free Tg≈0按既定128eps componentwise规则成立时才可讨论stationarity恢复；否则所有聚合仍是诊断积分。
- 单次扩箱不能证明网格收敛、生产bmax应改或边界法则已解决。

## 历史与保护
首轮53/53、raw-vb阶段解释、多轮/共同MAT初始化、P32巨大transfer/cost与sigma丢失、固定线性和旧边界规格均保留原范围；不因本任务重开。旧runtime-cache15/15年与Owner-A13/14年分开，2018修正覆盖仍未接受。
保护HJB SHA256=049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE；export blob=9e7dc9556a2b76811e78f89999abecc045886106。原D:\ResearchCode checkout、未跟踪文件、历史分支和全部科学证据只读保留，不reset/clean/stash/force-push。工作目录D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001。
