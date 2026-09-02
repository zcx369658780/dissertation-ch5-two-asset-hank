# MP4C CHNCapitalStock candidate reproducibility audit

## Terminal

`MP4C_STORED_R_CHNCAPITALSTOCK_REPRODUCIBILITY_UNRESOLVED__HANK_RERUN_NOT_AUTHORIZED`

The Owner-designated `R语言计算资本存量` sheet remains a candidate, not an
authorized HANK capital input. Its positivity cannot establish provenance or
correctness.

## Blocking evidence

The required independent reconstruction cannot be uniquely recovered locally:

- no `Rscript` executable is available on this host;
- no identifiable local R script, `CHNCapitalStock` package source, package
  metadata/version record, lockfile, or deterministic capital-construction source
  was found in the protected project tree;
- consequently package/function, version, inputs, initial-capital rule,
  depreciation, deflator/price-base treatment, NA preprocessing, units and
  stored-sheet generation lineage cannot be proven.

The task forbids network installation, package upgrade, guessing defaults, and
substitution based on positivity. Therefore no bounded R verification run was
possible, no stored-versus-reproduced cell comparison exists, and neither V1 nor
V2 can be claimed.

## Scope preserved

No MATLAB HANK, R PLM, Python stationary/household/HJB/KFE, comparator, shock,
IRF, R5, or Results computation was run. The historical annual batch remains
engineering-only evidence. Owner-A intended calendar semantics are not rejected,
but corrected inputs, unit/scaling proof, the 15-year preflight, and the exactly
eight-worker batch remain unauthorized pending recoverable capital construction
evidence.

## Required next authority

Provide the exact local R runtime or an exact package/source snapshot plus the
frozen raw input lineage used to generate the stored sheet. A new task can then
authorize an offline deterministic reproduction and strict 24-by-31 cell audit.
