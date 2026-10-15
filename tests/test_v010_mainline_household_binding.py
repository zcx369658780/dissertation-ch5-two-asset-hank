import inspect
import json
from pathlib import Path
import numpy as np
import pytest
from ch5_two_asset_hank.multi_province.mainline_household_runtime import (
    HAInputs, initial_labor_foc, make_grid, solve_conditioned_household,
)

FIXTURE=Path(__file__).parent/'fixtures/v010_mainline_synthetic_v1.json'


def test_frozen_fixture_git_blob():
    import hashlib
    raw=FIXTURE.read_bytes()
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() == '40915658d93403cfc21b33a6b864b332b7857749'


def test_grid_and_layout_without_solver():
    f=json.loads(FIXTURE.read_text(encoding='utf-8')); g=make_grid(f['grid'])
    assert g.shape == (20,20,2)
    assert g.b[0] == -2 and g.b[-1] == 5 and g.a[-1] == 10
    assert np.ravel_multi_index((1,0,0),g.shape,order='F') == 1
    assert np.ravel_multi_index((0,1,0),g.shape,order='F') == 20


def test_independent_exact_labor_foc_income():
    # c=l=u=1, R=0 is an exact oracle for gamma=2, phi=5, alpha_l=1.
    p={'alphal':1,'phi_l':5,'gamma_c':2}
    assert initial_labor_foc(1,u=1,resources=0,parameters=p) == 0
    assert initial_labor_foc(2,u=1,resources=0,parameters=p) > 0


def test_no_second_tax_or_seed_runner_execution():
    source=inspect.getsource(solve_conditioned_household)
    assert "inputs.w_eff*z" in source
    assert '1.0 - inputs' not in source
    assert 'bind_option_a_inputs(' not in source and 'loadmat(' not in source
    assert 'execute(' not in source


def test_bad_wage_rejected_without_HA():
    f=json.loads(FIXTURE.read_text(encoding='utf-8'))
    with pytest.raises(ValueError,match='wage'):
        HAInputs(.02,.06,0,.1,.07,f['parameters'],f['grid']).validate()
