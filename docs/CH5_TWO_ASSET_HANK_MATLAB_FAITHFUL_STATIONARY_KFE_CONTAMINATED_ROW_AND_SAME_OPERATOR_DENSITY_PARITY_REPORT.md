# MATLAB-faithful stationary KFE contaminated-row and same-operator density parity report

## Terminal classification

`MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY_BLOCKED`

The one MATLAB and one Python KFE solve both persisted finite objects from the same accepted MATLAB post-convergence operator. The single comparator call then failed at JSON persistence because a NumPy boolean scalar was not serializable. No comparison JSON was generated. The comparator was not repaired or rerun, so KFE parity is not accepted.

## Authority and frozen input

- Live start/final pre-publication `origin/main`: `2052fe8b9be69b6342c1264756fd59707fe1d6de`.
- Accepted HJB authorities remained unchanged: `MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_ACCEPTED` and `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HJB_OPERATOR_PARITY_ACCEPTED`.
- Accepted MATLAB/Python HJB objects matched `7351351B5D0F7012F03CB6A8CB79A6E31D8FC65FF5D7C26B4A241047F1B5DE94` and `A33EEA2F7A1698624EC4F773FFE42C2BF88B255F9C231960E8C182ECA2C870AB`.
- No HJB was rerun.
- The single common KFE input was MATLAB `A_post`, never iteration `A`.
- Frozen common operator NPZ/MAT hashes: `7A2ADC63...2C0F` / `2D4B8795...C3C8`.
- Grid/order manifest: `A851FF804E080F3EE302185E4CACE4D6EA61F595EBFCDCCE7D1115E3FA37B235`; shape `(5,5,2)`, Fortran `(b,a,z)`, `db=0.25`, `da=0.5`, cell weight `0.125`.
- Freeze marker: `MATLAB_FAITHFUL_KFE_SAME_POST_CONVERGENCE_OPERATOR_INPUT_FROZEN`.
- Artifact root: `D:\ProjectTemp\ch5-kfe-same-operator-20260830-001`.

## Source audit and implementation evidence

The source-extracted block uses `A_post'`, MATLAB `iFix=floor(0.37*50)=18` (Python row 17), RHS `0.007` at that row, exact unit-row replacement, full direct solve, and `sum(raw_g)*db*da` density normalization. No `dz`, z probability, trapezoid weight, recurrent-class restriction, eigensolve, or nullspace solve was introduced.

Candidate hashes preserved externally before restoration:

- faithful KFE source: `27DA91779788E76C9F92697247FFF520D460CB9CCAFAC2DE39CDCFF7440A3E88`;
- test: `578DC75064C52A312EE1220A0FEADAB450B13BA855A436924A04D7FC6163E728`;
- MATLAB evaluator: `C24FC39D...F644`;
- Python runner: `7C0A0B3D...4E3A`;
- comparator: `516E6B4D...5F2`;
- pre-execution freeze manifest: final frozen artifact identity recorded externally.

Engineering tests passed `3 passed in 0.72s`, covering row mapping, exact contaminated row, unchanged other transpose rows, RHS, independent synthetic direct solve, `db*da` normalization, Fortran reshape, and clean KFE/HJB imports. No HJB ran in tests.

## Scientific execution and persisted diagnostics

| Object | Calls/budget | Output SHA-256 |
|---|---:|---|
| MATLAB HJB | `0/0` | reused accepted output only |
| Python HJB | `0/0` | reused accepted output only |
| MATLAB KFE | `1/1` | `A53B304C134A909D99F1911983F8CB273AC295AEFF1A7DBBC9CFE621401F44E8` |
| Python KFE | `1/1` | `DF97F38C48CB46B5BC871DCB036B0AD3336DB17BC897A4921B8DEEA148AA98A7` |
| comparator | `1/1` | failed before persistence |

Read-only persisted diagnostics:

- row mapping: MATLAB 18 / Python 17;
- normalization factors: MATLAB `0.019701654849757503`, Python `0.019701654849757506`;
- raw contaminated residual infinity norms: MATLAB `8.673617379884035e-19`, Python `2.168404344971009e-18`;
- raw normalized-density maximum difference: `4.440892098500626e-16`;
- normalization errors: MATLAB `0`, Python `2.220446049250313e-16`;
- negative-count clean diagnostic: MATLAB `0`, Python `5` (diagnostic-only under the task; values were not used as veto evidence).

These diagnostics are not a persisted comparator acceptance result.

## Blocker, mismatch status, and closeout

- Exact comparator failure: `TypeError: Object of type bool is not JSON serializable` at final `json.dumps(result, ...)`.
- `comparison.json`: absent.
- Complete scientifically established material mismatch list: empty; no valid comparator artifact exists to establish PASS or MATERIAL MISMATCH.
- Complete unresolved list: comparator persistence and parity classification not reached as durable evidence.
- Complete source/environment failure list: one comparator NumPy-boolean serialization failure.
- Final ledger SHA-256: `C623AAD0E807F790B3F86A9631C128887DC49C1EB417DFEDAEA1F0C5ACA09F8D`, recording `0/0/1/1/1`.

The unaccepted faithful KFE source and test were restored out of repository paths after their hashes and full external artifacts were preserved. Repository mutation is this report only. KFE parity and the end-to-end stationary aggregate gate are not authorized. A new exact live task is required for serialization-only comparator correction and replacement comparison; no KFE or HJB rerun should be needed unless separately authorized.
