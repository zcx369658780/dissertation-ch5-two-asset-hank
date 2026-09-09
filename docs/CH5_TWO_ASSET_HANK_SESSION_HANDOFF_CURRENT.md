# Chapter 5 当前交接
更新：2026-09-09。唯一活动仓库zcx369658780/dissertation-ch5-two-asset-hank。
Owner最终科学authority；ChatGPT Reviewer规划/验收/发布；Codex bounded Builder。默认gpt-5.6-sol / medium，除非task明确例外。

## 当前状态
最新接受候选51ba55709dcec2ef82163f6f9f1766ba6ff90f32；验收整合main检查点a9420502e0b3f307a216b58fffd1b0b67d47e8bf。先fresh读live main，不把检查点当永久HEAD。
状态：OWNER_APPROVED_SINGLE_HOUSEHOLD_B_DOMAIN_EXPANSION_ACTIVE。
活动任务：tasks/CH5_MP4C_CALL725_RAH_0P07_B_DOMAIN_EXPANSION_SINGLE_HOUSEHOLD.md。
Owner批准流动资产b范围的小规模单户验证，并明确不要直接运行多个省份。生产参数/网格不改。

## 前置结论
- 安徽call725原参数rah=.09：原生HJB100未收敛，KFE non-finite；历史入口匹配。
- 单户仅rah改为float('0.07')并原生初始化：HJB26收敛，KFE/aggregate返回；只支持局部收益率+初始化链敏感性，不是.07安全定理或生产ramax修改依据。
- .07返回g不满足原Tg=0。29个upper-b外向rate的density-weighted escape=.6697587443279651，row replacement丢弃的唯一物质性方程隐含补入同量source；该source/escape解释只限有限箱代数，不是经济source法则。
- Qh仍有21负非对角元；生产数值有效性、2018修正年度、真正动态与Results都未接受。

## 本任务唯一新干预
Owner原格点：I20，b[-2,5]；J20，a[0,10]；Nz2，z[.8,1.3]。
新诊断只对安徽call725 rah=.07单户扩b上界，不跑firm/其他省份/GE/年度：
- 精确复用旧b前20节点；按旧db=7/19数学间距追加19节点，I39，上界约12；
- a/z/switch及全部经济状态、a_bar、原生初始化、helper、solver、Delta1000、crit1e-7、HJB maxit100不变；
- 旧bmax5 .07结果只读，不重跑；
- 新科学预算1初始化（<=1560 root/brentq）、1 HJB（<=100 solves）、自然到达时1 KFE/direct solve与1 aggregate；一个Python进程，科学开始后不重启；其余模型/MATLAB调用0。

源pin由state_count决定，1560状态下预期k576，物理坐标需实测。KFE density/aggregates因此不是固定pin纯bmax对照，必须作为次级诊断。主要看HJB、expanded upper-b drift/Q质量缺口、原Tg残差、tail/top-face质量和source/escape账本。单个扩箱点不证明网格收敛或生产bmax应改。

## 本地保护
工作目录D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001。旧.07科学根D:\ProjectTemp\ch5-call725-rah-0p07-native-init-20260908-002只读；新任务外部根D:\ProjectTemp\ch5-call725-rah-0p07-b-domain-expansion-20260909-001（占用用fresh suffix）。原D:\ResearchCode checkout、未跟踪文件、历史分支/证据保留；保护MATLAB根只读。不混入deep-learning-hank/Zotero/旧R5。
