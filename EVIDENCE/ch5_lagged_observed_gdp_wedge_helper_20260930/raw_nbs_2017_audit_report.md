# 2017 GDP/population read-only reconciliation

Date: 2026-09-30 (Asia/Shanghai). Status: RAW_TO_PRESERVED_PANEL_MATCH__OFFICIAL_VINTAGE_DIFFERENCE_IDENTIFIED.

Owner confirmed the GDP XLS was directly downloaded from NBS provincial annual data and authorized checking for processing mistakes. This is Owner-reported attribution, not an independently established download date or release edition.

## Read-only local check

The two specifically authorized XLS files were parsed as legacy BIFF workbooks using xlrd 2.0.2. The bundled runtime lacked this format reader, so a no-dependency xlrd install was placed only in a task-specific temporary directory, not the model or bundled dependency directories. No Excel automation, workbook save/export, model import or scientific entry occurred.

Files: D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\地区生产总值 亿元.xls and 年末常住人口 万人.xls. Before/after SHA-256 exactly matched the previously bound values 0EA17C78F60054ACCA26D0B56402977E560EE3FF4B220D666A5D0E98178F83E7 and 565B83873D56B8F9770F46BF897452B08A8850A3A954519643C1370188C09CAA.

Both contain worksheet 分省年度数据. The unique 2017 header is column H. Each H5:H35 block contains 31 distinct provinces with positive finite numeric values. GDP and population raw row orders are identical. Province keys match all 31 records in the preserved 2017 panel, whose SHA-256 is 774C357E9762A3DFD76373F3440EA8E1D32F2C23FB1F9CDC31A4D77FC9960A5F.

Across all 31 provinces, each raw GDP and population value equals the corresponding preserved panel value exactly. The panel's legacy GDP x1000 and population x100 fields also equal their stated transformations: 124 comparisons, zero mismatches. This verifies the named fields/year, not investment, capital, other years or the economic validity of legacy model-unit scales. Header/units/footer and all per-province comparisons are preserved in raw_2017_readonly_audit.json. The one successful audit invocation and a later two-cell 2022 GDP spot read were data inspection, not helper tests or model calls. No actual wedge matrix or per-capita output panel was constructed.

## Official comparison and price evidence

The new NBS provincial annual UI was reached through visible navigation, so the previous 403 at the legacy URL did not prevent checking its current replacement:
https://data.stats.gov.cn/dg/website/page.html#/pc/national/fsYearData

Selected path: 国民经济核算 -> 地区生产总值; selected region 北京市. The visible 2017 column and GDP row give 31325.9 亿元. The original XLS H5 and preserved panel give 29883.0 亿元. The same current webpage explicitly notes:

> 按照我国国民经济核算数据修订制度和国际通行做法，在第五次全国经济普查后，对1992年-2023年地区生产总值历史数据进行了系统修订。

This establishes a current revised series and an observed difference. It does not certify the original download edition or prove that every difference is due solely to one revision event.

The official 中国统计年鉴2023 table 3-9 地区生产总值(2022年) was inspected visually:
https://www.stats.gov.cn/sj/ndsj/2023/html/C03-09.jpg

Its explicit note is 本表绝对数按当年价格计算，指数按不变价格计算。 This is direct province-table current-price evidence for that table. The original file does not exactly match even its two checked 2022 records:

| Province/year | Original XLS | Yearbook 2023 table 3-9 | Unit |
|---|---:|---:|---|
| Beijing 2022, C5 | 41540.9 | 41610.9 | 亿元 |
| Tianjin 2022, C6 | 16132.2 | 16311.3 | 亿元 |

Yearbook 2023 national-accounts 简要说明 also explicitly says latest-year values are not final and may change when more financial/administrative data arrive; census and major accounting-method reforms can change historical values. Only those two yearbook province values were checked; no all-province/all-year official-match claim follows.

The official tables support a current-price interpretation of GDP absolute levels, but historical XLS price attribution and release vintage remain formally UNVERIFIED under the previously frozen exact-source gate. Do not set the helper's observed price_verified flag merely from a different-vintage table. Direct download attribution is now confirmed by Owner; price and vintage are separate claims.

## Decision consequence

No processing mismatch was found in the named 2017 raw-to-panel fields. Do not overwrite the old panel with the live revision or treat it as a repaired equivalent source. A choice to retain the frozen historical source with explicitly documented unknown download vintage, or replace it with a newly versioned full source, has to be stated before the integration/scientific comparison. Replacing only lagged GDP with a new statistical vintage while other calibrated inputs remain frozen also needs review for consistency.

Science remains zero this phase. Existing helper/model source unchanged; C9 paused, Objective A retained, old actual ledgers CALL_LEDGER_UNRESOLVED and Results eligibility FALSE. This audit is data evidence only, not nominal-price-source acceptance, annual binding, convergence or formal Results.
