# Chapter 5 Two-Asset HANK Pre-P5 Illiquid-Return Taper Authority Resolution and Numerical-Scope Review

## Terminal classification

`ILLIQUID_RETURN_TAPER_AUTHORITY_RESOLVED__P5_REVIEW_MAY_RESUME`

This is an equation-authority and read-only evidence-scope decision only. It is not P5 acceptance and does not authorize dynamics, calibration extension, or Results.

## Live authority and source continuity

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- Live start `origin/main` after fresh fetch: `1dc74aa2e43983d4a6c3ab3e95d32c5c09023eab`
- Live `origin/main` at report freeze, before the authorized report-only publication: `1dc74aa2e43983d4a6c3ab3e95d32c5c09023eab`
- The live task and predecessor dependency-closure report were present on that commit.
- Accepted Python scientific baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`
- Required continuity check, `git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`: empty.
- No Python or MATLAB source/test file was changed.

## Owner clarification recorded as repository authority

The following clarification is accepted and formalized by this report:

1. MATLAB naming was inherited from the earlier three-asset model: `b` is the liquid asset, `ah` is the domestic illiquid asset, and `af` is the foreign illiquid asset; their returns are `rb`, `rah`, and `raf` respectively.
2. The MATLAB expression `raah = rah .* (1 - 0.1*(ahmax./ah).^(-9))` came from the Kaplan/Moll two-asset numerical implementation lineage.
3. Its intended function is numerical stabilization near the upper illiquid-asset grid, reducing upper-bound policy/mass pile-up and associated HJB/distribution instability.
4. It was not intended as a structural economic assumption that domestic illiquid returns vary with the household's illiquid-asset state.
5. The present two-asset reconstruction retains only liquid `b` and domestic illiquid `a` as scientific asset states.

## Dissertation economic-equation evidence

The designated dissertation PDF and its active TeX source were inspected independently:

- PDF: `D:\Articles\2023年9月25日 博士毕业论文TEX稿件\基于异质性新凯恩斯模型的中国经济区域均衡协调发展研究.pdf`; SHA-256 `CAA45F96A68BACA6A38299248652326AE11479795827FB06E83EF71272766122`; 178 pages.
- Active Chapter 3 TeX: `D:\Articles\2023年9月25日 博士毕业论文TEX稿件\Main_Spine\c3.tex`; SHA-256 `DF6AD15190BC34023A89CD9EEF36732929B641F3B3A4D98FCFC05427199FFC57`; included by `main.tex`.

Both forms agree on the relevant structural equations:

- Equation `(3-18)` gives `dot a_h = d_h + r_ah a_h` and `dot a_f = d_f + r_af a_f`.
- Equations `(3-21)`–`(3-22)` continue to use the scalar-return terms `r_aht a_ht` and `r_aft a_ft`.
- Equation `(3-26)` gives the two-asset law `dot a = r_a a + d`.

No state-dependent illiquid-return taper appears in these economic equations. The dissertation evidence therefore does not contradict the Owner clarification; it affirmatively supports scalar `r_a` as the economic primitive.

## Final illiquid-return authority decision

`ILLIQUID_RETURN_ECONOMIC_AUTHORITY_CONSTANT_RA__MATLAB_TAPER_NUMERICAL_STABILIZATION_NOT_TO_INHERIT_AS_ECONOMIC_EQUATION`

Consequences:

- The accepted Chapter 5 illiquid drift is `mu_a = r_a * a + d`.
- Python production's constant-`r_a` drift is structurally aligned with equation `(3-26)`.
- MATLAB's effective schedule can be written `r_a_eff(a) = rah*(1 - 0.1*(a/amax)^9)`. It is a legacy upper-grid numerical stabilization device, not a missing Python economic primitive.
- Code appearance does not override the dissertation equation plus explicit Owner clarification.
- No authority exists to add the taper to Python, delete it from MATLAB, or manufacture full-HJB agreement through a new adapter.

The predecessor dependency audit's exact active-use finding remains useful for scope: the schedule affects MATLAB initialization, active illiquid drift and the upper-`a` boundary expression, as well as a post-solve statistic. That establishes MATLAB/Python full-HJB numerical non-comparability on this feature; it does not elevate the taper into an economic equation.

## Upper-`a` numerical-stabilization coverage

Classification:

`UPPER_A_NUMERICAL_STABILIZATION_NOT_EXPLICITLY_EVIDENCED_BUT_NONBLOCKING_FOR_CURRENT_P5`

| Question | Existing accepted evidence | Coverage finding |
|---|---|---|
| Upper-`a` state constraints/KKT | Final R4 reports boundary violations of approximately `8e-15` and KKT residuals approximately `9e-15` | Covered for the executed grid |
| Endogenous illiquid connectivity | `134` upward and `4` downward illiquid edges | Covered; dynamics are not one-way into the upper layer |
| Closed recurrent classes | One closed class of size `225`; recurrent `a` support `(0,1,2)` spans all three illiquid layers | Covered; an upper-`a`-only absorbing class is excluded |
| Left nullity | `1` | Covered |
| Stationary validity | `||G^T g||_inf = 3.885780586188048e-16`; normalization error `4.440892098500626e-16`; minimum mass `1.411264453687144e-17`; negative mass count `0`; mass-density consistency `3.3306690738754696e-16` | Covered |
| Mass share at `a_max` | No accepted report supplies this statistic | Not explicitly covered |
| Wider/higher illiquid-asset grid comparison | No accepted run changes the `a` support | Not covered |
| Asset-grid tail/truncation robustness | No accepted asset-upper-buffer protocol exists | Not covered |

This distinction is material: accepted evidence establishes a valid finite-grid solution, valid boundary handling, nondegenerate connectivity, and a unique stationary class. It does not directly measure whether economically material mass piles up at `a_max`, nor whether aggregates are robust to a wider illiquid-asset grid. The missing tail diagnostic is not an unresolved economic equation and does not prevent judging the current Python HA core for P5 evidence review.

## Exact R4 25-versus-29 buffer scope

The accepted final R4 protocol used:

- primary state shape `(3,3,25)`;
- buffer state shape `(3,3,29)`;
- identical asset grids in both solves: `a = [0,0.5,1.0]`, `b = [0,2.5,5.0]`;
- primary productivity support `z = 0.5:0.0625:2.0` (25 nodes);
- buffer productivity support `z = 0.5:0.0625:2.25` (29 nodes).

Thus the only support extension was productivity. The accepted common-core normalized changes of roughly `1e-9` (all below the `1e-3` threshold) establish productivity-upper-buffer robustness on that contract. They do not establish illiquid-asset upper-bound robustness and are not presented as an anti-pile-up test for `a_max`.

## P1–P4 impact

`P1_P4_SCOPE_ANNOTATION_ONLY_NO_RERUN`

- P1/P2 scalar-`r_a` comparisons remain on the dissertation-authorized economic equation.
- P3/P4 remain valid for the explicitly frozen drift/operator objects they tested.
- The tapered legacy MATLAB full HJB is not the economic-equation oracle for scalar-return Python reconstruction.
- Any mismatch caused by the taper is a known numerical-scope non-comparability, not an adverse primitive-parity finding.
- No accepted P1–P4 evidence is reopened, and no rerun is required or authorized.

## Implementation and additional-diagnostic decision

- Implementation change now: none.
- Additional bounded diagnostic before the current P5 evidence review: none.
- Future gate: before dynamics, calibration extension, or claims requiring asset-tail robustness, require a separately authorized, pre-frozen asset-grid tail diagnostic that reports `a_max` mass/policy behavior and compares against a wider/higher `a` grid without tuning after results are observed.

That future recommendation is numerical assurance only. It does not change `mu_a = r_a*a + d` and does not authorize dynamics or Results now.

## Files and operations

Files read included the live task, `AGENTS.md`, the current project-rule index and GitHub authority-routing rule, the accepted predecessor dependency report, accepted R4/truncation and P1–P4 evidence, relevant read-only Python source/tests, and the designated dissertation PDF/TeX sources.

The sole repository file written is this report:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_ILLIQUID_RETURN_TAPER_AUTHORITY_RESOLUTION_AND_NUMERICAL_SCOPE_REVIEW_REPORT.md`

Forbidden-operation check:

- MATLAB calls: `0`
- Python model/HJB/KFE/steady-state calls: `0`
- P1–P4 or R4 reruns: `0`
- deferred P5 review executions: `0`
- source/test/helper/cache modifications: `0`
- taper additions/deletions: `0`
- adapters added: `0`
- equation, tolerance, parameter, asset-bound, or fixture tuning: `0`
- dynamics/IRF/transition/calibration-extension/Results operations: `0`
- P5 acceptance issued: no

## Acceptance level and recommended next gate

Acceptance level: equation authority resolved; numerical evidence scope classified; current P5 route reopened for Owner/reviewer evidence review only. This report is not P5 acceptance.

Recommended next gate: resume the deferred

`CH5_TWO_ASSET_HANK_P5_ACCEPTANCE_DESIGN_REVISION_AND_EVIDENCE_SUFFICIENCY_REVIEW`

only after its required-read list is updated or superseded to include this report. That review must retain its own live authority and may not infer authorization for dynamics or Results.
