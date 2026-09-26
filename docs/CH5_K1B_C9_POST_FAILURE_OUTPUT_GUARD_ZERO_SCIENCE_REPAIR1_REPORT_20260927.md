# C9 output-guard Repair1：零科学测试与证据修正候选

状态：仅供 GPT Work 独立 ACCEPT/REJECT；不授权科学执行。签发任务 `CH5_K1B_C9_POST_FAILURE_OUTPUT_GUARD_ZERO_SCIENCE_REPAIR1_20260927` 只允许修改惰性测试，并新增本报告与收据。delegate `validators/multi_province/k1b_turn9_post_failure_new_attempt_outer_r2/run.py` 在本轮冻结。

## 修正目标与可证范围

独立审查对上一候选 `5e40792d7ed921a58b5991e413d49cd907ad38b3` 给出 `REJECT__ROOT_REPLACEMENT_WINDOW_TEST_GAP_AND_OVERBROAD_CLAIM__NO_SCIENCE`：旧测试在调用 `guard_output_mkdir` **之前**替换 owned output root，只验证了第一次 ownership 检查。Repair1 增加惰性临时目录回归，在该函数内部第一次 `owns_output_root` 成功之后、最终 ownership 检查之前替换根，要求守卫在原始 `Path.mkdir` 修改替换根之前阻断，并记录有界 `root_not_owned` 详情。

即使新回归通过，结论也仅限于**测试所覆盖的两个检查点**：调用前的更换可由首次检查发现，两次检查之间的更换可由最终检查发现。最终检查之后至原始 `Path.mkdir` 之间仍有 TOCTOU 窗口；现有代码未把被检查的目录身份与后续路径变更原子绑定。本轮不修复或宣称消除该残余风险。非 `mkdir` output-guard 失败详情亦在本任务范围之外；旧守卫的准入与诊断语义不在本轮扩展。

## 验证与候选身份

- 本轮唯一聚焦惰性测试：`python -m pytest -q tests/test_mp4c_k1b_turn9_post_failure_new_attempt_preflight.py::test_output_guard_mkdir_rechecks_root_before_original_mkdir`；退出码 `0`，`1 passed in 0.20s`。测试预算使用 `1/1`，没有第二次调用。
- 上一被拒候选的历史测试结果为 `7 passed, 1 skipped, 62 deselected`，**不是 Repair1 的测试结果**。其中真实目录 symlink 用例因本机环境无法创建而跳过；模拟 reparse 用例通过。不得把该 skip 说成真实 symlink 已验证。
- 签发 parent：`d52d96003090a1b0cd54d560dc206171e7f6e0de`；签发 `HEAD:src`：`00682b2e1a7ba23665f6e16f6acf48ad35874883`。candidate 与 tree 在提交内容冻结后才能确定，其精确值见最终交接；将其写入本报告会改变被哈希标识的 tree 与 candidate。
- 惰性测试原始 SHA-256：`F31F86D9975171441AF4CB7ADD5E6B072163DB27051D9EE5BD9F320087DBE161`；冻结 delegate 原始 SHA-256：`AA081078AC9B2997E3DFAA6BA5AF725F5C53013EA7F194780E5BE35A0C911BF2`。本报告和收据各自的最终原始 SHA-256、提交后的跟踪文件/暂存区状态见最终交接，避免自引用哈希。
- 本轮 preflight、`--execute`、wrapper、模型及科学调用均为 `0`。

## 受保护证据身份

以下为上一被拒候选收据中的参考哈希，Repair1 提交前后须由主代理只读复核；列出参考值本身不构成本轮复核结论。

| 受保护证据 | 原始 SHA-256 参考值 |
| --- | --- |
| C6 prime manifest | `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61` |
| C7 manifest | `413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91` |
| C8 manifest | `5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301` |
| C8 timing manifest | `5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D` |
| old C9 partial manifest | `80BD0D42CB73B4E39B811E759505480542D5A73227014F30B732C34A8AC1FDC3` |
| new C9 partial manifest | `3B10AB56BC2CE3D8FF9B4FB6442E012CB39686AF389624D17566CC8D68F57D20` |
| new C9 partial readback | `8191C24E8A472EE702C71A72DB4F4CCC9A0733D432226DFDB6EF0B4045792BAC` |

本轮只读复核了表中六份 manifest 与新 C9 readback，七项原始哈希全部匹配（`7/7`）。Git 状态中恰有六个既有受保护未跟踪 `reports/` 根，本轮未触碰或新增根。

## 不变的历史裁决与下一门

原先两次被禁止的 `--execute` 探测仍按**任务违规**保留，不计为本轮合规测试。既有 REJECT 均不因本轮修正而改判：

- `REJECT__TASK_BOUNDARY_VIOLATION_AND_STATIC_GAPS__NO_SCIENCE`
- `REJECT__SEALED_INPUT_PATH_GAP_AND_EVIDENCE_AMBIGUITY__NO_SCIENCE`
- `REJECT__FINAL_ENTRY_GUARDS_UNTESTED__NO_SCIENCE`
- `REJECT__ACTIVE_PREFLIGHT_AND_PREIMPORT_AUTHORITY_GAPS__NO_SCIENCE`
- `REJECT__PREIMPORT_AUTHORITY_PATH_AND_BEHAVIOR_EVIDENCE_GAPS__NO_SCIENCE`
- `REJECT__AUTHORITY_METADATA_FOLLOWS_UNSAFE_PATH__NO_SCIENCE`
- `REJECT__STALE_INERT_SOURCE_ORDER_ASSERTION__NO_SCIENCE`
- `REJECT__FULL_INERT_TEST_FAILED__NO_CANDIDATE__NO_SCIENCE`
- `REJECT__LEDGER_COMPLETENESS_AND_SEAL_READBACK_PATH_GAPS__NO_SCIENCE`
- `REJECT__NONAUTHORITY_PROPOSAL_MISSING_PROSPECTIVE_RUNNER_FIELD_BINDINGS__NO_SCIENCE`
- `REJECT__NONAUTHORITY_PROPOSAL_MISSING_PROSPECTIVE_SCHEMA_AND_ACTIVE_BINDINGS__NO_SCIENCE`
- `REJECT__IDENTITY_CHAIN_OWNER_ORDER_AND_TASK_ABSENCE_AMBIGUITY__NO_SCIENCE`
- `REJECT__IDENTITY_CHAIN_COMMITTED_FILE_GATE_OMITTED__NO_SCIENCE`
- `REJECT__COMPLETE_C9_NOT_DELIVERED__CALL_LEDGER_UNRESOLVED`
- `REJECT__COMPLETE_NEW_C9_EXECUTION__OUTPUT_GUARD_BLOCK_AND_CALL_LEDGER_UNRESOLVED`
- `REJECT__ROOT_REPLACEMENT_WINDOW_TEST_GAP_AND_OVERBROAD_CLAIM__NO_SCIENCE`

旧、新 C9 一次性尝试均已消耗；两份实际调用账本仍为 `CALL_LEDGER_UNRESOLVED`。C10、重试、部分续跑和 Results 均关闭，Results eligibility `FALSE`。Repair1 的下一门仅是 GPT Work 对本地候选独立 ACCEPT/REJECT；未来科学需新的明确 Owner 决定及独立审查的 R/C/O/T 链。
