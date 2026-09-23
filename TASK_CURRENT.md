# Current Builder Task

Task ID: `CH5_FULL_OUTER_STATE_MAP_ZERO_SCIENCE_DESIGN_20260923`

Status: `ACTIVE__ZERO_SCIENCE_DESIGN_ONLY`

## Authority and objective

The Owner selected the **complete outer state** route and authorized a reviewable, zero-science design. This selection does not adopt a convergence law, numerical tolerance, fixed-point claim, or scientific execution budget. Trace the active bounded K1B turn map from current source and sealed evidence, then propose a complete state/checkpoint and diagnostic contract for Owner decision. "Complete" means complete for the currently executed bounded K1B route; it does not mean full GE.

## Startup and identity

- Work only in `D:\ProjectTemp\c5k1bturn56`. Read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, this task, `REVIEW_GATE.md`, the accepted design dossier and its independent review, then directly relevant active source/evidence. Never access `deep-learning-hank`.
- Before any write, record local HEAD, clean/dirty status, and `HEAD:src`. The dispatch commit must have parent `724b53c0507de34ebd9a2c3eabc8d5f6a8885aad`; if identity or worktree differs, stop and report the first mismatch. GitHub state is not a gate.
- Preserve sealed turn3–turn6 evidence and the turn7 prepared bundle. Turn7 household has not run. Results eligibility stays `FALSE`.

## Exact allowed writes

1. `docs/CH5_FULL_OUTER_STATE_MAP_ZERO_SCIENCE_DESIGN_20260923.md`
2. `EVIDENCE/ch5_full_outer_state_map_design_20260923/design_receipt.json`

Do not modify any other path. Explicitly stage only those two outputs and make one local candidate commit if the checks below pass. Do not push or create a PR. A document-only local commit is candidate delivery, not scientific adoption.

## Required design

1. Trace actual turn entry, 31-province household/aggregation, labor, capital and C1, firm/monetary/fiscal, raw-return, next-share/payoff, and next-bundle sequence. For every input consumed in the next complete turn, give its exact field/key, dimensions, order, known units, source, checkpoint, writer, and consumers. Classify each as cross-turn dynamic state, frozen exogenous input, reconstructible derived/accounting quantity, household terminal output, numerical initialization/carryover, or diagnostic-only quantity. Resolve case-sensitive keys exactly; do not collapse `It`/`it` or `PIt`/`pit`. Mark unsupported identities or units `UNRESOLVED`.
2. Propose one same-stage checkpoint `C_n` after a legally completed turn and define candidate `x_(n+1)=F(x_n; theta_frozen)` for the active route. Show that listed state plus frozen inputs determines the next turn, or list each closure defect/hidden file or cache dependence. Account for old `Yt/Lt`, lagged firm inputs such as `Kt_prev/Lt_prev/Zt_1/pit_1` and prior returns, the prepared portfolio matrix, and all other actual consumers. Do not assume that the ten-field trajectory panel or six direct household inputs is a complete state.
3. Preserve adopted timing: completed `raw ra0_n` creates entering `S_(n+1)` and `rah_(n+1)`; `S[destination,origin]` and 31-province order are fixed. Distinguish completed-turn values from prepared-next-turn values and explain which same-stage consecutive checkpoints can be compared.
4. Propose componentwise diagnostics for every required dynamic component, including norm and scale/zero handling, plus an all-required-components rule. Explain the distinction between iteration-step change and mapping residual, and when they coincide for this exact unaccelerated map. Classify value, policy, and KFE distribution as state, deterministic inner outputs, or additional checks with a reason; absence of historical adjacent norms is `UNAVAILABLE`, not evidence of stability.
5. Give a short Owner decision table: recommended object, norms/scales, candidate tolerances only where units and precision support them, checkpoint timing, stopping rule, maximum-turn/call-budget scheme, and first-failure behavior. All proposed choices and numbers must be marked `PROPOSED_NOT_ADOPTED`; missing units, scales, or precision support stay `UNRESOLVED`. Do not derive thresholds from turn3–turn6 shrinkage or reuse inner HJB tolerances. Separate legality failure, valid but threshold-not-met, budget exhaustion, and criterion-met. A proposed two-turn batch or no-retry rule grants no calls.
6. State exactly what a future diagnostic could establish. Frozen wages or other frozen quantities must be identified as such. Do not equate this bounded-route fixed point with full GE equilibrium, mathematical contraction, steady state, or Results eligibility.

## Evidence and checks

- The JSON receipt must record task ID, start/precommit HEAD and `src` tree, input file paths and SHA-256, the design document's path and SHA-256, both output paths, explicit changed-path inventory, unresolved items, first failure if any, and a literal call ledger with zero for household/HJB/KFE, integration, firm, K1B network evaluation, GE, turn7, and all other model/scientific calls. Report the candidate commit and receipt SHA-256 after committing; the receipt must not attempt to hash itself.
- Static source reading, text search, and parsing sealed JSON are allowed. Do not import or execute model modules, scientific validators, or scientific tests. `git diff --check` and output readback are allowed.
- Stop on the first accepted-law/source contradiction, evidence identity mismatch, need for scientific execution, or need to alter an adopted mathematical rule. Preserve the first failure in the two allowed outputs if feasible. Ordinary missing provenance remains `UNRESOLVED`; finish independent parts.
- Before delivery verify only the two allowed outputs changed, `src` tree is unchanged, all call ledger entries are zero, and the worktree is clean after the explicit-path candidate commit.

## Terminal and next gate

Successful Builder terminal: `DESIGN_CANDIDATE_READY__ZERO_SCIENTIFIC_CALLS__OWNER_ADOPTION_PENDING`.

Return candidate commit, output hashes, exact checks, unresolved decisions, and first failure if present to GPT Work for independent ACCEPT/REJECT. Work acceptance of design quality is not Owner adoption of a convergence law. Do not run turn7, create a scientific successor, or change Results eligibility.
