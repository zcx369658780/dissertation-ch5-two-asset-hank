import ast
import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import sys

import numpy as np
from scipy import sparse


EXPORT = Path(__file__).parents[1] / "exports" / "matlab_faithful_two_asset_ha.py"
SPEC = importlib.util.spec_from_file_location("standalone_ha", EXPORT)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_dependency_and_public_api_boundary():
    tree = ast.parse(EXPORT.read_text(encoding="utf-8"))
    imports = {node.names[0].name.split(".")[0] for node in tree.body if isinstance(node, ast.Import)}
    from_imports = {node.module.split(".")[0] for node in tree.body if isinstance(node, ast.ImportFrom) and node.module != "__future__"}
    assert imports | from_imports <= {"dataclasses", "numpy", "scipy"}
    assert "ch5_two_asset_hank" not in EXPORT.read_text(encoding="utf-8")
    required = {"solve_matlab_faithful_hjb", "solve_matlab_faithful_stationary_kfe", "aggregate_stationary_household", "solve_household_steady_state"}
    assert required <= set(MODULE.__all__)
    assert not any("ge" in name.lower() or "dynamic" in name.lower() for name in MODULE.__all__)


def test_clean_room_import(tmp_path):
    target = tmp_path / EXPORT.name
    shutil.copy2(EXPORT, target)
    env = os.environ.copy(); env.pop("PYTHONPATH", None)
    code = "import importlib.util,sys; s=importlib.util.spec_from_file_location('matlab_faithful_two_asset_ha','matlab_faithful_two_asset_ha.py'); m=importlib.util.module_from_spec(s); sys.modules[s.name]=m; s.loader.exec_module(m); assert 'solve_household_steady_state' in m.__all__; assert not any(x.startswith('ch5_two_asset_hank') for x in sys.modules)"
    subprocess.run([sys.executable, "-I", "-c", code], cwd=tmp_path, env=env, check=True)


def test_bare_a_foc_and_taper():
    p = MODULE.EconomicParams(.05, 2., 1., .1, 2., 1e-6, 0., 0.)
    assert MODULE.transfer_candidate(1.5, 1., 0., p) == 0.
    result = MODULE.matlab_faithful_illiquid_return(np.array([0., 1., 2.]), 2., .04)
    assert result[0] == .04 and result[2] == .04 * (1. - .1)
    assert .036 < result[1] < .04


def test_source_axis_boundary_truncation_and_kfe_contract():
    backward = np.zeros((2, 2, 1)); forward = np.zeros_like(backward)
    backward[0, 0, 0] = 2.; forward[1, 0, 0] = 3.
    matrix = MODULE.assemble_source_axis(backward, forward, 0).toarray()
    assert matrix[0, 0] == -2. and np.count_nonzero(matrix[0]) == 1
    assert matrix[1, 1] == -3. and np.count_nonzero(matrix[1]) == 1
    assert MODULE.matlab_contaminated_row_index(50) == 17
    operator = sparse.csr_matrix(np.array([[-1., 1., 0.], [1., -2., 1.], [0., 1., -1.]]))
    kfe = MODULE.solve_matlab_faithful_stationary_kfe(operator, shape=(3, 1, 1), db=.5, da=.25)
    assert np.sum(kfe.density_vector) * kfe.cell_weight == 1.


def test_aggregate_weighting_and_fortran_broadcasting():
    grid = MODULE.MatlabFaithfulHJBGrid(np.array([-1., 1.]), np.array([0., 2.]), np.array([1., 3.]), np.zeros((2, 2)))
    shape = (2, 2, 2); g = np.ones(shape); C = np.arange(8., dtype=float).reshape(shape, order="F"); labor = np.ones(shape)
    q = MODULE.aggregate_stationary_household(grid, C, labor, g)
    weight = 4.
    assert q.c_ss == np.sum(C) * weight
    assert q.l_ss == np.sum(np.broadcast_to(grid.z[None, None, :], shape)) * weight
    assert q.a_ss == np.sum(np.broadcast_to(grid.a[None, :, None], shape)) * weight
    assert q.b_ss == np.sum(np.broadcast_to(grid.b[:, None, None], shape)) * weight
    assert q.total_assets == q.a_ss + q.b_ss
