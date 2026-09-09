# Chapter 5 当前交接
更新：2026-09-09。唯一仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Owner最终科学authority；ChatGPT Reviewer规划/验收/发布；Codex Builder默认`gpt-5.6-sol / medium`。

## 当前入口
fresh读取live main、AGENTS、规则索引、当前状态和active task。
当前状态：`REVISED_2018_GDP_AND_CANONICAL_WORKBOOK_ACCEPTED__2018_DATA_LAYER_CLOSED__SINGLE_TURN_VALIDATION_ACTIVE`。
active task：`tasks/CH5_MP4C_2018_CORRECTED_INPUT_SINGLE_TURN_VALIDATION.md`。
Results eligibility=FALSE。

## 2018最终静态输入已接受
- GDP：安徽省统计局四经普后2018现价GDP修订值`34010.9`亿元；保护workbook `34010.91`只在官方0.1亿元精度下匹配。final-use transformed GDP=`34010900.0`。
- POP：`6076`万人 / `607600.0`，依据2023《中国人口和就业统计年鉴》按2020人口普查修订的2011–2019历史值。
- CAP：PIM `K2018=1357314108.2013683` / transformed `1357314108201.3684`，冻结`K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`；资本是model-derived，2011投资统计定义断点保留。
- alpha=`0.772866243094144`；same-year `IND_Zt≈0.0006934644495858679`；steady_year=2018，analysis/data_MAT=10/10，level row=19，PLM vintage19/window2009–2018。

canonical workbook：`D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`，SHA256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`。私有xlsx不进GitHub；仓库保存manifest/readback/receipts。

## 当前task
首次修正数据后的科学运行，只执行一次2018 source-faithful ordered one-turn。必须先hash验证canonical workbook；完整31省顺序，仅1 turn，不进入steady-state/GE/annual/IRF。

捕获全省firm raw/used ra、wage、household rah/inputs、HJB/KFE返回、聚合和controller observables，重点生成安徽forensic record。旧mixed-year只能用保存证据比较，不得重跑。若任一province/household/HJB/KFE/firm失败，落盘并立即停止，无科学重试，不调GovInv/alpha、rates、grid、solver/tolerance或boundary law。

## 路线
single-turn验收 → 若通过，再进入受控multi-turn/steady-state prefix → 若仍高收益/不收敛，再审计GovInv调整速度 → household/KFE有效性 → 有限省份 → 年度覆盖 → MP5/MP6动态。

2022–2023六个非正资本/无效Zt是独立未来年份问题，不影响2018当前验证。