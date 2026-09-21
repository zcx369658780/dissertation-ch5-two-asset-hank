# Chapter 5 两资产 HANK 当前状态

更新：2026-09-21。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`.

状态：

`K1B_TURN3_ACCEPTED__K1B_TURN4_BOUNDED_CONTINUATION_ACTIVE`

Results eligibility=`FALSE`.

## Accepted K1B-active turn3

Candidate:

`1143cd8eb6e7722d7588107a0d69f68e8dd06df7`

Acceptance:

`docs/CH5_MP4C_K1B_TURN3_CORRECTED_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_ACCEPTANCE_20260921.md`

Accepted result:

- 31/31 corrected household HJB/KFE PASS;
- checkpoint range 11-15;
- max B `6.794251272701501e-11`;
- max D `6.750061443128175e-08`;
- 377 direct HJB updates;
- relaxation: 371 alpha=1, 6 alpha=.5, exhaustion 0;
- 31 SCC / 31 restricted GESVD / 31 stationary candidates / 31 full-Q checks;
- exactly one source-faithful-labor + frozen-K1B + C1 + firm integration;
- turn3 frozen share SHA `4C3AB67F1982AEB3B707D07C53BB98C5BA54C835234DFEDE45A96B09BC5E3AB6`;
- national private-capital residual `0.0`;
- C1 GovInv total `2341682906.900551`;
- completed-turn3 raw ra0 SHA `1C587932F4E8471209663D2262DB1BB308857EEEA1198D7868E4721CFB031E8F`;
- production source changes 0;
- scientific retries / solver substitutions 0 / 0.

## Accepted turn4 entering objects

Classification:

`TURN4_K1B_INPUT_CANDIDATE_ONLY__TURN4_HOUSEHOLD_NOT_RUN`.

- population z-score mean/std: `0.5185879356888632 / 0.1907497808664968`
- z-score SHA: `67F06784094DAE4F6691AD79EA8107830FEF076CB1A2E28A96A34919E5122741`
- frozen turn4 share SHA: `5E8FB74E547CBF776A70E908F1ECA7F8FD80DD1A7637100BBD159B7F0803028B`
- turn4 household rah SHA: `7DE65A71206F52AB3D2DA98D6D01C43A8A69D8B2C423BE49A15D5D287C434BE9`
- turn4 household calls: 0
- same-turn feedback: 0.

## Active task

`tasks/CH5_MP4C_K1B_TURN4_CORRECTED_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_20260921.md`

Rationale: one K1B-active turn establishes feasibility but not repeated-turn behavior. The active task executes exactly one more bounded K1B turn4 under identical frozen economics and numerical laws, prepares turn5, and stops before turn5 household.

No beta, distance, payoff, smoothing, labor, solver, Delta or tolerance changes are authorized.

K2, production-default replacement, full outer fixed point, GE, annual dynamics, shocks, IRFs, welfare and Results remain closed.
