# CH5 MP4C firm-price normalization and household-macro bridge forensic acceptance

Date: 2026-09-10

Reviewer verdict: `FIRM_PRICE_NORMALIZATION_FORENSIC_ACCEPTED__WAGE_UNIT_MISMATCH_AND_RETURN_LEVEL_EFFECTS_SEPARATED__BOUNDED_TRAJECTORY_DIAGNOSTIC_AUTHORIZED`

Accepted candidate: `770cb06b49a8ede720fdec4bbf6450c1552a4902`.

## Acceptance basis

1. The forensic cleanly separates wage and return mechanisms.
2. Wage follows the source-equivalent initialization identity `w_raw = mt*(1-alpha)*Y/L`; broad wage-bound hits therefore cannot be interpreted economically until the firm-wage/household-wage numeraire is normalized.
3. Firm return follows the source-equivalent initialization identity `ra_raw = .7240464015119004*(Y/K)-.025` under the frozen initialization contract. Common money rescaling leaves `Y/K` unchanged; the broad return-bound hits therefore reflect economic ratio levels relative to the legacy numerical safeguard, not a common-unit bug.
4. The household absolute currency normalization of `a/b` remains unresolved. The literal household-to-macro bridge remains `At*N` with an implicit coefficient one; this is not accepted as an economically identified conversion.
5. The newly surfaced `Rah.*raah` initialization expression versus later `Rah.*aaah` drift is accepted as a source-faithful forensic finding only. It is not repaired or reinterpreted here.
6. The legacy `ra` interval is accepted as a numerical/HJB-convergence safeguard, not an empirical rate interval. Intermediate boundary hits therefore do not by themselves invalidate a trajectory; final steady-state acceptance still requires no `ra` boundary hits.
7. No model/scientific solve occurred in the forensic task.

## Scientific interpretation

The next useful question is no longer whether the first initialization point is interior. The Owner has clarified that the historical MATLAB model intentionally tolerated many temporary boundary hits and judged success by whether the trajectory returned to the admissible interior and converged after repeated turns.

Therefore the next authorized scientific gate is a single bounded trajectory diagnostic that records the *time path* of boundary-hit counts and convergence gaps without tuning parameters after seeing the path.

## Boundary

This acceptance does not approve new price bounds, asset-bridge calibration, household currency normalization, solver-family replacement, KFE redesign, Results, annual simulation, GE, or IRF.
