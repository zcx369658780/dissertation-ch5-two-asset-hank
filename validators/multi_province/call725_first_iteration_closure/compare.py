"""Compare persisted call-725 iteration-one evidence; never import a model or solve.

Run with Python/NumPy/SciPy, --output pointing to a fresh task evidence directory.
All normalization is representational: F-order vectors, B/0/F labels, exact sparse
zeros. No evaluator, derivative reconstruction, or tolerance selection occurs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.io import loadmat

EPS_SCALE = 128 * np.finfo(np.float64).eps
SHAPE = (20, 20, 2)
PRE = Path(r"D:\ProjectTemp\ch5-mp4c-2018-call725-postcall-residual-vectorization-repair-20260904-001")
BINDING = Path(r"D:\ProjectTemp\ch5-mp4c-2018-call725-first-iteration-scalar-binding-repair-20260904-001\call725_first_iteration_scalar_binding.json")
CLOSURE = Path(r"D:\ProjectTemp\ch5-mp4c-2018-call725-zero-science-evidence-closure-20260904-002")
FORENSIC = Path(r"D:\ProjectTemp\ch5-mp4c-2018-call725-raw-liquid-derivative-root-cause-20260904-001")
REPO = Path(__file__).resolve().parents[3]


class EvidenceIncomplete(ValueError):
    """Required persisted object cannot be read; acquisition remains manual/task-gated."""


def require_fields(container, required, language):
    missing = sorted(set(required) - set(container))
    if missing:
        raise EvidenceIncomplete(f"{language} missing fields: {', '.join(missing)}")

# Required scientific objects in causal order; grids are separately input-bound.
DENSE_FIELDS = [
    (1, "old/V0", "initial_value", "old", SHAPE),
    (2, "va_f", "VahF", "va_f", SHAPE),
    (2, "va_b", "VahB", "va_b", SHAPE),
    (2, "post_boundary_vb_f", "VbF", "vb_f", SHAPE),
    (2, "post_boundary_vb_b", "VbB", "vb_b", SHAPE),
    (3, "liquid_label", "liquid_label", "liquid_label", SHAPE),
    (3, "transfer_label", "transfer_label", "transfer_label", SHAPE),
    (4, "consumption", "C", "consumption", SHAPE),
    (4, "labor", "l", "labor", SHAPE),
    (4, "transfer", "dh", "transfer", SHAPE),
    (4, "adjustment_cost", "adjustment_cost", "adjustment_cost", SHAPE),
    (4, "effective_illiquid_return", "Rah", "effective_illiquid_return", SHAPE),
    (5, "mu_a", "mu_a", "mu_a", SHAPE),
    (5, "mu_b", "mu_b", "mu_b", SHAPE),
    (5, "utility", "u", "utility", SHAPE),
    (6, "bb", "bbB", "bb", SHAPE),
    (6, "bf", "bbF", "bf", SHAPE),
    (6, "ab", "aaB", "ab", SHAPE),
    (6, "af", "aaF", "af", SHAPE),
    (8, "RHS", "rhs", "rhs", (800,)),
    (9, "V1", "updated", "v1", SHAPE),
    (9, "first_iteration_statistic", "dist", "statistic", (1,)),
]
SPARSE_FIELDS = [(7, name, name) for name in ("BB", "AAH", "Bswitch", "A")] + [(8, "matrix", "M")]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def labels(value: np.ndarray) -> np.ndarray:
    """Map the persisted Python categorical encoding, rejecting unknown labels."""
    value = np.asarray(value)
    if not np.isin(value, ["B", "0", "F"]).all():
        raise ValueError("unknown policy label")
    result = np.zeros(value.shape, dtype=np.int8)
    result[value == "B"] = -1
    result[value == "F"] = 1
    return result


def vector(value: np.ndarray, count: int) -> np.ndarray:
    """Accept only explicitly designated MATLAB row/column and NumPy vectors."""
    value = np.asarray(value)
    if value.shape not in ((count,), (1, count), (count, 1)):
        raise ValueError(f"invalid vector shape {value.shape}, expected length {count}")
    return value.reshape(count, order="F")


def compare_dense(left, right, expected_shape, *, exact=False) -> dict:
    left, right = np.asarray(left), np.asarray(right)
    result = {"available": True, "left_shape": list(left.shape), "right_shape": list(right.shape),
              "expected_shape": list(expected_shape), "shape_pass": left.shape == right.shape == tuple(expected_shape),
              "comparison": "exact" if exact else "128*eps64*max(1,abs(left),abs(right))",
              "order": "logical tensor (b,a,z); linear coordinate uses F-order"}
    result["finite"] = bool(np.isfinite(left).all() and np.isfinite(right).all())
    if not result["shape_pass"] or not result["finite"]:
        return dict(result, passed=False, material_mismatch_count=None, max_abs=None, max_scaled=None)
    left, right = left.astype(float), right.astype(float)
    delta = np.abs(left - right)
    bound = EPS_SCALE * np.maximum(1, np.maximum(np.abs(left), np.abs(right)))
    mask = left != right if exact else delta > bound
    coordinates = np.argwhere(mask)
    examples = []
    for coord in coordinates[:5]:
        idx = tuple(coord)
        examples.append({"index_zero_based": coord.tolist(), "left": float(left[idx]), "right": float(right[idx]),
                         "absolute_difference": float(delta[idx]), "scaled_difference": float((delta / bound)[idx])})
    result.update(passed=not bool(mask.any()), material_mismatch_count=int(mask.sum()),
                  exact_equal=bool(np.array_equal(left, right)), max_abs=float(delta.max(initial=0)),
                  max_scaled=float((delta / bound).max(initial=0)), representative_coordinates=examples)
    return result


def canonical_sparse(value):
    matrix = sparse.csr_matrix(value, copy=True)
    matrix.sum_duplicates()
    matrix.eliminate_zeros()  # Only exact +/-0; never epsilon pruning.
    matrix.sort_indices()
    return matrix


def compare_sparse(left, right, expected_shape=(800, 800)) -> dict:
    left, right = canonical_sparse(left), canonical_sparse(right)
    result = compare_dense(left.toarray(), right.toarray(), expected_shape)
    support_left, support_right = set(zip(*left.nonzero())), set(zip(*right.nonzero()))
    support_diff = support_left.symmetric_difference(support_right)
    result.update(left_nnz=left.nnz, right_nnz=right.nnz, support_mismatch_count=len(support_diff),
                  support_pass=not bool(support_diff), representation="canonical CSR; exact stored zeros removed",
                  support_examples=[list(map(int, p)) for p in sorted(support_diff)[:5]])
    result["passed"] = result["passed"] and result["support_pass"]
    return result


def residual(matrix, rhs, value) -> dict:
    matrix = canonical_sparse(matrix)
    rhs = vector(rhs, matrix.shape[0])
    value = np.asarray(value).reshape(-1, order="F")
    with np.errstate(over="ignore", invalid="ignore"):
        r = float(np.max(np.abs(matrix @ value - rhs)))
        norm_m = float(np.max(np.asarray(abs(matrix).sum(axis=1))))
        norm_v, norm_rhs = float(np.max(np.abs(value))), float(np.max(np.abs(rhs)))
        scale = norm_m * norm_v + norm_rhs
    finite = bool(np.isfinite([r, norm_m, norm_v, norm_rhs, scale]).all())
    if not finite:
        return {"available": True, "passed": False, "finite": False,
                "reason": "nonfinite persisted operand or residual/norm arithmetic overflow"}
    return {"available": True, "passed": True, "finite": True,
            "residual_inf": r, "matrix_inf_norm": norm_m, "value_inf_norm": norm_v,
            "rhs_inf_norm": norm_rhs, "backward_error_scale": scale,
            "normwise_backward_error": r / scale if scale else (0.0 if r == 0 else None),
            "method": "persisted M @ vec_F(V1) - RHS; no solve or condition estimator"}


def outcome(records: list[dict]) -> str:
    if any(not r["available"] for r in records):
        return "FIRST_ITERATION_EVIDENCE_INCOMPLETE"
    if any(not r["passed"] for r in records):
        return "FIRST_ITERATION_MATERIAL_MISMATCH"
    return "FIRST_ITERATION_PARITY_PASS"


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    if json.loads(path.read_text(encoding="utf-8")) != value:
        raise ValueError(f"JSON readback mismatch: {path}")


def verify_manifest_outputs(path: Path) -> None:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    for entry in manifest["outputs"]:
        artifact = Path(entry["path"])
        if digest(artifact) != entry["sha256"] or artifact.stat().st_size != entry["bytes"]:
            raise ValueError(f"manifest output readback mismatch: {artifact}")


def run(output: Path) -> dict:
    output.mkdir(parents=True, exist_ok=False)
    identities = []

    def verified(path: Path, expected: str | None = None):
        actual = digest(path)
        if expected and actual != expected.upper():
            raise ValueError(f"identity mismatch: {path}")
        identities.append({"path": str(path), "sha256": actual, "bytes": path.stat().st_size,
                           "expected_sha256": expected, "verified": True})
        return path

    manifest_path = verified(PRE / "audit_manifest.json", "5996ED519C9C0316ECC5EA30F26BABBAAE7F95C63EDABDCF51FF7807C44D4970")
    prior = {e["relative_path"]: e["sha256"] for e in json.loads(manifest_path.read_text())["entries"]}
    m = loadmat(verified(PRE / "matlab_core_stagewise.mat", prior["matlab_core_stagewise.mat"]))
    with np.load(verified(PRE / "python_strict_stagewise.npz", prior["python_strict_stagewise.npz"]), allow_pickle=False) as container:
        p = {k: container[k] for k in container.files}
    matrices = {name: sparse.load_npz(verified(PRE / f"python_strict_stagewise_{name}.npz", prior[f"python_strict_stagewise_{name}.npz"])) for _, _, name in SPARSE_FIELDS}
    for name in ("matlab_postcall_vectorized_stagewise_wrapper.m", "python_postcall_vectorized_stagewise_wrapper.py"):
        verified(PRE / name, prior[name])
    binding = json.loads(verified(BINDING, "A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6").read_text(encoding="utf-8"))
    init = loadmat(verified(Path(binding["mat_authority"]["path"]), "1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81"))
    require_fields(m, [mk for _, _, mk, _, _ in DENSE_FIELDS] + [mk for _, mk, _ in SPARSE_FIELDS]
                   + ["b", "ah", "z", "l0", "raw_VbF", "raw_VbB", "raw_VahF", "raw_VahB", "updated_vec", "Ic_B", "Ic_F", "Ic_0", "Idh_B", "Idh_F"], "MATLAB")
    require_fields(p, [pk for _, _, _, pk, _ in DENSE_FIELDS]
                   + ["b", "a", "z", "l0", "raw_vb_f", "raw_vb_b", "raw_va_f", "raw_va_b"], "Python")
    require_fields(init, ["b", "ah", "z", "v0", "l0"], "authoritative MAT")
    verified(CLOSURE / "scientific_expression_identity_receipt.json", "BDF57469FC8CC1FF4BC2EB3190C7D608D0FED2642869B4B618BCA9391AD5AA46")
    source = verified(REPO / "exports/matlab_faithful_two_asset_ha.py")
    # Git normalizes the checkout's CRLF text; calculate the frozen Git blob without importing it.
    raw = source.read_bytes().replace(b"\r\n", b"\n")
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    if blob != "9e7dc9556a2b76811e78f89999abecc045886106":
        raise ValueError("production Python blob mismatch")
    verified(Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m"), "049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE")
    verified(FORENSIC / "wrapper_stage_semantics_audit.json", "73164C36FD034921D9FB2DB62FCE4F6C481FA671A5B81DBAD193CB70549985BF")
    verified(REPO / "tasks/CH5_MP4C_CALL725_FIRST_ITERATION_CLOSURE.md")
    verified(Path(__file__).resolve())
    rows, stage_map = [], []

    def record(stage, name, left, right, expected_shape, exact=False, **extra):
        row = dict(stage=stage, name=name, **compare_dense(left, right, expected_shape, exact=exact), **extra)
        rows.append(row)

    for mk, pk, ik, expected in [("b", "b", "b", (20,)), ("ah", "a", "ah", (20,)), ("z", "z", "z", (2,)), ("initial_value", "old", "v0", SHAPE), ("l0", "l0", "l0", SHAPE)]:
        for language, source_data, key in [("matlab", m, mk), ("python", p, pk)]:
            left, right = source_data[key], init[ik]
            if len(expected) == 1:
                left, right = vector(left, expected[0]), vector(right, expected[0])
            record(1, f"input/{language}/{ik}", left, right, expected, exact=True)
    for stage, name, mk, pk, shape in DENSE_FIELDS:
        stage_map.append({"stage": stage, "object": name, "matlab_field": mk, "python_field": pk,
                          "required": True, "normalization": "B=-1,0=0,F=1" if stage == 3 else "MATLAB row/column to F-vector" if len(shape) == 1 else "none; logical (b,a,z) tensor"})
        if mk not in m or pk not in p:
            rows.append({"stage": stage, "name": name, "available": False, "passed": False})
            continue
        left, right = m[mk], p[pk]
        original_shapes = {"matlab_container_shape": list(left.shape), "python_container_shape": list(right.shape)}
        if stage == 3:
            right = labels(right)
        if len(shape) == 1:
            left, right = vector(left, shape[0]), vector(right, shape[0])
        record(stage, name, left, right, shape, exact=stage == 3, **original_shapes)
    for stage, mk, pk in SPARSE_FIELDS:
        stage_map.append({"stage": stage, "object": pk, "matlab_field": mk,
                          "python_file": f"python_strict_stagewise_{pk}.npz", "required": True,
                          "normalization": "canonical sparse coordinates; exact stored zeros only"})
        rows.append(dict(stage=stage, name=pk, **compare_sparse(m[mk], matrices[pk])))
    # Python uses scalar booleans rather than exposing arrays. These are explicit
    # views of consumed labels, not a claim of independently captured Python masks.
    mask_map = [("Ic_B", "liquid_label", "B"), ("Ic_F", "liquid_label", "F"),
                ("Ic_0", "liquid_label", "0"), ("Idh_B", "transfer_label", "B"), ("Idh_F", "transfer_label", "F")]
    for mk, pk, label in mask_map:
        record(3, f"branch_view/{mk}", m[mk], p[pk] == label, SHAPE, exact=True,
               provenance="Python label-derived view of scalar use_liquid/use_transfer branches; not an independent persisted mask")
    diagnostic = []
    for mk, pk, domain in [("raw_VbF", "raw_vb_f", slice(0, -1)), ("raw_VbB", "raw_vb_b", slice(1, None))]:
        diagnostic.append({"name": pk, "historical_full_array": compare_dense(m[mk], p[pk], SHAPE),
                           "defined_interior_quotients": compare_dense(m[mk][domain], p[pk][domain], (19, 20, 2), exact=True),
                           "excluded_boundary": "upper b=5" if pk.endswith("f") else "lower b=-2",
                           "semantics": "MATLAB raw copied after boundary; Python raw before boundary; uncomputed Python boundary zero is not a derivative comparison",
                           "required_for_primary_parity": False})
    for mk, pk in [("raw_VahF", "raw_va_f"), ("raw_VahB", "raw_va_b")]:
        record(2, pk, m[mk], p[pk], SHAPE, exact=True)
    # Deterministic identities and residuals do not regenerate model state.
    n, params = binding["scalar_binding"]["numerics"], binding["scalar_binding"]["parameters"]
    consistency, diagnostics = [], {}
    for language, matrix, op, rhs, value, old, utility, stat in [
        ("matlab", m["matrix"], m["A"], vector(m["rhs"], 800), m["updated"], m["initial_value"], m["u"], vector(m["dist"], 1)),
        ("python", matrices["M"], matrices["A"], p["rhs"], p["v1"], p["old"], p["utility"], p["statistic"]),
    ]:
        diagnostics[language] = residual(matrix, rhs, value)
        consistency.append(dict(name=f"{language}/residual_finite", **diagnostics[language]))
        consistency.append(dict(name=f"{language}/M_identity", **compare_sparse(matrix, (1/n["delta"]+params["rho"])*sparse.eye(800)-op)))
        consistency.append(dict(name=f"{language}/RHS_identity", **compare_dense(rhs, utility.ravel(order="F")+old.ravel(order="F")/n["delta"], (800,))))
        consistency.append(dict(name=f"{language}/statistic_identity", **compare_dense(stat, np.array([np.max(abs(value-old))]), (1,), exact=True)))
    consistency.append(dict(name="matlab/persisted_vec_F", **compare_dense(vector(m["updated_vec"], 800), m["updated"].ravel(order="F"), (800,), exact=True)))
    rows.sort(key=lambda row: row["stage"])
    combined = rows + consistency
    summary = {"outcome": outcome(combined), "comparison_rule": "abs(x-y)<=128*eps64*max(1,abs(x),abs(y)); categorical/shape/order exact; exact sparse zero removal only",
               "required_complete": all(r["available"] for r in combined), "required_check_count": len(combined),
               "required_pass_count": sum(r["passed"] for r in combined), "earliest_genuine_mismatch": next((r["name"] for r in combined if not r["passed"]), None),
               "rows": rows, "consistency_checks": consistency, "raw_vb_diagnostics": diagnostic,
               "solve_diagnostics": diagnostics, "acquisition": "both sides reused; all required stages present; fresh acquisition condition not triggered",
               "new_calls": {"matlab": 0, "python_hjb": 0, "direct_solve": 0, "retry": 0, "native_probe": 0, "iteration_2_plus": 0, "kfe": 0, "ge_annual": 0, "r_plm": 0, "shock_irf_results": 0},
               "remaining_conditional_invocations": {"matlab": 2, "python": 2},
               "historical_ledger": "durable pair MATLAB=1/Python=1; earlier unpersisted MATLAB invocation remains consumed in its original task; no reset"}
    write_json(output / "stage_map.json", {"primary_fields": stage_map, "mask_views": [list(row) for row in mask_map],
        "source_locations": {"matlab_wrapper": "boundary 38/40; raw copy 43; masks 50/60-61; labels 74; F-order solve 68",
                             "python_wrapper": "raw copy 23; boundary 26-29; labels 36; F-order solve 37",
                             "python_frozen_source": "liquid branches 289-300; transfer branches/boundary 348-366"}})
    write_json(output / "comparison_summary.json", summary)
    write_json(output / "input_source_identity.json", {"frozen_python_blob": blob, "entries": identities,
        "provenance_limit": "Reuse accepted wrapper-to-evaluator attribution and path equivalence; no new source-extraction certification or MATLAB evaluation."})
    outputs = [{"path": str(output / name), "sha256": digest(output / name), "bytes": (output / name).stat().st_size}
               for name in ("stage_map.json", "comparison_summary.json", "input_source_identity.json")]
    write_json(output / "manifest.json", {"protocol": "finite; manifest excludes itself", "inputs_and_sources": identities, "outputs": outputs})
    verify_manifest_outputs(output / "manifest.json")
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = run(args.output)
    except (EvidenceIncomplete, FileNotFoundError, KeyError) as exc:
        result = {"outcome": "FIRST_ITERATION_EVIDENCE_INCOMPLETE", "required_check_count": 0,
                  "required_pass_count": 0, "earliest_genuine_mismatch": None,
                  "missing_prerequisite": str(exc), "new_calls": {"matlab": 0, "python_hjb": 0, "direct_solve": 0},
                  "note": "Acquisition is not implemented; a task-authorized operator must evaluate the missing evidence."}
        if args.output.is_dir():
            write_json(args.output / "incomplete_receipt.json", result)
    print(json.dumps({k: result[k] for k in ("outcome", "required_check_count", "required_pass_count", "earliest_genuine_mismatch", "new_calls")}, indent=2))
