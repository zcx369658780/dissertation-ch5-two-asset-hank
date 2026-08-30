from __future__ import annotations

import pytest
import numpy as np

from ch5_two_asset_hank.multi_province import (
    DATA_PROVENANCE_MANIFEST,
    PROVINCE_ORDER,
    HouseholdOuterOutputs,
    MigrationLaborAllocation,
    ProvinceAxis,
    ProvinceMatrix,
    ProvinceVector,
    YearCacheBinding,
)


def test_province_axis_accepts_only_the_source_order() -> None:
    axis = ProvinceAxis(PROVINCE_ORDER)
    assert len(axis.labels) == 31
    assert axis.labels[0] == "北京"
    assert axis.labels[-1] == "新疆"

    reordered = list(PROVINCE_ORDER)
    reordered[0], reordered[1] = reordered[1], reordered[0]
    with pytest.raises(ValueError, match="exact source order"):
        ProvinceAxis(tuple(reordered))


def test_province_axis_rejects_wrong_count_duplicate_and_unknown_label() -> None:
    with pytest.raises(ValueError, match="exactly 31"):
        ProvinceAxis(PROVINCE_ORDER[:-1])
    duplicate = PROVINCE_ORDER[:-1] + (PROVINCE_ORDER[0],)
    with pytest.raises(ValueError, match="duplicate"):
        ProvinceAxis(duplicate)
    unknown = PROVINCE_ORDER[:-1] + ("未知省",)
    with pytest.raises(ValueError, match="unknown"):
        ProvinceAxis(unknown)


def test_province_vectors_and_matrices_fail_closed_on_shape_or_nonfinite_data() -> None:
    axis = ProvinceAxis(PROVINCE_ORDER)
    vector = ProvinceVector("population", np.arange(1.0, 32.0), axis)
    matrix = ProvinceMatrix("origin_destination", np.eye(31), axis, "destination", "origin")
    assert vector.values.shape == (31,)
    assert matrix.values.shape == (31, 31)
    assert not vector.values.flags.writeable
    assert not matrix.values.flags.writeable

    with pytest.raises(ValueError, match=r"shape \(31,\)"):
        ProvinceVector("population", np.ones(30), axis)
    with pytest.raises(ValueError, match=r"shape \(31, 31\)"):
        ProvinceMatrix("flows", np.ones((31, 30)), axis, "destination", "origin")
    bad = np.ones(31)
    bad[4] = np.nan
    with pytest.raises(ValueError, match="finite"):
        ProvinceVector("population", bad, axis)


def test_household_outer_outputs_preserve_lt_at_bt_and_diagnostics_roles() -> None:
    axis = ProvinceAxis(PROVINCE_ORDER)
    values = np.arange(1.0, 32.0)
    outputs = HouseholdOuterOutputs(
        ct=ProvinceVector("Ct", values, axis),
        household_lt=ProvinceVector("Lt", values + 1.0, axis),
        at=ProvinceVector("At", values + 2.0, axis),
        bt=ProvinceVector("Bt", values + 3.0, axis),
        at_tax=ProvinceVector("AtTax", values + 4.0, axis),
        converged=tuple([True] * 31),
        diagnostics=tuple({"iterations": 12} for _ in range(31)),
    )
    assert outputs.household_lt.values[0] == 2.0
    assert outputs.at.values[0] != outputs.bt.values[0]
    assert outputs.diagnostics[0]["iterations"] == 12

    with pytest.raises(ValueError, match="31 convergence"):
        HouseholdOuterOutputs(
            ct=outputs.ct,
            household_lt=outputs.household_lt,
            at=outputs.at,
            bt=outputs.bt,
            at_tax=outputs.at_tax,
            converged=(True,),
            diagnostics=outputs.diagnostics,
        )

    with pytest.raises(ValueError, match="ct must be named Ct"):
        HouseholdOuterOutputs(
            ct=ProvinceVector("consumption", values, axis),
            household_lt=outputs.household_lt,
            at=outputs.at,
            bt=outputs.bt,
            at_tax=outputs.at_tax,
            converged=outputs.converged,
            diagnostics=outputs.diagnostics,
        )


def test_migration_labor_matrix_rows_are_destination_and_columns_are_origin() -> None:
    axis = ProvinceAxis(PROVINCE_ORDER)
    asymmetric = np.zeros((31, 31))
    asymmetric[0, 1] = 2.0
    asymmetric[2, 0] = 7.0
    allocation = MigrationLaborAllocation(
        ProvinceMatrix("Lt_mat", asymmetric, axis, "destination", "origin")
    )
    np.testing.assert_array_equal(allocation.destination_supply(), asymmetric.sum(axis=1))
    assert not np.array_equal(allocation.destination_supply(), asymmetric.T.sum(axis=1))

    with pytest.raises(ValueError, match="rows=destination, columns=origin"):
        MigrationLaborAllocation(
            ProvinceMatrix("Lt_mat", asymmetric, axis, "origin", "destination")
        )


def test_data_manifest_freezes_source_and_cache_roles_without_raw_data() -> None:
    by_name = {entry.name: entry for entry in DATA_PROVENANCE_MANIFEST}
    assert set(by_name) == {
        "中国各省省会地理距离矩阵.xlsx",
        "2000年后各省数据_填充NA.xlsx",
        "2000年后各省数据.xlsx",
        "R语言估计结果_plm估计.xlsx",
        "数据估计结果_1000_100_0.mat",
        "Multi_Province_12sts_<year>.mat",
    }
    assert by_name["数据估计结果_1000_100_0.mat"].classification == "CACHE_DERIVED_NOT_PRIMARY_AUTHORITY"
    assert by_name["数据估计结果_1000_100_0.mat"].owner_approval_required
    assert by_name["Multi_Province_12sts_<year>.mat"].expected_sha256 is None
    assert all(entry.read_only_no_overwrite for entry in DATA_PROVENANCE_MANIFEST)


def test_unresolved_year_cache_binding_fails_closed() -> None:
    unresolved = YearCacheBinding(
        source_ii=1,
        dataset_row=1,
        cache_year=2009,
        semantics_status="UNRESOLVED_SOURCE_II_DATASET_ROW_CACHE_YEAR",
        owner_approved=False,
    )
    with pytest.raises(ValueError, match="Owner-verified"):
        unresolved.require_annual_execution_authority()

    verified = YearCacheBinding(
        source_ii=4,
        dataset_row=4,
        cache_year=2012,
        semantics_status="OWNER_VERIFIED",
        owner_approved=True,
    )
    assert verified.require_annual_execution_authority() == (4, 4, 2012)

    inconsistent = YearCacheBinding(
        source_ii=4,
        dataset_row=4,
        cache_year=2013,
        semantics_status="OWNER_VERIFIED",
        owner_approved=True,
    )
    with pytest.raises(ValueError, match=r"source_ii \+ 2008"):
        inconsistent.require_annual_execution_authority()
