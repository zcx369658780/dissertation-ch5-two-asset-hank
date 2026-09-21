# CH5 MP4C K1B turn-3 lagged raw-ra0 attractiveness activation safety gate

Date: 2026-09-21

## Terminal

`PASS__K1B_TURN3_LAGGED_RAW_RA0_ATTRACTIVENESS_ACTIVATION_SAFETY_GATE__SHARES_AND_HOUSEHOLD_PAYOFF_CANDIDATE_READY__NO_HJB_RUN`

Classification:

`TURN3_K1B_INPUT_CANDIDATE_ONLY__HOUSEHOLD_NOT_RUN`

This gate performed only deterministic population-z-score, stable foreign-only softmax, ordered payoff, and pure capital-network conservation arithmetic on accepted persisted inputs. It made zero model-science calls.

## Authority and input binding

- GitHub live-main baseline: `7b6c30a568e1c89ca6a553451abe382e48ee7e23`.
- Completed-turn2 raw ra0 SHA-256: `B3B50A6F0A3876904582DE05354C2DF76A71524FB53E41D4170109B8FCEB8951`.
- Accepted K1A turn3 payoff SHA-256: `5996A20CEE227389A7975703452EA6DAF1A2F817C517FFE43BEF3A53FA4292E2`.
- Accepted K1A share SHA-256: `AC8DD36BB21E2B907D7521C98F8E65DCA3803291B54296AA7C2681E8CC6F226F`.
- Distance canonical-LF SHA-256: `30401B7754A0126D544D54ABB36C6CB662E3E386663E3110EF3F68E417FDA084`.
- Run005 sealed manifest SHA-256: `C93BF19DB7C909A50C2753B0EA06FD4735F48A4C41C5A4C9CA6F8817B693B72F`.
- Run005 readback, canonical order, row count, JSON/NPZ bitwise raw-ra0 identity and tracked Git blobs: PASS.

## Population z-score

The exact convention is `ddof=0`, using ordered `math.fsum` arithmetic over all 31 model provinces.

- Ordered raw-ra0 mean: `0.5151713619509639`.
- Population standard deviation: `0.18665369395010123`.
- Ordered z-score mean: `-3.3127622508976447e-17`.
- Ordered z-score population variance: `1.0`.
- Z-score vector SHA-256: `E152FE1C33634F2127D2B535638FA2725687650496140641F0FC6D6A4C02B564`.
- Provenance: `COMPLETED_TURN2_RAW_RA0__USED_FOR_TURN3_K1B_ATTRACTIVENESS`.

Canonical-order z-score vector:

```text
[2.937848293449904, -0.714103595303393, -0.9730027377291585,
 -0.3967960328381897, -1.1346804784819673, -0.86963404782398,
 -1.4043061440872628, -1.0907812243933397, 2.503019275674002,
 0.17860500380639358, 0.5352218874046184, 0.7366092445868586,
 0.7473708946932336, 0.711728388206135, -0.9293009502502068,
 -1.0494524793910933, 0.15962897056949726, -0.13749731270667634,
 0.28641713924798984, -0.6950789776198767, 1.0989334031137468,
 0.9082167055927249, 0.16073934535784976, 0.36412437235814443,
 -0.5629436292099035, 0.8779976911225621, -0.257579795137193,
 0.0346477379828774, -0.8898628401216986, -0.5603760406590081,
 -0.5757120674135916]
```

No sample correction, clipping, winsorization, ranking, rescaling, smoothing, or other transformation was applied.

## K1B shares

The score was formed exactly as:

`score[j,i] = -2.0 * distance_score[j,i] + 0.5 * z_j`

Only `j != i` entered the existing stable softmax.

- Score-matrix SHA-256: `2369B0A216883B5A2B58411426AA58843FF733C69F596059478351F9E368963A`.
- Foreign conditional-share SHA-256: `E3585A0BEE82C852EEE779458DEEE7A024B7ABA74E6B1B1A511AD992DAF64610`.
- Full K1B portfolio-share SHA-256: `4C3AB67F1982AEB3B707D07C53BB98C5BA54C835234DFEDE45A96B09BC5E3AB6`.
- Orientation: destination by origin.
- Conditional diagonal: exact zero.
- Full diagonal: exact `1-theta_i`.
- Foreign column totals: `theta_i` within the frozen `1e-12` accounting tolerance.
- Full column totals: one within the frozen accounting tolerance.
- All shares: finite and nonnegative.

The full K1B matrix is persisted both in JSON and in the frozen NPZ plan. This exact matrix is the required share plan for any future turn3 K1B quantity and payoff accounting.

## K1A versus K1B

- Home shares bitwise identical: PASS.
- Changed foreign cells: `900 / 930` off-diagonal cells. The remaining 30 belong to the origin with `theta=0`.
- Maximum absolute foreign-share change: `0.044098231463694224`.
- Acceptance used no preferred reallocation direction, magnitude, or convergence criterion.

## Ordered turn3 K1B household payoff

The z-score entered attractiveness only. The completed-turn2 raw ra0 level entered the payoff only. Each origin payoff used ordered destination `math.fsum` with the same exact K1B share matrix.

- K1B rah turn3 SHA-256: `CEEFE34C16BA0DFDE9FA0C5590DFBB89084475BD88A8496EC18FEEBA7CB674D2`.
- Minimum / maximum: `0.30906980372526094 / 0.994711274812942`.
- Ordered mean: `0.5266585162077394`.
- K1A-vs-K1B maximum absolute payoff change: `0.04695611438918196`.
- Bitwise-equal K1A/K1B payoff entries: `1 / 31`, corresponding to the `theta=0` origin.

The turn3 candidate preserves every non-`rah` state field and all canonical row identities from accepted run005. Only `state.rah` and the required K1B classification metadata changed. Turn3 household execution remains zero.

## Timing and conservation panel

Timing mapping is unique under the current authority:

- score source is completed-turn2 raw ra0;
- no turn3 firm output was read;
- no same-turn return feedback occurred;
- the K1B share plan was frozen before turn3 household/runtime;
- future turn3 quantities may use future household wealth only with this already frozen `S_K1B`;
- future quantity and payoff accounting must use the same share-plan hash.

Using accepted turn2 household wealth only as a scale check:

- ordered origin private wealth: `140310000.0`;
- ordered destination private capital: `140310000.0`;
- national private-capital residual: `0.0`;
- every origin wealth column conserved: PASS;
- home retained identity: PASS;
- maximum ordered-payoff versus pure-network diagnostic difference: `1.1102230246251565e-16`.

This panel is not a turn3 capital prediction.

## Zero-science ledger

All required counts are zero:

- household HJB/KFE;
- direct HJB solves;
- selector/root;
- D2/Q;
- firm;
- integration/outer turn;
- turn3 household;
- K1B scientific runtime;
- K2;
- MATLAB;
- GE/Results;
- retry/tuning.

## Evidence

- Evidence root: `reports/ch5_mp4c_k1b_turn3_lagged_raw_ra0_activation_safety_gate_20260921_run001/`.
- Manifest SHA-256: `55908ED2B1C99436CF25A564AEE0E36589081B8CB20087505F7F5AB4F7AFC396`.
- Entries / bytes: `14 / 150,185`.
- Independent readback: PASS; bad paths: 0; readback scientific calls: 0.
- Focused tests: 4 passed.
- Production source and CURRENT: unchanged.
- Successor: not published.
