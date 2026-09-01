# MP4C annual-driver generalization and Chunk 01 execution report

Date: 2026-09-02

## Terminal

`MP4C_CHUNK01_2010_2011_PYTHON_ANNUAL_STATIONARY_COVERAGE_PASS`

Per-year markers:

- `MP4C_YEAR_2010_PYTHON_ANNUAL_STATIONARY_COVERAGE_PASS`
- `MP4C_YEAR_2011_PYTHON_ANNUAL_STATIONARY_COVERAGE_PASS`

This is Python annual stationary coverage only. It is not a MATLAB-Python parity claim; only corrected-2009 has formal cross-language parity authority.

## Authority and starting state

- Live task authority: `fa1cb01f449ca372bad645dd4b65e24911637249`.
- Required direct parent: `dde810ea4c62a1b59cbe335ba16a89701a4d2a02`; exact match.
- Fresh-fetch start: `HEAD == origin/main`, ahead/behind `0/0`, clean tracked worktree.
- The complete live task and every named controlling rule/report/source were read before implementation or science.
- Corrected-2009 remained the accepted anchor and was not run.

Frozen identities passed before mutation/science:

- `one_turn.py` Git blob `e5d6835cdc9e6d182e1c84e11f4d51938be592e1`;
- `firm.py` Git blob `1f7d37247e2d712fc0477a9f562dce81d1b367ce`;
- accepted 2009 driver Git blob `b1710ae3c5d8d7baf96e85c932d777fa5f3b908c`;
- accepted household oracle SHA-256 `B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3`;
- formal marker `MP4B_CORRECTED_CALENDAR2009_MATLAB_PYTHON_STATIONARY_PARITY_FORMALLY_ACCEPTED`.

The same identities were reverified after 2010 and after 2011 without drift.

## Annual-driver generalization

New driver:

`validators/multi_province/mp4c_python_annual_empirical.py`

Final SHA-256: `DAE2D5CB9BDBE83F23D92045063746AAACB39CAAD626057280B1D5DF4F208D86`.

The accepted 2009 driver and production `annual.py` were not modified. The smaller task-authorized option was used: write `CanonicalAnnualInput.canonical_bytes()` directly to an explicit `calendar_<year>_primary_premodel_input.json` external path.

The MP4C driver reuses the accepted driver bootstrap, grid, parameters, initial-array construction, source-postloop household adapter and outer scientific modules. It preserves the current repaired `one_turn.py`, including same-turn household `Lt -> firm_source["Lt_prev"]`, migration destination labor as current firm `Lt_supply`, and same-turn `AtTax`. The only authorized execution differences are explicit decoupled annual binding and ceilings of 250 outer turns, 7,750 household calls and 14,400 seconds. No equation, calibration, grid, tolerance, controller action, update order or convergence definition changed.

The first direct-script canonical preflight stopped before creating a canonical or making any scientific call because the new script had not yet bootstrapped the repository paths before importing `validators`. The new driver was repaired to use the accepted direct-script repository bootstrap ordering. `py_compile` then passed and the focused zero-science suite passed `45 tests`. No scientific one-shot had been consumed, so this was pre-science implementation completion, not a rerun.

## Verified local primary inputs and canonical preflight

Only the ignored local snapshot was used:

`D:\ProjectTemp\ch5-pre-p5-controlled-household-exec-repo-20260829\data_local\matlab_primary_source_snapshot`

Source hashes:

- filled annual workbook: `C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929`;
- regression workbook: `A6F444FCCCB30CB93AA5DE084F1DD163C54E5F53C4287C2CD3E13A045EB64A68`;
- distance workbook: `26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566`.

The unfilled workbook and derived MAT cache were not used.

| Year | Workbook numeric row | Analysis / `data_MAT` index | Regression vintage | Canonical SHA-256 |
|---:|---:|---:|---:|---|
| 2009 compatibility only | 10 | 1 | 10 | `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48` |
| 2010 | 11 | 2 | 11 | `84F655078762036B9BF52951666092777A49D53FDC5AF7C52483115009C2AD0B` |
| 2011 | 12 | 3 | 12 | `C08F2BE9254F0B6A9D1052F92B29BBD22709ACC60BBF91FB4DCFF64338CC5669` |

The reconstructed 2009 bytes exactly matched the accepted canonical SHA. No 2009 stationary call occurred. All canonical bindings, 31-province order, regression sheets, source hashes, finiteness, source formulas and fixed-calendar-2020 Zt anchor passed.

## 2010 execution

Run root:

`D:\ProjectTemp\ch5-mp4c-python-annual-2010-20260901-001`

- process exit: normal;
- terminal: `SOURCE_CONVERGED`;
- outer turns: `184`;
- household calls: `5,704`;
- final household convergence: `31/31`;
- unique province rows: `31/31`;
- frozen final fields: complete finite `31x20`;
- ra upper/lower: `0/0`;
- wage upper/lower: `10/12`;
- wall clock: `8675.640999999945` seconds;
- terminal SHA-256: `28670266659062D98A8F52B7C3656E374260562307ACB295E9E7F0B2C892DBD0`.

National aggregates:

| Ct | At | Bt | Yt |
|---:|---:|---:|---:|
| 294.77144496474534 | 37.60520924171005 | 66.05253128062964 | 416193851.5107822 |

The 2010 call was consumed once; reruns were zero. Shared identities passed after termination before 2011 launch.

## 2011 execution

Run root:

`D:\ProjectTemp\ch5-mp4c-python-annual-2011-20260901-001`

- process exit: normal;
- terminal: `SOURCE_CONVERGED`;
- outer turns: `184`;
- household calls: `5,704`;
- final household convergence: `31/31`;
- unique province rows: `31/31`;
- frozen final fields: complete finite `31x20`;
- ra upper/lower: `0/0`;
- wage upper/lower: `14/9`;
- wall clock: `6741.4370000000345` seconds;
- terminal SHA-256: `7939F2B562EB3EBFE45B68E513B98AFEB9F9474E17D5BE1FFFFB21210E8AE313`.

National aggregates:

| Ct | At | Bt | Yt |
|---:|---:|---:|---:|
| 303.95634280647533 | 45.95775468642976 | 65.28178784131526 | 497988339.42093873 |

The 2011 call was consumed once; reruns were zero. No anomaly occurred.

## Evidence roots and ledger

Preparation root:

`D:\ProjectTemp\ch5-mp4c-chunk01-2010-2011-preparation-20260901-001`

It contains the three canonical-preparation receipts, common preflight, exact launcher commands, chunk summary and complete artifact inventory. `artifact_inventory.json` covers 759 artifacts across the preparation and two run roots, is 194,702 bytes, and has SHA-256 `3980B209880A1DF1F49FEAE8BE8F07992A9F157B1AF5FEEF46ED58168929C000`.

Per-year roots contain the canonical JSON, calendar/run manifests, exact launcher, scientific identities, every turn input/output, complete terminal/history/final state, 31x20 evidence, coverage summary and execution ledger.

| Operation | Calls |
|---|---:|
| Python 2010 annual stationary | 1 |
| Python 2011 annual stationary | 1 |
| reruns | 0 |
| Python 2009 stationary | 0 |
| MATLAB | 0 |
| comparator | 0 |
| other years | 0 |
| AR(1)/shock/dynamics/IRF | 0 |
| R5/Results | 0 |

No binary/local data is a repository mutation. Allowed repository changes are the new MP4C driver, one focused test file and this report only.

## Exactly one recommended next gate

`MP4C_CHUNK02_2012_2013_PYTHON_ANNUAL_STATIONARY_EXECUTION`
