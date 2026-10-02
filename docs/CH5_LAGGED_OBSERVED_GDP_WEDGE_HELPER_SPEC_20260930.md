# One-year lagged observed-GDP labor wedge: inactive helper candidate

Date: 2026-09-30 (Asia/Shanghai)
Status: `OWNER_REQUESTED_PROGRAM_PREPARATION__INACTIVE_ENGINEERING_CANDIDATE__NO_SCIENCE`

## Authority and scope

The Owner approved proceeding with the program portion in the current Chapter 5 Work conversation on 2026-09-30. This specification implements the already discussed one-calendar-year lagged formula as a standalone candidate, with synthetic unit tests only. It does not adopt a final dissertation law, authorize integration or scientific execution, reopen C9, or resolve the actual old call ledgers. Convergence is a numerical requirement for an economically specified candidate; it is not sufficient economic validation or authority to tune formulas, tolerances, grids, or parameters until a PASS occurs.

Parent HEAD: `75cee92b1ad9e5cb6fc069bca892213838ffdddc`.
Parent `HEAD:src`: `00682b2e1a7ba23665f6e16f6acf48ad35874883`.
Only worktree: `D:\ProjectTemp\c5k1bturn56`.
Designated Builder: `核对第五章交接状态`, `01a0ef77-7753-7552-acc0-5ca3cbeac23c`, local app project `local-0758adfaed355d5be608096cdf92a3a2` (membership read back through the app API on 2026-09-30).

Historical Objective A, consumed C9 attempts, `CALL_LEDGER_UNRESOLVED`, and Results eligibility `FALSE` remain separate and unchanged. The existing solver, wrapper, live execution contracts, calibration, and six protected reports roots are outside the write scope. Preserve the Owner's uncommitted `AGENTS.md` model-selection change byte for byte.

## Exact candidate files

- `src/ch5_two_asset_hank/corrected_diagnostic/lagged_observed_gdp_wedge.py`
- `tests/test_ch5_lagged_observed_gdp_wedge.py`
- `EVIDENCE/ch5_lagged_observed_gdp_wedge_helper_20260930/builder_report.md`
- `EVIDENCE/ch5_lagged_observed_gdp_wedge_helper_20260930/builder_receipt.json`

Work owns this specification, `TASK_CURRENT.md`, the preserved prior task, preparation receipt, and the later independent review. The Builder must not change these Work-owned documents.

## Economic candidate and timing

For target calendar year `t`, observation year is exactly `t - 1`; there is no multi-year averaging option in this increment. For origin province `i` and destination province `j`:

`q[i] = 10000 * GDP_raw_100m_yuan[i,t-1] / population_raw_10k_persons[i,t-1]`

`phi[j,i] = 1 + amplitude * (q[i] - q[j]) / (q[i] + q[j])`

The default amplitude is `0.3`; a supplied amplitude must be finite and strictly between zero and one. This is a configurable pure-helper argument, not calibration or an authorized parameter sweep. Each test's amplitude is specified by its fixture.

Rows are destinations and columns are origins. A richer destination has a coefficient below one. Diagonals are exactly one. For finite positive `q`, require computed coefficients strictly inside `(1-amplitude, 1+amplitude)`; if floating-point rounding reaches an endpoint, fail explicitly rather than clipping or weakening the interval. Avoid overflow in the normalized difference, for example through a ratio of the smaller to the larger positive `q`. Calculate per-capita GDP without avoidable intermediate overflow/underflow: `GDP=population=1e305` must yield `10000`, and `GDP=population=1e-300` must also yield `10000`. A standard-library rational calculation using `fractions.Fraction` on the finite normalized float inputs, followed by one final float conversion, is acceptable. Reject a final per-capita value that cannot be represented as a finite positive float. An intermediate failure when the final result is representable is a defect, not an accepted stop.

No model `Yt`, `Lt`, wage, return, endogenous feedback, solver iteration, or warm-start state is an input. The returned annual matrix and its province/year metadata must be immutable snapshots. Changing a caller's record list or province-order list afterwards must not change the matrix. The future caller builds once for a target year and passes that fixed object throughout its outer iterations; that integration is not implemented or validated here. Lagged observed population is only the denominator for `q`; it does not replace target-year model population or divide it by three.

## Input and output contract

Use the standard library only, with frozen dataclasses (or an equally explicit immutable structure) for input records, provenance binding, and the annual output. Expose the builder `build_annual_labor_wedge(records, target_year, *, province_order, binding, amplitude=0.3)`.

Each record has a positive integer province index, integer observation year, raw GDP in 100-million yuan, and raw population in 10,000 persons. Integers for province indices and years must be built-in `int` excluding `bool`; valid target years are `2..9999`, observation and constant-price base years are `1..9999`. The explicit province order is nonempty, consists of unique positive integer indices, and determines both output axes. Require exactly one record for every declared province, no extras, and no wrong-year records. Reject booleans as numeric values or integer identifiers; reject missing, nonnumeric, non-finite, and nonpositive GDP/population. Convert caller containers into immutable tuples. Tests may use small province sets; eventual production binding requires the separately accepted exact 31-province order.

The provenance binding records input kind (`synthetic` or `observed`), a nonempty source-identifier string, a syntactically valid 64-hex SHA-256 string, population basis, GDP price basis, verification flag, and a price base year where applicable. Both kinds require a strict built-in `bool` verification flag, `population_basis='year_end_resident'`, and a valid source identifier/hash. For `input_kind='synthetic'`, require `price_basis='synthetic_fixture'`, verification flag `False`, and base year `None`; do not pretend the fixture establishes observed price provenance. For `input_kind='observed'`, the verification flag must be exactly `True` and GDP basis either `current_price` (base year must be `None`) or `constant_price` (base year must be a valid integer as above). Unknown/unverified observed price metadata must fail. Unit tests of the observed metadata branches use invented numerical records and a source identifier explicitly containing `synthetic-fixture`; that label is a test-fixture declaration separate from the hypothetical observed branch under test, and no actual observational source is read or accepted. The helper validates supplied metadata but does not hash or read files; a future reviewed loader must verify actual source bytes and attribution.

Output includes target year, observation year, province-order tuple, per-capita GDP tuple in yuan/person, immutable destination-by-origin coefficient tuple, amplitude, and the immutable provenance binding. No file I/O, cache, global mutable state, CLI, module execution side effects, solver imports, or dependencies beyond the standard library.

## Frozen synthetic verification

Use `unittest` and direct `importlib.util.spec_from_file_location` loading of this one file; register the module in `sys.modules` before execution if needed for dataclasses. Do not import the `ch5_two_asset_hank` package or any existing model module. Run only:

`python -B tests/test_ch5_lagged_observed_gdp_wedge.py`

No pytest/conftest collection, full suite, preflight, wrapper, `--execute`, HJB/KFE, firms, capital allocation, outer turns, model replay, or actual provincial matrix construction. Budget: science calls exactly zero; one initial focused unit-test invocation, followed by at most two invocations after concrete candidate fixes if necessary. Stop and report if a scientific import/entry occurs, a protected hash changes, source identity changes outside the new file, or the bounded test budget is exhausted.

Required meaningful cases: known asymmetric two-province fixture with explicit expected direction/value; exact unit conversion; shuffled input records with explicit axis order; every diagonal; positive/finite inputs and coefficient interval; common GDP-unit scaling invariance; immutability and input-container mutation; missing/extra/duplicate provinces, wrong year, invalid IDs/amplitudes/types, zero/negative/NaN/infinite values; unknown observed price basis rejected; hypothetical valid observed metadata accepted on invented numerical fixtures explicitly labelled as engineering validation; synthetic metadata allowlist and strict verification-flag type; constant-price base-year validation; representable per-capita values despite extreme raw scale; and explicit rejection on final per-capita overflow/underflow or floating-point coefficient interval endpoints. No actual GDP panel is read by the tests.

## Delivery and review

Record commands, exits, test counts, exact candidate SHA-256 values, parent identities, changed paths, unchanged integration-file SHA-256, `AGENTS.md` SHA-256, and all seven protected manifest/readback identities in the Builder receipt. Their exact path/hash allowlist is in the Work-owned `EVIDENCE/ch5_lagged_observed_gdp_wedge_helper_20260930/preparation_receipt.json`; read and verify only those exact paths rather than discovering historical evidence. The integration file is exactly `src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py`. Report all scientific counters as zero based on the command/import surface; do not assert recovered old actual counters. Produce the candidate without commit/push, then stop for independent engineering review. The Owner's earlier configuration-only uncommitted edit must never be staged or reverted.

Engineering review of this helper is not scientific route acceptance. A later source integration task, data-price/provenance acceptance, safe output design under Objective A, finite named scientific budget, and independent scientific review are all separate. Do not resume C9 or present helper tests as convergence, steady-state, GE, calibration, or Results evidence.
