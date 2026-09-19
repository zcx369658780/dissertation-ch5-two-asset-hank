# CH5 MP4C 2018 KFE D1-D3 V3 cell100 lower-b negative forward-a pre-screen repair and checkpoint-3 reexecution

Date: 2026-09-19

Task: `CH5_MP4C_2018_KFE_D123_V3_CELL100_LOWER_B_NEGATIVE_FORWARD_A_PRE_SCREEN_REPAIR_AND_CHECKPOINT3_REEXECUTION_20260919`

## Terminal classification

`COMPLETE_CHECKPOINT3_NONCONVERGED__STOP_BEFORE_V3_TO_V4`

The narrow active-lower-b / negative-transfer viability-filter defect was repaired without changing the frozen root, KKT, D1/D2/D3, switching, grid, calibration, or convergence laws. The single authorized accepted-V3 map completed all 800 cells, Q3 passed D2, and one checkpoint-3 evaluation completed. Primary convergence failed, no exact cycle was found, and checkpoint 3 has no authorized approximate period-2/3 window. Execution stopped before V3 to V4.

Results eligibility remains `FALSE`.

## Git and frozen input binding

- fresh live-main baseline: `3b3193607b72e0648c886f7fef52ca31f04a38d4`;
- task branch: `codex/ch5-mp4c-2018-kfe-d123-v3-cell100-lower-b-negative-forward-a-prescreen-repair-20260919`;
- scientific execution-head / implementation freeze commit: `b53c813b3c3052da9e82b1f2cba999524ed1f4ab`;
- accepted V3: `4FDB36C17ACDC60B56661AEE1C0437B65EC4A871FD4E5E08A9A996FB10EF85EF`;
- accepted V2-to-V3 artifact: `17F330AB0A226EE826880039055B9EA16FB93DD7B02F36F820D078178C6E4CCF`;
- accepted continuation sealed manifest: `9F772B9CEF73E15F0443952B25989BB6D644D73B9E04CB93B5AD047E1FBB7700`, all 113 entries read back;
- worktree was clean immediately before evidence creation;
- pre/post scientific-code freeze matched exactly; repaired selector SHA-256 was `0FB23B04182DCF9FF98ECCABF9443339F7BC372F3A161F0C880067D2F43CA1AD`;
- V2-to-V3 was not rerun.

The prohibited `zcx369658780/deep-learning-hank` repository was not entered, read, searched, used, or modified.

## Minimal repair

Only the active lower-b / negative-transfer pre-screen was changed. Each distinct authority-backed one-sided interior-a derivative branch is now represented directly, rather than allowing the 513-point unbounded log sampling grid to be treated as proof of branch nonexistence. All existing root, sign, direction, KKT, domain, finite-value, and Hamiltonian gates remain responsible for admissibility.

Upper-b logic and lower-b positive/zero-kink logic were unchanged. No tolerance, derivative floor, clipping, optimizer, widening, retry, or cell-specific scientific condition was added.

## Focused engineering gate

Before scientific entry:

- focused pytest suite: `73 passed`, `0 failed`, `0 errors`, `0 skipped`;
- JUnit SHA-256: `2D1054383ABA1C723BFEDE8332EDA11E591AA0253D97B42053807A82AC4C7580`;
- `py_compile`: PASS;
- `git diff --check`: PASS.

Coverage included exact V3 cell100 branch completeness and legal-root checks; unchanged V2 cell100 interior-a selection; prior lower-b completeness; unchanged upper-b domain filtering; positive active no-root behavior; liquid-Z, interior-a, joint, lower-a zero-kink, D1/D3/KKT and D2 zero-drift contracts; accepted-V3 binding; and zero HJB-update ledger enforcement.

## Exact V3 cell100 receipt

At F-order flat index 100, `(i_b,i_a,i_z)=(0,5,0)` and `(b,a,z)=(-2.0,2.6315789473684212,0.8)`, both active-lower-b negative branches were represented and used the unchanged scalar-root path.

| a branch | root | q_b | q_a | d | g_b | g_a | admissible |
|---|---|---:|---:|---:|---:|---:|---|
| backward | `ROOT_CONVERGED` | 0.012942099013665916 | 0.012088089476579748 | 0.04475402367270802 | 0 | 0.281595985582946 | no |
| forward | `ROOT_CONVERGED` | 0.012803445679273433 | 0.01134140574122853 | -0.018672540299433545 | 0 | 0.21816942161080446 | yes |

The forward-a root lies strictly inside the frozen legal interval `(0.012601561934698366, 0.015751950034835593)`, has negative transfer and forward-a-consistent positive drift, and has no rejection reasons. It is the selected cell100 policy. The backward candidate is rejected by the unchanged negative-transfer sign, a-direction, and transfer-KKT gates.

## Complete checkpoint 3

- P3 identity: `06062946687922E1FAC83E8D4B1B19101469CC284339522595A19F4DECB6B07B`;
- u3 identity: `9BB321A63A92154D4B733B28126AF29DC1441B95D44517D884F4C858AECFE6F4`;
- Q3 artifact: `4085E0D1B166E72650CA1E74E5CF9462F6677EEAFA8CDEF1FBD153F14088C255`;
- Q3 data/indices/indptr: `13CA224BF05EADD453078A6A6A54A87EADC0C76C4753A0577703298C1767A521` / `AFB69E0EF55C1E8CEBAF4040485297B8CAE211F85451AC4B89E9B27CED97FBD0` / `BC95DE3B2915B44B63AEC514B67F12005964891E1E78AAB43C6FD38370ABA495`;
- checkpoint-3 identity: `0DEEF7E54C4972BFF7BB67AE6B67BA5E54B588F3EEF5ACDE85048F3E02FE715D`;
- checkpoint arrays: `B4024EC1202533982BAF9C893F946D20B871B76B3BD369DD4F19B34BF1DD99BD`.

D2 passed:

- minimum off-diagonal: `1.39283511802249e-06`;
- exact diagonal-construction error: `0`;
- `max|Q3*1|=1.09356967925578e-14` within arithmetic tolerance `2.09649945489923e-13`;
- all coordinate-action and closed-face gates passed.

Checkpoint metrics:

- `B3=0.1291770476282596 > 1e-8`;
- `D3=0.05315900863346279 > 1e-7`;
- primary convergence: FAIL;
- exact-cycle recurrence: none;
- approximate period-2/3: not evaluated because neither complete window exists at checkpoint 3;
- policy identity changes versus P2: `800`;
- `||Q3-Q2||_inf=235.37818742999917`;
- maximum absolute Q-entry change: `117.04342704246497`;
- Q difference nnz: `2520`; sparsity pattern changed.

Switching statistics: 47 interior-a candidate attempts, 23 admissible and 21 selected; one joint candidate, admissible and selected at flat index 245; 39 liquid-Z selections. These are diagnostics only.

## Exact scientific ledger

| Operation | Calls |
|---|---:|
| accepted V0/V1/Q1 loads | 1 / 1 / 1 |
| accepted V2/P2/u2/Q2/checkpoint-2 loads | 1 / 1 / 1 / 1 / 1 |
| accepted V3 loads | 1 |
| V2 policy-map / Q2 assembly reruns | 0 / 0 |
| V2-to-V3 reruns | 0 |
| fresh V3 policy-map attempts | 1 |
| selector evaluations | 800 |
| total scalar-root invocations | 395 |
| liquid-Z root invocations | 137 |
| interior-a switching root invocations | 1 |
| joint-switching root invocations | 1 |
| Q3/D2 assemblies | 1 |
| checkpoint-3 evaluations | 1 |
| direct HJB solves / HJB updates | 0 / 0 |
| graph/SCC/topology gates | 0 |
| KFE/SVD/eigen/nullspace/`Q.T@p` | 0 |
| scientific retries / solver substitutions | 0 / 0 |
| damping/relaxation/adaptive Delta/continuation | 0 |
| parameter continuation/clipping/artificial diffusion | 0 |
| MATLAB/production/outer/firm/GE/annual/shock/IRF/Results | 0 |

## Durable evidence and changed paths

Fresh no-overwrite evidence root:

`reports/ch5_mp4c_2018_kfe_d123_v3_cell100_lower_b_negative_forward_a_prescreen_repair_checkpoint3_reexecution_20260919_run001`

- sealed-manifest schema: `CH5_D123_V3_CHECKPOINT3_REEXECUTION_V1`;
- sealed entries: `815`;
- sealed bytes: `13,308,005`;
- sealed-manifest SHA-256: `01FB50C300936B76F7C56CBD0BBFDF8A91ABFDDF5180FE5AB77FA7341DD8D1F6`.

Changed paths are limited to:

- `src/ch5_two_asset_hank/corrected_diagnostic/selector.py`;
- `src/ch5_two_asset_hank/corrected_diagnostic/v3_checkpoint3_reexecution.py`;
- `tests/test_mp4c_2018_kfe_d123_lower_b_active_negative_backward_a.py`;
- `tests/test_mp4c_2018_kfe_d123_v3_checkpoint3_reexecution.py`;
- the fresh evidence root above;
- this report.

No CURRENT file was modified. Main was not merged and no successor task was published.
