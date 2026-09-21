# Chapter 5 K1B turn4 安徽 F0364 first-failure — Reviewer acceptance

Date: 2026-09-21

Verdict:

`ACCEPTED_FAIL__K1B_TURN4_ANHUI_F0364_NO_ADMISSIBLE_POLICY__FORENSIC_REQUIRED`

Accepted Builder terminal:

`FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE`

Results eligibility remains `FALSE`.

## Independent Git review

- baseline: `ea2b4a99ac7ce12f950b43170bc86e8bfeede37f`
- candidate: `cc8f1ba22aa2b010325dce6e6c282802f5157c10`
- candidate tree: `150ab90ae7e24abf311550200eabfb251a945b2b`
- ancestry: 1 ahead / 0 behind
- merge-base: exact baseline
- production source changes: 0
- CURRENT changes by Builder: 0
- pre/post production-source freeze: exact
- focused tests: 6/6 PASS
- successor published by Builder: no.

The GitHub connector exposes only a paginated changed-file slice for this very large candidate. Scope acceptance therefore additionally relies on the sealed evidence manifest, source-freeze receipts and independent readback. Those support the Builder claim that no production/CURRENT drift occurred.

## Accepted first scientific failure

The first failure is accepted as real runtime evidence, not as a PASS and not yet as a selector-defect classification.

Exact object:

- province: 安徽, index 11
- checkpoint: 4
- flat F-order index: 364
- cell: `v004_f0364_b004_a018_z000`
- cell Git blob: `7ff0c9ff12ed39df1a2c1c55d195e10048914644`
- cell SHA-256: `F1170662F50FEB38BB6D26B233725B672B12397EA891C15CBBDC559DBA6DCB65`
- index `(b,a,z)=(4,18,0)`
- `b=-0.5263157894736843`
- `a=9.473684210526315`
- `z=0.8`
- selector outcome: `NO_ADMISSIBLE_POLICY`
- admissible comparison count: 0.

The sealed manifest independently binds the exact cell path to the same SHA-256.

Raw directional derivatives:

- `p_a_backward=8.895604077208148e-05`
- `p_a_forward=-0.000536125311776913`
- `p_b_backward=0.0015039676061569449`
- `p_b_forward=0.008487587452625978`.

The backward-liquid negative-transfer ordinary pair has a strict a-drift crossing:

- a-backward `g_a=1.8577376041602465`
- a-forward `g_a=-0.11099606925634653`.

The forward-liquid negative-transfer pair does not have that crossing.

## Stop-rule acceptance

Eleven provinces completed HJB/KFE before the failure.

- HJB/KFE PASS: 11/31
- direct HJB updates: 140
- SCC / restricted GESVD / stationary candidate / full-Q check: 11 each
- full-space GESVD: 0
- relaxation helper calls: 140
- alpha=1 / alpha=.5: 138 / 2
- relaxation exhaustion: 0
- scientific retries / solver substitutions: 0 / 0.

The 31/31 gate was not met, so household batch, source-faithful labor, frozen-S allocation, C1, firms, completed-turn4 raw ra0, turn5 preparation and turn5 household all remained zero. This is the correct first-failure behavior.

## Forensic target

A prior accepted Owner authority already established that interior-a zero-drift switching may use a finite **negative** D3 ratio when the liquid shadow remains positive and the implied illiquid shadow lies inside the closed one-sided derivative interval.

The current production selector contains the separate guard:

`if implied_q_b_interval[0] <= 0.0: return None`

after mapping the illiquid-derivative interval through the D3 ratio.

At the 安徽 failure the illiquid derivative interval crosses zero, unlike the earlier Beijing F0364 case. Therefore the mapped liquid-shadow interval may itself straddle zero.

This creates a precise forensic question: does the existing whole-mapped-interval positivity guard discard an otherwise admissible **positive** branch-local liquid shadow under the already accepted Owner switching contract?

That question is not answered merely by the runtime failure. It requires a zero-science scalar forensic before any selector repair or rerun.

## Evidence integrity

Evidence root:

`reports/ch5_mp4c_k1b_turn4_corrected_household_kfe_and_one_turn_integration_20260921_run001/`

- manifest entries: 2,114
- bytes: 29,129,317
- manifest SHA-256: `964E9996697698A0199F474F4AE8B9D728B8F86E3CA6C2F0F0DC7CFC3C1BB584`
- independent readback: PASS
- bad paths: 0.

## Route consequence

Turn4 runtime remains stopped.

The next task is zero-science only. It must classify the 安徽 F0364 mapped-interval/domain issue from persisted evidence and existing Owner authority.

No rerun, selector modification, HJB/KFE call, integration, turn5, K2, GE or Results is authorized by this acceptance.
