# CH5原始C/g快照与输出编解码的同counter计数

日期：2026-11-07。代码候选`8e73a2cb9b51d50f6b8fccec6bf1ced2f94e428b`。本轮完整普通工程交付：复用既有计数器，接入C/g不可变复制、快照/输出Base64、JSON、显式摘要和root回读，并将可选计数对象从休眠启动组合传入原root。更新五份外部源码，未改HA、算法/网格/controls、原C/g/权重或保存格式；子代理0，真实科学运行/新额度0。

## 实现与计费口径

C/g捕获保留原C顺序不可变字节副本；编码时每次物化和Base64/ASCII步骤独立计费，解码前先核对声明shape/dtype对应的字节容量再预留array_bytes_copied。原始C、原g分别保存，权重、dtype、shape、源布局、只读约束及request绑定保持；不从Ct倒推、不乘入g、不重归一化。

JSON渲染先计算有限数据结构的保守ASCII表示容量，再预留serialization_and_digest_bytes；采样回调后、调用renderer前再次核容量，输入被扩大时先拒绝。实际输出长度和预留容量分别记录，不把容量上界当实际消耗；未用满容量不退还。ASCII/Base64/解析/摘要按各自显式输入字节计费，Base64解码产物另计数组物化容量。容量规划、类型/有限性验证、标量/Python对象与计数账本开销不在本轮覆盖中；这些表示上界不是科学精度、网格、实际运行预算或内存峰值证明。

原snapshot和bound output接口增加可选byte_meter，默认路径保持原行为。原root要求计数器与CounterIdentity均为原对象；编码/回读中的子操作计数与原output_create/write/read及root顺序共存。休眠启动/root组合可传入同一meter，公开执行门仍在实际动作前拒绝，不创建Owner许可或消费账本。

预算不足会在renderer、ASCII转换、数组物化或解码动作前停止；坏载荷/回读失败保留既有文件和已占容量，root不返回、不重试。预留与样本只是本进程声明回放，不能替代可信实际账本、OS或科学证明。独立文件save/load辅助接口的I/O未自动接入root预留，默认及其他未接入路径也不构成强制计数。

## 对照与必要检查

| 本轮检查组 | 通过数 |
| --- | ---: |
| 新表示容量/编解码核心 | 10 |
| 新C/g快照/root组合 | 9 |
| 新休眠启动组合转接 | 1 |
| 原快照回归 | 13 |
| 原字节计数核心回归 | 11 |
| 原输出封装回归 | 21 |
| 原root回归 | 17 |

20新+62相关回归共82通过，不跨历史片相加；定点/变异复核不另计唯一测试数。用本轮启动前固定源码的旧snapshot及旧output encoder作对照：原相同输入/目标的完整canonical字节、摘要、dtype/shape/布局/原C-g/权重一致，包括非连续及大小端浮点容器。旧编码器仅作为本地数据格式参考，不是科学reference或运行资格。

一处组合测试把从只读快照重新捕获的源布局，与首次可写输入的布局混同，已改为同输入的旧实现严格对照，再核对root输出与此次捕获的摘要、原C/g字节及权重；未改科学语义或放宽数据检查。新增采样扩大JSON的拒绝检查。把JSON渲染移到预算预留前的变异被捕获，源码原字节恢复；错误与通过日志均留本地。

原fixture的合成来源差异工具继续明确固定摘要，累计七份相关外部来源均核对现场值，旧清单/reference/pin不反写。本轮新机器包绑定52源码/100静态内部边（4延迟、保守装载图无环），重新解析全部52文件以更新改动后的导入坐标；不是实际调用次数或完整native闭包。包内为source_manifest、startup_contract、codec_interfaces、binding_plan四份JSON。

65件启动基线中60件保持现场原字节；五份外部源码的旧字节保存Git及本地副本，其余47来源、前片机器记录、两份adoption和原7未跟踪项保持。主代理工程自审不冒充独立科学审查。NumPy仅合成容器；科学函数/HA实例化/外部动作禁入检查有效。

## 未覆盖和真实边界

本轮为可选、显式路由的快照/输出计数，不称完整字节或native覆盖。初次反序列化、其他传输/capsule编解码、未接入身份/grid/guard/loader计算、规划/校验/记账及native/求解器仍有缺口；complete_byte_accounting和live_counts_enforced均FALSE。后续可把复用的编解码端口接到明确的外部传输工件，并补其余可独立计数路径，不以局部通过补全未观察证明。

实际原包仍未读取/解释，original_packet_semantic_mapping=null。合格输入传输、科学worker/capsule/声明采纳、冻结grid/参数/controls工件、可信有限Owner决定与账本、完整计数和实际OS/source/module/root/Cg证明仍缺。真实p/单位/劳动激励、RP、外层经济停止与严格科学标准待Owner；已定Frisch/无额外z/A1/税/H/Lt_prev/输入不重问、不补默认。

actual grid hash/artifact、strict reference/thresholds及15实际预算仍null，NEW_RUN_BUDGET=0；所有实际工件槽位未填。全部运行/科学资格、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE及live_counts_enforced为FALSE，公开门拒绝。真实OS/HA/科学worker/实际网格及新额度均0。

旧关闭额度/STOP/16义务、历史dirty与保护基线保持，不移动缓存证据、不改Desktop/CUA/全局配置。代码/测试/机器记录只在本地；两树/GitHub仅本报告和三个CURRENT，main不合并。最终提交与逐文件Blob/实际字节/SHA256回读见本地交付回执。
