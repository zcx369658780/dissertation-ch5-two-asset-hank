# Chapter 5 corrected-2018 three-turn propagation validation

## Verdict

`CORRECTED_2018_THREE_TURN_FAIL__UPSTREAM_STATE_OR_FIRM_BLOCKER`

Terminal classification: `EVIDENCE_PERSISTENCE_COLLISION_AFTER_TURN2__TURN3_NOT_ENTERED`.

The only scientific process completed fresh turns 1 and 2, and both reproduced the accepted two-turn package exactly (`mismatch_count=0`). Before turn 3 entry, the runner attempted a second exclusive write of `predecessor_reproduction.json` and stopped with `FileExistsError`. No model, HJB, KFE, firm, controller, or province update for turn 3 was attempted. Scientific retry was prohibited and was not performed.

## Observed prefix

Anhui turn 1 and turn 2 remain exactly the accepted values, including household `rah` `0.089999999999999997 -> 0.082989205887981601`, raw firm `ra0` `-0.024969971131121638 -> -0.024968505109415375`, used `ra=0.02`, raw wage `2.5721358283733027 -> 2.1373365306922518`, and HJB iterations `64 -> 31`.

Turn-3 Anhui `rah`, provenance, firm state, national distributions, gap and adaptation behavior are **NOT CHECKED** because turn 3 was not entered. No inference from the prepared state is substituted for a scientific observation.

## Calls

- scientific processes: 1
- trajectory attempts/returns: 1/0
- turns entered/completed: 2/2
- province updates attempted/completed: 62/62
- household/HJB/KFE/firm returns: 62/62/62/62
- HJB/KFE direct solves: 2599/62
- labor roots/Brent: 49600/49600
- scientific retries: 0
- MATLAB/GE/annual/IRF/Results/turn4+: 0/0/0/0/0/0

## Post-failure repair boundary

The executed runner was preserved at SHA-256 `B56DE7A2A32251E6CBD37D0EAA1AD79B9E1CC8923CF78B70B411248C78845363`. The one-line persistence sequencing defect was repaired and static-tested at SHA-256 `1D53DADBC5D6AD75A695DCD84829C46F657795F368EA25248A5EE13B8C129813`, but the repaired runner was **not scientifically executed**. This repair does not convert the failed task into a PASS or authorize a retry.

Canonical workbook SHA-256: `AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`. Turn 4 authorized: **NO**. Steady state authorized: **NO**. Results eligibility: **FALSE**.
