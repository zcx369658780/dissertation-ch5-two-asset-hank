# Call725 rah=0.07 单一安徽家户流动资产域扩展诊断报告

- Diagnostic completion: `COMPLETE`；exact grid intervention binding: `PASS`。
- HJB status: `CONVERGED`，17次更新，统计量 `7.140894586754598e-08`。
- Expanded upper-b truncation: `PERSISTS`；source-free stationarity: `FAIL`。
- Truncation sensitivity: `EXPANSION_DOES_NOT_REMOVE_BOUNDARY_PRESSURE`。
- Results eligibility: `FALSE`。

## 输入与网格绑定

唯一新科学对象是2018安徽call725、`rah/r_a=float('0.07')`家户。旧 `.07` 结果来自只读证据 `D:\ProjectTemp\ch5-call725-rah-0p07-native-init-20260908-002`，未重新求解。除液体资产网格外，state、价格、EconomicParams、a、z、switch matrix、native initializer、helper、solver、Delta1000、crit1e-7、maxit100和drift tolerance均保持保存值。

旧20个b节点与新网格前缀逐位相同。保存binary64 db=`0.368421052631579`（`0x1.79435e50d7944p-2`），以逐节点binary64加法追加19个节点，最终I=39、state_count=1560，端点=`12.0`（偏离数学12为`0.0`）。a/z/switch逐位相同。新原生V0/l0在共同20x20x2子网格上各800/800逐位相同，证明没有热启动、插值或旧最终值复制。

源pin公式机械给出零基k=`576`；F-order索引 `(i_b,i_a,i_z)=(30,14,0)`，一基索引分别为`(31,15,1)`，物理坐标 `(b,a,z)=(9.052631578947366,7.368421052631579,0.8)`。旧pin为295，因此分布和聚合变化不能解释成固定pin下的纯bmax效应。

## HJB、算子与边界

扩箱HJB在17次更新后收敛，统计量 `7.140894586754598e-08`，完整value有限。最后迭代Qh有 `11` 个负非对角元，最小 `-3.464832800963844`；它与post-loop Q分开报告。post-loop Q负非对角元0，但 `Q*1` 最大绝对缺口 `3.4690347703114806`；按保存drift重建遗漏外向率后，`Q*1+ell` 最大绝对值 `2.942091015256665e-15`。

新upper-b=12仍有 `17` 个外向单元，最大rate `3.469034770311481`、未加权总rate `16.296417971077133`。lower-b、lower-a、upper-a外向单元均0。相对旧bmax=5的29个单元、最大rate约4.00987，边界计数和最大rate下降，但压力没有消失；单次扩箱不构成网格收敛证据。

## KFE、质量与分布

原adapter自然进入KFE并返回；原污染行直接求解raw有限。污染系统残差inf `1.6479873021779667e-17`，但未修改原转置 `||Tg||inf=0.5206986084614471`、尺度比 `0.11601750528081986`，超过冻结128-eps逐分量零界 `2.842170943040401e-14`，所以source-free stationarity明确FAIL。

归一化总质量 `0.9999999999999999`；b<=5质量 `0.5327650526244969`，b>5尾部质量 `0.46723494737550303`，新top face质量 `0.06835756005310577`。保留 `74` 个精确负density，带权负质量 `-2.394789364535285e-19`，未裁剪。density加权边界逃逸 `0.10096648917534981`，全部来自upper-b。

pin候选补偿源 `0.10096648917534987` 与 `escape-delta+offpin=0.10096648917534987` 差 `0.0`，冻结界 `2.842170943040401e-14`，有限箱质量账本通过。这只说明row replacement在保存解中补偿遗漏流，不采纳经济进入/退出法则。

诊断聚合：C=`10.734838396557656`，L=`0.6555579019227917`，A=`8.002891962174854`，B=`4.739916654430715`，A+B=`12.742808616605569`。由于Q不守恒且pin从295移到576，这些是次要、pin-dependent诊断。

## 调用账本与检查

唯一科学进程/worker正常返回，耗时 `5.296999999991385` 秒；科学重启0。native initialization1；labor root1560；nested brentq1560；adapter/HJB各1；HJB更新/直接求解17；KFE/直接求解各1；aggregate1。失败进入也计数。旧bmax=5新增调用0；其他利率、省份、firm、one-turn、GE、年度、MATLAB、IRF、Results均0。

合成测试覆盖嵌套网格、唯一维度变化、pin F-order、预算、无热启动、保存顺序、边界流、带符号质量和import-time零科学。首次 `...-001` 仅在旧manifest未登记science index的预检断言停止，科学进入0；正式证据根为 `D:\ProjectTemp\ch5-call725-rah-0p07-b-domain-expansion-20260909-002`。首次测试控制台编码失败未形成测试产物，随后一次9项运行暴露递推步长断言和合成稀疏格式问题；修正后9/9通过，失败与成功日志均保留。生产源码、参数、边界法则和solver均未修改。

本结果只支持：在这个单一安徽家户输入上，扩展到b=12降低但未消除upper-b压力，HJB收敛而KFE source-free stationarity仍失败。它不授权生产bmax=12，不证明网格收敛，也不解决既有generator、P32、sigma或年度接受问题。
