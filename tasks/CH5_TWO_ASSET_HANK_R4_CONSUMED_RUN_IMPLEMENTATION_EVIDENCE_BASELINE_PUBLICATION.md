# CH5_TWO_ASSET_HANK_R4_CONSUMED_RUN_IMPLEMENTATION_EVIDENCE_BASELINE_PUBLICATION

## Task

Publish the exact local implementation/evidence snapshot that produced the already-consumed R4 frozen steady-state failure, so that the consumed run becomes reconstructible from GitHub.

This is a provenance-baseline publication gate, not a scientific acceptance, repair, rerun, or parity gate.

## Owner authorization

The Owner explicitly authorized:

`同意按上述 27 个文件建立 R4 consumed-run implementation/evidence GitHub baseline。`

This task is the sole execution authority for that bounded publication.

## Repository

`zcx369658780/dissertation-ch5-two-asset-hank`

## Required live authority read-back

Before any mutation, fresh-fetch live GitHub `main` and read:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_R4_EXECUTION_EVIDENCE_AND_LOCAL_IMPLEMENTATION_AUTHORITY_RECONCILIATION.md`
- this task file

Confirm that this task exists on live `main` before proceeding.

## Scientific classification of this publication

The publication freezes the exact implementation/evidence identity of the consumed R4 run.

It MUST NOT be described as:

- accepted Python implementation;
- R4 steady-state acceptance;
- proof of economic correctness;
- MATLAB-Python parity;
- Results evidence.

The correct meaning is:

`PROVENANCE_BASELINE_ONLY__CONSUMED_RUN_IMPLEMENTATION_AND_EVIDENCE_GITHUB_BOUND`

## Source checkout safety

The existing local checkout containing the 27 source/evidence files is a stale checkout and MUST remain unchanged except for read-only inspection.

Do not pull, merge, rebase, reset, checkout, clean, stash, stage, commit, or push from that stale source checkout.

Determine and report its exact repository root as `SOURCE_ROOT`.

## Isolated publication workspace

Create a new isolated publication workspace from the freshly fetched `origin/main` state.

Allowed methods:

- a fresh clone; or
- a new isolated Git worktree/branch rooted exactly at fresh `origin/main`.

The isolated workspace MUST NOT reuse the stale source checkout as the commit workspace.

Record:

- source checkout root;
- isolated publication root;
- fresh `origin/main` commit before publication;
- publication branch/ref;
- `git status --short --untracked-files=all` before copying.

In the isolated workspace set local Git content-conversion behavior so staged blobs preserve the copied file bytes. In particular, disable automatic line-ending conversion for this workspace before staging, and verify staged blob content against the frozen SHA-256 identities below.

## Exact publication set

Exactly the following 27 pre-existing local files are authorized for snapshot publication.

No other pre-existing local untracked file is authorized.

### Package/config: 1

1. `pyproject.toml`
   - SHA-256: `31F165D792275A24A940EA39CF12C3BDC6344AC6E96254C8012E3D0AE9B436CE`
   - bytes: `285`

### Python implementation: 14

2. `src/ch5_two_asset_hank/__init__.py`
   - SHA-256: `AADD3691D97F3EB5D0401ABEB8DC11F5DA7F6D4BA33B31BC103EC2BB92715D9B`
   - bytes: `579`
3. `src/ch5_two_asset_hank/boundaries.py`
   - SHA-256: `42C683A8346CB27C2218946D4A5A0BD8C7CF0DE5E56E8BA9839D1F0297E9EB1F`
   - bytes: `6333`
4. `src/ch5_two_asset_hank/contracts.py`
   - SHA-256: `3EFB0FC4975A800F308CE9E019E43E3ECBC0C214FF12F22A0EE2DA25C6EC809C`
   - bytes: `5016`
5. `src/ch5_two_asset_hank/derivatives.py`
   - SHA-256: `53F338D2D697A15B33EDA2F04CB526CC94DC0FDC92C9E60E74A709B604098CFB`
   - bytes: `1358`
6. `src/ch5_two_asset_hank/diagnostics.py`
   - SHA-256: `9BB59526E1EF080D10655B2387330583B15CD9609F7B4E34FEE5D476C301D582`
   - bytes: `1462`
7. `src/ch5_two_asset_hank/economics.py`
   - SHA-256: `8C8B158ECCFC5A68C2CFC4335F8AD9AA3231F8394EFE1F10D40955470999315C`
   - bytes: `2519`
8. `src/ch5_two_asset_hank/generator.py`
   - SHA-256: `761F493FF64FDE68B151DCCB6A79CCBC3BBC28CA681BBDD13E9F8AEF40E33478`
   - bytes: `2317`
9. `src/ch5_two_asset_hank/hjb.py`
   - SHA-256: `39FC6F54964A311B1B41923743FB2450932A27B5CFF73C878A869F6B5DCE6AC6`
   - bytes: `3806`
10. `src/ch5_two_asset_hank/indexing.py`
    - SHA-256: `47F74CFB07942B702CE9BDA19B66FAB9C71BFC43EE95F5DB09BFBACF98ECA179`
    - bytes: `1551`
11. `src/ch5_two_asset_hank/kfe.py`
    - SHA-256: `D8385D03F29A97FC1FD16EF27D7EE2330D15AC5F4AA286A881D0941275EA3B28`
    - bytes: `5711`
12. `src/ch5_two_asset_hank/kfe_contract.py`
    - SHA-256: `F1C4F8D60567D6620E1F5DE65AF43949875AC780A2B562A07F4820D5056A3972`
    - bytes: `1565`
13. `src/ch5_two_asset_hank/policies.py`
    - SHA-256: `AE458B1EA81CB6D60F44AC5EAFC8BA5DD2128CEF912A09029F7493539C2BE271`
    - bytes: `27218`
14. `src/ch5_two_asset_hank/productivity.py`
    - SHA-256: `DE7428B74B83F74D9F8CBB6E5E5BC04F1A442A36E738B4D6D242FA79031DE720`
    - bytes: `3479`
15. `src/ch5_two_asset_hank/steady_state.py`
    - SHA-256: `8671A406CBC1563A8BE57726B97D9F6A9497C515D39651E340D1626DB3BFF29F`
    - bytes: `9821`

### Tests: 8

16. `tests/test_economics_boundaries.py`
    - SHA-256: `61A57070C4D27F59174DCF1BD3F39AF050B311E9AFFC8BED27B277E511FC9566`
    - bytes: `1786`
17. `tests/test_generators_and_kfe_contract.py`
    - SHA-256: `18AFC0796E28C9A04BFD1F95DD77D568314C01C401268EDD04A260AB137E62F6`
    - bytes: `3063`
18. `tests/test_hjb_diagnostics.py`
    - SHA-256: `F9E22CEB801A7A09EB7CB5304986E6E9AA6885A351B5C92B56F6693C4355617F`
    - bytes: `1361`
19. `tests/test_indexing_and_derivatives.py`
    - SHA-256: `46C68511357C78CF81A7A135604AEEC5480B9BC73BBA3582AB87FDDE27B75822`
    - bytes: `1414`
20. `tests/test_kfe_operator.py`
    - SHA-256: `18EE94C6EC7DBB2178845B642D0257DD8EC06E4BC9C4914531B52A52B4994EAD`
    - bytes: `4422`
21. `tests/test_r2_rerun_evidence.py`
    - SHA-256: `265B45E9B931406BCEB2B6AFEFFBC484E201B697E6A92ABE4BB732EC3CD28851`
    - bytes: `4613`
22. `tests/test_r4_policy_fixture_resolution.py`
    - SHA-256: `2E9F72BB4783F6110BF1F606D9DEE975EBE0D332326BCF1E6886FBB1DEED2D40`
    - bytes: `14267`
23. `tests/test_r4_steady_state.py`
    - SHA-256: `8017B0321026C14E3E79E08D835C94F0CF5F779F43F1FC6FC6C19ECFF785859B`
    - bytes: `1597`

### Existing R4 evidence reports: 4

24. `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION_RERUN_AFTER_LATEST_SLACK_LOWER_B_08125_REPORT.md`
    - SHA-256: `91F645C55278E97EB21D684F94BED7B5D236BE115244DA997CFE8DFDB1DAF3D3`
    - bytes: `5659`
25. `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_AUTHORIZATION_REPORT.md`
    - SHA-256: `61695E80A9B225CBADD3ABDA2A994D4A5DC5D11FFADF0E9DC6729AFB8F1F83E6`
    - bytes: `9318`
26. `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION_RERUN_AFTER_UPPER_A_LOWER_B_REPORT.md`
    - SHA-256: `9F57C71BB59BA2BF1B5C065D9F568D2B5A1C226D4BBA9E4651E1385C2C223F60`
    - bytes: `5443`
27. `docs/CH5_TWO_ASSET_HANK_R4_UPPER_A_LOWER_B_POLICY_SELECTION_FAILURE_LATEST_RESOLUTION_08125_REPORT.md`
    - SHA-256: `7F0DA80DEE30291FEA7A840951BFEDD2CF4601976E33DABEEBA7AC8061F68015`
    - bytes: `7401`

## Pre-copy identity gate

For every one of the 27 authorized files, before copying:

- confirm the source file exists under `SOURCE_ROOT`;
- confirm exact byte count;
- confirm exact SHA-256;
- confirm it is not a symlink/reparse indirection to an unexpected external target;
- confirm no path is outside `SOURCE_ROOT`.

If any one identity differs, stop with:

`BLOCKED_R4_BASELINE_SOURCE_IDENTITY_MISMATCH`

Do not update the expected identity and do not substitute another file.

## Copy rule

Copy only the 27 authorized files into the isolated publication workspace, preserving their exact repository-relative paths and file bytes.

Do not edit, format, normalize, regenerate, or otherwise transform contents.

Do not copy any other untracked file.

## Post-copy and staged-blob identity gate

Before staging:

- recompute SHA-256 and byte count for all 27 copied files and compare with the frozen identities.

Stage files only by explicit path. Forbidden:

- `git add .`
- `git add -A`
- wildcard staging that could include unrelated files.

After staging, verify:

- exactly 27 staged paths;
- staged path set exactly equals the authorized publication set;
- no staged deletion or modification of pre-existing GitHub files;
- the staged blob content for each of the 27 files, when materialized from the index, has the same SHA-256 as the frozen source identity.

Any mismatch must stop before commit.

## Test/run prohibition

Do not execute:

- Python;
- pytest;
- static compilation;
- frozen fixture;
- steady-state runner;
- HJB solver;
- generator/KFE solver;
- MATLAB;
- any scientific diagnostic.

This gate publishes identity only.

## Commit authorization

If and only if all identity gates pass, create exactly one commit containing the 27 authorized files and no other changed path.

Suggested commit message:

`Bind consumed R4 implementation and evidence baseline`

Before commit report the exact staged path list.

## Push authorization

Push is authorized only for this exact commit and only as a fast-forward publication onto live `main`.

Immediately before push:

- fresh-fetch remote state;
- confirm live `origin/main` still equals the publication workspace base commit;
- confirm the commit has exactly one parent equal to that base;
- confirm diff from base to publication commit contains exactly the 27 authorized added files.

If remote `main` moved, stop with:

`BLOCKED_REMOTE_MAIN_MOVED_BEFORE_BASELINE_PUBLICATION`

Do not merge, rebase, force-push, or republish automatically.

Force push is forbidden.

## Post-push verification

After push, fresh-fetch/read back GitHub and report:

- new live `origin/main` commit;
- parent/base commit;
- exact 27 changed paths;
- for all 27 GitHub files, Git blob/file existence;
- GitHub-side byte/content SHA-256 identity where safely verifiable;
- final source checkout status unchanged;
- final isolated publication workspace status.

Do not perform any follow-on scientific work in this task.

## Forbidden operations

Do not:

- modify any of the 27 file contents;
- include any of the other local untracked files;
- change fixture/config/parameters/tolerances;
- modify economic equations or policy contracts;
- diagnose the 25-vs-29 candidate mismatch;
- rerun any model/test;
- create artificial transitions;
- select recurrent classes;
- create invariant mixtures;
- implement transition solver;
- implement AR(1);
- run IRFs;
- modify MATLAB;
- claim MATLAB-Python parity;
- write Results prose;
- mutate the stale source checkout;
- merge/rebase/reset/force-push.

## Acceptance criteria

PASS requires all of:

- all 27 source identities match the frozen SHA-256 and byte counts;
- exactly 27 authorized files copied byte-for-byte;
- exactly 27 authorized paths staged;
- staged blobs preserve the frozen content identities;
- exactly one bounded commit created;
- diff contains exactly 27 added files and no other path;
- fast-forward push to live `main` succeeds;
- GitHub read-back confirms the publication.

Expected PASS classification:

`R4_CONSUMED_RUN_IMPLEMENTATION_EVIDENCE_BASELINE_GITHUB_BOUND`

Acceptance meaning:

`PROVENANCE_BASELINE_ONLY__NOT_SCIENTIFIC_ACCEPTANCE`

## Final response requirements

Report:

- verdict;
- files read;
- `SOURCE_ROOT`;
- isolated publication root;
- base `origin/main`;
- pre-copy 27-file identity check;
- post-copy 27-file identity check;
- exact staged file list;
- staged-blob identity check;
- commit hash;
- parent/base hash;
- pushed live `main` hash;
- GitHub read-back result;
- forbidden-operation check;
- source checkout git status;
- isolated workspace git status;
- acceptance level;
- recommended next gate.

## Recommended next gate

Only after independent GitHub L3 verification of this baseline publication:

`CH5_TWO_ASSET_HANK_R4_COMMON_CORE_CANDIDATE_IDENTITY_DIAGNOSTIC`

That future gate should be read-only/scientific-diagnostic first and must not automatically repair or rerun the consumed fixture.
