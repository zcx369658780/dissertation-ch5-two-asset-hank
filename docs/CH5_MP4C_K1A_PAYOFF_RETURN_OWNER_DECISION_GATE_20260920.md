# CH5 MP4C K1A payoff-return Owner decision gate

Date: 2026-09-20

Status: `OWNER_SCIENTIFIC_DECISION_REQUIRED__NO_RUNTIME_AUTHORIZED`

This gate does not add a new Builder task. It summarizes the already accepted payoff-return evidence now that the corrected household HJB-KFE and aggregate-interface route is closed.

## Controlling accepted evidence

The accepted K1A re-audit classifies:

`CLIPPED_RA_REMAINS_ONLY_TRANSITIONAL_BRIDGE__RAW_RA0_IS_SOURCE_CONSISTENT_CANDIDATE_REQUIRING_OWNER_PERIOD_NUMERAIRE_FREEZE`.

Source identity:

`ra0 = rk + after_tax_profit_over_K - delta`

with firm depreciation deduction approximately `.025`.

Source-used `ra` is `ra0` clipped to `[.02,.09]`.

Accepted bounded K1A evidence:

- equal-share upper clips: `754/775`
- geographic beta=2 upper clips: `755/775`
- lower clips: zero
- raw `ra0` median about `.2631`
- raw maximum about `1.12`
- used `ra` median `.09`
- 30 provinces are upper-clipped in all 25 turns
- static same-S raw-minus-clipped household payoff difference has median about `.172` and maximum about `.95`.

Thus the clip is a historical numerical safeguard that destroys most cross-province payoff dispersion. It is not accepted as an economically identified return interval.

## Existing authorities that must not be conflated

- K1B attractiveness signal is separately preregistered as completed-iteration raw-unclipped `ra0` cross-sectional z-score.
- `beta_return=0.5` is preregistered for K1B attractiveness only.
- attractiveness score is not household payoff return.
- current clipped/used `ra` may be described only as a transitional source-faithful payoff bridge.
- no accepted source supports an arbitrary transformed/expected payoff return.
- current source evidence does not prove that the rate period is annual, quarterly or another calendar unit.
- corrected macro data are annual, but data frequency alone does not identify the HJB return period.

## Owner choice required

### Option A — retain clipped used ra as final household payoff

This preserves current runtime behavior but would elevate the historical `[.02,.09]` numerical safeguard into economic payoff authority.

Current evidence does not identify that elevation. Adopting Option A would therefore be a new substantive scientific assumption.

### Option B — adopt raw net ra0 as household payoff candidate

This is the strongest source-consistent economic candidate because it is the pre-clip firm net return object and preserves province return dispersion.

Owner must additionally freeze:

1. model-period interpretation for the rate-like object;
2. numeraire interpretation;
3. whether raw `ra0` enters the household directly with no annualization, rescaling, clipping, smoothing or risk adjustment.

If adopted, the next task must be a narrowly bounded runtime-safety diagnostic before K1B or a long outer trajectory. It may not tune the payoff transform based on convergence.

### Option C — transformed / expected / risk-adjusted payoff

No current source-backed transformation has authority. Choosing this route requires a new scientific contract and calibration/estimation basis before implementation.

## Reviewer recommendation for Owner consideration

The evidence favors Option B as the source-consistent successor **provided the Owner explicitly adopts the unresolved period/numeraire convention**.

A minimal, auditable freeze would state:

- household illiquid payoff object = completed-iteration raw net firm return `ra0`;
- no `.02/.09` clipping in the economic payoff object;
- no extra annualization, rescaling, smoothing or risk adjustment unless separately justified;
- K1 quantity/return aggregation continues to use the same portfolio matrix S;
- lagged completed-iteration timing remains unchanged;
- K1B attractiveness remains a separate z-scored raw-`ra0` signal and does not replace payoff levels.

The phrase "one model-period return" is source-compatible. Mapping that model period to a calendar year is **not** established by the current source evidence and remains an Owner interpretation.

No runtime is authorized until Owner explicitly adopts a contract.
