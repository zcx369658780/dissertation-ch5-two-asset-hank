# CH5 MP4C K1 — k-unit normalization and asset-domain recalibration design audit

Date: 2026-09-14
Task ID: `CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_AUDIT`
Type: zero-science-runtime source/dimensional/calibration design audit.

## Goal

Design a source-consistent recalibration that can express monetary/asset quantities in `k` units (thousands of currency units), expand the household asset domain, and preserve the accepted MATLAB-faithful HJB/KFE equations. Do not implement or run the recalibration in this task.

The task must determine exactly which variables and parameters would numerically change under the proposed unit normalization, distinguish unit conversion from economic recalibration, and produce a bounded implementation proposal for Owner/Reviewer approval.

## Mandatory authority

Read live `AGENTS.md`, rule index, CURRENT status/handoff, the accepted real-composite-wage/macro-scale audit and its acceptance, `docs/CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_FREEZE_CURRENT.md`, accepted annual-HJB/KFE authority, designated original MATLAB source/provenance, and accepted current Python multi-province/household source.

## Zero runtime

HJB=0; KFE=0; global outer=0; firm runtime=0; MATLAB runtime=0; K1B/K2=0; GE/downstream/shock/IRF/Results=0.

Allowed work: source reading, symbolic/dimensional derivation, deterministic offline calculations, task-owned audit scripts/tests, documentation/evidence generation.

## Phase 1 — verify original MATLAB normalization

Trace the original MATLAB chain and record exact source locations/formulas for:

- `GDP_multiplier=1000`;
- `POP_multiplier=100`;
- GDP/capital import multiplication;
- population import multiplication;
- export division by the same multipliers;
- any comments identifying the successful/comparatively good version;
- all other monetary/quantity multipliers or divisors affecting GDP, capital, investment, government investment, population, labor, consumption, transfers, wages, household assets and productivity.

Do not paraphrase the original scaling as “everything divided by 1000” unless the source actually proves that. Produce an exact variable-by-variable table.

## Phase 2 — define the proposed k-unit convention

Treat Owner's preferred target as:

`1 model monetary unit = 1k currency units`

This is a proposed normalization, not yet accepted implementation authority.

For every model object, classify it as one of:

- monetary stock;
- monetary flow;
- per-capita monetary stock/flow;
- physical/person quantity;
- rate / dimensionless ratio;
- utility/value-function object;
- numerical-only object;
- dimension unresolved.

At minimum classify:

GDP/output, capital, investment, government investment, consumption, transfers, taxes, `a`, `b`, `At`, `Bt`, `wjt`, household composite `w`, population, labor, productivity, `ra`, `rb`, borrowing gap, depreciation rates, adjustment costs, `chi0`, `chi1`, `rho`, utility/value function and any price/return guards.

## Phase 3 — equation-by-equation scaling audit

For each relevant HJB/firm/wage/aggregation equation, derive whether a common monetary scale factor `s` leaves the equation invariant or requires parameter transformation.

Especially audit:

- CRRA utility and marginal utility;
- labor FOC and wage-consumption relation;
- liquid drift;
- illiquid drift/transfer control;
- adjustment-cost function;
- transfer FOC;
- borrowing-rate spread terms;
- `wjt -> composite w` aggregation;
- firm output/wage/investment equations;
- government transfer/investment objects;
- capital/return mapping.

For every parameter that has monetary dimensions or enters a non-homogeneous expression, state the required transformation under `x_new = x_old / scale_to_k` or prove numerical invariance.

No parameter may be silently left unchanged merely because it was unchanged in legacy code.

## Phase 4 — household asset-domain design

Owner-proposed illiquid upper bound:

`amax=100` in k units.

Clarify explicitly that `amax` is an individual household state-grid upper bound. `At` is the stationary average/aggregate implied by the distribution and is not mechanically equal to `amax`.

Audit:

- proposed `amin`;
- proposed `amax=100`;
- current `bmin=-2`, `bmax=5`;
- observed real-wage standalone `Bt` and b-boundary pile-up;
- borrowing interpretation of `bmin` under k units;
- a defensible candidate `bmax` or a bounded candidate set/range.

Do not invent a `bmax` solely to clear the boundary. The recommendation must use at least:

- accepted b-marginal evidence;
- income/wage scale in k units;
- current borrowing bound interpretation;
- source consistency with the intended asset variable.

If a single `bmax` cannot be scientifically frozen from current evidence, return `BMAX_OWNER_SELECTION_REQUIRED` with a small justified candidate set and the evidence needed to choose among them.

## Phase 5 — grid spacing / precision consequences

For current `I=20`, `J=20`, calculate current and proposed `db`, `da` for each candidate domain.

Do not change I/J in this task.

Flag whether `amax=100` with `J=20` or candidate `bmax` with `I=20` creates spacing so coarse that an independent precision-sensitivity gate is mandatory before production use.

Distinguish:

- domain adequacy;
- discretization precision.

## Phase 6 — macro consistency target

Using accepted same-state evidence only, construct a proposed k-unit reporting table for:

- provincial GDP;
- provincial per-capita GDP;
- capital;
- investment if available;
- raw firm wage;
- guarded `wjt`;
- household composite wage;
- household `At/Bt`.

For each, report the exact source conversion needed to express it in k units. If household wage cannot yet be mapped to the same real monetary unit as GDP/per-capita GDP, state `MONETARY_UNIT_BRIDGE_UNPROVEN` rather than forcing equality.

The task must answer whether Owner's intended interpretation “per-capita GDP around 50k and `amax=100` meaning 100k” is dimensionally implementable with the current source chain, or which bridge/calibration relation remains missing.

## Phase 7 — implementation proposal

Produce one explicit, bounded implementation proposal containing:

1. exact variables to rescale;
2. exact parameters to transform;
3. exact variables/rates that remain unchanged;
4. proposed `amin/amax/bmin/bmax`;
5. I/J kept fixed for first implementation diagnostic;
6. expected new `da/db`;
7. required parity/invariance checks before any scientific run;
8. a first post-implementation standalone test grid;
9. a hard-stop rule if unit-equivalence/parity fails.

Do not implement this proposal in this task.

## Required evidence

Create compact evidence under:

`docs/evidence/ch5_mp4c_k1_k_unit_normalization_asset_domain_design/`

At minimum:

- `original_matlab_scaling_trace.json`
- `dimension_classification.csv`
- `equation_scaling_transform.json`
- `parameter_transform_table.csv`
- `asset_domain_design.json`
- `grid_spacing_receipt.json`
- `macro_k_unit_mapping.csv`
- `implementation_proposal.json`
- `source_identity.json`
- `call_ledger.json`
- `sealed_manifest_sha256.json`

## Report

Create:

`docs/CH5_MP4C_K1_K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_RECALIBRATION_DESIGN_AUDIT_REPORT.md`

## Questions to answer

1. What exactly did the original MATLAB program multiply/divide by 1000, 100, or other scale factors?
2. Can a coherent “1 monetary model unit = 1k currency units” normalization be defined without changing model economics?
3. Which parameters must change numerically under that unit conversion?
4. Is `amax=100` dimensionally coherent under the proposed convention?
5. What should `bmax` be, or what bounded candidate set should Owner choose from?
6. What happens to `da/db` with I=J=20?
7. Can provincial GDP, per-capita GDP and household wage be placed on a common proven monetary scale, or does a bridge remain unresolved?
8. What exact bounded implementation task should follow?

## Hard stops

Stop on any model-source modification, parameter change, grid change, HJB/KFE runtime, full-model runtime, outcome-fitted rescaling, or invented monetary conversion unsupported by source/equation analysis.

## Git workflow

Fresh-fetch live main; use a fresh isolated worktree/branch. No reset/clean/stash/force push. Explicit stage paths only; no `git add .`/`git add -A`. One coherent Builder commit, non-force push, one remote readback. Do not merge main and do not publish a successor task.

## Final response

Return terminal classification first, then actual baseline/branch/worktree/candidate SHA, changed paths, original MATLAB scaling trace, k-unit dimensional convention, equation/parameter transformation summary, `amax=100` assessment, `bmax` recommendation/candidate set, grid-spacing implications, macro k-unit mapping, unresolved dimensional bridges, exact bounded implementation proposal, zero-runtime ledger, exactly one next Owner gate, and `Results eligibility=FALSE`.

Stop for independent ChatGPT Reviewer acceptance.
