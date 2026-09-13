# CH5 MP4C K1 — HJB value-update relaxation omega=0.5 same-input diagnostic acceptance

Date: 2026-09-13.

Reviewer verdict:

`OMEGA_0P5_SAME_INPUT_DIAGNOSTIC_ACCEPTED_AS_MIXED_EVIDENCE__NOT_A_PRODUCTION_HJB_CURE__ROUTE_REDIRECTED_TO_STANDALONE_MATLAB_FAITHFUL_CONVERGENCE_DOMAIN_SCAN`

Accepted candidate: `5576ba2f921a3ed86a6fdd2205ffb46a3dc34c9a`.

## Acceptance basis

The candidate is accepted only as a bounded same-input numerical diagnostic. It is one commit directly ahead of baseline `f905a7236084b2f23d54894fa336e074874d0c26`; changes are task-owned validator/analyzer/tests, report, compact evidence and CURRENT closeout only.

Execution facts accepted:

- exact-input coverage `62/62`;
- preregistered `omega=1` equivalence on one accepted converged and one accepted ceiling-failure call: full exact PASS;
- `64 HJB = 2 parity + 62 treatment`;
- direct solves `4,823`;
- scientific retries `0`;
- KFE/trajectory/MATLAB/firm/K1B/K2/GE/IRF/Results all `0`;
- treatment outputs after metadata-only label adjudication: `62/62` finite, correct shape and accepted label domain.

## Accepted mixed evidence

Baseline versus `omega=0.5` raw-gap convergence:

- turn1 `20/31 -> 23/31`;
- turn2 `2/31 -> 0/31`;
- all `22/62 -> 23/62`.

The intervention systematically reduces chattering diagnostics, but it is not a robust cure: seven previously converged calls are lost, all turn2 calls fail, and only `5/15` both-converged calls have value max-difference `<1e-6` with identical labels. Therefore no production solver, damping ladder, adaptive relaxation or modified HJB update is authorized.

## Scientific route correction

Owner clarified that the HJB numerical algorithm itself is established by the dissertation/MATLAB implementation and is not to be redesigned. The next priority is to identify the standalone parameter domain in which the MATLAB-faithful two-asset household HJB/KFE block yields:

1. MATLAB-style hard error / invalid transition-matrix outcome;
2. legal HJB but no value-function convergence;
3. HJB/KFE convergence with boundary-dominated steady-state distribution;
4. good steady-state convergence with finite coherent aggregates and non-pathological asset-distribution boundaries.

The immediate scan holds the original MATLAB household/grid/numerical settings fixed, fixes `rb=0.02` and borrowing gap `.07`, and varies only `ra` and the household wage input over the original multi-province ranges. This is a standalone household-block diagnostic, not a full multi-province run.

## Boundary

KFE may be used in this new standalone scan only to classify the converged household steady-state distribution and aggregates, using the already accepted MATLAB-faithful contaminated-row solve. This does not lift the separate corrected-2018 multi-province finite-box KFE blocker or authorize Results.

Results eligibility=`FALSE`.
