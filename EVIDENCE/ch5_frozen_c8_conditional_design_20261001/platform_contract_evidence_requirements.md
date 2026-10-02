# 平台契约证据要求

2026-10-01 · Work TASK26 / Builder 对话28 · DOCUMENTARY_REQUIREMENTS_ONLY。

TASK25 已获 `ACCEPT__UNEXECUTED_REJECTION_INTERFACE_SCAFFOLD_TEXT_ONLY`。这仅接受未执行拒绝接口的文本形态；语法、导入、实际拒绝、平台语义和保护效果均未验证。本文件只列文献契约证明义务，不新增实现、实验或运行授权。

## 接口与原有操作键

| 拒绝接口 | 原有操作键／地位 | 必须有独立文献支持的对象语义 |
|---|---|---|
| `anchor_directory` | 目录锚定前提；不新增第五类变更操作 | 目录身份与父链关系的含义、句柄绑定对象、所有权和存续条件；不把路径重查或“有句柄”视为保护充分性。 |
| `claim_root` | `root_claim` | 根认领涉及的父／根身份约束、并发替换时操作对象的含义，以及完成、失败和部分状态。 |
| `mkdir_each_parent` | `each_recursive_mkdir_parent` | 每个 P0…Pn 的父／目标身份、逐层父链关系、句柄生命周期，以及各层操作的检查至变更关系、完成和部分创建状态。 |
| `create_exclusive_json_npz_leaf` | `exclusive_json_npz_create` | 父／指定叶身份与父链绑定，排他创建、对象已存在及并发替换时的语义，完成、失败和可能的部分文件状态。 |
| `unlink_specified_leaf` | `specified_leaf_unlink` | 指定叶及父链的身份约束、名字与句柄所指对象的关系，以及并发替换、完成、失败和部分删除状态。 |

这些是接口到既有分类键的映射，不重绑定分类权威，也不建立任何原生平台语义。全部五个范围的支持状态均为 **UNKNOWN / NOT_ESTABLISHED**。

## 共同证据缺口

每项拟用原语在任何非拒绝实现之前，均须获得独立审查的文献契约支持：

- **精确平台与 API 版本**：明确适用版本、接口版本、文献版本及限制。当前平台／API 版本为 UNKNOWN；没有选定或猜测 API。
- **独立官方契约引用**：需有可核验的官方文献、精确支持段落、适用范围及独立审查结论。当前外部文献定位为 **NOT_PROVIDED**；本次未检索，不补写 URL、API 名称或引用。
- **身份与父链语义**：明确契约中的父、根、指定叶和每一级父链如何对应操作对象，以及并发替换、rename/delete/reparse/cross-volume 情形中的保证与缺口；不得从父目录推导受保护根授权。
- **句柄所有权与生命周期**：明确持有、转移、关闭、失效及完成前后绑定关系的契约责任；符号参数或句柄术语本身不证明这些条件成立。
- **检查至变更关系**：分别列清四类操作的原子性或非原子性保证、适用前提与未保证范围；路径复核不得代替原有窗口目标。没有文献支持的部分继续记 UNKNOWN。
- **完成、失败及部分状态**：分别支持成功、未完成、失败及部分创建／删除时对象、句柄和状态的含义与责任。不得从静态拒绝文本推断实际 fail-closed，也不得合并四类操作各自的失败／部分对象责任。

以上仅规定所需证据，不声称任何保证已建立，也不提出调用步骤、测试设计、目标路径、尝试额度或可运行代码。

## 保留边界与结论

完整 Objective A 及全部攻击者、主体、权限和路径替换能力保留，包括 principal/token、same-token、特权／admin writer、DACL／ownership、rename/delete、reparse、cross-volume。未覆盖能力不得被假定不存在。loader/cache/constructor/callback/transitive dependency、stdout/stderr 与行政 capture 威胁继续在范围内，不作为豁免。

`acl_dacl`、`separate_principal`、`sandbox`、`appcontainer` 与上述四个原有操作键的 **16 项全部 UNRESOLVED**；最终检查至变更窗口仍 **UNACCEPTED**。六个受保护根的具体定位授权仍缺失，不能补猜路径。七项 manifest/readback 是历史声明，不构成本次独立保护验证；本次未重读其正文或重核 fixed72。载体兼容、真实 observed master 准备与最终链仍是不同的未完成门。

文献证据本身不能证明整体保护、采用边界或授权实验。A3 仅保留已完成的精确未执行准备例外；后续实验仍须单独、明确的 Owner 授权和 Work 限定任务。本文件不签发后继任务。

本轮运行／导入／AST／编译／测试／probe／DLL／native／实验／模型／科学／消费者／actualdata／受保护根及输出根操作均为 0；没有新增运行预算。旧 actualdata、fixture、archiveadmin、V1、V2 各 consumed1/rem0，不重置。C9PAUSED、ObjectiveARETAINED、CALL_LEDGER_UNRESOLVED、priceFalse/releaseUNKNOWN/baseyearNone/modelFalse/ResultsFALSE 保留；历史 C8 科学证据保留，当前条件链科学调用0。

## 本次依据与交付门

仅使用三份允许文档；引用中的其他材料未跟随：

| 文件 | SHA256 |
|---|---|
| `work_unexecuted_isolation_review.md` | `468FFC29A7BD070D95393B0027E171FC233780B2A16A904A8043816C6DDF0C73` |
| `inert_isolation_implementation_scope.md` | `E947AA15BE4DE86C968092589E2A3A7A8F5D6227FD0DADC2C276F7EAC44EE1AE` |
| `objective_a_classification_supplement.md` | `64754C2EBCA1BF987777258AA065379D55A858D89BBD87B1166DFE8CA363AB22` |

任务单 SHA256：`3F66E369EC9CE55B68C1C15468010813F8FC1335D253771E553D884A655A8B23`。交付后 STOP，等待 Work 独立文档验收；不自验收。
