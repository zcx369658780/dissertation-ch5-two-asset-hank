from __future__ import annotations
import ast, importlib.util
from pathlib import Path
import pytest

REPO=Path(__file__).resolve().parents[1]
P=REPO/"validators/multi_province/quarterly_hjb_annual_firm_provenance_closure/build.py"
S=importlib.util.spec_from_file_location("closure",P); M=importlib.util.module_from_spec(S); assert S.loader; S.loader.exec_module(M)

def test_no_scientific_imports():
    names={a.name for n in ast.walk(ast.parse(P.read_text(encoding="utf-8"))) if isinstance(n,(ast.Import,ast.ImportFrom)) for a in n.names}
    assert not any(x.startswith(("numpy","scipy","ch5_two_asset_hank","exports","src")) for x in names)

def test_conflict_and_only_truthful_convention():
    assert sum(r["authority"]=="CONFLICTING" for r in M.depreciation())==1
    rows={r["convention"]:r for r in M.conventions()}
    assert rows["Q quarterly HJB"]["status"]=="NOT_SOURCE_CLOSED"
    assert rows["A annual HJB"]["status"]=="NOT_SOURCE_CLOSED"
    assert rows["M abstract model time"]["status"]=="ONLY_TRUTHFUL_CURRENT_CONVENTION"

def test_build_is_fail_closed(tmp_path:Path):
    out=tmp_path/"e"; M.build(out); assert (out/"manifest.sha256").is_file()
    with pytest.raises(FileExistsError): M.build(out)
