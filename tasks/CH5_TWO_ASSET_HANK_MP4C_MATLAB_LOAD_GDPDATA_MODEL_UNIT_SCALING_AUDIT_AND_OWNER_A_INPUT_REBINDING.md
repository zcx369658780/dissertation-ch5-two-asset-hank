# CH5_TWO_ASSET_HANK_MP4C_MATLAB_LOAD_GDPDATA_MODEL_UNIT_SCALING_AUDIT_AND_OWNER_A_INPUT_REBINDING

Date: 2026-09-03

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / MATLAB source auditor / unit-lineage analyst / input-only implementer

Owner: final scientific authority

## 1. Authority basis and Owner concern

Immediate predecessor execution:

`e12abaae0d57c85b5eb20693fd4d7d7ad18ca8b9`

The predecessor completed the 13-pass comparison package and 2018 KFE-singularity forensic without new model execution.

The Owner now raises a potentially material scientific-input concern:

> In the original MATLAB annual data preparation, especially `load_GDPdata.m`, GDP, population/employment, and capital were intentionally rescaled to smaller model units (for example 万人 / 亿元 or related reduced units). The current Python Owner-A path may have inherited the R/PLM estimation multipliers rather than the MATLAB runtime model-unit transforms.

This concern is scientifically plausible and must be resolved from source and numeric provenance before any further 2018 diagnosis or annual rerun.

The current Python Owner-A code visibly materializes model inputs as:

- GDP = workbook level × `gdp_multiplier`;
- CAP = workbook level × `gdp_multiplier`;
- POP = workbook level × `pop_multiplier`;

with current accepted scalar values `gdp_multiplier=1000`, `pop_multiplier=100`.

That current behavior is **not accepted as correct merely because it exists in Python**. The task must determine whether those factors and directions match the historical MATLAB runtime model-unit contract.

## 2. Core objective

Determine, with source and numeric proof, the exact end-to-end MATLAB model-unit transformations for:

- GDP / `Yt0`;
- capital / `Kt0`;
- employment or population / `Lt0` / `N`;
- any logged per-capita variables built from them;
- any output-side inverse transform used when writing `12年稳态值.xlsx`.

Then compare that exact contract against the current Python Owner-A input path.

If and only if a deterministic mismatch is proven and the correct transform is uniquely identified, prepare the smallest input-only Python correction and zero-science regression tests.

**No HANK scientific rerun is authorized in this task.**

## 3. Required live continuity

At start:

1. `git fetch origin`;
2. require this exact task live on `origin/main` as direct child of `e12abaae0d57c85b5eb20693fd4d7d7ad18ca8b9`;
3. require `HEAD == origin/main`, ahead/behind `0/0`;
4. require clean tracked worktree;
5. read completely:
   - `AGENTS.md`;
   - `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
   - every CURRENT rule named by the index;
   - the Owner-A 2009–2022 task/report;
   - the 13-pass comparison/2018 forensic task/report;
   - corrected-2009 same-input parity acceptance;
   - current `mp4c_owner_a_2009_2022.py`;
   - current `mp4c_python_annual_empirical.py`;
   - current `mp4c_matlab_runtime_cache.py`;
   - current annual production worker and output serializer.

## 4. Protected MATLAB source discovery

Resolve the actual current MATLAB source root. Expected candidate:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Do not assume the path if the file tree proves otherwise.

Locate and hash at minimum:

- `load_GDPdata.m`;
- `multi_prov_HANK_12sts.m`;
- the function/file containing `mpHANK_equilibrium_2000`;
- `HANK_mp_1eq.m`;
- `HANK_mp_1turn.m`;
- any helper called by `load_GDPdata.m` that reads or rescales GDP/CAP/POP/employment;
- the code that writes or assembles `12年稳态值.xlsx` if separate;
- the processed runtime cache `数据估计结果_1000_100_0.mat`.

Record SHA-256 and physical/logical path provenance.

Protected MATLAB source is read-only. Do not edit it.

## 5. Phase A — exact MATLAB multiplier/source audit — ZERO SCIENCE

No MATLAB model call, Python stationary call, household/HJB/KFE call, or R/PLM execution is allowed.

### 5.1 `load_GDPdata.m` literal audit

Read the full file, not snippets.

Extract every literal and expression relevant to:

- `GDP_multiplier`;
- `POP_multiplier`;
- any `CAP_multiplier` or reuse of GDP multiplier for capital;
- any division or multiplication by 10, 100, 1000, 10000, 1eN;
- unit comments such as 元/万元/亿元/人/万人;
- construction of GDP, CAP, POP/employment arrays;
- construction of `log_pgdp`, `log_pcap`;
- storage of those variables into `data_MAT`, `mydata2`, or cache structures.

For each field, state the transform as a mathematical expression:

`model_value = source_workbook_value × factor`

where `factor` is signed/positive and explicit.

Do not infer direction from variable names such as `multiplier`; inspect the arithmetic operator actually used.

### 5.2 Separate R-estimation units from MATLAB-runtime units

The recovered `D:\Rprogramme\main.r` uses its own PLM/calibration multipliers.

Do NOT assume those are the same as MATLAB runtime model units.

Create two separate contracts:

- `R_ESTIMATION_UNIT_CONTRACT`;
- `MATLAB_RUNTIME_MODEL_UNIT_CONTRACT`.

If they differ, this must be stated explicitly and treated as a source-design distinction, not silently reconciled.

### 5.3 Workbook -> cache numeric proof

Use the protected workbooks and processed cache read-only.

For multiple provinces and multiple years, including at least:

- Beijing;
- Henan;
- Guangdong;
- Tibet;
- Xinjiang;

and at least three calendar rows spanning early/middle/late available data, compare raw workbook cells against cache fields:

- GDP;
- CAP;
- POP;
- log_pgdp;
- log_pcap;
- cache `GDP_multiplier`;
- cache `POP_multiplier`.

Infer nothing from comments alone. Numerically prove the actual transformation used by the cached MATLAB runtime data.

Where the historical cache uses a different capital sheet from Owner-A, keep **unit transformation** and **capital provenance** as separate dimensions.

### 5.4 Cache -> MATLAB state audit

Trace exact values from cache/data objects into MATLAB state fields before the first household call:

- `Yt0`, `Yt`;
- `Kt0`, `Kt`, `Kt_prev`;
- `N`, `Lt`, `Lt_prev`;
- `GovInv` if it inherits capital units.

Determine whether additional scaling occurs after `load_GDPdata.m` / cache generation.

### 5.5 MATLAB state -> workbook output audit

Trace how final MATLAB states are written to:

`12年稳态值.xlsx`

for:

- `Yt0`, `Yt`;
- `Kt0`, `Kt`;
- `Lt0`, `Lt`.

Determine whether the output writer divides/multiplies by the same factors to restore display units.

This is critical: output-unit conversion must not be confused with model-runtime scaling.

## 6. Phase B — audit current Python unit semantics — ZERO SCIENCE

Inspect exact current Python source.

At minimum audit:

- `validators/multi_province/mp4c_python_annual_empirical.py::accepted_source_scalars`;
- `validators/multi_province/mp4c_owner_a_2009_2022.py::build_input`;
- `entry_states`;
- `validators/multi_province/mp4c_matlab_runtime_cache.py`;
- `validators/multi_province/mp4c_python_annual_production.py`;
- any legacy-workbook serialization path.

Freeze the current Python behavior field by field:

`workbook -> canonical runtime input -> entry state -> final model state -> legacy workbook-compatible export`.

In particular verify the current code path that uses:

- GDP ×1000;
- CAP ×1000;
- POP ×100;

and the later divide-back in `legacy_workbook_rows`.

Do not assume this is correct; compare to MATLAB source proof.

## 7. Required unit-contract verdict

For each of GDP, CAP, POP/employment, classify exactly one:

- `PYTHON_UNIT_TRANSFORM_EXACTLY_MATCHES_MATLAB_RUNTIME`;
- `PYTHON_UNIT_TRANSFORM_INVERTED_RELATIVE_TO_MATLAB_RUNTIME`;
- `PYTHON_UNIT_TRANSFORM_MISSING_FACTOR`;
- `PYTHON_UNIT_TRANSFORM_EXTRA_FACTOR`;
- `PYTHON_UNIT_TRANSFORM_FIELD_SOURCE_DIFFERS_BUT_UNIT_FACTOR_MATCHES`;
- `UNIT_TRANSFORM_PROVENANCE_UNRESOLVED`.

Also provide the exact numeric source-to-model factors for both languages.

If any field remains unresolved, STOP before patching.

## 8. Conditional input-only correction authority

The Owner authorizes a correction **only if** the preceding audit uniquely proves that current Python Owner-A model units differ from the MATLAB runtime contract.

If no mismatch is proven:

- make no scientific/input patch;
- terminal classification must say scaling is confirmed or unresolved;
- do not rerun.

If a mismatch is proven:

1. preserve all historical Owner-A input/output evidence unchanged;
2. create a new explicit representation name; do not silently mutate the semantic meaning of previously archived inputs;
3. separate R-estimation scalars from MATLAB-runtime model-unit factors in code/naming;
4. change only input scaling/materialization and directly required serialization metadata;
5. do not change equations, HJB/KFE, grids, calibration, controller logic, calendar binding, capital provenance, PLM vintage mapping, migration, firm, monetary or fiscal code.

Prefer explicit factor names such as:

- `gdp_source_to_model_factor`;
- `capital_source_to_model_factor`;
- `employment_source_to_model_factor`;
- `model_to_legacy_output_factor`.

Avoid ambiguous reused names if they obscure direction.

## 9. Zero-science rematerialization tests

If correction is required, materialize corrected **inputs only** for:

- 2009;
- 2015;
- 2018;
- 2022.

No stationary/HJB/KFE calls.

For all four years verify:

- 31 provinces exact;
- calendar/rolling/PLM indices unchanged;
- Owner-A capital provenance unchanged (`R语言计算资本存量`);
- source workbook hashes unchanged;
- source-to-model unit factors exact;
- log fields recomputed from corrected model-unit levels;
- inter-province asset ratio unchanged under common positive CAP/POP scaling when mathematically invariant, or explain any non-invariance;
- 2023 excluded.

Also compare corrected 2009 model-level GDP/CAP/POP against the closest source-proven MATLAB runtime model-unit construction available. Report exact differences and explain any residual difference due to Owner-A capital/population provenance rather than units.

## 10. Relationship to 2018 KFE failure

Do not rerun 2018.

If scaling mismatch is proven, state only:

`2018_KFE_SINGULARITY_MAY_HAVE_BEEN_REACHED_UNDER_A_MIS-SCALED_RUNTIME_INPUT__CAUSALITY_NOT_TESTED`

Do not claim the scaling caused or fixes the singularity without a new authorized scientific run.

If scaling matches MATLAB exactly, preserve the existing 2018 KFE blocker unchanged.

## 11. Required evidence root

Use a fresh no-overwrite root, preferred:

`D:\ProjectTemp\ch5-mp4c-matlab-load-gdpdata-unit-scaling-audit-20260903-001`

Required evidence at minimum:

- `matlab_source_identity_manifest.json`;
- `load_GDPdata_full_source_copy_or_hash_receipt.txt` (hash receipt sufficient if source copying is disallowed);
- `matlab_unit_transform_literal_audit.md`;
- `matlab_workbook_to_cache_numeric_scaling_audit.csv`;
- `matlab_cache_to_entry_state_unit_lineage.md`;
- `matlab_state_to_steady_workbook_output_unit_lineage.md`;
- `r_estimation_vs_matlab_runtime_unit_contract.md`;
- `python_current_unit_contract.md`;
- `matlab_python_unit_contract_comparison.csv`;
- `unit_scaling_verdict.json`;
- corrected-input previews/tests if and only if a mismatch is proven;
- `zero_science_execution_ledger.json`;
- `audit_manifest.json`.

## 12. Test requirements if code is patched

Run only zero-science focused tests.

At minimum:

- unit-transform literal tests;
- source workbook -> canonical level tests;
- model-to-legacy-output inverse-transform tests;
- 2009/2015/2018/2022 input materialization tests;
- province-axis tests;
- no-2023 tests;
- `py_compile`.

All tests must prove no scientific solver function is called.

## 13. Strict prohibition on scientific rerun in this task

Exact scientific execution budget:

- Python stationary: `0`;
- household: `0`;
- HJB: `0`;
- KFE: `0`;
- MATLAB model: `0`;
- R/PLM: `0`;
- 2018 retry: `0`;
- shock/IRF/R5/Results: `0`.

This task is intentionally an audit-and-input-rebinding gate. A new live task will authorize the bounded rerun after L3 reviews the exact multiplier direction and any patch.

## 14. Terminal classifications

If current Python units exactly match MATLAB runtime units:

`MP4C_MATLAB_LOAD_GDPDATA_UNIT_SCALING_AUDIT_PASS__PYTHON_OWNER_A_RUNTIME_UNIT_CONTRACT_CONFIRMED__NO_PATCH__NO_SCIENTIFIC_RERUN`

If a precise mismatch is proven and an input-only correction is prepared/tested:

`MP4C_MATLAB_LOAD_GDPDATA_UNIT_SCALING_DEFECT_PROVEN__OWNER_A_INPUT_ONLY_REBINDING_PREPARED_AND_ZERO_SCIENCE_TESTED__RERUN_NOT_YET_AUTHORIZED`

If provenance is insufficient:

`MP4C_MATLAB_LOAD_GDPDATA_UNIT_SCALING_PROVENANCE_UNRESOLVED__NO_PATCH__NO_RERUN`

## 15. Required repository report

Write:

`docs/CH5_TWO_ASSET_HANK_MP4C_MATLAB_LOAD_GDPDATA_MODEL_UNIT_SCALING_AUDIT_AND_OWNER_A_INPUT_REBINDING_REPORT.md`

One bounded commit/push may include only:

- audit/report utilities;
- input-only correction code if and only if mismatch proven;
- focused zero-science tests;
- the required report.

Do not commit local MATLAB source, workbooks, caches, or scientific output artifacts.
