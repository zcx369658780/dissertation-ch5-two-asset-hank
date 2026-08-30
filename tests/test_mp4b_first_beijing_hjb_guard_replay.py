from pathlib import Path
import ast
import numpy as np

from validators.multi_province.mp4b_first_beijing_hjb_guard_replay import _first_nonpositive


SOURCE=Path(__file__).parents[1]/"validators"/"multi_province"/"mp4b_first_beijing_hjb_guard_replay.py"


def test_synthetic_stop_uses_k_j_i_order_and_detects_before_policy():
    vf=np.ones((3,2,2)); vb=np.ones((3,2,2))
    vf[2,0,0]=0; vb[0,1,0]=-1; vf[0,0,1]=-2
    assert _first_nonpositive(vf,vb)==(2,0,0)


def test_replay_has_no_downstream_imports_and_stop_precedes_policy_call():
    text=SOURCE.read_text(encoding="utf-8"); tree=ast.parse(text)
    forbidden=("solve_household_steady_state","run_online_stationary","solve_kfe",
        "run_one_turn","run_manual_fixed_point")
    called={node.func.id for node in ast.walk(tree) if isinstance(node,ast.Call) and isinstance(node.func,ast.Name)}
    assert not called.intersection(forbidden)
    assert text.index("if idx is not None:") < text.index("policy=select_matlab_faithful_local_policy")
    assert "range(1,101)" in text and '"traversal_order":"k,j,i"' in text
