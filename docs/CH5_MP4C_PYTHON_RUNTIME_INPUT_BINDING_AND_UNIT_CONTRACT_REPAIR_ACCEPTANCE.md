# Chapter 5 MP4C Python runtime input-binding and unit-contract repair acceptance

Date: 2026-09-10

Reviewer verdict:

`PYTHON_RUNTIME_INPUT_BINDING_REPAIR_ACCEPTED__CORRECTED_2018_TRACK_A_UNIT_CONTRACT_ENFORCED__SCIENTIFIC_RERUN_STILL_NOT_AUTHORIZED`

Accepted candidate:

`a7bd3b1a705ff42e2933b22a8c6563ec47248ce4`

## Acceptance basis

The candidate implements the exact repair requested by `tasks/CH5_MP4C_PYTHON_RUNTIME_INPUT_BINDING_AND_UNIT_CONTRACT_REPAIR.md` without introducing an unapproved scientific redesign.

Key accepted points:

1. The active corrected-2018 runtime is now a single explicit Track-A/unit-normalized route using actual 2018 GDP and population, raw-NBS GFCF Track-A PIM capital, `delta_pim=.096`, `alpha=.7380939146868483`, `MU=10万元`, `NU=100 persons`, and same-year `Zt0`.
2. Legacy/canonical data remain only behind an explicitly historical replay API and are not an implicit fallback for corrected single/two/three/five-turn prepare paths.
3. The corrected runtime validates route, year, units, province order, all 31 province inputs, state/input equality, and an immutable province-input content hash before science starts.
4. The Anhui hard receipt matches the accepted initialization authority: `Y0=34010900`, `N0=L0=607600`, `K0=GovInv0=70182433.35888097`, `alpha=.7380939146868483`, `Zt0=1.681124916844091`.
5. Injection of the rejected old-scale Anhui capital/GovInv/Zt is fail-closed before a science launch marker is written.
6. `GovInv0=Ktarget` is preserved only as `SOURCE_FAITHFUL_INITIALIZATION_RULE__SCIENTIFIC_REDESIGN_PENDING`, using the corrected Track-A MU scale. No residual-GovInv redesign is adopted here.
7. `beta_a=1` remains explicitly `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`; no bridge identification or convergence-based scaling is introduced.
8. Labor roles are named distinctly enough to prevent silent conflation of population proxy, household labor and firm labor supply in the repaired runtime contract.
9. Focused task tests pass; full-suite collection problems are pre-existing module-isolation / stale historical-identity issues outside this task and did not execute tests against the repaired path.
10. Scientific/model calls are zero. No trajectory, HJB/KFE, firm runtime, outer turn, steady state, GE, annual, IRF or Results computation was run.

## Code-level reviewer checks

Reviewer inspection confirmed that `src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py` performs deterministic conversion and pre-science validation, and that corrected single-turn `prepare` builds the active payload only through this repaired route. The `execute` path reloads and validates the serialized payload before writing `science_started.json`, so the hard gate is placed before scientific state advancement.

The historical `build_legacy_canonical_runtime_payload` remains callable only by explicit name; its presence is not treated as an active fallback.

## Remaining scientific boundaries

Acceptance of this repair does **not** establish that the source-faithful initialization rule `GovInv0=Ktarget` is economically appropriate, identify the household-to-macro asset bridge coefficient, resolve wage absolute normalization, validate the KFE/HJB operators, or demonstrate outer-loop convergence.

The rejected 100-turn candidate `242e853708d3d0d4f891c7a043d7d4e3fba05c50` remains invalid as evidence for the corrected Track-A/unit-normalized trajectory because its runtime inputs violated the frozen contract.

A new bounded trajectory requires a separate exact task after Reviewer/Owner decide the next scientific diagnostic. Results eligibility remains `FALSE`.
