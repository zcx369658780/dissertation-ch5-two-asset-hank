# Chapter 5 session handoff archive — 2026-09-17 nonlinear V2 cell100 gate

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

This document is the durable GitHub-side handoff for the long Reviewer/Owner session ending after acceptance of the first bounded nonlinear continuation failure.

## 1. Governance and authority

- Owner is final scientific authority.
- ChatGPT acts as L3 independent Reviewer/scientific-route authority.
- Codex is bounded Builder/executor.
- GitHub live `main` is repository-state authority.
- `zcx369658780/deep-learning-hank` is a separate project and must never be used for this route.
- Protected/source-faithful MATLAB remains read-only.
- Corrected diagnostic successor work is separately governed and is not production replacement.
- Results eligibility remains `FALSE`.

Standing workflow: Reviewer may accept/fast-forward a clean Builder candidate and publish the next bounded task when no new Owner scientific/economic decision is required. Owner approval is required for new economic laws, major calibration, production replacement, causal interpretation and Results eligibility.

## 2. Accepted corrected household route

Owner-adopted corrected semantics include:

- D1 artificial upper numerical state constraints;
- D2 consumed-total-drift conservative generator assembly with actual neighbor distances, nonnegative retained rates, strict outward-boundary rejection and diagonal equal to negative retained outgoing-rate sum;
- D3 adjustment cost `C(d,a)=chi0*|d|+chi1*d^2/(2*max(a,a_bar))` with consistent KKT/transfer law;
- active lower-a zero-kink multiplier interval handling;
- interior zero-liquid `Z` switching law.

Call-725 corrected grid/calibration authority remains frozen. The practical state grid is `(b,a,z)=(20,20,2)`, F-order, b fastest.

## 3. Q0/V0 route and KFE findings

Accepted Option-A V0 seed was used to build a complete corrected 800-cell policy map and D2 operator Q0, followed by one direct HJB step V1.

Q0 source-free KFE uniqueness failed structurally because its exact-positive graph had two closed classes:

- class A `[5,405]` at asset node `(i_b,i_a)=(5,0)`;
- class B `[6,406]` at asset node `(6,0)`.

The four recurrent states were lower-a active zero-kink + interior-liquid Z states with exact `g_b=g_a=0`; only `z` switching remained. The two-sink result was explicitly **not** interpreted as economic multiple equilibria.

## 4. V1 remap / Q1 route

A fresh V1 policy remap produced a complete 800-cell map and Q1.

Q1 SHA-256:
`5F96C2CFAAFB3EA7EF32943A892A9191FEDCC5DBC7AB28D066F5893D3F560D1E`

Q1 exact-positive graph has one closed class:
`[5,6,405,406]`.

The previous two Q0 sinks merge because flat 405 gains a forward liquid edge and flat 6 gains a backward liquid edge, while flats 5 and 406 retain Z/zero drift.

The accepted Q1 pin-free/source-free KFE validation established:

- exactly one closed communicating class;
- numerical rank/nullity `799/1`;
- second-smallest singular value `0.01704325702964291` above frozen rank threshold;
- unique normalized invariant probability mass under the frozen arithmetic allowance;
- no row replacement, pin or balancing source.

This remains operator-level evidence only.

## 5. Accepted nonlinear HJB-KFE design

Accepted design candidate:
`ee83051d40c1389618288cef61d7d97711c1a861`.

Frozen design:

- nonlinear state is only `V_n`;
- `P_n,u_n,Q_n` are same-value derived checkpoint objects;
- order is derivatives -> complete corrected policy map -> D2 `Q_n` -> Bellman/value/stability metrics -> convergence/cycle decision -> at most one implicit HJB update;
- KFE is terminal-only after HJB convergence and must use final same-value `Q*`;
- `Delta=1000` fixed;
- complete call-725 trajectory has at most 100 HJB updates.

## 6. Owner-adopted corrected-target convergence law

Authority:
`docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_CONVERGENCE_LAW_OWNER_ADOPTION_20260917.md`.

Owner adopted:

- Bellman residual `B_n=||rho V_n-u_n-Q_n V_n||_inf <= 1e-8`;
- value change `D_n=||V_n-V_(n-1)||_inf <= 1e-7`;
- both must hold at the same checkpoint;
- policy/operator stability is mandatory diagnostic evidence only, not a convergence condition;
- each direct HJB solve requires normwise backward error `<=1e-12`;
- exact full-checkpoint recurrence at period `k>=2` before convergence fails closed;
- approximate periods 2/3 use complete lag-k windows with threshold `1e-8` after primary convergence fails;
- no more than 100 total HJB updates;
- no damping, relaxation, adaptive Delta, parameter continuation, clipping, artificial diffusion, solver substitution, scientific retry or post-hoc tolerance tuning.

## 7. Latest bounded nonlinear continuation and accepted failure

Builder candidate:
`922cd9118d617c044209515762ccecc9ec3fd34d`.

Builder terminal verdict:
`FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE`.

Reviewer acceptance:
`PASS__FAIL_CLOSED_CONTINUATION_EVIDENCE_ACCEPTED__V1_TO_V2_LINEAR_STEP_VALID__V2_CELL100_NO_ADMISSIBLE_POLICY_REQUIRES_ZERO_SCIENCE_ATTRIBUTION`.

Checkpoint 1:

- `B1=0.014710294187010184` > `1e-8`;
- `D1=0.47118375690461445` > `1e-7`;
- therefore not converged.

Exactly one new HJB update was executed:

- `V1 -> V2`;
- direct residual infinity norm `1.9012569296705806e-14`;
- normwise backward error `2.5514110567283015e-16`, passing `<=1e-12`;
- V2 SHA-256 `A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.

Fresh checkpoint-2 policy map:

- cells 0-99 passed;
- first failure at flat F index `100`;
- zero-based `(i_b,i_a,i_z)=(0,5,0)`;
- physical `(b,a,z)=(-2.0,2.6315789473684212,0.8)`;
- `p_b^B=p_b^F=0.012333311206716577`;
- `p_a^B=0.00903315440190679`;
- `p_a^F=0.008957007194295222`;
- selector outcome `NO_ADMISSIBLE_POLICY`;
- admissible comparisons `0`.

Because the policy map failed at cell 100:

- no complete P2/u2 exists;
- no Q2/D2 assembly exists;
- no B2/D2/policy-operator stability/cycle gate exists;
- no terminal topology/KFE was executed;
- checkpoint 1 remains the last complete same-value checkpoint;
- V2 is a valid linear-update output and incomplete-checkpoint input only.

Scientific ledger of the latest runtime:

- accepted V1 artifact loads 1;
- accepted Q1 loads 1;
- new policy maps attempted 1;
- selector evaluations 101;
- scalar roots 51;
- interior-Z roots 20;
- D2 assemblies 0;
- direct HJB solves 1;
- graph/SCC 0;
- KFE/SVD/`Q.T@p` 0;
- scientific retries 0;
- MATLAB/downstream/Results 0.

Sealed-manifest SHA-256:
`FC323B9691E28F20305CF5F71DD379C445CB80A506313A67DBC1954E88A5E041`.

## 8. Current scientific interpretation

Do not interpret the latest failure as nonlinear HJB nonexistence.

Current accepted statement is narrower: under the frozen corrected selector and accepted V2 derivatives, the first failing cell at the lower liquid boundary has no admissible selected policy in the current implementation/evidence.

Raw candidate rejection mechanisms include:

- lower-b primal infeasibility;
- b/a derivative-direction inconsistency;
- transfer-sign or transfer-KKT failures;
- one `ROOT_FAILURE_NO_UNIQUE_BRACKET`.

These are attribution targets, not repair authority.

## 9. Current active task

`tasks/CH5_MP4C_2018_KFE_D123_V2_CELL100_NO_ADMISSIBLE_POLICY_ZERO_SCIENCE_ATTRIBUTION_20260917.md`

This is zero-science only. Required classification:

- `ATTRIBUTED__FROZEN_V2_CELL100_LOCAL_KKT_INPUTS_STRUCTURALLY_INCOMPATIBLE`
- `ATTRIBUTED__SELECTOR_OMITS_AUTHORITY_BACKED_LEGAL_BRANCH`
- `ATTRIBUTED__ROOT_IMPLEMENTATION_OMISSION_WITHIN_AUTHORIZED_BRANCH`
- `BLOCKED__OWNER_SCIENTIFIC_DECISION_REQUIRED`
- `BLOCKED__INSUFFICIENT_PERSISTED_EVIDENCE`

All selector/root/policy-map/D2/HJB/KFE/MATLAB/downstream scientific calls must remain zero. No repair or reexecution is authorized before independent acceptance.

## 10. Startup order for the next session

Read in this order:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. this archive handoff
6. latest fail-closed acceptance and Builder report
7. Owner convergence-law adoption
8. current active zero-science task
9. exact cell-100 receipt and frozen selector/D1/D3/Z/KKT authority as needed.

The next Reviewer should independently inspect any Builder attribution candidate before merge. If attribution identifies an already-authorized selector/root implementation omission, Reviewer may publish a narrowly bounded repair/reexecution task without reopening economic law. If attribution finds genuine frozen KKT incompatibility or requires a new scientific law, stop and escalate appropriately.

Production replacement, GE, market clearing, annual calibration, dynamics, IRF, welfare, causal interpretation and Results remain outside the current gate.