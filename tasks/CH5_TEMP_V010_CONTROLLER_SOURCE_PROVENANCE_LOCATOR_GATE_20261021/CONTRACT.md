# 第五章 TEMP V010｜真实supervisor/reader有限来源定位与STOP控制协议溯源（长任务）
TASK_ID=CH5_TEMP_V010_CONTROLLER_SOURCE_PROVENANCE_LOCATOR_GATE_20261021
REVISION=ISSUED_20261021_R1
OWNER_AUTHORIZED=2026-10-21
MODE=SOURCE_ONLY__BOUND_PROVENANCE_LOCATOR
SCIENCE_BUDGET=0

## 1. 问题
上一轮已验收原Ledger跨进程共同协议的X1-X6限定结论，仍未找到**真实生产supervisor/reader程序源码**。旧私人归档已查8个basename只发现PARENT_STOP_REQUEST.json、MAIN_STOP_PROCESS_RECEIPT.json，不能由此推断整个系统没有控制器。本轮要核实真实STOP生产者、文件写入者、读取者、原run调用者、外部supervisor和worker各自的来源身份与证据链；禁止模拟控制器冒充真实来源。不得执行生产run或HA，不改旧journal、正式V010、原Budget或派生补丁。

## 2. 启动身份与可访问原件
先用同一live治理HEAD核CURRENT.md、TASK_CURRENT.md和docs/DOC_INDEX_CURRENT.md唯一ACTIVE。冻结合同/参数从ISSUE_MANIFEST标明的issue_commit读取，发行文件从live release commit，精确核全部Git Blob原件、SHA和预算。固定Review parent=0bc3bd53f234a6d6a7b760571d1eec933bef3969与live HEAD不同，不可混用。
旧私有zip `TEMP_V010_PRICE_BRIDGE_FACTORIAL_100_PRIVATE_FINAL.zip`位于参数列出的同一历史TEMP scratch根下4个精确候选之一，1,214,713B SHA256 `f3e8984fe4d2ef4be65692c27fa7594d96b870d372a8c45d029899f7891841d8`，实际存在性、reparse/共享保护及哈希必须重新验证，来源不一致STOP。只允许一次metadata census（历史278件，上限300），不解压旧模型HA数组或其他私有压缩包。必要时只读取原factorial_driver.py、temp_driver.py及两份STOP JSON四件已知hash成员，必须匹配原字节和来源。
前轮通过验收的公开ZIP可从**历史commit `e08fb30bbca028aa4cb495b1dba7a54729783241`**取得已清理的Git Blob `76a8b7bbf8b460b52c743a6a686ca12b0f907daa`，42773B SHA256 `a3f8247d0099f334382174ddf1403f039880c348f0f6cc6fdacb0742c6868ba6`，只读取三个精确固定身份的源证图与最多额外两个小原件。不因清理后的review HEAD中不存在原ZIP而误判原件不存在。

## 3. 五组有限溯源行动
P0：BOOTSTRAP0/1/2，可信父根、原源码zip、正式Git locator/index及所有保护目录只读身份；唯一新scratch`D:\ProjectTemp\ch5_temp_v010_controller_source_locator_20261021_01`不存在，才可创建并只写此处。
P1：一次性列出已认证私人archive ≤300件中央目录元数据，结合STOP JSON字段和原run静态调用线，列出角色候选但不扫全部私人正文。JSON STOP只是元数据，永远不能充当执行者源码。
P2：仅对冻结的三个**已知**历史TEMP scratch目录做一层内的有限目录元数据查询，最多10目录、每目录≤64项、总体≤320项；允许相对目录名清单见参数。只对文件类型/路径匹配的最多12个小候选读取内容，每个≤65536B，总≤196608B。不得glob磁盘、全项目递归、穿越联接点，未知目录与账号不得进入。
P3：只读静态解析来源认证的Python/PowerShell/batch文件及已有运行引用；无证据的文件名或日志类表述不得拔高为生产控制器。不能import/execute所发现的代码；若路径指向未知安全域，记录需要Owner追加权限并停在此源边界。
P4：GitHub在本次签发固定commit `0bc3bd53f234a6d6a7b760571d1eec933bef3969` 下最多5个参数列出的精确前缀，使用非recursive tree仅列metadata；每个≤64项、最多读8个真实候选；不可root recursive tree或全仓clone。仓库中同名模块不意味着它参与当时TEMP外部控制，必须验证实际调用/执行关联。
P5：给角色/时序证据链、A至E证据等级和严格负结论覆盖矩阵、下一步Owner可授权的精确路径或资料建议、首错和资源/隐私账本；自动发布证据。未发现源码但证明了限定范围与负结果，仍可结束当前SOURCE_ONLY任务，不能用另一个无HA fixture刷PASS。

## 4. 证据等级和因果链
A=AUTHENTICATED_EXECUTABLE_SOURCE（真实原始字节与SHA、静态AST、对应真实运行调用证明齐全）；
B=VERIFIED_RUNTIME_REFERENCE（有可核的命令或日志路径，但源码不可读）；
C=STOP_METADATA_ONLY（STOP/receipt/报告，不是执行源）；
D=NOT_FOUND_IN_FINITE_AUTHORIZED_SCOPE（具体扫描位置/数量/跳过项必须填实，绝不是全系统不存在）；
E=SOURCE_AMBIGUOUS_OR_UNSAFE_STOP（真实歧义/边界硬门）。
围绕STOP_PRODUCER、STOP_WRITER、STOP_READER、RUN_MAIN_CATCH、BUDGET_ADMISSION_CALLER、SUPERVISOR_DISPATCHER、WORKER_OBSERVER画具有来源证明的有向角色链。真实产线、测试fixture、静态推断必须分开。上层执行者**可能位于外部Codex/harness或操作脚本**：仅能将其标记为可能的未授权来源，不能私查global Codex会话、shell history、未知服务和其它工程目录。

## 5. 资源与禁止行为
总墙钟≤10800s，验证1200s、来源调查7200s、发布2400s（遵从全局180s封存预留），工程Python开始≤18、直接进程开始≤72、E1≤3批；完整预算由冻结TASK_PARAMETERS给定。无HA/HJB/KFE/GE/IRF、模型runner、旧100轮/A0–A3、生产修改或部署。真实来源查到也只输出静态定位和后续Owner决策门，不能直接做实际集成。

## 6. 强制GitHub Review三文件自动交付
Codex必须**自动**把脱敏后的`result.md`、`manifest.json`、`evidence_sanitized.zip`上传到仓库独立Review分支`review/ch5-temp-controller-source-provenance-gate-20261021`、临时目录`_review_tmp/ch5/temp-controller-source-provenance-gate-20261021/`，固定唯一parent=`0bc3bd53f234a6d6a7b760571d1eec933bef3969`。仅允许这三件新增，至少包括有限源目录元数据清单、源证矩阵、实际必要身份化小源码或脱敏关键片段、源控制调用图、负证据、Owner后续精确资料需求、首错隐私资源。不能只放hash/摘要或本地路径。GitHub默认精确Git Data API、非强制发布，不绕过401/403/429，不尝试未知认证切换或clone根递归。发布后真实远端ref/commit/tree/sole parent、3件原字节及ZIP所有成员CRC/长度/SHA256、自审隐私全部回读。Codex不得自行清理；Astra按既定五步先独立审核与永久归档readback，再普通nonforce只删除本轮三件并逐条404，PENDING时不删除。两份旧PENDING review SHA`4e05976bbc8068b971ba5915133e9a6c3b73193d`、`1579e7f1d7a1975c322dd6ae9af1776e88e83e7c`不可碰。Owner手工ZIP中转非默认流程。

## 7. 结果与停点
最终报告必须含实际run_id、actual_terminal、每个扫描根的状态/条数/失败/命中sha、A-E身份分层、外部控制器/reader确证与否、是否需要Owner新的外部访问授权、真实run执行次数=0、HA/GE/IRF调用=0、保护前后身份/内核UNKNOWN、首错与E1账、远端三原字节及全部ZIP成员、完整原始JSON Base64+字节长度+SHA256及独立外部controller完成事件。预定`WAIT_ASTRA_CONTROLLER_SOURCE_PROVENANCE_LOCATOR_REVIEW`仅计划停点，实际终态优先。不部署、不运行HA、不自动签发下一任务。
