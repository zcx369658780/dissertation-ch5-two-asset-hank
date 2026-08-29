# CH5 Two-Asset HANK Pre-P5 Python Boolean Serialization Correction and C/L r_a Completion

## Supplementary classification

`PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_ROBUSTNESS_COMPLETE_NEEDS_OWNER_DISCUSSION`

The external Python boolean/NumPy-scalar serialization defect was corrected without changing `run_one` scientific logic. The mandatory synthetic serialization preflight passed exactly once. The replacement Python baseline at `r_a=0.040` was executed exactly once, immediately persisted and read back before the replacement perturbation at `r_a=0.041` was executed exactly once and likewise persisted. All accepted Python scientific validity diagnostics passed.

The reused MATLAB and new Python responses agree that `L_hh` decreases, but disagree on the sign of the small `C_hh` response: MATLAB decreases by `0.0554334%`, while Python increases by `0.00943931%`. Because the native MATLAB and Python objects differ and the sign discrepancy is not resolved by this bounded task, the completed supplementary evidence requires Owner discussion. This is not P5 acceptance.

## Live authority and source continuity

- repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- fresh-fetched task/base `origin/main`: `1821f1991c90a197d6a3e728a3e763239e8e3836`
- task: `CH5_TWO_ASSET_HANK_PRE_P5_PYTHON_BOOLEAN_SERIALIZATION_CORRECTION_AND_CL_RA_COMPLETION`
- predecessor report commit: `b6d3bc4e3f12449c206c19d240a7317a5e841b89`
- accepted Python scientific baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`
- accepted P1-P4 evidence: `daa3e60ff97828ec80fb2e83bee863eb4aa632a4`
- isolated repository workspace: `D:\ProjectTemp\ch5-pre-p5-controlled-household-exec-repo-20260829`
- new external artifact root: `D:\ProjectTemp\ch5-pre-p5-python-boolean-completion-artifacts-20260829`
- `git diff 7a2388a2ba89073e307f05a909570e8c40a4be13..1821f1991c90a197d6a3e728a3e763239e8e3836 -- src tests`: empty

Python `src/tests` therefore remain unchanged from the accepted R4 scientific baseline. No production source or test was modified. P1-P4 were not rerun.

## Reused MATLAB evidence identity and read-back

MATLAB was not executed. The exact predecessor artifacts were read from `D:\ProjectTemp\ch5-pre-p5-controlled-household-persistence-reexec-artifacts-20260829`.

| Artifact | Bytes | SHA-256 | Result |
|---|---:|---|---|
| `matlab_out_0040.mat` | 19306 | `E723D267ABEFC16A20B4D17D6EC20554561B601FB028405FDA41D30EFAC03D00` | PASS |
| `matlab_out_0041.mat` | 19660 | `83B877820FEA59A655C98A4669189EEA0D3A17E4CDC1D9B334EBAF6115ED58BC` | PASS |
| `matlab_pair_output.json` | 1159 | `0083726D2D3911566DE71C6A97C6DF6FD58739019B8530661809EEBA189C1FEF` | PASS |

JSON read-back reproduced the accepted values. Both reused MATLAB rows have `convergent=1`, exact `Ct == sum(C,'all')`, exact `Lt == sum(l,'all')`, `sum(g,'all')=1`, finite aggregates, and only machine-scale signed probability roundoff.

## Predecessor Python identities and defect

| Artifact | Bytes | SHA-256 | Result |
|---|---:|---|---|
| predecessor `run_python_pair.py` | 6763 | `018C1E0A154F32E7D62C9BF7B19F20B3EACE30126D4DF687E40EDC76A2DCBA46` | PASS |
| predecessor `python_input_manifests.json` | 3255 | `32252AD3899FFE65EC96D31D6A74637A95597502FDCB6BA629C8D0CD2B3F8DA8` | PASS |

The predecessor control flow completed both `run_one` calls before final `json.dumps` raised `TypeError: Object of type bool is not JSON serializable`. The defect was confined to external serialization because `numpy.bool_` is not handled by the standard JSON encoder.

## Complete predecessor-to-corrected harness diff

```diff
--- run_python_pair_predecessor.py
+++ run_python_pair.py
@@
 import json
+import hashlib
 import sys
@@
-ARTIFACT = Path(r"D:\ProjectTemp\ch5-pre-p5-controlled-household-persistence-reexec-artifacts-20260829")
+ARTIFACT = Path(r"D:\ProjectTemp\ch5-pre-p5-python-boolean-completion-artifacts-20260829")
@@
+def json_native(value):
+    if isinstance(value, np.generic):
+        return value.item()
+    if isinstance(value, dict):
+        return {key: json_native(item) for key, item in value.items()}
+    if isinstance(value, (list, tuple)):
+        return [json_native(item) for item in value]
+    return value
+
+
+def persist_json(path: Path, payload) -> dict[str, object]:
+    native = json_native(payload)
+    encoded = json.dumps(native, indent=2, sort_keys=True, allow_nan=False)
+    path.write_text(encoded, encoding="utf-8")
+    raw = path.read_bytes()
+    if json.loads(raw.decode("utf-8")) != native:
+        raise RuntimeError(f"JSON read-back mismatch: {path}")
+    return {"path": path.name, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest().upper()}
+
+
 def main() -> None:
@@
-    rows = [run_one(0.040)]
-    rows.append(run_one(0.041))
-    output = {"execution_count_baseline": 1, "execution_count_perturbation": 1, "rows": rows}
-    (ARTIFACT / "python_pair_output.json").write_text(
-        json.dumps(output, indent=2, sort_keys=True, allow_nan=False), encoding="utf-8")
+    baseline = run_one(0.040)
+    baseline_artifact = persist_json(ARTIFACT / "python_out_0040.json", baseline)
+    perturbation = run_one(0.041)
+    perturbation_artifact = persist_json(ARTIFACT / "python_out_0041.json", perturbation)
+    output = {
+        "execution_count_baseline": 1,
+        "execution_count_perturbation": 1,
+        "per_rate_artifacts": [baseline_artifact, perturbation_artifact],
+        "rows": [baseline, perturbation],
+    }
+    persist_json(ARTIFACT / "python_pair_output.json", output)
```

The extracted `run_one` text region was byte-for-byte identical before and after correction: 3191 bytes. No scientific import, calculation, formula, input, grid, initialization, tolerance, solver call, diagnostic definition, or run ordering changed. The diff is confined to NumPy scalar conversion, JSON persistence/read-back/hash plumbing, per-rate immediate persistence, and artifact path.

## Mandatory pure-serialization preflight

Exactly one preflight was run before scientific execution. It contained native `bool`, `numpy.bool_`, `numpy.float64`, `numpy.int64`, nested lists/dictionaries, and every expected real `run_one` output field. It did not call HJB, KFE, generator, policy, fixture, or any model function.

The preflight proved:

- native and NumPy booleans preserved exact truth values;
- NumPy floating/integer values preserved their numeric values after `.item()` conversion;
- both synthetic summary rows retained the complete expected field set;
- `json.dumps(..., allow_nan=False)` succeeded;
- file write and JSON read-back succeeded.

Result: PASS.

| Preflight artifact | Bytes | SHA-256 |
|---|---:|---|
| `serialization_preflight.py` | 3281 | `AD70F4F84399898234E98B772D5360762D96319718BEF38EBE0C6D1BAAE3FFEC` |
| `serialization_preflight.json` | 2503 | `50EF18449435E8FAF8EFD5A454BF209DE672935DAA2BC1DD78D54709E8072BC6` |

After preflight, the corrected `run_python_pair.py` was frozen read-only at 7751 bytes, SHA-256 `C1388AEAE97821A163BA6EAF8ED53C308C391E0E3ABD976ACA9786DE69A92F04`. Its post-execution identity was unchanged.

## Frozen inputs and exact execution counts

The copied input manifest retained SHA-256 `32252AD3899FFE65EC96D31D6A74637A95597502FDCB6BA629C8D0CD2B3F8DA8`. Its baseline and perturbation objects differ only at `r_a: 0.040 -> 0.041`. The accepted R4 grids, productivity process, parameters, initial value, buffer protocol, HJB/KKT/generator/KFE tolerances, aggregation definitions, and all other inputs remained unchanged.

| Action | Count | Outcome |
|---|---:|---|
| MATLAB execution | 0 | reused exact persisted evidence |
| Python replacement baseline `r_a=0.040` | 1 | persisted and read back before perturbation |
| Python replacement perturbation `r_a=0.041` | 1 | persisted and read back |
| P1-P4 rerun | 0 | not performed |

| Python output | Bytes | SHA-256 |
|---|---:|---|
| `python_out_0040.json` | 2687 | `209AFBA4DDD19CC5ED213F89DE67B669D1C8A22D7730FC9519E00A8B9B23916C` |
| `python_out_0041.json` | 2109 | `B0A9866E70EB02CD606D24B270DF020B69B5091559590F0B3C9DC597D457B3CE` |
| `python_pair_output.json` | 6039 | `CC4761383E724C02F485BE95AB62A75835ACEAE577B5C05ABFF1B284F263F1BE` |

## Aggregate level comparison

| implementation | `r_a/rah` | `C_hh` | `L_hh` | `A_hh` | `B_hh` |
|---|---:|---:|---:|---:|---:|
| MATLAB | 0.040 | 9.093838085759417 | 0.7208465448372894 | 0.4205741387968296 | 2.162515255782729 |
| Python | 0.040 | 0.5570429699260410 | 0.9990139906201341 | 0.010765933312087405 | 0.015679440387058798 |
| MATLAB | 0.041 | 9.088797065167160 | 0.7201767277365387 | 0.5227979944275221 | 2.168714217374641 |
| Python | 0.041 | 0.5570955509235596 | 0.9988855345043183 | 0.014606300746026084 | 0.014966157166723877 |

Native levels are not required to match because the MATLAB snapshot and Python R4 object use different grids, productivity representations, and calibrations. Formal shared-input/adapter parity remains the accepted P1-P4 evidence.

## Within-language responses

| implementation | `Delta C_hh` | `%Delta C_hh` | `Delta L_hh` | `%Delta L_hh` |
|---|---:|---:|---:|---:|
| MATLAB | -0.00504102059225708 | -0.0554333664698860% | -0.000669817100750647 | -0.0929209005089758% |
| Python | 0.0000525809975185920 | 0.00943930726305966% | -0.000128456115815800 | -0.0128582899761055% |

Python supplementary asset responses are `Delta A_hh=0.00384036743393868` and `Delta B_hh=-0.000713283220334921`.

Response comparison:

- `Delta C_hh`: sign disagreement — MATLAB negative, Python positive;
- absolute Python percentage `C_hh` response is `0.170282049678284` times the MATLAB percentage magnitude;
- `Delta L_hh`: sign agreement — both negative;
- absolute Python percentage `L_hh` response is `0.138378878225179` times the MATLAB percentage magnitude.

Both consumption responses are quantitatively small, but their sign disagreement is not resolved by the known native-object differences within this bounded experiment. It therefore requires Owner discussion rather than automatic acceptance.

## Python scientific validity diagnostics

| Diagnostic | Python 0.040 | Python 0.041 | Result |
|---|---:|---:|---|
| primary converged / iterations | true / 34 | true / 35 | PASS |
| buffer converged / iterations | true / 34 | true / 35 | PASS |
| primary HJB residual | `8.365197423643167e-10` | `6.790542572687741e-10` | PASS |
| buffer HJB residual | `8.372715853965929e-10` | `6.796473384085289e-10` | PASS |
| primary KKT residual | `9.088497027490715e-15` | `8.889158330958007e-15` | PASS |
| buffer KKT residual | `9.423101212153411e-15` | `9.027425186000975e-15` | PASS |
| primary generator max row sum | `2.6645352591003757e-15` | `2.6645352591003757e-15` | PASS |
| buffer generator max row sum | `2.6645352591003757e-15` | `3.552713678800501e-15` | PASS |
| primary minimum off-diagonal | `4.284173835999994e-05` | `0.001196780817` | PASS |
| buffer minimum off-diagonal | `4.284173835999994e-05` | `0.00119678081696` | PASS |
| recurrent classes / size | 1 / 225 | 1 / 225 | PASS |
| recurrent `a` indices | `[0,1,2]` | `[0,1,2]` | PASS |
| left nullity | 1 | 1 | PASS |
| upward/downward `a` edges | 134 / 4 | 138 / 4 | PASS |
| KFE stationarity sup | `3.885780586188048e-16` | `4.996003610813204e-16` | PASS |
| normalization error | `4.440892098500626e-16` | `4.440892098500626e-16` | PASS |
| minimum mass | `1.411264453687144e-17` | `1.873085931268604e-17` | PASS |
| negative mass count | 0 | 0 | PASS |
| finite mass | true | true | PASS |
| mass-density error | `3.3306690738754696e-16` | `4.440892098500626e-16` | PASS |

All common-core normalized changes were below `3.78e-9`, far below the accepted `1e-3` bound. Raw policy mismatch counts were 2 and 1 respectively, but every reported mismatch canonicalized to the same accepted policy ID on primary and buffer grids, with Hamiltonian-gap bounds at machine scale. These are accepted near-tie aliases, not scientific failures.

## Forbidden-operation check

- MATLAB executed: no
- P1-P4 rerun: no
- MATLAB/Python production source or tests modified: no
- `run_one` scientific text changed: no; exact identity PASS
- scientific input changed outside frozen `r_a` pair: no
- grids, productivity, initialization, equations, FOCs, policy, boundary/KKT, generator/KFE, aggregates, or tolerances changed: no
- corrected harness edited after first scientific run began: no
- either replacement rate rerun: no
- tuning after observing outputs: no
- P5 acceptance issued: no
- AR(1), transition, IRF, calibration extension, dynamics, or Results entered: no
- merge, rebase, reset, or force-push: no

## Recommended next gate

P5 remains pending. The next gate should be an Owner discussion/reviewer assessment of whether the small cross-native-object `Delta C_hh` sign disagreement is economically material or acceptable given the different MATLAB snapshot and Python R4 calibration/representation. Only a separately published `CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P5_OWNER_FINAL_ACCEPTANCE` task may issue P5 acceptance.
