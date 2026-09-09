# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前阶段
MP4已完成原call725失败复现、rah=.07敏感性、KFE source/escape归因、b域压力测试、数据/插值审计、时间合同/Zt legacy审计、V2 pre-model实现、官方/付费数据审计和2018 PIM资本链闭合。Results=FALSE。

## 已冻结并闭合
- 时间合同：`steady_year=2008+ii`；同年level row=`ii+9`；PLM rolling 10-year；2018=2009–2018；same-year Zt。
- 人口：安徽2018=`6076`万人，后续官方年鉴按2020人口普查修订。
- 资本：继续PIM，`K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`；安徽K2000..K2018逐年binary64精确复现，PIM blocker关闭。2011投资统计定义断点继续作为限制。

## 当前 active task
`tasks/CH5_MP4C_2018_REVISED_GDP_AND_CANONICAL_DATA_WORKBOOK.md`

Owner授权公开检索修订后安徽2018现价GDP。任务从国家统计局/安徽统计局/官方年鉴等来源关闭GDP身份，并同时生成长期使用的版本化`CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`，集中保存年度绑定、31省GDP/人口/投资/PIM资本、PLM alpha、same-year Zt、安徽2018最终输入、provenance和data-quality flags。原保护/付费数据不覆盖，完整私有xlsx默认仅留本地证据根。

所有科学模型调用均为0。

## 后续顺序
修订后2018 GDP + canonical workbook验收 → 最终2018 V2 input → 真正2018单年小规模科学验证 → 若仍高收益/不收敛，再审计GovInv外层适应速度 → household/KFE有效性 → 有限省份 → 年度覆盖 → MP5/MP6动态。

当前不运行household/HJB/KFE/firm/GE/annual，不调GovInv/alpha，不扩大bmax，不切换PLM。2022–2023负资本问题继续独立处理。