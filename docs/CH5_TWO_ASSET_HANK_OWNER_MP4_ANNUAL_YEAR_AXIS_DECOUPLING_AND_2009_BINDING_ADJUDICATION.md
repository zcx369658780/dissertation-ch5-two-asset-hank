# CH5 Two-Asset HANK Owner/L3 Annual Year-Axis Decoupling and 2009 Binding Adjudication

Date: 2026-08-30
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
Owner: final scientific authority
L3 role: independent reviewer / scientific route authority

## Decision status

`OWNER_MP4_ANNUAL_YEAR_AXIS_DECOUPLING_AND_2009_BINDING_ADJUDICATION_ACCEPTED`

This adjudication resolves the `YEAR_MAPPING_SOURCE_CONFLICT_BLOCKED` terminal reported by MP4A without modifying the protected MATLAB source or pretending the current annual wrapper is internally consistent.

## 1. Confirmed source conflict

Freeze:

- `MATLAB_LEGACY_ANNUAL_YEAR_INDEX_COUPLING_DEFECT_CONFIRMED`
- `MATLAB_OUTPUT_YEAR_LABEL_IS_NOT_ECONOMIC_DATA_YEAR_AUTHORITY`

The current MATLAB annual wrapper overloads one scalar `ii` with three distinct roles:

1. analysis/output-year position, through `ii+2008`;
2. calibration-vintage cell, through `data_MAT{ii}`;
3. workbook economic-data row, through downstream `data_year=ii`.

With a workbook whose explicit calendar axis is 2000-2023, these roles cannot all identify calendar 2009 simultaneously. The conflict is in the current annual routing/index coupling, not in the already accepted two-asset household, MP2 one-turn arithmetic, or MP3 controller semantics.

Historical artifacts merely labelled `2009` are therefore not accepted as calendar-2009 model evidence unless their runtime provenance independently proves the corrected/decoupled data binding.

## 2. Dissertation evidence and intended economic calendar

Freeze:

- `OWNER_ECONOMIC_CALENDAR_YEAR_IS_WORKBOOK_CALENDAR_YEAR`
- `OWNER_2009_ANCHOR_USES_EXPLICIT_WORKBOOK_2009_ROW`

The dissertation defines the provincial panel as calendar-year data and explicitly presents multi-province stationary output for **2009, 2014, and 2020** against the corresponding actual data in Table 5-2. It later reports annual spillover/spatial results for **2009-2023**. Therefore the economic meaning of the first anchor year is actual calendar 2009, not the current wrapper's `ii=1` downstream workbook row 2000.

For the 2009 anchor, the primary annual economic data must use:

- workbook calendar year: `2009`;
- physical Excel row: `11` when row 1 is the header;
- zero-based data index: `9`;
- one-based MATLAB numeric data-row index: `10`.

## 3. Decoupled annual index contract

Freeze the following distinct identities for annual year `y` in 2009-2023:

- `calendar_year = y`;
- `analysis_index = y - 2008` (1..15);
- `workbook_data_row_index = y - 1999` (10..24, MATLAB one-based numeric row);
- `data_MAT_index = analysis_index`;
- `output_filename_year = calendar_year`;
- `regression_vintage_key = analysis_index + 9` under the current `reg_method=0` source convention.

For calendar 2009 specifically:

- `calendar_year = 2009`;
- `analysis_index = 1`;
- `workbook_data_row_index = 10`;
- `data_MAT_index = 1`;
- `output_filename_year = 2009`;
- source regression sheet suffix/key remains `10`.

The regression suffix/key is a source-defined calibration-vintage identifier. It must not be silently relabelled as a calendar year unless separate source evidence proves that interpretation.

This decoupling is the controlling annual binding for the Python reconstruction and for any diagnostic MATLAB wrapper used in same-input parity.

## 4. `IND_Zt` fixed-2020 source role

Freeze:

- `MATLAB_FIXED_2020_IND_ZT_RETAINED_AS_SOURCE_NUMERICAL_INITIALIZATION_ANCHOR`
- `FIXED_2020_IND_ZT_IS_NOT_ANNUAL_CALENDAR_IDENTITY`

The current `load_GDPdata.m` computes `IND_Zt` from the workbook's calendar-2020 row for every calibration-vintage cell. The dissertation describes estimated TFP as an **initial value** and the adaptive steady-state algorithm subsequently resets province `Zt` when output differs from the target data.

For the first faithful 2009 comparison, preserve the source's fixed-2020 `IND_Zt` construction as a numerical initialization convention. Do not reinterpret it as saying the annual model is a 2020 model, and do not redesign it in the annual-binding gate.

If later evidence shows that this initialization materially contradicts the intended dissertation calibration or prevents same-input parity, classify and adjudicate it separately. It is not part of the year-axis correction itself.

## 5. MAT cache role remains unchanged

Retain:

- `OWNER_DERIVED_MAT_CALIBRATION_CACHE_NOT_PRIMARY_SCIENTIFIC_AUTHORITY`
- `OWNER_PRIMARY_CALIBRATION_AUTHORITY_SOURCE_WORKBOOKS_REGRESSION_INPUTS_AND_LOAD_GDPDATA_TRANSFORMATION`

The MAT cache may be used only as a compatibility check. It must not decide calendar-year mapping or override primary-source reconstruction.

## 6. MATLAB-Python parity route after adjudication

The next route is:

1. **MP4A2** — zero-model annual-binding repair/preparation:
   - implement the decoupled annual index contract in Python input preparation;
   - create the canonical source-derived 2009 pre-model input identity;
   - prepare a non-destructive diagnostic MATLAB entry/wrapper that passes `data_MAT{1}` together with workbook `data_year=10` and labels output as 2009, without modifying protected MATLAB source;
   - prove both languages receive the same economic input identity before any solver runs.
2. **MP4B** — one controlled calendar-2009 stationary comparison:
   - one prepared MATLAB 2009 route;
   - one Python 2009 route;
   - persisted intermediate localization;
   - bounded mismatch diagnosis.
3. Only after stationary acceptance: source-named 2009 shock/response comparison.
4. Only after first-year stationary/response validation: consider the 2009-2023 batch route.

## 7. Historical-literal route

The current literal call `ii=1` may be retained as forensic evidence and may be described only as:

`LEGACY_SOURCE_LITERAL_2009_LABEL_WITH_2000_ECONOMIC_ROW`

It is not the scientific 2009 anchor and is not required to be run merely to establish the corrected 2009 route. If a future provenance question requires reproducing historical labelled outputs, that must be a separately bounded diagnostic task.

## 8. Mismatch diagnosis

Retain Owner authority:

`OWNER_PARITY_MISMATCH_BOUNDED_ROOT_CAUSE_DIAGNOSIS_AUTHORIZED`

A mismatch may be localized and classified, but no automatic formula repair, tolerance loosening, protected-source mutation, or unbounded rerun loop follows from this adjudication.

## 9. Boundary

This file does not authorize:

- MATLAB model execution;
- Python annual model execution;
- HJB/KFE/household/fixed-point execution;
- 2010-2023 batch execution;
- shock/IRF execution;
- genuine dynamic transition;
- Results claims.
