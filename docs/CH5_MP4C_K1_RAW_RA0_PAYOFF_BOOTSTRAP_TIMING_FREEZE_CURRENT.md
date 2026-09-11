# Chapter 5 MP4C K1 raw-ra0 payoff bootstrap/timing freeze

Date: 2026-09-12.
Status: `OWNER_APPROVED_COMMON_TURN1_CLIPPED_RA_BOOTSTRAP__RAW_RA0_PAYOFF_FROM_TURN2`.

This document records the Owner-approved initialization/timing convention required to execute the raw-`ra0` household payoff runtime-safety diagnostic.

## 1. Motivation

The accepted corrected-2018 initialization contains `ra`, `rah`, and `rk` for all 31 provinces but contains no provenance-bound prior-completed `ra0`. A completed firm turn does persist raw `ra0` into the next state. Therefore a raw-payoff experiment cannot truthfully use prior-completed `ra0` on its first allocation when starting from the accepted initialization.

The earlier safety task correctly stopped before runtime rather than inventing a raw return source.

## 2. Owner-approved bootstrap rule

Both Control and Raw paths start from the same accepted initialization and use the same entering clipped/source-used `ra` for turn 1.

Turn 1 is therefore a **common bootstrap turn**:

- Control C payoff source: entering source-used/clipped `ra`;
- Raw R payoff source: entering source-used/clipped `ra`;
- both use the same accepted K1 destination-by-origin `S` for quantity allocation and payoff aggregation;
- both otherwise have byte-identical scientific inputs and runtime settings.

After turn 1 completes, each path has a provenance-safe completed firm raw-return vector `ra0^(1)` and used/clipped `ra^(1)`.

From turn 2 onward:

- Control C continues to use prior-completed source-used/clipped `ra` as the payoff source;
- Raw R switches to prior-completed raw `ra0` as the payoff source;
- Raw payoff is `rah_i = sum_j S[j,i] * ra0_j` using the same `S` as private-capital quantities.

No same-turn feedback is allowed.

## 3. Counting and comparison semantics

The bounded safety diagnostic may run each path for at most 5 completed outer turns in total.

- turn 1: common bootstrap; no raw-vs-control household-payoff treatment difference is expected or claimed;
- turns 2-5: treatment horizon, at most 4 completed turns in which Raw R uses raw `ra0` while Control C uses clipped/source-used `ra`.

Any C/R payoff, household, HJB, control, drift, firm or convergence comparison intended to measure the raw-payoff treatment must report turn 1 separately and focus causal/mechanism descriptions on turns 2-5.

Turn 2 is the first authorized household iteration in which the raw-payoff treatment can enter.

## 4. Provenance requirement

For each Raw treatment turn `n >= 2`, the payoff source must be exactly the completed firm raw-return vector from turn `n-1` of the same Raw path.

The persisted evidence must prove:

`ra0^(n-1)_destination @ S^(n)_destination_origin = entering/active raw portfolio payoff for turn n`

subject to the route's existing allocation/household timing convention.

The Control path must analogously prove its prior-completed used-`ra` provenance.

No cross-path borrowing of return vectors is authorized after turn 1.

## 5. Scientific boundary

This bootstrap convention solves only the missing-initial-raw-return provenance problem. It does not alter the Owner-approved payoff contract:

- final K1 payoff source object remains raw `ra0`;
- raw `ra0` remains `MODEL_TIME_RETURN_RATE__CALENDAR_PERIOD_UNRESOLVED`;
- numeraire remains `INTERNAL_MODEL_PRODUCTIVE_CAPITAL_RETURN_NUMERAIRE__EXTERNAL_MARKET_MAPPING_UNRESOLVED`;
- `[.02,.09]` remains `EMPIRICAL_NUMERICAL_SAFEGUARD`, not an economic payoff interval.

The common turn-1 clipped bootstrap is an initialization convention only. It must not be interpreted as retaining clipped `ra` as the final K1 payoff law.

## 6. Other frozen objects

Unchanged:

- K1 pure-geographic benchmark `beta_distance=2`;
- `beta_return=0` for this safety task;
- fixed `theta_i=inter_prv_ratio_i`;
- source-faithful labor;
- C1 `GovInv=max(Ktarget-Kprivate,0)`;
- no smoothing/partial adjustment;
- firm/HJB/KFE equations;
- calibration, bounds, grids, tolerances and solver semantics.

K1B remains runtime-unauthorized. K2 remains unauthorized. Corrected-2018 KFE remains `DIAGNOSTIC_ONLY`. Results eligibility remains `FALSE`.
