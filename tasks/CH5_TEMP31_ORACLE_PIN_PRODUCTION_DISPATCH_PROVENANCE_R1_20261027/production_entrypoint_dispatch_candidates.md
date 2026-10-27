# Production dispatch候选

新增真实源码调用表达式，无实际部署/运行证明。ACTUAL_PRODUCTION=UNKNOWN；Owner当前TEMP31采纳路线仍BLOCKED。

| 来源 | 已证角色与调用 | 限制 |
| --- | --- | --- |
| LOCAL_ENTRY:1,64–75,336–350,370–372 | validation-only；顶层bootstrap先于HA imports；callback/controller传递 | 历史validator，不称生产 |
| LOCAL_BATCH:1,15–18,43–45,146–149 | 自称Owner-run scheduler；明确subprocess调用年度worker，含CLI | 真实静态caller，不是Owner当前采纳证明 |
| LOCAL_PRODUCTION:1,24–30,145–161,167–187,205–209 | 自称production worker；导入anchor；分representation；callback传controller；CLI | production标签不是部署身份 |
| LOCAL_EMPIRICAL:19–31,86–104,309–324 | 导入anchor/annual生成器；prepare_canonical实际静态调用；CLI派发 | 定位历史年度生成/消费入口，不认证当前采用 |
| corrected_diagnostic/optionb_turn2_household_integration.py | 固定前轮独立审阅已确认原1–5行opt-in且不改默认生产 | 本轮不重读原件，INHERITED_OPT_IN，不升格生产 |
| R2/R3和D1/D2/D3 | 隔离补丁/目标合同 | 未合并、未生产闭包 |

静态链：BATCH.launch_year→subprocess(PRODUCTION)；PRODUCTION顶层→ENTRY anchor→raw bootstrap guard；PRODUCTION.run_year→局部solve_batch→anchor.postloop→HA；LOCAL_RUNTIME:50–56消费callback。PRODUCTION与EMPIRICAL导入同一anchor，guard仍位于该静态导入路线；未执行import，不能称实际runtime报错。

从任务已知ENTRY/ANNUAL和同级精确目录定位候选；PRODUCTION→EMPIRICAL→ANNUAL最多跟随两层，BATCH为独立定位的直接caller。已知POSTLOOP/RUNTIME为任务锚点。组合跨锚点静态链不表示无限新增追踪；无全仓/全历史/会话JSONL/私人目录搜索。只有16次源码读取，余2次预留终核ENTRY/ORACLE，来源发现已关闭。

仍缺Owner采纳入口命令/配置、准确版本、真实canonical生成与输入原件、已批准TEMP31 adapter。没有这些不运行候选来制造证明。
