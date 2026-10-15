# 第五章 CURRENT：V0.0.8 corrected-model 人工数值里程碑正式受限验收关闭

日期：2026-10-15（Asia/Shanghai）
**终态：`CLOSED__ACCEPT__CORRECTED_SYNTHETIC_ACCOUNTING_CONDITIONAL_STATIONARY_AND_SHOCK_DIAGNOSTIC_ONLY__REAL_HANK_IRF_BLOCKED__WITH_OBSERVATIONS`**

Owner采纳新corrected-model路线（CES家庭劳动—双边工资对偶、全国一税只扣一次、统一全国财政、AtTax归属不自动确定、静态稳态先行）；Astra正式冻结commit `e222b302176f8ff627ced1442196299f804b9aa7` / plan blob `891e8dae2eead0c5c39bf20a7542c68a004b5e94` 并独立授权 `ASTRA_APPROVED_EXECUTION__V008_CORRECTED_MODEL_SYNTHETIC_STATIONARY_AND_SHOCK_GATES_ONLY`。Codex交付 [已接受V008候选](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/commit/d41d229b681e09b913c21deff7a057085b9bc419) commit `d41d229b681e09b913c21deff7a057085b9bc419`、tree `88833acf90613380afa30ab8d6ee7e0297e98664`，唯一parent `d8bb49d86ea674ea4ff5e3fdf03929baa08a6514`，GitHub真实diff仅13个新增白名单文件，main及原HJB/KFE/one_turn/firm/wage/C8源码未变。现有[正式独立验收](versions/0.0.8/acceptance.md)、[复盘](versions/0.0.8/retrospective.md)；[候选科学报告](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/d41d229b681e09b913c21deff7a057085b9bc419/versions/0.0.8/scientific_reconciliation.md)和[完整JSON数值](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/d41d229b681e09b913c21deff7a057085b9bc419/versions/0.0.8/acceptance_summary.json)在固定候选（不是治理分支同名相对路径）。

**受限成果：Gate A数学oracles、有界复式账户；Gate B独立确认实际人工1/2/31省条件稳态，根评估10/17/166，最大归一化经济残差1.1765e-12/1.4443e-14/9.9508e-14；Gate C四条单省条件静态冲击路径（TFP t0、税 t10、公共资本 t20，零/全/半/20期）140期结果已由Astra独立复算，半幅相对差6.8102e-6、尾部9.1365e-8。所有人工结果给定家庭分布/两资产/政府资本，不含完整HANK household Euler/HJB/KFE/GE，**不能是正式IRF**；Gate D正确`IRF_BLOCKED__NO_DYNAMIC_HANK_CLOSURE`。人工公共资本外部实物赠与仅是明确情景，不是现实政府投资政策。

Codex报告最终`24 passed 1 skipped`、pytest 5/8、root10/12、人工31省root2/2、路径4/4，合并耗时19.4分钟、新增17,836,781B、采样工作集约30.3MiB、原8 dirty/index SHA匹配、无真实C8/旧模型调用；这些是`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，网页未实跑pytest或读其D盘delivery。四条C预算耗尽，最后一棵树skip路径重复执行，但公开路径解已独立复算。

真实C8历史SHA有独立接受但当下byte/size身份和A–D读取依旧REQUEST_ONLY；A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE以及旧真实/data/science/consumer预算CLOSED。V007及历史2009 parity仍限原范围，不追改；无main merge，原dirty/untracked/ignored/B3不碰。V0.0.9 NOT_STARTED，NEXT_BASELINE_ADOPTION=UNDECIDED。按CH5_WORKFLOW_V1.2等待Owner新授权才设计真实或完整合成HANK稳态/动态IRF下一高风险阶段。
