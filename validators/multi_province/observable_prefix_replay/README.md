# Original-parameter observable prefix: implementation/source map

This external observer calls the unchanged annual worker once. It is not a replacement household solver or controller. Exact task authority and run-specific identities are in `receipts/preflight.json` and `receipts/zero_entry_failure_receipt.json` in the delivered report directory.

| Original dispatch | Observation only | Scientific invariance |
|---|---|---|
| annual worker `run_online_stationary` callback | Capture full 31-state tuple/tKN before every batch | dataclass replacement changes only callback; all other fields retain identity |
| anchor `_source_initial_arrays` | Entry/counter/state/grid, actual recomputed phi, returned V0/l0 | original initializer exactly once with identical arguments |
| anchor `_source_labor_root` / `brentq` | attempted calls and scoped residual profiler | no residual recomputation, root/args/limits unchanged |
| original post-loop adapter | inject wrappers around its original default HJB/KFE callables | original aggregator and false-HJB-to-KFE branch unchanged |
| faithful HJB | record original full return before KFE | original object returned, no extra evaluator |
| original sparse `spsolve` dispatch | separate HJB/KFE attempts; save KFE M/RHS/raw return | same callable/args/result, no extra direct solve |
| runtime one-turn and subordinate capital/migration/wage/firm | exact operands/returns at source call order | delegate once, no substitute formula used in science |
| runtime diagnostics/adaptation | exact input/output/action records | original branch and action code executes unchanged |
| runtime state freeze at completed record | durable full completed record | original freeze result returned unchanged |

`Store` copies mutable arrays/state immediately, persists NPZ then JSON with exclusive creation and fsync, then appends hash-index receipt. The `Budget` counts entries before delegating and supplies only the authorized external prefix/time stop. Call725 return triggers an intentional stop before original worker continues to call726. The science try/finally saves exception/current phase/counters, including failed direct entries. Import bootstrap failures occur before Store/model entry and are separately receipted.

`run.py` imports frozen production from the detached LF `source_runtime` supplied via process-local `CH5_OBSERVATION_RUNTIME`. This addresses only raw-byte bootstrap identity; original Builder CRLF checkout and global Git configuration remain intact. The launch receipt hashes the observer sources actually used. No science restart is permitted.

`analyze.py`, `report.py`, and `finalize.py` are postprocessing only. They do not import production modules. Same-stage scalar reconstruction is labelled derived, never a captured branch or a model call. The CSV tables retain case-distinct source names (`it`/`It`); use a case-sensitive parser. `finalize.py` requires an ended process and terminal record, checks task ceilings and every capture hash, builds a finite manifest, and independently reopens each member.

Synthetic tests cover observation primitives, original adapter AST with fake HJB/KFE functions, entry budgets, immutable snapshots, boundary comparison, and first-mismatch prefix logic. They establish bounded delegation properties; the actual prefix comparison is the separate empirical fidelity evidence. They are not numerical validity or Results acceptance tests.
