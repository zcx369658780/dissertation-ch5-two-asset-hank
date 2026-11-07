# 已采纳A输入包：获准只读语义核对结果

日期：2026-11-07。当前状态：DIRECT_FIELDS_VERIFIED_RECORD_LINEAGE_NOT_REHYDRATED。原输入包身份、六个直接取值路径及原快照一致性已核对；合格ProductionWageRecord、原生请求和worker传输尚未形成。沿[真实A返回里程碑](CH5_A_ORIGIN_RETURN_VALIDATION_PACKAGE_20261107.md)推进。

## Owner本次开放范围

Owner在明确问题“是否允许本地只读核对已采纳封存A输入包，用于字段与单位映射；不包含运行授权”后答复：

> 可以我允许，请继续。

本次只读取该3257字节封存对象，完整SHA256为8ed0fb98445ed02debfee0a971e0c728dbd583f6cc323ccfba22406b8191b225。读取前核路径祖先/普通文件、长度，打开后与读取后核身份及摘要，一致；原字节未改。未打开包中链接或引用的其它载荷。原包明细、精确定位、私有浮点值/位模式及下一只读范围提案只在本地保存，不发布原包或完整私有路径。

该包的scope明确为保存的合成外层组件输出，calendar_year和actual_grid_sha256均null，不是31省实证数据。封存的owner_adopted=false及PENDING状态保持原样；后来的owner_input_adoption.json已采纳决定继续有效，不因旧字段重新要求选择A输入，也不把读取授权转成HA消费/运行/科学接受。

## 已完成的字段映射

| 原请求/inputs字段 | 封存包取值路径 | 核对结果 |
| --- | --- | --- |
| inputs.r_a | state.rah | 与entering_snapshot[0].rah的JSON浮点位模式一致，不改成ra或r_a平方 |
| inputs.r_b | state.rb | 与A进入快照同字段位模式一致 |
| request.transfer_income | state.Tt | 与A进入快照一致，家户模型量直接交接，不在HA入口乘H |
| request.borrowing_rate_gap | state.rb_gap | 与A进入快照一致，不裁切或补值 |
| inputs.wages[0] | effective_net_wage | 与A进入快照w位模式一致；已保存的净工资标量，不重新算工资或扣税 |
| inputs.labor_weights[0] | labor_weights[0] | 包中明确保存单元素权重，符合原输入工厂约定；不补默认值，不解释成就业份额p |

保留origin=A、origin_index=0、province_order=[A,B]、生成1进入2。完整进入快照按既有ensure_ascii=False、排序/紧凑JSON格式序列化后，摘要同时与包内声明及Owner采纳记录一致；没有尝试切换格式追求hash。

上下文对应：producer_context_id供原工资record与BindingContext的同context核对；province_order/entering_iteration原样；entering_snapshot_sha256对应消费进入快照；source_bundle_identity保留生产者身份。生成快照和进入快照各有自己的摘要，不强求相同。historical_grid_metadata_identity及source_root_metadata_identity是历史元数据，不能用作当前实际网格或已装载源码证明。

以上为JSON值和接口角色核对。包内没有原生数组dtype/strides/flags/原始buffer元数据；现有构造器的只读单元素数组要求仍需在未来合格环境/record中落实。本轮未导入NumPy、未构造原生输入数组或BindingContext，不将JSON浮点位模式等同于历史NumPy数组字节证明。

## 单位与阶段依赖

原包没有显式单位字段，calendar_year=null；利率/差额、转移和净工资只能确认其现有模型接口角色，不能认定为现实年频、货币或实证人均单位。劳动力权重属于原单元素输入权重，不是A1中的p，不能据此设p=1。实际H/p/E、工资调查口径、单位/年频和收入/激励桥仍未采用。

当前OriginHouseholdRequest/Temp31NetWageInputs没有额外p字段，已采纳A请求的直接标量路径均在包中。因此后续A返回准备无需再次选择A值或临时补入p；两省完整外层劳动分配仍须真实p等口径。这个字段事实不删除现有严格接受/完整计数等门，也不证明经济收入等价。RP及外层更新/停止仍属于后续迭代的具体决定。

## 已收敛的下一缺口：原工资record血缘

包中只有fixture、producer_contract、worker_result三份来源长度/摘要引用，没有原工资输出bytes或SavedOuterWageObservation对象。fixture/producer_contract两份声明摘要与现有专用reader固定常量一致；这只核对引用，没有读取原工件。

现有reconcile_outer_wage_observation需要九角色原字节：contract、fixture、owner_decision、attempt_claim、worker_entry、process_output、trace、worker_result、final_receipt。现有测试源码已提供精确封存位置，已形成本地九文件只读范围提案；本轮九份工件均未打开，包外读取尚未授权。实际载荷须按原封存身份核对，旧最终回执/决定/claim仅为历史观察，不成为新许可。

下一步拟议仅核对这九份既有见证原字节，沿原reader准备工资记录血缘，不运行工资生产者、旧七入口、模型或科学函数，不修改旧source/claim/hash或续额度。不能从快照w列表重新序列化一份工资输出来冒充原output_bytes，也不能绕过原record工厂和消费拒绝门。

后续仍缺实际冻结grid/参数/controls、当前科学worker/capsule/声明/环境与保护、可信有限决定和15项预算、现有严格接受门的具体处置。实际root/Cg仍是未来获准运行后要取得的产物，不是本次阅读结果。

## 保存与核对边界

本地新增validators/multi_province/a_input_readonly_mapping_20261107/三个伴随JSON：owner_readonly_scope、semantic_mapping、dependency_split。旧A验证包四工件和旧空槽原样保留，通过新伴随记录描述最新只读事实，不改写旧方案或把input_packet槽自动升级为合格worker传输。

69件启动基线（52来源、前片来源/绑定记录、两份adoption、旧A包四件及原七件未跟踪项）原字节保持；原3257字节包另做读取前后身份/摘要核对。生产源码/测试未改，旧93项未重跑，本轮为标准库JSON/浮点位模式/AST核对，不是模型或科学单测。原包schema/六字段/快照摘要/历史状态与当前采纳权威均核对，包外载荷打开0，NumPy/项目模块导入/科学函数/真实OS/HA/网格/新预算均0。

本轮同步本报告、A包入口、三个CURRENT、路线图及计划/任务共八份脱敏文档；原包/值/精确路径/机器记录不发布，main不合并。当前代码候选保持6602117，运行/科学资格、Results、REAL_GE、complete_byte_accounting及live_counts_enforced仍FALSE，所有旧额度/STOP/16义务及保护保持。最终本地保存和逐文件Blob/实际字节/SHA256回读以交付回执为准。
