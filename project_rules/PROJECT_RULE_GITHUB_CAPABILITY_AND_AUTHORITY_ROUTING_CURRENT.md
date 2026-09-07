# GitHub 能力、授权与发布核验
更新：2026-09-07；仓库：zcx369658780/dissertation-ch5-two-asset-hank。

## 能力与角色
先检查已提供的 GitHub 操作及目标仓库访问，再判断能否执行。不能把“尚未核验 mutation”误写成“没有 GitHub 能力”。
Reviewer 在用户授权范围内可发布任务、规则、状态和交接，核验提交及报告。GitHub 写权限不等于科学执行权限。

## 发布
草拟具体变更 → 检查 scope 和内容 → GitHub 原子提交/发布 → 一次独立 readback → 提供 Builder prompt。
同一主题的多文件变更可一次提交。create blob/tree 等中间对象不需要分别发起验收任务。
发布后核验仓库、目标 branch、commit、允许变更路径及内容身份。mutation 返回成功本身不代替最终 readback。

## 主分支变化
非 force 更新，保留并发提交。发布前如 main 变化，审阅相关 diff 后重新基于 live main 构造变更。
启动任务时不要求 main 恰好停在 task 发布 commit；只要 task 有效、未被取代且科学输入/前提未变即可。
科学源、输入、容差或 authority 有实质变化时重新评估；不静默合并冲突。

## 边界
聊天不替代科学 task；未发布不得声称已发布。历史 task 不追溯扩权。
用户对本次治理更新与本地文档同步的授权明确成立；后续科学实验仍需自己的明确 task 和预算。
