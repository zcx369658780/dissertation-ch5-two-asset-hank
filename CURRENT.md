# 第五章 CURRENT：V009 GDP偏好方案B参数已冻结并单独授权剩余额度续跑

日期：2026-10-15（Asia/Shanghai）
**状态：`V009_CES_PHI_SCHEME_B_FROZEN_AND_SEPARATELY_AUTHORIZED__REMAINING_BUDGET_FULL_HANK_STATIONARY_RESUME__NO_RESULT_YET`**

Owner明确批准保留论文`max_phi=0.3`人均GDP差异引导双边劳动偏好的方案B，并在前一治理固定commit `c4fe97b4bc3510c42683579ff1aa7edd1df27807` / tree `7a0301e7a5a77b827a28c51066d6c84e16c086d2`、[新增冻结参数条款](versions/0.0.9/ces_phi_supplement.md) blob `1c9839fe639197176d0d8b1c981b4c13025dcd5a` 内封存：人工1省 `phi=((1,),)`；人工2省 `pgdp_ref=(1,2)`、目的行/来源列 `phi=((1,1.1),(0.9,1))`；不从求根时内生GDP重算，不抄旧MATLAB反号。

Astra另行签发 [一次剩余额度续跑许可](versions/0.0.9/ces_phi_resume_authorization.md) `ASTRA_APPROVED_EXECUTION__V009_CES_PHI_B__REMAINING_BUDGET_SINGLE_CONTINUATION`，仅允许在原计划 `cb76a840fdd9d1756728189bf29518679831aba6` / E1-E3的20×20×2 artificial scope内，修补旧PRE-PHI阻断候选的φ缺项并按**同一V009未耗尽的实验预算**尝试实际HJB/KFE/宏观稳态：pytest已消耗4/8（剩4）、完整science driver0/4、macro0/4、household0/176，toy计算及时间/存储全部累计。已发表原阻断候选`18256cd70b827e133e52d7609746c8afadb63ac1`不改/不自接受，后续隔离新候选唯一parent仍是原V008 accepted源码`d41d229b681e09b913c21deff7a057085b9bc419`，依原13路径白名单。任何失败严格STOP，不因冻结漏项而全量恢复预算或改其它参数。

真实2018/C8数据、原科学runners、24×24、现实31省HANK、动态IRF、Results预算仍0；A16 FAIL_CLOSED/window UNACCEPTED/C9 PAUSED/CALL_LEDGER_UNRESOLVED/model_activation=False/Results FALSE。V010 NOT_STARTED，V1.2+Owner连续立版长期规则不改。
