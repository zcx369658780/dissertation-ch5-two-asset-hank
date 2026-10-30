# Per-point source and stationarity warnings

| Point | HJB converged | first homecrit exceed | source KFE | original residual | pin-row295 residual | other799 max | strict |
|---|---|---|---|---:|---:|---:|---|
| E00 | True | None | True | 0.32506016464408599 | -0.32506016464408599 | 7.9053584967243851e-17 | False |
| E01 | False | None | False | - | - | - | NOT_EVALUATED |
| E02 | False | None | False | - | - | - | NOT_EVALUATED |
| E03 | True | None | True | 0.32169695841610524 | -0.32169695841610524 | 1.2490009027033011e-16 | False |
| E04 | True | None | True | 2.9445205842114848 | -2.9445205842114848 | 7.4969676122580872e-16 | False |
| E05 | False | None | False | - | - | - | NOT_EVALUATED |
| E06 | True | None | True | 0.31937903435241144 | -0.31937903435241144 | 1.2511693070482721e-16 | False |
| E07 | True | None | True | 0.49309206680405065 | -0.49309206680405065 | 3.0184188481996443e-16 | False |
| E08 | True | None | True | 0.49063309282561246 | -0.49063309282561246 | 2.3071822230491534e-16 | False |
| E09 | True | None | True | 0.60013744561092452 | -0.60013744561092452 | 1.7715863498413142e-16 | False |
| E10 | True | None | True | 0.67791825508255843 | -0.67791825508255843 | 3.2786273695961654e-16 | False |
| E11 | True | None | True | 0.74928528259194072 | -0.74928528259194072 | 3.3848791824997448e-16 | False |

The fixed solver is unchanged. Python external observation does not implement the original MATLAB internal homecrit STOP; trajectories after a breach are source-parity warnings, not proven MATLAB-equivalent continuations. Post-operator row sums, mass/negative-mass, raw and normalized pinned-system residuals and stale-policy implicit consistency remain distinct from original stationarity and full nonlinear Bellman optimality (NOT_EVALUATED). No density or operator repair.
