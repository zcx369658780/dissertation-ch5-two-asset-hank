# Chapter 5 MP4C origin-preserving bilateral labor-normalization implementation acceptance

Date: 2026-09-10

Reviewer verdict: `ORIGIN_PRESERVING_BILATERAL_LABOR_NORMALIZATION_ACCEPTED__FULL_MATRIX_TRACEABILITY_AND_ORIGIN_MASS_CONSERVATION_ENFORCED__GOVINV_REMAINS_NEXT_PRIMARY_STEADY_STATE_BLOCKER`

Candidate accepted: `a76ea81eda4093ce762bf6660b5fbdff0a7ec700`.

## Independent review

The candidate was independently compared against baseline `3e8d26d1c5430d9734ec5ac3d4c3e74e68217ee9`. It is one commit ahead and changes only the dedicated normalized labor successor path, its additive one-turn integration, exports, tests, report, and evidence package.

The legacy `reconstruct_migration_labor` and `run_source_faithful_one_turn` bodies remain source-faithful and separate. The new route is explicitly named `reconstruct_origin_preserving_normalized_migration_labor` and retains destination-row/origin-column orientation.

The normalized algorithm evaluates the existing Lt-separate-style attractiveness kernel without population, normalizes each origin column, then multiplies household labor per capita by that origin's population exactly once. It therefore constructs:

`L_origin[i] = household_labor_per_capita[i] * N[i]`

`s[j,i] = q[j,i] / sum_j q[j,i]`

`M[j,i] = s[j,i] * L_origin[i]`

`L_firm[j] = sum_i M[j,i]`.

The implementation enforces both origin-column conservation and national conservation. It retains the full `q`, `s`, origin mass, bilateral flow matrix, destination labor, column sums, net labor flow, and conservation residual as read-only evidence objects.

This preserves province-to-province labor provenance required for later household wage attribution while avoiding the previous multiplication of one origin's effective labor scale across all destinations without a conservation restriction.

## Key acceptance points

- 31x31 destination-by-origin provenance is retained.
- Each origin column sums to that origin's aggregate household labor mass.
- National destination labor equals national origin labor.
- Origin labor and same-province destination labor are allowed to differ, preserving net migration.
- Population is multiplied exactly once.
- Destination-wage changes alter bilateral shares without altering any origin total labor mass.
- Origin household-labor changes alter that origin's column mass without mechanically changing other origins' masses.
- Invalid/nonfinite/zero-total attractiveness columns fail closed; there is no equal-share fallback.
- Current CES-like household composite wage formula is intentionally unchanged.
- Capital, GovInv, controller, HJB, KFE, bounds, grids, and scientific runtime are unchanged.
- Focused tests passed and the evidence manifest/readback is internally consistent.
- Scientific/model calls remained zero.

## Scientific boundary

This acceptance freezes the bilateral labor-normalization implementation as an accepted successor component. It does not prove that the labor normalization is the dominant cause of the current steady-state failure, does not authorize changing the household wage aggregation rule, and does not authorize a new trajectory by itself.

The accepted 25-turn evidence still identifies GovInv as the dominant capital overshoot component. Therefore the next primary steady-state redesign gate remains GovInv initialization/private-capital reconciliation, while the normalized bilateral labor route can be integrated only under a separately authorized scientific task.

`Results eligibility=FALSE`.
