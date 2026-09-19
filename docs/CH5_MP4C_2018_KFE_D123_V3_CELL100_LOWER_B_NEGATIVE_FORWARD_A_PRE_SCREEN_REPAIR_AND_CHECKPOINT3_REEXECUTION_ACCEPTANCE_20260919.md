# CH5 MP4C 2018 KFE D1-D3 V3 pre-screen repair and checkpoint-3 acceptance

Date: 2026-09-19

Reviewer verdict:

`PASS__V3_LOWER_B_NEGATIVE_FORWARD_A_PRE_SCREEN_REPAIR_ACCEPTED__CHECKPOINT3_COMPLETE_NONCONVERGED__BOUNDED_CONTINUATION_TO_CHECKPOINT6_AUTHORIZED`

## Accepted candidate

- baseline live main before task: `3b3193607b72e0648c886f7fef52ca31f04a38d4`
- Builder candidate: `ea97d03d065bae1c9fd7cbb98043d0e673d1e4a1`
- candidate tree: `d35f09ebd23b066cfb17de1e4be4b6dd297c0bd0`
- candidate chain is exactly `2 ahead / 0 behind` baseline
- focused engineering gate: `73/73` passed
- Results eligibility remains `FALSE`

## L3 acceptance of repair

The active lower-b / negative-transfer viability-filter repair is accepted.

The repair removes the coarse unbounded log-screen false negative only for active lower-b negative transfer by representing each distinct authority-backed one-sided interior-`a` derivative branch directly. Existing root, sign, direction, KKT, domain, finite-value, deduplication and Hamiltonian gates remain unchanged.

Upper-b logic, lower-b positive/zero-kink logic, D1/D2/D3, liquid-`Z`, one-axis interior-`a`, joint switching, lower-`a` zero-kink, solver/tolerances, grid/calibration and HJB convergence law remain unchanged.

## Cell100 closure

At V3 flat 100, the previously omitted forward-`a` negative branch is now represented and produces:

- `q_b=0.012803445679273433`
- `q_a=0.01134140574122853`
- `d=-0.018672540299433545`
- canonical `g_b=0`
- `g_a=0.21816942161080446`
- transfer-KKT residual `0`
- no rejection reasons
- selected admissible.

The root lies strictly inside the accepted legal interval
`(0.012601561934698366,0.015751950034835593)`.

## Accepted complete checkpoint 3

Accepted V3 SHA-256:

`4FDB36C17ACDC60B56661AEE1C0437B65EC4A871FD4E5E08A9A996FB10EF85EF`.

Accepted same-value checkpoint-3 objects:

- P3 identity:
  `06062946687922E1FAC83E8D4B1B19101469CC284339522595A19F4DECB6B07B`
- u3 SHA-256:
  `9BB321A63A92154D4B733B28126AF29DC1441B95D44517D884F4C858AECFE6F4`
- Q3 artifact SHA-256:
  `4085E0D1B166E72650CA1E74E5CF9462F6677EEAFA8CDEF1FBD153F14088C255`
- Q3 data/indices/indptr:
  - `13CA224BF05EADD453078A6A6A54A87EADC0C76C4753A0577703298C1767A521`
  - `AFB69E0EF55C1E8CEBAF4040485297B8CAE211F85451AC4B89E9B27CED97FBD0`
  - `BC95DE3B2915B44B63AEC514B67F12005964891E1E78AAB43C6FD38370ABA495`
- checkpoint-3 identity:
  `0DEEF7E54C4972BFF7BB67AE6B67BA5E54B588F3EEF5ACDE85048F3E02FE715D`
- checkpoint-3 arrays SHA-256:
  `B4024EC1202533982BAF9C893F946D20B871B76B3BD369DD4F19B34BF1DD99BD`.

D2/Q3 is accepted as PASS:

- minimum off-diagonal `1.3928351180224885e-06`
- diagonal construction error `0`
- `max(abs(Q3 @ 1))=1.09356967925578e-14`
- zero outward closed-face violations.

## Nonlinear checkpoint-3 classification

The Owner primary convergence law fails:

- `B3=0.1291770476282596 > 1e-8`
- `D3=0.05315900863346279 > 1e-7`.

No exact cycle is established. No complete approximate period-2/3 window exists at checkpoint 3.

The increase in Bellman residual and large `Q3-Q2` change are diagnostics only. The adopted law contains no trend-based stop rule, so these facts do not independently authorize termination.

## Scientific ledger accepted

- fresh V3 map: `1`
- selector evaluations: `800`
- scalar roots: `395`
- liquid-`Z` roots: `137`
- interior-`a` roots: `1`
- joint roots: `1`
- Q3/D2 assemblies: `1`
- checkpoint-3 evaluations: `1`
- direct HJB solves / V3->V4 updates: `0/0`
- scientific retries / solver substitutions: `0/0`
- terminal KFE/topology/MATLAB/downstream: `0`.

The sealed evidence manifest is accepted with `815/815` readback and SHA-256:

`01FB50C300936B76F7C56CBD0BBFDF8A91ABFDDF5180FE5AB77FA7341DD8D1F6`.

## Successor authority

No new scientific law is required.

Reviewer authorizes a bounded continuation beginning from exact accepted checkpoint 3 and ending no later than checkpoint 6.

The successor may perform at most three updates:

`V3->V4->V5->V6`.

It must stop immediately on primary convergence, direct-solve failure, policy-map/D2 failure, exact cycle, authorized approximate period-2/3 cycle, or provenance/nonfinite failure.

No terminal KFE/topology/SVD work is authorized inside that continuation task.
