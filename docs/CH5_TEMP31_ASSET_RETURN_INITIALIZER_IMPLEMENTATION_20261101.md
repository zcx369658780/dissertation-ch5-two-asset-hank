# TEMP31 资产收益初始化：独立实现与静态合同核查 · 2026-11-01

STATUS=LOCAL_ADDITIVE_IMPLEMENTATION__STATIC_CONTRACT_PASS__NUMERICAL_NOT_RUN
LOCAL_CODE_CANDIDATE=1cdebe761dc4406a83093884ae15f0377d891b8f
LOCAL_CODE_PARENT=64dfaeb7e4c5dd6bb97874e38e9f7d0244c4e58f
LOCAL_CODE_TREE=7c2cdaec977353d9b41de0e68cdffad1d78cdbe6
CODE_PUBLICATION=LOCAL_ONLY_NOT_PUSHED
MODEL_IMPORTS_INITIALIZER_ROOT_HA_HJB_KFE_GE_IRF_CALLS=0

## 授权与实施范围

Owner先明确选择a*r_a(a)，再要求继续既有初始化实施规格。本轮将该已采纳项落成独立、显式opt-in实现，并做不导入模型的静态/符号工程验证。不重用旧科学预算、不改V010冻结合同、不修改历史初始化，也不接生产入口。

仅新增两份代码路径：

| 路径 | Git Blob | bytes / SHA-256 |
|---|---|---|
| src/ch5_two_asset_hank/multi_province/temp31_asset_return_initializer.py | 9a4b5f1a54c5b5f1a88317f8edfa2b52fd253955 | 5621 / a1b4edea027582b6cf4f3818fb2b1579e4926c09ae1a481586d1dad21d410372 |
| tests/test_temp31_asset_return_initializer_static.py | b2ed776f004050bab7db143ee2aee955fa8512b1 | 8598 / c7ea7f0642e7f3997cf6c3c0985bf6e9cb03760a8787d7571c0eb2b69579e934 |

上述candidate仅在独立本地源码工作区，不能使用GitHub候选链接冒称源码已公开交付。治理分支只同步这份实现说明和当前记录，不上传新增模型源码或原始回执。

## 实现的具体行为

- initial_nonlabor_resources显式计算capital_income=a*effective_return、liquid_income=b*liquid_return、R=capital_income+liquid_income+T；保留符号，拒非有限值/溢出，不平方、取绝对值、补floor或clip。
- temp31_asset_return_initial_arrays使用同一R求劳动根，再计算c0=w_eff*z*l0+R及V0效用；收益率折减仍调用原matlab_faithful_illiquid_return，不改参数或输入。
- 必须提供无默认值的resource_convention关键字，且显式等于V010_TOTAL_WEALTH_NUMERICAL_INITIAL_GUESS。这个标签用于数值初猜语义，不代表Owner已接受无成本提款/两账户均静止，也不是科学运行授权凭证。
- 核对net-wage消费者、省序/上下文的既有guard、进入state与消费者的rah/rb一致，限定现有单一unit-weight劳动类别；本冻结CRRA表达式对gamma_c=1明确拒绝，不偷偷新增log偏好分支。
- 独立劳动根遵循V010冻结区间max(0,-R/wage)+1e-12至1024、Brent绝对/相对容差1e-12、maxiter=100；不存在自动换初值、扩区间、重试或容差放宽。该函数本轮未调用。
- 生成小端float64、F-order的value/labor，检查有限性、正消费与两个资产轴的正V0斜率，再将返回数组设为只读。未来调用方仍须在首次HJB前封存输入与V0身份；本轮未生成任何真实V0。

## 实际完成的检查

先创建静态合同测试，记录新模块不存在导致的预期失败；实施后10项通过，补充有符号收益与固定收益率资产缩放的符号性质后，最终11/11通过。测试文件仅用stdlib解析AST和归一化符号多项式，从不import或执行模型实现。

覆盖：资本/流动收益与冻结R的符号恒等式；把资本收益故意改回rate*rate的AST变异被拒；R漏资本收入被拒；a=0或收益率=0时符号资本项消失；收益符号保留、固定收益率下资产缩放；劳动根与c0/V0同一资源来源；c0另造缺项资源的变异被拒；显式资源语义参数及拒绝guard；不读取tau/migration_costs再扣税、模块顶层无求解激活；固定根区间/容差/maxiter的源码合同；历史初始化Blob保持不变。

这些是AST/符号合同检查，不是以样本参数运行经济方程、求根实验、完整单元行为验证、数值驻定或科学接受。源码语法解析通过；旧565路径的Git Blob逐件仍与来源清单一致。未运行全套pytest或历史runner，因为它们可能导入/执行科学路径。

## 尚未完成及下一门

实际module import、标量资源函数/劳动根/数组初始化执行、FOC残差/资源可行性与V0斜率数值验证全部NOT_RUN。完整运行依赖、科学输入身份和调用/时间/内存预算尚未放行；实际验证需要另行明确的受界工程/科学范围，不能从11项静态检查推断PASS。

新入口未被任何生产文件导入或调用。正式两账户的d/chi、初始化现金流假设、实际31省接线、严格HJB/KFE、外层/GE/IRF和Results资格均保持原状态。原TEMP31平方helper、九月原件、旧dirty工作树/index、WASM/R12 STOP、R13未授权与16项义务保留；无分支删除或main合并。

ENGINEERING_VERDICT=PASS_BOUNDED_ADDITIVE_SOURCE_AND_STATIC_CONTRACT_ONLY
NUMERICAL_VALIDATION=NOT_RUN
INDEPENDENT_SCIENTIFIC_REVIEW=NOT_ESTABLISHED
OWNER_SCIENTIFIC_ACCEPTANCE_OF_EXECUTED_INITIALIZER=NOT_GRANTED

## 下一次实际初始化验证的具体提案（未授权、未执行）

供Owner单独决定：在固定candidate上，一次新Python子进程、墙钟最多30秒、一次数组初始化、最多8个劳动根、每根maxiter=100；失败即停、重试0。HJB/KFE/HA/GE/IRF/policy/MATLAB调用全部0。运行前须核来源和隔离import，不把此提案当作现有运行许可。

仅用明确标记的合成8格：b=[-0.1,0.1]，a=[0,1]，z=[0.8,1.2]，grid.switch_matrix为2×2零矩阵（初始化不使用）；rah=.09、rb=.02、rb_gap=.07、Tt=.1、rho=.05、gamma_c=2、phi=5、劳动权重1。为完整构造既有参数类型，另记录chi_0=.1、chi_1=2、a_bar=1e-6、mu_z=0、sigma_z=0；这些字段不在本次初始化资源式中消费，不是对调整成本的新经济采纳。工资沿已有numerical_bootstrap19语义：初始20与参考税.05构成19，合成省序A/B、origin0、税向量[.05,.05]、迁移楔为零矩阵，并明确V010_TOTAL_WEALTH_NUMERICAL_INITIAL_GUESS标签；不是实证工资或真实省份。

该提案只检验新初始化函数的同源资源、正消费、FOC残差诊断、有限V0/资产斜率与F-order身份，严格记录实际调用；不改输入或网格救通过。它不是原冻结20×20×2运行，也不修改原V010 fixture或采纳新经济参数。其输入/资源语义、工程import与8次求根预算必须由Owner另行授权；当前均NOT_RUN。
