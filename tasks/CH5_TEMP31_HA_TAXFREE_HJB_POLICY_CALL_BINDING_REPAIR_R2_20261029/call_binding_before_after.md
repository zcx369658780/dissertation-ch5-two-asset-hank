# Actual call binding and scope proof

Fixed source HJB Blob: fdbde69f6fde448300a9e52f5e67636409272ec8. Before: line14 imports select_temp31_netwage_local_policy, but the single actual call node at line105 names select_matlab_faithful_local_policy. There is no alias binding for that old name. Corrected policy Blob d90eb4ba627d4c702062116c2a4ffadac0f43d86 defines select_temp31_netwage_local_policy at line57.

The only source edit is:
```diff
- policy = select_matlab_faithful_local_policy(...)
+ policy = select_temp31_netwage_local_policy(...)
```
The ellipsis is explanatory only; evidence/hjb_change.diff contains the complete native one-line diff and full unchanged argument list. All positional/keyword expressions, keyword order and target signature match. Restoring only the Name in the repaired AST yields the original entire AST. Exact byte replacement separately proves spacing, newlines, comments and all other tokens unchanged; no broad name normalization is used.

The AST test follows the real Call node to its exact relative import and policy FunctionDef. It also verifies the policy's six corrected-economics imports have actual definitions and are used by real Call nodes. This bounded closure excludes runtime third-party imports, operator assembly and solver execution.

HJB finite differences, resources, boundary logic, operator, iterations, policy/economics formulas, six previous net wage sites and bootstrap19 are unchanged. The byte identity preservation check covers previous published files except the specifically authorized working HJB replacement. Original HJB is preserved in the source commit and evidence/hjb_before.py. No second independent defect was established within this task's static scope.
