# Fixed C8 conditional middle-stage design
2026-10-01；record14；DESIGN_ONLY／DEFAULT_BLOCKED，待Work独立review。

Owner仅采纳固定C8条件对照：固定完成C7进入C8的states、原C8家庭输出及同一进入C8 shares；仅前瞻替换labor/wage年度系数为target2018/obs2017。原N/params/distance保持，不用修订人口改旧state。精确pins、JSONpointers、类型与31简称顺序只列input_binding_spec.json。四baseline hash匹配不代表typed inputs齐备：household receipt只有求解receipt，无batch四向量；params、distance、NPZ member、完整canonical全称metadata、来源单位/明确历法仍UNKNOWN。C7 state Ct/At/AtTax/Lt不能冒充C8 batch。

## 前瞻边界与时序（当前不调用）
未来合法in-process observed auth→kernel/helper→prepare_annual_array(context,*,target_year,province_axis,source_sha256,input_kind,price_basis,price_verified,province_mapping)，先完成新authority/budget及保护审查。退出child没有live context/seal/master，CSV不可重封或改标synthetic；历史actual1consumed/rem0不复活。retain validated bytes/provenance，原标量/向量防御复制；nested records/params/distance/batch的浅复制或alias需要独立保护证明。

| 阶段 | 未来精确forwarding及计数提案 |
|---|---|
| labor | MigrationLaborInputs(consumption_by_origin=batch.ct,population_by_origin=N,old_firm_wage_by_destination=wjt,tax_by_origin=tau,phi_destination_origin=master,migration_wedge_destination_origin=distance,gamma_c=params['ga'],phi_l=params['phi_l'])→reconstruct_migration_labor；进入factory前attempt1，factory失败不冒充reconstruction已进入 |
| frozen capital | 固定原S，wealth=batch.at*N，原allocation/feedback同一次分配两标签，各attempt1；不重算shares/同turn payoff。原F-order字段hash及守恒、home checks保持 |
| C1 | residual_government_asset_levels(*,Ktarget_MU=old.Kt0,Kprivate_current_MU=private,province_order=order)；attempt1，GovInv=max(target-private,0)，MU_10WAN_YUAN，无新增控制律 |
| 31 firms | evaluate_firm(source,private[k],migration.lt_supply[k],params)；source仅override GovInv/AtTax/Lt_prev，wjt结果送wage；逐省先计attempt，最多31 |
| wage | composite_household_wages(provinces,[firm.wjt],同一master,distance,phi_l=params['phi_l'],alphal=params['alphal'])；attempt1 |

所有ceilings只是提案，当前各项live预算0。共享master成立在两个输入边界；原MigrationLaborInputs/原OneTurnInputs可内部copy，wage np.asarray也不证明内部身份。保持labor origin tax与wage destination tax的不同原式，不重写或测试模型公式；年度master immutable float64/C-order与S的little-endian float64/F-order/uppercaseSHA不同，S无shape/axis/dtype tag仍独立验。CONSERVATION_TOLERANCE=1e-12及既有C1/firm accounting checks、lagged raw return timing保持；完整单位/旧input明确calendar未提供即fail closed。

每阶段先记attempt，失败保留，阻所有下游；allocation与feedback不重复分配。旧CALL_LEDGER_UNRESOLVED不被新账本覆盖；future preparation attempts独立命名，不能复用actual1或fixtureprocess1。原source输出/完成次数未知不能填0。

## 接入与缺口
既有integration.integrate_turn的显式annual/array/mapping/middle接口及prepared-middle只允许synthetic；67–68 observed阻断保持。31-spy PASS仅工程编排，不安装真实callee。当前没有授权entry/candidatefile、launcher或输出root；candidatefile allowlist为空，默认不造额外bridge。若未来精确observed接入确有缺口，先提出最小diff和独立review，不能沿私有kernel绕过blocks。

依赖来自已接受合同：context/helper/array、integration/middle，以及原migration_labor/wage、frozen allocation/C1/firm；原one_turn还导入capital_allocation/monetary/fiscal等，当前slice不运行其fullouter。真实callee namespace/pins、package initializer、transitive imports及optional as_source_dict的副作用证明未闭合；本轮不读source、不import。

下一安全门：Work独立审三份设计文档与最终回执，再绑定缺失C8 aggregate/params/distance/member/full-name metadata/units-stage的精确locator与authority，以及ObjectiveA未解分类；不重新问已决价格或基线。真正准备/consumer执行仍需独立final-chain/protection review与新的明确Owner scoped grant。不是新均衡/fullouter/GE/Results。C9PAUSED、ObjectiveARETAINED/windowUNACCEPTED、priceFalse/releaseUNKNOWN/baseyearNone/modelFalse/ResultsFALSE保持。
