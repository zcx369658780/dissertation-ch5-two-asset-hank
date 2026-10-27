# 三个primary宏观原件：位置及身份矩阵

本轮C授权放宽到有限项目内位置，实际定位4/8；未取得任何允许原件，原始哈希0/3。不是把上一轮单一路径STOP直接重复为新结论。

| 原始basename | 本次准确相对路径 | 源码expected SHA-256 | 存在性/实际bytes/SHA | 证据层级 |
| --- | --- | --- | --- | --- |
| 中国各省省会地理距离矩阵.xlsx | data_local/matlab_primary_source_snapshot/中国各省省会地理距离矩阵.xlsx | 26e44d174a8effbdca526d95da38f0e5883e0c78fdfd036d2dff1d1fba5a3566 | ABSENT_AT_TESTED_PATH；bytes/SHA=NOT_MEASURED | SOURCE_METADATA_ONLY（存在性观察），不是原件认证 |
| 2000年后各省数据_填充NA.xlsx | data_local/matlab_primary_source_snapshot/2000年后各省数据_填充NA.xlsx | c826b01b6c124eaaadc063dfc2d5510e50e72ed85bb34848f28ab318e4b88929 | ABSENT_AT_TESTED_PATH；bytes/SHA=NOT_MEASURED | SOURCE_METADATA_ONLY（存在性观察），不是原件认证 |
| R语言估计结果_plm估计.xlsx | data_local/matlab_primary_source_snapshot/R语言估计结果_plm估计.xlsx | a6f444fcccb30cb93aa5de084f1dd163c54e5f53c4287c2cd3e13a045eb64a68 | ABSENT_AT_TESTED_PATH；bytes/SHA=NOT_MEASURED | SOURCE_METADATA_ONLY（存在性观察），不是原件认证 |

四次元数据顺序：Q01距离矩阵默认路径、Q02填充宏观工作簿、Q03回归工作簿、Q04项目data_local直接目录。前三条缺失，Q04为DIRECTORY_ABSENT，故没有可进入的primary/matlab命名直接子目录，也没有进行递归。依据代码与持久化合同没有另一条具体且获准的项目内相对位置；没有用私有绝对root扩展范围，extra路径检查0/2。查询剩余4次不是继续猜目录的许可。

expected来自EMPIRICAL:34–38、74–82；WORKER:155的默认根为data_local/matlab_primary_source_snapshot。没有打开xlsx单元格、header、zip或数据sheet，没有原件复制/搬迁/改名/换行，没有从Downloads或私人目录取代原件。Git-style Blob也NOT_MEASURED；源码常量不能填成原件hash。

这只排除本轮4个准确位置/锚点，不断言整个仓库、任意本地根或历史都没有这些文件。即便未来原始字节匹配也只到SOURCE_FOUND_NOT_MODEL_ADOPTED，不证明31省ID、年份/vintage、经济统计单位、当前canonical或TEMP31采用。
