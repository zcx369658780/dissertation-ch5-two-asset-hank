# Inactive lagged observed-GDP wedge Builder candidate

Status: CANDIDATE_PENDING_INDEPENDENT_ENGINEERING_REVIEW. Date: 2026-09-30.

Implemented a standalone standard-library helper with frozen record, provenance and annual-output dataclasses. Observation year is exactly target year minus one. Explicit immutable province axes use destination rows and origin columns. Default amplitude is 0.3. Per-capita conversion uses Fraction followed by a checked final float; normalized differences avoid summation overflow. Nonfinite/nonpositive inputs and rounded coefficient interval endpoints fail explicitly, without clipping. No existing solver, initializer, integration or scientific source is changed.

Metadata validation distinguishes synthetic fixtures from supplied verified current/constant-price observed metadata. Hypothetical observed-branch tests use invented numbers and a synthetic-fixture source label. No real panel, original spreadsheet, actual provincial matrix or real-source price verification was performed. Real GDP price provenance remains UNVERIFIED; this helper does not read/hash sources and does not independently establish the truth of caller metadata.

Verification: exactly one invocation of `python -B tests/test_ch5_lagged_observed_gdp_wedge.py`; exit 0, 12 unittest methods passed, including parameterized negative cases. No retries or further test invocations. Meaningful checks cover known asymmetric direction/value, units, axes, diagonals, scaling invariance, immutable snapshots, strict years/IDs/numerics, province coverage, provenance flags/base years, extreme representable raw scales, final overflow/underflow, coefficient endpoints and import surface. Helper imports only dataclasses, fractions, math and re. The test directly loads the exact helper and verifies no ch5_two_asset_hank package module was imported. Tests are engineering evidence, not scientific acceptance.

Parent HEAD: 75cee92b1ad9e5cb6fc069bca892213838ffdddc.
Parent HEAD:src: 00682b2e1a7ba23665f6e16f6acf48ad35874883.
All 13 pinned task/spec/preparation/prior-task/integration/AGENTS/protected manifest hashes matched at entry and after the focused test. Six protected report roots remain preserved. Work-owned documents and the Owner AGENTS change remain outside Builder ownership. Only the four task-allowed new files are delivered. No staging, commit or push.

Scientific calls are zero for this bounded command/import surface, including HANK, HJB/KFE, firms, capital allocation, outer turns, calibration, replay, annual simulation, steady-state, GE, welfare and Results. Preflight, execute and wrapper calls are zero. Both historic C9 attempts remain consumed with CALL_LEDGER_UNRESOLVED actual ledgers; Objective A is retained and C9/C10/retry/partial-resume/Results stay closed. Results eligibility is FALSE. No final formula adoption, integration, provenance acceptance or convergence claim follows. Stop for independent Work engineering review.

Candidate helper SHA-256: D09C8E28307407D3AD31292E1E10C25224177DED067ECCE9380C0C3AFF78E83C
Candidate test SHA-256: A185A201A3185FA9FE02049F275B89D0C1FBC1B51442485AB650D0857E108F81

## Required engineering repair, second focused invocation

Independent engineering review withheld acceptance and required two concrete repairs. The initial 12-method, exit-0 invocation remains historical evidence only; it did not establish candidate acceptance.

Repair 1: input_kind, population_basis and price_basis now require exact built-in str before any enum equality comparison. Added six rejection cases covering a mutable custom equality object and a str subclass for each field. Custom-object equality counters remain zero, confirming rejection precedes enum comparison.

Repair 2: after computing the unchanged formula, unequal per-capita values require strict coefficient direction below/above one. Rounded direction collapse raises ValueError; no nextafter, clipping, formula or amplitude change. Added the specified GDP 1.0 versus 1.0000000000000002, population 1 fixture in both axis orders; default amplitude 0.3 explicitly rejects collapse.

After both concrete repairs, invocation 2 of `python -B tests/test_ch5_lagged_observed_gdp_wedge.py` exited 0: 14 unittest methods passed in 0.004 seconds. No third invocation. Two total focused calls consumed; at most one further call remains only after a concrete authorized candidate fix. All 13 fixed file hashes and parent identities matched before repair and all 13 fixed file hashes matched after invocation 2. Scientific imports/calls and actual panel reads remain zero. Existing Work/Owner files and protected paths remain unchanged. The earlier candidate hashes above describe invocation 1; current repair hashes are in the appended section below and updated receipt. Stop for the same independent Reviewer; no self-acceptance, integration, C9 continuation, commit or push.
Repair candidate src/ch5_two_asset_hank/corrected_diagnostic/lagged_observed_gdp_wedge.py SHA-256: 4EFECAB1B554748F4119D245005D3106B195174124E9057DEA28E4A34E7D864A

Repair candidate tests/test_ch5_lagged_observed_gdp_wedge.py SHA-256: 0687F3E8B53CB133CBD9BD86A301BE2BBA9A329A3E86EAC8AD33EA67B834C0BC
