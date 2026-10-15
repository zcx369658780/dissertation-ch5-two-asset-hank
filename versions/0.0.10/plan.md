# V0.0.10 修订DRAFT：原MATLAB主线的Python修错与接续

更新：2026-10-15（Asia/Shanghai）。
**状态：V010_MAINLINE_ALIGNMENT_SOURCE_ONLY_AUTHORIZED__WAIT_CONSOLIDATED_PROPOSAL。**
**同步已限定接受；当前只允许mainline_alignment_task.md的精确SOURCE_ONLY任务，不是模型实施或科学运行许可。**

## 1. 范围与阶段

Owner在CH5_OWNER_SCOPE_REALIGNMENT_20261015.md明确恢复项目目的：修正原MATLAB错误，在省级HA条件稳态黑箱、有界多省顺序迭代、GovInv/Zt自适应校准及原递推冲击框架上Python重写第五章。这个主线不再讨论是否改成另一套人工HANK。

原V010 Newton/Jacobian/零私人资本取证DRAFT及聊天任务已停用，旧内容保持在db2c2e289419ecab7921667e210bd510ff3c447b，blob eae74d9db34b319544ec32cd1c7b71325db6e650；不读取旧失败数组、不研究Newton加速。纠偏后“先同步”草案在916e2b47d3489f6eacd814b55cc568d92be4c9fb，blob b8a02f55ded8b1518b41728e6e306581df631098。本次只推进其已规定的同步后阶段，没有改写既有正式科学冻结合同，也没有另立微版本。

同步结果见[限定验收](scope_sync_acceptance.md)：Codex报告16文档匹配、Scope ACK和停止，Astra核远端源身份并明确Windows原回执未经网页独立读取。原同步镜像、收据、历史合同均保留。无需再次同步同一16文档。

## 2. 本轮具体目标

以[主线基线与最小修错任务](mainline_alignment_task.md)为唯一执行入口。一次性取得：

- 原MATLAB参考与合适source-faithful Python/已接受HJB-KFE修复的真实基线建议，不能默认采用V008/V009人工候选。
- HA输入输出、单轮顺序、外层GovInv/Zt/边界/阻尼/退出与原冲击接口的精确图。
- 可直接复用、已证bug最小修复、与原科学决定冲突待裁决的集中清单。
- 一份可直接供Astra集中冻结的同V010 Python实施和验证方案，精确路径、输入/数据必要性、资源与停点；此时不实施。

特别处理原GovInv收益边界调节和后来C1残差律的不同角色；不自动回滚C1、不悄悄把它固定进恢复后的原外层方法。价格有界、raw/used、校准阶段与冲击阶段、Lt覆盖/人口单位/税/资本分配按原证核对。合法自适应校准不是一概禁止的事后调参，但实际更新律必须事前明确。

## 3. 不改变的主线与科学保护

HA可以作为模块黑箱，但其HJB/KFE、概率质量、聚合有效性仍须验证。原程序可能有错，恢复方法不等于复制bug或盲目要求所有原数值一致。phi富裕目的地低厌恶方向、max_phi=.3、人口人均不N=P/3，以及既有可信数学修复保留其范围。

V008/V009人工制度、Newton根、固定Bg/内生T、竞争企业、新动态HANK方法保留为非活跃辅助，不用作原主线前置或默认baseline。原递推冲击响应是第五章目标，未来完整前瞻方法另需研究决定，不自动阻塞本主线。

本轮不选择或合并代码基线、不写研究代码、不运行pytest/模型/HJB/KFE/IRF，不读真实C8/B3/旧失败数组，不重置旧预算。具体允许的普通源码与Owner辅助文本、3小时/60份/4MiB界限见任务全文；只有SOURCE_ONLY许可。

## 4. 下一停点

Codex交付V010_MATLAB_MAINLINE_BASELINE_AND_MINIMAL_REPAIR_PROPOSAL后STOP，Astra据真实源集中审议。若有GovInv/C1等重大科学取舍，集中提交Owner；否则依既有主线完成正式实施计划冻结，再单独授权数值/代码工作。当前未发此类授权，V011 NOT_STARTED。

原8 dirty/外置common-dir/untracked/ignored与B3不覆盖或清理。A16 FAIL_CLOSED、window UNACCEPTED、C9 PAUSED、CALL_LEDGER_UNRESOLVED、model_activation=False、Results FALSE和真实C8 A–D REQUEST_ONLY维持。V1.2及Owner连续版次委托不改。
