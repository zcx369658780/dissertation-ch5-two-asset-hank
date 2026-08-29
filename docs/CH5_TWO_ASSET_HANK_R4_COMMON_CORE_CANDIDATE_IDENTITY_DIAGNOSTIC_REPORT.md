# CH5 Two-Asset HANK R4 Common-Core Candidate-Identity Diagnostic

## Verdict

`PASS`

Primary scientific diagnosis:

`TRUNCATION_SENSITIVITY_NEAR_TIE_OR_IDENTIFIER_ONLY`

Acceptance meaning:

`R4_COMMON_CORE_CANDIDATE_IDENTITY_ROOT_CAUSE_DIAGNOSED__NO_REPAIR_AUTHORITY`

The four candidate-ID mismatches are deterministic selections between two candidates that are both constructed and admissible at the same lower-liquid-boundary state. Their Hamiltonian gaps are only `2.220446049250313e-16` to `1.5543122344752192e-15`. The selected consumption, labor, transfer, adjustment cost, and asset drifts differ only at machine scale. The differing `F` versus `Z` liquid-direction labels reflect alternative lower-boundary representations with different `lambda_b`, although both have `mu_b` within the frozen `1e-12` zero-drift tolerance and KKT residuals below `1e-14`.

No repair, tolerance change, fixture rerun, connectivity calculation, KFE calculation, or acceptance decision was performed.

## Authority and provenance

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- Live `origin/main` before execution: `c62d7e2ab248049a2558424aa0f1fb6297defb8d`
- Live task commit parent: `546b88be6316526682c5a02ef4671021d0f387c3`
- Consumed-run implementation/evidence baseline: `546b88be6316526682c5a02ef4671021d0f387c3`
- Diagnostic workspace: `D:\ProjectTemp\ch5-r4-common-core-diagnostic-20260829`
- Diagnostic branch/ref before report creation: `main`
- Pre-execution workspace status: clean

The following twelve live-main source blobs were compared with the consumed baseline and matched exactly:

| Source | Live/baseline Git blob |
|---|---|
| `src/ch5_two_asset_hank/steady_state.py` | `7b804645e5a08fa6c688a98052729c594c9f2519` |
| `src/ch5_two_asset_hank/hjb.py` | `8b3d67079f13dd5d905e8d472a134a3316b26579` |
| `src/ch5_two_asset_hank/policies.py` | `d739c6ae77d6c8ce42119e79bbd3817ab9365e0d` |
| `src/ch5_two_asset_hank/derivatives.py` | `5455706a308e000414209ac4f831c6c7327f8263` |
| `src/ch5_two_asset_hank/boundaries.py` | `1822089050614cc0fe059096832ab7a57e11cdfa` |
| `src/ch5_two_asset_hank/economics.py` | `fa29c7fcb9ed9ce52657affbb5a94c3b24662bed` |
| `src/ch5_two_asset_hank/contracts.py` | `4b373706e82f8d350e90ea3a1de8b51e4ec72275` |
| `src/ch5_two_asset_hank/generator.py` | `9e174df0bca9759c4167efef6b806c60ee451f3a` |
| `src/ch5_two_asset_hank/productivity.py` | `e7714c3440fa3536ab63b0721c83e2f5b32c6bcc` |
| `src/ch5_two_asset_hank/indexing.py` | `3aee864af5dce5128957896e5d7803c2a815aab6` |
| `src/ch5_two_asset_hank/kfe.py` | `1ace478651cf81255fedc80123779f7e33aaacdf` |
| `src/ch5_two_asset_hank/kfe_contract.py` | `f34490906b38144bcdd57b6b3a5be64ac78a4ad2` |

Source-drift gate: `12/12 PASS`.

## Files read and written

Read from live authority and baseline:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION_RERUN_AFTER_LATEST_SLACK_LOWER_B_08125.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_CONSUMED_RUN_IMPLEMENTATION_EVIDENCE_BASELINE_PUBLICATION.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_COMMON_CORE_CANDIDATE_IDENTITY_DIAGNOSTIC.md`
- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION_RERUN_AFTER_LATEST_SLACK_LOWER_B_08125_REPORT.md`
- the twelve source files in the blob table above

Written:

- `docs/CH5_TWO_ASSET_HANK_R4_COMMON_CORE_CANDIDATE_IDENTITY_DIAGNOSTIC_REPORT.md`

No other repository file was written or modified.

## Exact diagnostic execution

Ephemeral script outside the repository:

- path: `D:\ProjectTemp\ch5-r4-common-core-candidate-diagnostic-ephemeral.py`
- SHA-256: `4C5B52C4E63AFD4D79BBC923FBCEC28EC6106586E36C2B7072748968075F5028`
- bytes: `14803`

Execution environment and command:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
$env:PYTHONPATH='src'
python.exe D:\ProjectTemp\ch5-r4-common-core-candidate-diagnostic-ephemeral.py
```

The script called the existing internal `_solve(z)` path exactly as follows:

1. one 25-point HJB solve on `z=0.5:0.0625:2.0`;
2. one 29-point HJB solve on `z=0.5:0.0625:2.25`.

Execution counts:

- 25-point internal HJB solve: `1`
- 29-point internal HJB solve: `1`
- total HJB solves: `2`
- `run_frozen_r4_steady_state()` calls: `0`
- pytest calls: `0`
- KFE/connectivity/recurrent-class/aggregate calls: `0`

After the two solves, the script recomputed derivatives on the already-returned final values and called the existing pure `select_policy` calculation only to capture candidate lists immediately before its existing line-646 sort. The reconstructed final candidate-ID arrays exactly matched the HJB results. Production functions were not monkeypatched or modified.

HJB completion evidence:

| Grid | Shape | Iterations | Final change | HJB residual sup | KKT residual | Boundary violation |
|---|---:|---:|---:|---:|---:|---:|
| 25-point | `(3,3,25)` | 34 | `8.365242720742572e-09` | `8.365190762305019e-10` | `9.423101212153411e-15` | `8.215650382226158e-15` |
| 29-point | `(3,3,29)` | 34 | `8.372696314040695e-09` | `8.372716964188953e-10` | `9.035850477407446e-15` | `7.993605777301127e-15` |

Common-core normalized changes were:

- value: `2.934849005663455e-09`
- consumption: `2.1651891433372274e-09`
- transfer: `1.92715998714732e-09`
- labor: `3.76597996000552e-09`

All remain below the existing `1e-3` truncation guard. This diagnostic does not alter or reinterpret that guard.

## Complete mismatch localization

- Common-core productivity nodes: 17, from `0.5` through `1.5` at spacing `0.0625`.
- Compared states: `3 * 3 * 17 = 153`.
- Candidate-ID mismatches: `4`.
- Every mismatch is on the liquid lower boundary `b=0`.
- The mismatches do not form one contiguous productivity region. They occur at `z={0.5,0.5625,0.75}` across different illiquid-asset states.

| Tensor index `(i_a,i_b,i_z_core)` | `(a,b,z)` | Boundary regime `(a,b)` | 25 ID | 29 ID |
|---|---|---|---|---|
| `(0,0,4)` | `(0.0,0.0,0.75)` | `(lower,lower)` | `FZ` | `FF` |
| `(1,0,1)` | `(0.5,0.0,0.5625)` | `(interior,lower)` | `BZ` | `BF` |
| `(2,0,0)` | `(1.0,0.0,0.5)` | `(upper,lower)` | `BZ` | `BF` |
| `(2,0,1)` | `(1.0,0.0,0.5625)` | `(upper,lower)` | `BZ` | `BF` |

## Values and directional derivatives

`null` denotes an invalid outward derivative. All validity masks are identical between the two grids.

| State | Value 25 | Value 29 | `V_a^F` 25 / 29 | `V_a^B` 25 / 29 | `V_b^F` 25 / 29 | `V_b^B` 25 / 29 |
|---|---:|---:|---:|---:|---:|---:|
| `(0,0,4)` | `-21.54186323226287` | `-21.54186323226286` | `1.4695188933190906 / 1.4695188933190622` | `null / null` | `1.3432910998402932 / 1.3432910998403016` | `null / null` |
| `(1,0,1)` | `-21.112948169083566` | `-21.11294816908358` | `1.4429520282705397 / 1.4429520282704758` | `1.4938851800858401 / 1.4938851800857975` | `1.345305653026871 / 1.3453056530268825` | `null / null` |
| `(2,0,0)` | `-20.42460617951521` | `-20.424606179515248` | `null / null` | `1.4478948962984717 / 1.447894896298429` | `1.3171605522414993 / 1.3171605522415064` | `null / null` |
| `(2,0,1)` | `-20.391472154948296` | `-20.391472154948342` | `null / null` | `1.4429520282705397 / 1.4429520282704758` | `1.312382517375461 / 1.312382517375471` | `null / null` |

The value differences are `1.07e-14` to `4.62e-14`; valid directional-derivative differences are `7.11e-15` to `6.39e-14`.

The control shadow derivative reconstructed from the consumption FOC, `c^(-gamma_c)`, is respectively:

| State | 25 | 29 | Difference `29-25` |
|---|---:|---:|---:|
| `(0,0,4)` | `1.3512695969499569` | `1.3512695969499537` | `-3.11e-15` |
| `(1,0,1)` | `1.7201615258702152` | `1.7201615258702028` | `-1.24e-14` |
| `(2,0,0)` | `1.7761427384292177` | `1.7761427384291966` | `-2.11e-14` |
| `(2,0,1)` | `1.6632863303532692` | `1.6632863303532393` | `-3.00e-14` |

## Selected controls, drifts, multipliers, and KKT state

| State/grid | `c` | labor / aggregate | `d` | cost | `mu_a` | `mu_b` | `lambda_a` | `lambda_b` | stored KKT residual |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `(0,0,4)` 25 `FZ` | `0.7400447714187964` | `1.0134521977124678` | `0.01875488675096` | `0.001289490114589335` | `0.01875488675096` | `4.9960036108132044e-15` | `-1.199040866595169e-14` | `0` | `8.159411029326657e-15` |
| `(0,0,4)` 29 `FF` | `0.7400447714187981` | `1.0134521977124653` | `0.01875488675096` | `0.001289490114589335` | `0.01875488675096` | `1.5543122344752192e-15` | `1.2878587085651816e-14` | `0.00797849710965215` | `1.6436429868434048e-16` |
| `(1,0,1)` 25 `BZ` | `0.5813407549003914` | `0.9675908583019959` | `-0.0407718308372` | `0.0037009337316772526` | `-0.0207718308372` | `4.107825191113079e-15` | `0` | `2.220446049250313e-16` | `9.423101212153411e-15` |
| `(1,0,1)` 29 `BF` | `0.5813407549003956` | `0.9675908583019891` | `-0.0407718308372` | `0.0037009337316772526` | `-0.0207718308372` | `-3.885780586188048e-15` | `0` | `0.3748558728433202` | `9.035850477407446e-15` |
| `(2,0,0)` 25 `BZ` | `0.5630178129063987` | `0.8880713692146088` | `-0.1348093821677` | `0.015827253868603494` | `-0.09480938216769999` | `2.220446049250313e-15` | `4.6629367034256575e-15` | `0` | `2.4890462820001354e-16` |
| `(2,0,0)` 29 `BF` | `0.5630178129064054` | `0.8880713692145984` | `-0.13480938216771` | `0.015827253868605343` | `-0.09480938216770998` | `-1.6653345369377348e-15` | `-3.1086244689504383e-15` | `0.45898218618769016` | `1.7502109496558118e-15` |
| `(2,0,1)` 25 `BZ` | `0.6012193942504221` | `0.9355985608237138` | `-0.08246925563077` | `0.007524051843685145` | `-0.042469255630769996` | `1.7763568394002505e-15` | `3.1086244689504383e-15` | `2.220446049250313e-16` | `7.937356594753146e-17` |
| `(2,0,1)` 29 `BF` | `0.6012193942504329` | `0.9355985608236972` | `-0.08246925563079` | `0.007524051843687794` | `-0.042469255630789994` | `-9.992007221626409e-16` | `-1.5543122344752192e-15` | `0.3509038129777682` | `9.992007221626409e-16` |

For consumption, labor, transfer, cost, `mu_a`, `mu_b`, and stored KKT residual, every 25/29 difference is below `1e-12`, and therefore also below `1e-7`. `lambda_b` is not machine-equivalent: the `F` construction carries a positive lower-bound multiplier while the `Z` construction has a zero or machine-zero multiplier. This multiplier difference is a representation/KKT-branch distinction, not a material difference in the selected controls or drifts. Every candidate remains lower-bound feasible and every recorded KKT component is below `1e-14`.

## Complete admissible-candidate and Hamiltonian comparison

No candidate-construction availability switch occurred. At every mismatch, both candidate identities were present in both solves; therefore there is no excluded candidate whose missing-construction reason must be inferred.

| State | Grid | Rank 1 `(ID,H)` | Rank 2 `(ID,H)` | Hamiltonian gap | Relative gap |
|---|---|---|---|---:|---:|
| `(0,0,4)` | 25 | `FZ, -0.7870266107983093` | `FF, -0.7870266107983095` | `2.220446049250313e-16` | `2.220446049250313e-16` |
| `(0,0,4)` | 29 | `FF, -0.7870266107983098` | `FZ, -0.78702661079831` | `2.220446049250313e-16` | `2.220446049250313e-16` |
| `(1,0,1)` | 25 | `BZ, -1.0415649615914495` | `BF, -1.041564961591451` | `1.5543122344752192e-15` | `1.4922854471797152e-15` |
| `(1,0,1)` | 29 | `BF, -1.0415649615914473` | `BZ, -1.0415649615914488` | `1.5543122344752192e-15` | `1.4922854471797184e-15` |
| `(2,0,0)` | 25 | `BZ, -1.106053411048771` | `BF, -1.106053411048772` | `1.1102230246251565e-15` | `1.0037698121399327e-15` |
| `(2,0,0)` | 29 | `BF, -1.1060534110487665` | `BZ, -1.1060534110487672` | `6.661338147750939e-16` | `6.02261887283962e-16` |
| `(2,0,1)` | 25 | `BZ, -1.0077487944506553` | `BF, -1.0077487944506558` | `4.440892098500626e-16` | `4.4067451362434505e-16` |
| `(2,0,1)` | 29 | `BF, -1.0077487944506522` | `BZ, -1.0077487944506525` | `2.220446049250313e-16` | `2.203372568121732e-16` |

The candidate pairs have the same transfer and essentially the same consumption, labor, adjustment cost, and asset drifts within each solve. All reported `mu_b` values have magnitude at most `4.9960036108132044e-15`, far below the frozen `1e-12` drift-direction tolerance. Consequently, `drift_matches_direction` admits both the forward-labeled and zero-labeled liquid candidates.

The existing deterministic sort key is:

```text
(-hamiltonian, zero-transfer-candidate-first, candidate_id)
```

None of these identifiers has the zero-transfer suffix. The raw Hamiltonian is therefore the first effective key. The Hamiltonians are not bitwise equal, so their machine-scale ordering reverses before the lexical candidate-ID key can decide the result. If the Hamiltonians were exactly equal, lexical order would prefer `FF` over `FZ` and `BF` over `BZ`; that exact-tie rule does not control the four observed selections.

## State-level classification

| State | Classification | Reason |
|---|---|---|
| `(0,0,4)` | `NEAR_TIE_SELECTION_INSTABILITY` | Both `FZ` and `FF` exist in both solves; gap `2.22e-16`; controls/drifts are machine-equivalent; ranking reverses. |
| `(1,0,1)` | `NEAR_TIE_SELECTION_INSTABILITY` | Both `BZ` and `BF` exist in both solves; gap `1.55e-15`; controls/drifts are machine-equivalent; ranking reverses. |
| `(2,0,0)` | `NEAR_TIE_SELECTION_INSTABILITY` | Both `BZ` and `BF` exist in both solves; gaps `1.11e-15` and `6.66e-16`; controls/drifts are machine-equivalent. |
| `(2,0,1)` | `NEAR_TIE_SELECTION_INSTABILITY` | Both `BZ` and `BF` exist in both solves; gaps `4.44e-16` and `2.22e-16`; controls/drifts are machine-equivalent. |

Rejected primary classes:

- `MATERIAL_POLICY_DIFFERENCE`: not supported; physical controls and drifts are machine-equivalent.
- `BOUNDARY_REGIME_SWITCH`: not supported; all four states remain on the same lower-`b` boundary and retain feasibility.
- `CANDIDATE_CONSTRUCTION_AVAILABILITY_SWITCH`: not supported; both identities are available in both solutions.
- `IDENTIFIER_ONLY_EQUIVALENCE` alone: incomplete, because `lambda_b` differs between the `F` and `Z` representations even though physical controls/drifts and KKT residual quality are equivalent.

## Root cause and scientific assessment

Primary conclusion:

`TRUNCATION_SENSITIVITY_NEAR_TIE_OR_IDENTIFIER_ONLY`

The upper truncation changes common-core values and derivatives by roughly `1e-14`. At four lower-liquid-boundary states, the production candidate builder admits both a forward-labeled and zero-labeled liquid candidate because both drifts are inside the `1e-12` zero-drift band. Their Hamiltonians differ at only machine scale, and the tiny truncation-induced perturbation reverses the raw-Hamiltonian ordering. The deterministic selector then returns a different identifier despite numerically equivalent physical controls and drifts.

Assessment of the existing exact candidate-ID equality requirement:

`OVERLY_STRICT_FOR_THE_OBSERVED_FOUR_STATES`

Exact identifier equality is not scientifically necessary for these four observed states because the differing ID records which admissible lower-boundary representation won a machine-scale Hamiltonian comparison, not a material policy or drift change. A scientifically meaningful truncation contract should review equivalence in controls, drifts, feasibility, KKT quality, and Hamiltonian gaps, while explicitly deciding how lower-boundary multipliers and `F/Z` aliases are to be treated. This is a diagnostic assessment only; the existing requirement was not changed or bypassed.

## Forbidden-operation check

- `run_frozen_r4_steady_state()` called: no.
- Consumed steady-state fixture rerun: no.
- pytest or `tests/test_r4_steady_state.py`: not run.
- Connectivity, recurrent classes, left nullity, KFE, mass/density, or aggregates: not reached or called.
- Source, tests, fixture, configuration, parameters, tolerances, equations, and policy contracts modified: no.
- Candidate selection behavior monkeypatched or altered: no.
- Repair, tuning, artificial transition, invariant mixture, transition solver, AR(1), IRF, MATLAB, parity claim, or Results prose: none.
- Repository bytecode/cache artifacts: none; `PYTHONDONTWRITEBYTECODE=1` was set.
- Repository files written: this report only.

## Recommended next gate

A planning-only acceptance-contract review gate should decide how truncation compatibility treats machine-equivalent lower-boundary `F/Z` candidate aliases, Hamiltonian near-ties, and multiplier representation. That gate must not itself modify code or rerun the consumed fixture. Any later implementation change requires a separate, precisely authorized implementation task and independent validation.
