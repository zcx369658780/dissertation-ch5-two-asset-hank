# Task — K1A raw-ra0 Path-B turn-1 31-province fixed-price one-step cross-section

Date: 2026-09-20

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_K1A_RAW_RA0_PATH_B_TURN1_31_PROVINCE_FIXED_PRICE_ONE_STEP_CROSS_SECTION_20260920`

Status: `ACTIVE`

## Governance

Owner is final scientific authority. ChatGPT is L3 independent Reviewer/scientific-route authority. Codex is bounded Builder.

GitHub live main is repository-state authority.

Absolute prohibition:

`zcx369658780/deep-learning-hank`

must never be entered, read, searched, used or modified.

Fresh-fetch `origin/main` and read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_K1A_RAW_RA0_PAYOFF_OWNER_ADOPTION_20260920.md`
6. `docs/CH5_MP4C_K1A_RAW_RA0_CORRECTED_HOUSEHOLD_FIXED_PRICE_THREE_POINT_SAFETY_PANEL_ACCEPTANCE_20260920.md`
7. accepted three-point evidence
8. exact accepted checkpoint-11 household evidence
9. accepted K1A payoff CSV.

No new economic law is authorized.

## Objective

Evaluate the complete accepted **Path-B geographic-beta2 turn-1 raw household payoff cross-section** through the corrected household one-step law.

The purpose is to test all 31 simultaneous province-labelled raw portfolio payoff levels for selector/D2/direct-solve admissibility before any province-specific non-payoff input or outer feedback is introduced.

This remains a fixed-price payoff-isolation experiment.

It is **not** a true province-specific household batch: every non-payoff scalar and common starting V remain the accepted checkpoint-11 values.

## Exact source authority

Accepted CSV:

`docs/evidence/ch5_mp4c_k1a_payoff_return_reaudit/static_no_feedback_payoff_counterfactual.csv`

Frozen SHA-256:

`5496DA47A1F06E46088D4FA80B3803654FB6C47134EE0D32F2DF79028C0FE9F9`.

Select exactly:

- `path == B_GEOGRAPHIC_BETA2`
- `turn == 1`
- order by `province_index = 0..30`
- require exactly 31 rows
- require exact active province order
- require every row classification `STATIC_NO_FEEDBACK_COUNTERFACTUAL`
- require every row's next-allocation validation status `VALIDATED_SAME_S_AND_NEXT_ALLOCATION_PAYOFF`.

The exact preregistered raw household payoff vector is:

| province_index | province | r_a = static_raw_S_transpose_ra0 |
|---:|---|---:|
| 0 | 北京 | `0.8951047990241244` |
| 1 | 天津 | `0.40511685922852797` |
| 2 | 河北 | `0.33682681151169935` |
| 3 | 山西 | `0.4291478483179544` |
| 4 | 内蒙古 | `0.3343835179213208` |
| 5 | 辽宁 | `0.35788915914936925` |
| 6 | 吉林 | `0.2826739400149174` |
| 7 | 黑龙江 | `0.315792897526093` |
| 8 | 上海 | `0.8436338107969247` |
| 9 | 江苏 | `0.5309391086970456` |
| 10 | 浙江 | `0.585387220964732` |
| 11 | 安徽 | `0.6239080240565922` |
| 12 | 福建 | `0.612400758531959` |
| 13 | 江西 | `0.6163318073667522` |
| 14 | 山东 | `0.35334433320183295` |
| 15 | 河南 | `0.32804592118083026` |
| 16 | 湖北 | `0.5255285778404981` |
| 17 | 湖南 | `0.4775623850053351` |
| 18 | 广东 | `0.5549881090546146` |
| 19 | 广西 | `0.38090963566299624` |
| 20 | 海南 | `0.6734489815056439` |
| 21 | 重庆 | `0.6385985431144864` |
| 22 | 四川 | `0.5301703013356037` |
| 23 | 贵州 | `0.5570443031272924` |
| 24 | 云南 | `0.4037818827188449` |
| 25 | 西藏 | `0.6268193076948068` |
| 26 | 陕西 | `0.4544982462398813` |
| 27 | 甘肃 | `0.5077975242704716` |
| 28 | 青海 | `0.36949073815753725` |
| 29 | 宁夏 | `0.41304347656460016` |
| 30 | 新疆 | `0.4009777871328596` |

Independent Reviewer readback of this vector gives:

- count = 31
- minimum = Jilin `0.2826739400149174`
- median = Hunan `0.4775623850053351`
- maximum = Beijing `0.8951047990241244`.

Every value lies inside the already passed global three-point interval `[0.11048158315647279, 1.037811238406538]`, but prior range coverage is not a substitute for executing all 31 exact cross-section values.

Do not replace these `S'ra0` household portfolio payoffs with destination firm `ra0`.

## Common corrected-household authority

For every province-labelled payoff value, use the exact same common starting household object:

- V11 `A097A3DDA767B979224638A51CEDC53EA635687CCDEFBE190FED0B899606921F`
- grid `(20,20,2)`, F-order, b fastest
- accepted productivity generator
- accepted D1/D2/D3
- all accepted KKT/boundary/upwind/switching laws
- unchanged household taper.

Freeze all non-payoff scalars exactly:

- `r_b=0.02`
- borrowing-rate gap `0.07`
- `tau=0.05`
- wage `16.82014806560587`
- transfer income `0.1`
- `rho=0.05`
- `gamma_c=2`
- `phi=5`
- `chi_0=0.1`
- `chi_1=2`
- `a_bar=1e-6`
- labor weight `1`
- `Delta=1000`.

Only `r_a` changes by province label.

For every cell:

`effective_r_a(a)=r_a*(1-0.1*(a/10)^9)`.

No payoff clipping or transformation is permitted.

## Execution order and one-step law

Execute sequentially in exact `province_index=0..30` order.

For each reached province:

1. bind the exact source row and common V11/scalars;
2. execute exactly one complete 800-cell corrected policy map;
3. stop immediately on first selector failure;
4. after 800/800 PASS, assemble exactly one D2 Q;
5. require unchanged D2 structural/conservation gates;
6. compute `B_seed=||rho*V11-u-QV11||inf`;
7. execute exactly one fixed-`Delta=1000` implicit update with `scipy.sparse.linalg.spsolve`;
8. require no warning, finite shape/order, normwise backward error `<=1e-12`;
9. compute `D_step=||vec_F(V_plus-V11)||inf`;
10. persist compact policy/operator/switching/solve evidence;
11. do not perform a second update;
12. do not classify HJB convergence;
13. proceed to the next province only after all required one-step gates pass.

If a province fails, stop; do not skip it and continue later provinces.

## Compact evidence mode

The prior three-point task showed that verbose per-cell JSON persistence scales poorly. This task therefore authorizes **compact evidence representation only**, with unchanged scientific calls.

Before science, Builder must implement and validate a compact projection of selected policies.

Zero-science recertification requirement:

- load the already sealed LOW/MEDIAN/HIGH three-point cell receipts;
- project them into the proposed compact format without selector/Q/solve calls;
- reproduce exactly, for all three points:
  - canonical policy identity SHA-256
  - serialization-normalized identity-change count
  - active-constraint counts
  - transfer-branch counts
  - selected interior-a/liquid-Z/joint indices and counts
  - selected control/utility field hashes.

Only after that zero-science compact-projection recertification passes may the 31-point scientific batch begin.

For each new province PASS, compact evidence must preserve at minimum:

- exact source/province/r_a identity
- 800/800 selector outcome count
- canonical selected-policy identity vector/hash
- selected control and utility arrays/hashes
- branch/constraint/transfer representation sufficient to reproduce counts
- switching selected indices and root-status summary
- exact selector/root call ledger
- D2 receipt
- Q CSR identity/artifact
- B_seed receipt
- direct-solve receipt
- V_plus identity
- D_step
- pre/post code-freeze identity.

Do not persist 800 verbose candidate-exploration JSON files per province merely for governance convenience.

On a scientific failure, persist the complete failing cell input/result/exception receipt before stopping.

## Final 31-point comparison

If all 31 pass, produce one compact cross-section summary containing:

- per-province r_a
- B_seed
- D_step
- direct-solve backward error
- policy canonical identity
- serialization-normalized policy change count relative to accepted P11
- active-constraint counts
- transfer-branch counts
- switching counts/selected indices
- Q nnz
- max `abs(Q@1)`
- minimum off-diagonal
- maximum continuous-control changes relative to accepted P11.

Also report min/median/max across provinces for B_seed and D_step as descriptive summaries only.

Do not estimate trends, fit thresholds or infer convergence probabilities.

## Scientific budget

Maximum across the task:

- corrected policy maps: `31`
- selector evaluations: `24,800`
- D2/Q assemblies: `31`
- direct HJB solves / updates: `31 / 31`
- complete one-step cross-section evaluations: `31`
- scalar-root structural ceiling: `9,648,936`
- liquid-Z structural ceiling: `8,838,720`
- interior-a switching roots: `24,800`
- joint-switching roots: `24,800`
- scientific retries: `0`
- solver substitutions: `0`
- KFE/SVD/eigen/nullspace/stationary mass: `0`
- household aggregate evaluation: `0`
- capital-network scientific calls: `0`
- firm/wage/return calls: `0`
- outer-loop/steady-state/trajectory calls: `0`
- K1B feedback calls: `0`
- MATLAB scientific calls: `0`
- GE/annual/shock/IRF/welfare/Results: `0`
- payoff clipping/annualization/rescaling/smoothing/risk adjustment/z-score transformation: `0`.

Static compact-projection recertification of already persisted accepted evidence consumes zero scientific calls.

## Engineering boundary

Builder may add one isolated compact cross-section driver and focused tests.

Do not modify:

- selector law
- D1/D2/D3
- KKT/boundary/upwind/switching science
- grid
- productivity generator
- Delta
- taper
- convergence law
- default multi-province route
- K1/K1A/K1B equations
- firm equations
- Results code.

No parallel scientific execution is required. Sequential province-index order is the authority so the first failure is uniquely identified.

Routine pre-science engineering repair is allowed. Once scientific execution begins, no scientific retry is available.

## Stop conditions

Stop immediately on first:

- live authority/provenance drift
- CSV/hash/31-row/order/value mismatch
- compact-projection recertification mismatch
- selector failure
- D2 failure
- nonfinite policy/Q/V
- direct-solve warning/failure/backward error above `1e-12`
- code-freeze drift
- scientific budget breach.

Do not rescue any province with clipping, rescaling or a transformed return.

## Deliverables

Write:

`docs/CH5_MP4C_K1A_RAW_RA0_PATH_B_TURN1_31_PROVINCE_FIXED_PRICE_ONE_STEP_CROSS_SECTION_REPORT.md`.

Create a fresh compact evidence root under `reports/` with:

- authority/startup binding
- exact 31-row derivation receipt
- compact-projection recertification receipt
- one compact province directory/artifact per reached province
- cross-section comparison
- exact scientific ledger
- pre/post scientific code freeze
- terminal receipt
- sealed manifest and independent readback.

Terminal PASS marker:

`PASS__PATH_B_TURN1_31_PROVINCE_RAW_RA0_FIXED_PRICE_ONE_STEP_CROSS_SECTION__PROVINCE_SPECIFIC_OUTER_INPUTS_NOT_YET_AUTHORIZED`.

A PASS means the exact accepted turn-1 31-province raw payoff cross-section survives one corrected-household step under common checkpoint-11 non-payoff inputs.

It does not establish a true province-specific corrected household batch, HJB convergence, KFE, outer-loop stability, K1B, GE or Results.

Git workflow:

- isolated task branch
- ordinary non-force push
- remote SHA/tree readback
- clean worktree
- do not merge main
- do not modify CURRENT files
- do not publish successor.
