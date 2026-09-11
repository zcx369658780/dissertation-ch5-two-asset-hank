from __future__ import annotations

import csv
import json

from scripts.ch5_mp4c_k1a_payoff_return_reaudit import run_audit


def test_run_audit_rejects_missing_persisted_evidence(tmp_path) -> None:
    missing = tmp_path / "missing"
    output = tmp_path / "output"

    try:
        run_audit(missing, output)
    except ValueError as exc:
        assert "accepted persisted evidence" in str(exc)
    else:
        raise AssertionError("missing evidence must fail closed")


def _write_accepted_evidence(root) -> None:
    fields = [
        "turn", "province_index", "province", "Ktarget_2018_MU", "Kt_supply_private_MU",
        "GovInv_after_MU", "firm_K_total_MU", "Y", "firm_ra0", "firm_ra_used", "firm_rk",
        "firm_profit_over_K", "firm_after_tax_profit_component_over_K",
        "firm_ra0_reconstruction_residual", "household_rah_k1a_current_payoff_bridge", "ramin", "ramax",
    ]
    provinces = [f"p{index}" for index in range(31)]
    matrix = [[1.0 if destination == origin else 0.0 for origin in range(31)] for destination in range(31)]
    for directory in ("path_a_equal_share", "path_b_geographic_beta2"):
        prior_used = [0.02] * 31
        for turn in range(1, 26):
            turn_dir = root / directory / f"turn_{turn:02d}"
            turn_dir.mkdir(parents=True)
            rows = []
            used = []
            for index, province in enumerate(provinces):
                raw = 0.10 if index % 2 == 0 else 0.05 + turn * 0.0001
                if index == 1:
                    raw = 0.09  # At the upper boundary but not an upper clip.
                clipped = min(raw, 0.09)
                used.append(clipped)
                rows.append({
                    "turn": turn, "province_index": index, "province": province, "Ktarget_2018_MU": 10.0,
                    "Kt_supply_private_MU": 2.0, "GovInv_after_MU": 8.0, "firm_K_total_MU": 10.0,
                    "Y": 5.0, "firm_ra0": raw, "firm_ra_used": clipped, "firm_rk": raw + 0.9,
                    "firm_profit_over_K": 0.0, "firm_after_tax_profit_component_over_K": 0.0,
                    "firm_ra0_reconstruction_residual": 0.0,
                    "household_rah_k1a_current_payoff_bridge": prior_used[index], "ramin": 0.02, "ramax": 0.09,
                })
            with (turn_dir / "per_province_observables.csv").open("w", newline="", encoding="utf-8-sig") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerows(rows)
            allocation_dir = root / directory / "capital_network"
            allocation_dir.mkdir(parents=True, exist_ok=True)
            allocation = {
                "orientation": "DESTINATION_BY_ORIGIN", "province_order": provinces,
                "portfolio_shares_destination_origin": matrix,
                # allocation_n persists the entering, lagged payoff; allocation_{n+1}
                # is the receipt that validates turn_n's used return under the same S.
                "household_portfolio_return_by_origin": prior_used,
            }
            (allocation_dir / f"allocation_{turn:02d}_turn_{turn:02d}.json").write_text(
                json.dumps(allocation), encoding="utf-8"
            )
            prior_used = used


def test_run_audit_writes_static_no_feedback_receipts_from_same_persisted_s(tmp_path) -> None:
    evidence = tmp_path / "accepted"
    output = tmp_path / "output"
    _write_accepted_evidence(evidence)

    run_audit(evidence, output)

    summary = json.loads((output / "reaudit_summary.json").read_text(encoding="utf-8"))
    static_rows = list(csv.DictReader((output / "static_no_feedback_payoff_counterfactual.csv").open(encoding="utf-8")))
    assert summary["classification"] == "STATIC_NO_FEEDBACK_COUNTERFACTUAL"
    path_a = next(path for path in summary["paths"] if path["path"] == "A_EQUAL_SHARE")
    assert path_a["upper_clipped_count"] == 25 * 16
    assert path_a["share_exactly_0_09"] == 17 / 31
    assert len(static_rows) == 2 * 25 * 31
    assert static_rows[0]["classification"] == "STATIC_NO_FEEDBACK_COUNTERFACTUAL"
    assert static_rows[0]["next_allocation_payoff_validation_status"] == "VALIDATED_SAME_S_AND_NEXT_ALLOCATION_PAYOFF"
    assert static_rows[-1]["next_allocation_payoff_validation_status"] == "NOT_AVAILABLE_AUTHORIZED_CEILING"
    assert abs(float(static_rows[0]["raw_minus_clipped"]) - 0.01) < 1e-12
    assert (output / "cross_path_turn_comparison.csv").is_file()
    assert (output / "static_no_feedback_payoff_difference_by_province.csv").is_file()


def test_run_audit_refuses_to_overwrite_an_existing_output_root(tmp_path) -> None:
    evidence = tmp_path / "accepted"
    output = tmp_path / "output"
    _write_accepted_evidence(evidence)
    output.mkdir()

    try:
        run_audit(evidence, output)
    except FileExistsError:
        pass
    else:
        raise AssertionError("audit output root must never be overwritten")


def _rewrite_first_csv_row(root, field: str, value: float) -> None:
    path = root / "path_a_equal_share" / "turn_01" / "per_province_observables.csv"
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fields = reader.fieldnames
    rows[0][field] = str(value)
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def test_run_audit_rejects_tampered_used_ra_that_is_not_the_recorded_clip(tmp_path) -> None:
    evidence = tmp_path / "accepted"
    _write_accepted_evidence(evidence)
    _rewrite_first_csv_row(evidence, "firm_ra_used", 0.08)

    try:
        run_audit(evidence, tmp_path / "output")
    except ValueError as exc:
        assert "does not equal clipped raw ra" in str(exc)
    else:
        raise AssertionError("tampered firm_ra_used must fail closed")


def test_run_audit_rejects_tampered_current_allocation_lagged_payoff(tmp_path) -> None:
    evidence = tmp_path / "accepted"
    _write_accepted_evidence(evidence)
    path = evidence / "path_a_equal_share" / "capital_network" / "allocation_01_turn_01.json"
    allocation = json.loads(path.read_text(encoding="utf-8"))
    allocation["household_portfolio_return_by_origin"][0] = 0.03
    path.write_text(json.dumps(allocation), encoding="utf-8")

    try:
        run_audit(evidence, tmp_path / "output")
    except ValueError as exc:
        assert "does not match CSV lagged rah bridge" in str(exc)
    else:
        raise AssertionError("tampered allocation lagged payoff must fail closed")
