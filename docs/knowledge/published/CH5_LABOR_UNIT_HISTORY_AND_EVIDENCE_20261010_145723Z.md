# 历史正文发布副本
源文件：CH5_LABOR_UNIT_HISTORY_AND_EVIDENCE_20261010_145723Z.md；原bytes=4892，SHA256=676E3650E3ABB9A4B1C15CEDADBEC37256D74360F5222BE171806B7F15FC9EE9。私有日志定位脱敏，内容不作新验收。旧流程和路由由 ../../CH5_ASTRA_WORKFLOW_CURRENT.md 替代。

# 第五章劳动单位：已恢复的Owner决定与证据层级

截点：2026-10-10 14:57:23 UTC（北京时间22:57:23）。
保存授权：Owner要求马上保存重要劳动单位信息到项目文档。本文件只记录，不改变源码、参数、经济方案或路由，不运行模型。

## 确定的历史决定
9月29日原会话01a0ec2a-e8de-71d1-aa90-e7990e45276c：
- 08:15:55 UTC，Owner明确N_i按人、不按户；每户三人只是可讨论近似。
- 09:50:20 UTC，Owner授权将A_i/N_i等讨论稿口径改成家户；助手明确范围是独立TeX讨论稿，程序、参数与冻结数值证据未因此改变。
- 10:02:45 UTC，Owner原话：“现在我们封存户均这个思路，把稿件改回人均（不然前期的程序参数校准部分又要重来了）。”
- 10:13:53 UTC，Owner解释：人均劳动对应人均资产和人均收入，可以穿透家户成为统计量；家户不严格等于三个人。
这是已恢复的决定：户均方案封存、不实施，人口/人均方向恢复；不得再要求Owner重复选择人还是户，不恢复N=P/3。
原话来源：LOCAL_ONLY原会话日志（见来源会话/行号），Owner撤回在原始line538，补充解释line626；助手随后复核line758/781。时间均原记录UTC。文件历史记录未授科学运行。

## 人口统计对象与数值尺度分开
“按人口、不是按户”确定统计对象；NU_100_PERSONS确定数值尺度，二者兼容。若该合同适用于当前路径，N=1代表100人，不能直接写数值单位为1人。
9月29日助手源码核查记录：2018人口列“万人”乘100转为NU_100_PERSONS；货币MU_10WAN_YUAN=10万元。该记录是历史源码核查，不是本Work当前磁盘核验。
当前另会话01a0dcd7-2acc-7571-b292-5807a0be0b1d（标题“第五章 K1B 静态 runner 审查后接续”）创建于9月26日，但Owner贴来的劳动源码核查实际是10月10日turn01a1263c-77a0-7a92-a6d8-3e6b8b0b4ae2，而非9月26日核查。报告其读取D:\ProjectTemp\c5k1bturn56、HEAD a1db8c1，并指出corrected_2018_runtime.py仍标NU_100_PERSONS。
本Work本轮核对了该会话回复与历史对话，没有新读取上述Python源码或数据，也未Git核验其HEAD。因此这属于EXTERNAL_SESSION_SOURCE_REPORT，不冒称本Work fresh sourcepin/current Python验收。
9月27日前序会话01a0dcea-8575-7231-b779-863e02a173bc（“核验K1B静态入口安全门”）交接曾把A_iN_i单位列为待讨论；9月29日具体决定才补齐人户方向。
记忆摘要只记录了先前户均尝试，遗漏后来的撤回；原Owner撤回原话优先。此文件不修改长期记忆。

## 不同劳动量保持分开
1. 个体劳动选择l：外部Python报告称劳动收入w*z*l，但时间单位小时/年未注明；不等于就业人数。
2. 家户分布聚合Lt/l_ss：外部报告给出积分z*l或求和z*l*p；尚不能把其模型均值直接称已核物理人均值。
3. 默认企业端Lt_supply：外部报告及本Work已接受旧MATLAB字段证据一致，迁移劳动矩阵按来源列乘N，再按目的地行和；firm局部Lt取Lt_supply进入生产。当前称“模型生产端劳动投入”，不自动称已识别效率劳动。
4. 单独命名归一候选路径：外部报告称可用household Lt*N分配；不替代默认路径，不因文件存在而已启用或科学采用。
本Work新MATLAB证据确认：HJB局部Lt含zzz*l*g及网格步长求和；results.l、results.C保存加权贡献数组，results.g保存含网格面积的数组。g除总和的文字不证明概率合法或运行归一成立。HJB局部同名Lt与firm局部Lt的经济身份不能直接等同。
人口尺度不决定劳动是人数、工时或效率量；“户数—人数—就业—工时—生产效率”完整桥仍未证明。家户决策单位与人口统计对象可区分，但实际状态分布未记录逐户人数的历史限制不能凭说明消除。

## 后续准确目标
下一推荐：独立新SOURCE_ONLY门核对D:\ProjectTemp\c5k1bturn56\src\ch5_two_asset_hank\multi_province\corrected_2018_runtime.py中的NU/MU合同、输入转换及初始化Lt/N文字，不读取CSV/MAT/NPZ，不import或运行。当前路径仅来自Owner贴文及外部报告，长度/currentpin仍UNKNOWN；新门须另签一次metadata/完整bytes/strictUTF8/hash/caps/预算，不自动沿引用。
默认/归一候选的当前路由若需核验，也应另签有限源码门。改变默认劳动路径、归一/校准/参数/重要guards或科学桥仍需准确Owner科学门。
已确定的人户方向不重问；科学机制、具体口径识别、数据可比性和运行仍NOT_SELECTED/NOT_ADOPTED或UNKNOWN/NOT_CHECKED。
本次新增文件不作科学采用；旧失败预算、C9暂停、ResultsFALSE和所有保护边界保持。
