# CH5 MP4C 2018 corrected household fixed-point aggregate and adapter binding acceptance

Date: 2026-09-20

Reviewer verdict:

`PASS__CORRECTED_HOUSEHOLD_FIXED_POINT_AGGREGATES_AND_ATTAX_BOUND__OPT_IN_ADAPTER_ACCEPTED__OWNER_PAYOFF_RETURN_FREEZE_REQUIRED`

## Accepted candidate

- live main before Builder task: `ee81460b69652038e8807b12c7d3016b4f274d97`
- implementation-freeze commit: `7ce7182bf4567ca3a458e632cdf9c4fac88f0cb5`
- Builder candidate: `5830285db591c448cacffd8a7b28635bbcef2f54`
- candidate tree: `531a816563babdb57b53fd3d18510ebd352eb61c`
- ancestry: exactly `2 ahead / 0 behind`
- changed files: `16`
- CURRENT files changed by Builder: `0`
- default source-faithful household / one-turn / stationary route blobs: unchanged
- scientific solver/model retries: `0`.

## Exact accepted input binding

The task correctly re-bound the accepted checkpoint-11 household fixed point and terminal mass:

- V11 `A097A3DDA767B979224638A51CEDC53EA635687CCDEFBE190FED0B899606921F`
- P11 `89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3`
- u11 `2E9A077FFA809F2DECEE385FD9E7F50C03E16750C2A074F990C0F3CBCC212648`
- Q11 `33367258F3EADB1482D4A5CB30A64A8574830C993B0E5280C451499CBD6913AD`
- checkpoint identity `8093BE714CA83531816B20DFEB2BAB3DCB7AF9B971AD255C3596C1CA2A9E2A3B`
- stationary mass artifact `1DD70201EAC5EED0AE768362D99A76736276BFB4D5E6AF0D8DBDB4E9D6FE7D16`
- p `E215FAE862DA81AD6DEB603859709EA0CF73B8F6F1897567DF942B186CD65ED7`
- g `D02592257722313B81C7A1DB40B799ADED8E8BDB5100A65C469E0997DA22E1CE`.

The predecessor policy and terminal-mass manifests were fully read back with zero mismatches. The accepted state contract remains F-order `(b,a,z)`, b fastest, with `omega=70/361`.

The maximum elementwise `|p-omega*g|` is `3.469446951953614e-18`, below the prospectively frozen bound `1.7807977314990681e-13`. No second density normalization occurred.

## Independent source-law confirmation

Reviewer independently re-read the designated protected MATLAB source object with SHA-256

`049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`.

The source lines independently confirm:

- line 81: `raah = rah.*(1 - 0.1*(ahmax./ah).^(-9));`
- line 347: `Lt = sum(zzz.*l.*g*dah*db , 'all');`
- line 348: `Bt = sum(bbb.*g*dah*db , 'all');`
- line 351: `Aht = sum(aaah.*g*dah*db, 'all');`
- line 354: `Ct = sum(C.*g*dah*db, 'all');`
- line 365: `AhTax = Aht*rah - sum(aaah.*raah.*g*dah*db, 'all');`.

The Builder mapping of accepted `effective_r_a` to the source tapered `raah` is algebraically exact for the accepted grid.

AtTax is therefore accepted as the aggregate illiquid-return-flow gap between the uniform source `rah` and the household-used state-dependent tapered illiquid return. This closes the existing `FrozenHouseholdOutputs.AtTax` interface field without introducing a new K1 payoff-return law.

The source does not itself establish an external calendar or currency price numeraire for this rate-like flow. The adapter's "per model period / relative asset-flow" wording is accepted as an internal model-unit description only, not as an annual-return identification.

## Accepted aggregate fixture

Exactly one deterministic post-processing evaluation was performed.

| Output | Mass form | Density form | Abs. difference |
|---|---:|---:|---:|
| Ct | `11.72504598498222` | `11.725045984982218` | `1.7763568394002505e-15` |
| Lt | `0.6881256647265093` | `0.6881256647265092` | `1.1102230246251565e-16` |
| At | `9.210552290174773` | `9.210552290174773` | `0` |
| Bt | `1.6622560718337767` | `1.6622560718337767` | `0` |
| total assets | `10.87280836200855` | `10.87280836200855` | `0` |
| AtTax | `0.05117497248083413` | `0.05117497248083419` | `6.245004513516506e-17` |

Every difference is below its prospective binary64 aggregation bound.

The source aggregation semantics are accepted:

- `Ct=sum(C*p)`
- `Lt=sum(z*l*p)`
- `At=sum(a*p)`
- `Bt=sum(b*p)`
- total assets = `At+Bt`
- `AtTax=At*rah-sum(a*effective_r_a*p)`.

No `dz`, trapezoid, endpoint weighting or extra density normalization is allowed.

## Adapter acceptance

The new opt-in module

`src/ch5_two_asset_hank/multi_province/corrected_household_adapter.py`

is accepted as an interface/fixture adapter only.

It:

- requires explicit arrays, grids, omega and return inputs;
- performs deterministic reductions only;
- exposes the existing `FrozenHouseholdOutputs` contract explicitly;
- contains no household/KFE/firm/outer solver entry point;
- does not change the default source-faithful route.

Focused tests: `33/33` PASS. `py_compile` and `git diff --check` pass.

The fixture field `convergence_statistic=B11` is representational only. It must not replace the frozen scientific HJB convergence law, which remains the conjunction `B<=1e-8 AND D<=1e-7` with exact checkpoint provenance.

## Evidence acceptance

Evidence root:

`reports/ch5_mp4c_2018_corrected_household_fixed_point_aggregate_and_adapter_binding_20260920_run001/`

Sealed manifest:

`0FF6C22FC4C7A8D67119EA477A9BF1E125413F9AE0882B5B064BF1124A7EE3A6`

with 11 entries and 13,955 bytes. Readback bad count is zero.

Scientific ledger is accepted:

- aggregate post-processing evaluations: 1
- HJB / KFE / SVD / eigen / policy / selector / root / Q / D2: 0
- firm / price / allocation / outer / MATLAB / GE / annual / shock / IRF / welfare / Results: 0
- scientific retries: 0.

## Route consequence

The corrected fixed-price household object now has all of the following accepted together:

1. HJB convergence;
2. same-Q source-free unique stationary mass;
3. exact source stationary aggregates;
4. exact AtTax mapping;
5. an opt-in multi-province output adapter fixture.

The household numerical/interface gate is therefore no longer the active blocker.

The next blocker is substantive scientific authority already identified by the accepted K1A payoff-return re-audit:

`CLIPPED_RA_REMAINS_ONLY_TRANSITIONAL_BRIDGE__RAW_RA0_IS_SOURCE_CONSISTENT_CANDIDATE_REQUIRING_OWNER_PERIOD_NUMERAIRE_FREEZE`.

No successor Builder science task is published from this acceptance. Owner must explicitly adopt the payoff-return period/numeraire contract before runtime payoff-law change, K1B execution or a new corrected-household outer trajectory.

Results eligibility remains `FALSE`.
