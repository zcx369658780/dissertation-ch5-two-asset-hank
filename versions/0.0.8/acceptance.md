# V0.0.8 独立最终验收：corrected-model 人工经济体数值可行性与真正HANK-IRF阻断

日期：2026-10-15（Asia/Shanghai）

**Terminal: `CLOSED__ACCEPT__CORRECTED_SYNTHETIC_ACCOUNTING_CONDITIONAL_STATIONARY_AND_SHOCK_DIAGNOSTIC_ONLY__REAL_HANK_IRF_BLOCKED__WITH_OBSERVATIONS`**

**本版受到独立接受的只是新隔离 Python corrected-model 在人工经济体下的数学/复式账户与条件稳态（1、2、31个人工省份）及单省人工条件冲击路径；真正两资产 HANK 稳态/31省现实反事实/正式动态IRF仍没有通过或获得授权。Gate D 正确 BLOCKED，不因产品希望IRF而扩大模型资格。**

## 1. 冻结合同、代码候选与 GitHub 独立核验

- 冻结治理commit `e222b302176f8ff627ced1442196299f804b9aa7`，tree `596bb0d009287a6a05434d4fe848ea8b61019f71`，plan blob `891e8dae2eead0c5c39bf20a7542c68a004b5e94`，独立执行许可 `ASTRA_APPROVED_EXECUTION__V008_CORRECTED_MODEL_SYNTHETIC_STATIONARY_AND_SHOCK_GATES_ONLY`。
- 已独立从GitHub读真实commit对象：`d41d229b681e09b913c21deff7a057085b9bc419`，tree `88833acf90613380afa30ab8d6ee7e0297e98664`，唯一parent `d8bb49d86ea674ea4ff5e3fdf03929baa08a6514`，1 ahead/0 behind；只新增正式白名单的六个`reconciled_*.py`模块、四份`test_v008_*.py`及`versions/0.0.8/`三份交付（共13路径），科学原代码、原dirty文件与main均不在提交diff。远端`codex/ch5-v008-corrected-model-20261015`分支HEAD已回读为候选。
- [科学数值报告](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/d41d229b681e09b913c21deff7a057085b9bc419/versions/0.0.8/scientific_reconciliation.md)、[机读数值摘要](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/d41d229b681e09b913c21deff7a057085b9bc419/versions/0.0.8/acceptance_summary.json)、[执行/保护账](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/d41d229b681e09b913c21deff7a057085b9bc419/versions/0.0.8/execution.md)位于**固定代码候选**，不是治理分支中的同名相对路径。json blob `4bb776159616a603a0327592e7eb68b55196ac00`，230,974字符，包含人工稳态完整未知量、残差、四条路径每期响应。报告PRE_SEAL的candidate_sha/tree=null是避免提交自引用的正常前置状态，不能反称无远端候选；本验收已独立核实最终Git对象。
- GitHub组合CI status数为0，没有CI执行PASS的独立依据；Codex自报`24 passed,1 skipped`、5/8 pytest进程及Windows final_view属于`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，不能称Astra自行在Windows复跑pytest。

## 2. Gate A：合成经济数学Oracle，有限ACCEPT

静态实际源码及测试独立审查：
- `reconciled_labor.py`的双边CES、`phi[j][i]`目的行来源列、完整有限离散家庭分布按`N_i p_i z_i h_ji`积分与净工资收入对偶，未把 CES 指数硬当作简单`sum_j h`。测试有`eta=1/2`对应下的不同曲率、非对称省份、`N`缩放、状态`z`与工资独立oracle；
- `reconciled_household_prices.py`全国税仅一次，迁移费用种类显式；`reconciled_fiscal.py`Journal付款/收款、资本所有权私公分割、AtTax互斥归属选择和复制人口/地方分析分账均有受限数值oracle，旧raw/used clip的未接受混账被拒绝；
- 新测试通过是Codex本地回执等级，测试静态覆盖由GitHub直接见证。正迁移成本和非零`AtTax`仅在Gate A单项人工会计oracle，**没有**参与后续Gate B/C的完整均衡；不能说已闭合现实中介/迁移成本体系。
- 经济实现仅支持`SYNTHETIC_SCENARIO`，资产非负且净流动资产显式假设为单一全国政府债权；并不认证现实地区债务或2009/C8经济单位。

## 3. Gate B：人工条件稳态通过，独立数值复算

`reconciled_stationary.py`真实使用 n 个对数税前工资与统一人均转移`t`的n+1维未知量，有限差分/阻尼Newton以`log(Ls/Ld)`和全国预算残差求根；资本、家庭分布、税率、`markup=.9`、`delta=.05`等明确标作人工给定条件。没有把目标稳态直接返回，也没有调用历史 HJB/KFE/Euler/real consumers。
- 根据固定机读摘要，Astra独立以另外的算术表达式重新构造`N/A/Kg/S/Kprivate/K`、净工资CES、两类家庭分布的c与ell、双边总劳动、企业劳动需求/Y、收益分配、消费和财政/资源预算；与报告的三个`Y,C,L`匹配到浮点舍入，最大绝对差约`5.33e-15`。
- 三个有限人工稳态（顺序1/2/31省）残差向量评估次数10/17/166，最大绝对归一化经济残差分别`1.1765033391952784e-12`、`1.4443497459199443e-14`、`9.950791095908994e-14`；最高会计残差分别`8.274492202531292e-13`、`1.2309835524427652e-14`、`9.950791095908994e-14`。Astra从JSON逐字段重新计算所有残差最大值，且以独立预算表达式复算政府和资源误差均在冻结门内。
- 所谓`firm_wage_foc/capital_condition/capital_supply/household_budget/FOC`里有显式代数消元后由同组定义强制满足的恒等式；真正数值联立求的是 n 个劳动市场和一个财政工具，不能把全部已声明残差当作独立动态方程或资产市场联解。得到`SYNTHETIC_CONDITIONAL_STATIONARY_ACCEPTED`，但**不能**升级为31省两资产HANK一般均衡、稳态KFE分布或现实校准。

## 4. Gate C：四条单省人工条件冲击路径接受，且不是IRF

- 同一个已公布1省Gate B起点；`shock_path`按人为设定的三个AR(1) `rho=.5` 坐标：TFP t0、全国工资税 t10、公共资本存量 t20，四个预算内路径为40期零冲击、40期满幅1e-4、40期半幅5e-5、20期满幅1e-4。**这不是三个互相独立政策IRF、不是31省响应、不是前瞻性跨期动态均衡**。
- 每条路径把各期**独立的静态均衡方程**组成一个块对角联合求根，不因joint-block代码就使时期之间产生内生状态传递。已发表的每期未知量、人工shock、Y/L/C/转移及全部会计残差，Astra另外逐期重建并对比合计140个period blocks：Y完全匹配，L差最大约`2.22e-16`、C约`1.11e-16`；每期政府/资源/市场残差均符合冻结界。
- 从公开每期数组另算：零冲击误差0；前20期prefix差0；半幅局部响应相对偏差`6.810212990015854e-6`；末期相对响应`9.13651085896238e-8`，与Codex报告完全一致。全部是条件算术响应；明确`CONDITIONAL_SHOCK_PATH_DIAGNOSTIC_ACCEPTED`。
- 公共资本`SYNTHETIC_EXTERNAL_CAPITAL_ENDOWMENT`只通过“外部人工实物赠与/相反捐赠方资产变动”提供期界存量变动，**不是**财政投资政策的资金和实物动态闭合。其`resource_with_grant_residual`形式上把同一gift在资源两端相抵，是人工场景一致性而非经济识别。
- Codex已报告C预算四条路径全部消耗，因此最终封存pytest`24 passed, 1 skipped`，其中跳过C路径重新执行，并未冒充最终树的完整C复跑。最后添加的省分账与资本实物赠与函数在final tree聚焦测试中验证；原C主路径的final-tree过程一致性主要由报告的未改前缀说明和本轮公开数值静态复算支持，记`WITH_OBSERVATIONS`，不重开已耗尽的path预算。

## 5. Gate D：真实动态IRF正确BLOCKED

`reconciled_irf_gate.py`对动态HJB终值、KFE前向分布、资产/国有资本/政府债务转移、前瞻定价/通胀、跨期货币财政闭合、逐期完整HANK市场出清、初末合法HANK稳态和冲击时间/终值误差等8类实证要求缺失时返回`IRF_BLOCKED__NO_DYNAMIC_HANK_CLOSURE`。它最多表明在未来另有独立采纳证据之后可申请真正IRF实验，**从未签发动态科学调用许可**。

现有Gate B没有household Euler/HJB/KFE更新，Gate C只用外生人工冲击逐期重新解静态方程，旧MATLAB`mpHANK_shock_2000.m`逐期调用也不能升级。REAL_HANK_IRF、完整两资产HANK稳态、GE/IRF Results继续FALSE。

## 6. 资源、保护、最终分类

Codex报告完成预算（均`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，未读LOCAL_ONLY Windows全回执）：pytest 5/8，root尝试10/12，人工31省求解2/2，路径4/4，单root≤200 evaluations，路径≤40期；19.4分钟；新增存储17,836,781B，采样峰值约30.3MiB。没有数值失败；两次行政包装器错误记录修正。原8 dirty文件/index字节摘要前后相符、HEAD/branch未改且untracked/ignored未重扫仅由Codex报告；GitHub可以独立核实候选只增13文件、无原历史科学代码/main变化，但不能假装读取原D盘。无GitHub CI PASS证据。
- **`CLOSED__ACCEPT__CORRECTED_SYNTHETIC_ACCOUNTING_CONDITIONAL_STATIONARY_AND_SHOCK_DIAGNOSTIC_ONLY__REAL_HANK_IRF_BLOCKED__WITH_OBSERVATIONS`**。本版首个数值里程碑完成且关闭；不为下个IRF夸大Gate B/C。是否正式从人工经济体进入完整 corrected HANK/Euler/HJB/KFE/transition，必须另经Owner明确决定、完整科学/数据/资源准入、独立冻结和新的预算，不能继承当前耗尽的31省/路径额度。
- 继续 `A16 UNRESOLVED/FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、`model_activation=False`（指旧真实模型）、`Results FALSE`、旧受保护data/science/consumer预算CLOSED；真实原C8 A–D仍REQUEST_ONLY，manifest长度UNKNOWN，不使用B3替代或重开G0。V0.0.9 NOT_STARTED、NEXT_BASELINE_ADOPTION=UNDECIDED，不能自动main merge或后继模型数值运行。
