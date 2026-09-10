# Single-loop staged calibration contract

## Observables

- `gK=max_i abs(KNratio_i/tKNratio_i-1)`.
- `gY=max_i abs(Y_i/Y_prev_i-1)`.
- `gGDP=max_i abs(Y_i/Y0_i-1)`.
- `ra_bound_count`: exact lower/upper safety-bound hits.
- `gov_trigger_count`: provinces with clipped `ra<.04` or `ra>.07`.
- `dZ=max_i abs(Z_used/Z_old-1)` and `dG=max_i abs(GovInv_used/GovInv_old-1)`.
- `household_converged_count` and explicit density/operator validity remain independent scientific gates; staging cannot waive them.

## Stage A — stabilization

- Run the unchanged ordered household/allocation/firm map when scientifically authorized in a future task.
- Apply only approved w/rah damping.
- Freeze Zt and GovInv; log firm price bounds and all gaps.
- Enter Stage B only after both `gK` and `gY` remain below the preregistered `epsilon_enter` for `m_enter` consecutive turns.

Candidate grid: `epsilon_enter ∈ {.10,.05,.02}` and `m_enter ∈ {2,3,5}`. The source `.10` K/N gate is the baseline cell; adding gY is a proposed guard.

## Stage B — near-steady online calibration

- Preserve a single loop; do not wait for full `1e-9` convergence.
- Preserve source controller order: compute/log Zt proposal first when province GDP gap exceeds `.01`; then compute/log GovInv proposal from clipped ra (`×.9` below `.04`, `×1.1` above `.07`, hold otherwise).
- Store old, raw proposal, used value, relative change, trigger, and stage for every province.
- Continue w/rah damping and ordinary household/firm turns.
- Return to Stage A only if either gK or gY exceeds `epsilon_exit=2*epsilon_enter` for the preregistered exit count. This is hysteresis; a single small crossing does not chatter stages.

## Stage C — calibration freeze and confirmation

Candidate entry requires, for `m_freeze ∈ {3,5}` consecutive turns:

- `gGDP<=.01` (unchanged source GDP controller band);
- `gov_trigger_count=0` (all clipped ra in `[.04,.07]`);
- `max(dZ,dG) <= epsilon_controller`, with `epsilon_controller ∈ {1e-3,1e-4}`;
- gK and gY below a preregistered freeze threshold no looser than the selected Stage-B enter threshold.

On entry, freeze Zt and GovInv and continue the same loop. Final acceptance remains exactly the source predicate: `gK<1e-9`, `gY<1e-9`, 31/31 household convergence, and zero ra lower/upper-bound hits. Wage-bound counts remain diagnostic unless a later scientific task changes authority.

If Stage C violates the selected exit gate for the selected consecutive count, record `FINAL_CONFIRMATION_DESTABILIZED`, reopen Stage B, and retain the failed confirmation evidence. Do not launch a second full steady-state solve.

## Non-authority

The grids above are pre-registration candidates, not tuned production constants. No trajectory was run or inspected in this task. A future exact task must freeze one bounded matrix and a total turn/model-call budget before execution.
