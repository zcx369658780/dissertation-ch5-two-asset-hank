# V010第二次单点HA恢复：Windows Git argv守门预检阻断的独立验收

更新：2026-10-16（Asia/Shanghai）。

**审议裁决**：`ACCEPT_FAIL_CLOSED_DELIVERY_REPORT__RECOVERY_PROCESS_EXHAUSTED__HA_UNTESTED__WINDOWS_GIT_ARGV_GUARD_REJECTION_REPORTED`。
**科学结果**：`NO_NEW_SCIENTIFIC_CONCLUSION`。V010原实现的工程限域接受不撤销；本次单点价格`rah=.0675,w_eff=15.5,rb=.02`尚未开展corrected HJB/KFE试验。
**后续**：仅允许独立静态诊断执行器与只读原证；**不授权第三个Python进程或HA求解**。

## 1. 独立核实的GitHub边界

Astra经授权GitHub连接读取/验证：
- 本次已STOP恢复任务，固定发布commit `042195e633dec2eec532ab1b56da9822e912afe3`，tree `0a1483dd08916dc126699c93d4b1d45b30038c23`，task blob `000a7089183178e9014e9721f45c1f947e2290b1`；
- 恢复科学合同commit `9aca1018c77d19e9489f2baf59c02bc654923999`、tree `4a04fd536b1cd4dd82b07dbdc23b5d73d1c8f6cc`、blob `95843d1ec838f52b056a8ca768d3f4cc55022b6f`；合同限定单次Python进程、≤1HA、96MiB=100663296B新artifact、≤2GiB新clone；
- 不可变独立价格manifest blob `c23d331bed34e5ca478324cdc05034609ecb91b7`；数值`rah=.0675,w_eff=15.5,rb=.02,Tt=.1,rb_gap=.07`及固定20×20×2网格；
- 科学候选Python commit `94de4501dec051b969bee9d852eba2d4591f30ef`、tree `205eab47c4e4f9c6292c2ead9947d94d1a7579a5`；原V010 plan blob `85138d8859d53295262fe13bf5bc277bca95ed3f`，均保持原冻结authority。

## 2. Codex报告的本地事实，严格分开证据等级

用户转达`V010_CORRECTED_HA_ONE_SHOT_RECOVERY_RESULT`存于`D:\ProjectTemp\ch5_v010_corrected_ha_price_probe_recovery_20261016_01\V010_CORRECTED_HA_ONE_SHOT_RECOVERY_RESULT.md`。**该本地MD尚未作为附件提供，Astra无法直接读取该路径，也没有独立看到runner源码/拒绝argv/回执hash。** 以下均为`CODEX_REPORTED_WITH_LOCAL_RECEIPTS`，并非GitHub认证事实：

1. 私有runner的子进程守门未兼容Windows命令行实参形式，错误拒绝第一次只读Git预检；执行停在source/输入九模块硬门之前。
2. 这次恢复新Python进程**1/1已用**，但`HA=0, HJB=0, KFE=0, selector=0, root=0, pytest=0`；无新的经济模型计算和严格HJB数值结论。
3. 新artifact合计**117446B**，未触96MiB=100663296B；新增clone=0。
4. Codex报告原2026-10-15超额目录17个文件的size/SHA256/mtime均不变，原`43519638B`和超原32MiB的`9965206B`违约记录仍封存；Astra未实地重hash17份文件。
5. Codex报告模型候选及旧受保护工作树未写、C8/B3访问0，无失败后再次执行或变更。网页未独立核D盘private filesystem。

**这次没有新artifact超限；但Python 1/1用尽且预检未PASS，不能判合同完成。** 旧第一次GBK预检进程1/1用尽、HA0、超额硬门和本次Windows argv预检进程1/1用尽、HA0、无超额是两份独立失败；不得互相冲销，更不得将`HA0`理解为`Python process quota unused`。

## 3. 直接失败性质、未证明点和执行器设计缺口

- 直接障碍分类：`EXECUTOR_PREFLIGHT_GUARD_REJECTED_READ_ONLY_GIT__CODEX_REPORTED`；尚未读取原私有stdout和被拒绝的argv原件，所以**不能独立指认**究竟由`git` vs `git.exe`、`-C`位置、Windows带空格绝对路径、命令字符串/数组、`shell`或其他解析问题导致。
- 既有冻结任务要求唯一Python进程内部核候选head/tree、9个Git source blobs及实际Python`__file__`；若守门器将合法只读Git误拒，必然在HA前停止。纠错时不得为求PASS直接取消安全边界、默改经济数据或不再核source。
- 不涉及`NO_ADMISSIBLE_POLICY`、corrected selector/KFE数学、真实31省GE或是否存在稳态的因果结论。此前第一次synthetic HA checkpoint2 F25失败以及价格域历史比对仍是独立的旧事实。

## 4. 限域审议与下一步

本次**接受真实STOP的报告与现阶段科学0调用分类**（本地证明层级仍是Codex回执），不接受`PRECHECK_PASS`或`STRICT_CORRECTED_HA_PASS`；当前任务`CLOSED_WITH_NO_SCIENCE_RESULT`，禁止重启进程、修改freeze或换输出目录续配额。

后续唯一合理的低风险步骤是在同V010下精确检查**已存在**的私有runner、拒绝日志和Windows实际`subprocess`实参表示，形成仅在新隔离scratch内的修复提案和静态argv/拒绝矩阵。该工作不运行Python/Git修改/模型/pytest，也不消耗新的HJB/KFE预算。见[限定静态任务](windows_git_argv_guard_static_repair_task_20261016.md)。

第三次正式科学试验之前应建议Owner分开审批/冻结**短工程preflight过程**与**真正science过程**，让错误CLI拦截不再消耗整个HA科学窗口；这需要明确的新资源权限，**本报告绝不签发**。现有原V010、单点science freeze、输入及旧失败记录均保持不变。

## 5. 安全停点

原V010旧消耗据Codex为pytest 4/6、science driver 1/4、HA1/26、selector 1626、root1642；第一次单点probe进程1/1/HA0、第二次恢复进程1/1/HA0分别记录。当前新增Python/HA/selector/root/pytest/macro/IRF权限**0**；旧A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER UNRESOLVED、model_activation=False、Results FALSE、真实C8 A–D REQUEST_ONLY及原8dirty/index/external common-dir安全边界不变。V011 NOT_STARTED。
