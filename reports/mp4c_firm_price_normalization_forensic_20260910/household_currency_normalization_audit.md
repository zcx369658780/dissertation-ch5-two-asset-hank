# Household currency-normalization audit

## Source classification

| object | source clues | classification |
| --- | --- | --- |
| liquid asset `b` | grid `[-2,5]`; return income `Rb*b`; aggregate `Bt`; national fiscal term multiplies `Bt*rb*N` | `UNDEFINED_ABSOLUTE_CURRENCY_NORMALIZATION` |
| illiquid asset `a` | grid `[0,10]`; later illiquid drift uses `Rah*a`; aggregate `At`; productive-capital bridge multiplies `At*N` | `UNDEFINED_ABSOLUTE_CURRENCY_NORMALIZATION` |
| consumption `c` | budget uses `(1-tau)wzl + Rb*b + Tt - adjustment cost`; CRRA utility uses the resulting numerical flow | `IMPLIED_RELATIVE_UNIT_ONLY` |
| household wage `w` | initialized at `20`; later replaced by the 31-destination `wage_caculate` composite; appears in the same budget as `c`, `Rb*b`, and `Tt` | `IMPLIED_RELATIVE_UNIT_ONLY` |
| transfer `Tt` | initialized at `.1`; added directly to per-household budget; subtracted without `N` in firm government-income expression | `IMPLIED_RELATIVE_UNIT_ONLY` |
| `AtTax` | `At*rah-integral(a*raah*g)`; therefore a per-household asset-return wedge; added without `N` to aggregate-looking firm fiscal terms | `IMPLIED_RELATIVE_UNIT_ONLY` |

No inspected source declares a yuan value, price deflator, calendar-period conversion, or macro-unit coefficient for one grid unit of `a`, `b`, or the linked flow objects. Hence none qualifies as `SOURCE_DEFINED_UNIT` in an absolute-currency sense.

## Budget and aggregation trace

`HANK_2ASSETS_HJB.m:46-60` creates numerical grids. Its literal initialization income at `:81-90` first fills `Rah` with the tapered return vector `raah`, then computes `tempMat=Rah.*raah+Rb.*bbb+Tt`; this is return-times-return, not return-times-asset. Later expressions at `:193-194` and `:263-264` use `Rah.*aaah` in illiquid drift, while `w`, `Tt`, `b`, consumption, and adjustment cost share an internally relative budget numeraire. The forensic records this literal inconsistency and does not repair or reinterpret it. Lines `:347-365` integrate labor, assets, consumption, and `AtTax` over the normalized density. `HANK_mp_1turn.m:31,36,65` multiplies `At` and `Bt` by `N` in some macro paths, while `HANK_firm.m:89,95` multiplies `Ct` by N but adds `AtTax` and subtracts `Tt` without N in `Govinc`. This does not furnish a coherent absolute currency mapping.

The source also distinguishes firm `wjt` from household `w`: `wjt` enters migration/allocation formulas, while `wage_caculate.m:8-11` sums over 31 destinations and applies a nonlinear power before storing household `w`. The unnormalized destination sum can mechanically make `w` much larger than one firm wage. Thus legacy `wjt=.6` and `w=20` can coexist as numerical relative scales, but the inspected source does not prove they share one absolute currency unit. Conclusion: `HOUSEHOLD_CURRENCY_NORMALIZATION_UNRESOLVED`.
