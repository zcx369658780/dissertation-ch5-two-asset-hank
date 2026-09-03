# MP4C MATLAB `load_GDPdata` model-unit scaling audit

## Terminal verdict

`MP4C_MATLAB_LOAD_GDPDATA_UNIT_SCALING_AUDIT_PASS__PYTHON_OWNER_A_RUNTIME_UNIT_CONTRACT_CONFIRMED__NO_PATCH__NO_SCIENTIFIC_RERUN`

The Owner's concern was tested as an end-to-end model-unit lineage question,
not merely by confirming two literals.  The current Python Owner-A input path
uses the same source-to-model factors and directions as the protected MATLAB
runtime contract: GDP x1000, capital x1000, and population/employment x100.
No deterministic unit-factor defect exists, so no input patch and no scientific
rerun are authorized or required.  The existing 2018 KFE blocker is unchanged.

## Continuity and protected identities

- Live task authority: `17b907676a7917c8c7daedaee5ae1534bf4e3c87`, direct
  child of `e12abaae0d57c85b5eb20693fd4d7d7ad18ca8b9`.
- Start state: `HEAD == origin/main == 17b907676a7917c8c7daedaee5ae1534bf4e3c87`,
  ahead/behind `0/0`, tracked worktree clean.
- MATLAB primary root (read only):
  `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`.
- Protected runtime cache SHA-256:
  `923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A`.
- The source identity manifest records every MATLAB/Python/R/workbook hash at
  the external evidence root below.

## Exact MATLAB multiplier path

`multi_prov_HANK_12sts.m:81` actively sets
`param.GDP_multiplier=1000; param.POP_multiplier=100;`; line 128 passes both
into `load_GDPdata`.  The active industry-4 loader arithmetic is:

| Runtime field | Active workbook sheet | MATLAB expression | Source-to-model factor |
| --- | --- | --- | --- |
| GDP | `GDP` | `temp1(:,2:32) * GDP_multiplier` | x1000 |
| CAP | `总资本存量` | `temp2(:,2:32) * GDP_multiplier` | x1000 |
| POP | `常住人口` | `temp3(:,2:32) * POP_multiplier` | x100 |

`R语言计算资本存量` and `就业人数` are only commented alternatives in
`load_GDPdata.m:76-80`; they are not legacy MATLAB runtime sources.  The loader
constructs `log_pgdp=log(GDP/POP)` and `log_pcap=log(CAP/POP)`, so each runtime
per-capita ratio includes the net x10 implied by x1000 divided by x100.  Both
scalars are stored into the cache.

## Downstream read/use trace

There is no hidden second application of either multiplier:

- `mpHANK_equilibrium_2000.m:27-40` directly transfers cache CAP to
  `Kt0/Kt/Kt_1`, POP to `N/Lt/Lt_1`, GDP to `Yt0/Yt`, and CAP to `GovInv`
  through `GovInv_ratio=1`; it exponentiates the already-scaled cached logs.
- Neither `HANK_mp_1eq.m` nor `HANK_mp_1turn.m` reads a multiplier symbol.
  They consume inherited state scales in `Yt/Lt` migration terms,
  `inter_prv_ratio * At * N` capital aggregation, and `Bt * rb * N` fiscal
  aggregation.
- `HANK_firm.m` uses `Kt_supply + GovInv` and `Lt_supply` in production,
  return, wage, tax, and government-income blocks.  Therefore an inversion or
  missing factor would affect economic state magnitudes; it is not cancelled in
  a later firm/fiscal operation.
- `main.m:167-172` (with duplicate `main2.m:164-169`) divides Yt0/Yt/Kt0/Kt
  by 1000 and N/Lt by 100 before writing `12年稳态值.xlsx`.  This is the inverse
  runtime-to-display conversion, not input scaling.  `N` is displayed as Lt0.

## Numeric workbook-to-cache proof

Read-only sampling covers Beijing, Henan, Guangdong, Tibet, and Xinjiang at
2000, 2011, and 2022 (15 province-year observations).  Every cached level was
bitwise equal to its active source workbook level multiplied by the stated
factor: GDP/CAP x1000 and POP x100.  The largest log consistency residual was
`2.220446049250313e-16` for `log_pgdp` and `0` for `log_pcap`, ordinary binary64
evaluation noise only.  Cache metadata recorded 1000/100 in every sampled
entry.  The CSV preserves raw values, cache values, ratios, expected equality,
and both log recomputations.

## Python comparison and provenance boundary

`accepted_source_scalars()` fixes exactly 1000/100.  The Owner-A builder applies
GDP x1000, `R语言计算资本存量` x1000, and `就业人数` x100, recomputes both logs,
and transfers those model units unchanged into `Yt0/Yt`, `Kt0/Kt/Kt_prev`,
`N/Lt/Lt_prev`, and `GovInv`.  Its legacy-compatible serializer makes the same
inverse 1000/100 display conversion; the `final_31x20` remains in model units.

| Field | Classification |
| --- | --- |
| GDP | `PYTHON_UNIT_TRANSFORM_EXACTLY_MATCHES_MATLAB_RUNTIME` |
| CAP | `PYTHON_UNIT_TRANSFORM_FIELD_SOURCE_DIFFERS_BUT_UNIT_FACTOR_MATCHES` |
| POP | `PYTHON_UNIT_TRANSFORM_FIELD_SOURCE_DIFFERS_BUT_UNIT_FACTOR_MATCHES` |

The CAP/POP classifications deliberately retain the Owner-A source differences
(`R语言计算资本存量` versus `总资本存量`; `就业人数` versus `常住人口`).  They are
provenance distinctions, not multiplier-scale defects.  R's current estimation
contract happens to use the same numeric factors as Owner-A, but is reported
separately and is not used to redefine the protected MATLAB runtime contract.

## Evidence and execution boundary

Fresh no-overwrite evidence root:

`D:\ProjectTemp\ch5-mp4c-matlab-load-gdpdata-unit-scaling-audit-20260903-001`

It contains the source/hash receipt, literal audit, 15-row numerical CSV,
cache/state and state/workbook lineages, separate R/MATLAB/Python contracts,
comparison CSV, verdict JSON, zero-science ledger, and hash manifest.

Only source-text reads, protected XLSX XML parsing, protected HDF5 cache reads,
and evidence writing occurred.  Python stationary, household/HJB/KFE, MATLAB
model, R/PLM, 2018 retry, comparator, shock/IRF/R5, and Results calls all remain
exactly zero.

## Next authorized gate

No source/input correction follows from this audit.  Any further 2018 diagnosis
or annual execution requires a new live task; this report preserves the existing
2018 singular-KFE blocker without asserting causality.
