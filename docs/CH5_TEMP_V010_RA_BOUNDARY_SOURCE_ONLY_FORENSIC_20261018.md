# TEMP-V010 100轮原始资本回报上界与价格传导：独立源证分析

**日期：2026-10-18；审查状态：`SOURCE_ONLY_FORENSIC_COMPLETED__SCIENTIFIC_CAUSALITY_UNPROVEN__NO_SOLVER_AUTHORIZATION`。**

本文由Astra对已上传的 TEMP-V010 MATLAB-faithful HA黑箱100轮私人证据ZIP、原始 MATLAB 程序ZIP，以及同一固定模型Commit在ZIP内的 Python 源码进行**只读静态复算**产生。没有新运行HA、HJB、KFE、政策选择器或GE；没有代码补丁、参数修改或新任务。原TEMP100轮结论 `OWNER_100_ROUND_LIMIT_NONCONVERGED` 及正式V010 `ACTIVE_TASK=NONE / Results FALSE / V011 NOT_STARTED` 不变。

## 1. 原证身份

- 100轮证据ZIP：`TEMP_V010_MATLAB_HA_BLACKBOX_100PLUS_EVIDENCE.zip`，6,352,227B，SHA256 `4CD602CC3589F404E176937B96D21E265EB036374BCA95D708E5DC246A394156`。历史独立验收已验证909/909内文件。此次复算的两个数据文件：`run/trajectory.jsonl`（100轮）、`reference/fixture_RAW.json`（2,948B、Git Blob `40915658d93403cfc21b33a6b864b332b7857749`）。
- 固定V010模型 Commit `94de4501dec051b969bee9d852eba2d4591f30ef`、Tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`；ZIP内同源 `firm.py` Git Blob `3b902a2c62df816bdb85b0e09b127f1b7a547130`、`wage.py` Blob `1459d1b465f134a2d8746c252e71e060459465ca`、`steady_state.py` Blob `5fa6c73884067391bd2b998d4b050443c97c38e8`、`capital_network.py` Blob `dbb182f63ac62fd0cd8495463239c8e8c246a61b`、`one_turn.py` Blob `4242cf787d8c30bec7ac884dcd9e24bcea288c28`；独立重新计算上述Git blob均匹配固定源。
- 临时桥 `experiment_bridge.py` SHA256 `73D21D91DCDF421E5F65EEE7EEF862978A5EC720E5AD754C3533EC934B05FA28`，未更改源HA。历史成功的MATLAB-faithful HA `exports/matlab_faithful_two_asset_ha.py` SHA256 `B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3`继续只作原字节黑箱。
- 原MATLAB ZIP中 `HANK_firm.m`、`HANK_mp_1turn.m`、`HANK_mp_1eq.m`、`wage_caculate.m` 已直接阅读并单独验证。中文注释原始编码不同于运行转换文本，不用Git重写原版文件；这里引用的是对应函数/分支含义。

## 2. 第100轮及全过程：ra_used是受界报价，不代表原资本收益已经接近界内

企业公式（MATLAB `HANK_firm.m:40-74`，V010 `firm.py:87-134`）：

\[
Y=ZK^{\alpha}L^{1-\alpha},\quad r_k=m\alpha Y/K,\quad
r_{a0}=r_k-\delta+\max(0,\Pi)(1-\tau_c)/K,\quad r_{a,used}=\operatorname{clip}(r_{a0},r_{amin},r_{amax}).
\]

全部100轮、两省的 `ra0 > ramax=0.09`，其各自**最小**原始 `ra0` 分别为0.373331和0.415542；所以触界是实质性缺口而非近容差的误判。

| 状态 | SYN_A | SYN_B |
|---|---:|---:|
| 第1轮 `ra0` | 2.006987 | 1.785043 |
| 第25轮 `ra0` | 0.762377 | 0.828139 |
| 第50轮 `ra0` | 0.620461 | 0.707391 |
| 第75轮 `ra0` | 0.570389 | 0.610741 |
| **第100轮 `ra0`** | **0.384584** | **0.427239** |
| `ra_used` 全100轮 | 0.09 | 0.09 |
| `ra0` 全100轮最小 | 0.373331 | 0.415542 |
| 第100轮 `K=K_private+GovInv` | 2278.055 | 2668.517 |
| 第100轮 `L_firm` | 154.718 | 163.026 |
| 第100轮 `Y` | 1578.827 | 2020.823 |
| 第100轮 `rk` | 0.409584 | 0.452239 |
| 第100轮利润`PIt` | 0 | 0 |

本次F25原失败 `NO_ADMISSIBLE_POLICY` 属正式V010 corrected-selector线路，不能从TEMP旧黑箱此次完成100轮推定该数学门已修复。

## 3. GovInv/Zt控制器确实在响应，但只能间歇调整

原MATLAB `HANK_mp_1eq.m:42-61` 与固定V010 `steady_state.py:_adapt` 均在 `max KN gap <0.1` 且未收敛的条件下，按 `ra_used > ramax-0.02` 执行 `GovInv_next=1.1*GovInv`，同时按GDP目标偏离>1%调整Zt。原 `tKN_next=0.6*KN_current+0.4*tKN_prev` 保留。此门为**全国／全部合成省份最大KN gap的联合条件**，不能因某一省单独满足就改动该省。

实际100轮内两省各触发26次GovInv上调（共52次），各有23次Zt调整（共46次），其余轮次不调GovInv；GovInv增长倍数分别为 `1.1^26≈11.918`。第100轮A/B的GovInv分别由初值100/120升到1191.818/1430.181，Zt由6/6.2变为2.0323/2.3167。对应原始收益从约2降低到约0.4，但**未**回到0.09以内。

由于 `ra_used` 被clip成0.09，控制器只能观察它是否靠上界，无法从该量本身看出原始 `ra0` 离上界是0.01还是1.9。原收益/产出/GovInv/HJB是否可收敛仍要看真实动态，不能从单轮反事实断言500轮结果。第100轮max KN gap约0.107522、跨轮Y gap约0.012719、HA converged 0/2，因此除资本回报触界外，其余原停止条件也没达到。

作为**静态经济尺度的必要条件读数**，第100轮两省利润恰为0，`ra0=rk-δ`。若**只是假设**持有当轮 `m`、`alpha` 与冻结GDP目标不变，要令原始收益降到0.09且δ=0.025，则由 `rk=m*alpha*Y/K` 推得 

\[
K_{req}=m\alpha Y_{target}/(0.09+0.025).
\]

A/B分别为约7708/9867，是当轮实际K约3.38/3.70倍。此值并非另一组稳态求解，也**没有许可据此直接把GovInv或资产改成K_req**；m、Y、L、Z及HA均内生变化，固定其它变量的前提在真实外层不会成立。

## 4. 更值得科研复评的是两条跨部门价格传递差异（不是HA内部bug）

### 4.1 原生raw ra0传给家庭，而企业使用clip后的ra_used

冻结V010和此次TEMP桥把上一完整轮 raw 回报作为下轮资本网络的评分与收益：`S[j,i]`配置量与收益使用同一个矩阵，`rah_i=Σ_j S[j,i]ra0_j`，而企业当前 `ra_used_i=0.09`。在第100轮，S=[[0.9,0.2],[0.1,0.8]]，`rah≈(0.388849,0.418708)`，分别是企业使用回报的**4.32/4.65倍**。

原MATLAB `HANK_mp_1turn.m:28-41`则在企业运行前，按上一轮各省已受界的`ra`计算家庭`rah`（原固定foreign-share公式与V010 same-S已采纳机制也不同）。所以 TEMP“HA算法黑箱不改”不等于把MATLAB原来的**跨部门输入报酬**也复原。该差异是历史V010已采纳的经济传导修正，**不能擅自判bug或直接撤回**；却是当前合成实验不收敛的优先核查对象。

### 4.2 有界`wjt`与未截断`wt0`两种企业工资信号

MATLAB `HANK_firm.m:66-74,80-81`把企业工资 `wt0` 裁切成 `wjt`，随后 `wage_caculate.m:4-11` 使用**截断后的 `results{j}.wjt`**计算家庭下一轮复合工资。当前TEMP桥 `experiment_bridge.py:39-40`采用V010接口 `mainline_effective_wages([f.wt0 ...])`，即未截断的 `wt0`；`wjt` 虽在每轮都是1.3，却未进入家庭的复合工资路径。

用**同一轮已观测**税率、phi与sigma，对原`wage_caculate`解析式分别代入两种工资信号（只做代数计算，**绝不运行HA或生成另一条轨迹**），得到：

| 第100轮 | SYN_A | SYN_B |
|---|---:|---:|
| 原始厂商工资 `wt0` | 4.020457 | 4.935043 |
| 实际存档工资 `wjt` | 1.300000 | 1.300000 |
| TEMP实收家庭 `w_eff`（以wt0求） | 6.947956 | 7.028788 |
| 仅代入`wjt`所得MATLAB式 `w_eff` | 2.038005 | 2.018992 |
| 原报价/TEMP信号比率 | 3.409 | 3.481 |

全100轮以`wt0`复算TEMP实际 `w_eff` 的最大误差**0**，故不是读取字段混淆；在冻结phi/tax/sigma下以裁切`wjt`做同状态代数读取恰为常数2.038/2.019。这是**静态代数差异、不是替代方案能令HA收敛的实验证据**。同时，原V010财政工资税口径使用`tau*wt0*Lt_firm`，与MATLAB老财政已有修订；不能只改工资报价而不审查财政与劳动一致性。

### 4.3 被clip的价格差额变为企业税收补偿，财政读数须分账

固定firm源公式将 `ra0-ra_used` 差额乘 `Kt`，将 `wt0-wjt` 差额乘 `Lt`，计入`Corptax`边界补偿（而不是原生产真实利润）。第100轮A约为(671.1+420.9)≈1092、B约为(899.9+592.6)≈1493；分别约等于当轮GDP的**69.2%/73.9%**。这不是模型的现实税收率或政府预算真正出清证明，而是**合成报价尺度与原稳定化clip之间差距巨大**的又一个诊断。历史财政恒等校验通过不能代替对这些修订价格与收益传导的经济合理性判断。

## 5. 证据分类、不能推断与建议的下一科学决策

**已独立核实**：100轮公开可重算的静态轨迹字段、ra0在每轮均超界、同轮企/家庭回报差异、GovInv/Zt触发次数与固定控制器公式、原MATLAB和冻结V010工资来源不同、原始资本网络 payoff 使用raw same-S、固定内生利润归零条件及静态尺度/K恒等计算。原100轮科学调用的Windows进程真实性仍以已上传回执证明而非此处OS重跑。

**未证明**：这是单一的代码bug、上述价格传递差异足以解释全部不收敛、原HA算法有错或换价格可取得稳态、合成fixture与真实31省校准同分布、继续到500轮必失败。归因需有明确、冻结的价格桥选择与受界科学对照实验；不得把代数复算的反事实价格当成一次新的真实HA结果。

**建议优先级：**(A) Owner批准在**独立TEMP对照**中审议是否把家庭收益从 `same-S raw ra0` 改为“使用`ra_used`的同S滞后收益”，同时保持S数量守恒和原资本score的时序定义可区分；(B) 单独对照家庭工资使用`wjt_used`而不是`wt0_raw`，保留单次目的地税及显式财政桥。采用两个变量可分别试验，而不是未经控制把它们同时改成“新的V010”。如果Owner只愿先做一个低成本探测，先做**price-bridge纯代数stub及相同初值的冻结对照设计**，无需重跑HA；之后才独立批准科学HA预算。

这属于更改V010既有的**跨省收益及工资经济传导合同**，即使不改HA黑箱，也需要Owner明确E3科学决定。正式V010原冻结plan/旧失败/科学约束、TEMP实验停点与全部旧预算照旧；当前报告本身不授权另开科学进程，不修改SCIENTIFIC_DECISIONS.md。
