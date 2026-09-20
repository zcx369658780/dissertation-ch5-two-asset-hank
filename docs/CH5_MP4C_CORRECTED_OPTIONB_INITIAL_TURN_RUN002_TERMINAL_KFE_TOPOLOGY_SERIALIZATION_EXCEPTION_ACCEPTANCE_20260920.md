# Chapter 5 corrected Option-B initial-turn run002 terminal-KFE topology serialization exception acceptance

Date: 2026-09-20

Reviewer verdict:

`ACCEPTED_FAIL__BEIJING_HJB_CONVERGED__TERMINAL_KFE_TOPOLOGY_SERIALIZATION_EXCEPTION__NO_KFE_CLASSIFICATION__SERIALIZATION_REPAIR_AND_RUN003_AUTHORIZED`

## Accepted failed candidate

- live-main baseline: `67584b84d02823b56089a7eaa10e47ccaf811e5a`
- Builder candidate: `2027b917390f00bdcc40757b1ab2031f3e24d201`
- candidate tree reported and remotely read back by Builder: `04e57ec44070d0998fd1b8c694bd0c752e08f3fe`
- ancestry independently verified: `2 ahead / 0 behind`, merge-base exactly the baseline
- independently verified changed paths: 144
  - driver: 1
  - focused test: 1
  - report: 1
  - run002 evidence: 141
  - CURRENT files: 0
- Builder did not merge main and did not publish a successor.

The candidate has been fast-forwarded into live `main` as accepted failed-run evidence and as the successor-repair baseline.

## Checkpoint-0 repair acceptance

The authorized run001 engineering repair is accepted.

Before science, the Builder established:

- checkpoint-0 current-only policy diagnostics;
- checkpoint-0 current-only operator diagnostics;
- all previous-checkpoint comparison-only fields explicitly unavailable/null;
- checkpoint 1+ still routes through the unchanged comparative helpers;
- focused suite `43 passed`;
- `py_compile`, `git diff --check`, authority/blob/order, run001 lineage and code freeze all PASS;
- `nonlinear_continuation.py` remained unchanged in run002.

This closes the run001 `NoneType` diagnostics defect.

## Beijing HJB acceptance

Under the exact accepted outer-turn-1 Beijing initialization, run002 established corrected HJB convergence at checkpoint 12:

- `B=1.292732587643286e-11 <= 1e-8`
- `D=1.2743897048750341e-08 <= 1e-7`
- corrected policy maps / D2 assemblies: `13/13`
- direct HJB updates: `12`
- solver: only `scipy.sparse.linalg.spsolve`
- maximum normwise backward error: `3.0832786979441453e-16 <= 1e-12`
- final value SHA-256:
  `48396D52F13045B4F3370CA892C9989813BBEA8F0D45A577DD8C6D6EDE5ADA93`
- final Q artifact SHA-256:
  `E1F55D0B755CB83D4F6A3CB4FEFD6DBC8CD4F05C6D23FC5DE00302E16B74BF20`
- final D2/Q legality and conservation checks: PASS.

This is accepted as Beijing HJB convergence for the exact run002 input and frozen science.

It is not KFE acceptance and it does not establish a Beijing household stationary aggregate.

## Exact terminal-KFE failure classification

The first failing object is:

`北京 / checkpoint 12 / terminal_kfe_topology_receipt_serialization`.

Exception:

`TypeError: Object of type csr_matrix is not JSON serializable`.

The failure occurs after the topology helper has:

1. built the exact-positive graph;
2. executed exactly one strong SCC decomposition;
3. returned an in-memory topology dictionary.

The raw topology dictionary contains a CSR `adjacency` and NumPy `labels`. The unchanged `_terminal_kfe` then passes that raw dictionary directly to the generic JSON writer, which accepts neither object type.

The underlying topology result was not persisted, so closed-class count, component count/sizes and memberships are unavailable. They must not be inferred.

No second SCC was executed.

Therefore run002 terminal-KFE classification is:

- actual SCC decompositions: 1;
- topology scientific classification: unavailable;
- dense GESVD: 0;
- normalized stationary candidates: 0;
- `Q.T@p`: 0;
- KFE PASS/FAIL: not established.

This is a persistence/serialization defect after the SCC call, not evidence of a topology or KFE scientific failure.

## Ledger reconciliation

The sealed `scientific_ledger.json` reports SCC=0 because the initial-turn driver accumulates province-local terminal-KFE counters into its global ledger only after `_terminal_kfe` returns.

The zero-science post-terminal receipt independently audits the executed call path and records actual SCC=1. The original sealed ledger and terminal receipt were correctly left unchanged.

The discrepancy is accepted as an exception-path accounting defect. Future execution must accumulate terminal-KFE call counters even when terminal-KFE raises after consuming a scientific call.

## Accepted run002 scientific consumption

Actual run002 consumption:

- source-native initialization: 1
- labor roots: 800/800
- policy maps / D2: 13/13
- selector evaluations: 10,400
- scalar selector roots: 4,148
- interior-Z / interior-a / joint roots: 760 / 17 / 1
- direct HJB updates / post-update evaluations: 12 / 12
- SCC decompositions: 1
- GESVD / normalized mass / `Q.T@p`: 0 / 0 / 0
- aggregates / integration / firms: 0
- scientific retries / solver substitutions: 0 / 0
- turn 2 / K1B / K2 / MATLAB / GE / Results: 0.

Run001 remains separate historical consumption and is not reset, renamed or absorbed into run002.

## Evidence acceptance

Run002 evidence root:

`reports/ch5_mp4c_corrected_optionb_initial_turn_31_province_household_kfe_k1a_c1_one_turn_integration_20260920_run002/`

Final sealed manifest:

`D01A8A0CDF6808824735FEACABD7572249970DE97606A63BEA86209B5B6F531A`

with 139 entries and 1,949,298 bytes. Independent readback passed with zero bad paths. Pre/post scientific code freeze matched exactly.

## Repair authority

No Owner-level scientific choice is required.

The accepted topology algorithm and KFE mathematics remain unchanged. The successor may only:

1. replace raw topology-object JSON persistence with a deterministic JSON-safe projection of the already computed topology result;
2. preserve the in-memory topology object for the existing scientific checks;
3. record deterministic evidence identities for non-JSON carriers, preferably CSR identity/hash and labels hash rather than serializing the full sparse carrier;
4. fix exception-path terminal-KFE ledger accumulation so consumed calls are reflected even when the KFE function raises;
5. regression-test those changes with zero model science;
6. perform one fresh bounded run003 under the unchanged scientific contract.

The accepted `q1_kfe_validation.py` provides an existing JSON-safe SCC evidence pattern; it may be used as representational guidance only. The SCC/topology algorithm itself must not be replaced or rerun during zero-science testing.

Turn 2, K1B, K2, GE and Results remain closed. Results eligibility remains `FALSE`.
