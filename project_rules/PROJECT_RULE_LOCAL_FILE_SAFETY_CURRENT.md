# 本地文件安全与 No-Overwrite 规则

最后更新：2026-06-25
适用范围：Zotero、Obsidian / ResearchVault、ResearchData、BaiduNetdiskDownload、Matlab 模型目录、本地导出和 GitHub 提交
建议仓库路径：`project_rules/PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md`
规则状态：长期规则 / 本地安全边界

## 0. 默认只读

本项目所有本地路径默认只读。除非 task 文件明确授权，GPT / Codex MUST NOT 修改、移动、删除、覆盖、同步或提交本地正式文件。

## 1. 重要路径

以下路径具有安全边界意义：

    D:\ResearchVault
    D:\ResearchVault\note
    D:\spatial-hank-research-kb\SpatialHANKVault
    D:\spatial-hank-research-kb\zotero\exports
    D:\ResearchData
    D:\BaiduNetdiskDownload
    C:\MatlabProgram
    D:\MatlabProgram
    C:\MatlabProgram\2023年12月2日 多省份神经网络HANK\
    C:\MatlabProgram\2023年12月2日 多省份神经网络HANK_DIAGNOSTIC_PATCH_2026_06_23\

这些路径不应由 GPT 直接假定可访问。Codex 本地执行时也必须遵守 task 授权。

`C:\MatlabProgram` 是兼容性 logical path / junction entry。当前 physical storage root 为 `D:\MatlabProgram`。如果本机 junction 将 C 路径映射到 D 路径，则 `C:\MatlabProgram` 和 `D:\MatlabProgram` MUST 被视为同一个高风险 MatlabProgram 存储边界；不得把 D 盘路径当作一份新的、可绕过原始目录只读规则的独立副本。

## 2. Zotero 安全规则

除非 task 明确授权，Codex MUST NOT：

- 修改 Zotero SQLite；
- 写入 Zotero item、collection、tag、note；
- 修改 Zotero PDF 或 attachment；
- 删除、移动、重命名 Zotero 文件；
- 提交 Zotero database、PDF、附件到 GitHub。

允许的默认行为：

- 读取导出的 metadata / JSON / CSV；
- 读取 task 指定的只读导出文件；
- 生成候选报告；
- 生成待人工核验清单。

Zotero 写入 MUST 是单独高风险授权 gate。

## 3. Obsidian / ResearchVault 安全规则

除非 task 明确授权，Codex MUST NOT：

- 修改 `D:\ResearchVault` 或 `SpatialHANKVault` 正式笔记；
- 自动重写人工笔记；
- 批量迁移、重命名、删除笔记；
- 生成会污染 Dataview 索引的未审计笔记。

允许的默认行为：

- 生成候选笔记到安全 staging 目录；
- 生成 markdown 草稿供用户手动审核；
- 生成 manifest 和差异报告。

写入正式 vault MUST 明确说明目标路径、覆盖策略和人工审核边界。

## 4. 数据目录安全规则

`D:\ResearchData`、`D:\BaiduNetdiskDownload` 等 raw / purchased / private 数据目录默认只读。

Codex MUST NOT：

- 修改 raw data；
- 覆盖 cleaned / estimation data；
- 下载外部数据并混入正式数据目录；
- 提交 purchased/private/raw data 到 GitHub；
- 用未经授权的数据生成正式论文结论。

允许的默认行为：

- 读取 task 指定的样本或 manifest；
- 生成审计报告；
- 生成候选 merge plan；
- 在授权 staging/output 目录生成派生文件。

## 5. Matlab 目录安全规则

MatlabProgram storage root：

    logical compatibility entry: C:\MatlabProgram
    physical storage root: D:\MatlabProgram

Future tasks MUST record both the logical path used by commands and the resolved physical path / junction target when safely checkable. Direct `D:\MatlabProgram` paths are allowed only when the task explicitly states they are the physical target of the `C:\MatlabProgram` junction and not a separate copy.

原始 Matlab 目录：

    C:\MatlabProgram\2023年12月2日 多省份神经网络HANK\

默认 MUST be read-only。This C path may resolve through the junction to `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\`; the read-only rule follows the resolved target.

诊断补丁复制目录：

    C:\MatlabProgram\2023年12月2日 多省份神经网络HANK_DIAGNOSTIC_PATCH_2026_06_23\

也不是无限写入目录。任何写入、运行、输出都必须由 gate 明确授权。This C path may resolve through the junction to `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK_DIAGNOSTIC_PATCH_2026_06_23\`; it remains the only authorized patch/run location unless a future task says otherwise.

MUST NOT：

- 在原始目录直接打补丁；
- 覆盖原始 `.m` 文件；
- 直接运行 full main / main2；
- 覆盖既有 Matlab 输出；
- 把 `.mat`、大 Excel、图表、日志直接提交 GitHub；
- 把 smoke pass 当作模型结果 pass。
- 删除、重建、绕过或复制 `C:\MatlabProgram` junction，除非 future storage-maintenance task 明确授权；
- 将 `D:\MatlabProgram` 视为独立可变更副本来规避 C 路径下的高风险边界。

Future Matlab/model gates MUST preflight:

1. `C:\MatlabProgram` exists.
2. It is a junction or documented compatibility path to `D:\MatlabProgram`.
3. `D:\MatlabProgram` exists as physical storage.
4. Original and diagnostic-patch directories resolve under the expected physical root.
5. Physical target drive free space is checked before any run expected to write `.mat` output.

## 6. 写入授权格式

task 文件 SHOULD 使用明确语句授权写入，例如：

- `允许生成报告`
- `允许修改复制目录`
- `允许生成 diagnostics`
- `允许运行 smoke wrapper`
- `允许运行 Matlab 文件 <path>`
- `允许 git add / commit / push`
- `禁止 overwrite`
- `允许 overwrite <具体文件>`

不同授权之间 MUST NOT 互相推导。

示例：

- 允许创建 GitHub task，不等于允许运行 Matlab。
- 允许 smoke run，不等于允许 full main2 run。
- 允许诊断导出，不等于允许写 Results prose。
- 允许修改复制目录，不等于允许修改原始目录。

## 7. No-overwrite 原则

涉及输出文件时默认 no-overwrite。Codex MUST：

- 优先使用 timestamped run directory；
- 在输出前检查目录是否存在；
- 生成 manifest；
- 记录文件 hash / size / row count / source path；
- 不覆盖旧图表、旧 Excel、旧 `.mat`、旧 `.csv`、旧报告；
- 如果必须覆盖，必须由用户单独授权。

## 8. GitHub 提交安全

MUST NOT 提交：

- raw / purchased / private data；
- Zotero PDFs / SQLite；
- Obsidian 私密笔记全文；
- secrets / tokens / credentials；
- Matlab 大输出；
- 临时 cache、binary、log dump。

SHOULD 提交：

- text-first report；
- manifest；
- hash；
- source inventory；
- verdict；
- next gate recommendation。

## 9. 违规处理

如果 task 需要触碰未授权路径或高风险文件，Codex MUST stop and report。不得自行“顺手修复”或“为了完成任务先改一下”。

If a Matlab/model run fails with `No space left on device`, HDF5 write failure, Matlab access violation after failed `.mat` write, or `errno = 28`, the next gate MUST be storage/output-location remediation or retry authorization. It MUST NOT jump to Results, interpretation, or output validity claims.
