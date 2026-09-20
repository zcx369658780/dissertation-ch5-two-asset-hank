# Chapter 5 两资产 HANK 当前状态

更新：2026-09-21。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`HEBEI_F0005_COMPOSITION_FALSE_NEGATIVE_CONFIRMED__LOWER_A_INTERIOR_Z_REPAIR_TURN1_POLICY_PARITY_AND_TURN2_RUN004_ACTIVE`

Results eligibility=`FALSE`。

## Latest accepted forensic

Accepted candidate:

`26853c49a06ba0cc3da88df2df250f2f0fd22ff8`

Acceptance:

`docs/CH5_MP4C_TURN2_HEBEI_F0005_LOWER_A_LIQUID_SWITCH_FORENSIC_ACCEPTANCE_20260921.md`

Accepted classification:

`IMPLEMENTATION_COMPOSITION_FALSE_NEGATIVE_UNDER_ALREADY_ADOPTED_AUTHORITY`

The current 河北 checkpoint-1 flat-5 `NO_ADMISSIBLE_POLICY` is not a valid terminal under existing authority.

## Exact accepted combined candidate

At:

- 河北
- checkpoint 1
- flat 5
- `(b,a,z)=(-0.1578947368421053,0,0.8)`
- active lower-a
- interior liquid b

the already adopted lower-a zero-kink and interior-liquid Z laws uniquely imply:

- branches: `a=forward, b=zero`
- transfer: zero-kink
- `q_b=0.012085132579009488`
- `q_a=0.01087661932110854`
- `lambda_a=0.00028489863234105843`
- `d=0`
- `g_a=0`
- `g_b=0`
- KKT/complementarity residuals: 0
- Hamiltonian: `-0.1280816705218543`
- admissible: true.

The root is the unique positive zero of the existing liquid-drift equation inside the closed derivative interval.

## Implementation omission

Current ordinary endpoint construction returns early when the forward endpoint lower-a kink intersection is empty. That endpoint then lacks `g_b`/arithmetic-bound data, so the interior-Z constructor returns before root reconstruction.

Existing authority requires recomputing lower-a KKT at the switching shadow, so endpoint full lower-a admissibility cannot suppress this Z family.

This is an implementation composition omission only. No new equation/KKT/boundary/root/tolerance/calibration choice is required.

## Current active task

`tasks/CH5_MP4C_LOWER_A_INTERIOR_Z_COMPOSITION_REPAIR_TURN1_PARITY_AND_TURN2_RUN004_20260921.md`

Required ordering:

1. implement the narrow active-lower-a + zero-kink + interior-liquid-Z composition repair;
2. prove exact 河北 F0005 focused parity;
3. preserve F0364 and unrelated selector behavior;
4. replay all 408 accepted turn-1 policy maps;
5. only 408/408 exact identity parity authorizes fresh turn-2 run004;
6. stop at first new scientific failure or after one turn-2 integration;
7. do not run turn 3.

## Preserved authorities

Terminal KFE remains:

`OWNER_ADOPTED__UNIQUE_CLOSED_CLASS_SUPPORT_KFE_AS_TERMINAL_KFE_AUTHORITY`

Accepted selector authorities remain:

- active-upper-b negative branch enumeration repair;
- generic interior-liquid Z switching law;
- interior-a zero-drift switching law;
- interior-b finite-negative-ratio interior-a switching repair;
- lower-a zero-kink multiplier law.

The active task changes only their missing lower-a/Z implementation composition.

Turn3, K1B, K2, GE and Results remain closed.
