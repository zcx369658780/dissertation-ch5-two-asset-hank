from __future__ import annotations

from decimal import Decimal

import pytest

from validators.multi_province.ra_w_health_region_mapping.build import (
    canonical_health_label,
    classify_projection,
    nearest_observed_coordinate,
)


def test_coarse_legacy_labels_are_mapped_from_observed_boundary_geometry() -> None:
    assert canonical_health_label(
        source_label="QUALITY_AMBIGUOUS__OWNER_REVIEW_REQUIRED",
        modal_a=Decimal("0"),
        amin=Decimal("0"),
        amax=Decimal("10"),
        kfe_pathological=False,
    ) == ("LOWER_A_BOUNDARY_DOMINATED", "LOWER_A_BOUNDARY_DOMINATED")
    assert canonical_health_label(
        source_label="BOUNDARY_CONVERGED_CANDIDATE",
        modal_a=Decimal("10"),
        amin=Decimal("0"),
        amax=Decimal("10"),
        kfe_pathological=False,
    ) == ("UPPER_A_BOUNDARY_PILEUP", "UPPER_A_BOUNDARY_PILEUP")


def test_signed_kfe_pathology_overrides_health_label_but_preserves_modal_label() -> None:
    assert canonical_health_label(
        source_label="LOWER_A_BOUNDARY_DOMINATED",
        modal_a=Decimal("0"),
        amin=Decimal("0"),
        amax=Decimal("10"),
        kfe_pathological=True,
    ) == ("LOWER_A_BOUNDARY_DOMINATED", "KFE_NUMERICALLY_PATHOLOGICAL")


@pytest.mark.parametrize(
    ("health_label", "expected"),
    [
        ("INTERIOR_A_DISTRIBUTION_CANDIDATE", "EXACT_OBSERVED_INTERIOR_MATCH"),
        ("TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED", "EXACT_OBSERVED_AMBIGUOUS_MATCH"),
        ("LOWER_A_BOUNDARY_DOMINATED", "EXACT_OBSERVED_UNHEALTHY_MATCH"),
        ("UPPER_A_BOUNDARY_PILEUP", "EXACT_OBSERVED_UNHEALTHY_MATCH"),
        ("KFE_NUMERICALLY_PATHOLOGICAL", "EXACT_OBSERVED_UNHEALTHY_MATCH"),
    ],
)
def test_projection_requires_exact_decimal_coordinate(health_label: str, expected: str) -> None:
    observed = {(Decimal("0.06"), Decimal("1.3")): health_label}
    assert classify_projection(Decimal("0.06"), Decimal("1.3"), observed) == expected
    assert (
        classify_projection(Decimal("0.0600000000000001"), Decimal("1.3"), observed)
        == "UNOBSERVED_OR_INTERPOLATION_NOT_AUTHORIZED"
    )


def test_nearest_coordinate_reports_distances_without_assigning_a_health_class() -> None:
    observed = {
        (Decimal("0.06"), Decimal("1.3")): "INTERIOR_A_DISTRIBUTION_CANDIDATE",
        (Decimal("0.07"), Decimal("1.05")): "TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED",
    }
    nearest = nearest_observed_coordinate(Decimal("0.08"), Decimal("12.8"), observed)
    assert nearest["ra"] == "0.06"
    assert nearest["wage"] == "1.3"
    assert nearest["distance_ra"] == "0.02"
    assert nearest["distance_wage"] == "11.5"
    assert nearest["use"] == "DESCRIPTIVE_ONLY__NOT_ADMISSIBILITY_CLASSIFICATION"
