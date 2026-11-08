# A/0父端代写与一次handoff集成

日期：2026-11-08。代码候选b2cd776891e7c5b9e3a566935588d1beb116e05e。本轮完成有界输出消息协议、原配额broker接入及一次原handoff到六阶段opaque输出的离线集成；完整受保护可执行worker包仍INCOMPLETE，未提交最终Owner运行请求。

本轮从模型5f35fe66、治理本地802b1669、治理远端0cfffdc2恢复，main b7e595ce保持。两树身份/分支/remote/索引/dirty/untracked符合上轮回执；默认0子代理，不转移外层旧R40。按Owner自主权连续完成工程，不逐helper/测试/commit设Owner停点。

## 完成的接线与检查

新增标准库output_channel实现请求/响应的消息MAC、独立方向、同record/session、单调序列、对应请求摘要及显式有限帧/消息上限。消息只带固定operation/role和有界字节，不接受任意输出路径。固定五角色沿用原分区，工人只能写origin/worker_log，追加仅日志；父端storage仍使用原FirstReturnOutputBudget的独占创建、预付、累计读写和失败留存。

worker预算在handoff前只绑定一次通道。已路由数据write/read通过broker，工人不再在这些方法中打开数据文件；目录/文件身份只读核验保持。通道被删除/替换、方法改变或失效时拒绝，不回退直写。父端与工人配额是同一分区的镜像，不是双份额度。父端完成写入后回包丢失，文件和已预约容量保留，工人停止且不重复发送。

六项原handoff bytes与两早读观测作保字节编码，context摘要从外部固定值核对；只交付一次，不新建claim、预约或输入权限。离线链路已走通：原bootstrap替身handoff→单次消息交付→原session采纳→原六阶段opaque后端→broker代写/回读原C/g/权重。当前消息MAC只证明配置密钥下的消息一致性，**不认证Owner、真实父进程或OS peer**；真实密钥与保护通道尚未发行/安装。

新增12项协议、6项集成检查通过；相关旧输出预算12项、bootstrap19项回归通过。初始7/11/5等中间轮有重叠，不与最终组相加。覆盖篡改/反射/重复/外来record/分区/帧与消息上限/回包丢失/无重试/禁止直写回退/配额镜像/两8 KiB早读/原handoff/原始C-g往返。真实Win32、Job、科学后端均未调用，自审不替代独立科学审查。

## 当前来源下的实际A准备

原58源码中只有输出预算工程模块发生变化；算法/网格定义/controls及科学源码不改。新增来源伴随记录重新核58文件/134静态内部边；独立启动/通道支持另有代码候选，不称完整执行依赖闭包。当前58文件实际字节均匹配最终候选Git Blob；最后仅通道codec变化未影响这58文件，故未为恢复重跑该组装。

用当前原模块分别做本进程父端准备和worker重建：各58模块，两个命名空间共116次原模块编译，32实际依赖对象；父端404/工人414次显式导入分列，不累加成单工人观察。重新创建原类型A请求/inputs/record/context，恢复同一封存grid/参数/controls，worker session仅PREPARED。新传输139189/startup125303/外部启动包380644字节。

原A包SHA256仍8ed0fb98445ed02debfee0a971e0c728dbd583f6cc323ccfba22406b8191b225，grid仍1cc6002840d6a3dfef899c98d09f4796a8e14ccb9116a7952cdf78ab50305258。原快照、工资、向量、标量、context保持，没有重算科学值或生成网格。因当前工程来源已变，新增候选合同/输出身份描述；旧合同、target及原工件不反写。固定scope及原ledger/anchor保持同一，不换ledger续额；结果目录仍空。候选worker仍是拒绝运行的休眠入口，不是可运行科学worker。

实际A未绑定通道、未发行真实密钥。counter事件、输出操作、预约、保存输入交付及bootstrap读取均0；HA实例/初始化/HJB/KFE/原汇总、真实OS后端、实际外部进程、科学worker、新科学attempt均0。3次版本查询子进程请求被拒绝。15实际预算/批准次数/运行决定null，NEW_RUN_BUDGET=0。运行/科学/Results/REAL_GE/激活/producer/执行消费、正式环境/跨进程资格、完整计量/live enforcement/native写保护继续FALSE。

## 剩余完整worker工程

下一步仍是普通工程：为现有协议实现真实受保护IPC及OS peer/同record身份绑定、接当前环境和Job/进程证明、实现工人不能绕过broker写入的OS限制，然后接入最终精确capsule。当前broker只约束已路由IO，不覆盖native/其他直写，不能作为最终有限运行请求。不得只凭MAC/JSON/PID观察或Job内存限制宣布这些缺口关闭。

针对OS限制已核官方资料，但未采纳成新Owner决定或执行：Microsoft [CreateRestrictedToken](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-createrestrictedtoken)说明WRITE_RESTRICTED的写访问语义及受限应用的桌面隔离要求；[Restricted Tokens](https://learn.microsoft.com/en-us/windows/win32/secauthz/restricted-tokens)说明双重访问检查；[CreateProcessAsUserW](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessasuserw)仍有权限和有效标准句柄要求。不能据“受限自身token”推断免除全部权限，也不自动提升权限、改历史保护ACL/桌面或转凭据启动。此处仅确定后续实现约束，没有调用这些API或检查用户凭据。

Owner工程自主权/A优先级/首次返回A/长期中小网格许可均已定，不重问；AUTO_NEXT=FALSE不阻塞授权内工程，网格许可不发HA预算。主路线及HA黑箱、a*r_a/净工资/同inputs/正式post→原KFE→原归一化、原C/g逐格Frisch→原g权重→A1 pH/无额外z/税/H/Lt_prev保持。真实p/单位/激励、RP、外层停止及严格科学标准不补默认；真实保护/可信有限消费/失败留存/最终有限决定仍必需。

本轮147件选定基线145件保持，只变工程输出预算和测试helper；原七未跟踪及fixture原字节保持，旧manifest/机器证据/STOP/关闭额度/16义务/保护不改。源码/测试/机器/私有包仅本地；只同步本报告/短状态/工作流/交接四份脱敏文档。无reset/stash/clean、强推、合main、删分支、搬移证据、重绑保护或全局配置/memory修改。最终HEAD与逐文件回读见本地交付回执，API快照链不强推求同。
