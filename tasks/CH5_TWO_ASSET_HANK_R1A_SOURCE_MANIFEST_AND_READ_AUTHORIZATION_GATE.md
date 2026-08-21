# CH5_TWO_ASSET_HANK_R1A_SOURCE_MANIFEST_AND_READ_AUTHORIZATION_GATE

Repository:

zcx369658780/dissertation-ch5-two-asset-hank

Purpose:

Establish the authoritative MATLAB/dissertation source package required for R1A economic provenance binding.

This is a source authorization and provenance task, not an implementation task.

## Objective

Provide a precise, auditable source manifest before binding Chapter 5 two-asset HA equations.

## Required Source Binding

Identify and record:

1. Dissertation source materials:

- exact file path;
- page/section/equation location;
- version/date if available;
- hash or provenance identifier.

2. MATLAB source materials:

- exact root directory;
- entry files;
- dependent files;
- version/provenance information;
- SHA-256 or Git blob hash where available.

Known candidate source provided by Owner:

C:\\MatlabProgram\\2023年12月2日 多省份神经网络HANK\\HANK_2ASSETS\\HJB.m

This path is a candidate source reference only and must be verified.

## Required Output

Create a source manifest containing:

- authority ranking;
- source inventory;
- selected authoritative files;
- duplicate/conflicting source handling;
- variable/equation provenance mapping;
- unresolved ambiguities.

## Required Equation Targets

Bind sources for:

- household budget constraint;
- asset drifts mu_a and mu_b;
- adjustment cost chi(d,a);
- transfer/control convention;
- returns;
- taxes/transfers/borrowing spread;
- productivity process z and Q_z;
- utility and labor disutility;
- asset boundaries and KKT conditions.

## Forbidden Operations

Do not:

- modify MATLAB files;
- modify Python source;
- run MATLAB;
- run HJB/KFE solver;
- infer equations from DSH code;
- infer missing equations from generic HANK literature;
- create Results claims.

## Terminal Classification

Use one:

- CH5_TWO_ASSET_HANK_R1A_SOURCE_MANIFEST_COMPLETE
- CH5_TWO_ASSET_HANK_R1A_SOURCE_MANIFEST_BLOCKED_MISSING_ACCESS
- CH5_TWO_ASSET_HANK_R1A_SOURCE_CONFLICT_REQUIRES_OWNER_DECISION
