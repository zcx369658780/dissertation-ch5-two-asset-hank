# CH5 MP4C K1 — temporary transfer-control D1 admissibility freeze

Date: 2026-09-13.
Status: `OWNER_APPROVED_TRANSFER_CONTROL_D1_SYMMETRIC_1E5__FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION__OTHER_SCIENCE_FROZEN`.

## 1. Owner decision

The Owner approves the first temporary transfer-control admissibility stage:

- `D1 = 1e5` asset-model units per year;
- symmetric admissible interval `[-1e5, +1e5]`;
- exact inclusivity: `abs(d_raw) <= 1e5` is admissible;
- `abs(d_raw) > 1e5` is temporarily inadmissible.

This is a `TEMPORARY_NUMERICAL_CONTINUATION_SAFEGUARD`, not a structural economic transfer restriction.

The exact raw-candidate census shows that this interval rejects `55,990 / 87,027,200 = 0.064336%` raw branch-cell candidates and preserves `99.935664%` of the raw central mass. Final selected-cell static hit share in the accepted no-safeguard evidence is `0.044355%`. These are descriptive pre-implementation statistics, not convergence claims.

## 2. Frozen safeguard semantics

The approved semantic contract is:

`C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION`

For every raw nonzero transfer branch candidate already produced by the accepted transfer FOC:

1. persist the raw FOC candidate unchanged;
2. evaluate D1 admissibility using the raw value;
3. if `abs(d_raw) <= 1e5`, the branch remains eligible under all existing feasibility, boundary and selector rules;
4. if `abs(d_raw) > 1e5`, mark that raw branch `D1_INADMISSIBLE` and exclude it from selector competition;
5. do not clip the candidate to `+/-1e5`;
6. do not manufacture a replacement transfer candidate;
7. retain the already-existing zero-transfer / no-transfer option and every other otherwise-admissible branch under existing selector semantics;
8. if all nonzero branches are rejected by D1, the existing zero-transfer option remains available under its accepted law.

D1 is therefore an eligibility filter on raw FOC candidates, not a new FOC, not a candidate clipping rule and not a new zero-transfer law.

## 3. Safeguard location

D1 must act only after the accepted raw transfer candidate is constructed and before that rejected branch contributes to final candidate cost/drift/Hamiltonian/selector competition.

Required receipts:

- raw candidate value;
- branch identity;
- D1 admissible/inadmissible flag;
- existing feasibility/boundary flags separately from D1;
- whether the branch would otherwise have entered competition;
- selected final branch/control;
- fallback-to-zero usage where it occurs.

Raw receipts must never be overwritten by guarded eligibility state.

## 4. Frozen science outside D1

The following remain unchanged:

- `MODEL_TIME_BASE=ANNUAL_CONTINUOUS_TIME`;
- `rho=.05/year`;
- `rb=.02/year`;
- borrowing gap `.07/year`;
- firm/HJB `delta=.10/year`;
- `Q_z` off-diagonal `1/3/year`;
- `chi0=.1`;
- `chi1=2 years`;
- transfer FOC formula;
- derivative floor/safeguard;
- HJB/KFE equations;
- selector scoring and label meanings except for the additional D1 eligibility filter;
- boundary/KKT laws;
- grids, tolerances and solver semantics;
- G2 HJB return guard `[-.10,.35]` for the first D1 runtime diagnostic;
- wage safeguard `wjt in [.8,1.3]`;
- fixed theta, `beta_distance=2`, `beta_return=0`;
- accepted destination-by-origin `S` and same-S quantity/payoff law;
- source-faithful labor;
- C1 `GovInv=max(Ktarget-Kprivate,0)`;
- K1B/K2 OFF.

No change to `chi0/chi1`, derivative floor, return/wage guards, grid, tolerance or solver is authorized.

## 5. First-runtime treatment timing

For the first bounded causal diagnostic only:

- both paths use the same accepted turn-1 bootstrap with D1 OFF;
- beginning at turn 2, the control path remains D1 OFF;
- beginning at turn 2, the treatment path activates D1 exactly as specified above.

This preserves a byte-identical completed turn-1 scientific state and creates a turn-2 common-entering-state window in which the only scientific difference is D1 transfer-candidate admissibility.

This turn-2 timing is an experimental diagnostic design; it does not yet define the final production initialization convention.

## 6. Monitoring and interpretation

Every D1 runtime must record at least:

- raw branch candidate counts;
- D1 inadmissible counts/shares by sign, branch, province, turn and HJB iteration;
- selected-control changes induced by D1;
- number of cells where the previous winning branch becomes inadmissible;
- fallback-to-existing-zero counts;
- number of cells switching to another admissible nonzero branch;
- return/wage safeguard hit monitoring under the existing Owner contract;
- HJB convergence/statistics and transfer/cost/drift extrema;
- same-S, provenance, capital and C1 accounting.

A D1-dependent steady state remains `PROVISIONAL_STEADY_STATE`. Final accepted economics must ultimately demonstrate nondependence on binding temporary transfer-control and price safeguards where feasible.

## 7. Unapproved future stages

No D2/D3/OFF continuation stage is frozen here. `1e6`, `1e7` and OFF remain possible future options only. Advancement beyond D1 requires fresh Reviewer/Owner authority after D1 evidence.

Longer G2, G3/G4 return-guard continuation, wage-guard relaxation, K1B, K2, steady-state acceptance and Results remain unauthorized.

KFE remains `DIAGNOSTIC_ONLY`; the finite-box upper-b leakage / MATLAB-style pinning blocker remains independent.

Results eligibility=`FALSE`.
