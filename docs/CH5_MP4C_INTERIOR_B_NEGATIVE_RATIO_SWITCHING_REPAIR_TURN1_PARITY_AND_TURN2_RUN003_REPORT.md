# CH5 MP4C interior-b negative-ratio switching repair, turn-1 parity, and turn-2 run003 report

Date: 2026-09-21

## Terminal verdict

`FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE`

The authorized interior-liquid negative-ratio switching repair passed its
engineering gates, exact F0364 normal-selector parity check, and the mandatory
408-map turn-1 compatibility replay. The single fresh turn-2 run003 then
stopped at the first new scientific failure: Hebei, checkpoint 1, F-order flat
index 5, selector outcome `NO_ADMISSIBLE_POLICY`. The failing map did not reach
D2/Q assembly. No scientific retry, rescue, or further diagnosis was run.

## Authority, implementation, and code freeze

- actual live-main baseline: `c75d0b0de075278c690bc412657a0f4f10fa32e9`
- pre-science implementation commit: `5a350ad2f1ccc62d9f8c211b740416196136cee1`
- task: `CH5_MP4C_INTERIOR_B_NEGATIVE_RATIO_SWITCHING_REPAIR_TURN1_PARITY_AND_TURN2_RUN003_20260921`
- accepted entering-state blob: `85df3f0bdcc3b0bb3e7b12f0ba35dbb9abda764d`
- entering raw-payoff identity: `D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414`
- accepted turn-1 run004 manifest: `CF70E7D6A62A35F461D1A75B28F8F502B2CBDD2D94ED5D9DDFA099D821CC5EC6`
- accepted F0364 forensic manifest: `6FF469F423A7D5D321A59E1DC4031B04E967E3EE4A03E58865824D8B5D8CE1D0`
- accepted turn-2 run002 manifest: `A2A882B8D79A6897D0518447FA84F7775609E31D34452A5EB2F7B7773E9FD0B0`
- canonical initial-turn integration manifest: `79C6B15340AF641A736C79D0ED7C6450E39EA495263943280B6DDBD1B094F28D`

The selector change is limited to the existing interior-a switching
constructor. At an interior liquid node, a finite negative nonzero D3 ratio is
allowed, both a-derivative endpoints are divided by the ratio, and the two
images are sorted before testing the persisted liquid shadow. Ratio zero stays
fail closed. Negative-ratio behavior on active liquid faces stays fail closed.
Joint switching, D3/KKT, direction, finite-value, D2-admissibility,
deduplication, Hamiltonian comparison, and tie rules are unchanged.

`cost.py`, generator, nonlinear HJB/KFE, initial-turn integration, turn-2
integration, and canonical integration source blobs matched the baseline.
Post-execution source hashes matched the pre-execution freeze.

## Engineering gates

- focused tests: 15 passed
- `py_compile`: PASS
- `git diff --check`: PASS before scientific execution
- authority and predecessor manifest bindings: PASS
- pre-execution code freeze: PASS
- post-execution code freeze: PASS

An initial launcher attempt stopped during import because `PYTHONPATH=src` was
missing and raised `ModuleNotFoundError: ch5_two_asset_hank`. It created no
evidence root and made no selector or scientific call. After correcting only
the launcher environment, the authorized run was executed once. This import
failure did not consume a scientific retry.

## F0364 exact normal-selector parity

The focused selector check and the Beijing checkpoint-5 normal map both
selected the accepted switching candidate:

- transfer regime: negative
- derivative branches: b backward, a zero/switching
- `q_b=0.006091715618507631`
- `q_a=-0.0045978913784868415`
- `d=-7.8384208979658965`
- `g_a=0`
- `g_b=-4.227123020026542`
- transfer-KKT residual: `0`
- Hamiltonian: `-0.11188508398929994`
- admissible: true
- root status: `NOT_REQUIRED`

The mapped sign-aware q_b interval was
`[0.004111019263931103, 0.006526149020033277]`. The normal checkpoint map
persisted this receipt without an additional selector call. The focused check
also proved the forward liquid shadow was not emitted as switching, active-face
negative-ratio behavior was unchanged, ratio zero remained fail closed, and
F0364 introduced no root call.

## Mandatory turn-1 compatibility replay

Terminal:

`PASS__TURN1_ACCEPTED_POLICY_IDENTITY_PARITY_UNDER_INTERIOR_B_NEGATIVE_RATIO_REPAIR`

- accepted maps: 408
- maps replayed: 408
- exact matches: 408
- mismatches: 0
- accepted ordered digest: `E23F77D21521B31C62CFEFFFFA1ACF4C39D69D577A6CFBA697DAB03AE9428B6B`
- replayed ordered digest: `E23F77D21521B31C62CFEFFFFA1ACF4C39D69D577A6CFBA697DAB03AE9428B6B`

Separate turn-1 replay ledger:

- policy maps: 408
- selector evaluations: 326,400
- scalar selector roots: 130,705
- interior-z roots: 24,265
- interior-a switching roots: 392
- joint switching roots: 49
- HJB direct updates: 0
- D2/Q assemblies: 0
- SCC/KFE/SVD: 0
- aggregates/integration: 0
- scientific retries: 0

This exact parity opened the one authorized fresh turn-2 run003.

## Reached turn-2 results

Beijing and Tianjin completed HJB, terminal KFE, and stationary aggregates.
Both converged at checkpoint 12 after 12 direct updates.

| province | B | D | max direct-solve backward error | KFE residual inf | KFE mass sum | restricted dimension/nullity |
|---|---:|---:|---:|---:|---:|---:|
| Beijing | `3.243974533440053e-11` | `3.242754242904766e-08` | `2.1754586146795478e-16` | `3.2786273695961654e-16` | `0.9999999999999999` | `40/1` |
| Tianjin | `3.4566238760191936e-12` | `3.4545926119733394e-09` | `2.606842373633308e-16` | `2.203098814490545e-16` | `1.0` | `40/1` |

Stationary mass-form aggregates:

| province | At | Bt | Ct | Lt | AtTax | total assets |
|---|---:|---:|---:|---:|---:|---:|
| Beijing | `10.0` | `1.7104113648261137` | `12.183424284080282` | `0.6816823605951048` | `0.8815804892412894` | `11.710411364826113` |
| Tianjin | `10.0` | `1.6744625603118029` | `12.935923710397537` | `0.6649068120072927` | `0.39879402224705385` | `11.674462560311802` |

## First scientific failure

- province: Hebei (`province_index=2`)
- checkpoint: 1
- F-order flat index: 5
- grid index: `(b_index=5, a_index=0, z_index=0)`
- cell id: `v001_f0005_b005_a000_z000`
- physical state: `b=-0.1578947368421053`, `a=0`, `z=0.8`
- selector outcome: `NO_ADMISSIBLE_POLICY`
- selector evaluation ordinal: 806 within the partial map
- cell roots: 3 scalar roots, all interior-z; interior-a and joint roots were 0
- persisted attempted candidates: 15
- D2/Q at Hebei checkpoint 1: not run because the selector stopped first

The failure is recorded only as the first run003 rejection object. No further
scientific diagnosis or repair was performed. Provinces after Hebei were not
entered, and national integration was not reached.

## Exact fresh turn-2 run003 ledger

- source-native initializations: 3
- labor roots attempted/returned: 2,400 / 2,400
- completed policy/D2 maps: 27, plus the partial failing Hebei checkpoint-1 map
- selector evaluations: 21,600
- scalar selector roots: 9,644
- interior-z roots: 1,979
- interior-a switching roots: 0
- joint switching roots: 0
- D2/Q assemblies: 27
- direct HJB updates: 25
- post-update checkpoint evaluations: 24
- SCC decompositions: 2
- restricted GESVD: 2
- normalized stationary candidates: 2
- full-Q `Q.T@p`: 2
- full-space GESVD: 0
- aggregate evaluations: 2
- household batch, labor reconstruction, K1A, C1, firms, wage, monetary,
  fiscal, and canonical raw-next-payoff construction: all 0
- scientific retries, solver substitutions, damping/continuation, payoff
  transformations, and adaptive-controller calls: all 0
- turn-3 household, third outer turn, K1B, K2, MATLAB, GE, annual, shock, IRF,
  welfare, and Results calls: all 0
- wall time: `343.13523249997525` seconds

The turn-1 compatibility ledger is separate and is not included in these
turn-2 counts. The aggregate turn-2 ledger closes at the last completed map;
the partial failing map is preserved separately through its durable cell
receipt and selector ordinal. Historical accepted runs and forensics remain
lineage only.

## Evidence

- root: `reports/ch5_mp4c_interior_b_negative_ratio_repair_turn1_parity_turn2_run003_20260921`
- sealed manifest SHA-256: `E1DBBDF7E86B8F11A4DDB646A1CBD53259E5182D6EFE6A0D2679314874B8A403`
- entries: 306
- bytes: 4,583,535
- independent readback: PASS
- bad paths: none
- readback scientific calls: 0

Turn 3 was not run. K1B, K2, GE, and Results remained at zero. No CURRENT file
was modified, no successor was published, and main was not merged.
