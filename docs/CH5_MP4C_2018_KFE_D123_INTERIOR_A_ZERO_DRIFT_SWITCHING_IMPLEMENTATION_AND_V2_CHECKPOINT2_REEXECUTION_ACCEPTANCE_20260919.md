# CH5 MP4C 2018 KFE D1-D3 adopted interior-a switching implementation and V2 checkpoint-2 reexecution acceptance

Date: 2026-09-19

Reviewer verdict:

`PASS__ADOPTED_INTERIOR_A_SWITCHING_IMPLEMENTATION_ACCEPTED__CELL100_CLOSED__V2_FIRST_FAILURE_CELL185_SIMULTANEOUS_TWO_AXIS_SWITCHING_ADJUDICATION_REQUIRED`

## Accepted candidate

- baseline live main before task: `869f4023ae7b674d483f926f85e0de271479da0e`
- implementation freeze: `243548e062269b70a2b1905106765b6575d55253`
- Builder candidate: `fc9ac9464a0bcc0a1e4b6f2dafbd8795cf79bf6b`
- candidate tree: `058293b5d9614f3cba80726815f32b4ff0edc7a7`
- candidate chain is exactly `2 ahead / 0 behind` baseline
- source-faithful/production paths and D2 equation remain unchanged
- Results eligibility remains `FALSE`

## L3 acceptance of implementation

The Owner-adopted interior-`a` zero-drift switching law is implemented consistently with its authority.

Focused engineering tests passed `59/59`; Python compile and `git diff --check` passed. The implementation preserves the existing liquid-`Z`, lower-`a` zero-kink, D1/D2/D3, grid, calibration, root tolerance/solver family, HJB update law and nonlinear convergence law.

The scientific run used one fresh accepted-V2 policy-map attempt and no retry.

## Cell100 closure accepted

The adopted switching candidate at flat F index `100` is accepted as a valid closure of the previous one-sided crossing.

Accepted selected candidate:

- `q_b=0.012448197327813425`
- `q_a=0.008962703432234596`
- `d_Z=-0.236841961910238`
- raw `g_b=-5.620504062164855e-16`, canonical `g_b=0`
- `g_a=0`
- lower-b multiplier `0.00011488612109684763`
- D3 transfer-KKT residual `0`
- D2 assembler admissible `true`
- selector outcome `SELECTED_ADMISSIBLE`.

The root is inside the Owner-adopted exact interval and uses the existing frozen root routine/tolerance. No endpoint interpolation or unadopted two-axis switch is involved at cell100.

## First new scientific failure

The repaired map continues through cell184 and fails first at flat F index `185`, zero-based `(i_b,i_a,i_z)=(5,9,0)`, physical `(-0.1578947368421053,4.7368421052631575,0.8)`.

This cell is interior in both `b` and `a`.

Its frozen one-sided derivatives are:

- `p_b^B=0.013362109688537174`
- `p_b^F=0.009574726769001294`
- `p_a^B=0.00857557540065246`
- `p_a^F=0.008489317330830281`.

The existing liquid-`Z` law produces two negative-transfer zero-liquid-drift candidates:

- with backward-`a` shadow: `q_b=0.011845651796693632`, `g_b=0`, `g_a=+0.009287240997760404`, rejected because backward-`a` is direction-inconsistent;
- with forward-`a` shadow: `q_b=0.011826220238545775`, `g_b=0`, `g_a=-0.005170298666228812`, rejected because forward-`a` is direction-inconsistent.

Thus the strict `a` crossing emerges only after using the already-adopted liquid-`Z` shadow. Closing it would require a **jointly selected interior-`a` zero-drift shadow and interior-liquid zero-drift shadow**.

The current Owner adoption explicitly prohibits creating such a simultaneous newly-created two-axis switching candidate. The selector therefore correctly fails closed. This is not an implementation defect under current authority.

## Scientific ledger accepted

The run ledger is accepted:

- accepted V1/V2/Q1 loads: `1 / 1 / 1`
- fresh V2 policy maps: `1`
- selector evaluations: `186`
- total scalar roots: `99`
- existing liquid-`Z` roots: `40`
- adopted interior-`a` switching roots: `2`
- Q2/D2 assemblies: `0`
- checkpoint-2 diagnostics: `0`
- direct HJB solves / V2->V3: `0 / 0`
- topology/KFE/SVD/eigen/nullspace/`Q.T@p`: `0`
- scientific retries: `0`
- MATLAB/production/GE/annual/shock/IRF/Results: `0`.

The sealed evidence contains `194` entries totaling `2,982,663` bytes and includes exactly 186 durable V2 cell receipts through cell185.

## Consequence

No complete P2/u2/Q2 exists, so no B2/D2, policy/operator/cycle or terminal KFE claim exists.

The cell100 issue is closed. The next scientific object is cell185's potential **simultaneous two-axis zero-drift switching law**. Existing authority deliberately leaves this unadopted.

A zero-science scientific adjudication may study whether such a joint branch is mathematically supported, but no implementation/runtime is authorized until Owner later adopts a supported contract.

Production replacement, market clearing, GE, annual calibration, dynamics, IRF, welfare, causal interpretation and Results remain closed.
