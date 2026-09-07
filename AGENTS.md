# Chapter 5 Two-Asset HANK — Working Agreement

Updated: 2026-09-07. Owner-approved workflow revision: `CH5_ASTRA_WORKFLOW_2026_09_07`.

## Identity and authority
- Active repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- This is the sole active Chapter 5 model codebase. The one-asset R5 repository is historical evidence; `deep-learning-hank` is a separate project.
- Live GitHub main is repository-state authority. Scientific execution requires an active task published there.
- Read `project_rules/PROJECT_RULE_INDEX_CURRENT.md`, the exact task, and its relevant current sources. Do not restart historical gates from old handoffs.
- Owner decides genuine economic/scientific choices and retains final scientific authority. Reviewer defines tasks and accepts evidence; Builder completes authorized work.

## Execution style
The Astra migration describes a working style, not a claim about the executor's installed model. Do not change model/provider settings.
- Complete one logical work unit per task. Planning, bounded implementation, relevant checks, authorized execution, evidence closure and reporting can be phases of the same task.
- Continue through routine issues anticipated by the task: imports, paths, serialization, diagnostic shapes, manifests and report omissions. Repair them within allowed paths and budget.
- Ask only for a missing decision that materially changes economic meaning, authority, external effects or experiment scope. Naming and representation choices that preserve the scientific object belong to the reviewer/Builder.
- Reuse accepted unchanged evidence. Test changed behavior and affected scientific invariants; stop optional testing when the remaining risk is resolved.
- A failed ordinary check is not automatically a new gate. Preserve the failure, diagnose, repair within scope, and perform the relevant check again.
- Stop before changing equations, KKT/boundary laws, calibration, solver semantics, tolerances or experiment scope unless the current task explicitly authorizes that change. Never tune these merely to obtain PASS.
- Model invocations, including failed invocations, count in the task ledger. A new conversation does not reset budgets. Never claim zero model calls just because no output was returned.
- Protect original MATLAB and accepted evidence. Development scripts and draft reports may be revised within the task workspace.

## Git and local work
- Fetch before starting; record the actual baseline. Verify the task remains active and its input/source identities remain valid.
- Unrelated main changes are not an automatic blocker; assess the relevant diff. Material authority/input changes require reassessment.
- Preserve unrelated dirty files. Use an isolated worktree when possible; no reset, clean, stash, force-push or overwrite of user work for convenience.
- Stage explicit allowed paths. Verify the final changed-file list and one publication readback. Do not create a gate for each Git plumbing operation.
- Local documentation sync was accepted at branch commit `d2f3e6e7cc21fffe8807f577ec2262bb77afdc07`; do not repeat it. Read the current active task in the rule index.
- Owner standing authorization (2026-09-07): after evidence-based acceptance, Reviewer may publish the next bounded task without routine reconfirmation when no substantive scientific decision remains. Use proportionate checks and task-budgeted retries. This agreement itself does not authorize model calls.

## Reporting
Report outcome first: completed scope, evidence, changed paths, commit/publication status, real limitations, and next useful action. Use plain language; avoid repeating forbidden-operation lists and long terminal strings when a short status plus evidence is sufficient.
Scientific pass, implementation fidelity, numerical validity, and paper Results eligibility are distinct claims.
