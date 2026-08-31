# MP4B zero-science observability-helper initialization and trace-accounting audit

## Terminal verdict

MP4B_ZERO_SCIENCE_OBSERVABILITY_HELPER_INITIALIZATION_AUDIT_READY_FOR_OWNER_REAUTHORIZATION_REVIEW

This is a read-only zero-science observability-infrastructure result. It neither repairs the helper nor authorizes another MATLAB launcher.

Exact failed-assignment classification:

MP4B_OBS_HOUSEHOLD_INPUT_CONTAINER_INITIALIZATION_TYPE_MISMATCH_CONFIRMED

At MP4B_OBS.m:110, obs_empty_turn initializes household_inputs as [] (empty double). At line 19, household_inputs(i) receives the scalar struct returned by obs_household_input. Parenthesis indexing is correct for a struct array; the empty-double container is not. MATLAB therefore attempts the observed struct-to-double conversion before the first HANK_2ASSETS_HJB call.

Global classification:

MP4B_OBS_MULTIPLE_STATIC_SCHEMA_DEFECTS_LOCALIZED

The same defect pattern also appears in household_outputs, firm_inputs, firm_preclip, firm_outputs, and adaptation-path controller_actions. No other statically visible type/shape blocker was found in direct whole-field assignments.

## Live continuity and identities

- Repository: zcx369658780/dissertation-ch5-two-asset-hank.
- Task authority / starting HEAD / starting origin/main: 6fb0f5cb816162aef8185521dff1a8cc7e10e336.
- Required direct parent: 0dd1ab05ad5d7e6e923ab4d1f7ae8f998b66abcd.
- Fresh fetch and clean fast-forward established HEAD == origin/main, ahead/behind 0/0 before this report mutation.
- Read in full: AGENTS.md; all four named rules; this task; owner-reauthorized task/report; zero-science copy-binding remediation task/report; earlier blocked instrumented-run task/report.

All specified predecessor evidence hashes passed read-only verification: source-copy manifest 757D83D13B32BC92411F687069797A0F3DA4ADFC06FFEBD872B0674DBEDE9961; instrumentation manifest 511F59C6F6482DC5BBA7EBBFAD5B234C7D31B840AB2DE2CDDC836F4B74A52B2B; instrumentation diff 0B4B4D78EF45E33052E0888CC0E4AD8703167DC71DD8FA0D79BD01B5A053BB9F; pre-science gate CFA0EE14410F44C9E56D8977D4F1363590CB8AC70E392F62E8CD47404EEF753D; command 9F6E9A73CE4DECE261B390567DBD3EEC1BA287502D29D0C9FFB260DD31AB90D0; invocation binding 50614001EF125A035EB78EB9C796BF3BFEEC6E0017A4206FCBA01402FF63A3F2; trace MAT E3EC398D6B2A5284A07941D74C4DA6FB5C460BC61D373A860C7D024CD86C7EAF; terminal B36EA498862231AF914B9922B1A9581E405EFAE05893BEF8CE4D459B8F1BA5D9; trace summary F15DBA7B9FF42C7F2169CD7850543FB1DEDDDFE85640BCCFE7D49A2AD7CEE90C; stdout/stderr 40C4EFDC4091569931CA49827AC60AB131BCD424AF69AB54A9772C7B8F7C55E6; run manifest AE078A56AF7FA22F87049A037E9151C9D8BEC76153659946AA937C26F82D215E.

The immutable candidate wrapper and scientific body remained DA998FB04C35EE852F53A504D5F4EB17EC089A8EC616A082F38E2B5CB2CD5A93 and 80BAEDE65829F6A1215638F556544C92CAAB203A149FA6D1D88196BE22045F45.

## Complete observer event schema

| Operation | Source call site | Destination / intended value | Initializer and indexing | Static result |
| --- | --- | --- | --- | --- |
| init | wrapper:46 | global state / 0x1 turns struct | whole struct | compatible |
| turn_entry | HANK_mp_1eq:8 | turns(j).turn, entry 1x31 struct | turns indexed; entry direct replacement | compatible |
| household_input | HANK_mp_1turn:15 | household_inputs(i) scalar struct | [] double then () struct assignment | necessarily fails |
| household_output | HANK_mp_1turn:17 | household_outputs(i) scalar struct | [] double then () struct assignment | latent necessary failure |
| household_batch | HANK_mp_1turn:19 | convergence struct with 1x31 numeric flags | direct whole field | compatible |
| migration | HANK_mp_1turn:31 | 1x31 migration structs | direct whole field | compatible |
| capital | HANK_mp_1turn:46 | aggregate plus 1x31 province structs | direct whole field | compatible |
| firm_input | HANK_mp_1turn:51 | firm_inputs(i) scalar struct | [] double then () struct assignment | latent necessary failure |
| firm_preclip | HANK_firm:57 | firm_preclip(current_province) struct | [] double then () struct assignment | latent necessary failure |
| firm_output | HANK_mp_1turn:53 | firm_outputs(i) scalar struct | [] double then () struct assignment | latent necessary failure |
| composite_wage | HANK_mp_1turn:61 | 1x31 wage structs | direct whole field | compatible |
| policy | HANK_mp_1turn:75 | policy aggregate plus 1x31 structs | direct whole field | compatible |
| controller_pre | HANK_mp_1eq:38 | aggregate controller struct | direct whole field | compatible |
| controller_action | HANK_mp_1eq:70 | controller_actions(i) scalar struct | [] double then () struct assignment | latent necessary failure when eligible |
| controller_no_adaptation | HANK_mp_1eq:73 | 1x31 synthesized NONE snapshots | direct whole field | compatible; not branch-body events |
| controller_terminal | HANK_mp_1eq:47 | 0x1 terminal-marker struct | direct whole field | compatible |
| damping | HANK_mp_1eq:78 | 1x31 double; action tKNratio_after | direct and prior typed struct array | compatible after action container fix |
| get | wrapper:61,73 | whole global trace | return | compatible |
| summary | wrapper:62,74; helper:157-179 | scalar summary | local numeric counters / recorded events | household counter semantic defect |

For every per-province operation, the intended turn is current_turn and the intended province is i. All those fields can repeat once per source stage and province. A missing event is not a zero value: typed empty containers must remain distinguishable from a recorded zero/false result. Full arguments, field schemas, shapes, and repeated-event semantics are preserved in the external event-schema JSON.

## Initializer/assignment matrix and latent sweep

| Trace field | Initializer | Assignment | Type/shape outcome |
| --- | --- | --- | --- |
| turns | 0x1 struct | turns(j)=empty-turn struct | compatible |
| entry | [] double | direct 1x31 struct replacement | compatible |
| household_inputs | [] double | indexed scalar struct | incompatible; observed failure |
| household_outputs | [] double | indexed scalar struct | incompatible |
| household_convergence | [] double | direct scalar struct | compatible |
| migration | [] double | direct 1x31 struct | compatible |
| capital | [] double | direct scalar aggregate struct | compatible |
| firm_inputs | [] double | indexed scalar struct | incompatible |
| firm_preclip | [] double | indexed scalar struct | incompatible |
| firm_outputs | [] double | indexed scalar struct | incompatible |
| composite_wage | [] double | direct 1x31 struct | compatible |
| policy | [] double | direct scalar struct | compatible |
| controller | [] double | direct scalar struct | compatible |
| controller_actions via action | [] double | indexed scalar struct | incompatible |
| controller_actions via no-adaptation/terminal | [] double | direct struct array | compatible |
| damping | [] double | direct 1x31 double | compatible |
| current_turn/current_province | scalar double zero | scalar index assignment | compatible |
| summary locals | scalar double zero | formula/recorded-event aggregation | type-compatible; one semantic defect |

firm_preclip depends on current_province set by the immediately preceding firm_input call. The copied call order establishes that dependency without a separate index mismatch once firm_inputs is typed. household_batch flags are numeric: HANK_2ASSETS_HJB assigns convergent as numeric 0/1, so no coercion defect is present.

## Trace accounting

MP4B_OBS_ALLOCATION_DERIVED_HOUSEHOLD_CALL_COUNT_SEMANTIC_DEFECT_CONFIRMED

Helper line 178 defines household_call_count as numel(trace.turns)*31. It counts scheduled/inferred slots after a turn_entry, not attempted, entered, or completed HJB calls. Thus the partial trace reports 31 while controlling stack evidence proves completed household/HJB calls equal 0. The wrapper propagates the same derived counter on both success and exception paths.

outer_turn_count is an observed turn_entry count. terminal_turn requires a stored controller predicate. Adaptation eligibility and low/high/Zt counts are event-derived only if controller_action was reached. controller_no_adaptation generates state snapshots labelled NONE; these are not source branch-body action events.

The frozen specification-only future contract requires: scheduled_household_slots; household_call_entries; household_call_completions; firm_call_entries; firm_call_completions; controller_evaluations; low_action_events; high_action_events; and zt_reset_events. Scientific ledgers must use completion counters and never allocation size.

## Partial-trace evidence boundary

OBSERVED_EVENT: init; turn-1 entry; trace.current_turn=1; trace.current_province=0; turns(1).turn; and the 1x31 entry projection.

PREALLOCATED_OR_INFERRED_SLOT: household_inputs, household_outputs, household_convergence, migration, capital, firm_inputs, firm_preclip, firm_outputs, composite_wage, policy, controller, controller_actions, and damping. HDF5 metadata retains these as default empty-double fields; they are not scientific events.

Never reached: first HANK_2ASSETS_HJB, household output/batch, migration, capital, firm, wage, policy, controller, and all controller actions. This partial trace cannot support MATLAB/Python parity, chronology, controller divergence, or model-fault attribution.

## Minimal remediation specification

A future review may consider only an observability-only helper proposal that:

1. Types the six indexed per-province destinations as empty struct arrays with fields matching their current producer structs, preserving current i indexing and province order.
2. Keeps direct whole-field assignments only where their current direct type/shape compatibility holds.
3. Keeps absence distinct from recorded zero/false data and never synthesizes completed calls from slot capacity.
4. Adds the distinct event-derived entry/completion counters above and removes the allocation-derived household count from scientific execution ledgers.
5. Changes no scientific state, equation, calibration, grid, tolerance, controller branch, update order, call graph, or persistence frequency; it adds no retry or model call.

This is prose/specification only. No repaired helper, wrapper, or MATLAB execution was created.

## External audit artifacts

Audit root: D:\ProjectTemp\ch5-mp4b-observability-helper-initialization-audit-20260831-001

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| observer_event_schema.json | 10953 | 9BFC25A3C1F61CBD6825E3098A70C90A1466B5B07E691761B93F6AA953F81463 |
| observer_initializer_assignment_matrix.json | 5231 | DFE9146A4BE23CD5DD11970D62ED4C1313B88C290717C8E6E060033CCAC0061D |
| trace_accounting_semantics.json | 1946 | 4746EFDEA69C2CDFB44527F7BF10D114C6F281361191AE45723632A04F546340 |
| partial_trace_evidence_boundary.json | 1150 | 37780E69217CF34D16B3AA8D536AAD3723CA4BDE6A42C2DD5A843A3A7CA00844 |
| minimal_remediation_specification.md | 2248 | E9CBD7DEA49AFA98D1DAA6AD9027257494499E0D7B2C58DB52C69DA0420AEDB4 |
| audit_manifest.json | 2078 | 06C0723A0386D6539807ACC530B98A5C87CFF9743688A01E5447C7DE0B63F35E |

## Zero-science and closeout boundary

All current-task call counts are zero: MATLAB process/stationary/HJB/KFE/household/firm/controller/checkcode; Python stationary/HJB/KFE/household/MP2/MP3; comparator; Zhejiang/Shanxi replay; other year/batch; shocks/AR1; transition/dynamics/IRF; R5; and Results. HDF5 metadata inspection invoked no MATLAB or scientific module.

No predecessor source, helper, wrapper, remediation package, protected MATLAB, scientific module, comparator, test, contract, canonical data, rule, task, or prior report changed. The only repository change is this report. git diff --check and explicit-path closeout are performed with it.

Exactly one recommended next gate:

OWNER_REVIEW_OF_BOUNDED_OBSERVABILITY_HELPER_REMEDIATION_WARRANTED

This is not authorization to repair or rerun MATLAB.

