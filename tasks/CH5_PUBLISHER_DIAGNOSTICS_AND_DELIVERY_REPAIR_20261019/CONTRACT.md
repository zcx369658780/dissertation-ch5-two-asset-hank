# CH5 publisher repair: security-reviewed release

TASK_ID=CH5_PUBLISHER_DIAGNOSTICS_AND_DELIVERY_REPAIR_20261019
REVISION=SECURITY_REVIEWED_20261019
SCOPE=BOUNDED_PUBLISHER_REPAIR_AND_OWN_EVIDENCE_DELIVERY

## 1. Authority and immutable history
Owner authorized security review followed by task issuance. This contract does not override any platform approval, authentication, repository permission or safety decision. A platform denial stops that operation; no alternate tool, account, encoding or branch may be used to route around it.

The earlier unactivated draft commit 3d76281c4f0fabd1906bee60176f1e9224358940 and blocked release tree remain historical, not executable authorization. This release materially restricts command execution, log access and publication. It does not claim the platform disclosed its blocking reason. Prior failed tasks and missing stderr remain unchanged; a new reproduction is not historical evidence.

Task authorization requires CURRENT.md and TASK_CURRENT.md at the same live governance snapshot to name this task and revision. Read docs/DOC_INDEX_CURRENT.md, not a root-level index. Read this contract and TASK_PARAMETERS.json at the issue commit in ISSUE_MANIFEST.json; read that manifest from the later release snapshot in the launch prompt. The baseline/review parent is historical, not the required live HEAD. TASK_PARAMETERS is part of the contract; load constants from it, not from manually copied hashes.

## 2. One engineering objective
Implement src/ch5_evidence_publisher.py and tests/test_publisher.py using installed Python standard library and Git. No package installation, model code, old archive, old classifier or pre-existing publisher is a prerequisite. Only the two already public historical documents in TASK_PARAMETERS may be read as content inputs. New fixtures are synthetic, locally generated, inert and identified as such.

Build a task-specific publisher, not a general command runner. Expose selftest, package, publish and readback operations only. Reject arbitrary executable names, arbitrary shell strings, arbitrary repository URLs and destination branches. Use shell=False and tokenized argv. Executables are the resolved installed Python and Git; Git may use the existing SSH client solely for the fixed repository. Python children run only newly created test helpers under this scratch. No operating-system process enumeration, administrator rights or control of unrelated processes. Record installed executable identities once; do not modify the installations.

Git operations are restricted to the allowed families in TASK_PARAMETERS, with path/ref validation per operation. Local mutable Git stores must be newly created bare repositories beneath scratch/git. Production mutation is one new allowlisted review ref containing exactly three added files. Never modify main, governance, other review refs, old worktrees, configuration outside scratch, credential stores or repository history.

## 3. Filesystem and bootstrap
TASK_PARAMETERS freezes the new scratch, its parent and a finite protected-root list. Before any file write, verify relevant canonical paths, directory/file identities and parent-chain link/reparse properties. Do not recursively scan old evidence or dependencies. The trusted parent may contain the new child; this expected containment is not protected-root overlap. The new child must not overlap a protected root and must be absent before exclusive creation.

Formal worktree and existing evidence roots are metadata-only. Exactly the listed read-only Git metadata commands may resolve actual git-dir/common-dir/index with GIT_OPTIONAL_LOCKS=0; .git locator and index hashing are allowed only for before/after identity. No backup is designated; other backups are not asserted absent and remain outside read/write scope. Optional missing historical mirror is ABSENT, not a reason to invent a replacement. Unknown actual write routing or required Git identity is a hard stop.

BOOTSTRAP 0 is read-only. BOOTSTRAP 1 exclusively creates the exact target and immediately rechecks parent/child identity. BOOTSTRAP 2 writes the initial receipt and task files. All writes, local Git stores, new helpers and logs stay under this scratch. Failed attempts remain in separate attempt directories; never replace a failed attempt or reuse another task's directory. Temporary review paths exist only in Git trees, never as a checkout in a protected worktree.

## 4. Private diagnostic retention and public publication boundary
Before each allowed child starts, reserve the launch and open private binary stdout/stderr destinations under raw_private. Preserve bounded raw output before decoding or redacting. Drain both streams without deadlock. Record operation family, exact private argv/cwd, executable identity, exit/timeout, timestamps, raw byte counts and SHA256. Do not read/dump environments, SSH keys, browser data or credential files. Existing authentication is used by Git/SSH, never copied into logs or artifacts.

Public diagnostics are separate derivatives. Remove only private spans and keep intelligible command family/error context; do not overwrite the sole raw record with a whole-message privacy placeholder. Raw hashes are identities, not proof that a file is safe to publish. No raw_private file is directly included in the public package, even when synthetic. Generated retention proofs provide raw/public hashes and use an explicitly synthetic known fixture to demonstrate correctness. Secret-like unexpected real content is quarantined locally and blocks its publication. Control characters are represented safely in public output.

Observe numeric stream limits. If capture exceeds a limit, stop the child safely, preserve captured bytes and mark INCOMPLETE_OUTPUT_LIMIT; never describe a truncated stream as the complete original. Own-child timeout cleanup uses the handle obtained from that launch, never an unrelated PID or broad process-name kill. Loss of ownership or inability to reap is a hard stop.

## 5. Qualification and bounded E1 repair
Implement and retain results for 12 test groups:
T01 nonzero exit with original stderr retained and a readable redacted derivative;
T02 binary/non-UTF8/control-character output without raw corruption;
T03 exit zero with nonempty stderr is not automatically a failure;
T04 tokenized spaces, Unicode and quotes in inert arguments;
T05 bounded simultaneous stdout/stderr beyond a normal pipe buffer;
T06 own harmless child timeout, partial output preservation and confirmed reap;
T07 simulated log-write failure prohibits further publication;
T08 synthetic path/credential-shaped fixture redaction with unchanged private raw hash;
T09 invalid config, unsafe destination, lease replay and changed payload rejected;
T10 complete local fake-bare round trip including binary ZIP, sole parent, exact file bytes and member hashes;
T11 fake-remote deletion removes only three test files, preserving a sentinel and history;
T12 implementation lock, approved profile binding, stage accounting and resource-limit checks.

Expected negative test results are not task incidents. Unexpected syntax/argv/local configuration/assertion errors are E1 only when evidence survives and no permission, privacy, source or resource boundary is crossed. Preserve the first attempt and repair within the six engineering batches; do not request a new task per typo. Platform denials, credential/permission failures, true input mismatch or real protection/resource breaches are not E1.

Fake-bare uses its own small synthetic parent, does not access GitHub and does not require the production parent. Freeze final publisher/test source hashes before the final passing qualification. Freeze TWO explicit configuration profiles (local test and fixed GitHub delivery) in one publisher_lock.json. They intentionally differ in parent/destination; approve only those differences. The same implementation digest and operation-validation rules apply to both. Mutation of implementation or either profile requires requalification within remaining budget. No hidden production-only code path.

## 6. Resources and STOP
All budgets are in TASK_PARAMETERS. Governance intake GETs are allowed and counted; tests are offline; the separate DELIVERY phase has explicit network permission. Reserve controlled launches before creation. Distinguish direct starts, observed helpers, kernel observations and unavailable independent evidence; do not double count and do not turn UNKNOWN into zero. Application accounting is not a claim of arbitrary-descendant OS prevention. An unaccounted current child or inability to bound the current task stops it; historical independent-kernel UNKNOWN alone does not trigger new tests.

After a hard stop only safe local log flush, release of owned resources, final receipt and the reserved read-only remote reconciliation are allowed; no further tests or backend writes. If read-only reconciliation is itself denied or unsafe, keep UNKNOWN. Authentication errors and platform denials do not authorize alternative transports. Phase deadlines include a finalization reserve; record shorter child timeouts separately.

## 7. Mandatory own-evidence delivery
After all test groups and final fake-bare qualification pass, Codex MUST use the locked publisher to upload its own reviewed evidence to the exact branch/path in TASK_PARAMETERS. Use only existing SSH authentication to ssh.github.com:443 with normal host verification; do not inspect private keys, change SSH security settings or add credentials. Fetch only the fixed parent and necessary objects into the exclusive scratch bare store. No broad clone, worktree, shared object storage, alternates or force push.

The new package contains actual final publisher/test code, fixtures, per-test results, source/profile lock, readable public diagnostics, raw/public retention proofs, fake-bare byte-readback and cleanup proof, first errors/repairs, protection/resource summaries and a prepublication receipt. The public payload is explicitly enumerated under sanitized; do not glob or recursively package the scratch. Reject raw_private/input credential stores, unknown binaries, traversal, symlinks, duplicate/case-colliding names, nested archives or unresolved sensitive content. Raw fixture bytes remain private; their safe generated evidence is supplied separately. All earlier 491 archive members, model code and old classifier/adapter code remain excluded.

Publish exactly result.md, manifest.json and evidence_sanitized.zip. Manifest hashes payloads and ZIP members, not its own final hash. Postpublication commit/tree and manifest hash go in an external receipt to avoid self-reference. Actual publisher code must be readable in the evidence ZIP, not represented only by a digest.

Use a normal non-force push to create the single fixed review branch; sole parent is the fixed parent and diff is exactly three additions. After any ambiguous push, halt writes and use the reserved GETs to reconcile. Exact expected candidate found means no second push. A conflicting ref or unresolved result stops. A second ordinary push of the SAME immutable candidate is allowed only after confirmed ref absence, confirmed own-process reap, a recoverable non-authentication failure and remaining budget. At most one successful publication. Independently read ref/commit/tree/parent and all three raw files; recompute ZIP CRC, size and every member SHA256. A URL or Blob ID alone is not completion.

## 8. Receipt, review and cleanup
Return DELIVERY_FINAL_RECEIPT original bytes as complete Base64 with byte length and SHA256, plus a separate external controller-completion event after exit. Missing observations remain UNKNOWN; planned stop and actual phase are separate fields. No background polling or automatic successor. Failure to qualify means DELIVERY_BLOCKED with a safe terminal receipt, not an untested fallback publisher.

Astra reads actual remote bytes/code/tests, permanently archives the terminal review and reads it back, THEN MUST delete exactly the three temporary files from the specified review branch current tree in one non-force cleanup commit and verify absence. Check review HEAD before changing it. Keep files while review is pending. Cleanup failure is TEMP_CLEANUP_PENDING; no candidate is NOT_APPLICABLE_NO_CANDIDATE, not cleanup success. Git history is not erased.

Stop: WAIT_ASTRA_PUBLISHER_DIAGNOSTICS_REPAIR_REVIEW.
Science/model/old archive/old classifier rerun budgets are zero. Formal V010 and HA black box unchanged; model_activation=False; REAL_GE=False; Results=FALSE; V011=NOT_STARTED; FULL_RUNNER_IO_CLOSURE=BLOCKED.
