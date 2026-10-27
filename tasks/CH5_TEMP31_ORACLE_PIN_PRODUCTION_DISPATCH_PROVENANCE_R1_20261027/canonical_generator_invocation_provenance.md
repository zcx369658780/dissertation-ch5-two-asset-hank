# Canonical生成调用

本轮已找到精确静态caller，实际已批准/执行的TEMP31生成和真实输入绑定仍BLOCKED。

1. Primary annual：LOCAL_EMPIRICAL:20–25导入load_primary_annual_input，86–95 prepare_canonical将primary_sources、for_calendar_year、accepted_source_scalars传入并写canonical.canonical_bytes；309–313 CLI识别--prepare-canonical再调用。LOCAL_ANNUAL:136–159、432–456为原件守卫/年轴检查，253–280为payload和整文件SHA。代码调用存在不等于实际读过原Excel/生成过真实输入。

2. Runtime路线：LOCAL_BATCH:49–59的prepare_runtime_inputs在非Owner-A分支调用LOCAL_CACHE.load_runtime_year→add_runtime_support→canonical_bytes并写runtime_inputs。LOCAL_CACHE:13、57–73为缓存SHA/标签检查，87–107为距离轴和state映射。另分支调用LOCAL_OWNER_A.build_input→canonical_bytes（139–155、168–188）。Owner-A schema/authority字符串只作代码声明，本轮不代Owner认证。LOCAL_PRODUCTION:145–161按representation消费；非Owner-A还重建与supplied原字节比较。

3. 工资/税来源：LOCAL_EMPIRICAL:46–71 accepted_source_scalars有wjt/composite_wage/wage_tax常量；137–158和LOCAL_CACHE:98–107、LOCAL_OWNER_A:215–221将共用scalar按省复制。公开数字是源码常量，非薪资原表；未采用或构造31省实测工资。所有宏观workbook、保护cache和真实run canonical未打开；SOURCE_HASHES和guard存在不是原件可用证明。

| 要素 | 状态 |
| --- | --- |
| 生成器及精确静态caller/参数 | SOURCE_EXPRESSION_IDENTIFIED |
| 当前Owner采用入口/配置/representation/year | UNKNOWN |
| 实际生成调用、canonical原件及批准来源 | BLOCKED |
| 2009工资/税共用scalar源码来源 | IDENTIFIED_AS_CODE_CONSTANTS，不是31省实测/经济口径采纳 |
| canonical SHA | 完整序列化文件指纹，不能代D1 tuple digest |
| labels/shape检查 | STATIC_CHECKS_PRESENT，非行政ID真实join |
| D1共同旧期tuple、D2生产adapter、D3 | BLOCKED，不造假digest |
| NBS→w/wjt/net/劳动单位桥 | UNKNOWN/BLOCKED，MODEL_ADOPTED=FALSE |

最小下一事实：Owner指定入口/命令、准确版本或原始SHA、representation/year、实际canonical生成调用及原件准确路径/hash、source hashes、行政省ID/有序字典、旧期tuple来源。函数名或任意JSON hash不足。本轮不选路线、不开数据、不运行生成器。
