# Chapter 5 当前交接
更新：2026-09-09。唯一仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Owner最终科学authority；ChatGPT Reviewer规划/验收/发布；Codex Builder默认`gpt-5.6-sol / medium`。

## 当前入口
先fresh读取live main、AGENTS、规则索引和当前状态。
当前状态：`TEMPORAL_CONTRACT_IMPLEMENTATION_ACCEPTED__V2_ROLLING10Y_SAMEYEAR_ZT_STATIC_PASS__OFFICIAL_2018_DATA_STILL_BLOCKS_SCIENCE`。
当前 active task：无。Results eligibility=FALSE。

## 已冻结并实现的合同
Owner采用PLM rolling 10-year：2009=2000–2009、2018=2009–2018、2023=2014–2023；`steady_year=2008+ii`；同年level row=`ii+9`；PLM estimator/workbook保持；Zt公式保持但使用稳态同年GDP/CAP/POP。

Python annual/pre-model层已实现`CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`。2018静态corrected binding：analysis/data_MAT 10/10，row19/year2018，vintage19，window2009–2018，Zt2018。安徽index仍Python11/MATLAB12/Excel N；provisional输入GDP=34010910.0、POP=607600.0、CAP=1357314108201.3684、alpha=.772866243094144、IND_Zt=.0006934646534806338。

V2 metadata/source-hash合同拒绝missing、V1/legacy、内部不一致和hash mismatch。ii15旧cache alpha=.967775174774325不能覆盖当前workbook值1.0219847778591。原MATLAB源未修改，已有patch spec。

## 验收证据
候选`6746565506eb953ea599536d3f745764d225ffef`已接受。Scoped tests 22 passed；manifest 32项匹配，SHA256=`F529EF14096482734BC2FB98E90A739F2BBEF5D6AE23CE3D6B3AC8F1D8C10910`。历史annual-driver收集因受保护oracle身份不匹配在测试执行前停止，保留失败日志、不计入PASS、无模型调用。全部科学调用=0，仅构造2009/2018两个静态pre-model对象。

## 当前最高优先级blocker
2018输入仍是`PROVISIONAL_AUDITED_SOURCE__OFFICIAL_VERIFICATION_OPEN`。安徽2018 GDP、常住人口、固定投资/资本存量链尚未完成官方来源身份闭合。在此之前不运行新的2018 household/HJB/KFE/firm/GE/annual，不调GovInv/alpha，不继续扩大bmax。

2022–2023六个负资本/复数log是独立问题，不进入下一次2018小规模验证。

## 路线
官方2018数据身份闭合 → 真正2018单年小规模科学验证 → 若仍高收益/不收敛，再审计GovInv外层适应速度 → household/KFE有效性 → 有限省份 → 年度覆盖 → MP5/MP6动态。

生产网格仍I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。历史rah=.09/.07、KFE边界、Qh负率、P32/sigma和b域实验只代表旧混合年份输入。
