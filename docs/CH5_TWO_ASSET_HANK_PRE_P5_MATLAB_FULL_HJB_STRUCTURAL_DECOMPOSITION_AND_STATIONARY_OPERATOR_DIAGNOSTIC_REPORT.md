# Chapter 5 pre-P5 MATLAB full-HJB structural decomposition and stationary-operator diagnostic

## Terminal classification

`MATLAB_STATIONARY_OPERATOR_BOUNDARY_NONUNIQUENESS_SUPPORTED__P5_BLOCKED`

Acceptance level: Phase A read-only structural forensic audit completed and decisive. Phase B was not needed; R0 was reused only and R1–R4 were not run. This is structural diagnostic acceptance only, not P5 acceptance and not cross-language aggregate parity evidence.

## Live authority and continuity

- Live start `origin/main`: `b7e1756ec5ca468326116df3103ea20df1222161`.
- Execution branch started clean after a fast-forward to that live SHA.
- Accepted Python baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`.
- `git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests` was empty before Phase A. No Python source/test was changed.

## Protected identities

| Object | SHA-256 | Result |
|---|---|---|
| accepted original `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | PASS |
| accepted original `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` | PASS |
| production `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` | PASS |
| accepted original `lab_solve2.m` | `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20` | PASS |
| accepted test-only O1 FOC | `B28E73F439CB3DD40B2A6C00BE5D3E56FD7C4254DF468B4E2C0DCCED06DB7315` | PASS |
| accepted test-only O2 common-Q adapter | `D94848535E68C0CBF9BA51C91016E8DD91809221EEEA3F21DC4EE5D96EBE9225` | PASS |

No production tree, helper, adapter or cache was modified.

## Native R0 control versus failed W2 differential matrix

Reused native R0 evidence identities were snapshot manifest `50603C35F94A4B5AD56DE29AC1FBFCE583BF8E5A7BD6410AC39ACF3FCD804101` and persisted 0.040 output `E723D267ABEFC16A20B4D17D6EC20554561B601FB028405FDA41D30EFAC03D00`. Failed W2 identities were raw `FB943CCFDF451FD2CE25EF44D04417495D56EA0AEF620DB60521F7266EDBF34F` and summary `5E7E54FFCA8C6A92807D0FCB72EFDECA0E82B541F1A2A4B1A5BA19298CBEDC43`.

| Object affecting full HJB/KFE | R0 native control | W2 | Classification |
|---|---|---|---|
| HJB/cost/labor source | accepted originals | identical | IDENTICAL |
| FOC resolution | production original | accepted O1 | SCIENTIFIC_EQUATION_DIFFERENCE |
| productivity values | `[0.8,1.3]` | `[0.8,1.3]` | IDENTICAL |
| productivity Q/operator | `[[-1/3,1/3],[1/3,-1/3]]` | `[[-0.4,0.4],[0.3,-0.3]]` | PRODUCTIVITY_REPRESENTATION_DIFFERENCE |
| `ga,rho,alphal,frisch_l` | `2,.05,1,.2` | identical | IDENTICAL |
| `chi0,chi1,a_bar,fixcost,fixcost2` | `.1,2,1e-6,0,0` | identical | IDENTICAL |
| `rb,w,tau,rb_gap,Tt` | `.02,13.084227346448168,.05,.07,.1` | identical | IDENTICAL |
| `rah` | `.040026998056627239` | `.040` | SCIENTIFIC_EQUATION_DIFFERENCE |
| asset nodes | exact native 20x20 grids, `a in [0,10]`, `b in [-2,5]` | same nodes/bounds/counts | IDENTICAL |
| state shape/order | 20x20x2=800, MATLAB `[b,a,z]` | identical | IDENTICAL |
| `maxit` | 100 | 500 | NUMERICAL_CONTROL_DIFFERENCE |
| `crit` | `1e-7` | `1e-8` | NUMERICAL_CONTROL_DIFFERENCE |
| `Delta` | 1000 | 10 | NUMERICAL_CONTROL_DIFFERENCE |
| `maxiter` | 100, read into a local but unused | 500 | NUMERICAL_CONTROL_DIFFERENCE / no active effect |
| `homecrit` | .01 | `1e-11` | NUMERICAL_CONTROL_DIFFERENCE |
| prior `Ct/At/Bt/Lt` | `9.0937180040796441/.42299898139597236/2.162718089919998/5.4425427457428183e6` | zeros | BOOKKEEPING_ONLY |
| province/firm metadata and `wjt` | populated | absent | DISPLAY_ONLY (`show_result=0`) |
| starting-value formula | HJB lines 90–113 | same formula | IDENTICAL formula; small `rah`-driven initialization difference |
| stationary solve | transpose, row pin at `floor(.37M)`, RHS .007, cell-measure normalization | identical source | IDENTICAL |

R0 reused diagnostics: `convergent=1`, finite mass/aggregates, mass sum 1, minimum cell `-2.1408321898522033e-32`, `C_hh=9.093838085759417`, effective `L_hh=.7208465448372894`, `A_hh=.4205741387968296`, `B_hh=2.162515255782729`. W2 diagnostics: `convergent=false`, `MATLAB:nearlySingularMatrix`, RCOND `9.469722e-20`, mass sum 1, minimum `-0`, mass above `a_min=9.986691595828191e-18`, mass above `b_min=1`, `C_hh=9.348730703739667`, raw `H_hh=.6903227565218332`, effective `L_hh=.7437255264151377`, `A_hh=2.2629694319679536e-17`, `B_hh=.2105263157894739`.

## Convergence-control-flow audit

The original HJB reads numerical controls at lines 21–24, sets `convergent=0` at line 39, builds grids/productivity blocks at lines 46–66, and constructs the initial labor, consumption and `v02` at lines 79–113. The HJB loop is `n=1:maxit` (line 114): derivatives and state constraints are built at 116–136; four FOC candidates and direction selection at 137–154; the liquid and illiquid generator blocks at 155–232. A generator row-sum check at 233–239 may break the loop before a value update. Otherwise the implicit system

`((1/Delta+rho)I-A)V_new = u + V_old/Delta`

is solved at 240–245. `convergent` becomes one only if `max(abs(V_new-V_old))<crit` at 248–254. Iteration exhaustion merely prints when display is enabled and leaves the flag false (256–260).

Critically, there is no return/stop gate after a false convergence flag. Lines 262–333 rebuild policies and the final backward generator, and lines 334–345 execute the stationary solve unconditionally. Thus:

- `HJB_NONCONVERGENCE` is the failure to meet the value-change criterion or an early improper-generator break.
- `STATIONARY_OPERATOR_SINGULARITY_OR_NONUNIQUENESS` is a separate property of the final `A'` solve.

The near-singular warning is emitted at line 340, after the convergence decision and during `AT\vec`. Source order does not establish either failure as the cause of the other.

## O1 lower-asset derivation

Let `x=pa/pb` and

`S(x)=min(x-1+chi0,0)+max(x-1-chi0,0)`.

The production domestic FOC line 19 is

`d_original = S(x)*a/chi1`,

whereas accepted O1 is

`d_O1 = S(x)*max(a,a_bar)/chi1`.

The final illiquid drift is `mu_a=rah*a+d` (HJB line 264).

| Region | Production original | O1 | Structural implication |
|---|---|---|---|
| `a=0` | `d=0`, hence `mu_a=0` identically | `d=a_bar*S(x)/chi1`; positive only for `x>1+chi0`, negative for `x<1-chi0`, zero in deadband | original lower layer is exactly closed; O1 upward edge is shadow/state dependent |
| `0<a<a_bar` | `d=a*S/chi1` | `d=a_bar*S/chi1` | O1 removes proportional collapse but does not guarantee a positive direction |
| `a>=a_bar` | `d=a*S/chi1` | identical | no adapter difference |

At the lower node, HJB lines 142 and 146 accept only a positive FOC candidate above `1e-12`; a negative edge is state-constrained away. With native `a_bar=1e-6`, O1 affects only the exact lower node on the 20-node native grid and supplies at most a very small, shadow-dependent edge. With earlier `a_bar=.5`, it applies over a materially wider low-asset interval. W2's near-zero mass above `a_min` shows that its realized O1 policy did not create an effective escape edge.

Accepted Python instead treats the lower boundary through its explicit KKT/state-constraint policy selection and has accepted R4 one-recurrent-class evidence. The finding here concerns legacy MATLAB full-HJB integration; it does not invalidate the accepted Python redesign.

## Stationary-generator and recurrent-class audit

For liquid assets, lines 155–188 assemble backward transitions from signed liquid drift: negative drift goes to `b_{i-1}`, positive drift to `b_{i+1}`, and the diagonal is minus outgoing intensity. Boundary direction masks at lines 152–153 suppress lower/upper violations. The final version is rebuilt at 263–298.

For illiquid assets, lines 190–229 use `MhB=min(dhB,0)` and `MhF=max(dhF,0)+Rah*a`, with explicit upper-bound handling at 194–195. Negative drift maps to `a_{j-1}`, positive drift to `a_{j+1}`, and diagonal entries balance outgoing rates. The final signed-drift construction is at 299–332. Productivity transitions are the two diagonal `I*J` blocks and off-diagonal blocks of `Bswitch` at 64–66. Total backward generator is `A=BB+AAH+Bswitch`; rows should sum to zero.

The stationary equation uses `AT=A'` (335), replaces row `iFix=floor(.37M)` with a unit row, sets only `vec(iFix)=.007`, solves `AT\vec`, and normalizes by `g'1*db*dah` (337–342). It does not compute recurrent classes, left nullity, the residual of the original unmodified `A'`, or pin sensitivity.

The decisive structure is production FOC's exact factor `a`: at every `(b,z)` state on `a=0`, `d=0` and `rah*a=0`, so no illiquid transition leaves the `a=0` layer. Liquid and productivity moves stay inside that layer. Hence that layer contains at least one closed recurrent class. A unique stationary object, if every positive-a state were transient into that layer, would carry no material positive-a mass. Yet accepted native R0 reports `A_hh=.4205741387968296`. This combination supports either another recurrent class or a pin-selected/non-residual-qualified stationary vector. In both cases the fixed-row method can conceal nonuniqueness while returning a normalized vector and no warning. The native `convergent=true` flag certifies only value iteration, not stationary uniqueness.

This is sufficient to reject the legacy full-HJB stationary result as an unquestioned P5 oracle without rerunning R0 or decompositions.

## Common-Q/full-HJB audit

The accepted original MATLAB source is nominally parameterized by `Nz`, but `Bswitch` is explicitly assembled as a 2x2 block matrix from `la_mat(1:2,1:2)` at lines 64–66. Prior common fixtures used exactly two states, supplied `z=[.8,1.3]`, and set `grid.la_mat=[[-.4,.4],[.3,-.3]]`. Because R0 uses the same z values and ordering, this substitution:

- changes intended productivity transition intensities and invariant weights;
- does not change labor-income state values, initialization, reshape ordering, or asset boundary formulas;
- remains a pure input-level productivity-generator substitution for this two-state case;
- recomposes consistently with accepted P3 common-Q evidence after the established orientation adapter.

Native Q is symmetric with invariant weights `.5/.5`; common Q has invariant weights `3/7,4/7`. This can interact with endogenous policies, but Phase A does not support it as the sufficient blocker. The code is not generally `Nz`-agnostic despite reading `Nz` because block construction is hard-coded to two productivity states.

## Complete `results` and initialization dependency table

| `results` field | Read line | Classification | R0 | W2 |
|---|---:|---|---:|---:|
| `rb` | 26 | POLICY_EQUATION_ACTIVE; INITIALIZATION_ACTIVE; STATIONARY_ACTIVE | .02 | .02 |
| `rah` | 27 | POLICY_EQUATION_ACTIVE; INITIALIZATION_ACTIVE; STATIONARY_ACTIVE | .040026998056627239 | .040 |
| `w` | 28 | POLICY_EQUATION_ACTIVE; INITIALIZATION_ACTIVE; STATIONARY_ACTIVE | 13.084227346448168 | same |
| `rb_gap` | 29 | POLICY_EQUATION_ACTIVE; INITIALIZATION_ACTIVE; STATIONARY_ACTIVE | .07 | .07 |
| `tau` | 30 | POLICY_EQUATION_ACTIVE; INITIALIZATION_ACTIVE; STATIONARY_ACTIVE | .05 | .05 |
| `Tt` | 31 | POLICY_EQUATION_ACTIVE; INITIALIZATION_ACTIVE; STATIONARY_ACTIVE | .1 | .1 |
| `Ct` | 33 | BOOKKEEPING_ONLY (`Ct_1` output only) | 9.0937180040796441 | 0 |
| `At` | 34 | BOOKKEEPING_ONLY (`At_1`, `Atdot`) | .42299898139597236 | 0 |
| `Bt` | 35 | BOOKKEEPING_ONLY (`Bt_1`, `Btdot`) | 2.162718089919998 | 0 |
| `Lt` | 36 | BOOKKEEPING_ONLY (`Lt_1`, `Ltdot`) | 5.4425427457428183e6 | 0 |
| `prvname,Zt,Kt,Kt0,alpha` | 94 | DISPLAY_ONLY | populated | absent |
| `wjt` | 376 | DISPLAY_ONLY | 1.3 | absent |

No `results` field is `CONVERGENCE_ACTIVE` except indirectly through the six policy/initialization-active economic fields. Helpers accept `results` but do not dereference it. Therefore the earlier statement that `Ct/At/Bt/Lt` are bookkeeping-only is sufficient; no hidden saved `results` field changes the HJB start or iteration when `show_result=0`.

Initialization is completely reconstructed by lines 79–113 from `rb,rah,w,rb_gap,tau,Tt`, grid, `ga,alphal,frisch_l,rho`, and `lab_solve2`; Q does not enter `v02`. R0/W2 initialization differs only through the preregistered small `rah` difference, not prior aggregates or metadata.

## Frozen structural hypothesis manifest and Phase decision

External root: `D:\\ProjectTemp\\ch5-pre-p5-matlab-structural-diagnostic-artifacts-20260829-194514`.

- `phase_a_structural_hypothesis_manifest.md`: 6705 bytes, SHA-256 `78D55CB77D2E829B03F3CF648507F6124D056226178B90F3B0B2DE2BE3A2935C`.
- Frozen statuses: lower-a closed-class/nonuniqueness and arbitrary stationary pinning `SUPPORTED_SUFFICIENT`; O1/full-HJB, common-Q/full-HJB, and numerical-control effects `SUPPORTED_PLAUSIBLE`; joint O1+common-Q `UNRESOLVED_REQUIRES_REPLAY`; hidden results/initialization dependence and residual economic fields `NOT_SUPPORTED`.

Phase A established a decisive structural classification. Per the task's stop rule, Phase B was not entered.

| Object | Scientific HJB calls |
|---|---:|
| R0_CONTROL_REUSED | 0 new calls |
| R1 O1 isolation | 0 |
| R2 common-Q isolation | 0 |
| R3 O1+common-Q | 0 |
| R4 initialization/results normalization | 0 |

There are no replay diagnostics because no replay was authorized after the decisive Phase A finding.

## Primary blocker and oracle suitability

Primary blocker: the legacy MATLAB full-HJB couples an exactly closed production-FOC `a=0` layer with a stationary solver that arbitrarily pins one row and does not qualify recurrent-class uniqueness, left nullity, original-equation residual, or pin robustness. This makes its native full-HJB stationary output unsuitable as an unquestioned final P5 integration oracle under the accepted redesigns.

The legacy code remains useful as historical/native evidence and for already accepted modular equation/operator comparisons. The conclusion does not reject O1, O2, Python R4, or P1–P4; it narrows what the native full-HJB can certify.

## Files read and written

Reads: the live task, `AGENTS.md`, both required project rules, all nine required evidence reports, accepted Python HJB/policy/boundary/generator/KFE sources, accepted MATLAB HJB/cost/production-FOC/labor helper, accepted O1/O2 adapters, the read-only native snapshot manifest and R0 raw output, and predecessor W2 raw/summary artifacts.

Repository write: only this report.

External write: only the frozen text-first Phase A manifest in the new no-overwrite artifact root. No MAT replay, scientific harness, patched source, cache or binary was created.

## Forbidden-operation check

PASS: no parameter tuning; no C1/C2/C3 or A/B/C/W1/W2 rerun; no R0 rerun; no R1–R4 call; no Python HJB/KFE/steady state; no P1–P4 rerun; no third adapter; no MATLAB/Python production edit; no cache edit; no parity companion or final four-run sequence; no solver/tolerance mutation; no outer equilibrium, province, AR(1), transition, IRF, calibration extension, dynamics or Results work; and no P5 acceptance.

## Recommended next gate

Publish an Owner/reviewer decision task to revise the P5 acceptance design explicitly. The decision should state that accepted modular P1–P4 evidence and Python's recurrent-class/KFE qualifications—not an unqualified legacy full-HJB pinned stationary vector—define the integration standard, or else authorize a separate read-only stationary-uniqueness evidence design. It must not silently change accepted equations, add adapters, resume parameter tuning, or infer P5 acceptance.

