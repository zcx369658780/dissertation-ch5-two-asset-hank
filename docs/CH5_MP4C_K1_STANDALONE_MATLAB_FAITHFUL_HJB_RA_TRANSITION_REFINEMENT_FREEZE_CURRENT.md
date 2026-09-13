# CH5 MP4C K1 — standalone MATLAB-faithful HJB ra transition refinement freeze

Date: 2026-09-13.
Status: `OWNER_APPROVED_STANDALONE_RA_TRANSITION_REFINEMENT_3X3`.

## Owner/Reviewer decision

Keep the accepted MATLAB-faithful HJB/KFE algorithm frozen. Refine only the illiquid-return input `ra` inside the coarse transition interval identified by the accepted 3×3 scan.

The refinement fixes `rb=.02` and preserves the same household wage proxy points `w={.8,1.05,1.3}`.

Authorized `ra` points are exactly:

- `.065`;
- `.0725`;
- `.08`.

Cartesian product only: 3×3 = 9 points.

## Scientific purpose

Determine whether the stationary illiquid-asset distribution moves through an interior regime between the accepted lower-bound concentration at `ra=.055` and the artificial upper-bound pile-up at `ra=.09`.

Priority evidence:

- HJB convergence and MATLAB transition-matrix legality;
- `At` and full `a` marginal;
- `amin` and `amax` mass shares;
- modal `a` location;
- adjacent-bin comparison around the modal / upper endpoint;
- `Ct,Lt,Bt` continuity;
- stationary mass, finite checks and contaminated-row KFE receipts.

Do not require an automatic GOOD label. Preserve continuous evidence and allow Owner/Reviewer to identify an interior healthy band from the shape of the distribution.

## Frozen science

No HJB/KFE algorithm change. No damping/relaxation. No solver/tolerance/iteration-ceiling/grid/derivative-floor/FOC/selector/boundary/KFE change. No alternative wage mapping. No `rb` scan. No full multi-province outer model, firm, GE, shock, IRF or Results execution.

All non-scanned household parameters and numerics remain identical to the accepted coarse scan.

## Interpretation

A useful refinement point is one with legal/converged HJB and coherent standalone KFE receipts whose illiquid-asset distribution is materially interior rather than concentrated at `amin` or piled at artificial `amax`.

This is a numerical household-input domain map, not a final structural calibration claim.

Results eligibility=`FALSE`.
