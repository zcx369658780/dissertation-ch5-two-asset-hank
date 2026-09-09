"""Pure helpers for the zero-model-call provincial data audit."""
import math
import re

UNIT_MULTIPLIERS = {"GDP": 1000, "CAP": 1000, "POP": 100}


def parse_year(value):
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return int(value)
    match = re.search(r"(19|20)\d{2}", str(value or ""))
    return int(match.group()) if match else None


def annual_indices(ii):
    return {
        "analysis_index_matlab_1based": int(ii),
        "output_filename_year": int(ii) + 2008,
        "data_mat_cell_index_matlab_1based": int(ii),
        "data_year_row_matlab_1based": int(ii),
        "workbook_calendar_year_at_data_row": 1999 + int(ii),
        "regression_vintage_key": int(ii) + 9,
    }


def model_consumed_value(variable, workbook_value):
    """Apply the literal loader multiplier recorded in the data contract."""
    return float(workbook_value) * UNIT_MULTIPLIERS[variable]


def classify_fill(raw, filled, observed_before, observed_after):
    raw_missing = raw is None or (isinstance(raw, float) and math.isnan(raw))
    filled_missing = filled is None or (isinstance(filled, float) and math.isnan(filled))
    if raw_missing and not filled_missing:
        return "MISSING_FILLED_INTERIOR" if observed_before and observed_after else "ENDPOINT_OR_EXTRAPOLATION_SUSPECT"
    if raw_missing and filled_missing:
        return "MISSING_UNRESOLVED"
    if not raw_missing and not filled_missing and raw == filled:
        return "OBSERVED_UNCHANGED"
    if not raw_missing and not filled_missing:
        return "CHANGED_MECHANISM_UNRESOLVED"
    return "FILLED_VALUE_MISSING"


def missing_runs(values):
    runs=[]; start=None
    for index, value in enumerate(list(values) + [0]):
        missing=value is None or (isinstance(value,float) and math.isnan(value))
        if missing and start is None: start=index
        if not missing and start is not None:
            runs.append((start,index-1,index-start)); start=None
    return runs
