# Chapter 5 MP4C GovInv controller redesign forensic/spec — Reviewer acceptance

Date: 2026-09-11

Reviewer verdict:

`GOVINV_CONTROLLER_REDESIGN_SPEC_ACCEPTED__C0_FAILURE_MECHANISM_QUANTIFIED__OWNER_IDENTIFIES_GOVINV_AS_GOVERNMENT_ASSET_RESIDUAL__C1_LEVEL_REPLACEMENT_IMPLEMENTATION_AUTHORIZED`

Accepted candidate: `ac71e396cd64ecd1e7d6b6497981042800d8411e`.

## Acceptance basis

The candidate is accepted as a zero-science forensic/specification package. The historical C0 controller was exactly replayed on the accepted G1 ledger with zero mismatches. Of 775 province-turn actions, 258 (`33.290323%`) are statically adverse to the contemporaneous K-level gap, all of the form `total K > Ktarget` while the clipped-return controller still applies `GovInv *= 1.1`. The forensic correctly distinguishes this static directional inconsistency from a dynamic causal decomposition.

The package also correctly establishes that C0 is a return-bound controller rather than a capital-target controller: its trigger uses clipped `ra` and contains no `Ktarget`, private-K residual, or total-K residual. C1 is dimensionally coherent with the already accepted G1 initialization; C2 and C3 require additional unidentified targets/gains/state-machine choices.

## Owner scientific clarification incorporated

The Owner now clarifies the economic meaning of `GovInv`: it represents government/public productive assets introduced because empirically estimated total productive capital `Kt` is materially larger than household/private illiquid assets `At`, while province-level government asset stocks are not directly observed with sufficient reliability. In the historical MATLAB implementation, `GovInv` was therefore made endogenous and adjusted numerically through the return-bound feedback rule.

This clarification resolves an important identification question. `GovInv` is not to be interpreted as an arbitrary numerical balancing stock. It is a government/public productive asset residual used to reconcile observed total productive capital with model-implied private productive capital when the government component is unobserved.

Accordingly, the lowest-risk next controller design is not an estimated-gain C1 rule but a separately named **level-replacement residual definition**:

`GovInv_next = max(Ktarget - Kprivate_current, 0)`.

This is algebraically the `lambda_K=1` case of the generic C1 expression, but in the next implementation task it is not treated as a tuned gain. It is treated as the direct residual accounting definition implied by the Owner's economic interpretation. Dynamic stability is still unproven and requires a later bounded trajectory gate.

## Boundaries

This acceptance does not authorize production replacement, steady-state acceptance, normalized-labor activation, controller damping/hysteresis, return-target control, or Results. HJB/KFE blockers and `beta_a=1` diagnostic-only status remain unchanged.

Results eligibility remains `FALSE`.
