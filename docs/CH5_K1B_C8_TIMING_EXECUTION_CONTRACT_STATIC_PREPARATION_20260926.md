# C8 同冻结输入测时合同静态准备（零科学调用）

当前任务 CH5_K1B_C8_TIMING_EXECUTION_CONTRACT_STATIC_PREPARATION_20260926，签发 HEAD a71bb9ef146ea325b221e7790ea03bef98d05753，冻结 HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883。本文件和 tasks/CH5_K1B_TURN8_SAME_FROZEN_TIMING_MEASUREMENT_CONTRACT.json 是**已提交但非活动**的候选，不授予 --execute 或模型调用。

Owner 已采纳独立 SEPARATE_C8_TIMING_ONLY 预算：39 类最大 attempted-call 额度、五类显式逐省 guard、完整尝试最多一次且零重试；失败尝试消耗额度。Owner 同时采纳单调钟从 timed action 开始的协作式进程墙 43,200 秒。到达或超过墙时，runner 拒绝**下一次科学入口**；已经在途的操作可能越过 43,200 秒直到安全点。该墙是资源风险限额，不是科学时长上界，也不是强制杀进程时刻；人工停止、首错和不确定账本仍须保留原始终态，不能免费续跑或重试。

## 合同字段对照

| 合同字段 | 静态依据 | 候选值 |
|---|---|---|
| schema | accepted wrapper future_gate schema literal | CH5_K1B_SEPARATE_SINGLE_C8_TIMING_CONTRACT_V1 |
| execution_id | 本次候选身份；future_gate 要求与未来活动任务的授权 ID 一致 | CH5_C8_TIMING_MEASUREMENT_RUN001_20260926 |
| output_root | accepted wrapper OUTPUT；C7/C8 受保护根外独占新根 | reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001 |
| attempts | Owner adoption 与 wrapper future_gate | 1 |
| budget_namespace | Owner adoption、Repair1 proposal 和 wrapper future_gate/attempt journal | SEPARATE_C8_TIMING_ONLY |
| resource_policy | wrapper future_gate；Owner 协作式进程墙 | COOPERATIVE_PROCESS_WALL_CAP |
| resource_wall_seconds | Owner adoption，单调钟 12 小时 | 43200 |
| wrapper_sha256 | 已独立接受的 wrapper 文件 | 8DFA49C1121EF41FA750844F4F5017779C3E381CFA2E7CBE19C7834D1F0EAB4A |
| independent_review_sha256 | wrapper GPT Work ACCEPT 审查文件 | 6217FC40E7EC992CB3302E43B8744B0C530F6696B48801BFC1AAD75D4EBB24C9 |
| per_category_attempt_ceiling | 已接受 Repair1 proposal receipt 39 类原样复制 | 39 类 |
| per_province_attempt_ceiling | 已接受 Repair1 proposal receipt 5 类原样复制 | 5 类 |

后两项逐键、逐值从已独立接受的 Repair1 proposal receipt 复制，未取用 C9/C10 额度。execution_id 是**候选执行身份**，需未来 Owner 明确采纳；它不同于预算命名空间。C7 entering-C8 manifest/readback 与三份受保护 output manifest 身份见来源清单，测量输出根当前不存在且本任务不创建。

## 活动门与缺失授权

当前 TASK_CURRENT.md 状态是 ISSUED__ZERO_SCIENCE_STATIC_CONTRACT__WORK_REVIEW_PENDING，不可能满足 accepted wrapper 的未来任务状态 ACTIVE__ONE_SHOT_SEPARATE_C8_TIMING_MEASUREMENT。future_gate 还要求未来精确活动任务及其相同已提交副本、Owner 单次执行采纳文档、已提交合同与 wrapper 审查哈希相互绑定。未来 Owner 执行采纳文档 docs/CH5_K1B_TURN8_SAME_FROZEN_TIMING_MEASUREMENT_OWNER_ADOPTION.md 和活动任务副本 tasks/CH5_K1B_TURN8_SAME_FROZEN_TIMING_MEASUREMENT_EXECUTION.md 均不存在；本任务不创建。该合同只有经过 GPT Work 独立 ACCEPT、Owner 再明确一次性科学执行授权并签发活动任务后，才可能成为未来执行门的候选输入。当前不运行 wrapper/测量/C9/C10。

C9/C10 预启动仍为 BLOCKED__DURATION_BOUND_UNAVAILABLE；一次 C8 观察不自动建立其时长上界。Results eligibility = FALSE。

## 静态来源

- docs/CH5_K1B_C8_SEPARATE_TIMING_BUDGET_RESOURCE_OWNER_ADOPTION_20260926.md — SHA-256 F842D4C7D59D91AA77BF0C22421B100054C8DFF58C001CFAA39E3F8C817AA106
- docs/CH5_K1B_C8_SEPARATE_TIMING_BUDGET_RESOURCE_PROPOSAL_20260925.md — SHA-256 C15F6C263311F5AF34F1072E5704C3C9752DB9419655837A06AF713BDC70A938
- docs/CH5_K1B_C8_SEPARATE_TIMING_BUDGET_PROPOSAL_REPAIR1_INDEPENDENT_REVIEW_20260925.md — SHA-256 44034AE2BD8C0174BA9381EED469977F68FF4D33877EB4A7EB63B6602C4E8BEE
- EVIDENCE/ch5_k1b_c8_separate_timing_budget_resource_proposal_20260925/proposal_receipt.json — SHA-256 04BBE1BC83EF3A437FB95FA1B631BAC832CAA57E63ECBCEF2D6CCF88E0FE4513
- validators/multi_province/k1b_turn8_same_frozen_timing_measurement/run.py — SHA-256 8DFA49C1121EF41FA750844F4F5017779C3E381CFA2E7CBE19C7834D1F0EAB4A
- docs/CH5_K1B_TURN8_SAME_FROZEN_TIMING_RUNNER_REPAIR1_INDEPENDENT_REVIEW_20260925.md — SHA-256 6217FC40E7EC992CB3302E43B8744B0C530F6696B48801BFC1AAD75D4EBB24C9
- validators/multi_province/k1b_turn8_outer_r2/run.py — SHA-256 10920535BD50E688D1794B7E69C34F8A5C3C56456CAF6E8DF52FA8D9DFE31831
- reports/ch5_k1b_turn7_outer_r2_20260925_run001/turn8_entering_bundle_manifest.json — SHA-256 20861D4ADDBDF1099854EB86B00D24A097C627838B3F6EF5AFAEDABFFD647E5E
- reports/ch5_k1b_turn7_outer_r2_20260925_run001/turn8_entering_bundle_readback.json — SHA-256 5EB75667132473C2F283666B0F3B73BB18FDF00A83C09382827E4C44958246FA
- reports/ch5_turn6_same_frozen_input_repeat_20260923_run001/execution_artifact_manifest.json — SHA-256 7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61
- reports/ch5_k1b_turn7_outer_r2_20260925_run001/execution_artifact_manifest.json — SHA-256 413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91
- reports/ch5_k1b_turn8_outer_r2_20260925_run001/execution_artifact_manifest.json — SHA-256 5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301

另核对 TASK_CURRENT.md、CURRENT.md、SCIENTIFIC_DECISIONS.md 和 REVIEW_GATE.md。本任务模型调用 0、科学调用 0、失败尝试 0、重试 0；仅进行 JSON、映射、哈希、路径和 Git 差异静态检查。首个未决门是 GPT Work 对本三路径候选独立 ACCEPT/REJECT；此后仍须 Owner 另行一次性执行授权。
