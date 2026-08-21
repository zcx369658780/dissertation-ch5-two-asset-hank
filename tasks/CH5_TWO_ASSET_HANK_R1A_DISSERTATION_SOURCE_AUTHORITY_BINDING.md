# CH5 Two-Asset HANK R1A Dissertation Source Authority Binding

## Project

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Gate:

`R1A_SOURCE_PROVENANCE_BINDING`

Task:

`CH5_TWO_ASSET_HANK_R1A_DISSERTATION_SOURCE_AUTHORITY_BINDING`


## Objective

Bind the dissertation source authority for Chapter 5 Two-Asset HANK Reconstruction.

The purpose is to establish:

1. dissertation identity;
2. version and provenance;
3. Chapter 5 equation authority;
4. MATLAB correspondence boundary.

This is a source authority task only.

No model implementation is authorized.


## Authorized Sources

Dissertation source candidate:

`D:\Articles\2023年9月25日 博士毕业论文TEX稿件`

Uploaded dissertation PDF:

`基于异质性新凯恩斯模型的中国经济区域均衡协调发展研究.pdf`

MATLAB provenance source:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`


## Local File Safety

The following directories are STRICTLY READ ONLY:

- `D:\Articles\2023年9月25日 博士毕业论文TEX稿件`
- `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Allowed:

- read files;
- calculate hashes;
- generate reports outside protected directories.

Forbidden:

- modify;
- rename;
- delete;
- overwrite;
- create files inside source directories.


## Allowed Operations

Read-only audit only:

- identify dissertation file;
- record SHA-256;
- record version/date;
- locate Chapter 5;
- locate relevant equations;
- create equation inventory;
- map dissertation concepts to MATLAB provenance.


## Required Output

Create:

`docs/CH5_TWO_ASSET_HANK_R1A_DISSERTATION_SOURCE_AUTHORITY_BINDING_REPORT.md`

Report must include:

1. dissertation identity;
2. source hash;
3. Chapter 5 location;
4. equation inventory;
5. variable inventory;
6. MATLAB correspondence map;
7. unresolved conflicts;
8. next gate recommendation.


## Forbidden Operations

Do NOT:

- run MATLAB;
- run Python model;
- implement HJB;
- implement KFE;
- modify solver;
- calibrate parameters;
- generate numerical results;
- judge model correctness;
- enter equation freeze.


## Acceptance Criteria

PASS:

- dissertation source formally designated;
- provenance recorded;
- Chapter 5 equation authority identified;
- unresolved issues documented.

If source authority remains ambiguous:

Return:

`BLOCKED_DISSERTATION_SOURCE_AUTHORITY_NOT_AVAILABLE`


## Next Gate

`CH5_TWO_ASSET_HANK_R1_EQUATION_SPECIFICATION_FREEZE`
