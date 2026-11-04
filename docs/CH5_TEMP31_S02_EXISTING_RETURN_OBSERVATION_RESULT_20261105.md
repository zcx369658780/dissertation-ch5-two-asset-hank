# 同S02既有返回观测结果 · 2026-11-05

STATUS=COMPLETED_ONCE__SAVED_RETURN_WITNESS_VERIFIED__STRICT_HA_NOT_CERTIFIED__6_OF6_CLOSED_NO_RETRY
OWNER_EXACT_STATEMENT=好的我授权
DECISION=CH5_TEMP31_S2_OWNER_DECISION_20261105_06.json
DECISION_SHA256=d312214ba37980330e3f2c101a78b187907ebb16a6152afabfc109b74baaad2e
PROPOSAL=CH5_TEMP31_EXISTING_RETURN_OBSERVATION_PROPOSAL_20261104.json
PROPOSAL_SHA256=7a041c77f0f2471fbc9e17607cf8a2ccd505d1a1248d90a66e15270a200e2e61
CODE_CANDIDATE=56b0081c112d1c9239797785b7bca484012535cb
CODE_TREE=3ad359c878b054fcbb7301d89d833daf677d8bde
INTENT=temp31_s2_s02_existing_return_20261104
SYNC=PENDING_SYNC_AFTER_PRIOR_SSH_PUBLICKEY_REFUSAL__NO_NEW_PUSH_OR_FALLBACK

## 本次授权及实际链条

Owner批准先前具体展示的同S02=(rah .05,rb .015,家户净工资19)一次既有返回观察。第6份独立不可变决定、5份历史决定/账本、120秒/2GiB/零重试限额先登记；未重开第5次意图或借用旧初始化余额。意图保留提案原20261104名称，实际登记/执行为20261105，日期不重置额度。冻存提案的owner_run_approved=false是历史请求，授权通过CURRENT中的批准副本与新决定绑定，未改写原请求。

启动前两处活动树干净，治理HEAD=0b57d8e980995de6478be9a50efe101b406375a7，模型文档HEAD=3ec4fb4a876b91b2c3a1092e8b0a1c3ef86a1d4c；来源/输入/fixture/环境及历史保护核验匹配。算法冻结决定7975c4f...、11科学模块bytes/Blob/SHA-256和MATLAB原件保持。监督器创建唯一科学子进程，Job在恢复前绑定，限1活动进程、120秒含导入、2GiB。

唯一进程24.406秒、峰值提交内存1,377,935,360 bytes，exit0/RETURN_VERIFIED，退出及资源清理确认。初始化1、Python/native Brent各800，HJB1/线性22/policy17600，原KFE1/线性1、汇总1；没有producer、31省、GE、IRF、校准或真实数据运行。HJB收敛22轮、原值函数变化量2.126348430664393e-9；原参数/网格/原收敛规则未动。

原HJB返回后、原KFE之前，外层保存36个既有公开数组/CSR向量及8个800×800矩阵shape；未增加HA内部字段或钩子、重算policy或替换返回对象。KFE继续使用同次post_convergence_operator.full、原固定行/raw求解和原网格权重归一化。

## 新观测回答了什么

41份原运行文件在解码前封存。新的value/consumption/labor与原HJB见证完全一致，post full CSR与原HJB/KFE算子副本完全一致。与第5次已封存S02逐项比较，网格、初始化、HJB、KFE和HA汇总5个NPZ共29数组的header和值全部相同，最大数值差0；本次补证未改变旧S02联合价格假设不受支持的结论。

| 同次实际返回算子 | 最大绝对行和 | 行和缺口格数 | 负非对角项数 |
| --- | ---: | ---: | ---: |
| HJB迭代 full | 0.47898600898711785 | 38 | 8 |
| 原后置 full（实际KFE输入） | 4.301780456264862 | 14 | 0 |

表中计数沿用探索分箱abs(row sum)>1e-10及offdiag<−1e-12，仅为诊断口径，非新科学接受阈值。两类明显行和缺口均位于b上边界，均由bb分量体现；aah与bswitch行和在浮点误差量级。两类算子并不相同：full最大单项差41.53810939391825、矩阵无穷范数差83.0762187878365；aah也有差异，bswitch逐项相同。差异来自原HA返回的两套对象，未发现交接换算子或源码漂移。本结果既不授权替换迭代算子，也不证明它满足KFE生成元条件。

40个b上边界格中，14格mu_b>1e-12、25格mu_b<−1e-12，另1格落于零分箱；最大向外总漂移1.5848664838870548。14个正漂移格与原post的14个行和缺口逐格一致，原标签均liquid=F/transfer=B。对这些实际保存值，row_sum(post)=-mu_b/db；全网格外向边界速率与post行和的对应误差上界5.94e-15。这里只做保存值算术核查，未重算政策或生成替代算子。上b边界transfer=B不等于总mu_b向内；这一固定输入下的事实不能外推为所有价格都失败。

两套算子的密集逐行核查与CSR路径一致，Unicode标签另用UTF32解码交叉核对。新读器7个小格式夹具通过（数值、Unicode、对象类型/非法字符/截断/非有限拒绝）；科学模块导入和求解调用均0。不是外部独立科学评议。

## KFE结论及限制

原固定行系统残差4.786752591523502e-17，归一化质量约1；但完整原算子驻定残差3.6435094863120474。残差集中在被固定行替换的第295号零基方程，其余方程最大残差约1.03e-15；密度加权行和与全局质量变化算术一致，约−0.706497684326436。b上边界条件质量0.8514208544985201。原KFE完成和归一化并不消除原方程的缺口，不能据此认定稳态合格，也不能据此作边界质量的因果归因。

HJB22轮收敛只认证原停止规则在此输入满足，不认证算子守恒、KFE严格驻定或科学接受。严格criteria_reference/thresholds仍null；FORMAL_SOURCE_FREEZE、consumer_ready、formal_ha_accepted、科学接受、Results、model_activation、REAL_GE均FALSE。HA算法锁与全项目正式来源冻结是不同记录。

离线第一版核查曾把initial_value的物理存储也要求与初始化输出完全一致而停下。只读定位为原HJB.copy()将F存储转为C存储；按同一[b,a,z]坐标逐格比较完全相同、差0。保留失败脚本/发现，修正外部核查的存储假设后完成；没有改科学数组、HA代码或重跑模型。前一工程56项检查未重复运行；不能将本次离线修正当作第7次科学额度。

## 当前目标、阻塞与待讨论方向

已有目标仍是固定黑箱HA下获得可解释、可复核的家户稳态，再讨论多省份接线。HJB原收敛门在S01/S02已通过，当前阻塞转为完整后置KFE算子的边界守恒和原驻定缺口，严格接受标准也尚未绑定。迭代算子的额外符号问题已由本次见证揭示，应如实纳入后续可行性判断。

后续如继续价格路线，应先以历史认证离散点及这次保存证据讨论具体外部价格候选、观察目标及有限额度；不能仅凭HJB收敛扩展为连续可行价格盒，不能承诺再减rb即可解决KFE，也不能绕过黑箱修改算法/网格/边界/归一化。本轮只交付事实和讨论建议，不创建S03或任何后继运行提案/意图。

CURRENT=CLOSED_COMPLETED_NO_RETRY，第6次1/1、累计6/6已用，重试0。下一次科学运行须新具体Owner决定。旧初始化3/10余7保持原8格范围，工资/补录各1/1关闭；R12 STOP、R13未授权、WASM6 STOP、OWNER_BASELINE_REBIND未授权、16项义务及历史dirty树不变。

原数组/标签/日志及本轮控制器/分析/校核仅LOCAL_ONLY。治理文档与模型文档本地同步；模型代码仍本地，GitHub仍待同步，未在旧SSH拒绝后推送重试、换身份/协议或借API绕过。完成后停止。

只读远端引用刷新（2026-11-05）：main=b7e595ceb1cd7ffb5adfbf54e2de4e65f01090a5，治理分支=0ce082ead04102b2fa682cae4f3b6cd18e9fb61f。仅读取远端身份，未同步本地新文档、未修改本地remote-tracking refs，也未合并main。
