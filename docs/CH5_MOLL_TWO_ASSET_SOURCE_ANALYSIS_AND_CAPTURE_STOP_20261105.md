# Moll两资产本地参考：容差与正式KFE代码核对、采集停止记录 · 2026-11-05

STATUS=SOURCE_ANALYSIS_COMPLETE__HJB9_CONVERGENCE_LOGGED__FORMAL_G_PRECISION_NOT_OBSERVED__CAPTURE_REPAIR_READY
OWNER_SOURCE_INSTRUCTION=请你分析相关代码，可以直接运行看看重构KFE的精度
OWNER_MAXIT_APPROVAL=允许，仅恢复35次上限
SOURCE=two_asset_kinked.m
SOURCE_BYTES=13412
SOURCE_SHA256=1f71d6bf53fd268946aa8a43ab481ee6e5c74437acede9a2362a1add44760878
SOURCE_PROVENANCE=OWNER_SUPPLIED_LOCAL_REFERENCE__NO_INDEPENDENT_OFFICIAL_SITE_BYTE_AUTHENTICATION

## 三个判断位置

1. 第269行是max(abs(sum(A,2)))>10^(-9)，即1e-9，检查HJB迭代中刚装配A的行和；超出后输出Improper Transition Matrix并跳出循环。这个检查没有覆盖后续重构的正式post A，也不是Vchange或KFE驻定残差。
2. 第24行crit=10^(-5)，第295行用dist(n)<crit判断Vchange的最大绝对值，即1e-5。当前TEMP31为1e-7，数字上小100倍；但参考Delta100、当前Delta1000，模型、单位与网格也不同，不能因此声称经济近似误差精确改善100倍，也不据此更改当前控制。
3. 第331行起稳态分布部分，第333行明确使用更简单迎风格式重构转移矩阵。从最终s/m正负部分构造BB/AA，再A=AA+BB+Bswitch。第391行转置A，第394行固定MATLAB索引1657、rhs=.01，第399行求解，第400–401行按da*db归一化。此段未见post行和、完整A' g驻定残差或密度非负性容差判断；不意味着完整其它原作者包/调用者没有判据，也不把前两个阈值自动用作正式KFE标准。

原脚本循环结束后无额外if-converged包裹KFE，因此达到迭代上限或因矩阵检查break后仍可能进入后段。正式KFE的意图是在V收敛后使用，实际判断必须先看本次V是否满足原准入。

## maxit覆盖及Owner批准的唯一科学副本变化

第26行设maxit=35，但第85行再次maxit=1。最初讨论中我把覆盖行误说为91，已按实文件纠正为85。Owner随后明确允许仅去掉该覆盖、保留原35次上限。原件3个科学文件未改；35次副本仅该行改为注释，其余字节保持。FOC/cost文件原SHA分别76cae4d...、b0a327a...，完整pins在私有回执。

参考为原100×50×2、b=[−2,40]、a=[0,70]、w=4、ra=.05、rb_pos=.03、rb_neg=.12、rho=.06、xi=.1、Delta100。它使用给定收入和自动转入非流动资产机制，与当前TEMP31净工资/内生劳动及20×20×2模型有实质差异。这里只认证指定本地文件并作历史参考运行，不做来源替换、网格采用、参数校准或完整跨语言等价声明；Python仍唯一主动主线。

## 两次已登记参考启动及真实证据

本次参考检验独立于旧TEMP31的7/7关闭门，预先登记每版本一次、零自动重试；每次180秒含启动、4GiB聚合Job内存及每进程4GiB、最多8活动后代进程，Job在恢复前绑定并杀死关闭时残留后代。仅复制3个指定.m、使用私有偏好/临时目录，不写原源目录，不修改全局/Desktop配置。

| 参考启动 | 实际情况 |
| --- | --- |
| 原样maxit1 | 87.859秒、峰值约.726GiB、6个Job进程、exit73，已清理；我添加的-nojvm使第80行plot不支持，未进入HJB迭代或KFE，基线没有数值结论；不重跑该意图 |
| 只恢复maxit35 | 53.922秒、峰值约2.136GiB、6个Job进程、exit73，已清理；HJB在第9轮输出收敛，最后日志Vchange约3.6618e-6、HJB段计时约5.436秒；原KFE/归一化段及后续绘图已执行，但外层保存失败，没有g精度见证 |

第二次启动使用此前尚未消费且Owner已批准的35次副本额度；只去掉启动参数-nojvm，保留原样失败证据，没有重跑maxit1版本，也未增加当时2次参考额度。MATLAB为本机R2022b，图窗隐藏；locale相关启动warning原样保留，不修改全局环境。

保存失败来自外层capture的which路径检查。MATLAB run在执行另一个目录的capture.m时会临时切换当前目录，而之前只cd到code、未把code保留在会话路径上；此时which找不到原辅助文件，校验在保存之前抛错。原科学代码没有报HJB或KFE错误。因为没有g数组/矩阵见证，不能把日志收敛、无报错或绘图执行当作KFE数值精度，也不通过重新求解来补造已丢失结果。

## 修复准备与新一次请求

已在会话内显式保留私有code路径，并准备在原科学脚本返回后、外部指标检查之前先保存原A/AT/g/V等见证。原科学副本、35上限、网格、价格、公式均不变。1个独立MATLAB工程夹具用人工数组验证路径、MAT、JSON和17位浮点文本保存，17.5秒、峰值约1.141GiB、exit0/清理确认；没有调用原two_asset脚本、FOC/cost、HJB/KFE或求解器。工程夹具的假数组结果明确标注，不作为任何模型证据。

两次原参考启动额度已用，修复后的真实g采集尚未执行。新提案仅请求额外1次相同35次副本、180秒/4GiB/零自动重试，先新登记再启动，完成后保存并计算正式post行和、A' g完整残差、固定行/其余方程残差、归一化和边界质量，随后停止。用户批准待定，未生成该次启动claim。

## 当前边界

本报告给出静态代码与真实HJB9轮日志，正式KFE精度仍NOT_OBSERVED，不声称参考g已认证。原件/活动TEMP31科学模块和旧证据保持，TEMP31 CURRENT原字节7/7关闭、零重试，无第8次主线决定/意图。旧余额和R12/R13/WASM6/保护重绑定及16项义务保持，科学接受/Results等FALSE、当前严格阈值仍null。原源/完整日志/矩阵/夹具LOCAL_ONLY；仅本地存档，GitHub PENDING_SYNC，不重试推送或切换身份/协议。
