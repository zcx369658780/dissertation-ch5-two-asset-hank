# C8 同冻结输入过程级测时执行报告

任务 CH5_K1B_TURN8_SAME_FROZEN_TIMING_MEASUREMENT_EXECUTION；签发 HEAD d017ab1a6e6c44c7272cb4fb0571bf90909769b5。Owner 授权的唯一执行 ID 为 CH5_C8_TIMING_MEASUREMENT_RUN001_20260926。本报告只是 Builder 对**一次**已执行尝试的证据记录，等待 GPT Work 独立审查；不自我接受科学结果或启动后续任务。

## 过程结论

精确命令从唯一工作树调用一次：python -B validators/multi_province/k1b_turn8_same_frozen_timing_measurement/run.py --repository D:\ProjectTemp\c5k1bturn56 --execute --execution-id CH5_C8_TIMING_MEASUREMENT_RUN001_20260926。进程退出码 0；无第二次执行、无重试、无失败尝试。wrapper 分类为 COMPLETE_OBSERVED_ELAPSED_SAMPLE_ONLY；原 C8 delegate 数值终态与计时收据的 terminal 均为 VALID__LEVEL_NOT_MET_AT_BUDGET。这是完成的过程耗时观察，不是九分量收敛、固定点或 Results 判定。

单调钟 timed-action 起点 9261390000000 ns（2026-09-26T09:23:48.606750+08:00）；科学动作结束 12610437000000 ns；科学封存及独立读回结束 12643593000000 ns（2026-09-26T10:20:10.812028+08:00）。完整过程 elapsed_ns = 3382203000000，即 3382.203 秒，包含科学动作及封存读回；未被删失。它低于 43,200 秒协作资源墙，但资源墙仍只是风险限额，不是可靠科学时长上界。该样本只对应本次 C8 同冻结输入、环境和负载。

## 输出、账本与封存

测量根 reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001 在启动前不存在，运行中由 wrapper 独占创建；结束后为非链接目录，timing_receipt.output_root 精确指向它。accepted wrapper 在封存前后执行 output ownership 检查。原受保护 C6-prime、C7、C8 三根保持只读，manifest SHA-256 仍分别为 7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61、413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91、5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301。

尝试调用账本已解析：39 类逐项与新封存 turn8_scientific_ledger.json 一致，且均不超过独立合同上限；五类显式逐省 guard 保持原合同值，guard_denied=[]。turn8 household calls=1，terminal KFE attempts=31，full integrations=1，scientific retries=0；没有 C9 household 调用。完整逐类 attempted 与 source ledger 在机器收据中保留。数值终端收据 call_ledger_resolved=true。

尝试日志共 3772 条；最后一条 attempt_journal_0003772.json 的事件为 integration_source_reconciled，其总 attempted 与计时收据一致，31 省逐省值均在五类合同 guard 内。最后日志 SHA-256 为 86F1C6F65320E93C14B7CDE00B0B8ADDD2C9E96B3D7F8E220CA552A5AAF77E53。

science_artifact_manifest.json 含 8913 条；Builder 逐条只读核对路径、大小、SHA-256，全部通过。science_artifact_readback.json 状态 PASS、bad_paths=[]，其 manifest_sha256 与清单文件 SHA-256 一致。计时收据按设计在封存读回后写出，单列其 SHA-256。关键输出身份：

- reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001/preflight.json — SHA-256 C13AA6597462823F00A31BF83C4719E653890C48ED40F8149AB90B5F8A811804
- reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001/turn8_scientific_ledger.json — SHA-256 33672A89CB854F35F74FFC8B0886B4A48361B2D6F171313595708721A707355D
- reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001/terminal_receipt.json — SHA-256 BEDC0BD2C6DA705B428607CC7CD008985E1E1C222E67E6DC02CB9B47DD09BDC2
- reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001/science_artifact_manifest.json — SHA-256 5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D
- reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001/science_artifact_readback.json — SHA-256 E7F6CC63AC53220E8FECD90DA2402312AC5EBBCD354431405BC4ADC3E73C2DFB
- reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001/timing_receipt.json — SHA-256 AAA86104814A4994083CD50E4B7A8C35792BBB29CD797F12E318AAB8745497F8

## 权限和下一门

授权输入、活动任务与副本、Owner 一次性执行采纳、合同、wrapper/delegate 身份均按任务单入口核对通过；来源哈希：

- TASK_CURRENT.md — SHA-256 7A6626204E595DD47BE8D61F3D03DFFCAF858E1B4B1319847A3EFA1FD3376CB9
- tasks/CH5_K1B_TURN8_SAME_FROZEN_TIMING_MEASUREMENT_EXECUTION.md — SHA-256 7A6626204E595DD47BE8D61F3D03DFFCAF858E1B4B1319847A3EFA1FD3376CB9
- docs/CH5_K1B_TURN8_SAME_FROZEN_TIMING_MEASUREMENT_OWNER_ADOPTION.md — SHA-256 1914E2FE0C6E21E0F767210E6ED55FB3092B1D19A6DC8A9E19821043527F7D1A
- tasks/CH5_K1B_TURN8_SAME_FROZEN_TIMING_MEASUREMENT_CONTRACT.json — SHA-256 64E0A111E6C8FC186DB58F188CF55159ADCD3BBF213EF1457EF5EA7AEB569CB5
- validators/multi_province/k1b_turn8_same_frozen_timing_measurement/run.py — SHA-256 8DFA49C1121EF41FA750844F4F5017779C3E381CFA2E7CBE19C7834D1F0EAB4A
- validators/multi_province/k1b_turn8_outer_r2/run.py — SHA-256 10920535BD50E688D1794B7E69C34F8A5C3C56456CAF6E8DF52FA8D9DFE31831
- reports/ch5_k1b_turn7_outer_r2_20260925_run001/turn8_entering_bundle_manifest.json — SHA-256 20861D4ADDBDF1099854EB86B00D24A097C627838B3F6EF5AFAEDABFFD647E5E
- reports/ch5_k1b_turn7_outer_r2_20260925_run001/turn8_entering_bundle_readback.json — SHA-256 5EB75667132473C2F283666B0F3B73BB18FDF00A83C09382827E4C44958246FA

本次完整样本的 c9_c10_upper_duration_bound=null，Results eligibility=false。一次 C8 观察不能自动建立 C9/C10 可信时长上界；预启动 BLOCKED__DURATION_BOUND_UNAVAILABLE 保持。首个未决门为 GPT Work 对本次过程证据与报告的独立 ACCEPT/REJECT；不得自我验收、重跑或派发 C9。
