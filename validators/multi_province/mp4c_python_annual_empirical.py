"""MP4C source-faithful annual Python stationary entry for authorized years."""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from typing import Mapping

import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
for import_root in (str(SRC_ROOT), str(REPO_ROOT)):
    if import_root not in sys.path:
        sys.path.insert(0, import_root)

from validators.multi_province import mp4b_python_empirical as anchor
from ch5_two_asset_hank.multi_province.annual import (
    AnnualSourceScalars,
    DecoupledAnnualIndex,
    PrimaryAnnualSourceFiles,
    load_primary_annual_input,
)
from ch5_two_asset_hank.multi_province.one_turn import PreFrozenHouseholdOutputBatch
from ch5_two_asset_hank.multi_province.stationary_runtime import (
    OnlineStationaryInputs,
    run_online_stationary,
)
from ch5_two_asset_hank.multi_province.steady_state import SteadyStateConvergenceError


SOURCE_HASHES = {
    "2000年后各省数据_填充NA.xlsx": "C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929",
    "R语言估计结果_plm估计.xlsx": "A6F444FCCCB30CB93AA5DE084F1DD163C54E5F53C4287C2CD3E13A045EB64A68",
    "中国各省省会地理距离矩阵.xlsx": "26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566",
}
ACCEPTED_2009_CANONICAL_SHA = "507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48"
AUTHORIZED_SCIENTIFIC_YEARS = (2010, 2011)
MAX_OUTER_TURNS = 250
MAX_HOUSEHOLD_CALLS = 7750
WALL_CLOCK_LIMIT_SECONDS = 14400


def accepted_source_scalars() -> AnnualSourceScalars:
    """Return the exact accepted corrected-2009 primary scalar contract."""
    return AnnualSourceScalars(
        gdp_multiplier=1000.0,
        pop_multiplier=100.0,
        calibration_delta=0.096,
        zt_ratio=1.0,
        gov_inv_ratio=1.0,
        max_sigmau=0.5,
        rb_gap=0.07,
        rah=0.09,
        ra=0.09,
        nominal_rate=0.02,
        rb=0.02,
        rk=0.1,
        wjt=0.6,
        composite_wage=20.0,
        transfer_income=0.1,
        inflation=0.02,
        wage_tax=0.05,
        initial_at=2.0,
        initial_bt=1.0,
        initial_mt=0.9,
        initial_ct=4.0,
        corporate_tax=0.25,
    )


def primary_sources(local_root: Path) -> PrimaryAnnualSourceFiles:
    root = Path(local_root)
    return PrimaryAnnualSourceFiles(
        filled_workbook=root / "2000年后各省数据_填充NA.xlsx",
        regression_workbook=root / "R语言估计结果_plm估计.xlsx",
        distance_workbook=root / "中国各省省会地理距离矩阵.xlsx",
        expected_filled_sha256=SOURCE_HASHES["2000年后各省数据_填充NA.xlsx"],
        expected_regression_sha256=SOURCE_HASHES["R语言估计结果_plm估计.xlsx"],
        expected_distance_sha256=SOURCE_HASHES["中国各省省会地理距离矩阵.xlsx"],
    )


def prepare_canonical(year: int, local_root: Path, output_root: Path) -> dict[str, object]:
    """Build and persist one annual canonical input without any model call."""
    binding = DecoupledAnnualIndex.for_calendar_year(year)
    canonical = load_primary_annual_input(
        sources=primary_sources(local_root), binding=binding, scalars=accepted_source_scalars()
    )
    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=False)
    canonical_path = root / f"calendar_{year}_primary_premodel_input.json"
    canonical_path.write_bytes(canonical.canonical_bytes())
    payload = {
        "schema": "CH5_MP4C_ANNUAL_CANONICAL_PREPARATION_V1",
        "calendar_year": year,
        "binding": anchor._jsonable(binding),
        "canonical_path": str(canonical_path.resolve()),
        "canonical_sha256": canonical.canonical_sha256(),
        "source_hashes": dict(canonical.source_hashes),
        "province_order": list(canonical.province_axis.labels),
        "regression_sheet": canonical.regression_sheet,
        "fixed_zt_calendar_year": canonical.fixed_zt_calendar_year,
        "all_arrays_finite": all(
            np.isfinite(getattr(canonical, name)).all()
            for name in (
                "gdp", "cap", "pop", "log_pgdp", "log_pcap", "ind_alpha", "ind_zt",
                "initialized_zt", "gov_inv", "inter_province_asset_ratio", "distance", "sigmau",
            )
        ),
        "scientific_calls": {"household": 0, "hjb": 0, "kfe": 0, "mp2": 0, "mp3": 0, "stationary": 0},
    }
    anchor._write_json(root / "calendar_index_manifest.json", payload)
    return payload


def load_entry_state(canonical_path: Path) -> tuple[dict, tuple[dict[str, object], ...]]:
    canonical = json.loads(Path(canonical_path).read_text(encoding="utf-8"))
    year = int(canonical["binding"]["calendar_year"])
    expected = DecoupledAnnualIndex.for_calendar_year(year)
    expected_binding = {
        "analysis_index": expected.analysis_index,
        "calendar_year": expected.calendar_year,
        "data_mat_index": expected.data_mat_index,
        "output_filename_year": expected.output_filename_year,
        "regression_vintage_key": expected.regression_vintage_key,
        "workbook_data_row_index": expected.workbook_data_row_index,
    }
    if canonical["binding"] != expected_binding:
        raise ValueError("canonical annual binding mismatch")
    if canonical["regression_sheet"] != f"总面板回归系数_{expected.regression_vintage_key}_行业4":
        raise ValueError("canonical annual regression vintage mismatch")
    if canonical["source_hashes"] != SOURCE_HASHES:
        raise ValueError("canonical annual source hashes mismatch")
    vectors = canonical["vectors"]
    scalars = canonical["scalars"]
    states = []
    for index, name in enumerate(canonical["province_order"]):
        state = {
            "name": name, "N": vectors["pop"][index], "alpha": vectors["ind_alpha"][index],
            "Zt": vectors["initialized_zt"][index], "Kt0": vectors["cap"][index],
            "Kt": vectors["cap"][index], "Kt_prev": vectors["cap"][index],
            "Lt": vectors["pop"][index], "Lt_prev": vectors["pop"][index],
            "Yt0": vectors["gdp"][index], "Yt": vectors["gdp"][index],
            "Zt_1": vectors["initialized_zt"][index], "GovInv": vectors["gov_inv"][index],
            "inter_prv_ratio": vectors["inter_province_asset_ratio"][index],
            "rb_gap": scalars["rb_gap"], "rah": scalars["rah"], "ra": scalars["ra"],
            "it": scalars["nominal_rate"], "rb": scalars["rb"], "rk": scalars["rk"],
            "wjt": scalars["wjt"], "w": scalars["composite_wage"],
            "Tt": scalars["transfer_income"], "pit": scalars["inflation"],
            "pit_1": scalars["inflation"], "totalpit": scalars["inflation"],
            "epsilon_pi": 0.0, "tau": scalars["wage_tax"], "At": scalars["initial_at"],
            "Bt": scalars["initial_bt"], "mt": scalars["initial_mt"],
            "Ct": scalars["initial_ct"], "AtTax": 0.0, "GovSurplus": 0.0,
            "corptau": scalars["corporate_tax"], "ramin": 0.02, "ramax": 0.09,
            "wjtmin": 0.8, "wjtmax": 1.3,
        }
        states.append(state)
    return canonical, tuple(states)


def _terminal_evidence(result, call_count: int, elapsed: float) -> dict[str, object]:
    final = result.final_state
    last = result.history[-1]
    fields = (
        "Ct", "At", "Bt", "Lt", "Lt_supply", "Kt_supply", "rah", "Kt", "Yt", "mt",
        "KNratio", "w", "wjt", "rk", "ra", "GovInv", "rb", "it", "Zt", "Govinc",
    )
    frozen = [{"name": state["name"], **{field: float(state[field]) for field in fields}} for state in final]
    return {
        "status": result.termination_reason,
        "converged": bool(result.converged),
        "iteration_count": result.iteration_count,
        "household_call_count": call_count,
        "household_converged_count": last.household_converged_count,
        "ra_upper_count": last.ra_upper_count,
        "ra_lower_count": last.ra_lower_count,
        "wage_upper_count": last.wage_upper_count,
        "wage_lower_count": last.wage_lower_count,
        "province_order": [state["name"] for state in final],
        "final_31x20": frozen,
        "national": {field: float(sum(float(state[field]) for state in final)) for field in ("Ct", "At", "Bt", "Yt")},
        "wall_clock_seconds": elapsed,
        "history": result.history,
        "final_state": final,
    }


def run_python_once(canonical_path: Path, run_root: Path):
    root = Path(run_root)
    root.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    canonical, states = load_entry_state(canonical_path)
    year = int(canonical["binding"]["calendar_year"])
    if year not in AUTHORIZED_SCIENTIFIC_YEARS:
        raise ValueError(f"calendar year is outside this task authority: {year}")
    canonical_sha = anchor._sha256(Path(canonical_path))
    anchor._write_json(root / "python_run_manifest.json", {
        "schema": "CH5_MP4C_PYTHON_ANNUAL_SCIENTIFIC_RUN_V1",
        "calendar_year": year,
        "binding": canonical["binding"],
        "canonical_sha256": canonical_sha,
        "source_hashes": canonical["source_hashes"],
        "province_order": canonical["province_order"],
        "reg_threshold": 1e-9,
        "max_iterations": MAX_OUTER_TURNS,
        "max_household_calls": MAX_HOUSEHOLD_CALLS,
        "wall_clock_limit_seconds": WALL_CLOCK_LIMIT_SECONDS,
        "reruns": 0,
        "interface_only_unused_fields": {"mu_z": 0.0, "sigma_z": 0.0},
    })
    grid = anchor.MatlabFaithfulHJBGrid(
        np.linspace(-2, 5, 20), np.linspace(0, 10, 20), np.array([0.8, 1.3]),
        np.array([[-1 / 3, 1 / 3], [1 / 3, -1 / 3]]),
    )
    params = anchor.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
    numerics = anchor.MatlabFaithfulHJBNumerics(1000.0, 1e-7, 100, 1e-12)
    call_count = 0
    phi_matrix = np.ones((31, 31), dtype=float)

    def solve_batch(snapshot, iteration):
        nonlocal call_count
        if call_count + 31 > MAX_HOUSEHOLD_CALLS:
            raise RuntimeError("MP4C household-call ceiling would be exceeded")
        productivity = np.array([float(state["Yt"]) / float(state["Lt"]) for state in snapshot])
        phi_matrix[:] = 1.0 + 0.3 * (productivity[:, None] - productivity[None, :]) / (
            productivity[:, None] + productivity[None, :]
        )
        outputs = []
        anchor._write_json(root / f"turn_{iteration:03d}_household_inputs.json", {
            "iteration": iteration, "state_entering_turn": snapshot,
            "phi_destination_origin": phi_matrix,
        })
        try:
            for state in snapshot:
                initial, labor = anchor._source_initial_arrays(state, grid, params)
                result = anchor.solve_matlab_source_postloop_household(
                    grid, params,
                    anchor.HouseholdInputs(
                        float(state["rah"]), float(state["rb"]), float(state["tau"]),
                        np.array([state["w"]]), np.array([0.0]), np.array([1.0]),
                    ),
                    initial, labor, float(state["Tt"]), float(state["rb_gap"]), numerics,
                )
                call_count += 1
                aggregate = result.aggregates
                density = result.kfe.density
                effective = anchor.matlab_faithful_illiquid_return(
                    grid.a, grid.a[-1], float(state["rah"])
                )
                at_tax = aggregate.a_ss * float(state["rah"]) - float(
                    np.sum(grid.a[None, :, None] * effective[None, :, None] * density)
                    * result.kfe.cell_weight
                )
                outputs.append((
                    aggregate.c_ss, aggregate.l_ss, aggregate.a_ss, aggregate.b_ss, at_tax,
                    result.hjb.converged, result.hjb.iterations,
                    result.hjb.convergence_statistic,
                ))
        except Exception as exc:
            anchor._write_json(root / f"turn_{iteration:03d}_household_failure.json", {
                "iteration": iteration, "completed_households": len(outputs),
                "household_call_count": call_count, "error_type": type(exc).__name__,
                "error": str(exc),
            })
            raise
        batch = PreFrozenHouseholdOutputBatch(
            ct=[item[0] for item in outputs], household_lt=[item[1] for item in outputs],
            at=[item[2] for item in outputs], bt=[item[3] for item in outputs],
            at_tax=[item[4] for item in outputs], converged=tuple(item[5] for item in outputs),
            diagnostics=tuple({
                "hjb_converged": item[5], "hjb_iterations": item[6],
                "hjb_statistic": item[7], "iteration": iteration,
            } for item in outputs),
        )
        anchor._write_json(root / f"turn_{iteration:03d}_household_outputs.json", batch)
        return batch

    model_params = {
        "ga": 2.0, "phi_l": 5.0, "alphal": 1.0, "epsilon": 10.0,
        "theta": 100.0, "delta": 0.025, "istar": 0.015, "rho_pi": 1.25,
        "totalpit": 0.02, "epsilon_pi": 0.0,
    }
    try:
        result = run_online_stationary(OnlineStationaryInputs(
            tuple(canonical["province_order"]), states, model_params, phi_matrix,
            np.array(canonical["matrices"]["sigmau"]), solve_batch, 1e-9,
            MAX_OUTER_TURNS, True,
        ))
    except SteadyStateConvergenceError as exc:
        result = exc.result
        payload = _terminal_evidence(result, call_count, time.monotonic() - started)
        anchor._write_json(root / "python_terminal_summary.json", payload)
        raise
    except Exception as exc:
        anchor._write_json(root / "python_terminal_summary.json", {
            "status": "ERROR", "converged": False, "calendar_year": year,
            "household_call_count": call_count, "wall_clock_seconds": time.monotonic() - started,
            "error_type": type(exc).__name__, "error": str(exc),
        })
        raise
    payload = _terminal_evidence(result, call_count, time.monotonic() - started)
    anchor._write_json(root / "python_terminal_summary.json", payload)
    return result


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) == 4 and args[0] == "--prepare-canonical":
        prepare_canonical(int(args[1]), Path(args[2]), Path(args[3]))
        return 0
    if len(args) != 2:
        raise SystemExit(
            "usage: mp4c_python_annual_empirical.py --prepare-canonical YEAR LOCAL_DATA_ROOT FRESH_OUTPUT_ROOT | "
            "CANONICAL_JSON FRESH_RUN_ROOT"
        )
    run_python_once(Path(args[0]), Path(args[1]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
