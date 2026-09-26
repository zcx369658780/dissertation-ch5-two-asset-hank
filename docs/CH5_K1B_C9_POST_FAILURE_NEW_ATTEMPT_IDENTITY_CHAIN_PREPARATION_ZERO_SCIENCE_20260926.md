# C9 新尝试身份链依赖矩阵（零科学、非权威）

原候选记录保留为历史；其身份链措辞已被独立 REJECT。末尾 Repair1 节给出本轮有效澄清。

**状态：待 GPT Work 独立 ACCEPT/REJECT；不创建 R/C/O/T，也不授权运行。**

起点 HEAD `b189834e6451775bbe6754911babf5275c20886b`，父提交 `26910bc9aef91a8c77a604c144422f5a26a3052e`，`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。本轮仅创建矩阵 JSON、本报告和机器收据三条非权威路径。矩阵原始 SHA-256 `FE602C2E89CA2484A928E790A3491FA3550F5440B2CFADD94EE40BB4D5DF8FBB`；schema `CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_IDENTITY_CHAIN_NON_AUTHORITY_V1`、`active=false`、`execution_authorized=false`。

Owner 选择 A 仅采纳 27 字段的已接受映射作后续零科学准备基础。提案 `tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_ACTIVE_CONTRACT_PROPOSAL_20260926.json` 原始 SHA-256 `78AAF07333DCF1BA5A5717BF8DB252A616FEABDF2B7C04A8EC32D653241EA52E`，独立限域裁决 `ACCEPT__NONAUTHORITY_PROPOSAL_FIELD_MAPPING_ONLY__NO_SCIENCE`。最终 wrapper/delegate 原始 SHA-256 分别为 `B1B2F54649B175F4E56C73135DECEED85C1AC966FE49A76431CF4B12B06633FD`、`AD592FCEEB6563D56BFEA6A9F35029B83712A6ACCED80A1BAF8F53C144F99D56`；预算来源与 Owner 采纳文件原始 SHA-256 分别为 `66C2C028B07E2CB41FFBB05B643C6EF644291A0FC94C8DAF2FE888518D240460`、`C1D88891C08D7526996F72DE6F77AA6D0FA2C593BAD91017877C8B8A0A51573D`。

依赖关系来自 timed runner 的静态身份门；下面列的是未来所需字面 token，并非本轮生成的权威文件：

| 节点 | 未来 runner 路径 | 依赖与必需身份 | 当前状态 |
|---|---|---|---|
| R 独立 runner 审查 | `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_RUNNER_INDEPENDENT_REVIEW.md` | `Reviewer: GPT Work`、`Verdict: ACCEPT__C9_POST_FAILURE_NEW_ATTEMPT_RUNNER`、wrapper/delegate 哈希行；独立审查后其提交 SHA 才能绑定 C。 | `PENDING/ABSENT` |
| C live 合同 | `tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_CONTRACT.json` | 精确 runner schema、`active=true`、已接受 27 字段已知值、`independent_review_sha256=R`；先有不依赖已提交 C SHA 的内容审查与 Owner 内容采纳，之后才有已提交 C SHA 绑定 O/T。 | `PENDING/ABSENT` |
| O Owner 执行采纳 | `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_EXECUTION_OWNER_ADOPTION.md` | `OWNER_ADOPTED__SINGLE_NEW_C9_POST_FAILURE`、新执行 ID/输出根、C 与 R 提交 SHA；须有独立的 Owner 一次性科学决定。 | `PENDING/ABSENT` |
| T 未来执行任务/逐字节副本 | 现存 `TASK_CURRENT.md` 与未来 `tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_EXECUTION.md` | 两文件逐字节一致，含任务 ID/status、新执行 ID/根、O/C/R 提交 SHA 和 wrapper/delegate 哈希；当前任务不是未来执行任务。 | `PENDING/ABSENT` |

R/C/O/未来执行 T 的未知哈希均为 `PENDING/ABSENT`，不得推造或自我求解。Owner 一次性 C9 执行决定必须先于 O；O/T 后仍需最终独立 dispatch 审查，本轮不建立这些权限。

五份受保护未跟踪输出根的清单原始 SHA-256（C6-prime、C7、C8、C8-timing、C9-partial）为：`7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`、`413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`、`5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`、`5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`、`80BD0D42CB73B4E39B811E759505480542D5A73227014F30B732C34A8AC1FDC3`。新 C9 根、R/C/O 及未来执行 task-copy 均缺席；`TASK_CURRENT.md` 当前存在，是零科学任务而非执行 T。已封存 C8 输入的 `manifest/readback/json/npz` 四个哈希已在矩阵中逐项绑定。

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

## Repair1：Owner 两类采纳与未来任务缺席集澄清（2026-09-26）

起点任务提交 `418175e6f413261967e45cf15b6e0ec75d577299` 是被拒候选 `752a8fecf75608e943057a3890dd76621fbce309` 的直接子提交，`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。前一矩阵/报告/收据 SHA-256 分别为 `FE602C2E89CA2484A928E790A3491FA3550F5440B2CFADD94EE40BB4D5DF8FBB`、`D58C2C7A46BA23A24D5E32077921407A473A0E0D747051B43EB66DD0EDCD4902`、`CB1D92D485255FF6C90D770B3D7F26E7C4FDF7D3BF934B492D3ABAA21D82A97C`。本轮直接前置裁决 `REJECT__IDENTITY_CHAIN_OWNER_ORDER_AND_TASK_ABSENCE_AMBIGUITY__NO_SCIENCE` 与全部更早 REJECT 并存。当前矩阵 SHA-256 `FA6CB999D81E8C34CE4D5A1AFAC619EB746E24E3F0ED5B1FD385CE1F0E7AC636`。

无环次序是：R 的提交 SHA → 拟议 C 内容及**独立的 pre-C 内容审查/Owner 内容采纳**（尚无确定路径或哈希，也不依赖已提交 C SHA）→ 已提交 C SHA → **另一次明确的 Owner 单次 C9 执行决定** → 绑定 C/R 的 post-C 执行采纳 O → 未来执行版 `TASK_CURRENT.md` 与 task-copy 逐字节一致的 T → 最终独立 dispatch 审查。pre-C 内容采纳与 post-C 的 O 是不同决策；Owner 执行决定须先于 O，不待 O/T 组装完成才发生。每一步仍需未来单独授权，本矩阵不产生任何一步。

精确缺席集是 R、C、O、未来执行 task-copy 与新 C9 输出根。`TASK_CURRENT.md` **已存在**，内容是本轮零科学任务，不是未来执行 T；未来的执行版内容及其副本仍为 `PENDING/ABSENT`。顶层 `active=false`、`execution_authorized=false`；所有未来权威 SHA 仍为 `PENDING/ABSENT`。五份受保护清单原始哈希和已接受提案/runner/预算来源身份不变，旧实际账本仍 `CALL_LEDGER_UNRESOLVED`、旧完整 turn 扣账仅为治理记账、Results eligibility `FALSE`。本轮 `--execute` 探测、模型/科学调用、新 C9/C10 尝试、重试、部分续跑及受保护输出写入均为零；原两次违规探测及所有有限 ACCEPT 范围维持原样。

本轮来源：`TASK_CURRENT.md` SHA-256 `E29CE53951F990E1C656862E8348FD9BD75ABDC70AB855299021A8999149B560`；独立 REJECT 审查 SHA-256 `96F2CB9DC48D8F397A0009CE50432AF8FCBC489EDDCFC3D60B02DB487AF67BD8`。本轮唯一获准的无模型只读结构校验命令：

```text
python -c "import hashlib,json,pathlib; r=pathlib.Path.cwd(); m=json.loads((r/'tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_IDENTITY_CHAIN_PREPARATION_20260926.json').read_text(encoding='utf-8')); e=json.loads((r/'EVIDENCE/ch5_k1b_c9_post_failure_new_attempt_identity_chain_preparation_zero_science_20260926/preparation_receipt.json').read_text(encoding='utf-8')); p=json.loads((r/m['accepted_proposal']['path']).read_text(encoding='utf-8')); d=m['dependency_order']; assert m['active'] is False and m['execution_authorized'] is False and len(p['prospective_live_contract_fields'])==27; assert m['accepted_proposal']['raw_sha256']==hashlib.sha256((r/m['accepted_proposal']['path']).read_bytes()).hexdigest().upper(); assert [x['step'] for x in d]==list(range(1,8)) and [x['gate'] for x in d]==['R_COMMITTED_SHA','PROSPECTIVE_C_CONTENT_AND_DISTINCT_PRE_C_REVIEW_OWNER_CONTENT_ADOPTION','C_COMMITTED_SHA','EXPLICIT_OWNER_ONE_SHOT_C9_EXECUTION_DECISION','O_BINDING_C_AND_R','BYTE_IDENTICAL_FUTURE_EXECUTION_CURRENT_AND_TASK_COPY_T','FINAL_INDEPENDENT_DISPATCH_REVIEW']; assert d[1]['depends_on_committed_C_sha'] is False and d[1]['established_path_or_sha'] is False and d[3]['must_precede']=='O'; assert m['separate_gates']['pre_C_exact_live_content_review_and_owner_adoption']['depends_on_committed_C_sha'] is False and m['separate_gates']['post_C_owner_execution_adoption_O']['requires_committed_C_and_R_sha'] is True; assert m['absence_statement']['current_TASK_CURRENT_md_present'] is True and m['absence_statement']['current_TASK_CURRENT_md_is_future_execution_T'] is False and (r/'TASK_CURRENT.md').exists() and 'TASK_CURRENT.md' not in m['absent_live_and_new_root_paths']; assert all(not (r/x).exists() for x in m['absent_live_and_new_root_paths']); assert all(v['raw_sha256']==hashlib.sha256((r/v['path']).read_bytes()).hexdigest().upper() for v in m['protected_manifest_sha256'].values()); assert e['matrix_raw_sha256']==hashlib.sha256((r/e['matrix_path']).read_bytes()).hexdigest().upper(); print('PASS: acyclic Owner gates, current task present, future authority absent')"
```

唯一一次校验实际输出 `PASS: acyclic Owner gates, current task present, future authority absent`，退出码 `0`，未重跑。候选提交后仅待 GPT Work 独立 ACCEPT/REJECT。
