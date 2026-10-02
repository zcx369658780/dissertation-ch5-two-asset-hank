# Wage / middle static contract supplement
2026-10-01；record10；DOCUMENT_ONLY_CANDIDATE_PENDING_INDEPENDENT_WORK_REVIEW。
现有 synthetic seam + middle 具有承载31-size wholly invented fixture的静态能力；没有看到必须新增 production bridge 的能力缺口。31维实际通过、真实消费者兼容及传递导入安全仍 UNKNOWN。本轮只读指定两源并交付两文档，全部执行预算0。

当前修正 TASK SHA256：0353DA977DC2A027F72895BFC0FA69B54ED15EB6BD64951B399E9CDC6249283B。首次行政文本读取见末尾两个 pin 的path=null；Work随后改为明确path，hash/范围/预算不变。首次未记录旧rawSHA，未把旧版用于执行；两源读前以修正版及 prior receipt核hash。图谱未索引，采用bounded rg/定义范围，不追imports；不重读已接受五源。

## Wage：字面公式、轴与复制
wage.py 11–76：
`composite_household_wages(provinces: Sequence[Mapping[str,float]], firm_wages: Sequence[float], phi_mat: Sequence[Sequence[float]], sigmau_mat: Sequence[Sequence[float]], *, phi_l: float, alphal: float) -> tuple[float,...]`
无默认值；输出按origin。令 j=destination、i=origin、exponent=1+1/phi_l、outer=phi_l/(1+phi_l)，原式：
`base[j,i] = firm_wages[j] * (1 - taxes[j] - sigmau_mat[j,i]) / phi_mat[j,i]`
`W[i] = alphal ** (-outer) * (sum_j phi_mat[j,i] * base[j,i] ** exponent) ** outer`
taxes来自逐destination province["tau"]；与已接受labor的tax_by_origin[i]不同，分别保留原索引，不纠式、不宣称经济等价。

n>0、firm wage长度n、矩阵(n,n)、矩阵及工资finite、phi>0、phi_l/alphal finite positive；tau存在且finite。base<0拒绝，term核finite，total<0拒绝，最终value核finite/nonnegative。base/total没有独立finite检查；没有单独firm_wages>=0检查。不把隐含失败路径写成未存在的显式校验。

wages/matrices用np.asarray(dtype=float)，可能复用或转换，未见显式输入写入；这不是强制copy，也不建立函数内部same-object保证。继承seam的same-master只在两个注入边界成立；原labor constructor会copy。数值一致、对象身份、readonly backing是不同主张。

## Middle：接口、结果与固定身份
middle_stage.py 所列接口均无参数/返回注解、无默认值：
| 行 | 接口 |
|---|---|
| 155–172 | PreparedMiddleStage._validate(self, *, annual_context, prepared_array, province_mapping, ledger) |
| 174–182 | PreparedMiddleStage.validate_pre_spy(self, inputs, frozen_shares, expected_share_sha, *, annual_context, prepared_array, province_mapping, ledger) |
| 184–265 | PreparedMiddleStage.run(self, inputs, migration, frozen_shares, expected_share_sha) |
| 334–347 | prepare_middle_stage(*, annual_context, prepared_array, province_mapping, ledger, dependencies) |

prepare返回PreparedMiddleStage，run返回MiddleStageResult。75–149的dataclass均frozen；必填字段：
| 类 | 字段（类型）/默认值 |
|---|---|
| FixtureDependencies | c1_residual:object、evaluate_firm:object、fixture_label:str |
| CapitalResult | wealth/flows/private/domestic:tuple、capital_residual:float；no_same_turn_share_recomputation:bool=True |
| C1Result | province_order/GovInv_residual_MU/firm_K_accounting_MU:tuple；capital_unit:str='MU_10WAN_YUAN' |
| FirmResult | 15个float：Kt,Lt,Yt,mt,KNratio,wt0,wjt,rk,Thetat,It,PIt,Corptax,ra0,ra,Govinc |
| MiddleStageResult | firms:tuple、capital:CapitalResult、c1:C1Result；model_activation/full_outer_runtime_integrated:bool=False |
| PreparedMiddleStage | annual_context/prepared_array:object、province_mapping:tuple、ledger:dict、dependencies:FixtureDependencies；token=None且repr/compareFalse；seal=None且init/repr/compareFalse |

C1Result/FirmResult没有本地post_init或as_source_dict。callback raw对象可选as_source_dict()的定义/副作用未读，不推补。

seal核owner/token、原context/array/array seal/mapping/ledger/dependencies/callback identities及labels；dependency label与ledger label均要求非空原生字符串，没有要求二者相等。deps必须exact FixtureDependencies且两个callback callable。carrier核已加载adapter class/module __file__ locator和metadata/seal，synthetic-only；inputs须exact integration.OneTurnInputs，模型order匹配且phi is prepared-array master。不重新读取或hash源代码，也不重新认证raw sources。

## 输入、资本与失败账本
维度n=len(mapping)。STATE_FIELDS（19–21）：N,wjt,tau,inter_prv_ratio,Kt0,alpha,Zt,pit,Kt_prev,Zt_1,pit_1,rk,corptau,Tt,ramin,ramax,wjtmin,wjtmax；另需province_index/source_province_name/name严格mapping。PARAM_FIELDS（22）：ga,phi_l,alphal,epsilon,theta,delta。state/params有限非bool Real，N/Kt0/Zt>0、0<alpha<1、min<=max、epsilon!=0；无theta/inter_prv_ratio范围检查。batch.ct/at/at_tax/household_lt长度n且finite，ct>0、at>=0、household_lt>=0；at_tax无符号限制。distance shape/finite，仍与annual phi不同。

| 阶段/范围 | 字面检查及attempt顺序 |
|---|---|
| Ledger 14–16、66–72 | exact dict，engineering_fixture_label非空原生str；六项非负原生int：source_faithful_labor_reconstructions、frozen_k1b_quantity_allocations、k1b_feedback_calls、c1_residual_govinv_constructions、firm_evaluations、composite_wage_batches |
| pre-spy 174–182 | seal/carrier/input/sharehash检查，无migration参数。shares入口47–58只核2d/(n,n)/finite非boolReal后转float64，不直接核元素nonnegative、diag或columnsum |
| run 184–194 | 再验绑定/sharehash；migration.lt_supply长度n、finite且positive；这些失败不增加本文件下游计数 |
| capital 195–219 | allocation/feedback两项先递增（同一分配两个标签），再 wealth=at*N，flows=shares*wealth[None,:]，private=sum(axis=1)，domestic=diag(flows).copy()；不重算shares |
| capital checks 208–219 | shares columnsum1：rtol0/atol1e-12；flows/national residual：1e-12*max(1,sum(wealth))；domestic exact==(1-theta)*wealth；private>=0。发生在attempt已计后，不能写成未进入allocation |
| C1 220–245 | 保存target/private authority，先计attempt，再c1_residual(Ktarget_MU=targets,Kprivate_current_MU=private,province_order=...)；拒绝authority数组修改/order错位；GovInv exact max(target-private,0)，accounting exact max(target,private)；累计C1 count须恰1 |
| firms 247–265 | 复制省记录，只补GovInv/AtTax/Lt_prev；逐省先计再evaluate_firm(source,private_authority[index],labor[index],inputs.params)；15fields finite，Kt accounting偏差<=1e-12*max(1,abs(expected)) |

61–63、174–182：frozen hash为np.asarray(values,dtype="<f8").tobytes(order="F")的uppercase SHA256；expected hash匹配[0-9A-F]{64}。无shape/axis/dtype tag；独立shape/finite/axis检查仍必要。不是年度master的C-order digest。

本文件无独立events列表、不增加labor/wage计数；继承integration的labor计数在factory前、wage计数在callback前。没有retry/rollback：失败保留已增加的attempt，资本失败抑制C1/firm；C1失败抑制firm；某firm失败抑制余省和结果返回，继承seam因异常不进入wage。外部callback内部completion/count/side effects仍UNKNOWN，label/False flags不保证无科学。

## 最小下一工程门：复用，不新增bridge
现有seam+middle按n驱动，synthetic虚构mapping可取31项；全称/简称必须均虚构，不能借用observed canonical31名字、实际值、CSV或旧child seal。原observed blocks保持。静态能力足够，当前没有具体生产文件diff提案；若未来fixture揭示缺口，再独立定位最小diff，不预建重复master或bridge。

仅提案专用测试路径 tests/test_ch5_observed_consumer_bridge.py（本轮未创建/核存在性）；Work须另签精确编辑allowlist与有限新engineering预算。用纯虚构context/array/states/batch/distance/shares及显式science-free callbacks，不安装/默认真实生产消费者、不私调kernel、不启动新的observed auth。新测试应建立：
- 非对称31维轴和destination/origin索引可辨，两个callback接收同一master；原消费者内部copy与输入身份分开记录。
- 成功时顺序labor→allocation/C1→31逐省firm→wage，六项attempt分别1/1/1/1/31/1；private/flows/home/C1/accounting及wjt forwarding按原checks，F-order frozen hash不混年度C-order。
- 独立纯虚构失败case：篡改hash/axis/seal/mapping在相应入口阻断；资本/C1/某firm失败保留正确attempt并抑制下游；factory失败计labor attempt但不能声称reconstruction已进入。每case新fixture/ledger，只在明确测试预算内，不复活旧额度或重试真实数据。
- 用独立预期检查原wage的destination tau与labor origin tau差异，测试原式而非改式；callbacks证明工程编排，不代替真实consumer compatibility或经济正确性。

wage/header stdlib+numpy；middle/header stdlib+numpy，顶层常量/class/function声明，无可见顶层callback/I/O/运行流程；传递imports仍UNKNOWN。middle指向adapter（273）及integration（291）的literal __file__ locator，内容继承既有独立接受合同，本轮不追读。

本轮所有数值/Python/import/AST/tests/probes/auth/kernel/helper/array/matrix/reconstruction/science/model/consumer/writer/calibration/download/launcher为0；无source/tests/status/Git修改。实际data1 consumed/remaining0，原engineering remaining0；child seals/master已退出，CSV只证据。target2018/obs2017、价格限制、C9PAUSED、ObjectiveARETAINED/windowUNACCEPTED、历史CALL_LEDGER_UNRESOLVED/oldattemptsCONSUMED、price_verifiedFalse/releaseUNKNOWN/baseyearNone/model_activationFalse/ResultsFALSE、历史NONCOMPLIANT保留排除。停在Work独立ACCEPT/REJECT，无自accept/后继签发。

