"""Explicit provenance/algebra test groups; does not load production packages."""
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import unittest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--group", choices=("provenance", "algebra"), required=True)
    group = parser.parse_args().group
    root = Path(__file__).resolve().parents[2]
    path = root / "tests/test_temp31_ha_wage_debug_isolated.py"
    spec = importlib.util.spec_from_file_location("temp31_ha_debug_tests", path)
    tests = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tests)
    target = tests.ProvenanceGuardTests if group == "provenance" else tests.ConsumerAlgebraTests
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(target))
    forbidden = [name for name in sys.modules if name.startswith("ch5_two_asset_hank") or name.startswith("validators.multi_province")]
    print(json.dumps({"group": group, "tests_run": result.testsRun, "failures": len(result.failures),
        "errors": len(result.errors), "successful": result.wasSuccessful(),
        "production_imports": forbidden, "ha_hjb_kfe_ge_irf_calls": 0,
        "source_modules_loaded": [name for name in sys.modules if name.startswith("temp31_ha_debug_sandbox")],
        "scope": "synthetic 2/3 province formula/data/resource identities; no actual consumers"}), flush=True)
    return 0 if result.wasSuccessful() and not forbidden else 1


if __name__ == "__main__":
    raise SystemExit(main())
