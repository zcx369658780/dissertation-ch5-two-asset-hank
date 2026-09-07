# Chapter 5 两资产 HANK 当前状态
更新：2026-09-08。唯一活动仓库：zcx369658780/dissertation-ch5-two-asset-hank。
最新已接受诊断提交：8ef4a2a6c6df2ece2cda665890201c27dd083265。验收前live main为c90bb26fb17f03dd9f45cea668d9e65a9ea22f43；均为证据锚点而非永远最新main。

## 当前Owner方向与活动任务
状态：PRICE_AUDIT_PARTIAL_EVIDENCE_ACCEPTED__ORIGINAL_PARAMETER_PREFIX_OBSERVATION_ACTIVE。
Owner要求保留原MATLAB算法、a_bar和现有设置，先查rah/工资触界与原自适应机制；D1–D3修复target未采纳、未实施、暂缓。
保存证据审计已完成并验收，仍为PARTIAL_EVIDENCE。验收：docs/CH5_MP4C_PROVINCE_PRICE_BOUNDARY_AND_ADAPTATION_AUDIT_ACCEPTANCE.md；执行报告同名前缀_REPORT.md；摘要reports/province_price_boundary_audit_20260908/。
活动任务：tasks/CH5_MP4C_2018_ORIGINAL_PARAMETER_OBSERVABLE_PREFIX_REPLAY.md。
仅授权一次原输入原算法Python观测前缀，补捕获实际ra0/wt0/mt、完整共同旧状态和控制器事件；首次异常、原提前收敛、超时或家户call725结束即停。至多24轮入口、23轮完整one-turn；不跑到年度成功，不改价格/参数，不做.07敏感性，不启动MATLAB。预算见exact task。发布不代表已启动本地计算，尚未收到新任务完成报告。

## 本轮接受的价格与调整证据
失败路径是PID67056捕获运行，不与原8worker失败或observable retry拼接。725条入口记录覆盖第1–23轮各31省及第24轮前12省；不是725次成功家户求解。可重建第1–22轮全国gap；第23轮只有12省后态，全国最大值及决定省缺失。未保存的失败路径ra0/wt0/ra/wjt/mt/current household Lt等不填造。
年度终点分组：Owner-A修正403省年，工资上/下界225/120；旧runtime-cache465省年，18/400；两组ra触界均0、rah>.07均0。868行同阶段派生raw经clip与保存价格比较通过，但派生不是runtime捕获，端点结果不是所有中间价格都安全的证明。广东/江苏主要触工资上界；Owner-A海南/西藏/青海/宁夏13/13年触下界。源码收敛谓词不排除工资触界，历史特定配置接受不因此自动撤销。
安徽2018输入外省投资比例为0；非初始化入口2及7–24轮rah=.09，3–6轮=.02，7–24有18个连续已观察高界参照接触。call725 rah=.09识别第22轮厂商ra=.09，不能确定缺失ra0是严格超界还是恰等上界。SUPPORTED_LINK仅指这条滞后传递，不是高rah导致不收敛的因果证明。
原自适应确实运行：第4轮安徽GovInv54313245.2543264降至48881920.728893764；产出远低于目标时Zt从.000641551386937363重置为1.1943048929490467。此后多次GovInv*1.1。第22轮全国maxKNratiogap=.11947876361194498，由贵州决定，开关关闭。第23轮捕获的国资/生产率变化支持调整已执行，但全国最大误差未知。第24轮KFE异常发生在完整household batch返回前，本轮厂商及调整未执行。
第23轮安徽厂商使用Zt=.7163967429125945、GovInv115261012.11434016；Yt36636882.21977386、Kt115362461.89160682、Lt_supply3210665.858026796，Y/K=.317580620411841、派生Kt_supply101449.7772666663。之后GovInv增至126787113.32577418，Zt变为.6650485431957093。不同阶段的GovInv/Kt不能相减判断负资本。当前household Lt和旧firm Lt不是同一操作数，不能错代以补出raw价格。

## 审阅范围及证据保护
候选相对c90bb26 ahead1/behind0，27个新增文件均在任务允许路径，无生产修改，远端分支SHA核对。Reviewer读相关源码、报告/摘要、年度计数、控制器时间线、13项测试定义及实际13/13日志；L3提交/报告审阅+L4已发布日志检查，未独立执行测试/模型、读取Windows原始文件或重验全部45条manifest。Builder回执manifest SHA256：BD6BA6AF6BF20F9E10CAB87F1B8CBD00BB93853685018FAD3A57D55857BC9968。
有效证据根D:\ProjectTemp\ch5-province-price-boundary-audit-20260908-002。-001错误后处理曾将旧firm Lt代入current household Lt，191项传递不匹配已明确INVALID并保留，不是模型新发现。两次均为后处理，原任务新增科学调用及MATLAB启动0。
CAPTURE_TIME_RAW_HASH_GAP_REMAINS__RETROSPECTIVE_CURRENT_FILE_INTEGRITY_CERTIFIED仍成立；本轮读取不补造捕获时哈希。新观测运行需独立归档；只有已比较匹配的前缀才能支撑历史路径的对应解释。

## 原版源码口径
源码复核：docs/CH5_MP4C_PRICE_BOUNDARY_SOURCE_REVIEW_20260908.md。Owner zip SHA256 CEB94CCF34D2D218722B81E5111A8F4C530571A9F886BD4AFE0610A00321F755，32个.m匹配MP0库存；所含MAT为旧校准cache，无年度st。
原始ra0/wt0先计算，后clip为ra=[.02,.09]、wjt=[.8,1.3]；rah/w是家户输入，不直接套厂商硬边界。全国maxKNratiogap<.1且steady_state时才调整；ra>ramax-.02时GovInv*1.1，ra<ramin+.02时*.9。约.07/.04不是新收敛标准。初始化ra=rah=.09、wjt=.6单列。rah在新firm前使用旧ra产生。
资本是源规定的At*N分配与GovInv，不擅加缺失的本地项、不用At+Bt。权重和可小于1，不暗中归一化。firm Lt_supply与household Lt区分。

## 仍未解除的数值问题
独立完全共同初始化轨迹为MATLAB143步收敛、Python500步不收敛，尾100步约.00862持续切换，未证明极限环。该实验与新原生初始化的生产前缀重放分开。
M143_FINAL两端仍有18负非对角元和15泄漏。14/14保存快照预算/捕获漂移一致但都有上界向外预算漂移；边界规格15f51be9只作为诊断和提案接受，D1–D3未采纳。停止标志不能证明算子有效。
P32内点极大transfer/cost和M对角sigma丢失未解决。固定线性2ff3eb2中精确共同M/RHS四组仍FAIL；固定输入solver路径差异与输入微差敏感性并存，向量范数不是因果占比。ROW_POW2未普遍改善，不采纳；80位残差不等于80位解/条件数证明。不反复换solver或调容差追求1e-13一致。

## 历史接受与锚点
- raw-vb40/40为保存阶段差异：e98bfad214b0c85005fac2ce23b1e4585a20e634；主比较为边界覆盖后导数，非生产修复依据。
- 首轮25e5db97a0239d956d572359db5835cec945962f：53/53；V1最大差3.9968028886505635e-15；当时Reviewer独立15项测试。
- 多轮dedd0f8e5fa894b83c8b20e522d66893e7b6b377：第2步consumption、第3步更新V、第4步输入V超界；第24步离散分叉；共同第二步38/38。每端2次调用，MATLAB144/Python501次求解；当时独立4项可移植测试，2项Windows依赖未重跑。
- 四状态b2d7a814039a585b696d8cc5079b8b9865017501：M24/P24/M143_FINAL38/38，P32首差V1后统计量36/38；每端4次单步。M/RHS当时仅容差内一致。
- 固定线性30438ea1468ddc59862f40574bd06c8625427e1b及2ff3eb212ea9a0d101183f9ff49dd1043bb6b886：每端4次直接求解；此前Reviewer校验11项日志原字节/LF，未独立求解。原manifest A0FF925E71273345043ACE4F666E07A4C990116E7F7BF6BDC1011853A1C64BDD。
- 边界规格15f51be9733b5043e738d3e522b97554e95902b9：2,256异常快照行、112角点、112面；不等于独立经济状态/全为bug。188局部单元1,128标量重建；模型0调用；首轮失败保留，最终10/10为Builder日志。manifest3D243B94BF048FD749FDCD1A3B46662EA862A09AE9B67E277139D3FD58F98B90。
- household特定fixture及MP0–MP3历史限定接受继续保留，不升级为所有经验输入。
历史预算已消费，包括未持久化调用；本页不是累计科学调用表，旧任务不能重跑。

## 年度口径与后续
旧protected runtime-cache Python2009–2023的15/15年、465省年历史接受；不代表全部跨语言parity。Owner-A修正2009–2022共14年中13年PASS、2018失败，完整覆盖未接受。相关原年度/observable retry/termination报告继续为证据。
后续：一次原参数有界观测补齐实际厂商/调整证据→判断可区分的原因和必要科学选择→新task下验证→恢复修正2018及年度覆盖→独立动态规格/集成/稳健性/Results。价格关联不替代利率因果实验或数值有效性；不把顺序比较静态称为真正IRF。Results eligibility=FALSE。

## 身份和本地保护
HJB保护SHA256049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE；export blob9e7dc9556a2b76811e78f89999abecc045886106。
隔离共同初始化MAT SHA2561718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81；scalar binding SHA256A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6；不得替代年度原生初始化。
原2018年度input SHA256F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0。
工作目录D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001；原checkout及70未跟踪文件保留。本地docs-sync d2f3e6e7cc21fffe8807f577ec2262bb77afdc07已完成，不重开。所有此前证据根保留；新任务使用独立observable-prefix证据根。Reviewer未直接检查Windows目录。
