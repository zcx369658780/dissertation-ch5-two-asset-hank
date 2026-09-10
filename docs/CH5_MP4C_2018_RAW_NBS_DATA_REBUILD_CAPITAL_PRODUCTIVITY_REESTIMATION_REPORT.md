# Chapter 5 MP4C raw-NBS 2018 rebuild, capital and productivity re-estimation

Date: 2026-09-10

## Required answers

1. **Raw years actually available.** GDP has observations for 1992–2022 and 31/31 coverage for 1992–2022; population has observations and 31/31 coverage for 2000–2022; fixed capital formation has observations for 1992–2017 and 31/31 coverage for 1996–2017; depreciation has observations and 31/31 coverage for 1992–2017. Header-only blank years are not called available. Exact header/any/full coverage is in `source_hash_receipt.json`.
2. **Fully same-year 2018 four-source panel:** no. GDP and population are 31/31 in 2018, but the supplied fixed-capital-formation and depreciation files are 0/31 in 2018. No values were filled. Both flows are 31/31 in 2017, so the frozen lagged-flow definitions can still produce K_2018.
3. **Track-A K_2018:** all 31 values are in `corrected_2018_vs_matlab_ledger.csv` and its compact Markdown rendering. 安徽 is `70182.433358881` 亿元.
4. **Track-B diagnostic:** with the same K_2000=I_2000/0.1 initial stock and K_t=K_(t-1)+I_(t-1)-D_(t-1), 安徽 K_2018 is `84616.8` 亿元; Track-A/Track-B is `0.829414884028715`. Across provinces, the largest absolute Track-A/Track-B departure from 1 is `0.286281624762387`. Track B remains diagnostic only.
5. **New 2009–2018 alpha:** `0.738093914686848` (SE `0.0382577480354307`, t `19.2926649525554`, p `7.09401737185008e-55`, R² `0.692493753787364`, N `310`). This pooled OLS uses Track A and 31 provinces × 10 years; the legacy `0.772866243094144` is comparison only.
6. **Same-year Z_2018:** all 31 Track-A and diagnostic Track-B values are in the ledger. 安徽 Track-A Z is `0.0018759632501672073` and Track-B Z is `0.0016340686739896946`. GDP, population and capital are all bound to 2018; capital uses observed 2017 lagged flows by the declared identity.
7. **Versus legacy mixed-year MATLAB:** 安徽 GDP, population, capital and Track-A Z relative differences are respectively `213.040973%`, `-0.897080%`, `207.653399%`, and `192.410443%`. All-province exact values remain in CSV.
8. **安徽 outlier status:** its absolute legacy-relative difference ranks are GDP 6/31, population 31/31, capital 26/31, and Z 7/31 (1 = largest). GDP and Z are in the upper part of the cross-province distribution, but 安徽 is not the largest and capital is not unusually discrepant relative to other provinces. These are descriptive cross-object ranks, not causal evidence; the rebuild does not establish a unique 安徽 anomaly.
9. **Remaining scientific judgment:** yes. The two supplied flow files lack 2018 observations; raw gross fixed capital formation is not the same source route as the accepted canonical fixed-asset-investment calibration; Track-B initial stock is assumed; raw/canonical discrepancies are preserved in the ledger. Owner/Reviewer judgment is required before any production-input promotion.
10. **Model calls:** MATLAB HANK=0; Python household/HJB/KFE=0; firm/wage/migration/capital allocation=0; outer turn=0; steady state/GE/annual/IRF/Results=0.

## Verdict

`RAW_NBS_2018_REBUILD_PARTIAL__SOURCE_COVERAGE_OR_UNIT_AMBIGUITY`

The 31-province panel, both capital paths, pooled-OLS alpha, and same-year 2018 productivity are reproducible. The verdict is PARTIAL because actual 2018 fixed-capital-formation and depreciation observations are absent from the supplied raw files and because the raw GFCF route differs from the accepted canonical investment route. This is calibration evidence only. `Results eligibility = FALSE`.

## Methods and units

- Explicit province mapping: full NBS names to the accepted 31 short names, in the accepted order; recorded in `source_hash_receipt.json`.
- Panel retained: 2000–2018, 31 provinces, 589 rows. Raw GDP/I/D/K use 亿元; raw population uses 万人. Separate model columns use GDP ×1000, population ×100, and capital/flows ×10,000,000.
- Track A: K_2000=I_2000/0.1; for t=2001,…,2018, K_t=(1-0.096)K_(t-1)+I_(t-1). Thus K_2018 consumes I_2000,…,I_2017 and not a fabricated I_2018.
- Track B: same initial stock; K_t=K_(t-1)+I_(t-1)-D_(t-1). It is an observed-depreciation accounting diagnostic, not a production series.
- Alpha: pooled OLS, `log(Y/L) = intercept + trend + alpha*log(K/L) + error`, years 2009–2018, no missing exclusions.
- Z: Y_2018/(K_2018^alpha L_2018^(1-alpha)) using the explicit model-unit columns. No 2020 level enters the corrected object.

## Reconciliation and authority

The canonical workbook was read as an identity-bound comparison object only after its SHA-256 matched `AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`. Canonical comparison values are taken from the accepted 31-province audit ledger tied to that workbook. Raw values were never forced to match it. Detailed classifications appear in `data_quality_flags.csv`.

Live task authority was the exact task named by `project_rules/PROJECT_RULE_INDEX_CURRENT.md`. At execution start, the more general current status/handoff still stated that there was no active task; this documentation lag was retained rather than treated as broader authority.

No raw XLS file was modified or committed. The four files were opened read-only through Excel COM and hashes were fixed before use. No interpolation, forward fill, backward fill, model run, successor task, main merge, or Results publication occurred.

Development execution accounting before candidate publication: 1 successful read-only XLS extraction; 1 earlier PowerShell parser failure before any source workbook opened; 4 deterministic builder/regression runs (4 pooled OLS fits); 4 focused-test process invocations; and 2 Python compile checks. Scientific/model calls remained exactly zero in every attempt.
