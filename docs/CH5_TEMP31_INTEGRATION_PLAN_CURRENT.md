# TEMP31 当前生产接线方案 · 2026-11-01

STATUS=PLAN_READY__SOURCE_WORKSPACE_VERIFIED__SCIENTIFIC_IMPLEMENTATION_NOT_STARTED
OWNER_SOURCE_ADOPTION=56447829ce0e6c3c85552c53c351b26a2452a4bd__DEVELOPMENT_SOURCE_ANCHOR
SOURCE_ROOT_TREE=7b7cb29dd5b37be92561e7f1bc688c0d29789732
LOCAL_SOURCE_MATERIALIZATION_COMMIT=91941302f966f12d5f206691f74c800cadf3e797__LOCAL_ONLY_NOT_PUSHED
SCIENTIFIC_SOURCE_FREEZE=FALSE

本方案承接Owner对上一轮TEMP31选择建议的同意，落实来源采纳、独立源码工作区和接线设计。不重写V010冻结计划、不恢复旧预算，也不把选定来源等同于接受其中每个历史数值写法。唯一当前进度仍由CH5_LOCAL_FIRST_STATUS_CURRENT.md维护，Owner决定见OWNER_LOCAL_FIRST_CODEX_20261101.md。

## 已完成的工程基础

选定提交的src、exports、validators、tests及pyproject.toml共565路径、5,817,417源字节已全部物化。每件核对原始Git Blob、字节数和SHA-256；新Git中的四个目录子树和pyproject Blob与原提交逐项一致。新工作区使用独立.git、无alternates，源码物化提交为新根提交，不能冒充原56447829整棵仓库checkout或原历史祖先链。独立Git对象fsck --full --strict通过。

| 范围 | 原提交与新工作区共同身份 |
|---|---|
| src | 8ac1458f0586f1fad58e7bcb85d8acf1a3ef0600 |
| exports | f0614665143257e024cc7857afc3bbaf08e730c0 |
| validators | 3e7f0a8262c398aa8a65914ea376acbc294ebf41 |
| tests | a3281412de682d7c8e127f3bdc0da0d716f386bc |
| pyproject.toml | 5c778f7ccbbabfaf1046d4696cf843dc0adbb34c |

仅复制上述固定公开代码范围；随原目录保留的历史验证脚本不执行。未复制完整仓库历史、原始数据、数组、旧任务日志、源码缓存或MATLAB原件；不是G2全资产归档/恢复认证。原dirty工作树、原TEMP31 snapshot和原对象库保留。代码已齐不证明运行环境、输入或科学解有效。

## 接线对象与验证顺序

| 工作 | 具体实现方向 | 通过依据及当前状态 |
|---|---|---|
| 来源入口分离 | 新TEMP31入口显式绑定选定src；保留历史export及其入口身份关系，避免通过旧mp4b bootstrap混装新export | 先静态列全模块/Blob与实际入口；不以改旧ORACLE_SHA或覆盖export完成认证。PLAN_ONLY |
| 工资生产与家户消费 | 工作目的地tau[j]与sigma[j,i]只进入净工资生产一次；带context/省份轴/期次的净工资记录进入Temp31NetWageInputs；初始化、HJB边界、policy/FOC和预算消费同一记录 | 非对称目的地税、两轴置换、不同省序、伪造已扣税值和重复扣税注入必须可拒；只在获准工程实现范围验证纯结构/代数，不调用求解器。PLAN_ONLY |
| 初始化合同对齐 | 在接线前逐式核TEMP31历史初始化与既有V010冻结合同；不得原样激活已知不一致的helper，也不得暗改科学公式 | 见下方明确阻塞。NOT_CLOSED |
| 多省单轮适配 | 在新独立入口装配家户batch、目的地劳动、资本/回报、企业、工资和财政；先用显式stub观察绑定与账本 | 保留人均/省总量和目的地/来源地轴；不因函数名相似替换经济机制；新科学源码实现与调用须匹配已有合同和具体授权。NOT_STARTED |
| 外层与运行环境 | 明确同源模块加载、版本、runner I/O、状态交接、失败即停和调用预算；独立记录工程import与真实HA | pyproject只有依赖下限，尚无锁定且通过的环境。不安装、不import、不运行旧runner来试探。NOT_STARTED |
| 科学验证 | 获得对应新预算后，从固定输入单点HA开始，严格HJB/KFE及终端聚合；前门通过再考虑多省稳态 | 初猜、价格域、网格、容差、次数/时间/内存和真实数据采用均须对应Owner决定；当前科学调用0，旧耗额不复活。NOT_AUTHORIZED_BY_THIS_PLAN |

## 接线前必须处理的现存初始化不一致

选定源码src/ch5_two_asset_hank/multi_province/temp31_ha_taxfree_bootstrap.py第211行仍为temp=effective*effective+rb*b+Tt；第214行c=wage*l+rb*b+Tt未包含同一资产收益项。这是历史source-derived helper的实际写法，本轮只读识别，未执行、修改或宣称其数值后果已验证。

既有V010冻结计划versions/0.0.10/plan.md（冻结commit bf091da33d59293f147d52c11580327d3ac2a85d，Blob85138d8859d53295262fe13bf5bc277bca95ed3f）第2节明确R=r_b(b)*b+r_a(a)*a+Tt、c0=w_eff*z*l0+R，且不得用旧Rah.*raah错误替代a*r_a(a)。Bootstrap19历史隔离任务保留原初始化写法，来源真实性不授予其生产公式的新资格。

因此本方案不把历史helper接入生产。下一步先形成与已采纳V010合同的精确crosswalk：确认适用主线、初猜与效用式、根域/容差及工资记录；若现行TEMP31专门合同与该冻结要求实质冲突或需要新的科学选择，向Owner提交这一个具体决定。原冻结合同与历史helper均保留，不以一般工程权改写任一方，也不在新运行中恢复已修正错误。

## 其他科学与保护边界

源候选同时包含source-like与origin-normalized劳动函数，生产选择须保持已采纳机制，不由工程归一化便利决定。资本same-S/raw/lagged时序、人口/有效劳动/财政总量、首轮19数值初猜的资格、真实canonical/年份/31省轴、严格生成元/KFE门及16项未决义务均不由本方案接受。

本轮不改科学源码/参数/输入，不启动MATLAB、HJB/KFE/HA/GE/IRF或校准，不通过import触发计算。R12 STOP、R13未授权、六路径WASM STOP、OWNER_BASELINE_REBIND=NOT_AUTHORIZED保持。源码锚点采纳不等于保护状态重绑定。

## 分支清理位置

当前只具备选定代码范围的独立可核验副本。九月源/结果、各历史实验/STOP与私有资产的完整恢复仍未认证；本方案不授权删除分支。后续先逐分支列独有提交、已登记工作树/dirty和证据覆盖，确认保留引用及相应归档/保护门，再形成具体候选清单供Owner决定。
