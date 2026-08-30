# Chapter 5 Two-Asset HANK MP4B filename-concatenation repair report

Date: 2026-08-30

Live authority: `80dbe6a752d6b4fe3f4ee24beff232117bdd676d`

## Terminal verdict

`MP4B_FILENAME_CONCATENATION_REPAIR_PATH_SMOKE_AND_PRESOLVER_REVALIDATION_PASS`

All three required markers were established without a scientific/model call:

- `MP4B_FILENAME_CONCATENATION_REPAIR_STATIC_REVIEW_PASS`
- `MP4B_LOGICAL_PHYSICAL_PATH_EQUIVALENCE_SMOKE_PASS`
- `MP4B_2009_PRESOLVER_SAME_INPUT_IDENTITY_PASS`

This is infrastructure/presolver acceptance only. It does not accept or
authorize stationary parity.

## Continuity

Fresh fetch and fast-forward established clean
`HEAD == origin/main == 80dbe6a752d6b4fe3f4ee24beff232117bdd676d`.
Its direct parent is prior blocker commit
`60528127890a862d5c92ef4e7384a97e2ce1fe7f`.

All controlling rules, Owner MP4 decisions, MP4A2 evidence and prior MP4B
tasks/reports were read in full. Controlling rule blobs, protected source,
standalone oracle, MP2, MP3, annual binding and stationary runtime identities
remained unchanged. No active historical R5 import exists.

The prior smoke failure consumed zero scientific calls. All earlier scientific
budgets remain historical and were not reused.

## Complete filename-concatenation defect audit

All active `mp4b*.m` files under `validators/multi_province/matlab/` were
searched before repair for char-plus suffix construction and all remaining `+`
expressions were classified.

Affected finite set:

| File | Pre-repair line | Expression |
|---|---:|---|
| `mp4b_path_equivalence_smoke.m` | 25 | `helpers{i}+'.m'` logical file |
| `mp4b_path_equivalence_smoke.m` | 26 | `helpers{i}+'.m'` physical file |
| `mp4b_calendar2009_stationary_wrapper.m` | 47 | `required_helpers{helper_index}+'.m'` logical file |
| `mp4b_calendar2009_stationary_wrapper.m` | 48 | `required_helpers{helper_index}+'.m'` physical file |

Other plus expressions were numerical matrix or profiler call-count arithmetic,
not filename construction. No other active char-plus suffix existed.

`MP4B_FILENAME_CONCATENATION_DEFECT_SCOPE_COMPLETE`

## Exact repair and static review

The four affected expressions were changed only to R2022b-safe explicit char
concatenation:

```matlab
[helpers{i} '.m']
[required_helpers{helper_index} '.m']
```

Helper names, finite logical/physical allowed roots, byte/content equality
checks, `N_prov=31`, calendar binding, no-overwrite behavior and all scientific
expressions remain unchanged.

Post-repair identities:

| File | SHA-256 |
|---|---|
| `mp4b_path_equivalence_smoke.m` | `D505505F3ED24E1E6C0808DAD2DD4BCB753FFCC17AE7E04DA7868E6BCE97148B` |
| `mp4b_calendar2009_stationary_wrapper.m` | `DB3E9015C51CD9AE468CE693BF272605055276138EE8EAC7D2BF0BC43D37CB83` |
| focused test | `3A0DAE018E1CC06B19EE52470623DE43A622EDD36EEFBDB4BA1D7610C1EE036E` |

Static evidence:

- MATLAB `checkcode` returned no issues for all active MP4B helpers;
- post-repair unsafe `+'.m'` scan returned zero matches;
- focused tests assert both smoke and scientific wrapper use explicit safe
  construction;
- protected MATLAB hashes remained unchanged;
- `C:\MatlabProgram` remained a junction whose sole target is
  `D:\MatlabProgram`;
- exact finite-root guard and `N_prov=31` remained present;
- fresh smoke root was absent and D drive had more than 76 GB free.

`MP4B_FILENAME_CONCATENATION_REPAIR_STATIC_REVIEW_PASS`

## One-shot non-scientific path smoke

Root:
`D:\ProjectTemp\ch5-mp4b-filename-repair-path-smoke-20260830-001`

Manifest:
`path_equivalence_smoke_manifest.json`

Manifest SHA-256:
`0D4E337086E6D5CCAE5704CEC45CBB4DDA9E15C8AD8270633EF4C355F6FE7640`

The manifest records logical root
`C:\MatlabProgram\2023年12月2日 多省份神经网络HANK`, physical root
`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`, `N_prov=31`,
scientific call count zero, and these exact resolutions:

- `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\load_GDPdata.m`
- `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\load_distdata.m`
- `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\mpHANK_equilibrium_2000.m`
- `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_mp_1eq.m`
- `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_mp_1turn.m`
- `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m`

Every parent equals the exact verified physical model root and every logical
and physical helper text pair matched.

`MP4B_LOGICAL_PHYSICAL_PATH_EQUIVALENCE_SMOKE_PASS`

## Fresh presolver revalidation

Root:
`D:\ProjectTemp\ch5-mp4b-filename-repair-presolver-20260830-001`

Canonical SHA remained
`507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`.
Recursive semantic comparison covered the complete annual and prepared-state
contract and returned mismatch count zero.

| Manifest | SHA-256 |
|---|---|
| MATLAB | `B810618C7580BB7BFC3A9E78B4309119EF54EA7F2EBD1E492AFCBE9AEA99642D` |
| Python | `1F95CFCB2D81A02B38FD1DC2F2BED632E31566809AFD59DBA85A52D7060BECAC` |

`MP4B_2009_PRESOLVER_SAME_INPUT_IDENTITY_PASS`

## Scientific/model ledger

| Operation | Calls |
|---|---:|
| MATLAB stationary/model | 0 |
| MATLAB HJB/KFE | 0 |
| Python stationary/model | 0 |
| Python HA/HJB/KFE | 0 |
| wrong-year MATLAB | 0 |
| 2010-2023 batch | 0 |
| shocks/transition/dynamics/IRF | 0 |
| legacy R5 / Results | 0 |

Only `checkcode`, exactly one infrastructure smoke, presolver serialization and
comparison, hashes, compilation and non-model tests ran.

## Tests, unresolved items and forbidden-operation check

- complete focused MP1-MP4B suite: `64 passed`;
- Python compile: PASS;
- MATLAB checkcode: PASS;
- `git diff --check`: PASS;
- source/rule/canonical identity checks: PASS.

Unresolved item: corrected calendar-2009 MATLAB/Python stationary parity has not
been executed or accepted.

Forbidden-operation check: PASS. Protected MATLAB, accepted scientific Python,
primary data/cache and canonical input were not modified. No wrong-year route,
batch, model, shock, transition, dynamics, IRF, R5 or Results operation ran.

Git closeout uses explicit-path staging, one execution commit, one non-force
push, GitHub read-back of every changed path, clean worktree and ahead/behind
`0/0`.

## Exactly one recommended next gate

Recommend **fresh bounded corrected-calendar-2009 MATLAB/Python stationary
parity execution**, using the smoke-validated helper chain and separately
reauthorized one-run-per-language scientific budgets.
