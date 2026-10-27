# 三种canonical路径与现存原件证据

| 路径 | 生成/物化表达式 | representation/年份/轴 | 这次实际见证的原件 | 初始工资税与真实绑定 |
| --- | --- | --- | --- | --- |
| A primary annual | EMPIRICAL:74–105→ANNUAL.load_primary_annual_input；write canonical_bytes | ANNUAL V2；calendar year与滚动vintage索引分开，labels来自province_axis；不保证有representation键 | 未打开宏观workbook/真实canonical；不是生成函数存在即输入可用 | EMPIRICAL:46–71共用wjt/composite_wage/wage_tax标量，非31省实测；实际采用UNKNOWN |
| B protected runtime cache | BATCH:49–60→CACHE.load_runtime_year→add_runtime_support | CACHE:13–16 representation=MATLAB_PROTECTED_RUNTIME_DATA_CACHE；2009..2023；源码检查31标签/矩阵形状 | 读到合同声明cache basename及expected SHA；实际cache原件/输出JSON未读、hash未实测 | CACHE:98–107用accepted_scalars填state；与A的payload/representation不能混为一个文件合同 |
| C Owner-A | BATCH同段的owner_a.build_input→canonical_bytes | OWNER_A:28–52的长representation；2009..2022及rolling/end-year；schema单独 | 原始source files和actual canonical未读；代码authority字符串不是当前Owner采纳 | scalars来自同factory；另有POP来源表名差异，不能自动将N判就业或人口 |

本轮唯一准确输入路径存在性检查：WORKER:155与EMPIRICAL:74–82共同给出data_local/matlab_primary_source_snapshot/中国各省省会地理距离矩阵.xlsx。**该路径MISSING_AT_EXACT_PATH**，没有原始bytes/SHA、没有解析数据；随即停止，未检查第二份工作簿或其他替代根。不能断言全仓库没有该文件。expected SHA只是源码常量，不能冒充本次实测值。原工资三Excel不作替代，MODEL_ADOPTED=FALSE。

一个可读的matlab_persistence_contract.json只声明cache身份/legacy源链，不提供本次canonical实存证明、实际year、31省行政ID、有序输入值或共同旧期tuple。batch_manifest.json与run_manifest.json只有变量root下的写入表达式，没有准确获准目录，故NOT_PROVIDED_IN_BOUNDED_SCOPE；没有探查猜测目录或隐藏私人路径。

**需区分历史与当前年份合同**：冻结任务记载历史fixed_zt_calendar_year=2020独立于2009绑定。本轮当前ANNUAL:198–230、117–133使用zt_source_calendar_year=steady year；EMPIRICAL:105仍引用fixed_zt_calendar_year旧属性名。Q02在当前ANNUAL未定位同名字段定义。保留历史2020事实为历史，当前静态字段/消费者身份差别列版本合同缺口；未运行属性访问、未诊断观察到的异常、不选择2020或steady-year科研口径、不修schema。

另一个来源差别：ANNUAL:441的primary pop表是常住人口；OWNER_A:35为就业人数，再映射POP/N。本次没有读这两张表或验证统计定义；只确认代码文字不同，N/就业/有效劳动单位需要Owner与真实原件支持，不能静默互换。

普通canonical SHA是整序列化文件指纹，不是D1完整旧期tuple digest。真实输入year/vintage、31省行政ID/轴顺序、价格与模型期、工资gross/net及劳动单位均未由实际输入见证闭合。源码标签检查只记PROVEN_STATIC，实际校验/运行都是RUNTIME_UNVERIFIED。

| 接口/经济问题 | 实际静态证据或继承来源 | 证据状态/剩余裁决 |
| --- | --- | --- |
| 目的地工资税单次 | WAGE:55–72含destination tau；MIGRATION:98–126仍origin tau；ONE_TURN:194–209调用legacy接口 | PROVEN_STATIC差异；RUNTIME_UNVERIFIED；NEEDS_OWNER，未合并R2/R3 |
| gross/net w及HA税价格 | ORACLE:131–136、159–166使用同一税后价格；WORKER:167–187传state.w与tau | PROVEN_STATIC表达式；输入w已含税与否及实际重复楔子RUNTIME_UNVERIFIED，不按FOC/预算出现两次判双扣 |
| wjt/家户w/财政Lt | 企业边际劳动价与综合家户价及财政税基的旧审阅保持 | NEEDS_OWNER；不新开firm/fiscal源，不选择工资或税基公式 |
| 家户/有效劳动/人口 | ORACLE:686–696为z加权分布劳动；ONE_TURN:203使用N作origin population；ANNUAL:441读常住人口；OWNER_A:35把就业人数表命名POP | PROVEN_STATIC字段来源差别；真实原表/统计单位/经济人口桥未核，NEEDS_OWNER |
| sigma/phi/偏好与单位 | WAGE与MIGRATION双边destination×origin输入 | PROVEN_STATIC轴接口；成本承担、phi符号/alphal及实际单位/vintage NEEDS_OWNER |
| D1旧期tuple | RUNTIME:50–56传entering callback再构造one-turn输入 | PROVEN_STATIC引用；没有真实完整w/wjt/tau/sigma/phi/N/Ct/Lt tuple witness；RUNTIME_UNVERIFIED |
| D2/D3 | 显式31省生产adapter与先隔离spy只是既定目标 | NEEDS_OWNER；D2未认证，D3本轮预算0/NOT_RUN |
