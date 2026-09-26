# C9 output mutation 安全目标 A：Windows 能力核查（零科学，第一阶段）

状态：只读平台/API 可行性证据候选，待 GPT Work 独立 ACCEPT/REJECT；不是隔离实验、实现或运行批准。签发 baseline/parent `bf20d06f20f890eb4fff5f720fbdd666e8e176f9`，签发 `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。Owner 已选 A，保留并发/恶意路径替换安全目标；不接受最后检查到 mutation 的窗口为安全。已接受的 atomicity 设计仅为决策证据，不证明 Windows 实现。当前任务只新增本报告和收据。

## 一次只读目标主机探测

唯一一次探测使用 Python 3.11 标准库读取版本与 `os.supports_*` 集合，并用 `Get-Volume -DriveLetter D` 读取卷元数据；无临时目录、文件变更或 Win32 mutation API 调用。**原始命令及完整合并输出逐字保存在同目录收据**；调用时没有另存 shell 退出码或分离的 stdout/stderr，分别标为 `UNAVAILABLE`，不为补证重跑。记录：Windows `10.0.26200`（`sys.getwindowsversion`: major 10、minor 0、build 26200）；Python `3.11.9`、MSC v.1938、64-bit AMD64；工作树所在 `D:` 为固定 `NTFS` 卷。`platform.machine()` 返回空字符串，因此不据此补推额外架构属性。

在此 Python 进程中，`os.mkdir`、`os.unlink`、`os.rmdir`、`os.open`、`os.stat`、`os.lstat` 均**不在** `os.supports_dir_fd`；仅 `os.stat` 在所列函数中属于 `os.supports_follow_symlinks` 和 `os.supports_fd`。详见收据的逐项布尔值。这个结果排除在**当前 Python 3.11.9 构建上直接使用这些 stdlib `dir_fd` 接口**来完成所需相对创建/删除；不能推出受支持的原生 Windows 方案不存在，也不能把 `os.stat` 的句柄/不跟随能力当作 mutation 能力。主机 API 实际调用语义未探测。

## 官方合同、主机可用性与缺口

证据层严格分开：**官方页面存在 → 当前构建支持的接口 → Windows 精确语义 → 可丢弃目录隔离实验 → runner 集成**；前一层均不能推出后一层。下表的 `UNRESOLVED` 是安全目标 A 下的 fail-closed 结论，不是建议采用较弱目标 B。

| 现有操作与所需能力 | 官方文档明示合同 | 此主机证据 | Windows 未决语义及后续隔离规格 |
| --- | --- | --- | --- |
| 根声明：delegate `claim_output_root` 先检查父组件、再 `output.mkdir(parents=True)`、最后 `lstat` 记 `(st_dev, st_ino)`（198–207 行）。目标需锚定可信父句柄、无重解析地创建根并稳定绑定身份。 | Python 3.11 [`os.mkdir`](https://docs.python.org/3.11/library/os.html#os.mkdir) 的 `dir_fd` 是平台可选能力；微软 [`CreateDirectoryW`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createdirectoryw) 接收路径名，父目录缺失时返回路径错误。[`CreateFileW`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew) 说明打开目录需 `FILE_FLAG_BACKUP_SEMANTICS`，`FILE_FLAG_OPEN_REPARSE_POINT` 改变最终 reparse point 的打开处理。 | `os.mkdir in supports_dir_fd = false`；`D:` 是 NTFS。Win32 页面存在，但**未调用**原生 API，目标主机安全能力 `UNRESOLVED`。 | 未证实祖先 junction/reparse 不被跟随、共享模式阻止哪些并发 rename、跨卷路径/文件 ID/失败清理。后续需在单独授权的可丢弃根中，验证持有父句柄且最后检查后替换祖先时创建是否仍只落入锚定位置；保留原始错误码和句柄清理证据。 |
| 递归 `mkdir(parents=True)`：delegate 最终 ownership 检查后调用路径式原始 `Path.mkdir`（293–332、352–358 行）。目标需对**每一层**相对可信句柄创建且拒绝 reparse。 | Python [`os.mkdir`](https://docs.python.org/3.11/library/os.html#os.mkdir) 可条件支持 `dir_fd`，[`os.supports_dir_fd`](https://docs.python.org/3.11/library/os.html#os.supports_dir_fd) 是本地支持集合；Win32 `CreateDirectoryW` 文档无父目录 HANDLE 参数。 | 当前 `os.mkdir` 不在该集合；Win32 是否有适合此完整语义的受支持组合 `UNRESOLVED`。 | 最后检查之后、每层创建之前均可能替换根/父目录；`FILE_FLAG_OPEN_REPARSE_POINT` 对**中间组件**的完整保证未由所读文档证明。后续隔离须逐层注入 root/parent/junction 替换，断言无外逸创建与 first-failure 停止。 |
| `Path.unlink`：`guard_output_mutation` 检查后调用原始 unlink（281–291、359–361 行）。目标需在已锚定父句柄下删除**指定叶**，不因父路径替换而删除别处。 | Python 3.11 [`os.unlink`](https://docs.python.org/3.11/library/os.html#os.unlink) 的 `dir_fd` 仍是平台可选；Win32 [`DeleteFileW`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-deletefilew) 使用路径参数。[`SetFileInformationByHandle`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-setfileinformationbyhandle) 存在句柄信息设置接口，但本轮未建立可安全获得叶句柄及完整删除合同。 | 当前 `os.unlink in supports_dir_fd = false`；原生句柄删除的目标主机可用性/安全性 `UNRESOLVED`。 | 叶与祖先 reparse、共享/删除模式、持句柄后 rename、最后句柄关闭、跨卷边界和失败回滚均待证。后续隔离须在最后检查后替换父目录并验证没有删到替换根下的哨兵文件。 |
| 独占 JSON/NPZ 创建：`output_target` 检查后，`open("x")`/`open("xb")`（146–180 行）。目标需在已锚定父句柄下独占创建叶并避免重解析。 | Python [`os.open`](https://docs.python.org/3.11/library/os.html#os.open) 有条件 `dir_fd`；`x`/`xb` 的叶独占不等于父目录身份绑定。Win32 `CreateFileW` 文档列创建/共享/标志选项，但未提供本方案的整条相对路径安全证明。 | 当前 `os.open in supports_dir_fd = false`；Python 高层 `Path.open` 仍按路径解析；原生集成 `UNRESOLVED`。 | 祖先 junction、文件 ID 生命周期、share mode、创建失败清理、跨卷路径及与现有 sealer/收据写入的整合未证。后续隔离须在最后检查后替换父目录，验证独占叶只位于锚定目录。 |

微软 [`GetFileInformationByHandleEx`](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-getfileinformationbyhandleex) 与 [`FILE_ID_INFO`](https://learn.microsoft.com/en-us/windows/win32/api/winbase/ns-winbase-file_id_info) 提供已打开句柄的卷序列号/FileId 比较资料；[`FILE_ATTRIBUTE_TAG_INFO`](https://learn.microsoft.com/en-us/windows/win32/api/winbase/ns-winbase-file_attribute_tag_info) 提供属性与 reparse tag。这些是**身份/标签查询**合同，不会使后续字符串路径创建自动绑定同一目录。[`reparse points`](https://learn.microsoft.com/en-us/windows/win32/fileio/reparse-points) 文档说明打开时可能发生重解析。`FILE_FLAG_OPEN_REPARSE_POINT` 不可被泛化为所有祖先均不可替换。卷为 NTFS 也不解除共享、FileId 复用/生命周期、junction、清理或跨卷未决项。

官方 Python 3.11 [`os.supports_follow_symlinks`](https://docs.python.org/3.11/library/os.html#os.supports_follow_symlinks) 仅表明能否对对应函数指定 `follow_symlinks=False`，与 `dir_fd`/原子相对 mutation 是不同能力。没有从文档签名、API 页面或本机布尔值推导 `Path.mkdir`/`Path.unlink` 已具安全目标 A 的 containment。

## 后续门（本轮不执行）

结论：当前 Python 标准库相对操作在目标构建上不可用；Win32 句柄方案的**完整**无重解析、身份稳定、相对 create/delete 语义为 `UNRESOLVED`。在获明确平台/API 合同及后续隔离证据前，相关 output mutation 应 **fail closed**，不得把本报告视为可启动 runner 的能力 PASS；不得选择较弱威胁模型 B。

仅在新任务与独立审查后，才可在 `D:\ProjectTemp` 下**精确指定的新可丢弃目录**实施最小惰性隔离：固定少量 root/parent/junction 组合和一次性预算，在最后可注入点替换目标后分别尝试单层/递归创建、删除、独占创建；核验文件 ID、原始错误码、哨兵不变、句柄释放与失败清理。第一异常即停，不重试、不触碰本工作树、任何受保护 `reports/` 根或科学入口。若原生 API 不能形成可审查完整合同，应继续 fail closed，并交 Work/Owner 决定下一门，不能由 Builder 放宽安全目标。

本轮测试、临时目录 mutation、备份、preflight、`--execute`、wrapper、模型及科学调用均为 `0`；主机只读能力探测 `1/1`。先前两次被禁止的 `--execute` 探测仍是历史违规，不计作本轮合规证据；全部历史 REJECT 与有界 ACCEPT 保持原裁决范围。旧、新 C9 尝试均已消耗，两份实际调用账本仍为 `CALL_LEDGER_UNRESOLVED`；C10、重试、部分续跑、Results 关闭，Results eligibility `FALSE`。任何未来科学需新命名预算、fresh root、明确一次性 Owner 授权和独立审查 R/C/O/T。

冻结 delegate、测试、Owner A 采纳、已接受设计与审查的原始 SHA-256，以及六根七项保护哈希见同目录收据；全部逐项核对。候选提交及本报告/收据自身原始哈希在提交后交接独立审查，避免自引用。下一门仅为 GPT Work 独立 ACCEPT/REJECT。
