# Record17 delegated batch leaf contract

**仅设计／静态来源事实；完整输入与运行就绪仍未建立。** 任务 SHA256：8E8CA6009A359FF1398FFF2762427A8723E4502F3CE6B8EF918C80643A380916。

来源叶：validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py，SHA256 92018027502FFA5281F9BFAC91EE70D2BED17876B65100B3321819B2C0C59DB6。原 C8 root-level preflight.json（SHA256 9045C865C857B286111AF91F88ED53F5FEC85F3371199DA8E8475456624B39EB）声明的 old_runner_sha256 与此 pin 相同；src_tree 声明与固定 HEAD:src 相同。这是行政身份匹配，不是实际调用、重载或活 seal 证明。

## 批次字段的静态链

_batch(results: Sequence[Mapping[str, Any]]) 在 215–224 行按同一 results 顺序构造并返回一个 PreFrozenHouseholdOutputBatch：

| batch 字段 | results 中每个 row 的精确来源 | 行 |
|---|---|---|
| ct | row["aggregates"]["Ct"]["mass_form"] | 217 |
| household_lt | row["aggregates"]["Lt"]["mass_form"] | 218 |
| at | row["aggregates"]["At"]["mass_form"] | 219 |
| bt | row["aggregates"]["Bt"]["mass_form"] | 220 |
| at_tax | row["aggregates"]["AtTax"]["mass_form"] | 221 |

结合 record16 已接受的 serializer→final["aggregates"] 及 C8 runner 的 base._solve_province→results→old._batch→old.integrate_turn 静态转发，原先 old._batch 的 selector 叶缺口已补足。原源码在内存中构造 batch；序列化 receipt 保存相同结构的字段。未来若重载 receipt，需要另行证明解析器到 row["aggregates"] 的对应；本轮未重载、组装向量或认证原 C8 对象／实际运行阶段，不能把静态结构同源升级为 sealed runtime identity。

## 参数与距离的直接转发

integrate_turn 在 232 行调用 base._one_turn_inputs(repository, states, batch)。235–240 行将 household.ct、province 的 N/wjt/tau、两张矩阵及 inputs.params 的 ga/phi_l 传给 labor；289–300 行将复制并填入 GovInv/AtTax/Lt_prev 的 state 与完整 inputs.params 传给 firm；302–311 行 wage 使用 phi_l/alphal，monetary 使用 istar/rho_pi/totalpit/epsilon_pi，fiscal 使用 household.bt 等字段。这只闭合直接转发；原参数字典的定义、ga/phi_l/alphal/epsilon/theta/delta 的实际原 C8 来源仍 UNKNOWN，epsilon_pi 不替代 epsilon。

324–329 行定义从 repository / base.DISTANCE_RELATIVE 加载 distance score 并传入 share input；该常量定义不在本轮 source 中，精确 locator UNKNOWN。原 C8 preflight 的 distance_sha256 声明为 51A04FCAA1FA519B142BE2A155640F77E8746493AFDF4865ED243B96526E550D，目标未读取或 hashcheck。45–46 行输入 locator 为 TURN4_ROOT=reports/ch5_mp4c_k1b_turn4_anhui_f0364_positive_domain_intersection_repair_reexecution_20260921_run001，TURN5_INPUT 为其下 turn5_k1b_input_candidate.json；均未追读。

**仍需 Work 精确 locator／hash／字段 authority：** base._one_turn_inputs 的参数字典定义与原 C8 source-stage 绑定；base.DISTANCE_RELATIVE 的定义和原 C8 consumer 来源；sealed receipt／parser／实际阶段对应；明确 units/calendar、archive 与 canonical metadata。没有据文件名推断，亦不提出自动后继。

所有新运行预算／调用 0；固定 C8/C7 entering state/shares 及旧 population/params/distance 保留。C9 暂停，Objective A 保留／窗口未接受，16 项保护分类未解决，旧 consumed budgets／CALL_LEDGER_UNRESOLVED 不变，model/Results=False。无源码、测试、Git、重构、保护实施或新 output root。助手额外展示 227–228 签名行的分工偏差已记录并排除为新增合同依据。等待独立 Work review。

