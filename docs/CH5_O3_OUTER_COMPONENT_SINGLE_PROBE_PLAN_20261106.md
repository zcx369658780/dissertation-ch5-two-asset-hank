# O3原外层组件单次有限验证方案与准备完成记录

DATE=2026-11-06
STATUS=PREPARATION_ENGINEERING_COMPLETE__OWNER_NEW_PROBE_DECISION_PENDING
PROPOSED_GRANT=CH5_O3_OUTER_COMPONENT_SINGLE_PROBE_20261106
OWNER_APPROVAL=NOT_RECEIVED
REAL_WORKER_LAUNCHES=0
ORIGINAL_COMPONENT_CALLS=0
HA_HJB_KFE_CALLS=0
NEW_SCIENTIFIC_GRANTS_ISSUED=0
AUTO_NEXT=FALSE

## 目的与当前完成项

下一步用固定两省合成输入观察原外层组件的真实返回，并检查它们能否交给已完成的一轮拼装接口。此次准备不是再建预给定包装层：已写出实际调用六个原组件入口的执行器，但该分支尚未执行。完整HA（HJB、KFE、原汇总）仍按Owner决定作为引用Kaplan、Moll和Violante（2018）的不可变黑箱；不研究其内部算法，不调用它。

本轮Owner“请继续”承接的是上一交付列明的有限实调用方案准备；不将它扩大解释为新科学运行许可。现有21项标准库工程检查和只读文件身份核对通过，均不导入原科学模块、不启动真实worker或只读ver子进程。准备代码只作主代理自审，不称独立科学审查。

## 具体一次性范围（拟议，未授权）

一个Python3.11验证子进程，30秒父进程超时，固定两省A/B，一次尝试，零自动重试。启动前先登记独占ATTEMPT_CLAIM；启动失败、超时、计数不符、非有限结果、来源/路径保护拒绝或其它异常均关闭该次尝试，保留完整失败与部分日志，不换目录或改名续跑。

| 固定原入口 | 上限/完整观察要求 |
| --- | ---: |
| temp31_worksite_tax.reconstruct_temp31_worksite_labor | 1 |
| capital_allocation.allocate_productive_capital | 1 |
| firm.evaluate_firm | 2（每省1） |
| wage.composite_household_wages | 1 |
| monetary.taylor_assignment | 1 |
| fiscal_diagnostics.national_fiscal_diagnostics | 1 |
| 合计 | 7 |

允许这些入口自身的原私有辅助函数、数据类构造/校验与既有外层工程账项工作；7不是全部Python函数调用数。未包装入口、额外公开科学入口或超额进入立即停止。每次分别记录调用尝试、原源码函数进入和成功返回，参数及结果只保留LOCAL_ONLY。

HA/HJB/KFE/原HA汇总、初始化、Brent/root、MATLAB、O2原批次工厂、旧年度runner、外层控制/迭代、GE、IRF、政策运行均0。家户Ct/Lt/At/Bt/AtTax仍为明确合成的预给定量。本次即使捕获成功，也只证明这组固定输入下的外层组件观察及接口交接，不证明真实家户批次、真实31省生产链或均衡成立。

NumPy依赖如果需要，可额外执行至多1次固定Windows系统cmd.exe /c "ver"只读版本查询；不计入7次原组件入口，但计入独立ver上限。其它命令、回退命令、子进程和网络动作拒绝。此前只读版本查询被误拦的工程背景不构成旧额度重试资格；该例外必须包含在新Owner许可中。

## 固定合成输入

| 项目 | A | B |
| --- | ---: | ---: |
| 家庭规模H（原状态N） | 4 | 8 |
| 来源地居民就业份额p（同H分母） | .5 | .25 |
| 企业规模E=pH | 2 | 2 |
| 预给定Ct | 1 | 2 |
| 预给定家户Lt | .5 | 1 |
| 预给定At / Bt | 2 / 1 | 3 / 2 |
| 预给定家户AtTax | .25 | -.5 |
| 目的地tau / 家户Tt | .25 / .5 | .5 / 1 |
| 进入轮wjt / ra | 1 / .1 | 1.5 / .2 |
| inter_prv_ratio / GovInv | .2 / 1 | .3 / 2 |
| Yt / Zt / Zt_1 | 9 / 2 / 2 | 10 / 3 / 3 |
| alpha / Kt / Kt_prev | .3 / 7 / 7 | .35 / 10 / 10 |
| 状态Lt / 状态Lt_prev | 4 / 4 | 5 / 5 |

共同状态：pit=pit_1=.02、rah=.09、rb=.02、rb_gap=.07、w=19、rk=.5、corptau=.2、ramin=.02、ramax=.09、wjtmin=.8、wjtmax=1.3；进入状态AtTax=0，企业实际输入按合成家户AtTax覆盖。

共同参数：ga=2、phi_l=5、alphal=1、epsilon=10、theta=100、delta=.025、istar=.015、rho_pi=1.25、totalpit=.02、epsilon_pi=0。phi按目的地行/来源地列为[[1,2],[3,1]]，sigma为[[0,.1],[.2,0]]。这些是验证夹具，不是现实校准/观测或Owner科学采纳；未以原组件试算筛选输入或预填结果。

劳动原核按H计算一次，再由已采纳A1接口按来源列乘p一次；资本、消费、资产和家户财政继续使用H。工资税按目的地tau×当轮原企业输出gross工资（原裁切）×A1目的地劳动，不再乘H/p；财政Tt/AtTax分别乘同源H一次。保留原企业旧Govinc对照，外层金额账以已采纳子账组合。

**Lt_prev限制**：执行器保留原一轮对企业的Lt_prev=当轮家户Lt输入映射，不用进入状态的Lt_prev替换；只记录，不自行修正其经济含义或宣告该语义合格。这组组件调用不解决家户收入/劳动激励兼容、R/P收入共享、sigma是否财政收入等未采纳事项。

## 来源锁定、运行门与保护

MODEL_CODE_CANDIDATE=848feafec5e7e01ff96c38251e3f0ef4a44b91f0
MODEL_CODE_PARENT=434d32159920bf796e5f0e95f33a18862264afd1
MODEL_CODE_TREE=b620da06301dc17a1c66b3051fe1ef44c0ec04b5
MODEL_CODE_PUBLICATION=LOCAL_ONLY_NOT_PUSHED
CONTRACT_SHA256=9a5666380e50d3074059276592464236e0f9b1014592b0f0fa15b4724d7e48f4
WORKER_SHA256=e516e05284bef83b899ee3a40763ca765b7d82e25b77a6ed67b8496d8c5048cc
FIXTURE_SHA256=7fa51c0ba111fb57ac5fd204e7877dfd66a63856f3aedd02cad92dea87c1be3a

新增代码路径仅validators/multi_province/outer_component_probe_20261106/下run.py、fixture.json、contract.json及tests/test_outer_component_probe_contract.py。原源码修改0。contract永久保留PROPOSED_NOT_AUTHORIZED；未来如获具体批准，主代理将Owner真实原话和全部合同/执行器/夹具哈希及次数写入单独OWNER_DECISION，而非把方案状态当许可。未获批准时不创建正式grant目录或填写批准；测试中的模拟批准明确标识MOCK_ONLY，放在独立准备回执目录，不能用于真实执行。

正式运行位置固定在模型工作树同级、独立LOCAL_ONLY的本次grant目录；完整绝对定位仅私有回执保留。父进程独占claim后才能启动唯一child；child复核批准、父PID与claim，并独占登记worker entry，禁止绕过父进程直接续跑。已存在证据不覆盖。参数/原结果/候选状态/stdout/stderr/trace/最终回执均LOCAL_ONLY。

原模块只通过固定私有命名空间按锁定物理字节编译加载，不AST改写；禁止加载普通项目包或未列模块。Python审计拒绝项目未锁定文件读取、私有grant之外写入、删除/移动/切换目录、网络和额外子进程；路径任一祖先出现reparse/symlink则停止。父进程复核退出码、三类trace的精确7次、trace哈希和资格FALSE；缺失证据或未知计数不升级成功。

这仅是Python审计/profile与父进程超时保护，**不是OS级隔离、内存硬限额或GLOBAL_STOP认证**；native扩展行为及系统依赖不由Python审计完全覆盖。未认证的保护事项仍保持原状态，不借本次关闭16项义务。Python3.11要求及本地依赖影响保留为运行限制，依赖异常同样消耗该唯一尝试。

以下为运行器实际读取的16份物理文件锁定，不混同Git规范化Blob哈希；若换行/字节或路径改变，先停止并重新审阅具体方案，不能偷偷重封锁定后沿用批准。contract本身由上述CONTRACT_SHA256绑定，不放入自身manifest以避免循环。source_bundle_identity为此14模块集合的元数据身份，不冒称旧SourceBundleReceipt已运行；grid标识明确是合成元数据，未构建或修改HA网格。

| 相对路径 | 物理字节数 | SHA256 |
| --- | ---: | --- |
| src/ch5_two_asset_hank/multi_province/capital_allocation.py | 4233 | 8fd00e62b002e7a254a883a3786af7738972b79acc0ec0b05c795786565fecb2 |
| src/ch5_two_asset_hank/multi_province/firm.py | 4505 | f0aea719a4121f5562aaa9ccf3f219cc8afd6c51f84cc2f64a2fe486cef7fb69 |
| src/ch5_two_asset_hank/multi_province/fiscal_diagnostics.py | 1723 | d1ce633ee68cab1ecee88c546842a59521c2ad5cbffbd03be138561ccac12af6 |
| src/ch5_two_asset_hank/multi_province/monetary.py | 820 | 3aacb8046a27c80e9da8c1bdf5974e2efae3450fbc4eec7087651f88a5474ed5 |
| src/ch5_two_asset_hank/multi_province/outer_a1_scale.py | 8577 | 89a79b74c2b826d87058cdd4cfdf14a93d8bcf6ce2be1bd23fba2cb535b3fbd9 |
| src/ch5_two_asset_hank/multi_province/outer_fiscal_ledger.py | 7910 | 0f76d16706962e0d94497aa6db89b8b90ef1b75b7b230caf90aaeb34e0a513b2 |
| src/ch5_two_asset_hank/multi_province/outer_household_fiscal.py | 5450 | 672835896399a52829b1d3da3c94888fe2bef5e923559b44d1619ca4d8c4f515 |
| src/ch5_two_asset_hank/multi_province/outer_one_turn.py | 15993 | 0f5c5426b454a18bbf550150433d8bfcabb0f0914753cef6ff3dacfd60fe6632 |
| src/ch5_two_asset_hank/multi_province/outer_payroll_tax.py | 4863 | c04c361330f4d734a8e70f36d4f9539ffaab4accb9e556cb497f4e18b34e6ea2 |
| src/ch5_two_asset_hank/multi_province/outer_production_wage_bridge.py | 5769 | 3038df68e147d9826649cdf16b4f0ea5cba2de5251b6054ed68e245fcbdc06ad |
| src/ch5_two_asset_hank/multi_province/temp31_binding_skeleton.py | 8549 | 2e91f6a34a027f788d6d13524fabc5db71bdeac44b11de3df7afbe01d09fd523 |
| src/ch5_two_asset_hank/multi_province/temp31_wage_evidence_preflight.py | 23915 | 5278075702c0bf93f750ab858d438e5f0e5c6bd5d31eea4380f6ce36cd629fa6 |
| src/ch5_two_asset_hank/multi_province/temp31_worksite_tax.py | 10435 | 7cd0ec0e6038468f1d14ea52b3746e8f80f1613a9c3bd0d754f89dab74bb7571 |
| src/ch5_two_asset_hank/multi_province/wage.py | 3004 | 12393521821b5a7616eec8f19bcd4a10cbb2da37e0a87fcb5c5b4128a0c98dbe |
| validators/multi_province/outer_component_probe_20261106/fixture.json | 1466 | 7fa51c0ba111fb57ac5fd204e7877dfd66a63856f3aedd02cad92dea87c1be3a |
| validators/multi_province/outer_component_probe_20261106/run.py | 25587 | e516e05284bef83b899ee3a40763ca765b7d82e25b77a6ed67b8496d8c5048cc |

## 已执行的限定工程检查

21项全部通过：合同限额/类型/白名单拒绝、根与文件pin错配、未批准父/子不占额度或启动、逐项Owner记录匹配、证据独占不覆盖、模拟超时/非零/缺证/启动失败各仅一次、伪成功缺trace拒绝、父PID拒绝、网络/shell/写/删/未锁定读取拒绝、ver上限与命令注入拒绝、未列项目模块拒绝、人工函数计数/超额/非包装入口/错误身份、类定义与额外公开函数区分、重复JSON/非有限值拒绝、显式合成p、固定调用清单AST及reparse祖先拒绝。

`python -B validators/multi_province/outer_component_probe_20261106/run.py --check-plan`返回PLAN_PINS_MATCH_NOT_AUTHORIZED_NOT_RUN。该命令只读取身份，不是试跑。测试仅标准库与mock，模拟进程从未启动真实子进程；旧6份缓存字节/SHA256保持、新缓存0、原科学源码变化0；既有完成测试未整套重跑。测试/保护与同步回执私有保存。

## 下一决定与保留门

准备交付和GitHub回读完成后，请Owner只决定是否授权本方案的独立1次、30秒、7原入口和至多1次只读ver查询。回答前不执行。获批后也不自动进入第二轮、HA、31省、校准或GE；失败零重试，后继仍须对应新决定。TEMP31 7/7、Moll 3/3、工资/补录关闭；旧初始化余量仅原8格，均不借用。

strict reference/thresholds仍null；科学接受、FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、Results、model_activation、REAL_GE均FALSE。R12 STOP、R13未授权、WASM六路径STOP、保护重绑定未授权、历史dirty树及其HEAD/index/porcelain、16项义务保持。不reset/stash/clean、强推、合并main、删分支、移动证据/缓存或修改Desktop/CUA/全局配置。GitHub只同步本方案与当前治理入口，不上传模型代码或LOCAL_ONLY载荷，API写入0。

前置：[预给定一轮拼装](CH5_O3_SUPPLIED_ONE_TURN_ASSEMBLY_20261105.md)。当前入口：[路线图](CH5_MULTIPROVINCE_HANK_ROADMAP_CURRENT.md)、[任务清单](../tasks/todo.md)。最终治理提交及远端逐文件Blob/字节/SHA256核对以本次私有交付回执为准，提交前不预称已同步。
