# CH5 Two-Asset HANK MATLAB-Python HA P3/P4 Generator-KFE Numerical Parity

## Terminal classifications

- P3: `MATLAB_PYTHON_TWO_ASSET_HA_P3_GENERATOR_PARITY_PASS`
- P4: `MATLAB_PYTHON_TWO_ASSET_HA_P4_KFE_STATIONARY_PARITY_PASS`
- overall evidence: `MATLAB_PYTHON_TWO_ASSET_HA_NUMERICAL_PARITY_EVIDENCE_COMPLETE__OWNER_P5_ACCEPTANCE_PENDING`
- predecessor reuse: `P1_P2_EVIDENCE_REUSED_AND_ACCEPTED`

This completes the bounded P1-P4 numerical evidence. It does not issue Owner P5 acceptance and does not authorize dynamics or Results work.

## Live/source/runtime/workspace identity

- repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- fresh-fetched live/base `origin/main`: `aa2d31fbf38bc09da7dc99261d6f4dc577843efd`
- accepted Python scientific/test baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`
- accepted P2 evidence commit: `565c6564e5e5083183c853e65bca09c3bf1b9f05`
- isolated Git workspace: `D:\ProjectTemp\ch5-ha-p3-p4-parity-repo-20260829`
- external artifact root: `D:\ProjectTemp\ch5-ha-p3-p4-parity-20260829`
- `git diff 7a2388a2ba89073e307f05a909570e8c40a4be13..aa2d31fbf38bc09da7dc99261d6f4dc577843efd -- src tests`: empty
- MATLAB: `C:\Program Files\MATLAB\R2022b\bin\matlab.exe`, version `9.13.0.2049777 (R2022b)`
- Python: `C:\Users\zcxve\AppData\Local\Programs\Python\Python311\python.exe`, version `3.11.9`
- Octave substituted: no

The three MATLAB source identities passed:

| File | Bytes | SHA-256 |
|---|---:|---|
| `HANK_2ASSETS_HJB.m` | 12227 | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` |
| `HANK3_cost.m` | 691 | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` |
| `HANK3_FOC.m` | 565 | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` |

## Predecessor evidence verification

The two accepted predecessor roots were inspected read-only. Every required identity matched:

| Accepted object | Bytes | SHA-256 |
|---|---:|---|
| P1 MATLAB output | 146443 | `74A7C134F48948B89A10C9F8F72F81BBD6B4B7137F954A4458072193550BA886` |
| P1 Python output | 217784 | `359A07B6987417499DCB28EE7E7B7E6706480C7810ECAC4372E4B2D9C61650FD` |
| P1 comparison | 26665 | `41F02D4A0595C453E0DA3BB2A1D80DDBE53C43DF906C69D05F08BF4EF2ADA550` |
| P2 corrected MATLAB output | 3093 | `632486B34D952F88E0884E25A15DCBA1A476ADFF4D04792D36FEBED4CC39811C` |
| P2 accepted Python output | 5647 | `E27F3B557123B8ED1BBFB8986B63861075C43106264EAAC4FC867797E237978A` |
| P2 comparison | 2366 | `0851FD1AF8899594B21BC01F593B329918E56C06F5CEA68901A28EDD49B1AE56` |
| shared `manifest.json` | 2329 | `3D2A35A7118CFEE479C05C1339AB247D78F5A71BBA044779AAB678D59E72D449` |
| orientation verification | 385 | `B7ED9CE9FD7D4AFC1C1AE704DF4E16006AE3FA07752319C005D4CA4EA06C7DF2` |

Decision: `P1_P2_EVIDENCE_REUSED_AND_ACCEPTED`. Neither stage was rerun.

## Frozen P3/P4 harnesses and preflight

All six never-before-executed harnesses matched their frozen identities after byte copy:

| Harness | Bytes | SHA-256 |
|---|---:|---|
| `p3_matlab.m` | 914 | `8695C99E9E5591C5DCBC8EDF9DCA958DE9D9E2F58C4388D45FC5A0A184D92C51` |
| `p3_python.py` | 985 | `4D99C21DD95D4CEC45D627BA17ED4853EB6066EC7DD6BA26E4957739F1608622` |
| `compare_p3.py` | 1200 | `4504A7118EE222C859FF2DCA0133AE12DCF6298592019B3C8ADE7D2CA9FDE267` |
| `p4_matlab.m` | 679 | `9549C508E208D4507FC59392766D9408232371F2210ACFA487A14F8B6C3E9B34` |
| `p4_python.py` | 992 | `FE47FF72613E8E685AE6B9B107A5E6884993196CCE88B286F8ABA7B5B39A9893` |
| `compare_p4.py` | 1614 | `5533E22A60876E6B448FD938B79034E2F03F1DE51A83D65C5D7A1946E1879CDE` |

Pre-scientific review results:

- Python static compilation: PASS for all four Python harness/comparison files;
- MATLAB `checkcode`: zero issues for P3 and P4;
- production signatures: `_asset_generator(grid,drift,axis,tolerance)`, `make_kfe_input(generator,shape,cell_weights)`, and `solve_stationary_kfe(kfe_input,grid,*,...)` match harness calls;
- JSON: manifest and `p3` decode as MATLAB structs, vectors as doubles, `Q_common` as `2x2 double`;
- dimensions: `3x3x2=18` states, expected matrices `18x18`, `Q_common 2x2`;
- orientation: `[0,3,6,1,4,7,2,5,8,9,12,15,10,13,16,11,14,17]`; exact round trip PASS.

No plumbing defect was found. No corrected harness was created and no harness diff exists.

## Exact execution counts and output identities

| Stage/action | Count | Result |
|---|---:|---|
| P1 scientific/comparison | 0 | reused |
| P2 scientific/comparison | 0 | reused |
| MATLAB P3 | 1 | complete |
| Python P3 | 1 | complete |
| P3 comparison | 1 | PASS |
| MATLAB P4 | 1 | complete |
| Python P4 | 1 | complete |
| P4 comparison | 1 | PASS |

| Output | Bytes | SHA-256 |
|---|---:|---|
| `p3_matlab.json` | 3596 | `434E911B01261E8520C70090322D0083B76731689B16BF450B8CE50A40E3ABC6` |
| `p3_python.json` | 16959 | `7DA250A6F54D4C5C6BDFCFCC3977D86E600A9813D5DA2AFADBDC006366309AF2` |
| `p3_compare.json` | 1144 | `17A883EA3E6C69EB2521664D8723031174ADEC943EEFDB170C5EB5A4AEDCA7E5` |
| `p4_matlab.json` | 612 | `06A867DF082C35C13BF17964AE43E8B1020C8E0A511A98A97E143A2EA6C07EE6` |
| `p4_python.json` | 744 | `C690F66CDB570C3B9E7F7A32867FDBB1743710B7AC0B104EE2F0B2C646B37C94` |
| `p4_compare.json` | 1744 | `76C8DC5408A50D895C01A7D5B14FC67DED53247AC418F25C8403FF512AFAB388` |

## P3 complete generator evidence

Frozen object: `a=[0,0.5,1]`, `b=[0,2.5,5]`, `z=[0.75,1.25]`, `Q_common=[[-0.4,0.4],[0.3,-0.3]]`. Rows and destinations below are zero-based Python canonical indices after the frozen MATLAB-to-Python adapter. Unlisted entries are exactly zero. For every listed component and every row, mapped MATLAB and Python values are identical.

### Asset-component destination/rate/diagonal inventory

| Row | `G_a`: diagonal; destination:rate | `G_b`: diagonal; destination:rate | `G_z`: diagonal; destination:rate |
|---:|---|---|---|
| 0 | `-0.04; 1:0.04` | `-0.012; 3:0.012` | `-0.4; 9:0.4` |
| 1 | `-0.03; 2:0.03` | `-0.012; 4:0.012` | `-0.4; 10:0.4` |
| 2 | `-0.04; 1:0.04` | `-0.012; 5:0.012` | `-0.4; 11:0.4` |
| 3 | `-0.04; 4:0.04` | `-0.008; 6:0.008` | `-0.4; 12:0.4` |
| 4 | `-0.03; 5:0.03` | `-0.008; 7:0.008` | `-0.4; 13:0.4` |
| 5 | `-0.04; 4:0.04` | `-0.008; 8:0.008` | `-0.4; 14:0.4` |
| 6 | `-0.04; 7:0.04` | `-0.012; 3:0.012` | `-0.4; 15:0.4` |
| 7 | `-0.03; 8:0.03` | `-0.012; 4:0.012` | `-0.4; 16:0.4` |
| 8 | `-0.04; 7:0.04` | `-0.012; 5:0.012` | `-0.4; 17:0.4` |
| 9 | `-0.05; 10:0.05` | `-0.012; 12:0.012` | `-0.3; 0:0.3` |
| 10 | `-0.03; 9:0.03` | `-0.012; 13:0.012` | `-0.3; 1:0.3` |
| 11 | `-0.05; 10:0.05` | `-0.012; 14:0.012` | `-0.3; 2:0.3` |
| 12 | `-0.05; 13:0.05` | `-0.008; 9:0.008` | `-0.3; 3:0.3` |
| 13 | `-0.03; 12:0.03` | `-0.008; 10:0.008` | `-0.3; 4:0.3` |
| 14 | `-0.05; 13:0.05` | `-0.008; 11:0.008` | `-0.3; 5:0.3` |
| 15 | `-0.05; 16:0.05` | `-0.012; 12:0.012` | `-0.3; 6:0.3` |
| 16 | `-0.03; 15:0.03` | `-0.012; 13:0.012` | `-0.3; 7:0.3` |
| 17 | `-0.05; 16:0.05` | `-0.012; 14:0.012` | `-0.3; 8:0.3` |

### Full common generator sparse-row representation

This is a complete representation of the `18x18` total matrix; every omitted cell is zero.

| Row | Diagonal | Off-diagonal destinations and rates |
|---:|---:|---|
| 0 | `-0.452` | `1:0.04, 3:0.012, 9:0.4` |
| 1 | `-0.442` | `2:0.03, 4:0.012, 10:0.4` |
| 2 | `-0.452` | `1:0.04, 5:0.012, 11:0.4` |
| 3 | `-0.448` | `4:0.04, 6:0.008, 12:0.4` |
| 4 | `-0.438` | `5:0.03, 7:0.008, 13:0.4` |
| 5 | `-0.448` | `4:0.04, 8:0.008, 14:0.4` |
| 6 | `-0.452` | `3:0.012, 7:0.04, 15:0.4` |
| 7 | `-0.442` | `4:0.012, 8:0.03, 16:0.4` |
| 8 | `-0.452` | `5:0.012, 7:0.04, 17:0.4` |
| 9 | `-0.362` | `0:0.3, 10:0.05, 12:0.012` |
| 10 | `-0.342` | `1:0.3, 9:0.03, 13:0.012` |
| 11 | `-0.362` | `2:0.3, 10:0.05, 14:0.012` |
| 12 | `-0.358` | `3:0.3, 9:0.008, 13:0.05` |
| 13 | `-0.338` | `4:0.3, 10:0.008, 12:0.03` |
| 14 | `-0.358` | `5:0.3, 11:0.008, 13:0.05` |
| 15 | `-0.362` | `6:0.3, 12:0.012, 16:0.05` |
| 16 | `-0.342` | `7:0.3, 13:0.012, 15:0.03` |
| 17 | `-0.362` | `8:0.3, 14:0.012, 16:0.05` |

### P3 quantitative gates

| Matrix | Maximum mapped difference | Bound | MATLAB max row sum | Python max row sum | Minimum off-diagonal, both |
|---|---:|---:|---:|---:|---:|
| `G_a` | 0 | `1e-11` | 0 | 0 | 0 |
| `G_b` | 0 | `1e-11` | 0 | 0 | 0 |
| `G_z` | 0 | `1e-11` | 0 | 0 | 0 |
| `G` | 0 | `1e-11` | `5.551115123125783e-17` | `4.85722573273506e-17` | 0 |

All destinations, off-diagonal rates and diagonals agree exactly after mapping. Component recomposition `G-(G_a+G_b+G_z)` is zero up to `5.55111512312578e-17`, well below the generator bound. P3 failures: none.

## P4 complete KFE/stationary evidence

Both sides used their P3-accepted common backward generator. MATLAB solved the stationary object from `G'`. Python used `make_kfe_input` and `solve_stationary_kfe`; its forward-operator transpose error was exactly zero. MATLAB's recorded transpose identity error was also zero.

### Mapped stationary mass

| State | MATLAB mapped mass | Python mass | Absolute difference |
|---:|---:|---:|---:|
| 0 | 0.020982490054446235 | 0.020982490054446884 | `6.49e-16` |
| 1 | 0.057910036223009755 | 0.05791003622301111 | `1.35e-15` |
| 2 | 0.01741565991837216 | 0.01741565991837248 | `3.19e-16` |
| 3 | 0.054980353916310586 | 0.05498035391631077 | `1.80e-16` |
| 4 | 0.1544612384202828 | 0.154461238420283 | `1.94e-16` |
| 5 | 0.04770126480626376 | 0.04770126480626369 | `6.94e-17` |
| 6 | 0.015671079223094624 | 0.01567107922309423 | `3.94e-16` |
| 7 | 0.04506412272384537 | 0.045064122723843955 | `1.42e-15` |
| 8 | 0.014385183285803313 | 0.014385183285802548 | `7.65e-16` |
| 9 | 0.03161361834869862 | 0.031613618348699676 | `1.05e-15` |
| 10 | 0.08020103337219196 | 0.08020103337219378 | `1.82e-15` |
| 11 | 0.020448590654713075 | 0.020448590654713432 | `3.57e-16` |
| 12 | 0.08063785241058886 | 0.08063785241058911 | `2.50e-16` |
| 13 | 0.2077035592393955 | 0.20770355923939576 | `2.50e-16` |
| 14 | 0.05451573120715859 | 0.05451573120715849 | `9.71e-17` |
| 15 | 0.022144949925027625 | 0.022144949925027028 | `5.97e-16` |
| 16 | 0.05826800612073826 | 0.05826800612073632 | `1.9359513991901167e-15` |
| 17 | 0.01589523015005892 | 0.01589523015005775 | `1.17e-15` |

Maximum mapped difference: `1.9359513991901167e-15`, versus frozen bound `1e-10`: PASS.

### P4 diagnostic and aggregate gates

| Diagnostic | MATLAB | Python | Contract/result |
|---|---:|---:|---|
| forward transpose error | 0 | 0 | exact PASS |
| `||G^T g||_inf` | `1.1275702593849246e-16` | `1.1362438767648086e-16` | each `<=1e-10` |
| normalization error | `1.1102230246251565e-16` | 0 | each `<=1e-10` |
| minimum mass | `0.014385183285803313` | `0.014385183285802548` | above `-1e-12` |
| negative count | 0 | 0 | PASS |
| `A_hh` | `0.47216565807210165` | `0.47216565807210037` | difference `1.27675647831893e-15 <= 1e-10` |
| `B_hh` | `2.3571428571428403` | `2.3571428571428115` | difference `2.886579864025407e-14 <= 2.3571428571428404e-10` |

P4 failures: none.

## Files read and written

Read: live task/rules; accepted P1/P2/Owner reports; accepted P3/P4 production source and APIs; three designated MATLAB sources; all named predecessor evidence; all six frozen P3/P4 harnesses; and the generated P3/P4 JSON evidence.

Repository write: only this report. External writes were limited to byte-identical harness/input copies, Python static bytecode caches, and the exactly-once P3/P4 JSON outputs.

## Forbidden-operation check

- P1 or P2 rerun: no
- accepted predecessor output modified: no
- MATLAB production source/helper modified: no
- Python production source/test modified: no
- grid, drift, `Q_common`, formula, semantics, stationary equation, orientation or tolerance changed: no
- preflight numerically evaluated generator/mass/aggregate: no
- harness correction required or made: no
- any P3/P4 harness or comparison rerun: no
- P4 entered before P3 PASS: no
- P5 acceptance issued: no
- AR(1), transition, IRF, calibration extension or Results entered: no
- merge, rebase, reset or force-push: no

## Acceptance level and recommended next gate

P1, P2, P3 and P4 numerical evidence is complete and passing. Final scientific/Owner acceptance remains pending.

Recommended next gate after independent review:

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P5_OWNER_FINAL_ACCEPTANCE`

Only that gate may record final HA parity acceptance or decide whether dynamic extension can be unlocked.
