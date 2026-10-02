# 固定 C8 条件设计汇总（record19）

**DOCUMENTS_ONLY／DESIGN_ONLY；实际准备与科学执行均 CLOSED。** 本文采用 Work 合规 curated packet、限定语义澄清和已接受的 record14–17 设计事实；record18 的 REJECT 及原产物保持保留、排除，不恢复其合规性。

## 固定基线与证明级别

固定完成 C7 后进入 C8 的 states／S，以及原 C8 household outputs；保留原 N、integration 参数定义、migration-wedge transform 和 share distance，不校准、不重算家庭或 shares，也不以 C7 aggregates 替代 C8 batch。

已知的是 generic 原内存批次 selector 的静态定义及 C8 caller reuse：ct／household_lt／at／at_tax 分别来自 aggregates 下 Ct／Lt／At／AtTax 的 mass_form。原 C8 preflight 的 hash 仅绑定 helper **文件身份**；归档 receipt→batch 的重载身份、原运行对象与 live seal 仍 UNKNOWN。

ga、phi_l、alphal、epsilon、theta、delta 仅为 middle-required 六键子集，各记录 CONSTANT_LITERAL_NOT_EXTRACTED；它们不是完整的十键原字典，另四个 monetary／fiscal 键不属本 slice。household EconomicParams 与 integration.params 保持独立，不声明数值等价。

原 phi 来源仅记为 state Yt/Lt vector／broadcasting 的表达式类别；原 migration wedge 来源仅记为 accepted distance score 的固定 scalar transform，原 transform 保留。share distance 与 migration wedge 的来源角色分开；数值相等／不等一律 **NOT_EVALUATED**，不验证新 value／axis／data identity。distance 目标内容、metadata 和当前 hash 未核验。仅前瞻改变年度 coefficient 的来源，不改变原 wedge transform 或 share-distance 角色。

## 前瞻时序与对象寿命（未执行）

计划顺序为 labor → 原 S 下的冻结 allocation／C1 → 31 firms → wage；allocation 与 feedback 保持同一次分配，不形成新 share law、同 turn payoff 或 fullouter。

labor 与 wage 两个输入边界必须接收**同一原始、不可变 annual master**。前瞻合同要求它在合法准备进程中保持有效，并覆盖两个边界及该链的使用寿命；同 master 证据限于两个输入边界及既有 synthetic 证据，不扩展为整链 consumer 对象身份或 lifetime 已证。实际 source／import／output lifetime 仍 UNKNOWN；退出 child 的 context／seal／master 不在当前进程存活，不能由 CSV 重新封装或改标。

labor 保留 origin tau，wage 保留 destination tau。annual master 的 float64／C-order 与原 S 的 little-endian float64／F-order／uppercase hash 均作为声明合同分别保持，不表示当前数组 dtype／layout／axis 已核验；不混用序列化约定，不重算 field hash，也不据此补造 shape／axis／dtype metadata。

## 尚未开放的门

- 原 C8 的 live／parser／sealed 输入重建、显式 source units／calendar、archive member／shape／dtype，以及完整 canonical 全称 machine binding。
- 精确 source／import／output lifetime、callee namespace 与 transitive import／副作用审查；合成工程证据不安装真实 consumer，也不认证 observed 输入。
- Objective A 完整攻击者／principal／privilege／path-replacement 范围保留；16 类均 UNRESOLVED，合同 UNRESOLVED__FAIL_CLOSED，final-check-to-mutation 窗口 UNACCEPTED。C9 PAUSED；A3 无实施授权，无 isolation plan／实验／保护 PASS。
- 实际准备或科学运行须另有明确、限范围的 Owner authority，并完成 protection／final-chain 独立审查；当前没有预算、launcher、新 output root 或科学后继。

本轮 sourcebody／runtime／data／NPZ 及全部科学调用 0；源码、测试、Git、既有证据未改。旧 actual1／fixtureprocess1 均 consumed1／remaining0；历史 C8 science 保留，旧 C9 attempts 已消耗，CALL_LEDGER_UNRESOLVED 不变。price_verified=False、release=UNKNOWN、baseyear=None、model_activation=False、Results=False。已决基线／价格选择不重开；停在独立 Work review。
