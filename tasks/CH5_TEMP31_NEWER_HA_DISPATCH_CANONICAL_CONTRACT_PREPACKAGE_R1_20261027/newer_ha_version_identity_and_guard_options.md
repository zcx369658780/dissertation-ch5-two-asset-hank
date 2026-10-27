# 新版HA精确身份与A/B/C守卫来源政策（仅决策预包）

Owner决定仅为新版优先待审，非正式采纳。发文7dffdd9ccfbda364e55f2b110a8f1ebacdd1fb9d与候选基点32d6b827aabea861ea44ffe427abbd63dbe681be不同。

| 原件合同 | commit | tree | Git-style Blob | bytes | 原始SHA-256 | 换行统计 |
| --- | --- | --- | --- | --- | --- | --- |
| historical-old LF | ba98537fd5ae004f0aa37d319865da1f1739e503 | f432f0acb5d94e0f60cd976b74a236be883e0db3 | 9e7dc9556a2b76811e78f89999abecc045886106 | 28641 | b92f6efc59d9398f89f8fb6ee67bf6c5f947282d76895051bec194967ec9c3e3 | {"crlf":0,"lf_total":648,"bare_cr":0} |
| checked-in-newer LF | b69ae535a1518c68822733603f1e506620327375 | 8dbd81c0938f603511c7de1c763ed29b6d2d4b83 | e144c645d3f4dc842c2faa6b93b2ba0e24275dcf | 31143 | a7539eb6ba076176b81f832c1800d38d8d170dad8f3619d3b0f3893c5a163fff | {"crlf":0,"lf_total":716,"bare_cr":0} |
| current-worktree CRLF | a1db8c114dec0ab69d69a5576e153a7f868cba0e | local raw not a published tree | 6d586fc29c138fd8e531ad14ddfb009fda923638 | 31859 | f6007c1166c951b4a0c98b0fbf551921a2664d2e3943e7d77f847634261524f8 | {"crlf":716,"lf_total":716,"bare_cr":0} |

Git Blob是SHA-1对象身份，文件SHA-256单独记录；Git index的跟踪Blob不代表磁盘原始字节。ENTRY与ORACLE的path_status均为空，index指向b1710.../e144...；当前ORACLE与冻结新版逐行byte payload相同但raw不同。没有把当前文件称作未提交语义改动，也没有规范化或产生替代源。

旧pin为B92F...，ENTRY:30–36对目标磁盘raw SHA作严格比较，64在HA import前调用bootstrap。旧pin对应旧LF版本，新Git LF及当前CRLF都不等于旧pin；本轮没有运行守卫/入口，不将静态不匹配写成实测报错或源码损坏。只改成新Git LF hash也不自动接受当前CRLF原字节。

真实差异仍需科学审查：旧307–321的transfer分支被新版helper调用NEW_GIT:369–392取代；当前ORACLE:196–213、247–259有transfer candidate容器/选择，282–294增加可选transfer_candidate_abs_limit，419–438改shadow来源为eligible_shadow。这是函数/分支文字差异，非只换行；未证明默认参数行为完全等价、稳定性、KKT/收敛或Owner科学采纳。旧pin身份结论继承上轮独立验收，本轮不追首创任务或重放53摘录。

| 方案 | 现有来源事实 | 科学/生产/回滚风险 | 需要额外Owner批准吗 | 最小后续范围（建议，未发单） |
| --- | --- | --- | --- | --- |
| A 历史Oracle+旧pin | 28641B历史LF原件与B92F pin匹配 | Owner当前未选择回退；会失去新版helper/分支文本；匹配不等于科学正确 | 需Owner额外明确推翻/变更当前优先候选方向并冻结具体版本/字节合同；本轮不得回退 | 仅在新授权中审查旧/新科学差异和明确恢复范围；不是今天执行任务 |
| B 保留新版，另审版本化身份合同 | Owner已选新版优先待审；Git LF a753...与Windows CRLF f600...是不同原始身份 | 必须单独定版本ID、来源commit/Blob、目标raw SHA/bytes/换行及构建/部署证据；不能自动宽免pin或静默正规化 | 未来实施/版本正式采纳/guard改动仍需Owner额外冻结批准；当前没有实施许可 | 待入口/输入事实明确后，单独签发候选身份设计及必要独立科学审查；本轮只文档 |
| C 保持blocked，先补入口/输入认证 | 现有静态链与合同可引用；实际采用命令、真实canonical/旧期tuple未认证 | 继续blocked，不产生虚假生产/数值PASS；不改守卫或源码 | 提供精确采用入口/配置/版本/representation/year、原件位置和只读权限需Owner；不会自动签新任务 | 最小下一证据是Owner提供准确配置/运行清单和输入身份；其后再议guard/接线 |

B方案目前只讨论将来源版本、批准的目标raw表示、hash/长度和部署身份分开冻结的合同要素，不写guard代码、不生成patch、不认可自动去CR或哈希白名单。A不是默认回退；C不是恢复任何旧预算。任何将来检查通过也不自动等于TEMP31生产采纳、D1/D2/D3或科学接受。
