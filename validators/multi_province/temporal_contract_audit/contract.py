"""Pure temporal-contract helpers; no model or solver entry points."""

SUPPORTED_II = tuple(range(1, 16))


def annual_mapping(ii):
    if ii not in SUPPORTED_II:
        raise ValueError(f"unsupported ii={ii}")
    steady_year = 2008 + ii
    return {
        "ii": ii,
        "steady_year": steady_year,
        "filename_year": steady_year,
        "plm_vintage": ii + 9,
        "plm_sample_end_year": steady_year,
        "owner_expanding_sample_start_year": 2000,
        "workbook_implied_rolling_sample_start_year": steady_year - 9,
        "current_level_row_1based": ii,
        "current_level_year": 1999 + ii,
        "candidate_level_row_1based": ii + 9,
        "candidate_level_year": steady_year,
        "current_zt_row_1based": 21,
        "current_zt_year": 2020,
        "candidate_zt_row_1based": ii + 9,
        "candidate_zt_year": steady_year,
    }


def expected_plm_sheets(ii, industries=range(1, 5)):
    vintage = annual_mapping(ii)["plm_vintage"]
    return tuple(
        name
        for industry in industries
        for name in (
            f"总面板回归系数_{vintage}_行业{industry}",
            f"总面板回归截距_{vintage}_行业{industry}",
        )
    )


def classify_time_labels(labels):
    time_labels = tuple(x for x in labels if x.startswith("time"))
    if time_labels == tuple(f"time{i}" for i in range(1, 10)):
        return "FIXED_TEN_PERIOD_WINDOW_EVIDENCE"
    return "WINDOW_LENGTH_NOT_DERIVABLE"


def zt_from_levels(gdp, capital, population, alpha):
    if min(gdp, capital, population) <= 0:
        raise ValueError("positive levels required")
    return gdp * capital ** (-alpha) * population ** (alpha - 1)
