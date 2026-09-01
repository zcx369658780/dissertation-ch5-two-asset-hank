# MP4C MATLAB active data-source confirmation and Python local-copy staging report

Date: 2026-09-01

## Terminal

`MP4C_MATLAB_ACTIVE_DATA_SOURCE_CONFIRMATION_AND_PYTHON_LOCAL_COPY_STAGING_PASS`

Required markers:

- `MP4C_MATLAB_ACTIVE_DATA_FILENAMES_SOURCE_CONFIRMED`
- `MP4C_PYTHON_LOCAL_PRIMARY_SOURCE_COPY_HASH_IDENTICAL`
- `MP4C_FILLED_NA_ANNUAL_SOURCE_CONFIRMED_ACTIVE`
- `MP4C_DERIVED_MAT_CACHE_EXCLUDED_FROM_PRIMARY_COPY_SET`
- `MP4C_LOCAL_DATA_COPY_READY_FOR_2010_2023_BATCH`

This is data-provenance and byte-copy staging only. It does not authorize or execute an annual stationary run.

## Live authority and continuity

- Live task authority and execution-start `HEAD`: `0c9c15a93ec5973d3345f8921d122c5a336c418e`.
- Required direct parent: `59c0611a265854597f47713ad9ee981e7e569ecd`; exact match.
- After fresh fetch and fast-forward, `HEAD == origin/main`, ahead/behind `0/0`, and the worktree was clean.
- The complete task, `AGENTS.md`, all task-named current project rules, predecessor MP4C task/report, formal corrected-2009 acceptance report, MP4A2 task/report, annual input API, and protected MATLAB loader/caller chain were read before any copy.

Accepted scope remains 2009–2023 inclusive. Corrected-2009 remains the accepted anchor and was not regenerated or rerun. Future execution remains 2010–2023 only.

## Protected root identity

`C:\MatlabProgram` is a Junction whose exact target is `D:\MatlabProgram`. The protected project therefore has:

- logical root: `C:\MatlabProgram\2023年12月2日 多省份神经网络HANK`;
- physical root: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`.

The logical and physical `load_GDPdata.m` bytes hash identically. The D root was treated as the physical storage backing the protected C root, not as an independent mutable copy.

## Protected MATLAB source confirmation

| Role | Protected expression and caller chain | MATLAB-consumed filename | Bytes | SHA-256 |
|---|---|---|---:|---|
| Annual GDP/CAP/POP | `multi_prov_HANK_12sts.m:128 -> load_GDPdata`; `load_GDPdata.m:5` sets `writefile`; lines 74, 75 and 79 read GDP, total capital stock and resident population from it | `2000年后各省数据_填充NA.xlsx` | 171,292 | `C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929` |
| Regression inputs | `load_GDPdata.m:115` sets `regfile`; lines 117–124 construct and read annual coefficient/intercept sheets | `R语言估计结果_plm估计.xlsx` | 361,927 | `A6F444FCCCB30CB93AA5DE084F1DD163C54E5F53C4287C2CD3E13A045EB64A68` |
| Inter-province distance | `multi_prov_HANK_12sts.m:133 -> mpHANK_equilibrium_2000.m:17 -> load_distdata.m:6` | `中国各省省会地理距离矩阵.xlsx` | 39,895 | `26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566` |

Each source exists exactly once at the expected protected physical root. Relevant source identities are:

- `load_GDPdata.m`: `DECA8AF3F22097550B8957FE848989E6342619CB9929A1C00076E020549366C5`;
- `load_distdata.m`: `18F594DD7D1ED090CA2AF576DEBCD8DCAA73C012608A8921F8D5BD6CC24F478B`;
- `multi_prov_HANK_12sts.m`: `3C44449CFD4047B5C9E17E540AFEA2F50B4251150F8F74AB8CCEED26E15DEC97`;
- `mpHANK_equilibrium_2000.m`: `26EA44552DA33919F8CCD777C084E15ECA0EA9575FEE80A07F9E0056F3F97DE5`.

### Active, fallback and cache distinction

The filled-NA workbook is active. `load_GDPdata.m:7–9` reads `2000年后各省数据.xlsx` only if the filled `writefile` does not exist. The filled file currently exists; the unfilled workbook is therefore an inactive fallback and was not copied. Its frozen identity is 119,265 bytes, SHA-256 `09814A45D933B2685A35238A15C0C7BB501F00A63597796B3CADCE15C230ECB3`.

`load_GDPdata.m:106–110` can use `数据估计结果_1000_100_0.mat` as a runtime shortcut. That object remains a derived/cache representation, not primary scientific authority. It was explicitly excluded from the copy set: 2,421,344 bytes, SHA-256 `923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A`.

## Ignored byte-copy staging

One narrow ignore rule was required and added:

`data_local/`

No broad `.xlsx`, `.mat`, or data wildcard was added. Before any binary write, `git check-ignore -v` proved all three exact target paths were covered by that rule.

Local ignored copy directory:

`D:\ProjectTemp\ch5-pre-p5-controlled-household-exec-repo-20260829\data_local\matlab_primary_source_snapshot`

| Filename | Disposition | Source/copy bytes | Source/copy SHA-256 | Result |
|---|---|---:|---|---|
| `2000年后各省数据_填充NA.xlsx` | `COPY` | 171,292 / 171,292 | `C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929` / same | byte-identical |
| `R语言估计结果_plm估计.xlsx` | `COPY` | 361,927 / 361,927 | `A6F444FCCCB30CB93AA5DE084F1DD163C54E5F53C4287C2CD3E13A045EB64A68` / same | byte-identical |
| `中国各省省会地理距离矩阵.xlsx` | `COPY` | 39,895 / 39,895 | `26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566` / same | byte-identical |

Files retained their exact names. No workbook was opened in Excel/LibreOffice, rewritten by a spreadsheet library, renamed, transformed or overwritten.

## Zero-science compatibility checks

Static inspection confirms `PrimaryAnnualSourceFiles` accepts explicit filled/regression/distance `Path` values plus expected hashes, and `load_primary_annual_input` consumes those explicit fields. ZIP/XML metadata reads against the local copies established:

- GDP, total-capital-stock and resident-population sheets each expose exact 2009–2023 calendar rows;
- C:AG values are complete for all 15 rows;
- each annual sheet has the exact accepted 31-province order;
- all required `总面板回归系数_10_行业4` through `_24_行业4` sheets exist;
- distance `geom` is complete 31x31 and both axes exactly equal the accepted province order;
- all copied SHA-256 identities equal the protected originals.

The corrected-2009 canonical input was not regenerated. No household or stationary API was called.

## External evidence package

Fresh no-overwrite root:

`D:\ProjectTemp\ch5-mp4c-matlab-data-source-confirmation-python-copy-20260901-001`

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `annual_input_local_path_compatibility.json` | 907 | `FCA1F7858A6E65FA4DABEB0F5F466D5BF9D4894367B8D2DE450BFABA442147F0` |
| `matlab_active_data_source_map.json` | 2,382 | `DF2F798E2DE3F230E0EC895A96A2A2BB5042E871FF186C09AE773FE0A87839E9` |
| `python_local_copy_manifest.json` | 2,176 | `9FCB4A93EE381E8B619C4670797655A0305DFBCABF3F6D8C1E4CB7BD8297ADA1` |
| `source_file_identity_manifest.json` | 1,552 | `1AD5B3A5C28895705F5EA645D54C903129365EA8F71215A0322AD00995FF7DEC` |
| `source_vs_copy_hash_matrix.json` | 923 | `542D161DA8559AAD7DA84F703BE7497ED2058D20097A547E8C159497110480A1` |
| `zero_model_execution_ledger.json` | 528 | `151AF097F11CEE00C4D11D8C3D2416A0003E5E24441ECC441C60F91FBC80D1BF` |
| `staging_manifest.json` | 2,102 | `846EB437181E39F3E324E91198240F06955B2A86B271D39CE2B1435072726BAB` |

All seven JSON artifacts parsed successfully. The staging manifest records the other artifact receipts; its own identity is recorded here to avoid impossible cryptographic self-reference.

## Zero-model ledger and repository scope

| Operation | Calls |
|---|---:|
| MATLAB process/checkcode/model/stationary/HJB/KFE/household/firm/controller | 0 |
| Python stationary/HJB/KFE/household/MP2/MP3 | 0 |
| Comparator | 0 |
| Annual batch | 0 |
| Shock/AR(1)/transition/dynamics/IRF | 0 |
| R5/Results | 0 |

Repository mutations are exactly `.gitignore` and this report. Copied binary files are ignored local assets, remain unstaged, and are not Git/GitHub mutations. No source workbook, protected MATLAB file, cache, canonical artifact, scientific Python code, comparator, threshold, tolerance, model result, or prior evidence was changed.

## Exactly one recommended next gate

Bounded 2010–2023 Python annual stationary batch execution using the verified local primary-source copies and the frozen MP4C compute budget.
