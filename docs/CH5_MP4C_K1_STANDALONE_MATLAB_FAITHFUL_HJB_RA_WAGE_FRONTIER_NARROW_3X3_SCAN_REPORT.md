# CH5 MP4C K1 standalone MATLAB-faithful HJB `ra×wage` frontier narrow 3×3 scan report

Date: 2026-09-13

Task ID: `CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_SCAN`

## Outcome

`ALL_HJB_LEGAL_CONVERGED__NO_WAGE_ROBUST_INTERIOR_RA__TWO_DIMENSIONAL_HEALTH_REGION_REQUIRED`

All nine preregistered HJB points were legal and converged. The two interior-distribution candidates are `(ra,w)=(.06,1.3)` and `(.0675,1.3)`. No tested `ra` is interior at all three wages, and no connected wage-robust interior `ra` band exists. The frontier shifts materially with wage, so the frozen decision rule requires stopping automatic one-dimensional `ra` refinement and moving Owner review to the two-dimensional `(ra,w)` health region and provincial return mapping.

Results eligibility=`FALSE`.

## Git, provenance, and frozen-input receipt

- Fresh-fetched baseline: `origin/main=d0323df5a85617f3c856b93c88c98a08deb697be`.
- Branch: `codex/ch5-mp4c-k1-hjb-ra-wage-frontier-narrow-3x3-20260913`.
- Worktree: `D:\ProjectTemp\ch5-mp4c-k1-hjb-ra-wage-frontier-narrow-3x3-20260913-001`.
- Exact grid only: `rb=.02`, `ra={.06,.0675,.07}`, `w={.8,1.05,1.3}`; exact Cartesian product, nine points.
- Oracle SHA-256: `F6007C1166C951B4A0C98B0FBF551921A2664D2E3943E7D77F847634261524F8`, matching expected.
- Protected MATLAB source SHA-256: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`, matching expected; MATLAB runtime was not invoked.

Nine distinct fresh initial-value objects and nine distinct fresh baseline-labor objects were constructed. The input-invariance receipt has `varying_fields=[inputs.r_a,inputs.wages[0]]`, `unexpected_varying_fields=[]`, and `all_non_scanned_fields_identical=true`. The accepted grids, productivity transition, parameters, tax/transfer, borrowing-rate gap, initialization construction, derivative floor, FOC, selector, boundary laws, operator assembly, direct solve, tolerance, ceiling, legality rule, and contaminated-row KFE were unchanged. No warm start, damping, relaxation, price guard, or extra point was used.

## Call ledger

| Item | Actual / budget |
|---|---:|
| fresh initialization constructions | 9 |
| HJB started / completed | 9 / 9 |
| KFE started / completed | 9 / 9 |
| scalar labor roots | 7200 |
| scientific retries | 0 |
| engineering retries | 0 |
| global multi-province outer turns | 0 |
| firm / MATLAB / K1B / K2 / GE | 0 / 0 / 0 / 0 / 0 |
| annual downstream / shock / IRF / Results writes | 0 / 0 / 0 / 0 |

KFE ran exactly once only after each converged HJB.

## Required 3×3 matrix

Every cell has HJB class `HJB_CONVERGED`; the second line is the descriptive distribution class.

| `ra` \ `w` | `.8` | `1.05` | `1.3` |
|---|---|---|---|
| `.06` | `LOWER_A_BOUNDARY_DOMINATED` | `LOWER_A_BOUNDARY_DOMINATED` | `INTERIOR_A_DISTRIBUTION_CANDIDATE` |
| `.0675` | `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED` | `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED` | `INTERIOR_A_DISTRIBUTION_CANDIDATE` |
| `.07` | `UPPER_A_BOUNDARY_PILEUP` | `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED` | `TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED` |

Counts: HJB converged `9`, HJB nonconverged `0`, hard-error/invalid transition matrix `0`; lower `2`, interior `2`, ambiguous `4`, upper `1`.

Labels use exact modal location and top-two-bin endpoint-versus-interior ordering. No post-result percentage cutoff was fitted. Complete signed raw marginals are retained even where the contaminated-row KFE has nontrivial negative entries.

## Per-point HJB and KFE receipts

All HJBs converged in 9 iterations, returned finite scientific arrays of the expected `(20,20,2)` shapes, kept label arrays inside the accepted domains, and had no first illegal iteration. Total KFE mass is `0.9999999999999998–0.9999999999999999`.

| `ra,w` | final `max|ΔV|`; max `A2max` | `Ct,Lt,At,Bt` | `Bt_pos;Bt_neg` | `amin;amax;bmin;bmax;interior-a` | modal `a;b`; top three `a:mass` | ratio; density min/count; residual | label |
|---|---|---|---|---|---|---|---|---|
| `.06,.8` | `4.61015e-9`; `3.83027e-15` | `.882974;1.055145;-.338331;.288507` | `.410179;-.121672` | `1.037799;-.007112;.000114;0;-.030688` | `0;.210526`; `0:1.037799`, `.526316:-2.97e-13`, `1.052632:-3.80e-12` | `.777562`; `-.012590/340`; `2.22045e-16` | lower |
| `.06,1.05` | `9.42637e-9`; `5.32907e-15` | `1.111472;1.016586;.006762;.369479` | `.516417;-.146938` | `.999236;.000126;.001208;0;.000638` | `0;.210526`; `0:.999236`, `8.947368:.000171`, `9.473684:.000170` | `.744003`; `-1.65e-19/25`; `1.42109e-14` | lower |
| `.06,1.3` | `2.16723e-8`; `5.32907e-15` | `1.627175;.891818;8.735399;.580463` | `.632751;-.052288` | `0;.143222;1.52e-10;0;.856778` | `8.947368;.210526`; `8.947368:.213987`, `9.473684:.207297`, `8.421053:.180018` | `.690902`; `-1.00e-19/25`; `3.48300e-17` | interior |
| `.0675,.8` | `3.19050e-9`; `3.60822e-15` | `1.258213;.872804;8.964760;1.066572` | `1.091006;-.024433` | `0;.226616;0;0;.773384` | `9.473684;.210526`; `9.473684:.232967`, `10:.226616`, `8.947368:.189204` | `.972735`; `-4.05e-17/97`; `3.55289e-18` | ambiguous |
| `.0675,1.05` | `9.42516e-9`; `4.27436e-15` | `1.461623;.869779;8.973165;.907107` | `.943307;-.036200` | `0;.218451;0;0;.781549` | `9.473684;.210526`; `9.473684:.236807`, `10:.218451`, `8.947368:.199513` | `.922484`; `-2.19e-18/30`; `8.53809e-18` | ambiguous |
| `.0675,1.3` | `2.16705e-8`; `5.32907e-15` | `1.657915;.865304;8.935855;.807046` | `.858029;-.050983` | `0;.195638;2.28e-23;0;.804362` | `9.473684;-.157895`; `9.473684:.238140`, `8.947368:.206598`, `10:.195638` | `.821527`; `-5.62e-17/14`; `1.00736e-17` | interior |
| `.07,.8` | `3.18878e-9`; `3.55271e-15` | `1.267358;.864988;8.936969;1.174757` | `1.199477;-.024720` | `0;.224781;0;0;.775219` | `10;.210526`; `10:.224781`, `9.473684:.224536`, `8.947368:.189096` | `1.001092`; `-5.81e-18/1`; `2.84603e-18` | upper |
| `.07,1.05` | `9.42467e-9`; `5.32907e-15` | `1.471336;.861960;8.958043;1.009419` | `1.045375;-.035955` | `0;.218848;0;0;.781152` | `9.473684;.210526`; `9.473684:.231350`, `10:.218848`, `8.947368:.201897` | `.945958`; `-1.04e-17/120`; `8.67362e-18` | ambiguous |
| `.07,1.3` | `2.16698e-8`; `4.27436e-15` | `1.667043;.857186;8.949063;.890311` | `.941176;-.050864` | `0;.208959;-1.01e-23;0;.791041` | `9.473684;-.157895`; `9.473684:.231448`, `10:.208959`, `8.947368:.206311` | `.902836`; `-2.81e-17/140`; `1.49620e-17` | ambiguous |

The `.06,.8` contaminated-row solution is especially pathological: signed `amin` mass exceeds one, `amax` and aggregate interior-a mass are negative, density minimum is `-.01259`, and `At` is negative. These values are deliberately not clipped. Its descriptive lower-bound label only reports modal/dominance ordering; it is not an admissibility or production claim. The `.06,1.05` raw residual is `1.42e-14`, still reported without upgrading KFE validity.

## Scientific interpretation

No tested scalar `ra` is healthy across all three wages. At `w=.8`, the distribution moves from lower at `.06`, through mixed at `.0675`, to upper-bound pile-up at `.07`. At `w=1.05`, it moves from lower at `.06` to mixed at `.0675/.07`. At `w=1.3`, it is interior at `.06/.0675` and mixed at `.07`. Higher wage therefore shifts or broadens the interior frontier toward different `ra` values; a universal scalar interval is not supported.

There is no connected wage-robust interior band. Across the two interior candidates only, descriptive aggregate ranges are:

- `Ct=[1.6271748553562086,1.6579145830154138]`;
- `Lt=[.8653040707113617,.891817638945374]`;
- `At=[8.735398940966421,8.935854550440705]`;
- `Bt=[.5804628039224781,.807045544098199]`.

These ranges confer no GE, production, or Results authority.

## Evidence and sole next gate

- Compact evidence: `docs/evidence/ch5_mp4c_k1_standalone_hjb_ra_wage_frontier_narrow_3x3/`.
- Compact sealed-manifest SHA-256: `AEDC537B4A1E67D3E750876319B59DFBC306C6DD0665723CF979400C250AFD58`.
- External no-overwrite evidence: `D:\ProjectTemp\ch5-mp4c-k1-hjb-ra-wage-frontier-narrow-3x3-evidence-20260913-001`.
- External sealed-manifest SHA-256: `614D8D458DF481BD4FFCFE7688969DF7A243CC83BA6D1ED8BFDC70746E231AEF`.

Exactly one recommended next gate, not executed and not published as a successor task: `OWNER_REVIEW_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING`. It must review the two-dimensional `(ra,w)` region and provincial return mapping; automatic one-dimensional `ra` refinement should not continue.

This accepted standalone MATLAB-faithful contaminated-row KFE does not solve the corrected-2018 multi-province finite-box upper-`b` leakage or MATLAB-style pinning blocker. No global model, firm block, MATLAB runtime, K1B/K2, GE, annual downstream, shock, IRF, or Results action occurred.

Stop gate: independent ChatGPT Reviewer ACCEPT/REJECT of the candidate commit.
