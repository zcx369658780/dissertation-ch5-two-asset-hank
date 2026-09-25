# C8 同冻结输入独立计时预算与资源提案（零科学调用）

任务 CH5_K1B_C8_SEPARATE_TIMING_BUDGET_RESOURCE_PROPOSAL_ZERO_SCIENCE_20260925；签发 HEAD 22a6fe7d3b77cc248740dfc8c6fe416e5c27514c，冻结 HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883。**仅供 Owner 决策：所有额度为 PROPOSED_NOT_ADOPTED；不构成执行合同或科学调用授权。**

## 测量身份

Owner 选择路线 A：使用受保护 C7 输出中已封存、读回的 entering-C8 束，最多一次完整 C8 同冻结输入外层 turn 测量。输入 manifest、readback、JSON、NPZ 哈希见文末。候选执行身份绑定已独立 ACCEPT 的 wrapper validators/multi_province/k1b_turn8_same_frozen_timing_measurement/run.py（SHA-256 8DFA49C1121EF41FA750844F4F5017779C3E381CFA2E7CBE19C7834D1F0EAB4A）及 GPT Work 审查 docs/CH5_K1B_TURN8_SAME_FROZEN_TIMING_RUNNER_REPAIR1_INDEPENDENT_REVIEW_20260925.md（SHA-256 6217FC40E7EC992CB3302E43B8744B0C530F6696B48801BFC1AAD75D4EBB24C9），和已接受 C8 delegate validators/multi_province/k1b_turn8_outer_r2/run.py（SHA-256 10920535BD50E688D1794B7E69C34F8A5C3C56456CAF6E8DF52FA8D9DFE31831）。不改变或复用原 C8 输出和旧调用额度。

唯一独占候选输出根：reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001/。当前不存在；未来只有另行授权、独立审查的精确执行任务在重新核对身份及空置后才能创建。受保护 C6-prime、C7、C8 三根只读，本任务未创建测量根。

## 单次独立 attempted-call 预算候选

新测量采用独立 SEPARATE_C8_TIMING_ONLY 账本命名空间。下列 39 类总上限取已接受 C8 runner 的 CEILINGS，历史实际取封存 C8 账本；五类逐省 guard 取 runner 的 PER_PROVINCE。**仅五类有显式逐省 guard**；其余行的破折号表示本次总额，没有独立逐省 guard。零上限同样有效。本预算既不并入已耗尽 C6→C8 预算，也不挪用 C9/C10 已采纳额度。完整尝试总数最多 1，重试 0；逐次尝试先计数，失败照计；触顶、首个缺陷或不明账本即停，不拆分、多次尝试、续跑或补跑。

| C8 attempted-call 类别 | 独立测量候选总上限 | C8 封存实际 | 显式逐省 guard |
|---|---:|---:|---:|
| source_native_initializations | 31 | 31 | — |
| scalar_labor_roots_attempted | 24,800 | 24,800 | — |
| scalar_labor_roots_returned | 24,800 | 24,800 | — |
| corrected_policy_maps | 1,581 | 409 | 51 |
| d2_q_assemblies | 1,581 | 409 | — |
| selector_evaluations | 1,264,800 | 327,200 | 40,800 |
| scalar_selector_root_invocations | 620,000,000 | 141,125 | 20,000,000 |
| direct_hjb_updates | 1,550 | 378 | 50 |
| hjb_checkpoint_evaluations_after_update | 1,550 | 378 | — |
| relaxation_helper_invocations | 1,550 | 378 | — |
| alpha_candidates | 82,150 | 382 | — |
| terminal_kfe_attempts | 31 | 31 | 1 |
| scc_decompositions | 31 | 31 | — |
| restricted_dense_scipy_linalg_svd_gesvd | 31 | 31 | — |
| normalized_stationary_candidates | 31 | 31 | — |
| q_transpose_times_p | 31 | 31 | — |
| corrected_aggregate_evaluations | 31 | 31 | — |
| firm_evaluations | 31 | 31 | — |
| household_batch_constructions | 1 | 1 | — |
| full_integrations | 1 | 1 | — |
| source_faithful_labor_reconstructions | 1 | 1 | — |
| frozen_k1b_quantity_allocations | 1 | 1 | — |
| k1b_feedback_calls | 1 | 1 | — |
| c1_residual_govinv_constructions | 1 | 1 | — |
| composite_wage_batches | 1 | 1 | — |
| monetary_assignments | 1 | 1 | — |
| fiscal_diagnostic_batches | 1 | 1 | — |
| completed_raw_ra0_vectors | 1 | 1 | — |
| deterministic_next_k1b_preparations | 1 | 1 | — |
| raw_next_payoff_same_s_constructions | 1 | 1 | — |
| turn7_household_calls | 0 | 0 | — |
| turn8_household_calls | 1 | 1 | — |
| turn9_household_calls | 0 | 0 | — |
| full_space_800_dense_scipy_linalg_svd_gesvd | 0 | 0 | — |
| scientific_retries | 0 | 0 | — |
| solver_substitutions | 0 | 0 | — |
| k2_calls | 0 | 0 | — |
| ge_annual_shock_irf_welfare_results_calls | 0 | 0 | — |
| matlab_scientific_calls | 0 | 0 | — |

历史实际仅说明候选数值和资源暴露，不能推导未来调用量或耗时。未来合同必须逐项绑定上述类别、五个逐省 guard、输入、wrapper、delegate、唯一输出根及封存账本；改变任何身份或计数语义须先重新提案、独立审查。

## 资源墙和终止语义

Owner 仍须选定**具体有限的进程墙钟秒数**和协作式超限风险：到点后不得放行新的科学入口；在途操作可否越限到安全点、可承受的最大越限风险、无法安全停下或账本不明时如何保留原始终态，均待 Owner 明确。候选规则是在检查点和下一次调用前检查资源；到限即停止新操作，保留原始失败、已尝试账本及计时记录。不能核实已尝试调用时标 CALL_LEDGER_UNRESOLVED，首错即停、零重试。失败或中止只产生删失/失败耗时，不得伪作完整 turn 样本。有限资源墙是风险限额，**不是可信科学时长上界**；本任务没有可填写的时长上界秒数。

一次完整样本仅描述该冻结 C8 输入、环境和当次负载，不能自动建立 C9/C10 上界或解除 BLOCKED__DURATION_BOUND_UNAVAILABLE。跨输入外推、不确定性、安全余量及下一次 Asia/Shanghai 00:00 前能否预期完成，均须后续独立审查与 Owner 判断。当前 MEASURED_SCIENCE_RUNTIME_UNAVAILABLE；Results eligibility = FALSE。

## Owner 待决

| 项目 | 可审候选 | 仍需 Owner 决定 |
|---|---|---|
| 独立测量预算 | 上表 39 类本次总额、五类逐省 guard；完整尝试最多 1，重试 0 | 是否逐项采纳并固定于另行授权 |
| 进程资源墙 | 协作式停新入口、首错保留、不明账本停 | 具体有限秒数及在途越限风险语义 |
| 执行身份 | 固定 wrapper/delegate、C7 束、独占输出根 | 后续合同、独立实施审查及一次性科学授权 |
| 样本用途 | 仅 C8 同冻结输入一次观察 | 能否外推 C9/C10 上界及如何通过日界门；本提案不预设通过 |

## 来源和当前账本

- validators/multi_province/k1b_turn8_outer_r2/run.py — SHA-256 10920535BD50E688D1794B7E69C34F8A5C3C56456CAF6E8DF52FA8D9DFE31831
- validators/multi_province/k1b_turn8_same_frozen_timing_measurement/run.py — SHA-256 8DFA49C1121EF41FA750844F4F5017779C3E381CFA2E7CBE19C7834D1F0EAB4A
- docs/CH5_K1B_TURN8_SAME_FROZEN_TIMING_RUNNER_REPAIR1_INDEPENDENT_REVIEW_20260925.md — SHA-256 6217FC40E7EC992CB3302E43B8744B0C530F6696B48801BFC1AAD75D4EBB24C9
- reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8_scientific_ledger.json — SHA-256 33672A89CB854F35F74FFC8B0886B4A48361B2D6F171313595708721A707355D
- reports/ch5_k1b_turn8_outer_r2_20260925_run001/terminal_receipt.json — SHA-256 01BBF375DA61B387F697A581A9137C57FC87A3DC7CBC937838933A25F7297A7D
- reports/ch5_turn6_same_frozen_input_repeat_20260923_run001/execution_artifact_manifest.json — SHA-256 7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61
- reports/ch5_k1b_turn7_outer_r2_20260925_run001/execution_artifact_manifest.json — SHA-256 413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91
- reports/ch5_k1b_turn8_outer_r2_20260925_run001/execution_artifact_manifest.json — SHA-256 5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301
- reports/ch5_k1b_turn7_outer_r2_20260925_run001/turn8_entering_bundle_manifest.json — SHA-256 20861D4ADDBDF1099854EB86B00D24A097C627838B3F6EF5AFAEDABFFD647E5E
- reports/ch5_k1b_turn7_outer_r2_20260925_run001/turn8_entering_bundle_readback.json — SHA-256 5EB75667132473C2F283666B0F3B73BB18FDF00A83C09382827E4C44958246FA
- reports/ch5_k1b_turn7_outer_r2_20260925_run001/turn8_k1b_input_candidate.json — SHA-256 30EDAECEA59ABA03EFFD6C11530617BB7CF80FED175F58437F4DACA9E96D2F3A
- reports/ch5_k1b_turn7_outer_r2_20260925_run001/turn8_k1b_frozen_share_payoff_plan.npz — SHA-256 E6B5D428C1070C6F9F6D9C450F7CDB0D4C2C54F0658074C9C75E60E8FDB743DB

- docs/CH5_K1B_TURN8_SAME_FROZEN_TIMING_RUNNER_PREPARATION_20260925.md — SHA-256 A240CB2BEE54932CA8F40DF0381C720EF23C9B4DD11116E4AB26502FC3C93F1C
- docs/CH5_K1B_TURN8_SAME_FROZEN_TIMING_RUNNER_REPAIR1_20260925.md — SHA-256 8734046465CA86F02AF8C7A9B320F30901E87B5B2B01076FECFC53FC3C8DA320
- EVIDENCE/ch5_k1b_turn8_same_frozen_timing_runner_repair1_20260925/repair_receipt.json — SHA-256 2606C8C35D7630B17DDC4105C4C7759AF905610DD6CAFF530EE242F598D1E2C2

另据 TASK_CURRENT.md、CURRENT.md、SCIENTIFIC_DECISIONS.md、REVIEW_GATE.md、Owner 路线 A 选择文件及 wrapper 的准备/Repair1 报告核对权限。机器收据见 EVIDENCE/ch5_k1b_c8_separate_timing_budget_resource_proposal_20260925/proposal_receipt.json。本任务模型调用 0、科学调用 0、失败尝试 0、重试 0。下一门为 GPT Work 对两路径候选的独立审查，再由 Owner 决定独立预算、有限资源墙及以后另行的一次性执行授权；Builder 不自我 ACCEPT 或派发后续任务。
