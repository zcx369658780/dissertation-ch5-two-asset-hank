# K1B R2 未达标后的 rolling 与批处理零科学调用规格

任务 `CH5_K1B_POST_R2_ROLLING_BATCH_ZERO_SCIENCE_SPEC_20260925`；Owner 已选 B，**只授权设计**。起始 HEAD `0639a15544b5ed186bc6d609f0efab8345b6a0ae` 是派发基线 `d6ee4e044782226e3f7f6f0a8bdf85ef35680b8f` 的已提交后代；`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。此前已采纳的两轮额度已耗尽，C6→C7 为 2/9、C7→C8 为 5/9，终态 `VALID__LEVEL_NOT_MET_AT_BUDGET`。本规格不追溯改判，也不授权 turn9、任何科学/模型调用或 runner 实现。Results eligibility：`FALSE`。

## 拟议起点与 rolling 规则

拟议起点是已独立验收的合法 C8；进入 turn9 的输入/方案已封存并读回，但**turn9 尚未运行**。C8 的完整输出清单为 `reports/ch5_k1b_turn8_outer_r2_20260925_run001/execution_artifact_manifest.json`，SHA-256 `5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`。同根的 `turn9_k1b_input_candidate.json` 为 `FBB18A5B8B4FD94F337510DBB4E62F94188C27863EED1F79FE2E1A71B5BC39AB`，`turn9_k1b_frozen_share_payoff_plan.npz` 为 `E7E6AF79864F67A28386ECF8BEB3B71C6080E9A6C6E64F4CBA8125E1C19D34DD`，四项输入清单 `turn9_entering_bundle_manifest.json` 为 `40200B60729A5B4173E24661843980851F8610A9FA2186F7E411B7FE9E5CDC65`，读回收据 `turn9_entering_bundle_readback.json` 为 `E428D105600D091979B526ADD6BF61E0FC294050B9FAB97FE8B87A29A1012F85` 且 `status=PASS`、`bad_paths=[]`。这些载体足以描述拟议起点；真正执行前仍须新任务重核每一项身份。

拟议规则 `PROPOSED_NOT_ADOPTED`：起始 C8 的 rolling 计数为 `0`。只有一个新 turn 完成 31/31 接受的 HJB/KFE、恰好一次源忠实集成、当轮 raw `ra0`、封存并读回下一轮输入/方案后，才形成合法 `C_n`；随后比较 `C_(n-1)→C_n`。八个 31 省向量为 `Yt,Lt,wjt,rk,Kt_prev,w,raw_ra0_n,rah_(n+1)`，矩阵为目的地×来源地的 31×31 `S_(n+1)`。`Yt,Lt,wjt,w` 用 `max_i abs(new_i/old_i-1)`，旧分母须有限非零；`Kt_prev` 用 `max_i abs(new_i-old_i)/Kt0_i`，冻结的 `Kt0_i` 须正且同一；`rk,raw_ra0,rah,S` 用相应元素最大绝对差。全部九项须分别严格 `<1e-6`。

合法比较若九项全过，计数加 1；若任一项未过，计数归零并记录完整差值。这种合法未过不是求解失败或发散。计数从 1 到 2 的第二个**连续新比较**完成后，立即停在候选 `CRITERION_MET_FOR_BOUNDED_K1B_MAP_ONLY__INDEPENDENT_REVIEW_PENDING`。因此从 C8 起至少需要 C8→C9、C9→C10 两个新比较才可能达到候选终态；C7→C8 及更早读数不进入新计数。身份、分母、轴/形状、有限性、账本、科学内层、封存或读回有缺陷时，不更新计数，保存最早原始内层终态与位置并全局停止。任何完整合法 turn 到达既定窗口上限仍不足两次连续全过，终态为 `VALID__LEVEL_NOT_MET_AT_BUDGET`（一个通过则另记未确认的单次通过）；中途超额或超时导致检查点不完整时是失败终态，不冒充合法阈值未达标。提前成功、首失败和到预算上限均立即停止。

这一 prospective rolling 两次通过是**新的实质停止法**，须 GPT Work 独立审查后由 Owner 明确采纳。它不改变冻结经济与求解对象、31 省顺序、20×20×2 F-order 网格、HJB/KFE、源忠实 labor、原始 `ra0` 滞后收益、同一 destination-by-origin `S`、严格九项阈值。Clipped-`ra` 上界命中按现行准则只报告；原 MATLAB 零命中判据单独列示，不能因新准则通过而视为通过。即使候选数值准则通过，也不是数学固定点、稳态、GE、原 MATLAB predicate 或论文 Results。

## 有限窗口与成本：仅供 Owner 决定

**最小可解释窗口提案为从 C8 最多两个新完整 turn**，因为计数从零开始而两次新合法相邻比较至少需要 C9 和 C10。这个 `N=2` 是观察两次通过的最小逻辑长度与较小的风险敞口，**不是**根据已有下降读数推断的达标概率或足够轮数；窗口结束未过即报告有界未达标，不自动接续。可以逐 turn 派发并审查，或仅在单独验收 runner 后一次启动跑至两轮上限。两者科学调用的逐类上限相同；后者减少一次中间 Work/Codex 交接，但失去逐 turn 独立验收的机会。先以两个 turn 为一阶段、阶段末再决定是否重新设计，优于无依据地把窗口直接扩大。10/20-turn 一次启动只作比较例子：最大外层次数为拟议短窗口的 5/10 倍，逐类累计尝试上限若简单扩展也为 5/10 倍；上下文交接可能由约 10/20 次降为一次启动加最终审查，但模型调用与算力不减少，缺陷可在多轮后才接受独立检查。10/20 **不是提案预算或预测**。

接受的 C7/C8 封存账本显示：每轮各 31 次原生初始化、24,800 次 labor root 尝试、409 次 policy map/D2、327,200 次 selector evaluation、378 次 HJB update、31 次 terminal KFE、一次 household batch/集成、31 次 firm；selector roots 分别为 141,129 与 141,125，alpha candidates 均为 382。两轮实数相加为 62、49,600、818、654,400、756、62、2、62；selector roots 共 282,254。这些是**已观察成本**，不是未来期望值或新上限。未在接受的执行报告/收据中找到以秒计的 turn7/turn8 实测 wall/CPU 时间；文件时间戳不能代替运行时长。因此未来窗口的具体总 wall-clock、CPU/GPU 时间与货币成本上限均为 `UNRESOLVED`。不可据此声称短窗口会在某时限内完成。最小 Owner 决策是：是否原则上采纳从 C8 开始的两次连续新通过与 `N=2` 窗口；并在**执行批准前**要求一个可信的运行时长来源及独立给定的硬超时值 `T_owner`。该值未定时不得启动；硬超时先于下一操作检查，超时终态 `FAIL__OUTER_INCOMPLETE_CHECKPOINT__TIMEOUT`，保留已封存的前一完整检查点和全部已尝试调用账本。

下表是旧已采纳单轮上限的**未来两轮候选复制**，不是重开旧预算。逐省栏为每省每 turn 上限；合计为 `2×单轮`。表中实际 C7/C8 只提供成本参照，不证明新 turn 的用量相同。科学调用包括失败尝试；不得省际借额。`—` 表示该类只有整轮操作，不拆成逐省调用。完整机器表及同名源码类别在收据中。

| 类别 | 每省/turn | 单轮 | 两轮候选合计 |
|---|---:|---:|---:|
| 原生初始化 | 1 | 31 | 62 |
| labor roots 尝试/返回，各自 | 800 | 24,800 | 49,600 |
| policy maps、D2/Q，各自 | 51 | 1,581 | 3,162 |
| selector evaluations | 40,800 | 1,264,800 | 2,529,600 |
| selector root invocations（全部子类共用） | 20,000,000 | 620,000,000 | 1,240,000,000 |
| direct HJB updates、post-update checkpoints、relaxation helpers，各自 | 50 | 1,550 | 3,100 |
| alpha arithmetic candidates | 2,650 | 82,150 | 164,300 |
| terminal KFE attempts、SCC、restricted GESVD、normalized candidate、full-Q、aggregates、firm，各自 | 1 | 31 | 62 |
| household batch、source-faithful labor、frozen K1B allocation/feedback 同一事件、C1 GovInv、wage、monetary、fiscal、raw `ra0`、next preparation、same-S payoff、full integration，各自 | — | 1 | 2 |
| full-space GESVD、retry、solver substitution、K2/GE/MATLAB/Results | 0 | 0 | 0 |

原表的“turn8 后 household=0”属于**已耗尽的旧窗口**；本候选若经 Owner 采纳，须由新任务明确替换为新窗口 C9/C10 各最多一次、C10 后为零，而不能把旧预算挪用。`k1b_feedback_calls` 仅是 frozen K1B allocation 同一事件的账本别名，不能额外调用。`terminal_kfe_attempts` 一省一 turn 最多一次；selector root 子类共享 20,000,000/省，不叠加额度。对无独立逐省语义的整轮类别，逐省上限标 `—` 并以单轮 `1` 限制。

## 未来单启动 runner 的设计契约

1. **零调用前检**：在每次操作前核验任务指定 HEAD/源码树、runner 和 helper 哈希、封存起点及四项输入、31 省顺序、网格/轴、正 `Kt0` 与非零旧分母、输入读回、输出根唯一拥有权；拒绝任何已有、链接、重定向或不能独占的目标。固定逐项预算与 `T_owner`，确认本任务没有旧额度借用。
2. **逐 turn 计数**：调用入口先记尝试（失败也计），按每省、每 turn、整个窗口同时阻挡越界；记录每一类别、精确省份和最早原始终态。逐省 HJB 的内部迭代仍按既有法则；31/31 HJB/KFE 通过后才允许一次集成、31 firm、下一输入准备，且 raw `ra0_n` 只能影响下一 turn。
3. **原子封存**：完整 per-turn 输出及清单写至本 turn 独占临时位置，原子发布为不可变 checkpoint，再由独立读回过程逐项核对路径集合、字节数、SHA-256、31 个 terminal、账本和候选/方案。读回失败不得进入比较或下一 turn；旧完整 checkpoint 原样保留。
4. **比较与停机**：合法检查点与前一合法检查点计算九差，更新 rolling 计数；首个身份、经济/数值内层、预算、封存/读回或超时失败立即停，早达连续两次全过立即停，到两轮上限未过也立即停。所有终态都包含精确 attempted ledger 与原始最早失败位置。零重试、零恢复、零 warm start、零借额、零自动调节阈值/阻尼/求解器/校准/方程。
5. **崩溃与所有权**：崩溃后只能信任已原子封存且独立读回的完整前一 checkpoint；未完成的临时输出和可能未落盘的尝试账本标 `CALL_LEDGER_UNRESOLVED`，不能声称未尝试或直接续跑。输出根所有权丢失时停止并保留现场；新授权与独立核账前不得恢复。批次终止后 GPT Work 必须逐 turn 独立审核哈希、合法性、账本与 rolling 判定；runner 自判不是验收。

**未来零科学前检/测试计划（本任务不实现）**：静态解析 runner 与任务参数；用隔离的合成小账本检查严格小于、计数加一/归零、早停、首失败、超时、每省与累计越界、失败尝试记账及 output-root 拒绝；用合成封存样本检查原子发布/读回和崩溃恢复分类。任何测试不得导入或执行真实模型、HJB/KFE、integration、firm 或 `--execute`；需另发精确路径任务。通过合成测试不构成科学调用批准。

**后续执行任务模板，尚未填定/授权**：Owner 采纳文号；独立 runner 审查；起点 C8 完整清单及进入 turn9 四项哈希；冻结 HEAD/src/runner/helper、31 省与输入身份；新的输出根及独占策略；rolling 规则版本；`N=2` 或另经采纳的最大窗口；收据内每类逐省/单轮/累计额度；`T_owner` 与 CPU/GPU/算力预算及监测时钟；入口计数覆盖；原子封存/独立读回；所有终态及失败账本；零重试/零恢复；独立 Work 审查门。任一字段未定，任务不能进入科学执行。

来源文件的逐项 SHA-256 和全零本任务账本见机器收据。首阻断：无身份或载体缺失；**运行时长与时间上限依据未解决**，故不存在可执行的完整预算。后续先由 GPT Work 独立 ACCEPT/REJECT 本设计，再请 Owner 采纳或修改 stopping law、有限窗口与完整时间/调用上限。Results eligibility 始终 `FALSE`。
