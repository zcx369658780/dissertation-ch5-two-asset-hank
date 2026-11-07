# Owner长期网格授权与冻结工件保存

日期：2026-11-07。当前状态：ACTUAL_FROZEN_GRID_SAVED_AND_READBACK_VERIFIED_NOT_RUNTIME_QUALIFIED。

## 最新Owner决定

> 我授权，并且从现在起允许你生成中小规模网格（此授权长期有效），请继续

这是从本次决定起持续有效的中小规模网格生成许可。今后在已定科学定义和已授权范围内生成中小规模网格，不再逐次向Owner申请；不擅设到期日或把800格当成Owner规定的长期上限。若新的规模/取值改变冻结科学定义、路线或受保护资产，仍按具体影响处理；此许可不授予HA、初始化、HJB/KFE、原汇总调用或新的科学运行预算。

该决定覆盖当前入口中“生成仍未授权”的旧状态。旧plan/recipe/回执中的construction_authorized=FALSE、actual_grid=null保留为历史，不反写旧记录；本轮以新增伴随记录登记实际值。已采纳输入/逐格劳动等决定不重问。

## 本轮实际完成

仅生成一套已冻结20×20×2、b/a/z顺序的800格网格，沿原构造表达式及原switch_matrix；原八项EconomicParams、四项MatlabFaithfulHJBNumerics同时实例化封存，未选择新参数或controls。controls是原求解控制值，不是新的严格科学接受阈值。

四份数组以禁止pickle的NumPy文件保存并回读，合计数组原载荷368字节；同时保存原shape/dtype/strides、writeable及C/F连续标志。原构造参数数组与构造后网格轴在本进程为同一对象，原标志未改。重新读取后是新对象，仅证明相同字节/布局，不声称跨进程同对象或已安装worker守卫。

实际网格摘要：`1cc6002840d6a3dfef899c98d09f4796a8e14ccb9116a7952cdf78ab50305258`。

摘要使用原outer_ha_blackbox_executor的_array_identity/_grid_identity：四轴各按shape、dtype.str及tobytes(order='A')摘要，随后沿原UTF-8 canonical编码摘要。保存文件本身SHA与数组载荷SHA分列；此值来自实际数组，而非旧合成grid_metadata_identity。参数/controls的数值、JSON回读浮点位模式及canonical摘要一致。

为避免导入整个科学包，仅在本次隔离命名空间执行原数据类AST及原身份/canonical函数；构造参数直接从原annual源码AST取得，网格构造AST摘要与已封存recipe匹配。exports与contracts两处EconomicParams的AST一致。未改生产源码，也未调用原annual函数、初始化或科学路径。此对象不是目标worker已加载的原生实例，不构成模块/环境/源闭包准入。

## 核对与剩余缺口

| 已具备 | 限定含义 |
| --- | --- |
| A包六直接字段/快照、原九见证数据record | 沿用上轮只读结果；本轮未重放工资生产者或旧七入口 |
| 冻结实际grid、参数、controls及各自文件/原字节摘要 | 本轮已生成保存并回读；未来装载仍需对同一工件核对 |
| 76件启动基线/原七件未跟踪文件保持 | 含上轮新增四JSON；原52来源/旧adoption/STOP等未改 |

下一必要工程为A/0目标worker原生输入、原record的合格传输、来源/环境/模块/保护的具体接线。现有PRODUCER_INVOCATION_NOT_VERIFIED拒绝不被网格授权覆盖。当前worker/capsule/声明与适用消费证明尚未齐备，未生成request或启动worker。

真实A返回仍需要适用的有限HA决定及15项实际预算、首次返回与严格科学接受门的具体适用规则，以及将来运行中/后的真实OS、同输入、root、原C/g/权重工件。strict reference/thresholds及15项实际预算继续null，NEW_RUN_BUDGET=0；不使用旧关闭额度或旧V2资格。

真实p/单位/劳动激励、RP、外层经济停止及严格接受标准仍待具体科学决定。A-only不补成完整两省或31省结果；主路线、HA整体黑箱、算法、科学网格定义、原controls、净工资、a*r_a及正式post→原KFE→原归一化保持。

本轮科学包导入、HA/初始化/求解器/原汇总、真实科学OS后端与worker均0；旧93项不重跑，未新增通用包装/计数框架。工程核对为实际数据构造/封存/回读和主代理审查，非独立科学接受。consumer_ready、formal_ha_accepted、FORMAL_SOURCE_FREEZE、Results、model_activation、REAL_GE、complete_byte_accounting、live_counts_enforced均FALSE。

## 保存

新增本地机器目录validators/multi_province/frozen_grid_artifact_20261107/，含长期授权、实际身份及剩余依赖三份JSON；数组、参数/controls、完整manifest和生成/回读回执在本地证据目录。机器记录和数组不发布。两树仅同步本轮十份脱敏文档/入口；源码/测试未改，原证据、缓存、保护基线及全部关闭额度保持。

本轮GitHub首次读取治理ref发生传输错误，原失败记录保留；后续同工具/同分支读取已恢复，现场治理HEAD为98f22379f96b9d074ea9367cb602a6511b093d9b。本轮十份脱敏文档随后按该父提交/租约发布，最终HEAD和逐文件Blob、实际字节/SHA256回读以新增交付回执为准。main不合并，不换协议/账号，不强推求同。
