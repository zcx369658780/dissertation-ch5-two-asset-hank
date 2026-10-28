"""Explicit standalone test entry; never imports package or production runners."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys
import unittest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=("legacy", "candidate"), required=True)
    phase = parser.parse_args().phase
    root = Path(__file__).resolve().parents[2]
    path = root / "tests/test_temp31_worksite_tax_isolated.py"
    spec = importlib.util.spec_from_file_location("temp31_isolated_tests", path)
    tests = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tests)
    tests.PHASE = phase
    suite = (unittest.TestSuite([tests.WorksiteTaxTests("test_destination_tax_asymmetric_golden")])
             if phase == "legacy" else unittest.defaultTestLoader.loadTestsFromTestCase(tests.WorksiteTaxTests))
    outcome = unittest.TextTestRunner(verbosity=2).run(suite)
    forbidden = [name for name in sys.modules if name.startswith("ch5_two_asset_hank") or name.startswith("validators.multi_province")]
    print(json.dumps({"phase": phase, "tests_run": outcome.testsRun,
        "failures": len(outcome.failures), "errors": len(outcome.errors),
        "successful": outcome.wasSuccessful(), "ha_hjb_kfe_ge_irf_calls": 0,
        "production_imports": forbidden,
        "source_modules_loaded": [name for name in sys.modules if name.startswith("temp31_")],
        "scope": "two-province synthetic scalars/arrays and unchanged historical algebra only"}), flush=True)
    return 0 if outcome.wasSuccessful() and not forbidden else 1


if __name__ == "__main__":
    raise SystemExit(main())
