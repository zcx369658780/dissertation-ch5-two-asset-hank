# Chapter 5 Two-Asset HANK Post-P5 D2 Comparator-Field Authority and Heterogeneous Resumption Report

## Terminal classification

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

The static audit and MATLAB heterogeneous-result preflight passed. The single authorized Python comparator preflight then failed on its categorical-behavior assertion: matching `gap/bound` passed, deliberate `gap` and `bound` perturbations correctly failed, but a deliberately perturbed `canonical` value produced a recorded categorical mismatch without a failing exit. The frozen comparator accumulates categorical mismatch statistics but does not append those mismatches to its `failures` list, so its terminal PASS/FAIL remains driven only by numerical failures. The preflight expected exit `2`, observed exit `0`, and raised `AssertionError`.

The comparator preflight call was consumed. Per the live task, no repair/rerun and no replacement D2 scientific call were allowed. This is an engineering preflight/source-contract blocker, not a scientific mismatch. P5 remains Owner-accepted and the voluntary dynamic hold continues.

## Live authority and continuity

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Worktree: `D:\ProjectTemp\ch5-pre-p5-controlled-household-exec-repo-20260829`.
- Branch: `codex/ch5-adjustment-boundary-redesign`.
- Live start `origin/main`: `ee754220fdb39b9cd13af424366cd913b008b2e7`.
- Live task: `tasks/CH5_TWO_ASSET_HANK_POST_P5_D2_COMPARATOR_FIELD_AUTHORITY_AND_HETEROGENEOUS_RESUMPTION.md`.
- P5 marker: `MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`.
- Hold marker: `DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`.
- Accepted Python baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`.
- `git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`: empty.

## Artifact roots and protected identities

- Original household-decision root: `D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-artifacts-20260829-220000`.
- Accepted D1/resumption root: `D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-resumption-artifacts-20260829-223000`.
- Accepted D2 input-container root: `D:\ProjectTemp\ch5-post-p5-d2-container-resumption-artifacts-20260830-001000`.
- Prior result-schema blocked root: `D:\ProjectTemp\ch5-post-p5-d2-result-container-resumption-artifacts-20260830-054500`.
- Current fresh successor root: `D:\ProjectTemp\ch5-post-p5-d2-comparator-heterogeneous-resumption-artifacts-20260830-070000`.

| Artifact | SHA-256 |
|---|---|
| frozen manifest | `D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA` |
| corrected heterogeneous D2 MATLAB | `A7034181F3FC902E39EAB64CB8ED47C77BA52087B4E262325CAD33BAAECE3589` |
| corrected comparator | `EBF1B72AC4ED53791646C5E06345D5D31FE06E16B6E81E618AD73229801EF0AF` |
| frozen D2 Python | `DD9DDCB675BE7A5C3A672CF1936AB7CBA1553AC8334989B2CDAA777FB2914344` |
| frozen D3 MATLAB | `5D94EDF89259D543758E490EA25C9359C1B65588CF7BB0557EEEDFA6B7FF3F9A` |
| frozen D3 Python | `6054A0C59E7C0CD0C83AD1919C3CFAF7B2987D0545EE4CEB26B3345FF2D01ABC` |
| MATLAB preflight source | `F453756446792A39371A85DB9B8A1D6DCCB2E36D059CA3824533B2474D1E9135` |
| comparator preflight source | `ACFC5AD2B3A7DBFB92EFDCFBFF803360F6F3DC7C3E1F35B3E5ABE7BC2B76A150` |
| MATLAB diff record | `94C0732E657A2450F4FCE62A78E111AF67D2F35F1C4D35552FC418473D819F6A` |
| comparator diff record | `F1F97A87A79489A9545EECFD67B40B98ED48BD4CF06CD2AE1AC50FBEDB1DFF92` |
| frozen ledger | `FB217B3E00EA09416241FBF1ADC03A1FA4827C9C06CC77882B15B8008548FCBB` |
| successor freeze | `6C20B9A6526E4A062D3FDB7C7BB4A9872832BA38380F23CC92D0BA22DB38D5F1` |
| final execution results | `84C47713C27EAE0F9475BB5D8815309113ABDAEAB0DE4E620A76AF0802F51B71` |

No production MATLAB/Python source, helper, test, or cache was modified.

## D1 re-verification and zero calls

D1 artifacts were rehashed successfully:

- MATLAB `1FCA5F613C52B2E0F5CC45EF8B06BB96ED171ADB0F79F31A709151F2E91775CF`;
- Python `1C3A63759027AC8FF0F2FD56AB090CB8584110FCD9ACAAFDF937624245324F42`;
- comparison `1B95E6D23A1409874DE2548812FD1C34E11E955A68093C0A2818B54A521712B3`.

Accepted D1 remains `432/432 PASS`, `216/216` low-`a` PASS, all scalar maximum differences `0`, and all sign/direction mismatches `0`. Current D1 MATLAB/Python/comparison calls: `0/0/0`.

## Static schema/comparator re-audit

The frozen manifest contains exactly nine normal cases followed by one `lower_b_fz_near_tie`. IDs and order are unchanged and unique.

Normal MATLAB/Python rows both have exactly 16 fields:

`id,c,l,d,cost,mu_a,mu_b,utility,hamiltonian,a_direction,b_direction,lambda_a,lambda_b,kkt_max,boundary_feasible,boundary_violation`

The near-tie MATLAB/Python row has exactly 10 fields:

`id,canonical,raw,alias_available,gap,bound,boundary_feasible,kkt_max,mu_a,mu_b`

The frozen comparator already consumed heterogeneous rows. The only omitted numerical fields were `gap` and `bound`; no third omitted field was found.

## Authorized diffs

Comparator complete change:

```diff
-... 'kkt_max','boundary_violation']; ...
+... 'kkt_max','boundary_violation','gap','bound']; ...
```

Classification: `COMPARATOR_NEAR_TIE_GAP_BOUND_ONLY`. The existing `factor=128` floating rule and every other comparator line are unchanged.

MATLAB complete changes:

```diff
-function d2_matlab_corrected
+function d2_matlab_heterogeneous_corrected
```

Classification: `EXTERNAL_CALLABLE_ALIGNMENT_ONLY`.

```diff
-rows=struct([])
+rows=cell(1,numel(m.p2))
```

Classification: `HETEROGENEOUS_RESULT_CONTAINER_ONLY`.

Both existing row assignments changed only from `rows(k)=struct(...)` to `rows{k}=struct(...)`.

Classification for each: `HETEROGENEOUS_RESULT_CONTAINER_ONLY`.

The `jsonencode`/write line, `get_case`, all formulas, roots, KKT and multiplier code are unchanged.

## Engineering preflights

### MATLAB heterogeneous-result preflight

- invocation count: `1`;
- exit: `0`;
- result: PASS;
- result SHA-256: `815C6703FECE0438B0584C3AD16A1A772D3A42D2AA57C7F2A4FBA0BF6F6808A4`;
- normal keys: `16`;
- near-tie keys: `10`;
- fabricated fields: `0`;
- input IDs/order/unique: `10/10 PASS`.

### Python comparator preflight

- invocation count: `1`;
- terminal result: FAIL (`AssertionError`), consumed;
- matching fixture: exit `0`, PASS;
- perturbed `gap`: exit `2`, one failure;
- perturbed `bound`: exit `2`, one failure;
- perturbed `canonical`: mismatch_count `1` at index `2`, but failures list empty and exit `0`;
- preflight expected categorical perturbation exit `2`, so its final assertion failed;
- no same-task repair or rerun occurred.

Evidence hashes:

- matching compare: `CF814652F142D14DA6D6B5819A6E01A0EF95E53C541479F37C1EF4F6F13FBD7E`;
- gap perturbation compare: `624042E28A0B58960A8A4A4111DDE530EB94FD0055C279F79A8E6B46C5EF5B58`;
- bound perturbation compare: `A4CC7E9F8B8EC0DC5F9E0D1C53D5C3CCFB13BE4F9DDD38AF3C0063C08861E0D1`;
- categorical perturbation compare: `4B92D29308C6E6454C4BC523ADA62F79CC38002AF73EBF656108FF83ED5D79D2`.

## Call ledger and numerical disposition

Historical D2 MATLAB calls:

1. input-container blocker: `1`;
2. zero-field output-container blocker: `1`;
3. schema/comparator authority tasks: scientific calls `0`;
4. current replacement D2 MATLAB: `0`.

Current scientific calls:

- D2 MATLAB/Python/comparison: `0/0/0`;
- D3 MATLAB/Python/comparison: `0/0/0`.

Therefore nine-case normal maximum differences/worst cases, near-tie scientific comparison, D2 KKT/boundary mismatch counts, and all D3 360-case statistics are `NOT_REACHED_COMPARATOR_PREFLIGHT_FAILED`.

Scientific mismatch list: empty. No scientific stage ran.

Source/environment failure list contains one entry:

| Stage | Failure | Interpretation |
|---|---|---|
| comparator engineering preflight | categorical mismatch is recorded in `categorical_stats` but does not affect `failures` or exit; preflight assertion expected exit 2 and failed | preflight/source-contract mismatch; replacement D2 prohibited |

## Forbidden-operation check

- D1 rerun: no;
- failed preflight repaired/rerun: no;
- replacement D2 or D3 entered: no;
- D2/D3 science/cases/order/equations/parameters/roots/KKT/multipliers/tolerances changed: no;
- comparator additions beyond `gap/bound`: no;
- 17-field/union schema or fabricated fields: no;
- production sources/tests/helpers/cache modified: no;
- taper, bare-`a` oracle, `Tt/rb_gap`, hard-coded Python outputs: no;
- full HJB/KFE/steady state, P3/P4/R4, asset-tail, AR(1), transition, IRF, dynamics, calibration extension, Results: `0`;
- P5 revoked/reissued: no.

## Git status, acceptance, and next gate

At report freeze, this report is the sole repository change; `src/tests` remain unchanged and there are no unrelated paths. Final remote identity and clean status require post-publication verification.

Acceptance level: static heterogeneous schema and MATLAB serialization plumbing are qualified; comparator `gap/bound` numerical behavior is qualified; the complete mandatory comparator preflight did not pass, so D2/D3 remain unentered. D1 and P5 remain accepted; the dynamic hold continues.

Exact recommended next gate: publish only a comparator categorical-terminal-semantics/preflight correction task. It must decide whether existing categorical mismatch statistics are intentionally non-terminal or must populate `failures`; then authorize a corrected one-shot comparator preflight and, only after it passes, reauthorize the same frozen D2/D3 resumption. D1 must remain reuse-only.
