# MP4C 2018 captured evidence retrospective-manifest integrity certification

## Terminal

`MP4C_2018_CAPTURED_EVIDENCE_RETROSPECTIVE_MANIFEST_CERTIFIED__CURRENT_RAW_ARTIFACTS_INTERNALLY_CONSISTENT_AND_BOUND_TO_PUBLISHED_EXECUTION_REPORT__CAPTURE_TIME_HASH_GAP_EXPLICIT__READY_FOR_READ_ONLY_FORENSIC_REISSUE`

This is evidence-integrity work only.  It does not rerun 2018, solve an HJB or
KFE, run postmortem, or modify model, source, or test code.

## Provenance classification and limitation

The original preserved execution root did **not** contain
`audit_manifest.json`.  It was not created or backfilled by this task.

The new manifest is explicitly classified as:

`RETROSPECTIVE_MANIFEST__NOT_CAPTURE_TIME_HASH_RECORD`

It certifies current preserved-file hashes, internal consistency of the current
raw objects, and their consistency with the GitHub-published execution-report
anchors.  It cannot prove that raw artifacts whose hashes were not published at
capture time experienced no byte change between capture and this retrospective
certification.

## Authority and scope

- Current task authority: `c1644129e394512942a3567fa90baefde196dddb`.
- Direct parent: `aa6a1534873fb4cd90d2c783c10607752d5530fa`.
- Published execution commit: `01956ca46f117e4faab9f4ff4bba96ecbb780ea3`.
- Published execution-report blob: `f708b6b854ed7838ebd2c005bcb60cb6ec42f5e3`.
- At start, `HEAD == origin/main`, ahead/behind was `0/0`, and the tracked
  worktree was clean.
- The original root had 22 pre-sidecar files.  The retrospective sidecar was
  written only after all checks passed, using no-overwrite creation.

## Published anchors and raw-object consistency

- `household_call_ledger.csv` has 725 data rows and SHA-256
  `78F1BAFC3664D1ED644293FE98FA384468B23291F9CE8E42400EE0F63BB06A9F`.
- `hjb_return_ledger.csv` has 725 data rows and SHA-256
  `7D914989AD3CD047FA45CABA5A9209563465BE1799410BB01699F51CF542DA3F`.
- Capture context is outer iteration 24, household call 725, 安徽, province
  index 11.  HJB is nonconverged after 100 iterations with statistic
  `0.3038218386543494`; KFE path is
  `MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE`.
- The warning contains `MatrixRankWarning: Matrix is exactly singular`.
- A is 800×800 with 3106 finite stored entries.  After in-memory canonical
  sorting/coalescing, captured A transpose is exact `A.transpose()` including
  `indptr`, `indices`, and binary64 data.
- Faithful row `floor(0.37 * 800) - 1` is 295.  Replacing row 295 of captured
  A transpose by its unit row in memory reproduces captured B exactly,
  including sparse structure and binary64 data.
- RHS is finite shape `(800,)`, with exactly one nonzero at index 295 and the
  stored binary64 value `0.007`; raw solve is shape `(800,)` with 800
  non-finite entries.  No solve was performed.
- Existing postmortem JSON agrees with the published report: A transpose and
  B rank 799/nullity 1 at tolerance `3.821460885301736e-05`; SCC count 139;
  three closed SCCs of sizes 2, 24, and 4; max absolute row-sum residual
  `5.209558481541731`.
- Launch/preflight/input/code receipts are present and mutually consistent:
  PID 67056, expected input SHA, one execution, 725 calls, zero reruns,
  `first_capture=true`, fail-closed terminal, and no normal-completion summary.

## Cryptographic inventory

| Preserved file | SHA-256 |
| --- | --- |
| `first_singularity_operator_A.npz` | `A17AA9CF512D4D3FDD79235D0D1897CFB20486D2EF5FAA68850910C849AA1B42` |
| `first_singularity_operator_transpose.npz` | `7C1ADEDEE5B26BB30B5A8CC1C9D3D0E83DFF18FAE7860C39986E9E6C2D8FDA66` |
| `first_singularity_contaminated_matrix.npz` | `B04F5A4B99135272FCFF61BEAE220A2C25F5455E478F7994C1394CD6EC869EF4` |
| `first_singularity_rhs.npy` | `C8ADAA98B7B1B7484CAF2A1C4E44D7FD0106D62BCC8FB10084D11CD877CDABFB` |
| `first_singularity_raw_solve_vector.npy` | `F4D51DC00DBAB73F63322A73692EBEA13CAEC2D0A1204A514CBE39329DF8B8E2` |
| `first_singularity_localization.json` | `3628725A54B97344F501C0E44D32338A0B5CF6733D6022B9DD7A4C82C890BD63` |
| `first_singularity_hjb_status.json` | `2B2436E575BB057C9C4BD51F1F6CC5979CBBDACB78D9C9A452BFE90B6181CAF5` |
| `first_singularity_warning_and_traceback.txt` | `45C63691B33BEB75F651DD15F09E725D4B919EB78222DD09812473290B72141D` |
| `diagnostic_execution_receipt.json` | `052B33C17E3112E2975EDFFE949D1C88DC51DC87B65AF25F532BB19AFE88E5CB` |
| `diagnostic_child_terminal_sentinel.json` | `78ED3986BD3A0E3A22400D9FC65F1F64EDDE470B68F40392BE0D5BFA79154AA0` |
| `zero_or_bounded_science_ledger.json` | `ECCF1989443C49913E9639E8D9B0919D3F439E39383E6EF6DF51A24EA63FF487` |
| `diagnostic_child_launch_receipt.json` | `13442A4385AB6249CB387C1F7311164824261888B5656E2D21D6CA5888AE8209` |
| `durable_execution_preflight.json` | `CA8FE23037E9E3595853BF5E29DE6463532A9F0C3A07CA1455F67ACC050653B0` |
| `input_2018_identity.json` | `C2639E8C316B92D63C611E38378260EAF313D0D64A4AA61B8CCB3782E5F6C216` |
| `scientific_code_identity_manifest.json` | `99A3AACBFECC3FA5246535E38087DAE5D43E69FD1AC8527900B9E44398B61021` |
| `postmortem_operator_summary.json` | `8EBCDCFA1DC9B0C8C27933A6A279C6695E6525777BD5B9186DA6E062F67E51CC` |
| `postmortem_scc_closed_classes.json` | `8004321C9AF8C144A1366D4E5E34AB475145844E9F55B3412847B64A9A96199C` |
| `postmortem_rank_nullity.json` | `A4BA1650A08675F8A39F32E09526007AD03C855F270B5A1008AE9CF74111F775` |

## Retrospective manifest and sidecar

- Certification root:
  `D:\ProjectTemp\ch5-mp4c-2018-retrospective-evidence-integrity-certification-20260903-001`.
- Manifest and the optional original-root sidecar are byte-for-byte identical,
  11,711 bytes, SHA-256
  `D0472539EA553CFCFF7D34046EA71C8C68DD78C7FF7D44F58F7A3AD50D06C490`.
- The sidecar is named `retrospective_execution_evidence_manifest.json`; it is
  not an `audit_manifest.json` and makes no capture-time hash claim.

## Boundaries

New scientific PID, stationary, household, HJB, KFE, MATLAB, R/PLM, shock,
and IRF calls were all zero.  No model/source/test edits, repair, rerun,
postmortem rerun, forensic nullspace/SVD/SCC analysis, or Results claim occurred.
