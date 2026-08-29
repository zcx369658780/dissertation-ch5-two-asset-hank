# CH5 Two-Asset HANK R4 Steady-State Acceptance and MATLAB–Python HA Parity Preparation

## Classifications

- R4 acceptance: `R4_PYTHON_STEADY_STATE_ACCEPTED_FOR_PARITY_REVIEW`
- Parity preparation: `MATLAB_PYTHON_HA_PARITY_PREP_PARTIAL_DISSERTATION_AUTHORITY_PENDING`

This report freezes the independently accepted Python R4 synthetic steady-state evidence and prepares an owner-facing source map. It does **not** return a final MATLAB–Python parity PASS/FAIL.

## Live identity and source-continuity gate

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- Fresh-fetched live/base `origin/main`: `82ebacf64708e32b599ede5769ef5a57ed10116e`
- Isolated workspace: `D:\ProjectTemp\ch5-r4-matlab-python-parity-prep-20260829`
- Accepted Python implementation baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`
- Accepted R4 evidence commit: `8931eacf4e9f503b9ab12b75399f098177196dfb`
- `git diff 7a2388a2ba89073e307f05a909570e8c40a4be13..82ebacf64708e32b599ede5769ef5a57ed10116e -- src tests`: empty

Result: `PASS`. All accepted Python scientific/test source remains unchanged; post-baseline changes are governance/task/report-only.

## Files read

- `tasks/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_ACCEPTANCE_AND_MATLAB_PYTHON_HA_PARITY_PREP.md`
- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_RERUN_AFTER_CORRECTED_TRUNCATION_CONTRACT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_RERUN_AFTER_CORRECTED_TRUNCATION_CONTRACT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_CONTRACT_IMPLEMENTATION_CORRECTION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_AFTER_R1A_SOURCE_AUDIT_2026_08_21.md`
- `src/ch5_two_asset_hank/contracts.py`
- `src/ch5_two_asset_hank/economics.py`
- `src/ch5_two_asset_hank/derivatives.py`
- `src/ch5_two_asset_hank/boundaries.py`
- `src/ch5_two_asset_hank/policies.py`
- `src/ch5_two_asset_hank/generator.py`
- `src/ch5_two_asset_hank/hjb.py`
- `src/ch5_two_asset_hank/kfe_contract.py`
- `src/ch5_two_asset_hank/kfe.py`
- `src/ch5_two_asset_hank/productivity.py`
- `src/ch5_two_asset_hank/indexing.py`
- `src/ch5_two_asset_hank/steady_state.py`
- `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m`

## File written

- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_ACCEPTANCE_AND_MATLAB_PYTHON_HA_PARITY_PREP_REPORT.md`

## Independently accepted R4 evidence

All values below are read back from accepted GitHub report commit `8931eacf...`; nothing was rerun.

| Gate | Accepted evidence |
|---|---|
| HJB residual, primary / buffer | `8.365197423643167e-10 / 8.372715853965929e-10` |
| KKT residual, primary / buffer | `9.088497027490715e-15 / 9.423101212153411e-15` |
| generator max row sum, primary / buffer | `2.6645352591003757e-15 / 2.6645352591003757e-15` |
| minimum off-diagonal rate, primary / buffer | `4.284173835999994e-05 / 4.284173835999994e-05` |
| normalized change: value | `2.9348475455283523e-09` |
| normalized change: consumption | `2.165192411731261e-09` |
| normalized change: transfer | `1.92715998714732e-09` |
| normalized change: labor | `3.7659760021779296e-09` |
| normalized change: adjustment cost | `1.0345611728412862e-09` |
| normalized change: `mu_a` | `1.92715998714732e-09` |
| candidate compatibility | zero canonical mismatches; two raw `BF/BZ` mismatches, both bilateral qualified aliases canonicalized to `BZ` |
| `mu_b` compatibility | zero Z/F/B classification mismatches |
| endogenous `a` edges | upward `134`; downward `4`; directional rate and component-separation gates passed |
| recurrent class | count `1`; size `225`; `a` support `(0,1,2)`, including interior `a=0.5` |
| left nullity | `1` |
| `||G^T g||_inf` | `3.885780586188048e-16` |
| normalization error | `4.440892098500626e-16` |
| minimum mass / negative count | `1.411264453687144e-17 / 0` |
| mass-density consistency | `3.3306690738754696e-16` |
| synthetic `A_hh` | `0.010765933312087405` |
| synthetic `B_hh` | `0.015679440387058798` |

Acceptance interpretation: the frozen Python household steady-state fixture passed HJB/truncation, connectivity, recurrent-class, KFE, mass/density, and aggregate gates. This is not calibration, empirical, Results, or MATLAB parity acceptance.

## MATLAB source identity

Classification: `CURRENT_READ_ONLY_MATLAB_IDENTITY`. No complete expected MATLAB hash is present in live authority.

| Field | Identity |
|---|---|
| Exists | yes |
| Exact resolved path | `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m` |
| SHA-256 | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` |
| Bytes | `12227` |
| Lines | `427` |
| File type | regular file (`Archive` attribute); not a directory |
| Link/reparse identity | no `LinkType`, no target, no reparse indirection |

The file was read as source text only and was neither executed nor modified.

## Dissertation/equation authority status

The live R1A handoff records that MATLAB provenance was established but dissertation equation authority remained missing. Live GitHub provides no complete owner-designated dissertation source or equation-to-line binding in this task. Accordingly:

- code-to-code mapping proceeds as authorized;
- accepted R4 redesign decisions are identified where the GitHub task/report chain supplies authority;
- economic rows lacking that chain are marked `DISSERTATION_AUTHORITY_PENDING_OWNER_REVIEW`;
- final parity requires the Owner to designate the dissertation equation source and bind equations for utility/FOCs, budget/drifts, adjustment costs, productivity, boundaries, generator/KFE, and aggregates.

## MATLAB–Python structural map

MATLAB references below all refer to `HANK_2ASSETS_HJB.m`. “Owner?” identifies whether a scientific decision remains necessary.

| # | Object | Dissertation authority | MATLAB lines and formulation | Python lines and formulation | Primary classification | Owner? / unresolved question |
|---:|---|---|---|---|---|---|
| 1 | States: illiquid `a`, liquid `b`, productivity `z` | pending variable-definition binding | 10–20, 46–60: arrays are `[b,a,z]` | `contracts.py:23–46`: logical `(a,b,z)` | `ECONOMICALLY_EQUIVALENT_DIFFERENT_NUMERICS` | yes: confirm economic names and units |
| 2 | Shape, orientation, flattening | accepted Python indexing contract | 52–63, 161, 202, 241–245: MATLAB column-major, `b` fastest | `indexing.py:8–44`: `(a,b,z)`, `a` fastest, Fortran flatten, explicit MATLAB transpose | `AUTHORIZED_PYTHON_REDESIGN` | no for implementation; Owner should acknowledge orientation adapter |
| 3 | Household budget | pending equation binding | 263–264, 352–353: income minus `d`, cost, and consumption; `mu_a=d+r_a a` | `economics.py:49–65`: same two drift identities | `STRUCTURAL_MATCH` | yes: confirm taxes/transfers/rate symbols |
| 4 | Consumption FOC | pending equation binding | 124–126: `c` from `V_b`, with floor and zero-drift income candidate | `economics.py:24–27` | `ECONOMICALLY_EQUIVALENT_DIFFERENT_NUMERICS` | yes: MATLAB derivative floor is legacy numerical behavior |
| 5 | Labor FOC / regional labor | pending equation binding | 103–112, 127–136: scalar province labor | `contracts.py:79–104`; `economics.py:30–46`: vector wages, migration wedges, labor weights | `AUTHORIZED_PYTHON_REDESIGN` | yes: confirm dissertation multi-province aggregation |
| 6 | Rebalancing `d` sign | pending equation binding | 137–149, 262–264: positive `dh` raises illiquid drift and reduces liquid drift | `economics.py:16–21,49–65` | `STRUCTURAL_MATCH` | yes: bind symbol `d/dh` |
| 7 | Adjustment cost and low-`a` scaling | incomplete: external MATLAB function not bound | 137–149, 263, 352–353 call `HANK3_cost(...,dh,aaah,0)`; exact formula absent here | `economics.py:10–21`: `chi_0|d| + .5 chi_1 d^2/max(a,a_bar)` | `POTENTIAL_MATERIAL_MISMATCH_REQUIRES_OWNER_REVIEW` | yes: supply authoritative `HANK3_cost` formula and decide `m(a)=max(a,a_bar)` |
| 8 | Illiquid drift `mu_a` | pending equation binding | 264: `mh=dh+Rah.*aaah` | `economics.py:64` | `STRUCTURAL_MATCH` | yes: confirm return schedule (`Rah`) |
| 9 | Liquid drift `mu_b` | pending equation binding | 263 | `economics.py:59–65` | `STRUCTURAL_MATCH` | yes: confirm borrowing-rate wedge and transfers |
| 10 | Productivity law/support/boundary | accepted Python redesign; final dissertation binding pending | 16–20, 64–66, 188, 229: two-state exogenous `la_mat` switch | `productivity.py:27–53`: bounded diffusion with upwind drift, reflected lower support and no upper outflow | `AUTHORIZED_PYTHON_REDESIGN` | yes: confirm diffusion equation/support as dissertation authority |
| 11 | Directional derivatives | accepted reconstruction contract | 116–123: finite differences plus imposed endpoint derivatives/zeros | `derivatives.py:24–44`: differences plus explicit validity masks | `AUTHORIZED_PYTHON_REDESIGN` | no for code; Owner confirms economic endpoint contract |
| 12 | Upwind candidates | pending equation binding | 124–157: sign indicators assembled separately for liquid and transfer flows | `policies.py:491–553`: joint admissible derivative candidates | `AUTHORIZED_PYTHON_REDESIGN` | yes: confirm joint Hamiltonian selection is intended |
| 13 | Zero-drift candidates | accepted R4 redesign | 131–135 and 150–154 use residual indicator fallback; no explicit endogenous interior `mu_a=0` solve | `policies.py:173–258,675–727`: certified liquid-zero and interior illiquid-zero candidates | `AUTHORIZED_PYTHON_REDESIGN` | no for R4; Owner to accept relative to dissertation |
| 14 | Lower-`a` state constraint / KKT | accepted R4 redesign | 142–147, 152: sign clipping; no explicit multiplier audit | `boundaries.py:21–42,63–156`; `policies.py:514–553`: feasibility, multipliers, complementarity | `AUTHORIZED_PYTHON_REDESIGN` | no for R4; Owner validates equation authority |
| 15 | Lower-`b` borrowing constraint / KKT | accepted R4 redesign | 117–119, 131–144: endpoint derivative and sign masks | `boundaries.py:33–42,63–156`; `policies.py:142–192,514–553` | `AUTHORIZED_PYTHON_REDESIGN` | no for R4; Owner confirms borrowing-bound economics |
| 16 | Computational upper `a/b` no-outflow | accepted R4 redesign | 122–123, 143, 147, 153, 194–195: hard-coded endpoint behavior | `boundaries.py:37–40`; `generator.py:26–35` | `AUTHORIZED_PYTHON_REDESIGN` | yes: upper bounds are computational, not economic constraints |
| 17 | Corner cases | accepted R4 redesign | 144 and 153 contain narrow hard-coded corners; dual-upper closure is implicit | `policies.py:261–443,554–674`: explicit dual-upper, upper-a/lower-b, upper-a/interior-b candidates | `MATLAB_LEGACY_LIMITATION_NOT_TO_INHERIT` | no for R4; Owner should acknowledge legacy incompleteness |
| 18 | Hamiltonian comparison / deterministic selection | accepted R4 redesign | 131–154 uses ordered indicator rules, not a complete joint Hamiltonian maximization | `policies.py:58–104,497–553,728–754`: Hamiltonians, deterministic ordering, narrow near-tie canonicalization | `AUTHORIZED_PYTHON_REDESIGN` | no for R4; no broad candidate alias permitted |
| 19 | `G_a`, `G_b`, `G_z` construction | accepted operator contract | 155–232: `BB`, `AAH`, `Bswitch` separately then summed | `generator.py:13–57`: separate directional asset generators and Kronecker `G_z` | `ECONOMICALLY_EQUIVALENT_DIFFERENT_NUMERICS` | yes only for `z` law; component separation matches structurally |
| 20 | Generator row sum/off-diagonals | accepted Python validation contract | 189, 230–239 check component/total row sums; no explicit off-diagonal audit | `generator.py:53–57`; `hjb.py:61–62,76–81` validate both | `AUTHORIZED_PYTHON_REDESIGN` | no: stronger fail-closed audit is intentional |
| 21 | Productivity operator discretization | accepted Python redesign | 64–66: finite-state `Bswitch` | `productivity.py:27–78`: monotone diffusion generator and diagnostic moments | `AUTHORIZED_PYTHON_REDESIGN` | yes: final dissertation diffusion binding needed |
| 22 | KFE transpose | accepted R3/R4 operator contract | 333–340: `AT=A'`, pinned-row linear solve | `kfe_contract.py:20–41`; `kfe.py:44–46,104–119`: consume accepted `G`, forward operator exactly `G.T` | `STRUCTURAL_MATCH` | no on transpose; normalization method differs |
| 23 | Stationary normalization | accepted Python KFE contract | 337–345: arbitrary pinned row/RHS then density normalization | `kfe.py:96–132`: unique closed class, normalized stationary mass system, residual/nonnegativity checks | `MATLAB_LEGACY_LIMITATION_NOT_TO_INHERIT` | no: arbitrary pinning is not scientific uniqueness evidence |
| 24 | Mass, density, quadrature | accepted Python redesign | 341–345, 387–389: uniform `db*dah`; no explicit `z` quadrature in two-state chain | `kfe_contract.py:20–32`; `kfe.py:115–141`; `steady_state.py:241–248`: mass primary, density via cell weights, trapezoidal weights | `AUTHORIZED_PYTHON_REDESIGN` | yes: future shared object must define finite-state mass vs continuous density |
| 25 | Household aggregates `A_hh/B_hh` | pending equation binding | 347–351: quadrature-weighted `Aht`, `Bt` | `kfe.py:138–141`: expectations under stationary mass | `ECONOMICALLY_EQUIVALENT_DIFFERENT_NUMERICS` | yes: ensure same grids/distribution representation |
| 26 | Legacy shortcuts not inherited | accepted reconstruction principle | 81 and 90: tapered return plus apparent `Rah.*raah`; 188/229/343–344 assume `Nz=2`; 337–340 arbitrary KFE pin | Python uses explicit contracts throughout the files above | `MATLAB_LEGACY_LIMITATION_NOT_TO_INHERIT` | yes: decide whether line 90 is initialization defect or intended formula |

## Redesign-sensitive findings

| Area | MATLAB evidence | Accepted Python behavior | Status |
|---|---|---|---|
| Low-`a` adjustment-cost scaling | Exact cost is hidden behind `HANK3_cost` (137–149, 263); cannot prove its scale from designated file | `max(a,a_bar)` in `economics.py:10–21` and KKT at `boundaries.py:85–93,146–152` | unresolved parity question; Owner must bind formula |
| Lower-bound KKT/state constraints | directional clipping and endpoint substitutions (117–154) | explicit primal/dual/complementarity and drift feasibility (`boundaries.py:21–42,63–156`) | required by accepted R4 authority; final dissertation binding pending |
| Productivity diffusion/boundary | two-state `la_mat` switch (64–66) | monotone bounded diffusion with reflected lower endpoint (`productivity.py:27–53`) | authorized Python redesign; Owner must validate dissertation law |
| Interior zero-`mu_a` | no explicit endogenous crossing solution | explicit certified candidate (`policies.py:195–258,675–727`) | required by accepted R4 authority |
| Upper/corner candidates | hard-coded masks and partial endpoint closures (143–153,194–195) | explicit upper-a, upper-b, and corner candidates (`policies.py:261–443,554–674`) | required by accepted R4 authority; legacy limitation not inherited |
| Lower-`b` F/Z canonicalization | no candidate-level near-tie audit | only qualified active-lower-b F/Z machine-equivalent near ties canonicalize to Z (`policies.py:28–104`) | numerical stabilization under accepted contract, not an economic-policy alias |
| Generator/KFE transpose | `AT=A'` (333–340) | accepted backward `G` passed unchanged and transposed (`kfe_contract.py:35–41`; `kfe.py:44–46`) | structural match; Python adds uniqueness and mass auditing |

## Owner-facing manual parity checklist

The Owner decision column is intentionally blank and must be completed with exactly `ACCEPT`, `REJECT`, or `NEEDS_DISCUSSION`.

| ID | Compare | MATLAB lines | Python reference | Expected relationship | Proposed classification | Owner decision |
|---|---|---|---|---|---|---|
| O1 | Authoritative low-`a` cost scale and transfer FOC | 137–149, 263 | `economics.py:10–21`; `boundaries.py:146–153` | dissertation formula controls; not MATLAB-by-default | `POTENTIAL_MATERIAL_MISMATCH_REQUIRES_OWNER_REVIEW` | `ACCEPT / REJECT / NEEDS_DISCUSSION` |
| O2 | Productivity is two-state chain or bounded diffusion | 16–20, 64–66 | `productivity.py:27–53` | Python redesign must match dissertation law | `DISSERTATION_AUTHORITY_PENDING_OWNER_REVIEW` | `ACCEPT / REJECT / NEEDS_DISCUSSION` |
| O3 | Lower `a/b` state constraints and KKT multipliers | 117–154 | `boundaries.py:21–42,63–156`; `policies.py:514–553` | same no-outflow economics; Python provides explicit KKT audit | `AUTHORIZED_PYTHON_REDESIGN` | `ACCEPT / REJECT / NEEDS_DISCUSSION` |
| O4 | Interior `mu_a=0` crossing candidate | 141–154 | `policies.py:195–258,675–727` | Python explicit candidate replaces missing legacy case | `AUTHORIZED_PYTHON_REDESIGN` | `ACCEPT / REJECT / NEEDS_DISCUSSION` |
| O5 | Upper-a/lower-b and dual-upper closures | 143–153, 194–195 | `policies.py:261–443,554–674` | computational bounds must have no outflow and valid KKT | `MATLAB_LEGACY_LIMITATION_NOT_TO_INHERIT` | `ACCEPT / REJECT / NEEDS_DISCUSSION` |
| O6 | Lower-b F/Z near-tie representation | 131–154 | `policies.py:28–104,728–754`; `steady_state.py:76–154` | physical policy identical; canonical Z only in narrow qualified class | `AUTHORIZED_PYTHON_REDESIGN` | `ACCEPT / REJECT / NEEDS_DISCUSSION` |
| O7 | Budget and drift signs | 263–264, 352–353 | `economics.py:49–65` | exact economic sign agreement expected | `STRUCTURAL_MATCH` | `ACCEPT / REJECT / NEEDS_DISCUSSION` |
| O8 | Labor province/region aggregation | 103–112, 127–136 | `contracts.py:79–104`; `economics.py:30–46` | scalar legacy case should embed consistently in vector contract | `AUTHORIZED_PYTHON_REDESIGN` | `ACCEPT / REJECT / NEEDS_DISCUSSION` |
| O9 | Generator components and transpose | 155–239, 333–340 | `generator.py:13–57`; `kfe_contract.py:35–41`; `kfe.py:44–46` | backward rows conserve mass; forward is exact transpose | `STRUCTURAL_MATCH` | `ACCEPT / REJECT / NEEDS_DISCUSSION` |
| O10 | Stationary uniqueness/normalization | 337–345 | `kfe.py:49–132` | Python must retain closed-class and residual evidence; arbitrary pin is not inherited | `MATLAB_LEGACY_LIMITATION_NOT_TO_INHERIT` | `ACCEPT / REJECT / NEEDS_DISCUSSION` |
| O11 | Mass/density and aggregate conventions | 341–351, 387–389 | `kfe.py:115–141`; `steady_state.py:241–248` | compare only after shared measure/quadrature definition | `ECONOMICALLY_EQUIVALENT_DIFFERENT_NUMERICS` | `ACCEPT / REJECT / NEEDS_DISCUSSION` |
| O12 | MATLAB line 90 illiquid-income initialization | 81, 90, 111–113 | `economics.py:59–65`; fixture initialization must be separately mapped | determine whether `Rah.*raah` is typo, shortcut, or intended | `POTENTIAL_MATERIAL_MISMATCH_REQUIRES_OWNER_REVIEW` | `ACCEPT / REJECT / NEEDS_DISCUSSION` |

## Future shared-input numerical parity protocol — prepared, not executed

### Authority prerequisites

1. Owner completes O1–O12 and designates dissertation equation locations.
2. Freeze one shared economic object, parameter dictionary, state support, grid orientation adapter, boundary interpretation, productivity law, and mass/density convention.
3. Decide whether the MATLAB external dependencies (`HANK3_FOC`, `HANK3_cost`, labor solver and `la_mat`) are in scope and fingerprint them.
4. Publish a separate execution task with invocation budgets and comparison tolerances. No new tolerance is proposed here.

### Export contract

Both implementations should export immutable, state-indexed data with an explicit `[a,b,z]` canonical adapter:

- grids, parameters, rates, wages/wedges, and initial value;
- converged value function;
- consumption, labor vector, transfer `d`, adjustment cost, `mu_a`, `mu_b`;
- derivative directions, raw/canonical candidate IDs where available;
- boundary feasibility, KKT multipliers/residuals where supported;
- `G_a`, `G_b`, `G_z`, total backward generator summaries, row sums, minimum off-diagonal, and selected boundary/interior rows;
- forward operator identity and stationary mass/density only if the same productivity and measure object is supported;
- quadrature weights, normalization, `A_hh`, and `B_hh`.

### Expected comparison strength

| Object | Future expectation |
|---|---|
| shared input grids/parameters after orientation mapping | exact identity expected |
| budget/drift signs, no-outflow directions, `G^T` relationship | exact structural/directional identity expected |
| value, consumption, labor, transfer, costs and drifts under genuinely identical equations/numerics | tolerance-based numerical equivalence; tolerance requires later authority |
| generator selected rows/rates | exact identity only when discretization is identical; otherwise directional/sign/qualitative equivalence |
| KKT multipliers/candidate IDs | intentionally non-comparable where MATLAB lacks explicit objects; compare feasibility and physical controls instead |
| lower-b F/Z labels | intentionally non-comparable representation; compare canonical physical policy and drift class |
| productivity operator | intentionally non-comparable until Owner chooses one common law; current Python is an authorized redesign |
| stationary distribution and aggregates | tolerance-based only after common generator and mass/density convention; otherwise not comparable |
| Python uniqueness, KKT, canonicalization and audit fields | intentionally absent from legacy MATLAB; must not be removed to force parity |

The later task should compare a predeclared list of interior, lower-bound, upper-bound, upper-a/lower-b, dual-upper, zero-drift, and known near-tie states. Any failure must be fail-closed without tuning.

## Forbidden-operation check

- MATLAB execution: none
- Python/pytest/HJB/KFE/frozen-fixture execution: none
- MATLAB source modification: none
- Python source/test modification: none
- Fixture, parameters, grids, tolerances, equations, FOCs, policy, boundary/KKT, generator or KFE modification: none
- AR(1), transition, IRF, calibration, experiment or Results work: none
- Final MATLAB–Python parity PASS/FAIL claim: none
- Merge, rebase, reset or force-push: none

## Recommended next gate

`CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW`

That gate should record the Owner's O1–O12 decisions and bind dissertation equations before any numerical parity execution or AR(1), transition, or IRF work.
