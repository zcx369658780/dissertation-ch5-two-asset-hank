# Chapter 5 MP4C GovInv initialization and labor-normalization redesign specification

Date: 2026-09-10

Builder verdict: `GOVINV_LABOR_REDESIGN_SPEC_PASS__SEPARATE_CAPITAL_AND_LABOR_CORRECTION_PATHS_DEFINED`

## Scope and live authority

This is a zero-science design package. Live `origin/main` at task start was
`9d1662bd85cdb3dd5be8660d2d08aa2bbe497aae`, where
`project_rules/PROJECT_RULE_INDEX_CURRENT.md` names
`tasks/CH5_MP4C_GOVINV_INITIALIZATION_AND_LABOR_NORMALIZATION_REDESIGN_SPEC.md`
as the active Builder task. The older current-status, session-handoff, and roadmap
files still state that no Builder task is active; that documentation lag was preserved
and was not allowed to override the newer live rule index and exact task.

No MATLAB, household, HJB, KFE, `Lt_seperate`, firm, root/Brent, outer-turn,
steady-state, GE, annual, IRF, or Results call was made. Protected MATLAB was read
only. No production equation, parameter, grid, solver, bound, controller, or runtime
state was changed. `Results eligibility=FALSE`.

## Source findings

### Capital and GovInv

The protected source initializes `GovInv=Kt0*param.GovInv_ratio`
(`mpHANK_equilibrium_2000.m:27-40`). The corrected-2018 diagnostic specialization
sets the ratio to one, so G0 is `GovInv0=Ktarget`. Firm capital is then
`Kt=Kt_supply+GovInv` (`HANK_firm.m:14`), while `Kt_supply` is built only from
household illiquid `At*N` and the cross-province allocation
(`HANK_mp_1turn.m:29-37`). `Bt` and `At+Bt` are not productive private capital.

The accepted turn-1 ledger has positive private supply in 31/31 provinces. Hence G0
adds positive private capital on top of the full target by construction. In turns
20-25 there were zero GovInv decreases; median GovInv/target rose from
`2.143588810000001` to `2.8531167061100016`. G0 is therefore defensible only as a
historical/source-faithful numerical start, not as an economically identified
public-capital initialization.

G1, `GovInv0=max(Ktarget-Kt_supply_initial,0)`, is dimensionally and algebraically
coherent: when the selected private supply is below target, it makes initial firm
capital equal the target and preserves nonnegative GovInv. It is not yet identified.
`Kt_supply_initial` must be an At-only, population-scaled, cross-province allocated
stock in the same MU/year/price contract as `Ktarget`, observed at a declared point
before GovInv-dependent iteration. Generic initialized `At`, one explicitly budgeted
household initialization pass under predeclared prices, and a lagged/source state are
different scientific objects. The source and accepted evidence do not select one,
and the `At`-grid-to-MU bridge remains unresolved.

G2 is syntactically supported by the source parameter `GovInv_ratio`, but no inspected
source or accepted dissertation evidence identifies an economic fixed share `g0`.
G3 is compatible with the firm accounting identity, but no accepted province public-
capital series or public/private decomposition is available. G2 requires Owner/source
authority; G3 is `DATA_NOT_AVAILABLE` pending an admitted external series. Neither may
be tuned from convergence.

Detailed comparison: `reports/mp4c_govinv_labor_redesign_20260910/govinv_candidate_matrix.csv`.

### Existing controller

The firm computes raw `ra0` and clips it into stored `results.ra`
(`HANK_firm.m:54-65`). Only after a completed nonconverged turn, and only when
`maxKNratiogap<0.1` in steady-state mode, the outer loop first updates `Zt` for a
greater-than-one-percent output gap, then reads the **clipped** return. It multiplies
GovInv by `0.9` below `ramin+0.02` or by `1.1` above `ramax-0.02`; only afterward is
`tKNratio` refreshed as `0.6*current+0.4*old` (`HANK_mp_1eq.m:47-62`).

This is a return-bound controller, not a capital-target residual controller. It
retains the direction of a clipped boundary hit but loses the raw exceedance
magnitude. Initialization repair and controller redesign should be separated into
different future tasks so their effects remain attributable. A first future gate may
change initialization while preserving the controller; only a later, separately
authorized gate should decide whether to retain the trigger, study under-relaxation,
or replace the objective. No damping law or coefficient is selected here.

Detailed compatibility note:
`reports/mp4c_govinv_labor_redesign_20260910/govinv_controller_compatibility.md`.

## Labor dimensional chain and large-ratio mechanism

The source uses one mutable `results.Lt` field for three roles:

1. initialization sets `Lt=N`, where total-route `N` is resident population;
2. the household solver overwrites it with per-household efficiency labor
   `sum(z*l*g*da*db)`, with no population multiplication;
3. after migration/allocation, the firm overwrites it with destination aggregate
   `Lt_supply`.

`Lt_seperate.m` does **not** directly migrate the HJB `results.Lt`. For each origin
`i` and destination `j` it recomputes

`ell_ji = Ct_i^(-ga/phi_l) * [wjt_j*(1-tau_i-sigmau_ji)/phi_ji]^(1/phi_l)`.

It then multiplies each origin column by `N_i` exactly once. Rows are destinations,
columns are origins, and `Lt_supply_j=sum_i ell_ji*N_i`. The firm uses this row sum as
its labor input. The source imposes neither `sum_j ell_ji=1` nor a 0-1 employment/
hours bound. Consequently

`sum_j Lt_supply_j = sum_i N_i * sum_j ell_ji`,

which need not equal `sum_i N_i`. In the accepted turns 20-25, aggregate firm labor
divided by aggregate population proxy is about `12.4493351333288`; the pooled
province-turn ratio range is the already accepted `4.589147349109114` to
`153.05180501585224`.

Classifications:

- **Confirmed:** household labor and destination firm labor are efficiency-labor
  levels, not headcount shares; `Lt_seperate` multiplies population exactly once;
  its origin columns are not normalized; national labor is not conserved relative
  to population; nonlinear labor supply has no employment-rate normalization; and
  `results.Lt` changes role over the turn.
- **Likely contributor:** the undeclared household consumption/wage numeraires and
  the sum across 31 unnormalized destination choices amplify numerical scale.
- **Unresolved:** the intended economic period/unit of efficiency labor and the
  independent employment/workplace target. The accepted evidence does not support
  calling the ratio an observed employment excess or diagnosing a second population
  multiplication.

The object that may eventually be compared with a population/employment target is
destination aggregate `firm_Lt_supply`, but only after a reference has been placed in
the same efficiency-labor, period, geographic, and aggregate-unit contract. HJB
household `Lt` is an intermediate per-household efficiency-labor object and must not
be compared directly with province workplace employment.

Detailed chain:
`reports/mp4c_govinv_labor_redesign_20260910/labor_object_dimensional_chain.csv`.

## Labor-reference candidates

L0, `Ltarget_i=N_i`, is retained only as a transparent population-proxy baseline. It
conserves the national population total but is not observed workplace employment and
is not commensurate with current firm efficiency labor.

L1 is mathematically feasible only as a **new, explicitly normalized calibration
reference**, not as a literal static execution of `Lt_seperate`. The literal source
weights depend on endogenous `Ct_i` and `wjt_j`, in addition to taxes, geography/
migration cost, and GDP-per-capita-based `phi_ji`; therefore geography and GDP per
capita alone do not identify the source `ell_ji`.

If Owner authorizes an exogenous source-inspired kernel `q_ji>=0`, its origin-column
shares can be defined as

`s_ji = q_ji / sum_k q_ki`, and `Lref_j = sum_i s_ji*N_i`.

Then `sum_j Lref_j=sum_i N_i`. The allowed contents of `q_ji`—including whether
source `phi_ji`, distance-based `sigmau_ji`, a tax convention, or an exogenous wage
proxy enters—remain `OWNER_OR_DATA_DECISION_REQUIRED`. This design must be described
as a migration-adjusted population reference, not observed workplace employment.

L2, `e_i*N_i`, would be more empirically interpretable only with authoritative,
year-aligned province employment/labor-force data. The protected loader mentions an
employment sheet, but no accepted 2018 definition, coverage, workplace/residence
mapping, or hash-bound data authority exists in this task. L2 is
`DATA_NOT_AVAILABLE`.

L3 may use a separately authorized migration mechanism only to create destination
shares, followed by normalization to an independently fixed national labor aggregate
`Lbar`: `Lref_j=Lbar*q_j/sum_k q_k`. This preserves destination-share structure and
prevents the current unnormalized level explosion, but `Lbar`, origin weights, and
whether endogenous `Ct/wjt` may enter are Owner/data decisions. It is a calibration-
normalization change, not a proof of observed employment.

Detailed comparison:
`reports/mp4c_govinv_labor_redesign_20260910/labor_reference_candidate_matrix.csv`.

## Lowest-risk joint sequence

The dependency is one-way:

`frozen 2018 Y/K/N/alpha -> selected external labor reference -> same-year Z ->`
`pre-household firm-price receipt -> optional one-pass private-K observation ->`
`GovInv0 -> complete initial state -> separately governed controller -> outer loop`.

The first four documentary/algebraic gates are zero-science. Use of a newly selected
labor reference in model state, price initialization, any household observation pass,
construction of a runtime GovInv state, firm evaluation, or outer loop requires a new
exact task and explicit scientific-call budget. If a household pass is later chosen,
it must be exactly one labelled initialization observation after prices are fixed; it
is not a turn, cannot retry implicitly, and cannot be followed automatically by
`Lt_seperate`, firm, controller, or trajectory execution.

Initialization correction should precede any controller study. Capital and labor
identification must remain separate so a labor-scale change cannot be credited as a
GovInv/controller repair. The full staged contract is in
`reports/mp4c_govinv_labor_redesign_20260910/joint_initialization_sequence.md`.

## Required answers

1. **Can G0 remain scientifically defensible?** No, not beyond a historical/source-
   faithful numerical start. It lacks a public-capital identification contract and
   mechanically adds positive private supply above the target.
2. **Is G1 structurally coherent?** Yes as an accounting initialization, conditional
   on an independently defined At-only `Kt_supply_initial` in matching MU/year units.
   Its observation point and At-to-MU bridge remain Owner decisions; no current object
   is selected.
3. **Split initialization and controller?** Yes. First identify and test initialization
   with the controller frozen; decide controller objectives/damping in a separate task.
4. **Why can `firm_Lt_supply/N0` reach 5-150?** The numerator sums nonlinear,
   destination-specific efficiency-labor levels across 31 destinations after one
   population multiplication, without share or national-total normalization. It is
   not a headcount share. Wage/consumption numeraire ambiguity may further affect scale.
5. **Which labor object should face a target?** Destination aggregate
   `firm_Lt_supply`, but only against an independently identified reference with the
   same efficiency/period/geography/unit contract. Neither raw N0 nor household Lt is
   presently such a target.
6. **Is geography/GDP-per-capita migration adjustment feasible?** A conserved static
   reference is mathematically feasible after exogenous kernel and column
   normalization are specified. It is not uniquely recoverable from literal
   `Lt_seperate` without endogenous `Ct/wjt`, so its kernel is an Owner calibration
   choice rather than source-determined fact.
7. **Lowest-risk implementation order?** Close labor-reference/national-total and
   private-K observation decisions; validate static units; authorize at most one
   initialization household observation if needed; select GovInv initialization;
   assemble one initial-state receipt; only afterward open a separate controller and
   bounded-trajectory task.
8. **Remaining Owner choices?** Private-K observation and unit bridge; G1 versus an
   externally justified G2/G3; whether any source-inspired static migration kernel is
   admissible; fixed national labor aggregate and origin weights; admission of
   employment/public-capital data; and future controller objective/damping authority.

## Evidence and stop boundary

Repository package: `reports/mp4c_govinv_labor_redesign_20260910/`.
The package contains candidate matrices, the dimensional chain, joint initialization
sequence, Owner decision matrix, zero-call ledger, source/hash receipt, focused static
test receipt, and manifest/readback.

This PASS means the capital and labor correction paths are separately specified and
their unresolved identification gates are explicit. It does not select or implement a
production winner, authorize a scientific call, accept a steady state, or support
Results. The next gate is independent ChatGPT Reviewer ACCEPT/REJECT of this candidate.
