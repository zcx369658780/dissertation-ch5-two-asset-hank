from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest
from scipy import sparse

from ch5_two_asset_hank.corrected_diagnostic import nonlinear_continuation as continuation
from ch5_two_asset_hank.corrected_diagnostic.nonlinear_continuation import (
    FailClosed,
    _restricted_rank_view,
    _terminal_kfe,
    _topology_json_receipt,
)
from ch5_two_asset_hank.corrected_diagnostic import optionb_initial_turn_integration as driver
from ch5_two_asset_hank.corrected_diagnostic.optionb_initial_turn_integration import (
    EXPECTED_C1_BLOB,
    EXPECTED_INITIALIZATION_BLOB,
    EXPECTED_K1A_BLOB,
    EXPECTED_SOURCE_INITIALIZATION_BLOB,
    INITIALIZATION_RELATIVE,
    _blob,
    _checkpoint_diagnostics,
    _check_ledger,
    _local_ledger,
    _new_ledger,
    _predecessor_lineage,
    _terminal_kfe_with_accounting,
    load_initial_states,
    same_s_raw_next_payoff,
)
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER


REPOSITORY = Path(__file__).resolve().parents[1]


def test_exact_initialization_binding_and_state_order() -> None:
    states, receipt = load_initial_states(REPOSITORY)
    assert receipt["status"] == "PASS"
    assert receipt["git_blob"] == EXPECTED_INITIALIZATION_BLOB
    assert receipt["row_count"] == 31
    assert tuple(state["name"] for state in states) == PROVINCE_ORDER
    assert [row["province_index"] for row in receipt["rows"]] == list(range(31))
    assert all(all(row["checks"].values()) for row in receipt["rows"])


def test_published_component_blobs_are_exact() -> None:
    assert _blob(REPOSITORY, INITIALIZATION_RELATIVE) == EXPECTED_INITIALIZATION_BLOB
    assert _blob(REPOSITORY, Path("validators/multi_province/corrected_2018_single_turn/run.py")) == EXPECTED_SOURCE_INITIALIZATION_BLOB
    assert _blob(REPOSITORY, Path("src/ch5_two_asset_hank/multi_province/k1a_runtime_adapter.py")) == EXPECTED_K1A_BLOB
    assert _blob(REPOSITORY, Path("src/ch5_two_asset_hank/multi_province/c1_residual_public_asset.py")) == EXPECTED_C1_BLOB


def test_same_s_raw_payoff_uses_destination_by_origin_orientation() -> None:
    raw = np.arange(31, dtype=float) / 10.0
    shares = np.eye(31)
    shares[:, 0] = 0.0
    shares[1, 0] = 0.25
    shares[2, 0] = 0.75
    result = same_s_raw_next_payoff(raw, shares)
    assert result[0] == 0.25 * raw[1] + 0.75 * raw[2]
    assert np.array_equal(result[1:], raw[1:])


def test_scientific_ledger_accepts_ceiling_and_rejects_overrun() -> None:
    ledger = _new_ledger()
    ledger.update(
        source_native_initializations=31,
        scalar_labor_roots_attempted=24_800,
        scalar_labor_roots_returned=24_800,
        corrected_policy_maps=1_581,
        selector_evaluations=1_264_800,
        d2_q_assemblies=1_581,
        direct_hjb_updates=1_550,
    )
    _check_ledger(ledger)
    ledger["direct_hjb_updates"] += 1
    with pytest.raises(FailClosed):
        _check_ledger(ledger)


def _diagnostic_fixture() -> tuple[list[dict[str, object]], dict[str, np.ndarray], sparse.csr_matrix]:
    rows = [{
        "derivative_branches": {"b": "forward", "a": "backward"},
        "active_constraints": ["a_lower"],
        "transfer_branch": "zero_kink",
        "interior_z_receipt": None,
        "lower_a_zero_kink_multiplier_receipt": None,
    }]
    arrays = {
        name: np.array([[[float(index + 1)]]])
        for index, name in enumerate(("utility", "c", "l", "d", "g_b", "g_a", "q_b", "q_a"))
    }
    return rows, arrays, sparse.csr_matrix([[-1.0, 1.0], [1.0, -1.0]])


def test_checkpoint0_diagnostics_are_current_only_and_comparisons_are_na(monkeypatch) -> None:
    rows, arrays, q = _diagnostic_fixture()
    monkeypatch.setattr(driver, "_policy_diagnostics", lambda *args: pytest.fail("comparative policy helper called"))
    monkeypatch.setattr(driver, "_operator_diagnostics", lambda *args: pytest.fail("comparative operator helper called"))
    policy, operator = _checkpoint_diagnostics(rows, arrays, q, None, None, None)
    assert policy["diagnostic_mode"] == "CURRENT_ONLY__NO_PREVIOUS_CHECKPOINT"
    assert policy["identity_change_count"] is None
    assert policy["previous_checkpoint_comparison"] is None
    assert all(value is None for value in policy["continuous_field_max_abs_change"].values())
    assert set(policy["selected_field_sha256"]) == set(arrays)
    assert operator["diagnostic_mode"] == "CURRENT_ONLY__NO_PREVIOUS_CHECKPOINT"
    assert operator["nnz"] == 4
    assert operator["difference_nnz"] is None
    assert operator["previous_checkpoint_comparison"] is None


def test_checkpoint1_plus_routes_to_existing_comparative_helpers(monkeypatch) -> None:
    rows, arrays, q = _diagnostic_fixture()
    calls = []
    monkeypatch.setattr(driver, "_policy_diagnostics", lambda *args: calls.append("policy") or {"mode": "comparative"})
    monkeypatch.setattr(driver, "_operator_diagnostics", lambda *args: calls.append("operator") or {"mode": "comparative"})
    policy, operator = _checkpoint_diagnostics(rows, arrays, q, rows, arrays, q)
    assert calls == ["policy", "operator"]
    assert policy == {"mode": "comparative"}
    assert operator == {"mode": "comparative"}


def test_partial_previous_checkpoint_state_fails_closed() -> None:
    rows, arrays, q = _diagnostic_fixture()
    with pytest.raises(FailClosed, match="BLOCKED__PARTIAL_PREVIOUS_CHECKPOINT_DIAGNOSTICS_STATE"):
        _checkpoint_diagnostics(rows, arrays, q, rows, None, q)


def test_predecessor_run001_lineage_is_preserved_read_only() -> None:
    receipt = _predecessor_lineage(REPOSITORY)
    assert receipt["status"] == "PASS"
    assert receipt["run001_run002_files_modified"] is False
    assert receipt["run001"]["historical_scientific_ledger"]["corrected_policy_maps"] == 1
    assert receipt["run001"]["historical_scientific_ledger"]["direct_hjb_updates"] == 0
    assert receipt["run002"]["sealed_scientific_ledger"]["scc_decompositions"] == 0
    assert receipt["run002"]["actual_scc_decompositions"] == 1


def test_topology_projection_is_explicit_json_safe_and_zero_science(monkeypatch) -> None:
    monkeypatch.setattr(
        continuation,
        "analyze_exact_positive_topology",
        lambda *_args, **_kwargs: pytest.fail("SCC topology helper called by projection"),
    )
    monkeypatch.setattr(
        continuation.linalg,
        "svd",
        lambda *_args, **_kwargs: pytest.fail("SVD called by projection"),
    )
    topology = {
        "adjacency": sparse.csr_matrix(([1, 1], ([0, 1], [1, 0])), shape=(2, 2)),
        "labels": np.array([0, 0], dtype=np.int32),
        "exact_positive_edge_count": 2,
        "component_count": 1,
        "component_sizes": [2],
        "closed_labels": [0],
        "closed_members": [[0, 1]],
        "closed_class_count": 1,
        "transient_state_count": 0,
        "condensation": {
            "edge_count": 0,
            "edges": [],
            "nodes": [{
                "label": 0,
                "members": [0, 1],
                "successors": [],
                "reachable_closed_ordinals": [0],
            }],
        },
    }
    receipt = _topology_json_receipt(topology)
    assert json.loads(json.dumps(receipt, allow_nan=False)) == receipt
    assert receipt["component_count"] == 1
    assert receipt["closed_members"] == [[0, 1]]
    assert receipt["condensation"] == topology["condensation"]
    assert receipt["adjacency_csr"]["shape"] == [2, 2]
    assert receipt["adjacency_csr"]["nnz"] == 2
    assert set(receipt["adjacency_csr"]["identity"]) == {"data", "indices", "indptr"}
    assert receipt["labels"]["length"] == 2
    assert len(receipt["labels"]["sha256"]) == 64
    assert _topology_json_receipt(topology) == receipt


def test_terminal_kfe_success_accounting_accumulates_once(monkeypatch, tmp_path) -> None:
    local = _local_ledger()
    ledger = _new_ledger()

    def stub(*_args):
        local["terminal_topology_gates"] += 1
        local["terminal_restricted_dense_gesvd"] += 1
        local["terminal_normalized_stationary_candidates"] += 1
        local["terminal_q_transpose_times_p"] += 1
        return {"status": "PASS"}

    monkeypatch.setattr(driver, "_terminal_kfe", stub)
    result = _terminal_kfe_with_accounting(
        1, sparse.eye(2, format="csr"), 0.0, tmp_path, local, ledger
    )
    assert result == {"status": "PASS"}
    assert ledger["scc_decompositions"] == 1
    assert ledger["restricted_dense_scipy_linalg_svd_gesvd"] == 1
    assert ledger["full_space_800_dense_scipy_linalg_svd_gesvd"] == 0
    assert ledger["normalized_stationary_candidates"] == 1
    assert ledger["q_transpose_times_p"] == 1


def test_terminal_kfe_exception_accounting_preserves_consumed_calls(monkeypatch, tmp_path) -> None:
    local = _local_ledger()
    ledger = _new_ledger()

    def stub(*_args):
        local["terminal_topology_gates"] += 1
        raise RuntimeError("after SCC")

    monkeypatch.setattr(driver, "_terminal_kfe", stub)
    with pytest.raises(RuntimeError, match="after SCC"):
        _terminal_kfe_with_accounting(
            1, sparse.eye(2, format="csr"), 0.0, tmp_path, local, ledger
        )
    assert ledger["scc_decompositions"] == 1
    assert ledger["restricted_dense_scipy_linalg_svd_gesvd"] == 0
    assert ledger["full_space_800_dense_scipy_linalg_svd_gesvd"] == 0
    assert ledger["normalized_stationary_candidates"] == 0
    assert ledger["q_transpose_times_p"] == 0


def _synthetic_unique_closed_topology(closed_members=(0, 1)) -> dict[str, object]:
    labels = np.ones(800, dtype=np.int32)
    labels[list(closed_members)] = 0
    return {
        "adjacency": sparse.csr_matrix((800, 800)),
        "labels": labels,
        "exact_positive_edge_count": 0,
        "component_count": 2,
        "component_sizes": [len(closed_members), 800 - len(closed_members)],
        "closed_labels": [0],
        "closed_members": [list(closed_members)],
        "closed_class_count": 1,
        "transient_state_count": 800 - len(closed_members),
        "condensation": {"edge_count": 0, "edges": [], "nodes": []},
    }


def _synthetic_q() -> sparse.csr_matrix:
    q = sparse.lil_matrix((800, 800), dtype=float)
    q[0, 0], q[0, 1] = -1.0, 1.0
    q[1, 0], q[1, 1] = 1.0, -1.0
    return q.tocsr()


def test_restricted_rank_gate_uses_local_and_inherited_thresholds() -> None:
    values = np.array([2.0, 1.0, 0.0])
    local = _restricted_rank_view(values, 3, 3)
    inherited = _restricted_rank_view(values, 800, 3)
    assert (local["numerical_rank"], local["numerical_nullity"]) == (2, 1)
    assert (inherited["numerical_rank"], inherited["numerical_nullity"]) == (2, 1)
    assert inherited["tau_rank"] > local["tau_rank"]


def test_terminal_kfe_unique_closed_support_exactly_once_and_zero_transient(
    monkeypatch, tmp_path
) -> None:
    topology_calls = 0
    svd_shapes = []
    original_svd = continuation.linalg.svd

    def topology(_q):
        nonlocal topology_calls
        topology_calls += 1
        return _synthetic_unique_closed_topology()

    def svd(matrix, **kwargs):
        svd_shapes.append(matrix.shape)
        return original_svd(matrix, **kwargs)

    monkeypatch.setattr(continuation, "analyze_exact_positive_topology", topology)
    monkeypatch.setattr(continuation.linalg, "svd", svd)
    local = _local_ledger()
    receipt = _terminal_kfe(1, _synthetic_q(), 1e-12, tmp_path, local)
    assert receipt["status"] == "PASS"
    assert topology_calls == 1
    assert svd_shapes == [(2, 2)]
    assert local["terminal_restricted_dense_gesvd"] == 1
    assert local["terminal_full_space_dense_gesvd"] == 0
    assert local["terminal_q_transpose_times_p"] == 1
    with np.load(tmp_path / "terminal_kfe/stationary_mass_arrays.npz", allow_pickle=False) as archive:
        p = archive["p"]
        assert np.all(p[:2] > 0.0)
        assert np.array_equal(p[2:].view(np.uint64), np.zeros(798, dtype=np.uint64))


def test_terminal_kfe_multiple_closed_classes_fails_before_svd(monkeypatch, tmp_path) -> None:
    topology = _synthetic_unique_closed_topology()
    topology["closed_members"] = [[0], [1]]
    topology["closed_class_count"] = 2
    monkeypatch.setattr(continuation, "analyze_exact_positive_topology", lambda _q: topology)
    monkeypatch.setattr(
        continuation.linalg, "svd", lambda *_a, **_k: pytest.fail("SVD must not run")
    )
    with pytest.raises(FailClosed, match="TERMINAL_TOPOLOGY_OR_KFE_GATE"):
        _terminal_kfe(1, _synthetic_q(), 1e-12, tmp_path, _local_ledger())


def test_terminal_kfe_strict_positive_closed_support_gate(monkeypatch, tmp_path) -> None:
    monkeypatch.setattr(
        continuation, "analyze_exact_positive_topology", lambda _q: _synthetic_unique_closed_topology()
    )

    def nonpositive_candidate(_matrix, **_kwargs):
        return np.eye(2), np.array([2.0, 0.0]), np.array([[0.0, 1.0], [1.0, 0.0]])

    monkeypatch.setattr(continuation.linalg, "svd", nonpositive_candidate)
    with pytest.raises(FailClosed) as failure:
        _terminal_kfe(1, _synthetic_q(), 1e-12, tmp_path, _local_ledger())
    assert failure.value.detail["stage"] == "restricted_candidate_or_embedding"
