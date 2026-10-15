# 第五章 CURRENT：V0.0.8 corrected-model 实施及受界稳态/冲击诊断已冻结

日期：2026-10-15（Asia/Shanghai）
**状态：V008_FROZEN__OWNER_ADOPTED_CORRECTED_MODEL__WAIT_SEPARATE_SYNTHETIC_IMPLEMENTATION_AUTHORIZATION__REAL_HANK_AND_IRF_CLOSED**

Owner已经批准Astra研究包：CES家庭劳动指数—目的地双边最优化与工资对偶；一套全国工资税只扣一次；全国统一财政账户（省级仅分账）；AtTax/迁移成本/资本clip的经济归属尚未自动采纳；静态稳态先行，再视真实动态方程研究HANK IRF。Owner还明确希望将其落实到Python并检验能否获得稳态、IRF是否正常。固定合同见 [V008正式冻结计划](versions/0.0.8/plan.md)，本冻结**不凭文件本身签发实现许可**，须Astra独立回读后单独签发受限合成corrected-model实现授权。

此版本实施代码基线：V007 accepted candidate `d8bb49d86ea674ea4ff5e3fdf03929baa08a6514`，tree `9b685397ad5bc76a4ac3bf4203776389742c5ec5`，只在全新隔离候选分支/目录新增reconciled模块和测试。原D盘历史worktree及8 dirty/untracked/ignored、外部Git common-dir、B3有限备份保持，不merge main、不改source-faithful `firm.py/wage.py/one_turn.py`、HJB/KFE/old C8科学路径。
数值验收划分四门：Gate A经济oracle；Gate B人工条件稳态（不等于完整两资产HANK均衡）；Gate C同稳态基础上的人工条件冲击路径（不等于真正动态HANK IRF）；Gate D前瞻性HJB/KFE/政策动态等真实IRF准入审查，缺完整闭合返回`IRF_BLOCKED__NO_DYNAMIC_HANK_CLOSURE`。Codex可获范围内的新的人工经济体数值预算，但旧模型/受保护2018数据/完整31省HANK/真正IRF数值/Results预算0。

当前原C8真实阶段A–D仍REQUEST_ONLY；A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、旧science/data/consumer预算CLOSED；已接受C8/2009 parity和V007经济来源问题不能被新synthetic表现取代。V0.0.9 NOT_STARTED。CH5_WORKFLOW_V1.2保持。
