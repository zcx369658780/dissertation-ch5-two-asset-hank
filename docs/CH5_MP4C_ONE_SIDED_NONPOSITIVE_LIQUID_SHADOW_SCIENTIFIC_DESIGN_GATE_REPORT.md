# CH5 MP4C one-sided / nonpositive liquid-shadow scientific design gate

Date: 2026-09-21

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Baseline: `a5519fccb8276b6c7db1de16d4c05abf13efd73f`

## Terminal

`PASS__ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_DESIGN_GATE__EXTENSION_NOT_SCIENTIFICALLY_JUSTIFIED__PRESERVE_CURRENT_FAIL_CLOSED_RECOMMENDED__NO_IMPLEMENTATION`

Classification:

`EXTENSION_SCIENTIFICALLY_UNJUSTIFIED__CURRENT_FAIL_CLOSED_RECOMMENDED`

No generic extension law is proposed. No selector implementation, CURRENT edit, model run, or successor publication was performed.

## Authority conclusion

The existing liquid-`Z` law is a local derivative-selection law. It selects a zero-liquid-drift shadow from the closed interval spanned by the backward and forward raw liquid derivatives, after imposing `q_b=c^{-gamma}>0`. D3/KKT branch feasibility answers whether controls are internally coherent for an assumed shadow. It does not create a value-function derivative and therefore does not enlarge the viscosity/upwind derivative-selection domain.

When one raw liquid derivative is nonpositive and the other is positive, the raw hull is `[p^-,p^+]` and its consumption-domain intersection is `(0,p^+]`. The nonpositive endpoint is unusable as a consumption shadow and is evidence of local transient non-monotonicity. It does not support extrapolating beyond `p^+`.

## F0063 algebra

For 黑龙江 checkpoint 3 / flat 63:

- raw liquid hull: `[-0.0002428532863339202, 0.014463823441006161]`;
- positive-domain intersection: `(0, 0.014463823441006161]`;
- positive-transfer / forward-`a` liquid drift at the sole positive endpoint: `-1.5960747263712167`;
- D3 positive-transfer feasibility interval: `[0.014463823441006161, 0.022217644565431547]`.

On the positive-transfer branch with fixed `q_a`,

`d'(q_b)=-a q_a/(2 q_b^2)<0`

and the D3 equality gives `1+C_d=q_a/q_b>0`. Hence

`g_b'(q_b)=w l/(phi q_b)+(1/gamma)q_b^(-1/gamma-1)-d'(1+C_d)>0`.

The drift is strictly increasing. Since it is still negative at the largest positive raw derivative, no zero-liquid root exists anywhere in the positive derivative hull.

The unique diagnostic root is:

- `q_b=0.01801822665826406`;
- `q_a=0.024439409021974706`;
- `d=0.2023985483449149`;
- `g_b=-3.95516952522712e-16`;
- `g_a=0.6931065423365061`;
- D3/KKT residual `0`;
- gap above the sole positive derivative `0.0035544032172578986`.

It is coherent control algebra inside the D3 branch-feasibility interval, but it is outside the local derivative hull. Repository authority supplies no monotonicity, consistency, superdifferential, or subdifferential argument that identifies this extrapolated co-state with a viscosity derivative.

## Design comparison

| Design | F0063 result | Scientific judgment |
|---|---|---|
| 0. Current two-positive-shadow law | Fail closed | Recommended |
| 1. Positive derivative-hull restriction | No root | Coherent; creates no new candidate |
| 2. D3 branch-feasibility extrapolation | Contains the diagnostic root | Rejected: control feasibility is not derivative-selection authority |
| 3. Historical `1e-6` derivative floor | Changes the derivative domain | Non-authoritative comparator; not recommended |

The rejection of Design 2 does not depend on how frequently mixed-sign derivatives occur. Frequency cannot supply the missing viscosity/upwind consistency argument.

## Persisted sign-census audit

The exact requested 408-map and 101-map raw-sign censuses cannot be computed from persisted evidence without violating this task's zero-science boundary.

| Evidence set | Complete maps | Derivative receipts | Numeric raw derivative arrays | Complete-map cell JSON |
|---|---:|---:|---:|---:|
| accepted turn1 | 408 | 408 | 0 | 0 |
| turn2 run004 | 101 | 101 complete-map receipts | 0 | 0 |

Each `derivative_receipt.json` stores only the four derivative-field SHA-256 values. The persisted NPZ files contain value/policy/operator fields, not raw derivatives. Successful checkpoint compaction explicitly deletes `cell_*.json`. Reconstructing derivatives from persisted `value` would be a forbidden derivative recomputation from `V`.

The evidence root includes a 509-row province/checkpoint availability table. Terminal/final checkpoints are marked where a province terminal receipt exists; every raw-sign count is `UNAVAILABLE__RAW_DERIVATIVE_VALUES_COMPACTED_AWAY`.

This is a material evidence limitation. No counts were inferred from selected `q_b`, derivative hashes, or recomputed finite differences.

## Available failed-map prefix census

The failed 黑龙江 checkpoint retains cells 0 through 63. This is the only persisted map segment containing numeric raw derivatives.

Interior-liquid counts among the 57 persisted interior cells are:

| Pattern | Count |
|---|---:|
| `(+,+)` | 55 |
| `(<=0,+)` | 1 |
| `(+,<=0)` | 1 |
| `(<=0,<=0)` | 0 |

The seven persisted active liquid-face cells are all `(+,+)`. The first mixed-sign occurrence in this prefix is flat 62.

## Cross-cell falsification panel

The complete set of persisted mixed-sign cell JSONs contains two cells.

| Cell | Pattern | Current outcome | Positive-endpoint drift | Extrapolated positive root | Result |
|---|---|---|---:|---:|---|
| F0062 | `(+,<=0)` | `SELECTED_ADMISSIBLE` | `-1.5874998202934136` | `0.018102906378381266` | Existing ordinary positive endpoint is already admissible; extension is unnecessary |
| F0063 | `(<=0,+)` | `NO_ADMISSIBLE_POLICY` | `-1.5960747263712167` | `0.01801822665826406` | Root exists only beyond the positive derivative; extension lacks derivative-selection authority |

Both extrapolated roots are finite, positive-transfer, forward-`a` coherent, and D3/KKT exact by construction. That common control coherence does not cure the derivative-domain defect. F0062 also shows that the mere mixed-sign trigger would create an unnecessary candidate unless precedence suppresses it after an ordinary admissible policy, making Design 2 dependent on selector outcome rather than a standalone derivative law.

## Viscosity/upwind judgment

The current law's closed derivative hull has a direct local interpretation: it uses only slopes supplied by the discrete value function. Intersecting this hull with `q_b>0` preserves that interpretation. Extending above the only positive slope replaces local derivative selection with a new co-state extrapolation.

The nonpositive slope may be treated as unusable for consumption and as a transient non-monotonicity signal. Zero is a domain boundary, not an observed positive derivative. Nothing in the accepted D1-D3, interior-`a`, joint-switching, or nonlinear HJB authority supplies a consistent extrapolation operator or a convergence argument for Design 2. No general viscosity theorem is claimed here.

## Zero-science ledger

- persisted complete-map metadata reads: 509
- persisted cell JSON loads: 64
- independent scalar root diagnostics: 2
- production selector/root helper calls: 0 / 0
- derivative recomputation from `V`: 0
- HJB/direct update, D2/Q, KFE/SVD, aggregate/integration: all 0
- turn2 replay/rerun, turn3, MATLAB, GE/Results, retry/tuning: all 0

Focused validator tests: `4 passed`.

## Evidence

Evidence root:

`reports/ch5_mp4c_one_sided_nonpositive_liquid_shadow_scientific_design_gate_20260921_run001/`

The sealed manifest and independent readback are stored in that root. The complete-map census limitation is separately machine-readable and is not hidden by the scientific rejection classification.
