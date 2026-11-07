# CH5来源与数组守卫的原counter字节计数

日期：2026-11-07。普通工程完整交付，代码候选`a8ac09735d9a4b372d7af56c3bb51ea2c3ad1113`。本轮复用既有模块，更新ArtifactByteMeter、外部runtime guards和休眠entry三处外部源码；未修改HA、算法/网格/controls或原C/g快照格式。子代理0，真实科学运行/新额度0。

## 完整接线

字节计数器新增显式buffer物化操作：先以buffer.nbytes预留array_bytes_copied，再按指定A/C/F顺序转成bytes；短输出或异常保留容量和可知实际字节数，不退还、不伪装0。空文件和空buffer允许显式0字节操作，仍记录尝试/返回/校验；采样重入会在载荷动作前拒绝，避免守卫采样回调递归进入自身。

VerifiedSourceBytes可接入显式计数端口：重新捕获时对声明和每份源码的SHA256输入计费，所有初次/重复源码载荷读取逐次计费。来源pin、原字节、路径及reparse检查保留。基础守卫不新增项目或数值依赖；端口本身不是资格，休眠entry挂接入口要求原ArtifactByteMeter及同record/context/execution/source/grid身份。

ArrayGuard和ExternalStateGuard可对grid及输入工资/权重数组的物化字节和显式SHA256输入计费。检查所有原对象、base、shape/dtype/strides/flags和布局后才开始数组载荷读取，仍以原A顺序字节核对；转置和有步长数组与原tobytes语义一致，不改变数组或经济计算。

meter_worker_entry_guards在已有原counter建立后重新捕获带计数的来源/布局守卫，返回的entry保留同一声明、inputs、plan、request和roots。原始反序列化及初次守卫准备没有被追溯计费；这一点在新回执中明确FALSE。可在已有root阶段内调用这些守卫，同counter计数与原格式合成C/g写入/回读、root封闭共存，全部运行/科学资格仍FALSE。

## 修复与验证

首轮组合发现逐数组核对会先物化前面的正常数组，再遇到后面的坏布局。已改为先核全部布局再读数组字节，失败检查先复现后修复；原正常字节语义和守卫检查不放宽。将buffer物化移到预算预留前的变异被禁止提前物化的检查捕获，源码按原字节恢复。

| 本轮检查组 | 通过数 |
| --- | ---: |
| 新计数/来源核心 | 8 |
| 新worker/guard/root组合 | 5 |
| 原外部守卫回归 | 28 |
| 原休眠entry回归 | 16 |
| 原字节计数核心/组合回归 | 11+6 |
| 原启动封装回归 | 16 |

13新+77相关回归共90通过，不跨历史片累加；定点或变异复核不另计唯一数量。覆盖重复读取/复制费用、容量前置、空载荷、错误复制长度、源漂移保留、计数端口身份、采样重入、全布局先拒绝、A顺序非连续buffer、原worker对象与同counter阶段内守卫及root/Cg回放。NumPy仅合成容器；既有科学函数/HA实例化/外部动作禁入检查有效。

旧entry/启动测试使用历史来源清单，本轮测试副本只叠加这三份外部源码的固定SHA256差异，并核对现场精确摘要；标记test_only及不等于旧提交Blob，不反写旧清单、reference或机器pin。新增统一测试副本工具用于两处原fixture，禁止通过宽松目录扫描或忽略其他来源变化放行。它是合成工程检查，不是当前运行来源采纳。

当前机器包绑定52源码/99静态内部边（4延迟、保守装载图无环），含source_manifest、startup_contract、guard_interfaces、binding_plan。65件启动基线中62件保持现场原字节；三份授权修改的外部源码原字节保留Git和本地副本。其余49来源、前片机器记录、两份adoption和原7未跟踪项未改。工程自审不冒充独立科学审查。

## 未覆盖与实际边界

本轮计费仅针对挂接守卫及显式buffer端口。初次反序列化/守卫准备、未接入的JSON/base64/身份与grid摘要、其他loader读取、C/g快照复制、输出target守卫及其他数组/求解器/native成本仍未完整覆盖。未挂接的原路径仍可用，complete_byte_accounting与live_counts_enforced继续FALSE，不称全部开销已强制执行或内存峰值已证明。

实际原包读取/解释、真实OS/HA/科学worker、实际网格构造和新额度均0。实际原包语义适配、科学worker/capsule/声明资格、grid/参数/controls工件、可信Owner有限决定/账本、完整计数和实际OS/source/module/root/Cg证明仍缺。后续可继续完善明确外部编解码、快照和未接入计数；不得从局部计费补全未观察证明。

真实p/单位/劳动激励、RP、外层经济停止及严格科学标准仍待Owner；已定输入/Frisch/无额外z/A1/税/H/Lt_prev不重问，不补默认。actual grid hash/artifact、strict reference/thresholds及15实际预算仍null，NEW_RUN_BUDGET=0。全部运行/科学资格、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE、live_counts_enforced均FALSE；公开门拒绝。

全部旧关闭额度/STOP/16义务及历史dirty/保护基线保持，不移动缓存证据，不改Desktop/CUA/全局配置。模型代码、测试、机器记录只在本地；两树/GitHub仅同步本报告与三个CURRENT，main不合并。最终保存提交及逐文件Blob/字节/SHA256回读见本地交付回执。
