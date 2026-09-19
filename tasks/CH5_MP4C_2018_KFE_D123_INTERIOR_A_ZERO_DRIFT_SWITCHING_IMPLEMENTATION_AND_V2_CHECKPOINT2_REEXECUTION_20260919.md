# Task — adopted interior-a zero-drift switching implementation and V2 checkpoint-2 bounded reexecution

Date: 2026-09-19

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:
`CH5_MP4C_2018_KFE_D123_INTERIOR_A_ZERO_DRIFT_SWITCHING_IMPLEMENTATION_AND_V2_CHECKPOINT2_REEXECUTION_20260919`

## Governance

Owner has explicitly adopted:

`docs/CH5_MP4C_2018_KFE_D123_INTERIOR_A_ZERO_DRIFT_SWITCHING_OWNER_ADOPTION_20260919.md`.

Owner is final scientific authority. ChatGPT is L3 Reviewer/scientific-route authority. Codex is bounded Builder.

Never enter, read, search, use or modify:
`zcx369658780/deep-learning-hank`.

Fresh-fetch live `origin/main`. Read in order:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. Owner adoption above
6. the zero-science adjudication report and Reviewer acceptance
7. repaired-selector checkpoint-2 report and acceptance
8. accepted liquid-`Z`, lower-`a` zero-kink, D1/D2/D3 and nonlinear-convergence authorities
9. exact accepted V2 artifacts/receipts and current corrected selector source.

## Objective

Implement only the Owner-adopted **interior-`a` zero-drift switching law** in the corrected-diagnostic route, verify it with focused engineering tests including the exact cell100 regression, then perform one bounded checkpoint-2 reexecution from the accepted V2 field.

The task must determine whether the adopted switching closure is sufficient to produce the first complete scientifically valid V2 policy map and checkpoint-2 object.

## Frozen identities

Accepted V2 field SHA-256:

`A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.

Pre-adoption repaired selector SHA-256:

`DBEB8EDCDA18B14579F36C2B68A50A47C9E717F49E84BC31A2E4E17180E9C327`.

Accepted cell100 switching proof:

- state `(b,a,z)=(-2.0,2.6315789473684212,0.8)`;
- `p_b=0.012333311206716577`;
- `p_a^F=0.008957007194295222`;
- `p_a^B=0.00903315440190679`;
- `d_Z=-0.23684196191023801`;
- D3 ratio `q_a/q_b=0.72000010894821909`;
- legal switching interval
  `q_b in [0.012440285887428097,0.012546045881996438]`;
- frozen liquid equality changes sign from
  `-0.0039748658728543454` to `+0.048890867998731984`;
- the equality is strictly increasing, so one unique compatible crossing exists.

Do not hard-code the cell100 root value or a cell identifier into scientific logic.

## Allowed implementation

Modify only:

- corrected-diagnostic selector code directly required for the adopted branch;
- a narrowly scoped helper if needed for deterministic interval/root/receipt construction;
- focused tests/fixtures;
- the checkpoint-2-only execution helper only if required to expose the adopted receipt fields or ledger, without changing scientific equations or budgets.

Do not modify:

- source-faithful/production selector or model paths;
- MATLAB;
- D1/D2/D3 equations;
- the liquid-`Z` law;
- lower-`a` zero-kink law;
- root tolerance or solver family;
- grid, calibration, payoff equations;
- HJB update equation;
- `Delta=1000`;
- convergence thresholds/cycle law;
- terminal KFE law.

## Required implementation semantics

Implement the Owner adoption literally:

1. At interior `a`, evaluate existing one-sided candidates first.
2. Trigger only on a strict arithmetic-bound-separated crossing for the same existing liquid branch/active set and transfer regime:
   backward candidate `g_a>0`, forward candidate `g_a<0`, neither direction-consistent.
3. Set `d_Z=-r_a a`; infer transfer regime from its sign.
4. Obtain `q_a` from unchanged D3 KKT/subgradient.
5. Require `q_a` inside the closed sorted interval between `p_a^F` and `p_a^B`.
6. Preserve the existing liquid-axis law.
7. For an active liquid face, intersect the derivative-implied `q_b` interval with the exact face multiplier domain and use the existing scalar root routine/tolerance only on that interval.
8. Require one unique legal root; otherwise fail closed.
9. Do not create simultaneous new `a`-switching plus liquid-`Z` switching. Such a case must fail closed for separate adjudication.
10. Reconstruct controls/KKT/Hamiltonian from the switching shadows; no endpoint interpolation.
11. Canonical zero drifts require the existing arithmetic-residual rule.
12. Include a legal switching candidate in the unchanged deduplication/Hamiltonian comparison.
13. Persist the Owner-adopted audit receipt fields.
14. D2 itself remains unchanged and consumes the resulting canonical drifts if reached.

If `d_Z=0`, use only already-adopted D3 zero-kink/subgradient semantics. If the combined selection is not uniquely specified by existing authority, fail closed rather than inventing a rule.

## Focused engineering gate

Before any scientific run, run a focused test set that covers at minimum:

- exact cell100 fixture creates the adopted interior-`a` switching candidate;
- cell100 candidate uses `d_Z=-r_a a`, D3 KKT, the legal derivative interval and lower-b domain;
- the compatible liquid root lies strictly inside the accepted cell100 interval;
- raw/canonical `g_a` and active-face `g_b` satisfy existing residual rules;
- cell100 no longer fails solely because the two one-sided `a` branches point toward one another;
- the candidate is admissible under D1/D2/D3 and enters the unchanged Hamiltonian comparison;
- no trigger when either one-sided `a` branch is already direction-consistent;
- no trigger at lower/upper `a` boundaries;
- upper-b active-domain handling remains correct;
- lower-b repaired eight-case coverage remains intact;
- positive active no-root behavior remains fail closed;
- liquid-`Z` behavior is unchanged;
- lower-`a` zero-kink behavior is unchanged;
- no simultaneous newly-created two-axis switching;
- D2 zero-drift consumption behavior remains unchanged;
- all previously affected selector/KKT/D1/D3 tests continue to pass.

No tolerance weakening, assertion deletion or fixture retuning to the expected result is allowed.

Engineering tests may call the selector on deterministic fixtures. Record these as engineering calls separately; they do not consume the one authorized scientific V2 map.

## Scientific execution budget

Only after the engineering gate and all artifact/hash bindings pass:

- fresh accepted-V2 policy-map attempts: exactly 1 maximum;
- selector evaluations: at most 800, stopping at first fail-closed cell;
- ordinary scalar roots: only those naturally required by the one map;
- adopted interior-`a` switching roots: only those naturally required by the one map, at most one per qualifying active-liquid switching candidate;
- interior-liquid `Z` roots: only existing-law calls naturally required by the one map;
- Q2/D2 assemblies: at most 1, only after all 800 cells select admissible policies;
- checkpoint-2 Bellman/value/policy/operator/cycle diagnostic evaluation: at most 1, only if Q2 exists;
- direct HJB solves: 0;
- `V2->V3` HJB updates: 0;
- graph/SCC/topology/KFE/SVD/eigen/nullspace/`Q.T@p`: 0;
- MATLAB/source-faithful/production/outer/firm/wage-return/GE/annual/shock/IRF/Results: 0;
- scientific retries: 0;
- solver substitutions/damping/relaxation/adaptive Delta/continuation/clipping/artificial diffusion: 0.

A launcher/path/import failure before scientific entry may be corrected within scope and must be preserved in a zero-science blocked receipt. Once the scientific map begins, no retry is authorized.

## Required scientific behavior

### If the V2 map fails

Stop at the first failure. Persist the exact cell receipt, the adopted switching evidence if relevant, and the complete ledger.

Do not repair a second scientific issue inside this task.

### If the V2 map completes

Persist complete P2/u2 identity, assemble exactly one Q2 under unchanged D2, and evaluate checkpoint 2:

- `B2` Bellman residual;
- `D2=||V2-V1||_inf`;
- policy/active-set/control/drift changes versus checkpoint 1;
- count/location of adopted interior-`a` switching selections and rejected switching candidates;
- Q2 identity and `Q2-Q1` norm summary;
- exact/approximate cycle diagnostics under the frozen order.

Evaluate the frozen primary convergence law.

Do **not** perform terminal topology/KFE and do **not** execute `V2->V3`, even if checkpoint 2 is nonconverged.

If checkpoint 2 passes the primary Bellman/value law, classify only as an HJB convergence candidate pending separate terminal gates.

## Evidence

Use fresh no-overwrite evidence roots.

Persist:

- pre/post scientific-code hashes;
- accepted V1/V2/Q1 binding;
- Owner-adoption document identity;
- focused test receipt;
- exact scientific call ledger;
- all V2 cell receipts until failure or completion;
- adopted switching receipts;
- P2/u2/Q2 and checkpoint-2 metrics if reached;
- finite manifest/readback evidence;
- changed-file list;
- final Git status.

## Deliverable

Write:

`docs/CH5_MP4C_2018_KFE_D123_INTERIOR_A_ZERO_DRIFT_SWITCHING_IMPLEMENTATION_AND_V2_CHECKPOINT2_REEXECUTION_REPORT.md`

Commit and ordinary non-force push one task branch.

Do not merge main.
Do not publish a successor task.
Do not update CURRENT files.

## Terminal classifications

Use the narrowest supported marker, distinguishing at least:

- `BLOCKED__INTERIOR_A_SWITCHING_IMPLEMENTATION_OR_PREFLIGHT_FAILURE_BEFORE_SCIENCE`
- `FAIL__ADOPTED_INTERIOR_A_SWITCHING_V2_MAP_FIRST_FAILURE`
- `PASS__ADOPTED_INTERIOR_A_SWITCHING_V2_MAP_COMPLETE__CHECKPOINT2_NONCONVERGED__NO_V3_UPDATE`
- `PASS__ADOPTED_INTERIOR_A_SWITCHING_V2_MAP_COMPLETE__CHECKPOINT2_HJB_CONVERGENCE_CANDIDATE__TERMINAL_GATES_NOT_RUN`

Results eligibility remains `FALSE`.
