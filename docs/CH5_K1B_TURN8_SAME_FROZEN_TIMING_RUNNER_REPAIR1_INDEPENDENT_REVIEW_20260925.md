# Independent GPT Work review — C8 same-frozen timing wrapper Repair1

Reviewer: GPT Work
Verdict: ACCEPT__C8_SAME_FROZEN_TIMING_WRAPPER
Wrapper path: `validators/multi_province/k1b_turn8_same_frozen_timing_measurement/run.py`
Wrapper SHA-256: `8DFA49C1121EF41FA750844F4F5017779C3E381CFA2E7CBE19C7834D1F0EAB4A`

Candidate `68a00e72fbee13d88ec35db4d47679823d10ab2e`; parent `076f5202e1c49d849a5c0da6bab93b4e6235891a`; tree `767324a945e0b02cfa4d30a79d396490943d8897`. Exactly the four Repair1 allowlisted paths changed. The frozen `HEAD:src` tree is `00682b2e1a7ba23665f6e16f6acf48ad35874883`; tracked files are clean. The only untracked roots are the protected C6-prime, C7 and C8 outputs. Their execution manifest SHA-256 values respectively remain `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`, `413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`, and `5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301`. The separate measurement output root is absent.

Independent readback matched every source, protected-manifest and candidate-artifact SHA-256 in `EVIDENCE/ch5_k1b_turn8_same_frozen_timing_runner_repair1_20260925/repair_receipt.json`; JSON parsed and `git diff HEAD^ HEAD --check` passed. The Builder used one of two authorized static test invocations, reporting `14 passed`, zero failed or skipped. Work did not rerun that test or make a scientific/model call.

The new future gate requires the committed wrapper digest to match this separately committed GPT Work ACCEPT review, the future current task and its committed copy, Owner adoption, and structured measurement contract. Missing or stale identities refuse before output creation. The accepted C8 delegate hash gate remains unchanged. The wrapper no longer overrides `c8.turn8_terminal`; the accepted delegate writes its original numerical terminal to its sealed science output and returns the same value, which the wrapper records as `source_terminal`. `COMPLETE_OBSERVED_ELAPSED_SAMPLE_ONLY` remains a separate timing classification. The inert test exercises preservation of the original terminal.

This accepts **wrapper code only**. It does not adopt a measurement budget or resource wall cap, authorize `--execute` or any scientific call, establish a C9/C10 duration upper bound, or change C9/C10 prelaunch blocking. The separately budgeted C8 observation remains a proposal. Task-scoped model/scientific/failed/retry ledger is zero. Results eligibility remains `FALSE`.
