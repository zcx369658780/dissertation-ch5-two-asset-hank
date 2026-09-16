# CH5 MP4C 2018 KFE D1-D3 Cell 5 liquid-direction switch algebraic attribution

Date: 2026-09-16

Task: `CH5_MP4C_2018_KFE_D123_CELL5_LIQUID_DIRECTION_SWITCH_ALGEBRAIC_ATTRIBUTION_ZERO_SCIENCE_20260916`

## Verdict

`BLOCKED__OWNER_DECISION_REQUIRED_FOR_NEW_INTERIOR_SWITCHING_LAW`

Cell 5 has one finite positive liquid shadow that makes the consumed liquid drift
exactly zero.  Using the persisted Cell 5 inputs,

`q_b* = 0.01250021388291760706054915182349077777...`

is unique and lies strictly between the two raw one-sided derivatives:

`p_b^F = 0.012481806039037598 < q_b* < p_b^B = 0.02256028269097067`.

This is not an averaging or fitted interpolation result.  It is the unique
positive solution of the frozen zero-liquid-drift control equations.  Repository
history contains two genuine precedents for such an object: the MATLAB/source-
faithful `I0` fallback and the accepted Python HJB `Z` candidate constructed by
`_zero_liquid_shadow` and compared through the Hamiltonian.

Those precedents do not, however, uniquely settle the current corrected-target
contract.  The later corrected-HJB design freezes two raw interior finite
differences and derives its root ceiling from the explicit premise that all 720
interior-`b` cells use zero scalar roots.  The isolated corrected selector follows
that premise: it enumerates only backward and forward liquid derivative options
at an interior liquid node and has no `Z` option.  The D1-D3 adoption changes the
boundary law, consumed-drift generator and adjustment-cost KKT, but no accepted
document explicitly says whether the historical/production interior liquid `Z`
law is inherited by this separate corrected target.

The repository therefore contains an authority ambiguity, not permission for the
Builder to add the branch.  Cell 5 proves that a mathematically legal zero-drift
candidate exists and that the two-branch corrected selector is not complete as a
general representation of the repository's historical/production upwind logic.
It does not prove that the candidate is already a frozen D1-D3 corrected-contract
branch.  Adopting it here would select an interior generalized derivative between
the raw one-sided slopes and add an interior root/selection law that the current
corrected one-step budget expressly did not allocate.

## Git identity and publication convention

- Fresh-fetched baseline: `8473a204acdc8e2be2e2d6a405370651400110d0`.
- Branch: `codex/ch5-mp4c-2018-kfe-d123-cell5-liquid-direction-switch-algebraic-attribution-zero-science-20260916`.
- The only changed path is this report.
- Candidate convention: the final candidate SHA is returned after the report-only
  commit, non-force push and remote readback.  A commit cannot embed its own SHA
  without changing that SHA.

The accepted lower-`a` repair candidate `054ba005a351d279f98b243bd2891225872ba86e`
and Cell 5 evidence are unchanged between that candidate and this baseline for all
relevant scientific source and receipt paths.

## Authority and files read

Startup authority was read from the freshly fetched baseline in the required
order:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_LOWER_A_ZERO_KINK_REPAIR_OPTION_A_REEXECUTION_FAIL_CLOSED_ACCEPTANCE_20260916.md`
6. `docs/CH5_MP4C_2018_KFE_D123_LOWER_A_ZERO_KINK_MULTIPLIER_REPAIR_AND_OPTION_A_REEXECUTION_REPORT.md`
7. `reports/ch5_mp4c_2018_kfe_d123_lower_a_zero_kink_option_a_reexecution_20260916/cell_0005.json`
8. `docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_REPORT.md`
9. `docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_ACCEPTANCE.md`
10. the active task named above.

Directly relevant accepted/current authority and source also read:

- `docs/CH5_MP4C_2018_KFE_D123_DIAGNOSTIC_BUNDLE_OWNER_ADOPTION_ACCEPTANCE_20260916.md`
- `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_DIAGNOSTIC_CONTRACT_IMPLEMENTATION_STATIC_VALIDATION_ACCEPTANCE_20260916.md`
- `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_DIAGNOSTIC_CONTRACT_IMPLEMENTATION_STATIC_VALIDATION_REPORT.md`
- `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_ONE_STEP_DESIGN_AND_INPUT_BINDING_REPORT.md`
- `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_OPTION_A_SEED_OWNER_ADOPTION_ACCEPTANCE_20260916.md`
- `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_OPTION_A_SINGLE_POLICY_MAP_DIRECT_STEP_REPORT.md`
- `tasks/CH5_MP4C_2018_KFE_D123_TINY_REAL_CELL_CORRECTED_SELECTOR_PANEL_20260916.md`
- `docs/CH5_MP4C_2018_KFE_D123_TINY_REAL_CELL_CORRECTED_SELECTOR_PANEL_REPORT.md`
- `src/ch5_two_asset_hank/corrected_diagnostic/selector.py`
- `src/ch5_two_asset_hank/policies.py`
- `src/ch5_two_asset_hank/matlab_faithful_policy.py`
- `src/ch5_two_asset_hank/economics.py`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_HJB_DEPENDENCY_CLOSURE_AND_PYTHON_FUNCTIONAL_COVERAGE_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`

Key frozen identities at the fetched baseline are:

| Object | Git blob | SHA-256 |
|---|---|---|
| Cell 5 receipt | `6193cbebb65103afd7c1e308917347ed1a6c598f` | `923894CE813DC3922482FDC428531AC0E157FB4EB42FEFADCACB6446BCD3110F` |
| corrected selector | `489668b3acba566dd0691357f4a7b0be4b606197` | `B76AB0C4DBCDBACC89E863ED936BF7301575FA169EFF63E3E74B9A19F14797DF` |
| accepted Python HJB policy selector | `37bd85c4624bbbafd4ba310805d1c0b8ca08bb24` | `D4B2D56D989113085B0B7DD27155E0B16194224D858C735CCC07019DAB38C24C` |
| source-faithful local policy | `2021db630f3057026ffc37d375a43aaddbccec48` | `09D1FD2007A1F5BBEBA023E239FC8442B37F99A72AED293AB9FFEC6FC9DA0E83` |
| frozen household equations | `810e0875febc873ae85bef7e88edd4de349b00b2` | `191F4A93D35FB5861CA7E9260F59CFACA5B9C5750F26BBEDDAE68FE600CC4009` |

No relevant source or Cell 5 receipt changed after the accepted lower-`a` repair
candidate.  The new main commits are governance/review/task authority for this
attribution.

## Frozen Cell 5 evidence

- F-order flat index: `5`.
- Coordinate `(b_index,a_index,z_index)`: `(5,0,0)`.
- Cell ID: `option_a_f0005_b005_a000_z000`.
- State: `b=-0.1578947368421053`, `a=0`, `z=.8`.
- Effective liquid return: `0.09000000000000001`.
- Effective illiquid return: `.09`.
- Net wage: `12.783312529860462`.
- Transfer income: `.1`.
- `p_a^F=p_a^B=-1.687538997430238e-15`.
- `p_b^F=0.012481806039037598`.
- `p_b^B=0.02256028269097067`.
- Selector outcome: `NO_ADMISSIBLE_POLICY` from 12 candidates, zero admissible
  comparison policies and zero Cell 5 roots.

The two repaired active lower-`a`/zero-kink candidates are identical in their
a-side legal structure and differ only through the liquid shadow branch:

| liquid branch | `q_b` | `l` | `c` | `g_b` | sole rejection |
|---|---:|---:|---:|---:|---|
| forward | `0.012481806039037598` | `0.692762175341232` | `8.950788293751211` | `-0.009203423814039269` | `B_DERIVATIVE_DIRECTION_INCONSISTENT` |
| backward | `0.02256028269097067` | `0.779825780944651` | `6.657753803353461` | `+3.3967923469887262` | `B_DERIVATIVE_DIRECTION_INCONSISTENT` |

Both have `d=0`, `cost=0`, `g_a=0`, a nonempty repaired lower-a multiplier/kink
intersection and the marker
`ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERVAL_CANONICAL_MIN`.  Cell 5 is therefore
not a recurrence of the repaired lower-`a` omission.

## Pure algebra

For the active lower-`a`, zero-kink candidate, all frozen non-liquid objects are
fixed and `d=C(d,a)=g_a=0`.  With `gamma_c=2`, `phi=5` and labor weight one,

```
c(q) = q^(-1/2)
l(q) = (q*w_net)^(1/5)
g_b(q) = w_net*l(q) + r_b_eff*b + T - c(q)
```

where `w_net=12.783312529860462` and

```
m = r_b_eff*b + T
  = 0.085789473684210521421052631578947...
```

Thus

```
g_b(q) = w_net^(6/5) q^(1/5) + m - q^(-1/2).
```

For every `q>0`,

```
g_b'(q) = (w_net^(6/5)/5) q^(-4/5) + (1/2) q^(-3/2) > 0.
```

Also `g_b(q)->-infinity` as `q->0+` and `g_b(q)->+infinity` as
`q->+infinity`.  A unique finite positive zero therefore exists.

For a root calculation that avoids fractional powers, set `ell=l(q)`.  Then
`q=ell^5/w_net`, zero drift requires `c=w_net*ell+m`, and the positive root is
equivalently determined by the monotone algebraic equation

```
(w_net*ell+m)^2 * ell^5 - w_net = 0,
```

with the positive-resource condition.  Independent high-precision Decimal
interval refinement of this polynomial, without importing or calling any
repository selector/root/model routine, gives

```
ell* = 0.69296638844788872911447186732779271547...
q_b* = 0.01250021388291760706054915182349077777...
c*   = 8.94419538990225862044461516003964206147...
```

Substitution using the persisted binary64 arithmetic gives `g_b(q_b*)=0.0`.
The endpoint evaluations reproduce the receipt exactly.  The strict locations
are

```
q_b* - p_b^F = 0.00001840784388000906054915182349077777...
p_b^B - q_b* = 0.01006006880805306293945084817650922223...
```

At this zero, the repaired lower-a kink/multiplier intersection is also nonempty:
its D3 interval is `[0.9*q_b*,1.1*q_b*]`; since `p_a` is slightly negative, the
deterministic minimum would be
`q_a=0.0112501924946258463544942366411417...` and
`lambda_a=0.0112501924946275338934916668791417...`.  This is an algebraic
legality check only, not construction or selection of a new receipt candidate.

## Historical/source-faithful and accepted-Python precedent

The source-faithful path has a genuine third liquid state.  In
`matlab_faithful_policy.py`, the backward liquid candidate is used only when its
drift is negative and the forward candidate only when its drift is positive.
If neither condition holds, the code assigns liquid label `0`, uses the frozen
baseline labor, and sets consumption equal to current liquid resources.  The
resulting liquid drift is zero by construction.  The accepted dependency audit
binds that baseline labor to `lab_solve2` and states that `l0`, `C_0` and the
`Ic_0` branch are scientifically active, not dead initialization code.

The accepted Python HJB path is even more explicit.  `policies.py` defines
`_zero_liquid_shadow`, constructs the liquid drift from the consumption and labor
FOCs, certifies a finite zero, appends the result as derivative direction `Z`,
checks its drift direction and includes it in Hamiltonian selection.  The Owner
structural parity audit keeps the relevant upwind/zero/candidate semantics in the
accepted O2-O12 route and requires future local-HJB comparisons to include
liquid-zero cases.

Cell 5 has exactly the source switching pattern: its backward candidate points
forward and its forward candidate points backward.  The algebraic `q_b*` is the
same type of endogenous zero-liquid shadow represented by those historical and
accepted-Python paths.  It is not a central difference, arithmetic average,
convex-weight rule, derivative floor, drift clipping or tolerance substitution.

## Corrected-target authority conflict

The separate corrected D1-D3 target does not carry this precedent forward
unambiguously:

1. The D1-D3 Owner adoption explicitly changes the finite-box state constraints,
   consumed-total-drift D2 assembly and regularized-cost D3 KKT.  It preserves
   source-faithful/production paths as evidence and does not say that every
   production selector candidate is inherited by the isolated target.
2. The written repair specification requires explicit derivative-branch
   selection, direction consistency and Hamiltonian comparison, but says that
   reference-derived interior controls are not automatically target-optimal.
3. The corrected-HJB design freezes both raw one-sided derivatives at an interior
   liquid node.  Its accepted root budget is derived from the statement that 720
   interior-`b` cells use zero roots; roots are allocated only to liquid-face
   active constraints.
4. The current corrected selector implements that two-branch reading exactly:
   `_interior_options(...,"b",...)` returns only backward and forward, an
   inactive liquid face sets `q_b=p_b`, and scalar-root logic runs only for an
   active liquid face.  Consequently no interior `Z` shadow can enter its
   Hamiltonian comparison.

The older source/production authority therefore proves precedent and mathematical
legality, while the newer corrected-route authority proves that this branch was
not included in the frozen execution design or root accounting.  Neither side may
silently override the other.  Under the active task's explicit ambiguity rule,
the Builder must return the decision to Owner.

## Required-question answers

1. **Should the frozen corrected selector already contain a third branch?**
   Repository HJB history says a third zero-liquid branch is scientifically real,
   but the current corrected-route documents do not uniquely adopt it and instead
   budget interior nodes as root-free.  Therefore the answer is not authority-
   closed; Builder cannot add it.
2. **Does Cell 5 have a unique finite `q_b*`?** Yes.  It is the value above,
   strictly between `p_b^F` and `p_b^B`, with uniqueness proved by strict
   monotonicity.
3. **Is using `q_b*` already authorized?** It is authorized precedent in the
   historical/source-faithful and accepted Python HJB routes, but not uniquely
   bound into the separate D1-D3 corrected selector.  In that target it would be
   a new interior derivative-selection/root law unless Owner explicitly adopts
   the inheritance.
4. **Did the selector omit a mathematically legal frozen-contract branch?** It
   omitted a mathematically legal and repository-precedented branch.  Current
   authority is insufficient to call it a frozen-corrected-contract omission;
   doing so would erase the contrary two-branch/root-budget evidence.
5. **Scope.** The mathematical condition is generic: whenever the liquid drift is
   monotone in the shadow and the two one-sided candidates bracket zero with
   inward-pointing signs, a unique switching shadow can arise.  Only Cell 5 was
   inspected here, so no statement is made about its incidence elsewhere.

## Zero-call ledger

| Operation | Calls |
|---|---:|
| real selector evaluations | 0 |
| synthetic scientific selector evaluations | 0 |
| scalar root invocations | 0 |
| policy maps | 0 |
| D2 assemblies | 0 |
| HJB solves or iterations | 0 |
| KFE | 0 |
| MATLAB | 0 |
| outer / firm / wage-return recalculation | 0 |
| GE / annual / shock / IRF / Results | 0 |
| retries | 0 |

Persisted JSON parsing, source/text inspection, binary/hash verification and
independent Decimal arithmetic were the only computations.  The Decimal interval
refinement evaluated the displayed algebraic polynomial only; it did not import
or invoke the repository scalar-root implementation or any model module.

## Interpretation boundary and next gate

This report establishes a local algebraic root and an authority conflict.  It is
not a new policy receipt, HJB result, selector validation, convergence statement,
KFE/equilibrium result, production change or Results evidence.  Results
eligibility remains `FALSE`.

The one smallest successor route is an independent Reviewer/Owner decision on a
single proposition: **whether the already accepted historical/production
zero-liquid `Z` law is inherited by the isolated D1-D3 corrected selector, with a
revised prospective interior-root budget and exact Hamiltonian/derivative-
interval contract**.  Only after explicit adoption may Reviewer publish a fresh
implementation-and-Option-A-reexecution task.  No successor task is published by
this report.
