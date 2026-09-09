# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`CORRECTED_2018_THREE_TURN_CONTROLLED_FAIL_ACCEPTED__PERSISTENCE_REPAIR_FROZEN__REEXECUTION_ACTIVE`。
最新接受候选：`8b80b491421603b94a281211d683d94e2a78fdaf`。报告：`docs/CH5_MP4C_2018_CORRECTED_INPUT_THREE_TURN_PROPAGATION_REPORT.md`；Reviewer验收：同前缀 `_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_CORRECTED_INPUT_THREE_TURN_PROPAGATION_REEXECUTION.md`。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## 2018数据层与前两轮科学证据
2018 canonical 数据层继续冻结并已闭合。canonical workbook SHA256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`。

已接受 corrected-2018 turn1/turn2：fresh turn1、turn2均可完整31省执行；两轮证据已经建立turn3是corrected firm `ra=.02`第一次能够通过下一次native capital-allocation timing进入household composite `rah`的高信息量门。

安徽已接受前缀：turn1 `rah=.09`、raw `ra0=-.02496997113112164`、used `ra=.02`、raw wage `2.5721358283733027`；turn2 `rah=.0829892058879816`、raw `ra0=-.024968505109415375`、used `ra=.02`、raw wage `2.1373365306922518`、HJB 31次、`nk_gap=.34756612158493083`。

## 三轮任务受控FAIL
候选`8b80b491...`的fresh turn1/turn2再次完全复现，`mismatch_count=0`。科学进程只有1个，完成2 turns / 62 province updates，62/62 household/HJB/KFE/firm均返回，科学重试0。

进入turn3之前，runner对`predecessor_reproduction.json`执行第二次排他写入并触发`FileExistsError`。因此turn3从未进入；安徽turn3 rah/provenance、firm、controller及全国turn3指标全部保持`NOT_CHECKED`。不得用准备状态或公式推算替代科学运行观测。

该失败分类为工程evidence persistence collision，不是household/HJB/KFE/firm/经济状态失败。

执行runner身份已保存。候选中随后完成一行证据写入顺序修复及静态回归检查；修复后runner没有科学执行，因此原任务保持FAIL。Reviewer已接受该repair仅为工程持久化修复，不改变任何模型方程、状态传播、capital allocation、controller、数值算法、grid、bounds、solver/tolerance。

## 当前 active task：three-turn reexecution
新exact task明确授权在已接受修复runner上进行一次fresh corrected-2018三轮重执行。它是新的科学授权，不是上个任务的隐式retry。

执行前必须核验canonical workbook和repair身份/静态门。只允许1 scientific process、turn1+turn2+turn3、最多93 province updates、scientific retries=0。turn1/turn2必须先复现接受证据，之后才可进入turn3。

即使PASS：turn4、5–10 turn prefix、steady-state、GE、annual、IRF、Results均未授权。

## 后续路线
three-turn reexecution验收 → 若真实观测到turn3 direct corrected-rate transmission，再决定是否发布短5–10 turn prefix。只有后续corrected轨迹出现高收益反转、数值失败或不收敛迹象时，才重新进入GovInv/household-KFE诊断。

2022–2023六个非正资本/无效Zt仍是独立未来年份数据质量问题。生产网格继续I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。
