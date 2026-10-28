# 目录角色与证据强度

|对象|角色/属性|证据|可信边界|
|---|---|---|---|
|ANCESTOR_00/01|PROJECT_LOCAL_WORKTREE_DIRECTORY；旧属性16、非reparse|固定前候选hash对应的两份私有记录复用|本轮未重新lstat上层；不认证目标或科学采用|
|ANCESTOR_02|PROJECT_LOCAL_WORKTREE_DIRECTORY；安全父侧、旧/新属性16|旧记录已逐件pin；新增一次lstat核对|只认证所测元数据字段，非安装来源|
|ANCESTOR_03|LEXICAL_DEPENDENCY_DIRECTORY；旧/新属性1040|私有精确命名线索、深度3及新lstat|只作词法角色分类，不证明物理来源|
|ANCESTOR_03 native tag|0xA0000003，IO_REPARSE_TAG_MOUNT_POINT|Python/Windows lstat原生字段及stat常量|标签类别；不确定目标路径或junction/volume-mount子类型|
|安全侧构建/依赖声明|NO_ADMISSIBLE_MANIFEST|允许映射/记录未指定准确文件路径|不代表磁盘上不存在文件；未猜测/搜寻|
|物理来源/依赖刷新/重命名/WASM安全|OTHER_OR_UNKNOWN / BLOCKED|无获准可读来源清单或目标内容|不得采纳新保护基线|

真实组件名称、私有精确层级映射及目标路径不在GitHub。词法类别的原始名称对应关系仅Owner可核。
