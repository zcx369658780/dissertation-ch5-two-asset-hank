# CH5 MP4C 2018 KFE D123 interior-a zero-drift switching implementation and V2 checkpoint-2 reexecution

Date: 2026-09-19

Task: `CH5_MP4C_2018_KFE_D123_INTERIOR_A_ZERO_DRIFT_SWITCHING_IMPLEMENTATION_AND_V2_CHECKPOINT2_REEXECUTION_20260919`

## Terminal classification

`FAIL__ADOPTED_INTERIOR_A_SWITCHING_V2_MAP_FIRST_FAILURE`

The Owner-adopted corrected-diagnostic interior-`a` zero-drift switching law was implemented and passed the complete focused engineering gate. The sole authorized accepted-V2 policy-map attempt then selected the new switching candidate at cell100 and continued without retry. The first subsequent failure was flat F index 185, where the frozen selector returned `NO_ADMISSIBLE_POLICY`. Execution stopped immediately. No Q2/D2 assembly, checkpoint-2 Bellman evaluation, HJB update, terminal topology/KFE work, MATLAB or downstream work occurred.

Results eligibility remains `FALSE`.

## Git and authority binding

- Fresh live-main baseline: `869f4023ae7b674d483f926f85e0de271479da0e`.
- Task branch: `codex/ch5-mp4c-2018-kfe-d123-interior-a-zero-drift-switching-implementation-v2-checkpoint2-20260919`.
- Worktree started clean and `0 ahead / 0 behind` live `origin/main`.
- Implementation/helper/test freeze commit used for the scientific run: `243548e062269b70a2b1905106765b6575d55253`.
- Accepted V2 field SHA-256: `A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.
- Pre-adoption selector SHA-256: `DBEB8EDCDA18B14579F36C2B68A50A47C9E717F49E84BC31A2E4E17180E9C327`; baseline Git blob `eac9b06805e2bcb69e078fd927a9a641c6cafd96`.
- Implemented selector SHA-256: `3175FBBC99120A9735287594A27602205505048BADD11A989CEAC682BE6390D8`.
- Owner-adoption document SHA-256: `F5C4515078BBFFE32F9924758AF2DC5DD1C344A86DEB3EB596AFF91106F2FD95`.
- Post-execution scientific-code freeze matched the pre-execution freeze exactly.
- `deep-learning-hank` was never entered, read, searched, used or modified.

## Implemented scope

Only the corrected-diagnostic route changed. The selector now:

1. evaluates the ordinary one-sided candidates first;
2. pairs backward/forward `a` candidates only within the same liquid branch, active set and transfer regime;
3. requires a strict arithmetic-bound-separated backward-positive/forward-negative `g_a` crossing at an interior `a` node;
4. fixes `d_Z=-r_a a`, derives the smooth nonzero-transfer D3 ratio, and requires `q_a` in the closed sorted one-sided derivative interval;
5. intersects the implied `q_b` interval with the unchanged active liquid-face multiplier domain;
6. reuses the frozen 513-point log screen and `brentq` tolerance on that exact interval, with a separately counted adopted-switching root;
7. reconstructs controls, D1/D3/KKT objects and Hamiltonian from the switching shadows and canonicalizes zero drifts only within the existing arithmetic bounds;
8. never constructs a candidate carrying both a new interior-`a` switch and a liquid-`Z` switch.

D2 code and law were unchanged. A small backward-compatible ledger hook in the nonlinear checkpoint mapper records the new root category when the caller supplies that ledger field. The one-shot checkpoint runner was rebound to this task, Owner adoption, new selector identity, fresh evidence root and exact terminal classifications.

## Focused engineering gate

The exact focused suite passed before the scientific run:

- result: `59 passed`, `0 failed`, `0 errors`, `0 skipped`;
- elapsed pytest time: `0.93 s`;
- JUnit SHA-256: `D753399AE3DBF308F6B21A5671E06A955A31D2EF80999CFF73471F93A369A6E8`;
- Python compile gate: PASS;
- `git diff --check`: PASS.

Coverage included the exact cell100 candidate and interval/root receipt, strict-crossing and boundary non-triggers, no two-axis combined candidate, lower-b eight-case preservation, upper-b domain behavior, positive active no-root failure, unchanged liquid-`Z`, unchanged lower-`a` zero-kink, unchanged D2 zero-drift consumption, and the previously affected selector/KKT/D1/D3/nonlinear contract tests. Engineering selector/root calls were fixture-only and did not consume the scientific map budget.

## Cell100 adopted switching receipt

Durable receipt: `checkpoint_002/cell_0100.json`, SHA-256 `4BC27E1E444EFB826363187154028720EFAF711FBEAC6A8E2AC5B9B210950898`.

- flat/index/state: `100`, `(0,5,0)`, `(b,a,z)=(-2.0,2.6315789473684212,0.8)`;
- endpoint `a` shadows: backward `0.00903315440190679`, forward `0.008957007194295222`;
- endpoint `g_a`: backward `+0.00670682022114244`, forward `-0.0005429159000894801`;
- endpoint arithmetic bounds: `2.1262403671510936e-13`, `2.1276416386913154e-13`;
- `d_Z=-0.236841961910238`, negative-transfer D3 ratio `q_a/q_b=0.7200001089482191`;
- closed derivative interval: `[0.008957007194295222,0.00903315440190679]`;
- implied/intersected lower-b root interval: `[0.012440285887428097,0.012546045881996438]`;
- liquid-equality endpoint values: `-0.003974865872854345`, `+0.048890867998731984`;
- root status: `ROOT_CONVERGED` using `BRENTQ_UNIQUE_LOG_SCREENED_EXACT_INTERVAL`;
- switching shadows: `q_b=0.012448197327813425`, `q_a=0.008962703432234596`;
- raw drifts: `g_b=-5.620504062164855e-16`, `g_a=0.0`; canonical drifts: `g_b=0`, `g_a=0`;
- lower-b multiplier: `0.00011488612109684763`;
- transfer KKT residual: `0.0`;
- Hamiltonian/utility: `-0.12993469950435585`;
- D2 assembler admissible: `true`;
- selector outcome: `SELECTED_ADMISSIBLE`, with this switching candidate selected uniquely.

Thus the adopted branch closes the accepted cell100 defect exactly as authorized. This local success does not imply completion of the 800-cell map.

## First scientific failure

Durable receipt: `checkpoint_002/cell_0185.json`, SHA-256 `69A1CFF66B1CFB6977EC744742635060128BFDB3DE052876C85CC2B5A8A9A337`.

- flat/index/state: `185`, `(5,9,0)`, `(b,a,z)=(-0.1578947368421053,4.7368421052631575,0.8)`;
- derivatives: `p_b^B=0.013362109688537174`, `p_b^F=0.009574726769001294`, `p_a^B=0.00857557540065246`, `p_a^F=0.008489317330830281`;
- outcome: `NO_ADMISSIBLE_POLICY`;
- candidates: `12`; admissible policies: `0`;
- cell roots: `4`, all existing liquid-`Z` roots; adopted interior-`a` roots: `0`.

The negative-transfer liquid-`Z` candidate built from backward `a` has `q_b=0.011845651796693632`, `g_b=0`, `g_a=+0.009287240997760404` and is rejected for backward-`a` direction inconsistency. The corresponding forward-`a` liquid-`Z` candidate has `q_b=0.011826220238545775`, `g_b=0`, `g_a=-0.005170298666228812` and is rejected for forward-`a` direction inconsistency. The remaining ordinary and liquid-`Z` candidates fail their persisted liquid direction, illiquid direction, transfer-sign or D3 KKT gates.

This pattern crosses in `a` only after introducing the existing liquid-`Z` shadow. Closing it would require a simultaneously newly-created `a` switching shadow and liquid-`Z` shadow. The adopted law expressly forbids constructing that combined two-axis switching candidate. The selector therefore correctly failed closed; this task does not adjudicate or repair that new scientific issue.

## Exact scientific ledger

| Operation | Calls |
|---|---:|
| accepted V1 artifact loads | 1 |
| accepted V2 artifact loads | 1 |
| accepted Q1 loads | 1 |
| new corrected V2 policy-map attempts | 1 |
| selector evaluations | 186 |
| total scalar-root invocations | 99 |
| existing interior-liquid `Z` root invocations | 40 |
| adopted interior-`a` switching root invocations | 2 |
| D2/Q2 assemblies | 0 |
| checkpoint-2 diagnostic evaluations | 0 |
| direct HJB solves | 0 |
| V2-to-V3 HJB updates | 0 |
| ordinary graph/SCC summaries | 0 |
| terminal topology gates | 0 |
| terminal dense SVD | 0 |
| terminal normalized stationary candidates | 0 |
| terminal `Q.T@p` | 0 |
| scientific retries | 0 |
| solver substitutions | 0 |
| damping/relaxation/adaptive-Delta/continuation calls | 0 |
| MATLAB/production/outer/firm/GE/annual/shock/IRF/Results calls | 0 |

Because the map stopped at cell185, P2/u2 are incomplete and no Q2 identity, B2/D2, Q2-Q1, policy/operator/cycle or convergence metrics exist. The final durable checkpoint remains the accepted V2 value with a partial, non-checkpoint policy-map receipt prefix through cell185; it is not a completed checkpoint 2.

## Durable evidence and changed paths

Fresh no-overwrite evidence root:

`reports/ch5_mp4c_2018_kfe_d123_interior_a_zero_drift_switching_implementation_v2_checkpoint2_reexecution_20260919_run001`

- sealed-manifest schema: `CH5_D123_INTERIOR_A_SWITCHING_V2_CHECKPOINT2_REEXECUTION_V1`;
- sealed entries: `194`; sealed bytes: `2,982,663`;
- sealed-manifest SHA-256: `A71B21AA66EF158CD4F0AA9C6892046F94F4B8DD826C4E8FC5BCE993216266B7`;
- checkpoint evidence contains the derivative receipt and exactly 186 durable cell receipts, `cell_0000.json` through `cell_0185.json`.

Changed paths are limited to:

- `src/ch5_two_asset_hank/corrected_diagnostic/selector.py`;
- `src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py`;
- `src/ch5_two_asset_hank/corrected_diagnostic/checkpoint2_reexecution.py`;
- `tests/test_mp4c_2018_kfe_d123_interior_a_zero_drift_switching.py`;
- `tests/test_mp4c_2018_kfe_d123_lower_b_active_negative_backward_a.py`;
- the fresh evidence root above;
- this report.

No CURRENT file, source-faithful/production path, D2 equation, calibration, grid, tolerance, solver, convergence law or accepted artifact was modified. Main was not merged and no successor task was published.
