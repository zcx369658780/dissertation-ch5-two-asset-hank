# CH5 TEMP31｜2018规范数据、31省修正模型实装及10/20轮价格边界诊断
TASK_ID=CH5_TEMP_V010_31PROV_CANONICAL2018_CORRECTED_PRICE_10_20_20261022
REVISION=ISSUED_20261022_R1
OWNER_APPROVED=2026-10-22
AUTHORITY_BASE=d401df1b54e522fad184c60ea121dec0387a1f33
REVIEW_BRANCH=review/ch5-temp-31prov-canonical2018-price-10-20-20261022
REVIEW_PARENT=d401df1b54e522fad184c60ea121dec0387a1f33
REVIEW_TEMP_PATH=_review_tmp/ch5/temp-31prov-canonical2018-price-10-20-20261022/

## 一、研究目标与不可变正式科学界
Owner批准TEMP改为真实31省，不能以31份双省合成数据代替。优先实装已接受Python修正：家户与人口/总量单位、31×31省际劳动力迁移与资本份额、企业原价/裁切、GovInv/Zt、资本组合、财政及已认证的旧轮/本轮状态。正式V010冻结，不变更原HJB/KFE/FOC、数值算法、论文Results，不授权正式31省GE或IRF。唯一首个TEMP31参数ARM；首10轮，条件合格最多20轮。运行/验收后必须与Owner讨论，不得自动下一组参数。
31省2018规范数据为本轮暂定的唯一可取输入。旧MATLAB标2018的源其实混用2009 GDP/CAP/POP、2020 Zt，不可使用。历史2009 corrected MATLAB/Python31省184轮一致性只作静态参照，不能声称本次31省自动收敛。

## 二、来源和单位硬门
治理migration/astra-workflow-20261012同一live HEAD读取CURRENT/TASK_CURRENT/DOC_INDEX及issue manifest，冻结合同与参数Git Blob。锁定Python模型commit 94de4501dec051b969bee9d852eba2d4591f30ef；逐件验证：
- src/ch5_two_asset_hank/multi_province/mainline_household_runtime.py = 3d2d7d92aea0036f36d88ef15c05cbb3b40eba90
- src/ch5_two_asset_hank/multi_province/migration_labor.py = ed71689bd4e2c7cee2c0d59034781309d73f8b7d
- src/ch5_two_asset_hank/multi_province/capital_network.py = dbb182f63ac62fd0cd8495463239c8e8c246a61b
- src/ch5_two_asset_hank/multi_province/one_turn.py = 4242cf787d8c30bec7ac884dcd9e24bcea288c28
- src/ch5_two_asset_hank/multi_province/steady_state.py = 5fa6c73884067391bd2b998d4b050443c97c38e8
- src/ch5_two_asset_hank/multi_province/firm.py = 3b902a2c62df816bdb85b0e09b127f1b7a547130
- src/ch5_two_asset_hank/multi_province/wage.py = 1459d1b465f134a2d8746c252e71e060459465ca
- src/ch5_two_asset_hank/multi_province/fiscal_diagnostics.py = 663e7e4a944d78392695c81062d97d961491ed4f
HA blackbox参考commit216283cf4f1303afa60f1915e143a0b7303a9ffb，exports/matlab_faithful_two_asset_ha.py blob9e7dc9556a2b76811e78f89999abecc045886106。正式versions/0.0.10/plan.md blob85138d8859d53295262fe13bf5bc277bca95ed3f只读；不将MATLAB-faithful受界诊断与正式corrected V010 solver混为一类。
唯一许可的私人数据是同年2018规范工作簿只读确切路径 D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx；预期SHA256=AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67。仅读取来源已归档的31省2018 GDP/POP/PIM capital/PLM alpha/Zt和质量/单位列，不扫描其它protected C8/2018/历史MATLAB缓存，不公开.xlsx。路径/哈希/年份/省份顺序任何不符直接STOP_DATA_SOURCE。不得自动回退到2009或混年2018。
文档docs/CH5_MP4C_MULTI_PROVINCE_STEADY_STATE_CALIBRATION_AND_INITIALIZATION_REDESIGN_SPEC.md提出MU=10万元、NU=100人、GDP亿元×1000、PIM资本万元÷10、人口万人×100，但状态PARTIAL，特别家庭资产a/b网格到At*N的asset_bridge、企业工资/收益界同单位尚未被Owner正式裁决。先建立31省unit_authority.csv确认有新鲜正式采纳来源，若资产桥或价格界单位无源可证，STOP_UNIT_BRIDGE_UNRESOLVED且HA=0。不能假设系数1/100/10000或临时扩大上下界。

## 三、31省TEMP候选实装
BOOTSTRAP0先核可信D:\ProjectTemp父目录、唯一scratch不存在、reparse/符号链接身份、protected Git/index/common-dir；BOOTSTRAP1仅在 D:\ProjectTemp\ch5_temp_31prov_canonical2018_price10or20_20261022_01 建立工作区，首次写前复查。严格不写正式V010、旧数据、旧journal或其他项目，不部署原生产Budget派生补丁。
只可实施明确已接受的修正并逐项记录source_SHA/Owner决定/变动的函数与公式/验证结果到accepted_corrections.csv；不能引入V008/009 Newton、K2或未经采纳的双边归一化劳动替代。每省家户Ct/At/Bt/Lt_HA/AtTax人均量×N恰一次；31×31来源i与目的j的phi[j,i]、目的地tau[j]仅扣一次、Lt_mat[j,i]目的地行和为企业Lt，不二次×N，区分Lt_HA和Lt_prev/Lt_firm；资本S[j,i]列和1且包含本地保留1-theta_i、K1B外省softmax beta_distance=2 beta_return=.5、前完整轮raw-ra0 zscore ddof0，Kprivate_j=sum_i S[j,i]*At_i*N_i，rah_i=sum_j S[j,i]*ra0_raw_j，同一S用于数量与收益；firm Kt=Kprivate+GovInv，ra0_raw/ra_used、wt0_raw/wjt_used和裁切补偿分别记录；Zt/GovInv原收益界更新及tKN阻尼0.6/0.4不变；目的地工资税一次，家庭人均AtTax/Tt乘N一次，already-aggregate的公司税/GovInv收入不再乘N。不可为跑31省改变HA网格/效用/税规则/上下界。
首次HA前通过无HA矩阵轴置换、财政量纲、31来源守恒、32×? 禁止错轴、重复乘N、收益lag等确定性oracle，及本任务新scratch单science runner的预算/STOP/进程回收测试；真实生产GLOBAL_STOP依旧UNVERIFIED。缺单位/可信STOP/正确源必须STOP_BEFORE_HA，保留真实未决表，不用mock充数。

## 四、唯一2018年31省10/20轮
此ARM用2018 canonical原始参数N/Zt/GovInv初值scale全部1，不主动调任何参数。每完整轮31省各最多一次HA，前10完整轮；真正非有限/危险KFE/错误/预算溢出立即STOP，部分轮不入比例分母。HJB source D不收敛的有限postloop在上一TEMP协议允许且本轮KFE质量可靠时只能标TEMP_DIAGNOSTIC_NOT_STRICT_HA，绝不能算正式V010稳态PASS。
第10轮若完整10轮，先验联合恶化门：第8—10轮maxKN gap均值>=1.2×第1—3轮且maxY gap同样>=1.2倍，且第6—10轮至少4轮31省中>=16省有任一企业raw ra0或wt0越界，则10轮停；否则只在同一进程、同一账、安全/资格/时间足够时继续至20轮。不得自动第二年份、第二ARM或调整参数。
外层最多20、HA/HJB启动<=620、KFE进入<=620、science driver<=1、每HA HJB updates<=100、roots<=400000、全局roots<=248000000；失败同样计费。

## 五、必须提交的两张全省逐轮表
price_rounds_31.csv每省每完整轮（最多620行）记录省名/年/轮/N/Zt/mt/原始wt0与企业used wjt/上下界、原始ra0与企业used ra/上下界、rk/divrate、家庭rah/w_eff、原变量身份/单位，分别给上下界真命中raw>bound或raw<bound，不把used==bound误判clip，不把家庭参考区间当家庭实际clip。每省1—10轮和全轮命中次数/比例、首次触及、首轮开始或后来撞界、持续/反复/返回内区、原价距离边界；每轮全国多少省上/下界/31、最严重省份及分位数。
firm_household_rounds_31.csv每省×轮记录厂商Zt,Kt,Kprivate,GovInv,Lt_firm,K/L,Y、家户At人均/At×N、Lt_HA人均/N×Lt_HA、目的地Lt_mat行和、31×31资本S列守恒、财政桥残差及source/units/time；Lst未有源码映射则UNMAPPED而不是编造。ha_status_31.csv和national_rounds.csv保存每省HJB D/B/KFE、部分轮、max KN/Y、早停决策。另需31省markdown汇总表、t=1,5,10,15,20及转折轮、source unit及代码集成差异表；不能造缺失数据。

## 六、执行预算和交付停点
wall<=28800秒（源/单位3600、工程7200、科学14400、交付3000、封存600），工程Python<=20启动、direct<=90、E1<=2批仅无科学方程变更的确定性修复，科学driver<=1，HA/HJB<=620，KFE<=620，scratch新增<=512MiB，独立clone objects<=2GiB，旧预算0。对文件、命令、进程、重试记首次错误和实耗，无法观察系统kernel子进程记UNKNOWN。
Codex必须自动将result.md、manifest.json、evidence_sanitized.zip三原件脱敏发布到独立Review分支 review/ch5-temp-31prov-canonical2018-price-10-20-20261022 目录 _review_tmp/ch5/temp-31prov-canonical2018-price-10-20-20261022/，唯一parent=d401df1b54e522fad184c60ea121dec0387a1f33，nonforce，Git API写<=8次、发布<=1次、公开三件<=5MiB、展开<=12MiB、成员<=64；每件Git Blob/SHA256/远端完整原字节/ZIP所有CRC、size、SHA256逐项回读。平台401/403/429或安全拒绝硬STOP，不切换账号/SSH/代理绕过。三个历史PENDING ref f8db0251fb98f2b157affc9bf7391895b86edba0、4e05976bbc8068b971ba5915133e9a6c3b73193d、1579e7f1d7a1975c322dd6ae9af1776e88e83e7c全部留存；Astra独立终审归档远端回读后仅精确清理本轮Review三件，PENDING保留。
最终run_id、actual_terminal、全部矩阵/价格/单位门、原始JSON Base64/bytes/SHA256和外部进程退出后完成事件。停止后WAIT_ASTRA_AND_OWNER_31PROV_PARAMETER_DISCUSSION；不得自动新调参任务。model_activation=False,REAL_GE=False,Results=FALSE,V011=NOT_STARTED,FULL_RUNNER_IO_CLOSURE=BLOCKED。
