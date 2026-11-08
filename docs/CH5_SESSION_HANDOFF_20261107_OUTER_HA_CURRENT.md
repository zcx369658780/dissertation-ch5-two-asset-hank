# CH5当前交接：统一准备入口与轻量保护设计

更新：2026-11-08。

Owner最新建议已落实为统一输入准备：代码9e9b0315625d11000404d7d34a26f65a703503b5，同包完整解码实测35→1，31个原请求/冻结输入一致。25项受影响回归与5项新入口检查通过，不重跑未变检查，不逐helper/测试/commit等“继续”。见[工程精简记录](CH5_OWNER_LEAN_ENGINEERING_20261108.md)。

Owner已明确选择“采用轻量保护，完整OS写隔离留到扩大运行前（建议）”。该决定仅降低首次小规模本地试验的文件保护要求：独立运行副本、硬资源限制、原件及副本前后摘要核对、失败留存；承认其不能在OS层面阻止同用户native代码写到原目录。首次试验不再以前置全面native写隔离为条件；扩大运行前仍须完成完整OS写隔离。设计采纳不等于实现或验证完成，不改原件ACL、权限或全局配置，也不新增HA次数或预算。见[已采纳保护设计](CH5_LOCAL_TRIAL_PROTECTION_OPTIONS_20261108.md)。

本轮起点模型0cb62c08d43080cd3df815ff13e27d6a55c741c4、治理本地1996817c873e4e8199bf2398369def809600c349、治理远端c725e792edae79e3ad94396293af155f39f8781d；main b7e595ceb1cd7ffb5adfbf54e2de4e65f01090a5未合治理。最终HEAD、六文档原字节/Blob回读和保护核对见模型树同级LOCAL_ONLY_CH5_LEAN_ENGINEERING_20261108/DELIVERY_RECEIPT.json；回执不是运行/重放许可。

启动先核两树真实根/工作树/分支/HEAD/remote和staged/dirty/untracked。模型分支codex/ch5-temp31-local-first-source-20261101；治理分支governance/ch5-codex-local-first-20261101。读AGENTS、短状态、工作流、本卡、本轮工程精简与保护决定。默认0子代理；外层Zotero旧R40不授权CH5。API脱敏快照链不同，不强推求同。

已提交137cd9eabdb5b17093fa091477dfa58f7c8368da纯重构及9e9b0315625d11000404d7d34a26f65a703503b5统一prepare_provincial_worker_inputs入口。一次完整decode后接原工厂/冻结原类型，调用方批量用household_batch.requests；原公开validate/select保留用于真正边界。25项原回归、5项入口检查通过，追加入口前已测源码前缀完全一致，没有重跑未变25项。35→1来自准确旧代码对照，输入/负零/只读向量/工资/原grid/参数/controls一致；不是HA性能或稳态结论。

下一完整普通工程是同record的实际启动—输入—结果/失败留存包，补可信父端有限决定/已用scope、当前原模块装载、worker入口、环境/硬资源限制及已采纳轻量保护。全面OS/native防绕写不再首次试验前置；扩大运行前补齐。保持离线，不调用真实Win32/Job或科学后端。实际执行包可审阅后集中确定有限运行；不逐helper/测试/commit等“继续”。

原31省12组件传输、原请求工厂和冻结类型已接通；两期62条参考、123条工资观测与2017西藏私营缺失保留。31演示仍合成、实际31省包0，真实w/Tt/利差及来源采用未补默认。Owner已定2022主基准/2017对照、时间按年；源码推得10万元/百人而非千人，历史缓存单位未认证，前向采用/劳动桥不默认ell=1。年薪gross参照非HA净综合工资，分母须同群体全年平均工作地人数。资本后期代理、福建2负投资、就业历史差异及GDP版本问题保留。

路线外层→31省校准→基准→政策/写作、四阶段和五组利率候选保持；财政差额只诊断。本金/rah同权，本省1−q_i、他省q_i/(n−1)；At×H、不乘p不含Bt、G加一次。HA不直接读GDP/K，相同直接输入不因省名不同构成新数值问题；不授权克隆/复用科学结果。工资收入比对不是单省HA新门槛，外层alpha/Z/H/p/G另列。

原A优先PREPARED；原58源/134边与专用工资证据不重绑给31省。原包SHA256=8ed0fb98445ed02debfee0a971e0c728dbd583f6cc323ccfba22406b8191b225；grid SHA256=1cc6002840d6a3dfef899c98d09f4796a8e14ccb9116a7952cdf78ab50305258。原root/C/g未得，A事件/输出/预约/消费/bootstrap读0；真实HA/项目OS后端/科学worker/新attempt0，失败数/比例null，15实际限制/批准次数/运行决定null，NEW_RUN_BUDGET=0。运行/科学接受/Results/REAL_GE/激活/producer/消费/环境/跨进程/完整计量/live/native资格FALSE。

HA整体黑箱、算法/网格定义/controls、a*r_a、净工资一次、同inputs、正式post→原KFE→原归一化、原C/g逐格Frisch→原g权重→A1 pH、无额外z、税/H/Lt_prev保持。A优先级、首次返回A、长期中小网格和工程自主权不重问；网格许可不发HA预算。旧STOP/关闭额度/16义务/历史dirty保持；六缓存与已消费execution_decision共七未跟踪原字节、fixture标M但原字节/Blob等于提交，不清理重写暂存。源码/测试/机器/私有包本地，仅本轮六份脱敏规则/文档同步。禁止reset/stash/clean、强推、合main、删分支、搬移证据缓存、换目录续额、公开私有原值/完整路径或改Desktop/CUA/全局配置/memory。
