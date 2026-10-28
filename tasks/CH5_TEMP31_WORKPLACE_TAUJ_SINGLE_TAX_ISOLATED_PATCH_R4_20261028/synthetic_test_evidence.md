# Exact two-command synthetic budget

| Invocation | Command | Expected | Actual |
|---|---|---|---|
| 1 | python -B validators/multi_province/temp31_worksite_tax_isolated.py --phase legacy | Destination-tax golden rejects unchanged origin-tax history | exit 1; 1 test; 1 assertion failure; 0 errors |
| 2 | python -B validators/multi_province/temp31_worksite_tax_isolated.py --phase candidate | Candidate contract and history golden checks pass | exit 0; 12 tests; 0 failures; 0 errors |

Both claims were saved before invocation; raw output hashes and exit codes are in evidence/test_1_receipt.json and evidence/test_2_receipt.json. Budget is 2/2, with no extra test commands. The first assertion failure is the intended economic counterexample, not a tool error, skipped case or repair of the historical function.

Fixture: C=(1,4), N=(2,3), gross wages=(2,4), destination tau=(0.1,0.3), phi=((1,2),(4,1)), sigma=((0,0.1),(0.2,0)), gamma_c=2, phi_l=1. Destination-tax source-like matrix is ((3.6,0.15),(1,0.525)); unchanged origin-tax history is ((3.6,0.1125),(1.4,0.525)). Invocation 1 exposes 0.1125 versus 0.15. Candidate row sums are (3.75,1.525).

For household labor=(0.5,2), origin mass=(1,6), normalized shares=((18/23,2/9),(5/23,7/9)); flows=((18/23,4/3),(5/23,14/3)), each origin column preserves its mass and national mass is 7. A population doubling test detects an erroneous second N multiplication. Independent row and column permutations, a tax-only swap, same-tax degeneracy, tau=0/sigma=0, non-unit labor elasticity, bad shapes/phi/bases and zero normalizers are checked.

Existing wage.py yields net composites (sqrt(4.24),sqrt(9.12)). Proposed initialization and HJB data share one tuple, retain the raw taxes/wedges separately, and have effective wage exactly equal to that input. Wrong nonzero second tax/wedge construction raises ValueError; an intentionally double-taxed numeric wage fails the equality assertion under assertRaises. These are observed mutation detections, not claims of executed HA behavior.

Outputs report no production imports. Direct file imports avoid package initialization; the new module uses standard-library algebra only. Historical migration/wage imports use the already available NumPy. No solver, empirical loader, installed dependency, real 31-province computation or private dataset was invoked.

Invocation 1 stderr contains a private workspace prefix. Its original bytes remain local and are not a payload. The published stderr replaces only that exact prefix with <ISOLATED_CANDIDATE_ROOT>; transformation hashes/count are in evidence/redaction_record.json. Other stdout/stderr payloads are original captured bytes. Full production initialization/HJB integration and full test suite: NOT_EXECUTED, outside scope.
