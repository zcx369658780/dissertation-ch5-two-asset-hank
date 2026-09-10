# Chapter 5 MATLAB 2018 input-data and initial-state comparison audit — Reviewer acceptance

Date: 2026-09-10.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Accepted candidate: `1321b7a227e6b1e341623222eeecd11748189727`.

## Verdict

`MATLAB_2018_INPUT_DATA_AUDIT_ACCEPTED__MATERIAL_EXTERNAL_SCALE_AND_YEAR_MIXTURE_CONFIRMED__NO_CAUSAL_COLLAPSE_CLAIM`

Reviewer accepts Builder verdict:

`MATLAB_2018_INPUT_DATA_AUDIT_PASS__MATERIAL_EXTERNAL_SCALE_DIFFERENCES_IDENTIFIED`.

## Evidence reviewed

- candidate commit and changed-file scope relative to `31b8de0ef897e3edd8b88115e5cd64be2b8aa80c`;
- main audit report;
- 31-province comparison ledger, including Anhui row;
- zero-call ledger;
- test receipt.

The candidate is one commit ahead of the publication baseline and contains only the audit report, repository-safe ledgers/receipts, validator code and focused static tests required by the task.

## Accepted findings

1. The original MATLAB object labelled 2018 is a mixed-vintage object: GDP/CAP/POP are taken from panel row 10 corresponding to 2009 levels, Zt is reconstructed from row 21 corresponding to 2020 levels, while alpha uses PLM vintage 19.
2. Alpha matches the corrected canonical 2018 value exactly in all 31 provinces.
3. GDP and capital differ materially in all 31 provinces; population and Zt differ materially for subsets of provinces.
4. The capital source/transform route carries an additional dimensional-scaling ambiguity: a source documented in 万元 is multiplied by the same `x1000` multiplier used for GDP in 亿元, with no source-side dimensional rationale established by this audit.
5. GovInv is initialized from Kt0 and therefore inherits the same year/scale issue.
6. Original MATLAB 2018 persisted household aggregates, Kt_supply, first-turn firm prices and next-turn composite prices are unavailable without a scientific rerun because the expected 2018 steady-state cache is absent.
7. Scientific/model calls for this audit are accepted as zero. The task supports a data/provenance diagnosis only and does not identify the cause of the accepted turn3 aggregate-asset collapse.

## Anhui-specific finding

Anhui is materially affected:

- GDP: `10864.68` vs corrected `34010.9` 亿元, relative difference `-68.0553%`;
- capital: `228121755.48548824` vs corrected PIM `1357314108.2013683` 万元, relative difference `-83.1931%`;
- population: `6131` vs `6076` 万人, relative difference `+0.9052%`;
- Zt: `0.000641551386937363` vs corrected same-year `0.0006934644495858679`, relative difference `-7.4860%`;
- alpha: exact match at `0.772866243094144`.

The large Anhui discrepancy is therefore real in the audited data route, and is dominated by GDP/capital year-level differences rather than population or alpha. It is a plausible outer-loop scale concern, not a proven cause of instability.

## Scientific boundary

No household/KFE/firm/outer-loop rerun is authorized by this acceptance. Results eligibility remains `FALSE`.
