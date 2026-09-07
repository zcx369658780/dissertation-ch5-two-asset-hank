# MP4C provincial price boundaries and adaptive-controller audit

Date: 2026-09-08
Repository: zcx369658780/dissertation-ch5-two-asset-hank
Issuer: ChatGPT Reviewer, under the Owner's explicit request to inspect provincial rah/wjt boundary contact before further diagnosis.
Publication baseline: da543d7960451da5b2ed9f67dae906269d45b273; record fresh origin/main at execution.

## 1. Complete work unit and decision boundary

Using protected source and ALREADY-PERSISTED states/logs, determine which provinces have high/low raw firm returns or wages, which are clipped or exactly at bounds, what prices actually reached households, and whether the original adaptive mechanism acted before the corrected-2018 Anhui call-725 failure. Compare the failed path with available successful annual endpoints, preserving each dataset and run identity.

Complete source mapping, a read-only evidence extractor, relevant synthetic tests, saved-state arithmetic, provincial tables, diagnosis, and publication in this ONE task. Routine path/schema/encoding/serialization/report repairs remain inside scope.

Owner direction: retain the original algorithm, a_bar and other calibration/numerics. The prior D1-D3 boundary/generator/FOC target is NOT adopted and is deferred. Its accepted findings remain evidence, not an implementation authorization. Its non-adoption is not a blocker for this audit and requires no renewed Owner confirmation.

This task is a diagnostic, not a rate experiment. Do NOT change ramax to .07/.065, reset rah, modify GovInv/Zt, alter capital/portfolio weights, or implement the deferred target. A high-price association cannot by itself establish the cause of nonconvergence or erase known operator defects.

## 2. Workspace, source identities and required reading

Use the existing Chapter-5 worktree when clean and suitable:
D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001
Suggested new branch: codex/ch5-province-price-boundary-audit-20260908.
Verify remote and fetch. Preserve other branches, the original D:\ResearchCode\dissertation-ch5-two-asset-hank checkout and its reported 70 untracked files. No reset/clean/stash/force-push. Use an isolated worktree only if needed. Zotero and deep-learning-hank are not work targets.

Read AGENTS, rule index, current status, this task, relevant workflow/local-safety and MATLAB/Python rules, then:
- docs/CH5_MP4C_PRICE_BOUNDARY_SOURCE_REVIEW_20260908.md (Reviewer actually inspected the uploaded archive; source-line map and hash evidence).
- src/ch5_two_asset_hank/multi_province/{firm,capital_allocation,one_turn,steady_state,stationary_runtime}.py and the annual/input/persistence adapters actually identified by the relevant run manifests.
- docs/CH5_TWO_ASSET_HANK_MP4C_OWNER_A_2009_2022_CORRECTED_8WORKER_ANNUAL_STATIONARY_REPORT.md
- docs/CH5_TWO_ASSET_HANK_MP4C_2018_OBSERVABILITY_REPAIR_SINGLE_RETRY_AND_2009_2022_COMPOSITE_ACCEPTANCE_REPORT.md
- docs/CH5_TWO_ASSET_HANK_MP4C_L3_FORMAL_2009_2023_ANNUAL_STATIONARY_COVERAGE_ACCEPTANCE_REPORT.md
- the existing call-725 input-capture/termination evidence reports and manifests needed to locate the original outer-loop state. First-iteration closure and multi-iteration reports supply frozen household inputs, NOT an outer-loop replay authorization.
Do not re-audit the entire historical gate chain.

Protected source root: D:\MatlabProgram\2023年12月2日 多省份神经网络HANK (C:\MatlabProgram is the previously certified logical alias). Read, never overwrite. Check relevant identities once; reuse unchanged certified mappings.
The Owner-uploaded 多省份HANK_matlab原版程序.zip has SHA256 CEB94CCF34D2D218722B81E5111A8F4C530571A9F886BD4AFE0610A00321F755. Its 32 .m entries match the prior MP0 inventory hashes; its calibration MAT matches 923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A. It contains no annual st files. The ChatGPT attachment path is not assumed to exist on Windows: use the hash-matched protected local files, without requiring another upload or copying the archive into Git.
Protected HJB SHA256: 049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE.
Frozen Python export blob: 9e7dc9556a2b76811e78f89999abecc045886106.
Call-725 scalar binding SHA256: A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6; authoritative initialization MAT SHA256: 1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81. Reuse the certified bindings; do not load large household arrays unless actually needed.
Do not confuse the archive calibration cache with the later Owner-A corrected-input source or replace one with the other.

## 3. Source contract to audit

Trace the actual executed chain, with file/line and runtime manifest attribution:
1. multi_prov_HANK_12sts.m configuration, annual-cache bypass, and mpHANK_equilibrium_2000 initialization.
2. Firm raw ra0/wt0 -> source clipping and associated Corptax adjustment -> stored ra/wjt.
3. Old-state firm ra and inter_prv_ratio -> household rah; firm wjt and migration/preference inputs -> composite household w.
4. Complete turn -> convergence decision -> conditional Zt/GovInv adaptation -> next-turn household inputs.

Important source observations to independently map, not repair:
- Active firm bounds are ra=[.02,.09], wjt=[.8,1.3] in the entry file. Read each run's effective bounds and identify any cache/runtime override; commented .065/.01/1 are not active values.
- These clips apply to ra and wjt, NOT directly to rah or composite w. A rah comparison against firm bounds is a descriptive reference, not automatically a violated native constraint. Preserve the literal portfolio weights, report their row sums/implied range where useful; do not silently normalize them. Composite w=16.82014806560587 is not comparable to the firm-wage upper bound 1.3.
- Initialization sets ra=rah=.09 and wjt=.6. Label initialization separately: initial wjt below .8 is not proof that a completed firm clip failed.
- rah is assembled BEFORE the new firm evaluation, using carried old ra. Household calls consume the copied old-turn states. Record this lag explicitly; do not compare stored rah with same-snapshot post-firm ra as though contemporaneous.
- HANK_mp_1eq adaptation requires maxKNratiogap<.1 AND steady_state==1, after a complete turn and unless the convergence branch has already terminated. When active, abs(Yt/Yt0-1)>.01 triggers Zt reset; ra<ramin+.02 triggers GovInv*.9; ra>ramax-.02 triggers GovInv*1.1. With entry bounds those thresholds are approximately .04/.07; retain the actual source expressions/strict inequalities and binary64 values.
- The global maximum can be determined by a DIFFERENT province from the high-ra province. A thrown household/KFE error may prevent the turn and subsequent adaptation from completing. Distinguish an exception from a nonconverged household flag returned normally.
- Final source acceptance excludes ra touching either bound, but does not include wage-bound counts in its final predicate. Do not change that predicate. Do not add a rah>.07 condition to the source controller.

## 4. Evidence acquisition without new model calls

Priority A: corrected-2018 failed path. Recover all available 31-province common-old-state snapshots and completed outer-turn records leading to outer iteration 24/call 725, plus the exact Anhui call input. Locate through existing report/manifest paths and bounded repository/source-root inventories, not an all-drive search. Relevant known roots include:
- D:\ProjectTemp\ch5-mp4c-owner-a-corrected-2009-2022-8worker-20260902-001
- D:\ProjectTemp\ch5-mp4c-owner-a-2018-observable-single-retry-20260903-002
- the call-725 input-capture and termination evidence linked by current reports.

For each recovered snapshot identify run, calendar year, input regime, outer iteration, province order, capture phase, precision, and whether it is before/after firm evaluation/adaptation. Identify the actual run which captured call 725; do not splice histories from separate retries/replays. Later single-household HJB iterations 1..500 are NOT outer iterations or new provincial price observations.

Priority B: compare terminal states for the existing Owner-A 13 PASS years (2009-2017 and 2019-2022) with available failed-2018 states. Keep the absent 2018 terminal explicit. Priority C: inspect the accepted original-runtime-cache Python 2009-2023 endpoints as a SEPARATE 15-year regime. Read existing native MATLAB annual st snapshots if manifest-located; label their lineage separately from Python endpoints. This is saved-file extraction, never an annual recomputation.

Use small persisted summaries first; targeted MAT/HDF5 field reads next. Do not load full g/V panels merely to obtain provincial scalar states. Hash consumed material evidence, recording the existing provenance caveats rather than pretending retrospective checks prove capture-time identity. The zip's calibration MAT is not a substitute for a missing 2018 path or terminal state.

Missing fields are an evidence result. Publish all available provinces and a 31-province roster with explicit missing fields/coverage. A source initialization or a final endpoint cannot establish intervening touch duration. Count-only or rounded logs do not establish exact per-province binary64 contacts. Do not invent names/values or extend the trajectory past failure to fill a table. This task has NO conditional fresh-run budget.

## 5. Required diagnostic outputs

### A. Provincial boundary panel
For each available run/year/outer-step/phase/province record both 0-based and MATLAB 1-based indices and:
- ra0, clipped ra, household rah, wt0, clipped wjt, composite w;
- effective ramin/ramax/wjtmin/wjtmax and their source;
- lower/upper distances, raw strict excursions, exact contacts, clipped amount where identifiable, finite status and availability/provenance;
- captured vs derived vs rounded-log vs missing, and native constraint vs descriptive comparison.

Compare raw values to bounds with exact source <,>,== semantics. An exact contact without raw evidence does not prove clipping rather than an exactly-equal raw value. For full-precision values, add a separate near-boundary diagnostic abs(x-bound)<=128*eps64*max(1,abs(x),abs(bound)); it does NOT replace strict flags, excuse outside values, or change the convergence criterion. Report outside-by-roundoff and near-inside separately. Rounded logs must be labelled uncertain at this scale. NaN/Inf/missing never count as interior/pass.

Give 31-province tables and compact annual/iteration counts with observed denominators; list raw excursions separately from clip contacts. Summaries must not double-count the same observation copied into several artifacts. For each province with enough consecutive path coverage, report first/last contact, observed frequency and longest confirmed consecutive spell, clearly separating initialized contact from later contacts. Missing steps break confirmed spells. Also report rah relative to the Owner's approximately .07 recollection descriptively, not as a newly certified safe cutoff.

### B. Controller timeline and failure linkage
At every available complete step: maxKNratiogap and its province, maxYtgap, steady_state, whether convergence exited first, whether the adaptive block was reached/enabled, ra trigger and actual Zt/GovInv before/after. Compare expected action from the literal source condition with captured action; distinguish CAPTURED_ACTION, DERIVED_EXPECTATION and UNOBSERVED_ACTION.
For Anhui call 725, trace the last price-producing stages and any lagged ra/portfolio inputs to rah=.09. Show whether updates were absent because the global gate was closed, occurred but remained insufficient, were pending because the failure interrupted a turn, or cannot be determined. Do not claim the cause without the relevant records.

### C. Upstream price decomposition
For flagged provinces and same-regime controls, extract available alpha, Zt_init, Zt_used, Zt_after_adaptation, Yt/Yt0, Kt0, Kt_supply, GovInv_used, GovInv_after, Kt, Lt_supply, N, mt, rk, divrate, inter_prv_ratio, and source-defined capital components. Never replace productive At*N by At+Bt, or firm Lt_supply by household labor. Do not silently add a retained-local-capital term absent from the actual source or change portfolio ratio placement.
Prefer captured ra0/wt0 (Python FirmResult persists both). If absent, reconstruct only when all same-stage operands exist, using the original source expressions, original profit floor and tax/depreciation terms; mark reconstructed values. A post-adaptation Zt/GovInv cannot stand in for the values used to produce earlier Yt/prices. A consistent algebraic identity using saved Yt/Kt/Lt may be reported as derived, not falsely called runtime capture. Preserve any mismatch with stored raw/capped values under the unchanged 128-eps comparison; don't coerce it away.
This is descriptive attribution: distinguish high Zt, high Y/K, small capital denominator, marginal-cost movement, portfolio transmission, unit/index discrepancies and missing evidence. GDP/POP/CAP scaling and year/vintage must come from the consumed regime's manifest. Do not rerun PLM, recalibrate data or infer a causal decomposition from unlike years/regimes. Owner hypotheses remain hypotheses unless evidence discriminates them.

## 6. Allowed implementation, checks, resources and exclusions

Allowed writes only:
- validators/multi_province/price_boundary_audit/
- tests/test_mp4c_price_boundary_audit.py
- reports/province_price_boundary_audit_20260908/ (small JSON/CSV/Markdown and relevant test log)
- docs/CH5_MP4C_PROVINCE_PRICE_BOUNDARY_AND_ADAPTATION_AUDIT_REPORT.md

External no-overwrite root: D:\ProjectTemp\ch5-province-price-boundary-audit-20260908-001 (choose unused suffix if occupied). Preserve source files, all previous outputs, failures and annual caches. Do not upload the archive, private workbooks, calibration MAT or large state arrays to Git. Publicizable model-state scalar diagnostics may be committed within the report paths, consistently with prior evidence practice.

Allowed: read-only source/JSON/CSV/MAT/HDF5 ingestion, scalar algebra on saved operands, summarization, source-expression comparison and synthetic extractor/classifier tests. Build a standalone inspector with no import-time scientific execution. Do not call load_GDPdata, annual entry points, online/manual one-turn/controller runners, HJB/KFE, initialization/labor-root solvers or any direct/iterative solver to manufacture evidence. No native MATLAB startup is needed or authorized.
Budget: NEW household/HJB/KFE/linear-or-root solves/one-turn/GE/annual/R-PLM/shock/IRF/Results calls = 0; scientific retries = 0. Ordinary source reads, deterministic saved-scalar arithmetic and synthetic IO tests may repeat within scope; record them separately. Time budget <=3 hours. Stop optional expansion when the core question and remaining evidence gap are clear, not because every historical directory has not been hashed.

Test changed behavior only: exact/near/strict-outside classification; init vs post-firm separation; ra vs rah and wjt vs w; lag/phase handling; original controller threshold sides and global gate; missing/rounded/nonfinite handling; no model import/call side effects. No broad scientific regression run or tolerance tuning. A source mismatch blocks only dependent inference, not preservation/reporting of valid material.

## 7. Delivery and publication

One report with: source map, evidence coverage/provenance, 31-province failed-path tables, separated annual panels, adaptation timeline, raw-price decomposition, actual ledger, focused tests, clear limitations and a concrete next diagnostic recommendation. Use one finite manifest excluding itself and its final readback receipt. Emit a compact summary JSON for review.
Separate completion from findings:
- diagnostic_completion: COMPLETE or PARTIAL_EVIDENCE;
- boundary_findings: actual observed excursions/contacts or NONE_OBSERVED over explicitly stated coverage (never universal NONE when records are missing);
- high_rah_root_cause: SUPPORTED_LINK / NOT_ESTABLISHED / EVIDENCE_MISSING, with precise scope; no convergence-causality claim from correlation alone.
Retain Results eligibility=FALSE and original numerical algorithm unchanged.

Stage explicit allowed paths, commit and non-force push the dedicated branch, verify remote SHA once. Builder does not merge main or announce independent Reviewer acceptance. Return report path, branch/SHA, coverage counts, most important flagged provinces, controller findings, all new scientific-call counts=0 if true, and what remains unknown. Do not execute a suggested rah sensitivity test or resume 2018 in this task.
