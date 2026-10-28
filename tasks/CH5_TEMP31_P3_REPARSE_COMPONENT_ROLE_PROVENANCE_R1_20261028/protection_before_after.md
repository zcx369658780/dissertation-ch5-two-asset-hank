# 保护快照及基线分层

|时间点|status SHA-256|非空NUL记录数|基线身份|
|---|---|---|---|
|历史旧记录|c443420c888f5e776cfb6cd05b27cbed56e58a787b82639aa23a47ce7f2ac2f3|5971（既有任务）|历史保留；不在本轮重读原始流|
|既有恢复观察|734f11763de35c822f7fbf9a3ab8e2c6b8fb0ae7c8e7c49174ae3e19948e865b|5971（既有记录）|未采纳为新可信基线|
|本次BEFORE|734f11763de35c822f7fbf9a3ab8e2c6b8fb0ae7c8e7c49174ae3e19948e865b|5971|新测观察|
|本次AFTER|734f11763de35c822f7fbf9a3ab8e2c6b8fb0ae7c8e7c49174ae3e19948e865b|5971|新测观察|

BEFORE UTC=2026-10-28T01:35:52.801264+00:00；北京时间=2026-10-28T09:35:52.801264+08:00。AFTER UTC=2026-10-28T01:40:18.442589+00:00；北京时间=2026-10-28T09:40:18.442589+08:00。

HEAD=a1db8c114dec0ab69d69a5576e153a7f868cba0e；branch=codex/ch5-mp4c-k1b-turn5-turn6-bounded-continuation-20260922；index SHA=28058a7e2d9ab773c5813205c75999e6c221533aeae0b9bb094b9a83451bf7cc；refs SHA=600912e7f3dabd0661d2314f533bb432d95cf4bd35b622ab5b16d6149e3c6729，count=243。两次11件保护资产bytes/SHA均匹配既有执行者保护身份，别名逐项见source_inventory。

捕获模式：`git --no-optional-locks -C SCIENCE_TREE status --porcelain=v1 -z --untracked-files=all; raw refs for-each-ref --format=%(refname) %(objectname); raw index SHA256`。原始NUL状态流留本地，不公布其他未跟踪记录。两次保护快照预算已关闭；AFTER后只处理证据和隔离GitHub候选，不再访问科研树。状态稳定不证明历史漂移来源，也不构成P3解阻或新基线批准。
