# Chapter 5 两资产 HANK 当前状态

更新：2026-09-16。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`INTERIOR_ZERO_LIQUID_Z_OWNER_ADOPTED__OPTION_A_REEXECUTION_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted checkpoints

Owner-adopted D1/D2/D3 corrected diagnostic bundle、isolated static implementation、historical ten-cell fail-closed evidence、failed-cell algebraic attribution、corrected-HJB one-step design/input binding、Option A seed adoption，以及 lower-a zero-kink multiplier repair均继续有效。Source-faithful/production paths remain frozen。

## Cell 5 attribution accepted

Builder candidate `fdfabfb8ba12fa52add525b68050de67c2d6369d` is accepted by `docs/CH5_MP4C_2018_KFE_D123_CELL5_LIQUID_DIRECTION_SWITCH_ATTRIBUTION_ACCEPTANCE_20260916.md`.

Accepted facts: Cell 5 has one unique finite positive zero-liquid shadow `q_b*=0.01250021388291760706054915182349077777...`, strictly between the raw forward/backward liquid shadows. Historical/source-faithful `I0` and accepted Python HJB `Z` logic provide genuine zero-liquid switching precedent. The former corrected selector did not explicitly inherit that branch and its earlier root ceiling treated interior-b nodes as root-free.

## Owner adoption

Owner explicitly adopted inheritance of the interior zero-liquid `Z` switching law into the corrected D1-D3 selector. Authority: `docs/CH5_MP4C_2018_KFE_D123_INTERIOR_ZERO_LIQUID_Z_OWNER_ADOPTION_ACCEPTANCE_20260916.md`.

The adopted Z branch is generic for interior liquid direction crossings. It is a unique zero-drift root of the frozen control equations inside the interval between positive one-sided liquid shadows; it is not an average/interpolation/floor/clip/tolerance repair. Z must pass the existing a-side D1/D3/KKT/finite checks and enter the same Hamiltonian comparison as backward/forward candidates.

The one-map scalar-root ceiling is updated from 264 to 3144: retain 264 boundary-liquid roots plus at most `720*4=2880` interior-Z roots. A Z root is allowed only when the strict crossing trigger is met; the ceiling is not blanket permission to call roots.

## Active gate

Current active Builder task:
`tasks/CH5_MP4C_2018_KFE_D123_INTERIOR_Z_SWITCHING_REPAIR_AND_OPTION_A_REEXECUTION_20260916.md`。

After focused preflight and code freeze, run one fresh Option-A map from Cell 0. Ceiling: <=800 selectors, <=3144 scalar roots total, interior-Z roots <=2880, D2<=1 only after all 800 cells pass, sparse direct HJB solve<=1 only after D2 PASS, retries=0. No V1 selector map or nonlinear continuation.

KFE/MATLAB/outer/firm/wage-return/GE/annual/shock/IRF/Results remain zero. Even a full-map/direct-step PASS remains one-step diagnostic evidence only; production replacement and Results remain unauthorized.
