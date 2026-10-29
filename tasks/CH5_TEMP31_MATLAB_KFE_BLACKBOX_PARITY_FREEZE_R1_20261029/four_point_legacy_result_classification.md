# Four-point legacy interpretation

| Point | raw/density max difference | normalization difference | original residual | non-pin residual | raw pinned-system residual | strict certified |
|---|---:|---:|---:|---:|---:|---|
| P0 | 0 | 0 | 4.686593832556138 | 1.6518372191536135e-15 | 2.8456122435781354e-17 | FALSE |
| P2 | 0 | 0 | 0.32557163336740258 | 1.0148132334464322e-16 | 1.3064636178450328e-17 | FALSE |
| P4 | 0 | 0 | 3.7634433046985296 | 9.4368957093138306e-16 | 1.4619788669609224e-17 | FALSE |
| P5 | 0 | 0 | 3.4077708099368875 | 1.5569143196891844e-15 | 1.9827347229328662e-17 | FALSE |

Each old HJB convergence fact and old KFE_NOT_CERTIFIED file is retained unchanged. All four source methods returned finite normalized density, with STATIONARITY_WARNING and strict certification FALSE. The source method execution and external strict failure coexist. Only the KFE replay occurred this task; historical HJB convergence is archive metadata, not a new HJB run.
