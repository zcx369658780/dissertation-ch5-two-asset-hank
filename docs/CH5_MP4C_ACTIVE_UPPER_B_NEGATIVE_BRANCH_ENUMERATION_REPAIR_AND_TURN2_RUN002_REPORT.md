# CH5 MP4C active upper-b negative branch repair and turn-2 run002 report

Date: 2026-09-20

## Terminal verdict

`FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE`

The authorized active-upper-b negative-transfer enumeration repair passed its
zero-science gates and exact F0579 parity check.  The single fresh turn-2 run002
then stopped at the first new scientific failure: Beijing, checkpoint 5,
F-order flat index 364, selector outcome `NO_ADMISSIBLE_POLICY`.  No scientific
retry or repair was attempted.

## Authority and code freeze

- actual live-main baseline: `f0885e30832f30f3259f0549f6831fa9c17f6905`
- pre-science code-freeze commit: `ac198ce7`
- task: `CH5_MP4C_ACTIVE_UPPER_B_NEGATIVE_BRANCH_ENUMERATION_REPAIR_AND_TURN2_RUN002_20260920`
- entering-state blob: `85df3f0bdcc3b0bb3e7b12f0ba35dbb9abda764d`
- entering raw-payoff identity: `D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414`
- forensic run002 manifest: `0DB648C10B42F5A8A187334FACEC123F9FD231999E09F650FE19C33114F420B4`
- turn-2 run001 manifest: `50D2E87C94E762D3936C64E3AAD416F600118AEBB8DCE1588DB369938FA2351A`
- canonical initial-integration manifest: `79C6B15340AF641A736C79D0ED7C6450E39EA495263943280B6DDBD1B094F28D`
- cost, generator, nonlinear HJB/KFE, and turn-2 integration source blobs matched the baseline.
- post-execution source hashes matched the pre-execution freeze.

The selector change is limited to exempting active `upper_b` + `negative`
from the pre-root single-branch count gate.  The existing viability screen,
branch-specific root path, post-root checks, deduplication, Hamiltonian ordering,
and tie rule remain in force.

## Zero-science preservation gate

Focused and regression tests: 18 passed.  `py_compile` and `git diff --check`
passed before science.

The predecessor impact audit read every persisted JSON receipt in the specified
roots:

| target | JSON receipts | cell receipts | candidate dictionaries | target token files | matches |
|---|---:|---:|---:|---:|---:|
| accepted turn-1 run004 household | 2665 | 0 | 0 | 0 | 0 |
| reached turn-2 run001 checkpoint 0/1 | 11 | 0 | 0 | 0 | 0 |

These accepted roots use compact checkpoint evidence and do not persist rejected
candidate dictionaries.  The known checkpoint-2 F0579 partial receipt was
excluded exactly as required.  The preservation set is empty.

## F0579 repair parity

The formal receipt was captured from the normal Beijing checkpoint-2 map; it
did not invoke an additional selector or root path.

- backward branch root: `0.004697887028753478`; rejected only by
  `A_DERIVATIVE_DIRECTION_INCONSISTENT`
- forward branch selected: `q_b=0.00470259773014529`,
  `q_a=-0.0004814219651986697`, `d=-2.1102602580753396`,
  `g_a=1.6015031989929152`
- transfer-KKT residual: `6.505213034913027e-19`
- Hamiltonian: `-0.07995936564187259`
- selector root invocations for F0579: 4

All exact forensic parity checks passed.

## Reached HJB checkpoints

Only Beijing was reached.  Checkpoints 0 through 4 completed their policy map,
D2/Q assembly, and direct update.  Primary convergence failed at every evaluated
post-update checkpoint, with no exact or approximate period-2/3 cycle.

| checkpoint | B | D | D2 | primary | direct-solve backward error |
|---:|---:|---:|---|---|---:|
| 0 | 0.35948978452765235 | N.A. | PASS | N.A. | 2.1754586146795478e-16 |
| 1 | 0.019968227378343403 | 0.5603661628256393 | PASS | FAIL | 1.4650295837509506e-16 |
| 2 | 0.0072664556369222005 | 0.01838411533067008 | PASS | FAIL | 1.6676439766061158e-16 |
| 3 | 0.10349094906054289 | 0.015768036556986775 | PASS | FAIL | 1.352321353333044e-16 |
| 4 | 0.1804040891891172 | 0.010078032277111681 | PASS | FAIL | 8.036417542743297e-17 |

The maximum direct-solve backward error was
`2.1754586146795478e-16`, below the frozen `1e-12` ceiling.

Selected-policy active-constraint counts for checkpoints 0 through 4 were,
respectively:

- checkpoint 0: none 720, lower-a 40, upper-a 40;
- checkpoint 1: none 760, upper-a 40;
- checkpoint 2: none 732, lower-b 10, upper-b 18, upper-a 39,
  upper-a+upper-b 1;
- checkpoint 3: none 722, lower-b 19, upper-b 19, upper-a 38,
  lower-b+upper-a 1, upper-a+upper-b 1;
- checkpoint 4: none 723, lower-b 19, upper-b 19, upper-a 37,
  lower-b+upper-a 1, upper-a+upper-b 1.

Q nnz was 3080, 3119, 3091, 3085, and 3115.  Each D2 receipt passed all
off-diagonal, diagonal, conservation, coordinate-action, and closed-face gates.
Liquid-z selected-policy counts were 40, 41, 40, 35, and 6; interior-a and joint
switching selected-policy counts were zero throughout.

## First scientific failure

- province: Beijing (`province_index=0`)
- checkpoint: 5
- F-order flat index: 364
- grid index: `(b_index=4, a_index=18, z_index=0)`
- physical state: `b=-0.5263157894736843`,
  `a=9.473684210526315`, `z=0.8`
- outcome: `NO_ADMISSIBLE_POLICY`
- D2/Q at checkpoint 5: not run because the policy map stopped first

The durable cell receipt contains eight attempted candidates.  Their rejection
reasons are combinations of the existing a/b derivative direction checks,
transfer KKT check, and positive-transfer sign check.  No selector exception
occurred.  This newly exposed scientific issue was not repaired inside the task.

## Exact run002 scientific ledger

The exception-path runtime snapshot omitted the partial checkpoint-5 map.  A
deterministic reconciliation used only the durable cumulative budget in
`checkpoint_005/cell_0364.json`; it made no scientific call.

- source-native initializations: 1
- labor roots attempted/returned: 800/800
- policy maps started: 6 (5 complete, 1 partial)
- selector evaluations: 4365
- scalar selector roots: 2262
- interior-z roots: 642
- interior-a switching roots: 0
- joint switching roots: 0
- D2/Q assemblies: 5
- direct HJB updates: 5
- post-update checkpoint evaluations: 4
- SCC / restricted GESVD / full-space GESVD / normalized candidate / `Q.T@p`:
  0 / 0 / 0 / 0 / 0
- aggregates / household batch / K1A / C1 / firms / wage / monetary / fiscal /
  raw-next-payoff: all 0
- scientific retries / solver substitutions / damping or continuation /
  payoff transformations: all 0
- turn-3 household calls / third outer turns / K1B / K2 / adaptive controller /
  MATLAB / GE / annual / shock / IRF / welfare / Results: all 0

Historical run001 and forensic consumption is retained as lineage and is not
merged into this run002 ledger.

## Evidence

- root:
  `reports/ch5_mp4c_corrected_optionb_turn2_upper_b_negative_repair_20260920_run002`
- sealed manifest SHA-256:
  `A2A882B8D79A6897D0518447FA84F7775609E31D34452A5EB2F7B7773E9FD0B0`
- entries: 430
- bytes: 6,449,626
- independent readback: PASS, zero bad paths

Turn 3 was not run.  No CURRENT file was modified, no successor was published,
and main was not merged.
