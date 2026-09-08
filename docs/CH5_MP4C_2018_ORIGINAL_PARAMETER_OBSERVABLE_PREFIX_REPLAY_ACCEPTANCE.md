# 2018 原参数可观测前缀重放 — Reviewer 验收

日期：2026-09-08。唯一仓库：zcx369658780/dissertation-ch5-two-asset-hank。
候选：9d76747f48858a3e9289de8f284fffbc49aaedce。
审阅时 live main：09de5178d6a51bf6b36fbd4a309d161a8ef99d44。
任务：tasks/CH5_MP4C_2018_ORIGINAL_PARAMETER_OBSERVABLE_PREFIX_REPLAY.md。

## 验收决定
接受本次观测获取及已比较前缀/失败复现。保留 Builder 的 OBSERVABLE_PREFIX_CAPTURE_COMPLETE 和 MATCHED_PREFIX_AND_FAILURE_REPRODUCED。
Reviewer marker：ORIGINAL_PARAMETER_PREFIX_REPLAY_ACCEPTED__CAUSAL_RATE_QUESTION_OPEN。
这不是全数组历史同一性、跨语言 parity、数值修复、完整2018年度或 Results 验收。原来的 PARTIAL_EVIDENCE 审计按其当时证据保留；本次新增捕获形成独立证据，不倒填旧运行文件或捕获时哈希。

候选相对上述main为ahead1/behind0，远端 codex/ch5-2018-observable-prefix-replay-20260908 指向候选。比较返回的新增路径全部位于允许的单份报告、reports目录、单个测试与observable_prefix_replay诊断目录；无生产/helper/参数/原任务修改。采用保留候选历史的非force后继提交整合。

## Reviewer实际审阅范围
读取了exact task、报告关键结果及完整工程/预算段、prefix_comparison、delivery_checks、manifest_readback、最终tests_05日志及15项测试定义；审阅run、observer、control、analyze、finalize的观测、比较、预算和保存实现，并复用未改变的原worker/controller/post-loop契约。读取首次启动stderr，确认失败位于bootstrap import、早于Store与worker科学进入；后续LF工作树身份与重试原因按发布回执/源码审阅。
证据标签为L3提交/代码/报告审阅与L4已发布日志检查。Reviewer没有独立运行15项测试、模型或求解器，没有直接读取Windows完整capture/MAT/NPZ，没有独立重算4278行或重验13800个文件引用。相应数值和外部哈希是本次Builder发布证据，不是Reviewer本地复算。

## 接受的复现和预算事实
- 725个实际家户入口，每个11个连续字段，共7975项；prefix_comparison逐字段最大绝对与scaled误差全部0，首差null；类别/省序比较通过。此范围内是完全一致，不泛称全部历史内部数组逐位相同。
- 报告中725组历史HJB停止状态/步数与统计量比较通过；旧审计的44项控制器标量比较通过。旧运行未捕获的内部对象没有历史全数组对照。
- 原异常在第24轮安徽call725复现。原生初始化HJB在100步返回false，统计量0.3038218386543494；原post-loop adapter仍进入KFE，随后ValueError: faithful contaminated-row solve is non-finite。KFE原始非有限线性返回已保存，但无有效KFE返回对象和该户aggregate。未进入call726。
- 24份完整31省共同入口状态在每轮第一户前保存；实际家户入口725，返回724；firm返回713、全国controller记录23、逐省action记录713。第24轮其余19省只有共同旧状态，无本轮家户结果；没有第24轮firm/适应阶段。
- 一次Python科学进程，科学耗时2874.297秒；首次bootstrap因CRLF原始字节身份不符失败，科学进入0，消耗一次允许的外部启动重试。同一HEAD的隔离LF工作树恢复原raw身份，不是求解器或算法切换。科学开始后重启0。
- native initialization/HJB/KFE各725次；HJB直接求解19961，KFE直接求解725，KFE成功返回724；劳动根入口580000，其内brentq入口同为580000，不将嵌套计数当作额外独立初始化；root residual4837970=bracketing1160000+brentq3677970。23次one-turn、713次firm、23次controller均在预算内。
- 原worker实际传入的外层上限250与source默认500分开记录；此次外部prefix上限没有修改二者。每户原生初始化、HJBmaxit100、Delta1000、crit1e-7、a_bar及算法均保留。MATLAB、独立诊断求解、其他年度/R-PLM/动态/IRF/Results调用0。Reviewer新增科学调用0。

## 新捕获对科学判断的贡献
1. 第22轮安徽ra0=0.21979491622969854，第23轮ra0=0.21906938941252802，均严格高于.09；不再只是缺raw情况下的边界接触推断。第23轮wt0=2.5772708754207905，严格高于1.3。实际返回ra=.09、wjt=1.3；家户消费的是rah=.09，不是raw .219069。
2. 第23轮安徽rk=.244069389412528、delta=.025、截零后PIt=0，故divrate=0，ra0=rk-delta。mt=.9943859584740543。结合Y/K=.317580620411841可定位到较高的当期资本租金，而非该时点正利润分红。此为同阶段代数分解，不是Zt/K/mt的因果贡献率。
3. 原国资反馈确实起作用，但raw仍位于clip上方。安徽第5轮ra0约.53423，到第23轮约.21907；在raw降至.09以下之前，截断后的ra仍可长期保持.09。不能以存储价格不变反推没有调整，也不能单独将raw下降全归因于GovInv。
4. 第23轮全国最大nk_gap=.04124871080231385，决定省贵州，门打开；安徽Zt .7163967429125945→.6650485431957093，GovInv115261012.11434016→126787113.32577418。原先未知的第23轮全国最大值/决定省已由新捕获补足。第22轮贵州使门关闭是另一时点，不与此冲突。
5. 第5–15轮31省厂商ra都在上界；第23轮仍24省在上界，7省内部。第23轮工资19上界、5下界、7内部。问题并非安徽一个省出现高raw价格，但唯一call725异常不能推广为24省都失败。
6. 第23轮安徽Kt_supply/Kt=.0008794002451333387，约.08794%；其余约99.91206%为模型GovInv。保持源资本定义及模型单位，不据此擅补本地资本项。current household Lt_prev=.6661844894752886与destination Lt_supply=3210665.858026796是源中不同对象，不能互换；本轮未作单位/公式修正。
7. 安徽外省权重0，turn23组合收益计算使用turn22 ra，随后才计算turn23新firm价格和调Zt/GovInv。call725的高rah具有明确滞后；当轮适应动作不会即时改写已经形成的家户输入。4278项代数核对为713个firm返回各6项身份，报告全部通过；clipping branch归因是对raw/returned的派生，不称内部逐行trace。

## 测试、manifest和限制
最终日志tests_05为15条ok、Ran 15 tests、OK；日志LF SHA256为6AD4825B997E6BF5C6E6B191C45AFF2718208B34E2FB308D24BCAD0DE126C246。早期合成检查、日志编码/句柄修正及PowerShell大小写列解析故障均保留；不算科学重试。
外部manifest_02.json SHA256：4C18B9AA14C23356594F1A0ECCBA346B3DB2AE668B7204A73D88A226B98B0146。Builder独立重读回执记录13800个文件引用，含13696个capture文件、8321个capture索引条目；这些计数不是科学调用，也不包装为Reviewer直接验证。旧capture-time raw-hash gap保持原限定。历史完整环境二进制没有全部记录，不从标量复现反推其逐位相同。
原生初始化此次100步失败，与后期完全共同MAT初始化实验MATLAB143/Python500结果分开。已有边界/生成算子、P32极端policy和sigma丢失继续未解决。

## 下一步：科学选择，不自动改变参数
不再重复725次前缀或补做相同观测，也不重做年度触界表。当前没有active Builder successor。
Reviewer建议Owner考虑一个独立Python单户诊断：对新捕获的安徽call725输入，只将rah从.09改为.07，其他外生/价格标量、网格、helper、a_bar、求解器及100步规则不变；按原算法重新生成该诊断价格下的原生初始化，复用本次保存的.09作为对照。它检验的是源生初始化在内的单户求解链对rah的敏感性，不是固定V0/l0下单步算子的纯效应，更不是一般均衡或校准采纳。
该推荐未获Owner批准、未发布exact task、没有调用预算。批准后在一份任务中写明输入绑定、实现/测试、单户有限执行及HJB/KFE有效性检查；不自动把生产ramax改成.07，不因KFE返回就宣称HJB收敛，不继承本次725-call预算。D1–D3仍未采纳。Results eligibility=FALSE。
