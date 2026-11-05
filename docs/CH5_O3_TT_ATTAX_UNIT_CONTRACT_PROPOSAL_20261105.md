# O3转移支付与资产收益差额：单位追踪及财政边界决策稿

DATE=2026-11-05
STATUS=STATIC_UNIT_TRACE_COMPLETE__PROPOSED_FISCAL_AGGREGATION_PENDING_OWNER
GOVERNANCE_PARENT=ef98f7907cc6dc7c70d05b4344011245e671e07a
MODEL_DOCUMENT_HEAD_AT_RECHECK=41af56d32868a361d828291b3b089388ec848b3d
MODEL_CODE_CANDIDATE=caa5a83c6b480f616286ffb7eabbae6abdb1f9e8
NEW_SCIENTIFIC_RUN_GRANT=NONE

## 核查结论与建议

已核清一个需要拆开的同名量：论文政府预算中的Tt是转移支付**总额**；当前state.Tt却原值进入每来源地家户的transfer_income接口。AtTax在当前O2批次合同中明确属于**未乘人口的家户统计量**，旧one_turn又把它原值送入省级企业Govinc。字段名相同不代表它们已经在同一总量尺度。

建议将两者在外层显式拆成家户量与省级金额，按已定A1的家庭财政H聚合约定，只在财政边界乘一次同轮来源地H：

```text
household_transfer_per_H[i] = entering_state[i].Tt
asset_return_gap_per_H[i] = household_batch.at_tax[i]

provincial_transfer_total[i] = H[i] * household_transfer_per_H[i]
provincial_asset_gap_revenue[i] = H[i] * asset_return_gap_per_H[i]
```

这项省级财政换算**尚未获Owner采纳、未实施**。Owner此前已采纳工作地工资总额税基；该已定事项不重开。本稿只请求确定上面两个原家户量的财政聚合合同，不新增税种、税率、收入共享制度或财政平衡目标。

## 来源追踪

| 层次/位置 | 定点证据 | 可以与不可以推出的内容 |
| --- | --- | --- |
| 论文c3.tex第48—53行，审计摘录T3_L48_53 | Tt+M*rb+S=L*w*tau_w+公司税+政府投资收益；文字明确Tt为“对家户的转移支付总额” | 政府支出侧使用总额可证；不证明代码同名标量已经是总额 |
| 论文c5.tex第155—164行，T5_L155_164 | GovExp对各省Tt及其它支出求和 | 省级支出相加的角色可证；不自动采纳该稿中的其它货币/债券表达式 |
| validators/multi_province/mp4b_python_empirical.py:115及348—354 | Tt由transfer_income标量载入，再作为家户调用的外部transfer_income传入；AtTax在返回后以a_ss*rah减去实际有效资产收益的分布汇总构造，式中未乘N | 生产者/消费者角色及没有人口因子可证；不执行其旧runner，不把初始化旧式恢复为当前方案 |
| src/ch5_two_asset_hank/multi_province/outer_ha_batch_adapter.py:191 | 将进入快照Tt原值赋给OriginHouseholdRequest.transfer_income | 当前O2保留家户输入角色，未变成省级转移总额 |
| 同文件:204及217 | Ct/Lt/At/Bt/AtTax原值复制且不乘人口/税；强制UNSCALED_STATS | 当前批次的AtTax是未乘人口统计量；标签/结构检查不证明真实数据资格 |
| src/ch5_two_asset_hank/multi_province/temp31_binding_skeleton.py:14 | UNSCALED_STATS=HOUSEHOLD_STATS_UNSCALED_BY_POPULATION | 明确禁止先在批次放大后又在财政放大 |
| src/ch5_two_asset_hank/multi_province/one_turn.py:222及firm.py:135 | batch.at_tax原值送firm；Govinc直接加AtTax、减Tt | 原链没有这两项显式H聚合；不据此认证真实运行误差，也不在本轮改写原链 |
| 原MATLAB HANK_firm.m第89及95行，M_F_L80_98 | Ct_total=Ct*N，但Govinc直接加AtTax、减Tt | 原源链确实区分过家户消费与总消费；原财政的省级单位闭合仍不能由“忠实复现”推定 |
| src/ch5_two_asset_hank/multi_province/capital_allocation.py:77及fiscal_diagnostics.py:22 | 资本使用At*N；政府债息诊断使用Bt*rb*N | 与H聚合的其它外层角色相容；本稿不改资本配置、债务定义或利率时序 |

本次只利用已有审计摘录的外部输入/输出及财政角色，不重审HJB/KFE方程、求解、归一化或网格。当前选定单来源worker外部调用也把state.Tt原值传入净工资HA；它是关闭额度中的历史调用点，本轮未执行。

## 拟议的财政边界合同

- 家户侧Tt不乘H，原AtTax重构及HA返回均保持；只在独立外层财政账生成省级总额，使用同一来源省、进入迭代和单位合同的H。
- H沿已有家庭人口尺度；企业就业尺度E=pH仅用于既定A1生产劳动，不能替代这两项家庭财政聚合。不得对已含pH的工资税子账再次乘H或p。
- 拟议账的两个新字段明确写total；旧state.Tt和batch.at_tax仍为原家户角色，不全局重命名、覆盖或在HA内修改。
- 资产收益差额沿既有Govinc收入角色准备入账，不把它解释为新增现实法定资产税，不新增扣款或重新计算密度；不裁剪符号、不改为绝对值，不乘工作地工资税率。
- 若输入已经是省级总额，必须走独立明确的total输入合同，不允许把它伪装为当前UNSCALED_STATS再乘H；当前真实来源资格仍未建立，不能用字段标签自行放行。
- 政府向家户支付转移和家户收到转移是同一项的支出/收入两面，不构成家户重复扣税；政府收入记AtTax也不授权在HA内再扣一次资产收益。

若采纳，独立外层金额账可按下列角色组合：

```text
Govinc_candidate[i] = ExistingCorptax[i] + AdoptedWageTax[i]
                     + provincial_asset_gap_revenue[i]
                     + ExistingGovInv[i] * ExistingRa[i]
                     - provincial_transfer_total[i]
```

此式为待采纳的金额清单，不是已接受的完整财政/均衡公式；旧Corptax含原工资/收益裁切补偿，保持原角色。全国债息诊断仍保留Bt*rb*H的原角色，不在此稿添加财政余额等于零的条件，也不改原GovInv自适应或央行规则。

## 本次能够确定的边界

家户原量与省级总额必须分列，且当前O2明确不含人口放大。按“每H金额流→同单位H规模”的模型内部合同，应在财政边界放大一次。由于改变实际Govinc中的金额尺度，本稿将这一步作为具体Owner科学选择呈交，不据一般工程授权自动落入原生产公式。

现实人口单位/户数/就业的桥、货币尺度、模型期间与统计年度转换仍未认证；H不能取未经采纳的户均人数或就业率，旧s_H=64.8906755511未采纳。即使Owner接受上述模型内部聚合，真实数据仍须同一分母、货币/频率及来源见证，不能称为现实财政校准完成。不是重新询问A1或已经采纳的工资税口径。

## 固定来源与本轮交付

原静态审计固定提交9bdc9e83127d32e6e29a0a5895800fd97d92cd3a：
[source_excerpts.json](https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/9bdc9e83127d32e6e29a0a5895800fd97d92cd3a/tasks/CH5_TEMP31_WAGE_LABOR_TAX_SEMANTICS_STATIC_AUDIT_R1_20261027/source_excerpts.json)，Blob 3081a685a9c7f8d0e1662a4401387399e9806846。只复用T3_L48_53、T5_L155_164、M_F_L80_98、C_EMP_L101_121、C_EMP_L337_355、C_O_L194_238和C_A_L200_225的必要角色证据，不重做116段/13报告审计。历史报告中的current不代替本次模型HEAD；当前代码传值/行号已定点重核。

本轮仅新增单位决策稿和更新当前入口。TESTS=NOT_RUN_DOCUMENT_ONLY；MODEL_IMPORTS=0；SCIENTIFIC_CALLS=0；SOURCE_EDITS=0；NEW_RUN_GRANTS=0；SUBAGENTS=0。工资税14项检查为上轮结果，本轮未重跑。私有定点证据、现场及同步回执LOCAL_ONLY保存。

工资税[已采纳实施记录](CH5_O3_PAYROLL_TAX_IMPLEMENTATION_20261105.md)保持；HA整体黑箱及原算法/网格冻结。TEMP31 7/7、Moll 3/3、工资/补录关闭，初始化旧余量仅原8格；严格reference/thresholds仍null，科学接受、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE。保护义务、历史dirty树、缓存、索引及LOCAL_ONLY载荷保持；只同步脱敏治理文档，不推模型分支或代码，不合并main。

OWNER_TT_ATTAX_AGGREGATION_DECISION=NOT_RECEIVED
NEXT=Owner决定是否按上述每H角色在财政边界各乘H一次；真实物理单位与其它E3缺口不自动关闭。
