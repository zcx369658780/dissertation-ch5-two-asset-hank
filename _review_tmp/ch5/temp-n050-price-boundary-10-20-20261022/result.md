# TEMP N050 半自动诊断

run_id=a6e047fe0b864ef899ce016e042b43cf
science_terminal=TEMP_MAX20_COMPLETED_NONCONVERGED

完成外层轮次：20；HA/HJB尝试=40；HJB进入=40；KFE进入=40。

第10轮决策原件：
{
  "decision": "TREND_NOT_OBVIOUS_AT_10",
  "first_KN_mean": 1.1846664077873126,
  "last_KN_mean": 0.11295376356148679,
  "first_Y_mean": 0.1256590388784766,
  "last_Y_mean": 0.04674584532532844,
  "relative_threshold": 1.2,
  "both_raw_outside_rounds_6_10": 5,
  "boundary_required": 4,
  "remaining_safety_and_budget_required": true
}

# 每省边界汇总

比例分母仅包含实际完整轮；raw越界才计裁切。家庭字段仅参考带。

| province | stage | firm_field | valid_complete_rounds | upper_hits | lower_hits | upper_pct | lower_pct | first_hit_round | trend | first_contiguous_hit_interval | inside_to_outside | outside_to_inside |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SYN_A | FIRST_10 | ra | 10 | 10 | 0 | 100 | 0 | 1 | PERSISTENT | [1, 10] | [] | [] |
| SYN_A | FIRST_10 | wjt | 10 | 10 | 0 | 100 | 0 | 1 | PERSISTENT | [1, 10] | [] | [] |
| SYN_A | ALL_COMPLETE | ra | 20 | 20 | 0 | 100 | 0 | 1 | PERSISTENT | [1, 20] | [] | [] |
| SYN_A | ALL_COMPLETE | wjt | 20 | 20 | 0 | 100 | 0 | 1 | PERSISTENT | [1, 20] | [] | [] |
| SYN_B | FIRST_10 | ra | 10 | 10 | 0 | 100 | 0 | 1 | PERSISTENT | [1, 10] | [] | [] |
| SYN_B | FIRST_10 | wjt | 10 | 10 | 0 | 100 | 0 | 1 | PERSISTENT | [1, 10] | [] | [] |
| SYN_B | ALL_COMPLETE | ra | 20 | 20 | 0 | 100 | 0 | 1 | PERSISTENT | [1, 20] | [] | [] |
| SYN_B | ALL_COMPLETE | wjt | 20 | 20 | 0 | 100 | 0 | 1 | PERSISTENT | [1, 20] | [] | [] |

两套完整逐轮CSV和Markdown见ZIP：price_rounds.csv/.md、firm_household_rounds.csv/.md；字段身份见field_mapping.json。所有数值来自实际完整轮，未完成轮不计分母。单次science driver，未重启或试第二ARM。

N由100/160改为50/80；Zt初值6/6.2、GovInv初值100/120不变，原适应律和same-S/lagged raw规则保留。企业raw越界才称实际clip；家庭rah和w_eff没有独立clip，列出的边界仅同单位参考。Lst未证实为源码字段，记UNMAPPED；Lt_HA=l_ss为每人有效劳动，Lt_supply为目的地Lt_mat行和，二者不被强行等同。MATLAB POP×100、GDP/CAP×1000只作量纲来源对照；本轮不重估初始Zt。

条件比较K/L↑通常工资↑、资本边际回报↓，Z↑通常二者↑；本轮N同时改变N*At与劳动，加上固定初始GovInv，不能先验判断K/L方向或自动推出下一组参数。历史基准仅引用已归档100轮审查，未读取私人原轨迹，因此逐轮NOT_COMPARABLE。

资格测试8项PASS，仅限本scratch合作进程。保留首次日志目录工程错误和E1修正；科学首错见driver_terminal.json。正式V010未改，Results=FALSE，V011=NOT_STARTED，真实31省/GE/IRF为0，生产GLOBAL_STOP/supervisor/reader仍UNVERIFIED，OS外部descendants UNKNOWN。

三文件发布及远端原件回读结果以后续最终原始JSON为准。本候选须Astra独立终审；Codex不自受、不清理、不自动签发下一参数。旧三个候选只读保留。
