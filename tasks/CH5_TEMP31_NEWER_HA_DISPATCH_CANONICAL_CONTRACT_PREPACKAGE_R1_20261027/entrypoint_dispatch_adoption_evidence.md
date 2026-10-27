# 启动/调度/运行记录的分层证据

| 路线候选 | 命令/调用源码（未执行） | (1)代码声明 | (2)现存运行清单 | (3)Owner本轮批准 | (4)执行结果 |
| --- | --- | --- | --- | --- | --- |
| MP4C batch | BATCH:146–149 CLI参数data-root/runtime-cache/output-root/workers/years/owner-a-inputs；43–45 subprocess指向年度worker | PROVEN_STATIC | 输出root为CLI变量；没有可认证实际batch_manifest.json完整相对路径 | 未选TEMP31正式启动、year或representation | NOT_RUN |
| 年度worker | WORKER:205–209 runtime_input/runtime_cache/output_root；24–30导入validation anchor/empirical/cache/Owner-A/controller；167–187回调到OnlineStationaryInputs | PROVEN_STATIC，不凭production标题升格 | run_manifest.json在root变量下写；本轮未有实际run_root可读见证 | UNKNOWN | NOT_RUN |
| primary canonical准备 | EMPIRICAL:309–319的prepare选项→74–105 prepare_canonical→ANNUAL生成器 | PROVEN_STATIC，import anchor仍在前 | 无实际输出目录/生成清单原件 | UNKNOWN | NOT_RUN，未生成JSON |
| validation anchor | ENTRY:16–36、64–75旧raw pin守卫/HA imports | VALIDATION_ONLY | 不构造伪运行凭据 | 不是TEMP31正式采纳入口 | NOT_RUN |

新实际只读见证：BATCH:98准确引用的validators/multi_province/matlab_persistence_contract.json可读，schema=CH5_MP4C_MATLAB_PERSISTENCE_CONTRACT_V1，audit_mode=READ_ONLY_ZERO_SCIENCE。它声明保护MATLAB runtime cache SHA、legacy writer/consumer、checkpoint兼容边界；**是一份持久化来源合同，不是带Owner本次批准时间、源码版本、TEMP31工作地税采纳和实际启动结果的run manifest。** 私有logical_root/physical_root/root_relationship只作脱敏字段存在记录，不跟随绝对路径。

静态调用可组合为batch→worker→anchor raw hash guard→局部solve_batch→callback/controller；RUNTIME:35–56取得entering state并调用household_solver。guard位于worker/empirical的anchor导入路线上，不通过import证明可执行。BATCH:49–60物化runtime cache/Owner-A，WORKER:145–157分representation消费；CLI定义、写manifest表达式、SOURCE_CONVERGED标签都不代替实际运行记录/Owner采纳。

最多两层新增定位，精确源码14个版本化对象；除了准确引用的合同文件，没有实际approved output_root路径，不搜索任何目录寻找同名batch_manifest/run_manifest。距离原件在精确相对路径缺失即早停；本报告不宣称整个仓库无启动配置/输入，也不从旧历史会话寻找证据。
