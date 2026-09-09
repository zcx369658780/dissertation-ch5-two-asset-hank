# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`PURCHASED_DATASET_GAP_CLOSURE_AUDIT_ACTIVE__NO_SCIENCE_RUN`。
最新接受候选：`729d2c13c5864e0f607ac6dc8fd863d19f02d3f7`。官方身份审计结论：`PARTIAL_OFFICIAL_IDENTITY__MANUAL_DATA_REQUIRED`。
当前 active Builder task：`tasks/CH5_MP4C_PURCHASED_DATASET_GAP_CLOSURE_AUDIT.md`。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## 已冻结年度合同
V2时间合同保持：PLM rolling 10-year；`steady_year=2008+ii`；同年GDP/CAP/POP一基row=`ii+9`；2018使用2009–2018 PLM vintage19；Zt保持公式但使用同年水平量。资本递推仍为`K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`，因此K2018只依赖I2000..I2017。

## 当前数据blocker
官方身份审计尚未取得第四次经济普查修订后的安徽2018精确GDP、足以解释人口差异的后续权威口径，以及可防御地连续拼接的2000–2017官方固定资产投资绝对值链。2011固定资产投资统计范围存在官方确认的制度断点。

Owner补充：原CNKI整理面板存在缺失和潜在偏误；另有一批人工校对、付费购买的高质量本地数据，位于`D:\BaiduNetdiskDownload`，可作为第二来源审计。截图明确显示的高优先级目录包括：
- `中国各地级市全要素生产率数据（1978-2022年）`
- `sj479-地级市-固定资产投资额数据（2000-2024年）`
- `NJ73-中国人口与就业统计年鉴1949-2023年`
以及其他人口、就业等候选数据。

## 当前任务
只读盘点和质量/口径审计这些付费数据，重点判断：
1. 是否存在可追溯到官方修订口径的2018安徽GDP/常住人口；
2. 城市级固定资产投资数据能否在严格满足可加总、覆盖完整、口径一致等条件后形成安徽2000–2017候选链；
3. 付费TFP数据是否适合作为独立生产率验证基准或未来替代输入候选。

付费数据是高质量二手整理源，不因购买/人工校对而自动升级为官方authority。原始付费文件只读、不得提交GitHub或外传；只提交hash、schema、极小必要提取值和来源说明。

所有MATLAB、household/HJB/KFE、roots/solves、firm/one-turn/controller、stationary/GE/annual、IRF/Results科学调用均为0。不得修改生产数据、PLM、GovInv/alpha、bmax或任何模型方程。

## 路线
付费数据缺口闭合审计 → Reviewer判断是否形成可接受candidate data package / 是否仍需官方手工资料 → 真正2018单年小规模科学验证（仅在数据身份足够关闭后） → 若仍高收益/不收敛，再审计GovInv外层适应速度。

生产网格继续冻结I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。2022–2023六个负资本/复数log仍为独立问题。
