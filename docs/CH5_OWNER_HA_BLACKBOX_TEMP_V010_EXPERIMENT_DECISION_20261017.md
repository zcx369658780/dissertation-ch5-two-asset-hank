# CH5 Owner 2026-10-17：HA黑箱优先与临时长轮次实验决定

**决定性质：新的Owner独立探索方向；不是对V010冻结科学计划、先前FAIL_CLOSED、后继Results或V011的追溯修订。**

Owner明确反对反复在Kaplan–Moll附录修改衍生的旧两资产HA内部修改selector、HJB、KFE和接受门。他要求在可证明曾复现MATLAB结果的早期Python家庭模型上开**隔离临时版本**，将家庭求解整个模块作为**原字节不变的黑箱**，不再为局部CP2_F25尝试旧corrected selector补丁。

Owner认为V010原外层5轮实验限制过低，要求**至少100轮作为实验观察窗口**、整个连续外层运行不每轮请求外部验收/暂停；本次历史参照MATLAB为最多500轮，曾独立接收的2009年31省 MATLAB/Python同源稳态为184轮、Python5704家庭调用、31省HJB全收敛。Bellman B可计算则只作为**临时探索诊断**，不能强行改造成旧MATLAB-faithful HA的数值拒绝门；但非法输出、非有限值及源程序原异常不伪装成有效经济稳态。

本次实际已创建隔离 GitHub 实验分支 `experiment/ch5-temp-matlab-ha-blackbox-100plus-20261017`，**固定实验任务发行Commit `503b418f790d61049f3df9016a783dcecc793237`，Blob `0f7917d3f8b89e99c6cd1c9430bf364a02cc30b3`**：
https://github.com/zcx369658780/dissertation-ch5-two-asset-hank/blob/503b418f790d61049f3df9016a783dcecc793237/experiments/TEMP_V010_MATLAB_FAITHFUL_HA_BLACKBOX_100PLUS_20261017/EXPERIMENT_CONTRACT.md

其模型源码父为历史2009 parity成功运行前已完成修复的 commit `216283cf4f1303afa60f1915e143a0b7303a9ffb` / tree `b7a28f7afe7e8de23fb5afdfb377d36c9d025b50`；忠实家户黑箱 `exports/matlab_faithful_two_asset_ha.py` Git Blob `9e7dc9556a2b76811e78f89999abecc045886106`。2009正式验收独立主审Commit `84c26d2e61fb397e0e54621869a95c5b136963eb`。这只是当前核验到的**最早正式验收的31省完整稳态复现锚点**，不要夸大为全仓最早Python源码，也不能把2009单年校准接受扩成所有省年真实结果。

**实验与生产双轨：**
1. 正式治理CURRENT/TASK_CURRENT继续`ACTIVE_TASK=NONE`；V010既有E3科学合同、Owner九月joint-Z采用决定和之前科学STOP全部不动，`model_activation=False`、`Results FALSE`、`V011 NOT_STARTED`。
2. 实验分支自己的实验任务以固定Commit/Blob定义TEMP授权，允许离线只读复用2009证据、仅在本次冻结双省合成fixture上运行老HA黑箱＋最长500轮外层对照；真实2009输入只作为旧证明锚点，原C8/2017/2018/B3及旧保护目录无新权力。
3. 原旧HA及旧MATLAB源、后续V010数学模块的身份与原文件不得更改。独立实验桥/控制器可作为新文件，但不会自动并入正式V010源；只有审议真实实验结果并经Owner明确采纳后，才可决定是否调整正式模型数值路线。
4. 因实验分支是从历史代码commit派生，**其根目录CURRENT/TASK_CURRENT是2026-09-01历史快照，不是2026-10-17现行执行许可**；Codex必须读该实验分支固定实验任务和当前治理分支身份，不得混淆。
5. 保持历史任务的所有已用预算关闭、FULL_RUNNER_IO_CLOSURE=BLOCKED、C盘SSD与D盘旧dirty/index/external common-dir保护；实验结果需独立审计而非Codex自己宣布Python或HANK科学PASS。

**长期交接锚点：**后续顾问若看到“HA应作为黑箱”“100轮后观测趋势”“Bellman只作为探索指标”，先查本决定及实验固定合同，再决定是否开展后续验证；不要把已经STOP的F25修复任务重新签发，也不把临时试验设置倒灌为正式V010已接受科学结论。
