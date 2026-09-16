# CH5 MP4C 2018 KFE D1-D3 Cell 5 liquid-direction switch — Reviewer acceptance

Date: 2026-09-16
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

## Verdict

`PASS__CELL5_SWITCH_ATTRIBUTION_ACCEPTED__MATHEMATICALLY_LEGAL_Z_BRANCH_AND_REPOSITORY_PRECEDENT_CONFIRMED__OWNER_DECISION_REQUIRED_FOR_CORRECTED_TARGET_INHERITANCE`

Accepted Builder candidate: `fdfabfb8ba12fa52add525b68050de67c2d6369d`.

The candidate is one commit ahead of baseline `8473a204acdc8e2be2e2d6a405370651400110d0`, changes only `docs/CH5_MP4C_2018_KFE_D123_CELL5_LIQUID_DIRECTION_SWITCH_ALGEBRAIC_ATTRIBUTION_REPORT.md`, and has an all-zero scientific/model call ledger.

## Accepted findings

1. Cell 5 has a unique finite positive liquid shadow `q_b*=0.01250021388291760706054915182349077777...` such that the consumed liquid drift is exactly zero under the frozen Cell-5 non-liquid objects.
2. The root lies strictly between the raw one-sided liquid derivatives: `p_b^F=0.012481806039037598 < q_b* < p_b^B=0.02256028269097067`.
3. The backward candidate has positive liquid drift and the forward candidate has negative liquid drift, so the current two-branch corrected selector is not a complete representation of the repository's broader historical/accepted HJB upwind logic at this state.
4. Repository precedent for a third zero-liquid branch is real: the source-faithful MATLAB/Python `I0`/zero-liquid behavior and the accepted Python HJB `Z` candidate with an endogenous zero-liquid shadow and Hamiltonian comparison.
5. The current corrected D1-D3 selector and accepted corrected-HJB budget do not explicitly inherit that interior switching law. The accepted one-step budget even assumes zero scalar roots for interior-b cells. Therefore adding the `Z` branch to the corrected target would change the corrected-target derivative-selection/root contract and requires Owner authority.
6. This ambiguity is not permission to add averaging, interpolation, derivative floors, drift clipping, fitted tolerances, or an outcome-driven branch.

## Scientific interpretation boundary

The Cell-5 evidence establishes a mathematically legal zero-liquid candidate with repository precedent. It does not establish that the branch is already part of the frozen corrected D1-D3 contract, does not establish HJB convergence or economic equilibrium existence, and does not authorize KFE, production replacement, or Results.

## Owner decision required

Owner must explicitly decide whether the corrected D1-D3 selector shall inherit the repository's historical/accepted **interior zero-liquid `Z` switching law**.

If Owner adopts it, the successor task must separately freeze at least:

- the exact zero-liquid equation and scalar-root domain;
- the condition under which `Z` is eligible (including the backward/forward drift-direction crossing pattern);
- whether `q_b*` must lie inside the closed interval bounded by the two raw one-sided derivatives;
- how the zero-liquid candidate is paired with the already accepted a-side branch/KKT logic;
- Hamiltonian comparison against backward/forward candidates;
- a new finite interior-root budget replacing the prior `720 interior-b cells = 0 roots` premise;
- fail-closed behavior for no root, multiple roots, invalid domain, nonfinite arithmetic, or branch ambiguity;
- fresh Option-A execution from Cell 0 after implementation/preflight/code freeze.

If Owner does not adopt this inheritance, the current corrected selector remains two-branch and Cell 5 remains `NO_ADMISSIBLE_POLICY` for Option A under that contract. No further Option-A rerun should occur without a different explicit scientific decision.

No active scientific Builder task is authorized by this acceptance. Results eligibility=`FALSE`.
