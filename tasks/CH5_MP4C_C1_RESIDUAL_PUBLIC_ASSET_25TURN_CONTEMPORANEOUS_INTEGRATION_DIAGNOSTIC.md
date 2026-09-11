# Chapter 5 MP4C C1 residual public-asset contemporaneous integration and 25-turn diagnostic

Date: 2026-09-11

Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Integrate the accepted pure C1 public-asset residual definition into a separately named corrected-2018 diagnostic successor route and run exactly one bounded 25-turn trajectory.

The accepted economic interpretation is:

`GovInv` represents unobserved government/public productive assets that bridge the gap between accepted total productive-capital target and model-implied private productive capital.

Therefore the successor numerical steady-state iteration must use the level identity

`GovInv_j = max(Ktarget_j - Kprivate_j, 0)`

rather than the historical clipped-return `0.9/1.1` GovInv heuristic.

This task tests the dynamic/numerical consequences of that residual-level definition while freezing all unrelated mechanisms. It is diagnostic only, not production or Results.

## 2. Required authority

Fresh-read live `origin/main`, then read at minimum:

- `AGENTS.md`;
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- current status/handoff/roadmap;
- accepted C1 pure implementation report and Reviewer acceptance;
- accepted GovInv controller forensic/spec and acceptance;
- accepted G1 initialization probe/integration reports and acceptances;
- accepted corrected-2018 runtime-binding report/acceptance;
- accepted G0/G1 25-turn evidence;
- current `government_assets.py`, capital allocation, firm, one-turn/controller harnesses;
- protected MATLAB `HANK_mp_1eq.m`, `HANK_mp_1turn.m`, `HANK_firm.m` if locally accessible, read-only.

## 3. Frozen data/numerics

Use the accepted corrected-2018 contract only:

- actual 2018 GDP and population;
- raw-NBS GFCF Track-A PIM Ktarget;
- `delta_pim=.096`;
- `alpha=.7380939146868483`;
- MU=`10万元`, NU=`100 persons`;
- same-year `Zt0`;
- firm depreciation `.025`;
- current accepted price bounds;
- current HJB/KFE equations, grids, tolerances, solver families;
- `beta_a=1` only as `SOURCE_FAITHFUL_DIAGNOSTIC_ONLY`.

No tuning after science starts.

## 4. C1 timing contract

The outer loop is a numerical steady-state iteration, not economic calendar time. Under the accepted C1 public-asset definition, every completed household/private-capital allocation supplies the contemporaneous `Kprivate_j` used to define public productive assets for the same firm evaluation.

For the separately named C1 successor one-turn route, the order must be:

1. pre-frozen household outputs;
2. source-faithful migration/labor allocation;
3. At-only private productive-capital allocation;
4. C1 residual public-asset level replacement using current `Kprivate` and fixed `Ktarget`;
5. firm evaluation using `Kt = Kprivate + GovInv_C1`;
6. unchanged household composite wage;
7. unchanged Taylor assignment/fiscal diagnostics;
8. unchanged Zt/tKNratio outer numerical logic except the historical C0 GovInv `0.9/1.1` action is disabled in this successor route.

Do not reinterpret the C1 update as a gain controller or as an economic within-period government investment flow.

## 5. Initialization

Use the accepted G1 initialization observation contract:

- exactly one labelled initialization household observation pass;
- exactly one At-only capital allocation;
- initial GovInv from the accepted C1 residual helper;
- 31/31 accounting firm K must equal Ktarget unless private K is at/above target, in which case GovInv=0 and private overshoot remains.

No second initialization pass.

## 6. Historical C0 preservation

Do not modify or delete the historical/source-faithful clipped-return GovInv controller.

The new route must be separately named. C0 remains available for parity/history.

In the C1 successor route only:

- no `GovInv *= .9`;
- no `GovInv *= 1.1`;
- no clipped-ra GovInv action;
- no lambda/gain;
- no ra_target;
- no damping/hysteresis for GovInv.

## 7. What remains unchanged

Keep unchanged:

- source-faithful migration/labor route for this isolated capital experiment;
- accepted normalized-labor successor is NOT activated;
- wage formula;
- Zt update formula and timing, except ensure it does not overwrite C1 GovInv;
- tKNratio damping and convergence diagnostics;
- firm equations;
- capital allocation;
- household equations;
- HJB/KFE continuation rules;
- price bounds.

## 8. HJB/KFE continuation

Use accepted continuation behavior:

- finite structurally usable HJB `converged=false` continues as `HJB_NONCONVERGED_DIAGNOSTIC_ONLY`;
- false flags remain false for final convergence;
- malformed/nonfinite/unusable HJB fails closed;
- KFE validity remains independent and does not get promoted by successful continuation.

## 9. Scientific budget

Exactly one scientific process.

Initialization maximum:

- 31 HJB;
- 31 KFE;
- 31 aggregates;
- 1 At-only allocation.

Then exactly one trajectory, maximum:

- 25 outer turns;
- 775 province household updates.

No second trajectory, no second initialization, no beta cells, no scientific retry, no parameter tuning.

## 10. Required per-turn capital receipt

For every province and completed turn record:

- Ktarget;
- private K current;
- residual GovInv current;
- total firm K current;
- private K/target;
- GovInv/target;
- total K/target;
- residual floor binding;
- capital gap before replacement;
- capital gap after replacement;
- raw/used ra;
- raw/used wage;
- rah;
- At/Bt/Lt/Ct;
- HJB classification;
- KFE classification;
- Zt before/after;
- KN/Y/GDP gaps;
- source final predicate components.

## 11. Hard C1 accounting assertions

At each province-turn, after current private K is known and before firm evaluation:

- if private K < Ktarget, require total firm K = Ktarget within deterministic tolerance;
- if private K >= Ktarget, require GovInv=0 and total firm K=private K;
- require GovInv nonnegative;
- require no historical C0 GovInv action in this successor route.

Any violation is a hard implementation/scientific-stop error.

## 12. Comparison baselines

Do not rerun G0 or G1+C0.

Read accepted historical evidence and compare selected turns 1,2,3,5,10,15,20,21,22,23,24,25 against:

- accepted G0 source-faithful GovInv route;
- accepted G1 initialization + historical C0 controller route.

Compare at least:

- total K/target min/median/max;
- GovInv/target min/median/max;
- private K/target min/median/max;
- raw-ra lower/interior/upper counts;
- HJB convergence count;
- max KN gap;
- max GDP-level gap;
- Zt adjustment count;
- rah min/median/max where available.

## 13. Key questions

The report must answer directly:

1. Does contemporaneous C1 keep 31/31 firm accounting K at target whenever private K remains below target?
2. Does any province hit the residual floor because private K reaches/exceeds target?
3. Does the late-window total-K overshoot seen under C0 disappear dynamically, not only statically?
4. What happens to raw/used `ra` once capital is held at Ktarget?
5. Are `ra` boundary counts materially different from G0/G1+C0?
6. Does `rah` become more stable/interior, or remain essentially unchanged/problematic?
7. Do KN/Y/GDP gaps improve, remain oscillatory, or worsen?
8. Does Zt become the next dominant adjustment channel after GovInv is no longer free to compound?
9. Do HJB and KFE blockers remain independent?
10. Is there enough evidence to proceed next to an experiment that activates the accepted normalized bilateral labor route on top of C1, or must another capital/price issue be addressed first?

## 14. Phase-A zero-science tests

Before science, test at minimum:

1. C1 successor one-turn route is separately named;
2. source-faithful one-turn/controller routes remain byte/behavior unchanged;
3. current private K is passed into C1 before firm evaluation;
4. firm sees `Kprivate + GovInv_C1`;
5. below-target identity closes exactly;
6. at/above-target floor behavior is correct;
7. no C0 `0.9/1.1` action can execute in C1 successor route;
8. no lambda, ra_target, damping, hysteresis is present in C1 GovInv logic;
9. normalized labor is not activated;
10. prepare stage makes zero scientific calls.

## 15. Outputs

At minimum:

- separately named C1 successor one-turn/controller integration source;
- focused tests;
- `docs/CH5_MP4C_C1_RESIDUAL_PUBLIC_ASSET_25TURN_CONTEMPORANEOUS_INTEGRATION_DIAGNOSTIC_REPORT.md`;
- `reports/mp4c_c1_residual_public_asset_25turn_20260911/initialization_receipt_31province.csv`;
- `.../province_turn_capital_ledger.csv`;
- `.../national_turn_summary.csv`;
- `.../baseline_selected_turn_comparison.csv`;
- `.../anhui_trace.csv`;
- `.../hjb_convergence_path.csv`;
- `.../scientific_validity_ledger.csv`;
- `.../c1_accounting_assertion_receipt.json`;
- `.../call_ledger.json`;
- runtime/source hash receipts;
- focused/static test receipt;
- manifest/readback;
- bounded invocation receipt.

## 16. Allowed verdicts

- `C1_RESIDUAL_PUBLIC_ASSET_25TURN_PASS__CAPITAL_TARGET_HELD_AND_BOUNDED_PATH_QUANTIFIED`
- `C1_RESIDUAL_PUBLIC_ASSET_25TURN_PARTIAL__ACCOUNTING_CONTRACT_VALID_BUT_TRUE_HARD_FAILURE_BEFORE_LATE_WINDOW`
- `C1_RESIDUAL_PUBLIC_ASSET_25TURN_FAIL__CAPITAL_TARGET_HELD_BUT_OTHER_STATE_INSTABILITY_PERSISTS_OR_WORSENS`
- `C1_RESIDUAL_PUBLIC_ASSET_INTEGRATION_BLOCKED__CONTEMPORANEOUS_PRIVATE_K_TO_FIRM_ORDER_NOT_IMPLEMENTABLE_WITHOUT_BROAD_REDESIGN`

PASS only means the bounded diagnostic completed with the C1 accounting contract enforced. It is not production steady-state acceptance.

## 17. Git boundary

Use dedicated branch/worktree.

- no force push;
- no reset/clean/stash;
- preserve unrelated files;
- explicit staging only;
- commit + non-force push candidate;
- do not merge main;
- do not publish successor task;
- do not run steady-state production acceptance, GE, annual, IRF, or Results;
- `Results eligibility=FALSE`.

Return verdict, branch, candidate SHA, Phase-A tests, initialization summary, completed turns, C1 accounting assertion summary, G0/G1+C0 comparison, ra/rah behavior, KN/Y/GDP/Zt behavior, HJB/KFE validity, call ledger, and report path.
