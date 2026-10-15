# V0.0.10 实施交付：Astra独立限域验收（2026-10-15）

**裁决**：`ACCEPT_LIMITED_GITHUB_ENGINEERING_SOURCE__REPORTED_FINAL_24_TESTS__FIRST_HA_FAIL_CLOSED__SCIENCE_NOT_ACCEPTED`。
**项目终态**：`V010_IMPLEMENTATION_CANDIDATE_REVIEWED__AWAIT_FAILCELL_LOCAL_EVIDENCE__NO_NEW_SCIENCE_PERMISSION`。
本记录是独立验收，不是修订冻结计划，不是补发科研预算、后继模型实施、选举V011或真实Results资格。

## 1. GitHub事实，独立验证
- 候选 commit `94de4501dec051b969bee9d852eba2d4591f30ef`，tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`，唯一parent `a1db8c114dec0ab69d69a5576e153a7f868cba0e`，与固定代码父吻合；比对确认为`1 ahead / 0 behind`。
- 15/15更改路径都在冻结`versions/0.0.10/plan.md`白名单：原7代码修改、新2个runtime、新4聚焦tests、1人工fixture、1validator。Astra通过GitHub连接器读取了候选15个文件源码正文。旧corrected_diagnostic、原MATLAB、历史旧模型等不在本提交diff。
- `tests/fixtures/v010_mainline_synthetic_v1.json` Git blob `40915658d93403cfc21b33a6b864b332b7857749`，与冻结fixture原blob一致。候选未合并main，本验收不做Git merge。
- 冻结计划commit `bf091da33d59293f147d52c11580327d3ac2a85d` / tree `668fa20883a295ee9bd831a0c542d39e366bec43` / plan blob `85138d8859d53295262fe13bf5bc277bca95ed3f` 未追改；签发任务commit `cf829b695b80ece7e31328141feaec40165b0e9c`。

## 2. 源码有根据的工程实现
- `mainline_household_runtime.py` 使用已有corrected policy-selector、raw derivatives、consumed drift Q、deterministic halving、B/D联合门、唯一闭类source-free KFE、五字段aggregate；它是新入口，但该HA并未在本次科学绑定通过，也没有进行terminal KFE。
- opt-in `run_mainline_one_turn`（原legacy route仍留存）使用目的地税及一次净工资桥，`Lt_HA`与`Lt_prev`分账，私人K1完整本地留存/外省资产同S、上轮raw-payoff；不调用C1残差律。
- `firm.py`仅在显式mainline选项下按省级N桥接AtTax/Tt并计工资税；GovInv原0.9/1.1 `_adapt`保持外层角色。人工测试确有原税、φ、资本、财政、时序和GovInv端点oracle，但不等于31省科学有效。
- 新`mainline_response.py`是3期条件递推入口，仅在`TARGET_CALIBRATION_VERIFIED`后可进入；工程stub存在，并无实际冲击运行证明。

## 3. Codex报告的本地执行与科学FAIL
**以下不属于Astra独立重跑**。据Codex：最终候选树focused pytest 24项PASS，过程4/6子进程（中间有2失败/一次导入失败）；首science driver 1/4、HA尝试1/26，V0 FOC max 2.19e-12、b斜率正；checkpoint0 B=2.3410249912350563，checkpoint1 B=0.2328433126744121、D=3.290243356756511；checkpoint2 F-order flat25返回NO_ADMISSIBLE_POLICY，直接solve2次、无终端KFE、无宏观校准、无冻结验证/3期响应。selector cells=1626，roots=1642（含V0 800）；总耗时19.1min。前两次checkpoint均未达到HJB B/D门，不能由B下降推出稳态存在或最终树科学通过。
- 仅以本轮冻结20×20×2 F-order b-fast格点推算，flat25对应`(ib=5,ia=1,iz=0)`、`b=-3/19≈-0.157895`、`a=10/19≈0.526316`、`z=0.8`，b与a均是内部节点。这不是拒绝原因的证明。
- `NO_ADMISSIBLE_POLICY`意味着该时点按已接受selector当前候选约束没有任何候选被判为可接受策略，**不**表示原MATLAB有界31省GE没有固定点。缺少该次本地`first_failed_cell.json`，不能判断是导数/边界/切换约束、数值浮点、V0或数学错误。
- Codex报告科学源码identity绑定在**封存前实现**，最终候选未再次运行science，只运行最终tree工程测试；因此不能以本次science失败/成功声称最终候选树的科学输出已复验。
- Codex提交的本地`DELIVERY_RECEIPT.json` SHA256 `322D707CF666D5CEDF1E4B907F7FE75A5423734867BA717D28CCB6DD73A792C9`；本轮Astra不能访问D盘，不独立证明这个SHA、19.1分钟、84.4MiB RSS、约399MB clone、dirty字节或原始测试process收据。GitHub没有可见CI测试状态可替代该回执。

## 4. 需在再次进行科学调用前解决（不追改冻结）
1. **唯一缺的实质诊断证据**：从此轮现有synthetic科学输出安全提取`first_failed_cell.json`的cell数值、全部候选rejection reason分类/计数、root/active-set与切换分支概要，以及`attempt_summary.json`、`V0_before_HJB.json`和所需checkpoint的来源哈希；可提供脱敏文件或集中只读报告。不得重算、不得新root/selector/HJB/KFE/pytest，不读C8/旧V009/B3。若涉及完整受保护路径，只提供允许的哈希和相对路径。
2. **价格边界来源**：`mainline_initial_states`中`ramin=0.02`,`ramax=0.09`,`wjtmin=0.8`,`wjtmax=1.3`可在固定原MATLAB历史审计找到，但冻结synthetic fixture没有逐项列出；以原审计来源及既有固定值做证据归属，不将其误称为fixture显式字段；若未来需要不同值必须按前瞻性新合同审批，不能临场改数救PASS。
3. **科学总账与最终树**：若未来获准延续，明确保存跨进程已耗4/6 pytest、1/4 science、1/26 HA，以及1,626 selector cells/1,642 roots；不能因为新output目录初始化ledger而把全局账本清零。必须核对封存前science源哈希与最终候选所使用模块sha，不得把不同树的science结果串在一起。
4. 完整双省外层及校准、真实31省、20期IRF等均不能因engineer代码完整而认证。仅在原因清楚、续跑是否遵守原冻结科学合同及剩余额度确定后，才单独讨论是否允许继续**同V010**受界科学验证；任何数学新法则要停下提交Owner。

## 5. 当前指令
- 限定接受此GitHub工程候选作为`V010_CODE_CANDIDATE_FOR_CORRECTIVE_REVIEW`；不推main、不认定数值science/GE/IRF/Results通过，不关闭V010。
- 目前Codex原任务已STOP；下一步只需交现有失败原证的脱敏摘录供Astra查因，**不新增自动ACTIVE科学执行任务**。任何后继科学尝试均需独立许可，且不得重开旧C8/C9额度。
- 守A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE，真实C8 A–D REQUEST_ONLY，V011 NOT_STARTED；历史D盘8 dirty、index/common-dir/untracked/ignored不触。
