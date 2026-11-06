# B3输入、冻结网格身份及外部HA准入方案：输入采纳待Owner决定

DATE=2026-11-06
OWNER_CONTINUATION=可以请继续
STATUS=STATIC_INPUT_GRID_PLAN8_CHECKS_PASS__OWNER_INPUT_ADOPTION_PENDING
MODEL_PLAN_CANDIDATE=cd0c235fab990209e28a97a4cfa98a6c20b9279b
MODEL_PLAN_TREE=533f1191d4b6378deccc86d39d27518b7f3fa50a
UNCHANGED_HA_ENVIRONMENT_CODE_CANDIDATE=aa3fdc2574901d4aca33dc0c299f4db784741bf3
MODEL_PARENT=114c4808f4f129e21050fb322c1ee8343be07c67
GOVERNANCE_PARENT=3e71048da9430e884c1f1e09ef58503c57e44d65
CHECKS=8_PASS
GRID_GENERATIONS_PROJECT_IMPORTS_SCIENTIFIC_CALLS_REAL_WORKERS_NEW_GRANTS=ALL0
ACTUAL_GRID_SHA256=null
OWNER_INPUT_ADOPTED=FALSE
SCIENTIFIC_RUN_AUTHORIZED=FALSE
SUBAGENTS=0

## 输入候选已具体化，尚未采纳

建议下一次接线候选复用已关闭七入口观察中**生成于第1轮、进入第2轮的两省保存快照及当轮净工资，只选择来源A**。保留A/B上下文和完整进入快照，来源索引为0；不运行B、不提交部分省份为完整O2批次、不拿旧合成B家户量冒充真实HA返回。它是外层合成接线候选，不是实证省份、基准经济或稳态接受。

已把候选的rah/rb/rb_gap/Tt和净工资按保存值原样封存，未重算、裁切、舍入、补扣税或重标为首轮19。其利率与工资不同于旧首轮/诊断点位，不能自动继承既往数值可行性；原快照的convergent字段也不能当作新HA收敛标志。新输入是否采纳属于Owner科学取值决定，不由工程角色自行确定。本轮已提交这一明确问题，当前记录为待答复，不把继续工程当作HA运行许可。

完整候选值、两行进入快照、来源文件长度/SHA和本机定位只在LOCAL_ONLY私有决策稿中；不把原保存载荷放到GitHub。候选包SHA256为8ed0fb98445ed02debfee0a971e0c728dbd583f6cc323ccfba22406b8191b225。模型分支的机器计划只引用这个封存对象及其身份，未生成实际ProductionWageRecord、请求、模型参数或网格对象。

来源地输入仍走原ProductionWageRecord与保存观察伴随绑定；保持生成快照与进入快照区分、原语义/数值与同一record引用。历史生产者合同16项artifact及其source_bundle标签、旧9源角色证明、当前24文件消费者清单分别保留，不能为相等而重封旧hash。历史上下文名与旧grant同名不产生新授权；未来具体worker、完整消费者来源和实际网格另行绑定，原消费门仍拒绝。

## 冻结网格与身份方案

本轮只读原年度入口的既有构造式及其已封存参考，不执行旧年度runner或HA内部算法：

| 项目 | 静态锁定内容 |
| --- | --- |
| 实际类/轴 | exports中的MatlabFaithfulHJBGrid，b/a/z顺序，另含switch_matrix |
| b | 原np.linspace(-2,5,20) |
| a | 原np.linspace(0,10,20) |
| z | 原[0.8,1.3] |
| switch_matrix | 原[[-1/3,1/3],[1/3,-1/3]]构造式，未求值为新数组 |
| shape/节点 | 原20×20×2，共800格；不是旧初始化8格夹具 |
| 参数 | 原EconomicParams的8项值，与既有参考/年度构造逐项核对；无新取值 |
| controls | 原delta=1000、convergence_tolerance=1e-7、max_iterations=100、drift_tolerance=1e-12；只记录原控制，不作为新科学接受阈值 |
| 实际身份 | actual_grid_sha256和artifact均null，未构造、未授权构造，不以合成grid标签填充 |

当前休眠后端的网格摘要是b/a/z/switch_matrix各自的shape、dtype.str及tobytes(order='A')的SHA，再按原canonical格式汇总。未来BindingContext.grid_sha256必须来自实际原网格，不能复制fixture的grid_metadata_identity。保持原摘要算法与接口，不切换字节顺序、重排、转换或更改flags以追求某个hash。

另需在外部伴随回执中核同一轴对象、strides和原writeable/C/F flags；这些不在当前后端摘要字段中，本轮明确标为未安装，不能宣称现有hash已经覆盖。未来生成/绑定实际网格必须有明确适用范围，且原样传递各阶段，不修改任何HA算法、网格或数值控制。

## 外部准入与预算尚未完成

原初始化→HJB原成功标志→正式post送原KFE→原汇总→原外部AtTax重构→原回复的既有顺序保持，不以临时迭代算子替换post，不增加内部残差、行和、固定行、尺度或精度诊断。新回复仅可复制同次原五项家户量，保持每H单位；财政边界乘H与A1等既有决定不重开。

机器计划列出**待审预算骨架而非额度**：拟议1个worker/1个来源/120秒/每进程2GiB/Job2进程/必要时固定ver1次，零自动重试；原网格一次、初始化一次及至多800根、HJB一次且最多100原线性步、policy至多80000、原KFE/线性解/汇总/外部AtTax/回复各一次。原工资重跑、来源B、其它外层组件、GE/IRF/MATLAB和真实数据调用均0。墙钟/内存是拟议上限，不是本次HA测量或放行。

这些数字不是新controls，也不能把旧关闭预算或六阶段计数当新许可。有效回报函数在既有路径的重复调用总数及完整native子调用清单尚未列全，effective_illiquid_return_total_max仍null，call_inventory_complete/all_native_subcalls_covered/counts_enforced均FALSE。完整计数及保护必须在未来固定执行器上完成，不因填了表就视作完整可运行预算；不为预算整理解释或更改黑箱数值方法。

依次尚需：Owner采纳具体输入；实际冻结网格字节及外部对象/flags保护；同一输入记录的限定消费分支；完整消费者源码/环境/唯一worker绑定；外部执行器与完整计数；最后适用Owner对具体输入/源码/次数/资源/STOP的科学运行决定。当前原公开入口和工资门均未放行，没有可执行HA许可或新worker。

## 8项检查、身份与保留

8项标准库静态检查通过，未导入项目或NumPy/SciPy：24源码及4个精确参考文件长度/SHA；年度网格/参数/controls的AST及字面值一致；实际grid hash保持null、原摘要与未来伴随字段分列；候选原值/完整快照及来源pin一致；生产者/消费者范围分列；预算未完整/未执行；全部科学/运行资格保持FALSE。检查针对来源和方案的一致性，不是数值或模型验证。

首次静态编制误用旧合同字段名，在计划写入前遇KeyError；已按其真实artifacts字段读取16项身份，原已封存候选未覆盖、错误回执保留。工程自审另补明有效回报/native计数尚未完整，修正机器计划后8项复核通过。主代理自审不称独立科学审查。

| 新本地路径 | Git Blob | 字节 | SHA256 |
| --- | --- | ---: | --- |
| validators/multi_province/outer_ha_input_grid_plan_20261106/plan.json | b86ccc99afa894ec123e6c2876f0394d6618c7aa | 7238 | d00c846426e63f41f16b649b08e4d9ff522c5fc531df9f5ec12ca07ea9cf5fc6 |
| tests/test_outer_ha_input_grid_plan.py | cd4b91d7e2e86057944e5e4b7a8d144b754ba3ef | 9651 | 724fe4cab0e20ec1fd435365598c7d03469385b999a12c79a46d8a2763615d69 |

只有机器计划和静态检查两个新本地路径，原生产/HA/网格源码、V2执行器及合同不改。V2上轮14份执行交接、5份真实输出、已消费决定和6份缓存逐件长度/SHA保持，新缓存0；不重做成功环境检查。代码/测试/私有候选仅本地，GitHub只同步脱敏治理文档，API写入0、模型代码不推、不合并main。

TEMP31 7/7、Moll 3/3、七入口1/1、工资/补录、旧四项无模型及V2 1/1均关闭，零自动重试；旧初始化余额仅原8格、不跨借。strict reference/thresholds仍null，科学接受、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE。R12 STOP、R13未授权、WASM六路径STOP、保护重绑定未授权及16项义务保持；历史dirty树/原件/缓存/证据不移动或清理，无reset/stash/clean、强推、删分支或全局配置修改。

下一步先等Owner对已封存输入候选作出科学选择，再推进相应实际网格身份和外部准入工程；输入选择本身不授权网格生成、HA运行或发放额度。前置：[V2环境1/1关闭结果](CH5_B3_ENVIRONMENT_V2_SINGLE_CHECK_RESULT_20261106.md)。当前：[路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)、[任务清单](../tasks/todo.md)。
