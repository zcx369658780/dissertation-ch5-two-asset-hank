# Original KFE pin-row method: separated propositions

| MATLAB334-344 excerpt | fixed core Python | export | conclusion |
|---|---|---|---|
| M=I*J*Nz; AT=A transpose | 32,37 | 654,659 | source row of G becomes column in transposed equations |
| iFix=floor(.37*M) | 25-28,38 | 647-650,660 | 800 gives MATLAB296/Python295 |
| unit replacement row; rhs=.007 | 39-40 | 661-662 | different linear system from original G transpose |
| mldivide of replaced system | 41 | 663 | same static solve role; backend runtime NOT_TESTED |
| normalize raw by sum(raw)*db*dah | 43-45 | 665-667 | unit signed mass normalization does not imply stationarity |
| reshape by MATLAB columns | 47,order=F | 669,order=F | b fastest,then a,then z |
| raw-system residual | 46 | 668 | residual is for replaced matrix, not original G transpose |

Core/export functions have identical ASTs after ignoring source locations; neither was imported or executed.

The following are distinct: (1) source algorithm returned, (2) replaced-system algebra residual small, (3) density integrates to1, (4) original generator is conservative with valid rates, (5) all original G.T@g equations vanish, (6) strict economic stationarity is certified. No one of(1)-(3) certifies(4)-(6). R4 inherited original pin-equation residuals remain nonzero. No alternative solve, clipping, diagonal repair or changed RHS performed.
