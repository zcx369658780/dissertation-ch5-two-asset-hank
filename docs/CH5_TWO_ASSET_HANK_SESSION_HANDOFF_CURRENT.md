# Chapter 5 当前交接
更新：2026-09-09。唯一仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Owner最终科学authority；ChatGPT Reviewer规划/验收/发布；Codex Builder默认`gpt-5.6-sol / medium`。

## 当前入口
先fresh读取live main、AGENTS、规则索引、当前状态和active task。
当前状态：`TEMPORAL_CONTRACT_AND_ZT_LEGACY_AUDIT_ACTIVE__PLM_PRESERVED`。
active task：`tasks/CH5_MP4C_TEMPORAL_CONTRACT_AND_ZT_LEGACY_AUDIT.md`。
Results eligibility=FALSE。

## 已接受的数据审计
`f850937ccb7b11b835ce5e45b9819ee25412ad03`已接受：所谓2018的`ii=10`实际消费2009水平数据；同时使用regression vintage19 alpha和固定2020水平行构造Zt。填充数据还存在endpoint风险和2022–2023负资本/复数log_pcap，但这些不是当前2009来源call725的直接原因。

## Owner最新澄清
原年度设计意图不是从2000直接求稳态。PLM需要历史样本，因此首个目标是用2000–2009样本估计用于2009稳态的技术对象；后续年份应使用截至对应稳态年的估计。去年在`load_GDPdata.m`等代码里准备/比较过其他估计方法，但PLM效果最好，所以当前继续保留PLM，不为收敛改估计器。

Owner怀疑Zt固定使用2020水平行是遗留代码，而非有意基准年锚定。

## 当前任务
零模型调用复核时间合同：验证`steady_year=2008+ii`，验证同年水平量是否应使用`ii+9`数据行，核对PLM vintage/sheet是否已经与扩展估计窗口一致，并静态追踪Zt固定2020行的来源和替代分支。若没有文档化经济依据，将其分类为likely legacy fixed-year anchor，并给出最小source patch plan；不执行patch。

当前禁止HJB/KFE/household/firm/GE/年度/MATLAB/root/direct/eigen等科学调用；不修改原始Excel/MAT、生产loader、PLM方法、alpha/GovInv、bmax/amax或边界法则。

## 路线
时间合同冻结 → Owner接受Zt年度语义和必要官方数据口径 → 最小年份索引修复 → 真正2009/2018单年小规模验证 → 若仍高收益/不收敛，再审计GovInv外层适应速度。不要先用收敛算法补偿错误年份输入。

生产网格仍I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。Owner历史经验：真正收敛稳态Bt基本在0附近，b=12只保留压力测试。

工作目录：`D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001`。数据审计外部证据根：`D:\ProjectTemp\ch5-2018-raw-data-audit-20260909-007`。历史证据继续保护。
