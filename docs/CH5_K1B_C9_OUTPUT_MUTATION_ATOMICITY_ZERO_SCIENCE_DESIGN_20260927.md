# C9 output mutation 原子性：零科学设计证据

状态：仅供 GPT Work 独立 ACCEPT/REJECT 的静态设计候选；不采纳实现、不授权运行。签发 baseline/parent `fc84ba099ef96360042e08632e3c4ef31710986f`，签发 `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。本轮仅新增本报告及收据，测试、runner、合同、科学源和输出均冻结。

## 已接受范围与待解决问题

Repair1 独立裁决 `ACCEPT__BOUNDED_ZERO_SCIENCE_MKDIR_GUARD_AND_CHECK_WINDOW_EVIDENCE_ONLY` 只接受 `mkdir` 缺失后缀的静态行为及**第一次成功 ownership 检查后、最终检查前**替换根时的惰性阻断证据。先前 `REJECT__ROOT_REPLACEMENT_WINDOW_TEST_GAP_AND_OVERBROAD_CLAIM__NO_SCIENCE` 不被追溯改判。诊断 `ACCEPT__ZERO_SCIENCE_DIAGNOSIS_ONLY__NO_REPAIR_OR_EXECUTION_AUTHORITY` 也仅是根因证据。两次历史被禁止的 `--execute` 探测仍为违规；此前全部 REJECT 维持原范围。

当前 `guard_output_mkdir` 在输出根内逐个 `lstat` 现存组件并再次核对根身份（delegate 293–332 行），`guarded_mkdir` 然后调用原始、按路径解析的 `Path.mkdir`（352–358 行）。两者之间没有被持有的目录句柄或原子提交。因此多次 `lstat` 与 `(st_dev, st_ino)` 比较只证明**检查瞬间**的属性，不能证明下一次路径解析仍指向同一对象。

| 变更表面 | 最后检查到变更的窗口 | 当前可证边界 |
| --- | --- | --- |
| `Path.mkdir(parents=True)` | 专用 guard 最终 `owns_output_root` 返回后到原始 `Path.mkdir`；原始递归建父目录会再次进入补丁守卫，但每一层仍有类似窗口 | 已测试两次 ownership 检查之间的替换；**未**测试或关闭最后检查之后的替换。路径可在该窗口指向另一个根/父目录。 |
| `Path.unlink` | `guard_output_mutation` 的根及组件检查（281–291 行）完成后到原始 `Path.unlink`（359–361 行） | 现有检查不把被检叶或父目录绑定到删除动作；新有界 failure detail 也仅属于 `mkdir`，不能外推到 `unlink`。 |
| 输出文件创建 | `output_target` 最后 ownership 检查并返回路径（146–164 行）后，`write_output_json`/`write_output_npz` 分别以 `open("x")`/`open("xb")` 创建（166–180 行） | 独占创建可阻止覆盖同名已存在叶，但不锁定已检父目录；它不是 `Path.mkdir`/`Path.unlink` 拦截器的一部分。 |
| 初始输出根声明 | `claim_output_root` 检查父组件、按路径 `mkdir`，再 `lstat` 记录身份（198–207 行） | 启动时也存在检查、创建与身份记录的分离；这项更广的修复需单独范围。 |

`seal_generated_bundle_guarded` 在检查后把路径交给 sealer 读取，也有检查到读取的路径漂移问题，但本设计只将其登记为相邻读路径风险，不将其混作本轮输出 mutation 修复。现有 `path_components_safe` 会拒绝检查时的 symlink/reparse 与 `lstat` 错误；不能从这种静态检查推导出并发替换下的原子安全。

## 威胁假设与决策选项

| 假设 | 可作的有限表述 | 不能作的表述 |
| --- | --- | --- |
| 可信单进程、无其他写者且本进程不在检查与动作间替换路径 | 在这个明确前提下，检查时的身份/组件结果可供普通路径操作使用；仍需完整 runner 审查。 | 不能称代码本身提供了抗并发原子性。 |
| 协作并发进程可能重命名/替换目录 | 重复检查可发现恰好落在检查点的变化；冲突可能导致阻断或路径重定向。 | 不能保证所有合法竞态都按原根变更，或把 Repair1 测试推广到最后窗口。 |
| 恶意进程可在任意时刻替换根、父目录、symlink 或 Windows reparse/junction | 当前路径级检查不足以证明 mutation 始终包含于原 owned root。 | 不能宣称 hostile replacement 已被阻止。 |

**选项 A：句柄锚定的逐层相对操作。** 设计目标是打开并保留可信目录句柄，逐层拒绝重解析，并使创建/删除相对于已验证的句柄发生，连同失败时关闭句柄和不触碰替换根的语义一起证明。Python `os.mkdir`/`os.unlink` 文档列出有条件的 `dir_fd` 接口，`os.supports_dir_fd` 用于判断某函数是否支持它；这些文档**不能证明**本项目目标 Windows 上具备所需组合，也不能证明 `Path.mkdir`、`open` 和原始科学源调用已获得原子绑定。Win32 `CreateDirectoryW` 文档给的是路径名接口；`CreateFileW`/`SetFileInformationByHandle` 的句柄能力本身也不足以证明安全的逐层相对 `mkdir` 与 `unlink` 已有可维护实现。Windows 文件 ID 稳定性、reparse 处理、共享模式、失败回滚与跨卷行为均待官方 API 证据和隔离验证。不可把可能的 `ctypes`/原生 API 草案写成已证实修复。

**选项 B：能力门与 fail closed。** 如果后续独立审查证明某个平台/版本可满足选项 A 的完整语义，可在运行前验证精确能力；不支持、能力不可确认或隔离测试失败时拒绝 output mutation。现有代码没有这样的完整能力门。允许的平台清单、依赖及拒绝未来执行的后果须由 Work/Owner 明确决定，Builder 不自行扩大或降低既定安全要求。

**选项 C：明确缩窄威胁模型。** 若 Owner 只授权可信单进程、排除协作和恶意并发写者，现有检查可按此较窄前提被评估；这是接受残余风险的治理决定，**不是**原子修复。Work 应写清独占工作区、外部写者、reparse 类型与允许的检测保证；Owner 决定是否接受及后续链能否继续。任何放宽既有安全目标或允许无界 mutation race 的选择必须先经 Work/Owner，不由本设计候选采纳。

平台文档基准（本轮只读核对页面可访问，未进行 Windows API 实现验证）：[Python `os.mkdir`](https://docs.python.org/3/library/os.html#os.mkdir)、[`os.unlink`](https://docs.python.org/3/library/os.html#os.unlink)、[`os.supports_dir_fd`](https://docs.python.org/3/library/os.html#os.supports_dir_fd)；[Win32 `CreateDirectoryW`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createdirectoryw)、[`CreateFileW`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew)、[`SetFileInformationByHandle`](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-setfileinformationbyhandle)。页面存在不等于 Windows 原子性已成立。

## 后续最小惰性证据门

后续若获独立授权实施选项 A/B，应先固定受支持平台、攻击者能力、API 合同和原始终态处理，再在一次性临时目录中验证：

1. 在**最终** ownership 检查成功之后、原始 mutation 前最后可注入点替换根及已存在父目录，证明受保护根外无创建/删除；对 `parents=True` 的每层父目录创建与 `unlink` 分别验证，并以调用哨兵或等价证据区分 guard 阻断与原始操作失败。
2. 已存在的父目录与叶为真实 symlink/Windows reparse/junction 时阻断；权限不足时明确标为环境未验证。对 `lstat` 非缺失错误及能力未知路径 fail closed，不把普通缺父误标为 reparse。
3. 使用实际被批准的平台句柄/能力路径做隔离验证：身份锚、无重解析、并发替换、失败清理与不外逸；仅 mock 不能确证 Windows 原生语义。保护旧受保护输出与冻结输入不得参与这些实验。
4. 失败详情保持有界、不敏感；原始终态不被覆盖，科学启动后的实际账本缺口仍以 `CALL_LEDGER_UNRESOLVED` 保留。非 `mkdir` 守卫是否引入同类诊断应作为**单独 scope 决定**，不可顺手扩展。

现有测试已覆盖第一次与最终 ownership 检查之间的替换、检查时的危险组件及 `lstat` 错误；它们不满足上述最后窗口或真实 Windows 能力证据。不得用科学重试替代惰性验证。

## 证据身份与下一门

冻结 delegate 原始 SHA-256 `AA081078AC9B2997E3DFAA6BA5AF725F5C53013EA7F194780E5BE35A0C911BF2`；惰性测试 `F31F86D9975171441AF4CB7ADD5E6B072163DB27051D9EE5BD9F320087DBE161`；Repair1 独立审查 `D52FD4A47FB6DA9AA7FE301BE6B2F31C09AD84BA574F96B74A3599B698FD022C`；被拒前候选审查 `64F0BA1E63954312D3A96273FB5F4787907AE14C9E3EEB3EA1FB0D2842B3880A`；accepted diagnosis 审查 `4E6745BF3A9F50F1A13EE898C729FC96CC82CDFDEC355EF230F15AABAFF5ECC7`；Repair1 收据 `C38C089B1674F5305F201A173C5BEE0E5C50AF38DF7931B167BB90FF299C01DA`。六个受保护未跟踪根及七项清单/readback 原始 SHA-256 见同目录设计收据，本轮逐项只读核对 `7/7`。本轮测试、preflight、`--execute`、wrapper、模型、科学调用均为 `0`；没有新增 `reports/` 根。

旧、新 C9 尝试均已消耗，两份实际调用账本仍为 `CALL_LEDGER_UNRESOLVED`。C10、重试、部分续跑和 Results 均关闭，Results eligibility `FALSE`。本候选的下一门仅为 GPT Work 独立 ACCEPT/REJECT；之后需 Work/Owner 先裁定威胁模型或平台安全目标，才能另签实现任务。任何未来科学尝试仍需新的明确 Owner 决定和独立审查的 R/C/O/T 链。本报告自身、收据自身及最终 candidate/tree 的精确哈希身份在提交后交接给独立审查，避免自引用。
