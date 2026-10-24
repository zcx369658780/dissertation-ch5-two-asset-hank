# Owner 决策记录｜历史 Python 基线选择｜2026-10-24

STATUS=OWNER_SELECTED_BASELINE_DIRECTION__EXACT_SOURCE_IDENTITY_RECOVERED_CANDIDATE_REVIEW_PENDING

## Owner 决定

Owner 明确选择以2026年9月初首次复现 MATLAB 多省份 HANK 的 Python 版本作为后续修订基础。GPT/Astra 必须先独立审阅来源身份、MATLAB/TeX 对照和隔离修订候选；Owner 最终接受后，才可能另行冻结新的正式来源。

## 历史验证边界

历史 corrected-2009 案例记录：Python SOURCE_CONVERGED，184轮外层迭代、5,704次 household calls、31/31省家户收敛；历史 MATLAB 对照为184轮、5,704次调用。该历史证据不等于本轮候选重新收敛，也不证明所有经济学接口都正确。

2026-09-01历史审查曾发现 household Lt 未正确映射至 firm Lt_prev，北京保留过期 186000.0。当前被选基线报告称此缺陷已修复，不应重复修改。

## 本轮候选状态

Codex run_id：156211a0597e49c4a40f37e5c9489812
终态：PASS_BOUNDED_HISTORICAL_BASELINE_IDENTIFIED__PATCH_CANDIDATE_READY__GPT_REVIEW_PENDING
上传 ZIP：CH5_TEMP31_HISTORICAL_BASELINE_PATCH_CANDIDATE_R1_OFFLINE_REVIEW_20261024.zip
ZIP大小：131442字节
ZIP SHA256：36143632a1497d3f7e470bafbc3155ac5d1937b104f02169e939ec7bf0e7959c

Codex报告的基线候选 commit 为 ba98537fd5ae004f0aa37d319865da1f1739e503，tree 为 f432f0acb5d94e0f60cd976b74a236be883e0db3。候选旧锚点 94de4501dec051b969bee9d852eba2d4591f30ef 在本地缺失，未作为来源。上述身份和候选 diff 仍等待 GPT/Astra 独立验收。

## 已批准的隔离候选方向

1. 修正第三章式（3-34）综合工资一般公式的 alphal/varphi 幂次，保留当前 alphal=1，不改 HA 算法。
2. 目的地经济指标更高时劳动厌恶更低；动态 Y/L 与现实/滞后人均 GDP 的最终选择仍为 E3。
3. 工资税只扣一次：HA 专用净工资价格副本，财政原 tau 保留；无法证明所有 w/tau 用途一致时不得生产绑定。
4. 若 tau 为工资总额比例税，政府工资税按税前工资率乘企业劳动核算；sigma 归宿另行决定。
5. 用 HA 异质性聚合劳动进行省际拆解，不从平均消费独立生成第二套劳动。
6. A1-A：就业比例 p 仅用于统计换算；企业效率劳动按 H_i×LHA_i×omega_ji，不额外乘 p。
7. 保留 GDP 反推生产率的基本方向，区分产出迭代变化与 GDP 目标残差。

## 未决与保护

动态指标/时点、唯一生产入口、净工资实际接线、最终价格与 HA 批次规则、价格/HA/GDP 残差标准、HU/期间/共同单位、sigma 收受方及资源含义、完整财政单位、是否正式冻结候选仍待 Owner E3 或独立证据。正式 V010 不变，V011 未启动，Results=FALSE，model_activation=False，REAL_GE=False。三个历史 PENDING Review、历史 STOP 和已关闭预算保持原样。

本决定只记录基线方向，不代表候选已被 Astra 接受或正式来源已冻结。