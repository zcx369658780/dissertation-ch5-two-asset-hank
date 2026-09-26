# Independent GPT Work review — C9 new static runner Repair1

Reviewer: GPT Work
Verdict: **REJECT__SEALED_INPUT_PATH_GAP_AND_EVIDENCE_AMBIGUITY__NO_SCIENCE**

Candidate `0e71c8edfed120c5f117f2e16815748b280fa3a5` (parent `e738c5b1f76b28e1319955eadbf2c4baaadc8420`, tree `ba47f7715710edb4ae7066bfaf19ee4d1b4c2e61`) adds exactly the five Repair1-authorized paths. Wrapper, delegate, test, report and receipt raw SHA-256 values are `D4F2A1BACA2838217950CC7468A5B27509B558A3BD3A6865A9ECB7B0E9E9CB01`, `44080FE05EEAD299F34DBD1FAB33EDCB3A0E77B04459402169F5ADD24EEBC84A`, `4D1FB993E00C04582865B74A9FFFF0EEDD7DEDAA58D5BEE3E47DD286D4B8DBE6`, `EB75C82E84A0BCDCEA0B46501BE53B5442AA890C4B98B13E9BB789ABB0150B1F`, and `47540885CF338CC315DE4CC0519E81D8A03D6A1D8971778C49BC6487BDBC5901`. `git diff HEAD^ HEAD --check` passed; tracked files were clean; `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`.

Repair1 added five protected manifest checks and reparse-aware path walking to the wrapper and delegate. The new test source contains no wrapper `--execute` invocation, and its targeted read-only run reports `10 passed`. The prior two prohibited probes remain explicitly recorded as the original rejected task's history, not as authorized calls. These facts support a **zero-science Repair1**, not an active C9 runner.

The candidate is still rejected for two concrete reasons:

1. Future identity checks hash/read the old C9 `timing_failure.json` and several sealed C8 input leaf files without first proving each complete path is a regular file free of symlink/Windows reparse components. A protected manifest hash alone does not protect those separate leaf paths. The wrapper's static and future gates both have this gap; the delegate's old-failure receipt read also lacks the complete-path check. The future execution path must fail closed before delegate/model loading and root claim on any substituted sealed input.
2. The receipt's `task_id` is Repair1, but its `this_task_counts` and `test_runs` still describe the original task's two `--execute` probes and three seven-pass runs, while separate Repair1 fields claim zero probes and one ten-pass run. The historical violation is correctly retained, yet the mixed fields make the current task counters ambiguous. Tests simulate failure for only the first of five protected manifests, and do not exercise an unsafe output-root parent component. The report overstates that coverage.

The five protected C6-prime/C7/C8/C8-timing/C9-partial manifest SHA-256 values remain `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`, `413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`, `5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`, `5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D`, and `80BD0D42CB73B4E39B811E759505480542D5A73227014F30B732C34A8AC1FDC3`. The new output root and live contract/adoption/execution task are absent. Actual old calls remain `CALL_LEDGER_UNRESOLVED`; full-old-turn charge remains governance accounting only.

Repair1 is not accepted as an execution identity chain. A separate scoped, zero-science Repair2 may correct the exact path and evidence gaps without repeating any `--execute` probe. C9/C10, retries, partial resume, convergence and Results remain closed; Results eligibility is `FALSE`.
