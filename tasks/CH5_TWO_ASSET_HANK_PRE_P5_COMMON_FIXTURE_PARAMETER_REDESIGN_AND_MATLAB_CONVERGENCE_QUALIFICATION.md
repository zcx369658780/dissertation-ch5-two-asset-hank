# CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_PARAMETER_REDESIGN_AND_MATLAB_CONVERGENCE_QUALIFICATION

Date: 2026-08-29

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Task purpose

Diagnose why the most recent synthetic common MATLAB fixture failed its own convergence gate, redesign the common fixture in a pre-registered and auditable way, and qualify the first candidate that is numerically valid for the accepted original MATLAB household solver.

This task is **not** the final MATLAB-Python parity experiment.

It must not execute Python household/KFE solves and must not execute the four-run MATLAB/Python baseline/perturbation sequence.

P5 remains blocked throughout this task.

## 2. Live repository authority

GitHub `main` is the sole repository-state authority.

Task-authoring parent observed by the reviewer before publication:

`6321c191f1b6bb045afad5ea086365e3391b22f1`

Do not assume that SHA is still live when execution begins.

Before any local scientific work:

1. fresh-fetch `origin/main`;
2. confirm this exact task file exists on live `main`;
3. record live `origin/main` SHA;
4. read the required governance and evidence files below;
5. verify accepted Python scientific/test continuity against the accepted baseline.

Accepted Python scientific baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

Required continuity check:

`git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`

It must be empty. If not empty, stop before Phase A candidate freeze and report a source-drift blocker.

## 3. Required GitHub reads

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_AFTER_PRE_P5_SAME_INPUT_CONVERGENCE_BLOCK_2026_08_29.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_RATE_MATCHED_INITIALIZATION_EXECUTION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_HOUSEHOLD_CALL_SNAPSHOT_AUTHORITY_PREP_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_PERTURBATION_EXECUTION_REPORT.md`

P1-P4 are accepted evidence and must not be rerun.

## 4. Frozen scientific background

Current terminal state:

`TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_RATE_MATCHED_NEEDS_DIAGNOSTIC__P5_BLOCKED`

Latest consumed scientific run:

- accepted original MATLAB common baseline only;
- `rah=0.040`;
- exactly one run;
- `convergent=false`;
- near-singular stationary solve warning;
- `RCOND=1.280574e-18`;
- returned descriptive `A_hh≈0`, `B_hh≈0`;
- Python did not run;
- no perturbation run occurred.

These outputs are failure diagnostics, not parity evidence.

Accepted structural adapters remain exactly:

### O1 MATLAB low-a FOC helper

SHA-256:

`B28E73F439CB3DD40B2A6C00BE5D3E56FD7C4254DF468B4E2C0DCCED06DB7315`

Only scientifically material change:

`a -> max(a,a_bar)`

### O2 Python common-Q adapter

SHA-256:

`D94848535E68C0CBF9BA51C91016E8DD91809221EEEA3F21DC4EE5D96EBE9225`

No third scientific adapter is authorized.

## 5. MATLAB authority and local safety

Designated original MATLAB tree:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

It is read-only.

Required accepted identities:

- `HANK_2ASSETS_HJB.m`
  - `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_cost.m`
  - `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- production `HANK3_FOC.m`
  - `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`
- `lab_solve2.m`
  - `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`

The adjacent diagnostic-patch/cache tree may be read only to recover already-saved known-convergent parameter/grid provenance. It must not be executed as the scientific HJB source and must not be modified.

Canonical known-convergent reference already accepted for read-only use:

- cache: `Multi_Province_12sts_2016.mat`
- candidate: `C2016-P10`
- province: Jiangsu / P10
- saved `results{10}.convergent=1`
- saved `results{10}.rah=0.040026998056627239`

The fact that this native snapshot converged near `rah=0.04` means the latest failure must **not** be diagnosed as “rah=0.04 alone is necessarily invalid.”

## 6. Reviewer diagnostic priority

The highest-priority mechanism is a **joint boundary/calibration degeneracy of the synthetic common fixture**, not a Python solver failure.

The diagnostic order is frozen as follows:

1. **Return/discount wedge first.** The failed synthetic fixture has `rho=0.05`, `r_b=0.03`, `rah=0.040`, and returned nearly zero aggregate holdings in both asset dimensions. The dissertation route describes a preferred/stable illiquid-return region around `0.04-0.07` and requires `r_a>r_b`; moving the common test rate into the interior of that range is the first minimal intervention.
2. **Labor-curvature mapping second.** The failed common fixture used `phi/frisch_l=1`, while the Chapter 5 dissertation calibration uses inverse Frisch curvature `5`. The exact MATLAB/Python semantic mapping must be source-verified before using the second candidate.
3. **Asset support / borrowing / resolution third.** The failed fixture used only five nodes on `a in [0,2]` and five non-borrowing nodes on `b in [0,5]`. This is much narrower than the known native-style support and may force the stationary object toward the joint lower boundary or create weakly connected/transient asset layers.
4. **Adjustment technology is an audited secondary mechanism.** Fresh-read the exact native `chi0`, `chi1`, and `a_bar`, but do not add a fourth run or silently change these values in Candidates 1-3. If all three candidates fail, report the native adjustment values and whether they are a plausible next redesign dimension.
5. **Common two-state productivity must remain common.** Keep the accepted common productivity object `z=[0.8,1.3]`, `Q_z_common=[[-0.4,0.4],[0.3,-0.3]]`; do not redesign productivity in this task.

This ordering is pre-registered to prevent “try parameters until it converges.”

## 7. Phase A — read-only diagnosis and candidate freeze

Phase A is mandatory and must finish before any MATLAB scientific qualification call.

### A1. Source audit

Read the accepted original MATLAB HJB and the minimum caller/config/cache material needed to verify:

- exact meaning of `ga`;
- exact meaning of `frisch_l`;
- how labor curvature enters the FOC/policy;
- exact `rho` field used by HJB;
- exact `rb`, `rah`, `w`, `tau`, `Tt`, `rb_gap` inputs;
- exact native `chi0`, `chi1`, `a_bar` for the domestic branch;
- exact native asset-grid bounds/node counts for the selected converged snapshot;
- how `convergent` is set;
- stationary solve location and warning behavior.

Do not change source.

### A2. Failure-mechanism audit

Using source equations, existing persisted failed-run evidence, and read-only native configuration evidence, classify each mechanism as:

- `SUPPORTED_PRIMARY`
- `SUPPORTED_SECONDARY`
- `POSSIBLE_NOT_ESTABLISHED`
- `NOT_SUPPORTED`

for:

- low `rah` relative to `rho`;
- absence of a borrowing region in `b`;
- narrow `a` support;
- coarse asset grids;
- labor-curvature mismatch (`1` versus native/dissertation mapping);
- adjustment-cost parameters;
- common-Q connectivity;
- stationary-system near-singularity as consequence versus primary cause.

Do not infer causality from one failed run alone.

### A3. Pre-register exactly three candidate fixtures

Before the first scientific MATLAB call, create a local text-first `candidate_manifest.json` or equivalent JSON/Markdown manifest containing all three candidates, their exact arrays/parameters, order, acceptance rules, and SHA-256.

All three candidates must be frozen before any scientific output is observed.

No candidate may be edited after the first scientific call begins.

#### Candidate 1 — minimal return repair

Start from the failed common gamma2 fixture and change only:

- qualification `rah = 0.055`.

Record the future parity companion rate as `0.056`, but **do not run 0.056 in this task**.

Keep exactly:

- `rho=0.05`
- `ga/gamma_c=2.0`
- `phi/frisch_l=1.0`
- labor weight `1.0`
- `chi0=0.05`
- `chi1=1.0`
- `a_bar=0.5`
- `rb=0.03`
- `w=1.0`
- `tau=0`
- migration cost `0`
- `Tt=0`
- `rb_gap=0`
- `fixcost=0`
- `fixcost2=0`
- `a=[0,0.5,1.0,1.5,2.0]`
- `b=[0,1.25,2.5,3.75,5.0]`
- `z=[0.8,1.3]`
- `Q_z_common=[[-0.4,0.4],[0.3,-0.3]]`

This candidate isolates the Owner/reviewer hypothesis that the previous common illiquid return sat too close to the low edge for this synthetic object.

#### Candidate 2 — return repair plus dissertation/native labor curvature

Candidate 2 is identical to Candidate 1 except:

- `phi = 5.0`
- MATLAB `frisch_l = 5.0`

This candidate is valid only if Phase A source audit confirms that the two fields represent the same inverse-Frisch curvature in the accepted common labor FOC.

If the mapping is not confirmed, stop before any scientific run with:

`COMMON_FIXTURE_REDESIGN_BLOCKED_LABOR_MAPPING_UNRESOLVED`

Do not substitute another number.

#### Candidate 3 — return + labor repair + native-style asset support/resolution

Candidate 3 is identical to Candidate 2 except the asset grids become:

- `a = [0,1,2,3,4,5,6,7,8,9,10]`
- `b = [-2,-1.3,-0.6,0.1,0.8,1.5,2.2,2.9,3.6,4.3,5.0]`

This gives:

- `Na=11`
- `Nb=11`
- `Nz=2`
- `242` states
- uniform `da=1.0`
- uniform `db=0.7`

The grid deliberately restores a borrowing region and materially wider illiquid support while keeping a bounded, auditable state count.

Before freezing Candidate 3, verify both accepted MATLAB and accepted Python grid contracts can represent these exact arrays without production-source mutation. If either cannot, stop pre-scientifically and report the interface blocker. Do not silently alter the grid.

### A4. Candidate-order freeze

The run order is exactly:

1. Candidate 1
2. Candidate 2 only if Candidate 1 fails qualification
3. Candidate 3 only if Candidates 1 and 2 fail qualification

The first fully qualified candidate is frozen and all later candidates remain unrun.

Maximum MATLAB scientific qualification calls in this task: **3**.

Each candidate may be called at most once.

No rerun is authorized.

## 8. Phase B — MATLAB convergence qualification only

Only after Phase A candidate manifest is fully frozen and hashed may Phase B begin.

For each entered candidate:

1. reconstruct the rate-matched initial value using the already accepted initialization protocol for that candidate rate;
2. use the accepted original MATLAB `HANK_2ASSETS_HJB.m`;
3. use only the accepted O1 external test helper where required by the already accepted common-equation protocol;
4. use a timestamped no-overwrite external artifact directory;
5. persist raw output immediately after the HJB call returns;
6. capture/read back summary and raw identities;
7. record warnings, including any singular/nearly-singular stationary-system warning;
8. apply the frozen qualification criteria below;
9. stop immediately at the first qualified candidate or after Candidate 3 fails.

Do not run Python.

Do not run a perturbation rate.

Do not compare languages.

## 9. Frozen qualification criteria

A candidate is `QUALIFIED` only if all are true:

1. MATLAB returns `convergent=true`.
2. All exposed household arrays and stationary mass are finite.
3. Stationary mass sums to `1` within absolute tolerance `1e-10`.
4. Minimum stationary mass is at least `-1e-12`.
5. No MATLAB singular/nearly-singular warning is emitted by the stationary solve for that run.
6. The stationary distribution is not a complete joint-lower-bound collapse:
   - mass on states with `a > a_min` is at least `1e-4`;
   - mass on states with `b > b_min` is at least `1e-4`.
7. Returned aggregate objects needed for later parity (`Ct/Lt/At/Bt` or their accepted exposed equivalents) are finite.
8. Source/adapters/harness identities remain unchanged from the frozen pre-scientific manifest.

If `convergent=true` but criterion 5 or 6 fails, classify the candidate:

`CONVERGED_BUT_NUMERICALLY_UNQUALIFIED`

and proceed to the next pre-frozen candidate without editing anything.

Do not widen tolerances after seeing output.

## 10. Diagnostics to persist for every entered candidate

Persist at minimum:

- candidate ID and full manifest;
- exact MATLAB command/call signature;
- source hashes;
- O1 helper hash;
- reconstructed initialization hash;
- raw MATLAB output hash;
- convergence flag;
- warning message/identifier and RCOND if exposed;
- mass sum;
- minimum mass;
- mass above lower `a` bound;
- mass above lower `b` bound;
- `C_hh`;
- raw hours `H_hh` if derivable from exposed arrays without a new scientific adapter;
- effective labor `L_hh`;
- `A_hh`;
- `B_hh`;
- whether the candidate passed every frozen criterion.

These aggregates are qualification diagnostics only. They are not cross-language parity evidence.

## 11. Explicitly forbidden operations

Do not:

- modify accepted Python `src/` or `tests/`;
- modify MATLAB production source;
- modify the diagnostic-patch tree or canonical caches;
- add a third scientific adapter;
- rerun P1-P4;
- run Python HJB/KFE/steady state;
- run future parity companion rate `0.056`;
- run any MATLAB-Python four-run parity sequence;
- change candidate parameters after scientific execution starts;
- change solver tolerances;
- widen acceptance tolerances;
- switch solvers;
- run outer multi-province equilibrium, AR(1), transition, IRF, calibration extension, or Results;
- infer P5 acceptance;
- overwrite prior artifacts;
- use `git add .` or `git add -A`;
- commit raw `.mat`, large output, logs, caches, or local artifacts.

## 12. Allowed repository write

The only repository file this task may create/update is:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_PARAMETER_REDESIGN_AND_MATLAB_CONVERGENCE_QUALIFICATION_REPORT.md`

The report must be text-first and must not embed raw binary output.

External timestamped artifacts may be created outside the repository under a no-overwrite temporary/project-temp root.

## 13. Commit and push authority

If the task reaches a terminal classification and repository state is otherwise clean:

- explicitly stage only the single report path above;
- commit that report;
- push to `main`;
- report commit SHA and final `origin/main`;
- report final `git status --short --untracked-files=all`.

Do not commit any other path.

## 14. Required terminal classifications

### Qualified

If the first fully qualified candidate is found:

`COMMON_FIXTURE_QUALIFIED_FOR_FINAL_SAME_INPUT_PARITY__P5_STILL_BLOCKED`

The report must freeze:

- candidate ID;
- exact parameter/grid manifest;
- manifest SHA-256;
- qualification MATLAB raw-output SHA-256;
- convergence/warning/mass diagnostics;
- future baseline rate `0.055` and perturbation rate `0.056` only if Candidate 1/2/3 uses that frozen rate pair;
- the fact that Python has not yet been executed on this fixture.

Recommended next gate only:

`CH5_TWO_ASSET_HANK_PRE_P5_FINAL_TRUE_SAME_INPUT_FOUR_RUN_PARITY_ON_QUALIFIED_FIXTURE`

Do not create or execute that next task.

### None qualified

If all three pre-frozen candidates fail qualification:

`COMMON_FIXTURE_PARAMETER_REDESIGN_NO_CANDIDATE_QUALIFIED__P5_BLOCKED`

Report the failure criterion for each candidate and the Phase A audit of native adjustment parameters. Recommend a new Owner/reviewer redesign gate; do not invent Candidate 4 after seeing results.

### Pre-scientific blocker

If source identity, Python continuity, labor mapping, grid representation, adapter identity, or candidate-freeze requirements fail before the first MATLAB call:

`COMMON_FIXTURE_PARAMETER_REDESIGN_BLOCKED_PRE_SCIENTIFIC__P5_BLOCKED`

No MATLAB scientific call may occur after such a blocker.

## 15. Final response requirements

Report:

- terminal classification;
- live start `origin/main`;
- accepted Python baseline continuity result;
- MATLAB source identity result;
- Phase A mechanism-classification table;
- exact three-candidate frozen manifest and manifest hash;
- candidate execution counts;
- per-candidate qualification table;
- selected qualified candidate, if any;
- files read/written;
- external artifact root and important hashes;
- forbidden-operation check;
- commit SHA / final `origin/main` if report was committed;
- git status;
- acceptance level;
- recommended next gate.

P5 must remain explicitly `BLOCKED`.