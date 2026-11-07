# O3原始消费矩阵保存与逐格Frisch劳动分配

DATE=2026-11-06
STATUS=RAW_C_G_POINTWISE_FRISCH_BRANCH_IMPLEMENTED__71_BOUNDED_CHECKS_PASS
OWNER_SCOPE=SAVE_RAW_CONSUMPTION_MATRIX_AND_USE_EXISTING_FRISCH_ALGORITHM
OWNER_POINTWISE_AGGREGATION_EXPLICITLY_CONFIRMED=TRUE
ACTUAL_HA_ENTERPRISE_RUNS_GRID_GENERATIONS_NEW_RUN_BUDGET=ALL0
SUBAGENTS=0
SYNC=PENDING_SYNC__NO_REMOTE_RETRY

## 本次Owner要求与口径

后续Owner明确答复“按上述逐格积分口径实现，不额外新增z因子”：分别保存原始C、g与原权重，逐格代入原Frisch式后按g积分，最后沿既定A1乘pH。这与本地代码候选4c4c198一致，确认问题已回答。新本地owner_pointwise_adoption.json单独记录该答复；此前范围解释及交付回执保留其历史时点。本次只补录决定，代码不改、测试不重跑、运行和额度均0，不将公式确认扩大为科学接受或实际HA运行许可。

Owner核对原MATLAB确实用汇总Ct倒推劳动后，明确要求在Python保存C矩阵，计算劳动分配时使用，继续采用原算法。本轮将原始逐格消费c(b,a,z)、原KFE分布g及原cell_weight分别保存；不把已经乘g/权重的MATLAB results.C直接带入消费负幂。

按此前已明确的有效劳动口径，逐格继续使用原Frisch幂式，不额外引入z因子；保留目的地税、迁移楔子、原phi系数及参数。该范围来自本次修改要求和已有Owner定义，不产生新的运行批准或科学接受。

## 实际改动与公式

原HA求解、正式post→原KFE→原归一化及原汇总全部保持。原汇总仍只调用一次、原Ct/Lt/At/Bt/AtTax数值返回不替换。仅在休眠外部后端的汇总返回后复制已经存在的hjb.consumption、density.density和density.cell_weight，作为同次请求的伴随记录。

新分配路径按下式计算来源i到工作地j的原H尺度劳动，再由原A1适配乘p一次：

\[
L^H_{ji}=H_i\sum_{b,a,z}
c_i(b,a,z)^{-\gamma_c/\phi_l}
\left[\frac{w^{enter}_j(1-\tau_j-\sigma_{ji})}{\phi_{ji}}\right]^{1/\phi_l}
g_i(b,a,z)\,\Delta a\Delta b,\qquad
L^{A1}_{ji}=p_iL^H_{ji}.
\]

与旧路径相比，修改的是消费输入与逐格积分：不再对汇总Ct作负幂。原Frisch指数、工资/税方向、劳动厌恶系数、H和p的处理保持；不重归一化g或来源列，不裁切或补值，不额外乘能力。

原标量Ct仍为其他消费/资产/财政接口保留。新阶段中的Ct仅作原批次的摘要身份交接，不进入劳动核计算；检查已验证修改摘要Ct不会改变新劳动矩阵。

## 保存、传递与消费

- 新outer_consumption_snapshot.py提供只读字节副本及save/load接口。dtype、shape、原strides/flags、原cell_weight、原点位/省序/轮次/网格身份和摘要随档保存；文件以新建模式写入，拒绝覆盖。
- 归档以C序列化副本仅用于保存C/g，不重排或修改原HA数组、原网格对象及其flags；原来源布局另记。读取仍只是数据绑定，不授予真实HA来源资格或消费许可。
- OriginHouseholdReply新增可选伴随记录，O2批次逐来源传递并核同一request/inputs/grid身份。旧只有标量的回复保留兼容性。
- 新outer_distribution_labor.py是当前选定矩阵分配路径。要求完整、逐来源、同请求的C/g记录；缺任何来源就拒绝，不回退Ct、不复制A替代B，也不冒充完整O2批次。
- A1新增显式矩阵来源语义及逐来源snapshot hash，仍只乘p一次。既有外层拼装核对应记录与新劳动来源hash后接收结果。
- 旧标量分配及已关闭观察作为历史兼容保留；新路线以矩阵准备入口为准，不将旧返回改标签为新算法输入或新计算结果。

本轮没有运行真实HA，因此没有真实C/g文件产生。保存函数已可用于未来获授权worker的明确私有输出位置；本轮文件读写只覆盖新的离线矩阵样例，所有旧原件/证据保留。现有公开执行门仍在构造真实后端前拒绝。

## 验证与证据边界

新检查27项：原始C/g/权重分离、字节只读、源数组不变、非连续来源布局、无覆盖归档、读取完整性和同请求/省序/轮次绑定；原生回复伴随传递；逐格手算结果、常数C退化为原核、Ct不参与核、原密度不重归一化、目的地税/楔子方向、A1只乘p一次、缺省/错省/错价格/非法域拒绝及既有单轮拼装。

因本轮修改A1、O2和拼装，另执行受影响的44项回归：A1 15、原拼装23、原生O2 6；共71项最终唯一检查通过。SciPy未使用真实求解器，原HA/企业/工资等科学生产函数尝试0、真实后端实例化0。矩阵核仅在新离线夹具上计算，不是实际经济运行。

保存功能先有预期缺接口失败；矩阵检查初次有测试导入断言变量名错误，已修正并保留原错误日志。检查过程不借用或重开旧科学worker额度。主代理工程自审不称外部独立科学审查。

静态对比确认公开执行拒绝、原阶段顺序、原initializer/HJB/KFE/AtTax边界以及原汇总调用本身未改变。HJB/KFE/原汇总算法、网格、controls均未改；旧6缓存、已消费决定和已采纳输入包原字节保持。

## 后续门与历史说明

后续静态来源准备已完成：[新矩阵路径31文件/55边绑定](CH5_O3_RAW_C_SOURCE_BINDING_20261106.md)。16接口和509静态调用位置只提供审阅定位，不是实际次数或native/运行许可；实际网格、运行环境、worker与完整计数等门继续保持未就绪。

旧按标量Ct展开的收入对应式仅适用于旧分支，不再作为新矩阵分支的关系。本次按g积分不自动证明家庭收入等价或解决H/E、真实p、单位及进入/输出工资原始量绑定；实际结果尚未取得。

现有源清单和V2环境观察只对应当时版本。新增外部模块/接口使新候选需要新的精确来源闭包与运行绑定；不修改旧pin、不重跑旧V2、不复用旧24/34证据认证当前候选。新增C/g复制、归档和矩阵计算也须纳入未来具体资源/调用清单，不把旧预算骨架当批准。

实际grid hash和严格reference/thresholds仍null；consumer_ready、scientific_acceptance、FORMAL_SOURCE_FREEZE、formal_ha_accepted、Results、model_activation、REAL_GE仍FALSE。单来源A输入采纳只保留原值，本轮不运行A/B，不生成网格、不启动HA；全部关闭额度、STOP、保护基线和16项义务保持。代码/检查/机器计划仅本地；GitHub同步仍待此前SSH问题解决，本轮不重试。

关联：[劳动与收入决定](CH5_O3_EFFECTIVE_LABOR_OWNER_CLARIFICATION_20261106.md)；[收入对应账历史](CH5_O3_LABOR_INCOME_ACCOUNT_MAP_20261106.md)；[当前状态](CH5_LOCAL_FIRST_STATUS_CURRENT.md)；[路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)。
