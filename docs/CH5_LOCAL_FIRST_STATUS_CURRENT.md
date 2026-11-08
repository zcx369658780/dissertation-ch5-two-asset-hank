# CH5 当前短状态

更新：2026-11-08。Owner已采纳[资本持仓修正与闭合/校准分层](CH5_OWNER_CAPITAL_CLOSURE_ADOPTION_20261108.md)，代码候选5bc766a11b7c257ca4e8d79f4bc3fa7d33e65510。本金与rah共用来源持仓权重，本省1−q_i、其余q_i/(n−1)；补齐本省私人资产，企业只加一次政府资本，资本用H不乘p，Bt不入生产资本。

新增outer_capital_ownership和outer_capital_one_turn，后续外层资本阶段选择prepare_owned_capital_stage→assemble_owned_capital_outer_one_turn。原MATLAB同源资本/控制器及已采纳A输入原字节保留；新增入口不冒充历史已执行结果。新11/7项及相关原拼装23项分组通过，只用合成/31虚拟省记账，无真实HA/企业/OS调用或运行预算。

Owner明确财政差额作诊断、不要求为零，不保证所有市场出清；旧外层方案可作临时参考，最终Z/GovInv倾向数据或文献，尚无新值采纳。给定参数迭代与校准分开记录，不能把自动调参值当数据估计或把局部数值收敛当完整GE。GovInv按当前公式为政府资本存量，不直接用当期投资流量替代。

真实A/0优先级保持。[原父端代写/单次handoff](CH5_A_OUTPUT_CHANNEL_20261108.md)离线集成仍有效，但完整受保护worker仍INCOMPLETE；真实IPC/peer、环境/Job、OS禁止绕写及最终capsule待实现。当前A58源/134边未变，原PREPARED不重跑/重绑；新资本只用于后续外层阶段，已采纳A第2轮原包/快照/工资/向量/参数/grid不追改。

实际A counter/输出/预约/消费/bootstrap读、HA/初始化/HJB/KFE/汇总/真实OS/外部进程/科学worker/新attempt均0，原root/C/g未得。15实际预算/批准次数/运行决定null，新预算0；全部运行/科学/Results/REAL_GE/激活/producer/消费/环境/跨进程/完整计量/live/native保护FALSE。

本轮153件既存基线全保持，只新增六件代码/测试/机器文件；原七未跟踪及fixture原字节/Blob保持。HA黑箱/冻结算法网格controls、a*r_a/净工资/同inputs/post→原KFE→原归一化、原C/g逐格Frisch→原g权重→A1 pH/无额外z/税/H/Lt_prev保持。旧STOP/关闭额度/16义务/保护不动，默认0子代理，外层旧R40不授权CH5；源码测试机器私有包本地，仅四份脱敏文档双端保存。
