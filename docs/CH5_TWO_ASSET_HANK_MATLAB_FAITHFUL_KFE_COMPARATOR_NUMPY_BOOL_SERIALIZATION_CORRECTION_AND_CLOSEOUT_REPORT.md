# MATLAB-faithful KFE comparator NumPy-bool serialization correction and closeout report

## Terminal and acceptance

`MATLAB_FAITHFUL_KFE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_PASS`

Freeze:

- `MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_KFE_DENSITY_PARITY_ACCEPTED`

The single replacement comparator persisted PASS against the already frozen MATLAB/Python KFE outputs. No HJB or KFE solver was rerun.

## Authority and frozen objects

- Live start/final pre-publication `origin/main`: `aca49787243d1f944b86b59e88e6b3a582f6b40f`.
- Accepted HJB authorities remained unchanged.
- MATLAB/Python KFE outputs: `A53B304C134A909D99F1911983F8CB273AC295AEFF1A7DBBC9CFE621401F44E8` / `DF97F38C48CB46B5BC871DCB036B0AD3336DB17BC897A4921B8DEEA148AA98A7`.
- Common post-convergence A: `7A2ADC63CE7A4BB5184036E4CFC07EC082185C90C5B818C572ED05756D222C0F`.
- Grid manifest/contract: `A851FF80...B235` / `638597AA...2E56`.
- Shape `(5,5,2)`, Fortran `(b,a,z)`, `db=0.25`, `da=0.5`, cell weight `0.125`, MATLAB row 18 / Python row 17, RHS `0.007`.

## Serialization-only audit and correction

Classification: `KFE_COMPARATOR_NUMPY_SCALAR_JSON_SERIALIZATION_ONLY`.

The predecessor exception was `TypeError: Object of type bool is not JSON serializable` at final `json.dumps`. The first sorted payload path was `direct.cell_weight`, exact type `numpy.bool_`; `direct.db` and `direct.da` had the same type. All scientific comparisons, certificates, mismatch aggregation, and PASS/MATERIAL selection completed before persistence. No ndarray reached the payload.

The new comparator retained every scientific line and added only a JSON `default=` callback converting `np.generic` via `.item()`, otherwise raising `TypeError`. Changed lines are `KFE_COMPARATOR_JSON_SERIALIZATION_TYPE_NORMALIZATION_ONLY`.

- Predecessor comparator: `516E6B4D088143C1976A202B2B3CCAED6D131524BD10DA7315570C03DF44D5F2`.
- Corrected comparator: `92E2931C9CEDDF6FE99B3D8670CA317550181CA78224481361D948A0DABA4F1C`.
- Exact diff: `DBA9BA3C3DC40F348C4F0B36DA2335971E107CCDE5C4B708944FA0B0E22C8A24`.
- Audit: `31B2E86661B0C84B8F74BAAEDD4590F463435ACF4F8A4B2102AE3E4EF2C5040D`.
- Exactly one no-science serializer preflight: `KFE_COMPARATOR_SERIALIZER_PREFLIGHT_PASS`; native scalars and NumPy scalar values were preserved, ndarray remained fail-closed, payload fields/order/result logic were unchanged.

## Replacement comparison

- Calls in this successor: MATLAB HJB `0`, Python HJB `0`, MATLAB KFE `0`, Python KFE `0`, replacement comparator `1/1`.
- Persisted comparison SHA-256: `B7639171F531000EFB6ACFBD70FA801F248EC6E463D54D92C0D9E82E175A8950`.
- Direct PASS: common A, transpose, contaminated matrix, row index, RHS, shape, `db`, `da`, and cell weight.
- Raw NNZ: A `179/179`, transpose `179/179`, contaminated matrix `176/176`; mathematical support and values passed.
- MATLAB/Python raw residuals: `8.673617379884035e-19` / `2.168404344971009e-18`.
- Both backward-error bounds: `5.684341886080802e-14`; both certificates PASS.
- Normalization errors: `0` / `2.220446049250313e-16`; same-input normalization replay PASS.
- Raw-g maximum difference: `2.0816681711721685e-17`.
- Density maximum difference: `4.440892098500626e-16`, classified `KFE_DIRECT_SOLVER_PROPAGATED_DIAGNOSTIC_DIFFERENCE`.
- Minimum density: MATLAB `0`, Python `-6.878877566082026e-18`; negative counts `0/5`. This remains explicitly diagnostic-only and non-vetoing under the frozen faithful contract.
- Material mismatch list: empty. Unresolved scientific residual list: empty. Source/environment failure list: empty.

## Published implementation and boundary

Faithful KFE source/test were restored byte-identically:

- `matlab_faithful_kfe.py`: `27DA91779788E76C9F92697247FFF520D460CB9CCAFAC2DE39CDCFF7440A3E88`;
- `test_matlab_faithful_kfe.py`: `578DC75064C52A312EE1220A0FEADAB450B13BA855A436924A04D7FC6163E728`.

No accepted HJB source, clean KFE, steady-state, or comparator production path changed. No aggregates, equilibrium loops, D1-D3, tail, transition, IRF, dynamics, calibration, or Results ran.

The only recommended next gate is: **MATLAB-faithful end-to-end stationary distribution and household aggregate parity using each language's own accepted post-convergence operator, including the requested C^ss, L^ss, A^ss, B^ss comparison table.** This report does not itself authorize that execution.
