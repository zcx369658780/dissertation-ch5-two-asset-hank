# CH5 MP4C K1A raw-ra0 corrected-household fixed-price three-point safety panel acceptance

Date: 2026-09-20

Reviewer verdict:

`PASS__RAW_RA0_FIXED_PRICE_THREE_POINT_ONE_STEP_SAFETY_ACCEPTED__PATH_B_TURN1_31_PROVINCE_FIXED_PRICE_CROSS_SECTION_AUTHORIZED`

## Accepted candidate

- live main before Builder task: `ed17a6e30f079fe7f73dcb2214b5e1a98095c75c`
- implementation-freeze commit: `824a63a1fbd9c68a94671ff7deafe24e1c796f68`
- Builder candidate: `51111c26a5f62f42fcf8cef636ae9f56d3788527`
- candidate tree: `6992faf9e04df14466946912961e55cc16df2196`
- ancestry: exactly `2 ahead / 0 behind`
- independently tree-compared changed paths: `2448`
  - driver: 1
  - focused test: 1
  - report: 1
  - evidence: 2445
  - CURRENT files: 0
- Builder did not merge main and did not publish a successor.

## Source and authority acceptance

The exact accepted payoff evidence file is:

`docs/evidence/ch5_mp4c_k1a_payoff_return_reaudit/static_no_feedback_payoff_counterfactual.csv`

with frozen SHA-256:

`5496DA47A1F06E46088D4FA80B3803654FB6C47134EE0D32F2DF79028C0FE9F9`.

The Builder independently sorted all 775 `B_GEOGRAPHIC_BETA2` observations by exact Decimal value before science and reproduced the preregistered points exactly:

- LOW: Qinghai turn 5, `0.11048158315647279`
- MEDIAN: Hunan turn 12, `0.26259451366691877`
- HIGH: Beijing turn 4, `1.037811238406538`.

They are portfolio-weighted `S'ra0` household payoff values, not destination firm returns.

Exact checkpoint-11 V/P/u/Q, grid and non-payoff scalar binding passed. The only changed economic scalar in the panel was `r_a`; the accepted state-dependent taper remained unchanged.

## Accepted one-step safety result

All three preregistered points completed exactly one corrected 800-cell policy map, one D2/Q assembly and one frozen direct implicit update.

| Point | B_seed | D_step | backward error | normalized policy identity changes |
|---|---:|---:|---:|---:|
| LOW | `0.0012787655754729066` | `0.019623779080780945` | `2.0486705345909371e-16` | 51 |
| MEDIAN | `0.010402976627898047` | `0.13237145029256903` | `1.8258654602313007e-16` | 80 |
| HIGH | `0.05667966349584988` | `0.18050857122147956` | `1.9352806692350628e-16` | 82 |

All direct solves used only `scipy.sparse.linalg.spsolve`, fixed `Delta=1000`, produced no warnings and are far inside the frozen `1e-12` backward-error bound.

`B_seed` and `D_step` remain diagnostics only. No HJB convergence classification was performed because accepted V11 was not generated under the new raw payoff values.

No monotonicity, threshold or fitted trend is accepted from the three observations.

## Policy, switching and D2 acceptance

All three maps passed 800/800 selector cells and unchanged D2 structural/conservation gates.

Accepted policy canonical identities:

- LOW `7F263A6B42822365E8141A7BC12E095B2F496FD53D20C082430C8D0652AF8457`
- MEDIAN `AF849F45C69525E626D1C5FC19E5569D0BDD5A3E34CC3FB19E8C309387C70426`
- HIGH `40D5B52F3BBF995F78662682136FAE807908DDBD2E10DC791DA24D33EBF235C6`.

Transfer-branch counts are unchanged at all three points: negative 298, positive 323, zero-kink 179.

The panel exercised both accepted switching mechanisms relevant here:

- LOW selected 14 interior-a switching policies and used one interior-a root;
- MEDIAN selected one liquid-Z policy at flat index 381;
- HIGH selected one liquid-Z policy at flat index 798;
- no joint-switching root was invoked.

Every Q has `nnz=3120`, nonnegative off-diagonals, exact-zero diagonal-construction error, and row-sum residual within its prospective floating-point bound.

The HIGH operator differs materially from accepted Q11, but it remains a legal D2 generator. That is exactly why this result is classified as one-step safety rather than convergence.

## Serialization-normalized diagnostic repair

The initial in-memory identity-change comparison again encountered tuple/list representation mismatch for `active_constraints`.

After all science ended, Builder reloaded both accepted and new selected-policy receipts from persisted JSON and repeated only the representation comparison.

The accepted corrected counts are `51 / 80 / 82`.

This is a zero-science representation repair:

- new policy maps: 0
- selector evaluations: 0
- Q assemblies: 0
- HJB solves: 0
- scientific retries: 0.

No scientific policy identity changed.

## Ledger and evidence acceptance

Scientific ledger:

- policy maps: 3
- selector evaluations: 2400
- scalar roots: 813
- liquid-Z roots: 44
- interior-a roots: 1
- joint roots: 0
- D2/Q assemblies: 3
- direct HJB solves/updates: 3/3
- complete point evaluations: 3
- scientific retries / solver substitutions: 0/0
- KFE/SVD/eigen/nullspace/mass: 0
- capital network / firm / outer / K1B / MATLAB / GE / annual / shock / IRF / welfare / Results: 0
- payoff clipping/rescaling/smoothing/risk adjustment/z-score: 0.

Evidence root:

`reports/ch5_mp4c_k1a_raw_ra0_corrected_household_fixed_price_three_point_safety_panel_20260920_run001/`

Final sealed manifest:

`6D0A210F3979B0E0499FA8CC4C21803EB59077D655286D7119E0F85741BB5ED4`

with 2444 entries and 38,471,991 bytes.

The persisted independent readback receipt verifies the pre-self-inclusion manifest; the final report records the final external readback with zero bad paths. Pre/post scientific-code hashes match. Persisted pre-science focused suite: 15 PASS.

## Scientific interpretation and successor

The adopted raw-ra0 payoff law survives a deliberately broad fixed-price one-step stress panel spanning the accepted Path-B global minimum, median and maximum household portfolio payoff observations.

This is sufficient to authorize the next proportionate gate: test one **simultaneous 31-province payoff cross-section** from accepted Path-B turn 1, while still freezing every non-payoff household input at checkpoint-11 values.

That successor is not yet a true province-specific household batch because wages, liquid rates, transfers and starting values remain common. It exists to detect any intermediate raw-payoff selector/D2 discontinuity missed by the three-point panel before province-specific inputs or outer feedback are introduced.

Current successor:

`tasks/CH5_MP4C_K1A_RAW_RA0_PATH_B_TURN1_31_PROVINCE_FIXED_PRICE_ONE_STEP_CROSS_SECTION_20260920.md`.

Results eligibility remains `FALSE`.
