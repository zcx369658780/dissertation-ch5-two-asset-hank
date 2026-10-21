# CH5 GitHub精确对象恢复 · R2发行勘误（R1原件不改）

TASK_ID=CH5_TEMP_V010_GITHUB_EXACT_OBJECT_TRANSPORT_RECOVERY_20261021
REVISION=ISSUED_20261021_R2
TYPE=ISSUANCE_TECHNICAL_CORRECTION_ONLY
PARENT_RELEASE=8f3e1adf95b3ebfd404c0448f00e678a4098ab35
R1_CONTRACT_GIT_BLOB=0b5b453bd3b85c59ee5e118c742ae6cc1511c5ea
R1_PARAMETERS_GIT_BLOB=867bf276c39a70c16fe7fdf30af56a72b29dc35a
OWNER_SCOPE=2026-10-21 B-only已批准内容不变
TASK_EXECUTION=NOT_STARTED

## 唯一更正（优先于R1合同B3公式片段）
原R1合同B3中的字节字面量 `b"\\0"` 容易被解释成反斜杠加字符零，而非Git对象头所需的单个NUL零字节，不能照该字面写法实现。Git Blob SHA1应按下面标准库的**完整字节公式**校验：
```python
import hashlib
def git_blob_sha1(raw_bytes: bytes) -> str:
    header = b"blob " + str(len(raw_bytes)).encode("ascii") + bytes([0])
    return hashlib.sha1(header + raw_bytes).hexdigest()
```
`bytes([0])`是恰一个零字节，长度必须是**实际获取、完整解码的原始字节**的数量，绝非响应Base64文本长度、字符长度或SHA256十六进制长度。将计算出的40位十六进制SHA1与R1四枚预先冻结的 Git Blob 逐一比较。SHA256仍另用原始字节单独核验。
本更正只修正Git对象头表示；不改变四件source commit/path/blob、请求次数和回退条件、全部预算、Review parent/branch/temp path/三文件、A不重跑、科学0、旧PENDING保留与平台拒绝硬STOP。R1合同和参数仍为不可变发行原件；**有效执行合约为R1合同+R1参数+本R2勘误，出现上述公式冲突以本勘误为准**。当前唯一授权任务仍为原TASK_ID，没有并行新任务。须在本轮R2发行清单里核这三个Git Blob；没有实际R2 live release HEAD/原件回读不可执行。
