# CH5 TEMP31｜多省劳动聚合数学审查与后续纠错登记｜2026-10-23

STATUS: NON_OPERATIVE_RESEARCH_CORRECTION_REGISTER__OWNER_E3_PENDING
AUTHORITY: Owner 2026-10-23 requested a durable correction register; this document records research findings, not executable permission.
FORMAL_V010: UNCHANGED
V011: NOT_STARTED
Results: FALSE
MODEL_ACTIVATION: FALSE
HA_HJB_KFE_OUTER_GE_IRF_NEW_BUDGET: 0
GITHUB_SCOPE: ONE_OWNER_REQUESTED_DOC_ONLY_MILESTONE; NO AUTOMATIC_GITHUB_WORKFLOW_REACTIVATION

## 1. Fixed evidence and provenance

- Original dissertation TeX ZIP (local Owner Project Source): 博士论文tex.zip, 284056 bytes, SHA256 c0505aff92a87d2b7ca5670213cd4f3b48298d1bded4fa287960abadde8e7661.
- MATLAB source ZIP (local Owner Project Source): 多省份HANK_matlab原版程序.zip, 1578316 bytes, SHA256 ceb94ccf34d2d218722b81e5111a8f4c530571a9f886bd4afe0610a00321f755.
- c3.tex in ZIP equals previously supplied c3.tex; chapter 3, section 3.2.3, approximate source lines 330–404.
- Source files: HANK_2ASSETS_HJB.m, Lt_seperate.m, wage_caculate.m, HANK_mp_1turn.m, HANK_firm.m, HANK_mp_1eq.m.
- c5.tex and files with c5_* prefixes have histories of prior Codex edits/backup. Do not silently treat any c5 variant as sole current authoring authority; determine authoritative TeX version before future edits.
- Previous owner-selected TEMP31 A1 research route remains in force. R/P mechanisms, consumption relocation, new labor normalization and formal corrections are not adopted or activated.

## 2. Original mathematical contract

For origin i, destination j, inverse Frisch parameter phi>0, aggregate labor disutility parameter varphi>0, positive destination disutility weights beta_ji>0 and effective wage q_ji>0:

q_ji = w_j^gross (1 - tau_j - sigma_ji)  [this is the intended destination-tax convention; legacy implementations differ].

u(c,{l_ji}) = c^(1-gamma)/(1-gamma) - sum_j beta_ji l_ji^(1+phi)/(1+phi).

Individual FOC: beta_ji l_ji^phi = V_b z q_ji.

Scalar labor index L satisfies varphi L^(1+phi) = sum_j beta_ji l_ji^(1+phi).
The scalar net wage W is defined by W z L = sum_j q_ji z l_ji.

Let a_j=(q_ji/beta_ji)^(1/phi), S=sum_j a_j, Q=sum_j q_ji a_j. Then
l_ji=(V_b z)^(1/phi) a_j,
L=(V_b z)^(1/phi)(Q/varphi)^(1/(1+phi)),
W=varphi^(1/(1+phi)) Q^(phi/(1+phi)).

At given household-independent q and beta, l_ji/L=(varphi*q_ji/(beta_ji*W))^(1/phi).
Aggregating with g_i: firm-facing destination effective labor L_ji=H_i L_i^HA (varphi*q_ji/(beta_ji*W_i))^(1/phi), provided the HA labor policy and W_i use exactly the same FOC/units. Net source payroll identity: sum_j q_ji L_ji = W_i H_i L_i^HA. The A1 E_i=p_i H_i interface remains an unresolved independent economic decision; do not insert p_i twice.

CRITICAL: L is a nonlinear index, not necessarily the arithmetic sum of destination physical labor hours or effective labor quantities.

## 3. NEW MATH RESULT: arithmetic labor balancing

Want simultaneously (a) original individual FOCs, (b) unchanged separable destination disutility, (c) scalar disutility equivalence, (d) L=sum_j l_ji.
Write shares s_j=l_ji/sum_k l_ki. Necessary and sufficient at a given positive wage vector:
varphi = sum_j beta_ji s_j^(1+phi).

For baseline beta_ji^0>0 let s_j^0 proportional to (q_ji/beta_ji^0)^(1/phi). Multiplying every destination beta_ji^0 by a COMMON k_i preserves relative shares at that given wage vector, while scaling their levels:
k_i = varphi / sum_j beta_ji^0 (s_j^0)^(1+phi).
Then beta_ji=k_i beta_ji^0 achieves arithmetic equality at that wage vector AND satisfies FOCs and the scalar wage-income identity. This is an algebraic existence result, not an approved model parameterization.

Example phi=1, varphi=1, q=(3,4), beta^0=(1,1), V_b z=1: initial destination l=(3,4), L_index=5, arithmetic sum=7; k=49/25=1.96 gives l=(75/49,100/49), L_index=sum=25/7. If q changes to (3,5) with k fixed, the equality fails (effective index coefficient 1.04125 rather than 1).

For 31 symmetric destinations and phi=5 with varphi=1, beta_j^0=1, k=31^5=28629151. This massively changes the level of labor aversion relative to the legacy bounded-around-1 scheme; unsuitable as a harmless patch.

NO-GO for a universal FIXED positive beta_j, fixed varphi, phi>0, >=2 independently responsive destinations: equality would require varphi(sum_j l_j)^(1+phi)=sum_j beta_j l_j^(1+phi) for all positive l, but the left side has positive cross terms and right side is separable. A calibration at one steady state remains exact only for wage movements preserving relative optimal destination shares (including common proportional wage shifts). Recalculating k_i after every shock implicitly makes preferences wage/policy dependent and compromises structural welfare interpretation.

## 4. Proportional ex-post scaling is NOT a free repair

Given original l_j and nonlinear L, multiplying all destination l_j by lambda=L/sum_j l_j enforces sum_j l_j_new=L. But:
- firm/source payroll changes to lambda times original payroll; to keep scalar earnings identity at fixed L requires W_new=lambda W;
- separable labor disutility changes by lambda^(1+phi), while scalar varphi L^(1+phi) is unchanged;
- original destination FOCs generally cease to hold; changing W or varphi in the HA budget/utility changes the optimal L itself.
Example q=(3,4), beta=(1,1), phi=1: l=(3,4), L=5, lambda=5/7. Original payroll=25; post-scale payroll=125/7, inconsistent with unmodified W L=25.
Verdict: do NOT implement an end-of-pipeline equal-ratio labor patch without jointly redefining the economic model and rederiving its optimality and resource constraints.

## 5. Corrective registry (not yet implemented)

| ID | Severity | Evidence and location | Action gate |
|---|---|---|---|
| CH5-LAB-01 | MATHEMATICAL CONFIRMED | c3.tex approx. lines 395–401; wage_caculate.m line 11: general varphi exponent old -phi/(1+phi), consistent +1/(1+phi). Both equal if varphi=1. | Future Author/Owner approval before code/TeX change. Retain varphi=1 in current frozen work. |
| CH5-LAB-02 | MATH/DESIGN PENDING E3 | Nonlinear L index vs arithmetic sum_j l_j; baseline-only normalization possible, dynamic exact balancing with fixed preference weights generally impossible. | Prefer to retain nonlinear index, account for physical destination labor separately; Owner decide. |
| CH5-LAB-03 | LEGACY STATIC DIRECTION CONTRADICTION | HANK_mp_1turn.m line 10 has plus (destination Y/L minus source Y/L). Owner intended higher destination GDPpc to REDUCE disutility. c5.tex around line 253 also has plus (source/destination indices must be fixed carefully). Legacy Y/L is not necessarily GDP/H. | After source/version review, set beta_ji=1+kappa*(GDPpc_i-GDPpc_j)/(GDPpc_i+GDPpc_j) and protect positive range; do not edit V010 blindly. |
| CH5-LAB-04 | LEGACY TAX INTERFACE RISK | Lt_seperate.m line 7 uses source results{i}.tau, wage_caculate.m line 8 uses destination results{j}.tau, while HANK_2ASSETS_HJB.m lines 127–130 apply (1-tau)*w to aggregate wage. | Audit single tax wedge end-to-end, keep destination income tax separate from migration resource wedge. No immediate repair without Owner E3. |
| CH5-LAB-05 | LEGACY GOVERNMENT ACCOUNTING SUSPECTED | HANK_firm.m line 95: Govinc = Corptax + Lt*results.tau + AtTax + GovInv*ra - Tt; wage factor wjt appears absent if tau is ad valorem wage tax. | Check full tax units, wage caps/subsidies and government boundaries; do not conclude Python V010 shares this issue. |
| CH5-LAB-06 | SCIENTIFIC BRIDGE PENDING | Lt_seperate.m derives destination labor from average Ct; HA actual L=sum z*l*g; they need not coincide because of nonlinear averaging. | Continue source-only algebra/consistency checks using HA L and same dual W. |
| CH5-LAB-07 | A1/UNITS E3 PENDING | E=pH vs household H and z-mixture; risk of double-scaling when HA already embeds labor-state heterogeneity. | Owner decision; no real data/HA admission. |
| CH5-LAB-08 | NO CHANGE | GDP target anchoring via Z and independent reporting of HA–firm consistency, convergence and GDP matching. | Preserve GDP anchor; no solver execution or calibration permitted by this register. |
| CH5-LAB-09 | OPTIONAL FUTURE | Consumption place allocation by labor shares is a candidate only, not proof of shopper location, origin budgets or destination goods market clearing. | No adoption without separate economic/accounting analysis. |

## 6. Next scientific decision and research governance

Recommended discussion order: (1) owner position on nonlinear composite labor index vs arithmetic physical labor; (2) consistent destination wage/tax and accounting bridges; (3) source/final TeX authority and bounded formula repair; (4) GDP calibration separately. Do not change phi, beta, tax scheme, household FOC or formal V010 merely to force a convergence or balancing diagnostic PASS.

The user request authorizes creation of this ONE document as a milestone correction register. It does not reactivate GitHub automatic issue/review/cleanup, authorize future code edits, or create an ACTIVE research task. Three historical PENDING Review records and Windows Dirty files are untouched.
