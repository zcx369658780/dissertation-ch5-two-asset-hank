# Liquid-return and joint-price comparisons

E05/E06 perturb rb around E02 at common rah=.05 and wt19.5. E07-E11 are separately compared with frozen oldD09 and D11; changed axes are explicit. None is a new adaptive model run. The transition flag is preregistered only for the main wage ladder, so it is not extended as a new acceptance criterion here.

| Pair | changed axes | status | delta At | delta Bt | delta b upper | TV a | TV b | transition flag | strict warning |
|---|---|---|---:|---:|---:|---:|---:|---|---|
| E02 -> E05 | rb | UNTESTED_INTERVAL | - | - | - | - | - | NOT_EVALUATED | True |
| E02 -> E06 | rb | UNTESTED_INTERVAL | - | - | - | - | - | NOT_EVALUATED | True |

| Pair | changed axes | status | delta At | delta Bt | delta b upper | TV a | TV b | transition flag | strict warning |
|---|---|---|---:|---:|---:|---:|---:|---|---|
| D09 -> E07 | wt | OBSERVED_CONDITIONAL_DISTRIBUTION_COMPARISON | 0.03783775423 | 0.007207078694 | -0.006111030766 | 0.01731059631 | 0.01349532501 | NOT_APPLIED_OUTSIDE_MAIN_LADDER | True |
| D09 -> E08 | wt | OBSERVED_CONDITIONAL_DISTRIBUTION_COMPARISON | -0.03563651171 | -0.006516924082 | 0.005803237461 | 0.01618802214 | 0.01276922072 | NOT_APPLIED_OUTSIDE_MAIN_LADDER | True |
| D09 -> E09 | rah | OBSERVED_CONDITIONAL_DISTRIBUTION_COMPARISON | 0.4997031093 | -0.0826461116 | -0.02928723182 | 0.181241178 | 0.04611853715 | NOT_APPLIED_OUTSIDE_MAIN_LADDER | True |
| D09 -> E10 | rah, wt | OBSERVED_CONDITIONAL_DISTRIBUTION_COMPARISON | 0.8498567391 | -0.08380046434 | -0.05173150795 | 0.352889089 | 0.09538365013 | NOT_APPLIED_OUTSIDE_MAIN_LADDER | True |
| D09 -> E11 | rah | OBSERVED_CONDITIONAL_DISTRIBUTION_COMPARISON | 1.041946725 | -0.0851766299 | -0.06073892481 | 0.4565199083 | 0.1231247302 | NOT_APPLIED_OUTSIDE_MAIN_LADDER | True |
| D11 -> E07 | rah | OBSERVED_CONDITIONAL_DISTRIBUTION_COMPARISON | -1.037289967 | 0.06600366576 | 0.05715930313 | 0.4534820546 | 0.1188920688 | NOT_APPLIED_OUTSIDE_MAIN_LADDER | True |
| D11 -> E08 | rah, wt | OBSERVED_CONDITIONAL_DISTRIBUTION_COMPARISON | -1.110764233 | 0.05227966298 | 0.06907357135 | 0.4869432603 | 0.1422373209 | NOT_APPLIED_OUTSIDE_MAIN_LADDER | True |
| D11 -> E09 | rah, wt | OBSERVED_CONDITIONAL_DISTRIBUTION_COMPARISON | -0.5754246118 | -0.02384952454 | 0.03398310207 | 0.2899712473 | 0.08476349612 | NOT_APPLIED_OUTSIDE_MAIN_LADDER | True |
| D11 -> E10 | rah | OBSERVED_CONDITIONAL_DISTRIBUTION_COMPARISON | -0.225270982 | -0.02500387728 | 0.01153882594 | 0.130400646 | 0.03549838314 | NOT_APPLIED_OUTSIDE_MAIN_LADDER | True |
| D11 -> E11 | wt | OBSERVED_CONDITIONAL_DISTRIBUTION_COMPARISON | -0.03318099584 | -0.02638004284 | 0.002531409087 | 0.02929427503 | 0.01092086681 | NOT_APPLIED_OUTSIDE_MAIN_LADDER | True |

Multiple-price differences cannot be attributed to a single input. Even single-price contrasts remain conditional on cold initialization, fixed finite grids and source-method densities with stationarity risk; they are not formal economic comparative-static estimates. No new experiment is authorized by this report.
