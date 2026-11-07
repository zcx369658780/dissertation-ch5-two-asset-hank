# worker休眠入口、输入传输反序列化与外部保护接线

日期：2026-11-07。Owner接续：“可以，请继续”。工程验收：休眠入口和给定请求的输入往返/守卫接线完成；真实科学入口调度与运行资格未建立。子代理0。

工程代码候选：`56ce2934cb8bba11445844aae383fc966e7f24e9`。新增outer_worker_input_transport、outer_dormant_worker_entry及对应检查，原47份来源未改。

## 完整实现成果

输入传输格式绑定已准备A/0第2轮请求、A/B上下文、原进入快照、来源计划、封存工资证据及原候选packet摘要。原候选packet只作为不透明字节保留，不解析其内容，不读取实际私有候选、不从它补选数值。价格用原float的hex形式往返，工资/权重分别保留dtype、shape及字节；不舍入、不重税、不回退19或Ct、不增加z，也不重新调用工资生产者。

反序列化复用原工资观测核对、工资record适配、BindingContext、Temp31NetWageInputs、OriginHouseholdRequest及原执行准备接口。还原的是worker内部新对象，各阶段共用同一个request/inputs/record；不要求跨进程保留父进程对象地址。重建后核对binding/execution/工资观测摘要和数组原字节，不能用等值替代对象冒充同一worker内的原对象。

完整来源清单带有Git等注释字段，而原consumer只接受path/sha256/byte_count三字段。新增确定性投影，保留原完整清单及外部摘要，三项原pin值不变；未放宽旧接口字段校验或改写历史清单。启动合同绑定原清单，传输中的来源计划必须精确匹配该投影。

休眠入口的main在独立脚本执行时先拒绝，再到任何import；公开执行入口在反序列化、文件读取或后端构造前拒绝。没有运行许可开关、pickle/eval或任意代码解码。入口源码候选已经存在，但actual_worker_program/capsule仍未采纳，不能称科学worker已获准安装或运行。

私有离线准备路径只重建给定请求并接入既有VerifiedSourceBytes与ExternalStateGuard。grid/params/numerics/modules均须显式给定，不生成或补默认。adapter参数必须就是守卫监控的adapter模块，角色集合须完整，错配在解码前停止。给定grid字节须符合声明摘要；该核对不证明它是实际冻结网格或来自已采纳参数/构造源。

守卫被接到既有counter采样边界之前。源码、对象身份、数组布局/字节/flags、参数或模块别名变化会阻止后续采样/阶段；既有不透明后端六阶段→原格式合成C/g写入/回读→声明root封闭已在该守卫下通过。边界检查不等于连续OS保护、实际装载源证明或完整调用预算。

## 必要检查、修复和证据边界

| 检查组 | 本轮通过数 |
| --- | ---: |
| 新休眠入口/输入反序列化/保护组合 | 16 |
| 原启动静态合同回归 | 18 |
| 原外部对象/源码守卫回归 | 28 |
| 原root/Cg组合回归 | 17 |

本轮16新+63相关回归，共79通过，不与历史片段相加。覆盖原字节/浮点位模式、worker内原类型与同对象关系、外部pin、坏证据/非有限数/object dtype/长度、独立入口先拒绝、源码投影、声明grid身份、布局/参数/record替换和guard-before-sample。来源投影保持旧三字段合同；adapter与监控角色错配先失败复现再修复，删除该身份判断的变异被捕获，源码恢复为已通过检查的原字节。错误和通过日志均留存。

只在本进程使用已封存的合成工资证据、合成输入packet副本及小型布局/Cg数组夹具。NumPy用于数据容器与字节往返，科学函数/HA实例化/外部动作禁入检查有效。没有实际原包读取/解释、真实HA实例、科学求解器、实际Win32/Job后端、科学worker进程或实际网格构造；不迁移旧V2资格或复用旧额度。

一次性绑定49份来源、90条静态内部边（4延迟，保守装载图无环）。新目录`validators/multi_province/outer_dormant_worker_entry_20261107/`保存source_manifest、当前startup_contract、entry_interfaces及binding_plan四份JSON。接口清单仅覆盖新两模块，不宣称完整native/字节计数。49份源码字节/Blob和来源投影第二次回读一致；原47来源、上片4机器记录、两份adoption、原7未跟踪文件共60件启动基线原字节保持。主代理工程自审不冒充独立科学审查。

## 剩余实际工件与许可

实际原候选packet到请求字段的语义适配尚未完成；本轮不会把不透明原包的摘要匹配宣称为内容已解释。当前实际传输工件、冻结grid/参数/controls来源资格、科学worker/capsule/启动声明采纳、可信Owner账本和有限决定、完整求解器/native/重复字节计数，以及实际OS/module/root/Cg证明仍缺。

后续普通工程可把休眠入口和传输摘要与已有capsule/固定启动声明做同record静态封装，并准备原包到请求的明确适配；不借此读取未开放私有载荷、生成实际grid或启动真实后端。真实p/单位/劳动激励、RP、外层停止和严格科学标准仍待Owner；已定输入、Frisch/A1/税/H/Lt_prev不重问。

actual grid/strict reference/thresholds、15实际预算和实际输入传输仍null，NEW_RUN_BUDGET=0。全部运行/科学资格、consumer_ready、formal_ha_accepted、FORMAL_SOURCE_FREEZE、Results、model_activation、REAL_GE、live_counts_enforced及完整native/字节资格均FALSE。HA/网格/controls、a*r_a、净工资、原post→KFE→归一化及全部保护/STOP/关闭额度不变。

双树/GitHub仅同步本报告及三个当前入口，模型代码、测试、机器包与原始载荷/完整私有路径只留本地；main不合并，Desktop/CUA/全局配置未改。最终提交与逐文件Blob/字节/SHA256回读见本地交付回执。
