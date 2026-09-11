# 记忆与当前状态维护
更新：2026-09-11。

长期记忆只保留仓库、研究目标、重大路线、用户偏好及关键边界。临时路径、每个 gate 的数值和日志留在任务报告。

Chapter 5 当前状态唯一入口：
`docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`。
路线唯一正文：
`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`。
资本网络科学设计冻结稿：
`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。

状态摘要包含：已接受范围、当前未解决问题、最新证据、active task、推荐下一步和 Results 状态。不得只在顶部追加新状态而保留正文中的旧“唯一下一步”指令。
更新重大状态时同步摘要；普通内部修复不要求另建交接任务。长期规则不写“尚未开始”这类易失效的阶段事实。

历史报告按当时证据保留；新报告可明确取代旧解释。CURRENT 文件与历史内容冲突时核实 live 状态，不从过期 handoff 重新启动已完成任务。

## Owner 长期协作偏好与持续授权 — 2026-09-07
Owner 明确授权：Reviewer 在验收任务报告后，如不存在实质科学选择，可直接完成必要的仓库接收/状态更新并发布下一份完整 bounded task，再给 Codex 启动 prompt，不再询问“是否继续”。
Owner 有备份和冗余试错，偏好减少审核往返、重复证明、过度细分 gate；普通工程修复和有限重试应预授权在同一任务内。选择与风险匹配的最小充分证据，不为提升 L 标签额外运行。
这是降低流程负担及增加明确范围内试错空间，不是允许伪造验收、隐瞒失败、事后调容差或静默改变方程/校准。新的科学范围和预算仍写入 live GitHub task。真正 Owner 决策保留最终 authority。
本规则是持久化项目记忆；不宣称已修改 ChatGPT 账户级记忆或本地模型设置。

## Chapter 5 长期科学记忆 — K1 bilateral capital network，2026-09-11

Owner 的原经济意图必须长期保留：每省 household illiquid wealth 同时持有本省和外省企业资产，本省权重更高；household `rah`应由实际省际 portfolio weights 对 destination returns 加权得到。旧 MATLAB / source-faithful Python 只统计跨省流入、漏掉本省 retained capital，并在 `rah` 外省项中残留 destination `theta_j` 二次权重，这两项已被认定为 legacy economic-logic defect；legacy route继续仅为parity authority。

Owner曾尝试三资产多省HANK，但单HA耗时约由两资产20秒增至三资产5分钟；若为30个外省目的地增加显式asset states会造成不可接受的31资产HJB维度爆炸。因此当前重大路线是：household继续两资产`(b,a)`，通过post-household bilateral provincial portfolio fund layer实现资本网络，不把31省资产写入household state vector。

冻结的nested Scheme B：
- K1固定`theta_i=inter_prv_ratio_i`作为origin总外投比例；
- home share=`1-theta_i`；
- foreign destination conditional shares形成完整`destination x origin`矩阵；
- quantity allocation与household `rah`使用同一矩阵；
- K2未来才讨论让`theta_i`内生化。

K1 zero-science implementation已接受，candidate=`742ae11dbb057c7d33650ed4bc8d4db59b90d435`。它实现home retained capital、origin/national private-capital conservation、foreign-only stable softmax、same-matrix `rah`，并保持legacy capital allocation byte-identical。

Owner明确要求 capital share 使用lagged/completed-iteration return attractiveness，禁止 same-turn `firm -> ra -> shares -> K -> firm`反馈；这来自过去真实遇到的数值震荡经验。该时序是steady-state numerical fixed-point convention，不是calendar-time instantaneous adjustment。

后续顺序长期冻结为：K1A repaired equal/space-only → K1B lagged-return endogenous foreign shares → K2 endogenous home-vs-foreign margin。第一次K1 scientific integration继续冻结source-faithful labor；资本网络独立验证后再stack normalized bilateral labor。

任何2-hour+ steady-state科学运行前，必须先冻结distance/friction score、dimensionless normalization、lagged-return score、`beta_distance`、`beta_return`、payoff return concept与是否需要smoothing。不得边跑边调。

C1 GovInv仍定义为不可直接观测政府/公共生产性资产 residual：`max(Ktarget-Kprivate,0)`；但K1改变Kprivate后必须重新联合验证。price/raw-ra旧结论也必须在K1后复核，不能据旧路径直接改`.02/.09` return bounds。

KFE继续单独治理：clean/source-free KFE方法学已有稳定实现；corrected-2018 empirical finite-box upper-b leakage/pinning仍是独立blocker。
