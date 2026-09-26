# C9 新尝试合同非权威提案（零科学）

以下原候选记录保留为历史；其提案已被独立 REJECT，末尾 Repair1 节记录本轮有效候选。

**状态：仅供 GPT Work 独立 ACCEPT/REJECT 的提案；不可执行。** 本报告、提案 JSON 和收据不建立 live 合同、runner-recognized ACCEPT、Owner 一次性执行采纳或任务。

起点 HEAD `4f2ce2373e3ff58fb19870e9f7724c3298694daf`，父提交 `c175292de6ea07991b1ea22b00ce738bcd7c11b3`，`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。起点跟踪文件与暂存区干净，仅五个受保护未跟踪输出根；五份清单 SHA-256（C6-prime、C7、C8、C8-timing、C9-partial）依次为 `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`、`413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`、`5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`、`5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`、`80BD0D42CB73B4E39B811E759505480542D5A73227014F30B732C34A8AC1FDC3`。

提案路径 `tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_ACTIVE_CONTRACT_PROPOSAL_20260926.json`，独立 schema 为 `CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_NON_AUTHORITY_CONTRACT_PROPOSAL_V1`，`active=false` 且 `execution_authorized=false`，原始 SHA-256 `0D9417478008190D517ABE3FA61A8AA4FCA1F2CBB6AC18C6788B6D91F6D83950`。新身份 `C9_POST_FAILURE_NEW_ATTEMPT_001`，预算命名空间 `C8_START_C9_POST_FAILURE_NEW_ATTEMPT_001_C10_PROSPECTIVE`，独占但未创建的输出根 `reports/ch5_k1b_turn9_post_failure_new_attempt_001`。

预算映射直接逐字段复制已采纳来源 JSON：每类别 39 键、省级 5 键、C9 加未来 C10 累计 39 键、项目生命周期治理上限 39 键；旧完整 turn 治理扣账另为 39 键，不代表实际调用。四张上限图的规范 SHA-256 分别为：

- category `F76B958C8D57CEAD22B61A497FCCFBF45143E1DC2AA07CCC656EBA6252464C20`
- province `FDA5A76D45B639FD0B793E6270D051255CCFC0F85E7E982A152A4AA7743D7028`
- cumulative `3E2DF35B6D867A0680E1ABBBB778205982F1845139D775A63A9D4672B7D6CA3A`
- lifetime governance `D5C5D10AD030FFD2F12AA81FFFD8DBD5CF8655D4870452593C7AA3B5A224604C`

旧 C9 一次性尝试已消耗，实际账本仍为 `CALL_LEDGER_UNRESOLVED`；完整旧 turn 仅作治理扣账。新 C9 仅前瞻一尝试、零重试。36,000 秒单调合作式资源墙只阻止到期后的下一次科学入口，不打断已进入调用，也不自动授权 C10。Results eligibility 为 `FALSE`。

未来 runner-recognized review SHA、精确 live 合同 Owner 采纳、Owner 一次性执行采纳、逐字节任务副本及最终独立 dispatch review 均为 `PENDING/ABSENT`。这些门解决前，精确 live 合同字节不能最终确定；不得把此提案复制成 live 合同。

来源原始 SHA-256：

- `TASK_CURRENT.md`：`FF5621F8A9FC8C1478133FB4AD83C5E4DA71C9F87386508E55C03A8943FE2E98`
- `EVIDENCE/ch5_k1b_c9_new_budget_failed_ledger_policy_zero_science_proposal_20260926/proposed_budget.json`：`66C2C028B07E2CB41FFBB05B643C6EF644291A0FC94C8DAF2FE888518D240460`
- `docs/CH5_K1B_C9_NEW_BUDGET_FAILED_LEDGER_POLICY_OWNER_ADOPTION_20260926.md`：`C1D88891C08D7526996F72DE6F77AA6D0FA2C593BAD91017877C8B8A0A51573D`
- `docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_FINAL_STATIC_PREPARATION_INDEPENDENT_REVIEW_20260926.md`：`17A6EBFB415A38D225268FFAD501D9FF623CA1C5CF0B4919BB9BC7CB71B34826`
- `validators/multi_province/k1b_turn9_post_failure_new_attempt_timed/run.py`：`B1B2F54649B175F4E56C73135DECEED85C1AC966FE49A76431CF4B12B06633FD`
- `validators/multi_province/k1b_turn9_post_failure_new_attempt_outer_r2/run.py`：`AD592FCEEB6563D56BFEA6A9F35029B83712A6ACCED80A1BAF8F53C144F99D56`
- `reports/ch5_k1b_turn8_outer_r2_20260925_run001/execution_artifact_manifest.json`：`5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`
- `reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn9_entering_bundle_manifest.json`：`40200B60729A5B4173E24661843980851F8610A9FA2186F7E411B7FE9E5CDC65`
- `reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn9_entering_bundle_readback.json`：`E428D105600D091979B526ADD6BF61E0FC294050B9FAB97FE8B87A29A1012F85`
- `reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn9_k1b_input_candidate.json`：`FBB18A5B8B4FD94F337510DBB4E62F94188C27863EED1F79FE2E1A71B5BC39AB`
- `reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn9_k1b_frozen_share_payoff_plan.npz`：`E7E6AF79864F67A28386ECF8BEB3B71C6080E9A6C6E64F4CBA8125E1C19D34DD`

历史独立 REJECT（各自只约束其候选）：`REJECT__TASK_BOUNDARY_VIOLATION_AND_STATIC_GAPS__NO_SCIENCE`；`REJECT__SEALED_INPUT_PATH_GAP_AND_EVIDENCE_AMBIGUITY__NO_SCIENCE`；`REJECT__FINAL_ENTRY_GUARDS_UNTESTED__NO_SCIENCE`；`REJECT__ACTIVE_PREFLIGHT_AND_PREIMPORT_AUTHORITY_GAPS__NO_SCIENCE`；`REJECT__PREIMPORT_AUTHORITY_PATH_AND_BEHAVIOR_EVIDENCE_GAPS__NO_SCIENCE`；`REJECT__AUTHORITY_METADATA_FOLLOWS_UNSAFE_PATH__NO_SCIENCE`；`REJECT__STALE_INERT_SOURCE_ORDER_ASSERTION__NO_SCIENCE`；`REJECT__FULL_INERT_TEST_FAILED__NO_CANDIDATE__NO_SCIENCE`；`REJECT__LEDGER_COMPLETENESS_AND_SEAL_READBACK_PATH_GAPS__NO_SCIENCE`。有限的 final-entry 静态顺序 ACCEPT、惰性测试/证据 ACCEPT，以及最终静态准备 `ACCEPT__WHOLE_RUNNER_STATIC_PREPARATION_ONLY__NO_SCIENCE` 均不构成 live 或科学许可。原候选两次被禁止的 `--execute` 探测保留为违规历史，本轮为零。

本轮模型调用、科学调用、`--execute` 探测、新 C9/C10 尝试、重试、部分续跑及受保护输出写入均为零。新输出根、live 合同、runner-recognized ACCEPT 审查、Owner 执行采纳和一次性任务五条路径全部缺席。

文件定稿后的唯一获准只读、无模型提案验证命令：

```text
python -c "import hashlib,json,pathlib; r=pathlib.Path.cwd(); p=json.loads((r/'tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_ACTIVE_CONTRACT_PROPOSAL_20260926.json').read_text(encoding='utf-8')); e=json.loads((r/'EVIDENCE/ch5_k1b_c9_post_failure_new_attempt_active_contract_proposal_zero_science_20260926/proposal_receipt.json').read_text(encoding='utf-8')); b=json.loads((r/p['budget_source_path']).read_text(encoding='utf-8')); c=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest().upper(); assert p['schema']!='CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_CONTRACT_V1' and p['active'] is False and p['execution_authorized'] is False; assert [len(p[k]) for k in ('per_category_attempt_ceiling','per_province_attempt_ceiling','c9_c10_cumulative_ceiling','project_lifetime_governance_ceiling')]==[39,5,39,39]; assert p['per_category_attempt_ceiling']==b['proposed_c9_per_category_attempt_ceiling']; assert all(c(p[k])==p['canonical_map_sha256'][n] for k,n in (('per_category_attempt_ceiling','category'),('per_province_attempt_ceiling','province'),('c9_c10_cumulative_ceiling','cumulative'),('project_lifetime_governance_ceiling','lifetime'))); assert all(not (r/x).exists() for x in e['absent_live_and_new_root_paths']); assert e['proposal_raw_sha256']==hashlib.sha256((r/e['proposal_path']).read_bytes()).hexdigest().upper(); print('PASS: proposal-only schema, four maps, source binding, and absent live/new-root paths')"
```

唯一一次验证实际结果：`PASS: proposal-only schema, four maps, source binding, and absent live/new-root paths`，退出码 `0`。验证通过只证明提案结构与已采纳来源一致，不构成合同、runner 或科学 ACCEPT。下一门：GPT Work 独立 ACCEPT/REJECT。

## Repair1：未来 runner 字段绑定修复（2026-09-26）

起点任务提交 `05d067be61409e7cdee9baa8da1b0b0b22ca5b5c` 是被拒候选 `c91c3030efb3d303fa50c7bb1aba66bc075d9d3a` 的直接子提交；`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。前一候选提案/报告/收据原始 SHA-256 分别为 `0D9417478008190D517ABE3FA61A8AA4FCA1F2CBB6AC18C6788B6D91F6D83950`、`E5A8DED802CCB1A4014460DF671163ADB769A60D24066D4A03E802ADD99CB342`、`267715BFD86C0384411F5CDC82CB624CA698C2666A8999AA7AABE7B4C74F057E`。独立裁决 `REJECT__NONAUTHORITY_PROPOSAL_MISSING_PROSPECTIVE_RUNNER_FIELD_BINDINGS__NO_SCIENCE`，与先前九项 REJECT 并存。

本轮提案仍用独立 schema、顶层 `active=false` 和 `execution_authorized=false`；新原始 SHA-256 为 `18BFB7B274936BFB06806BD3F27871D277815DC644CD80A29791F52FD36D039B`。新增 `prospective_live_contract_fields` 只列未来 runner 字段已知映射，字段本身不构成 live 合同。它把新 `execution_id` 与仅作旧尝试来源的 `old_execution_id=C9_TIMED_RISK_RUN001` 分开，使用 `output_root`、`attempts=1`、`retries=0`、字面 `resource_policy=COOPERATIVE_PROCESS_WALL_CAP`、`resource_wall_seconds=36000`，并绑定预算/Owner 文件、wrapper/delegate 原始哈希和不变 `src_tree`。`sealed_input_sha256` 精确为 `manifest/readback/json/npz` 四键；四张预算上限图和旧治理扣账图直接复制已采纳 JSON。

已知字段映射不能最终确定 live 合同字节。`independent_review_sha256` 与 runner-recognized review、精确 live 采纳、Owner 一次性执行采纳、逐字节任务及最终 dispatch 审查仍为 `PENDING/ABSENT`。没有新 C9 根或 live 权威链。旧实际账本仍为 `CALL_LEDGER_UNRESOLVED`，完整旧 turn 扣账只属治理记账；C10、Results 和新科学执行均关闭。原两次禁止的 `--execute` 探测仍是违规历史，本轮探测、模型/科学调用、新 C9/C10 尝试、重试、部分续跑及受保护输出写入均为零。

本轮唯一获准的无模型、只读提案检查命令（文件定稿后运行）：

```text
python -c "import hashlib,json,pathlib; r=pathlib.Path.cwd(); p=json.loads((r/'tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_ACTIVE_CONTRACT_PROPOSAL_20260926.json').read_text(encoding='utf-8')); e=json.loads((r/'EVIDENCE/ch5_k1b_c9_post_failure_new_attempt_active_contract_proposal_zero_science_20260926/proposal_receipt.json').read_text(encoding='utf-8')); b=json.loads((r/p['budget_source_path']).read_text(encoding='utf-8')); f=p['prospective_live_contract_fields']; assert p['schema']!='CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_CONTRACT_V1' and p['active'] is False and p['execution_authorized'] is False; assert f['execution_id']=='C9_POST_FAILURE_NEW_ATTEMPT_001' and f['old_execution_id']=='C9_TIMED_RISK_RUN001' and f['execution_id']!=f['old_execution_id']; assert f['output_root']=='reports/ch5_k1b_turn9_post_failure_new_attempt_001' and f['attempts']==1 and f['retries']==0 and f['resource_policy']=='COOPERATIVE_PROCESS_WALL_CAP' and f['resource_wall_seconds']==36000; assert f['budget_proposal_sha256']==p['budget_source_raw_sha256'] and f['budget_owner_adoption_sha256']==p['budget_owner_adoption_raw_sha256'] and f['wrapper_sha256']==p['wrapper_raw_sha256'] and f['delegate_sha256']==p['delegate_raw_sha256'] and f['src_tree']==p['src_tree']; assert f['sealed_input_sha256']=={'manifest':p['sealed_c8_input_raw_sha256']['entering_manifest'],'readback':p['sealed_c8_input_raw_sha256']['entering_readback'],'json':p['sealed_c8_input_raw_sha256']['json'],'npz':p['sealed_c8_input_raw_sha256']['npz']}; assert all(f[k]==b[v] for k,v in (('per_category_attempt_ceiling','proposed_c9_per_category_attempt_ceiling'),('per_province_attempt_ceiling','proposed_c9_per_province_attempt_ceiling'),('c9_c10_cumulative_ceiling','proposed_c9_plus_future_c10_cumulative_ceiling'),('project_lifetime_governance_ceiling','full_old_turn_charge_project_lifetime_governance_ceiling_if_new_grant_adopted_not_calls'))); assert f['old_governance_charge_per_category']=={k:v['full_old_turn_governance_charge_not_calls'] for k,v in b['old_failure_category_matrix'].items()}; assert f['independent_review_sha256']=='PENDING/ABSENT' and all(x=='PENDING/ABSENT' for x in p['future_authority'].values()); assert f['automatic_c10_authorization'] is False and f['results_eligibility'] is False; assert all(not (r/x).exists() for x in e['absent_live_and_new_root_paths']); assert e['proposal_raw_sha256']==hashlib.sha256((r/e['proposal_path']).read_bytes()).hexdigest().upper(); print('PASS: non-authority proposal matches prospective runner fields and live paths remain absent')"
```

唯一一次检查实际输出为 `PASS: non-authority proposal matches prospective runner fields and live paths remain absent`，退出码 `0`；未重跑。本轮只证明提案字段对应，不构成 runner、合同或科学 ACCEPT；提交后等待 GPT Work 独立 ACCEPT/REJECT。
