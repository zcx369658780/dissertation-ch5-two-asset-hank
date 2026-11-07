# A/0 bootstrap传递与早期读取预付

日期：2026-11-08。状态：ACTUAL_A_BOOTSTRAP_HANDOFF_PREPARED_NOT_RUN_AUTHORITY。

本轮[bootstrap传递与早期读预付](CH5_A_BOOTSTRAP_HANDOFF_20261108.md)离线集成完成，代码候选26a2140a8b453ee6328250529eb27ae4325c5ed7。固定有限决定、已用两预约及V2输出分配可经动态context传给新工人本地契约；不重新预约、不恢复同actor额度。该协议没有提供父进程或Owner身份认证，公开执行门仍拒绝。

新检查19项通过；相关回归分组output12、capsule16、native替身16、attempt22、worker-core12均通过，不将重复覆盖相加。实际A当前57来源/131静态内部边、20元数据模块/两原数据AST准备及136665字节传输、153551字节startup回读通过；原包/快照/工资/向量原字节保持。

## 协议与计量

新增标准库bootstrap及V2声明。最终决定和两份预约形成后才生成动态context，避免将摘要放入决定前声明造成自引用。context最多16384字节；最终Windows命令按UTF-16限制在32767字符以内。参数摘要验证传递一致性，不证明父进程或Owner身份。

工人V2预算建立时，固定预约和capsule预约各预付8192字节读取容量；两项实际read_returned初始仍0，早读返回观察单独传递。预付从原工人64/32 KiB读分区内扣除，父预算不重复扣。早读先查大小，再读取该大小，不额外读sentinel；核目录/文件身份、非reparse、前后大小时间和原摘要。capsule是独立准备输入，封装最多2 MiB、源码最多1 MiB，不混成运行输出。

bootstrap核具体有限决定、原契约/V2分配、同counter身份、原包scope及两预约，再向封装入口注入原字节和早读观察。接收端新契约核外部context pin、留存字节/摘要/分配，使用工人剩余读配额再次回读两预约，复制已用状态。actor绑定单一契约，拒绝再次预约或用新对象恢复容量。私有协议接口不构成实际准入API；原公开执行入口继续拒绝。

原V1默认分配字节和快照字段保持；旧capsule bootstrap原字节、历史fixture/PINS和生产pin不改。新57源测试伴随表绑定当前候选，旧56源表未反写。原C/g及原权重保存格式不改，toy数据不冒充真实科学输出。

## 验证与实际A准备

19项新检查覆盖V2预付/容量不可复用、V1兼容、错摘要/重复key/未批准/错分配/超大文件拒绝、有限命令、新本地counter绑定及bootstrap→原六阶段替身→原C/g和权重保存回读。相关回归分组12/16/16/22/12通过；中间3/11/16/18/19项及重复回归不累加。所有带守卫检查的禁止科学源码尝试/外部动作/SciPy sentinel调用均0。内存将固定预约读上限8192改8193被测试检出，finally恢复，真实源码未变异。工程自审不是独立科学审查。

当前来源57份/131边，未解析0，eager DAG无环；比上轮56源只改attempt/output_budget/native三个工程源码，新增bootstrap。逐文件提交Blob/实际字节/SHA256一致。实际A仅装载20元数据模块及两原数据AST，不迁移旧52模块/32外部对象资格。

新a_bootstrap_handoff_20261108五记录为source_manifest、output_allocation、preparation、decision_draft、integration。实际工人仍原休眠入口，未实例化科学核心、未验证native环境、未采纳候选账本信任。固定账本只有anchor，结果目录空，counter事件/输出操作0；无决定和交付时构造可用context被拒绝。两项read_reserved各8192仅为容量预付，实际早读0，bootstrap_output_reads_metered及跨进程worker资格仍FALSE。

拟议总写/读各2 MiB、全局5文件/原结果1份、1工人/300秒/3 GiB、8192声明事件/5000ms清理/1次保持；五类写容量671744、读容量1376256字节，不扩额、不转借。九后置计数及全部15实际预算仍null。

实际A仅PREPARED，决定/15实际预算/批准次数仍null，NEW_RUN_BUDGET=0。实际预约、保存输入交付、bootstrap读取、HA/初始化/HJB/KFE/原汇总、真实OS/科学worker和新科学attempt均0，原root/C/g未取得。运行/科学资格、Results、REAL_GE、激活、producer验证、执行消费、完整计量、live enforcement均FALSE。

主路线外层闭环→31省数据/校准→基准→政策/第五章写作不变。HA整体黑箱/算法/原网格与controls、a*r_a、净工资、同inputs、正式post→原KFE→原归一化，以及原C-g逐格Frisch→原g/权重→A1 pH/无额外z/税/H/Lt_prev保持。真实p/单位/激励、RP、外层停止及正式科学标准不补默认。Owner已定A/长期中小网格授权及A阶段严格/完整native前置后置不重问。

## 余下完整工程与保存

下一完整工程：实际科学worker入口与当前模块/环境装载、同record受保护进程接线、可信有限决定的来源与消费绑定，以及未路由/native文件写保护。已完成的是离线传递协议和早读容量预付，不是实际跨进程认证、OS隔离或完整字节计量。最终精确包可审阅后才提交具体有限运行决定；普通工程不逐helper问继续。

116件选定基线112件原字节保持，只改三个工程源码和测试helper；旧字节在Git保留。原七未跟踪、全部旧STOP/关闭额度/16义务及保护基线保持，不重绑、不重试或换目录续额。模型源码/测试/机器记录/私有载荷仅本地，远端仅精确allowlist脱敏文档；不强推/合main/删分支/改全局配置。最终HEAD/远端及逐文件核验以交付回执为准。
