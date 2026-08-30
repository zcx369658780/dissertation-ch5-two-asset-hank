# CH5_TWO_ASSET_HANK_OWNER_MATLAB_FAITHFUL_NUMERICAL_APPROXIMATION_AUTHORITY_RESET_AND_GAP_AUDIT

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / auditor

Owner: final scientific authority

## 1. Purpose

Freeze an Owner-directed route reset for Chapter 5 reconstruction: the final Python target is no longer the mathematically regularized / corrected-equation reconstruction as the sole production authority. The primary reconstruction target is now a **MATLAB-faithful numerical implementation** that preserves the designated MATLAB/Moll/Kaplan-style numerical approximations used by the working Chapter 5 code, even where those approximations deliberately trade tiny mathematical inconsistency for numerical stability, solvability, or computational efficiency.

This task is an authority-reset and static gap-audit task only. It must not yet mutate Python production source/tests or rerun scientific HJB/KFE/steady-state/dynamics.

The immediately preceding supplementary corrected-equation parity chain is frozen at:

`docs/CH5_TWO_ASSET_HANK_POST_P5_D2_COMPARATOR_INPUT_CONTAINER_NORMALIZATION_AND_RESUMPTION_REPORT.md`

with accepted terminal classification:

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

That chain must not be resumed through a wrapper-aware D2 comparator task unless a future Owner task explicitly reopens it.

## 2. Owner authority reset

Freeze the following marker as the new primary reconstruction authority:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

Interpretation:

1. Dissertation equations continue to determine economic interpretation and notation.
2. The designated working MATLAB implementation determines the authoritative numerical approximations required for faithful Chapter 5 reconstruction when the MATLAB code intentionally regularizes, stabilizes, or approximately solves the theoretical system.
3. A numerical device is not to be deleted merely because it is absent from the dissertation structural equations or is mathematically less elegant.
4. Clean/reference diagnostics may be retained, but they must not silently replace or veto a designated MATLAB numerical algorithm when the reconstruction goal is faithful replication.
5. Any future departure from these frozen MATLAB numerical devices requires explicit Owner authority.

Owner provenance: the Owner states that the relevant regularization/stabilization devices follow the Moll/Kaplan computational lineage used in two-asset HANK implementations and have been retained because they materially improve numerical solvability and distributional behavior. Treat this as Owner scientific/provenance authority for the reconstruction route; do not invent external bibliographic claims not present in repository/source evidence.

## 3. Frozen faithful numerical contracts

### 3.1 Illiquid adjustment-cost denominator floor

The designated MATLAB cost is:

```matlab
chi0.*abs(d) + chi1.*d.^2/2.*(max(a,a_bar)).^(-1)
```

Freeze the faithful interpretation:

`max(a,a_bar)` is a **numerical denominator floor** preventing division by zero / pathological evaluation at the economic lower bound `a=0`.

It is not authority to replace every occurrence of `a` in the household first-order condition by `max(a,a_bar)`.

### 3.2 Bare-a transfer FOC must be restored

The designated MATLAB transfer FOC is:

```matlab
(min(pa./pb - 1 + chi0,0) + max(pa./pb - 1 - chi0,0)).*a/chi1
```

Freeze:

`MATLAB_FAITHFUL_TRANSFER_FOC_USES_BARE_A`

Consequences:

- the production faithful Python implementation must use the raw illiquid asset level `a` in this FOC;
- at `a=0`, this numerical contract implies the corresponding direct transfer candidate collapses to zero;
- the previously accepted O1 helper that substitutes `max(a,a_bar)` into the FOC is retained only as corrected-equation diagnostic evidence, not final faithful production authority;
- do not delete prior evidence, but reclassify it.

### 3.3 Illiquid-return upper-grid taper must be restored

Freeze the designated MATLAB numerical stabilization:

```matlab
raah = rah.*(1 - 0.1*(ahmax./ah).^(-9));
```

Equivalent algebraic form is allowed only if numerically equivalent on the designated grid.

Freeze marker:

`MATLAB_FAITHFUL_ILLIQUID_RETURN_TAPER_IS_REQUIRED_NUMERICAL_STABILIZATION`

Interpretation:

- this taper is **not** a structural claim that the economic return process is state-dependent;
- it is nevertheless part of the faithful numerical implementation;
- its purpose is to reduce artificial upper-illiquid-grid pile-up / stabilize the stationary distribution on a finite asset grid;
- the final faithful Python reconstruction must implement it in the same role as MATLAB;
- the previous constant-`r_a` corrected-equation track remains useful reference evidence but is not sufficient final Chapter 5 parity authority.

Do not redesign the coefficient `0.1`, exponent `-9`, or the use of `ahmax/ah` in this task.

### 3.4 Asset lower bounds

Freeze the intended state-domain distinction:

- illiquid/fixed asset: economic lower bound `a >= 0`;
- liquid asset: lower bound may be negative, representing household borrowing.

Do not impose `b >= 0` merely for symmetry with `a`.

### 3.5 MATLAB stationary KFE contaminated-row solve must be restored

Freeze the designated MATLAB stationary-distribution solve:

```matlab
A = BB + AAH + Bswitch;
M = I*J*Nz;
AT = A';
vec = zeros(M,1);
iFix = floor(0.37*M);
vec(iFix) = 0.007;
AT(iFix,:) = [zeros(1,iFix-1),1,zeros(1,M-iFix)];
g_stacked = AT\vec;
g_sum = g_stacked'*ones(M,1)*db*dah;
g_stacked = g_stacked./g_sum;
```

Freeze marker:

`MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_SOLVE_IS_REQUIRED`

Interpretation:

- the singularity of the stationary operator is expected;
- the contaminated/pinned row is part of the designated numerical method used to obtain the stationary density;
- final faithful Python must reproduce the row choice rule `floor(0.37*M)`, RHS value `0.007`, linear solve, and `db*dah` normalization unless later MATLAB source inspection proves an exact context-specific variation;
- recurrent-class, nullity, unmodified-residual, pin-sensitivity, or other modern diagnostics may remain as **diagnostic checks only**;
- they must not replace the faithful contaminated-row production solve or automatically invalidate it merely because the algorithm uses row contamination.

Do not redesign the pinned row or RHS in this task.

## 4. Reclassification of existing evidence

Do not revoke or delete prior accepted evidence.

Reclassify:

- accepted P1-P4 corrected/common-equation parity;
- Owner-accepted P5 marker;
- D1 432/432 corrected-equation parity;
- all post-P5 D2 harness/comparator evidence generated under corrected/common-equation assumptions;

as:

`CORRECTED_EQUATION_RECONSTRUCTION_TRACK_ACCEPTED_REFERENCE_EVIDENCE`

They remain scientifically useful for diagnostics and regression, but they are **not sufficient final acceptance evidence for the MATLAB-faithful Chapter 5 reconstruction**.

The prior P5 marker remains historically accepted, but its scope is now explicitly:

`P5_ACCEPTED_FOR_CORRECTED_EQUATION_TRACK_NOT_FINAL_MATLAB_FAITHFUL_PARITY`

No dynamics may begin from the faithful route until new faithful HJB/KFE/steady-state parity gates pass.

## 5. Current task scope — static faithful gap audit only

After fresh-fetching live main and reading all required rules, perform a static audit comparing the current production Python implementation against the designated MATLAB implementation for the newly frozen faithful numerical contracts.

Designated MATLAB root:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

At minimum inspect:

- `HANK_2ASSETS_HJB.m`
- `HANK3_FOC.m`
- `HANK3_cost.m`
- `lab_solve2.m`
- any directly called helper required to locate the stationary KFE solve or `raah` construction

Known designated hashes to verify when present:

- `HANK_2ASSETS_HJB.m` `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_FOC.m` `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`
- `HANK3_cost.m` `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `lab_solve2.m` `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`

Inspect current Python production modules under `src/ch5_two_asset_hank/` that implement:

- adjustment cost;
- transfer candidate / FOC;
- illiquid drift/return;
- HJB policy construction;
- operator/generator;
- stationary KFE solve / steady-state distribution;
- boundary handling relevant to `a=0` and negative `b`.

Also inspect existing tests that would conflict with or need reclassification under the faithful route.

## 6. Required gap matrix

Produce a precise matrix with at least these rows:

1. cost denominator floor;
2. transfer FOC scaling at `a<a_bar` and `a=0`;
3. illiquid-return taper definition and where it enters drift/operator;
4. liquid/illiquid lower-bound handling;
5. stationary KFE linear-system construction;
6. contaminated-row index rule;
7. contaminated-row RHS value;
8. stationary normalization measure (`db*dah`, productivity weights if applicable in source context);
9. current Python clean/reference diagnostics that should remain diagnostic-only;
10. existing tests/fixtures whose expected behavior encodes corrected-equation rather than faithful-MATLAB assumptions.

For every row report:

- MATLAB exact source expression/location;
- current Python expression/location;
- classification: `ALIGNED`, `FAITHFUL_GAP`, `DIAGNOSTIC_ONLY_DIFFERENCE`, or `OWNER_CLARIFICATION_REQUIRED`;
- whether production source mutation will be required;
- whether tests must be updated, split, or retained as corrected-track regression tests.

Do not modify production code in this task.

## 7. Required implementation route proposal

At the end of the audit, propose the smallest implementation sequence, expected to be approximately:

1. faithful household numerical primitives: bare-`a` FOC + denominator floor contract;
2. faithful `raah` taper and its integration into illiquid drift/generator;
3. faithful HJB/policy regression against designated MATLAB states;
4. faithful KFE contaminated-row solver;
5. faithful steady-state distribution/aggregate comparison;
6. only after those pass, dynamics/IRF.

But do not force this sequence if static source inspection reveals a dependency that requires another order. Report exact dependencies.

The report must distinguish:

- production faithful implementation;
- clean/reference implementation/diagnostics;
- corrected-equation historical regression evidence.

## 8. Explicit prohibitions

Do not:

- resume the wrapper-aware D2 comparator chain;
- modify Python production source/tests in this task;
- modify MATLAB source;
- delete or rewrite historical reports;
- rerun D1/D2/D3;
- rerun HJB/KFE/steady state;
- run asset-tail diagnostics;
- enter AR(1), transition, IRF, dynamics, calibration extension, or Results;
- reinterpret the Owner-frozen numerical devices as mistakes to be removed;
- silently replace MATLAB algorithms with mathematically cleaner alternatives;
- invent external Moll/Kaplan bibliographic evidence not present in repository/source materials.

If exact MATLAB intent/source is ambiguous beyond the Owner decisions frozen here, use:

`OWNER_PROVENANCE_REQUIRED`

and stop that sub-issue rather than guessing.

## 9. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_OWNER_MATLAB_FAITHFUL_NUMERICAL_APPROXIMATION_AUTHORITY_RESET_AND_GAP_AUDIT_REPORT.md`

The report must include:

1. terminal classification;
2. live start/final `origin/main`;
3. repository/source identities and hashes;
4. exact Owner authority markers frozen by this task;
5. explicit reclassification of P1-P5/D1/D2 corrected-track evidence;
6. complete MATLAB-faithful gap matrix;
7. exact Python modules/functions/tests affected by each faithful gap;
8. items already aligned and not to be changed;
9. diagnostic-only tools that should remain but not override faithful algorithms;
10. any `OWNER_CLARIFICATION_REQUIRED` items;
11. proposed ordered implementation task chain;
12. statement that no production scientific code/test mutation occurred;
13. git status;
14. acceptance level;
15. exact recommended next implementation gate.

## 10. Terminal classifications

Use exactly one:

### Audit complete

`MATLAB_FAITHFUL_NUMERICAL_APPROXIMATION_AUTHORITY_RESET_AND_GAP_AUDIT_PASS`

Use if all frozen Owner contracts can be mapped to exact MATLAB and current Python locations sufficiently to issue bounded implementation tasks.

### Audit blocked

`MATLAB_FAITHFUL_NUMERICAL_APPROXIMATION_AUTHORITY_RESET_AND_GAP_AUDIT_BLOCKED`

Use only if a designated source/hash is unavailable or a required exact numerical contract cannot be resolved without new Owner provenance.
