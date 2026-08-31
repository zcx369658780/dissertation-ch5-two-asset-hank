from __future__ import annotations
import ast, hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE_MAP=ROOT/'validators/multi_province/mp4b_beijing_household_source_map.json'
CONTRACT=ROOT/'validators/multi_province/mp4b_beijing_household_comparator_contract.json'
PYRUN=ROOT/'validators/multi_province/mp4b_beijing_household_parity.py'
MATRUN=ROOT/'validators/multi_province/matlab/mp4b_beijing_household_parity_runner.m'
WRAPPER=ROOT/'validators/multi_province/matlab/mp4b_beijing_household_wrapper.m'

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()
def test_source_map_is_complete_and_exact():
    m=json.loads(SOURCE_MAP.read_text(encoding='utf-8'))
    assert m['marker']=='MP4B_BEIJING_FIRST_TURN_HOUSEHOLD_SAME_INPUT_SOURCE_MAP_PREFLIGHT_PASS'
    assert m['province']=='北京' and m['province_index_zero_based']==0 and m['calendar_year']==2009
    assert not m['ambiguous_execution_critical_fields'] and not m['historical_r5_runtime_dependency'] and not m['second_province_state']
    assert set(m['matlab_bindings']['results']['fields'])=={'prvname','rah','rb','rb_gap','w','tau','Tt','Ct','At','Bt','Lt','Zt','Kt','Kt0','alpha','wjt'}
def test_wrapper_and_runners_have_single_call_structure():
    wrapper=WRAPPER.read_text(encoding='utf-8'); mat=MATRUN.read_text(encoding='utf-8'); py=PYRUN.read_text(encoding='utf-8')
    assert sha(WRAPPER)=='518B0F9137ADA16155EE76EA2A08B21C0B3D91D67C321A2EF89C063B1EAC5AFD'
    assert wrapper.count('manifest = HANK_2ASSETS_HJB(')==1
    assert mat.count("mp4b_beijing_household_wrapper('run'")==1
    assert py.count('result=m.solve_household_steady_state(')==1
    tree=ast.parse(py)
    called={node.func.id for node in ast.walk(tree) if isinstance(node,ast.Call) and isinstance(node.func,ast.Name)}
    called|={node.func.attr for node in ast.walk(tree) if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute)}
    for token in ('HANK_mp_1turn','HANK_mp_1eq','mpHANK_equilibrium_2000','multi_prov_HANK_12sts'):
        assert token not in mat and token not in called
def test_no_overwrite_and_no_r5_imports():
    text=MATRUN.read_text(encoding='utf-8')+PYRUN.read_text(encoding='utf-8')
    assert "fopen(path,'x')" not in text and '.createNewFile()' in text
    assert "path.open('x'" in text and "full.open('xb')" in text
    tree=ast.parse(PYRUN.read_text(encoding='utf-8'))
    imports={alias.name for node in ast.walk(tree) if isinstance(node,ast.Import) for alias in node.names}
    imports|={node.module or '' for node in ast.walk(tree) if isinstance(node,ast.ImportFrom)}
    assert not any(name.startswith(('chapter5_model','ch5_two_asset_hank')) for name in imports)
def test_comparator_is_frozen_at_required_gate():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'))
    assert c['marker']=='MP4B_BEIJING_FIRST_TURN_HOUSEHOLD_COMPARATOR_CONTRACT_FROZEN'
    assert c['scaled_tolerance']==1e-7 and c['mandatory_continuous']==['Ct','Lt','At','Bt','At_plus_Bt']
    assert c['optional_tax_disposition']=='EXCLUDED_NOT_UNIQUELY_SOURCE_BACKED' and not c['tolerance_widening_after_execution']
