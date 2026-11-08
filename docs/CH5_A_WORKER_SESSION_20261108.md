# A/0工人本地组装与输出身份封存

日期：2026-11-08。状态：ACTUAL_A_OUTPUT_IDENTITY_AND_WORKER_SESSION_SOURCE_PREPARED_NOT_RUN_AUTHORITY。

本轮[工人本地组装与输出身份封存](CH5_A_WORKER_SESSION_20261108.md)完成，代码候选e783ec8253784d3c6c0decaa695a1a547cae0858。新工人会话从原entry与外部pin合同重建独立counter、原输出目标、V2工人预算和六阶段核心。接收已用预约后一次组装；失败留存，不重新预约或恢复actor容量。公开/独立执行入口仍拒绝。

新检查14项通过；相关bootstrap19、origin21、worker-core12分组回归通过，不累加重复覆盖。实际A当前58来源/134静态内部边、22元数据模块/两原数据AST准备回读通过；传输139189/startup156787字节。原包/快照/工资/向量保持原字节，原输出身份在新输入对象和独立counter上重建为同契约。

## 发现与修复

原输出目标包含随机target_id。重新调用原工厂会取得不同身份号，无法复现父端契约中的output_target摘要；路径相同仍会拒绝。新接口接受原目标身份字节及独立外部pin，重算全部来源、执行、工资/快照、origin、目录和文件名绑定后，要求canonical身份原字节完全一致。保留旧target_id，同时新目标仍捕获新工人本地对象引用、数组和目录守卫。默认工厂行为及原输出格式保持。

新worker_session从原RehydratedWorkerEntry和限长外部pin合同重建目标、CounterIdentity、独立contract/counter与V2预算；重建合同须逐字节相等后才取得工人actor。准备阶段无worker事件、无输出/预约写入。私有接收端先核context与两已用预约，再创建唯一worker段、phase、return和driver。driver仅对准确已绑定的bootstrap工人预算允许在消费状态组装，旧PREPARED路径保留。

session保留原entry/plan/request/输出目标引用，样本提供者方法绑定及阶段边界守卫；公开/独立入口在任何dispatch前拒绝。私有执行复用原driver/root/六阶段与原C/g保存回读，不插入HA内部hook，不改变科学口径。失败是该session终态，不能再次采纳或执行，同actor不可重建续额。

## 验证与实际A

14项新检查覆盖外部合同pin先于IO、旧声明拒绝、原目标身份逐字段核验、身份保留时不生成UUID、重建合同完全相等、actor不可复用、已用预约/同counter/目标绑定、错handoff无worker事件且不可重试、公开/独立门无IO/导入、原六阶段替身C/g和权重回读、阶段失败留存和本地对象替换拒绝。相关bootstrap19、origin21、worker-core12分别通过。中间1项检查与重复覆盖不累加。

最初RED为接口尚未实现；随后检查暴露随机输出身份问题，失败日志保留。去掉原身份绑定条件的内存变异被检查检出，finally恢复，真实源码未变异。带守卫检查的禁止科学源码尝试/外部动作/SciPy sentinel均0。工程自审不替代独立科学审查。

来源58份/134静态内部边、未解析0、eager DAG无环；相对上轮57源仅改worker_driver和origin_output两个工程源码，新增worker_session。源码逐文件Blob/实际字节/SHA256核验；新58源测试伴随表不反写历史fixture/PINS/生产pin。124选定基线121件原字节保持，另三件仅两个工程源码和测试helper；旧字节在Git。

实际A仅22个标准库元数据模块及两原数据AST，不读取新私有数据、不生成网格，不迁移旧完整模块/环境资格。将输出身份封存为第六本地记录，在新解码的原请求/inputs/record/plan上重建原目标，并建立与父端字节完全相等的独立counter契约。原3257字节A包、A-B快照/工资/向量与旧资料不改。

新a_worker_session_20261108六记录：source_manifest、output_allocation、output_target_identity、preparation、decision_draft、integration。父/工人输出容量已准备，worker事件/输出操作0，账本仅候选anchor、结果目录空。实际A仍原休眠capsule，未创建科学worker_session、未采纳账本信任或验证native环境。仅保存身份和重建合同，不等于输入交付/实际执行。

拟1工人/300秒/3 GiB、总写读各2 MiB/全局5文件/原结果1份、8192声明事件/5000ms清理/1次保持。写/读分区671744/1376256字节，两早读各8192在原读分区内预付，实际读取0，不扩额/退款/转借。九后置计数及全部15实际批准仍null。

实际A仅PREPARED：15实际预算/批准次数/运行决定仍null，NEW_RUN_BUDGET=0。实际预约、输入交付、bootstrap读取、HA/初始化/HJB/KFE/原汇总、真实OS/科学worker及新科学attempt均0，原root/C/g未取得。运行/科学资格、Results、REAL_GE、激活、producer验证、执行消费、完整计量和live enforcement均FALSE。

路线保持外层闭环→31省数据/校准→基准→政策/第五章写作。HA整体黑箱、原算法/网格/controls、a*r_a、净工资、同inputs、正式post→原KFE→原归一化，原C-g逐格Frisch→原g/权重→A1 pH/无额外z/税/H/Lt_prev不变。真实p/单位/激励、RP、外层停止和正式科学标准不补默认。A、长期中小网格许可及A阶段严格/完整native前置后置已定，不重问。

## 余下工程与保存

下一完整工程仍须完成实际科学入口的当前完整源码/依赖/冻结对象装载与绑定、同record受保护进程/环境、可信有限决定的来源和消费，以及未路由/native写保护。本轮会话组合只由替身执行；实际A没有实例化科学worker会话。元数据装载、同摘要、原输出身份重建均不证明父进程认证或OS保护。最终精确包可审阅后才提交具体有限运行决定，普通工程不逐helper问继续。

原七未跟踪、旧STOP/关闭额度/16义务/保护和历史dirty保留，不重绑/重试或换目录续额。代码/测试/机器记录/私有载荷仅本地，远端仅六份精确allowlist脱敏文档；不reset/stash/clean、强推、合main、删分支、移动证据或改Desktop/CUA/全局配置。最终本地HEAD/远端和逐文件回读以交付回执为准。
