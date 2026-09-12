# CH5 MP4C K1 — transfer-control raw-candidate census instrumented bounded diagnostic

Date: 2026-09-13.
Task ID: `CH5_MP4C_K1_TRANSFER_CONTROL_RAW_CANDIDATE_CENSUS_INSTRUMENTED_BOUNDED_DIAGNOSTIC`.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Type: bounded scientific runtime diagnostic with observation-only instrumentation.

## 1. Goal

Repeat the already accepted annual G1/G2 five-turn scientific design with **no science change**, while adding observation-only instrumentation that captures an exact cell-level census of all raw pre-selector transfer candidates needed to freeze a later temporary transfer-control admissibility ladder.

This task does not implement, activate, clip, reject, cap or otherwise alter any transfer candidate.

## 2. Authority reads

Fresh-fetch live `origin/main`, record actual SHA, and verify this exact task remains active. Read at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`;
- `docs/CH5_MP4C_K1_TRANSFER_CONTROL_TEMPORARY_ADMISSIBILITY_SAFEGUARD_FREEZE_CURRENT.md`;
- `docs/CH5_MP4C_K1_TRANSFER_CONTROL_ADMISSIBILITY_SAFEGUARD_ZERO_SCIENCE_DESIGN_ACCEPTANCE.md`;
- `docs/CH5_MP4C_K1_TRANSFER_CONTROL_ADMISSIBILITY_SAFEGUARD_ZERO_SCIENCE_DESIGN_REPORT.md`;
- `docs/CH5_MP4C_K1_G1_VS_G2_HA_HJB_INSTRUMENTED_BOUNDED_DIAGNOSTIC_ACCEPTANCE.md`;
- accepted annual/K1/price-guard freezes;
- active transfer FOC / policy / HJB source.

Do not redo data, parity, annual-time-base, capital-network or prior forensic audits.

## 3. Frozen science

Use exactly the already accepted annual G1/G2 science:

- `MODEL_TIME_BASE=ANNUAL_CONTINUOUS_TIME`;
- `rho=.05/year`;
- `rb=.02/year`;
- borrowing gap `.07/year`;
- firm/HJB `delta=.10/year`;
- `Q_z` off-diagonal `1/3/year`;
- `chi0=.1`;
- `chi1=2 years`;
- fixed theta;
- `beta_distance=2`;
- `beta_return=0`;
- accepted destination-by-origin `S`;
- same `S` for quantity and payoff;
- source-faithful labor;
- smoothing OFF;
- partial adjustment OFF;
- C1 unchanged;
- K1B/K2 OFF.

Price safeguards remain exactly:

- G1 HJB `r_a in [-.05,.20]`;
- G2 HJB `r_a in [-.10,.35]`;
- wage safeguard `wjt in [.8,1.3]` in both paths.

No transfer-control admissibility safeguard is active in this task.

## 4. Observation-only instrumentation contract

Instrumentation must expose/persist raw candidate values without changing any value used by accepted science.

For a given scientific input, instrumentation ON/OFF must produce identical scientific outputs within exact/accepted floating readback tolerance.

Instrumentation must not:

- clip/reject/cap/floor transfer candidates;
- reorder candidate construction or competition;
- modify selector scores/labels;
- alter transfer FOC;
- change derivative floors;
- change matrix/operator assembly;
- change solver stopping rules or call ordering;
- change equations, parameters, guards, grids, tolerances or boundary/KKT laws.

If exact raw arrays cannot be exposed without science change, stop before trajectory execution and report `BLOCKED_INSTRUMENTATION_REQUIRES_SCIENCE_CHANGE`.

## 5. Exact raw-candidate census

For every HJB call and every HJB iteration, persist the cell-level raw candidate values actually computed by the accepted source for every transfer branch that exists, including exact source names such as `d_bb`, `d_bf`, `d_fb`, `d_ff` where applicable.

Each raw observation must retain enough keys to recover:

- path G1/G2;
- outer turn;
- province name/index;
- HJB call identity;
- HJB iteration;
- branch identity;
- zero-based `(i_b,i_a,i_z)`;
- `b,a,z` coordinates or a stable grid hash + indices;
- raw candidate `d`;
- selected transfer label where available;
- whether this raw branch was ultimately selected at that cell;
- return-guard status;
- wage-guard status;
- boundary/interior classification;
- HJB final converged/nonconverged classification for that call.

Do not relabel summaries as raw observations.

## 6. Storage policy

The expected raw population is large. Full raw census should be persisted in the external evidence root, not committed wholesale to Git.

Preferred storage:

- chunked/compressed NPZ, Parquet, Arrow or equivalent lossless numeric format;
- deterministic file naming by path/turn/province/HJB call;
- manifest with SHA-256 for every census chunk;
- exact row/cell counts and readback verification.

Repository-tracked compact evidence should contain only summaries, manifests, threshold-count tables and priority witnesses needed for review.

No lossy quantile sketch may substitute for the exact raw census if full raw arrays are available without science change.

## 7. Pre-run parity gate

Before full trajectories prove on focused accepted fixtures that instrumentation ON/OFF has exact scientific parity for at least:

- HJB value/result arrays;
- consumption/labor;
- selected transfer `d`;
- adjustment cost;
- effective return;
- `mu_a`, `mu_b`;
- policy labels;
- operator/update;
- iteration count;
- convergence flag/statistic.

Science calls before this parity gate must be zero or limited to already authorized fixture-level parity calls that do not advance a trajectory state. Any output difference blocks the full runtime.

## 8. Runtime design

Run exactly two trajectories from byte-identical accepted initialization:

- G1: frozen return guard `[-.05,.20]`;
- G2: frozen return guard `[-.10,.35]`.

Each path: at most 5 completed outer turns.

Turn 1 remains the common bootstrap. Turns 2–5 use each path's own immediately prior completed annual raw `ra0 @ S`. No cross-path borrowing and no same-turn return feedback.

## 9. Runtime budget

Maximum:

- trajectory invocations: 2;
- G1 completed turns: <=5;
- G2 completed turns: <=5;
- HJB calls: <=310 total;
- KFE calls: <=310 total;
- MATLAB: 0;
- standalone KFE: 0;
- K1B/K2/GE/annual downstream/shock/IRF/Results: 0.

Scientific retries after state advancement: 0.

One pre-state-update engineering retry is allowed only for census serialization/output-shape defects with byte-identical scientific inputs.

## 10. Exact census validation

The final evidence must prove:

1. expected HJB call/iteration/cell/branch counts reconcile exactly with executed call ledgers;
2. every persisted raw candidate is finite/nonfinite exactly as computed;
3. recomputed per-array min/median/p95/p99/max/hash matches prior accepted instrumented summaries for overlapping calls where those summaries exist;
4. selected `d` reconstructed from the recorded selected branch matches the scientific selected-control output where selector semantics permit exact identity;
5. no census instrumentation value entered the scientific calculation.

Any mismatch blocks scientific interpretation and must be reported without tuning/retry.

## 11. Required exact distributions

Using the exact raw census, compute separately by branch and pooled:

- count / finite / NaN / +/-Inf;
- min/max;
- p50/p75/p90/p95/p97.5/p99/p99.5/p99.9/p99.95/p99.99;
- same quantiles for `abs(d)`;
- positive/negative/zero frequencies;
- positive-tail quantiles;
- absolute negative-tail quantiles;
- path G1/G2 partitions;
- turn 2 common-state partition;
- turns 3–5 path-history partition;
- interior/boundary partition;
- converged/nonconverged HJB-call partition;
- branch-specific distributions.

## 12. Threshold sensitivity grid

Compute **exact raw-cell** hit counts/shares at a preregistered diagnostic grid, at minimum symmetric:

- `D=1e2`;
- `3e2`;
- `1e3`;
- `3e3`;
- `1e4`;
- `3e4`;
- `1e5`;
- `3e5`;
- `1e6`;
- `3e6`;
- `1e7`;
- `1e8`.

Also compute separate positive and negative threshold exceedance counts.

These remain `DIAGNOSTIC_SENSITIVITY_GRID`, not frozen safeguard stages.

## 13. Scale-break analysis

Using exact raw observations, determine whether a stable numerical separation exists between central raw-candidate mass and explosive tail.

Use:

- ordered `abs(d)` tail gaps;
- log10 magnitude distribution;
- adjacent order-statistic ratios;
- quantile spacing;
- branch/path/turn robustness;
- sign-specific tails;
- selected versus nonselected branches;
- corresponding adjustment-cost scale.

Do not choose a threshold by maximizing past HJB convergence.

## 14. Semantics remain unimplemented

The prior accepted preferred design is:

`C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION`

This task may evaluate static consequences under candidate intervals, but must not implement it.

Candidate clipping remains nonpreferred and must not be activated.

## 15. Candidate ladder design output

If the exact raw census reveals a robust scale break, propose a 3–4 stage + OFF ladder for **Owner/Reviewer freeze only**.

Each stage must state:

- exact interval;
- symmetric/asymmetric rationale;
- exact raw hit share;
- exact selected-control hit share;
- branch-specific hit shares;
- G1/G2 shares;
- turn-2 shares;
- sign-specific shares;
- ordinary central-mass preservation;
- priority-checkpoint classification.

If no robust cutoff exists, return `NUMERIC_TRANSFER_SAFEGUARD_LADDER_REMAINS_OWNER_DECISION_REQUIRED` with options instead of invented precision.

## 16. Priority checkpoints

Explicitly include raw-census trajectories for:

- 湖北 turn 2 interior extreme;
- 山东 turn 2 high-statistic case;
- 广东 turn 2 large amplification;
- 辽宁 turn 2 raw positive extreme;
- 吉林 turn 2 raw negative extreme;
- 四川 turn 4 worst-HJB context;
- 云南 turn 4 G1-extreme/G2-improved context.

Do not claim that excluding any candidate would make HJB converge.

## 17. Price-bound monitoring

Continue Owner-required MATLAB-style monitoring for return and wage guards by province/turn. Transfer-candidate analysis must remain separate from existing return/wage saturation evidence.

## 18. Stop conditions

Stop affected path on:

- instrumentation changes scientific outputs;
- census count/hash reconciliation failure;
- NaN/Inf scientific hard-stop outside accepted behavior;
- scientific exception;
- return provenance/same-turn feedback failure;
- same-S/capital/C1 failure;
- unauthorized science/parameter/guard/grid/tolerance/solver change.

No tuning after stop.

## 19. Allowed tracked changes

Allowed only as diagnostics:

- observation-only raw-candidate census hooks/wrappers;
- bounded runner/finalizer;
- focused tests;
- report `docs/CH5_MP4C_K1_TRANSFER_CONTROL_RAW_CANDIDATE_CENSUS_INSTRUMENTED_BOUNDED_DIAGNOSTIC_REPORT.md`;
- compact evidence under `docs/evidence/ch5_mp4c_k1_transfer_control_raw_candidate_census/`;
- truthful CURRENT closeout docs.

Full raw census belongs in sealed external evidence, not Git.

Forbidden:

- any transfer candidate cap/rejection/clipping implementation;
- `chi0/chi1` change;
- derivative-floor change;
- return/wage guard change;
- HJB/KFE equation or boundary/KKT change;
- grid/tolerance/solver change;
- K1/C1/labor-science change;
- K1B/K2/Results.

## 20. Git/local safety

Fresh isolated worktree from live main. Explicit stage paths. No `git add .` / `git add -A`. No reset/clean/stash/force push. Preserve accepted evidence. One coherent commit, non-force push, one remote commit/report readback. Do not merge main and do not publish a successor task.

Do not touch the unrelated dirty `D:\Zotero-Analytical-Workflow` checkout.

## 21. Final response

Return:

- classification;
- actual baseline, branch/worktree/candidate SHA;
- changed paths;
- instrumentation parity gate;
- exact frozen science;
- call ledgers/completed turns/retries;
- raw-census population and manifest;
- exact branch-wise/raw pooled distributions;
- exact sign frequencies;
- exact diagnostic threshold hit shares;
- scale-break finding;
- selected-versus-raw comparison;
- priority checkpoints;
- return/wage monitoring;
- proposed ladder or unresolved Owner numeric choice;
- K1/C1/same-S/provenance gates;
- NaN/Inf/hard-stop status;
- KKT availability;
- KFE caveat;
- exactly one next gate;
- Results eligibility=`FALSE`.

Stop. Do not implement the safeguard.
