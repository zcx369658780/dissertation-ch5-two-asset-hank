# Two bounded source-only commands

Both commands run from the isolated candidate root, using the same new test script bytes (SHA-256 recorded in both preclaims). No model module is imported and no initializer, policy or solver is invoked.

1. `python -B tests/test_temp31_hjb_policy_call_binding_r2.py --phase before`
   Predeclared exit1. Actual exit1; 1 test, 1 expected failure, specifically UNBOUND_HJB_POLICY_CALL line=105 symbol=select_matlab_faithful_local_policy. This is a real separate command against the unmodified source, not an internally simulated red phase.
2. `python -B tests/test_temp31_hjb_policy_call_binding_r2.py --phase after`
   Predeclared exit0. Actual exit0; 8 tests passed: actual import/Call/def; old-name mutant detection; exact single-name bytes; remaining AST and argument/order equality; real policy keyword signature; six policy/economics bindings; no extra tax/migration attributes; previous published file byte preservation.

Budget consumed: 2/2. No retries, whole-suite runs or further test commands. Scientific calls 0. Git metadata/diff formatting checks are delivery operations, not numerical tests.

Each invocation has claim, stdout, stderr_public and receipt under evidence/. Private stderr raw bytes are retained LOCAL_ONLY. Public stderr is an exact workspace-prefix replacement; each receipt binds original and public byte counts/SHA-256 and replacement count. Empty stdout files are intentional. The command wrapper's exit0 only means capture matched the predeclared outcome; the real test exits are 1 and 0 as recorded.
