# Exact observed-consumer source contracts
2026-10-01；record9；DOCUMENT_ONLY_CANDIDATE_PENDING_INDEPENDENT_WORK_REVIEW。

只在 D:\ProjectTemp\c5k1bturn56 读取 TASK 指定五个源文件的相关定义/header。五文件读前 hash 与既有 receipt 一致；精确 pins/ranges 见本轮 receipt。该树图谱未索引，采用 bounded textual fallback，不索引、不追 imports。静态定义不是运行、经济等价或传递导入安全证明。

## 公共年度对象与准备合同
以下签名无类型注解；默认值仅限表中 province_axis=CANONICAL_AXIS 及明确列出的 optional seam 参数。context 为 annual_observed_labor_context.py；array 为 annual_labor_array_adapter.py。

| 定义/范围 | 字面接口 |
|---|---|
| context 288–301 | authenticate_observed_binding(raw_sources, *, province_axis=CANONICAL_AXIS) |
| context 403–405 | prepare_observed_context(raw_sources, **_)：始终 ProductionBlocked |
| context 429–463 | prepare_observed_data_only_context(raw_sources, *, data_only, progress) |
| context 103–104 | AnnualContext.validate(self, *, target_year, province_axis, source_sha256, input_kind, price_basis, price_verified) |
| array 126–149 | prepare_annual_array(context, *, target_year, province_axis, source_sha256, input_kind, price_basis, price_verified, province_mapping) |
| array 81–82 | AnnualArrayCarrier.validate(self, *, annual_context, target_year, province_axis, source_sha256, input_kind, price_basis, price_verified, province_mapping) |

AnnualContext frozen 字段：target_year:int、observation_year:int、province_axis:tuple、source_sha256:str、input_kind:str、price_basis:str、price_verified:bool、provenance:tuple、wedge:object、phi_destination_origin:tuple（必填）；model_activation:bool=False；_preparation_token:object=field(default=None,repr=False,compare=False)；_seal:object=field(default=None,init=False,repr=False,compare=False)。seal 绑定 wedge 身份与完整 metadata；validate 核 exact type/token/seal、轴/hash/滞后年/价格/有限系数与方向、activation False，强制 phi is wedge.coefficients。validate 不重新认证 raw bytes。

AnnualArrayCarrier frozen 字段：annual_context:object、province_mapping:tuple、province_order:tuple、phi_destination_origin:object、backing_bytes:bytes（必填）；token/seal defaults 同上。seal 绑定 carrier/context/context seal/coefficients/master/backing 身份和年度 metadata。prepare 由原 tuple 转 C-order bytes，再 frombuffer 得到 master，不重算 phi。validate 核 context、mapping/order、float64、shape/strides/C-order/read-only、exact bytes base owner及与 tuple 逐项一致。observed 必须既定 canonical31 全称→简称映射，synthetic 必须虚构名称；不复制完整31表。

data-only 要求 data_only is True、原生 list[str] progress，拒绝既有 owned stage events；auth 要求 exact dict/固定七键/exact bytes，先核 hash 再解析。入口保留阶段事件，返回原 kernel context；私有 _preload_data_only_helper(raw_helper) 固定 hash 后建立 ModuleType。这里只读取其代码，未 preload/auth/kernel/helper。context 377–380 的 dormant 旧说明不覆盖429–459新增 data-only 调用；原403–405阻断保持。seals 是进程内身份/metadata保护，不是消费者授权或 hostile-path 全面证明。

## 原 labor、batch 与 OneTurnInputs
migration_labor.py 36–74：MigrationLaborInputs 的前六字段均 np.ndarray：consumption_by_origin、population_by_origin、old_firm_wage_by_destination、tax_by_origin、phi_destination_origin、migration_wedge_destination_origin；gamma_c:float、phi_l:float。均必填。向量/矩阵 np.array(dtype=float,copy=True) 后只读；n>=2，finite，矩阵(n,n)。gamma_c/phi_l finite positive，消费/人口positive，工资nonnegative、phi positive。

98–131：reconstruct_migration_labor(inputs: MigrationLaborInputs) -> MigrationLaborResult。字面公式（j=destination，i=origin）：
`base = wjt[j] * (1.0 - tau[i] - migration_wedge[j,i]) / phi[j,i]`
`lt_mat[j,i] = ct[i] ** (-gamma_c/phi_l) * base ** (1.0/phi_l) * N[i]`
base 与结果须 finite/nonnegative；lt_supply=np.sum(lt_mat,axis=1)。不改式、不推经济等价。MigrationLaborResult(lt_mat:np.ndarray,lt_supply:np.ndarray) 再复制，只读，并核 finite/shape/exact row sums（76–95）。

one_turn.py 59–133：PreFrozenHouseholdOutputBatch 必填 ct、household_lt、at、bt、at_tax:np.ndarray；converged:tuple[bool,...]；diagnostics:tuple[Mapping[str,object],...]。向量复制只读；ct>0、household_lt>=0、at>=0、有限且同长；converged只核boolean及长度，不要求全True；diagnostics复制为 MappingProxyType，嵌套值深不可变性未建立。
原 OneTurnInputs 必填 province_order:tuple[str,...]、old_provinces:tuple[Mapping[str,float],...]、params:Mapping[str,float]、两矩阵:np.ndarray、household_outputs:PreFrozenHouseholdOutputBatch。order 唯一非空且同长，ordered records 的 name 与位置相符；records/params浅复制代理；矩阵复制只读并核(n,n)/finite。此原 carrier 与 integration.py 的同名浅层 carrier 是不同定义，不能混同。

one_turn.py 194–258 的原组合调用依赖：labor 用 batch.ct、N/wjt/tau、ga/phi_l；capital 用 batch.at、N/inter_prv_ratio/ra；firm 用原省记录、batch.at_tax/household_lt、供给和 params；wage 用省记录、firm.wjt、两矩阵、phi_l/alphal。后续 monetary/fiscal 的被导入实现未读，不属于本轮接入；可见参数依赖 istar/rho_pi/totalpit/epsilon_pi，不授权调用。完整单位、选定 input bundle locator/year/stage/hash/尺度仍 UNKNOWN。

## 现有 synthetic seam
integration.py 47–53 的完整签名：
`integrate_turn(repository, task_root, turn_root, turn, states, batch, frozen_shares, expected_share_sha, ledger, household_rows, *, annual_context, target_year, province_axis, source_sha256, input_kind, price_basis, price_verified, params, migration_wedge_destination_origin, spies, prepared_array=None, province_mapping=None, prepared_middle_stage=None)`
无返回类型注解。其 frozen OneTurnInputs 字段类型为 province_order:tuple、old_provinces:tuple，其余 params/phi/migration_wedge/household_outputs:object；SyntheticSpies 四个必填 object callbacks：migration_inputs_factory、reconstruct_migration_labor、firm_stage、composite_household_wages（10–25）。

60–115：核已加载 context/array/middle class 及 __file__ exact locator，不自行 import；调用相应 validate。67–68 要求 synthetic 且 exact SyntheticSpies，observed 在消费调用前阻断。states 必须 tuple[dict]、annual index/source-name严格匹配，prepared-array 时短名映射匹配；N/wjt/tau 与 params ga/phi_l/alphal 必须存在；batch.ct/distance 核 scalar finite/shape，未在此建立所有state scalar/深不可变性。
prepared_array 时直接复用其 master，否则复用 context tuple；distance/batch仍原引用。117–138 的同一 inputs.phi 传入两个 callback 边界；若 factory 构造原 MigrationLaborInputs，内部会复制，不能声称内部数组仍 is master。顺序 labor→opaque firm 或 prepared middle→wage；wage 用 firm.wjt。prepared-middle 需 array，其 validate/run 实现未读。

prepared-middle 模式118在 factory 前计 source_faithful_labor_reconstructions attempt，135在 wage 前计 composite_wage_batches；factory失败不等于 reconstruction已进入。默认 callback 模式没有本地两项增量；其他内部attempt/completion及完整失败账本UNKNOWN。未见局部retry；异常不在此catch。返回 inputs/migration/wages/middle_result/context，full_outer_runtime_integrated=False、model_activation=False；flags不能证明 callbacks 无科学副作用。

## UNKNOWN 与下一精确门
| 定义/依赖 | 允许文件中字面 locator | 本轮结论 |
|---|---|---|
| composite_household_wages | one_turn.py:33 from .wage import composite_household_wages；231–238调用 | 定义/signature/公式 NOT_READ/UNKNOWN；下一只读请求可精确指定 src/ch5_two_asset_hank/multi_province/wage.py，不搜索或追读 |
| PreparedMiddleStage.validate_pre_spy/run | integration.py:108 Path(__file__).with_name('middle_stage.py').resolve() | 实现/内部账本 NOT_READ/UNKNOWN；下一请求可指定 validators/multi_province/annual_observed_labor_diagnostic/middle_stage.py |
| helper wedge/kernel | context:52、414同目录 lagged_observed_gdp_wedge.py | 本轮未读helper定义/执行；不重开已接受hash/tolerance leaf |
| capital/firm/fiscal/monetary | one_turn.py:17–33相对导入 | 传递side effects/未接受定义UNKNOWN；C1/firm已有合同只继承prior readiness |
| 真实 callbacks 与选定 scientific inputs | 注入 object，无真实callee locator | UNKNOWN，先给精确bindings，不能凭类名或成功CLI推补 |

module可见情况：context/header stdlib，adapter/migration有numpy，one_turn有相对领域imports，integration/header stdlib。可见声明、class/常量初始化及函数内动作，不证明传递import closure/安全；所有进口解析与运行未执行。图谱及import closure未建立。

继承prior readiness与work_field_hash_binding：CONSERVATION_TOLERANCE=1e-12；frozen hash little-endian float64/F-order/uppercaseSHA、无shape/axis/dtype tag，独立shape/axis/finite检查；年度master为C-order。C1 GovInv=max(Kt0-private,0)/MU_10WAN_YUAN；firm只override GovInv/AtTax/Lt_prev，供给private[index]/migration.lt_supply[index]，输出wjt入wage；allocation/feedback alias同阶段，不重复记账。未重读其leaf，也未运行。

提案（不ISSUE、不创建）：先开上表 wage 精确定义和必要middle ledger只读门，再判现有 seam 是否覆盖需要。对 canonical31 invented-fixture 共享master验证，可提 tests/test_ch5_observed_consumer_bridge.py，只用虚构名称/数据及显式callbacks，单独新engineering预算、首失败停止、独立review；不重复建已有synthetic编排。只有既有seam不能覆盖已审合同，才另提 inactive validators/multi_province/annual_observed_labor_diagnostic/observed_consumer_bridge.py 的精确diff；不改production blocks、不默认科学callee、不私绕kernel。canonical31真实consumer compatibility仍NOT_EXECUTED。

实际data1 consumed/remaining0、原engineering remaining0。已退出child的seal/master不存在，CSV/hash仅证据，不能重新封装/伪造token/observed改synthetic；合法新in-process准备需新明确authority/budget。所有本轮Python/import/AST/test/probe/auth/kernel/helper/array/matrix/science/model/consumer/outputwriter/calibration/download为0，无源码/Git变更。target2018/obs2017、retrospective_revised/year_end_resident/current_price_methodologically_attributed、price_verifiedFalse/releaseUNKNOWN/baseyearNone保持。C9PAUSED、ObjectiveARETAINED/windowUNACCEPTED、历史CALL_LEDGER_UNRESOLVED/oldattemptsCONSUMED、model_activationFalse/ResultsFALSE、historicalNONCOMPLIANT保留/排除。交付两文档后停在 Work 独立 ACCEPT/REJECT。
