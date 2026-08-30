# Matlab / 模型诊断门禁规则

最后更新：2026-06-25
适用范围：Matlab 模型目录、学位论文第 5 章、多省份 HA-NK / HANK-like 模型、diagnostics、simulation、Results prose
建议仓库路径：`project_rules/PROJECT_RULE_MATLAB_MODEL_DIAGNOSTIC_GATES_CURRENT.md`
规则状态：长期规则 / 模型运行与诊断门禁

## 0. 总原则

Matlab / 模型任务 MUST gate-by-gate 执行。任何通过上一个 gate 的结论都不自动授权下一 gate 的写入或运行。

默认：

- 原始 Matlab 目录只读；
- 复制目录也需授权；
- 不运行 full main；
- 不覆盖输出；
- 不把 smoke pass 当作模型结果；
- 不写 Results prose，除非 diagnostic output review 通过。

## 1. 关键路径

MatlabProgram root path policy:

    logical compatibility entry: C:\MatlabProgram
    physical storage root: D:\MatlabProgram

`C:\MatlabProgram` may be a junction / compatibility path to `D:\MatlabProgram`. When this mapping is present, both paths are one high-risk MatlabProgram boundary. `D:\MatlabProgram` MUST NOT be treated as a separate copy that can bypass original-directory read-only rules, diagnostic-patch gate rules, or no-overwrite policy.

原始目录：

    C:\MatlabProgram\2023年12月2日 多省份神经网络HANK\

诊断补丁复制目录：

    C:\MatlabProgram\2023年12月2日 多省份神经网络HANK_DIAGNOSTIC_PATCH_2026_06_23\

原始目录 MUST NOT 被修改。任何补丁 MUST 先进入复制目录或新建 timestamped copydir。

Future Matlab gates MUST record the logical path used by the command and, where safely checkable, the resolved physical path / junction target. If a direct D path is used, the task/report MUST state that it is the physical target of the C junction and not an independent copy.

## 2. Gate 层级

推荐门禁顺序：

1. Readonly source inventory gate
2. Copydir creation gate
3. Default-off diagnostics patch gate
4. No-overwrite manifest patch gate
5. Smoke wrapper patch gate
6. Smoke wrapper run gate
7. Main2 legacy output guard patch gate
8. Syntax/checkcode gate
9. Main run authorization gate
10. Main diagnostic run implementation gate
11. Diagnostic output review gate
12. Results outline gate

MUST NOT 跳 gate。任何 gate 的 PASS 只对该 gate 范围有效。

## 3. Gate 1：Readonly source inventory

允许：

- 读取 `.m` 文件；
- 列出入口函数、脚本、依赖、输出路径；
- 生成 source inventory report；
- 识别潜在 overwrite / output / figure / save / xlswrite / writetable 操作。

禁止：

- 修改文件；
- 运行模型；
- 创建输出；
- 推断 Results。

## 4. Gate 2：Copydir creation

允许在 task 明确授权下：

- 创建诊断复制目录；
- 复制必要源文件；
- 生成 copy manifest；
- 记录 hash / file count。

禁止：

- 修改原始目录；
- 自动运行模型；
- 覆盖既有 copydir，除非单独授权。

## 5. Gate 3：Default-off diagnostics patch

允许：

- 在复制目录添加默认关闭的 diagnostics 开关；
- 增加不会改变默认运行结果的 helper；
- 生成 patch report。

禁止：

- 改变原始模型默认结果；
- 打开 diagnostics；
- 运行 main；
- 覆盖输出。

## 6. Gate 4：No-overwrite manifest patch

任何输出逻辑必须：

- 使用 timestamped run directory；
- 检查目录是否存在；
- 生成 manifest；
- 不覆盖旧 `.mat`、`.csv`、`.xlsx`、figures；
- 记录 output provenance。

## 7. Gate 5-6：Smoke wrapper patch / run

Smoke 只用于验证 helper 层、路径、语法和最小执行链。

Smoke PASS MUST NOT 被解释为：

- full model pass；
- calibration pass；
- transition dynamics pass；
- result validity pass；
- 可写 Results prose。

Smoke run 必须明确可运行的 `.m` 文件和最大运行范围。

## 8. Gate 7-8：Legacy output guard / syntax

`main2` 或类似 legacy output 必须先加 no-overwrite guard，再考虑运行。

Syntax/checkcode gate 只证明语法或静态检查状态，不证明模型经济含义。

## 9. Gate 9-10：Main run authorization / implementation

任何 full main / main2 / long simulation / IRF / calibration run MUST 有单独授权 gate，写明：

- 可运行的脚本；
- 工作目录；
- logical path and resolved physical path / junction target for MatlabProgram;
- physical target drive free space before any `.mat`-writing run;
- 最大时间 / 中断策略；
- 输出目录；
- no-overwrite；
- manifest；
- 失败时是否允许修复并重跑；
- 是否允许生成图表 / Excel / `.mat`；
- 不写 Results prose 的边界。

如果 failure 出现，Codex MUST NOT 自动修复并重跑，除非 task 明确授权。

If the failure contains `No space left on device`, HDF5 MAT write failure, Matlab access violation after a failed `.mat` write, or `errno = 28`, the next gate MUST be storage/output-location remediation or retry authorization. It MUST NOT proceed to Results prose, Results outline, or model-output validity interpretation.

## 10. Gate 11：Diagnostic output review

在 output review 前，不得写 Results prose。

Review MUST 检查：

- output manifest 完整；
- HJB/KF 状态；
- distribution 状态；
- fixed-point / convergence 状态；
- shock provenance；
- tax label；
- shock label；
- legacy output manifest；
- 图表 / Excel / `.mat` 的来源与 hash；
- 是否存在 smoke-only 误用；
- 人工审阅状态。

## 11. Gate 12：Results outline

只有在 diagnostic output review 通过后，才 MAY 进入 Results outline。

Results outline 仍不是最终 Results prose。它应包含：

- 可写结论；
- 不能写的结论；
- caveats；
- 图表引用资格；
- 需要人工核验的输出；
- reviewer-facing limitation。

## 12. 失败处理

失败默认只生成 failure report。不得自动扩大权限。

禁止：

- 失败后直接改原始目录；
- 失败后运行 full main；
- 失败后覆盖输出；
- 失败后写结论；
- 失败后提交 raw output。

## 13. 非声明

本规则不禁止 Matlab 运行。它要求 Matlab 运行必须有明确 gate、明确脚本、明确输出目录、明确 no-overwrite、明确结果边界。
