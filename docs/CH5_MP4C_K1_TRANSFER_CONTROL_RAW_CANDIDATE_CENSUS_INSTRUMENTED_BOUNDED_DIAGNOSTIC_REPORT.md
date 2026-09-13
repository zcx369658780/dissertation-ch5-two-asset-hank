# CH5 MP4C K1 — transfer-control raw-candidate census instrumented bounded diagnostic report

Date: 2026-09-13
Task: `CH5_MP4C_K1_TRANSFER_CONTROL_RAW_CANDIDATE_CENSUS_INSTRUMENTED_BOUNDED_DIAGNOSTIC`

## 1. Classification

`EXACT_RAW_CANDIDATE_CENSUS_COMPLETE__NUMERIC_TRANSFER_SAFEGUARD_LADDER_REMAINS_OWNER_DECISION_REQUIRED`

The observation-only census completed the exact accepted G1/G2 five-turn runtime and persisted every raw transfer candidate. It confirms a continuous heavy finite tail over many orders of magnitude. A large isolated top gap exists only between about `4.191e9` and `1.611e12`; it is driven by the two largest positive observations and is not a branch/path/turn-2-robust operational cutoff. No transfer safeguard was implemented or activated.

Preferred future semantics remain unimplemented:

`C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION`

Results eligibility=`FALSE`.

## 2. Authority, baseline, isolation, and changed scope

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Fresh live baseline: `c27741bf763052cd777d0d7261e8d2e951cb0b95`.
- Branch: `codex/ch5-mp4c-k1-transfer-raw-census-20260913`.
- Worktree: `D:\ProjectTemp\ch5-mp4c-k1-transfer-raw-census-20260913-001`.
- External evidence: `D:\ProjectTemp\ch5-mp4c-k1-transfer-raw-census-evidence-20260913-001`.
- The dirty `D:\Zotero-Analytical-Workflow` checkout was not cleaned or modified.
- The protected oracle, transfer FOC, selector, HJB/KFE equations, boundary/KKT law, grid, tolerances and solver were not modified.

The only shared-wrapper change is an optional read-only iteration observer. Task-owned modules serialize and reconcile the copied observations; full raw arrays are external-only.

## 3. Instrumentation parity gate

The focused accepted fixture compared the protected oracle with census instrumentation ON. Exact equality passed for:

- HJB value and initial value;
- consumption, labor, selected transfer and adjustment cost;
- effective illiquid return, `mu_a`, `mu_b`, utility;
- liquid and transfer labels;
- within-loop operator and post-convergence operator;
- iteration count, convergence flag and convergence statistic.

All observation arrays were read-only copies and none entered scientific calculation. Official parity used two fixture HJB invocations and zero trajectory state advancements. Development tests invoked twelve additional small fixture HJB solves across the initial failing serialization-readback check and the repaired passing run; these were not province scientific calls and did not advance trajectory state. The one pre-run defect was Unicode metadata comparison in the NPZ verifier; it was repaired before science. Runtime engineering retries=`0` and scientific retries=`0`.

Focused suite: `8 passed`.

## 4. Frozen science and runtime ledger

Both paths retained `MODEL_TIME_BASE=ANNUAL_CONTINUOUS_TIME`, `rho=.05/year`, `rb=.02/year`, borrowing gap `.07/year`, firm/HJB `delta=.10/year`, `Q_z` off-diagonal `1/3/year`, `chi0=.1`, `chi1=2 years`, fixed theta, `beta_distance=2`, `beta_return=0`, accepted destination-by-origin `S`, same `S` for quantity/payoff, source-faithful labor, smoothing OFF, partial adjustment OFF, C1 unchanged, and K1B/K2 OFF.

Price guards remained G1 `r_a in [-.05,.20]`, G2 `r_a in [-.10,.35]`, and both-path `wjt in [.8,1.3]`. No transfer-control safeguard existed.

| Ledger | G1 | G2 | Total |
|---|---:|---:|---:|
| trajectory invocations | 1 | 1 | 2 |
| completed turns | 5 | 5 | 10 |
| HJB calls | 155 | 155 | 310 |
| HJB iterations/direct solves | 13,362 | 13,834 | 27,196 |
| KFE calls | 155 | 155 | 310 |
| HJB converged calls | 38 | 26 | 64 |
| HJB nonconverged calls | 117 | 129 | 246 |
| scientific/runtime retries | 0 | 0 | 0 |

MATLAB, standalone KFE experiment, K1B, K2, GE, annual downstream, shock/IRF and Results calls were all `0`.

## 5. Exact census and reconciliation

- HJB call chunks: `310/310`.
- Grid cells per iteration: `800`; raw branches: `4`.
- Raw observations: `27,196 × 800 × 4 = 87,027,200`.
- Finite=`87,027,200`; NaN=`0`; `+Inf=0`; `-Inf=0`.
- Selected iteration-cells: `21,756,800`; exact raw-contributor reconstruction matches=`21,756,800/21,756,800`.
- Final-call selected cells: `248,000`.
- Old accepted overlap: `310/310` HJB calls.
- Recomputed raw arrays: `108,784`; checked min/median/p95/p99/max/hash fields: `652,704/652,704` exact matches.

Each NPZ contains path/turn/province/call metadata, iteration, branch identity, implicit zero-based indices plus exact grid arrays/hashes, raw `d`, selected transfer and label, raw-contributor and selector-direction masks, adjustment cost, return/wage input position, boundary bits, and final HJB convergence classification.

## 6. Exact raw distributions

| Population | count | min | max | abs p50 | abs p99 | abs p99.9 | abs p99.99 | positive / negative / zero |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `d_bb` | 21,756,800 | -2.785464010e9 | 1.714597479e12 | 2.62146 | 4,126.50 | 87,799.34 | 1,555,860.23 | 25.8201% / 65.5524% / 8.6275% |
| `d_bf` | 21,756,800 | -2.710347230e9 | 4.190962675e9 | 2.88551 | 2,079.53 | 35,379.52 | 649,021.57 | 25.5125% / 66.0726% / 8.4150% |
| `d_fb` | 21,756,800 | -2.623956919e9 | 1.611417707e12 | 2.65717 | 3,730.37 | 77,502.81 | 1,388,456.78 | 26.0810% / 65.2594% / 8.6596% |
| `d_ff` | 21,756,800 | -2.292697579e9 | 4.185028038e9 | 2.85511 | 2,094.58 | 35,824.73 | 631,312.38 | 25.1762% / 66.2906% / 8.5332% |
| pooled | 87,027,200 | -2.785464010e9 | 1.714597479e12 | 2.75556 | 2,888.04 | 58,175.12 | 1,015,033.53 | 25.6474% / 65.7938% / 8.5588% |

Exact p50/p75/p90/p95/p97.5/p99/p99.5/p99.9/p99.95/p99.99, absolute, positive-tail and absolute-negative-tail results for pooled, every branch, G1/G2, turn 2, turns 3–5, interior/four boundaries and converged/nonconverged calls are in `exact_distributions.json`.

## 7. Preregistered exact threshold grid

| `D` | raw `|d|>D` | raw share | `d>D` | `d<-D` |
|---:|---:|---:|---:|---:|
| 1e2 | 8,921,741 | 10.251670% | 3,306,220 | 5,615,521 |
| 3e2 | 4,066,119 | 4.672239% | 1,861,563 | 2,204,556 |
| 1e3 | 1,867,409 | 2.145776% | 906,107 | 961,302 |
| 3e3 | 845,711 | 0.971778% | 385,145 | 460,566 |
| 1e4 | 346,752 | 0.398441% | 148,646 | 198,106 |
| 3e4 | 147,705 | 0.169723% | 62,438 | 85,267 |
| 1e5 | 55,990 | 0.064336% | 24,291 | 31,699 |
| 3e5 | 23,131 | 0.026579% | 10,218 | 12,913 |
| 1e6 | 8,826 | 0.010142% | 3,939 | 4,887 |
| 3e6 | 3,812 | 0.004380% | 1,707 | 2,105 |
| 1e7 | 1,500 | 0.001724% | 638 | 862 |
| 1e8 | 241 | 0.000277% | 124 | 117 |

These are `DIAGNOSTIC_SENSITIVITY_GRID` values only.

## 8. Scale break and adjustment-cost scale

The pooled `abs(d)` quantiles progress smoothly from p99 `2.888e3` to p99.5 `7.380e3`, p99.9 `5.818e4`, p99.95 `1.366e5`, and p99.99 `1.015e6`. Every decade from `1e2` through `1e8` has observations, both signs and both G1/G2 paths. Branch and turn-2 shares are similar but not identical.

The largest adjacent top-tail ratio is `384.498`, from `4.190962675e9` to `1.611417707e12`; the next largest is only `1.328`. Because the exceptional jump isolates the top two positive observations rather than a stable cross-partition boundary, it does not identify an admissibility cutoff.

Using the unchanged formula `0.1|d| + d^2/max(a,1e-6)`, raw-candidate implied adjustment cost is finite throughout: median `1.8307`, p99 `1.3001e6`, p99.9 `5.1240e8`, p99.99 `1.5421e11`, max `5.0779e23`. Among `|d|>1e3/1e4/1e5/1e6`, median cost is respectively `1.0593e6`, `9.0740e7`, `8.1858e9`, and `8.8240e11`. These are static scale diagnostics, not counterfactual HJB results.

## 9. Selected versus raw

Across all HJB iterations, selected `d` has abs p50 `1.6972`, p99 `2,644.08`, p99.9 `56,258.76`, p99.99 `961,370.59`, min `-2.785458582e9`, and max `4.190962675e9`.

The 248,000 final-call cells reproduce the prior accepted selected-control population exactly: abs p50 `1.379676`, p99 `1,621.104`, p99.9 `37,156.244`, p99.99 `480,578.820`, min `-42,699,421.260`, max `2,800,319.829`.

## 10. Numeric options for Owner/Reviewer, not a frozen ladder

| symmetric option | raw hit | G1 / G2 raw hit | turn-2 raw hit | branch raw hits `bb/bf/fb/ff` | final selected hit | central raw preserved |
|---|---:|---:|---:|---:|---:|---:|
| `[-1e3,1e3]` | 2.145776% | 2.113054% / 2.177382% | 2.247446% | 2.577406% / 1.783203% / 2.450466% / 1.772030% | 1.398387% | 97.854224% |
| `[-1e4,1e4]` | 0.398441% | 0.399989% / 0.396945% | 0.418928% | 0.539482% / 0.277090% / 0.496930% / 0.280262% | 0.275000% | 99.601559% |
| `[-1e5,1e5]` | 0.064336% | 0.063667% / 0.064983% | 0.067899% | 0.089636% / 0.043099% / 0.081303% / 0.043306% | 0.044355% | 99.935664% |
| `[-1e6,1e6]` | 0.010142% | 0.010049% / 0.010231% | 0.010609% | 0.014129% / 0.006890% / 0.012709% / 0.006839% | 0.007661% | 99.989858% |
| OFF | 0 | 0 / 0 | 0 | 0 / 0 / 0 / 0 | 0 | 100% |

For the four finite options, pooled positive/negative raw hit shares are respectively `1.041177%/1.104599%`, `0.170804%/0.227637%`, `0.027912%/0.036424%`, and `0.004526%/0.005615%`. Final selected positive/negative shares are `0.545565%/0.852823%`, `0.072581%/0.202419%`, `0.009274%/0.035081%`, and `0.001210%/0.006452%`.

The negative tail is more frequent, while the two global positive maxima are much larger. A symmetric ladder is simple but not distribution-symmetric; an asymmetric ladder would require an Owner choice about acceptable sign-specific exclusion. Therefore:

`NUMERIC_TRANSFER_SAFEGUARD_LADDER_REMAINS_OWNER_DECISION_REQUIRED`

## 11. Priority checkpoints

- 湖北 turn 2 interior: G2 iteration 98 `d_bb=-2.108479821e8` is pooled abs rank 121 (percentile `99.999862%`) and contributes to selected `d=-2.106136635e8`; G1 iteration 100 remains ordinary at that cell.
- 山东 turn 2: G2 iteration 72 branch maxima are `-2.864e7/-2.943e7` at pooled abs ranks 657/642; G1 branch maxima remain around `5.5e3–8.2e3`.
- 广东 turn 2: G2 iteration 82 `d_bb=-5.820e6`, `d_fb=-6.155e6` rank 2,319/2,208; G1 remains `|d|<=68.9` at its branch witnesses.
- 辽宁 turn 2: G2 iteration 25 `d_bb=1.714597479e12` and `d_fb=1.611417707e12` are pooled abs ranks 1 and 2; neither is selected at its witness cell.
- 吉林 turn 2: G1 iteration 24 `d_bb=-2.785464010e9` and `d_fb=-2.623956919e9` rank 7 and 9; `d_bb` contributes to selected `d=-2.785458582e9`.
- 四川 turn 4: G1 converges at iteration 57 with ordinary checkpoint values; G2 iteration 100 includes `d_bf=5.3136e4` and selected `d=5.2642e4` at the upper-`b` checkpoint.
- 云南 turn 4: G1 iteration 100 `d_bb=-1.188059026e7` is rank 1,317 and selected; G2 at the same cell improves to selected `d=1,535.815`. This is path-history context, not same-state causality.

No checkpoint is interpreted as proof that future rejection would make an HJB converge.

## 12. Return/wage monitoring and scientific invariants

G1 turns 2–5 have return upper hits `31/31` each turn. G2 upper/unsaturated counts are `18/13` at turn 2 and `22/9` at turns 3–5. Neither path records a return lower hit. Turn 1 is common bootstrap with the return guard not applied.

Wage lower/upper/unsaturated counts are `4/24/3` for G1 turns 1–5 and G2 turns 1–4; G2 turn 5 is `13/12/6`. Exact province names and raw/guarded extrema are in `price_monitoring.json`. Transfer-tail analysis does not erase these binding price safeguards.

Across all 310 province-turns: same-S identity passed, same-turn feedback remained false, source-faithful labor remained true, normalized labor remained false, maximum capital-column residual was `3.7253e-9`, maximum national private-capital conservation residual was `2.9802e-8`, maximum C1 accounting residual was `2.9802e-8`, and maximum raw-`ra0` reconstruction residual was `5.5511e-17`.

Scientific NaN/Inf hard-stop count=`0`; scientific exceptions=`0`.

## 13. External evidence and compact evidence

External sealed manifest:

- path: `D:\ProjectTemp\ch5-mp4c-k1-transfer-raw-census-evidence-20260913-001\sealed_manifest_sha256.json`;
- entries excluding manifest: `1,679`;
- bytes excluding manifest: `2,750,207,621`;
- SHA-256: `7E44C136D6E6656A78A0472FC29AE76CC270C3C4D0178786BE010EAFEC9F6A3B`;
- all entries read back and rehashed: `TRUE`.

Compact evidence is under `docs/evidence/ch5_mp4c_k1_transfer_control_raw_candidate_census/`. Full raw arrays are not committed.

## 14. KKT, KFE, and Results boundary

Standalone KKT residual remains `UNAVAILABLE_IN_ACCEPTED_EVIDENCE`. All 310 KFE returns remain `DIAGNOSTIC_ONLY`; finite-box upper-`b` leakage and MATLAB-style pinning remain independent blockers. HJB convergence, finite raw candidates and exact census reconciliation do not establish KFE admissibility, steady-state acceptance or Results authority.

Results eligibility=`FALSE`.

## 15. Exactly one next gate

`INDEPENDENT_GPT_L3_ACCEPT_OR_REJECT_RAW_CANDIDATE_CENSUS_CANDIDATE`

Stop. This candidate does not implement a transfer safeguard, merge main, freeze a numeric ladder, authorize another runtime, or publish a successor task.
