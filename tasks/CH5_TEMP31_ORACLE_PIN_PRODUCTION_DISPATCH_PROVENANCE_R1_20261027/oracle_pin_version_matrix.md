# Oracle pin版本矩阵

结论类别（a）：找到完全匹配的历史原件；多个受保护版本的选择仍属于Owner。

期望SHA-256 `b92f6efc59d9398f89f8fb6ee67bf6c5f947282d76895051bec194967ec9c3e3` 精确匹配 `ba98537fd5ae004f0aa37d319865da1f1739e503:exports/matlab_faithful_two_asset_ha.py`，28641 bytes，Blob `9e7dc9556a2b76811e78f89999abecc045886106`，648个LF行，tree `f432f0acb5d94e0f60cd976b74a236be883e0db3`。

| 版本 | 源码路径 | commit / tree | Git Blob | 原始字节数 / SHA-256 | 与pin | 独立可复核范围 |
| --- | --- | --- | --- | --- | --- | --- |
| LOCAL_ENTRY | validators/multi_province/mp4b_python_empirical.py | a1db8c114dec0ab69d69a5576e153a7f868cba0e / local raw bytes not a published tree | 102dbb88a629283a71a3f02541cd7f74f9944213 | 22204 / b9165a71e6a206dc78ad86c23c3502f27a4d81f1329d2efe83c304809556789b | NOT_RAW_SHA_MATCH | local-byte hash and short original fragments only |
| LOCAL_ORACLE | exports/matlab_faithful_two_asset_ha.py | a1db8c114dec0ab69d69a5576e153a7f868cba0e / local raw bytes not a published tree | 6d586fc29c138fd8e531ad14ddfb009fda923638 | 31859 / f6007c1166c951b4a0c98b0fbf551921a2664d2e3943e7d77f847634261524f8 | NOT_RAW_SHA_MATCH | local-byte hash and short original fragments only |
| F1_ENTRY | validators/multi_province/mp4b_python_empirical.py | b69ae535a1518c68822733603f1e506620327375 / 8dbd81c0938f603511c7de1c763ed29b6d2d4b83 | b1710ae3c5d8d7baf96e85c932d777fa5f3b908c | 21791 / 9033218710204ca4ea2af0351376e47bb5b4f203923e6155dc4776add336091e | NOT_RAW_SHA_MATCH | fixed Git object |
| F1_ORACLE | exports/matlab_faithful_two_asset_ha.py | b69ae535a1518c68822733603f1e506620327375 / 8dbd81c0938f603511c7de1c763ed29b6d2d4b83 | e144c645d3f4dc842c2faa6b93b2ba0e24275dcf | 31143 / a7539eb6ba076176b81f832c1800d38d8d170dad8f3619d3b0f3893c5a163fff | NOT_RAW_SHA_MATCH | fixed Git object |
| F2_ENTRY | validators/multi_province/mp4b_python_empirical.py | ba98537fd5ae004f0aa37d319865da1f1739e503 / f432f0acb5d94e0f60cd976b74a236be883e0db3 | b1710ae3c5d8d7baf96e85c932d777fa5f3b908c | 21791 / 9033218710204ca4ea2af0351376e47bb5b4f203923e6155dc4776add336091e | NOT_RAW_SHA_MATCH | fixed Git object |
| F2_ORACLE | exports/matlab_faithful_two_asset_ha.py | ba98537fd5ae004f0aa37d319865da1f1739e503 / f432f0acb5d94e0f60cd976b74a236be883e0db3 | 9e7dc9556a2b76811e78f89999abecc045886106 | 28641 / b92f6efc59d9398f89f8fb6ee67bf6c5f947282d76895051bec194967ec9c3e3 | VERSION_MATCH | fixed Git object |
| F3_ENTRY | validators/multi_province/mp4b_python_empirical.py | 2aa2f67f4e5eaa1117d174b7866c3eb7b7b109b0 / 4b30e019d8089d2f3fdb2f9bc92ceebf47378473 | b1710ae3c5d8d7baf96e85c932d777fa5f3b908c | 21791 / 9033218710204ca4ea2af0351376e47bb5b4f203923e6155dc4776add336091e | NOT_RAW_SHA_MATCH | fixed Git object |
| F3_ORACLE | exports/matlab_faithful_two_asset_ha.py | 2aa2f67f4e5eaa1117d174b7866c3eb7b7b109b0 / 4b30e019d8089d2f3fdb2f9bc92ceebf47378473 | e144c645d3f4dc842c2faa6b93b2ba0e24275dcf | 31143 / a7539eb6ba076176b81f832c1800d38d8d170dad8f3619d3b0f3893c5a163fff | NOT_RAW_SHA_MATCH | fixed Git object |

Git Blob为Git-style SHA-1对象身份，文件SHA-256是独立算法，二者不互代。

当前本地ENTRY/ORACLE分别413/716个CRLF；冻结b69同名对象分别413/716个LF。按物理行去除行终止符后逐行byte payload相等。这只是缓存内比较：没有写入规范化来源、计算替代原件身份或修改工作树。两个本地路径porcelain均空，index的Blob分别b1710.../e144...；整体dirty不代表这两个路径本身dirty。

历史匹配ORACLE与冻结b69 ORACLE有真实文本增改，648→716行，并非只换行：新增MatlabFaithfulTransferCandidates及select_matlab_faithful_transfer_candidates_from_raw（F1_ORACLE:196–260）；local policy新增可选transfer_candidate_abs_limit（F2_ORACLE:216–235/F1_ORACLE:282–301）；原分支选择换成helper调用（F2_ORACLE:302–325/F1_ORACLE:369–397）；shadow transfer使用eligible_shadow（F2_ORACLE:350–370/F1_ORACLE:419–438）；__all__导出增加helper/class（F2_ORACLE:640–648/F1_ORACLE:706–716）。只陈述源码差异，不认证效果、科学正确性或变更原因。

三份冻结ENTRY都为同一Blob b1710ae3c5d8d7baf96e85c932d777fa5f3b908c，均保留B92F pin。只能证明所查三版已有它；首次引入commit/任务UNKNOWN，未全历史扫描。匹配版本存在不证明当前损坏，也不赋予回退、替换、改pin或换行权限。
