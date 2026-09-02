# MP4C CHNCapitalStock reproduction audit: revised closeout

## Terminal

`MP4C_STORED_R_CHNCAPITALSTOCK_REPRODUCIBILITY_UNRESOLVED__HANK_RERUN_NOT_AUTHORIZED`

## Verified 2000--2022 segment

R 4.6.1 and `CHNCapitalStock` 0.1.1 called `CompK_ZJ(prv, bt=2000)` for all
31 accepted provinces. Compared with the stored candidate sheet, the 23 by 31
matrix has 713 cells, 51 exact cells, maximum absolute difference
`4.94765117764473e-10`, maximum relative difference `4.1882024315552e-15`,
and 36 cells above `1e-10`. These are ordinary Excel floating serialization
differences, not a material discrepancy.

The recovered function initializes 1952 capital as investment divided by 0.1,
normalizes investment price at the requested base year, and recurs with
`K[t]=K[t-1]*(1-delta)+RealInvest[t]`, default `delta=0.096`.

## 2023 blocker

The installed package `asset` data covers 1952--2022 only. Historical
`D:\Rprogramme\main.r` likewise filters its output to 2000--2022. Read-only
search found no later construction source, asset dataset, package copy, or 2023
investment-price/deflator input proving an equal-definition extension. The stored
2023 row cannot prove itself, and reconstructing it would require guessed inputs.

Thus the intermediate finding is
`MP4C_STORED_R_CHNCAPITALSTOCK_2000_2022_REPRODUCIBILITY_VERIFIED__2023_EXTENSION_PENDING`.
No HANK, PLM, MATLAB, Python stationary/household/HJB/KFE, comparator, shock,
IRF, R5, or Results call occurred; the 8-worker batch was not started.
