# O3 A1：H/p/E接口与预给定劳动矩阵适配

DATE=2026-11-05
STATUS=BOUNDED_A1_SCALE_INTERFACE_ENGINEERING_COMPLETE__REAL_P_NOT_ADOPTED
GOVERNANCE_PARENT=aa5c0ea09934e884658610b1946226ef43282d70
MODEL_PARENT=428b77eaf53dc3f0a42ec58a2b7c543684be2b34
MODEL_CODE_CANDIDATE=79f41ddbbee1bfe362fc26896887ac3000ddb39f
MODEL_CODE_CANDIDATE_TREE=629e753dcab36bb94f099963b343921774de08c8
MODEL_BRANCH_AND_CODE=LOCAL_ONLY_NOT_PUSHED
NEW_SCIENTIFIC_RUN_GRANT=NONE

## 已有决定与来源核对

沿Owner已选A1：家庭资产/消费/财政使用H，企业劳动规模E=pH；保留原消费驱动劳动核与目的地税，不采用A2归一化。复用10月22日主体映射记录及10月23日A1决定，未重开A/B或A1/A2。

10月22日资料已区分H_resident、E_origin、E_destination、工资调查年度平均覆盖和企业有效劳动。p在本接口声明为来源地居民就业人数相对同分母H的份额，不把工作地就业人数、劳动力参与率、工资调查覆盖人数或工资总额/均值推算值替代它。

历史SOURCE_ONLY终审只认证10个非NA候选格分布7省，I/S实际均0；其中多为工资，少数人口/人数候选并非同口径完整就业面板。它不构成7省已有完整p，更不构成31省p已被采用。本轮限定的当前annual.py及mp4b入口字符串/字段核对没有发现显式p字段；不能据此断言全部历史附件不存在p适配器或所有外部数据都缺失。本轮不读取私有workbook、不补抓官方来源或重做旧资料盘点。

固定历史来源：
- [10月22日映射路线](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/aa5c0ea09934e884658610b1946226ef43282d70/docs/CH5_TEMP31_2018_EMPLOYMENT_WAGE_IMPUTATION_LABOR_MAPPING_ROADMAP_20261022.md)，Blob 8535c07350f22429ba2a5aad64e6314f71e0cd83。
- [10月22日限域终审第3—4节](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/aa5c0ea09934e884658610b1946226ef43282d70/docs/CH5_TEMP31_2018_EMPLOYMENT_WAGE_MAPPING_FINAL_INDEPENDENT_REVIEW_20261022.md)，Blob f2f043bacefb1157937e15ed1c078327bbb7d243。该日“未选A/B”为历史时点，后续Owner的A1选择优先；其中推荐的守恒迁移矩阵不替换当前A1原量式。
- [10月23日A1决定](CH5_O3_LABOR_WAGE_TAX_DECISIONS_RECOVERED_20261105.md)及后续已采纳工资税/H财政聚合保持；不恢复旧离线派单流程或已关闭预算。

## 本轮独立工程

仅新增模型树：
- src/ch5_two_asset_hank/multi_province/outer_a1_scale.py
- tests/test_outer_a1_scale.py

prepare_a1_scales核对共同BindingContext及进入快照原字节SHA256，按同一来源省序读取N并保留为家庭H。p须逐来源地显式提供，携带同一上下文、H分母单位ID和来源引用；没有p默认值，不从工资或其它人口字段估算。来源引用与单位ID只是数据声明，不证明真实来源已采用。

输出只读A1ScaleLedger，分别暴露household_h_by_origin和enterprise_e_by_origin，E仅计算H*p。H沿原源输入正值域，p沿所声明居民就业份额的[0,1]域；这不是新增科学接受阈值。空/重复/错序、缺p、错上下文/快照/分母、工作地或参与率角色、不合法标量均拒绝。real_data_accepted及执行/科学接受/激活标志保持FALSE。

apply_a1_employment_scale仅接受**预给定**、已按目的地税处理、含原消费驱动核和H尺度且未归一化的来源劳动矩阵：

```text
E[i] = p[i] * H[i]
L_S0[j,i] = original_consumption_kernel[j,i] * H[i]  # 由外部提供，本文不计算核
L_A1[j,i] = p[i] * L_S0[j,i]
L_supply[j] = sum_i L_A1[j,i]
```

它核对矩阵上下文、原H、轴/shape/非负有限值和原量式语义，重建工程规模账以拒绝派生量或资格篡改，然后按来源列乘p一次。既不重算q，也不按HA劳动/就业人数归一化，不重复乘H/E/z。输出矩阵、目的地劳动和原H分别保留，不据来源标签认证真实劳动函数调用。

## p=0与原接口边界

当前temp31_worksite_tax.py的Temp31LaborInputs在构造时要求传入人口尺度为正；直接把E=0塞入该旧参数会被拒绝。本适配选择消费原H尺度L_S0，再按列乘p，保留原核和该构造器，不把p=0改成小正数或改写科学源码。p=0按A1代数保留零E和零列。

这只是预给定矩阵接口上的处理，不是已执行原工作地税函数，也不证明目的地企业劳动必为正。后续若某目的地供给为零，原企业正值门保持，不伪造可行值。源量式与A1数据身份仍需真实接线时的见证。

## 检查结果与边界

15项限定玩具检查通过：H保持与E计算；非对称矩阵的来源列缩放和不守恒归一化；p=0；缺省/错序/重复；分母/角色/来源声明；非法p/H与原快照字节、缺字段、重复键/非有限值；陈旧上下文；派生规模/布尔冒充数值及资格篡改；矩阵原H/上下文/语义、shape/数值/行和溢出；结果只读、未接受状态；31个虚拟来源地标签及导入限制。

测试用python -B及sys.dont_write_bytecode=True，经独立命名空间只加载标准库绑定/工资工程校验/来源预检常量和新模块；不加载HA包初始化或既有劳动、企业、工资、初始化、HA等科学生产者，不加载真实p或科学数组。31是工程标签，不是模型运行。此前财政18项、工资税14项、家户财政13项、O1/O2与历史51,159项检查未重跑。

ENGINEERING_CHECKS=15_PASS
NEW_CODE_PATHS=2
EXISTING_SOURCE_EDITS=0
SCIENTIFIC_PRODUCER_IMPORTS=0
SCIENTIFIC_KERNEL_CALLS=0
MODEL_RUNS=0
REAL_EMPLOYMENT_PANEL_ADOPTED=FALSE
HA_ALGORITHM_AND_GRID_EDITS=0
NEW_SCIENTIFIC_RUN_GRANTS=0
SUBAGENTS=0
REVIEW=MAIN_AGENT_SELF_REVIEW__NOT_INDEPENDENT_SCIENTIFIC_REVIEW

完整日志、历史角色证据、Git现场及6份旧缓存字节/SHA256保护和交付回执LOCAL_ONLY保存。模型分支和代码仅本地，远端仅脱敏治理文档。

## 下一步

A1的显式H/p/E接口和预给定原劳动矩阵适配已完成；真实p面板、单位/来源资格及完整O3仍未完成。下一工程目标为将O2家户批次、同轮原工作地劳动结果、本A1适配、资本/企业/工资和已定财政账接入独立外层一轮，企业用E对应的A1劳动，家庭资本/财政继续用H；不复制HA、不运行旧年度runner、不把保存单省结果充作完整批次。

真实科学生产者调用与模型运行须对应前瞻有限许可，旧TEMP31 7/7、Moll 3/3、工资/补录保持关闭，初始化旧余量仅原8格。严格reference/thresholds仍null；科学接受、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE。R12/R13/WASM、保护重绑定、16项义务及历史dirty树/原件/索引/缓存/LOCAL_ONLY保护保持，不合并main。

当前入口：[路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)、[任务清单](../tasks/todo.md)。
