# C9 安全目标 A：精确解释器能力身份 Repair1（零科学）

状态：一次性只读身份修正候选，待 GPT Work 独立 ACCEPT/REJECT；不是隔离实验、原生 Windows 安全证明、runner 修改或科学授权。签发 baseline/parent `f59452b627805101a2dd4e46e16084ede16ef51d`，`HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`。本轮仅新增本报告及同目录收据。

## 旧 PATH 证据与精确目标证据

前一候选 `107965099b6dbd31fe6f56db932dbdbd01c82b4b` 被独立裁决 `REJECT__TARGET_INTERPRETER_IDENTITY_UNBOUND__NO_SCIENCE`。其一次 `python -` 由 PATH 解析，未保存 `sys.executable`；因此只证明**那个未绑定进程**的 Python 3.11.9/64-bit 和 `os.supports_*` 向量，不能证明历史 C9 指定解释器的能力。旧报告原始 SHA-256 `CEFC809980C5005C9D5BFC62AAF73D3A26587D0F0F9405C295E676CA39322131`、旧收据 `272B5013874E5BE56FF4E817537B96971033CF1CA9A3782FCFB9276011B5460B`；旧 probe 的独立 shell 退出码及 stdout/stderr 分离仍为 `UNAVAILABLE`，不回溯补称成功，也不改判该 REJECT。

历史新 C9 执行任务草稿第 19、22、30 行与本任务均字面绑定 `C:\Users\zcxve\AppData\Local\Programs\Python\Python311\python.exe`。本轮只调用这个**绝对路径**一次，未使用 PATH fallback。其 `sys.executable` 原样输出为 `C:\Users\zcxve\AppData\Local\Programs\Python\Python311\python.exe`，与指定字符串一致；解释器退出码 `0`，shell 命令退出码 `0`。完整 `sys.version` 为 `3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)]`；`struct.calcsize("P")*8=64`，`platform.architecture()=["64bit","WindowsPE"]`；Windows build `26200`。同目录收据保留**实际调用的完整 PowerShell 命令、原始输出和逐项布尔向量**，而不依靠版本字符串推断身份。命令内先以 `Test-Path` 对该字面路径做只读存在检查，再由该绝对路径直接执行标准库 `-c`；未导入项目代码。

| 函数 | `supports_dir_fd` | `supports_follow_symlinks` | `supports_fd` |
| --- | --- | --- | --- |
| `os.mkdir` | false | false | false |
| `os.unlink` | false | false | false |
| `os.rmdir` | false | false | false |
| `os.open` | false | false | false |
| `os.stat` | false | true | true |
| `os.lstat` | false | false | false |

因此，**该精确解释器构建**没有所列 Python 标准库 `dir_fd` 创建/删除接口。此前 PATH 进程恰好给出相同版本与向量，但旧进程身份仍未绑定；本轮证据是独立的一次精确路径探测，不能追溯接受旧候选。`os.stat` 的 `supports_fd` 或 `supports_follow_symlinks` 不等于创建/删除能力。

## 不能越过的安全边界

Owner 选择安全目标 A，保留并发/恶意路径替换的 containment 要求。`os.supports_*` 只描述此解释器暴露的标准库能力；它既不证明原生 Win32 句柄相对方案不存在，也不证明该方案可行。祖先 junction/reparse、共享模式、FileId 生命周期、失败清理、跨卷行为、最后检查到 mutation 的原子绑定、隔离实验和 runner 集成均仍为 `UNRESOLVED__FAIL_CLOSED`。原始能力报告中对“目标解释器”的过度归属以本轮新证据**向前修正**，原文件与 REJECT 保持不变。不得以本轮向量授权可丢弃目录 mutation 实验；那需要另行签发和审查。

本轮精确解释器 probe 使用 `1/1`，无第二次调用、PATH fallback 或重试；文件变更实验、测试、preflight、`--execute`、wrapper、模型、科学调用均为 `0`。历史两次被禁止的 `--execute` 探测仍是违规，所有历史 REJECT 及有界 ACCEPT 均保持原裁决范围。旧、新 C9 尝试均已消耗，两份实际调用账本仍为 `CALL_LEDGER_UNRESOLVED`；C10、重试、部分续跑和 Results 均关闭，Results eligibility `FALSE`。

冻结 delegate/测试、Owner A、被拒审查、历史执行任务草稿、旧报告/收据的原始 SHA-256 和六个受保护根的七项 manifest/readback 哈希见同目录收据，已逐项只读复核。下一门仅为 GPT Work 独立 ACCEPT/REJECT；任何后续 mutation 隔离需要新任务，科学还需新命名预算、fresh root、明确一次性 Owner 授权及独立 R/C/O/T 审查。本报告与收据自身原始哈希、candidate/tree 在提交后交接，避免自引用。
