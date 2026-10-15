# V010：原MATLAB主线的Python基线、迭代接口及最小修错集中方案

日期：2026-10-15（Asia/Shanghai）。
**任务ID：V010_MATLAB_MAINLINE_BASELINE_AND_MINIMAL_REPAIR_PROPOSAL。**
**权限：ASTRA_AUTHORIZED_SOURCE_ONLY_MAINLINE_ALIGNMENT；不授权模型实现、数值运行或真实数据访问。**

Owner要求的16文档同步已由Astra按scope_sync_acceptance.md限定接受。此任务取代当前入口中的同步动作，仅放开下列准确SOURCE_ONLY审阅；不改变Owner主线，不重开旧V010 Newton取证，不再派一轮相同同步任务。以本任务所在Astra公布的新固定commit/tree读取，不混合动态分支文档。此前916e2b4同步镜像与回执原样保留，读取本次任务正文属于正常接续，不需要覆盖那个镜像。

## 1. 只交一个可直接用于冻结实施的方案

本次要确定：**在原HA黑箱＋有界多省顺序迭代＋GovInv/Zt自适应校准架构下，究竟以哪份已有Python代码为基线，修哪几个真实问题，按什么原方法验证。**

不是再写一份通用HANK理论报告，不研究Newton/Jacobian、不重新设计债券财政闭合，不把完整前瞻动态IRF作为前置。优先利用已定位历史审计与已接受数值修复；不从头遍历几个月文档或重建知识库。主线代码基线在本任务完成前仍UNSELECTED。

## 2. 精确来源及只读权限

先读新的CURRENT、TASK_CURRENT、V010 plan、本任务、scope_sync_acceptance，以及已同步的Owner纠偏、路线图和科学索引。只读核对治理HEAD、实际原模型HEAD/branch/common-dir、staged/dirty类别与候选关系。不要因最近人工候选最新而将它选作默认父提交。

核心已核历史来源：
docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_SOURCE_AUDIT_AND_CONTRACT_FREEZE_REPORT.md。
该文档记载原HA/单轮/外层链、GovInv/Zt触发与收敛规则；其“MATLAB primary numerical authority”等旧措辞仅历史，不能压过Owner“原程序含错、继承框架并修错”的最新决定。引用原阈值和参数只证明历史写法，不自动设为本次执行参数。

允许只读Owner已提供、在本地确能安全准确定位的一份原MATLAB ZIP中的必要.m文本：HANK_2ASSETS_HJB.m、HANK_mp_1turn.m、HANK_mp_1eq.m、mpHANK_equilibrium_2000.m、multi_prov_HANK_12sts.m、HANK_firm.m、Lt_seperate.m、wage_caculate.m及实际存在的原递推冲击入口。可读一份已提供博士论文第5.2.7/5.3节（PDF物理页100—102及必要邻页）以核研究意图。ZIP/PDF不可达则用已有精确审计定位并写NOT_IN_CODEX_VIEW，不擅自遍历历史审计中的受保护本地根；不打开ZIP内.mat或原始工作簿/数据缓存。

Python只在本仓已知Git源及其直接数学依赖中寻找原有one_turn/steady_state/household adapter、firm、migration_labor、wage、government_assets、货币财政、外层参数更新与原冲击路径的对应实现。允许有限git ls-tree/show/log/diff读取版本与精确源，不fetch/pull/checkout或动原index。需要核本地未提交实现时，只读已知两个普通源码差异：src/ch5_two_asset_hank/multi_province/government_assets.py和validators/multi_province/annual_observed_labor_diagnostic/middle_stage.py；不覆盖、不暂存、不自动纳入推荐基线。其余dirty仅路径/类别核验，不全树扫描。

现有corrected_diagnostic中已接受的HJB/KFE与聚合修复，按实际采纳文档及具体函数核兼容性；不能把旧top-level/source-faithful标签或某个toy PASS当整个新主线已认证。不运行任何这些函数。

## 3. 四项实质核对

### A. 明确可继续的原方法代码基线

给出一个首选Python基线建议及真实commit/tree/parent、是否含所需HJB/KFE修复、是否保留原单轮/外层结构、与原工作树dirty和人工支线的关系。若一份commit无法同时满足，给最小的准确源文件/已接受修复组合及理由，最多一个备选，不生成新的实现候选或自动合并。

原MATLAB参考身份、Python源忠实/修正后目标身份、V008/V009人工辅助身份分列。源码版本与历史运行/数据身份不能混称。恢复主线不是checkout旧HEAD并重新带回已证bug。

### B. HA黑箱到外层校准的最小接口图

每个接口列实际文件/函数/行段、输入、输出、单位、状态覆盖顺序和当前缺口：
1. HA输入资产域、rb/rah/w、税/转移及本省参数，输出Ct/At/Bt/Lt/分布及已有统计；Gini只核已有输出，不新造不在程序中的实现。
2. 单轮：各省HA → 迁移劳动 → 私人资本供给/持有收益 → firm → 综合工资/货币财政 → 下一轮。
3. 外层：GovInv/Zt调节、阻尼、数据目标、价格边界/触边标志、全省收敛退出。明确rb是原货币规则输出、Tt是否固定、GovSurplus是否诊断等原角色，不预设另一套未知量/残差根。
4. 稳态校准、校准冻结后的验证、原冲击递推三个阶段分别核变量角色。尤其查冲击期是否继续调整Zt/GovInv、是否会抵消注入的冲击；只报告实际行为和需修正的问题，不默改原动态规则。

### C. 主线修复与旧科学决定的最小冲突清单

逐项分类“可直接复用 / 有原证的bug需最小修复 / 重要科学差异待Owner裁决”，至少核：
- 原GovInv按收益边界调节与后来C1=max(Ktarget-Kprivate,0)：在实际Python caller中哪个生效，二者在哪一步冲突。提出恢复原方法角色的最小方案，保持C1历史接受，不默认强制其中任何一式进入新主线；若须Owner选择，把这一项集中讲清，而非发多份任务。
- 原价格边界、raw/used回报、触边退出与K1 raw-ra0/lagged，同S数量收益。避免把“在可行价格范围寻找固定点”误作允许用clip隐藏残差，也避免不受界价格搜索进入主线。
- phi来源减目的/人口人均/双边轴；max_phi=.3机制保留，人工1:2参考比不移入现实31省。
- Lt在HA与firm前后赋值、来源/目的劳动单位、工资税是否重复、AtTax/Tt角色、资本数量或收益遗漏。只依实际源确定bug；未解释项标缺口，不以新增Bt=Bgov、内生T或竞争性模型代替核查。
- 已接受HA数值算法和新接口的兼容性：保留必要的HJB/KFE验证与历史修复，不重新发明家庭模块，不因它是黑箱便跳过科学有效性。

### D. 直接可执行的同V010后续长任务建议

提出一份最小允许代码路径清单和一套验证次序：原/修正目标的同输入HA对照 → 单轮字段/顺序/边界回读 → 按原外层逻辑的有界小规模运行 → 逐步多省稳态及原递推冲击接口。只设计，不执行。

明确哪些测试可在纯人工接口层完成，哪些必须使用指定现实数据、模型运行或待Owner批准的更新律；一次性提出相称的实际资源/调用预算和保护要求，不能把旧耗尽额度拿来续跑。需要年度/校准原件时列精确缺项及来源请求，不打开其内容。

优先复用已有主线程序完成实质修错，避免输出大量新治理文档、全部源重审或新的模型规格。将“原方法数值复现”“针对已证bug的修正版”“经济/论文解释”分账；对有bug的原值不强求Python修正版继续精确一致。

## 4. 窗口、禁止项与交付

一次集中SOURCE_ONLY，最多3小时；精确Git/普通源码/必要合同最多60份、文本累计不超过4MiB。已同步并已审段落可按准确来源复用，不为凑数重复读取。必要Owner提供PDF≤16MiB、ZIP≤3MiB各一份，单独记真实读取身份/文本页或成员，不属于现实经济数据授权。超过或访问不能安全定位时，只报告缺口，不扩范围。

新科研调用、HJB/KFE/selector/scalar-root/宏观迭代/Newton/IRF/pytest/MATLAB执行均0；真实C8/2017/2018 JSON/NPZ/CSV/MAT/Excel及B3/旧V009失败数组的stat/read/hash/parse均不允许。普通只读Git/文本差异、受界PDF或ZIP文本抽取可用，不import研究包；临时文本工具输出仅在安全独立临时区≤8MiB，记录后不触原仓和证据。禁止任何模型/参数/网格/科学合同修改、代码候选、git commit/push、重新同步覆盖那16个已接受文档或修改本地QMD/BasicMemory。

唯一报告名称：V010_MATLAB_MAINLINE_BASELINE_AND_MINIMAL_REPAIR_PROPOSAL。
直接在当前Codex会话集中交付：①推荐baseline真实Git身份与保护；②HA—单轮—外层—冲击接口图；③最小bug及科学冲突表（最多3项真正Owner新决策，不重复已采纳的主线）；④一份可据此冻结实施的精确修复/验证任务；⑤实际源读取、未证事项及零科学执行账。

完成即：WAIT_ASTRA_V010_MAINLINE_ALIGNMENT_PROPOSAL_REVIEW / STOP。
不自授科学ACCEPT，不自动实施、不恢复旧Newton调查、不启动V011。既有A16/window/C9/CALL_LEDGER/model_activation=False/Results FALSE和旧预算保护保持。工作流V1.2不改，此任务不是新同步微版本。
