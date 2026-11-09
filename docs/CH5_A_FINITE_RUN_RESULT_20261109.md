# A/0一次有限批准的实际结果与离线修复

日期：2026-11-09。终态：CLOSED_STOP_NO_AUTOMATIC_RETRY。

Owner对[精确审阅单](CH5_A_FINITE_RUN_REVIEW_20261109.md)答复“批准这一次有限试验（建议）”。真实决定和六项硬额度已保存；九项延期native限制保持null。以下是实际尝试结果，覆盖旧文档“全部批准仍null/原A仅PREPARED”的当前结论。

| 项目 | 实际观察 |
|---|---|
| 合同/清单 | e094a04b / 62abe2e8，原精确候选恢复后执行 |
| 次数 | 批准1，消费1，剩余0，自动重试0 |
| 最远阶段 | 固定预约、限域消费、worker请求和capsule预约完成，Win32创建前停止 |
| 停止原因 | RuntimeError:NO_SCIENCE_IN_PARENT_CONTROLLER；temp31_toy_supervisor._require被误判 |
| 实际工人/HA/子端bootstrap | 0 / 0 / 0；未创建进程，未有PID/创建时间/Job或环境实机资格 |
| 父端事件/控制通道 | 2 / 0字节；worker请求1，正常返回0 |
| 受控runtime IO | 建3文件、写1279字节、读2439字节；不含所有源读取/native IO的完整计量 |
| 首次工件 | 无origin、无worker_log；有291字节supervisor_log；原root/C/g未取得 |
| 审计/清理 | 四次原件核对无失败，1125封存文件执行前后保持；线程/管道无存活、清理通过 |
| 耗时 | 父端恢复、核对、尝试及收取合计48.75秒，不能当HA求解耗时 |

三次NumPy准备期只读版本子进程请求被拒绝，实际外部子进程0；kernel32后端加载0。顶层failure为null只是外层收取正常，内层lifecycle.failure明确保存停止原因，不能据此称执行成功。

原父端脚本只放行原系统装配_kernel，遗漏其首先调用的纯_require断言。代码图调用边及原源码一致，离线旧规则复现相同停止；因此这是工程误判，不能据此判某省HA不收敛。没有调整工资、利率、科学输入、网格或算法。

离线修复代码e413bf9cf911a8a0a14181456874a0d9069be6da：新增精确父端辅助守卫，仅允许该完整路径/顶层限定名的_require，以及仅EXECUTION期的_kernel，不开放整个旧toy模块。父端原HA backend/六阶段、旧toy runner、其他文件或类内同名函数继续拒绝。辅助Python调用守卫不是OS写隔离、完整native观察或运行许可。

8项针对性检查通过，含原_kernel/_require函数体与替身Win32/私有通道全生命周期；全部系统符号调用为替身，科学后端未实例化。旧32项及历史session/省级组未变，不重跑或累加为唯一总数。初次测试替身结构体缺storage已修正；首次带审计检查在标准库ctypes导入处被拒绝，改为标准库预加载后再设无外部动作边界，相关离线失败保留，均非科学重试。

原执行脚本、候选12固定工件/63副本和两预约不改，原58源/134边不重绑。修复只保存独立模块、测试及审阅用补丁；按固定摘要装载辅助守卫的替换脚本已在内存编译，未写回执行脚本、未运行、未建立新候选/scope/额度。

本次300秒/3 GiB、写读各2 MiB含控制通道、5文件/1结果、8192事件/5000ms的有限批准已结束，不自动重试、换目录续额或重开已消费scope。runtime/科学接受/Results/REAL_GE/激活/跨进程环境/完整native计量/live/native写隔离资格均FALSE，NEW_RUN_BUDGET=0。九项延期native限制仍null；六项实际批准值及Owner决定已保存，不能继续写“批准次数和全部15项仍null”。A阶段后置strict reference/thresholds及完整native计量、轻量文件保护和扩大前全面OS隔离决定不变。

下一完整工程是对新辅助守卫及其精确父端装载补丁做整包离线审阅，形成新的可审阅运行方案；本轮已有8项回归和补丁摘要，不重新检查未变32项或历史session组。任何后续真实执行均需新的精确有限Owner决定，明确接续已消费scope的方法；不能将本次原批准、补丁或普通工程修复当作重试授权。

本地完整结果在原FINITE_A_RUN_20261109/RUN_RESULT.json；脱敏机器摘要为validators/multi_province/a_finite_run_20261109/run_stop.json；离线检查、精确补丁、不可变摘要及最终交付见POST_STOP_OFFLINE_REPAIR_FINAL。上述均非运行/重放许可。仅六份脱敏文档双端同步，源码/测试/机器/私有载荷本地。main与全部旧STOP/保护义务保持。
