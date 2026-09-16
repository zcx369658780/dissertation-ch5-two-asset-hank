# CH5 MP4C 2018 KFE D1-D3 ten-cell reexecution fail-closed acceptance

Date: 2026-09-16
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
Role: L3 independent Reviewer

## Verdict

`ACCEPT_FAIL_CLOSED_EVIDENCE__7_OF_10_SELECTED_AND_D2_ADMISSIBLE__CELLS_4_8_10_NO_ADMISSIBLE_POLICY_REQUIRE_ZERO_SCIENCE_ATTRIBUTION`

Builder candidate `c46db7a335fa02caac7bbd48e3d0cfb0518ef9a2` is accepted as valid fail-closed evidence. The scientific panel itself does not PASS.

The two previously authorized implementation repairs are accepted:

- active face equalities may canonicalize a raw floating equality residual to exact zero only when that face is active and the raw residual lies inside the prospectively derived arithmetic bound; raw residual, bound, canonical value and marker are preserved;
- full selector comparison receipts are durably persisted before the strict D2 check.

D2 zero-tolerance outward-face rejection remains unchanged. No inactive/slack face is canonicalized.

## Accepted execution facts

The fresh exact preregistered ten-cell panel was executed once under frozen scientific code:

- Cells 1,2,3,5,6,7,9: `SELECTED_ADMISSIBLE` and strict D2 PASS.
- Cells 4,8,10: `NO_ADMISSIBLE_POLICY`; D2 correctly not run.
- Real selector evaluations: 10.
- Scalar roots: 31.
- Adverse-numerics retries: 0.
- HJB/KFE/MATLAB/outer/firm/wage-return/GE/annual/shock/IRF/Results: all 0.
- Post-execution scientific-code hashes match the pre-execution freeze.

This evidence is not a model-wide failure. It is a bounded finding about the frozen historical derivative/state inputs and the adopted corrected selector contract.

## Reviewer interpretation of the three failed cells

No repair is authorized by this acceptance.

Cells 4 and 8 are dual-upper M143_FINAL corners. Their receipts show that non-active upper-b branches fail because the inward upper-b derivative gives an invalid `q_b<=0` domain, while active upper-b branches fail because the adopted upper-state-constraint multiplier relation cannot produce a strictly positive `q_b` from that frozen inward derivative. This is potentially an algebraic incompatibility of the historical derivative state with the corrected state-constraint KKT, not evidence for a derivative floor or cap.

Cell 10 has positive upper-b derivative domain and active-upper-b roots do exist, but no candidate simultaneously satisfies the interior-a derivative-direction/KKT/sign conditions and upper-b feasibility. This is a different failure class from Cells 4/8.

These interpretations must be proven or falsified from existing receipts and frozen equations before any new selector call.

## Next gate

The next gate is a zero-science, no-rerun attribution task. It must classify Cells 4/8/10 into exact algebraic failure classes, check whether the selector active-set/regime enumeration is complete under the frozen D1/D3 contract, and determine whether the failures arise from:

1. structural incompatibility of the frozen historical derivative inputs with corrected KKT/state constraints;
2. an implementation/enumeration omission;
3. a derivative-direction fixed-point conflict at an interior axis; or
4. an unresolved ambiguity requiring Owner scientific choice.

No HJB, KFE, selector reexecution, root solve, parameter change, derivative floor, transfer cap, tolerance change, grid change or production edit is authorized.

Results eligibility=`FALSE`.
