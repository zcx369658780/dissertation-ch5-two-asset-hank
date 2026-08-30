# MP4B initial-labor source-domain repair report

Date: 2026-08-30

## Terminal verdict

`MP4B_INITIAL_LABOR_SOURCE_DOMAIN_REPAIR_BLOCKED`

The protected MATLAB semantics and Python zero-endpoint domain defect were
established. The bounded Python repair passed static tests. The sole authorized
MATLAB scalar diagnostic then failed in its validation helper before producing
the first `fzero` result, so frozen-cell MATLAB/Python root parity was not
established. Python stationary execution was not authorized or attempted.

## Continuity and source identities

- live task/HEAD/origin-main at execution start:
  `4c5ae1d81379355e18e005016f42543ecd7fe466`
- direct parent: `72e1e7a1dc60c528127880520ce760816a6e320e`
- `HANK_2ASSETS_HJB.m` SHA-256:
  `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `lab_solve2.m` SHA-256:
  `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`

Both files were read through the protected logical C path, whose documented
physical target is D. They were not modified.

## Exact MATLAB source semantics

`HANK_2ASSETS_HJB.m:79-90` constructs
`rb_neg=rb+rb_gap`, selects `Rb` by the sign of `b`, defines
`raah=rah*(1-0.1*(ahmax/ah)^(-9))`, broadcasts it as `Rah`, and computes
`tempMat=Rah.*raah+Rb.*bbb+Tt`.

Lines 100-106 loop in `nz,j,i` order and use:

```text
params=[alphac,alphal,tau,w,z,frisch_l,tempMat,ga]
x0=((1-tau)*w*z)^(frisch_l*(1-ga)/(1+ga*frisch_l))
[l0j,fval,exitflag]=fzero(@(l) lab_solve2(l,params),x0,options)
```

`lab_solve2.m:11` is exactly

```text
l - (alphac/alphal*(1-tau)*w*z)^frisch_l
    * (l*(1-tau)*w*z+tempMat)^(-ga*frisch_l)
```

The frozen values are `alphac=1`, `alphal=1`, `ga=2`, `frisch_l=.2`.
Immediately after the root loop, HJB lines 111-112 use
`c0=(1-tau)*w*z*l0+Rb*b+Tt` and
`v02=(alphac*c0^(1-ga)/(1-ga)-alphal*l0^(1+1/frisch_l)/(1+1/frisch_l))/rho`.
The Python consumption/value initialization has the same coefficients and
exponents. Marker established:
`MP4B_INITIAL_LABOR_MATLAB_SOURCE_SEMANTICS_FROZEN`.

## First failing cell and domain proof

The preserved turn-1 loop first reaches Beijing at zero-based `(i,j,k)=(0,0,0)`:

| quantity | value |
|---|---:|
| `b,a,z` | `-2, 0, 0.8` |
| `Rb,raah` | `0.09, 0.09` |
| `tempMat` | `-0.0719` |
| `B=(1-tau)wz` | `15.2` |
| `x0=B^(-1/7)` | `0.6778993253895345` |
| base at old Python `l=0` | `-0.0719` |
| open-domain boundary `-tempMat/B` | `0.004730263157894736` |

Thus the old zero endpoint was not a source endpoint and was outside the real
domain. Its fractional power produced NaN before `brentq` could bracket.

On `B*l+tempMat>0`, with positive source `alphac/alphal`, `B`, `frisch_l`
and `p=ga*frisch_l`, the residual is continuous and
`f'(l)=1+A*p*B*(B*l+tempMat)^(-p-1)>0`. It has at most one real root.
Every frozen cell's source `x0` is strictly inside the domain. Marker established:
`MP4B_PYTHON_INITIAL_LABOR_ZERO_ENDPOINT_IS_NONSOURCE_DOMAIN_ERROR_CONFIRMED`.

## Repair and static evidence

Only the validation-entry root bracket changed. It evaluates the unchanged
source residual first at source `x0`; a negative residual expands upward, while
a positive residual approaches the open domain boundary using interior
midpoints. It has a fixed 128-step search limit and fails closed. It never uses
clipping, epsilon substitution, NaN replacement, equation changes, or solver
switching. `c0` and `v02` remain unchanged.

Python compile, direct bootstrap tests, positive/negative liquid cells, both
productivity states, old-endpoint rejection, source-`x0` admissibility,
impossible-domain failure, formula identity, MP3 seven-scenario and online
runtime regressions passed: `36 passed`. `git diff --check` passed.
`MP4B_INITIAL_LABOR_SOURCE_DOMAIN_REPAIR_STATIC_REVIEW_PASS` was established
for the Python repair.

## Frozen cells and failed scalar diagnostic

The eight cells were predeclared as the Cartesian product
`b={-2,4/19}`, `a={0,10}`, `z={0.8,1.3}`. Python roots were:

| b | a | z | Python root | residual | MATLAB root |
|---:|---:|---:|---:|---:|---|
| -2 | 0 | .8 | .6792542039265690 | 4.11e-15 | unavailable |
| 4/19 | 0 | .8 | .6757964176493583 | 0 | unavailable |
| -2 | 10 | .8 | .6792832786668417 | 4.44e-15 | unavailable |
| 4/19 | 10 | .8 | .6758251235775711 | 0 | unavailable |
| -2 | 0 | 1.3 | .6333079596259149 | 7.77e-16 | unavailable |
| 4/19 | 0 | 1.3 | .6311790863732587 | 1.11e-16 | unavailable |
| -2 | 10 | 1.3 | .6333258210921237 | 6.66e-16 | unavailable |
| 4/19 | 10 | 1.3 | .6311967980580924 | -1.11e-16 | unavailable |

The sole scalar-diagnostic invocation used
`D:\ProjectTemp\ch5-mp4b-initial-labor-scalar-diagnostic-20260830-001`.
It failed at the first result-row assignment with MATLAB's dissimilar-structure
subscript-assignment error. No JSON manifest was created, so no manifest SHA is
available and no protected `lab_solve2`/`fzero` root result was persisted.
The helper's empty structure was replaced afterward by an explicit eight-row
typed template, but it was not rerun. Therefore
`MP4B_INITIAL_LABOR_PYTHON_MATLAB_FROZEN_CELL_ROOT_PARITY_PASS` is not established.

## Later gates and call ledger

Because scalar parity failed, fresh presolver comparison, the second direct
bootstrap smoke, and Python stationary execution were not reached. Fresh
presolver mismatch count is therefore unavailable, not assumed zero.

The preserved MATLAB stationary artifacts were nevertheless rehashed read-only:

- output: `6233AB8B7380BE4D4E136851BC59F747EEB78B285B3A7A5903FEFFE64BCF464B`
- profile: `040C38E9E5FEE374202840C7741B7A15D6CFAE668FF8302619225FEEEC5DC90C`
- terminal JSON: `04D143B7553D1041B810B875575C06AE3E2F82132B2D55FEFDF5C3ED8AAB7270`
- status/turns/household calls: `COMPLETED / 184 / 5704`.

| operation | calls |
|---|---:|
| MATLAB validation-helper `checkcode` only | 1 |
| validation-only MATLAB scalar diagnostic | 1 (failed before first root result) |
| MATLAB stationary/HJB/KFE/multi-province | 0 |
| Python stationary top-level | 0 |
| Python household/HJB/KFE | 0 |
| scientific rerun | 0 |

No new Python run root, household outputs, outer iterations, final state, or
MATLAB/Python final comparison exists. First divergence is the scalar validation
helper's untyped-empty-structure output initialization; classification:
`VALIDATION_HELPER_INFRASTRUCTURE_ERROR`. Material mismatch list is empty because
no cross-language roots were obtained. Unresolved residual is the eight-cell
MATLAB/Python root parity. Environment/source failure lists are empty.

Forbidden-operation check: no MATLAB stationary/HJB/KFE/multi-province route,
wrong-year/batch, shocks, transition, dynamics, IRF, R5, Results, protected-source
write, Python science, or diagnostic rerun occurred.

## Exactly one recommended next gate

Authorize one bounded static review of the corrected scalar diagnostic helper
and exactly one replacement eight-cell scalar invocation; keep Python and MATLAB
stationary execution closed until frozen-cell root parity passes.
