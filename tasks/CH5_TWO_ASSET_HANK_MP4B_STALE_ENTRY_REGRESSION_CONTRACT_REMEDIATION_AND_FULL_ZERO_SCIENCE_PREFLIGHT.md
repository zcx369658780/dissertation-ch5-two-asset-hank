# CH5_TWO_ASSET_HANK_MP4B_STALE_ENTRY_REGRESSION_CONTRACT_REMEDIATION_AND_FULL_ZERO_SCIENCE_PREFLIGHT

Date: 2026-08-31

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / validation-contract remediator / zero-science preflight executor

Owner: final scientific authority

## 1. Purpose

Remediate the single stale regression contract that blocked the source-postloop corrected-calendar-2009 stationary reexecution before any science, then rerun the complete mandatory zero-science preflight bundle.

Accepted predecessor terminal:

`MP4B_PYTHON_ONLY_CORRECTED_CALENDAR2009_STATIONARY_REEXECUTION_WITH_SOURCE_POSTLOOP_ADAPTER_AGAINST_PRESERVED_MATLAB_BLOCKED`

Predecessor completion commit:

`f82d99fef301dc9ba9d8de58ebe7bdeafdd7efb3`

The predecessor established that every scientific/model call remained zero. Its only blocking test was:

`tests/test_mp4b_python_empirical_entry.py::test_entry_freezes_source_controller_and_no_forbidden_runtime_imports`

The stale assertion still required the superseded `solve_household_steady_state` route even though the accepted source-semantics task deliberately replaced that driver call with `solve_matlab_source_postloop_household`.

This task is strictly a **zero-science test-contract remediation and preflight revalidation**. It does not authorize Python stationary execution, household/HJB/KFE execution, comparator science, MATLAB execution, or automatic reauthorization of the stationary gate.

## 2. Accepted authority

Primary numerical authority remains:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

Accepted source-postloop authority remains:

- `MP4B_MATLAB_HJB_NONCONVERGENCE_POSTLOOP_KFE_AGGREGATE_SEMANTICS_FROZEN`
- `MP4B_PYTHON_STATIONARY_ABORT_ON_HJB_NONCONVERGENCE_SOURCE_SEMANTICS_MISMATCH_CONFIRMED`
- `MP4B_PYTHON_MULTI_PROVINCE_SOURCE_POSTLOOP_HOUSEHOLD_ADAPTER_STATIC_PASS`

Accepted classification:

`PYTHON_IMPLEMENTATION_ERROR__MULTI_PROVINCE_DRIVER_ABORTS_BEFORE_MATLAB_SOURCE_POSTLOOP_KFE_AND_AGGREGATES`

Do not reopen or reinterpret this adjudication in the present task.

## 3. Live continuity

Required execution-start predecessor:

`f82d99fef301dc9ba9d8de58ebe7bdeafdd7efb3`

At start:

1. fresh-fetch `origin/main`;
2. confirm this exact task is live on `main` as the direct child of `f82d99fef301dc9ba9d8de58ebe7bdeafdd7efb3`;
3. require a clean worktree;
4. verify repository identity and all controlling rule files;
5. verify the accepted scientific/validation identities in Section 4;
6. verify the current stale test blob is the expected predecessor version before editing;
7. verify no historical R5 / `chapter5_model` runtime dependency.

Any identity failure => stop before mutation.

## 4. Immutable identities

Require exact SHA-256 before and after the task unless explicitly listed as mutable below:

- `src/ch5_two_asset_hank/economics.py`:
  `F2B67D393D7495A83281C259F6D9CC5F8AFF18B3C4ABDEB7A07F354582DEF2D1`
- `src/ch5_two_asset_hank/matlab_faithful_policy.py`:
  `ECF56FAA7E87A0F5156E5866F1873556D6603E98AA33C8E41C400FD016C75CDC`
- `exports/matlab_faithful_two_asset_ha.py`:
  `B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3`
- accepted MP2 `src/ch5_two_asset_hank/multi_province/one_turn.py`:
  `D18C4385745E33E917B79994CAA069BE8825C9F22919A5A9EDE918845312D98D`
- accepted MP3 `src/ch5_two_asset_hank/multi_province/steady_state.py`:
  `7065D0FCBFDA6A88C8F773DEBDF277F6E300A8E0195B7CC635F7A0033D74D88C`
- stationary runtime:
  `226BE912AB776F57A8D8EFACE912AB2A3331E865638AC36976F6D578BDB086A0`
- source-semantics map:
  `6A4FD1576100D7CE36787EAA7E6B833ACED2D94B89B929EC6ADD45559995C028`
- source-postloop adapter:
  `8A6308870606A02886E9A8E4B32E942A7D433237405E6B9E86EE4175FB2DFF06`
- validation driver:
  `9033218710204CA4EA2AF0351376E47BB5B4F203923E6155DC4776ADD336091E`
- canonical corrected-2009 input:
  `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`
- reused stationary comparator contract:
  `E74E5BF8506AF841BEDB07004C9DCD71E64E1F6143DC8B5C01F9FF734C6C3C3A`
- frozen final-state field map:
  `A1D0F04D9FC77975D7E11EDBA44EF91FD860D5344D72688B68494FD9316024CB`
- read-only final-state comparator helper:
  `A6F7D2BBF7EE0936A6A0A45880B41D7AC77DB5AA7C3CA4B0F207F2D2A2DC08CF`

Preserved MATLAB baseline remains read-only and must not be executed:

- stationary output `6233AB8B7380BE4D4E136851BC59F747EEB78B285B3A7A5903FEFFE64BCF464B`
- profile `040C38E9E5FEE374202840C7741B7A15D6CFAE668FF8302619225FEEEC5DC90C`
- terminal JSON `04D143B7553D1041B810B875575C06AE3E2F82132B2D55FEFDF5C3ED8AAB7270`

Current stale test path:

`tests/test_mp4b_python_empirical_entry.py`

Expected predecessor Git blob SHA:

`52f729a22c911b8596eecd6a42ebee8dc9d8909a`

If the stale test differs from this expected predecessor object, stop and report instead of guessing a merge.

## 5. Exact authorized remediation

Modify only the stale contract inside:

`test_entry_freezes_source_controller_and_no_forbidden_runtime_imports`

The predecessor assertion currently requires:

`solve_household_steady_state`

That assertion is obsolete and conflicts with the already accepted source-postloop routing.

Replace only the route expectation so the test proves all of the following:

1. the driver contains and uses `solve_matlab_source_postloop_household`;
2. the driver does **not** call `solve_household_steady_state(`;
3. `run_online_stationary` remains present;
4. `solve_root` remains absent;
5. historical `chapter5_model` imports remain absent;
6. source controller constants/expressions already checked by the test remain unchanged.

Do not weaken, delete, xfail, skip, parameterize away, or broadly rewrite the test. Do not change unrelated assertions in the file.

The intended edit should be the smallest semantic correction consistent with the accepted driver.

Required marker after static inspection:

`MP4B_STALE_ENTRY_REGRESSION_CONTRACT_ALIGNED_WITH_ACCEPTED_SOURCE_POSTLOOP_ADAPTER`

## 6. Zero-science preflight rerun

After the test-only correction, rerun the same complete mandatory zero-science preflight bundle that previously returned `63 passed, 1 failed`.

The bundle must include the accepted checks for:

- direct-script bootstrap;
- fresh corrected-2009 presolver identity with semantic mismatch count `0`;
- all `24,800/24,800` first-turn source initialization cells;
- first-Beijing input semantic mismatch count `0`;
- source-postloop adapter routing/static acceptance;
- MP2 focused regression;
- all seven MP3 scenario contracts;
- online stationary-runtime focused regression;
- accepted raw-`Vb` household/export regression;
- final-state field-map/comparator-helper focused tests;
- stale entry test after remediation;
- clean-process/no-R5 dependency checks;
- `py_compile` for touched validation/test Python;
- `git diff --check`.

Use exactly the same regression selection represented by the predecessor's `63 passed, 1 failed` bundle unless a path/name resolution issue makes that impossible. Expected successful disposition is `64 passed`; if the selected test count changes unexpectedly, record the reason and stop BLOCKED rather than silently treating a narrower suite as equivalent.

No real model calls may be made by the tests. If any test unexpectedly invokes household/HJB/KFE/stationary science, stop.

Required marker only if the complete bundle passes:

`MP4B_SOURCE_POSTLOOP_ADAPTER_2009_STATIONARY_REEXECUTION_PREFLIGHT_PASS`

This marker means **preflight readiness only**. It does not authorize the stationary execution.

## 7. Scientific/model call ledger — all zero

All counts must remain exactly zero:

- Python stationary top-level;
- Python household adapter on real model inputs;
- Python HJB;
- Python KFE;
- Python household aggregation on real model inputs;
- turn-2 Shanxi replay;
- qualified comparator science;
- MATLAB stationary / household / HJB / KFE / presolver;
- MP2 / MP3 scientific execution;
- other year / annual batch;
- shocks / AR1 / transition / dynamics / IRF;
- historical R5;
- Results.

Reading/hashing the preserved MATLAB baseline and running zero-model schema/static tests are allowed.

Do not create a Python scientific stationary run root in this task.

## 8. Allowed repository changes

Allowed only:

- minimal edit to `tests/test_mp4b_python_empirical_entry.py` described in Section 5;
- one bounded report:
  `docs/CH5_TWO_ASSET_HANK_MP4B_STALE_ENTRY_REGRESSION_CONTRACT_REMEDIATION_AND_FULL_ZERO_SCIENCE_PREFLIGHT_REPORT.md`;
- optional bounded CURRENT roadmap status update recording the remediation/preflight result.

Do not modify:

- `validators/multi_province/mp4b_python_empirical.py`;
- `validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py`;
- final-state field map/helper;
- comparator contracts;
- any production/export source;
- MP2/MP3/stationary runtime;
- protected MATLAB;
- canonical data/cache/workbooks;
- project rules;
- historical R5.

## 9. Acceptance

PASS terminal:

`MP4B_STALE_ENTRY_REGRESSION_CONTRACT_REMEDIATION_AND_FULL_ZERO_SCIENCE_PREFLIGHT_PASS`

PASS requires:

- exact minimal stale-test remediation;
- `MP4B_STALE_ENTRY_REGRESSION_CONTRACT_ALIGNED_WITH_ACCEPTED_SOURCE_POSTLOOP_ADAPTER` established;
- complete preflight bundle passes with expected `64 passed` unless a fully explained non-narrowing count difference is independently evident;
- `MP4B_SOURCE_POSTLOOP_ADAPTER_2009_STATIONARY_REEXECUTION_PREFLIGHT_PASS` established;
- all scientific/model calls remain zero;
- all immutable identities remain unchanged.

BLOCKED terminal:

`MP4B_STALE_ENTRY_REGRESSION_CONTRACT_REMEDIATION_AND_FULL_ZERO_SCIENCE_PREFLIGHT_BLOCKED`

Use BLOCKED for any additional failing regression, unexpected test-count reduction, identity mismatch, or need to modify scientific/validation code beyond the single stale test contract.

## 10. Required report

Include at minimum:

1. terminal verdict;
2. live continuity;
3. stale test predecessor blob SHA;
4. exact before/after assertion diff;
5. explanation why this is test-contract remediation rather than scientific-code repair;
6. immutable identity table;
7. all zero-science preflight markers and artifact identities reused/recreated;
8. exact regression command/selection and count;
9. exact failing tests if any;
10. `py_compile` and `git diff --check`;
11. complete zero scientific/model call ledger;
12. Python scientific run-root existence check showing no root was created;
13. production/export/scientific-module mutation count;
14. changed paths;
15. forbidden-operation audit;
16. Git commit/push/read-back closeout;
17. exactly one recommended next gate.

## 11. Next-stage boundary

Even on PASS, do **not** run or automatically reauthorize stationary science within this task.

On PASS recommend exactly one next gate:

**a separately published one-shot Python-only corrected-calendar-2009 stationary reexecution using the already accepted source-postloop adapter and the same immutable MATLAB baseline. MATLAB rerun remains zero.**

That successor requires independent L3 review and a new live GitHub task authority.

## 12. Closeout

Explicit-path staging only. One execution commit. One non-force push. GitHub read-back every changed path. Require final:

- `HEAD == origin/main`;
- ahead/behind `0/0`;
- clean worktree;
- forbidden-operation audit PASS.
