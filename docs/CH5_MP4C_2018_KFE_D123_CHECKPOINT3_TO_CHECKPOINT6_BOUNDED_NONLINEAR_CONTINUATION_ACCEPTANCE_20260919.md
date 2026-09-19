# CH5 MP4C 2018 KFE D1-D3 checkpoint-3 to checkpoint-6 bounded continuation acceptance

Date: 2026-09-19

Reviewer verdict:

`PASS__CHECKPOINT3_TO_6_TRAJECTORY_ACCEPTED__REPRESENTATION_ONLY_CYCLE_DIAGNOSTIC_RESUME_ACCEPTED__CHECKPOINT6_NONCONVERGED__BOUNDED_CONTINUATION_TO_CHECKPOINT10_AUTHORIZED`

## Accepted candidate

- baseline live main: `28e74c0cfafd6826ea7f5600897d58608c58f44a`
- Builder candidate: `cc540b6d8ea4ff93ecbf4b8af9f7ece5aa2c2bb7`
- candidate tree: `d4d53fd562f656e1a267201a71b904bc9d2d03a3`
- candidate chain: `3 ahead / 0 behind`
- focused engineering gate: `78/78` passed
- Results eligibility remains `FALSE`

## L3 acceptance

The checkpoint-3 to checkpoint-6 trajectory is accepted.

The task consumed exactly updates 4-6, produced complete checkpoints 4, 5 and 6, passed D2 at all three checkpoints, and respected the frozen HJB update, convergence and cycle laws.

No selector, D2, direct-solve, convergence or cycle terminal condition was triggered before the bounded checkpoint-6 ceiling.

## Engineering resume after checkpoint-4 diagnostic exception

The initial scientific process completed and sealed:

- V3->V4 direct solve;
- complete 800-cell V4 policy map;
- Q4/D2 PASS;
- entry into checkpoint-4 diagnostic evaluation.

It then raised `ValueError: Improper number of dimensions to norm.` because the approximate-cycle helper applied the vector infinity norm directly to a three-dimensional value-field difference.

The corrective code change is accepted as a **representation-only engineering repair**:

- the frozen adopted quantity is `||vec_F(V_j-V_(j-k))||_inf`;
- the repair explicitly applies `.ravel(order="F")` before `np.linalg.norm(..., ord=inf)`;
- no tolerance, cycle window, period, stopping order, value field, policy, Q operator or model equation changed.

The sealed V4 scientific prefix was verified and reused without recomputing V3->V4, the V4 map or Q4. The resume then continued from that immutable prefix.

This acceptance treats the recovery as non-scientific resume rather than a scientific retry. It is not authority for outcome-dependent reruns: future scientific objects must still fail closed unless a similarly representation-only, provenance-preserving engineering correction is independently reviewable.

## Accepted complete checkpoints

Checkpoint 4:

- V4 `938682CEA35E4ED77F02087AB6BDE9204A0B4C00B9E898E3200799D1367C149B`
- P4 `8ACC7002ED5E77DA072F283DB86FD06C4ED00E7F42F6FB9672D123891B5774EE`
- u4 `2DB3FA93B25D701B6EB36FAEF2EDBEA24C4198393B48D2C12DA6B2D23FBF9B06`
- Q4 `94432703101724F6F76317A00F9DDCA7583065AB7094416BDC03E85DDEB9AE91`
- checkpoint identity `69BA60083B3D96CDCFF1BE935AC425C04F68DF44A9FDB545209FA4280742F420`
- `B4=0.179987383327527`
- `D4=0.0136984055627334`.

Checkpoint 5:

- V5 `34077AE29E144E3BC5773A830A7577419EEE19B41424A7771C74E46554DECD6B`
- P5 `702010801BDC2559C97883852F0F662CE94859F299945BAEA2B7B8FD8917DB43`
- u5 `8D4F441128371ECFD685401489179D4DFAACB992D2325EDADAC58F9A5B835A2D`
- Q5 `1BF6CB8031116064B8CF603243BDFA86565DD8A6B8B09EADEF409D0ADFD632E2`
- checkpoint identity `1CACE68D0BD30F24F16FB032ECCB6BCA2B2F939AF3A6B4556098DB1CBF577080`
- `B5=0.0317254872882517`
- `D5=0.0193420794201278`.

Checkpoint 6:

- V6 `69865ACDD71A26A3E3F4A8DAD55C964F826D34C774C9B8193FE997973EE6D89F`
- P6 `63026FBE8BE72E3B29B5FC44EBD100C01C146179D05B55C779E9E232AEA435A3`
- u6 `09D5A6622535709146751865931109F058FED3688FAE755C5EF9A0E00AD8B89E`
- Q6 `039734AF0BC38AD3BD0FF38854CBE8B4B0B93BA415EC2A47B1C09F827EA7F454`
- Q6 data/indices/indptr:
  - `CE091A208909AEA1D71637DD269FF5D98A59CE5785F90870212D453F86DBFDC9`
  - `B44ED2AC2E4E86E01B040089645FE66EEC5CFB7874E6DCDA6A307803632B70E4`
  - `DC38CF83DFC0A6F522020AC8DBC16EDBEB4E1D273A59EDCA6697CD721E3593F2`
- checkpoint identity `B26177C216DA6902226BD93E802A2B1FE0E794B29BE14EA1A1BCBFFD8F8691A1`
- checkpoint arrays `C703E99742D87565D3FB15EDE4091B265EF36B47D6109DA44052B5290DC4F98D`
- `B6=0.005940678766947715`
- `D6=0.010000685482095761`.

All D2 receipts are PASS.

## Convergence and cycle classification

At checkpoints 4, 5 and 6 the primary convergence law fails because both metrics remain above the frozen thresholds.

No exact checkpoint identity recurrence exists.

The authorized approximate period-2 rule was evaluated when available and did not trigger. The authorized approximate period-3 rule was first fully available at checkpoint 6 and did not trigger.

The observed fall from `B4` to `B6` and the changes in policy/Q are diagnostics only. They do not change the frozen stopping law.

## Accepted scientific ledger

Cumulative new work from checkpoint 3:

- direct HJB solves / updates: `3 / 3`
- fresh policy maps: `3`
- selector evaluations: `2400`
- scalar roots: `821`
- liquid-Z roots: `51`
- interior-a roots: `4`
- joint roots: `0`
- D2/Q assemblies: `3`
- complete checkpoint evaluations: `3`
- scientific retries: `0`
- topology/KFE/SVD/eigen/nullspace/`Q.T@p`: `0`
- MATLAB/production/GE/downstream/Results: `0`
- solver substitution/damping/relaxation/adaptive Delta/parameter continuation/clipping/artificial diffusion: `0`.

The resume sealed manifest is accepted:

`1BFAB497357EE2740B259E23AD970EEB927799D9FD37A60A7D30E544E1970725`

with `1633` entries and `26,156,422` bytes. The sealed original prefix remains immutable and separately evidenced.

## Successor authority

Checkpoint 6 is complete and nonterminal under the Owner law. No new scientific-law decision is required.

Reviewer authorizes one bounded continuation from exact checkpoint 6 through checkpoint 10, consuming at most global updates 7-10.

The successor must stop immediately on primary convergence, exact/authorized approximate cycle, policy-map/D2 failure, direct-solve accuracy failure, provenance/nonfinite failure, or complete checkpoint 10.

Terminal topology/KFE is not authorized inside that continuation task.
