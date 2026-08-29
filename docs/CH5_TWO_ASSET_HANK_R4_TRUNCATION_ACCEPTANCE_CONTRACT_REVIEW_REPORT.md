# CH5 Two-Asset HANK R4 Truncation Acceptance-Contract Review

## Verdict

`PASS`

Primary classification:

`REQUIRE_SELECTOR_NEAR_TIE_CANONICALIZATION_AND_PHYSICAL_EQUIVALENCE`

Acceptance meaning:

`R4_TRUNCATION_ACCEPTANCE_CONTRACT_REVIEWED__IMPLEMENTATION_AND_RERUN_NOT_AUTHORIZED`

This review accepts the diagnosis `TRUNCATION_SENSITIVITY_NEAR_TIE_OR_IDENTIFIER_ONLY`. The consumed failure is classified as a numerical acceptance-contract failure, not evidence of a scientific model failure. R4 steady state remains unaccepted.

## Authority and evidence read

- Live `origin/main`: `fbc927d93b21cb9ff5ced0dce8765689a1109572`
- Consumed-run provenance baseline: `546b88be6316526682c5a02ef4671021d0f387c3`
- Candidate-identity diagnostic report commit: `524690c6ab82b0f42758c48c157406d53863d98e`
- Review workspace: `D:\ProjectTemp\ch5-r4-truncation-contract-review-20260829`
- Initial workspace status: clean

Files read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_TRUNCATION_ACCEPTANCE_CONTRACT_REVIEW.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_COMMON_CORE_CANDIDATE_IDENTITY_DIAGNOSTIC.md`
- `docs/CH5_TWO_ASSET_HANK_R4_COMMON_CORE_CANDIDATE_IDENTITY_DIAGNOSTIC_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_AUTHORIZATION_REPORT.md`
- `src/ch5_two_asset_hank/steady_state.py`
- `src/ch5_two_asset_hank/policies.py`
- `src/ch5_two_asset_hank/boundaries.py`
- `src/ch5_two_asset_hank/contracts.py`
- `src/ch5_two_asset_hank/diagnostics.py`

File written:

- `docs/CH5_TWO_ASSET_HANK_R4_TRUNCATION_ACCEPTANCE_CONTRACT_REVIEW_REPORT.md`

No existing file was changed.

## Accepted diagnosis

The four mismatches among 153 common-core states are accepted as the relevant evidence for contract design:

| State | 25 ID | 29 ID | Shared regime |
|---|---|---|---|
| `(a,b,z)=(0.0,0.0,0.75)` | `FZ` | `FF` | lower `a`, lower `b` |
| `(0.5,0.0,0.5625)` | `BZ` | `BF` | interior `a`, lower `b` |
| `(1.0,0.0,0.5)` | `BZ` | `BF` | upper `a`, lower `b` |
| `(1.0,0.0,0.5625)` | `BZ` | `BF` | upper `a`, lower `b` |

For all four states:

- both identities are constructed and admissible in both solves;
- the boundary regime does not change;
- values and directional derivatives differ at roughly `1e-14`;
- consumption, labor, transfer, adjustment cost, `mu_a`, `mu_b`, feasibility, and KKT quality are machine-equivalent;
- `|mu_b| <= 4.996e-15`, well inside the frozen `1e-12` zero-drift band;
- Hamiltonian gaps are `2.22e-16` to `1.55e-15`;
- raw `lambda_b` differs because `F` and `Z` encode different lower-boundary multiplier representations.

The evidence does not support a material policy, boundary-regime, or candidate-availability difference.

## Alternatives A-D

### A. Keep exact raw identifier equality

Decision: reject.

Raw `candidate_id` is an implementation-level label containing direction and construction history. In the diagnosed states it changes when two admissible, physically equivalent lower-boundary candidates exchange a machine-scale Hamiltonian ranking. Treating this observable label as the scientific object violates the distinction between physical policy and selection representation. Exact equality remains useful as a diagnostic signal, but not as an unconditional acceptance criterion.

### B. Canonical candidate-equivalence classes

Decision: accept only as a narrow, conditional alias rule.

The contract must not declare all `F` and `Z` labels equivalent. A lower-liquid-boundary alias class may be formed only when all of the following hold:

1. the state is at the active lower liquid boundary;
2. the two identifiers have the same illiquid direction/branch;
3. they have the same transfer suffix and transfer-zero disposition;
4. they differ only in the liquid `F` versus `Z` label;
5. both candidates are constructed, admissible, boundary-feasible, and KKT-valid in both compared solves;
6. both selected liquid drifts satisfy `|mu_b| <= 1e-12`;
7. the physical-policy equivalence conditions below pass;
8. the Hamiltonian near-tie rule below passes.

Examples admitted by this design include `FF <-> FZ` and `BF <-> BZ` under those conditions. The design does not alias:

- different illiquid directions;
- different transfer suffixes;
- lower- versus upper-boundary regimes;
- interior versus boundary candidates;
- `F/Z` pairs with economically nonzero liquid drift;
- candidates with different availability, feasibility, or KKT validity;
- materially different controls or drifts.

### C. Physical-policy compatibility contract

Decision: accept as the common-core acceptance layer, with the narrow alias rule applied only where raw IDs differ.

Existing value/control truncation guards remain in force. The replacement contract does not weaken the global `1e-3` normalized-change guard. Instead, it adds a state-level decision:

- If canonical candidate identities are equal, the identity portion passes, subject to all existing global and state feasibility/KKT guards.
- If raw identities differ, the state passes only through the narrow lower-`b` alias exception defined in this report.
- If the alias exception does not pass in full, truncation compatibility fails at that state.

This prevents a broad physical tolerance from silently replacing candidate-selection evidence.

### D. Near-tie canonicalization before selection

Decision: require a future selector-level canonicalization, paired with the physical-equivalence acceptance check.

Changing only `steady_state.py` would make the acceptance check tolerate an unstable selector while leaving policy snapshots and generators dependent on machine-order noise. The selector should return a deterministic canonical representative for a proven near-tie equivalence class. The steady-state comparison should independently verify canonical physical-policy equivalence rather than trusting the label alone.

## Chosen truncation contract

The future common-core contract is layered and fail-closed.

### Layer 1: preserve existing guards

The following remain unchanged:

- HJB convergence and residual requirements;
- KKT residual requirements;
- generator validity requirements;
- the normalized `1e-3` common-core changes for value, consumption, transfer, and labor;
- the frozen `1e-12` drift/zero classification threshold.

Failure of any existing guard remains terminal.

### Layer 2: candidate availability and validity

For each common-core state, the comparison must retain auditable candidate-selection evidence sufficient to establish:

- the selected candidate is constructed and admissible in each solve;
- a raw-ID mismatch is not caused by an unpaired candidate appearing or disappearing;
- boundary feasibility and KKT validity agree;
- the candidate availability difference, if any, is itself only a duplicate representative inside the same proven alias class.

Any material candidate-construction availability switch fails.

### Layer 3: state-level physical-policy equivalence for raw-ID mismatches

For a raw-ID mismatch, define the machine-equivalence bound for a scalar pair `x,y` as:

```text
tau_machine(x,y) = 16 * eps_float64 * max(1, |x|, |y|)
```

Vector labor is checked componentwise with the same definition. The factor 16 provides a bounded allowance for the short floating-point expression chains observed in policy reconstruction; it is approximately machine precision scale, not an economic tolerance.

The following must all hold:

1. consumption is machine-equivalent;
2. every labor component and aggregate labor are machine-equivalent;
3. transfer is machine-equivalent and has the same zero/nonzero/sign disposition under the frozen threshold;
4. adjustment cost is machine-equivalent;
5. `mu_a` is machine-equivalent and has the same `F/B/Z` classification under `1e-12`;
6. `mu_b` is machine-equivalent or both values independently lie inside `[-1e-12,1e-12]` and are canonicalized to `Z`;
7. boundary active-set and feasibility results are identical;
8. both KKT state residuals and every required component remain within the existing `1e-7` contract;
9. the effective shadow prices used by the controls are machine-equivalent;
10. Hamiltonians satisfy the near-tie rule;
11. identifier differences satisfy the narrow alias definition.

The special `mu_b` clause uses the existing zero band rather than requiring machine equality because drift classification, not the last floating-point bit or sign of a value inside that band, is the economic object. It cannot convert an economically nonzero drift into zero because both values must independently satisfy the already-frozen `1e-12` condition.

### Layer 4: auditable output

Any accepted alias must report, state by state:

- raw and canonical IDs;
- coordinates and boundary regime;
- raw controls, drifts, shadow prices, multipliers, KKT components, and Hamiltonians;
- all relevant differences and bounds;
- candidate availability in both solves;
- the precise equivalence rule invoked.

No mismatch may be silently summarized away.

## Multiplier decision

Decision:

`RAW_MULTIPLIER_EQUALITY_NOT_REQUIRED_IF_COMPLEMENTARITY_AND_SHADOW_POLICY_ARE_EQUIVALENT`

At an active lower liquid boundary, `lambda_b` is a dual representation of the state constraint. The `F` construction may retain a positive lower-boundary multiplier while a zero-drift construction incorporates the same effective shadow value into the zero-drift control solution and reports a zero multiplier. Requiring raw `lambda_b` equality would make representation identity, rather than the primal policy and KKT system, the acceptance object.

Raw multipliers may differ only if:

- both are dual-feasible under the existing KKT contract;
- both share the same active lower-boundary state;
- primal feasibility holds;
- complementarity and all KKT residual components pass `1e-7`;
- effective shadow prices are machine-equivalent;
- physical controls and drifts satisfy the equivalence rules;
- neither representation changes the economically meaningful drift classification.

Raw multiplier differences must still be reported. A multiplier sign violation, complementarity failure, effective-shadow difference, active-set difference, or KKT validity difference remains a hard failure.

## Hamiltonian near-tie and canonicalization decision

For two already-admissible, physically equivalent alias candidates with Hamiltonians `H_i,H_j`, define:

```text
tau_H = 16 * eps_float64 * max(1, |H_i|, |H_j|)
near_tie iff |H_i - H_j| <= tau_H
```

This is a derived machine-precision-scaled rule. It does not reuse `1e-7`, `1e-12`, or `1e-3` as a Hamiltonian tolerance, because those would be too broad for ranking. It cannot mask an economically material policy difference because physical-policy, boundary, availability, and KKT equivalence are prerequisites; `tau_H` is applied only after those gates pass.

Within a qualifying lower-`b` near-tie class:

1. canonicalize the liquid direction to `Z` when `|mu_b| <= 1e-12`;
2. preserve the illiquid direction and transfer suffix exactly;
3. if multiple canonical `Z` representatives remain, retain the existing zero-transfer-first rule and then lexical identifier ordering;
4. retain complete raw candidate evidence for audit.

Outside the near-tie class, the larger Hamiltonian wins under the existing deterministic ordering. A candidate with `|mu_b| > 1e-12` must retain its economically meaningful `F` or `B` direction and cannot be rewritten as `Z`.

Canonical `Z` is scientifically preferred inside the zero band because it reflects the frozen drift classification and produces a stable representation for a policy whose liquid drift is economically zero. Preferring `F` would preserve a directional label unsupported by a drift outside the zero band.

## What must still fail

The future contract must fail on any of the following:

- materially different consumption, labor, transfer, cost, `mu_a`, or `mu_b`;
- different economically meaningful drift direction outside the `1e-12` zero band;
- different active boundary regime or feasibility;
- any KKT validity or complementarity failure;
- materially different effective shadow prices;
- candidate construction/admissibility present in only one solve without a proven alias counterpart;
- different illiquid directions or transfer suffixes;
- an `F/Z` pair away from the active lower liquid boundary;
- Hamiltonian separation above `tau_H` for the proposed alias pair;
- failure of existing HJB, generator, KKT, or scalar truncation guards.

## Future implementation surface

A later, separately authorized implementation gate may change only the minimum surface needed to encode this contract:

1. `src/ch5_two_asset_hank/policies.py`
   - add a pure, deterministic near-tie equivalence/canonicalization step before final candidate selection;
   - preserve raw candidate diagnostics needed for audit;
   - do not change candidate construction, economics, tolerances, or admissibility rules.
2. `src/ch5_two_asset_hank/steady_state.py`
   - replace unconditional raw `candidate_id` array equality with a state-level canonical physical-policy compatibility check;
   - retain every existing truncation and downstream stop gate.
3. `src/ch5_two_asset_hank/contracts.py`, only if strictly necessary
   - add immutable diagnostic fields for raw/canonical IDs or candidate-equivalence evidence;
   - do not change economic parameter or policy meanings.
4. Tests explicitly named by the future task
   - add focused unit and bounded integration regressions for the contract.

No future patch under this design may change:

- `1e-12`, `1e-7`, or `1e-3` thresholds;
- grids, fixture values, parameters, equations, transfer mechanism, or policy FOCs;
- boundary economics or KKT definitions;
- generator, KFE, connectivity, recurrent-class, density, or aggregate logic;
- accepted source provenance outside the named minimal files.

## Mandatory regression tests for a future implementation gate

The future gate must require at least:

1. **Observed four-state regression** — the four diagnosed lower-`b` pairs canonicalize to the same `Z`-based identity while retaining raw IDs and passing physical-policy evidence.
2. **Permutation determinism** — reordering otherwise identical candidate construction input does not change the canonical result.
3. **Exact and near tie** — exact equality and gaps at/below `tau_H` choose the canonical `Z` representative.
4. **Outside near tie** — a gap above `tau_H` is not canonicalized; the larger Hamiltonian wins.
5. **Nonzero drift protection** — `|mu_b| > 1e-12` cannot canonicalize to `Z` and retains `F` or `B`.
6. **Material-control failure** — materially different `c`, labor, `d`, cost, or drifts fails even with near-tied Hamiltonians.
7. **Boundary failure** — different active sets or feasibility fails.
8. **KKT failure** — invalid dual sign, complementarity, shadow price, or component residual fails.
9. **Multiplier representation** — raw `lambda_b` may differ only when effective shadow prices, physical policy, feasibility, and KKT quality pass; otherwise fail.
10. **Availability switch** — a genuinely missing candidate or unpaired admissibility switch fails.
11. **Alias-scope protection** — different illiquid direction, transfer suffix, upper-boundary state, or interior state does not enter the lower-`b` alias class.
12. **Existing guard preservation** — HJB residual, generator, KKT, and `1e-3` normalized-change failures remain terminal.
13. **State-level audit output** — every raw-ID mismatch reports raw/canonical IDs, bounds, candidate availability, physical differences, multipliers, KKT, and Hamiltonians.
14. **Bounded 25/29 integration test** — under separately authorized execution, the exact frozen pair reaches the revised compatibility gate and confirms the four aliases without running downstream KFE/connectivity unless that later task explicitly authorizes it.

The implementation gate must use test-first evidence for the pure canonicalization helper and the fail-closed negative cases. Passing these tests is engineering evidence only and does not itself authorize a steady-state rerun or acceptance.

## Interpretation of the consumed failure

Classification:

`NUMERICAL_ACCEPTANCE_CONTRACT_FAILURE__NOT_SCIENTIFIC_MODEL_FAILURE`

The consumed run correctly stopped under its then-current exact-ID rule. The later diagnostic showed that the rule bound acceptance to an unstable representational label at four machine-equivalent lower-boundary states. This does not retroactively turn the consumed run into PASS, does not establish downstream connectivity/KFE/aggregate validity, and does not accept the model. It establishes only that the next blocker should be resolved through a narrowly implemented contract rather than scientific recalibration or policy repair.

## Forbidden-operation check

- Python, pytest, HJB, KFE, steady-state fixture, MATLAB, and numerical models run: none.
- Source, tests, fixture, parameters, tolerances, equations, policy contracts, rules, tasks, or existing reports modified: no.
- Selector canonicalization or alias mapping implemented: no.
- `1e-12` zero-drift threshold changed: no.
- Connectivity, KFE, aggregates, transition solver, AR(1), IRF, Results, or MATLAB-Python parity work: none.
- Repository write: this new report only.

## Recommended next gate

Publish a narrowly scoped implementation task for selector near-tie canonicalization plus the state-level physical-policy truncation compatibility check. It should authorize only the minimal source/test surface named above, require the mandatory regression suite, and stop after bounded compatibility evidence. It must not automatically rerun the consumed steady-state fixture or enter connectivity/KFE/aggregate acceptance.
