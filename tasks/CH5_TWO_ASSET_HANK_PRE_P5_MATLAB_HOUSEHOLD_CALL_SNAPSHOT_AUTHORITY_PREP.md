# CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_HOUSEHOLD_CALL_SNAPSHOT_AUTHORITY_PREP

## Task

Resolve the MATLAB baseline-authority ambiguity exposed by the blocked pre-P5 native aggregate robustness attempt, without running any model.

The Owner's intended robustness question is specifically about the two-asset **HA household block**:

- compute household aggregate consumption and labor, `C_hh` and `L_hh`;
- compare a baseline with `r_a/rah = 0.040` against a perturbation `0.041`;
- hold every other household-block input fixed.

Therefore this task must prepare an auditable **frozen household-call snapshot authority** for MATLAB, rather than silently choosing a full multi-province general-equilibrium year/route.

This is read-only source/data archaeology and authority preparation only. It does not authorize MATLAB or Python scientific execution, P5 acceptance, AR(1), transition, IRF, calibration extension, or Results work.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Accepted evidence

Blocked robustness report commit:

`4612cf045fdf0233300f64005417a1ddc0a998e8`

Accepted P1-P4 parity evidence commit:

`daa3e60ff97828ec80fb2e83bee863eb4aa632a4`

Accepted Python scientific baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

P1-P4 evidence remains accepted and must not be rerun.

## Required live GitHub read-back

Fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_AGGREGATE_CL_AND_RA_PERTURBATION_ROBUSTNESS_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`

Verify Python `src/tests` remain unchanged from the accepted baseline. If not, stop:

`BLOCKED_MATLAB_HA_SNAPSHOT_PREP_PYTHON_SOURCE_DRIFT`

## MATLAB source identity

Read-only verify the designated source tree:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Require the already accepted source identities for:

- `HANK_2ASSETS_HJB.m`
- `HANK3_cost.m`
- `HANK3_FOC.m`

Also fingerprint all caller/configuration files actually used in the authority map, including at minimum:

- `HANK_mp_1turn.m`
- `HANK_mp_1eq.m`
- `mpHANK_equilibrium_2000.m`
- `multi_prov_HANK_12sts.m`
- relevant top-level entry files

## Scientific experiment to prepare

The successor experiment should be a controlled **household-call perturbation**, not a re-equilibrated full multi-province economy.

For one frozen MATLAB household input tuple, the future experiment will invoke:

`HANK_2ASSETS_HJB(param, grid, num, CHI, results_in, show_result)`

with all inputs byte/logically identical across the two runs except:

- baseline: `results_in.rah = 0.040`
- perturbation: `results_in.rah = 0.041`

The endogenous cross-province update in `HANK_mp_1turn` occurs outside this isolated household call and therefore is **not** part of the future two-run household-block perturbation. The purpose is to test the HA block itself while holding the rest of the household state fixed, exactly matching the Owner requirement that other parameters remain unchanged.

Do not execute this experiment in the current task.

## Snapshot-authority archaeology

Determine whether the designated MATLAB tree contains one or more existing saved/cached states from which a complete, auditable pre-`HANK_2ASSETS_HJB` input tuple can be reconstructed without solving the model.

Inspect read-only:

- `Multi_Province_12sts_<year>.mat` files and any directly relevant cached/state `.mat` files;
- caller code that creates `param`, `grids{i}`, `num`, `CHI`, and `results_temp{i}` immediately before the household call;
- year/data index mapping;
- province index mapping;
- any stored per-province household state sufficient to reconstruct the direct call.

For `.mat` files, record at minimum:

- exact path;
- year/data index;
- bytes;
- SHA-256;
- variable inventory / shapes needed for authority resolution;
- whether loading the file is sufficient to recover the direct household-call inputs without numerical solving.

Read-only metadata or data loading is allowed. Do not call any model solver, HJB, KFE, equilibrium, shock, or iteration function.

## Candidate snapshot table

Produce a candidate table. Each candidate must include:

- candidate ID;
- year/data index;
- province index/name if resolvable;
- source/cache file path and SHA-256;
- whether the candidate represents a converged steady-state source state;
- exact origin of `param`;
- exact origin of `grid`;
- exact origin of `num`;
- exact origin of `CHI`;
- exact origin of `results_in`;
- observed native `results_in.rah` before any future override;
- whether all non-`rah` household inputs can be frozen exactly;
- whether `C`, labor, stationary distribution, `Ct`, `Lt`, `Aht`, `Bt` are produced by the direct HJB call;
- blockers or missing fields.

Do not silently choose a candidate merely because it is the newest year or first province.

## Preferred candidate properties

Rank candidates by reproducibility only, not by economic desirability:

1. complete direct-call input tuple reconstructible without running upstream equilibrium;
2. converged steady-state provenance is explicit;
3. no cache/recompute ambiguity remains after the artifact is selected;
4. exact hashes can freeze all required source/state objects;
5. no missing external data lookup is needed during the future household call;
6. direct-call output exposes the native aggregate objects needed for `C_hh/L_hh`.

If exactly one candidate dominates under these reproducibility criteria, label it:

`RECOMMENDED_REPRODUCIBLE_HOUSEHOLD_SNAPSHOT`

but do not execute it and do not convert recommendation into Owner approval.

If several candidates remain equally valid, return the smallest Owner decision set needed to select one, preferably just year/data index and province scope.

## Python side preparation

Read-only document the accepted Python R4 baseline used for the future paired robustness run:

- exact grid and productivity support;
- exact parameters;
- `r_a=0.040` baseline;
- exact external-harness construction needed for `r_a=0.041` while all else is unchanged;
- aggregate formulas `C_hh=sum(g*c)` and `L_hh=sum(g*l)`;
- validity diagnostics to report.

Do not run Python.

## Comparability framing

The future MATLAB household-call robustness and Python R4 robustness are **native/controlled comparative-static checks**, not a new exact shared-input parity gate.

P1-P4 remain the formal exact/adapter parity evidence.

For the future two-rate robustness check, report side by side:

- baseline `C_hh`, `L_hh`;
- perturbed `C_hh`, `L_hh`;
- `Delta C_hh`, `Delta L_hh`;
- percentage changes;
- sign and relative response magnitude.

Do not invent a native-level equality tolerance.

## Required output

Write exactly one report:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_HOUSEHOLD_CALL_SNAPSHOT_AUTHORITY_PREP_REPORT.md`

The report must contain:

- live/source identities;
- caller/input provenance map;
- `.mat` cache/state inventory relevant to direct household-call reconstruction;
- candidate snapshot table;
- recommended reproducible candidate if uniquely justified;
- exact remaining Owner decisions, if any;
- explicit future `rah=0.040 -> 0.041` injection semantics;
- proof that the future experiment freezes all non-`rah` household inputs;
- Python robustness-side preparation;
- aggregate formulas;
- forbidden-operation check;
- recommended successor gate.

## Classification

Return exactly one:

- `MATLAB_HA_HOUSEHOLD_SNAPSHOT_AUTHORITY_READY_FOR_OWNER_SELECTION`
- `MATLAB_HA_HOUSEHOLD_SNAPSHOT_AUTHORITY_UNIQUE_RECOMMENDATION_READY`
- `MATLAB_HA_HOUSEHOLD_SNAPSHOT_AUTHORITY_BLOCKED_MISSING_STATE_ARTIFACTS`
- `MATLAB_HA_HOUSEHOLD_SNAPSHOT_AUTHORITY_BLOCKED_OTHER`

## Commit/push authorization

Only the report may be added to the repository.

If and only if it is the sole repository change, commit once and fast-forward push after fresh remote verification.

Suggested commit subject:

`Prepare MATLAB HA household snapshot authority`

## Forbidden operations

Do not:

- execute MATLAB or Python HJB/KFE/model/equilibrium/shock code;
- modify any MATLAB or Python production source/test;
- modify or regenerate caches/state files;
- choose a scientific year/province without explicit source-based uniqueness or later Owner approval;
- change any parameter;
- issue P5 acceptance;
- enter AR(1), transition, IRF, calibration extension, or Results work;
- merge, rebase, reset, or force-push.

## Recommended successor gate

If snapshot authority is ready and the Owner selects/accepts one frozen MATLAB household-call snapshot:

`CH5_TWO_ASSET_HANK_PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_PERTURBATION_EXECUTION`

That successor may execute exactly four one-shot runs: MATLAB/Python baseline `0.040` and perturbed `0.041`, compute `C_hh/L_hh`, and report the requested side-by-side comparison before P5.