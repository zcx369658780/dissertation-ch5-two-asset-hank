# V010 corrected HA 历史价格单点对照：新科学授权冻结合同

更新：2026-10-15（Asia/Shanghai）。

**状态：SINGLE_POINT_CORRECTED_HA_SCIENCE_FREEZE__INPUT_LOCKED__AWAIT_SEPARATE_TASK_ISSUE。**
**科学权威**：Owner明确批准上一轮拟定的`rah=.0675,w_eff=15.5,rb=.02`单点corrected HA新授权；Astra将其限定为一次**新的、独立记账**的synthetic省级HA科学调用。不修改历史V010冻结`plan.md`，不重新分配旧科学次数，不改原`synthetic_fixture_v1.json`。

## 1 固定代码与研究输入

- 唯一模型来源：`94de4501dec051b969bee9d852eba2d4591f30ef`，tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，sole parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`；未科学ACCEPT的V010工程候选。
- 全量输入放在`versions/0.0.10/corrected_ha_price_probe_v1.json`。该文件在**本合同固定Git提交**中拥有唯一Git blob，未来task必须准确填写freeze commit/tree/manifest blob及本合同blob，不用动态分支最新值替代。
- 冻结人工根：原`synthetic_fixture_v1.json` blob `40915658d93403cfc21b33a6b864b332b7857749`，使用其完整`parameters`、`grid`以及SYN_A `transfer=.1,rb_gap=.07`。**仅新对照的**`HAInputs.rah=.0675`、`HAInputs.w_eff=15.5`；`HAInputs.rb=.02`与原一致。已扣税的有效工资直入HA，不在HA内部重复征税。
- 网格`(b,a,z)=20×20×2`、b-fast F-order，`a=[0,10]`、`b=[-2,5]`、`z=[.8,1.3]`，原`z_generator`不变。原V0公式、scalars及`Delta=1000`与冻结参数完全相同。
- source Git blob至少要逐项验证：`multi_province/mainline_household_runtime.py` `3d2d7d92aea0036f36d88ef15c05cbb3b40eba90`；`corrected_diagnostic/selector.py` `51517dde0c829060b6e0c0d594ec60e7e6143883`；`corrected_diagnostic/generator.py` `f86234340c6e09c7129225da1677614669754177`；`corrected_diagnostic/option_a_step.py` `e0fcbf01af9b1778d245d960fe85c592f55c032c`；`corrected_diagnostic/nonlinear_continuation.py` `a473f86eef22ad893673dba2a80ec8029de8afd1`；`corrected_diagnostic/contracts.py` `41186454de5ba1f55d3ba273f7ce57457ded11ca`；`multi_province/corrected_household_adapter.py` `f79e089f06d0d74867284dc88c94c594215dc02e`；transitive `v1_q1_topology.py` `a238c999d3a6e18e8672efa1aae00498e747d403`；`q1_kfe_validation.py` `45f4b95024c4441809dba3fe27044f25b3339f0f`。
- 只可使用此commit中原已接受corrected算法及其导入链，无代码修复/库升级/参数调试/回退旧MATLAB HJB-KFE。

## 2 理论解释与不得越过的推断

2026-09旧MATLAB-faithful曾在同数字`(ra=.0675,w=15.5,rb=.02)`及原20x20x2资产盒报告HJB+污染行KFE成功；但此前旧`w`作为家户工资字段仍存在税楔语义，不必然等于这次**已扣过税的`w_eff=15.5`**；求解器、初始价格映射、KFE法和经济模型数量也非全同。因此这次是`historical_numeraire_nearby_numeric_diagnostic`，不是同一经济体重复执行，绝不能用旧结果当新PASS。
原V010失败点`rah=.055,rb=.02,w_eff≈1.7085897434929322`只作历史只读对照；两个坐标同时变化，本单点无论PASS或FAIL均**不能**分别归因于`rah`、`w`或真实31省GE存在性。

## 3 新增硬预算与受限执行

- **恰好至多一（1）次HA科学尝试**，一个（1）science进程，pytest=0，宏观迭代=0，IRF=0，MATLAB=0，数据读取C8/B3/2017/2018=0，模型源码变更=0。
- 单HA HJB value updates≤100、policy/Q maps≤101、selector cells≤80800、scalar roots≤400000（其中V0初值root也计入）、直接稀疏solve≤100、终端source-free KFE≤1且只在HJB的同checkpoint`B≤1e-8,D≤1e-7`及合法Q门均PASS后准予调用；后向误差≤1e-12、global deterministic-halving最多52。根/selector各原本的内部细分guard依旧有效。
- 新任务专属累计墙钟≤2小时（含只读预检和1 science进程）；新独立科学输出≤32MiB，输出增量和Python缓存/日志均要计数；RSS实测目标≤512MiB，无法取得则`UNKNOWN`；额外安全clone若必要其Git对象和文件≤1GiB，不得触旧保护仓Git common-dir。硬额触及立即STOP。
- 唯一允写是新的隔离输出`D:\ProjectTemp\ch5_v010_corrected_ha_price_probe_20261015_01`（允许私有runner脚本、run JSON/log与摘要；必须无旧输出覆盖），不许更改任一仓库的tracked源文件、旧研究证据、旧fixture/plan或模型Git分支。执行只能从**已固定候选Git来源**加载生产方法，不能把私有runner中的更改过的方法当科学结果。
- 可重用现存独立V010实现clone作为**只读源**，但必须证明与固定候选全量Git commit/tree一致，并逐项确认源文件blob及实际Python `__file__`；如缺失或有改动，才可在本新目录安全建立不共享原dirty仓的独立Git clone。禁止进入或修改`D:\ProjectTemp\c5k1bturn56`及其index/8 dirty/外部common-dir/untracked/ignored。严禁调用`deep-learning-hank`等其它项目。
- 只可写一个轻量、可审的私有runner来读取冻结manifest的完整`ha_inputs`、检查Python/NumPy/SciPy版本与源码哈希、预封存输入SHA后调用`HAInputs`+`solve_conditioned_household`**一次**；`global_ledger`至少含`roots`/`cells`且新增尝试扣1，原V010已耗账另列不得清零。超限/依赖/异常一律STOP，无自动重试。

## 4 接受与停止

成功定义仅为此点`STRICT_CORRECTED_HJB_AND_TERMINAL_SOURCE_FREE_KFE_PASS`：全policy/Q完整合法、同checkpoint B/D及KFE质量通过且五字段聚合合格；若存在bmax/amax边界质量或明显网格敏感性，另注明诊断局限，不能提升为`GE`或真正历史数据稳态。

失败必须记录第一个fail stage/checkpoint/flat/原root与selector拒绝原因，及源/V0/输入/manifest SHA、预算已耗/剩余，不可改`rah/w_eff/rb`、温启动、切网格、降容差、加root迭代、重跑或将失败class成PASS。早停也消费了本任务唯一science许可，剩余额度不可另造名复用。

最终集中交付`V010_SINGLE_POINT_CORRECTED_HA_PRICE_PROBE_RESULT`，含实际模型source路径与commit/blob，完整输入哈希、正确税语义、科学门与KFE摘要（如有）、各调用账、墙钟/RSS/文件bytes、旧试验不可比处和剩余科学UNKNOWN。Codex只报告，不自授通过；终态`WAIT_ASTRA_V010_SINGLE_POINT_PRICE_PROBE_REVIEW/STOP`。

**严格保护**：原V010实施冻结、代码candidate、旧科学额度（Codex报告4/6 pytest、1/4 driver、1/26 HA，1,626 selector cells、1,642 roots）和全部失败回执保持不变；新预算在另一账册，仅对本唯一HA计1/1。V011 NOT_STARTED，A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、真实C8 A–D REQUEST_ONLY。
