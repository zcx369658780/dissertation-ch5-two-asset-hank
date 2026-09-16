import numpy as np
from scipy import sparse

from ch5_two_asset_hank.corrected_diagnostic.v1_q1_topology import (
    analyze_exact_positive_topology,
    policy_branch,
)


def test_exact_positive_topology_finds_closed_classes_and_reachability() -> None:
    # 0 -> 1, while 1 and 2 are separate closed singleton classes and 3 can
    # reach both.  Diagonal entries are intentionally irrelevant to the graph.
    q = sparse.csr_matrix(
        np.array(
            [
                [-1.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 1.0, -2.0],
            ]
        )
    )

    result = analyze_exact_positive_topology(q)

    assert result["exact_positive_edge_count"] == 3
    assert result["component_count"] == 4
    assert result["closed_members"] == [[1], [2]]
    assert result["transient_state_count"] == 2
    by_member = {
        tuple(node["members"]): node for node in result["condensation"]["nodes"]
    }
    assert by_member[(0,)]["reachable_closed_ordinals"] == [0]
    assert by_member[(3,)]["reachable_closed_ordinals"] == [0, 1]


def test_policy_branch_distinguishes_z_from_directional_candidate() -> None:
    assert policy_branch({"interior_z_receipt": {"marker": "Z"}}) == (
        "INTERIOR_Z_ZERO_LIQUID_SWITCH"
    )
    assert policy_branch({"interior_z_receipt": None}) == (
        "ENUMERATED_DIRECTIONAL_DERIVATIVE_POLICY"
    )
