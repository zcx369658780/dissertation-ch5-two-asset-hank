# CH5 MP4C 2018 KFE D1-D3 corrected HJB Option A single policy-map/direct-step report

Date: 2026-09-16

Task: `CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_OPTION_A_SINGLE_POLICY_MAP_DIRECT_STEP_20260916`

## Verdict

`FAIL__OPTION_A_POLICY_MAP_FIRST_CELL_NOT_ADMISSIBLE__STOPPED_WITHOUT_RETRY`

The Owner-bound Option A run stopped at the first F-order cell, zero-based index `(b,a,z)=(0,0,0)`, after exactly one real selector evaluation and four scalar-root invocations. The selector returned `NO_ADMISSIBLE_POLICY`; the complete 12-candidate comparison receipt was persisted before termination.

Cells 2–800 were not executed. The full-map gate was therefore not satisfied, so D2 assembly and the sparse direct HJB solve were not called. No repair, alternate seed, retry, second policy map or nonlinear continuation was attempted.

This is a narrow one-step-input policy-map failure at the first Option A derivative state. It is not evidence of nonlinear HJB nonexistence, KFE failure, equilibrium nonexistence, production readiness or Results eligibility.

## Git identity and exact changed paths

- Fresh-fetched `origin/main`: `3425ec22027697e95ff220cdb142323113aed136`
- Branch: `codex/ch5-mp4c-2018-kfe-d123-corrected-hjb-option-a-single-policy-map-direct-step-20260916`
- Candidate SHA convention: the final candidate is the commit containing this report and evidence; its SHA is returned after non-force push and remote readback.
- Scientific-code Git HEAD before selector call 1: `3425ec22027697e95ff220cdb142323113aed136`; the exact uncommitted implementation identity is bound by the per-file SHA-256 freeze.

Exact changed paths:

- `src/ch5_two_asset_hank/corrected_diagnostic/option_a_step.py`
- `tests/test_mp4c_2018_kfe_d123_option_a_single_step.py`
- `reports/ch5_mp4c_2018_kfe_d123_corrected_hjb_option_a_single_step_20260916/cell_0000.json`
- `reports/ch5_mp4c_2018_kfe_d123_corrected_hjb_option_a_single_step_20260916/execution_ledger.json`
- `reports/ch5_mp4c_2018_kfe_d123_corrected_hjb_option_a_single_step_20260916/execution_summary.json`
- `reports/ch5_mp4c_2018_kfe_d123_corrected_hjb_option_a_single_step_20260916/manifest.json`
- `reports/ch5_mp4c_2018_kfe_d123_corrected_hjb_option_a_single_step_20260916/post_execution_freeze_check.json`
- `reports/ch5_mp4c_2018_kfe_d123_corrected_hjb_option_a_single_step_20260916/pre_execution_freeze.json`
- `reports/ch5_mp4c_2018_kfe_d123_corrected_hjb_option_a_single_step_20260916/preflight.json`
- `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_OPTION_A_SINGLE_POLICY_MAP_DIRECT_STEP_REPORT.md`

No frozen MATLAB/source-faithful path, accepted historical evidence, production integration, calibration, grid constant or Results material was changed.

## Exact Option A and frozen-input readback

| Object | Readback |
|---|---|
| Seed | `hjb100_initialization.mat:v0` |
| Seed path | `D:\ProjectTemp\ch5-mp4c-2018-call725-matlab-termination-replay-after-path-recertification-20260904-001\hjb100_initialization.mat` |
| Container | 13,362 bytes; SHA-256 `1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81` |
| `v0` field | shape `(20,20,2)`; F-order little-endian float64 SHA-256 `564B95B818713477691389903C3CFF72B5A7F991B924D52FBEB23D5A3675D665`; finite range `[-2.6471989790143082,-1.710759724165037]` |
| Scalar binding | 2,732 bytes; SHA-256 `A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6` |
| Liquid grid | field SHA-256 `A3FF663C18A2088A75B0E76C8ADA982EAF6D33ACFECB8DAA17C6D7DDE0533A76` |
| Illiquid grid | field SHA-256 `AE3A3A789FBC0DC9900B8153DEC717264C74AAB6FDA356C21C0EB22EEAC52567` |
| Productivity grid | field SHA-256 `A35F6FAB6E4564C6F4B1962A2ADE64E477F808432F747ABC7ACCF5E70B0B39B7` |

The driver bound the exact call-725 scalars, including `r_a=.09`, `r_b=.02`, borrowing gap `.07`, `tau=.05`, `w=16.82014806560587`, `T=.1`, `rho=.05`, `gamma_c=2`, `phi=5`, labor weight `1`, `chi_0=.1`, `chi_1=2`, `a_bar=1e-6`, `Delta=1000`, and the exact productivity generator `[[-1/3,1/3],[1/3,-1/3]]`. No price or calibration block was called.

## Implementation and preflight

The isolated driver implements only the task-authorized surface:

- Option A container/field/scalar/grid hash binding;
- raw forward/backward finite differences from `V0`;
- representation-only boundary carrier duplication with marker `UNUSED_BOUNDARY_SLOT_DUPLICATES_INWARD_RAW_DERIVATIVE`;
- exact F-order traversal with `b` fastest;
- one shared `SelectorBudget(800,264)`;
- atomic durable per-cell receipts and first-failure stop;
- full-map-only D2 gate, prospective coordinate-action bounds and at-most-one direct solve;
- complete scientific-call ledger and pre/post code-freeze hashes.

Preflight passed before selector call 1:

- focused tests: `4 passed`;
- `py_compile`: PASS;
- exact Option A file/field/scalar/grid readback: PASS;
- exact 800-cell F-order enumeration: PASS;
- all raw derivative fields finite: PASS;
- boundary adapter markers: 80 liquid-face cells and 80 illiquid-face cells, exact expected counts;
- static selector proof: lower faces select `forward`, upper faces select `backward`, and boundary axes use only `_inward_derivative` rather than interior alternatives;
- `git diff --check`: PASS.

The first ordinary CLI preflight launcher did not resolve the repository's `src` layout and exited before importing the module; it made no selector/root/model call and created no evidence. The successful preflight and sole scientific execution used an explicit `sys.path` pointing to this worktree's `src`. `ruff` was unavailable in the environment and was not an acceptance gate.

## Scientific-code freeze

Pre-execution freeze was durably written before selector call 1. The frozen new-code identities were:

- `src/ch5_two_asset_hank/corrected_diagnostic/option_a_step.py`: `081136C92D4A1C04ED0C2B011CB27799BACA207A3EC3E8A50AAEFE5209AD3F33`
- `tests/test_mp4c_2018_kfe_d123_option_a_single_step.py`: `10EC0CA632316522CF52E80EF7E382D04408C856CA7410775DD46EF0A8A8F390`
- accepted selector: `FC81DB9E72C005512116047D965FC08D3E39EBE703D7EF6F60DA54A56F39A58D`
- accepted generator: `F52451213E04EA999FE132B77AA92D1B66819B4D36BA5C539E9DD5EED4A63DB3`

The post-execution hash map matches the complete pre-execution scientific-code hash map exactly. No scientific code or focused test was edited after selector call 1.

## First failing cell and comparison receipt

Identity:

- F-order flat index: `0`
- zero-based coordinate: `(0,0,0)`
- state: `b=-2`, `a=0`, `z=.8`
- `V0=-2.6471989790143082`
- effective liquid return: `0.09000000000000001`
- effective illiquid return: `.09`
- net wage: `12.783312529860462`
- inward/raw derivatives: `p_b^F=0.023046602641887657`, `p_a^F=0`; unused backward carrier fields duplicate those inward values and are not additional candidates.

The selector evaluated all four geometric active sets crossed with the three transfer regimes: 12 comparison candidates, zero admissible policies, four counted scalar-root invocations.

| Active set | Negative | Zero kink | Positive |
|---|---|---|---|
| slack | lower-a primal/direction failure | transfer KKT residual | sign + lower-a primal/direction + KKT failures |
| lower-a | active-equality wrong transfer sign | transfer KKT residual | active-equality wrong transfer sign |
| lower-b | root failure: no unique bracket | root failure: no unique bracket | root failure: no unique bracket |
| lower-a + lower-b | active-equality wrong transfer sign | root failure: no unique bracket | active-equality wrong transfer sign |

For the slack zero-kink and active-lower-a zero-kink candidates, `g_a=0` and D2 face feasibility were satisfied, but the frozen transfer KKT interval was `[0.020741942377698892,0.025351262906076425]` while the candidate residual was `0.020741942377698892`; both were rejected by the accepted exact selector contract. The report records this receipt without changing its tolerance, KKT law or branch enumeration.

The complete durable comparison set is `cell_0000.json`, SHA-256 `4ECE066D3A276E751959429430CCE8C60D10FDE856FC3D1F32417270A7B7E266`, 18,088 bytes.

## Gates not reached

- Cells 2–800: `NOT_EXECUTED_AFTER_FIRST_CELL_FAILURE`
- complete 800-cell policy map: not obtained
- D2 assembly: not called
- D2 invariant/coordinate-action evidence: unavailable because the full-map gate failed
- sparse direct HJB solve: not called
- `V1`: not produced
- historical Cells 4/8/10 `V0/V1` derivative diagnostics: unavailable because no direct step occurred

## Exact call ledger

| Operation | Calls |
|---|---:|
| corrected policy maps started | 1 |
| real selector evaluations | 1 |
| scalar root invocations | 4 |
| passed cells | 0 |
| attempted cells | 1 |
| D2 generator assemblies | 0 |
| sparse direct HJB solves | 0 |
| selector evaluations on `V1` | 0 |
| nonlinear continuation iterations | 0 |
| adverse-numerics/scientific retries | 0 |
| KFE | 0 |
| MATLAB | 0 |
| outer | 0 |
| firm | 0 |
| wage/return recalculation | 0 |
| GE / annual / shock / IRF / Results | 0 |

All failed selector/root invocations are included. The launcher-only preflight path error is not a selector or model invocation.

## Evidence closure

Evidence root:
`reports/ch5_mp4c_2018_kfe_d123_corrected_hjb_option_a_single_step_20260916/`

The sealed manifest contains 6 entries totaling 27,005 bytes. It covers preflight, pre-execution freeze, the complete first-cell receipt, execution summary, call ledger and post-execution freeze check. Evidence was not overwritten or regenerated.

## Limitations and next gate

This result establishes only that the Owner-selected Option A raw derivative state at the first grid cell has no admissible policy under the frozen corrected selector as executed. It does not identify a new economic law, authorize a tolerance/KKT/root change, prove that another seed would pass, or establish corrected HJB/KFE/equilibrium nonexistence.

Results eligibility remains `FALSE`. Production paths remain unchanged. This Builder report does not merge `main` and does not publish a successor task. The next gate is independent Reviewer assessment of the frozen candidate and first-cell receipt.
