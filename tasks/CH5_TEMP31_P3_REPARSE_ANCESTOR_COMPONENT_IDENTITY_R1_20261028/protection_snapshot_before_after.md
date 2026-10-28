# 保护快照

|时间点|status SHA-256|NUL记录|证据性质/保护选择|
|---|---|---|---|
|历史旧基线|c443420c888f5e776cfb6cd05b27cbed56e58a787b82639aa23a47ce7f2ac2f3|5971（既有冻结记录）|保留历史，不在本轮读取或重写原始流|
|既有恢复观察|734f11763de35c822f7fbf9a3ab8e2c6b8fb0ae7c8e7c49174ae3e19948e865b|5971（既有记录）|不是Owner已采纳新基线|
|本次BEFORE|734f11763de35c822f7fbf9a3ab8e2c6b8fb0ae7c8e7c49174ae3e19948e865b|5971|本次原字节测量|
|本次AFTER|734f11763de35c822f7fbf9a3ab8e2c6b8fb0ae7c8e7c49174ae3e19948e865b|5971|本次诊断STOP后原字节测量|

BEFORE UTC=2026-10-28T00:33:22.123703+00:00；北京时间=2026-10-28T08:33:22.123703+08:00。AFTER UTC=2026-10-28T00:36:23.454128+00:00；北京时间=2026-10-28T08:36:23.454128+08:00。

两次HEAD=a1db8c114dec0ab69d69a5576e153a7f868cba0e；branch=codex/ch5-mp4c-k1b-turn5-turn6-bounded-continuation-20260922；index SHA=28058a7e2d9ab773c5813205c75999e6c221533aeae0b9bb094b9a83451bf7cc；refs SHA=600912e7f3dabd0661d2314f533bb432d95cf4bd35b622ab5b16d6149e3c6729、count=243。11件保护资产各自bytes/SHA两次实测一致并匹配既有执行者保护上下文，公开别名逐项见source_inventory。预期身份不提升为新可信基线授权。

捕获模式：`git --no-optional-locks -C SCIENCE_TREE status --porcelain=v1 -z --untracked-files=all; refs raw for-each-ref --format=%(refname) %(objectname); raw index SHA`。不发布原始NUL流或其他未跟踪记录。保护快照预算2/2已关闭，AFTER以后仅处理缓存和候选GitHub证据，不再访问科学树。Owner正式P3批准是新授权事实，保护基线继续BLOCKED。
