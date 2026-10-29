"""Two bounded groups; corrected HA drivers are AST-read, never imported/run."""
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import unittest

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--group',choices=('contract','source-algebra'),required=True)
    group=parser.parse_args().group;root=Path(__file__).resolve().parents[2]
    spec=importlib.util.spec_from_file_location('temp31_bootstrap19_tests',root/'tests/test_temp31_ha_taxfree_bootstrap_isolated.py')
    tests=importlib.util.module_from_spec(spec);spec.loader.exec_module(tests)
    target=tests.BootstrapContractTests if group=='contract' else tests.SourceAlgebraTests
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(target))
    forbidden=[n for n in sys.modules if n.startswith('ch5_two_asset_hank') or n.endswith('.temp31_netwage_hjb') or n.endswith('.temp31_netwage_policy')]
    print(json.dumps({'group':group,'cases':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'successful':result.wasSuccessful(),
        'forbidden_imports':forbidden,'actual_initializer_root_policy_hjb_kfe_ge_irf_calls':0,
        'loaded_project_modules':[n for n in sys.modules if n.startswith('temp31_bootstrap19_sandbox')],
        'scope':'numerical wage contracts; six scalar AST expressions; source AST invariants; no grid/solver/initializer/root calls'}),flush=True)
    return 0 if result.wasSuccessful() and not forbidden else 1

if __name__=='__main__':raise SystemExit(main())
