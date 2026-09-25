# K1B turn8 R2 runner preparation — zero science

Task: `CH5_K1B_TURN8_R2_RUNNER_PREPARATION_ZERO_SCIENCE_20260925`.

Candidate classification: `K1B_TURN8_R2_RUNNER_CANDIDATE_READY__ZERO_SCIENCE__WORK_REVIEW_PENDING`.

The new runner prepares a separately authorized, one-shot C7→C8 bounded comparison. Its default command performs only read-only static preflight. The future `--execute` branch requires a distinct byte-identical committed active task, exact future task and execution IDs, approved disjoint output root, and unchanged committed runner before model import or output creation. This preparation made **zero** scientific/model calls and did not create a turn8 output root.

## Frozen input and prior failure

- Dispatch HEAD: `e4cd465a3827e2b06a4e7ec5435f651a23673c26`, descendant of accepted turn7 execution `586b066e9add81fba6f2c86ed3fdd0092a3dbeea` and Owner adoption `2d43179bc9e9348efe8f61c19217ee10be6bd5d3`. `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`.
- Accepted C7 entering-turn8 JSON SHA-256 `30EDAECEA59ABA03EFFD6C11530617BB7CF80FED175F58437F4DACA9E96D2F3A`; NPZ `E6B5D428C1070C6F9F6D9C450F7CDB0D4C2C54F0658074C9C75E60E8FDB743DB`; entering manifest `20861D4ADDBDF1099854EB86B00D24A097C627838B3F6EF5AFAEDABFFD647E5E`; full C7 output manifest `413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91`.
- The pinned C6→C7 comparison receipt SHA-256 is `6DE97F35A8D599183F19F920A95B61CC01CE21B3E6E1AFAB19935FC44623835E`, and its terminal receipt SHA-256 is `E4753713354D54B49716574A29424D4F709A427851DE7F1CC9B7CDAA8D31D3FB`. It was a legal `VALID__NINE_COMPONENT_LEVEL_NOT_MET` with only 2/9 components strictly below `1e-6`. R2 is unattainable on the named C6→C7/C7→C8 pair. A future legal C7→C8 miss maps to `VALID__LEVEL_NOT_MET_AT_BUDGET`; a lone second pass maps to `VALID__ONE_PASS_UNCONFIRMED_AT_BUDGET`.
- The protected C6-prime repeat output manifest stayed at SHA-256 `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61` and is never an input.

## Candidate controls and checks

The static preflight hashes and reads back all 5,141 artifacts in the accepted C7 full manifest, rejects missing/extra or reparse paths, verifies the entering-turn8 seal, terminal and prior comparison, and binds C7 province order, destination-by-origin `S`, share columns, JSON/NPZ bit identities, lagged raw return and `rah`. It binds frozen source, helper, runner, distance, Owner adoption and budget proposal identities. The runner subtracts the accepted turn7 attempted ledger from every adopted two-turn ceiling before reserving turn8. It enforces the adopted per-province and per-turn ceilings, counts failed entries, permits one turn8 household batch and one integration only after 31/31 household PASS, and fixes turn9 household calls at zero.

After a future legal turn8, the runner would seal/read back entering-turn9 material, compare C7→C8 under all nine adopted formulas and strict `<1e-6` tests, and report clipped `ra` hits separately from the original MATLAB zero-hit predicate. It cannot issue a two-pass criterion terminal for this accepted prior miss. Output writes are exclusive and root-bound; reused `mkdir`/`unlink` mutations are guarded for ownership and reparse components. Root loss carries the earliest terminal and available ledgers. Filesystem check-to-operation rename races remain non-atomic.

- Focused inert/static tests: `21 passed, 1 skipped` (directory symlink capability unavailable); model evaluation, HJB/KFE, firm, integration and turn8 household calls `0`.
- Default runner: `PASS__STATIC_PREFLIGHT_ONLY`, `scientific_calls=0`, prior C6→C7 terminal bound, and planned output absent.
- Runner SHA-256: `10920535BD50E688D1794B7E69C34F8A5C3C56456CAF6E8DF52FA8D9DFE31831`; focused test SHA-256: `A97D0D8714F6C8B4E9EAECD74271E034A3762234C3F1B7F4C7B2DCB3DAC8EA69`.
- Task-scoped scientific/model ledger: turn8 household `0`, HJB `0`, terminal KFE `0`, integration `0`, firm `0`, K1B feedback `0`, turn9 household `0`, K2 `0`, GE `0`, MATLAB `0`, Results `0`, retries `0`.

The companion machine receipt records the changed paths and report hash. Its own hash and the local candidate commit are reported after commit to avoid a self-referential digest. Independent GPT Work ACCEPT/REJECT is the next gate; no turn8 execution is authorized by this candidate. Results eligibility remains `FALSE`.
