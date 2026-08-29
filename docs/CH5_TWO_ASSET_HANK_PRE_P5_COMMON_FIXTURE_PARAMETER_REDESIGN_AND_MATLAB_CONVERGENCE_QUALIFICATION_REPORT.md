# Chapter 5 two-asset HANK pre-P5 common-fixture redesign and MATLAB qualification report

## Terminal classification

`COMMON_FIXTURE_PARAMETER_REDESIGN_BLOCKED_PRE_SCIENTIFIC__P5_BLOCKED`

Named Phase A blocker: `COMMON_FIXTURE_REDESIGN_BLOCKED_LABOR_MAPPING_UNRESOLVED`.

The accepted source proves that Python `phi` and MATLAB `frisch_l` are reciprocal semantic fields, not the same field. Therefore task-specified Candidate 2 (`phi=5`, `frisch_l=5`) cannot be certified as a common inverse-Frisch object. The task expressly forbids substituting another number and requires stopping before any scientific run when this mapping is not confirmed. All MATLAB qualification counts are zero. P5 remains blocked.

## Live authority and continuity

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Live start `origin/main`: `c533504ce2a42b16e9f92e0a789f6991c88df0a8`.
- Live task: `CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_PARAMETER_REDESIGN_AND_MATLAB_CONVERGENCE_QUALIFICATION`.
- Accepted Python baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`.
- Required `git diff --name-only <baseline> -- src tests`: empty (`PASS`).

## MATLAB and cache identities

| object | SHA-256 | result |
|---|---|---|
| accepted `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | PASS |
| accepted `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` | PASS |
| production `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` | PASS |
| accepted `lab_solve2.m` | `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20` | PASS |
| read-only 2016 native cache | `FC58289EC695A6B7583405CC7F6A7FC3C88B0512F0C93CEAB76F3442CA9F771A` | PASS |

The cache was read only for `C2016-P10` provenance. The diagnostic-patch HJB was not executed.

## Phase A source and native audit

The accepted MATLAB HJB reads `ga`, `rho`, and `frisch_l` directly. Its household labor objects are:

```text
l = (V_b * net_wage / alphal)^frisch_l
labor disutility exponent = 1 + 1/frisch_l
```

Accepted Python defines:

```text
l = (V_b * net_wage / labor_weight)^(1/phi)
labor disutility exponent = 1 + phi
```

Hence the exact semantic mapping is:

`Python phi = 1 / MATLAB frisch_l`.

The native cache independently confirms this: `param.phi_l=5` (inverse Frisch) and `param.frisch_l=0.2` (Frisch elasticity). It does not support setting both Python `phi` and MATLAB `frisch_l` to 5.

Selected native reference values were:

| object | C2016-P10 value |
|---|---:|
| `ga`, `rho`, `alphal` | 2, 0.05, 1 |
| `phi_l`, `frisch_l` | 5, 0.2 |
| `chi0`, `chi1`, `a_bar` | 0.1, 2, `1e-6` |
| `fixcost`, `fixcost2` | 0, 0 |
| asset grid | `b: 20 nodes [-2,5]`; `a: 20 nodes [0,10]` |
| `rb`, saved `rah` | 0.02, 0.040026998056627239 |
| `w`, `tau`, `Tt`, `rb_gap` | 13.084227346448168, 0.05, 0.1, 0.07 |
| saved `convergent` | 1 |

The accepted MATLAB main sets `convergent=1` only when its iteration change falls below `crit`. Its stationary system is solved at line 340 after replacing one row; the predecessor warning arose at that solve. This confirms the warning location but not an independent causal mechanism.

## Failure-mechanism classification

| mechanism | classification | evidence-bounded interpretation |
|---|---|---|
| low `rah` relative to `rho` | `SUPPORTED_PRIMARY` | Pre-registered first joint-wedge hypothesis; not sufficient alone because the native reference converged near 0.04. |
| no borrowing region in `b` | `SUPPORTED_PRIMARY` | Failed object collapsed at the lower liquid boundary; native support includes `b=-2`. |
| narrow `a` support | `SUPPORTED_PRIMARY` | Failed object collapsed at the lower illiquid boundary; native support extends to `a=10`. |
| coarse asset grids | `SUPPORTED_SECONDARY` | Failed grid was 5x5 versus native 20x20, but resolution was not separately isolated. |
| labor-curvature mismatch | `SUPPORTED_SECONDARY` | Failed fixture used elasticity 1; native mapping is inverse curvature 5 / elasticity 0.2. |
| adjustment-cost parameters | `POSSIBLE_NOT_ESTABLISHED` | Native `(0.1,2,1e-6)` differs from synthetic `(0.05,1,0.5)`, but the task did not isolate this dimension. |
| common-Q connectivity | `NOT_SUPPORTED` | Frozen two-state Q is irreducible; no evidence identifies productivity switching as the primary failure. |
| stationary near-singularity | `SUPPORTED_SECONDARY` | Observed after non-convergence and boundary collapse; treated as a consequence, not an established root cause. |

These labels do not infer causality from one failed run. The supported-primary entries describe the pre-registered joint boundary/calibration mechanism, not independent causal proofs.

## Frozen three-candidate manifest

External manifest: `candidate_manifest.json`, 3479 bytes, SHA-256 `B06DDE32AD1FD7FADBB2DE41E7E5D5A3EC854908ED35F12CA91B0F161388353D`.

Common to all candidates: `rho=0.05`, `ga/gamma_c=2`, labor weight/`alphal=1`, `chi0=0.05`, `chi1=1`, `a_bar=0.5`, `rb=0.03`, `w=1`, `tau=0`, migration cost=0, `Tt=0`, `rb_gap=0`, `fixcost=fixcost2=0`, qualification `rah=0.055`, future unexecuted companion rate `0.056`, `z=[0.8,1.3]`, and `Q=[[-0.4,0.4],[0.3,-0.3]]`.

| candidate | labor fields | `a` grid | `b` grid | states | Phase A status |
|---|---|---|---|---:|---|
| 1 | `phi=1`, `frisch_l=1` | `[0,0.5,1,1.5,2]` | `[0,1.25,2.5,3.75,5]` | 50 | frozen; not run because global Candidate-2 mapping gate blocks Phase B |
| 2 | `phi=5`, `frisch_l=5` | Candidate 1 grid | Candidate 1 grid | 50 | frozen exactly as tasked; labor semantic gate FAIL |
| 3 | `phi=5`, `frisch_l=5` | `[0,1,2,3,4,5,6,7,8,9,10]` | `[-2,-1.3,-0.6,0.1,0.8,1.5,2.2,2.9,3.6,4.3,5]` | 242 | MATLAB/Python grid interface PASS; inherited labor semantic gate FAIL |

Candidate 3 has uniform `da=1` and `db=0.7`. Static construction proved accepted MATLAB `linspace` and accepted Python `GridSpec` can represent its exact arrays without source mutation.

The run order, maximum three calls, one-call-per-candidate rule, complete frozen qualification criteria, and all exact parameters are included in the hashed manifest. No candidate was edited after observing scientific output because no scientific output was generated.

## Qualification execution and diagnostics

| candidate | MATLAB scientific calls | convergence | warnings | mass/aggregate criteria | qualification |
|---|---:|---|---|---|---|
| 1 | 0 | NOT RUN | NOT RUN | NOT RUN | blocked before Phase B |
| 2 | 0 | NOT RUN | NOT RUN | NOT RUN | invalid common labor mapping |
| 3 | 0 | NOT RUN | NOT RUN | NOT RUN | invalid common labor mapping |

Python HJB/KFE/steady-state calls: 0. MATLAB perturbation `0.056` calls: 0. Outer MATLAB equilibrium/turn/shock calls: 0.

No candidate raw output, reconstructed scientific initial value, warning capture, mass diagnostic, or qualification aggregate exists. Inventing any of these would violate the pre-scientific stop.

## Files read and written

Read:

- live task, `AGENTS.md`, both required project rules;
- the six required handoff/parity/source/snapshot/controlled-execution reports;
- accepted Python `contracts.py` and `economics.py` labor/grid contracts;
- accepted MATLAB HJB, cost, FOC and labor-initialization helper;
- original caller/config evidence in `multi_prov_HANK_12sts.m`;
- read-only `C2016-P10` fields from the hashed 2016 cache.

Repository write: only this report.

External artifact root:

`D:\ProjectTemp\ch5-pre-p5-common-fixture-qualification-artifacts-20260829-182807`

| external artifact | SHA-256 |
|---|---|
| `candidate_manifest.json` | `B06DDE32AD1FD7FADBB2DE41E7E5D5A3EC854908ED35F12CA91B0F161388353D` |
| `phase_a_audit.json` | `312AB785246D4FCE6C07F3C40D37791610524541E4E1BD73C0111C2C17B07160` |

Both JSON artifacts passed strict parse/read-back. No raw MAT, model output, log, cache, or scientific harness was created.

## Forbidden-operation check

- Python `src/tests` modified: no.
- MATLAB production source modified: no.
- diagnostic-patch tree/cache modified: no.
- third scientific adapter added: no.
- P1-P4 rerun: no.
- Python HJB/KFE/steady state run: no.
- MATLAB qualification or companion-rate run: no.
- four-run parity entered: no.
- candidate changed after scientific execution: no scientific execution occurred.
- solver/tolerance changed or switched: no.
- outer equilibrium, multi-province, AR(1), transition, IRF, calibration extension, dynamics, or Results entered: no.
- P5 acceptance inferred or issued: no.

## Acceptance level and recommended next gate

Acceptance level: Phase A diagnosis, native audit, three-candidate pre-registration, and interface checks are complete; MATLAB convergence qualification is **not authorized to proceed under the unresolved task-specified labor mapping**. P5 is explicitly **BLOCKED**.

Recommended next gate:

`CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_LABOR_CURVATURE_MAPPING_CORRECTION_AND_MATLAB_REQUALIFICATION`

That Owner/reviewer gate should explicitly decide whether Candidate 2/3 must use the scientifically common mapping `Python phi=5` and `MATLAB frisch_l=0.2`, then republish an exact candidate order and fresh one-shot MATLAB qualification budget. This report does not create or execute that successor and does not authorize the final four-run parity experiment.
