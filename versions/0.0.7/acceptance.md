# V0.0.7 独立终验：原C8历史来源交叉表与经济单位关键义务

2026-10-15（Asia/Shanghai）

**终态：`CLOSED__ACCEPT__HISTORICAL_SOURCE_CROSSWALK_AND_ECONOMIC_UNIT_CRITICAL_OBLIGATIONS_ONLY__WITH_OBSERVATIONS`。**
**本版只接受HISTORICAL_SOURCE_CROSSWALK_DOCUMENTARY与ECONOMIC_UNIT_CRITICAL_OBLIGATIONS两项受限证据，既不是经济单位通过，也不是实际模型BUG已经独立确诊或允许修复。**

## 1. 固定合同与候选身份

- Owner已启动 V0.0.7，Astra冻结计划 `635cea1c54afecc78d6678805a263a889985a291`，tree `a7b77ef0c915ad28dd9f4dcd90022c4e3ac70f9d`，`versions/0.0.7/plan.md` blob `940ac55265f5ee9bf9b82c3e955f900fbddf32ce`。独立实施授权：`ASTRA_APPROVED_EXECUTION__CH5_V007__SOURCE_ONLY_HISTORICAL_AND_ECONOMIC_UNIT_AUDIT_ONLY`。本版不授予受保护文件访问或模型运行。
- 真实候选 commit `d8bb49d86ea674ea4ff5e3fdf03929baa08a6514`，Git tree `9b685397ad5bc76a4ac3bf4203776389742c5ec5`，唯一 parent `198b70f8b1c7b802bc2e18cb4bb0825bdb495b00`；GitHub compare恰为1 ahead/0 behind，仅新增三个冻结白名单文件。远端候选分支 `codex/ch5-v007-source-unit-audit-20261015` 已回读确实指向上述 commit。远端main并未包含候选，本验收不合并或推广main。
- 三份候选：[完整来源/量纲证据](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/d8bb49d86ea674ea4ff5e3fdf03929baa08a6514/versions/0.0.7/provenance_unit_evidence.md)、[执行回执](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/d8bb49d86ea674ea4ff5e3fdf03929baa08a6514/versions/0.0.7/execution.md)、[候选摘要](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/d8bb49d86ea674ea4ff5e3fdf03929baa08a6514/versions/0.0.7/acceptance_summary.json)。GitHub实际blob分列：`provenance_unit_evidence.md=6dd60d145aa6d6335c3b09973ecbac406b7eade1`、`execution.md=9404fefc617b0a6e5dbc66e7079b522029f113f7`；`acceptance_summary.json`已独立读取其完整正文并核实PRE_SEAL状态，不用其空候选SHA代替后封存回执。
- 候选成功普通non-force push和远端分支/commit/tree事实已由GitHub独立回读；Windows候选外本地delivery JSON、原本地HEAD/index/8 dirty字节哈希、测试/工具运行耗时、分项存储与瞬时资源只能列为`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，非网页直接检查。Codex报告总约10.5分钟、新增存储15,335,719B，科学Python/pytest/MATLAB/solver、旧模型/真实consumer和protected stat/read/hash/parse/extract均0；本版既定不要求pytest测试，不能以无测试宣称模型验证。

## 2. 实质受限接受（INDEPENDENT_GITHUB_CODE）

- 原C8的runner/dispatch/accepted执行来源以及历史manifest的独立接受范围已核；历史manifest为5,141成员+manifest自身第5,142项，当时已回读、SHA `5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`，成员汇总63,801,638B**不是manifest本体大小**。当前原件身份、字节、是否可安全读取均未知。C6→C7严格R2为2/9，C7→C8为5/9；不等于固定点/GE/Results。旧C8 ledger PASS不解决后续C9 CALL_LEDGER_UNRESOLVED。
- 独立审查候选所引GitHub Python代码：`validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py` L289–295确实在`source=dict(province)`后把原`Lt_prev`覆盖为当次household `Lt`，而现在的 firm `Lt`为`migration.lt_supply`；同文件L361–371虽存储了下一轮firm Lt_prev，但下一轮实际caller又可覆盖它。`firm.py` L77、L93真实使用`Lt_prev`进入劳动变化项。没有当前人口/劳动单位可比证据。
- `optionb_turn2_household_integration.py`的`_province_inputs`将同一个`state.Tt`传入家庭transfer；`nonlinear_continuation.py`传到cell，`selector.py` L407–415作为家户预算直接加项；`firm.py` L135又在地区`Govinc`直接扣相同字段。`AtTax`是质量加权均值却在firm端直接作为财政项，`Lt*tau`在工资税比例楔子解释下需要货币计价桥。这是可证伪、未闭合的科学量纲义务，不是已证实的real-C8财务错误。
- `fiscal_diagnostics.py` L41–44仍按地区Govinc减`Bt*rb*N`，加重地区总量与家庭均值尺度一致性义务。资产/人口的条件单位`M=10万元`、`U=100人`下`wealth_i=At_i*N_i`要求`[At]=M/U`；`q=1000(Y/N)`仅可证明换算代数，不能证明household At、Ct、wjt的历史经济尺度。
- 候选用最小符号反例、FOC货币重新标定条件、labor/price/calendar和Owner待决问题清楚区分“源忠实”“条件性经济解释”“历史实际原件认证”。不动方程、参数、HJB/KFE、S、C1、raw-ra0/lagged、税率位置或旧Results资格。

## 3. 本轮额外独立取得的原MATLAB辅助证据（非Codex执行回执）

Astra在**本轮**只读查看Owner上传的原始 MATLAB ZIP 中精确7个有关文本（没有执行MATLAB，也没有访问protected C8历史产物）。该用户上传包属于`AUXILIARY_ORIGINAL_MATLAB_TEXT_VERIFIED_BY_ASTRA`，**不能**视为历史C8当时的MATLAB execution code SHA、C8真实原件或已采纳新科学方程；本审议不发布原ZIP内容。
- `HANK_2ASSETS_HJB.m` L347计算`Lt=sum(z*l*g*da*db)`并于L397写`results.Lt`；`HANK_mp_1turn.m` L14–16调用HJB，L23–26将按N放大的跨省劳动填到`Lt_supply`，L44–46直接将HJB结果送入firm，中间没有把`results.Lt`覆盖为地区总劳动。`HANK_firm.m` L9用`results.Lt_supply`做当前Lt，L21从`results.Lt`取旧劳动，用于L35中的NKPC项。**对这个上传的版本，原MATLAB一轮函数不存在“firm前已换回地区总劳动”的解疑解释**，加重劳动尺度风险；但不能由此确定真实C8运行字节及量化误差。
- `HANK_2ASSETS_HJB.m` L31、L90、L111及L352–353把`Tt`作为家户收入项，L365、L406用均值构造`AtTax`；`HANK_firm.m` L95明确相同`Govinc=Corptax+Lt*tau+AtTax+GovInv*ra-Tt`；`HANK_mp_1turn.m` L65的`Bt*rb*N`人口乘数与此直接加总形成不同尺度需要解释。`Lt_seperate.m` L6–15直接说明origin个人劳动再乘人口N；`wage_caculate.m` L8显示destination税，`Lt_seperate.m` L7为origin税，方向一致。不能因式子来自原MATLAB便自动通过经济正确性检查。
- Codex诚实注明其本地会话未直接取得原MATLAB辅助ZIP；Astra补充的本轮独立证据不追溯改写Codex执行账，不替代后续真实历史版本/模型时间/numeraire证据。

## 4. A–D读取建议仍仅REQUEST_ONLY

- A：单 C8 manifest，1,048,576B；A+B：5文件、3,538,944B；A+B+C：36文件、4,046,848B；含可选D：37文件、4,112,384B，已纠正前版中间累计少计64KiB的问题。
- manifest本体大小当前未知，不能把历史5,141成员63,801,638B当文件本身大小。任一A–D阶段的存在性stat、大小检测、字节读取、hash、解析、字段提取**全部0授权**，每阶段必须有新的Owner精确批准及匹配该被动操作的安全/权限/输出生命周期审议。A成功不自动放行B/C/D；B3与初始run004北京来源不得默认替代；目录/reparse攻击A16仍未证明。
- 即使原37件全部匹配，经济单位、真实C8 consumer、GE fixed point和Results也不会自动被认证。

## 5. 终裁与下一步

**`CLOSED__ACCEPT__HISTORICAL_SOURCE_CROSSWALK_AND_ECONOMIC_UNIT_CRITICAL_OBLIGATIONS_ONLY__WITH_OBSERVATIONS`**

仅`HISTORICAL_SOURCE_CROSSWALK_DOCUMENTARY_ACCEPTED`与`ECONOMIC_UNIT_CRITICAL_OBLIGATIONS_ACCEPTED`。`REAL_C8_SOURCE_AUTHENTICATED=False`、`ECONOMIC_UNITS_VERIFIED=False`、`REAL_CONSUMER_AUTHORIZED=False`、`GE_CONVERGED=False`、`RESULTS_ACCEPTED=False`。本版关闭，不能以“来源或单位义务接受”宣称真经济结论、改写HJB/KFE/财政/劳动定律或重新运行受保护模型。

未来需Owner聚焦两项经济学真正取舍：劳动对象/动态基准（Lt_prev versus destination current Lt）和财政税/资产收益/人口转移的共同计价。优先把原MATLAB辅助赋值链与模型归一化文献做一个真正可证伪的选择；若科学修订确有必要需独立立版和合同。阶段A的真实读取另须严格操作许可，不属于本版。V0.0.8 NOT_STARTED、下一版基线接纳UNDECIDED，未授权新实现、科学调用或读取。

始终保持Owner采纳的Option1条件诊断、人口/人均且不N=P/3、2017 observed→2018 target历史回溯、价格方法归属但direct_price_verified=False/price_verified=False、raw-ra0同S lagged及C1，严格R2 2/9+5/9未过。Objective A16 UNRESOLVED/FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE、旧data/science/consumer预算CLOSED及D3-real/D4-real未授权均保持。
