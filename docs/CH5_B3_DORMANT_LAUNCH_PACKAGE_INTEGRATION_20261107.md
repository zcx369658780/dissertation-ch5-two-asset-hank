# CH5同record休眠启动封装与字段对应核对

日期：2026-11-07。Owner接续授权内普通工程。完整工程包完成实现、必要离线检查、修复及主代理工程自审；科学运行0，子代理0。

代码候选：`299a427e6fedd8284c855d302b2c089e5c4f2f98`。新增outer_dormant_launch_package及对应检查；原49份来源未改。此前休眠入口、原始C/g及root替身组合保持，本轮负责父端启动准备及同record静态封装。

## 集成成果

给定休眠entry和其外部摘要后，将入口源码、startup合同、输入传输、capsule、四个启动参数、固定启动声明及CounterIdentity绑定到同一record。入口原字节必须匹配同一startup来源清单；capsule保存原入口字节和argv，启动声明固定源码、Python摘要、工作目录、显式子环境、bootstrap及attempt路径。counter绑定execution、来源投影、binding、声明、输出目标和声明grid摘要。这里的输出目标摘要仍为调用方显式给定，不据此宣称实际输出或其资格已取得。

准备接口不读文件、不创建文件或attempt。单独的显式只读回查核对五份已物化工件、指定Python可执行文件的字节，并检查目录/祖先的类型和reparse状态、读取前后身份及既存attempt；发现变化即拒绝，保留现有文件，不修复、不重绑、不消费。该检查不是连续OS保护、模块执行来源证明或环境运行资格。

已有native启动声明解析器接受合成封装，生命周期/backend仅作静态准备。检查中真实kernel入口被禁止调用，公开执行在文件读取、占位或实际后端动作前拒绝。独立worker的main仍在任何import前拒绝。没有增加运行开关或科学预算。

字段对应明确为：r_a←进入快照A的rah，r_b←rb，transfer_income←Tt，borrowing_rate_gap←rb_gap，wages←封存工资record的A输出，labor_weights←既有单来源单位权重合同。标量按hex位模式核对，工资/权重按保留dtype和字节解读核对；不重算价格/工资、不补税、不改Frisch/A1。

审查补强：从封存工资证据复用原观测与工资record工厂，重建原binding，并按现有元数据合同复核execution摘要，再允许封装。不能仅把传输中声明的摘要串接。此核对只针对已准备请求与原进入快照/record；实际原候选packet没有读取或解释，original_packet_semantic_mapping仍null，不把不透明原包摘要当成语义适配已完成。

## 检查与证据范围

| 本轮检查组 | 通过数 |
| --- | ---: |
| 新启动封装/字段对应/只读回查 | 16 |
| 休眠entry及输入/守卫/root组合回归 | 16 |
| native后端替身回归 | 16 |
| capsule替身回归 | 16 |

本轮16新+48相关回归，共64通过，不与历史片段相加。检查覆盖源码pin、argv/record身份、篡改摘要/上下文/价格/工资/权重、路径冲突/越界、显式环境与线程、原工件漂移、既存attempt保护、reparse拒绝、不可变包复核及公开门先拒绝。封存record校验先失败复现后修复；删除execution摘要比较的变异被捕获，源码恢复原字节。修复后定点复核不另计唯一测试数。错误与通过日志均留本地。

新本地机器包固定50源码/93静态内部边（4延迟、保守装载图无环），保留来源与两份adoption原字节，含source_manifest、startup_contract、launch_interfaces及binding_plan四份JSON。新模块接口清单不代表完整native/重复字节计数。原49来源、前片4机器记录、2份adoption及7未跟踪项共62件启动基线原字节保持。

NumPy只用于既有合成请求、布局及C/g容器；既有科学函数、HA实例化和外部动作禁入检查有效。native回归只调用替身。实际原包读取/解释、实际Win32/Job/科学后端、科学worker、实际网格构造和新额度均0。主代理工程自审不冒充独立科学审查。

## 剩余实际工件与Owner边界

启动封装工程已完整交付。尚缺实际原包的明确语义适配与合格传输，当前科学worker/capsule/启动声明采纳，冻结grid/参数/controls资格，可信有限Owner决定及消费账本，完整求解器/native/重复字节计数，以及真实OS/source/module/root/Cg证明。五件合成工件的只读回查不填这些实际资格。

后续独立普通工程可在给定请求上将启动包身份与已有输出目标/root回报合同接合，并用替身核对跨包拒绝及失败保留；不读取未开放私有载荷、不调用真实后端、不生成网格。真实原包的字段语义须有明确已开放来源，不能从摘要或旧proposal推断。

真实p/单位/劳动激励、RP、外层经济停止和严格科学接受标准仍待Owner；已定输入/逐格Frisch/无额外z/Lt_prev/A1/税/H口径不重问。actual grid hash/artifact、strict reference/thresholds及15实际预算仍null，NEW_RUN_BUDGET=0。实际worker/transport/capsule/声明槽位仍null；全部运行/科学资格、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE及live_counts_enforced均FALSE，公开门拒绝。

HA黑箱、算法/网格/controls、同inputs、a*r_a、净工资、正式post→原KFE→原归一化保持。所有STOP/关闭额度/16义务、保护基线及七件未跟踪原字节保持。模型代码、测试、机器包和私有工件仅本地；双树/GitHub只同步本报告和三个当前入口，main不合并。最终保存提交和逐文件Blob/字节/SHA256以本地交付回执为准。
