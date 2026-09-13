# CH5 MP4C K1 — transfer-control D1=1e5 bounded runtime diagnostic

Date: 2026-09-13
Task ID: `CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC`
Type: bounded scientific runtime diagnostic.

## Goal
Compare fresh G2 control versus G2+D1 from byte-identical accepted initialization. Turn 1 is identical with D1 OFF. From turn 2 onward, control keeps D1 OFF and treatment activates the Owner-frozen D1 transfer-candidate admissibility safeguard. Turn 2 is the common-entering-state causal window; turns 3-5 are path-history propagation.

## Mandatory authority
Read live `AGENTS.md`, rule index, project status, `docs/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_ADMISSIBILITY_FREEZE_CURRENT.md`, raw-census acceptance/report, prior safeguard freeze, accepted annual/K1/price-guard freezes, and active transfer/HJB/policy source.

## Frozen science
Keep annual continuous time; `rho=.05`, `rb=.02`, borrowing gap `.07`, `delta=.10`, `Q_z=1/3`, `chi0=.1`, `chi1=2`, fixed theta, `beta_distance=2`, `beta_return=0`, accepted `S`, same-S quantity/payoff, source-faithful labor, C1 unchanged, smoothing/partial-adjustment OFF, K1B/K2 OFF.

Both paths use G2 `r_a in [-.10,.35]` and wage safeguard `wjt in [.8,1.3]`. No other parameter, guard, derivative floor, equation, boundary/KKT law, grid, tolerance or solver change is authorized.

## Exact D1 contract
Treatment from turn 2 uses symmetric `[-1e5,+1e5]`, inclusive: `abs(d_raw)<=1e5` admissible, `abs(d_raw)>1e5` inadmissible. Persist raw FOC candidate unchanged. Inadmissible raw branch is excluded from selector competition. Do not clip. Do not manufacture a replacement candidate. Existing zero-transfer/no-transfer option and all other admissible branches remain under accepted selector semantics. Keep existing feasibility/boundary rejection reasons separate from D1 rejection.

## Pre-run gates
Before trajectories prove: D1 OFF exact-parity with accepted outputs; raw candidates identical before eligibility; no-candidate-hit fixture gives D1 ON/OFF exact equality; a pure selector fixture confirms rejected raw value remains unchanged, no clipped endpoint is created, and existing zero/other admissible branches remain available. Fixture calls must not advance trajectory state.

## Runtime
Run exactly two trajectories, max 5 turns each.

Control C: turn1 common bootstrap D1 OFF; turns2-5 G2 with D1 OFF.
Treatment D1: turn1 same bootstrap D1 OFF; turns2-5 same G2 plus D1.
Each path uses own prior-completed annual raw `ra0@S`; no cross-path borrowing; no same-turn feedback.

Budget: 2 trajectories; <=310 HJB; <=310 KFE; MATLAB/standalone-KFE/K1B/K2/GE/downstream/IRF/Results all 0; scientific retries after state advancement 0. One pre-state-update engineering retry only for serialization/output-shape defects with byte-identical scientific inputs.

## Turn-2 common-state checks
Before treatment confirm equality of completed turn1 state, entering household value state/hash, raw annual `ra0`, converted `rah`, consumed G2 `r_a`, wage input/status, grid/parameters/numerics, and raw transfer candidates before D1 eligibility.

Record first D1 rejection by province/iteration/cell/branch; whether rejected branch would otherwise win; whether final control switches to existing zero or another admissible nonzero branch; and immediate differences in selected `d`, cost, `mu_a`, `mu_b`, drifts, operator, `V_new`, statistic and labels.

Turns3-5 must be labelled `PATH_HISTORY_PROPAGATION__NOT_SAME_STATE_CAUSAL`.

## Mandatory D1 receipts
Record raw branch values, sign, D1 admissibility, existing feasibility/boundary status, previous-winning-branch rejected flag, selected final branch/control, fallback-to-zero flag, switch-to-other-nonzero flag, and D1 hit counts/shares by branch/sign/province/turn/iteration.

Continue MATLAB-style return/wage boundary monitoring by province/turn.

## Diagnostics
Per path/turn report HJB convergence/ceiling/statistics, selected-transfer distribution/extrema, adjustment-cost tails, `mu_a/mu_b`, drift extrema, consumption/labor, policy labels, material outward boundary counts, NaN/Inf, outer residuals and KFE classification.

Priority checkpoints: 湖北 T2, 山东 T2, 广东 T2, 辽宁 T2, 吉林 T2, 四川 T4, 云南 T4 where path history permits.

Hard stop on D1 OFF parity failure, any raw-candidate mutation, clipping/manufactured candidate, scientific exception/nonfinite hard-stop, provenance/same-S/capital/C1 failure, or unauthorized science change. No tuning after stop.

## Required questions
Answer whether D1 improves HJB convergence; reduces transfer/cost/drift heavy-tail stress; introduces rejection/fallback instability; how often rejected branches would otherwise win; how often selection moves to zero versus another nonzero branch; whether effects concentrate in nonconverged calls; whether K1/C1/provenance and price-monitoring remain intact; and whether longer D1 is supported. Do not auto-authorize any wider D stage.

## Allowed changes
Only D1 eligibility filter with OFF mode exact-parity, task-owned diagnostics/receipts, bounded runner/finalizer, focused tests, report `docs/CH5_MP4C_K1_TRANSFER_CONTROL_D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC_REPORT.md`, compact evidence under `docs/evidence/ch5_mp4c_k1_transfer_control_d1_1e5/`, and truthful CURRENT closeout docs.

Forbidden: clipping; any other D threshold; D2/D3/OFF runtime; `chi0/chi1` or derivative-floor change; return/wage guard change; HJB/KFE/boundary/KKT/grid/tolerance/solver/K1/C1/labor change; K1B/K2/Results.

Fresh isolated worktree. Explicit stage paths. No `git add .` / `git add -A`, reset, clean, stash or force push. One coherent commit, non-force push, one remote readback. Do not merge main or publish successor task. Do not touch `D:\Zotero-Analytical-Workflow`.

Final response must include classification, baseline/branch/worktree/candidate SHA, changed paths, parity gates, call ledger, turn1 equality, turn2 immediate D1 response, D1 hit/switch/fallback counts, HJB and control-stress comparison, price monitoring, accounting/provenance, hard stops, KKT/KFE caveat, whether longer D1 is supported, exactly one next gate, and `Results eligibility=FALSE`.
