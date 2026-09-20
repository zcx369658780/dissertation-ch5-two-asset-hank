# Chapter 5 两资产 HANK 当前状态

更新：2026-09-20。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`RUN002_BEIJING_HJB_CONVERGENCE_ACCEPTED__TERMINAL_KFE_TOPOLOGY_SERIALIZATION_EXCEPTION_ACCEPTED__SERIALIZATION_AND_LEDGER_REPAIR_RUN003_ACTIVE`

Results eligibility=`FALSE`。

## Accepted scientific foundation

Still accepted:

- corrected D1/D2/D3 household law;
- same-checkpoint HJB convergence law `B<=1e-8 AND D<=1e-7`;
- source-free terminal KFE contract;
- stationary Ct/Lt/At/Bt/AtTax mapping;
- corrected aggregate adapter;
- Owner Option-B raw-ra0 payoff law;
- three-point and exact 31-payoff fixed-price one-step safety progression.

## Run001

Candidate `159786968d2bb47c12b0b7b88ed8aeaa6d0e8bdf` is accepted failed evidence.

Its checkpoint-0 diagnostic `NoneType` defect was repaired by run002 and is closed.

## Accepted run002 evidence

Candidate:

`2027b917390f00bdcc40757b1ab2031f3e24d201`.

Acceptance:

`docs/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_RUN002_TERMINAL_KFE_TOPOLOGY_SERIALIZATION_EXCEPTION_ACCEPTANCE_20260920.md`.

### Beijing HJB

Accepted under the exact turn-1 initial state:

- checkpoint: 12
- B: `1.292732587643286e-11`
- D: `1.2743897048750341e-08`
- policy/D2 maps: 13/13
- HJB updates: 12
- maximum solve backward error: `3.0832786979441453e-16`
- final Q SHA-256: `E1F55D0B755CB83D4F6A3CB4FEFD6DBC8CD4F05C6D23FC5DE00302E16B74BF20`.

Beijing HJB convergence is accepted.

### Terminal KFE

Exactly one SCC decomposition was actually consumed. Persistence then failed with:

`TypeError: Object of type csr_matrix is not JSON serializable`.

The topology result was not persisted. Therefore closed-class count, component membership, GESVD rank/nullity, stationary mass and Beijing KFE PASS/FAIL remain unclassified.

Run002 actual SCC=1 while its sealed global ledger says SCC=0; the discrepancy is accepted as an exception-path accumulation defect and is documented by the sealed post-terminal zero-science receipt.

Run002 manifest:

`D01A8A0CDF6808824735FEACABD7572249970DE97606A63BEA86209B5B6F531A`.

Independent readback passed; pre/post code freeze matched.

## Active successor

`tasks/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_TERMINAL_KFE_TOPOLOGY_SERIALIZATION_REPAIR_AND_RUN003_REEXECUTION_20260920.md`.

The successor is limited to:

1. explicit topology-specific JSON-safe receipt projection after the unchanged SCC calculation;
2. exception-path scientific-call ledger accumulation;
3. zero-science regression validation;
4. one fresh run003 under all existing scientific authorities.

No economic, HJB, KFE, solver, tolerance, calibration, K1A/C1 or payoff-law change is authorized.

Turn 2, K1B, K2, GE and Results remain closed.
