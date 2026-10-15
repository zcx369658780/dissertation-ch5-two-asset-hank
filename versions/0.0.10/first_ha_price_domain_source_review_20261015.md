# V010首次HA失败：现有失败原证与历史已验收价格域的交叉审议

日期：2026-10-15（Asia/Shanghai）
**性质：SOURCE_ONLY独立复核；不追改V010冻结实施计划、人工fixture、候选代码或历史科学接受。**
**验收分类：REPORTED_FAILCELL_CONSISTENT_WITH_ACCEPTED_SELECTOR__HISTORICAL_PRICE_SCALE_MISMATCH_SUPPORTED__CAUSAL_ROOT_NOT_PROVEN。**
**状态：V010_PRICE_DOMAIN_REVIEW_COMPLETE__NEW_SYNTHETIC_SCIENCE_DECISION_PENDING__NO_ACTIVE_CODEX_TASK。**

## 1. 固定身份和证据等级

- 已签发首次失败回执提取任务：commit `36d12eeba3b132ee0e0a76604f0158b61fce957a`、tree `e3bc48e5304b1940ebc589b4286541f153f208f9`、task blob `c745710e13c6a4de2cd81df31d8a584f74d9fba6`。
- 已审代码候选：commit `94de4501dec051b969bee9d852eba2d4591f30ef`、tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`；source tree的`selector.py` blob `51517dde0c829060b6e0c0d594ec60e7e6143883`，`wage.py` blob `1459d1b465f134a2d8746c252e71e060459465ca`，`stationary_runtime.py` blob `677f82911abe55dc462ebdd1601dfd65297b1e13`。
- 冻结计划 `bf091da33d59293f147d52c11580327d3ac2a85d`、plan blob `85138d8859d53295262fe13bf5bc277bca95ed3f`；人工fixture blob `40915658d93403cfc21b33a6b864b332b7857749`。
- Codex本轮报告`V010_FIRST_HA_FAILED_CELL_SOURCE_ONLY_EVIDENCE`：10个已有原对象读135699B，所有科学import/solver/pytest/Git写入为0；脱敏JSON SHA-256 `5D4F4D777514BA84DE920DF196ECDA7C7A6EF29BD3871AAD9141B05F800EEB14`。这些源自其Windows本地只读回执和用户转述，**Astra没有直接取得D盘MD/JSON，不能独立证明原10件SHA、字节数或候选计数**，证据等级`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`。其固定任务Git身份已在既有治理链核对。
- 本次Astra**独立GitHub源码/历史接受核查**证实下述价格域、原算法/数值边界和selector规则；没有运行任何HJB/KFE、模型、pytest或获取真实C8数据。

## 2. 已经独立确认的历史价格域（注意算法资格不同）

**2026-09-13真实综合工资域的standalone诊断**，固定旧资产边界`a=[0,10]`、`b=[-2,5]`，`I=J=20`，`rb=.02`，`ra∈{.06,.0675,.07}`，`w_eff∈{13,15.5,18}`。9组MATLAB-faithful HJB 9/9报告收敛、9组原standalone污染行KFE完成；但9组`modal b=bmax=5`，存在显著有限盒上界堆积，**非全局健康区、非corrected strict KFE、非GE**。
  - 固定历史接受：`docs/CH5_MP4C_K1_REAL_COMPOSITE_WAGE_DOMAIN_STANDALONE_3X3_AND_MACRO_SCALE_AUDIT_ACCEPTANCE.md`，blob `198ebde571bc84e0491be9dfa550b0ce3bf9c6be`。
  - 历史相同输入域扩展至`a=[0,100], b=[-2,20], I=J=20`：原HA HJB/KFE 9/9，`modal b`转为2.631579，非bmax；`At≈84—89`对有限域极敏感，`J=20`尚不足精度认证。见`docs/CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_DIAGNOSTIC_ACCEPTANCE.md`，blob `0ec5b909d4edf2a1ff19f323ac42644a68e7c04a`。
  - 进一步同一扩展域`I=20,J=160`接受五个代表性价格状态（4新鲜HJB/KFE，中心复用）。仅是实用家户数值诊断网格，不证明连续极限/GE/Results。见`docs/CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION_ACCEPTANCE.md`，blob `5c41c96c1732784f3ab77733be426bb8f613429c`。
  - **低工资域反例**：`w∈{.8,1.05,1.3}`、`ra∈{.06,.0675,.07}`虽9/9原HJB收敛，但不少分布在a边界/污染KFE病态，例如`ra=.06,w=.8`出现负`At`。历史已明确`NO_UNIVERSAL_RA_HEALTH_BAND`。见`docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_SCAN_ACCEPTANCE.md`，blob `f8bdb1d7af06615310e8069d066a76d900fde120`。

**科学界限**：以上9/9是原`MATLAB-faithful`求解器按当时value-change与污染行KFE资格执行的结果，**没有证明V010 corrected selector的同checkpoint B≤1e-8、D≤1e-7、source-free terminal KFE能够在该区收敛**。不可将历史有界HJB接受升级为目前严格方案的数值保证。

## 3. V010首省真正进入HA的输入（Git源码可独立确定）

`validators/multi_province/v010_mainline_validation.py`中首个`binding`直接以`mainline_initial_states(fixture)[0]`调用HA，**没有先走`prepare_mainline_household_states`的同S前轮回报重映射**。
- SYN_A：`rah=0.055`，`rb=0.02`；企业gross工资`[1.0,1.2]`、目的地税`[.04,.06]`、迁移加法楔`[[0,.15],[.15,0]]`、`pgdp_ref=[3,4.5]`、`phi_l=5`、`alphal=1`。
- 由新`mainline_phi`和旧`composite_household_wages`的**确定性静态算术（未调用模型）**：`phi=[[1,1.06],[.94,1]]`，`w_eff(SYN_A)=1.7085897434929322`、`w_eff(SYN_B)=1.7245032349674767`。
- V010冻结网格仍为`a=[0,10]`, `b=[-2,5]`, shape 20×20×2，与历史旧域相同，但初始`rah`和家户有效工资**都不在历史真实工资9点已测试价格集合**（更不是健康二维区域认证）。`rb=.02`相同。
- 原综合工资聚合对**目的地数量不归一化**，单目标贡献近似相同情况下`w_eff∝n^{phi_l/(1+phi_l)}=n^{5/6}`，将31目的地改为2目的地会改变家庭工资量级（equal-contribution理论比值`(31/2)^(5/6)≈9.816`）。这仅是结构性尺度**解释假设**，不是新校准系数，也不意味着可直接将两省工资乘9.816来修复V010。

因此：`HISTORICAL_PRICE_SUPPORT_MISMATCH=SOURCE_SUPPORTED`；`PRICE_MISMATCH_CAUSED_NO_ADMISSIBLE_POLICY=UNPROVEN`。

## 4. 报告失败单元与原selector逻辑核对

Codex报告checkpoint=2 / F-order flat=25的12个候选均不合格。原因频次为`B_DERIVATIVE_DIRECTION_INCONSISTENT:8`, `A_DERIVATIVE_DIRECTION_INCONSISTENT:7`, `TRANSFER_KKT_RESIDUAL:8`，positive/negative转移符号不一致各3次；同一候选可有多原因（频次不可相加求候选数）。3个liquid-Z root报告收敛，仍有拒绝；A-switch报告`g_a=0`及KKT约5.55e-17，但`g_b≈+0.046129`与b-backward不匹配；joint root=0。
- **Git独立核规则**：`selector.py:658–663`要求显著正漂移用forward导数；`:982–1001`分别检验B/A方向与transfer KKT；`:1404–1420`对joint两侧液体零漂移候选设精确前置，`:1718–1740`仅构造完整合法joint contexts；`:1742–1750`无任何可采纳策略时才是`NO_ADMISSIBLE_POLICY`，不是`NO_UNIQUE_ADMISSIBLE_POLICY`。这些代码约束**与Codex所述失败方式相容**，但不证明原JSON确实含这些值，也不证明旧数学selector bug或漏解。
- checkpoint0、1的Bellman未过门；checkpoint2的政策/Q尚不完整、未产生Bellman。用户转述的`D≈.4599367498`并非HJB成功。
- `PROXIMATE_DOMAIN_GATE=SUPPORTED_BY_CODE_PLUS_CODEX_REPORT`；`ULTIMATE_ROOT_CAUSE=INSUFFICIENT_EVIDENCE`。不可用价格假设直接覆盖原拒绝原因，也不准放宽KKT/方向门或代入人工Newton。

## 5. 集中下一科研选择（未授权）

**本次不发布新科学任务，不继续使用原V010未用满的账，也不改已冻结fixture**。建议Owner下一次仅审议**同V010的独立、前瞻性、严格受界的单省corrected HA价格域对照实验**：
- 原V010首次`(rah=.055,w_eff=1.7085897435,rb=.02)`失败作为**只读历史观察，不重跑、不改回执**；
- 独立新诊断输入`(rah=.0675,w_eff=15.5,rb=.02)`，保留**V010同20×20×2、a=[0,10],b=[-2,5]网格、相同V0生成、同corrected selector、同严格B/D/KFE合同**，最多一次省级HA尝试，非原两省firm可生的工资，不伪称两省GE或健康区；先验证历史价格点在corrected体系是否有可采纳解。
- 若中央对照可通过，才考虑明确新许可下分别改变一个输入的其他受限点以识别`rah`和`w_eff`作用；若失败立即保留并审源码/领域约束，而不是随机调参求PASS。
- 新价格只是**诊断人工输入**，不是对`synthetic_fixture_v1.json`进行追改，也不能无记录改`GovInv/Zt`、地区工资税、raw/used资本、HJB根/容差。任何科学执行前要另行冻结新输入身份、源码SHA、额度、路径/保护和停止，明确与旧已耗4/6 pytest、1/4 science driver、1/26 HA不混账，明确独立合同是否引用旧额度；未经Owner批准不执行。

当前`ACTIVE_CODEX_TASK=NONE`，后续科学决定未批准，`Results=FALSE`、A16 FAIL_CLOSED、C9 PAUSED、CALL_LEDGER UNRESOLVED、window UNACCEPTED、真实C8 A–D REQUEST_ONLY、原8 dirty/index/common-dir保护，V011 NOT_STARTED。
