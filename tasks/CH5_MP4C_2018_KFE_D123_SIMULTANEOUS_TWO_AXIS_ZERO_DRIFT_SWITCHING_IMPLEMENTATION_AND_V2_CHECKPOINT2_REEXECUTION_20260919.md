# Task — adopted simultaneous two-axis zero-drift switching implementation and V2 checkpoint-2 bounded reexecution

Date: 2026-09-19

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:
`CH5_MP4C_2018_KFE_D123_SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_IMPLEMENTATION_AND_V2_CHECKPOINT2_REEXECUTION_20260919`

## Governance

Owner has explicitly adopted:

`docs/CH5_MP4C_2018_KFE_D123_SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_OWNER_ADOPTION_20260919.md`.

Owner is final scientific authority. ChatGPT is L3 Reviewer/scientific-route authority. Codex is bounded Builder.

Never enter, read, search, use or modify:
`zcx369658780/deep-learning-hank`.

Fresh-fetch live `origin/main`. Read in order:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. Owner adoption above
6. cell185 zero-science adjudication report and Reviewer acceptance
7. interior-`a` implementation/reexecution report and acceptance
8. interior-`a` Owner adoption
9. liquid-`Z` Owner adoption
10. accepted D1/D2/D3, lower-`a` zero-kink and nonlinear-convergence authorities
11. exact accepted V2 artifacts/receipts and current corrected selector source.

## Objective

Implement only the Owner-adopted **simultaneous two-axis zero-drift switching law** in the corrected-diagnostic route, verify it with focused tests including exact cell185 regression and one-axis non-regression, then perform one bounded checkpoint-2 reexecution from the exact accepted V2 field.

The task asks whether the adopted coupled closure is sufficient to produce the first complete scientifically valid V2 policy map and checkpoint-2 object.

## Frozen identities

Accepted V2 SHA-256:

`A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.

Current accepted selector scientific baseline is the implementation accepted in:

`docs/CH5_MP4C_2018_KFE_D123_INTERIOR_A_ZERO_DRIFT_SWITCHING_IMPLEMENTATION_AND_V2_CHECKPOINT2_REEXECUTION_ACCEPTANCE_20260919.md`.

Accepted cell185 joint proof:

- state `(b,a,z)=(-0.1578947368421053,4.7368421052631575,0.8)`;
- liquid interval
  `[0.009574726769001294,0.013362109688537174]`;
- illiquid interval
  `[0.008489317330830281,0.00857557540065246]`;
- `d_ZZ=-0.42626460578345887`;
- D3 ratio `q_a/q_b=0.7200216108914285`;
- exact joint `q_b` interval
  `[0.011790364625750628,0.011910163904713082]`;
- fixed-transfer liquid equality endpoints
  `-0.023007467717380714` and `+0.041147374843733764`;
- strict monotonicity implies exactly one compatible joint root.

Do not hard-code cell185, the root value, or expected selected-policy identity into scientific logic.

## Allowed implementation scope

Modify only:

- corrected-diagnostic selector code directly required by the adopted joint law;
- a narrow helper if needed for interval/root/receipt construction;
- focused tests/fixtures;
- checkpoint-2-only runner/ledger hooks only as needed to expose joint-root counts and receipts without changing equations/budgets.

Do not modify:

- source-faithful/production paths;
- MATLAB;
- D1/D2/D3 equations;
- ordinary one-sided laws;
- one-axis liquid-`Z`;
- one-axis interior-`a`;
- lower-`a` zero-kink;
- root solver family/tolerance;
- grid/calibration/payoff equations;
- HJB update law;
- `Delta=1000`;
- convergence thresholds/cycle law;
- terminal KFE law.

## Required implementation semantics

Implement the Owner adoption literally:

1. joint law only at interior-interior asset nodes with no asset-face active set;
2. evaluate ordinary and one-axis candidates first;
3. require the accepted coupled strict-crossing evidence under one common transfer regime;
4. impose `d_ZZ=-r_a a` and infer its transfer regime;
5. use unchanged D3 to map the illiquid derivative interval into `q_b`;
6. intersect that interval exactly with the liquid derivative interval and require a finite positive nondegenerate intersection;
7. use only the existing scalar root routine/tolerance on the exact intersection to solve fixed-`d_ZZ` `g_b=0`;
8. require exactly one legal root; fail closed otherwise;
9. set `q_a` from unchanged D3;
10. reconstruct all controls/KKT/Hamiltonian from the joint shadows;
11. canonicalize zero drifts only within existing arithmetic bounds;
12. create exactly one joint candidate per node/regime and prevent sequential-order duplicates;
13. include a legal joint candidate in unchanged deduplication/Hamiltonian comparison;
14. persist the full Owner-adopted joint receipt;
15. leave D2 unchanged.

If `d_ZZ=0` and existing authority does not uniquely specify the required joint kink selection, fail closed rather than inventing a rule.

## Focused engineering gate

Before scientific execution, cover at minimum:

- exact cell185 fixture triggers one and only one joint candidate;
- `d_ZZ`, D3 ratio and both derivative intervals are correct;
- the exact interval intersection matches the accepted static proof;
- joint root lies strictly inside the accepted cell185 interval;
- `q_a` lies strictly inside the accepted illiquid interval;
- raw/canonical `g_b,g_a` obey existing residual rules;
- D3 KKT residual passes;
- candidate is D2 admissible and enters unchanged Hamiltonian comparison;
- no joint trigger if a one-axis candidate is already admissible/direction-consistent;
- no joint trigger at any asset boundary;
- no joint trigger across different transfer regimes;
- no duplicate joint candidates from sequential axis order;
- existing cell100 one-axis interior-`a` selection is unchanged;
- existing liquid-`Z` fixtures are unchanged;
- lower-`a` zero-kink is unchanged;
- upper/lower liquid-boundary behavior is unchanged;
- D2 zero-drift consumption is unchanged;
- all previously affected D1/D3/KKT/selector/nonlinear-contract tests pass.

No tolerance weakening, assertion deletion, or fixture retuning to force the expected scientific result is allowed.

Engineering fixture calls must be recorded separately from the scientific budget.

## Scientific execution budget

Only after focused tests, compile/static checks, authority hash binding, and accepted V1/V2/Q1 binding pass:

- fresh accepted-V2 policy-map attempts: at most 1;
- scientific selector evaluations: at most 800, stop at first fail-closed cell;
- total scalar roots: only those naturally required by that one map;
- existing liquid-`Z` roots: only natural calls;
- adopted one-axis interior-`a` roots: only natural calls;
- adopted joint-switch roots: only natural calls, at most one per qualifying joint candidate;
- Q2/D2 assemblies: at most 1 and only after all 800 cells succeed;
- checkpoint-2 Bellman/value/policy/operator/cycle evaluation: at most 1 and only if Q2 exists;
- direct HJB solves: 0;
- V2->V3 updates: 0;
- graph/SCC/topology/KFE/SVD/eigen/nullspace/`Q.T@p`: 0;
- MATLAB/source-faithful/production/outer/firm/wage-return/GE/annual/shock/IRF/Results: 0;
- scientific retries: 0;
- solver substitution/damping/relaxation/adaptive Delta/continuation/clipping/artificial diffusion: 0.

A launcher/path/import failure before scientific entry may be corrected within scope and preserved as a zero-science blocked receipt. Once the scientific map starts, no retry is authorized.

## Scientific behavior

### If the V2 map fails

Stop at the first failure.

Persist the exact receipt, joint/one-axis evidence as applicable, and the complete ledger.

Do not repair another scientific issue in the same task.

### If the V2 map completes

Persist complete P2/u2, assemble exactly one Q2 under unchanged D2, and compute checkpoint 2:

- `B2`;
- `D2=||V2-V1||_inf`;
- policy/active-set/control/drift changes versus checkpoint 1;
- selected/rejected counts and locations for one-axis liquid-`Z`, one-axis interior-`a`, and joint switching;
- Q2 identity and `Q2-Q1` norm summary;
- exact/approximate cycle diagnostics under the frozen order.

Evaluate the frozen primary convergence law.

Do not perform terminal topology/KFE and do not execute V2->V3.

If primary Bellman/value convergence passes, report only an HJB convergence candidate pending separate terminal gates.

## Evidence and deliverable

Use fresh no-overwrite evidence roots.

Persist:

- pre/post scientific-code hashes;
- accepted V1/V2/Q1 binding;
- Owner-adoption identity;
- focused test receipts;
- exact scientific-call ledger with joint-root count;
- all cell receipts until failure/completion;
- joint-switch receipts;
- P2/u2/Q2/checkpoint metrics if reached;
- sealed manifest/readback;
- changed-file list and final Git status.

Write:

`docs/CH5_MP4C_2018_KFE_D123_SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_IMPLEMENTATION_AND_V2_CHECKPOINT2_REEXECUTION_REPORT.md`

Commit and ordinary non-force push one task branch.

Do not merge main.
Do not publish a successor task.
Do not modify CURRENT files.

## Terminal classifications

Use the narrowest supported marker, distinguishing at least:

- `BLOCKED__JOINT_SWITCHING_IMPLEMENTATION_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE`
- `FAIL__ADOPTED_JOINT_SWITCHING_V2_MAP_FIRST_FAILURE`
- `PASS__ADOPTED_JOINT_SWITCHING_V2_MAP_COMPLETE__CHECKPOINT2_NONCONVERGED__NO_V3_UPDATE`
- `PASS__ADOPTED_JOINT_SWITCHING_V2_MAP_COMPLETE__CHECKPOINT2_HJB_CONVERGENCE_CANDIDATE__TERMINAL_GATES_NOT_RUN`

Results eligibility remains `FALSE`.
