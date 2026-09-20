# CH5 MP4C 2018 KFE D1-D3 checkpoint-11 terminal source-free KFE validation acceptance

Date: 2026-09-20

Reviewer verdict:

`PASS__CHECKPOINT11_TERMINAL_SOURCE_FREE_KFE_ACCEPTED__CONDITIONAL_HOUSEHOLD_HJB_KFE_FIXED_POINT_ESTABLISHED`

## Accepted candidate

- live main before Builder task: `bc10e8778dab6d8ba00feaa0b18fc5957d7b6435`
- Builder implementation-freeze commit: `cf265c874f13b4612643acea3c697109a35864fc`
- Builder candidate: `e8aec1d2138b2cfa3c0896f4f5d95430478c635f`
- candidate tree: `83ff62d418178243d678d457066e7227f7c4aa86`
- ancestry: exactly `2 ahead / 0 behind`
- changed files: 16
- CURRENT files changed by Builder: 0
- Builder did not merge main and did not publish a successor.

## Exact accepted household object

Checkpoint-11 HJB authority remains:

- V11 `A097A3DDA767B979224638A51CEDC53EA635687CCDEFBE190FED0B899606921F`
- P11 `89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3`
- u11 `2E9A077FFA809F2DECEE385FD9E7F50C03E16750C2A074F990C0F3CBCC212648`
- Q11 `33367258F3EADB1482D4A5CB30A64A8574830C993B0E5280C451499CBD6913AD`
- checkpoint identity `8093BE714CA83531816B20DFEB2BAB3DCB7AF9B971AD255C3596C1CA2A9E2A3B`
- B11 `5.456747553811425e-11`
- D11 `5.4012647243695255e-08`
- D2 PASS
- primary HJB convergence PASS.

The predecessor 819-entry evidence manifest was completely read back before terminal science. Q11 was sparse-loaded exactly once; policy remap, Q11 reassembly, HJB update and checkpoint-12 work were all zero.

## Structural/topology acceptance

Q11 is an `800 x 800` CSR generator with 3,118 nonzeros and zero negative off-diagonals. The accepted D2 construction remains bound exactly.

Independent terminal audit:

- exact-positive directed edges: `2318`
- SCC count: `13`
- closed communicating classes: exactly `1`
- closed-class size: `320`
- closed-class membership: F-order flat indices `240..399` and `640..799`
- transient states: `480`
- `max(abs(Q11 @ 1)) = 1.7763568394002505e-15`
- frozen conservation bound: `1.8450485966201867e-14`.

The Q11 closed class was discovered from Q11 itself and was not imposed from historical Q1.

## Numerical nullspace acceptance

Exactly one full dense
`scipy.linalg.svd(A, full_matrices=True, lapack_driver="gesvd", check_finite=True)`
was executed with `A=Q11.T` and no removed/replaced row.

Accepted diagnostics:

- rank / nullity: `799 / 1`
- singular values at or below `tau_rank`: `1`
- `sigma_max = 18.528640726738875`
- second-smallest `= 3.400562953690602e-06`
- smallest `= 1.2380844366549938e-16`
- `tau_rank = 3.554655589411806e-12`
- second-smallest / threshold `= 956650.473767361`
- warnings: none.

Structural closed-class count and numerical nullity agree at one.

## Source-free invariant mass acceptance

Exactly one null-vector orientation decision and one total-mass normalization were used. No clipping, absolute-value repair, truncation, second normalization, pin equation, row replacement, source RHS or balancing source occurred.

Accepted source-free mass diagnostics:

- `||Q11.T @ p||inf = 1.9114484300919443e-16`
- `tau_stationarity = 6.317146315298578e-13`
- backward ratio `= 5.804911693166085e-17`
- `math.fsum(p)=0.9999999999999999`
- `omega*math.fsum(g)=0.9999999999999999`
- minimum p `=-1.4797178815899388e-16`
- arithmetic nonnegative allowance `=1.9184653865526386e-13`
- total negative mass `=3.612331458450193e-15`
- total-negative bound `=1.5347723092421108e-10`.

Accepted stationary-mass identities:

- artifact `1DD70201EAC5EED0AE768362D99A76736276BFB4D5E6AF0D8DBDB4E9D6FE7D16`
- p `E215FAE862DA81AD6DEB603859709EA0CF73B8F6F1897567DF942B186CD65ED7`
- g `D02592257722313B81C7A1DB40B799ADED8E8BDB5100A65C469E0997DA22E1CE`
- stationarity residual `8711794D28F3EEECC5F316B0AB69625E9CEFA72823556BA86F0EBEE75EDF6ED7`.

## Ledger and evidence acceptance

Scientific ledger:

- Q11 load / structural audit / Q11@1: `1 / 1 / 1`
- graph / SCC / dense gesvd: `1 / 1 / 1`
- stationary candidate / orientation / normalization: `1 / 1 / 1`
- Q11.T@p: `1`
- scientific retry / solver substitution: `0 / 0`
- row replacement / direct KFE solve: `0`
- policy / selectors / roots: `0 / 0 / 0`
- D2 reassembly / HJB / checkpoint 12: `0 / 0 / 0`
- downstream: `0`.

Wall time `1.525664599990705s`; peak resident memory `100,478,976` bytes.

Evidence root:

`reports/ch5_mp4c_2018_kfe_d123_checkpoint11_terminal_source_free_kfe_validation_20260920_run001/`

Sealed manifest:

`B7C06E3C369B6A5400DE76252DD70A539EFF1F2E4072C04639A1E93E512F5C1D`

with 12 entries and 41,890 bytes; readback failures are zero. Focused tests: 21 PASS. Pre/post scientific-code hashes match.

## Scientific interpretation

For the frozen corrected household prices/calibration, the project now has an accepted same-value pair:

- HJB convergence at V11/P11/u11/Q11; and
- a unique, normalized, nonnegative-within-arithmetic-allowance, pin-free/source-free invariant mass for the same Q11.

This establishes the conditional household HJB-KFE fixed-point candidate required to reopen the deferred integration route.

It does not by itself establish a multi-province outer fixed point, market clearing, final payoff-return authority, production replacement, GE, annual dynamics, shocks, IRFs, welfare or Results eligibility.

Historical K1A trajectories that used the earlier diagnostic KFE route remain diagnostic only and are not retroactively upgraded.

## Successor authority

No new economic law is required for the next step.

The next active task is a zero-solver corrected-household aggregate/interface binding task:

`tasks/CH5_MP4C_2018_CORRECTED_HOUSEHOLD_FIXED_POINT_AGGREGATE_AND_ADAPTER_BINDING_20260920.md`.

It may recover and bind the accepted source aggregation formulas, aggregate the already accepted checkpoint-11 mass/policies once, and build an opt-in corrected household adapter/fixture. It may not run HJB/KFE/firm/outer/GE science or switch the production default.

The separate Owner payoff-return/period/numeraire decision remains required before any new K1B or outer-loop runtime change.

Results eligibility remains `FALSE`.
