# MP4B stale entry regression remediation and zero-science preflight report

Date: 2026-08-31

## Terminal verdict

`MP4B_STALE_ENTRY_REGRESSION_CONTRACT_REMEDIATION_AND_FULL_ZERO_SCIENCE_PREFLIGHT_PASS`

The single stale entry-test contract was aligned with the already accepted
source-postloop adapter. The exact predecessor regression selection then passed
`64 passed`. This is preflight readiness only; no stationary science is
authorized or executed by this task.

## Live continuity

- repository: `zcx369658780/dissertation-ch5-two-asset-hank`;
- branch: `codex/ch5-adjustment-boundary-redesign`;
- fresh-fetched live task commit: `d10ed24838111e442d9662ae2f4ee927e0da4d68`;
- direct parent: `f82d99fef301dc9ba9d8de58ebe7bdeafdd7efb3`;
- start `HEAD == origin/main`, ahead/behind `0/0`, worktree clean;
- task issuer, repository identity, controlling rules, allowed paths, zero-science
  budget and closeout contract were verified before mutation.

## Exact stale-contract remediation

Expected predecessor Git blob SHA:
`52f729a22c911b8596eecd6a42ebee8dc9d8909a` (matched before editing).

Exact assertion change:

```diff
-    assert "solve_household_steady_state" in text and "run_online_stationary" in text
+    assert "solve_matlab_source_postloop_household" in text and "run_online_stationary" in text
+    assert "solve_household_steady_state(" not in text
```

All existing assertions for `run_online_stationary`, absence of `solve_root`,
absence of historical `chapter5_model` imports, and the source-controller
constants/expressions remain unchanged. The test was not weakened, skipped,
xfail-marked or broadly rewritten.

Marker established:
`MP4B_STALE_ENTRY_REGRESSION_CONTRACT_ALIGNED_WITH_ACCEPTED_SOURCE_POSTLOOP_ADAPTER`.

This is a validation-test contract remediation, not scientific-code repair:
the accepted validation driver already used the source-postloop route and its
bytes were immutable. No production, export, adapter, driver, runtime, MP2, MP3,
economic or comparator implementation was changed.

## Immutable identities

| Object | SHA-256 | Result |
|---|---|---|
| `economics.py` | `F2B67D393D7495A83281C259F6D9CC5F8AFF18B3C4ABDEB7A07F354582DEF2D1` | exact |
| `matlab_faithful_policy.py` | `ECF56FAA7E87A0F5156E5866F1873556D6603E98AA33C8E41C400FD016C75CDC` | exact |
| standalone export | `B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3` | exact |
| MP2 `one_turn.py` | `D18C4385745E33E917B79994CAA069BE8825C9F22919A5A9EDE918845312D98D` | exact |
| MP3 `steady_state.py` | `7065D0FCBFDA6A88C8F773DEBDF277F6E300A8E0195B7CC635F7A0033D74D88C` | exact |
| stationary runtime | `226BE912AB776F57A8D8EFACE912AB2A3331E865638AC36976F6D578BDB086A0` | exact |
| source-semantics map | `6A4FD1576100D7CE36787EAA7E6B833ACED2D94B89B929EC6ADD45559995C028` | exact |
| source-postloop adapter | `8A6308870606A02886E9A8E4B32E942A7D433237405E6B9E86EE4175FB2DFF06` | exact |
| validation driver | `9033218710204CA4EA2AF0351376E47BB5B4F203923E6155DC4776ADD336091E` | exact |
| canonical corrected-2009 input | `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48` | exact |
| comparator contract | `E74E5BF8506AF841BEDB07004C9DCD71E64E1F6143DC8B5C01F9FF734C6C3C3A` | exact |
| final-state field map | `A1D0F04D9FC77975D7E11EDBA44EF91FD860D5344D72688B68494FD9316024CB` | exact |
| read-only comparator helper | `A6F7D2BBF7EE0936A6A0A45880B41D7AC77DB5AA7C3CA4B0F207F2D2A2DC08CF` | exact |

Read-only preserved MATLAB identities also matched exactly:

- stationary output: `6233AB8B7380BE4D4E136851BC59F747EEB78B285B3A7A5903FEFFE64BCF464B`;
- profile: `040C38E9E5FEE374202840C7741B7A15D6CFAE668FF8302619225FEEEC5DC90C`;
- terminal JSON: `04D143B7553D1041B810B875575C06AE3E2F82132B2D55FEFDF5C3ED8AAB7270`.

## Complete zero-science preflight

The predecessor's exact regression selection was recovered from its local
execution evidence and rerun unchanged:

```text
python -m pytest tests/test_mp4b_matlab_source_postloop_household_adapter.py tests/test_mp4b_preserved_matlab_python_final_state_field_map.py tests/test_mp2_source_faithful_one_turn.py tests/test_mp3_manual_update_map.py tests/test_mp4b_stationary_runtime.py tests/test_matlab_faithful_two_asset_ha_standalone_export.py tests/test_matlab_faithful_kfe.py tests/test_mp4b_python_empirical_entry.py -q
```

Result: `64 passed in 7.67s`.

This exact bundle covered direct-script bootstrap, corrected-2009 presolver
identity mismatch `0`, all `24,800/24,800` source-initialization cells,
first-Beijing input semantic mismatch `0`, adapter routing/static acceptance,
MP2, all seven MP3 scenarios, online stationary runtime, accepted raw-`Vb`
household/export behavior, field-map/helper checks, stale entry regression and
clean-process/no-R5 checks. Temporary pytest outputs were isolated; no model run
root was created. Reused predecessor artifact identities remain:

- bootstrap manifest: `F15AC535BEC43CE0FD32002574D3F5AAE8F7B9BAF6ADDCF948E56223D7C8B11A`;
- presolver evidence: `7F766674C6AC8C12ABF37C957F50E27A36F490D17EB37E2AB19C1F8A9EC43843`;
- source initialization: `36C1DA1F1BEABD857BA54417A168CB8CA17FC0F984FF50627F12652220980A8B`;
- first-Beijing input: `EC221AC91BFC805335384BEB52B4EE25E9BD6ECFCAD14207480AE87E2D59F44A`.

`python -m py_compile tests/test_mp4b_python_empirical_entry.py`: PASS.
`git diff --check`: PASS.

Marker established:
`MP4B_SOURCE_POSTLOOP_ADAPTER_2009_STATIONARY_REEXECUTION_PREFLIGHT_PASS`.

## Zero scientific/model call ledger

| Operation | Calls |
|---|---:|
| Python stationary top-level / rerun | 0 / 0 |
| real household adapter / HJB / KFE / aggregate | 0 / 0 / 0 / 0 |
| Shanxi replay | 0 |
| qualified comparator science | 0 |
| MATLAB stationary / household / HJB / KFE / presolver | 0 / 0 / 0 / 0 / 0 |
| MP2 / MP3 scientific execution | 0 / 0 |
| other year / annual batch | 0 / 0 |
| shocks / AR1 / transition / dynamics / IRF | 0 / 0 / 0 / 0 / 0 |
| historical R5 / Results | 0 / 0 |

The intended Python scientific root
`D:\ProjectTemp\ch5-mp4b-python-only-source-postloop-reexecution-20260831-001`
was checked and does not exist. Production/export/scientific-module mutation
count: `0`.

## Changed paths and forbidden-operation audit

Changed paths are exactly:

- `tests/test_mp4b_python_empirical_entry.py`;
- this bounded report.

No validator driver/adapter, field map/helper, comparator contract,
production/export/scientific source, MATLAB, canonical data, rule or historical
R5 path was modified. No stationary reauthorization was inferred.
Forbidden-operation audit: PASS.

## Git closeout

Closeout uses explicit-path staging, one execution commit, one non-force push
and live GitHub read-back of both changed paths. The exact execution commit is
reported by the immutable post-push `HEAD == origin/main` read-back because a
commit cannot embed its own SHA without changing that SHA.

Required final state: `HEAD == origin/main`, ahead/behind `0/0`, clean worktree.

## Exactly one recommended next gate

Publish a separately reviewed one-shot Python-only corrected-calendar-2009
stationary reexecution using the already accepted source-postloop adapter and
the same immutable preserved MATLAB baseline; MATLAB rerun remains zero.
