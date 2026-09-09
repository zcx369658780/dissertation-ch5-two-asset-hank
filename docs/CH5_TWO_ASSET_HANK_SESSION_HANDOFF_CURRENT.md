# Chapter 5 当前交接
更新：2026-09-09。唯一仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Owner最终科学authority；ChatGPT Reviewer规划/验收/发布；Codex Builder默认`gpt-5.6-sol / medium`。

## 当前入口
先fresh读取live main、AGENTS、规则索引、当前状态和active task。
当前状态：`TEMPORAL_CONTRACT_MINIMAL_IMPLEMENTATION_ACTIVE__ROLLING_10Y_PLM_FROZEN`。
active task：`tasks/CH5_MP4C_TEMPORAL_CONTRACT_MINIMAL_IMPLEMENTATION.md`。
Results eligibility=FALSE。

## 已冻结科学合同
Owner确认PLM采用rolling 10-year window，避免过旧数据干扰生产力估计：2009用2000–2009，2018用2009–2018，2023用2014–2023。`steady_year=2008+ii`；同年GDP/CAP/POP一基row=`ii+9`；PLM estimator不变。候选审计中“expanding from 2000”解释已被Reviewer验收文件撤销。

旧入口ii10/2018实际消费row10/2009水平量，是confirmed defect。固定row21/2020构造全部Zt缺少已发现经济依据，分类`LIKELY_LEGACY_FIXED_YEAR_ANCHOR`；当前批准方向为保持Zt公式，改用稳态同年level row。

## 当前实现任务
只修改Python annual/pre-model输入合同及provenance/metadata：
- 断言calendar/index/level-row/vintage/rolling-window映射；
- same-year GDP/CAP/POP/log与same-year Zt；
- temporal-contract version和source hashes；
- stale/old/inconsistent cache metadata fail closed；
- 只读生成2009/2018 corrected pre-model摘要；
- 原MATLAB源不修改，只给未来patch spec。

本任务MATLAB model、household/HJB/KFE、root/direct/eigen、firm/one-turn/controller、annual/GE/IRF/Results调用全部0。

## 仍未关闭
安徽2018官方GDP/人口/固定投资资本链等核验继续开放；ii15 industry4旧cache alpha与较新PLM workbook不一致；2022–2023六个负资本/复数log是独立数据质量问题。旧rah=.09/.07、KFE边界、Qh负率、P32/sigma和b域实验只代表旧混合年份保存输入。

## 路线
实现验收 → 关闭2018数据身份/官方核验 → 真正2018单年小规模验证 → 若仍高收益/不收敛，再审计GovInv外层适应速度。不要用收敛算法补偿错误数据合同。

生产网格仍I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。Owner历史经验：真正收敛稳态Bt基本在0附近，b=12只保留压力测试。

工作目录：`D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001`。历史证据继续保护。
