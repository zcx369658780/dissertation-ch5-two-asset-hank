# CH5 MP4C K1 — k-unit normalization and asset-domain recalibration design audit acceptance

Date: 2026-09-14.

Reviewer verdict:

`K_UNIT_NORMALIZATION_AND_ASSET_DOMAIN_DESIGN_ACCEPTED__MACRO_REBASE_COHERENT__HOUSEHOLD_MONETARY_BRIDGE_UNPROVEN__BMAX_OWNER_SELECTION_REQUIRED`

Accepted candidate: `6b89d8e47f075906d463f58f3e984bf8665710f6`.

## Acceptance basis

The candidate is accepted as a zero-science-runtime design audit. Independent review verified it is exactly one commit ahead of baseline `d7d6d4718d27abe33a8915fd2b07ac042a125783`, with changes confined to the task-owned report, CURRENT closeout docs, sealed evidence, focused tests and task-owned audit builder. No scientific model source, parameter, grid, guard or Results path was modified.

Accepted terminal classification:

`MACRO_K_UNIT_REBASE_COHERENT__HOUSEHOLD_MONETARY_BRIDGE_UNPROVEN__BMAX_OWNER_SELECTION_REQUIRED`

Results eligibility=`FALSE`.

## Accepted normalization findings

The original MATLAB chain does not support a global “divide everything by 1000” rule. The accepted active configuration is `GDP_multiplier=1000` and `POP_multiplier=100`; GDP/capital use the GDP route and population uses the population route, while household `C/Tt/a/b/At/Bt/w` do not have a proven corresponding multiplier in the designated source chain.

For the proven macro chain, a coherent k-unit re-expression exists: aggregate monetary quantities currently in the internal `MU=100k` representation scale numerically by `100`, person quantities currently in `NU=100 persons` also scale numerically by `100`, so `Y/N`, `K/N`, Cobb-Douglas productivity, raw firm wage and dimensionless return/rate expressions remain invariant. This is accepted only as a unit re-expression of the proven macro chain, not as household recalibration authority.

The household monetary bridge remains unproven. The audit correctly distinguishes the source-defined `wjt -> composite w` aggregation from a real-currency/period mapping. Therefore no factor may be introduced merely to align `wjt`, composite wage, household assets and macro per-capita GDP.

## Accepted household scaling logic

Conditional on a household monetary rescale `x' = h x`, the audit’s equation-level transformation is accepted as design authority: `alphac' = h^(gamma-1) alphac`, `a_bar' = h a_bar`, derivative floor scales by `1/h`, drift tolerance by `h`, while `ra/rb/borrowing gap/rho/delta/tax rates` and the pure monetary-rescale values of `chi0/chi1` remain unchanged. These transforms are not authorized for implementation until the household monetary bridge is frozen.

## Accepted asset-domain findings

`amax=100` is accepted as a scientifically plausible first illiquid-asset upper-domain candidate only conditional on the household k/person bridge. It denotes an individual household state-grid upper bound, not an aggregate `At=100` target.

The current `bmax=5` is accepted as diagnostically inadequate: prior real-wage evidence has the liquid-asset marginal mode at `bmax` in all nine points with material upper-bound mass. The audit proposes the bounded set `{20,50}` but does not select one. That restraint is accepted.

With `I=J=20`, domain expansion makes the grids materially coarser. Keeping 20×20 is accepted only for a first bounded domain diagnostic; a separate precision-sensitivity gate is mandatory before any production use.

## Reviewer recommendation on BMAX Owner selection

For the first bounded diagnostic, the Reviewer recommends `bmax=20`, not `50`, subject to Owner approval. The reason is methodological rather than outcome-fitting: `bmax=20` already expands the upper liquid-asset domain from `5` by a factor of four and exceeds the accepted maximum `Bt` by more than four times, while preserving materially finer spacing (`db≈1.158`) than `bmax=50` (`db≈2.737`) at fixed `I=20`. If the resulting distribution still binds at `bmax=20`, that is informative evidence for a later bounded expansion; starting at `50` would confound domain adequacy with an unnecessarily severe precision loss.

This recommendation does not itself authorize implementation.

## Scientific boundary

The following remain unresolved and must not be silently assumed:

- household k/person monetary bridge and model-period mapping;
- aggregate/per-capita basis closure of mixed government-account objects;
- production adequacy of `amax=100`;
- final `bmax` selection until Owner freezes it;
- grid precision after domain expansion;
- corrected-2018 multi-province finite-box upper-`b` leakage and MATLAB-style pinning.

No HJB, KFE, MATLAB, firm, global outer, K1B/K2, GE, downstream, shock, IRF or Results runtime occurred in this design audit.

## Exactly one next Owner gate

`OWNER_REVIEW_HOUSEHOLD_K_UNIT_BRIDGE_AND_BMAX_SELECTION`

Owner should decide whether to adopt the conditional household identity “current household monetary quantities are already expressed in k per person (and per model period for flows)” for the next bounded diagnostic, and select one `bmax` candidate. Reviewer recommendation: choose `bmax=20` for the first diagnostic, with `amax=100`, `amin=0`, `bmin=-2`, `I=J=20`, followed by a dedicated precision-sensitivity gate if the domain diagnostic succeeds.

No successor runtime task is authorized by this acceptance alone.
