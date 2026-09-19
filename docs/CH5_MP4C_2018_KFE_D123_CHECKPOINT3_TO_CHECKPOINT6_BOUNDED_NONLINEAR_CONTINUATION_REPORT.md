# Chapter 5 MP4C-2018 D123 checkpoint 3 to checkpoint 6 bounded nonlinear continuation report

Date: 2026-09-19

Task: `CH5_MP4C_2018_KFE_D123_CHECKPOINT3_TO_CHECKPOINT6_BOUNDED_NONLINEAR_CONTINUATION_20260919`

## Terminal verdict

`COMPLETE_CHECKPOINT6_NONCONVERGED__TERMINAL_GATE_NOT_RUN`

The bounded trajectory reached a complete checkpoint 6.  The frozen primary
convergence law failed at checkpoints 4, 5, and 6.  No exact recurrence and no
authorized approximate period-2/3 recurrence was detected.  Execution stopped
at the checkpoint-6 ceiling.  Terminal topology and KFE were not run.  Results
eligibility is `FALSE`.

## Git and execution binding

- fresh live-main baseline: `28e74c0cfafd6826ea7f5600897d58608c58f44a`
- task branch: `codex/ch5-mp4c-2018-kfe-d123-checkpoint3-to-checkpoint6-bounded-nonlinear-continuation-20260919`
- accepted checkpoint-3 identity: `0DEEF7E54C4972BFF7BB67AE6B67BA5E54B588F3EEF5ACDE85048F3E02FE715D`
- implementation commit before runtime: `728a8926e4b0eaec276b1f53432ee96bb821bc3f`
- resume-repair/evidence-freeze commit before resume: `7599e32`
- focused engineering gate: `78 passed`; JUnit SHA-256 is recorded in the resume evidence
- `py_compile`: PASS
- `git diff --check`: PASS
- scientific code hash before/after the resume: exact match

One launcher command failed before Python could import the repository package
because `src` was absent from `PYTHONPATH`.  It created no evidence root, bound
no scientific input, and made zero scientific calls.  The launch environment
was corrected once.  The scientific ledger therefore correctly retains
`scientific_retries=0`.

## Preserved prefix and recovery boundary

The first scientific process used the original fresh root:

`reports/ch5_mp4c_2018_kfe_d123_checkpoint3_to_checkpoint6_bounded_nonlinear_continuation_20260919_run001/`

Its sealed manifest has SHA-256
`7BE53C6075C3B34680100921E65A3F98BEEE15C348681B2A241A2E6557C95030`,
815 entries, and 12,893,793 bytes.  It completed and persisted exactly:

- one V3-to-V4 direct solve;
- all 800 V4 selector evaluations and the complete P4/u4 map;
- one Q4/D2 assembly with D2 PASS;
- entry into checkpoint-4 evaluation.

It then stopped with `FAIL__SCIENTIFIC_GATE_AFTER_ENTRY` because the
approximate-cycle diagnostic applied `numpy.linalg.norm(..., ord=inf)` to a
three-dimensional value field.  The repair only flattens the difference in
the frozen F order before applying the adopted vector infinity norm.  The
resume loader verifies every sealed entry, the exact terminal receipt, exact
pre/post code hashes, V4/P4/Q4 identities, D2 PASS, and the cumulative ledger.
It does not rerun V3-to-V4, the V4 map, or Q4.

The no-overwrite resume evidence root is:

`reports/ch5_mp4c_2018_kfe_d123_checkpoint3_to_checkpoint6_bounded_nonlinear_continuation_20260919_resume001/`

Its sealed manifest has SHA-256
`1BFAB497357EE2740B259E23AD970EEB927799D9FD37A60A7D30E544E1970725`,
1,633 entries, and 26,156,422 bytes.

## Direct-solve receipts

All solves used the frozen `scipy.sparse.linalg.spsolve` equation with
`Delta=1000`; all normwise backward errors are below `1e-12`.

| update | residual infinity norm | normwise backward error | status |
|---|---:|---:|---|
| V3 to V4 | `3.9294956177826634e-14` | `7.540706588859553e-17` | PASS |
| V4 to V5 | `3.95794508278868e-14` | `1.61754874065192e-16` | PASS |
| V5 to V6 | `1.80966353013901e-14` | `1.73088198105602e-16` | PASS |

## Complete checkpoint metrics

| checkpoint | B_n | D_n | primary | exact cycle | approximate cycle | disposition |
|---|---:|---:|---|---|---|---|
| 4 | `0.179987383327527` | `0.0136984055627334` | FAIL | none | none | continue |
| 5 | `0.0317254872882517` | `0.0193420794201278` | FAIL | none | none | continue |
| 6 | `0.005940678766947715` | `0.010000685482095761` | FAIL | none | none | bounded stop |

Primary convergence was tested first using the inclusive thresholds
`B_n<=1e-8` and `D_n<=1e-7`.  The complete period-2 window was evaluated from
checkpoint 4 onward.  The complete period-3 window was first evaluated at
checkpoint 6.  Neither authorized approximate rule passed at tolerance
`1e-8`.  No trend-based stop was introduced.

### Identities

| checkpoint | V SHA-256 | P identity | u SHA-256 | Q artifact SHA-256 | checkpoint identity |
|---|---|---|---|---|---|
| 4 | `938682CEA35E4ED77F02087AB6BDE9204A0B4C00B9E898E3200799D1367C149B` | `8ACC7002ED5E77DA072F283DB86FD06C4ED00E7F42F6FB9672D123891B5774EE` | `2DB3FA93B25D701B6EB36FAEF2EDBEA24C4198393B48D2C12DA6B2D23FBF9B06` | `94432703101724F6F76317A00F9DDCA7583065AB7094416BDC03E85DDEB9AE91` | `69BA60083B3D96CDCFF1BE935AC425C04F68DF44A9FDB545209FA4280742F420` |
| 5 | `34077AE29E144E3BC5773A830A7577419EEE19B41424A7771C74E46554DECD6B` | `702010801BDC2559C97883852F0F662CE94859F299945BAEA2B7B8FD8917DB43` | `8D4F441128371ECFD685401489179D4DFAACB992D2325EDADAC58F9A5B835A2D` | `1BF6CB8031116064B8CF603243BDFA86565DD8A6B8B09EADEF409D0ADFD632E2` | `1CACE68D0BD30F24F16FB032ECCB6BCA2B2F939AF3A6B4556098DB1CBF577080` |
| 6 | `69865ACDD71A26A3E3F4A8DAD55C964F826D34C774C9B8193FE997973EE6D89F` | `63026FBE8BE72E3B29B5FC44EBD100C01C146179D05B55C779E9E232AEA435A3` | `09D5A6622535709146751865931109F058FED3688FAE755C5EF9A0E00AD8B89E` | `039734AF0BC38AD3BD0FF38854CBE8B4B0B93BA415EC2A47B1C09F827EA7F454` | `B26177C216DA6902226BD93E802A2B1FE0E794B29BE14EA1A1BCBFFD8F8691A1` |

All three D2 receipts are PASS.  Relative to the immediately preceding
checkpoint, selected-policy identity changes were 264, 800, and 108; Q
infinity-norm differences were `160.712284045792`, `68.2431435090027`, and
`24.162152198419452`.  Selected interior-a switching-policy counts were 24,
28, and 33.  Selected liquid-Z and joint-switching counts were zero at all
three checkpoints.  These are diagnostics only and are not termination laws.

## Exact cumulative scientific ledger

| item | count |
|---|---:|
| accepted V0/V1/V2/V3 loads | `1` each |
| accepted P2/u2/Q2/checkpoint-2 manifest loads | `1` each |
| accepted P3/u3/Q3/checkpoint-3 manifest loads | `1` each |
| accepted Q1 loads | `1` |
| direct HJB solves / HJB updates | `3 / 3` |
| fresh corrected policy maps | `3` |
| selector evaluations | `2400` |
| scalar roots, total | `821` |
| liquid-Z roots | `51` |
| interior-a switching roots | `4` |
| joint-switching roots | `0` |
| D2/Q assemblies | `3` |
| complete checkpoint evaluations | `3` |
| V2 or V3 policy-map reruns | `0` |
| Q2 or Q3 assembly reruns | `0` |
| scientific retries | `0` |
| solver substitutions | `0` |
| damping/relaxation/adaptive-Delta/continuation | `0` |
| parameter continuation/clipping/artificial diffusion | `0` |
| graph/SCC and terminal topology gates | `0` |
| KFE/SVD/eigen/nullspace/Q.T@p | `0` |
| MATLAB/production/outer/firm/GE/annual/shock/IRF/Results | `0` |

The three-map, 2,400-selector, three-Q, three-evaluation, and three-update
ceilings were reached but not exceeded.  The reused checkpoint-4 prefix is
included once in these cumulative counts.  The resume did not double-count
or repeat its already completed scientific objects.

## Scope closure

No newly exposed scientific defect was repaired.  No terminal KFE or
downstream computation was attempted.  No CURRENT file was modified, main was
not merged, and no successor task was published.  This candidate requires the
next independent review gate before any further continuation or terminal gate.
