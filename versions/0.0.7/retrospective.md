# V0.0.7 复盘：从工程源合同过渡到可证伪的经济量纲问题

2026-10-15（Asia/Shanghai）

**终态：`CLOSED__ACCEPT__HISTORICAL_SOURCE_CROSSWALK_AND_ECONOMIC_UNIT_CRITICAL_OBLIGATIONS_ONLY__WITH_OBSERVATIONS`**。固定计划`635cea1c54afecc78d6678805a263a889985a291`，接受候选`d8bb49d86ea674ea4ff5e3fdf03929baa08a6514`（tree `9b685397ad5bc76a4ac3bf4203776389742c5ec5`，唯一parent为`198b70f8b1c7b802bc2e18cb4bb0825bdb495b00`）。一次普通non-force远端候选发布，GitHub核实恰三份新文档，未变科学代码/测试、未合main。

## 进展

V006已把五字段、三轴和年度双消费者做成synthetic工程，V007不重复测试或再封一层合同。本版在历史C8已经独立核过5,141成员manifest的事实基础上，用一份详细经济学报告形成可证伪关系：household `Lt`对destination `Lt_supply`；`Govinc`的`Lt*tau`计价；`AtTax`和`Tt`家庭均值到地区财政总量的桥；`At*N`、2017/2018与模型期名义货币的条件必要式。Python caller中`Lt_prev`被同一轮household均值覆盖是已核实的静态实现事实。完整经济单位与真实C8数值仍未证。

Astra在本轮另对Owner上传的原版MATLAB ZIP做单次只读辅助文本对照：`HANK_mp_1turn.m` 的家庭→按N放大迁移→firm顺序与`HANK_firm.m`使用`results.Lt`为旧劳动吻合，未见中途恢复旧地区firm劳动。`HANK_2ASSETS_HJB.m`显示Tt家户流、AtTax分布均值，原firm财政式也有Lt*tau、AtTax和Tt。由此进一步缩小“只是Python移植层误写”的解释空间，但原ZIP不是历史C8当时运行代码，不能宣布实数BUG已确认。

## 过程观察及限制

- Codex独立隔离候选、三白名单文档、UTF-8/LF与JSON校验、一次集中push符合V1.2。公开PRE_SEAL刻意不填封存后的SHA，最终远端候选身份由Astra直接读GitHub；本地delivery回执、原dirty/index保护与资源只能按Codex转述分账。
- 旧固定Git对象在本地不全使cat-file一次exit128；随后仅用GitHub只读恢复，未为方便而fetch/checkout原共享工作树。TextEncoder工具环境及PowerShell白名单包装器失败已披露并在普通范围内修正，初失败保留；未导致越权科学调用。
- 完成报告比预定快；Codex报告约10.5分钟、总新增15,335,719B，缺连续存储簇、瞬时峰值和独立Windows原始计数；仍不冒充全部资源遥测通过。
- 分阶段37文件保护访问需要新Owner许可，manifest实际字节长度未知；A16/window是完整敌对保护未证而不是可以为只读自动豁免。一次普通A阶段被动读取如有机会也必须准确安全合同，但不再启动备份/G0/A16微任务。
- MATLAB辅助源码现在可以在Astra这一侧阅读，无须因Codex本地无法读就强迫Owner再上传一次同一ZIP；未来需要校准/模型公理/官方统计证据，须另行限定与授权。不要重复V007 SOURCE_ONLY写作。

## 后续优先级

优先科学解决两个“可以判真伪”的经济问题：劳动平均/总量及迭代旧期含义，和地区财政各项人口与工资计价桥；取得共同单位法则之后再决定是否需要修改科学模型或以真实C8投入验证。A阶段manifest历史字节认证独立列新访问门，不能替代经济理论决定。既有R2不达严格收敛、C9调用账与A16/window风险继续独立关停。

CH5_WORKFLOW_V1.2无需升级。V0.0.8 NOT_STARTED；未经Owner新决定，不自动签发数据权限、合并main、科学修订或启动新模型。
