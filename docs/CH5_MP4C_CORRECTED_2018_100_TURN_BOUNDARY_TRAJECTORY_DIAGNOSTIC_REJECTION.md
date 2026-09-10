# Chapter 5 corrected-2018 100-turn boundary trajectory diagnostic — Reviewer rejection

Date: 2026-09-10

Candidate reviewed: `242e853708d3d0d4f891c7a043d7d4e3fba05c50`.

Reviewer verdict:

`REJECT_FOR_FROZEN_INPUT_CONTRACT_VIOLATION__TRAJECTORY_USED_LEGACY_CANONICAL_CAPITAL_SCALE_INSTEAD_OF_UNIT_NORMALIZED_TRACK_A_BASELINE`

## Reason

The exact task froze the diagnostic baseline to the already accepted corrected-2018 / unit-normalized contract: actual 2018 GDP and population, raw-NBS GFCF Track-A PIM capital, `delta_pim=.096`, `alpha=.7380939146868483`, common macro units `MU=10万元`, `NU=100 persons`, source-faithful `beta_a=1` only as a diagnostic bridge, source-lagged `rah`, no new damping/hysteresis/controller changes.

The candidate did not execute that frozen baseline. Its runtime receipt and Anhui trace show that the run inherited the earlier canonical corrected-three-turn payload and old capital/GovInv scale. For Anhui the accepted unit-normalized initialization receipt requires Track-A `K0=70,182,433.35888097 MU` and same-year `Zt0=1.681124916844091`, whereas the candidate trajectory entered turn 1 with `GovInv=1,357,314,108,201.3684` and `Zt=0.0006934644495858679`, with firm K dominated by the inherited old-scale GovInv object.

Therefore the observed persistent `ra=.02`, low `rah`, turn2->turn3 asset collapse, controller behavior, and 100-turn oscillation cannot be interpreted as the requested Track-A/unit-normalized trajectory result. The evidence remains useful only as a forensic demonstration that the legacy capital/GovInv scale can lock the system at the return lower bound.

## Acceptance boundary

- Candidate is not merged to `main`.
- No claim is made that the corrected Track-A/unit-normalized model fails to approach a steady state.
- The independent KFE/HJB diagnostic blockers observed in the candidate remain historical diagnostic evidence but are not reaccepted here as evidence about the intended corrected runtime baseline.
- Results eligibility remains `FALSE`.

## Required successor action

Before any new scientific trajectory, repair the current Python multi-province runtime/input construction so that the accepted corrected-2018 data and unit contract are the objects actually consumed by initialization and later turns. Add hard runtime receipts/assertions that make a silent fallback to canonical/legacy capital scale impossible. The implementation repair must be reviewed before any new trajectory is authorized.
