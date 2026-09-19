# CH5 MP4C 2018 KFE D1-D3 checkpoint-6 to checkpoint-10 bounded continuation acceptance

Date: 2026-09-20

Reviewer verdict:

`PASS__CHECKPOINT6_TO_10_TRAJECTORY_ACCEPTED__CHECKPOINT10_COMPLETE_NONCONVERGED__BOUNDED_CONTINUATION_TO_CHECKPOINT12_AUTHORIZED`

## Accepted candidate

- baseline live main before task: `c852473a3123513e26493db1fef75a65a8680b0d`
- Builder candidate: `537ed052a674d5f38f3586d6c94528af5e76b48b`
- candidate tree: `7f7e70ea5dee599f26fc2b7608e2c22db4b26f85`
- candidate chain: exactly `2 ahead / 0 behind`
- focused engineering gate: `83/83` passed
- source-faithful/production routes and frozen scientific laws remain unchanged
- Results eligibility remains `FALSE`

## L3 acceptance

The checkpoint-6 to checkpoint-10 trajectory is accepted.

The task reused accepted V6/P6/u6/Q6 without rerunning its policy map or Q6, consumed exactly four new HJB updates, and produced complete same-value checkpoints 7, 8, 9 and 10.

All four direct solves passed the frozen normwise backward-error gate. All four policy maps completed 800/800 cells. All four D2/Q gates passed. No exact recurrence and no authorized approximate period-2/3 recurrence was detected.

No scientific retry, damping, relaxation, adaptive Delta, parameter continuation, clipping, artificial diffusion, solver substitution, topology/KFE, MATLAB, production, GE or Results work occurred.

## Accepted checkpoint trajectory

| checkpoint | B_n | D_n | primary |
|---|---:|---:|---|
| 7 | `0.000983868092531745` | `0.0027865782347942236` | FAIL |
| 8 | `0.00016252618227152738` | `0.0006617669262674042` | FAIL |
| 9 | `8.986962138773924e-06` | `0.00011033293848816683` | FAIL |
| 10 | `3.874510913493001e-08` | `5.8692895192891115e-06` | FAIL |

The frozen primary law remains conjunctive and inclusive:

- `B_n <= 1e-8`
- `D_n <= 1e-7`.

Checkpoint 10 therefore is complete but not an HJB convergence candidate.

The strong decline in B and D and zero selected-policy identity changes between checkpoints 9 and 10 are diagnostic only. They are not a separate convergence or continuation rule.

## Accepted checkpoint 10

- V10:
  `AE1610BA320F57AF73EE3C5411C298BF00610606B13B5185F2CD65BF1736FB24`
- P10:
  `89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3`
- u10:
  `215BEC4AABBC337147D73A227751CD6A89CC483E3CA056470A2AEF161AA41F38`
- Q10 artifact:
  `917479763C4690FEAB358098D7F1CE2EBB4DD7C4939A7060156E7A4FCDEE59BD`
- Q10 identity:
  - data `B9B180F2ACF9082B5B23C1C52A27652B4FB6CD5215B7DB4816B1102400C720D2`
  - indices `9A1E128BD9B13A6711B20FB992699DB405DEF5450543921ACAB69B57FA5474E6`
  - indptr `63190CF1D9F4C98D89C81A9990736462F19170B45F97E03AD7B507D492D9C327`
- checkpoint identity:
  `4FC2855AB4102AEAE8B173D0EBBBF40FCD334583A039BE4AE65C8DE2B1145C8D`
- checkpoint arrays:
  `BEA1D08A10C53E4EF3246A413A9446633DAAD6A4ACCAD4E34463BB74756C5512`
- `B10=3.874510913493001e-08`
- `D10=5.8692895192891115e-06`
- D2 status: PASS
- exact cycle: none
- approximate period-2: none
- approximate period-3: none.

Checkpoint-10 D2 diagnostics include:

- minimum off-diagonal `2.7404765911298575e-06`
- diagonal construction error `0`
- `max(abs(Q10 @ 1))=1.4988010832439613e-15`
- zero outward closed-face violations.

## Direct solve acceptance

All four solves used the frozen equation, fixed `Delta=1000`, F order, and existing `scipy.sparse.linalg.spsolve`.

Backward errors:

- V6->V7: `2.0086287473344903e-16`
- V7->V8: `2.474008165761441e-16`
- V8->V9: `2.1980596450830867e-16`
- V9->V10: `2.1551480423314607e-16`.

All are far below the frozen `1e-12` limit.

## Evidence acceptance

Accepted evidence root:

`reports/ch5_mp4c_2018_kfe_d123_checkpoint6_to_checkpoint10_bounded_nonlinear_continuation_20260919_run001/`

Sealed manifest:

`1959B54DB2EC27BA1F12493F71E9E8AAD5F5442D20099D77EC84C0C2AE902EAC`

with `3249` entries and `52,183,186` bytes. Readback records zero missing and zero mismatched entries.

## Successor authority

No new scientific-law decision is required.

Reviewer authorizes one narrowly bounded successor from exact accepted checkpoint 10 through checkpoint 12:

`V10 -> V11 -> V12`.

The successor must stop immediately on:

- primary convergence;
- exact cycle;
- authorized approximate period-2/3 cycle;
- selector/policy-map failure;
- D2 failure;
- direct-solve accuracy failure;
- provenance/nonfinite failure;
- complete checkpoint 12.

If primary HJB convergence is reached, no additional HJB update is permitted and terminal topology/KFE remains a separate Reviewer gate.

This two-update horizon is deliberately narrow because checkpoint 10 is already close to both frozen thresholds. It is not a prediction that convergence must occur by checkpoint 12.
