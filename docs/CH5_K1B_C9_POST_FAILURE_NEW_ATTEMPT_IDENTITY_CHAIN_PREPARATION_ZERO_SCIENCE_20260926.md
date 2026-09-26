# C9 新尝试身份链依赖矩阵（零科学、非权威）

**状态：待 GPT Work 独立 ACCEPT/REJECT；不创建 R/C/O/T，也不授权运行。**

起点 HEAD `b189834e6451775bbe6754911babf5275c20886b`，父提交 `26910bc9aef91a8c77a604c144422f5a26a3052e`，`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。本轮仅创建矩阵 JSON、本报告和机器收据三条非权威路径。矩阵原始 SHA-256 `FE602C2E89CA2484A928E790A3491FA3550F5440B2CFADD94EE40BB4D5DF8FBB`；schema `CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_IDENTITY_CHAIN_NON_AUTHORITY_V1`、`active=false`、`execution_authorized=false`。

Owner 选择 A 仅采纳 27 字段的已接受映射作后续零科学准备基础。提案 `tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_ACTIVE_CONTRACT_PROPOSAL_20260926.json` 原始 SHA-256 `78AAF07333DCF1BA5A5717BF8DB252A616FEABDF2B7C04A8EC32D653241EA52E`，独立限域裁决 `ACCEPT__NONAUTHORITY_PROPOSAL_FIELD_MAPPING_ONLY__NO_SCIENCE`。最终 wrapper/delegate 原始 SHA-256 分别为 `B1B2F54649B175F4E56C73135DECEED85C1AC966FE49A76431CF4B12B06633FD`、`AD592FCEEB6563D56BFEA6A9F35029B83712A6ACCED80A1BAF8F53C144F99D56`；预算来源与 Owner 采纳文件原始 SHA-256 分别为 `66C2C028B07E2CB41FFBB05B643C6EF644291A0FC94C8DAF2FE888518D240460`、`C1D88891C08D7526996F72DE6F77AA6D0FA2C593BAD91017877C8B8A0A51573D`。

依赖关系来自 timed runner 的静态身份门；下面列的是未来所需字面 token，并非本轮生成的权威文件：

| 节点 | 未来 runner 路径 | 依赖与必需身份 | 当前状态 |
|---|---|---|---|
| R 独立 runner 审查 | `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_RUNNER_INDEPENDENT_REVIEW.md` | `Reviewer: GPT Work`、`Verdict: ACCEPT__C9_POST_FAILURE_NEW_ATTEMPT_RUNNER`、wrapper/delegate 哈希行；独立审查后其提交 SHA 才能绑定 C。 | `PENDING/ABSENT` |
| C live 合同 | `tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_CONTRACT.json` | 精确 runner schema、`active=true`、已接受 27 字段已知值、`independent_review_sha256=R`；其提交 SHA 后续绑定 O/T。精确 live 字节仍须另行审查与 Owner 采纳。 | `PENDING/ABSENT` |
| O Owner 执行采纳 | `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_EXECUTION_OWNER_ADOPTION.md` | `OWNER_ADOPTED__SINGLE_NEW_C9_POST_FAILURE`、新执行 ID/输出根、C 与 R 提交 SHA；须有独立的 Owner 一次性科学决定。 | `PENDING/ABSENT` |
| T 当前任务/逐字节副本 | `TASK_CURRENT.md` 与 `tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_EXECUTION.md` | 两文件逐字节一致，含任务 ID/status、新执行 ID/根、O/C/R 提交 SHA 和 wrapper/delegate 哈希；当前任务不是未来执行任务。 | `PENDING/ABSENT` |

R/C/O/T 任一未知哈希均为 `PENDING/ABSENT`，不得按此矩阵推造或自我求解。即使技术身份链未来组装完成，仍需 Owner 后续明确的一次性 C9 科学决定及最终独立 dispatch 审查才能派发；本轮不建立这些权限。

五份受保护未跟踪输出根的清单原始 SHA-256（C6-prime、C7、C8、C8-timing、C9-partial）为：`7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`、`413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`、`5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`、`5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`、`80BD0D42CB73B4E39B811E759505480542D5A73227014F30B732C34A8AC1FDC3`。新 C9 根和 R/C/O/T live 路径全部缺席。已封存 C8 输入的 `manifest/readback/json/npz` 四个哈希已在矩阵中逐项绑定。

旧尝试已消耗，实际账本 `CALL_LEDGER_UNRESOLVED`，完整旧 turn 扣账仅是治理账，不是实际调用；新 C9/C10、重试、部分续跑、模型/科学调用和 `--execute` 探测均为零，Results eligibility `FALSE`。所有历史独立 REJECT 保留：`REJECT__TASK_BOUNDARY_VIOLATION_AND_STATIC_GAPS__NO_SCIENCE`；`REJECT__SEALED_INPUT_PATH_GAP_AND_EVIDENCE_AMBIGUITY__NO_SCIENCE`；`REJECT__FINAL_ENTRY_GUARDS_UNTESTED__NO_SCIENCE`；`REJECT__ACTIVE_PREFLIGHT_AND_PREIMPORT_AUTHORITY_GAPS__NO_SCIENCE`；`REJECT__PREIMPORT_AUTHORITY_PATH_AND_BEHAVIOR_EVIDENCE_GAPS__NO_SCIENCE`；`REJECT__AUTHORITY_METADATA_FOLLOWS_UNSAFE_PATH__NO_SCIENCE`；`REJECT__STALE_INERT_SOURCE_ORDER_ASSERTION__NO_SCIENCE`；`REJECT__FULL_INERT_TEST_FAILED__NO_CANDIDATE__NO_SCIENCE`；`REJECT__LEDGER_COMPLETENESS_AND_SEAL_READBACK_PATH_GAPS__NO_SCIENCE`；`REJECT__NONAUTHORITY_PROPOSAL_MISSING_PROSPECTIVE_RUNNER_FIELD_BINDINGS__NO_SCIENCE`；`REJECT__NONAUTHORITY_PROPOSAL_MISSING_PROSPECTIVE_SCHEMA_AND_ACTIVE_BINDINGS__NO_SCIENCE`。有限 ACCEPT 只保留各自范围；原两次被禁止的 `--execute` 探测仍为违规历史，不予重分类。

来源路径及原始 SHA-256：

- `TASK_CURRENT.md`：`56E9DE7C53A033E72259721252254FC301F8DDFCDB1B54974C640DCA2F4C1ED6`
- `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_PROPOSAL_OWNER_SELECTION_A_20260926.md`：`A52AEF73F3D8DEC60067A3E2668C80B4DFBAB59F23482C134F98F85494CE5B6B`
- `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_ACTIVE_CONTRACT_PROPOSAL_REPAIR2_INDEPENDENT_REVIEW_20260926.md`：`7ECB074BEFF6BB1C07FB2309F5C7F3174D464CE7B10630561D3A660DCC6929BE`
- `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_FINAL_STATIC_PREPARATION_INDEPENDENT_REVIEW_20260926.md`：`17A6EBFB415A38D225268FFAD501D9FF623CA1C5CF0B4919BB9BC7CB71B34826`
- `tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_ACTIVE_CONTRACT_PROPOSAL_20260926.json`：`78AAF07333DCF1BA5A5717BF8DB252A616FEABDF2B7C04A8EC32D653241EA52E`
- `EVIDENCE/ch5_k1b_c9_post_failure_new_attempt_active_contract_proposal_zero_science_20260926/proposal_receipt.json`：`5A055DB9FB0AF0046F2538F0D740936EA52A901E6BD7035737067842589AFA64`
- `validators/multi_province/k1b_turn9_post_failure_new_attempt_timed/run.py`：`B1B2F54649B175F4E56C73135DECEED85C1AC966FE49A76431CF4B12B06633FD`
- `validators/multi_province/k1b_turn9_post_failure_new_attempt_outer_r2/run.py`：`AD592FCEEB6563D56BFEA6A9F35029B83712A6ACCED80A1BAF8F53C144F99D56`
- `EVIDENCE/ch5_k1b_c9_new_budget_failed_ledger_policy_zero_science_proposal_20260926/proposed_budget.json`：`66C2C028B07E2CB41FFBB05B643C6EF644291A0FC94C8DAF2FE888518D240460`
- `docs/CH5_K1B_C9_NEW_BUDGET_FAILED_LEDGER_POLICY_OWNER_ADOPTION_20260926.md`：`C1D88891C08D7526996F72DE6F77AA6D0FA2C593BAD91017877C8B8A0A51573D`

本轮唯一获准的无模型只读结构校验命令：

```text
python -c "import hashlib,json,pathlib; r=pathlib.Path.cwd(); m=json.loads((r/'tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_IDENTITY_CHAIN_PREPARATION_20260926.json').read_text(encoding='utf-8')); e=json.loads((r/'EVIDENCE/ch5_k1b_c9_post_failure_new_attempt_identity_chain_preparation_zero_science_20260926/preparation_receipt.json').read_text(encoding='utf-8')); p=json.loads((r/m['accepted_proposal']['path']).read_text(encoding='utf-8')); assert m['schema'].endswith('NON_AUTHORITY_V1') and m['active'] is False and m['execution_authorized'] is False; assert m['accepted_proposal']['raw_sha256']==hashlib.sha256((r/m['accepted_proposal']['path']).read_bytes()).hexdigest().upper() and len(p['prospective_live_contract_fields'])==27; assert [x['node'] for x in m['dependency_matrix']]==['R','C','O','T'] and all(x['status']=='PENDING/ABSENT' for x in m['dependency_matrix']); assert all(not (r/x).exists() for x in m['absent_live_and_new_root_paths']); assert all(m['protected_manifest_sha256'][k]['raw_sha256']==hashlib.sha256((r/v['path']).read_bytes()).hexdigest().upper() for k,v in m['protected_manifest_sha256'].items()); assert e['matrix_raw_sha256']==hashlib.sha256((r/e['matrix_path']).read_bytes()).hexdigest().upper(); print('PASS: non-authority R-C-O-T dependencies, accepted proposal and absent live paths')"
```

唯一一次校验实际输出 `PASS: non-authority R-C-O-T dependencies, accepted proposal and absent live paths`，退出码 `0`，未重跑。通过也不构成 live、runner 或科学 ACCEPT；下一门 GPT Work 独立 ACCEPT/REJECT。
