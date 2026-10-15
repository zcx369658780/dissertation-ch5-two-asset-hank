# V0.0.8 跨来源经济理论版前提案独立科学审议（非冻结）

日期：2026-10-15（Asia/Shanghai）

**审议状态：`V008_SOURCE_ONLY_THEORY_PROPOSAL_REVIEWED__WAIT_OWNER_CORRECTED_MODEL_CHOICE__NO_IMPLEMENTATION_OR_REAL_READ`。**
**结果：Codex版前科学提案限于DESIGN_ONLY接受，允许作为Owner讨论的证据材料；既不采纳一份新的已冻结经济方程，也不批准具体实现、真实C8输入、科学调用、GE或Results。**

## 1. 证据身份与限度

- Owner已启动 V0.0.8。现行草案为 [versions/0.0.8/plan.md](plan.md)，版前commit `91e65c15c8493da4b2dbc936bbd2819027089bcc`、blob `0c53d11f1f5911795e5f3a2fcfa3793aa9337ad0`，不能改写成冻结科学合同。
- Codex交付 `V0.0.8_M1_LABOR_FISCAL_MODEL_CROSS_SOURCE_SCIENTIFIC_RECONCILIATION_PROPOSAL` 于Owner本轮会话；无实现候选/Git写入，报告自己注明 PDF与ZIP `NOT_IN_CODEX_VIEW`、Git只读23次、0科研/真实数据运行，属于`CODEX_REPORTED_SOURCE_ONLY`。网页Astra已独立核GitHub当前已接受Python代码、历史Lt映射/2009 parity、双边归一化组件和GE source audit，审阅Owner提供的博士PDF及原MATLAB ZIP，不能反向声称Codex自己已读附件。
- PDF《基于异质性新凯恩斯模型的中国经济区域均衡协调发展研究》，物理页94–97（论文页74–77）：(5-1)各目的地劳动负效用，(5-2)原家庭预算统一工资税只扣一次、未明示Tt，(5-3)劳动聚合和综合工资，(5-11)双边微观积分乘来源人口构成目的省劳动，(5-16)全国政府`GovInc/GovExp`含利润税、`Lt^s*tau`、国有资本回报、转移和`(Y+B)rb`，但具体账户含义/闭合并未建立。PDF表5-1 `delta=0.0025` 与MATLAB初始化`0.025`存在明确矛盾；31/26省文字冲突；旧论文文本不是经济正确性权威。
- Owner上传MATLAB ZIP下的 `HANK_2ASSETS_HJB.m`、`HANK_mp_1turn.m`、`Lt_seperate.m`、`wage_caculate.m`、`HANK_firm.m`和`multi_prov_HANK_12sts.m` 已本轮精确只读；逐文件SHA256与已公开的 2026-08-30 `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_SOURCE_AUDIT_AND_CONTRACT_FREEZE_REPORT.md` 所记这六文件SHA256一致。因此该ZIP的这些成员有历史源码审计的文字/hash对应，但**不等于2026-09-25 Python C8原件或当次实际模型执行代码认证**，也不证明原MATLAB方程正确。
- GitHub可核早期 `docs/CH5_TWO_ASSET_HANK_MP4B_FIRM_LT_PREV_SAME_TURN_HOUSEHOLD_MAPPING_REPAIR_AND_ZERO_MODEL_VALIDATION_REPORT.md`：将household Lt送到firm Lt_prev是2026-09-01源忠实修复，旧2009 parity 184 turns/31省/max normalized diff约`3.835889478194021e-11`受限通过；这既不解决单位，也不能按新理论追溯否决其源忠实资格。2026-09-10已接受的来源列归一化劳动组件只证守恒，原C8未激活，也不证工资劳动双边FOC一致。
- V007已正式有限关闭，accepted candidate `d8bb49d86ea674ea4ff5e3fdf03929baa08a6514`、tree `9b685397ad5bc76a4ac3bf4203776389742c5ec5`。下一正确模型分支代码基线尚PROPOSED；不能因V007是文档已接受就覆盖原dirty、自动合并main或签发本版实现授权。

## 2. 静态确证与条件性理论结论

1. **劳动指数与实际双边劳动的区分是成立的。** 若`ell_i=(sum_j phi_ji h_ji^(1+eta))^(1/(1+eta))`、`v_ji`是每效率单位一致净收入、`eta>0`，最优化得到`W_i=(sum_j phi_ji^(-1/eta) v_ji^(1+1/eta))^(eta/(1+eta))`及`h_ji/ell_i=phi_ji^(-1/eta)(v_ji/W_i)^(1/eta)`，严格`sum_j v_ji h_ji=W_i ell_i`，**一般不要求sum h=ell**。需识别原家户HJB单一`l`是否真的代表这一指数并处理`alphal`、`z`、效用权重与价格净税路径，否则CES形式接近不意味着已匹配实现。
2. **旧双边劳动并非微观积分的精确重构。** PDF (5-11)要求`N_i int z h_ji dmu_i`，旧`Lt_seperate.m` / 当前Python source-faithful用`Ct_i^(-gamma/eta)`等省级均值构造劳动并乘`N_i`，既没逐状态积分，也未显式带有状态`z^(1+1/eta)`项。`E[c^-a] != (Ec)^-a`在异质消费下成立（需正确处理z相关性），不能把旧Ct插件默认为微观最优化精确加总。L1若成立，应以`int z ell_i dmu_i`和严格dual allocation恢复一致；L2按真实总工时配置须相应把综合工资改为份额收入，不能沿用CES工资却强制数量守恒。
3. **工资重复扣税仅在“同一工资税”解释下确证。** `wage_caculate.m:8`使用目的省`tau_j`（Python `wage.py:59–62`），原`HANK_2ASSETS_HJB.m`对收到的`results.w`再乘`1-tau_i`（Python `nonlinear_continuation.py:724`）；`HANK_mp_1turn.m:49–53`证明综合工资给下一次household。单目的地、alphal=1、无迁移成本、税率同值时形成`(1-tau)^2*w_gross`，与PDF (5-2)仅一次全国税不一致。若是两层税，必须分别命名、规定序列/税基/收款人与财政现金流，不能凭相同`tau`假定合法。
4. **财政资金去向未被旧命名识别。** `AtTax=At*rah-int a*r_eff dmu`是分布平均收益差，乘N可成为地区收益差，但不一定属于政府税；可能是中介费用、实际资源成本或利润，必须互斥归属。人均`Tt`进家庭预算却作为地区Govinc直接扣除，没有已证人口桥；`Lt*tau`一般缺工资货币计价。`Bt*rb*N`中的`Bt`是净家庭流动资产，不能未经资产负债表证明就是政府债务。PDF(5-16)全国统一政府账与Code的逐省Govinc/GovSurplus不同，不自动引入31个独立地方政府和地方债。
5. **raw/used收益与clip税的潜在重复记账是条件性检验，不是现行C8已证bug。** `firm.py:118–135`对`(ra0-ra_used)*Kt`调整Corptax，现行接受路径使用raw-ra0做私人payoff、used ra计GovInv；在假设同一期、同资本池、无其他结算/工资clip时，会出现私人资本份额的多记项。原K1B私有收益与现金流有lagged timing，现无同一时期完整资产负债表，禁止据此改clip公式或宣称已量化C8重复支付。
6. **政府和资本时序应先界定静态目标与全国账户。** `GovInv`在历史C1是政府资本**存量残差**，不是当期财政投资现金流；未来应独立给公共资本动态/折旧融资。原`firm.mt`用`Lt_prev`等当作`t-1`，而旧source outer iteration的`k-1`不是经济时间。优先给静态/稳态的合法现金账与价格条件，不能为了“静态”偷偷设稳态通胀为0或更改原`0.02`，动态NKPC需单独推导。

## 3. 需要纠正或降级的Codex推荐

- **优先建议研究L1/CES劳动对偶是合理的研究方向**，但仅为`PREFERRED_DESIGN_CANDIDATE`，不是`OWNER_ADOPTED_SCIENTIFIC_FORMULA`；严格对偶工资、两资产HJB labor_index的statewise定义、税后收入与劳动效用定标必须作为同一个模型规格。
- **不能预先把`AtTax`定为政府征收**；CODEX表中方案I的这一行需降级为分别审查政府征收/中介转移/实际成本，未裁决不并账。
- **不能默认添加各省独立债务预算**。论文是统一政府/全国税率；校验用的省级账户可以是全国政府的分析子账，中央统一预算与跨区转移先为基准。若要地方独立财政/发债是新的Owner制度决定。
- 旧论文(5-16)列式与代码差异、折旧0.0025/0.025、31/26文字冲突仍是`CONFLICT`，不能把任一旧文本当经济正确答案。旧G0/B3、安全历史与C8受限科学计算完全不在本版修订范围。

## 4. 下一科研方向的Owner单次决定（待批）

**Astra建议作为一个完整方向包供Owner批准**：
- 以L1：**CES劳动指数+严格来源居民与工作地双边最优化/工资对偶**为纠正模型主线；L2实际工时+外生份额为可证伪对照、不自动激活旧origin-normalized route。
- 只存在**一套明确计价的全国工资税**，税率在家庭净工资构造时只扣一次；如未来加入双层税另须明确Owner决定。迁移成本是现金/资源/效用何者须书面定义、分开归属。
- 以**全国统一政府财政账户**为基准、各省仅分解账，不默认地方债。公共资本存量/净投资、私人raw/公共used收益、工资税、AtTax/中介成本、Tt等分别记账；`AtTax`的最终经济归属保持`UNADOPTED`并在方案比较中互斥建模，不因为姓名含Tax就自动视为税。不得把财政残差默认为自动平衡的GE。
- **先定义可审核的静态/稳态完整经济账户与资源一致性**，分开经济时间和迭代时间；完整动态NKPC/非零通胀、K2、IRF/福利等依论文首稿科学必要性再批准。不得从这条路线推断V008已有科学实现许可。

Owner如同意这一方向包，Astra才能集中冻结V008正式科学设计、精确实施路径/资源和验证oracle，然后**另行**独立授权隔离人工经济体内的新corrected-model实现；原C8不改、不运行/读真实原件。若Owner不同意L1，应集中指出首选的L2/其他机制，不进行重复科研SRC审查。

## 5. 状态及保留约束

V008当前仍**DRAFT/WAIT_OWNER**，未冻结、无新科学/工程实现许可。V007`CLOSED`、历史2009 parity和C8有限accepted资格不追改。代码基线PROPOSED/UNDECIDED，main未合并前版，原D盘8 dirty、untracked/ignored、B3均不触碰。
继续维持`A16 UNRESOLVED/FAIL_CLOSED`、`window UNACCEPTED`、`C9 PAUSED`、`CALL_LEDGER_UNRESOLVED`、`model_activation=False`、`Results FALSE`，旧科学/data/consumer预算CLOSED；C8 A–D 37件仍仅REQUEST_ONLY，阶段A manifest当前长度UNKNOWN。V0.0.9 NOT_STARTED，CH5_WORKFLOW_V1.2不变。
