# TEMP31 2018工资与就业来源审计：实际STOP

run_id=a456168dea274581b2b63df0533610ea

actual_terminal=STOP_E1_EXHAUSTED_SOURCE_VALUE_UNIT_GATE；总体NOT_PASS。

来源值机检在吉林单位人数行失败，2批E1已耗用，未修复、未重跑来源流水线。自动交付的是STOP证据和未经端到端最终验证的整理观察，不是31省数据通过或经济模型资格通过。

# 31省来源观察与缺失报告

以下为已取得来源的整理观察，整个数值流水线未完成最终验证，不能称为31省数据核验PASS。MISSING表示本轮未核准官方原值，不证明未发布。仅摘录与原站字节、统计局原表与官方转载分级列在来源账。

上海官方2019发布2018非私营140270元；部分非官方转载140400元，未裁定修订关系。非官方汇总存在西藏遗漏及陕西以后错位，拒绝取值。新疆75457来自2021年鉴明确2018行，原站404、只有官方连接器摘录；不拿兵团或2017就业替代。山西、河北、安徽部分值为后年官方发布明确2018基期，均保留vintage。甘肃两工资为省统计局署名稿的事业单位转载，主办身份由页脚和发改委预算公开摘录交叉说明，非统计局原表。

吉林2793233人→279.3233万人这一观察触发来源值机检失败：机检按整理后的单位直接查原表字面值，未执行转换验证。原始数据及错误完整保留，未修复重跑，未升级数值资格。辽宁5-23观察67324元的非私营口径未独立证实，因此主表工资MISSING。浙江官方云表顶层行标签未映射，88883不录主表。

吉林、辽宁单位人数是年末框架；福建705.36万、湖南546.27万、重庆391.2万、宁夏67.97万为调查/单位人数，未证明为年度平均工资分母。私营覆盖人数和两类年度平均分母均未核准，不能合并工资。部分就业时点未明示，CSV保留TIME_UNSPECIFIED；就业地/居住地桥UNMAPPED。

全国工资82461/49575元、年末就业77586万与城镇43419万为独立校验点，不代省份，不强制省份加总等于全国。2018旧口径不机械拼接2020后七普统一测算。


|省份|私营工资 元/年|非私营工资 元/年|总就业 万人|城镇就业 万人|非私营调查/框架 万人|
|---|---:|---:|---:|---:|---:|
|北京|76908|145766|1237.8|MISSING|MISSING|
|天津|MISSING|MISSING|MISSING|MISSING|MISSING|
|河北|39512|68717|MISSING|MISSING|MISSING|
|山西|34535|65917|MISSING|MISSING|MISSING|
|内蒙古|MISSING|MISSING|MISSING|MISSING|MISSING|
|辽宁|MISSING|MISSING|2260.6|1050.2|501.6267|
|吉林|35026|68533|MISSING|MISSING|279.3233|
|黑龙江|MISSING|MISSING|MISSING|MISSING|MISSING|
|上海|57056|140270|MISSING|MISSING|MISSING|
|江苏|54161|84688|4750.9|3227.5|MISSING|
|浙江|MISSING|MISSING|MISSING|MISSING|MISSING|
|安徽|MISSING|74378|MISSING|MISSING|MISSING|
|福建|52930|74316|2791.37|MISSING|705.36|
|江西|MISSING|MISSING|2636.1|MISSING|MISSING|
|山东|MISSING|MISSING|MISSING|MISSING|MISSING|
|河南|40209|63174|MISSING|MISSING|MISSING|
|湖北|MISSING|MISSING|3580|MISSING|MISSING|
|湖南|40175|70221|3738.58|1863.85|546.27|
|广东|MISSING|MISSING|6508.65|MISSING|MISSING|
|广西|MISSING|MISSING|MISSING|MISSING|MISSING|
|海南|MISSING|MISSING|603.73|277.81|MISSING|
|重庆|52558|78928|MISSING|MISSING|391.2|
|四川|43352|77686|4881|1680|MISSING|
|贵州|MISSING|MISSING|MISSING|MISSING|MISSING|
|云南|MISSING|75701|2992.8|862.7|MISSING|
|西藏|MISSING|MISSING|MISSING|MISSING|MISSING|
|陕西|MISSING|MISSING|2071|MISSING|MISSING|
|甘肃|39834|70695|1555.6|637.6|MISSING|
|青海|MISSING|MISSING|MISSING|MISSING|MISSING|
|宁夏|MISSING|78384|MISSING|MISSING|67.97|
|新疆|MISSING|75457|MISSING|MISSING|MISSING|

观察覆盖（未最终验证；分母31省）：

- wage_private_yuan_year: 12/31
- wage_nonprivate_yuan_year: 16/31
- N_employed_total_wan: 13/31
- N_employed_urban_wan: 7/31
- N_wage_covered_private_wan: 0/31
- N_wage_covered_nonprivate_wan: 6/31
- N_resident_wan: 4/31


SOURCE_ONLY：工资元/人/年÷1000→MU/NU/年；s_H=64.8906755511未采纳。未改变N、工资界、HA网格、效用或asset_bridge。

HA/HJB/KFE/roots/science_driver/outer/GE/IRF全部0。正式V010不改，Results=FALSE，V011=NOT_STARTED，生产GLOBAL_STOP仍未验证。旧32/32结构与32/32符号检查仅Codex报告，不升级独立PASS。私人规范工作簿未读未上传。五个受保护对象元数据与bootstrap一致，不能据此声称文件全量哈希审计。

Review仅指定三件文件，固定唯一父7d0b6b43604b70bbaccd64dca9549836dee6234b。ZIP含原始官方公开来源字节、连接器摘录、31省CSV、来源和缺失账、实际异常、预算、逐成员隐私与CRC/SHA。发布后的候选commit/tree/parent及远端字节核验另记最终JSON，本文不预先宣称上传PASS。

停止等待Astra独立验收和Owner讨论；无后续任务，无自行清理候选，三个历史PENDING保持原样。
