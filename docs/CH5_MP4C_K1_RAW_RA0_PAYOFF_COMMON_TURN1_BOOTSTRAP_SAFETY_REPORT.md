# CH5 MP4C K1 raw `ra0` payoff common-turn-1 bootstrap safety report

Date: 2026-09-12

## Verdict

`RAW_RA0_PAYOFF_SHORT_HORIZON_RUNTIME_SAFETY_SUPPORTED_WITH_COMMON_TURN1_BOOTSTRAP`

Both bounded paths completed 5/5 outer turns. Raw completed all four authorized treatment turns without NaN/Inf, scientific exception, same-turn feedback, same-`S` failure, K1 capital failure, or C1 accounting failure.

This classification means only that the frozen raw-payoff route remained executable over four treatment turns under the task's existing hard-stop rules. Raw materially worsened HJB convergence and produced very large finite drift/control magnitudes. This result is not evidence of steady-state convergence, economic admissibility, final KFE validity, K1B/K2 validity, or Results eligibility.

## Authority and identity

- live-main baseline: `9f973e627a3b7c7acac1d78c1b18b68a0c4a16c0`
- worktree: `D:\ProjectTemp\ch5-k1-raw-ra0-bootstrap-safety-20260912-001`
- branch: `codex/ch5-k1-raw-ra0-bootstrap-safety-20260912`
- accepted runtime payload SHA-256: `EBB9FD91F3D3CE5D46476FE7BF1D0662E26EEA5C87357E4B13907CC76EBE9355`
- external evidence root: `D:\ProjectTemp\ch5-k1-raw-ra0-bootstrap-safety-evidence-20260912-001`
- external manifest SHA-256: `69E85A9CAF6A23F5B7402821112F1A0465E2617F8A44ACEE167BC61D25B1E644`
- manifest readback: `1041/1041 PASS` (manifest file itself excluded from its entries)
- Results eligibility: `FALSE`

## Implementation and provenance

No production model, accepted K1 capital-network formula, firm, HJB, KFE, C1, labor, bound, calibration, grid, tolerance, solver, K1B, or K2 source was changed.

The task-bounded runner reuses the accepted K1A beta-distance-2/C1 route and adds only:

1. a hard 5-turn ceiling;
2. explicit modes `BOOTSTRAP_CLIPPED_RA`, `CONTROL_CLIPPED_RA`, and `RAW_PRIOR_COMPLETED_RA0`;
3. post-firm/next-state payoff plumbing.

Turn 1 uses the accepted entering clipped/source-used `ra` in both capital allocations. After each firm turn completes, the runner applies that same turn's own-path `ra` (Control) or `ra0` (Raw) to the already-frozen destination-by-origin `S`, then writes the result only into the next household state. It rebuilds through the accepted K1 engine and requires the payoff-only rebuild to preserve `S` and private-capital quantities bit-for-bit. Raw turn `n>=2` therefore enters HJB with exactly its own completed turn `n-1` `ra0 @ S`. No Control return is borrowed and no completed firm return enters the same-turn household solve.

## Pre-run gate

The gate passed before science:

- fresh live authority and task identity: PASS;
- initialization fields: `ra0=0/31`, `ra=31/31`, consistent with the Owner bootstrap freeze;
- Control/Raw runtime payload bytes: identical;
- both beta-distance `2`, beta-return `0`;
- common turn-1 clipped bootstrap: PASS;
- Raw turn-2 same-path completed turn-1 `ra0` wiring: PASS;
- Control turn-2 same-path completed turn-1 `ra` wiring: PASS;
- payoff switch leaves `S` and quantities bit-identical: PASS;
- source-faithful labor and C1 markers: PASS;
- K1B/smoothing/partial adjustment: OFF;
- raw payoff clipping/scaling/normalization/annualization/smoothing: none;
- zero-science focused suite: `33/33 PASS`.

The first Control launcher was rejected before `science_started.json`, HJB, KFE, trajectory state, or any scientific state update because its Phase-A receipt omitted the required zero-valued `initialization_observations` field. The receipt shape was corrected without changing scientific inputs, and the task's single permitted pre-state-update engineering retry was consumed. A later redundant no-overwrite preflight invocation correctly refused to overwrite the already-passed gate; it was not a trajectory/model call. Scientific retries remained zero.

## Call ledger

| Item | Control | Raw | Total |
|---|---:|---:|---:|
| trajectory invocations | 1 | 1 | 2 |
| completed turns | 5 | 5 | 10 |
| province updates | 155 | 155 | 310 |
| HJB calls | 155 | 155 | 310 |
| HJB direct solves | 11,084 | 13,616 | 24,700 |
| KFE calls/direct solves | 155/155 | 155/155 | 310/310 |
| labor-root/Brent calls | 124,000 | 124,000 | 248,000 |
| engineering retries | 1 | 0 | 1 |
| scientific retries | 0 | 0 | 0 |

MATLAB, standalone KFE experiment, K1B, K2, GE, annual, shock/IRF, and Results calls were all zero.

## Turn-1 common bootstrap

Control and Raw turn 1 were exactly reproducible:

- all compared province-level `rah`, C/L/A/B, private K, GovInv, total firm K, Y, wage, firm `ra0`, used `ra`, HJB iteration and statistic differences were exactly zero;
- all saved elements of value, consumption, labor, transfer `d`, adjustment cost, effective illiquid return, `mu_a`, `mu_b`, utility, and both policy-label arrays were identical;
- both had 20/31 converged HJB returns;
- both produced provenance-safe own-path firm `ra0` after turn 1.

No turn-1 difference is interpreted as a raw-payoff effect.

## Treatment turns 2-5

### Household `rah`

| Turn | Control median | Raw median | Raw-Control | Raw/Control |
|---:|---:|---:|---:|---:|
| 2 | 0.090000 | 0.477562 | 0.387562 | 5.306249 |
| 3 | 0.090000 | 0.506445 | 0.416445 | 5.627165 |
| 4 | 0.090000 | 0.504810 | 0.414810 | 5.609001 |
| 5 | 0.090000 | 0.503177 | 0.413177 | 5.590860 |

The increase is immediate at turn 2 and consistent with the prior static clipping audit. These values retain unresolved model-time/calendar and external-numeraire interpretation.

### HJB convergence

| Turn | Control converged | Raw converged | Control max statistic | Raw max statistic |
|---:|---:|---:|---:|---:|
| 2 | 13/31 | 4/31 | 2.409349 | 403.687024 |
| 3 | 13/31 | 4/31 | 0.467488 | 98.856013 |
| 4 | 12/31 | 4/31 | 1.175189 | 152.681212 |
| 5 | 11/31 | 0/31 | 17.995004 | 297.019203 |

Over treatment turns, Control converged in `49/124` province-turns and Raw in `12/124`. Raw therefore materially worsened HJB convergence immediately when the raw payoff first entered at turn 2, and all 31 Raw HJB returns were nonconverged at turn 5. The accepted continuation rule preserved these finite returns as `HJB_NONCONVERGED_DIAGNOSTIC_ONLY`; they are not scientific convergence evidence.

### Consumption, transfer and drifts

Raw median consumption versus Control was `8.8210 vs 9.7320`, `9.6013 vs 9.7927`, `12.0245 vs 9.6518`, and `10.6201 vs 10.1024` over turns 2-5. It remained finite but did not move monotonically.

Raw/Control maximum absolute illiquid-drift ratios were approximately `32.39`, `3.30`, `0.52`, and `24.12`. Liquid-drift ratios were approximately `1111.15`, `12.91`, `0.39`, and `542.94`. Raw maximum absolute liquid drift reached `1.293188164448144e12` at turn 3; maximum absolute illiquid transfer reached `2.736218759510891e6`. Control also contained large finite drifts, so these comparisons demonstrate severe numerical/control sensitivity rather than a clean stable policy response.

Saved HJB arrays contained zero NaN/Inf entries in both paths. Raw lower-`b` outward raw-drift counts were `0, 6, 9, 7` for turns 2-5, while Control was zero; upper-bound raw-drift counts were material in both paths. These are descriptive post-processing counts. The accepted HJB return object exposes no standalone KKT residual, so KKT is reported `UNAVAILABLE_IN_ACCEPTED_RETURN_OBJECT`; no new KKT PASS is claimed. No existing runtime hard-return validator or scientific exception fired.

## K1, C1, labor and KFE

- quantity/payoff same-`S`: all 310 province-turn rows PASS;
- same-turn feedback: `0/310`;
- raw source provenance: Raw turns 2-5 all point to the same path's immediately preceding completed firm `ra0`;
- maximum absolute national private-capital conservation residual: `2.9802322387695312e-08 MU`;
- maximum absolute origin capital-column residual: Control `5.587935447692871e-09 MU`, Raw `2.7939677238464355e-09 MU`;
- maximum absolute C1 accounting residual: Control `1.4901161193847656e-08 MU`, Raw `7.450580596923828e-09 MU`;
- total firm K/target remained approximately one in every turn;
- source-faithful labor was active for all rows; normalized labor remained off.

All `310/310` KFE returns remain `DIAGNOSTIC_ONLY`. Finite-box upper-`b` leakage plus MATLAB-style pinning remains an independent blocker.

## Interpretation and next gate

The bounded route survived all authorized turns without a formal hard stop, so the permitted short-horizon runtime-safety classification is supported. The result simultaneously shows that raw `ra0` causes a large household-payoff level jump, much poorer HJB convergence, and large finite control/drift changes. It does not justify proceeding automatically to K1B.

The next gate is a fresh independent ChatGPT Reviewer ACCEPT/REJECT of the exact candidate and external evidence. Reviewer/Owner should specifically decide whether the severe finite nonconvergence and drift sensitivity are acceptable as short-horizon mechanism evidence or require a new scientific-route decision before any further raw-payoff or K1B work.

Do not merge `main` or publish a successor task inside this Builder task. Results eligibility remains `FALSE`.
