# V0.0.9 Astra独立签发：新合成两资产HANK HJB/KFE与资产出清有限数值实施许可

日期：2026-10-15（Asia/Shanghai）

**Authorization:** `ASTRA_APPROVED_EXECUTION__CH5_V009__OWNER_ADOPTED_SYNTHETIC_TWO_ASSET_HJB_KFE_STATIONARY_ONLY`
**仅授权一次：执行已冻结[正式V009计划](plan.md)的13个新增白名单路径、独立人工模型数学oracles以及限额内1省主网格完整HJB/KFE/资产财政市场稳态；仅全部通过后才尝试非对称2省。**

## 独立前提与身份

Owner已批准[E1–E3人工科研决策](owner_scientific_adoption.md)，经Astra对治理分支实际远端readback，计划冻结commit `f7caeb54b13ec977d1b503b124067ae522ca2433`，tree `7c51c01cb81b5ca1dfe2124de4de1e3a154e71cf`，`versions/0.0.9/plan.md` blob `cb76a840fdd9d1756728189bf29518679831aba6`，治理compare 1 ahead/0 behind仅6份科研/版本文档，未改模型/不动main。历史代码基线 `d41d229b681e09b913c21deff7a057085b9bc419` tree `88833acf90613380afa30ab8d6ee7e0297e98664` 已独立读取；必须以其为唯一parent创建安全隔离新candidate。Owner长期工作流仍V1.2，不授予无需审议的新科学law。

**准入**：只准`MODEL_TIME_SYNTHETIC`，本版plan §3所有人工数值、(b,a,z) 20×20×2 F-order、a/b非负与私人资本/全国债权、人工固定S及R、省级资本再配置、CES工资一次税和全国统一财政。在任何Python solver/pytest运行前，Codex须先完成只读精准依赖审计、人工校准/初值哈希预注册、独立新root与原dirty保护，禁止先试参数再预注册。

**工程实现**：最多plan§1列出的13个新增路径；已有HJB/KFE/old runners和原dirty/source全部只读，绝不调用原C8/2009/2018的受保护或已耗旧科学生产入口。新HJB/KFE可复用经审静态纯数学算法，但新数值进程的所有attempted必须按V009独立持久账精确计数。

**明确硬科学上限**：≤8小时；focused pytest≤8进程且每进程≤600s；独立scientific drivers≤4进程且每个≤2h；宏观完整attempt总≤4（1省≤2、2省≤2）；每次1省宏观残差eval≤24，每次2省≤32；household HJB+KFE attempted总≤176、每家户HJB直接更新≤100、policy/Q mapping≤101、terminal restricted-gesvd≤1；直接更新≤17,600、policy/Q≤17,776、KFE terminal-gesvd≤176；selector/scalar-root attempted每家庭≤400,000且累计≤70,400,000；不因局部/跨日/新进程或修复失败重置。所有实验和最终树验收共同分享上限。累计新增磁盘≤256MiB，操作性Git≤64、受限view≤32、LOCAL_ONLY人工证据≤144、公开≤16MiB；内存采样目标512MiB，达限即阻止下一科学进入，未可测必须标UNKNOWN。进程依赖错误、数值约束失败或预算超限按冻结plan§5 STOP。

**明确零预算**：24×24网格/1152维验证、真实31省两资产HANK、前瞻动态 HJB/KFE/IRF、真实2017/2018/C8 JSON/NPZ/CSV/MAT/receipts的stat/read/hash/parse/extract、旧HJB/KFE科学runners、C9/outer/C1生产消费者、旧已耗V008 roots/paths、B3/G0/A16/hostile保护、MATLAB科学调用、真实Results都为0。路径名/科学模拟对象不能绕过上述禁令。

**预定STOP**：`WAIT_ASTRA_V009_SYNTHETIC_HANK_NUMERICAL_ACCEPTANCE / STOP`。实际收敛须依赖同checkpoint HJB、最后同策略Q下KFE unique closed class、资产债券/劳动/企业/全国财政/商品完整残差，不承诺一定成功；若不可行交原样失败证据，不改参数/guards追PASS。任何新的经济制度/科学容差/保护权限冲突向Astra报告，必要时由Owner新决定。不得自授ACCEPT、自动启动V0.0.10或合并main。
