# Unit-rescaling invariance contract

## Definitions

Let numerical aggregate money quantities transform as `Y'=s_M Y` and `K'=s_M K`, and numerical labor/population as `L'=s_N L`. Parameters `alpha`, `mt`, `delta_firm`, `theta`, `pit`, and `corptau` do not change. Productivity is recomputed from the Cobb-Douglas identity.

| object | source-equivalent form | transformation |
| --- | --- | --- |
| `Z` | `Y/(K^alpha L^(1-alpha))` | `Z'=(s_M/s_N)^(1-alpha) Z` |
| `Y/K` | aggregate output-capital ratio | unchanged under common Y/K money rescaling |
| `Y/L` | output per numerical labor unit | `(s_M/s_N)(Y/L)` |
| `ra_raw` | `mt*alpha*Y/K-delta+PIt*(1-corptau)/K` | unchanged under common Y/K money rescaling; also unchanged by a pure L rescale when Z is recomputed from the identity |
| `w_raw` | `mt*(1-alpha)*Y/L` | `(s_M/s_N)w_raw` |
| household `w` | same per-labor flow unit, if an explicit common mapping exists | must transform by `s_M/s_N`; current source does not define that absolute mapping |

Here `PIt=max(((1-mt)-theta*pit^2/2)Y,0)`, so `PIt/K` is also invariant to common money rescaling of Y and K.

## Direct answers

1. `ra_raw` is invariant to a common numerical money rescaling of Y and K. Changing 亿元 to another common money unit cannot remove the high-return observations.
2. `w_raw` is not numerically invariant when only the money or labor unit changes: it scales as `s_M/s_N`. A common money rescale of Y and K leaves return unchanged but rescales wage unless the wage numeraire is simultaneously remapped. A labor-unit rescale changes wage inversely.
3. Under `MU=10万元` and `NU=100 persons`, one numerical `MU/NU` equals `100,000/100=1,000 yuan per person per model period`. This statement converts the macro ratio only; the protected household source does not state that its grid/flow period and currency numeraire equal this unit.
4. The legacy `[.8,1.3]` wage bounds cannot be compared economically to current raw wages about `7.76–36.39` without an explicit mapping between the legacy household/firm wage numeraire and `MU/NU`. Applying the macro interpretation literally would make the bound `800–1,300 yuan/person/period` and the raw values about `7,764–36,391 yuan/person/period`, but source evidence does not establish that the same period/currency mapping governed the legacy bounds.

No unit mapping is inferred from boundary success or convergence.
