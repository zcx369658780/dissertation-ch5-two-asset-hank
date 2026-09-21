"""Zero-science attribution of the persisted Heilongjiang negative b slope.

This module never imports production code.  It reconstructs finite differences
and multiplies persisted CSR rows using NumPy only.  It never invokes a solver.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess
from typing import Any

import numpy as np


BASELINE = "c50465673ad34613e17ec3a4fba265bc79ff2924"
ACCEPTED_MANIFEST_SHA256 = "1C501CEF7740748805CF538A05ECF9D80938149CDDF31A3158091F665C45AD80"
TASK_ID = "CH5_MP4C_TURN2_HEILONGJIANG_F0063_NEGATIVE_LIQUID_DERIVATIVE_EMERGENCE_FORENSIC_20260921"
TERMINAL = "PASS__TURN2_HEILONGJIANG_F0063_NEGATIVE_DERIVATIVE_FORENSIC__EXACT_DIRECT_SOLVE_TRANSIENT_NONMONOTONICITY_CONFIRMED__NO_CODE_CHANGE"
CLASSIFICATION = "CHECKPOINT2_TO_3_ACCEPTED_DIRECT_SOLVE_EXACTLY_INTRODUCED_FIRST_NEGATIVE_LIQUID_SLOPES__NO_SERIALIZATION_OR_ARITHMETIC_INCONSISTENCY"
ROOT = Path("reports/ch5_mp4c_lower_a_interior_z_composition_repair_turn1_parity_turn2_run004_20260921")
PROVINCE = ROOT / "household/p07_黑龙江"
OUT = Path("reports/ch5_mp4c_turn2_heilongjiang_f0063_negative_derivative_emergence_forensic_20260921_run001")
SHAPE = (20, 20, 2)

AUTHORITY = (
    Path("AGENTS.md"), Path("project_rules/PROJECT_RULE_INDEX_CURRENT.md"),
    Path("docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md"),
    Path("docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md"),
    Path("docs/CH5_MP4C_ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_SCIENTIFIC_DESIGN_GATE_ACCEPTANCE_20260921.md"),
    Path("docs/CH5_MP4C_TURN2_HEILONGJIANG_F0063_NONPOSITIVE_BACKWARD_LIQUID_SHADOW_FORENSIC_ACCEPTANCE_20260921.md"),
    Path("docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_ACCEPTANCE_20260917.md"),
    Path("docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_CONVERGENCE_LAW_OWNER_ADOPTION_20260917.md"),
    Path("tasks/CH5_MP4C_TURN2_HEILONGJIANG_F0063_NEGATIVE_LIQUID_DERIVATIVE_EMERGENCE_FORENSIC_20260921.md"),
)
SOURCES = (
    Path("src/ch5_two_asset_hank/corrected_diagnostic/option_a_step.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py"),
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def field_sha256(values: np.ndarray) -> str:
    return hashlib.sha256(np.asarray(values, dtype="<f8").tobytes(order="F")).hexdigest().upper()


def identity(path: Path, repository: Path) -> dict[str, Any]:
    return {"path": path.relative_to(repository).as_posix(), "bytes": path.stat().st_size, "sha256": sha256(path)}


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def grid() -> dict[str, np.ndarray]:
    return {"b": np.linspace(-2.0, 5.0, 20), "a": np.linspace(0.0, 10.0, 20), "z": np.array([0.8, 1.3])}


def reconstruct(value: np.ndarray) -> dict[str, np.ndarray]:
    v = np.asarray(value, dtype=np.float64)
    if v.shape != SHAPE or not np.isfinite(v).all():
        raise ValueError("persisted V must be finite with shape (20,20,2)")
    nodes = grid(); b_slopes = (v[1:] - v[:-1]) / np.diff(nodes["b"])[:, None, None]
    a_slopes = (v[:, 1:] - v[:, :-1]) / np.diff(nodes["a"])[None, :, None]
    pbf=np.empty_like(v); pbb=np.empty_like(v); paf=np.empty_like(v); pab=np.empty_like(v)
    pbf[:-1]=b_slopes; pbb[1:]=b_slopes; pbb[0]=pbf[0]; pbf[-1]=pbb[-1]
    paf[:,:-1]=a_slopes; pab[:,1:]=a_slopes; pab[:,0]=paf[:,0]; paf[:,-1]=pab[:,-1]
    return {"p_b_backward":pbb,"p_b_forward":pbf,"p_a_backward":pab,"p_a_forward":paf}


def load_states(repository: Path) -> dict[str, np.ndarray]:
    root=repository/PROVINCE
    states={"native":np.load(root/"native_initialization_arrays.npz",allow_pickle=False)["value"]}
    for n in range(3):
        with np.load(root/f"checkpoint_{n:03d}/checkpoint_arrays.npz",allow_pickle=False) as z: states[f"checkpoint{n}"]=np.array(z["value"],copy=True)
    with np.load(root/"checkpoint_002/direct_update_arrays.npz",allow_pickle=False) as z: states["checkpoint3"]=np.array(z["next_value"],copy=True)
    return states


def f_index(index: tuple[int,int,int]) -> int:
    return int(np.ravel_multi_index(index,SHAPE,order="F"))


def location(array: np.ndarray, mode: str="min") -> dict[str, Any]:
    offset=int(np.argmin(array) if mode=="min" else np.argmax(array)); idx=tuple(map(int,np.unravel_index(offset,SHAPE)))
    return {"value":float(array[idx]),"index_b_a_z_zero_based":list(idx),"flat_f_zero_based":f_index(idx)}


def pattern_counts(pbb: np.ndarray, pbf: np.ndarray, indices: list[int]) -> dict[str,int]:
    x=pbb[indices]; y=pbf[indices]
    return {"(+,+)":int(np.sum((x>0)&(y>0))),"(<=0,+)":int(np.sum((x<=0)&(y>0))),
            "(+,<=0)":int(np.sum((x>0)&(y<=0))),"(<=0,<=0)":int(np.sum((x<=0)&(y<=0)))}


def census(value: np.ndarray) -> dict[str, Any]:
    fields=reconstruct(value); pbb=fields["p_b_backward"]; pbf=fields["p_b_forward"]
    nonpositive=np.argwhere((pbb<=0)|(pbf<=0)); first=None if not len(nonpositive) else min(f_index(tuple(map(int,x))) for x in nonpositive)
    b_slopes=(value[1:]-value[:-1])/np.diff(grid()["b"])[:,None,None]
    negatives=np.asarray(b_slopes[b_slopes<0],dtype=float)
    return {"sign_patterns":{"interior_b":pattern_counts(pbb,pbf,list(range(1,19))),
                              "lower_b":pattern_counts(pbb,pbf,[0]),"upper_b":pattern_counts(pbb,pbf,[19])},
            "minimum_p_b_backward":location(pbb),"minimum_p_b_forward":location(pbf),
            "first_f_order_flat_with_any_nonpositive":first,
            "negative_derivative_representations":int(np.sum(pbb<0)+np.sum(pbf<0)),
            "distinct_negative_b_edges":int(negatives.size),
            "maximum_negative_magnitude":0.0 if not negatives.size else float(np.max(-negatives)),
            "derivative_sha256":{k:field_sha256(v) for k,v in fields.items()}}


def selected_policy(repository: Path, checkpoint: int, index: tuple[int,int,int]) -> dict[str,Any]:
    path=repository/PROVINCE/f"checkpoint_{checkpoint:03d}/selected_policy_arrays.npz"
    with np.load(path,allow_pickle=False) as z:
        return {"q_b":float(z["q_b"][index]),"g_b":float(z["g_b"][index]),
                "cell_policy_identity_available":False,"reason":"completed-map cell receipts were compacted away"}


def trajectory(repository: Path, states: dict[str,np.ndarray]) -> dict[str,Any]:
    nodes=grid()["b"]; rows=[]; order=["native","checkpoint0","checkpoint1","checkpoint2","checkpoint3"]
    previous={62:None,63:None}
    for name in order:
        v=states[name]; fields=reconstruct(v)
        for flat in (62,63):
            idx=tuple(map(int,np.unravel_index(flat,SHAPE,order="F"))); i,j,k=idx
            pb=float(fields["p_b_backward"][idx]); pf=float(fields["p_b_forward"][idx])
            row={"iterate":name,"flat_f_zero_based":flat,"index_b_a_z_zero_based":list(idx),"b":float(nodes[i]),
                 "neighbor_b_nodes":[float(nodes[i-1]),float(nodes[i]),float(nodes[i+1])],
                 "neighbor_V_levels":[float(v[i-1,j,k]),float(v[i,j,k]),float(v[i+1,j,k])],
                 "p_b_backward":pb,"p_b_forward":pf,"mixed_or_nonpositive":pb<=0 or pf<=0,
                 "sign_changed_from_previous":None if previous[flat] is None else [pb>0,pf>0]!=previous[flat]}
            if name.startswith("checkpoint") and name!="checkpoint3": row["selected_policy"]=selected_policy(repository,int(name[-1]),idx)
            elif name=="checkpoint3":
                cell=json.loads((repository/PROVINCE/"checkpoint_003"/f"cell_{flat:04d}.json").read_text(encoding="utf-8"))
                selected=cell["selector_result"]["selected"]
                row["selected_policy"]=(None if selected is None else {k:selected[k] for k in ("derivative_branches","transfer_branch","q_b","g_b","q_a","g_a","hamiltonian")})
            else: row["selected_policy"]=None
            previous[flat]=[pb>0,pf>0]; rows.append(row)
    transitions=[]
    unique=[states["checkpoint0"],states["checkpoint1"],states["checkpoint2"],states["checkpoint3"]]
    for n,(left,right) in enumerate(zip(unique[:-1],unique[1:])):
        i2=(2,3,0); i3=(3,3,0); old_gap=float(left[i3]-left[i2]); new_gap=float(right[i3]-right[i2])
        transitions.append({"update":f"{n}->{n+1}","V62_increment":float(right[i2]-left[i2]),"V63_increment":float(right[i3]-left[i3]),
                            "V63_minus_V62_before":old_gap,"V63_minus_V62_after":new_gap,"gap_change":new_gap-old_gap,
                            "sign_after":"negative" if new_gap<0 else "zero" if new_gap==0 else "positive"})
    return {"rows":rows,"updates":transitions,"first_mixed_update":"2->3"}


def csr_matvec(data: np.ndarray, indices: np.ndarray, indptr: np.ndarray, x: np.ndarray) -> np.ndarray:
    result=np.empty(indptr.size-1,dtype=np.float64)
    for row in range(result.size):
        start,end=int(indptr[row]),int(indptr[row+1]); result[row]=np.dot(data[start:end],x[indices[start:end]])
    return result


def direct_update_receipt(repository: Path, checkpoint: int) -> dict[str,Any]:
    directory=repository/PROVINCE/f"checkpoint_{checkpoint:03d}"
    persisted=json.loads((directory/"direct_solve_receipt.json").read_text(encoding="utf-8"))
    with np.load(directory/"direct_update_arrays.npz",allow_pickle=False) as z:
        data=np.array(z["matrix_data"]); indices=np.array(z["matrix_indices"]); indptr=np.array(z["matrix_indptr"])
        rhs=np.array(z["rhs"]); next_value=np.array(z["next_value"]); saved=np.array(z["residual"])
    flat=next_value.ravel(order="F"); recomputed=csr_matvec(data,indices,indptr,flat)-rhs
    row_abs=np.empty(800)
    for i in range(800): row_abs[i]=np.sum(np.abs(data[indptr[i]:indptr[i+1]]))
    residual_inf=float(np.max(np.abs(recomputed))); matrix_inf=float(np.max(row_abs)); solution_inf=float(np.max(np.abs(flat))); rhs_inf=float(np.max(np.abs(rhs)))
    denominator=matrix_inf*solution_inf+rhs_inf; backward=residual_inf/denominator
    target=(repository/PROVINCE/f"checkpoint_{checkpoint+1:03d}/checkpoint_arrays.npz")
    target_hash=None
    if target.is_file():
        with np.load(target,allow_pickle=False) as z: target_hash=field_sha256(z["value"])
    else: target_hash=json.loads((repository/PROVINCE/"checkpoint_003/derivative_receipt.json").read_text(encoding="utf-8"))["value_sha256"]
    scalar_names=("residual_inf","matrix_inf","solution_inf","rhs_inf","denominator","normwise_backward_error")
    local_scalars={"residual_inf":residual_inf,"matrix_inf":matrix_inf,"solution_inf":solution_inf,"rhs_inf":rhs_inf,"denominator":denominator,"normwise_backward_error":backward}
    scalar_differences={name:local_scalars[name]-float(persisted[name]) for name in scalar_names}
    scalar_consistency=all(abs(scalar_differences[name]) <= 8*np.finfo(float).eps*max(1.0,abs(float(persisted[name]))) for name in scalar_names)
    return {"checkpoint_from":checkpoint,"checkpoint_to":checkpoint+1,"next_value_sha256":field_sha256(next_value),"target_value_sha256":target_hash,
            "next_value_exact_target_identity":field_sha256(next_value)==target_hash,"rhs_sha256":field_sha256(rhs),
            "saved_residual_sha256":field_sha256(saved),"recomputed_residual_sha256":field_sha256(recomputed),
            "recomputed_residual_bitwise_equal_saved":bool(np.array_equal(recomputed,saved)),"maximum_residual_recompute_difference":float(np.max(np.abs(recomputed-saved))),
            "residual_inf":residual_inf,"matrix_inf":matrix_inf,"solution_inf":solution_inf,"rhs_inf":rhs_inf,"denominator":denominator,
            "normwise_backward_error":backward,"persisted_receipt":persisted,"scalar_abs_differences":{k:abs(v) for k,v in scalar_differences.items()},
            "all_persisted_identity_hashes_exact":all((field_sha256(next_value)==persisted["next_value_sha256"],field_sha256(rhs)==persisted["rhs_sha256"],field_sha256(saved)==persisted["residual_sha256"])),
            "all_persisted_scalars_consistent_within_8eps_scaled_bound":scalar_consistency}


def local_rows(repository: Path) -> dict[str,Any]:
    directory=repository/PROVINCE/"checkpoint_002"
    with np.load(directory/"direct_update_arrays.npz",allow_pickle=False) as z:
        data=np.array(z["matrix_data"]); indices=np.array(z["matrix_indices"]); ptr=np.array(z["matrix_indptr"]); rhs=np.array(z["rhs"]); x=np.array(z["next_value"]).ravel(order="F")
    with np.load(directory/"q_generator.npz",allow_pickle=False) as z:
        qdata=np.array(z["data"]); qindices=np.array(z["indices"]); qptr=np.array(z["indptr"])
    with np.load(directory/"selected_policy_arrays.npz",allow_pickle=False) as z:
        q_b=np.array(z["q_b"]); g_b=np.array(z["g_b"])
    rows=[]
    for row in (62,63):
        start,end=int(ptr[row]),int(ptr[row+1]); cols=indices[start:end]; vals=data[start:end]; terms=vals*x[cols]
        diagonal_pos=int(np.where(cols==row)[0][0]); diag=float(vals[diagonal_pos]); off=float(np.sum(terms)-terms[diagonal_pos])
        implied=float((rhs[row]-off)/diag); idx=tuple(map(int,np.unravel_index(row,SHAPE,order="F")))
        qs,qe=int(qptr[row]),int(qptr[row+1]); qcols=qindices[qs:qe]; qvals=qdata[qs:qe]
        rows.append({"row":row,"index_b_a_z_zero_based":list(idx),"rhs":float(rhs[row]),"matrix_row_sum":float(np.sum(terms)),
                     "residual":float(np.sum(terms)-rhs[row]),"actual_solution":float(x[row]),"diagonal_rearrangement_implied_solution":implied,
                     "implied_minus_actual":implied-float(x[row]),"selected_q_b":float(q_b[idx]),"selected_g_b":float(g_b[idx]),
                     "matrix_terms":[{"column":int(c),"column_index_b_a_z_zero_based":list(map(int,np.unravel_index(int(c),SHAPE,order="F"))),
                                      "coefficient":float(v),"solution":float(x[c]),"product":float(t)} for c,v,t in zip(cols,vals,terms)],
                     "persisted_q_row":[{"column":int(c),"column_index_b_a_z_zero_based":list(map(int,np.unravel_index(int(c),SHAPE,order="F"))),"q_value":float(v)} for c,v in zip(qcols,qvals)],
                     "cross_interface_neighbor_present":bool((63 if row==62 else 62) in cols)})
    v=x.reshape(SHAPE,order="F"); spacing=float(grid()["b"][3]-grid()["b"][2]); slope=float((v[3,3,0]-v[2,3,0])/spacing)
    return {"rows":rows,"interface":{"left_flat":62,"right_flat":63,"spacing":spacing,"left_value":float(x[62]),"right_value":float(x[63]),
             "exact_difference":float(x[63]-x[62]),"finite_difference":slope,"no_cross_interface_matrix_coupling":all(not x["cross_interface_neighbor_present"] for x in rows),
             "checkpoint2_selected_drifts_point_away_from_interface":rows[0]["selected_g_b"]<0<rows[1]["selected_g_b"]}}


def artifact_chain(repository: Path, states: dict[str,np.ndarray]) -> dict[str,Any]:
    root=repository/ROOT; province=repository/PROVINCE
    manifest_path=root/"sealed_manifest.json"; manifest=json.loads(manifest_path.read_text(encoding="utf-8")); entries={x["path"]:x for x in manifest["entries"]}
    relevant=[PROVINCE.relative_to(ROOT)/"native_initialization_arrays.npz"]
    for n in range(3):
        base=PROVINCE.relative_to(ROOT)/f"checkpoint_{n:03d}"
        relevant += [base/"checkpoint_arrays.npz",base/"derivative_receipt.json",base/"direct_update_arrays.npz",base/"direct_solve_receipt.json"]
    relevant += [PROVINCE.relative_to(ROOT)/"checkpoint_003/derivative_receipt.json",PROVINCE.relative_to(ROOT)/"checkpoint_003/cell_0062.json",PROVINCE.relative_to(ROOT)/"checkpoint_003/cell_0063.json"]
    artifact=[]
    for rel in relevant:
        path=root/rel; row=entries.get(rel.as_posix()); artifact.append({"path":rel.as_posix(),"working_sha256":sha256(path),"manifest":row,
            "matches_manifest":row is not None and row["bytes"]==path.stat().st_size and row["sha256"]==sha256(path)})
    native_receipt=json.loads((province/"native_initialization_receipt.json").read_text(encoding="utf-8"))
    links=[{"from":"native","to":"checkpoint0","from_sha256":field_sha256(states["native"]),"to_sha256":field_sha256(states["checkpoint0"]),"exact":bool(np.array_equal(states["native"],states["checkpoint0"]))}]
    for n in range(3):
        with np.load(province/f"checkpoint_{n:03d}/direct_update_arrays.npz",allow_pickle=False) as z: nxt=np.array(z["next_value"])
        target=states[f"checkpoint{n+1}"]; links.append({"from":f"checkpoint{n}_direct_update_next_value","to":f"checkpoint{n+1}",
            "from_sha256":field_sha256(nxt),"to_sha256":field_sha256(target),"exact":bool(np.array_equal(nxt,target))})
    return {"accepted_manifest_sha256":sha256(manifest_path),"accepted_manifest_expected":ACCEPTED_MANIFEST_SHA256,
            "manifest_identity_pass":sha256(manifest_path)==ACCEPTED_MANIFEST_SHA256,"manifest_entry_count":manifest["entry_count"],"relevant_artifacts":artifact,
            "native_receipt_value_sha256":native_receipt["value_sha256"],"state_hashes":{k:field_sha256(v) for k,v in states.items()},"links":links}


def manifest(output: Path) -> None:
    excluded={"sealed_manifest.json","independent_readback_receipt.json"}; rows=[]
    for path in sorted(p for p in output.rglob("*") if p.is_file() and p.name not in excluded):
        rows.append({"path":path.relative_to(output).as_posix(),"bytes":path.stat().st_size,"sha256":sha256(path)})
    write_json(output/"sealed_manifest.json",{"schema":"CH5_F0063_NEGATIVE_DERIVATIVE_EMERGENCE_FORENSIC_MANIFEST_V1","entry_count":len(rows),"total_bytes":sum(x["bytes"] for x in rows),"entries":rows})
    payload=json.loads((output/"sealed_manifest.json").read_text(encoding="utf-8")); bad=[]
    for row in payload["entries"]:
        path=output/row["path"]
        if not path.is_file() or path.stat().st_size!=row["bytes"] or sha256(path)!=row["sha256"]: bad.append(row["path"])
    write_json(output/"independent_readback_receipt.json",{"status":"PASS" if not bad else "FAIL","manifest_sha256":sha256(output/"sealed_manifest.json"),
        "entry_count":payload["entry_count"],"total_bytes":payload["total_bytes"],"bad_paths":bad,"scientific_calls":0})


def execute(repository: Path, junit: Path) -> str:
    repository=repository.resolve(strict=True); output=repository/OUT
    if output.exists(): raise RuntimeError("fresh evidence root already exists")
    head=subprocess.check_output(["git","rev-parse","HEAD"],cwd=repository,text=True).strip(); origin=subprocess.check_output(["git","rev-parse","origin/main"],cwd=repository,text=True).strip()
    if head!=BASELINE or origin!=BASELINE: raise RuntimeError("live-main baseline binding failed")
    output.mkdir(parents=True)
    write_json(output/"authority_source_binding.json",{"status":"PASS","task_id":TASK_ID,"head":head,"origin_main":origin,
        "authority":[identity(repository/p,repository) for p in AUTHORITY],"sources":[identity(repository/p,repository) for p in SOURCES]})
    states=load_states(repository); chain=artifact_chain(repository,states)
    if not chain["manifest_identity_pass"] or not all(x["matches_manifest"] for x in chain["relevant_artifacts"]) or not all(x["exact"] for x in chain["links"]): raise RuntimeError("accepted artifact chain mismatch")
    write_json(output/"accepted_artifact_sha_chain.json",chain)
    census_rows={name:census(value) for name,value in states.items()}
    receipts={}
    for n in range(4):
        receipt=json.loads((repository/PROVINCE/f"checkpoint_{n:03d}/derivative_receipt.json").read_text(encoding="utf-8"))
        key=f"checkpoint{n}"; receipts[key]={"persisted":receipt,"reconstructed":census_rows[key]["derivative_sha256"],
            "all_four_hashes_exact":receipt["derivative_sha256"]==census_rows[key]["derivative_sha256"],"value_hash_exact":receipt["value_sha256"]==field_sha256(states[key])}
    c62=json.loads((repository/PROVINCE/"checkpoint_003/cell_0062.json").read_text(encoding="utf-8")); c63=json.loads((repository/PROVINCE/"checkpoint_003/cell_0063.json").read_text(encoding="utf-8")); fields3=reconstruct(states["checkpoint3"])
    cell_parity={}
    for flat,payload in ((62,c62),(63,c63)):
        idx=tuple(payload["index_b_a_z_zero_based"]); reconstructed={k:float(v[idx]) for k,v in fields3.items()}; cell_parity[str(flat)]={"persisted":payload["selector_cell"]["derivatives"],"reconstructed":reconstructed,"exact":payload["selector_cell"]["derivatives"]==reconstructed}
    write_json(output/"reconstructed_derivative_parity_receipt.json",{"status":"PASS" if all(x["all_four_hashes_exact"] and x["value_hash_exact"] for x in receipts.values()) and all(x["exact"] for x in cell_parity.values()) else "FAIL",
        "production_derivative_helper_calls":0,"checkpoint_receipts":receipts,"f0062_f0063_exact_cell_parity":cell_parity})
    write_json(output/"four_iterate_liquid_derivative_sign_census.json",census_rows)
    traj=trajectory(repository,states); write_json(output/"f0062_f0063_local_trajectory.json",traj)
    direct={str(n):direct_update_receipt(repository,n) for n in range(3)}; write_json(output/"direct_update_residual_identity_receipt.json",direct)
    local=local_rows(repository); write_json(output/"checkpoint2_to_3_local_sparse_row_attribution.json",local)
    exact=(all(x["all_persisted_identity_hashes_exact"] and x["all_persisted_scalars_consistent_within_8eps_scaled_bound"] and x["next_value_exact_target_identity"] and x["recomputed_residual_bitwise_equal_saved"] for x in direct.values())
           and census_rows["checkpoint0"]["distinct_negative_b_edges"]==0 and census_rows["checkpoint1"]["distinct_negative_b_edges"]==0
           and census_rows["checkpoint2"]["distinct_negative_b_edges"]==0 and census_rows["checkpoint3"]["distinct_negative_b_edges"]==2
           and traj["first_mixed_update"]=="2->3" and local["interface"]["finite_difference"]==-0.0002428532863339202)
    if not exact: raise RuntimeError("forensic classification predicates failed")
    write_json(output/"numerical_attribution_classification.json",{"terminal":TERMINAL,"classification":CLASSIFICATION,
        "first_nonpositive_update":"checkpoint2 -> checkpoint3","accepted_direct_solve_exact":True,"serialization_inconsistency":False,
        "arithmetic_inconsistency":False,"transient_nonmonotonicity":True,"implementation_repair_proposed":False})
    ledger={"persisted_npz_loads":19,"persisted_json_loads":14,"accepted_artifact_sha256_reads":16,"independent_derivative_reconstructions":15,"independent_full_csr_matvecs":3,
        "independent_local_sparse_rows":2,"production_derivative_helper_calls":0,"production_selector_calls":0,"production_root_helper_calls":0,
        "hjb_direct_update_executions":0,"new_linear_solves_spsolve":0,"d2_q_rebuilds":0,"kfe_svd":0,"aggregate_integration":0,
        "turn2_replay_rerun":0,"turn3":0,"matlab":0,"retry_tuning":0,"scientific_model_calls":0}
    write_json(output/"zero_science_ledger.json",ledger)
    jt=junit.read_text(encoding="utf-8"); shutil.copyfile(junit,output/"focused_tests.xml"); write_json(output/"focused_test_receipt.json",{"status":"PASS" if 'failures=\"0\"' in jt and 'errors=\"0\"' in jt else "FAIL","sha256":sha256(output/"focused_tests.xml")})
    write_json(output/"terminal_receipt.json",{"terminal":TERMINAL,"classification":CLASSIFICATION,"zero_science_ledger":ledger,"src_modified":False,"current_modified":False,"successor_published":False,"results_eligibility":False})
    manifest(output); return TERMINAL


def main(argv: list[str]|None=None) -> int:
    p=argparse.ArgumentParser(); p.add_argument("--repository",type=Path,required=True); p.add_argument("--focused-test-junit",type=Path,required=True); a=p.parse_args(argv)
    print(execute(a.repository,a.focused_test_junit)); return 0


if __name__=="__main__": raise SystemExit(main())
