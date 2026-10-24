# CH5 会话交接｜历史 Python 基线与隔离修订候选待 Astra 独立审阅

**记录日期：** 2026-10-24（北京时间）  
**性质：** Owner 单次明确授权的 GitHub 里程碑备份；不恢复 GitHub 日常任务中转工作流。  
**本次写入前治理分支 HEAD：** `3cdfd1cbb308fae79ffac9ab9f846b48c1402a42`

## 1. 新会话第一项工作

Owner 已上传历史 Python 基线恢复与隔离修订候选的离线交付 ZIP。**下一会话应先独立审阅此 ZIP，不要自动签发新的科研任务。**

- ZIP：`CH5_TEMP31_HISTORICAL_BASELINE_PATCH_CANDIDATE_R1_OFFLINE_REVIEW_20261024.zip`
- 大小：131,442 字节
- SHA256：`36143632a1497d3f7e470bafbc3155ac5d1937b104f02169e939ec7bf0e7959c`
- 外层成员：5；内层成员：28
- Codex run_id：`156211a0597e49c4a40f37e5c9489812`
- 自报终态：`PASS_BOUNDED_HISTORICAL_BASELINE_IDENTIFIED__PATCH_CANDIDATE_READY__GPT_REVIEW_PENDING`
- **当前状态：GPT/Astra 独立科学审阅尚未完成；不等于 Owner 接受，也不等于正式来源冻结。**

Owner 提供的本地 ZIP 路径不写入公开文档；以文件名、字节数和 SHA256 识别上传原件。

## 2. Owner 最新决定

Owner 明确选择：以**2026年9月初首次成功复现 MATLAB 多省份 HANK 的 Python 版本**作为后续修订基础；由 GPT/Astra 审阅 MATLAB 原程序、博士论文 TeX 和隔离候选，审阅通过后再由 Owner 决定是否冻结新的正式来源。

历史验证记录所支持的案例：
- corrected-2009 稳态；
- Python：`SOURCE_CONVERGED`；
- 184轮外层迭代、5,704次家户调用、31/31省家户收敛；
- 历史 MATLAB 对照：184轮、5,704次调用。

以上是**历史指定案例**的证据，不表示候选修改后已重现收敛，也不表示所有财政、劳动和生产接口都正确。

Owner 本轮没有授权正式 V010 修改、正式来源冻结或 HA/HJB/KFE/outer/GE/IRF/真实31省校准。

## 3. 本轮 Codex 报告的基线身份（等待 Astra 独立审阅）

- 候选历史基线 commit：`ba98537fd5ae004f0aa37d319865da1f1739e503`
- tree：`f432f0acb5d94e0f60cd976b74a236be883e0db3`
- 历史 HA 导出 SHA256：`b92f6efc59d9398f89f8fb6ee67bf6c5f947282d76895051bec194967ec9c3e3`，报告称与原入口 guard 匹配且 guard 未修改。
- 早前候选锚点 `94de4501dec051b969bee9d852eba2d4591f30ef` 在本地对象库中 missing；本轮未将其当作来源，交付含候选比较表。
- Codex 报告通过 `git cat-file` 对390个原始 Git 文件逐件核验长度、Git Blob、SHA256并导出。
- 本轮选择依据是原 pre-science-gate 执行 authority、固定 SHA 的 Python 终态/比较器及正式接受链，而不是仅按日期或184/5704计数选择。
- 原始390文件与正式工作树未改；本机 HEAD 前后为 `a1db8c114dec0ab69d69a5576e153a7f868cba0e`，refs摘要和 Git index摘要前后相同。上述均为 Codex 回执事实，仍需 Astra 根据 ZIP 内证据独立核验。

## 4. 隔离候选包含的变化

交付报告称原 Python 候选只有三处一行改动：
1. `src/ch5_two_asset_hank/multi_province/wage.py`：综合工资一般公式中 `alphal` 的幂次修正为 `1/(1+phi_l))。
2. `src/ch5_two_asset_hank/multi_province/firm.py`：工资税收入候选改为 `lt * wjt * tau)，待 Astra 核验工资单位与税率口径。
3. `validators/multi_province/mp4b_python_empirical.py`：反转目的地劳动厌恶偏好方向，使目的地生产率指标较高时厌恶系数较低；动态指标仍为 `Y/L)，未替 Owner 决定改用现实/滞后人均 GDP。

另有不接生产调用的 `isolated_bridge_candidate.py`，包括劳动桥、私有净工资切片、工资账和 GDP 目标残差帮助函数。该文件明确声明生产绑定仍 BLOCKED。

TeX 草稿只修订第三章 `c3.tex) 的综合工资一般公式；`c5.tex) 原有来源/目的地下标方向被判为正确，不应机械反号。若有 `c5_` 前缀文件，不能未经证据将其认定为最终权威原稿。

`Lt\rightarrow Lt_{prev}` 映射缺陷在本轮选定基线中已修复，不应重复改动。

## 5. 限域测试与资源（Codex 自报，待 Astra 核验）

- 合成场景：2省、3省、31省。
- 2,132项数值对照；5项预期拒绝/保护测试。
- 最大绝对差：`1.81898940355e-12`；最大相对差：`8.32667268469e-16`。
- 便携纯算术重放：1,046项通过。
- 未运行历史184轮/5,704次家户科学验证；未运行原控制器、生产 firm、正式 one_turn 或真实31省校准。
- 实耗：1,027.489363秒；显式进程60次（PowerShell 14、Python 16、只读 Git 28、rg 2）；E1=1（git archive 的 CRLF 表示问题，随后通过原始 blob 导出恢复；源码/guard未改）。
- 网络/GitHub、正式 HA/HJB/KFE/roots/outer/GE/IRF、正式 one_turn/生产 firm、真实31省校准、正式源码/TeX/Dirty/index/refs写入均为0。
- GPU与系统全局进程指标：UNKNOWN。

## 6. 尚未解决的 E3 与绝对边界

仍待 Owner 决定或后续证据支持：
- 动态 `Y/L`、现实人均 GDP、滞后人均 GDP 的指标与时点；
- 唯一当前生产回调、净工资实际接线及最终 household batch/价格快照规则；
- 完整价格残差、HA残差与 GDP 目标残差标准；
- HU、居民/就业/效率劳动/工资/资产共同单位与模型期间；
- 迁移楔 `sigma` 的收受方、现金/资源含义；
- 完整财政边界与单位；
- 是否接受隔离候选并正式冻结新来源。

保持：
- `FORMAL_V010=UNCHANGED`
- `V011=NOT_STARTED`
- `Results=FALSE`
- `model_activation=False`
- `REAL_GE=False)
- `FULL_RUNNER_IO_CLOSURE=BLOCKED)
- 三个历史 PENDING Review 原样保留。
- 历史 STOP 与已关闭预算不追溯改写、不自动续期。

## 7. 下一会话建议流程

1. 读取 Owner 上传的 ZIP 原字节，独立核对外层/内层成员、manifest、SHA256、CRC、路径安全和有限隐私。
2. 重点审阅 `CANDIDATE_DIFF.patch`、`HA_W_TAU_USAGE_INVENTORY.json)、`BASELINE_IDENTITY_AND_FILE_MANIFEST.json)、`HISTORICAL_VALIDATION_AND_SOURCE_MAPPING.json)、`NEW_CANDIDATE_TEST_RESULTS.json)、`APPROVED_CHANGE_REVIEW_AND_E3.md) 和 `TEX_FORMULA_CANDIDATE.tex)。
3. 区分历史基线身份成立、隔离数学候选通过、经济学制度采纳、正式来源冻结四种不同结论。
4. 向 Owner 报告需要其决定的 E3；不因 Codex 自报 PASS 自动接受候选。
5. 不在没有新的明确授权前签发下一科研任务或启动任何正式 HA/GE。

## 8. 本次 GitHub 备份范围

本次 GitHub 写入是 Owner 为会话交接作出的单次明确授权，仅更新本交接文档、CURRENT、TASK_CURRENT、DOC_INDEX_CURRENT 与项目长期记忆的当前状态段。此举不恢复 GitHub 自动任务/Review中转工作流；日常工作仍为离线 MD → 本地 Codex → Owner手动上传 ZIP → Astra独立验收。


## 9. GitHub 持久记录导航

- Owner决定：[CH5_TEMP31_OWNER_DECISION_HISTORICAL_PYTHON_BASELINE_20261024.md](CH5_TEMP31_OWNER_DECISION_HISTORICAL_PYTHON_BASELINE_20261024.md)
- 任务与交付摘要：[CH5_TEMP31_HISTORICAL_BASELINE_PATCH_CANDIDATE_TASK_RECORD_20261024.md](CH5_TEMP31_HISTORICAL_BASELINE_PATCH_CANDIDATE_TASK_RECORD_20261024.md)
- 当前索引：[DOC_INDEX_CURRENT.md](DOC_INDEX_CURRENT.md)
- 当前状态：[/CURRENT.md](../CURRENT.md) | [TASK_CURRENT.md](../TASK_CURRENT.md) | [项目长期记忆](CH5_PROJECT_MEMORY_CURRENT.md)
