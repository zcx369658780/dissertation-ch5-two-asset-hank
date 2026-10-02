# Annual K1B leaf contracts — static read-only candidate

2026-09-30 Asia/Shanghai. DOCUMENT_CANDIDATE_PENDING_WORK_REVIEW_WITH_READ_SCOPE_DEVIATION.
Only D:\ProjectTemp\c5k1bturn56. Task SHA-256 04028A233B8AC89519B791FF9B4450B021E6259C9FE49DD7B23D32350BFD6A10. HEAD75cee92b1ad9e5cb6fc069bca892213838ffdddc; HEAD:src00682b2e1a7ba23665f6e16f6acf48ad35874883. Work records27completed, active28; no recount. Prior premature Work handoff is withdrawn under Owner's continuation; historical evidence is preserved. This document grants no execution or source-change permission.

## Finding and bounded source identities

C1 formal inputs/result/units, firm consumed state/params/result and the capital conservation tolerance are now statically established. Exact field-hash bytes/dtype/order/shape semantics are STILL UNREAD_NOT_AUTHORIZED: nonlinear_continuation re-exports _field_sha256 from option_a_step rather than defining it. Therefore the complete source-bound bridge contract is NOT FULLY READY. Minimum next closure is a separately authorized read of that literal leaf definition; no imports were followed here. Work must additionally disposition the scope deviation below before treating this intake as fully compliant.

| Allowed read source under src/ch5_two_asset_hank/ | Raw SHA-256 | Bounded evidence |
|---|---|---|
| corrected_diagnostic/optionb_turn2_household_integration.py | E2D5EDBBF73ABF60DBA183FB04A5D364D3D83FFCD262254F58EAD53EC2F36D07 | import bindings27–69; _new_ledger356–396; _check_ledger399–443; _one_turn_inputs857–873; integration relevant counter callsites944–988 |
| corrected_diagnostic/nonlinear_continuation.py | E43B3990370F39B82486E05C4F286CA2719FBFA304333CB7999C5180C3875701 | _field_sha256 import24–33; FailClosed86–90 only |
| multi_province/government_assets.py | D64AB4DBCFB5D682ED2553A4EAD76930A756EBF11E606B6CBD4B94CB5986B705 | residual result27–58, immediate scalar validation/residual, batch115–152 |
| multi_province/firm.py | D4C3DADA5577F25E0159831DCC9DE3883EA656E80AA3E1C407E6BB0AF0D4CA0D | FirmResult21–41; evaluate_firm44–134 |
| multi_province/capital_network.py | FB193687A07770FF6F10301AB453734753E4BFFE9E00D9D58D444CF4C206FEC5 | CONSERVATION_TOLERANCE21; no next-share algorithm facts adopted |

45 protected plus5 read-source identities matched before reading. Repaired middle-callsite spec1C4E4B5A1485A0A71A1E26DA1EC50E232F0E6E6A42AE2D7B8BD6462937E8A223 and receiptC2A5621F2606BBDF1F1DA1808D62AE885B03830ECFA3F22BCF9DF0F11576A3F0 remain prior accepted authority; original overbroad timing candidate remains REJECT.

## Wrapper namespace, annual input replacement and hash gap

Option-B source is the original multi_province.one_turn module, with OneTurnInputs and PreFrozenHouseholdOutputBatch imported from it; residual_government_asset_levels is imported directly from multi_province.government_assets. C1_UPDATE_ORDER is separately imported from multi_province.c1_residual_public_asset; its body remains unread, no inference or activation.

_one_turn_inputs(repository:Path,states:tuple[dict[str,Any],...],batch:PreFrozenHouseholdOutputBatch)->OneTurnInputs computes old endogenous productivity from states Yt/Lt, creates its old directional phi, loads accepted distance then sets migration wedges=0.5*distance. It returns OneTurnInputs(PROVINCE_ORDER,states,params,phi,wedges,batch). Visible fixed params are ga2.0,phi_l5.0,alphal1.0,epsilon10.0,theta100.0,delta0.025,istar0.015,rho_pi1.25,totalpit0.02,epsilon_pi0.0. These are source constants, not actual source-data readback or a calibration proposal. The annual bridge must bypass old phi construction while accepting the unchanged explicitly bound distance/wedge/params; do not silently recalculate distance from an unread loader, transpose or assert the old/new phi are numerically equivalent.

Hash binding chain: Option-B imports _field_sha256 from nonlinear_continuation, which imports it from .option_a_step. There is no local definition in either allowed file. We establish the reference chain and share-check callsite only; byte order, dtype conversion, inclusion of shape and serialization remain UNKNOWN. Literal missing module: ch5_two_asset_hank.corrected_diagnostic.option_a_step, symbol _field_sha256. Proposed locator src/ch5_two_asset_hank/corrected_diagnostic/option_a_step.py is import-derived and NOT_READ; Work must explicitly bind its exact bytes/location and authorize that definition alone. Do not substitute a guessed NumPy.tobytes hash or fixture digest for the original production identity.

FailClosed(terminal:str,detail:dict[str,Any]|None=None) is a RuntimeError storing terminal and detail or an empty dict. Static exception shape is established; no exception/solver runtime was executed.

## Original ledger meanings and timing

Option-B _new_ledger initializes its counters to zero. _check_ledger imposes ceilings, rejecting actual>ceiling; it does not prove minimum counts, successful completion or authority. Integration relevant ceilings: source_faithful_labor_reconstructions1, k1a_capital_network_allocations1, c1_residual_govinv_constructions1, firm_evaluations31, composite_wage_batches1. turn3_household_calls, third_outer_turns, k1b_feedback_calls, k2_calls, adaptive_controller_calls and matlab_scientific_calls have zero ceilings in THIS Option-B checker. Other solver ceilings are outside the proposed slice and never become a new budget.

The historical selected K1B integrate_turn has frozen_k1b_quantity_allocations and k1b_feedback_calls increments for its frozen-allocation alias. Therefore do NOT wire Option-B _check_ledger unchanged into a K1B bridge and claim compatibility: its K1B zero ceiling conflicts with that historical caller. Preserve actual runner-defined keys/budgets; do not initialize a new ledger to erase existing attempts or generalize Option-B caps to K1B. Wrapper checker runs at explicit driver checkpoints, not automatically at every inner stage.

Pre-call/pre-stage counts established for labor, frozen-capital allocation/K1B alias, C1 and each firm in the selected historical middle stage remain as recorded in the repaired prior spec. completed_raw_ra0_vectors increments after vector creation; raw_next_payoff_same_s_constructions after ordered_payoff. Other downstream historical timing remains unchanged; no universal pre-call rewrite. Failed attempted calls retain their consumed increments. A synthetic bridge ledger verifies its own wiring only; historical actual ledgers remain CALL_LEDGER_UNRESOLVED.

## C1 formal contract and accounting

residual_government_asset_levels(*,Ktarget_MU:object,Kprivate_current_MU:object,province_order:Sequence[str])->ResidualGovernmentAssetBatch. Province order must equal the original31 model short names; target/private converted to float arrays of shape(31,). Immediate scalar validation rejects bool/np.bool_, nonfinite and unrepresentable values, requires target>0 and private>=0. Important representation distinction: batch casts arrays BEFORE passing elements to the scalar validator, so do not claim scalar bool refusal proves raw batch Boolean arrays are rejected. Any bridge input-type refusal must be explicit and reviewed, not inferred from scalar validation.

Capital unit is MU_10WAN_YUAN. Scalar residual is max(target-private,0); firm accounting equals target when private<target, otherwise private with zero residual. Overshoot is preserved, not capped. No gain/smoothing/rule change. Batch fields are province_order,Ktarget_MU,Kprivate_current_MU,GovInv_residual_MU,firm_K_accounting_MU,firm_K_over_target,private_at_or_above_target,residual_floor_binding,capital_gap_before_MU,capital_gap_after_MU,status,capital_unit. Numeric/flag arrays are copied read-only. status is per-province status tuple. Owned read-only C1 outputs do not become immutable annual phi delivery authority.

Caller checks exact GovInv equality against maximum(Kt0-private,0), nonnegative and one C1 construction. Each returned firm.Kt must equal firm_K_accounting_MU within1e-12*max(1,abs(expected)). These are preserved caller predicates; no C1 or firm execution here.

## Firm formal contract

evaluate_firm(province:Mapping[str,float],kt_supply:float,lt_supply:float,params:Mapping[str,float])->FirmResult. Consumed provincial keys: GovInv,alpha,Zt,pit,Kt_prev,Lt_prev,Zt_1,pit_1,rk,corptau,AtTax,tau,Tt,ramin,ramax,wjtmin,wjtmax. Params: epsilon,theta,delta. Preserve the source dictionary and only historical caller overrides GovInv from C1, AtTax from batch.at_tax and Lt_prev from batch.household_lt. Destination private capital and migration.lt_supply are its two supply arguments.

Source validation requires finite consumed scalars and supplies; effective Kt=kt_supply+GovInv and Lt=lt_supply are positive, alpha in(0,1), Zt>0, epsilon!=0, clipping min<=max. No additional sign law on theta/delta/epsilon is invented. All final FirmResult values are checked finite. Result fields: Kt,Lt,Yt,mt,KNratio,wt0,wjt,rk,Thetat,It,PIt,Corptax,ra0,ra,Govinc; as_source_dict supplies them to historical caller. This source does not declare their full numeric units; preserve caller convention and mark unspecified units rather than invent conversion. Raw ra0 and used ra are distinct, never silently replace one with the other. Existing clips/formulas/definitions remain unchanged; this task does not execute, endorse new clipping, or test scientific compatibility.

## Frozen capital tolerance and narrow bridge proposal

CONSERVATION_TOLERANCE=1e-12 at capital_network.py21. Historical shares/flows destination-row/origin-column and exact home-retained diagonal checks remain in the accepted prior callsite specification: shares columns sum1 at rtol0/atol tolerance; wealth=batch.at*population; flows=shares*wealth[None,:]; private=row sums; origin/national capital checks use tolerance*max(1,sum(wealth)); home retained exact; frozen SHA must use ORIGINAL hash semantics once those are read. No same-turn share recomputation, altered share algorithm or fallback to generic capital allocation.

The smallest inactive dependency-injected design remains conditional on the unresolved hash definition and Work's scope disposition. Exact proposed future allowlist unchanged:
- CREATE validators/multi_province/annual_observed_labor_diagnostic/middle_stage.py
- MODIFY validators/multi_province/annual_observed_labor_diagnostic/integration.py
- CREATE tests/test_ch5_annual_k1b_middle_stage.py

Explicit prepared annual carrier/context/map enters the bridge. Preserve original model short names, 1-based canonical index and source full-name provenance; do not mix historical zero-based receipt indices. SAME immutable-bytes-backed master is passed at labor-input/wage boundaries, same-year reused once-prepared. Original OneTurnInputs/MigrationLaborInputs copies are retained and checked only for numeric agreement; neither owned-copy nor view replaces the master. Frozen capital->C1->per-province firms stays between labor and wages. No opaque spy acceptance proves actual middle implementation.

Future invented2/3-province spies can test event order, argument forwarding/overrides, frozen arithmetic/checks, master identity, name/axis/dimension refusal, ledger attempt timing, hash-hook mismatch, C1/firm output mismatch and wage suppression after first failure. Original C1 batch requires31provinces, so a small fixture C1 spy is deliberately a toy contract and cannot be called original API runtime validation. Hash fixtures do not establish actual byte semantics. Real C1/firm/labor/wage or package code remains unimported/unexecuted; actual31-province arrays/data/auth/conversion remain closed. Proposed finite test budget requires future exact Work issuance, evidence root and source backup; current budget0.

## Static read-scope deviation and authority gate

Helper observed_boundary_spec used an over-wide text slice in capital_network.py that exposed approximately241–339, including later build_bilateral_capital_network/foreign-share generation content outside the authorized subsection. Main also used a context search around _one_turn_inputs that exposed the following function header/initial cast at Option-B876–879. No source was executed/imported and no data accessed. These out-of-subsection reads are a scope deviation; their contents are excluded from substantive findings/proposal. No further reads of those sections or transitive imports are authorized or performed. Main records the deviation and leaves acceptance/disposition to Work; do not represent this intake as wholly scope-compliant.

Two helpers are disjoint and read-only: array_contract_spec owns wrapper/hash/ledger; observed_boundary_spec owns C1/firm/tolerance. Builder owns only two result documents and retains final reporting authority. Neither helper accepts its own work. Minimum next authorized action would be a separate bounded definition read for option_a_step._field_sha256 and Work review; no source implementation/scientific successor follows automatically.

Current test/formula-helper/science/model/calibration/production/auth-success/conversion/actual matrices/real numeric/probe/download/AST-process/source-edit/Git/publication/output-activation counts are0. Prior30PASS process(old16inside), previous3tests and helper24PASS stay consumed. C9PAUSED, both attempts consumed, ObjectiveARETAINED, price=current_price_methodologically_attributed/price_verifiedFalse, releaseUNKNOWN, model_activationFalse, ResultsFALSE; old actual CALL_LEDGER_UNRESOLVED unchanged. Stop for Work independent review.