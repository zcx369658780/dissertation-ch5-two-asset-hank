# 31省原请求工厂与冻结工件原类型接入

日期：2026-11-08。代码候选`5a46db64ccba3ea94dbd65535148fcef9f890a6a`。本轮完成[独立候选传输](CH5_PROVINCIAL_INPUT_TRANSPORT_20261108.md)之后的原请求工厂和原Python数据类型接线，没有运行HA或创建受保护worker。

## 完成的离线集成

新增outer_provincial_request_bridge。prepare_provincial_request_bundle读取完整候选包，在外部参数/controls文件pin一致、grid数据身份一致后，调用原outer_ha_batch_adapter.prepare_household_batch，得到原PreparedHouseholdBatch及31个原OriginHouseholdRequest/Temp31NetWageInputs。每个请求保留同一批次context和同一待验证工资记录，标量浮点位模式/负零、净工资与单元素劳动权重、只读向量不变，不再扣税或乘H/p/z。

grid组件只封装原保存的四份.npy字节。装载前先核小尺寸shape/dtype/载荷长度，拒绝伪造大数组/对象数组，再用allow_pickle=False装载并构造原MatlabFaithfulHJBGrid。网格按原shape/dtype/tobytes(order='A')定义重新核到`1cc6002840d6a3dfef899c98d09f4796a8e14ccb9116a7952cdf78ab50305258`；参数和controls原JSON逐字段/float_hex/canonical/file SHA核对后构造原EconomicParams、MatlabFaithfulHJBNumerics。原数组布局/标志保持，没有修改原工件、冻结定义或controls。

validate/select入口核同一原批次/工资记录/31请求及其inputs对象身份、原grid/参数/controls根对象、数组对象/布局/内容和标量位模式；相同值的新对象、负零变化、可写向量或数据篡改均不能静默替代。它是边界一致性检查，不是跨进程或native持续保护。

三类共享工件（grid封装、原参数、原controls）已有可回读的本地组件身份；另保存带真实冻结工件的31请求合成演示。示例利率/工资/转移是合成工程输入，不是从现实62条参考推得的省级值或新的科学采用。真实31省完整运行包仍0；没有填现实w/Tt/rb_gap或重绑A。

## 原定义与检查证据

检查使用已定位的本地Python及实际NumPy/SciPy依赖，原项目模块按当前完整源码在检查专用命名空间执行，绕过包__init__且不读写项目缓存，不抽取AST替代原工厂或数据类。实际原源码定义/对象的核对不迁移成正式环境、子进程、源闭包或消费资格。

最终10项集成检查全部通过：原31请求/共享record/只读向量，原grid和参数/controls类与身份，31路原索引/负零/不重复税，外部pin拒绝，伪造大尺寸/对象.npy提前拒绝，grid内容/数组/根对象/布局篡改，参数/请求对象及位模式篡改，全部运行/科学标志FALSE。当前测试与源文件摘要已绑定；此前未变15/13/14组不重跑，不累加唯一总数。

两次初始设置错误原样保留：检查器过早禁止标准库ctypes初始化，以及旧Python缺少Path.is_junction；两次实际tests_run均0。修正检查顺序与lstat重解析判断后通过，进一步补根对象身份检查后作必要复核。没有修改全局环境/安装依赖、放开项目OS操作或重试科学attempt。最终检查进程中3个只读版本子进程请求被拒绝，实际外部子进程0；旧环境资格不继承。原工资、初始化/HJB/KFE/原汇总、项目Win32/Job/科学worker调用均0。

机器记录在`validators/multi_province/provincial_native_request_20261108/progress.json`；完整检查、合成演示、冻结grid封装及回读观察仅本地。原六缓存和已消费execution_decision共七未跟踪及fixture原字节保持，既有冻结源/工件字节保持。

## 科学解释与下一工程

GDP/资本是外层/校准参考，不直接进入当前单省HA的数值调用；若利率、净工资、转移、借贷利差、grid和偏好等直接输入相同，省名不同不会形成不同数值问题。未来安排逐省点集时应识别这种相同输入，不能把同一数值检查包装成31个不同校准结果。本轮没有新增结果复用/克隆规则或将一个省份未执行的结果记为已测试。

当前原工厂接通适用于已有合法后续轮次工资envelope的准备路径；首轮候选视图不因此获得生成第0轮的生产证明，也未修改原首次bootstrap。工资收入比对仍是事后校准工具，不新增为首次A或单省给定价格HA的门槛。

下一完整工程是把同批真实来源/输入采用及原请求接入同record受保护worker：源码/生产者证据、可信父端/IPC/peer、当前环境/Job和native防绕写仍未齐。现有A专用入口/58源/134边与SavedOuterWageObservation不迁移给31省；A优先级、原PREPARED及原包/工资/快照/grid/参数/controls保持。新原类型检查不会打开公开运行门。

真实科学输入采用/31省完整包/HA测试省份/新科学attempt均0，失败数/比例null，原root/C/g未得；15实际限制/批准次数/运行决定null，NEW_RUN_BUDGET=0。运行/科学接受/Results/REAL_GE/激活/生产者/消费/环境/跨进程/完整计量/live/native保护FALSE。旧STOP/关闭额度/16义务/保护全部保持。源码测试机器及私有载荷只留本地，仅四份脱敏文档同步治理，不改main、全局配置或memory。
