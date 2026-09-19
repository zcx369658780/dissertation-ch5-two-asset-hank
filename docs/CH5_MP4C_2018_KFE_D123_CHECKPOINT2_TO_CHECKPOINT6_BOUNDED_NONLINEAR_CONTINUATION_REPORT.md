# CH5 MP4C 2018 KFE D1-D3 checkpoint-2 to checkpoint-6 bounded nonlinear continuation

Date: 2026-09-19

Task: `CH5_MP4C_2018_KFE_D123_CHECKPOINT2_TO_CHECKPOINT6_BOUNDED_NONLINEAR_CONTINUATION_20260919`

## Terminal classification

`FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE`

The exact accepted complete checkpoint 2 was bound and reused without rerunning its policy map or Q2 assembly. The single `V2 -> V3` direct solve passed the frozen backward-error gate. The first fresh V3 policy map then stopped at its first failure, F-order flat index 100, after cells 0 through 99 passed. No P3/u3/Q3 or complete checkpoint-3 evaluation exists. No further update, retry, repair, D2 assembly, convergence/cycle evaluation, topology or KFE operation was performed.

The last complete nonlinear checkpoint remains checkpoint 2. The final reached value state is incomplete checkpoint 3, with V3 SHA-256 `4FDB36C17ACDC60B56661AEE1C0437B65EC4A871FD4E5E08A9A996FB10EF85EF`.

Results eligibility remains `FALSE`.

## Git and execution binding

- fresh live-main baseline: `aac2c854a8a208f4abb469ce310b3347195f4df7`;
- task branch: `codex/ch5-mp4c-2018-kfe-d123-checkpoint2-to-checkpoint6-bounded-nonlinear-continuation-20260919`;
- scientific execution-head / implementation freeze commit: `b58d5e982229914f4e4744b6b4b686e16b20a20f`;
- the worktree was clean before evidence creation and the branch was `1 ahead / 0 behind` live `origin/main`;
- the post-execution scientific-code hash set exactly matched the pre-execution freeze;
- `deep-learning-hank` was not entered, read, searched, used or modified.

## Engineering and preflight gate

The focused engineering suite passed before scientific entry:

- `69 passed`, `0 failed`, `0 errors`, `0 skipped`;
- pytest elapsed time: `1.53 s`;
- JUnit SHA-256: `B70C371845CCFCE3D9A382ADF8F072AD081C9370AFEB72ADF3B5CC42066C8AC4`;
- `py_compile`: PASS;
- `git diff --check`: PASS.

The focused coverage includes accepted-checkpoint-2 exact binding, the prohibition on V2-map/Q2 reruns, the four-update/map ledger ceiling, direct-solve backward error, primary/exact/approximate gate order, approximate period-2 availability only from checkpoint 4, approximate period-3 availability only from checkpoint 6, and all affected selector/D1/D2/D3/liquid-Z/interior-a/joint/lower-a/lower-b contracts.

All accepted checkpoint-2 preflight checks passed, including sealed-manifest readback of all 816 entries and exact V0/V1/Q1/V2/P2/u2/Q2 identities.

## Exact accepted checkpoint-2 reuse

- V2: `A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`;
- P2: `EBCBABC0593EF163D2E7FA300F6FFEB6E3C187D232D4CCEA5D59AB7180CD1D95`;
- u2: `C222F4B147F48EA177A28AAF289F3ED5EA76F531BC08201070DD63698BF98D73`;
- Q2 artifact: `346DBCDA13392DAF6897DC185767B0E7C5961AA76A9AAA686053AEDA33C02F9F`;
- Q2 data/indices/indptr: `3278FFDA5ABA29E8C8E7ECC84649DF7A787AD7BDA5E936657F585B65A9844BEB` / `6FF05054740279B563416E942AFEC958804FBD1AF63C660C9877D3175FB5B066` / `180A552000B935F15F1934266DE86FF9E3D7550005366AB92B312793648F0200`;
- checkpoint-2 identity: `71DC6975E814060A4F63961A736E6E9DDF766C51CE4672C3EF777E5E15B80C2C`;
- accepted sealed-manifest SHA-256: `B3CC70792E41E0EBDDE138057406C86D07063AD44959B595FA1B503B9D5AE2EA`;
- accepted `B2=0.006582827785543588`, `D2=0.05439336697877817`, primary convergence FAIL.

The task ledger records `v2_policy_map_reruns=0` and `q2_assembly_reruns=0`.

## V2 to V3 direct update

The first and only direct HJB solve used the frozen equation, `Delta=1000`, accepted u2/Q2, F ordering, and `scipy.sparse.linalg.spsolve`.

- status: PASS;
- warnings: none;
- original-equation residual infinity norm: `1.4391265956703592e-14`;
- normwise backward error: `2.439151619375125e-16 <= 1e-12`;
- rhs SHA-256: `C3FC71FCD0463CC171ED37ED2C1893E8930DC1E5D40677D6E852CB4B88B655F9`;
- residual SHA-256: `D37D609D09D306662282BD7E4479331D45DB414B90464C786EDE4546E74E9D83`;
- V3 SHA-256: `4FDB36C17ACDC60B56661AEE1C0437B65EC4A871FD4E5E08A9A996FB10EF85EF`;
- direct-update artifact SHA-256: `17F330AB0A226EE826880039055B9EA16FB93DD7B02F36F820D078178C6E4CCF`.

This consumed global HJB update 3. It did not establish a complete checkpoint 3.

## First checkpoint-3 failure

The one fresh V3 map evaluated exactly 101 selectors. Cells 0 through 99 returned `SELECTED_ADMISSIBLE`. The first failure is:

- checkpoint: `3`;
- flat F index: `100`;
- zero-based index `(i_b,i_a,i_z)=(0,5,0)`;
- state `(b,a,z)=(-2.0,2.6315789473684212,0.8)`;
- outcome: `NO_ADMISSIBLE_POLICY`;
- enumerated candidates: `7`;
- admissible candidates: `0`.

The seven persisted candidates comprise four slack-liquid forward-b cases and three active-lower-b cases. Their rejection reasons are preserved verbatim in `checkpoint_003/cell_0100.json`. The active-lower-b candidates are:

| a branch | transfer label | root | q_b | q_a | d | g_a | rejection reasons |
|---|---|---|---:|---:|---:|---:|---|
| backward | negative | `ROOT_CONVERGED` | 0.012942099013665916 | 0.012088089476579748 | 0.04475402367270802 | 0.281595985582946 | `TRANSFER_SIGN_INCONSISTENT_NEGATIVE`; `A_DERIVATIVE_DIRECTION_INCONSISTENT`; `TRANSFER_KKT_RESIDUAL` |
| forward | zero_kink | `ROOT_CONVERGED` | 0.012837941893151116 | 0.01134140574122853 | 0 | 0.236841961910238 | `TRANSFER_KKT_RESIDUAL` |
| forward | positive | `ROOT_CONVERGED` | 0.012433508172707636 | 0.01134140574122853 | -0.24715187043766376 | -0.010309908527425748 | `TRANSFER_SIGN_INCONSISTENT_POSITIVE`; `A_DERIVATIVE_DIRECTION_INCONSISTENT`; `TRANSFER_KKT_RESIDUAL` |

This receipt establishes only the frozen selector's first failure at V3. It does not authorize a new branch, repair, scientific-law inference, tolerance change or retry.

Because the map is incomplete:

- P3/u3 identities do not exist;
- Q3 was not assembled;
- D2 legality at checkpoint 3 was not evaluated;
- B3/D3, policy/operator stability, exact-cycle and approximate-cycle metrics were not evaluated;
- checkpoints 4 through 6 were not entered.

## Exact task scientific ledger

| Operation | Calls |
|---|---:|
| accepted V0 loads | 1 |
| accepted V1 loads | 1 |
| accepted Q1 loads | 1 |
| accepted V2 loads | 1 |
| accepted P2 loads | 1 |
| accepted u2 loads | 1 |
| accepted Q2 loads | 1 |
| accepted checkpoint-2 manifest loads | 1 |
| V2 policy-map reruns | 0 |
| Q2 assembly reruns | 0 |
| new direct HJB solves / updates | 1 / 1 |
| new corrected policy-map attempts | 1 |
| selector evaluations | 101 |
| total scalar-root invocations | 46 |
| liquid-Z root invocations | 15 |
| interior-a switching root invocations | 0 |
| joint-switching root invocations | 0 |
| D2/Q assemblies | 0 |
| complete checkpoint evaluations | 0 |
| graph/SCC/topology gates | 0 |
| KFE/SVD/eigen/nullspace/`Q.T@p` | 0 |
| scientific retries | 0 |
| solver substitutions | 0 |
| damping/relaxation/adaptive Delta | 0 |
| parameter continuation/clipping/artificial diffusion | 0 |
| MATLAB/production/outer/firm/GE/annual/shock/IRF/Results | 0 |

## Durable evidence and changed paths

Fresh no-overwrite evidence root:

`reports/ch5_mp4c_2018_kfe_d123_checkpoint2_to_checkpoint6_bounded_nonlinear_continuation_20260919_run001`

- sealed-manifest schema: `CH5_D123_CHECKPOINT2_TO_CHECKPOINT6_CONTINUATION_V1`;
- sealed entries: `113`;
- sealed bytes: `1,739,107`;
- sealed-manifest SHA-256: `9F772B9CEF73E15F0443952B25989BB6D644D73B9E04CB93B5AD047E1FBB7700`;
- pre/post scientific-code freeze: exact match.

Changed paths are limited to:

- `src/ch5_two_asset_hank/corrected_diagnostic/checkpoint2_to_checkpoint6.py`;
- `tests/test_mp4c_2018_kfe_d123_checkpoint2_to_checkpoint6.py`;
- the fresh evidence root above;
- this report.

No CURRENT file, source-faithful/production path, scientific equation, KKT law, D1/D2/D3 law, selector law, root solver/tolerance, grid, calibration, convergence/cycle law or terminal KFE law was modified. Main was not merged and no successor task was published.
