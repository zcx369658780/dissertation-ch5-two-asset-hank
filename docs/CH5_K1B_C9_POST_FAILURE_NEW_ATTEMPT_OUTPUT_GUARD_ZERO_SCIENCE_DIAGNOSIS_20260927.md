# 新 C9 输出守卫失败：零科学诊断

状态：非权威诊断候选；不修改守卫，也不授权新尝试。起点 commit b278da2b6324d3ddae2364fb87826a71cdc9462b，parent ad54c132fef03ab3fd195f36318df3443985c7df，HEAD:src 00682b2e1a7ba23665f6e16f6acf48ad35874883。

## 结论与证据边界

已提交源代码在省份 0 构造 output/turn9/household/p00_<province>，调用 province_root.mkdir(parents=True, exist_ok=False)（冻结源 651–652 行）。委托层 guarded_mkdir 先执行 guard_output_mutation，再调用原始 mkdir（委托 296–301 行）；省份入口仅检查 output/turn9 路径，未创建它（1017–1024 行）。path_components_safe 允许缺失的最终目标，但遇到缺失的中间父目录时返回 False（209–220 行）。因此在 turn9 或 household 尚未创建时，针对省份叶目录的预检查足以触发 BLOCKED__OUTPUT_COMPONENT_REPARSE_POINT（266–276 行），使 parents=True 的父目录创建逻辑根本无机会运行。

这只是由静态控制流和现存部分证据支持的充分解释，不证明故障瞬间确有真实 symlink 或 Windows reparse point。相同错误码还覆盖缺失中间父目录、lstat 的其他 OSError 和 Windows 属性不可得。守卫异常构造了路径字符串，但 preserved top-level first_failure/timing_failure/terminal_receipt 仅记录原始终态，没有保存被拒 mkdir 路径、首个失败组件、lstat 异常或 stat/reparse 属性。不能从错误码反推真实 reparse。

## 调用账本分层

执行终态 CALL_LEDGER_UNRESOLVED；原始守卫终态 BLOCKED__OUTPUT_COMPONENT_REPARSE_POINT。确认的 turn9_household_calls 尝试为 1；39 类确认图除这一项外均为 0，province 0 的持久化类别细项为 0。另有 17 类 reserved exposure，包括 direct_hjb_updates=50、scalar_selector_root_invocations=20000000 和 terminal_kfe_attempts=1，这些只是风险预留，不能加到已确认调用或当作实际调用。省份 0 处于 inflight，详细实际调用仍 UNKNOWN；旧 C9_TIMED_RISK_RUN001 的实际账本同样 CALL_LEDGER_UNRESOLVED，旧完整 turn 扣账只属治理记账。partial readback PASS 只覆盖 11 项部分文件；complete_outer_turn=false、safe_pause=false，未完成省份或 integration，retry_allowed=false。C10、重试、部分续跑和 Results 均关闭，Results eligibility FALSE。

## 来源及原始 SHA-256

| 身份 | 路径 | SHA-256 |
| --- | --- | --- |
| task | TASK_CURRENT.md | 02F78C98DF420F504AF1DD95B6BA08980E12C05A9FDDDF4E73BAADB129CB9BEB |
| frozen_source | src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py | E2D5EDBBF73ABF60DBA183FB04A5D364D3D83FFCD262254F58EAD53EC2F36D07 |
| delegate | validators/multi_province/k1b_turn9_post_failure_new_attempt_outer_r2/run.py | AD592FCEEB6563D56BFEA6A9F35029B83712A6ACCED80A1BAF8F53C144F99D56 |
| inert_test | tests/test_mp4c_k1b_turn9_post_failure_new_attempt_preflight.py | F22BCE672DE5D1E62C3BBC7353D822059290F5AEE074147BD6B5F352DB72F3F1 |
| execution_review | docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_EXECUTION_INDEPENDENT_REVIEW_20260927.md | 323123872BDE5EE35489620C247813D43232B242DC6F520B2760A1F291303183 |
| old_execution_review | docs/CH5_K1B_C9_ONE_SHOT_EXECUTION_INDEPENDENT_REVIEW_20260926.md | F161A12203ABE6A392A510309F647A38C8AB46BFA1F3A72F1ED93AE6BDAD68A7 |
| new_first_failure | reports/ch5_k1b_turn9_post_failure_new_attempt_001/first_failure.json | 49AA81E126BE4BDF55289A416EACAA8CEC0B80EEB18D2F40A80009BEFC68DD11 |
| new_timing_failure | reports/ch5_k1b_turn9_post_failure_new_attempt_001/timing_failure.json | B74E538FEF4C0216794DB1FDF3C94FFA2FDD8C75081DA38413B495949321FBB9 |
| new_terminal_receipt | reports/ch5_k1b_turn9_post_failure_new_attempt_001/terminal_receipt.json | 0AAF0BF700B381D97A397ED8090A99CAD648089D654CD76D02D7F5FDEE5E7D82 |
| new_partial_manifest | reports/ch5_k1b_turn9_post_failure_new_attempt_001/partial_artifact_manifest.json | 3B10AB56BC2CE3D8FF9B4FB6442E012CB39686AF389624D17566CC8D68F57D20 |
| new_partial_readback | reports/ch5_k1b_turn9_post_failure_new_attempt_001/partial_artifact_readback.json | 8191C24E8A472EE702C71A72DB4F4CCC9A0733D432226DFDB6EF0B4045792BAC |

六个受保护输出根及新根 readback 的哈希：

| 清单 | 路径 | SHA-256 |
| --- | --- | --- |
| C6_prime | reports/ch5_turn6_same_frozen_input_repeat_20260923_run001/execution_artifact_manifest.json | 7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61 |
| C7 | reports/ch5_k1b_turn7_outer_r2_20260925_run001/execution_artifact_manifest.json | 413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91 |
| C8 | reports/ch5_k1b_turn8_outer_r2_20260925_run001/execution_artifact_manifest.json | 5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301 |
| C8_timing | reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001/science_artifact_manifest.json | 5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D |
| old_C9_partial | reports/ch5_k1b_turn9_timed_risk_exception_run001/partial_artifact_manifest.json | 80BD0D42CB73B4E39B811E759505480542D5A73227014F30B732C34A8AC1FDC3 |
| new_C9_partial | reports/ch5_k1b_turn9_post_failure_new_attempt_001/partial_artifact_manifest.json | 3B10AB56BC2CE3D8FF9B4FB6442E012CB39686AF389624D17566CC8D68F57D20 |
| new_C9_readback | reports/ch5_k1b_turn9_post_failure_new_attempt_001/partial_artifact_readback.json | 8191C24E8A472EE702C71A72DB4F4CCC9A0733D432226DFDB6EF0B4045792BAC |

## 未来仅可在新任务下做的惰性回归案例

现有 inert test 覆盖真正的 reparse 和部分缺失权威/清单门，但未覆盖 owned output 内 parents=True 且中间父目录缺失的 mkdir 控制流。本轮不运行测试或修复。未来测试应在完全临时、无模型的 owned root 中逐项验证：

- missing intermediate ancestors under an unchanged owned root, parents=True：allow only a safe missing suffix, then preserve root ownership and component checks at each creation; no false reparse classification。
- true symlink or Windows reparse in an existing parent or leaf：block before following or mutating the unsafe component。
- lstat OSError other than missing：fail closed and preserve distinct diagnostic detail。
- owned output root replaced between checks：fail closed on identity mismatch and perform no out-of-root mutation。
- parents=False with missing parent：do not synthesize parents; preserve ordinary missing-parent failure without a false reparse claim。

历史裁决与边界：原两次被禁止的 --execute 探测仍是违规，不改判为合规测试。以下 REJECT 均保留其原候选范围：

- REJECT__TASK_BOUNDARY_VIOLATION_AND_STATIC_GAPS__NO_SCIENCE
- REJECT__SEALED_INPUT_PATH_GAP_AND_EVIDENCE_AMBIGUITY__NO_SCIENCE
- REJECT__FINAL_ENTRY_GUARDS_UNTESTED__NO_SCIENCE
- REJECT__ACTIVE_PREFLIGHT_AND_PREIMPORT_AUTHORITY_GAPS__NO_SCIENCE
- REJECT__PREIMPORT_AUTHORITY_PATH_AND_BEHAVIOR_EVIDENCE_GAPS__NO_SCIENCE
- REJECT__AUTHORITY_METADATA_FOLLOWS_UNSAFE_PATH__NO_SCIENCE
- REJECT__STALE_INERT_SOURCE_ORDER_ASSERTION__NO_SCIENCE
- REJECT__FULL_INERT_TEST_FAILED__NO_CANDIDATE__NO_SCIENCE
- REJECT__LEDGER_COMPLETENESS_AND_SEAL_READBACK_PATH_GAPS__NO_SCIENCE
- REJECT__NONAUTHORITY_PROPOSAL_MISSING_PROSPECTIVE_RUNNER_FIELD_BINDINGS__NO_SCIENCE
- REJECT__NONAUTHORITY_PROPOSAL_MISSING_PROSPECTIVE_SCHEMA_AND_ACTIVE_BINDINGS__NO_SCIENCE
- REJECT__IDENTITY_CHAIN_OWNER_ORDER_AND_TASK_ABSENCE_AMBIGUITY__NO_SCIENCE
- REJECT__IDENTITY_CHAIN_COMMITTED_FILE_GATE_OMITTED__NO_SCIENCE
- REJECT__COMPLETE_C9_NOT_DELIVERED__CALL_LEDGER_UNRESOLVED
- REJECT__COMPLETE_NEW_C9_EXECUTION__OUTPUT_GUARD_BLOCK_AND_CALL_LEDGER_UNRESOLVED

本轮测试、preflight、--execute、模型及科学调用均为 0；没有触碰受保护输出或权威链。新 C9 一次性尝试已消耗。下一门仅为 GPT Work 对本诊断候选独立 ACCEPT/REJECT；任何修复或再尝试须另行签发。
