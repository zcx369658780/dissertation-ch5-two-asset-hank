# 有界停止：SSH认证与分批读取成功，保护状态基线发生差异

终态：`STOP__PROTECTED_UNTRACKED_BASELINE_DRIFT__D_ROOT_DISCOVERY_NOT_STARTED`。没有开展本轮目录与原件调查，不能对其他模型目录的原件存在性作结论。

固定任务发文 `afa9d4725ea9666f298a0e87d2f122f4a366761e` 已完整读取；候选固定基点 `1aa1026daceb6b0966470f28fcaa7516cde4a908` 与发文提交角色分开。现行工作流、独立审阅规则、上轮独立验收及 CURRENT 中的 Owner 新授权已从同一固定提交读取。GitHub AGENTS 含旧离线优先历史内容；现行 2026-10-25 权威规则及冻结任务覆盖这些工作流冲突，不改治理文件。

此前单次大范围历史 fetch 未完成，结束后封存为 STOP。Owner随后明确授权认证测试及分批 SSH。指定密钥认证成功；GitHub认证测试返回码1并附成功消息，属于无交互式shell的正常返回。此次以 depth=1、blob:none 取得固定提交元数据，再按单个文件读取任务与规则，均成功；没有切换密钥、账号或协议。此前中断原因仍UNKNOWN，不能由本次成功推断。

恢复核验时 HEAD、index、243条refs及11件保护资产与前次基线一致；dirty/untracked状态摘要由 `c443420c888f5e776cfb6cd05b27cbed56e58a787b82639aa23a47ce7f2ac2f3` 变为 `734f11763de35c822f7fbf9a3ab8e2c6b8fb0ae7c8e7c49174ae3e19948e865b`。5971个NUL状态记录总量不变，差异为3个未跟踪WASM路径移出、3个路径移入，均属既有依赖目录。本轮未读其内容、未修改或清理，变化时间和来源UNKNOWN。主代理在任何根目录列举之前触发保护核验断言并STOP。准确路径仅保存在Owner本地lookup，不上传。

D根目录覆盖=NOT_STARTED；所有模型候选、primary实测、历史manifest与canonical均NOT_MEASURED/NOT_READ。目录/文件时间排序不可用，优先版本建议0个，不因停止而猜测目录或版本。任务的全部调查和科研执行计数均0。此后仅生成报告、授权候选发布与逐项远端回读。

这是保护状态差异引起的执行停止，不是权限拒绝，不是数据来源缺失或科学否决，也不是模型执行失败。保护状态在恢复快照之后的稳定性另由交付回执核验；不能把恢复前后的差异写成全程未变。

发文任务、来源规则和元数据证据可供GPT独立审阅。真实数据来源、TEMP31入口、canonical、31省顺序、Zt年份与人口/就业口径仍BLOCKED。新版HA仅优先待审；NBS工资候选未采纳；ORACLE_SHA、R2/R3、V010/V011与全部历史STOP/PENDING未改。

完成固定候选回读后STOP，不自动重试目录调查、Issue、PR、合并、清理或后继。
