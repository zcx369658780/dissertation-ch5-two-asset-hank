from pathlib import Path

import numpy as np

from validators.multi_province.turn2_heilongjiang_f0063_negative_derivative_emergence_forensic import run


REPO=Path(__file__).resolve().parents[1]


def test_sha_chain_and_derivative_receipts_are_exact():
    states=run.load_states(REPO); chain=run.artifact_chain(REPO,states)
    assert chain["manifest_identity_pass"]
    assert all(x["matches_manifest"] for x in chain["relevant_artifacts"])
    assert all(x["exact"] for x in chain["links"])
    for n in range(4):
        receipt=__import__("json").loads((REPO/run.PROVINCE/f"checkpoint_{n:03d}/derivative_receipt.json").read_text(encoding="utf-8"))
        fields=run.reconstruct(states[f"checkpoint{n}"])
        assert receipt["derivative_sha256"]=={k:run.field_sha256(v) for k,v in fields.items()}


def test_first_negative_edges_appear_only_at_checkpoint3():
    states=run.load_states(REPO); rows={k:run.census(v) for k,v in states.items()}
    assert rows["checkpoint0"]["distinct_negative_b_edges"]==0
    assert rows["checkpoint1"]["distinct_negative_b_edges"]==0
    assert rows["checkpoint2"]["distinct_negative_b_edges"]==0
    assert rows["checkpoint3"]["distinct_negative_b_edges"]==2
    assert rows["checkpoint3"]["sign_patterns"]["interior_b"]=={"(+,+)":716,"(<=0,+)":2,"(+,<=0)":2,"(<=0,<=0)":0}
    assert rows["checkpoint3"]["first_f_order_flat_with_any_nonpositive"]==62


def test_f0062_f0063_and_direct_solve_residual_parity():
    states=run.load_states(REPO); fields=run.reconstruct(states["checkpoint3"])
    assert fields["p_b_forward"][2,3,0]==-0.0002428532863339202
    assert fields["p_b_backward"][3,3,0]==-0.0002428532863339202
    for n in range(3):
        receipt=run.direct_update_receipt(REPO,n)
        assert receipt["next_value_exact_target_identity"]
        assert receipt["recomputed_residual_bitwise_equal_saved"]
        assert receipt["all_persisted_identity_hashes_exact"]
        assert receipt["all_persisted_scalars_consistent_within_8eps_scaled_bound"]
    local=run.local_rows(REPO)["interface"]
    assert local["no_cross_interface_matrix_coupling"]
    assert local["checkpoint2_selected_drifts_point_away_from_interface"]
    assert local["finite_difference"]==-0.0002428532863339202


def test_forensic_does_not_import_production_or_call_solvers():
    source=(REPO/"validators/multi_province/turn2_heilongjiang_f0063_negative_derivative_emergence_forensic/run.py").read_text(encoding="utf-8")
    assert "from ch5_two_asset_hank" not in source
    assert "import ch5_two_asset_hank" not in source
    assert "spsolve(" not in source
    assert "scipy" not in source
