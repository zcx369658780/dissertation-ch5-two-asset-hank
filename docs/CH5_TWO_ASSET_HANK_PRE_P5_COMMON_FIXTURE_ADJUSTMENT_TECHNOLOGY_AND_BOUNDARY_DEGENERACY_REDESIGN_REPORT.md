# Chapter 5 pre-P5 common-fixture adjustment-technology and boundary-degeneracy redesign report

## Terminal classification

`COMMON_FIXTURE_NATIVE_ANCHOR_STILL_DEGENERATE_NEEDS_STRUCTURAL_DIAGNOSTIC__P5_BLOCKED`

Acceptance level: bounded pre-P5 source/common-support audit and MATLAB-only diagnostic execution completed. No common fixture qualified, neither non-common witness produced a valid non-degenerate solve, final parity was not run, and P5 remains blocked.

## Authority and continuity

- Live start `origin/main`: `bf5df8dd1e5640f3b1feb621d22b6938ef1142f1`.
- Execution branch/starting HEAD: `codex/ch5-adjustment-boundary-redesign` at the same SHA.
- Live task was read from fresh-fetched `origin/main` before work.
- Accepted Python baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`.
- `git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests` was empty. No Python production or test file was changed.
- Accepted predecessor classification was retained as input evidence only; none of its exhausted candidates was rerun.

## Protected identities

| Object | SHA-256 | Result |
|---|---|---|
| accepted original `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | PASS |
| accepted original `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` | PASS |
| production `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` | PASS |
| accepted original `lab_solve2.m` | `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20` | PASS |
| accepted test-only O1 `HANK3_FOC.m` | `B28E73F439CB3DD40B2A6C00BE5D3E56FD7C4254DF468B4E2C0DCCED06DB7315` | PASS |
| accepted test-only O2 common-Q adapter | `D94848535E68C0CBF9BA51C91016E8DD91809221EEEA3F21DC4EE5D96EBE9225` | PASS |

MATLAB path assertions immediately before every entered call resolved the original HJB, original cost helper, O1 temporary FOC helper, and original labor helper exactly as frozen. No third adapter was introduced.

## Source/common-support audit

The accepted MATLAB HJB reads `rb`, `rah`, `w`, `rb_gap`, `tau`, and `Tt` from its input at lines 26–31. It constructs `rb_neg=rb+rb_gap` and applies it only at `b<0` (`Rb = rb` for `b>=0`, `rb+rb_gap` for `b<0`) at lines 79–80. `Tt` is unconditional liquid income: it enters initialization at lines 90 and 111, liquid forward/backward boundary consumption at lines 117/119, HJB liquid drift at lines 126 and 129–130, final drift at line 263, and stationary budget diagnostics at lines 352–353. Wage and tax enter as `(1-tau)*w*z*l`; `rah` supplies the illiquid return schedule. The O1 helper changes only the low-`a` transfer-control denominator from `a` to `max(a,a_bar)`; `chi0`, `chi1`, and `a_bar` therefore govern the transfer/adjustment technology together with the unchanged cost helper.

Accepted Python `HouseholdInputs` contains `r_a`, `r_b`, `tau`, wages, migration costs, and labor weights; `EconomicParams` contains the preference and adjustment parameters. Production `asset_drifts` uses `r_b*b + labor_income - transfer - cost - consumption` and `r_a*a + transfer`. It exposes neither an unconditional household-income term corresponding to MATLAB `Tt` nor a negative-`b` rate spread corresponding to `rb_gap`. Zero fixed costs are neutral and match production Python adjustment technology.

The MATLAB `results.Ct/At/Bt/Lt` inputs are copied as prior aggregates and used for output deltas/bookkeeping, not current policy equations. Province/display fields are used only when display is enabled. No additional nonzero, scientifically active MATLAB-only household field was found that the frozen objects failed to neutralize.

### Common-support matrix

| MATLAB field | Meaning / audited source | Native value | Python production equivalent and mapping | Status | Treatment |
|---|---|---:|---|---|---|
| `rho` | discount rate | 0.05 | `EconomicParams.rho`, identity | COMMON_SUPPORTED | native/common |
| `ga` | CRRA curvature | 2 | `gamma_c`, identity | COMMON_SUPPORTED | native/common |
| `frisch_l` | inverse labor-curvature parameter | 0.2 | `phi=1/frisch_l=5` | COMMON_SUPPORTED | corrected reciprocal mapping |
| `alphal` | labor-disutility weight | 1 | `labor_weights=1` | COMMON_SUPPORTED | native/common |
| `chi0`,`chi1`,`a_bar` | transfer/adjustment technology via O1 FOC and cost | 0.1, 2, 1e-6 | like-named production parameters | COMMON_SUPPORTED | native values |
| `rb` | liquid return for `b>=0` | 0.02 | `r_b`, identity | COMMON_SUPPORTED | native for B/C/W1/W2 |
| `rah` | illiquid return | 0.040026998056627239 saved | `r_a`, identity | COMMON_SUPPORTED | preregistered 0.040 or 0.055 |
| `w` | wage | 13.084227346448168 | wages, identity | COMMON_SUPPORTED | native for B/C/W1/W2 |
| `tau` | labor-income tax | 0.05 | `tau`, identity with zero migration cost | COMMON_SUPPORTED | native for B/C/W1/W2 |
| `Tt` | unconditional liquid income/transfer | 0.1 | none | NOT_CURRENTLY_REPRESENTABLE | zero in A/B/C/W1; 0.1 only in W2 |
| `rb_gap` | extra liquid return only for `b<0` | 0.07 | none | NOT_CURRENTLY_REPRESENTABLE | zero in A/B/C; 0.07 only in W1/W2 |
| `fixcost`,`fixcost2` | fixed adjustment terms | 0, 0 | production has no nonzero fixed-cost term | ZERO_NEUTRAL | zero throughout |
| prior `Ct/At/Bt/Lt` | prior-output bookkeeping/deltas | cache values | no scientific mapping required | INITIALIZATION_ONLY | set to zero consistently |
| province/display fields | display metadata | native metadata | none | DISPLAY_ONLY | display disabled |

Thus A/B/C were true common-supported objects. W1/W2 were deliberately non-common witnesses and could never qualify as parity fixtures.

## Native reference and frozen manifest

Read-only native reference: `C2016-P10`, 2016 Jiangsu. Exact scalars were `ga=2`, `rho=0.05`, `alphal=1`, `phi_l=5`, `frisch_l=0.2`, `chi0=0.1`, `chi1=2`, `a_bar=1e-6`, `fixcost=fixcost2=0`, `rb=0.02`, saved `rah=0.040026998056627239`, `w=13.084227346448168`, `tau=0.05`, `Tt=0.1`, and `rb_gap=0.07`; saved `convergent=true`.

Exact native `a` grid:

`[0, 0.5263157894736842, 1.0526315789473684, 1.5789473684210527, 2.1052631578947367, 2.631578947368421, 3.1578947368421053, 3.6842105263157894, 4.2105263157894735, 4.7368421052631575, 5.263157894736842, 5.789473684210526, 6.315789473684211, 6.842105263157895, 7.368421052631579, 7.894736842105263, 8.421052631578947, 8.947368421052632, 9.473684210526315, 10]`

Exact native `b` grid:

`[-2, -1.631578947368421, -1.263157894736842, -0.8947368421052633, -0.5263157894736843, -0.1578947368421053, 0.21052631578947345, 0.5789473684210527, 0.9473684210526314, 1.3157894736842102, 1.6842105263157894, 2.052631578947368, 2.421052631578947, 2.7894736842105257, 3.1578947368421053, 3.526315789473684, 3.894736842105263, 4.263157894736842, 4.63157894736842, 5]`

All objects used common `z=[0.8,1.3]` and `Q_z=[[-0.4,0.4],[0.3,-0.3]]`. A used the preregistered 11-node grids `a=[0,1,...,10]` and `b=[-2,-1.3,-0.6,0.1,0.8,1.5,2.2,2.9,3.6,4.3,5]`; B/C/W1/W2 used the exact native 20-node asset grids above. Static contract construction proved A/B/C scalar/vector/grid representability without a Python scientific call.

The complete A/B/C/W1/W2 manifest was written, strict-JSON read back, frozen, and hashed before the first HJB call:

- `manifest.json`: `FFC986B319766923FB9100267B780FC09C4DA0FBED95A2E605619DF9D8A2E1FC`.
- `static_common_support_audit.json`: `CC1584389A20AD91CFCAA803261620D5F4AF2A2B39858E6872877C0B0FCEB59A`.
- frozen MATLAB harness `run_object.m`: `CAB0EAE957FA5D5750238007679AEF2CA59EC502B5B3ACCB6E0885B33CB55A59`.
- manifest verifier `verify_manifest.py`: `D5024C2A471727E8D747C2D902AA2B691EE83526A49507A5A042CCD84A1C8E43`.

The manifest and harness hashes remained identical after all calls.

## Exact execution counts

| Scientific operation | Count |
|---|---:|
| MATLAB A at `rah=0.055` | 1 |
| MATLAB B at `rah=0.040` | 1 |
| MATLAB C at `rah=0.055` | 1 |
| MATLAB W1 at `rah=0.040`, `rb_gap=0.07`, `Tt=0` | 1 |
| MATLAB W2 at `rah=0.040`, `rb_gap=0.07`, `Tt=0.1` | 1 |
| Python HJB/KFE/steady state | 0 |
| companion rate | 0 |
| predecessor candidates / P1–P4 | 0 |

Attempt markers, immediate raw MAT persistence, summary JSON read-back, and rate-matched initialization artifacts exist once for every entered object. No rerun occurred.

## Qualification and witness diagnostics

| Object | Common? | convergent | warning / RCOND | mass sum | min mass | mass `a>a_min` | mass `b>b_min` | `C_hh` | `H_hh` | `L_hh` | `A_hh` | `B_hh` | disposition |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| A | yes | false | `MATLAB:nearlySingularMatrix`, `1.641814e-17` | 1.0000000000000002 | -1.4264817142067335e-17 | -1.137790776380863e-16 | -1.7295494100652644e-16 | 1.0260994320788104 | 1.0090738541012512 | 1.0860994320788104 | -3.3507990307117482e-16 | -2.0000000000000004 | NOT_QUALIFIED |
| B | yes | false | `MATLAB:nearlySingularMatrix`, `8.709517e-19` | 1 | -0 | 9.128169905230875e-17 | 1.782801391586499e-17 | 9.245612104537905 | 0.6935464381069001 | 0.7470313891898142 | 2.068429696928388e-16 | -2 | NOT_QUALIFIED |
| C | yes | false | `MATLAB:nearlySingularMatrix`, `7.058047e-19` | 1.0000000000000002 | -0 | 7.673152256965139e-17 | 1.4636785679045435e-17 | 9.245203726760714 | 0.6935143913188239 | 0.7469985350263219 | 1.7386816674115965e-16 | -2.0000000000000004 | NOT_QUALIFIED |
| W1 | no | false | `MATLAB:nearlySingularMatrix`, `8.382814e-19` | 1 | -0 | 8.802494850891133e-17 | 1 | 9.277174496087783 | 0.6925539831444256 | 0.7460138414419148 | 1.9946322149496927e-16 | 0.21052631578947387 | NOT_QUALIFIED |
| W2 | no | false | `MATLAB:nearlySingularMatrix`, `9.469722e-20` | 1 | -0 | 9.986691595828191e-18 | 1 | 9.348730703739667 | 0.6903227565218332 | 0.7437255264151377 | 2.2629694319679536e-17 | 0.2105263157894739 | NOT_QUALIFIED |

All exposed arrays and reported aggregates were finite, mass normalization met `1e-10`, and minimum mass met `-1e-12`. Every object nevertheless failed `convergent=true` and the no-singular-warning criterion. A/B/C collapsed at both asset lower boundaries. W1/W2 moved all liquid mass away from `b_min`, showing that the unsupported borrowing spread materially changes liquid-boundary location, but both retained essentially zero mass away from `a_min`, remained nonconvergent, and retained a nearly singular stationary solve. Consequently they are not valid non-degenerate witnesses.

First qualified common candidate: none.

Python production representability did **not** become the terminal blocker in this execution: the unsupported `rb_gap`/`Tt` witnesses changed the liquid boundary outcome but did not restore a valid non-degenerate MATLAB solution. The terminal evidence therefore points to a remaining structural/full-integration diagnostic rather than permission to extend Python's economic contract.

## Persistence identities

External artifact root: `D:\ProjectTemp\ch5-pre-p5-adjustment-boundary-redesign-artifacts-20260829-191012`.

| Object | initial MAT SHA-256 | raw MAT SHA-256 | summary JSON SHA-256 |
|---|---|---|---|
| A | `C3BEC40D9018C74668C76F47FC999857578C96EF4EE4A48C107B15EAE645F57C` | `BC46CEA091E1372A8F51F6C4BBE23A6141FA84DCA6C857FBA9375D32E601817B` | `FACC4EAC020390D31B7713C57B7D7615DB002E372BC7D521AB76114F5EACB00C` |
| B | `266D71761DEAE27A6F6299EEEB2A4074D694206D364284E2AA55BA34BFFB420D` | `5BEF6B2CE5F15DEEFCC22F5BFA5B318F3FABD29B7AE10D46586B2910389C133F` | `3A5629E18DA70B3E5F6887970F2C7C124B40224E8C59BDF693BCAFF1B6CF8D94` |
| C | `EFF209AC4AA7AE2DC550FACFDE3CDE2B29453A87E32C4A713967CCB920BDB1E7` | `89F244568338F6872812BDF9E439F3975259CFD31E59DBD1F52A9574687D2354` | `D0AD1AD622F5DF42DB6A8B87EBE6DF2BD4221F30497A5EF2F9F1F4F0F6CF30F5` |
| W1 | `1CB1B0964121CF92C4CF7074FB9497565541B3E37D33E57BA9E2ACFB31DA873A` | `C6B5A09F9D7F8B38F1EC0374663673DF12A119A0B445ECC3644888C22458E9CD` | `9A4194B81608D19940CCA71A646786C98CC417781440E40FE367E6EFD0D605C9` |
| W2 | `359B504C2C2D636EBDF7E1E03B5956F2AB900D0F6723ACA157736F81A4D58149` | `FB943CCFDF451FD2CE25EF44D04417495D56EA0AEF620DB60521F7266EDBF34F` | `5E7E54FFCA8C6A92807D0FCB72EFDECA0E82B541F1A2A4B1A5BA19298CBEDC43` |

Each raw file was saved immediately after its HJB return and loaded successfully before summary serialization and before the next call.

## Files read and written

Repository/governance reads included the live task, `AGENTS.md`, the current rule index and GitHub authority-routing rule; all reports explicitly required by the task; accepted Python `contracts.py` and `economics.py`; the accepted original MATLAB HJB, cost, FOC and labor helpers; and the minimum native caller/cache material needed for field/grid/source provenance.

Repository write: only this report.

External writes: the timestamped root above containing the frozen manifest, static audit, verifier, frozen harness, copied accepted O1/O2 adapters, and for A/B/C/W1/W2 exactly one attempt marker, one initialization MAT, one raw MAT and one summary JSON. No raw artifact, cache, binary, harness, or adapter is staged for Git.

## Forbidden-operation check

PASS: no Python HJB, KFE or steady state; no Python `Tt`/`rb_gap` implementation; no third adapter; no MATLAB production/helper edit; no Python `src/tests` edit; no cache edit; no predecessor-candidate or P1–P4 rerun; no companion rate; no final four-run parity; no outer equilibrium, province, transition, AR(1), IRF, dynamics, calibration extension or Results execution; no tolerance/solver change; and no P5 acceptance.

## Recommended next gate

Publish a new exact, read-only-first structural diagnostic task. It should isolate the remaining full-integration differences—especially O1 low-`a` behavior under the common-Q/full-HJB combination, initialization/result-field dependence, and stationary-generator boundary structure—without modifying production code and without granting parity or P5 execution. The current task does not authorize further tuning or reruns.

