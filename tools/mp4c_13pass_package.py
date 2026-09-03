"""Read-only MP4C 13-pass package builder; never invokes a scientific routine."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import os
import shutil
import statistics
import zipfile
from pathlib import Path

PASS_YEARS = (*range(2009, 2018), *range(2019, 2023))
FIELDS = ("Ct", "At", "Bt", "Lt", "Lt_supply", "Kt_supply", "rah", "Kt", "Yt", "mt", "KNratio", "w", "wjt", "rk", "ra", "GovInv", "rb", "it", "Zt", "Govinc")
WIDE_FIELDS = ("Yt", "Kt", "Lt", "Ct", "At", "Bt", "ra", "rah", "rb", "w", "wjt", "Zt", "GovInv", "Govinc")
ROOT = Path(os.environ.get("MP4C_PACKAGE_ROOT", r"D:\ProjectTemp\ch5-mp4c-manual-steady-state-comparison-package-20260903-001"))
ORIGINAL = Path(r"D:\ProjectTemp\ch5-mp4c-owner-a-corrected-2009-2022-8worker-20260902-001")
DIAGNOSTIC = Path(r"D:\ProjectTemp\ch5-mp4c-13pass-matlab-comparator-2018-diagnostic-20260903-001")
RETRY = Path(r"D:\ProjectTemp\ch5-mp4c-owner-a-2018-observable-single-retry-20260903-002")
MATLAB = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK_DIAGNOSTIC_PATCH_2026_06_23\12年稳态值.xlsx")
LABEL = "LEGACY_CALENDAR_BINDING_DIAGNOSTIC_ONLY__NOT_SAME_INPUT_PARITY_EVIDENCE"


def sha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n"
    if path.exists():
        if path.read_bytes() != text.encode("utf-8"): raise FileExistsError(path)
        return
    path.write_text(text, encoding="utf-8", newline="\n")


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    handle = io.StringIO(newline="")
    with handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="raise")
        writer.writeheader()
        writer.writerows(rows)
        text = handle.getvalue()
    if path.exists():
        if path.read_bytes() != text.encode("utf-8"): raise FileExistsError(path)
        return
    path.write_text(text, encoding="utf-8", newline="")


def write_text_no_overwrite(path: Path, text: str) -> None:
    if path.exists():
        if path.read_text(encoding="utf-8") != text: raise FileExistsError(path)
        return
    path.write_text(text, encoding="utf-8", newline="\n")


def copy_record(src: Path, dest: Path, *, year: int | str, kind: str, records: list[dict], source_root: Path, representation: str = "N/A", semantic_indices: dict | None = None, status: str = "N/A") -> None:
    if not src.exists():
        raise FileNotFoundError(src)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        if sha(dest) != sha(src):
            raise FileExistsError(dest)
    else:
        shutil.copy2(src, dest)
    records.append({"zip_path": str(dest.relative_to(ROOT)).replace("\\", "/"), "source_absolute_path": str(src), "filename": src.name,
                    "year": year, "artifact_type": kind, "source_batch_root": str(source_root), "representation": representation,
                    "rolling_window_entry_index": (semantic_indices or {}).get("rolling_window_entry_index", "N/A"),
                    "regression_vintage_index": (semantic_indices or {}).get("regression_vintage_index", "N/A"),
                    "calendar_level_row_index": (semantic_indices or {}).get("calendar_level_row_index", "N/A"), "status": status,
                    "sha256": sha(dest), "bytes": dest.stat().st_size, "copied": True})


def input_rows(year: int, data: dict, input_sha: str) -> list[dict]:
    binding = data["binding"]
    vectors, derived = data["vectors"], data["derived"]
    rows = []
    for i, province in enumerate(data["province_order"]):
        row = {"year": year, "province": province, "province_index": i + 1, "GDP": vectors["GDP"][i], "CAP": vectors["CAP"][i],
               "POP": vectors["POP"][i], "log_pgdp": vectors["log_pgdp"][i], "log_pcap": vectors["log_pcap"][i],
               "IND_alpha": vectors["IND_alpha"][i], "IND_Zt": vectors["IND_Zt"][i],
               "inter_province_asset_ratio": derived["inter_province_asset_ratio"][i], "runtime_input_sha256": input_sha,
               "rolling_window_entry_index": binding["rolling_window_entry_index"], "regression_vintage_index": binding["regression_vintage_index"],
               "calendar_level_row_index": binding["calendar_level_row_index"], "source_hashes_json": json.dumps(data["source_hashes"], ensure_ascii=False, sort_keys=True),
               "representation": data["representation"]}
        rows.append(row)
    return rows


def prepare() -> None:
    if ROOT.exists():
        raise FileExistsError(f"fresh no-overwrite root already exists: {ROOT}")
    ROOT.mkdir(parents=True)
    records: list[dict] = []
    final_rows, level_rows, wide = [], [], {field: {} for field in WIDE_FIELDS}
    provenance = {"schema": "CH5_MP4C_13PASS_PACKAGE_CONTEXT_V1", "pass_years": list(PASS_YEARS), "original_root": str(ORIGINAL),
                  "diagnostic_root": str(DIAGNOSTIC), "retry_root": str(RETRY), "matlab_workbook": {"path": str(MATLAB), "sha256": sha(MATLAB), "bytes": MATLAB.stat().st_size},
                  "legacy_label": LABEL}
    for year in PASS_YEARS:
        source = ORIGINAL / f"year_{year}"
        inp = source / f"calendar_{year}_matlab_runtime_cache_input.json"
        final = source / "final_steady_state.json"
        value, canonical = read_json(final), read_json(inp)
        input_hash = sha(inp)
        for name, kind in ((final, "final_steady_state"), (inp, "corrected_runtime_input"), (source / "SUCCESS.json", "success_receipt"),
                           (source / "run_manifest.json", "run_manifest"), (source / "checkpoint_manifest.json", "checkpoint_manifest"), (source / "year_timing.json", "year_timing")):
            copy_record(name, ROOT / "python_source" / f"year_{year}" / name.name, year=year, kind=kind, records=records, source_root=ORIGINAL,
                        representation=canonical["representation"], semantic_indices=canonical["binding"], status=value["status"])
        rows = value["final_31x20"]
        if len(rows) != 31:
            raise ValueError(f"year {year}: expected 31 terminal rows")
        if canonical["province_order"] != [row["name"] for row in rows]:
            raise ValueError(f"year {year}: province order mismatch")
        for row in rows:
            output = {"year": year, "province": row["name"]}
            for field in FIELDS:
                v = float(row[field])
                if not math.isfinite(v):
                    raise ValueError(f"year {year} {row['name']}: nonfinite {field}")
                output[field] = v
            output.update({"runtime_input_sha256": input_hash, "rolling_window_entry_index": canonical["binding"]["rolling_window_entry_index"],
                           "regression_vintage_index": canonical["binding"]["regression_vintage_index"], "calendar_level_row_index": canonical["binding"]["calendar_level_row_index"],
                           "representation": canonical["representation"]})
            final_rows.append(output)
            for field in WIDE_FIELDS:
                wide[field].setdefault(row["name"], {})[year] = output[field]
        level_rows.extend(input_rows(year, canonical, input_hash))
    if len(final_rows) != 403 or len(level_rows) != 403:
        raise AssertionError("13 years x 31 provinces must be 403")
    final_header = ["year", "province", *FIELDS, "runtime_input_sha256", "rolling_window_entry_index", "regression_vintage_index", "calendar_level_row_index", "representation"]
    level_header = ["year", "province", "province_index", "GDP", "CAP", "POP", "log_pgdp", "log_pcap", "IND_alpha", "IND_Zt", "inter_province_asset_ratio", "runtime_input_sha256", "rolling_window_entry_index", "regression_vintage_index", "calendar_level_row_index", "source_hashes_json", "representation"]
    write_csv(ROOT / "python_owner_a_steady_state_2009_2022_13pass_long.csv", final_rows, final_header)
    write_csv(ROOT / "python_owner_a_input_levels_2009_2022_13pass_long.csv", level_rows, level_header)
    dump(ROOT / "workbook_context.json", {"years": list(PASS_YEARS), "fields": list(WIDE_FIELDS), "wide": wide, "province_order": [r["province"] for r in final_rows[:31]], "legacy_label": LABEL})
    dump(ROOT / "package_context.json", {"provenance": provenance, "final_rows": final_rows, "level_rows": level_rows, "records": records})


def corr(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) < 2 or len(set(xs)) < 2 or len(set(ys)) < 2: return None
    mx, my = statistics.fmean(xs), statistics.fmean(ys)
    denom = math.sqrt(sum((x-mx)**2 for x in xs) * sum((y-my)**2 for y in ys))
    return None if denom == 0 else sum((x-mx)*(y-my) for x,y in zip(xs,ys)) / denom


def ranks(values: list[float]) -> list[float]:
    ranked = sorted(enumerate(values), key=lambda t:t[1]); result=[0.0]*len(values); i=0
    while i < len(ranked):
        j=i
        while j+1 < len(ranked) and ranked[j+1][1] == ranked[i][1]: j += 1
        rank=(i+j+2)/2
        for k in range(i,j+1): result[ranked[k][0]]=rank
        i=j+1
    return result


def neighbor_rows() -> list[dict]:
    by_year = {}
    for year in (2017, 2018, 2019):
        path = ORIGINAL / f"year_{year}" / f"calendar_{year}_matlab_runtime_cache_input.json"
        data = read_json(path); by_year[year] = (data, sha(path))
    fields = ("GDP", "CAP", "POP", "log_pgdp", "log_pcap", "IND_alpha", "IND_Zt", "inter_province_asset_ratio")
    result=[]
    for i, province in enumerate(by_year[2018][0]["province_order"]):
        for field in fields:
            values=[]
            for year in (2017,2018,2019):
                data=by_year[year][0]
                values.append((data["vectors"].get(field) or data["derived"].get(field))[i])
            d17, d19 = values[1]-values[0], values[2]-values[1]
            denom=max(abs(values[0]), abs(values[1]), abs(values[2]), 1e-300)
            result.append({"province":province,"province_index":i+1,"field":field,"value_2017":values[0],"value_2018":values[1],"value_2019":values[2],
                           "delta_2018_minus_2017":d17,"delta_2019_minus_2018":d19,"max_abs_relative_step":max(abs(d17),abs(d19))/denom,
                           "objective_flag":"NUMERIC_STEP_RECORDED__NOT_CAUSAL_INFERENCE","input_sha256_2017":by_year[2017][1],"input_sha256_2018":by_year[2018][1],"input_sha256_2019":by_year[2019][1]})
    return result


def failure_material(records: list[dict]) -> None:
    source_2018 = ORIGINAL / "year_2018" / "calendar_2018_matlab_runtime_cache_input.json"
    binding = read_json(source_2018)["binding"]
    copies = [(source_2018, ROOT / "failure_2018" / "original" / source_2018.name, "original_failed_input"),
              (RETRY / "calendar_2018_matlab_runtime_cache_input.json", ROOT / "failure_2018" / "retry" / "calendar_2018_matlab_runtime_cache_input.json", "retry_input"),
              (RETRY / "retry_2018_execution_receipt.json", ROOT / "failure_2018" / "retry" / "retry_2018_execution_receipt.json", "retry_execution_receipt"),
              (RETRY / "retry_2018_stdout.log", ROOT / "failure_2018" / "retry" / "retry_2018_stdout.log", "retry_stdout"),
              (RETRY / "retry_2018_stderr.log", ROOT / "failure_2018" / "retry" / "retry_2018_stderr.log", "retry_stderr"),
              (RETRY / "year_2018" / "run_manifest.json", ROOT / "failure_2018" / "retry" / "run_manifest.json", "retry_run_manifest"),
              (ORIGINAL / "year_2018" / "run_manifest.json", ROOT / "failure_2018" / "original" / "run_manifest.json", "original_run_manifest")]
    for src,dest,kind in copies:
        copy_record(src,dest,year=2018,kind=kind,records=records,source_root=RETRY if src.is_relative_to(RETRY) else ORIGINAL,
                    representation="OWNER_A_2009_2022_VERIFIED_CHNCAPITALSTOCK_ROLLING_PLM_END_YEAR_CALENDAR_INPUT", semantic_indices=binding,
                    status="PROCESS_EXCEPTION_FAIL" if src.is_relative_to(RETRY) else "SHARED_FAIL")
    stderr = (RETRY / "retry_2018_stderr.log").read_text(encoding="utf-8")
    write_text_no_overwrite(ROOT / "failure_2018" / "exact_traceback_utf8.txt", stderr)
    records.append({"zip_path":"failure_2018/exact_traceback_utf8.txt", "source_absolute_path":str(RETRY / "retry_2018_stderr.log"), "filename":"exact_traceback_utf8.txt", "year":2018, "artifact_type":"exact_traceback", "source_batch_root":str(RETRY), "representation":"N/A", "rolling_window_entry_index":binding["rolling_window_entry_index"], "regression_vintage_index":binding["regression_vintage_index"], "calendar_level_row_index":binding["calendar_level_row_index"], "status":"PROCESS_EXCEPTION_FAIL", "sha256":sha(ROOT / "failure_2018" / "exact_traceback_utf8.txt"), "bytes":(ROOT / "failure_2018" / "exact_traceback_utf8.txt").stat().st_size, "copied":False})
    same = sha(source_2018) == sha(RETRY / "calendar_2018_matlab_runtime_cache_input.json")
    repo = Path(__file__).resolve().parents[1]
    for report in (
        repo / "docs/CH5_TWO_ASSET_HANK_MP4C_13PASS_MATLAB_COMPARATOR_AND_2018_FAILURE_ROOT_CAUSE_DIAGNOSTIC_REPORT.md",
        repo / "docs/CH5_TWO_ASSET_HANK_MP4C_2018_OBSERVABILITY_REPAIR_SINGLE_RETRY_AND_2009_2022_COMPOSITE_ACCEPTANCE_REPORT.md",
    ):
        copy_record(report, ROOT / "failure_2018" / "predecessor_reports" / report.name, year=2018, kind="predecessor_report", records=records, source_root=repo,
                    representation="N/A", semantic_indices=binding, status="PROCESS_EXCEPTION_FAIL")
    write_text_no_overwrite(ROOT / "2018_KFE_FAILURE_SUMMARY.md", f"""# 2018 KFE failure summary\n\nBoth attempts used the same Owner-A 2018 scientific input: `{sha(source_2018)}`. Byte-identical: `{same}`.\n\nThe first batch attempt lost the triggering exception through the scheduler observability defect. The sole observable retry captured `MatrixRankWarning: Matrix is exactly singular`, followed by `ValueError: faithful contaminated-row solve is non-finite`. This is a process exception, not ordinary convergence failure.\n\nNo scientific mutation or second retry is authorized.\n\nLocalization from preserved evidence: province, outer iteration, household call, and control state are `UNKNOWN_FROM_EXISTING_EVIDENCE`; no generator/matrix artifact was persisted in the failed original year directory.\n\nTraceback source chain: `exports/matlab_faithful_two_asset_ha.py:596-597` -> `validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py:37` -> `validators/multi_province/mp4c_python_annual_production.py:174,187` -> `src/ch5_two_asset_hank/multi_province/stationary_runtime.py:52`.\n""")


def finalize() -> None:
    context=read_json(ROOT / "package_context.json"); records=context["records"]; final_rows=context["final_rows"]
    extracted=read_json(ROOT / "matlab_extract.json")
    matlab_rows=extracted["rows"]
    py={(r["year"],r["province"]):r for r in final_rows}
    overlap=[]
    for row in matlab_rows:
        if row["year"] not in PASS_YEARS: continue
        for field in ("Yt","Kt","Lt"):
            m=row[field]; p=py[(row["year"],row["province"])][field]; diff=p-m; denom=max(abs(m),1e-300)
            overlap.append({"year":row["year"],"province":row["province"],"variable":field,"matlab_legacy_value":m,"python_owner_a_value":p,"raw_difference":diff,"absolute_difference":abs(diff),"relative_difference_abs_matlab_denominator":abs(diff)/denom,"python_to_matlab_ratio":p/m if m != 0 else "","semantic_label":"NOT_SAME_INPUT__DIAGNOSTIC_ONLY"})
    write_csv(ROOT / "matlab_python_legacy_overlap_diagnostic_13pass.csv",overlap,list(overlap[0]))
    summary=[]
    for year in PASS_YEARS:
        for field in ("Yt","Kt","Lt"):
            rows=[r for r in overlap if r["year"]==year and r["variable"]==field]; abses=[r["absolute_difference"] for r in rows]; rels=[r["relative_difference_abs_matlab_denominator"] for r in rows]; worst=max(rows,key=lambda r:r["absolute_difference"])
            xs=[r["matlab_legacy_value"] for r in rows]; ys=[r["python_owner_a_value"] for r in rows]
            summary.append({"year":year,"variable":field,"mean_absolute_difference":statistics.fmean(abses),"median_absolute_difference":statistics.median(abses),"max_absolute_difference":max(abses),"mean_relative_difference":statistics.fmean(rels),"median_relative_difference":statistics.median(rels),"max_relative_difference":max(rels),"pearson_correlation":corr(xs,ys),"spearman_rank_correlation":corr(ranks(xs),ranks(ys)),"worst_province":worst["province"],"matlab_value":worst["matlab_legacy_value"],"python_value":worst["python_owner_a_value"],"semantic_label":"NOT_SAME_INPUT__DIAGNOSTIC_ONLY"})
    write_csv(ROOT / "matlab_python_legacy_overlap_diagnostic_summary.csv",summary,list(summary[0]))
    neighbors=neighbor_rows(); write_csv(ROOT / "input_2017_2018_2019_neighbor_comparison.csv",neighbors,list(neighbors[0]))
    failure_material(records)
    provenance_fields = ["zip_path", "source_absolute_path", "filename", "year", "artifact_type", "source_batch_root", "representation",
                         "rolling_window_entry_index", "regression_vintage_index", "calendar_level_row_index", "status", "sha256", "bytes", "copied"]
    write_csv(ROOT / "source_artifact_provenance.csv", records, provenance_fields)
    hypotheses=[
      {"hypothesis_id":"OBSERVED_SINGULAR_SYSTEM","hypothesis":"The contaminated-row linear system was exactly singular on the retry.","mechanism":"spsolve emitted MatrixRankWarning and produced non-finite raw values.","evidence_for":"Preserved retry stderr.","evidence_against":"None for the observed numerical condition.","status":"SUPPORTED","would_require_new_scientific_run_to_test":"NO","minimal_future_test":"None; already observed."},
      {"hypothesis_id":"MULTIPLE_CLOSED_CLASSES","hypothesis":"Generator nullity exceeds one due to multiple closed communicating classes.","mechanism":"Pinning one normalization row does not remove all stationary null directions.","evidence_for":"Mathematically compatible with singular contaminated system.","evidence_against":"No generator/operator persisted for 2018.","status":"POSSIBLE","would_require_new_scientific_run_to_test":"YES","minimal_future_test":"Authorized diagnostic persistence of 2018 generator and communicating-class analysis."},
      {"hypothesis_id":"DISCONNECTED_MASS_BLOCK","hypothesis":"A disconnected/reducible mass block leaves the pinned system singular.","mechanism":"The transposed generator contains an additional null direction.","evidence_for":"General finite-state KFE possibility.","evidence_against":"Exact province/call/operator unknown.","status":"POSSIBLE","would_require_new_scientific_run_to_test":"YES","minimal_future_test":"Authorized targeted generator connectivity audit at the failing call."},
      {"hypothesis_id":"INPUT_MISMATCH","hypothesis":"Observable retry used a different scientific input.","mechanism":"Input discontinuity causes a distinct solve.","evidence_for":"None.","evidence_against":"Original/retry SHA-256 values are byte-identical.","status":"DISFAVORED","would_require_new_scientific_run_to_test":"NO","minimal_future_test":"None; retained identity evidence already rejects this explanation."},
      {"hypothesis_id":"HJB_NOT_CONVERGED","hypothesis":"HJB nonconvergence alone caused the exception.","mechanism":"An invalid post-convergence operator reaches KFE.","evidence_for":"The adapter deliberately uses post-loop output even when HJB is not converged.","evidence_against":"Logs do not preserve province-level HJB state; singularity is not ordinary convergence failure.","status":"UNRESOLVED","would_require_new_scientific_run_to_test":"YES","minimal_future_test":"Authorized per-call HJB/KFE diagnostic receipt without solver mutation."}
    ]
    write_csv(ROOT / "2018_kfe_singularity_hypothesis_matrix.csv",hypotheses,list(hypotheses[0]))
    write_text_no_overwrite(ROOT / "python_program_correctness_evidence_map.md", """# Python program-correctness evidence map\n\n## Already strong evidence\n\n- Previously accepted MATLAB-faithful household/HJB/KFE parity gates.\n- The corrected-2009 same-input cross-language stationary-parity anchor.\n- Thirteen Owner-A years have complete finite 31x20 terminal results and valid artifacts.\n- Owner-A 2000-2022 capital segment was independently reproduced from CHNCapitalStock.\n- Calendar, index, and scaling contracts are explicit.\n\n## Not yet proven\n\n- Strict same-input MATLAB/Python parity for every annual 2010-2022 year.\n- Correctness of the 2018 KFE stationary distribution under its current input.\n- A 2023 data extension.\n- Numerical shock/IRF results.\n\n## Current 2018 blocker\n\nThe frozen 2018 input produces an exactly singular contaminated-row KFE solve. The scientific cause is not established without separately authorized targeted diagnostics.\n""")
    write_text_no_overwrite(ROOT / "README.md", f"""# CH5 MP4C manual comparison package\n\nContains exactly the 13 successful Owner-A years: {', '.join(map(str,PASS_YEARS))}. 2018 is deliberately absent, because both authorized attempts failed; it is not zero-filled. 2023 is out of scope.\n\nMATLAB multi-year materials are `{LABEL}`. MATLAB/Python overlap statistics are manual diagnostic artifacts, never parity PASS/FAIL. The corrected-2009 same-input contract remains a separate accepted anchor.\n\nNo scientific model was executed to build this package.\n""")
    # include compact package outputs and only allowed source copies
    members=[]
    package_roots = [
        ROOT / "python_source", ROOT / "failure_2018",
        ROOT / "README.md", ROOT / "python_owner_a_steady_state_2009_2022_13pass_long.csv",
        ROOT / "python_owner_a_input_levels_2009_2022_13pass_long.csv", ROOT / "PYTHON_OWNER_A_STEADY_STATE_2009_2022_13PASS.xlsx",
        ROOT / "MATLAB_LEGACY_STEADY_STATE_RECORD_EXTRACT.xlsx", ROOT / "matlab_python_legacy_overlap_diagnostic_13pass.csv",
        ROOT / "matlab_python_legacy_overlap_diagnostic_summary.csv", ROOT / "2018_KFE_FAILURE_SUMMARY.md",
        ROOT / "input_2017_2018_2019_neighbor_comparison.csv", ROOT / "2018_kfe_singularity_hypothesis_matrix.csv",
        ROOT / "python_program_correctness_evidence_map.md",
        ROOT / "source_artifact_provenance.csv",
        *(ROOT / f"matlab_legacy_{field}_2009_2022.csv" for field in ("Yt", "Kt", "Lt", "Yt0", "Kt0", "Lt0")),
    ]
    for candidate in package_roots:
        if candidate.is_dir(): members.extend(path for path in candidate.rglob("*") if path.is_file())
        elif candidate.is_file(): members.append(candidate)
    manifest=[{"zip_path":str(p.relative_to(ROOT)).replace("\\","/"),"sha256":sha(p),"bytes":p.stat().st_size} for p in sorted(members)]
    write_csv(ROOT / "package_file_manifest.csv",manifest,["zip_path","sha256","bytes"])
    zip_path=ROOT / "CH5_MP4C_MANUAL_COMPARISON_PACKAGE_2009_2022_13PASS_PLUS_2018_FAILURE.zip"
    with zipfile.ZipFile(zip_path,"x",compression=zipfile.ZIP_DEFLATED) as archive:
        for p in sorted(members+[ROOT / "package_file_manifest.csv"]): archive.write(p,p.relative_to(ROOT).as_posix())
    dump(ROOT / "final_receipt.json",{"terminal":"MP4C_13PASS_STEADY_STATE_COMPARISON_PACKAGE_COMPLETE__2018_KFE_SINGULARITY_FORENSIC_COMPLETE__NO_SCIENTIFIC_RERUN","zip": {"path":zip_path.name,"sha256":sha(zip_path),"bytes":zip_path.stat().st_size},"rows":{"python_steady_state":len(final_rows),"input_levels":len(context["level_rows"]),"overlap":len(overlap)},"scientific_calls":0})


if __name__ == "__main__":
    parser=argparse.ArgumentParser(); parser.add_argument("phase",choices=("prepare","finalize")); args=parser.parse_args()
    {"prepare":prepare,"finalize":finalize}[args.phase]()
