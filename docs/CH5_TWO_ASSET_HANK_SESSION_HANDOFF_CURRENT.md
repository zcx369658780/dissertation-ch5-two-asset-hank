# Chapter 5 当前交接
更新：2026-09-09。唯一仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Owner最终科学authority；ChatGPT Reviewer规划/验收/发布；Codex Builder默认`gpt-5.6-sol / medium`。

## 当前入口
fresh读取live main、AGENTS、规则索引、当前状态和active task。
当前状态：`PURCHASED_DATASET_GAP_CLOSURE_AUDIT_ACTIVE__NO_SCIENCE_RUN`。
active task：`tasks/CH5_MP4C_PURCHASED_DATASET_GAP_CLOSURE_AUDIT.md`。
Results eligibility=FALSE。

## 已冻结合同
PLM rolling 10-year：2018=2009–2018；`steady_year=2008+ii`；同年level row=`ii+9`；same-year Zt；资本递推`K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`，所以K2018只需I2000..I2017。PLM、模型方程、GovInv、grid均不改。

## 为什么新增任务
官方身份审计只取得2018安徽初步GDP=30006.82亿元、人口=6323.6万人，与当前workbook 34010.91/6076不一致；后续修订谱系未闭合。固定资产投资2011存在制度断点，未取得可直接拼接的官方2000–2017链。

Owner说明原面板主要来自知网整理数据，存在较多缺失/后续校正风险；另购买了人工校对数据，位于`D:\BaiduNetdiskDownload`，质量较高，可作为第二来源补缺和交叉核验。

## 当前task
只读审计付费数据，优先：
- `中国各地级市全要素生产率数据（1978-2022年）`
- `sj479-地级市-固定资产投资额数据（2000-2024年）`
- `NJ73-中国人口与就业统计年鉴1949-2023年`
以及其他直接相关候选。

必须盘点文件hash/schema/粒度/年份/单位/缺失/来源说明；核对安徽2018 GDP和人口；评估城市投资能否形成2000–2017安徽候选链；评估TFP数据是否适合作为独立验证基准。城市→省份不得在覆盖、可加总和口径未证明时直接汇总。TFP不得在本task替换PLM或选择新的省级聚合方法。

所有付费原始文件只读、不提交GitHub、不外传；仓库只保存必要小规模提取、hash、schema和provenance。科学模型调用全部0。

## 路线
付费数据审计 → Reviewer判断candidate data package/剩余官方缺口 → 数据身份足够闭合后真正2018小规模验证 → 若仍高收益/不收敛，再审计GovInv调整速度。

生产网格继续I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。不继续扩大bmax。
