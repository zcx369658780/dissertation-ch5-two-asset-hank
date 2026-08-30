# MATLAB-faithful HJB comparator NumPy scalar serialization correction and closeout report

## Terminal classification

`MATLAB_FAITHFUL_HJB_COMPARATOR_NUMPY_SCALAR_SERIALIZATION_CORRECTION_AND_CLOSEOUT_MATERIAL_MISMATCH`

The serializer-only correction succeeded and the one replacement comparator persisted a valid result. The unchanged frozen comparison rules reported numerical and sparse-pattern/value mismatches. No tolerance or scientific source was changed after the result, and the unaccepted faithful HJB candidate sources were restored before reports-only publication.

## Live GitHub continuity and predecessor capture

- Pre-fetch local HEAD: `1285abfac4548743f8b7f15a7e59923118c32120`.
- Successor authority: `044287b716b8f61941fd2b8a619adb5465d40a60`, the direct child of `1285ab...`; its only changed path was the successor task.
- `git merge --ff-only origin/main` succeeded without cleaning, stashing, resetting, or overwriting the four predecessor paths.
- Freeze: `PREDECESSOR_DIRTY_WORKTREE_CAPTURED_BEFORE_SUCCESSOR_AUTHORITY_SYNC`.
- Fresh no-overwrite artifact root: `D:\ProjectTemp\ch5-hjb-comparator-serialization-closeout-20260830-001`.
- Captured status/name-status/full patch/path/hash artifacts: `1891D13D...387D2`, `9F10FE16...C248`, `7EEE8E46...62677`, `73C07D25...7F24`, `66F96053...23D8`.
- The captured dirty set was exactly the predecessor report plus `matlab_faithful_policy.py`, `matlab_faithful_hjb.py`, and `matlab_faithful_operator.py`.
- Predecessor BLOCKED report SHA-256: `544057B338BB540CAA0DF413BBC93D7E9F79099ED3BAEDD33A7DA72C9F65EBBB`; it remained byte-unchanged and is published for provenance.
- Candidate source hashes preserved before restoration: policy `D8A595B9...F8C2`, HJB `92483136...F1DE`, operator `0C9F6C1A...1AAC`.

## Frozen predecessor scientific evidence

- Corrected MATLAB evaluator: `F6D33348329D242AC3C7D867D455DDD0B87184C00A5AD66332A1B62F359599FE`.
- MATLAB output: `52CE922D7960AB77D87A226747B0B79A29AFAD0C6B9759C7A81AD937CB7E73BF`; converged, 12 iterations, statistic `9.076792650830612e-10`.
- Python output: `A33EEA2F7A1698624EC4F773FFE42C2BF88B255F9C231960E8C182ECA2C870AB`; converged, 12 iterations, statistic `9.07700581365134e-10`.
- Frozen comparator: `4471CCC837A66245DCB8D2CA1D45F1BD79CBEE5EAE80874B14933E06C75F9A92`.
- Manifest/order/initialization/tolerances: `784ADA48...F6C7A`, `52EB9943...2926D`, `C6662095...52A9F`, `915B3539...EF72D`.
- Predecessor ledger: `156398C89EB72F60C331CA01EBC3F09246E11114205BA34EFC728A4D252E1CBE`, recording MATLAB/Python/comparator `1/1/1`.

No MATLAB or Python HJB was rerun in this successor.

## Comparator failure audit and correction

The predecessor exception was `TypeError: Object of type int64 is not JSON serializable`. The exact object was `numpy.int64` from an unconverted mismatch `worst_index` tuple. Failure occurred at the final `json.dumps(result, ...)` persistence expression, after all field, tolerance, categorical, ordering, sparse-pattern/value, mismatch accumulation, and `PASS`/`MATERIAL_MISMATCH` aggregation logic had executed.

Classification: `COMPARATOR_NUMPY_SCALAR_JSON_SERIALIZATION_ONLY`.

The corrected comparator was created separately; the predecessor comparator was not overwritten. Its only behavioral change is a JSON `default=` callback that returns `obj.item()` for `np.generic` and raises `TypeError` otherwise. Every changed line is classified `COMPARATOR_JSON_SERIALIZATION_TYPE_NORMALIZATION_ONLY`. No ndarray conversion was added.

- Corrected comparator: `615D4FC8C17D3909A8F733555C160C2EC344EFD6C1C7B243F9D2FDB5E5611CAD`.
- Exact diff: `1CDA49E3190D4DCD5044B7711E1502B27FCE01641E7D4982724ACD8C16C185AD`.
- Static audit: `08CD2D4C9D4457D05CE1BE5C87EE59DB9833918D552C719656ADAE31701210E8`.
- Freeze manifest: `1317DA422BA4CD8F6576BC85C240E948C1F8C250B4441724221BD07BFF59A73D`.
- Exactly one no-science preflight: `COMPARATOR_SERIALIZER_PREFLIGHT_PASS`; result hash `56ED62E10F6C84A2576D1ACF75A77EE07B23B642AA9441B99AF2EF2CCA837275`.
- Preflight proved native int/float/bool preservation, identical `np.int64` value, unchanged payload result/field structure, and fail-closed ndarray handling.

## Replacement comparator and complete parity result

- Successor calls: MATLAB HJB `0/0`; Python HJB `0/0`; replacement comparator `1/1`.
- Persisted comparison SHA-256: `F04B66152ED02E993020B76F01C65CD9BE6E8D2793159F037FEAA64EFE648836`.
- Comparator terminal: `MATERIAL_MISMATCH` (native exit `2`).
- Grid `a/b/z`, initialization, convergence boolean, iteration count, liquid labels, and transfer labels: PASS/exact.
- `V`: PASS, maximum difference `2.0961010704922955e-13` against absolute `1e-7`.
- Consumption: PASS, `2.7644553313166398e-14` against local bound `2.842170943040401e-14`.
- Adjustment cost: PASS, `1.8193779816044753e-14` against `2.842170943040401e-14`.
- Effective illiquid return: PASS, exact.
- Bswitch: exact pattern and values, `100/100` stored entries.

Array mismatches under the unchanged `128*eps64*max(...)` direct bound:

| Field | Maximum difference | Bound at worst | Worst index |
|---|---:|---:|---|
| labor | `6.661338147750939e-14` | `3.3853969187746126e-14` | `[0,1,1]` |
| transfer | `7.16093850883226e-14` | `2.842170943040401e-14` | `[4,3,1]` |
| mu_a | `7.16093850883226e-14` | `2.842170943040401e-14` | `[4,3,1]` |
| mu_b | `1.1934897514720433e-13` | `2.842170943040401e-14` | `[0,1,1]` |
| utility | `1.0746958878371515e-13` | `4.8839464585583654e-14` | `[0,1,1]` |

Sparse mismatches:

| Operator | Pattern | MATLAB/Python nnz | Maximum value difference |
|---|---|---:|---:|
| iteration BB | mismatch | `96/97` | `Infinity` |
| iteration AAH | mismatch | `110/120` | `Infinity` |
| iteration A | exact | `217/217` | `5.098144129078719e-13` |
| post BB | exact | `89/89` | `4.773959005888173e-13` |
| post AAH | mismatch | `80/90` | `Infinity` |
| post A | exact | `179/179` | `4.773959005888173e-13` |

Categorical mismatch count is zero. Complete mismatch list contains exactly 11 fields: `labor`, `transfer`, `mu_a`, `mu_b`, `utility`, iteration `BB`, iteration `AAH`, iteration `A`, post `BB`, post `AAH`, and post `A`. Source/environment failure list is empty for the replacement comparator.

## Closeout and acceptance

Because the result is MATERIAL MISMATCH, all three unaccepted faithful scientific source paths were restored to live task-authority state after their full patch and hashes were preserved. Repository publication contains reports only:

- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_SOURCE_EXTRACTED_BOUNDARY_ASSEMBLY_CORRECTION_AND_REPLACEMENT_PARITY_REPORT.md`;
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_HJB_COMPARATOR_NUMPY_SCALAR_SERIALIZATION_CORRECTION_AND_CLOSEOUT_REPORT.md`.

Acceptance level: serializer correction and persisted comparison evidence only. Neither `MATLAB_FAITHFUL_HJB_SOURCE_EXTRACTED_BOUNDARY_ASSEMBLY_CORRECTION_AND_REPLACEMENT_PARITY_PASS` nor `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HJB_OPERATOR_PARITY_ACCEPTED` is frozen. The PASS-only stationary KFE next gate is not authorized and no next scientific gate is recommended.

The reports are explicitly staged, committed once, pushed once without force to `main`, read back from live GitHub, and the closeout requires `HEAD == origin/main` with a clean worktree.
