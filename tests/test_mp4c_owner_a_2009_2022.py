from __future__ import annotations

import json
from pathlib import Path

import pytest

from validators.multi_province import mp4c_owner_a_2009_2022 as owner_a
from validators.multi_province import mp4c_run_full_annual_batch as batch


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "data_local" / "matlab_primary_source_snapshot"
CACHE = REPO / "data_local" / "matlab_runtime_snapshot" / "数据估计结果_1000_100_0.mat"


def test_owner_a_scope_is_exact_and_excludes_2023() -> None:
    assert owner_a.YEARS == tuple(range(2009, 2023))
    assert 2023 not in owner_a.YEARS
    assert owner_a._binding(2009)["rolling_window_entry_index"] == 1
    assert owner_a._binding(2022)["regression_vintage_index"] == 23
    with pytest.raises(ValueError):
        owner_a._binding(2023)


def test_owner_a_static_plm_artifacts_cover_only_vintages_10_23() -> None:
    audit = owner_a.static_plm_audit(DATA, CACHE)
    assert len(audit["years"]) == 14
    assert [row["regression_vintage_index"] for row in audit["years"]] == list(range(10, 24))
    assert all(not row["vintage_24_consumed"] for row in audit["years"])


@pytest.mark.parametrize("year", owner_a.YEARS)
def test_owner_a_input_has_exact_indices_and_finite_recomputed_levels(year: int) -> None:
    payload = owner_a.build_input(DATA, CACHE, year)
    owner_a.validate(payload)
    assert payload["representation"] == owner_a.REPRESENTATION
    assert payload["binding"]["calendar_level_row_index"] == year - 1999
    assert payload["source_fields"]["CAP"] == "R语言计算资本存量"
    assert payload["no_2023_scientific_input"] is True


def test_owner_a_input_canonical_bytes_are_json_serializable() -> None:
    payload = owner_a.build_input(DATA, CACHE, 2009)
    serialized = json.loads(owner_a.canonical_bytes(payload))
    assert serialized["source_hashes"] == payload["source_hashes"]


def test_scheduler_owner_a_mode_requires_exact_14_year_scope(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="exactly 2009..2022"):
        batch.run_batch(DATA, CACHE, tmp_path, 8, tuple(range(2009, 2022)), True)
