# V0.0.10 版前DRAFT：V009私人资本零支持与首次Newton试探策略不可行的可证伪取证

日期：2026-10-15（Asia/Shanghai）
**状态：`V010_OWNER_CONTINUATION_DRAFT__WAIT_CODEX_V009_NEWTON_TRIAL_AND_ZERO_PRIVATE_CAPITAL_FORENSIC__ZERO_SCIENCE_CALLS`。**
**来源**：Owner持续顺序科研版本委托`docs/CH5_OWNER_CONTINUOUS_VERSION_DIRECTIVE_20261015.md`；V009初版内生两资产HANK失败且硬单省宏观预算2/2耗尽，新版仅SOURCE_ONLY+精确V009本地合成回执静态取证，**不自动授权任何 HJB/KFE/selector/真实科学模型求解、重新计算宏观root、科研代码变更或真实数据读取**。这仍是DRAFT，不是冻结实施计划。

## 1. 下一次研究必须回答一个可操作问题

不重开Owner早已采纳的GDP相对劳动偏好（人工2省目的×来源`phi=((1,1.1),(.9,1))`），不改其它经济参数、资产域、贴现、调整成本或KFE停止条件。集中证明：
1. 五次完成的人工家庭KFE中`A=0`是哪些政策、特定价格与最终`Q`闭类支持导致（是否所有非零质量均在`a=0`、流入/流出率/稳定性、是否存在可能的非零a吸引区），而不是仅报告一行均值；
2. 第六次不 admissible 的输入`x_trial`是第一次 full Newton 提议还是其它支路，`x_trial-x`由首点+四个雅可比点的保存残差是否可独立重建；检查trial价格/回报/财政工具是否越过数学可行域；在无新的模型调用下评估**原宏观line-search对trial的错误处理是数值策略改进空间还是经济学必然不可行**；
3. `h7_f179`对应(b=2上界,a索引8,z=.8)的8个策略候选为何全被拒（正液态影子、边界漂移、kink、active-set、derivative/价差输入/非零cost、顺序和报错标签），分开特定trial-price诊断与被接受初始price-point结论；
4. 以原冻结科学法则为准，提出一份**精准下一版科学路线建议**：可行域感知的Newton阻尼/线搜索是否只需要“遇特定不可行trial先缩步”，或真正需重新定义资本基金/债券/家庭约束、增大网格等重要科学选择；每一改动的反例、所需Owner裁决及新预算（但本轮零运行）。

## 2. 来源和证据

唯一当前失败候选 `e25f8e22490dddf57568e14aec2819d52603a78f` tree `4b161428470e4bc8070ed4ec4010a0ea08f9695a` parent `d41d229b681e09b913c21deff7a057085b9bc419`；[V009最终审议](../0.0.9/acceptance.md)、[复盘](../0.0.9/retrospective.md)、原V009冻结`cb76a840fdd9d1756728189bf29518679831aba6`、Owner CES补充`1c9839fe639197176d0d8b1c981b4c13025dcd5a`及一次剩余额度授权`76616b2bef739a2119c510475f786d4134a7f5e6`。原受保护C8的历史报告不是本版取证输入。

公开GitHub新源**只读**：`reconciled_hank/{contracts,household,stationary,stationary_kfe,accounts}.py`及四focused测试，正对宏观eval序列/Jacobian/Newton trial handling/单调HJB/KFE产生a=0质量的相关行；可以对照原`corrected_diagnostic/{selector,cost,boundary,generator}.py`和精确已接收HJB/KFE定律，不许执行这些模型/旧runner。

Codex在本地可从它自己准确的、**新的V009合成数据**来源回执核实后有限只读，优先精确已知的
`D:/ProjectTemp/ch5_v009_hank_20261015_01/receipts/FINAL_DELIVERY_PHI_B.json`（Owner已提供其SHA256 `E75E4C1B4434AB8D3850114B0F6329C46B54C08DA21E8D9E90EF9860C6FF3D79`，Codex须自己验证）和此回执明确指向、物理根确认为**同一新合成V009`V009_LEDGER_DIR`**的目标。
可按需要只读有限的本版`science_counts.json`+上一次高计数副本、macro评价回执、household完成回执（最多五份）、编号h7的失败记录/8个拒绝候选与单份`household_007/failure_state.npz`、最多五份**本次人工**terminal `terminal.npz`/`Q.npz`。如果真实文件名/根未明确证实，先从owner指定的最终回执查真实路径，绝不根据历史C8路径猜或遍历全盘。所有来源必须经过安全根/非reparse/明确合成人工来源校验，不信任从失败JSON中出现的任意绝对路径。
- 有界文件数≤36（含8个精确既有Git源码/合同、最多24件本版**新合成**本地回执/数组及其它精确来源）；Git正文累计≤2MiB，本地合成回执/数组累计读字节≤32MiB，单个合成`.npz`最大≤8MiB；无界递归扫描、原D盘8个dirty全文、C8真正受保护JSON/NPZ/CSV/MAT及C盘B3都**禁止stat/read/hash/parse/extract**。
- 对人工数组只允许安全的**离线读取与代数取证**（例如质量支持统计、已保存jac的线性代数验证、严格`allow_pickle=False`的既有V009 synthetic npz字段），不调用`solve_household/map_policy/selector/stationary_mass/solve()/scipy.optimize`、不重新组Q、不在新模型价格上调用任何政策或KFE。否则进入未经授权科学调用的STOP。
- 最长3小时，源码文件和合成receipt读取/分析费用仅静态取证；0新pytest、0python模型import执行/科学root、0HJB/KFE/selector/scalar root/GESVD、0新trial或求稳态、0Git提交/push/branch重写/原模型dirty或LOCAL_ONLY资产写。普通离线数据解析若需要Python应在隔离只读进程且不import任何研究`reconciled_hank`/旧生产模块，任何输出仅内存/Owner文本报告，不创建伪运行receipt。

## 3. 重要分析限制

- 5个完成价格点`A=0`与正KFE质量推得平稳质量支持`a=0`，**仅限五个price points**；不能据此宣称E1–E3人工经济体根本无完整资本均衡。
- n=1时`phi11=1`，与方案A相同；两省`phi=.9/1.1`尚未运行。不得用单省失败推翻Owner的GDP偏好方案B。
- 首个driver `os.replace`账本PermissionError不是经济失败；本版静态取证不得自行修改持久账本/原先递增count或为数字整洁重新运行。
- `NO_ADMISSIBLE_POLICY`是某个`full-step Newton candidate`的点上家庭拒绝，**不等于已接受根候选的无可行性**；若报告要推荐新line search必须明确其**不同于V009冻结“出错立即STOP”语义**，所以要有新的数学不变量、专用attempted预算及Owner科学取舍，不能借“工程修复”偷跑新实验。
- 禁止为分析方便假设最终5组私有全记录已在GitHub：`versions/0.0.9/acceptance_summary.json`是PRE_SEAL，网页没有本地原始科学回执。若本轮Codex读到当地原始数组，请精确陈述实际字段/来源和摘要哈希并选择性脱敏文本回报。

## 4. 唯一交付与停止

一次性向Owner与Astra交付 **`V0.0.10_M2_V009_PRIVATE_CAPITAL_ZERO_SUPPORT_AND_NEWTON_TRIAL_FAIL_CLOSED_FORENSIC`**：
- 固定Git commit/源码路径/版本保护，按证据级别区分本人直接读的LOCAL_ONLY、GitHub可公开复验的源码、重新推导的经济恒等与尚未证部分；
- 五个宏观完成点评估保存的`x`、控制/支持与A=0证据（不发布私人科学真实输入）、首个Jacobian和其解向量、首个Newton unaccepted full trial的详细方程和residual/domain，必须与具体model日志逐一一致；若没有原完整字段说`NOT_AVAILABLE`不脑补；
- flat179的状态坐标、反证或受支持的实际8候选拒绝原因、哪些上/下约束被触发；
- 对“资本零支持”和“宏观不接受不可行trial”两条独立假说进行错误归因分级，给出一个优先、可证伪、严谨的新科学算法修订提案，说明首个受限科学实验需要的最小参数与独立oracle、最多2个新重点Owner选择（若无需新经济方程则可报告无额外选择）、新科学预算建议，但**不申请在本版DRAFT中立刻运行**；
- 操作/合成回执字节账、失败及0所有新科学调用、0旧真实/保护读取、V009原预算消耗不重置。

终态：`WAIT_ASTRA_V010_V009_FAILURE_FORENSIC_SCIENTIFIC_REVIEW__NO_IMPLEMENTATION_OR_SCIENCE_AUTHORIZED / STOP`。
原C8 A–D REQUEST_ONLY、A16 UNRESOLVED/FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE。V0.0.11 NOT_STARTED。继续V1.2工作流/Owner连续版前立版授权，无自动后台代理。
