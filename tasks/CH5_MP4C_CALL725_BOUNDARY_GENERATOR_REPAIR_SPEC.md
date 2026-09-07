# Call-725 boundary/generator repair specification and drift witnesses

Date: 2026-09-07.
Task: CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC.
Repository: zcx369658780/dissertation-ch5-two-asset-hank.
Issuer: Reviewer under Owner standing authorization.
Accepted predecessor: 2ff3eb212ea9a0d101183f9ff49dd1043bb6b886.
Acceptance: docs/CH5_MP4C_CALL725_FROZEN_LINEAR_SYSTEM_ATTRIBUTION_ACCEPTANCE.md.
Must be active on live main. Publication is not execution or approval of a new scientific law.

## Goal
Produce one implementation-ready, evidence-backed proposal for the legacy boundary/generator problems, with explicit authority decisions and future tests. Complete the selected saved-array analysis, local algebraic witnesses, relevant synthetic tests, specification and report in this task. Do not return another generic recommendation to inspect boundaries.
The P32 crossed-linear-system question is already complete: fixed-input solver-path differences and input sensitivity coexist; prescribed row scaling is not a general repair. Do not repeat it. The remaining route must distinguish source fidelity, admissible policies, generator conservation, floating representation and nonlinear convergence.
This task designs a repair; it does not adopt it. Owner retains final authority for economic/FOC/boundary-law choices. No need to interrupt this design task merely because its final proposal contains such choices: state the unresolved alternatives and recommend one with reasons.

## Startup and protected scope
Work in D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001, using an isolated worktree only if needed to preserve unrelated dirty work. Fetch and record live main, remote/HEAD/status. Read AGENTS, rule index, current status, this task, the two most recent diagnostic reports/acceptances, and relevant local-file and scientific-route rules. Reuse unchanged historical evidence; do not repeat full-history audits or local documentation sync.
Create branch codex/ch5-call725-boundary-generator-repair-spec-20260907 from effective current main. Preserve historical branches, D:\ResearchCode\dissertation-ch5-two-asset-hank and its unrelated files. No reset/clean/stash/force-push. Do not change Zotero/global/model/provider configuration.
New evidence root: D:\ProjectTemp\ch5-call725-boundary-generator-repair-spec-20260907-001; choose a fresh suffix if occupied and pass the actual root consistently. Earlier evidence roots remain read-only.
Frozen Python export blob:9e7dc9556a2b76811e78f89999abecc045886106.
Protected HJB SHA256:049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE.
Scalar binding SHA256:A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6.
These are read-only source authorities, not modules to execute. Read relevant helper/extracted-wrapper text and source locations only; no source-directory archaeology or production imports.

## A. Bind existing evidence; no regeneration
Read-only roots:
- D:\ProjectTemp\ch5-call725-frozen-linear-system-20260907-001 (final manifest SHA256 A0FF925E71273345043ACE4F666E07A4C990116E7F7BF6BDC1011853A1C64BDD).
- D:\ProjectTemp\ch5-call725-policy-operator-stability-20260907-001 (manifest SHA256 EB213BD4174AB1145A332674D5D49326A7A5B4B51C17839524DA12A992203C23).
- D:\ProjectTemp\ch5-call725-multi-iteration-trajectory-20260907-001 (artifact_inventory.json SHA256 6D77926997A566E94FE3F016E2BD632042D22276D20D07997DCAB287749E46FC).
Verify the manifest/readback relationships and consumed entries only. Old CURRENT-document hashes refer to their historical commits, not live revised documents. Publish a compact consumed-input receipt. Never reconstruct inputs from rounded report numbers.

Fixed snapshot scope:
1. Both saved language outputs for each common-state replay M24, P24, P32, M143_FINAL in the policy/operator root: matlab_<case>/step_0001.mat and python_<case>/step_0001.npz plus its stored sparse companions.
2. Original trajectory MATLAB steps52 and57; Python steps146,401,424,500, using their persisted dense/sparse outputs.
Use original fields and F-order association from the accepted schema. M143_FINAL replay input is the post-step143 terminal value, not the preceding iterate. Do not chain states or substitute checkpoints.
Reuse existing all-trajectory generator summaries and tail-switch coordinates; do not recalculate all643 steps. The selected14 snapshots are the maximum real-state scope, not14 new evaluations. Missing authoritative files make affected witnesses incomplete; complete independent valid sections without regeneration or replacement states.

## B. Concrete source-to-policy-to-generator witnesses
For each selected stored operator, compare its action on the coordinate functions with the persisted economic drifts:
- b_grid has the saved liquid coordinate at each (b,a,z); compute A @ vec_F(b_grid).
- a_grid has the saved illiquid coordinate; compute A @ vec_F(a_grid).
- Compare those vectors to saved mu_b and mu_a. Independently reconstruct the local budget drifts from the saved consumed c,l,d,cost, effective return and exact binding. Preserve all three objects: budget drift, captured drift, operator-implied drift.
Sparse matvecs/reductions on saved arrays are allowed; no evaluator or solve. Attribute discrepancies to actual source expressions: consumed versus shadow transfer candidates, split cash-flow channels, forced upper-b labels, upper-a rate replacement, or omitted grid-exterior edges. A net inward budget drift does not by itself certify that every split rate is nonnegative; show the component contributions rather than assuming equivalence.

Record all selected-snapshot negative off-diagonal rows, omitted outward-rate rows and materially different drift rows in a compact machine-readable table, with a small representative witness set in prose. Include coordinates, face/corner classification, sparse neighbors/rates/diagonal, controls, relevant derivative operands, source line locations, signed branch margins, reconstruction checks and provenance. New source-formula reconstruction is not independent runtime capture. Keep prior label-derived mask caveats.
Cover the known upper-a and upper-b failures, all eight (b,a) corner/productivity combinations as relevant to each snapshot, the worst-rate states, the MATLAB terminal state, and the reported two tail-switch coordinates. Do not claim continuous-state or full-grid refinement validity from these snapshots.

Derive a local feasibility witness where present: with nonnegative off-diagonal rates and zero row sum on a closed finite grid, A applied to a coordinate at its maximum cannot be positive, and at its minimum cannot be negative. Compare this necessary condition with the captured budget drift. Identify whether preserving that drift and imposing a conservative nonnegative generator are simultaneously possible without changing a boundary policy or truncation treatment. This is an algebraic diagnostic, not permission to enforce a new boundary law.
Separate genuine missing outgoing edges from cancellation in stored sums; use compensated or Decimal arithmetic only where needed, reusing accepted pure diagnostics. The P32 interior norm-driving row704 and its lost sigma remain a separate representation/interior-policy concern; a boundary proposal must explicitly say what it does NOT resolve.

## C. Repair contract and minimum scientific decisions
Deliver a source-versus-proposal table for each necessary change, labelled CURRENT_FROZEN_AUTHORITY, DERIVED_IDENTITY, PROPOSED_REQUIRES_SCIENTIFIC_DECISION or UNRESOLVED. Cite exact repository/source evidence. Existing corrected KKT/R1/R4 material may be consulted only when directly relevant, after stating its present authority; do not reactivate an old runtime or restart those phases.

The specification must address:
- Economic lower bounds versus artificial upper truncations. Do not silently treat a finite upper grid as a newly assumed economic borrowing/saving limit, or silently choose reflecting/absorbing boundaries.
- Local budget feasibility at each face and jointly at corners; where a state-constraint closure is proposed, give its Hamiltonian/KKT conditions, multiplier signs, active/slack alternatives, consumption/labor/transfer coupling and zero-transfer kink treatment. This is a written derivation, not a root solve or implementation of a replacement selector.
- Consistency between the control used in utility/budgets and the drift used in the operator. Explain whether retaining the source's separate flow upwinding is compatible with the proposed closure; replacing it with total-drift upwinding is a finite-grid discretization change, not automatically an exact refactor.
- Treatment of omitted outward edges and diagonal contributions under the proposed truncation law. For a proposed closed conservative finite-state generator, explicitly require nonnegative off-diagonals and diagonal equal to minus the retained outgoing-rate sum in mathematical arithmetic. Separate floating residual budgets from mathematical identities; no tolerance fitted to current failures.
- Transfer FOC denominator and adjustment-cost consistency: explain what frozen arithmetic does, the domain on which the FOC is justified, and whether an additional scientific choice is needed. Do not introduce a derivative floor, transfer cap, or replace bare-a by max(a,a_bar) merely to stabilize the run. Separate this issue from boundary-only changes.
- Numerical representation: carry forward sigma loss and original-unit residual findings. No post-hoc diagonal patch, nextafter inflation, damping or solver replacement is approved. Do not promise that changing boundaries alone repairs the extreme interior state or the500-step convergence gap.

Compare at most three serious options: continued frozen-source reproduction as a diagnostic reference; the smallest mathematically consistent boundary/discretization repair supported by the witnesses; and a broader constrained-policy/FOC repair only if the evidence shows the smaller scope insufficient. Recommend one implementation scope, list its tradeoffs and exclusions, and isolate only the genuinely unresolved Owner decisions. If existing current authority already resolves a choice, cite it rather than asking Owner again. Recommendations are not adopted scientific authority.

Give a concrete future changed-file/API plan that preserves the frozen MATLAB-faithful reference, plus a proposed bounded validation sequence. The future sequence should combine implementation, relevant tests and authorized runs into one work unit when possible; it is a proposal, not execution authority in this task.
Specify tests for faces/corners and active/slack cases, budget/operator drift association, nonnegative conservative generator assembly, interior behavior under the chosen discretization, and stable numerical diagnostics. Distinguish unchanged-source parity tests from redesigned-target correctness tests: do not require a corrected policy to match a known invalid legacy boundary, and do not silently remove the old failed parity rows. Keep the existing128-eps comparison for unchanged same-object checks. Any new correctness tolerances must be justified prospectively, not tuned to the current failures.
Future HJB convergence, KFE nonnegativity/mass, GE/annual coverage and Results remain separate dependent claims. Propose the smallest next execution budget but do not consume it.

## Budget, tests and repairs
New HJB/policy/evaluator calls=0; new direct/root/optimization/condition-estimator solves=0; MATLAB scientific or static-check process launches=0; trajectories/KFE/GE/annual/dynamics/IRF/Results=0. No residual-refinement, inverse, eigen/SVD or high-precision solution. No new calibration, initialization, grid or parameter experiments.
Allowed: exact existing-file reads/hashes, sparse matvecs/reductions, local legacy-expression reconstruction, written symbolic derivations, and synthetic arithmetic/IO/coordinate tests with mocked solver boundaries. A full replacement policy map or a real-state candidate optimizer is out of scope even if described as postprocessing. No model import with evaluation side effects.
Whole task <=2 hours. Routine parsing, path, serialization, witness/schema, local test and report problems may be repaired within the allowed paths. Preserve failures; repair postprocessing from saved inputs rather than rerun science. No scientific retry budget exists.
Run only focused tests of new diagnostic behavior, retain the actual log and parse counts. Handle raw-byte versus Git-normalized text explicitly when relevant. Required failed shell commands must stop dependent publication steps: in PowerShell check native exit codes or run dependent phases separately. Do not create an extra governance task for this repair.

## Deliverables and publication
Allowed repository paths only:
- validators/multi_province/call725_boundary_generator_repair_spec/
- tests/test_call725_boundary_generator_repair_spec.py
- docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_REPORT.md
- reports/call725_boundary_generator_repair_spec_20260907/ (small text/JSON/log evidence only).
No production, helper, historical report, CURRENT or task edits by Builder. No private MAT/NPZ/secrets in Git.
Deliver the source/drift/row witnesses, face/corner feasibility table, authority/decision matrix, explicit recommended repair contract and future API/test/run plan, actual zero-science ledger, focused test log, finite manifest and compact digest/readback receipt. Reuse unchanged accepted evidence rather than republish all prior arrays. Exclude manifest itself and terminal receipts from its entries.
Completion when these substantive deliverables are present: BOUNDARY_GENERATOR_REPAIR_SPEC_COMPLETE__SCIENTIFIC_DECISIONS_EXPLICIT__NO_MODEL_RUN. Unresolved scientific adoption choices are an expected output, not fabricated acceptance. Use EVIDENCE_INCOMPLETE for material missing evidence and state the exact gap.
Stage explicit allowed paths, non-force publish the dedicated branch, verify remote SHA once, return outcome/decision recommendation/evidence/commit. Do not merge main or implement/start the proposed successor. Reviewer will review the specification and resolve or escalate the real scientific choices before any changed-law execution.
