# A/0首次返回预算适用性与有限额度提案

日期：2026-11-07。工程状态：ACTUAL_A_PARTIAL_BUDGET_DECLARATIONS_VALIDATED_NOT_EXECUTABLE。候选95fbdd4eca230bb3df9fbb3e2bf6089724fbfbbb。本报告完成预算声明及实际A数据集成，最终可执行运行包尚未完成，不是运行批准。

## 范围与额度提案

沿用[Owner已采纳A](CH5_OWNER_A_FIRST_RETURN_POLICY_ADOPTION_20261107.md)：仅原A/0、生成1进入2、A/B上下文、原20×20×2网格、八参数/四controls。原3257字节包及grid身份保持，不执行B、外层迭代或自动重试，不重问A政策。

| 必须有限的保护项 | 本轮数值提案 | 含义及限制 |
| --- | --- | --- |
| workers | 1 | 仅A单工人，不并发B |
| wall_clock_seconds | 300秒 | 工作截止上限，包含启动准备；不是完成时间预测或收敛保证 |
| process_commit_bytes | 3 GiB（3221225472字节） | 拟Job/进程内存上限；当前可用物理资源未认证 |
| output_bytes_written | 2 MiB（2097152字节） | 原800格C/g结果与元数据的单份输出写入上限；超限停止，不截断 |
| output_bytes_read | 2 MiB（2097152字节） | 对同一结果文件回读的累计上限 |
| output_file_count | 1 | 原origin输出工件一份；不是把全部监督证据排除后就声称完整输出受控 |

拟议总尝试1次，包括首次资源取得前的持久预约；准备失败、部分输出和超时均消费该次，不自动重试，不换目录续额。额外拟议8192条声明事件上限（保留STOP位置）、5000毫秒清理等待；清理不增加科学工作时间，也不授予额外尝试。这些均为本轮新提案，不复用旧120秒/2 GiB或任何关闭额度。

九项固定后置：root_solve_entries、residual_evaluations、effective_return_entries、hjb_iterations、sparse_solver_entries、native_subcalls、source_file_bytes_read、array_bytes_copied、serialization_and_digest_bytes。其提案值为null，明确未完整执行对应限额；能看到的声明事件仍保留计数，不代表完整native/重复调用/字节库存。不是无限预算已获准，也不用任意大数掩盖缺口。

**15项实际批准预算、实际Owner运行决定和批准尝试数仍null，NEW_RUN_BUDGET=0。** 严格reference/thresholds对本首次返回阶段已允许后置，不重新提交政策问题；正式科学接受仍未满足。

## 工程实现与验证

复用outer_counter_replay：默认prepare_counter_replay仍要求15项显式非负整数；政策专用prepare_first_return_counter_replay先核政策摘要、原A包、原plan/网格/来源/绑定身份，再接受恰好六项正整数和九项null。工人必须1，缺项、额外项、布尔值、零保护值、九项中填数和错plan均拒绝。worker/output摘要在此只是声明，实际身份在后续完整包中绑定。

政策专用回执列checked_limit_keys和deferred_unenforced_limit_keys，replay_limits_checked=FALSE、complete_byte_accounting=FALSE；六项只是对提供的合成事件/采样做检查，不是实际OS监测或运行许可。政策绑定摘要进入链种子；原默认链种子、回执和事件格式保持。

11项新检查通过，包含六类硬上限、九项后置声明、冻结默认路径、错政策/原包/plan拒绝、STOP留存及原六阶段/root/合成C-g输出回读。相关31计数、16政策、24替身生命周期、17根输出回归分别通过，不与历史或重复覆盖累计为唯一测试总数。三种默认路径与原版逐字节比较通过。内存中将正数条件故意放宽后，五类零上限子检查失败，恢复原函数；工人0仍被固定1拒绝，源码未被该变异修改。

所有带科学禁入守卫的本轮检查均记录禁止科学源码尝试、外部动作、SciPy sentinel调用0。测试中的C/g为替身矩阵。审查为主代理工程自审，不是独立科学审查；未重跑历史整套93项。

当前53来源/106静态内部边、未解析0，eager DAG无环；相对上一候选只改计数器和政策两个来源，不增加通用框架。新来源伴随清单逐文件核提交Blob/工作树字节；旧pin/manifest及历史null不改。实际A沿原reader/工厂/codec复建当前计划，政策和新预算声明通过；原包、A/B快照、工资和向量字节保持。新传输116769字节/startup128635字节已保存回读，字节数相同不表示摘要相同。

本次实际A检查只装载11标准库元数据模块与两原数据AST，NumPy仅作数据容器；预算counter尚无事件，工人/输出使用明确的待定声明摘要，不冒充实际capsule/目标。原52完整模块/32外部对象证据不迁移为当前候选资格。

## 最终运行包尚缺的工程

1. 将已采纳保存来源规则接入具体限域执行消费，复用原HA六阶段；当前原消费/科学执行门仍拒绝。
2. 固定可信持久账本、实际worker/capsule/output身份；现有独占预约是NOT_RUN_AUTHORITY，旧package claim只接受SYNTHETIC_RESERVED_NOT_RUN_AUTHORITY，不能直接当真实许可。
3. 当前来源/环境与同record Win32 Job/进程的启动前保护、监测和清理组合；已有原生实现及替身测试不等于实际保护证明。
4. 有限监督证据/日志输出及统一计量，明确禁止未经计量的stdout/stderr旁路；本轮一文件上限只覆盖原结果工件，不能声称全部磁盘输出已受控。
5. 将以上具体工件与本轮数值提案组成最终可执行候选，才请求具体有限Owner运行决定。原root/C/g/权重则在获准执行后取得，不提前伪造为前置实测工件。

上述独立工程继续在既有授权内完成，不逐helper请示；本次不向Owner提出尚未具体化的运行批准，也不再次请求A政策。真实p/单位/激励、RP、外层停止和正式科学接受仍按后续依赖处理，不补默认。

## 保存和边界

本地a_budget_profile_20261107新增source_manifest、budget_proposal和integration。93件基线仅两个声明源码与一条测试夹具修改，其余90件和原七件未跟踪原字节保持；旧源码字节保留在Git及本地副本。实际HA/初始化/求解/原汇总、真实OS后端、科学worker和新科学attempt均0。

全部运行/科学资格、Results、REAL_GE、激活、FORMAL_SOURCE_FREEZE、producer_invocation_verified、执行消费、live_counts_enforced及完整计量均FALSE。原黑箱算法/网格定义/controls和C-g逐格Frisch→原权重→A1 pH合同、全部旧STOP/关闭额度/16义务/保护不变。两树保存并发布脱敏文档；代码/测试/机器记录/原数组与私有传输只本地，不合main、不强推。
