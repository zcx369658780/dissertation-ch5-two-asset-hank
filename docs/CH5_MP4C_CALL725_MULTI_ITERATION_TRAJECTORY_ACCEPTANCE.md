# Reviewer acceptance: call-725 trajectory diagnosis
Date: 2026-09-07
Candidate: dedd0f8e5fa894b83c8b20e522d66893e7b6b377.
Review main: 373264625f0f9580575cda5a36d7a70b371a040b.
Decision: accept COMPLETE diagnostic deliverable and TRAJECTORY_DIVERGENCE_WITH_COMMON_STATE_PARITY_PASS in its stated scope. Full trajectory parity and convergence acceptance are NOT granted.

Reviewed21 added files' scope; inspected report, capture/generator/launcher/comparison/postprocessing code, test source, result/ledger/integrity/state/manifest and common-state/stage summaries. No production source changed. Candidate is one commit ahead, zero behind review main.
Independently ran four portable tests: sparse support/no densification and numbering; state/stop capture; Python parse/trace newline; exact synthetic MAT/sparse roundtrip. All four passed. Two source-preservation tests need external Windows predecessor wrappers and were not rerun here; Builder reports six total tests and MATLAB checkcode pass. Reviewer did not read Windows raw MAT/NPZ or rerun models. Acceptance is L3 repository/report evidence with these independently executed focused checks.

Accepted facts:
- First generated beyond-bound difference: step2 consumption,519 coordinates,max abs1.3500311979441904e-11.
- Small incoming differences can pass the derivative bound and still amplify through consumption arithmetic. The local derivative-to-consumption reconstruction supports this particular finding.
- Common MATLAB pre-step2 state:38/38 cross-language comparisons pass. This does not prove all later common states pass.
- First beyond-bound incoming V: step4; first transfer-label and BB support split:step24.
- At100 neither converges. MATLAB converges143 at1.0492009705487249e-8; Python500 remains0.008617352704437531.
- Stored linear backward errors are small, but large operator scales and divergent nonlinear trajectories remain unresolved. No blanket scientific/numerical-validity PASS.
- Calls: MATLAB2 invocations/144 solves; Python2/501; retry0; downstream0. Reviewer model calls0.

The finalizer contains task-specific literal earliest-step facts; these agree with the inspected supporting summaries but are not generic verdict logic for successors.
Next: tasks/CH5_MP4C_CALL725_POLICY_OPERATOR_STABILITY.md. No additional production change or long trajectory is authorized by this acceptance itself. Original Builder report is preserved.
