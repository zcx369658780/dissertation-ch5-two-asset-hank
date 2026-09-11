from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import numpy as np

from ch5_two_asset_hank.multi_province import c1_residual_public_asset as c1
from ch5_two_asset_hank.multi_province.one_turn import OneTurnInputs, PreFrozenHouseholdOutputBatch
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER
from validators.multi_province.c1_residual_public_asset_25turn import run


ROOT = Path(__file__).resolve().parents[1]
C1_SOURCE = ROOT / "src/ch5_two_asset_hank/multi_province/c1_residual_public_asset.py"
RUN_SOURCE = ROOT / "validators/multi_province/c1_residual_public_asset_25turn/run.py"


def _inputs(private: np.ndarray) -> OneTurnInputs:
    n = 31
    household = PreFrozenHouseholdOutputBatch(
        ct=np.ones(n), household_lt=np.ones(n), at=np.ones(n), bt=np.ones(n),
        at_tax=np.zeros(n), converged=(True,) * n, diagnostics=({},) * n,
    )
    provinces = tuple({
        "name": name, "N": 1.0, "wjt": 1.0, "tau": 0.1,
        "inter_prv_ratio": 1.0, "ra": 0.05, "Kt0": 10.0,
    } for name in PROVINCE_ORDER)
    params = {"ga": 2.0, "phi_l": 5.0, "alphal": 1.0, "istar": 0.015,
              "rho_pi": 1.25, "totalpit": 0.02, "epsilon_pi": 0.0}
    return OneTurnInputs(tuple(PROVINCE_ORDER), provinces, params, np.ones((n, n)), np.zeros((n, n)), household)


def test_c1_one_turn_order_and_firm_capital_contract(monkeypatch) -> None:
    trace: list[str] = []
    private = np.full(31, 2.0)
    private[1] = 12.0
    migration = SimpleNamespace(lt_supply=np.ones(31), lt_mat=np.eye(31))
    capital = SimpleNamespace(kt_supply=private, household_illiquid_return_rah=np.full(31, 0.05))

    monkeypatch.setattr(c1.source, "reconstruct_migration_labor", lambda *_args, **_kwargs: trace.append("migration") or migration)
    monkeypatch.setattr(c1.source, "allocate_productive_capital", lambda *_args, **_kwargs: trace.append("capital") or capital)

    def firm(province, private_k, _labor, _params):
        trace.append("firm")
        return SimpleNamespace(Kt=private_k + province["GovInv"], Govinc=0.0, wjt=1.0)

    monkeypatch.setattr(c1.source, "evaluate_firm", firm)
    monkeypatch.setattr(c1.source, "composite_household_wages", lambda *_args, **_kwargs: trace.append("wage") or np.ones(31))
    monkeypatch.setattr(c1.source, "taylor_assignment", lambda **_kwargs: trace.append("taylor") or SimpleNamespace(rb=0.01))
    monkeypatch.setattr(c1.source, "national_fiscal_diagnostics", lambda *_args, **_kwargs: trace.append("fiscal") or SimpleNamespace(Govinc=np.zeros(31)))

    result = c1.run_c1_residual_public_asset_one_turn(_inputs(private))
    assert trace[:2] == ["migration", "capital"]
    assert trace[2:33] == ["firm"] * 31
    assert trace[-3:] == ["wage", "taylor", "fiscal"]
    assert result.firms[0].Kt == 10.0
    assert result.c1_accounting.GovInv_residual_MU[0] == 8.0
    assert result.firms[1].Kt == 12.0
    assert result.c1_accounting.GovInv_residual_MU[1] == 0.0
    assert result.c1_accounting.residual_floor_binding[1]


def test_c1_initialization_uses_accepted_batch_helper() -> None:
    states = tuple({"name": name, "GovInv": 10.0} for name in PROVINCE_ORDER)
    target, private = np.full(31, 10.0), np.full(31, 2.0)
    private[4] = 11.0
    result, accounting = run.build_c1_initial_states(states, target, private)
    assert result[0]["GovInv"] == 8.0
    assert result[4]["GovInv"] == 0.0
    assert np.array_equal(accounting["g1_total"], np.maximum(target, private))


def test_c1_row_assertions_cover_below_and_above_target() -> None:
    rows = [
        {"province": "甲", "Ktarget_2018_MU": 10.0, "Kt_supply_private_MU": 2.0, "firm_K_total_MU": 10.0},
        {"province": "乙", "Ktarget_2018_MU": 10.0, "Kt_supply_private_MU": 12.0, "firm_K_total_MU": 12.0},
    ]
    run._correct_turn_rows(rows)
    assert rows[0]["GovInv_C1_MU"] == 8.0 and not rows[0]["residual_floor_binding"]
    assert rows[1]["GovInv_C1_MU"] == 0.0 and rows[1]["residual_floor_binding"]
    assert max(row["c1_accounting_abs_residual_MU"] for row in rows) == 0.0


def test_c1_outer_adaptation_changes_only_zt() -> None:
    states = [{"name": "甲", "Zt": 2.0, "GovInv": 8.0, "Yt": 12.0, "Yt0": 10.0,
               "Kt": 10.0, "Lt": 4.0, "alpha": 0.7}]
    updated, actions = run._adapt_c1_zt_only(states, 0.01, True)
    assert updated[0]["Zt"] != 2.0
    assert updated[0]["GovInv"] == 8.0
    assert actions[0].govinv_before == actions[0].govinv_after == 8.0
    assert actions[0].govinv_action == "C1_RESIDUAL_LEVEL__NO_C0_ACTION"


def test_c1_route_is_separate_and_contains_no_gain_controller() -> None:
    source = C1_SOURCE.read_text(encoding="utf-8") + RUN_SOURCE.read_text(encoding="utf-8")
    assert "run_c1_residual_public_asset_one_turn" in source
    assert "residual_government_asset_levels" in source
    for forbidden in ("lambda_K", "ra_target", "hysteresis"):
        assert forbidden not in source


def test_source_faithful_labor_and_exact_budget_are_preserved() -> None:
    source = C1_SOURCE.read_text(encoding="utf-8") + RUN_SOURCE.read_text(encoding="utf-8")
    assert "reconstruct_migration_labor" in source
    assert "reconstruct_origin_preserving_normalized_migration_labor" not in source
    assert "normalized_labor_route_active\": False" in source
    assert "g1.execute(root)" in source
    assert "scientific_retries" not in source or '"scientific_processes": 0' in source


def test_prepare_and_phase_a_are_zero_science_by_construction() -> None:
    source = RUN_SOURCE.read_text(encoding="utf-8")
    marker = source.index("def execute")
    assert "g1.execute" not in source[:marker]
    assert '"scientific_processes": 0' in source[:marker]
    assert '"hjb_calls": 0' in source[:marker]
    assert '"trajectory_calls": 0' in source[:marker]
