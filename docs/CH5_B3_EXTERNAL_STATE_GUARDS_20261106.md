# HA外部对象守卫与源码字节复核准备

DATE=2026-11-06
STATUS=OFFLINE_GUARDS_IMPLEMENTED__PUBLIC_RUNTIME_STILL_DENIED
ENGINEERING_CODE_CANDIDATE=7f09b870573a34da678c174b2766de8a5a63a43f
SOURCE_SNAPSHOT_COMMIT=7f09b870573a34da678c174b2766de8a5a63a43f
OFFLINE_NEW_CHECKS=28
RELATED_SEQUENCE_REGRESSIONS=13
ACTUAL_GRID_GENERATIONS_HA_BACKEND_INSTANCES_SCIENTIFIC_CALLS_WORKERS_NEW_SCIENTIFIC_BUDGET=ALL0
SUBAGENTS=0
SYNC=PENDING_SYNC__NO_REMOTE_RETRY

## 已完成

在Owner已确认的原始C/g逐格Frisch路径上，新增纯标准库外部守卫，并接入尚休眠的原HA后端prepare/check_identity。真实后端本轮未实例化；公开execute_origin仍在构造后端之前拒绝。

- 保持grid、四个轴/转换数组、request、inputs、context、工资record、工资/劳动权重数组、params、numerics、模块映射及模块对象、np和binding的强引用。等值替换也拒绝。
- 数组伴随快照包括type、shape、dtype、strides、writeable/C/F/aligned/owndata、base引用、数据地址与原order=A字节SHA。先检查对象和布局，再读取内容；不改变数组flags、布局或原grid hash算法。
- 原值精确检查覆盖request价格、inputs字段、context、工资record及其资格字段、参数/controls和binding。未知值或循环结构拒绝，不通过隐式数值转换补默认值。
- 源码复核要求明确绝对根、既定consumer声明原字节及外部传入的预期声明SHA；只读取固定src包或exports下的.py。拒绝越界、非规范路径、重复项/JSON键、错误长度/SHA、链接或reparse路径；Windows reparse状态未知也停止。
- 返回只读的原始源码bytes映射，可再次回读。没有compile、exec、导入或真实loader。私有构造器新增两个必填关键字source_root及expected_consumer_manifest_sha256，不从CWD推断来源。

## 检查与证据边界

28项新增检查全部通过，使用合成数组、简单配置及新建的假源码。假源码含一执行就抛错的语句，复核过程只读。13项相关回归覆盖公开拒绝、opaque阶段顺序、正式post交接、失败不重试等；没有运行旧24文件的历史hash测试或旧环境worker。最初缺模块的RED日志、首轮24项及最终28项日志分别保留，未覆盖证据。

原网格/输入hash函数、prepare_origin_execution、execute_origin、阶段驱动和六个科学边界方法共12处AST与前一提交一致。HA算法、原汇总、原网格和controls均未改。新测试仅导入NumPy处理合成数组，不是对当前完整科学环境重新资格认证。

本项是阶段边界变更检测，不是OS级防写、连续监控，不能证明中间没有临时改动后恢复。模块对象保持也不等于函数实现/实际执行来源已确认。实际后端接线仅静态核对，未作真实backend、grid或HA验证。主代理自审和第二次字节回读不称外部独立科学审查。

## 新来源清单

本地validators/multi_province/outer_external_guards_source_binding_20261106/另存source_manifest.json、operation_inventory.json、historical_delta.json和binding_plan.json。32文件、56条包内导入边、未解析0；32/32工作树字节与固定提交Blob一致。相对上一31/55清单，新增守卫模块1个、executor改变1个、共有30个保持；旧四件机器记录原字节保持。

22个选定接口、590处静态调用位置仅是语法清单，不是实际运行次数、完整函数闭包或native预算。所有实际调用上限仍未完成，不能把六阶段各一次或静态位置数作为科学预算。旧V2证据不自动覆盖新32文件候选。

## 保持关闭与后续缺口

实际grid hash/artifact、实际C/g产物、严格reference/thresholds仍null。consumer_ready、scientific_acceptance、FORMAL_SOURCE_FREEZE、formal_ha_accepted、Results、model_activation、REAL_GE仍FALSE。仅A/索引0的已采纳输入原值及A/B上下文保持；不补B或冒充完整批次。全部关闭额度/STOP和历史dirty树保护不变。

仍需将已验证源码bytes绑定到实际装载/执行模块，完成同record限定消费和输出绑定、完整有效回报/native/重复调用清单与enforcement、唯一受保护worker及适用有限决定。实际网格生成、环境worker或HA运行不能由这次工程准备触发。下一工程范围应从这些缺口中明确选定，本项不自动启动后继。

保留7个既存未跟踪文件（含6缓存与已消费决定），长度/SHA不变；已采纳输入包SHA不变。代码/测试/机器计划仅本地，治理树仅脱敏文档；不公开私有载荷或完整证据定位。此前SSH失败本轮未重试，不合并main。

关联：[上一静态来源记录](CH5_O3_RAW_C_SOURCE_BINDING_20261106.md)；[逐格消费分配](CH5_O3_RAW_CONSUMPTION_MATRIX_ALLOCATION_20261106.md)；[当前状态](CH5_LOCAL_FIRST_STATUS_CURRENT.md)。
