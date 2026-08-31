# MP4B source-postloop corrected-2009 Python reexecution report

Date: 2026-08-31

## Terminal verdict

`MP4B_PYTHON_ONLY_CORRECTED_CALENDAR2009_STATIONARY_REEXECUTION_WITH_SOURCE_POSTLOOP_ADAPTER_AGAINST_PRESERVED_MATLAB_BLOCKED`

The mandatory zero-science regression gate failed before Python science. No
stationary, household, HJB, KFE, aggregation or comparator call occurred. The
failure is a stale predecessor test contract, not scientific output.

## Live continuity and immutable identities

- live task/start HEAD: `043d2f72b306f19af9e1a4c92a6a2ae477f10e7a`;
- direct parent: `45a5e86d197e1032068b2d8b1d468a9a9dfda006`;
- start worktree: clean;
- `economics.py`: `F2B67D393D7495A83281C259F6D9CC5F8AFF18B3C4ABDEB7A07F354582DEF2D1`;
- `matlab_faithful_policy.py`: `ECF56FAA7E87A0F5156E5866F1873556D6603E98AA33C8E41C400FD016C75CDC`;
- standalone export: `B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3`;
- MP2: `D18C4385745E33E917B79994CAA069BE8825C9F22919A5A9EDE918845312D98D`;
- MP3: `7065D0FCBFDA6A88C8F773DEBDF277F6E300A8E0195B7CC635F7A0033D74D88C`;
- stationary runtime: `226BE912AB776F57A8D8EFACE912AB2A3331E865638AC36976F6D578BDB086A0`;
- source-semantics map: `6A4FD1576100D7CE36787EAA7E6B833ACED2D94B89B929EC6ADD45559995C028`;
- source-postloop adapter: `8A6308870606A02886E9A8E4B32E942A7D433237405E6B9E86EE4175FB2DFF06`;
- validation driver: `9033218710204CA4EA2AF0351376E47BB5B4F203923E6155DC4776ADD336091E`;
- canonical 2009 input: `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`.

No active historical R5 runtime import was found.

## Preserved MATLAB and comparator identities

Immutable root:
`D:\ProjectTemp\ch5-mp4b-fresh-calendar2009-matlab-20260830-001`.

| Artifact | SHA-256 |
|---|---|
| stationary output | `6233AB8B7380BE4D4E136851BC59F747EEB78B285B3A7A5903FEFFE64BCF464B` |
| profile | `040C38E9E5FEE374202840C7741B7A15D6CFAE668FF8302619225FEEEC5DC90C` |
| terminal JSON | `04D143B7553D1041B810B875575C06AE3E2F82132B2D55FEFDF5C3ED8AAB7270` |

MATLAB was only read/hashed. Preserved facts remain `COMPLETED`, 184 turns,
5,704 households and final 31/31 flags.

Reused comparator contract:
`validators/multi_province/mp4b_python_only_2009_stationary_comparator_contract.json`,
SHA-256 `E74E5BF8506AF841BEDB07004C9DCD71E64E1F6143DC8B5C01F9FF734C6C3C3A`.
Marker established:
`MP4B_REEXECUTION_2009_STATIONARY_COMPARATOR_CONTRACT_REUSED_UNCHANGED`.

## Frozen final-state field map and helper

- field map:
  `validators/multi_province/mp4b_preserved_matlab_python_final_state_field_map.json`;
- field-map SHA-256:
  `A1D0F04D9FC77975D7E11EDBA44EF91FD860D5344D72688B68494FD9316024CB`;
- marker: `MP4B_PRESERVED_MATLAB_PYTHON_FINAL_STATE_FIELD_MAP_FROZEN`;
- read-only comparator helper:
  `validators/multi_province/mp4b_compare_preserved_matlab_python_final_state.py`;
- helper SHA-256:
  `A6F7D2BBF7EE0936A6A0A45880B41D7AC77DB5AA7C3CA4B0F207F2D2A2DC08CF`.

The map was frozen before Python output and uniquely maps 31-province household
aggregates, final firm/destination labor, At-only productive state/returns,
firm, wage/monetary, GovInv and convergence/boundary fields. It excludes
`AtTax`, household-Lt substitution and `At+Bt` productive-capital substitution.
Mandatory national sums are `Ct/At/Bt/Yt`. Read-only schema tests confirmed 31
unique provinces, final 31/31 flags and wage-bound counts 7/17.

## Zero-science preflight disposition

Preflight root:
`D:\ProjectTemp\ch5-mp4b-source-postloop-reexecution-preflight-20260831-001`.

Passed:

- direct bootstrap, manifest SHA `F15AC535BEC43CE0FD32002574D3F5AAE8F7B9BAF6ADDCF948E56223D7C8B11A`;
- fresh presolver mismatch `0`, artifact SHA `7F766674C6AC8C12ABF37C957F50E27A36F490D17EB37E2AB19C1F8A9EC43843`;
- source initialization `24,800/24,800`, SHA `36C1DA1F1BEABD857BA54417A168CB8CA17FC0F984FF50627F12652220980A8B`;
- first-Beijing input mismatch `0`, SHA `EC221AC91BFC805335384BEB52B4EE25E9BD6ECFCAD14207480AE87E2D59F44A`;
- adapter routing/static acceptance;
- immutable identities and no R5 runtime;
- field-map/helper focused checks: `10 passed`;
- `py_compile`: PASS;
- `git diff --check`: PASS;
- scientific run root confirmed absent before the gate.

Failed required regression bundle:

`63 passed, 1 failed`.

Failure:
`tests/test_mp4b_python_empirical_entry.py::test_entry_freezes_source_controller_and_no_forbidden_runtime_imports`
still asserts that `solve_household_steady_state` must appear in the driver.
The accepted predecessor deliberately removed that call and requires
`solve_matlab_source_postloop_household`. The live task permits focused tests
only for the new field map/comparator, so this stale existing test was not
modified.

Therefore
`MP4B_SOURCE_POSTLOOP_ADAPTER_2009_STATIONARY_REEXECUTION_PREFLIGHT_PASS`
is not established, and Section 10 requires science to remain closed.

## Scientific execution and comparisons

- intended Python run root: not created;
- Python terminal category / outer turns: unavailable / 0;
- stationary top-level / reruns: `0 / 0`;
- household adapter/HJB/KFE/aggregate completed or attempted: all `0`;
- per-turn convergence counts: unavailable because no turn ran;
- first-Beijing output comparison: not rerun; only accepted predecessor evidence remains;
- qualified comparator: `0`;
- mapped provincial and national differences: unavailable and not fabricated;
- controller/boundary/adaptation comparison: unavailable because Python science did not begin.

First supported blocker: stale entry-preflight test contract. Classification:
`VALIDATION_TEST_CONTRACT_OUT_OF_DATE_WITH_ACCEPTED_SOURCE_POSTLOOP_ADAPTER`.
Material scientific mismatch list: empty because no science ran. Environment
failure list: empty. Unresolved execution item: required regression gate.

## Complete zero-call and forbidden-operation ledger

| Operation | Calls |
|---|---:|
| Python stationary / rerun | 0 / 0 |
| real household adapter / HJB / KFE / aggregate | 0 / 0 / 0 / 0 |
| Shanxi or ad-hoc household replay | 0 |
| qualified comparator | 0 |
| MATLAB stationary / household / HJB / KFE / presolver | 0 / 0 / 0 / 0 / 0 |
| MP2 / MP3 scientific execution | 0 / 0 |
| other year / annual batch | 0 / 0 |
| shocks / AR1 / transition / dynamics / IRF | 0 / 0 / 0 / 0 / 0 |
| historical R5 / Results | 0 / 0 |

Production/export/scientific-module mutation count: `0`. Adapter, driver,
stationary runtime, MP2, MP3, protected MATLAB, canonical data and project rules
were unchanged. Forbidden-operation audit: PASS.

## Changed paths

- final-state field map JSON;
- read-only final-state comparator helper;
- focused field-map/helper test;
- bounded CURRENT roadmap status update;
- this report.

## Git closeout

Explicit-path staging, one execution commit, one non-force push, GitHub read-back
of each changed path, `HEAD == origin/main`, ahead/behind `0/0` and clean
worktree are required and recorded after publication.

## Exactly one recommended next gate

Authorize a zero-science validation-test contract remediation that updates only
the stale entry regression to require the accepted source-postloop adapter and
re-runs the complete preflight bundle; it must not execute or automatically
reauthorize stationary science.
