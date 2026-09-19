# CH5 MP4C 2018 KFE D1-D3 checkpoint-10 to checkpoint-12 bounded continuation acceptance

Date: 2026-09-20

Reviewer verdict:

`PASS__CHECKPOINT11_HJB_CONVERGENCE_CANDIDATE_ACCEPTED__TERMINAL_SOURCE_FREE_KFE_GATE_AUTHORIZED`

## Accepted candidate

- live main reviewed before acceptance: `6d6d07110b886c24aacf9ab28e77eaedb8ef0c82`
- Builder implementation-freeze commit: `9a0ec377358d997410fa0d7e87e34b46cda2edf6`
- Builder candidate: `47ab268e788c856b2515ebadca0356dbecbcda81`
- candidate tree: `cf526ce6be2e62ddb42cce0359495cc69a29ecc4`
- ancestry: exactly `2 ahead / 0 behind`; live main is the merge base and ancestor
- independently tree-compared changed paths: `823`
  - source driver: 1
  - focused test: 1
  - report: 1
  - evidence: 820
  - CURRENT files: 0
- main was not merged by Builder; no successor was published by Builder.

## L3 acceptance

The exact accepted checkpoint-10 state was bound successfully and not regenerated. V10 policy-map reruns and Q10 assemblies are both zero.

Exactly one new HJB update `V10 -> V11` was executed with the frozen equation, fixed `Delta=1000`, F order and `scipy.sparse.linalg.spsolve`. The direct solve passed the frozen normwise backward-error gate:

- residual infinity norm: `1.1046719095020308e-14`
- normwise backward error: `2.426444339908083e-16 <= 1e-12`
- warnings: none.

Checkpoint 11 completed all 800 policy cells, passed D2, and then passed the frozen primary HJB convergence law before any cycle classification:

- `B11 = 5.456747553811425e-11 <= 1e-8`
- `D11 = 5.4012647243695255e-08 <= 1e-7`.

The task therefore stopped immediately at checkpoint 11. `V11 -> V12` was not executed. Exact and approximate cycle checks were correctly not evaluated after primary convergence PASS.

Accepted checkpoint-11 identities:

- V11: `A097A3DDA767B979224638A51CEDC53EA635687CCDEFBE190FED0B899606921F`
- P11 canonical identity: `89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3`
- u11: `2E9A077FFA809F2DECEE385FD9E7F50C03E16750C2A074F990C0F3CBCC212648`
- Q11 artifact: `33367258F3EADB1482D4A5CB30A64A8574830C993B0E5280C451499CBD6913AD`
- Q11 CSR:
  - data `9D489C6A5C8E4A1F705CEC228EDE380FF0A5F51D569CA31DE9BCF9B4BC56537A`
  - indices `9A1E128BD9B13A6711B20FB992699DB405DEF5450543921ACAB69B57FA5474E6`
  - indptr `63190CF1D9F4C98D89C81A9990736462F19170B45F97E03AD7B507D492D9C327`
- checkpoint-11 identity: `8093BE714CA83531816B20DFEB2BAB3DCB7AF9B971AD255C3596C1CA2A9E2A3B`
- checkpoint arrays: `F620823F15CEB71A168437880AC8655FCBC075D0B7894CBA013780759A8157B2`.

D2 acceptance includes:

- Q11 nnz `3118`
- same CSR sparsity pattern as Q10
- `||Q11-Q10||inf = 0.0001457303875539162`
- minimum off-diagonal `2.7404782515125115e-06`
- diagonal construction error exactly `0`
- `max(abs(Q11 @ 1)) = 1.7763568394002505e-15`
- zero outward closed-face violations
- liquid/illiquid coordinate-action maximum errors `1.0658141036401503e-14` and `2.7200464103316335e-14`.

Scientific ledger is accepted: 1 solve/update, 1 policy map, 800 selector evaluations, 270 scalar roots, 14 liquid-Z roots, 1 interior-a switching root, 0 joint roots, 1 D2/Q assembly, 1 checkpoint evaluation, 0 scientific retries, 0 solver substitutions, 0 prohibited numerical adjustments, 0 topology/KFE/SVD/eigen/nullspace/Q.T@p calls and 0 downstream calls.

Evidence root:

`reports/ch5_mp4c_2018_kfe_d123_checkpoint10_to_checkpoint12_bounded_nonlinear_continuation_20260920_run001/`

Sealed manifest:

`5E67E595B32024213EC5E6517389A7DCA6462A24FB735B06EB2F85D6E1621E41`

with `819` entries and `13,089,592` bytes; recorded path/byte/SHA-256 readback failures are zero. Focused tests: `87/87` PASS. Pre/post scientific-code hash maps match.

## Non-blocking diagnostic representation note

The checkpoint-11 manifest reports `policy_diagnostics.identity_change_count=800` while the canonical P11 identity equals P10 exactly. Reviewer inspected the implementation and representative serialized cells.

The rowwise counter directly compares in-memory `_selected_identity` dictionaries. Current selector `active_constraints` is a tuple, while accepted P10 receipts are JSON-loaded lists. Those representations compare unequal in Python even though canonical JSON normalization yields the same policy identity. Representative serialized cells 0, 185, 760 and 799 match exactly on derivative branches, active constraints, transfer branch and switching markers.

Therefore `identity_change_count=800` is a representation-only false-positive diagnostic and is not accepted as a scientific policy-change count. It does not enter B/D convergence, D2, the direct solve, or the terminal KFE contract. No HJB rerun is authorized to repair this diagnostic.

## Successor authority

Checkpoint 11 is accepted as the HJB convergence candidate under the frozen corrected household prices/calibration.

The next and only active scientific task is a separate terminal same-value topology/source-free KFE validation on exact Q11:

`tasks/CH5_MP4C_2018_KFE_D123_CHECKPOINT11_TERMINAL_SOURCE_FREE_KFE_VALIDATION_20260920.md`.

No HJB update, policy remap or Q11 reassembly is authorized in that task.

Production, market clearing, GE, annual calibration/dynamics, shocks, IRFs, welfare and Results remain closed. Results eligibility remains `FALSE`.
