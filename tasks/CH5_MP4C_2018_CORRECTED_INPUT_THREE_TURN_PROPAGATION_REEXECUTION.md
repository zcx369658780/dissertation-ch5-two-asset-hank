# CH5 MP4C corrected-2018 three-turn propagation reexecution

Date: 2026-09-09. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## Objective

Reexecute exactly one fresh corrected-2018 three-turn trajectory on the accepted persistence-repaired runner, solely to obtain the previously unobserved turn-3 propagation evidence.

This task exists because the predecessor task stopped before turn 3 due only to an exclusive evidence-write collision. It is a new scientific authorization, not an implicit retry of the failed task.

## Required authority

Read before execution:
- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
- `docs/CH5_MP4C_2018_CORRECTED_INPUT_THREE_TURN_PROPAGATION_ACCEPTANCE.md`
- this exact task.

## Canonical input identity

Use only:
`D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`

Required SHA-256:
`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`

If missing or mismatched, stop with `BLOCKED_CANONICAL_INPUT_IDENTITY` and scientific calls = 0.

## Accepted predecessor evidence

Turn 1 and turn 2 must reproduce accepted evidence before turn 3 is entered.

For Anhui:
- turn1 `rah=.09`, `ra0=-.02496997113112164`, used `ra=.02`, raw wage `2.5721358283733027`, HJB iterations 64, `nk_gap=98575.17052447716`;
- turn2 `rah=.0829892058879816`, `ra0=-.024968505109415375`, used `ra=.02`, raw wage `2.1373365306922518`, HJB iterations 31, `nk_gap=.34756612158493083`.

The accepted turn-2 provenance establishes that turn-3 is the first point where corrected entering firm `ra=.02` can enter household composite `rah` through the native capital-allocation timing.

## Accepted persistence repair

The predecessor task preserved the executed runner and statically tested a one-line persistence-sequencing repair that prevents a second exclusive write collision on `predecessor_reproduction.json`.

Before scientific execution:
1. verify the repaired runner/source identity against the accepted predecessor repair receipt;
2. run the scoped static regression checks proving the evidence file is written exactly once / subsequent reproduction evidence uses a distinct path or noncolliding persistence sequence as implemented;
3. do not alter any scientific/model semantics while doing so.

If the repair identity or static gate cannot be verified, stop before science with `BLOCKED_REPAIRED_RUNNER_IDENTITY`.

## Scientific budget

Exactly one fresh scientific process and one corrected-2018 trajectory are authorized.

Maximum:
- turn 1 + turn 2 + turn 3 only;
- 31 provinces in frozen source order per turn;
- 93 province updates maximum;
- scientific retries = 0.

Forbidden:
- turn 4;
- steady-state loop;
- GE;
- annual model;
- MATLAB model run;
- IRF;
- Results.

A failed scientific invocation counts and must be preserved.

## Reproduction gates

Turn 1 and turn 2 must be compared against the accepted predecessor values/fields.

If turn 1 mismatch: stop with `CORRECTED_2018_THREE_TURN_REEXEC_FAIL__TURN1_REPRODUCTION_MISMATCH`.

If turn 2 mismatch: stop with `CORRECTED_2018_THREE_TURN_REEXEC_FAIL__TURN2_REPRODUCTION_MISMATCH`.

Do not loosen tolerances/comparators to enter turn 3.

## Turn-3 central scientific question

Observe, do not infer, the actual turn-3 household `rah` and its native provenance.

For Anhui preserve at minimum:
- turn-3 `rah`;
- native formula;
- source old-ra field and source turn;
- source old-ra vector SHA-256;
- own old ra;
- inter-province ratio;
- weighted old-ra total;
- `manual_override=false`;
- entering firm `ra`;
- firm raw/used `ra`;
- raw/used wage;
- HJB iterations/statistic/convergence;
- KFE status;
- C/L/A/B/A+B;
- nk_gap/yt_gap;
- controller/adaptation gate and any source-faithful action.

Explicitly answer whether turn-2 entering firm `ra=.02` participates in constructing turn-3 household `rah`, and quantify the resulting value relative to turn1 `.09` and turn2 `.0829892058879816`.

## National turn-3 summary

For each turn report:
- household `rah` min/median/max;
- raw firm `ra0` min/median/max;
- firm rate lower/interior/upper counts;
- raw wage min/median/max;
- wage lower/interior/upper counts;
- nk_gap and yt_gap min/median/max;
- HJB iteration min/median/max and failures;
- KFE failures;
- controller/adaptation actions.

If the native adaptation gate opens in turn 3, execute only the action already implied by the frozen source code for that turn. Do not append turn 4.

## Frozen scientific contract

Do not modify:
- canonical data;
- temporal contract;
- GDP/population/PIM/PLM/alpha/same-year Zt;
- province order;
- distance matrix;
- productive-capital route `At*N`;
- household Lt vs firm lt_supply distinction;
- capital-allocation rule;
- GovInv/adaptation rule;
- rate/wage bounds;
- `a_bar`;
- grids;
- household/HJB/KFE algorithms;
- boundary laws / D1-D3;
- solvers, tolerances or iteration limits.

## Evidence root

Use a fresh root:
`D:\ProjectTemp\ch5-corrected-2018-three-turn-reexec-20260909-001`

If occupied, use a fresh suffix. Never overwrite predecessor evidence.

Repository outputs should include a report plus machine-readable:
- repaired-runner identity receipt;
- turn1 reproduction;
- turn2 reproduction;
- turn-by-turn observables;
- Anhui forensic;
- turn3 rah provenance;
- transition summary;
- controller observables;
- call ledger;
- tests/static checks;
- manifest/readback.

Do not commit the private canonical workbook.

## Allowed verdicts

- `CORRECTED_2018_THREE_TURN_REEXEC_PASS__DIRECT_CORRECTED_RATE_TRANSMISSION_OBSERVED`
- `CORRECTED_2018_THREE_TURN_REEXEC_FAIL__TURN1_REPRODUCTION_MISMATCH`
- `CORRECTED_2018_THREE_TURN_REEXEC_FAIL__TURN2_REPRODUCTION_MISMATCH`
- `CORRECTED_2018_THREE_TURN_REEXEC_FAIL__HOUSEHOLD_OR_NUMERICAL_BLOCKER`
- `CORRECTED_2018_THREE_TURN_REEXEC_FAIL__UPSTREAM_STATE_OR_FIRM_BLOCKER`
- `BLOCKED_CANONICAL_INPUT_IDENTITY`
- `BLOCKED_REPAIRED_RUNNER_IDENTITY`

Even if PASS:
- turn 4 authorized = NO;
- 5–10 turn prefix authorized = NO;
- steady state authorized = NO;
- Results eligibility = FALSE.

Commit and non-force push a dedicated branch. Do not merge main. Do not launch a successor scientific task.