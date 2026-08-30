# MP4B replacement eight-cell scalar-root parity report

Date: 2026-08-30

## Verdict

`MP4B_INITIAL_LABOR_REPLACEMENT_8CELL_SCALAR_ROOT_PARITY_PASS`

Marker established:
`MP4B_INITIAL_LABOR_PYTHON_MATLAB_FROZEN_CELL_ROOT_PARITY_PASS`.

This verdict is scalar-validation-only. Presolver, household, HJB/KFE,
multi-province, and stationary execution were not run.

## Live continuity and prior attempt

- live task/HEAD/origin-main at start:
  `ad3cd2e23e1ac77c95c8fb54f1b5dff2d362d08f`
- direct parent: `9fa649c80420ae0f95aaddb30234e85314c980c5`
- prior failed scalar root:
  `D:\ProjectTemp\ch5-mp4b-initial-labor-scalar-diagnostic-20260830-001`
- prior call count: one scalar diagnostic, zero persisted roots, no model calls
- prior failure: assignment into an untyped empty MATLAB structure

## Static helper audit and persistence repair

The current typed template and every assigned row have the identical ordered
field set:
`i,j,k,b,a,z,Rb,raah,tempMat,B,x0,l0,fval,exitflag,root_base`.
`repmat(template,1,8)` fixes exactly eight result rows.

The cell set remains the Cartesian product
`b={-2,4/19}`, `a={0,10}`, `z={.8,1.3}`. Parameters remain
`alphac=1, alphal=1, tau=.05, w=20, frisch_l=.2, ga=2, Tt=.1,
rb=.02, rb_gap=.07, rah=.09, a_max=10`. The frozen `raah`, `tempMat`,
`B`, `x0`, `lab_solve2`, `fzero`, and `root_base` formulas are unchanged.

Static call scanning found no HJB, KFE, one-turn/equilibrium, annual, or
multi-province model function. The helper hashes protected `lab_solve2.m`
before any root call and requires
`74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`.

The helper previously used R2022b-incompatible `fopen(output_json,'x')`.
It now:

1. rejects an existing output or missing caller-created directory;
2. atomically reserves the exact new path with
   `java.io.File(output_json).createNewFile()`;
3. opens only that newly reserved empty file with `fopen(...,'w')`;
4. fails closed on reservation/open failure.

No pre-existing file can be truncated. Helper SHA-256 before repair was
`42224D2F9A77B6260149E8C4DA356F753E40D537878526A2312C17A29CFA30E2`;
after repair it is
`213DD0D154133676F69BE15BA71A7318DC89D3A8C91A4683B0B5975522A17DFA`.
R2022b checkcode ultimately passed with no findings. Marker established:
`MP4B_INITIAL_LABOR_SCALAR_DIAGNOSTIC_HELPER_STATIC_REVIEW_PASS`.

## Scalar manifests

Fresh root:
`D:\ProjectTemp\ch5-mp4b-replacement-8cell-root-parity-20260830-001`.

- Python manifest: `python_scalar_roots.json`
- Python manifest SHA-256:
  `F34C2E8425A8A1E6227AC96044C8C1B80FB0D18C1AC78583771B6CCF4E1D759F`
- current frozen Python repair SHA-256:
  `58EA4BDD1AEF8B8111DD406EE616DB8D9A8F5E174EC8019B37602054F06490E3`
- MATLAB manifest: `matlab_scalar_roots.json`
- MATLAB manifest SHA-256:
  `DE48C79ECA4DAC5C4085F892E217911060824ACB0827081FE9C1F8B6EE38207C`
- comparison manifest SHA-256:
  `027591E9EBE5CF231CC873FB9EAF90C295FB8414EFC97FE68EC1BB836EE3EB55`

Both scalar manifests record eight cells and zero stationary/model calls.

## Complete root comparison

All root-difference limits equal `1e-10` because every compared root has
absolute value below one.

| b | a | z | x0 | MATLAB root | Python root | abs diff | MATLAB/Python residual | root-base | exit | result |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| -2 | 0 | .8 | .6778993253895345 | .6792542039265661 | .6792542039265690 | 2.89e-15 | 0 / 4.11e-15 | 10.252763899683806 | 1 | PASS |
| 4/19 | 0 | .8 | .6778993253895345 | .6757964176493583 | .6757964176493583 | 0 | 0 / 0 | 10.384416074586037 | 1 | PASS |
| -2 | 10 | .8 | .6778993253895345 | .6792832786668385 | .6792832786668417 | 3.22e-15 | -1.11e-16 / 4.44e-15 | 10.251666835735945 | 1 | PASS |
| 4/19 | 10 | .8 | .6778993253895345 | .6758251235775712 | .6758251235775711 | 1.11e-16 | 1.11e-16 / 0 | 10.383313404694873 | 1 | PASS |
| -2 | 0 | 1.3 | .6324748961240604 | .6333079596259144 | .6333079596259149 | 5.55e-16 | 0 / 7.77e-16 | 15.570806602760085 | 1 | PASS |
| 4/19 | 0 | 1.3 | .6324748961240604 | .6311790863732586 | .6311790863732587 | 1.11e-16 | 0 / 1.11e-16 | 15.702433959735277 | 1 | PASS |
| -2 | 10 | 1.3 | .6324748961240604 | .6333258210921231 | .6333258210921237 | 5.55e-16 | -1.11e-16 / 6.66e-16 | 15.569708780975439 | 1 | PASS |
| 4/19 | 10 | 1.3 | .6324748961240604 | .6311967980580924 | .6311967980580924 | 0 | -1.11e-16 / -1.11e-16 | 15.701332438350670 | 1 | PASS |

All Python roots and both bracket endpoints are strictly inside their open real
domains. All MATLAB root bases are positive. Maximum source-input absolute
difference is `2.78e-17`, limited to normal local IEEE evaluation order; cell
identity and source formulas are unchanged. Eight of eight cells pass without
tolerance adjustment.

## Call ledger and checks

Current-task calls:

| operation | count |
|---|---:|
| MATLAB static `checkcode` invocations | 3 |
| replacement MATLAB scalar diagnostic | exactly 1, eight cells |
| Python scalar-manifest arithmetic | 1, eight cells |
| MATLAB stationary/HJB/KFE/multi-province | 0 |
| Python stationary/household/HJB/KFE | 0 |
| MP2/MP3 empirical, wrong-year, annual batch, shocks/dynamics/IRF/R5/Results | 0 |

Focused template/persistence/forbidden-call and Python scalar tests passed.
MATLAB R2022b checkcode passed. Strict no-overwrite was retained.
`git diff --check` passed. No protected MATLAB or accepted Python root logic was
modified. Presolver and stationary gates were deliberately not entered.

## Exactly one recommended next gate

Authorize fresh Python direct-script/bootstrap smoke, fresh calendar-2009
presolver equality, and one Python-only stationary invocation against the
preserved completed MATLAB run; MATLAB stationary remains zero.
