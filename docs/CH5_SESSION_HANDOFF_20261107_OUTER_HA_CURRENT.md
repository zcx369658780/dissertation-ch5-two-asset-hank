# CH5当前交接：工资收入目标与统计分母已核

最新完成[工资收入目标与校准桥](CH5_OBSERVED_PAY_TARGETS_AND_CALIBRATION_BRIDGE_20261108.md)，代码候选b9cbe57453eba09d908dc740fa353c0336287217：123条年薪已形成带尺度条件的收入参照，未生成wt；新增同工作地/同群体/全年平均人数的gross工资总额比对接口，最终13项检查通过。统计分母由官方说明核实，不能用年底就业或居民H替代；原劳动语义已定，不重问。本接口是事后解释/校准工具，不新增单省价格HA准入门。实际比对/HA/新attempt均0，新预算0。

更新：2026-11-08。最新完整说明为[工资接入/年度时间/原源码单位核查](CH5_OBSERVED_WAGE_UNITS_AND_ANNUAL_TIME_20261108.md)。本轮起点模型566c339326b3b163cd889049d555cc2bd3201112，治理本地6d63077b364f8da6dca876da5a5bac9701556f0c、远端48fe4c57a1ecfbc60da85e11151ccb9e1d405673；main b7e595ceb1cd7ffb5adfbf54e2de4e65f01090a5未合治理。工程代码40bc2d011daacdf171b040c262f158cc8a4e2f80；最终保存位置以LOCAL_ONLY_CH5_OBSERVED_WAGE_BRIDGE_20261108交付回执为准，回执不是重放/运行许可。

启动核真实两树根/工作树/分支/HEAD/remote及staged/dirty/untracked，定点读AGENTS、短状态、工作流、Owner自主决定与本卡/最新说明。默认0子代理，Zotero旧R40不转移。模型codex/ch5-temp31-local-first-source-20261101，治理governance/ch5-codex-local-first-20261101；API脱敏快照链与本地链不同，不强推求同。

Owner已定2022主基准/2017对照，并明确时间“就是年”。随后要求查看load_GDPdata，回忆“千人”；定点核当前保护源码：原注释万人×POP_multiplier100，得到百人刻度；GDP亿元×1000得到10万元总货币单位。原N=加载人口、初始Lt=N，后续个人劳动时长×人口；它不证明工时单位或后续ell恒1。总口径当前选常住人口，就业行注释；缓存返回可能绕过构造，未读历史表/缓存作单位认证。源码前后哈希保持。

新增outer_observed_wage_units及测试，观测年薪/gross系数/原工资参数分层；必须显式时间、货币和有效劳动桥，税/迁移交原函数一次。14项检查通过，本次恢复不重跑；真实资料按省/年/统计群体/源哈希/单元格核对，四批共123条观测、2017西藏私营缺1，不填0或替换/平均。完整工资值仅本地，没有生成新gross/net HA工资。owner_annual_time追加年度决定，source_scale_audit追加源码事实，早期progress未答字段仅历史。

已有两期62条省级参考、资本2157原源/713候选、后期代理/福建2负投资/就业37历史差异/2017陕西新疆及GDP版本问题见[数据接入](CH5_REAL_DATA_BASELINE_2022_CONTROL_2017_20261108.md)，不自动改值或生成Z/G。五组利率候选围绕(.025,.08)，步长仍为方案，不是预算或连续稳态域。

下述为此前直接系数桥计划；当前收入目标已按最新报告实现，直接工资系数仍不默认ell：若采用10万元/百人尺度，w_gross=年薪/(1000×ell)，不默认ell=1，不改Frisch/偏好；再形成31省同批税/迁移/劳动权重/转移/借贷利差/冻结grid参数controls合法初值表。现有worker transport只支持A/0第2轮，不是31省接口。本轮input_contract_map只是静态来源表，没有复制A为31省值。完整外层Z/H/p/G等另列，不全部提前设为单省门。

原A仍PREPARED，58源/134边、原包/快照/工资/参数/grid/controls及首次返回A政策保持，不重绑/重跑；新模块不并入原A闭包，原root/C/g未取得。真实IPC/peer、同record保护/环境/Job、native绕写防护及最终worker仍不完整。A counter/输出/预约/消费/bootstrap读0，HA/初始化/HJB/KFE/汇总/科学worker/新attempt0；15实际限制/批准次数/运行决定null，新预算0。失败省份/比例null，不把未测试31省算失败。全部运行/科学/Results/REAL_GE/激活/producer/消费/环境/跨进程/完整计量/live/native保护FALSE。

Owner路线与四阶段、财政差额仅诊断、资本本金/rah同权（本省1−q_i/跨省q_i/(n−1)，At×H、不乘p不含Bt、企业加G一次）保持。HA黑箱/冻结算法网格controls、a*r_a、净工资一次/同inputs/post→原KFE→原归一化、原C/g逐格Frisch→原权重→A1 pH/无额外z/同源税/H/Lt_prev不改。普通工程连续完成，不逐片段再问继续；实际数值采纳/有限运行/保护决定仍由Owner保留。

保存原六缓存+已消费execution_decision共七未跟踪原字节；fixture status M但字节/Blob等于提交，不重写暂存。旧STOP/关闭额度/16义务/历史dirty/保护不动。禁止reset/stash/clean、强推、合main、删分支、搬移证据缓存、重绑保护/换目录续额、公开私有原值/完整路径，或改Desktop/CUA/全局配置/memory。源码测试机器私有包只留本地，仅五份脱敏文档同步治理。
