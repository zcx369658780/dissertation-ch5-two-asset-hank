# MP4B Owner-reauthorized instrumented MATLAB corrected-2009 one-shot

## Terminal verdict

`MP4B_OWNER_REAUTHORIZED_INSTRUMENTED_MATLAB_CORRECTED2009_ONE_SHOT_BLOCKED_NO_RERUN`

The one permitted MATLAB launcher entered the corrected-2009 stationary route and
then failed in the copied observability helper on the first outer turn, before the
first `HANK_2ASSETS_HJB` call.  The error was
`MATLAB:invalidConversion` / `无法从 struct 转换为 double。` at
`MP4B_OBS` line 19 while assigning `household_inputs(i)`.  The preserved stack
reaches `HANK_mp_1turn`, `HANK_mp_1eq`, and `mpHANK_equilibrium_2000`, but the
failing observer call precedes the household/HJB call.  This task has no
repair-and-rerun lane; no repair, second launcher, baseline interpretation, or
MATLAB/Python chronology adjudication was performed.

The exact Owner reauthorization consumed by this one-shot was:

> 同意重新授权一次 instrumented MATLAB corrected-2009 stationary one-shot，使用已冻结的 path-normalized candidate wrapper，仅增加 observability；禁止修改方程、参数、网格、算法、controller、容差与更新顺序；MATLAB stationary=1，rerun=0。

## Live continuity and pre-science authority

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Branch: `codex/ch5-adjustment-boundary-redesign`.
- Fresh-fetched task authority / initial `HEAD` / initial `origin/main`:
  `535044b4030df6c25cf83092538f54496b8bd680`.
- Required direct parent: `b2d6a1ed6c230f2c2be1ca3acf08109753defe57`, verified as
  the sole parent.
- Pre-launch worktree was clean and ahead/behind was `0/0`.
- Read in full before creating the copy root: `AGENTS.md`, the current rule
  index, GitHub capability/authority routing, local-file safety, MATLAB model
  diagnostic gates, the zero-science copy-binding remediation task/report, the
  blocked instrumented-run task/report, and the accepted final-state,
  representation, and controller-localization evidence reports.

All 12 protected repository identities, the comparator-helper Git blob
`cbe7ce4e4855c139cc7bb3b20b56d124c4add266`, the seven protected MATLAB
identities, canonical 2009 input, preserved baseline, predecessor observability
artifacts, remediation matrix/diff/wrapper, and frozen invocation body were
verified before launch.  The repository identities matched the exact hashes
listed in the live task, including source semantics map
`6A4FD157...59995C028`, source-postloop adapter `8A630887...FB2DFF06`,
validation driver `90332187...D336091E`, comparator contract
`E74E5BF8...6C3C3A`, final-state map `A1D0F04D...6024CB`, and helper
`0FD6889E...7853EF3`.

The immutable canonical input
`D:\ProjectTemp\ch5-mp4a2-2009-input-binding-20260830-001\calendar_2009_primary_premodel_input.json`
matched `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`.
The frozen candidate wrapper matched
`DA998FB04C35EE852F53A504D5F4EB17EC089A8EC616A082F38E2B5CB2CD5A93`;
the frozen scientific invocation body remained
`80BAEDE65829F6A1215638F556544C92CAAB203A149FA6D1D88196BE22045F45`
at 5,424 characters.  The remediation static matrix and wrapper diff matched
`4EA6C18F71D16678BFD5E7094EBE143C22C31D380182E7518602228AEFE28345` and
`BE627CC2C5DD953C588F04BF139BB83E35F3ED3DE96FBC50ECF28BA9C6F8874E`.

`C:\MatlabProgram` was verified as the documented Junction to
`D:\MatlabProgram`.  Both logical and physical protected roots were read-only.
All seven post-run protected-source hashes exactly matched their pre-run values:

| File | SHA-256 |
| --- | --- |
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` |
| `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` |
| `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` |
| `lab_solve2.m` | `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20` |
| `HANK_mp_1eq.m` | `ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF` |
| `HANK_mp_1turn.m` | `D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF` |
| `HANK_firm.m` | `EE02C15414ADF9F99AADE04F1F22E64FA7094C8AB77753B6130BC4BFA6CE7BD5` |

## Fresh copy and observability gate

Fresh no-overwrite root:
`D:\ProjectTemp\ch5-mp4b-instrumented-matlab-calendar2009-owner-reauthorized-20260831-001`.

- D: free space before copy: `75,291,262,976` bytes; required threshold:
  `10,737,418,240` bytes; PASS.
- Protected tree: 32 `.m` files.  All 32 copied `.m` files matched the protected
  originals before instrumentation.
- Only copied `HANK_mp_1eq.m`, `HANK_mp_1turn.m`, `HANK_firm.m`, and added
  `MP4B_OBS.m` were changed.  Their copied hashes matched the accepted
  predecessor patch hashes exactly.
- New source-copy manifest SHA-256:
  `757D83D13B32BC92411F687069797A0F3DA4ADFC06FFEBD872B0674DBEDE9961`.
- New instrumentation manifest SHA-256:
  `511F59C6F6482DC5BBA7EBBFAD5B234C7D31B840AB2DE2CDDC836F4B74A52B2B`.
- Complete new copied-source diff SHA-256:
  `0B4B4D78EF45E33052E0888CC0E4AD8703167DC71DD8FA0D79BD01B5A053BB9F`.
- Pre-science gate SHA-256:
  `CFA0EE14410F44C9E56D8977D4F1363590CB8AC70E392F62E8CD47404EEF753D`.

The frozen wrapper was not copied or edited.  The exact one-shot command is
preserved at `exact_launcher_command.txt` under the fresh run root (SHA-256
`9F6E9A73CE4DECE261B390567DBD3EEC1BA287502D29D0C9FFB260DD31AB90D0`).
It used only the new root's `source_copy` and retained the canonical SHA argument.

## One-shot launcher evidence and ledger

One MATLAB launcher was started.  The completed MATLAB executable reported exit
status `0x00000001`.  It passed the normalized copied-root binding and wrote the
invocation-binding manifest, then reached outer turn 1.  It did not reach a
completed household call: the observer failed immediately before the first call
to `HANK_2ASSETS_HJB`.

| Route or call | Count | Evidence |
| --- | ---: | --- |
| MATLAB launcher process | 1 | terminal stdout/stderr |
| corrected-2009 stationary top-level | 1 | `mpHANK_equilibrium_2000` stack entry |
| outer `HANK_mp_1eq` | 1 | stack / trace turn entry |
| `HANK_mp_1turn` | 1 | stack |
| MATLAB household/HJB | 0 | failure occurred at pre-HJB observer call |
| KFE, household aggregation, firm, controller/adaptation | 0 | no corresponding source layer reached |
| MATLAB reruns / other MATLAB scientific runs | 0 | one-shot budget honored |
| Python stationary/HJB/KFE/household/MP2/MP3 | 0 | forbidden route unused |
| comparator replay, Zhejiang/Shanxi replay | 0 | forbidden route unused |
| other year/batch, shocks/AR1, transition/dynamics/IRF, R5/Results | 0 | forbidden routes unused |

`instrumented_terminal_status.json` and `instrumented_trace_summary.json` state
`outer_turn_count=1` and `household_call_count=31`; the latter is the observer's
formula (`numel(turns)*31`), not evidence of 31 completed HJB calls.  The stack
is the controlling evidence for the zero-HJB statement.

## Preserved artifacts

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `instrumented_invocation_binding_manifest.json` | 2,297 | `50614001EF125A035EB78EB9C796BF3BFEEC6E0017A4206FCBA01402FF63A3F2` |
| `instrumented_outer_trace.mat` | 263,224 | `E3EC398D6B2A5284A07941D74C4DA6FB5C460BC61D373A860C7D024CD86C7EAF` |
| `instrumented_terminal_status.json` | 156 | `B36EA498862231AF914B9922B1A9581E405EFAE05893BEF8CE4D459B8F1BA5D9` |
| `instrumented_trace_summary.json` | 224 | `F15DBA7B9FF42C7F2169CD7850543FB1DEDDDFE85640BCCFE7D49A2AD7CEE90C` |
| `matlab_launcher_stdout_stderr.txt` | 1,169 | `40C4EFDC4091569931CA49827AC60AB131BCD424AF69AB54A9772C7B8F7C55E6` |
| `run_manifest.json` | 4,488 | `AE078A56AF7FA22F87049A037E9151C9D8BEC76153659946AA937C26F82D215E` |

`run_manifest.json` was written only after the launcher terminated to inventory
the preserved failure evidence.  It explicitly records this timing; it does not
repair the failed launcher or authorize a rerun.

## Consequences and forbidden-operation audit

The run did not produce an admissible completed stationary trace.  Therefore the
mandatory preserved-MATLAB baseline-admissibility gate was not evaluated,
`MP4B_OWNER_REAUTHORIZED_INSTRUMENTED_MATLAB_BASELINE_ADMISSIBLE` was not
established, and no chronological MATLAB/Python alignment, extra low-return or
Zt-reset localization, wage-boundary chronology, propagation chain, or
same-input fault classification is supported.  All such analyses remain
unavailable rather than negative findings.

No protected MATLAB source, Python scientific module, validation driver,
adapter, comparator/helper/contract, field map, production/export file, MP2,
MP3, stationary runtime, canonical data, calibration, or project rule was
modified.  No MATLAB `checkcode` process was launched.  All copied sources,
traces, logs, and manifests remain outside Git under the fresh `D:\ProjectTemp`
root.  Repository scope is this report only.

`git diff --check` and explicit-path Git closeout are performed with this report.

Recommended next gate: **one Owner-reviewed, zero-science observability-helper
initialization audit that decides whether a new one-shot MATLAB authorization is
warranted; it must not itself repair or rerun this stationary execution.**
