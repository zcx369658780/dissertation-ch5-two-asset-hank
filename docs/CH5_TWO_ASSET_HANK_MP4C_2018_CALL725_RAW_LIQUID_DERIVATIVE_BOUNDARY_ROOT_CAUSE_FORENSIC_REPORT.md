# MP4C 2018 call-725 raw liquid-derivative boundary root-cause forensic

## Authority, evidence, and zero-call boundary

This report was produced under
`CH5_TWO_ASSET_HANK_MP4C_2018_CALL725_RAW_LIQUID_DERIVATIVE_BOUNDARY_ROOT_CAUSE_FORENSIC`.
At audit start, live `origin/main` and `HEAD` were both
`9bd70b1db9f6286cd7de1903cc744ee9dcd6a4f6`, its direct parent was
`a0537d671b9d811979c95a9fa3b2424db352771f`, and the task blob was
`11a1d4a9ac34bd92d0ca97fa875363230ec9ee34`.  The tracked worktree was
clean with ahead/behind `0/0`.

The predecessor artifacts were reread, not regenerated:

| Artifact | SHA-256 |
| --- | --- |
| MATLAB `matlab_core_stagewise.mat` | `B863BBE5A3CF6327954C71520F609B9949FE9DEF64BA5225AA4CE9661392B69E` |
| Python `python_strict_stagewise.npz` | `CEAE235AC0DC62C1FCD0D9728F840DEEA1E12038ABFCE73CA0DA6BD449CE915F` |
| protected `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` |
| frozen Python source blob | `9e7dc9556a2b76811e78f89999abecc045886106` |

The durable predecessor ledger remains MATLAB iteration 1 = 1 and Python
strict iteration 1 = 1; native probe, retries, KFE, GE/annual, R/PLM, and
shock/IRF/Results remain 0. This forensic added 0 MATLAB HJB calls, 0 Python
HJB calls, 0 direct-solver calls, 0 native probes, and 0 downstream calls.

Fresh no-overwrite evidence root:
`D:\ProjectTemp\ch5-mp4c-2018-call725-raw-liquid-derivative-root-cause-20260904-001`.
Its finite manifest SHA-256 is
`50D3580A46BE5E6367DD1D11D2C4870E1206D18C9D0CDE8C6CC0A152E8F23EC4`;
the detached manifest-readback receipt is
`6A03B0B24314718CC0258AA523667FDECD84821E2EFBF8FBBE7F797518F77722`.

## Exact persisted-array topology

The machine-readable complete coordinate table contains all 80 coordinates,
with zero-based and MATLAB one-based indices and exact grid values.  It was
formed directly from the persisted arrays under the frozen rule
`abs(x-y) > 128*eps64*max(1,abs(x),abs(y))`.

| Field | Material entries | Interior | Lower `b` plane | Upper `b` plane | Maximum absolute difference |
| --- | ---: | ---: | ---: | ---: | ---: |
| raw `vb_f` | 40 | 0 | 0 | 40 | 0.01228045195367922 |
| raw `vb_b` | 40 | 0 | 40 | 0 | 0.012844718557132808 |

The dimensions are `(20, 20, 2)`, hence a complete liquid-boundary plane is
`20 * 2 = 40` points.  This is not an inference from the count: every
`raw_vb_f` coordinate has zero-based `b_index = 19` (`b = 5`), and every
`raw_vb_b` coordinate has zero-based `b_index = 0` (`b = -2`). All other
liquid-derivative coordinates, including each interior difference quotient,
are exact under the frozen rule.

## Stage semantics and source expressions

The MATLAB external wrapper writes its upper and lower boundary values on
lines 38 and 40, then copies `raw_VbF=VbF; raw_VbB=VbB` on line 43. Its
fields named `raw` are consequently post-boundary derivatives.

The Python external wrapper calculates the interior quotients and copies
`raw=[x.copy() for x in (vb_f,vb_b,va_f,va_b)]` before its boundary loop.
Thus its `raw_vb_f` upper boundary and `raw_vb_b` lower boundary retain their
initial zeros; its separately persisted `vb_f` and `vb_b` are post-boundary.

The protected MATLAB source was read only at logical path
`C:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m`.
`C:\MatlabProgram` is a Junction with target `D:\MatlabProgram`; the resolved
physical file read was therefore
`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m`.
Neither the file nor its immediate source parent exposed a further junction or
reparse target. MATLAB lines 116--119 establish
the interior forward/backward quotients and upper/lower overwrites; lines
79--80 establish the negative-`b` borrowing-rate branch; lines 26--31 bind
`rb`, `rah`, `w`, `rb_gap`, `tau`, and `Tt`; and line 44 fixes
`alphac=1` before the `(-ga)` marginal-utility exponent.

The frozen Python source uses the matching interior formulas on line 532,
the `b < 0` rate branch on lines 536/265, and the same
`((1-tau)*w*z*l0 + Tt + rb*b)**(-gamma_c)` boundary marginal utility on
lines 537--540. The normalized mapping receipt records each expression and
its source lines. No formula gap was found.

## Operand binding and deterministic replay

At every affected boundary coordinate, persisted MATLAB and Python `b`, `a`
(coordinate association), `z`, and `l0` match exactly as binary64 values.
The shared scalar binding re-hashed to
`A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6`:
`rb=0.02`, `rb_gap=0.07`, `tau=0.05`, `w=16.82014806560587`, `Tt=0.1`,
and `gamma=2`. No migration/wedge scalar enters this raw-boundary expression.

Pure arithmetic replay over those persisted operands (without an evaluator or
direct solve) gives post-boundary MATLAB-versus-Python maxima of
`1.734723475976807e-18` for both the upper-forward and lower-backward planes,
which pass the frozen rule. Python's pre-overwrite raw boundary slots are
exactly zero. The same result is reflected by the already-persisted
post-boundary `vb_f`/`vb_b` comparisons, which pass.

## Classification and future boundary

The strongest supported classification is:

`CALL725_RAW_VB_STAGE_NAMING_OR_PERSISTENCE_SEMANTICS_GAP_CONFIRMED__NO_PRODUCTION_CHANGE`

The earliest causal mechanism is a representation-stage mismatch: MATLAB
labels post-boundary derivatives as raw, while Python labels the pre-overwrite
interior arrays as raw. The 40/40 differences are therefore not an interior
finite-difference, boundary-formula, operand-binding, or side/index defect.

Any future change belongs only to a separately authorized external
wrapper/comparator staging decision. The Owner must first choose a single
meaning for the compared field (pre-overwrite interior or post-overwrite
boundary-adjusted); no protected MATLAB, Python production source, tolerance,
or model object may be changed on the basis of this report.

Terminal:

`MP4C_2018_CALL725_RAW_LIQUID_DERIVATIVE_ROOT_CAUSE_FORENSIC_COMPLETE__NO_RERUN_NO_KFE_NO_GE_NO_PRODUCTION_CHANGE`
