# Observed labor / composite wage readiness

2026-10-01；DOCUMENT-ONLY CANDIDATE，待Work独立review。原数据/工程额度均remaining0，本文件不授权执行。

## 接受层次与生命周期

已接受：immutable annual carrier/common-spy seam；sealed immutable array/literal31 mapping；fixture-only frozen capital/C1/firm中间桥接；实际data-only认证、年度转换与捕获矩阵证据。依据分别为TASK点名的dual consumer、array、middle engineering reviews及independent_actual_data_review.md。原labor/C1/firm/wage和household/fullouter在新observed路线仍NOT_EXECUTED，不否认历史其他路线的科学执行。

实际子进程已退出。CSV/hash是证据，不保留sealed AnnualContext/array或same-object identity；禁止CSV重包装seal、伪造token、改标synthetic。未来须另有精确bindings、新authority/budget，在同一进程合法prepare一个context/master并交给两真实边界。原production blocks保持，不能私调kernel绕过。

固定target2018/obs2017；retrospective_revised/year_end_resident/current_price_methodologically_attributed；price_verifiedFalse、releaseUNKNOWN、baseyearNone、model_activationFalse、ResultsFALSE。GDP亿元、人口万人；q=10000*GDP/population是年末人口proxy，非官方人均GDP；phi[j,i]=1+0.3*(q_i-q_j)/(q_i+q_j)，destination行/origin列，amplitude不变。不normalize/transpose/clip/round/recalibrate。

canonical31全名/短名映射严格引用array specification §§Immutable arrays and provincial state mapping，原样存于本轮receipt的canonical_province_mapping。index1-based；state.name及PROVINCE_ORDER保留短名，统计全名只作provenance；old_provinces是ordered records tuple，不改为name-keyed mapping。消费/population/tax/wealth按origin；旧工资、private capital、labor totals按destination；composite wage回origin。migration distance wedge不同于annual phi。

## 文档已建立的合同与UNKNOWN

下表来自指定accepted文档；提案签名不冒充当前完整production API。

| 接口 | 已建立内容 | 未建立门 |
|---|---|---|
| Historical integrate_turn | (repository,task_root,turn_root,turn,states,batch,frozen_shares,expected_share_sha,ledger,household_rows)->dict[str,Any]；middle spec §Established static contract | 新observed入口完整签名、source namespace/ledger init UNKNOWN |
| Annual context/array | 元数据、axis/source、authoritative tuple、owner-bound seal；immutable-bytes-backed float64 C-order master；same-context/master | array spec提案prepare_annual_array(context,*,target_year,province_axis,source_sha256,input_kind,price_basis,price_verified)没有完整绑定最终province_mapping等参数；当前public prepare/validate/formal fields schema UNKNOWN，不能由成功CLI补推 |
| Labor | MigrationLaborInputs(consumption_by_origin=batch.ct,population_by_origin=N,old_firm_wage_by_destination=wjt,tax_by_origin=tau,phi_destination_origin=master,migration_wedge_destination_origin=wedge,gamma_c=params['ga'],phi_l=params['phi_l'])，随后reconstruct_migration_labor | 原函数完整签名、内部原labor公式/import closure UNKNOWN；不得补推或改式 |
| Frozen capital | wealth=batch.at*population；flows=shares*wealth[None,:]；private=sum(flows,axis=1)；domestic=diag(flows).copy()；固定shares、feedback alias同一次分配 | 已建立CONSERVATION_TOLERANCE=1e-12；Work新增允许的field-hash supplement明确little-endian float64/F-order/uppercase SHA256/no shape tag，shape/axis/type/finite另验 |
| C1 | residual_government_asset_levels(*,Ktarget_MU:object,Kprivate_current_MU:object,province_order:Sequence[str])->ResidualGovernmentAssetBatch；GovInv=max(Kt0-private,0)，capital_unit=MU_10WAN_YUAN | batch先cast再scalar验证，raw boolean拒绝不能声称已建立 |
| Firm | evaluate_firm(province:Mapping[str,float],kt_supply:float,lt_supply:float,params:Mapping[str,float])->FirmResult；supply为private[index]/migration.lt_supply[index]；只override GovInv/AtTax/Lt_prev | 其余完整units和dependency side effects UNKNOWN；canonical31 compatibility NOT_EXECUTED |
| Wage | composite_household_wages(provinces,[firm.wjt],master,wedge,phi_l=params['phi_l'],alphal=params['alphal'])，origin-ordered | 原完整signature/内部wage公式/source namespace UNKNOWN；不凭调用推式，也不以wt0替代wjt |

C1 fields：province_order,Ktarget_MU,Kprivate_current_MU,GovInv_residual_MU,firm_K_accounting_MU,firm_K_over_target,private_at_or_above_target,residual_floor_binding,capital_gap_before_MU,capital_gap_after_MU,status,capital_unit。
Firm source keys：GovInv,alpha,Zt,pit,Kt_prev,Lt_prev,Zt_1,pit_1,rk,corptau,AtTax,tau,Tt,ramin,ramax,wjtmin,wjtmax；params epsilon/theta/delta。Result fields：Kt,Lt,Yt,mt,KNratio,wt0,wjt,rk,Thetat,It,PIt,Corptax,ra0,ra,Govinc。出处source_contracts §C1/firm，middle spec §Established contract。

## 保留顺序、检查和最小slice

合法annual preparation/input binding后：labor→frozen capital→C1→逐destination firm→wage，两消费边界必须收到同一master。原constructor内部copy不等于共享master。

保留shares入口/run两次身份复核、column sums1、flows列守恒wealth、national private residual及domestic=(1-theta)*wealth原checks；财富不是at+bt，按CONSERVATION_TOLERANCE=1e-12，列守恒rtol0/atol tolerance、origin/national checks tolerance*max(1,sum(wealth))、home retained exact；frozen hash用已建立F-order规则，不混同annual C-order，不造新数值。C1非负/精确max/count1；firm.Kt按已记录1e-12*max(1,abs(expected))对accounting核对，as_source_dict全部finite后才放行wage。原labor/wage内部公式在本轮允许文档未写出：UNKNOWN，下一只读任务定位原式而非设计替代。

attempt在进入阶段前计；nested factory失败保留labor attempt；allocation与K1B alias是一个阶段两标签；失败抑制下游，不重置ledger。source_contracts带历史READ_SCOPE_DEVIATION/NONCOMPLIANT，只采用Work接受的C1/firm/tolerance/ledger事实，排除其超范围capital_network算法/Option-B函数头。

最小保持时序的未来slice使用预先验证的household batch/state/params/distance/frozen shares，经过完整labor→capital/C1/firm→wage依赖链，不新增household solve。封存input exact locator/year/stage/hash/units尚UNKNOWN，本轮不读值。借旧firm wage跳过firm的同阶段合法性未建立；不作为等价捷径。原consumer/fullouter运行仍无授权。

C9PAUSED、ObjectiveARETAINED/windowUNACCEPTED、oldattemptsCONSUMED/historicalCALL_LEDGER_UNRESOLVED、price_verifiedFalse/model_activationFalse/ResultsFALSE、historicalNONCOMPLIANT保持。下一门见next_boundary_packet.md。
本轮Work补充只读授权work_field_hash_binding.md，继承已关闭hash门；source_contracts早期UNREAD描述属于被该supplement解决的历史状态，不再建议重复读取leaf。CONSERVATION_TOLERANCE=1e-12来自source_contracts §Frozen capital tolerance。
