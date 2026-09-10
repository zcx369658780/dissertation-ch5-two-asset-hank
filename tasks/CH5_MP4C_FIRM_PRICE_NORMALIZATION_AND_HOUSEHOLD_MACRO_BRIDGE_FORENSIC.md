# CH5 MP4C firm-price normalization and household↔macro bridge forensic

Date: 2026-09-10. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Perform a **zero-household / zero-steady-state forensic** explaining why the accepted unit-normalized 2018 initialization still produces broad firm-price boundary hits:

- raw `ra`: 30/31 above `[.02,.09]`;
- raw `wjt`: 31/31 above `[.8,1.3]`.

The goal is **not** to widen bounds or tune parameters. The goal is to separate, using source equations and deterministic algebra only, the following candidate sources:

1. firm-price equations are economically consistent but expressed in units incompatible with legacy bounds;
2. wage and household-flow normalization is inconsistent with the new macro `MU/NU` contract;
3. firm-return normalization embeds a different capital/period convention;
4. household `a/b` grid ↔ macro capital bridge is undefined and therefore cannot yet be combined consistently with firm-side macro quantities;
5. legacy bounds were numerical safety ranges calibrated under the old mixed-year/multiplier scale and are not invariant to the corrected unit contract;
6. some other source-backed normalization/ordering issue exists.

No HJB, KFE, household controls, allocation call, outer turn, steady state, GE, annual, IRF or Results is authorized.

## 2. Required authority

Read current live governance plus:

- `docs/CH5_MP4C_UNIT_NORMALIZED_INITIALIZATION_ONLY_PROBE_REPORT.md`;
- `docs/CH5_MP4C_UNIT_NORMALIZED_INITIALIZATION_ONLY_PROBE_ACCEPTANCE.md`;
- `docs/CH5_MP4C_MULTI_PROVINCE_STEADY_STATE_CALIBRATION_AND_INITIALIZATION_REDESIGN_SPEC.md`;
- raw-NBS rebuild report and ledgers;
- MATLAB logic audit.

Read protected MATLAB source read-only at:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

At minimum:

- `HANK_firm.m`;
- `HANK_mp_1turn.m`;
- `wage_caculate.m`;
- `HANK_2ASSETS_HJB.m`;
- `multi_prov_HANK_12sts.m`;
- `mpHANK_equilibrium_2000.m`;
- `load_GDPdata.m`.

Do not modify protected source.

## 3. Frozen diagnostic inputs

Use the accepted initialization probe receipt exactly as the baseline:

- actual 2018 GDP/POP;
- raw-NBS GFCF Track-A PIM `K2018` with `delta_pim=.096`;
- `alpha=.7380939146868483`;
- macro unit `MU=10万元`;
- population unit `NU=100 persons`;
- protected firm `delta=.025` where source uses it;
- protected-source `mt0=.92` under zero-change initialization;
- existing firm safety bounds unchanged.

Do not select a new production capital route in this task.

## 4. Scientific/model-call budget

Zero:

- MATLAB model calls;
- Python household/HJB/KFE/control;
- `HANK_firm` runtime call;
- `Lt_seperate`;
- capital allocation runtime;
- outer turn;
- steady state;
- GE/annual/IRF/Results;
- root/direct/iterative/eigen solves.

Allowed:

- static source inspection;
- deterministic algebra from saved 2018 receipt;
- unit/dimensional transformations;
- per-province formula decomposition;
- symbolic/manual-equivalent checks;
- source hashes;
- serialization/tests.

## 5. Workstream A — decompose raw wage and return formulas

For each province, decompose protected-source initialization formulas into components.

For wage, explicitly show the identity equivalent to the source, including:

`w_raw = mt * (1-alpha) * Y/L`

when the Cobb-Douglas identity is imposed.

Record:

- `Y/L` in current model units;
- labor share `(1-alpha)`;
- `mt`;
- resulting raw wage;
- legacy wage bound ratio `w_raw/1.3`.

Determine whether the broad wage-bound hit follows mechanically from `MU/NU` choice rather than from province-specific economic abnormality.

For `ra`, decompose at least:

- marginal-product component `mt*alpha*Y/K`;
- firm depreciation deduction;
- profit/dividend/corporate-tax component exactly as source defines it;
- any other additive term;
- total `ra_raw`;
- ratio to `.09`.

Produce national min/median/max and top/bottom provinces by each component.

## 6. Workstream B — unit-rescaling invariance test

Pure algebra only.

Let aggregate money unit scale by `s_M` and population/labor unit by `s_N`. Derive how the protected formulas transform for:

- `Z`;
- `Y/K`;
- `Y/L`;
- raw `ra`;
- raw `wjt`;
- household `w` if expressed in the same wage unit.

Identify which quantities should be economically invariant to money-unit changes and which numerically change under a population/labor unit change.

Explicitly answer:

- Is `ra_raw` invariant to common money rescaling of Y and K?
- Is `w_raw` invariant to common money rescaling of Y but not labor rescaling?
- What unit does one numerical unit of `wjt` imply under `MU=10万元`, `NU=100 persons`?
- Can legacy wage bounds `[.8,1.3]` be compared directly to `w_raw≈8–36` under this new unit contract without an explicit wage normalization mapping?

Do not choose a new mapping solely to make bounds pass.

## 7. Workstream C — recover household monetary normalization

Statically inspect `HANK_2ASSETS_HJB.m` and initialization parameters to identify every clue about the numerical meaning of one unit of:

- liquid asset `b`;
- illiquid asset `a`;
- consumption `c`;
- wage `w`;
- transfer `Tt`;
- `AtTax`.

Trace budget equations and state grids.

Classify each as:

- `SOURCE_DEFINED_UNIT`;
- `IMPLIED_RELATIVE_UNIT_ONLY`;
- `UNDEFINED_ABSOLUTE_CURRENCY_NORMALIZATION`.

Determine whether `wjt` `[.8,1.3]` and initial household `w=20` can coexist under a single source-defined absolute currency unit, or whether they only function as numerical relative scales.

Do not infer an asset bridge from convergence.

## 8. Workstream D — household↔macro bridge equation

Write the exact current source bridge:

`At_grid -> At*N -> Kt_supply -> Kt_supply + GovInv -> firm K`.

Then write the dimensionally explicit successor form:

`K_private_MU = At_grid * beta_a * N_NU`

where `beta_a` is an unknown conversion factor unless source evidence defines it.

Using saved initialization-only data only, compute descriptive ratios for `beta_a=1` but do not calibrate `beta_a`.

Show algebraically what would be required for a valid bridge:

- a documented household currency normalization;
- or an independent economic calibration target not based on convergence.

List legitimate future identification routes (e.g. aggregate household illiquid assets versus productive private capital accounting identity) without adopting one.

## 9. Workstream E — legacy bounds provenance

Search protected source and repository history/docs for the scientific/numerical origin of:

- `ra` bounds `[.02,.09]`;
- `wjt` bounds `[.8,1.3]`;
- legacy initial `ra=.09`, `rah=.09`, `wjt=.6`, `w=20`.

Classify each bound as:

- economically calibrated;
- empirically chosen numerical convergence range;
- source-provenance unknown.

Owner has already stated that historical rate bounds were numerical/HJB-convergence safeguards. Preserve that interpretation where source/history supports it.

Do not widen or rescale bounds in this task.

## 10. Required conclusions

The report must distinguish at least these possibilities:

- `PRICE_BOUND_HITS_PRIMARILY_UNIT_NORMALIZATION_MISMATCH`;
- `PRICE_BOUND_HITS_PRIMARILY_ECONOMIC_RATIO_LEVELS`;
- `MIXED_UNIT_AND_ECONOMIC_LEVEL_EFFECTS`;
- `HOUSEHOLD_CURRENCY_NORMALIZATION_UNRESOLVED`;
- `INSUFFICIENT_SOURCE_EVIDENCE`.

Multiple classifications may apply to wage and return separately.

A particularly important distinction:

- high `ra_raw` driven by `Y/K` is not fixed by a common money-unit rescale;
- high `w_raw` driven by `Y/L` may depend directly on the chosen population/labor normalization and therefore cannot be judged against legacy numeric wage bounds without matching units.

## 11. Evidence outputs

Use fresh root, e.g.:

`D:\ProjectTemp\ch5-firm-price-normalization-forensic-20260910-001`

Required repository-safe outputs:

- `docs/CH5_MP4C_FIRM_PRICE_NORMALIZATION_AND_HOUSEHOLD_MACRO_BRIDGE_FORENSIC_REPORT.md`;
- `reports/mp4c_firm_price_normalization_forensic_20260910/province_price_component_decomposition.csv`;
- `.../unit_rescaling_invariance_contract.md`;
- `.../household_currency_normalization_audit.md`;
- `.../asset_bridge_identification_contract.md`;
- `.../legacy_price_bound_provenance.csv`;
- source/hash receipt;
- zero scientific-call ledger;
- focused tests/static checks;
- manifest/readback.

## 12. Allowed verdicts

- `FIRM_PRICE_NORMALIZATION_FORENSIC_PASS__WAGE_UNIT_MISMATCH_AND_RETURN_LEVEL_EFFECTS_SEPARATED`;
- `FIRM_PRICE_NORMALIZATION_FORENSIC_PARTIAL__HOUSEHOLD_CURRENCY_NORMALIZATION_UNRESOLVED`;
- `FIRM_PRICE_NORMALIZATION_FORENSIC_BLOCKED__SOURCE_EVIDENCE_INSUFFICIENT`.

## 13. Authority after completion

Even on PASS:

- do not change price bounds;
- do not choose `beta_a`;
- do not run household/HJB/KFE;
- do not run first outer turn or steady state;
- do not test damping/hysteresis;
- do not change GovInv controller;
- do not enter GE/annual/IRF/Results;
- do not merge main;
- do not publish a successor task.

Commit and non-force push dedicated branch only.
