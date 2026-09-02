# MP4C latest-R PLM and 2023-capital-lineage audit

## Outcome

The recovered latest `D:\Rprogramme\main.r` is fixed as SHA-256
`18ab62c26ad6bcb201f2bdc38611b920bcef99b6b4c0d6f0f681b3dec4dd72c0`
(170 lines). It confirms the intended aggregate PLM semantics:

- aggregate `for (ind in 4:4)`;
- `GDP_multiplier=1000`, `POP_multiplier=100`, and aggregate capital multiplied
  by the same `GDP_multiplier`;
- `itime=10:24`, ten-row `(itime-9):itime` windows, `time=0:9`, and
  `plm(log(pgdp) ~ 1 + time + log(pcap), model="within")`;
- aggregate capital read from `R语言计算资本存量`.

It does not establish a 2023 capital construction. Its capital preamble creates
24 rows for `2000:2023` but selects only the 23 `CompK_ZJ` values through 2022.
An isolated R 4.6.1 test deterministically stopped with:

```
replacement has 23 rows, data has 24
```

Thus that preamble cannot silently create the stored 2023 row.

## PLM verification status

No PLM reproducibility marker is issued. The authorized R 4.6.1 user library
contains `CHNCapitalStock 0.1.1`, `openxlsx 4.2.8.1`, and `dplyr 1.2.1`, but
does not contain the latest source's required `readxl`, `tidyr`, `plm`, `broom`,
`car`, or `stargazer`. No package installation, update, substitute estimator, or
PLM execution was performed. Therefore neither a PLM match nor a PLM mismatch is
claimed.

## 2023 capital lineage

The existing 2000--2022 acceptance remains unchanged:

`MP4C_STORED_R_CHNCAPITALSTOCK_2000_2022_REPRODUCIBILITY_VERIFIED__2023_EXTENSION_PENDING`.

The exact installed `CompK_ZJ` recurrence is
`K[t] = K[t-1] * (1 - 0.096) + RealInvest[t]`. All 31 stored 2023 capital
values can be diagnostically mapped to an implied real-investment value, but the
current raw workbook has zero numeric provincial 2023 fixed-investment cells and
neither raw nor filled workbook has a price-index/deflator sheet. No later
`main.r`, modified package, or provenance-qualified 2023 input pair was found.

Accordingly:

`MP4C_STORED_R_CHNCAPITALSTOCK_2023_LINEAGE_UNRESOLVED__HANK_RERUN_NOT_AUTHORIZED`.

Interpolation, smoothing, carry-forward prices, extrapolation, and manual fill
were not accepted. The historical workbook was not changed.

## Boundaries and evidence

No MATLAB HANK, Python stationary/household/HJB/KFE, comparator, shock/IRF, R
rolling-PLM, or 8-worker execution occurred. The old-PC `E:/...` literal was
not executed. The verified current source workbooks remain read-only at
`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`.

The no-overwrite external evidence package is:

`D:\ProjectTemp\ch5-mp4c-latest-r-plm-2023-capital-forensics-20260902-001`.

## Exact next gate

A new live task is required after both of the following are made available and
identified without installation or inference:

1. an R 4.6.1-compatible local library containing the exact latest-program PLM
   dependencies, so the copied verifier can reproduce the stored aggregate
   `ind=4` workbook; and
2. a provenance-qualified, same-definition 2023 investment-price/deflator input
   pair or later historical construction source that reproduces the stored
   31-province capital row.

Only after both verification gates, unit/scaling, and all 15 zero-HANK input
preflights pass can the authorized eight-worker batch be considered.
