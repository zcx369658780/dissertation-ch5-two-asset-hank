# Return and wage bound provenance

| object | source values | classification | evidence |
| --- | ---: | --- | --- |
| firm return bounds | `[.02,.09]` | `EMPIRICAL_NUMERICAL_SAFEGUARD` | `multi_prov_HANK_12sts.m:49-52` contains commented alternatives `.01/.065`; `HANK_firm.m:55` explicitly says the range prevents failure during convergence; `HANK_mp_1eq.m` rejects final return-bound hits. No empirical-rate dataset or period convention is cited. |
| firm wage bounds | `[.8,1.3]` | `SOURCE_VALUE_WITH_UNRESOLVED_ECONOMIC_UNIT` | `multi_prov_HANK_12sts.m:53-55` gives the values and a commented former upper value `1`; `HANK_firm.m` clips and tax-compensates, but inspected source gives no currency, period, deflator, or economic calibration. |

The classification names follow the exact task vocabulary. Historical use does not make either interval structural. Current evidence is `INSUFFICIENT_EVIDENCE` for widening or removing the return clips and supplies no defensible replacement upper bound.
