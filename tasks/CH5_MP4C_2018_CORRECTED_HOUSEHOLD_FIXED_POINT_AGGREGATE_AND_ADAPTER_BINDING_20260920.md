# Task — corrected household fixed-point aggregate and adapter binding

Date: 2026-09-20

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_2018_CORRECTED_HOUSEHOLD_FIXED_POINT_AGGREGATE_AND_ADAPTER_BINDING_20260920`

## Governance

Owner is final scientific authority. ChatGPT is L3 independent Reviewer/scientific-route authority. Codex is bounded Builder.

GitHub live `main` is repository-state authority.

Absolute prohibition:

`zcx369658780/deep-learning-hank`

must never be entered, read, searched, used or modified.

Fresh-fetch live `origin/main`. Read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_CHECKPOINT11_TERMINAL_SOURCE_FREE_KFE_VALIDATION_ACCEPTANCE_20260920.md`
6. `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_END_TO_END_STATIONARY_DISTRIBUTION_AND_HOUSEHOLD_AGGREGATE_PARITY_REPORT.md`
7. `src/ch5_two_asset_hank/multi_province/household_adapter.py`
8. exact accepted checkpoint-11 policy/mass evidence.

No new scientific law is authorized.

## Objective

Close the zero-solver interface gap between the accepted corrected checkpoint-11 household fixed point and the multi-province household output contract.

The task must:

1. recover and source-map the exact stationary household aggregation semantics for `Ct`, `Lt`, `At`, `Bt`, total assets and `AtTax`;
2. bind exact checkpoint-11 policy fields and accepted stationary mass `p` / density view `g`;
3. compute exactly one deterministic aggregate receipt from those already accepted arrays;
4. implement the minimum opt-in corrected-household aggregate/adapter layer needed to expose the frozen multi-province output contract;
5. fixture-lock the adapter against the accepted checkpoint-11 object;
6. leave all existing source-faithful/default production and outer-loop routes unchanged.

This task is an interface/aggregation task, not a new HJB/KFE or outer-loop experiment.

## Exact accepted input authority

Checkpoint 11:

- V11 `A097A3DDA767B979224638A51CEDC53EA635687CCDEFBE190FED0B899606921F`
- P11 `89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3`
- u11 `2E9A077FFA809F2DECEE385FD9E7F50C03E16750C2A074F990C0F3CBCC212648`
- Q11 `33367258F3EADB1482D4A5CB30A64A8574830C993B0E5280C451499CBD6913AD`
- checkpoint identity `8093BE714CA83531816B20DFEB2BAB3DCB7AF9B971AD255C3596C1CA2A9E2A3B`.

Terminal mass evidence:

- evidence root `reports/ch5_mp4c_2018_kfe_d123_checkpoint11_terminal_source_free_kfe_validation_20260920_run001/`
- manifest `B7C06E3C369B6A5400DE76252DD70A539EFF1F2E4072C04639A1E93E512F5C1D`
- stationary mass artifact `1DD70201EAC5EED0AE768362D99A76736276BFB4D5E6AF0D8DBDB4E9D6FE7D16`
- p `E215FAE862DA81AD6DEB603859709EA0CF73B8F6F1897567DF942B186CD65ED7`
- g `D02592257722313B81C7A1DB40B799ADED8E8BDB5100A65C469E0997DA22E1CE`
- `omega=70/361`.

Bind these exactly before post-processing.

## Frozen core aggregate semantics

The accepted source audit already establishes the following stationary source objects:

- `Ct = sum(C .* g * da * db, all)`
- `Lt = sum(z .* l .* g * da * db, all)`
- `At = sum(a .* g * da * db, all)`
- `Bt = sum(b .* g * da * db, all)`
- total assets = `At + Bt`.

Because accepted `p = g * omega` and `omega=da*db` on this uniform grid, the equivalent mass-form reductions are:

- `Ct = sum(C * p)`
- `Lt = sum(z * l * p)`
- `At = sum(a * p)`
- `Bt = sum(b * p)`.

Use F-order `(b,a,z)`, b fastest. Do not introduce trapezoid weights, endpoint weights, dz weights or a second density normalization.

## AtTax mapping gate

`AtTax` is required by the existing multi-province output contract but is not part of the four core aggregate identities above.

Before implementing its corrected adapter field, recover the exact source expression and all required operands from the designated protected MATLAB source and/or already accepted source-mapping evidence.

Requirements:

- preserve exact source economic meaning;
- identify units and whether it uses raw/used illiquid return;
- identify whether it is an aggregate flow, tax base, or another diagnostic;
- bind every operand to the corrected household object.

If the exact AtTax source law cannot be recovered unambiguously, do not invent or approximate it. In that case:
- persist the four core aggregates and total-assets receipt;
- report `BLOCKED__ATTAX_SOURCE_MAPPING_REQUIRES_OWNER_OR_SOURCE_RECOVERY`;
- do not expose a false complete `FrozenHouseholdOutputs` adapter.

A failure of AtTax mapping does not invalidate the accepted HJB-KFE fixed point.

## Implementation boundary

Preferred new module:

`src/ch5_two_asset_hank/multi_province/corrected_household_adapter.py`

or an equivalently isolated new module.

Do not silently change `household_adapter.py`, `one_turn.py`, `stationary_runtime.py`, K1/C1/labor/firm code, or package defaults unless only an explicit non-default export is needed and byte-level default routing remains unchanged.

The new adapter must be opt-in and fixture-oriented. It must not invoke HJB/KFE internally in this task.

The adapter must accept explicit arrays/metadata; no hidden calibration defaults.

## Allowed deterministic post-processing

Exactly one accepted checkpoint-11 aggregate evaluation is authorized.

This is post-processing of already accepted arrays, not a new model solve.

Persist:

- input identity receipt;
- source formula map with source lines/evidence references;
- p/g equivalence checks;
- aggregate values;
- F-order array identities;
- AtTax mapping receipt;
- adapter fixture receipt;
- no-default-route-change attestation;
- manifest/readback.

## Solver/model budget

Maximum:

- HJB solves/updates: 0
- KFE/nullspace/SVD/eigen solves: 0
- policy maps/selectors/roots: 0
- Q/D2 assemblies: 0
- firm calls: 0
- wage/return calls: 0
- capital/labor allocation calls: 0
- outer-loop / steady-state / trajectory calls: 0
- MATLAB scientific calls: 0
- GE/annual/shock/IRF/welfare/Results: 0
- accepted checkpoint-11 aggregate post-processing evaluations: 1
- scientific retries: 0.

Static source reads, hashes, tests and serialization do not consume the model budget.

## Tests

Focused tests must cover at least:

- exact accepted artifact/provenance binding;
- p versus g*omega equivalence within prospective binary64 arithmetic bounds;
- F-order shape/orientation;
- aggregate mass-form versus density-form equivalence;
- no hidden/default solver call;
- no change to existing source-faithful/default routing;
- AtTax mapping contract if recovered;
- fail-closed behavior if AtTax mapping is unavailable or incomplete.

Do not test by running the outer model.

## Stop conditions

Stop immediately on:

- accepted artifact/provenance mismatch;
- p/g inconsistency beyond prospective arithmetic bounds;
- source aggregate semantic ambiguity affecting Ct/Lt/At/Bt;
- AtTax source ambiguity that would require inventing economics;
- attempted default production-route switch;
- unexpected model/solver invocation.

Do not repair scientific equations, payoff-return semantics, K1 coefficients, labor normalization, calibration or price units inside this task.

## Deliverables

Write:

`docs/CH5_MP4C_2018_CORRECTED_HOUSEHOLD_FIXED_POINT_AGGREGATE_AND_ADAPTER_BINDING_REPORT.md`.

Create a compact fresh evidence root under `reports/`.

Commit and ordinary non-force push one task branch. Do not merge main. Do not modify CURRENT files. Do not publish a successor.

Terminal PASS marker if all required fields including AtTax are closed:

`PASS__CORRECTED_HOUSEHOLD_FIXED_POINT_AGGREGATES_BOUND__OPT_IN_ADAPTER_FIXTURE_READY`.

If AtTax remains source-ambiguous:

`BLOCKED__ATTAX_SOURCE_MAPPING_REQUIRES_OWNER_OR_SOURCE_RECOVERY`.

Either outcome leaves Results eligibility `FALSE`.
