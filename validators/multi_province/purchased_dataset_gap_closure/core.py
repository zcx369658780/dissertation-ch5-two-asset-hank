"""Pure helpers for the purchased-dataset gap-closure audit.

The module has no model, solver, estimation, or purchased-file entry point.
"""

from __future__ import annotations

from collections.abc import Mapping


CITY_SUM_REQUIREMENTS = (
    "additive_absolute_levels",
    "complete_exact_once_coverage",
    "boundary_changes_reconciled",
    "no_province_residual_omitted",
    "unit_and_scope_consistent",
    "documentation_supports_aggregation",
)


def excel_column(number: int) -> str:
    """Return the one-based Excel column label."""
    if number < 1:
        raise ValueError("Excel columns are one-based")
    label = ""
    while number:
        number, remainder = divmod(number - 1, 26)
        label = chr(65 + remainder) + label
    return label


def city_sum_is_authorized(requirements: Mapping[str, bool]) -> bool:
    """Require affirmative evidence for every task-defined aggregation gate."""
    return all(requirements.get(name) is True for name in CITY_SUM_REQUIREMENTS)


def classify_secondary_value(
    value: float,
    *,
    provisional: float,
    preliminary_official: float,
    traceable_official: bool = False,
    revised_vintage: bool = False,
) -> str:
    """Classify agreement separately from authority and revision evidence."""
    if value == provisional and traceable_official and revised_vintage:
        return "SECONDARY_SUPPORTS_REVISED_OFFICIAL_VINTAGE"
    if value == provisional:
        return "SECONDARY_MATCHES_PROVISIONAL"
    if value == preliminary_official:
        return "SECONDARY_MATCHES_PRELIMINARY_OFFICIAL"
    return "SECONDARY_VALUE_DIFFERS"


def stable_complete_panel(year_city_sets: Mapping[int, set[str]], years: range) -> bool:
    """Check exact city-set stability over a requested year interval."""
    sets = [set(year_city_sets.get(year, set())) for year in years]
    return bool(sets) and bool(sets[0]) and all(current == sets[0] for current in sets)
