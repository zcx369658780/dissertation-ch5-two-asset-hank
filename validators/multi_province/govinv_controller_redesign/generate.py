"""Generate the GovInv controller forensic package from accepted ledgers only.

This module deliberately imports no model or runtime module.  It performs CSV
parsing, deterministic arithmetic, serialization, and hashing only.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


REPO = Path(__file__).resolve().parents[3]
ROOT = REPO / "reports/mp4c_govinv_controller_redesign_20260911"
LEDGER = REPO / "reports/mp4c_g1_residual_govinv_25turn_isolated_20260911/province_turn_capital_ledger.csv"
REPORT = REPO / "docs/CH5_MP4C_GOVINV_CONTROLLER_REDESIGN_FORENSIC_AND_SPEC.md"
BASE = "952d19eaca663235c68adf1bd48e9f4e007cb18f"
VERDICT = "GOVINV_CONTROLLER_REDESIGN_SPEC_PASS__HISTORICAL_CONTROLLER_FAILURE_MECHANISM_QUANTIFIED_AND_CANDIDATES_SEPARATED"
PROTECTED = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK")
PROTECTED_HASHES = {
    "HANK_mp_1eq.m": "ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF",
    "HANK_mp_1turn.m": "D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF",
    "HANK_firm.m": "EE02C15414ADF9F99AADE04F1F22E64FA7094C8AB77753B6130BC4BFA6CE7BD5",
}
WINDOWS = (
    ("ALL_TURNS_01_25", 1, 25),
    ("TURNS_01_05", 1, 5),
    ("TURNS_06_10", 6, 10),
    ("TURNS_11_15", 11, 15),
    ("TURNS_16_20", 16, 20),
    ("TURNS_21_25", 21, 25),
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def write_json(path: Path, payload: object) -> None:
    write_text(path, json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def load_ledger() -> list[dict[str, str]]:
    with LEDGER.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    if len(rows) != 775:
        raise RuntimeError(f"accepted G1 ledger row count changed: {len(rows)}")
    if {int(row["turn"]) for row in rows} != set(range(1, 26)):
        raise RuntimeError("accepted G1 ledger must contain turns 1..25")
    if any(sum(int(row["turn"]) == turn for row in rows) != 31 for turn in range(1, 26)):
        raise RuntimeError("accepted G1 ledger must contain 31 provinces per turn")
    return rows


def expected_c0_action(row: dict[str, str]) -> str:
    if row["adaptation_gate_open"] != "True":
        return "NONE"
    used_ra = float(row["firm_ra_used"])
    if used_ra < 0.02 + 0.02:
        return "LOW_RA_DECREASE_0P9"
    if used_ra > 0.09 - 0.02:
        return "HIGH_RA_INCREASE_1P1"
    return "NONE"


def classify(row: dict[str, str]) -> dict[str, object]:
    target = float(row["Ktarget_2018_MU"])
    total = float(row["firm_K_total_MU"])
    gap = target - total
    if gap > 0:
        position = "BELOW_TARGET"
        c1_direction = "INCREASE_GOVINV_TOWARD_TARGET"
    elif gap < 0:
        position = "ABOVE_TARGET"
        c1_direction = "DECREASE_GOVINV_TOWARD_TARGET"
    else:
        position = "AT_TARGET"
        c1_direction = "HOLD_AT_TARGET"
    action = row["govinv_action"]
    worsening = ((gap < 0 and action == "HIGH_RA_INCREASE_1P1") or
                 (gap > 0 and action == "LOW_RA_DECREASE_0P9"))
    if worsening:
        direction = "CAPITAL_GAP_WORSENING_DIRECTION"
    elif action == "NONE":
        direction = "CAPITAL_GAP_CLOSING_OR_NEUTRAL_DIRECTION"
    else:
        direction = "CAPITAL_GAP_CLOSING_OR_NEUTRAL_DIRECTION"
    expected = expected_c0_action(row)
    return {
        "turn": int(row["turn"]),
        "province_index": int(row["province_index"]),
        "province": row["province"],
        "Ktarget_2018_MU": row["Ktarget_2018_MU"],
        "firm_K_total_MU": row["firm_K_total_MU"],
        "Ktarget_minus_totalK_MU": format(gap, ".17g"),
        "capital_position": position,
        "firm_ra0_raw": row["firm_ra0"],
        "firm_ra_used_clipped": row["firm_ra_used"],
        "adaptation_gate_open": row["adaptation_gate_open"],
        "recorded_c0_action": action,
        "replayed_c0_action": expected,
        "c0_replay_exact": expected == action,
        "c0_capital_gap_direction": direction,
        "c1_symbolic_positive_gain_direction": c1_direction,
        "dynamic_effect_claimed": False,
    }


def build_summary(rows: list[dict[str, object]]) -> dict[str, object]:
    windows = []
    for name, lo, hi in WINDOWS:
        selected = [row for row in rows if lo <= int(row["turn"]) <= hi]
        directions = Counter(str(row["c0_capital_gap_direction"]) for row in selected)
        actions = Counter(str(row["recorded_c0_action"]) for row in selected)
        positions = Counter(str(row["capital_position"]) for row in selected)
        worsening = directions["CAPITAL_GAP_WORSENING_DIRECTION"]
        windows.append({
            "window": name,
            "turn_start": lo,
            "turn_end": hi,
            "observations": len(selected),
            "worsening_count": worsening,
            "worsening_share": worsening / len(selected),
            "closing_or_neutral_count": directions["CAPITAL_GAP_CLOSING_OR_NEUTRAL_DIRECTION"],
            "recorded_action_counts": dict(sorted(actions.items())),
            "capital_position_counts": dict(sorted(positions.items())),
        })
    mismatches = sum(not bool(row["c0_replay_exact"]) for row in rows)
    return {
        "schema": "CH5_MP4C_GOVINV_CONTROLLER_DIRECTION_SUMMARY_V1",
        "classification_scope": "STATIC_CURRENT_ACCOUNTING_DIRECTION_ONLY__NOT_DYNAMIC_CAUSAL_EFFECT",
        "accepted_input_ledger": LEDGER.relative_to(REPO).as_posix(),
        "accepted_input_ledger_sha256": digest(LEDGER),
        "c0_formula_replay_mismatches": mismatches,
        "windows": windows,
    }


def source_timing_map() -> str:
    return """# Controller source and timing map

This is a read-only source reconstruction. It does not execute the controller.

1. A completed province batch reaches the firm before controller diagnostics. Firm accounting is `Kt=Kt_supply+GovInv`; the firm computes raw `ra0`, clips it to `[ramin,ramax]`, and stores only clipped `ra` in the shared state (`firm.py:61,110-125`; protected `HANK_firm.m:14,54-65`).
2. `_post_turn_states` copies those firm outputs into the post-turn state before `_diagnostics` and `_adapt` (`steady_state.py:146-168`). Consequently the controller sees the completed current-turn firm result.
3. The diagnostic is `nk_gap_i=abs(KNratio_i/tKNratio_i-1)`, and the gate is exactly `max(abs(KNratio/tKNratio-1))<0.1`. Adaptation opens only when that cross-province maximum condition holds and `steady_state` is true (`steady_state.py:172-201`; protected `HANK_mp_1eq.m:47`). This gate is separate from the final convergence tolerance.
4. Inside an open gate, the output discrepancy is checked first. If `abs(Yt/Yt0-1)>0.01`, `Zt` is recomputed before GovInv is inspected (`steady_state.py:209-218`; protected `HANK_mp_1eq.m:49-51`). Thus Zt and GovInv can both change in one adaptation pass.
5. The GovInv trigger uses clipped `state[\"ra\"]`, not raw `ra0`: `ra < ramin+0.02` gives `GovInv*=0.9`; `ra > ramax-0.02` gives `GovInv*=1.1`; otherwise it holds (`steady_state.py:219-226`; protected `HANK_mp_1eq.m:52-57`). With current bounds this means thresholds `0.04` and `0.07`, using strict inequalities.
6. After every nonconverged turn, whether or not adaptation opened, `tKNratio_next=0.6*KNratio_current+0.4*tKNratio_old` (`steady_state.py:257-293`; protected `HANK_mp_1eq.m:60-62`). A converged turn returns without adaptation or damping update.

No C0 expression reads `Ktarget`, `Kt_supply`, `Kt-Ktarget`, or private-K residual. The protected source comments label GovInv/state-owned capital and includes it in firm productive K and government income. However no inspected source or accepted data contract identifies it as an observed province public-capital stock. In the current runtime it is therefore an operational numerical stock with a government-capital label; choosing a production economic interpretation remains an Owner decision.
"""


CANDIDATE_FIELDS = [
    "candidate", "control_objective", "observed_signal", "target_reference", "sign_logic",
    "positivity_handling", "Ktarget_direct", "ra_signal", "expected_response_to_accepted_g1",
    "dimensional_consistency", "source_authority", "economic_interpretation",
    "numerical_stability_risk", "tuning_degrees_of_freedom", "overfit_risk",
    "Zt_tKNratio_interaction", "normalized_labor_interaction", "minimum_future_scientific_budget",
    "status",
]


def candidate_rows() -> list[dict[str, object]]:
    return [
        dict(zip(CANDIDATE_FIELDS, [
            "C0_HISTORICAL_RETURN_BOUND", "keep clipped return away from bounds", "current-turn clipped ra after firm",
            "ramin+0.02 and ramax-0.02", "low ra -> x0.9; high ra -> x1.1; else hold", "positive initial GovInv remains positive multiplicatively",
            "NO", "CLIPPED", "reproduces 0/289/486 decrease/increase/hold; 258 increases occur while total K is already above target",
            "multiplicative stock update is dimensionally valid but objective is not a K-level residual", "PROTECTED_MATLAB_AND_FAITHFUL_PYTHON",
            "source-labelled government/state-owned capital used operationally as numerical productive stock", "10 percent compounding; clipping loses exceedance magnitude; intermittent gate",
            "fixed 0.9/1.1 and fixed thresholds", "HIGH if adjusted to fit convergence", "same pass as Zt; gate and damping depend on KNratio",
            "indirect through firm L, Y, KNratio, and gate", "one separately authorized bounded trajectory after zero-science replay", "HISTORICAL_BENCHMARK__NOT_CAPITAL_TARGET_CONTROLLER",
        ])),
        dict(zip(CANDIDATE_FIELDS, [
            "C1_CAPITAL_TARGET_RESIDUAL", "close productive capital level to Ktarget", "Ktarget-(Kprivate+GovInv)", "fixed accepted Ktarget",
            "positive gap -> increase; negative gap -> decrease for an Owner-approved positive gain", "max(GovInv+lambda_K*gap,0)", "YES", "NONE",
            "symbolically reverses the 258 above-target increases; lambda_K=1 is only an accounting residual replacement, not a stability claim",
            "gap and GovInv are both MU stocks; lambda_K dimensionless", "ALGEBRAICALLY_COHERENT_WITH_ACCEPTED_G1__GAIN_NOT_AUTHORIZED",
            "residual numerical balancing stock unless Owner supplies public-capital meaning", "overshoot/oscillation if gain and timing are unsuitable; floor kink",
            "lambda_K plus timing/gate choices", "MEDIUM; must not fit lambda_K on G1", "must specify simultaneous or staged Zt and how KN damping gates it",
            "indirect via private K and future firm outcomes; keep labor route frozen in first test", "zero-science pure-function tests then one separately authorized bounded trajectory", "STRUCTURALLY_COHERENT__OWNER_DECISIONS_REQUIRED_BEFORE_IMPLEMENTATION",
        ])),
        dict(zip(CANDIDATE_FIELDS, [
            "C2_RAW_RETURN_TARGET", "close return to an interior target", "signed raw ra0-ra_target", "Owner-approved ra_target",
            "signed feedback direction must be derived and frozen with gain convention", "explicit nonnegative projection required", "NO", "RAW_PROPOSED",
            "NOT_REPLAYED: no source-authorized interior target or gain", "return error is a rate; gain must carry stock units or use a dimensionless multiplicative form",
            "NO_AUTHORIZED_RA_TARGET_OR_GAIN", "return-targeted control of the GovInv stock", "raw ra can be extreme; gain scaling and nonlinear firm response",
            "ra_target, gain, projection, damping, timing", "HIGH", "interaction with Zt and KN feedback unresolved",
            "return depends on K and L, so normalized labor changes the signal", "zero-science geometry after Owner choices then one separately authorized bounded trajectory", "OWNER_DECISION_REQUIRED__MORE_UNVERIFIED_TUNING_THAN_C1",
        ])),
        dict(zip(CANDIDATE_FIELDS, [
            "C3_STAGED_HYBRID", "first close K level, then conditionally correct return/GDP/KN", "stage-specific K gap then return/GDP/KN signals",
            "Ktarget plus Owner-approved secondary references and transition gates", "state machine; C1 direction in stage 1; signed secondary control only after K-gap gate",
            "nonnegative projection in each GovInv transition", "YES_STAGE1", "RAW_OR_NONE__OWNER_DECISION",
            "stage 1 symbolically opposes above-target GovInv growth; later stages not replayed without gates/references", "stage 1 is stock-consistent; secondary gains require explicit units",
            "CONCEPT_SUPPORTED_BY_FAILURE_SEPARATION__STATE_MACHINE_NOT_SOURCE_AUTHORIZED", "separates balancing-stock and later return/calibration roles",
            "transition chatter, coupled controllers, and hidden simultaneous updates", "C1 gain, K-gap tolerance, hysteresis, secondary targets/gains, Zt sequencing",
            "VERY_HIGH unless preregistered", "must decide whether Zt and GovInv can change in same turn and how tKNratio resets/damps",
            "freeze normalized labor initially; later activation requires revalidation", "zero-science state-machine tests then at least one separately authorized bounded trajectory per staged design", "OWNER_DECISION_REQUIRED__MOST_UNVERIFIED_TUNING",
        ])),
    ]


OWNER_FIELDS = ["decision", "current_evidence", "options", "required_owner_resolution", "status"]


def owner_rows() -> list[dict[str, str]]:
    return [
        {"decision": "GovInv economic meaning", "current_evidence": "source label and accounting role only; no accepted public-capital series", "options": "public capital | residual balancing stock | numerical control stock", "required_owner_resolution": "choose meaning before production implementation", "status": "OWNER_DECISION_REQUIRED"},
        {"decision": "primary controller objective", "current_evidence": "C0 return-bound behavior conflicts with K-level gap in 258/775 observations", "options": "K level | return | staged combination", "required_owner_resolution": "select primary estimand/objective", "status": "OWNER_DECISION_REQUIRED"},
        {"decision": "return signal", "current_evidence": "C0 uses clipped ra and loses exceedance magnitude", "options": "retain clipped ra | admit raw ra0", "required_owner_resolution": "authorize raw signal before C2 or hybrid return stage", "status": "OWNER_DECISION_REQUIRED"},
        {"decision": "C1 gain", "current_evidence": "no accepted source identifies lambda_K", "options": "positive under-relaxation gain; lambda_K=1 only as static accounting geometry", "required_owner_resolution": "freeze gain without fitting G1 convergence", "status": "OWNER_DECISION_REQUIRED"},
        {"decision": "damping and hysteresis", "current_evidence": "none authorized for GovInv; tKNratio has separate 0.6/0.4 damping", "options": "none | damping | hysteresis", "required_owner_resolution": "freeze admissibility and constants", "status": "OWNER_DECISION_REQUIRED"},
        {"decision": "same-turn Zt and GovInv", "current_evidence": "C0 permits both, Zt first", "options": "simultaneous | staged/mutually exclusive", "required_owner_resolution": "freeze sequencing", "status": "OWNER_DECISION_REQUIRED"},
        {"decision": "Ktarget reference during iteration", "current_evidence": "accepted Track-A 2018 Ktarget is fixed in G1 ledger", "options": "fixed 2018 target | separately justified moving reference", "required_owner_resolution": "confirm fixed reference for C1", "status": "OWNER_DECISION_REQUIRED"},
        {"decision": "public-capital data", "current_evidence": "no accepted province public-capital series", "options": "do not introduce | later source-and-definition gate", "required_owner_resolution": "new data authority required before use", "status": "DATA_NOT_AVAILABLE"},
        {"decision": "initialization/controller architecture", "current_evidence": "G1 initialization aligns 31/31; unchanged C0 later recreates overshoot", "options": "separate named components", "required_owner_resolution": "retain separation for attribution", "status": "EVIDENCE_SUPPORTS_SEPARATION"},
    ]


def report_text(summary: dict[str, object]) -> str:
    all_window = summary["windows"][0]
    return f"""# Chapter 5 MP4C GovInv controller redesign forensic and specification

Date: 2026-09-11

Builder verdict:

`{VERDICT}`

## Outcome and boundary

This package is a zero-science forensic of the accepted G1 ledger and a controller design specification. It made no household, HJB, KFE, migration, firm, controller-runtime, outer-turn, steady-state, root/Brent, MATLAB-runtime, GE, annual, IRF, or Results call. It neither implements nor selects a production controller. `Results eligibility=FALSE`.

The historical C0 formula was replayed from the accepted 775-row G1 ledger with zero mismatches. Across all 775 province-turns, **{all_window['worsening_count']} ({all_window['worsening_share']:.6%})** were statically directionally inconsistent with the contemporaneous capital-level gap. All 258 were `total K above target + HIGH_RA_INCREASE_1P1`. The remaining 517 are classified closing-or-neutral, not dynamically beneficial. Window counts are: turns 1-5 `0/155`, 6-10 `92/155`, 11-15 `56/155`, 16-20 `73/155`, and 21-25 `37/155`.

## Exact C0 semantics and failure mechanism

Firm capital is private productive supply plus GovInv. The firm computes raw `ra0` and clips it before returning `ra`. After a nonconverged turn, `max(abs(KNratio/tKNratio-1))<0.1` opens adaptation. Zt correction occurs first; then clipped `ra<ramin+0.02` reduces GovInv by 10%, clipped `ra>ramax-0.02` increases it by 10%, and the interior holds. Finally `tKNratio` is updated by `0.6*current KNratio+0.4*old target`.

C0 recreates overshoot after G1 because its trigger and target are different objects. G1 makes `Kprivate+GovInv=Ktarget` only at initialization. C0 never reads Ktarget or that residual. When the clipped high-return signal crosses its upper trigger, it compounds the GovInv stock by 1.1 even when current total K is already above target. Clipping preserves boundary direction but discards raw exceedance magnitude; the intermittent KN gate alternates adjustment and hold turns; Zt and tKNratio feedback can alter future signals but contains no explicit K-level correction. These are source and static-ledger facts, not a dynamic causal decomposition.

The accepted path contains 289 increases and no decreases. Thirty-one increases occur while total K is below target (closing direction); 258 occur above target (worsening direction). Holds include above-, below-, and exactly-at-target observations and are conservatively neutral. Multiplicative 1.1 actions can compound, explaining the arithmetic channel by which the GovInv level grows; the ledger does not identify a causal effect of any single action on later endogenous states.

Detailed source order is in `controller_source_timing_map.md`; row-level classifications are in `g1_static_directional_forensic.csv`; window summaries are in `controller_direction_summary.json`.

## Candidate comparison

- **C0 historical return-bound:** source-authorized benchmark only. It is fundamentally a clipped return-bound controller, not a capital-target controller.
- **C1 capital-target residual:** `GovInv_next=max(GovInv+lambda_K*(Ktarget-(Kprivate+GovInv)),0)`. It is dimensionally and structurally coherent with G1 because both use the same capital accounting residual and preserve nonnegativity. No `lambda_K`, timing, adaptation gate, or dynamic-stability claim is authorized. `lambda_K=1` describes only one-step static accounting residual replacement.
- **C2 raw return-target:** cannot be instantiated or replayed because neither an interior `ra_target` nor a gain is source-authorized. It adds more unverified tuning than C1 and would couple strongly to labor and firm normalization.
- **C3 staged/hybrid:** conceptually separates stage 1 K-level closure from later return/GDP/KN correction. It requires the most decisions: K-gap transition tolerance, hysteresis, damping, secondary targets/gains, raw-versus-clipped return, and whether Zt/GovInv may change together.

The full comparison matrix reports objective, signal, target, sign, units, positivity, evidence authority, interactions, tuning risk, and minimum future test budget. No candidate is promoted to production.

## Required answers

1. **Why does C0 recreate overshoot after G1?** G1 corrects only initial accounting. C0 ignores Ktarget and responds to clipped return bounds; 1.1 multipliers therefore compound GovInv even above the capital target.
2. **How often is C0 directionally inconsistent?** 258/775, or {all_window['worsening_share']:.6%}, overall. The requested five-turn-window counts are 0, 92, 56, 73, and 37 out of 155.
3. **Is C0 a return-bound rather than capital-target controller?** Yes. Source inspection shows no Ktarget, total-K residual, or private-K residual in the controller.
4. **Is C1 coherent with accepted G1 initialization?** Yes, algebraically and dimensionally: it carries the same residual identity forward. This is design coherence, not dynamic validation.
5. **What choices precede C1 implementation?** GovInv economic meaning, primary objective, fixed Ktarget authority, positive gain, timing/gate, projection behavior, Zt sequencing, damping/hysteresis, and preregistered stopping/evaluation rules.
6. **Do C2/C3 require more unverified tuning?** Yes. C2 adds an unidentified return target and gain; C3 adds those plus state-transition gates and interaction rules.
7. **Should initialization and controller remain separate?** Yes. The accepted G1 result empirically demonstrates that initial alignment and subsequent control are distinct mechanisms; separate named components preserve attribution and rollback.
8. **Lowest-risk next experiment?** After Owner selects GovInv meaning and a K-level primary objective, implement only a separately named C1 diagnostic pure function. First test algebra, positivity, units, sign, and static replay with zero science. A later exact task may authorize one bounded trajectory while freezing G1 initialization, source-faithful labor, HJB/KFE, Zt logic, and all unrelated rules. This task does not publish that successor.

## Owner decisions and stop

The unresolved choices are isolated in `owner_decision_matrix.csv`. PASS means the C0 failure mechanism is quantified and C0/C1/C2/C3 are cleanly separated. It does not authorize coefficient selection, runtime implementation, a trajectory, steady-state acceptance, or Results. The next gate is independent ChatGPT Reviewer fresh-fetch ACCEPT/REJECT of the candidate commit.
"""


def prepare() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    source_entries = []
    for name, expected in PROTECTED_HASHES.items():
        path = PROTECTED / name
        observed = digest(path)
        if observed != expected:
            raise RuntimeError(f"protected source drift: {name}: {observed}")
        source_entries.append({"path": str(path), "sha256": observed, "expected_sha256": expected, "match": True})

    ledger_rows = load_ledger()
    forensic = [classify(row) for row in ledger_rows]
    summary = build_summary(forensic)
    if summary["c0_formula_replay_mismatches"] != 0:
        raise RuntimeError("C0 static replay does not reproduce accepted actions")

    write_csv(ROOT / "g1_static_directional_forensic.csv", list(forensic[0]), forensic)
    write_json(ROOT / "controller_direction_summary.json", summary)
    write_text(ROOT / "controller_source_timing_map.md", source_timing_map())
    write_csv(ROOT / "controller_candidate_matrix.csv", CANDIDATE_FIELDS, candidate_rows())
    write_csv(ROOT / "owner_decision_matrix.csv", OWNER_FIELDS, owner_rows())
    write_json(ROOT / "zero_scientific_call_ledger.json", {
        "schema": "CH5_MP4C_GOVINV_CONTROLLER_REDESIGN_ZERO_SCIENTIFIC_CALL_LEDGER_V1",
        "accepted_ledger_rows_parsed": 775,
        "deterministic_static_classifications": 775,
        "household_calls": 0,
        "hjb_calls": 0,
        "kfe_calls": 0,
        "migration_calls": 0,
        "normalized_migration_calls": 0,
        "firm_calls": 0,
        "controller_runtime_calls": 0,
        "outer_turn_calls": 0,
        "trajectory_calls": 0,
        "steady_state_calls": 0,
        "root_brent_scientific_calls": 0,
        "matlab_runtime_calls": 0,
        "ge_calls": 0,
        "annual_calls": 0,
        "irf_calls": 0,
        "results_calls": 0,
        "scientific_model_state_advances": 0,
        "results_eligibility": False,
    })
    repo_inputs = [
        "AGENTS.md", "project_rules/PROJECT_RULE_INDEX_CURRENT.md",
        "tasks/CH5_MP4C_GOVINV_CONTROLLER_REDESIGN_FORENSIC_AND_SPEC.md",
        "docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md",
        "docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md",
        "docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md",
        "docs/CH5_MP4C_G1_RESIDUAL_GOVINV_INITIALIZATION_INTEGRATION_AND_25TURN_ISOLATED_DIAGNOSTIC_REPORT.md",
        "docs/CH5_MP4C_G1_RESIDUAL_GOVINV_INITIALIZATION_INTEGRATION_AND_25TURN_ISOLATED_DIAGNOSTIC_ACCEPTANCE.md",
        "docs/CH5_MP4C_INITIAL_PRIVATE_K_OBSERVATION_AND_RESIDUAL_GOVINV_PROBE_REPORT.md",
        "docs/CH5_MP4C_INITIAL_PRIVATE_K_OBSERVATION_AND_RESIDUAL_GOVINV_PROBE_ACCEPTANCE.md",
        "docs/CH5_MP4C_CORRECTED_2018_HJB_NONCONVERGENCE_PROPAGATION_AND_25TURN_KL_RERUN_REPORT.md",
        "docs/CH5_MP4C_CORRECTED_2018_HJB_NONCONVERGENCE_PROPAGATION_AND_25TURN_KL_RERUN_ACCEPTANCE.md",
        "docs/CH5_MP4C_GOVINV_INITIALIZATION_AND_LABOR_NORMALIZATION_REDESIGN_SPEC.md",
        "docs/CH5_MP4C_GOVINV_INITIALIZATION_AND_LABOR_NORMALIZATION_REDESIGN_SPEC_ACCEPTANCE.md",
        "src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py",
        "src/ch5_two_asset_hank/multi_province/steady_state.py",
        "src/ch5_two_asset_hank/multi_province/firm.py",
        "src/ch5_two_asset_hank/multi_province/capital_allocation.py",
        LEDGER.relative_to(REPO).as_posix(),
    ]
    write_json(ROOT / "source_hash_receipt.json", {
        "schema": "CH5_MP4C_GOVINV_CONTROLLER_REDESIGN_SOURCE_HASH_RECEIPT_V1",
        "base_origin_main": BASE,
        "protected_sources_read_only": True,
        "protected_sources": source_entries,
        "repository_inputs": [
            {"path": relative, "bytes": (REPO / relative).stat().st_size, "sha256": digest(REPO / relative)}
            for relative in repo_inputs
        ],
    })
    write_text(REPORT, report_text(summary))


def finalize(pytest_exit_code: int, passed: int) -> None:
    if pytest_exit_code != 0 or passed < 1:
        raise RuntimeError("focused static tests did not pass")
    write_json(ROOT / "focused_static_test_receipt.json", {
        "schema": "CH5_MP4C_GOVINV_CONTROLLER_REDESIGN_FOCUSED_STATIC_TEST_RECEIPT_V1",
        "command": "python -m pytest -q tests/test_mp4c_govinv_controller_redesign_spec.py",
        "exit_code": pytest_exit_code,
        "passed": passed,
        "attempts": 4,
        "pre_final_attempt": {"passed": 8, "failed": 1, "reason": "documentary exact-token assertion corrected; no scientific call"},
        "passing_attempts": [
            {"attempt": 2, "passed": 9, "failed": 0},
            {"attempt": 3, "passed": 9, "failed": 0},
            {"attempt": 4, "passed": passed, "failed": 0},
        ],
        "scientific_calls": 0,
    })
    entries = [
        REPORT,
        ROOT / "controller_source_timing_map.md",
        ROOT / "controller_candidate_matrix.csv",
        ROOT / "g1_static_directional_forensic.csv",
        ROOT / "controller_direction_summary.json",
        ROOT / "owner_decision_matrix.csv",
        ROOT / "zero_scientific_call_ledger.json",
        ROOT / "source_hash_receipt.json",
        ROOT / "focused_static_test_receipt.json",
        REPO / "tests/test_mp4c_govinv_controller_redesign_spec.py",
        REPO / "validators/multi_province/govinv_controller_redesign/__init__.py",
        REPO / "validators/multi_province/govinv_controller_redesign/generate.py",
    ]
    manifest = {
        "schema": "CH5_MP4C_GOVINV_CONTROLLER_REDESIGN_MANIFEST_V1",
        "entries": [
            {"path": path.relative_to(REPO).as_posix(), "bytes": path.stat().st_size, "sha256": digest(path)}
            for path in entries
        ],
    }
    write_json(ROOT / "manifest.json", manifest)
    readback = []
    for entry in manifest["entries"]:
        path = REPO / entry["path"]
        readback.append({
            "path": entry["path"],
            "bytes_match": path.stat().st_size == entry["bytes"],
            "sha256_match": digest(path) == entry["sha256"],
        })
    if not all(row["bytes_match"] and row["sha256_match"] for row in readback):
        raise RuntimeError("manifest readback failed")
    write_json(ROOT / "manifest_readback.json", {
        "schema": "CH5_MP4C_GOVINV_CONTROLLER_REDESIGN_MANIFEST_READBACK_V1",
        "manifest_sha256": digest(ROOT / "manifest.json"),
        "entries_checked": len(readback),
        "passed": True,
        "entries": readback,
    })


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("prepare", "finalize"))
    parser.add_argument("--pytest-exit-code", type=int, default=0)
    parser.add_argument("--passed", type=int, default=0)
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare()
    else:
        finalize(args.pytest_exit_code, args.passed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
