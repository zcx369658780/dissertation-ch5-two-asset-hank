"""R9 source-authenticated fixtures, actual frozen Python assembly, and comparator."""
from __future__ import annotations
import ast,hashlib,json,math,os,re,stat,sys,types
from pathlib import Path
TASK="CH5_TEMP31_R6_R3_R2_R9_FIXED_SMALL_OPERATOR_PARITY_20261031"
W=Path(os.path.abspath(__file__)).parents[2]
L=W/"tasks"/TASK/"LOCAL_ONLY"
FROZEN={"matlab_source":"0e38270154ab8953290ae3ef6c92f95d38230afb","python_source":"9a511e151c9bf449412dc5605dfa1a2076711277","indexing_source":"3aee864af5dce5128957896e5d7803c2a815aab6"}
FIELDS=("b_backward","b_forward","a_backward","a_forward")
NAMES=("BB","AAH","Bswitch","A")
_PREPARED=False;_COMPARED=False
class ParityMismatch(RuntimeError):pass
def ident(raw):return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),git_blob=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest())
def dump(p,obj):
    with p.open("x",encoding="utf-8",newline="\n") as f:json.dump(obj,f,indent=2,allow_nan=False);f.write("\n")
def safe(p):
    p=Path(os.path.abspath(p))
    for q in reversed([p,*p.parents]):
        st=os.lstat(q)
        assert not stat.S_ISLNK(st.st_mode) and not getattr(st,"st_file_attributes",0)&0x400,"REPARSE"
    return p
def source_pair_gate():
    sources={}
    for role,blob in FROZEN.items():
        raw=safe(L/(role+"_fixed_utf8.txt")).read_bytes()
        assert ident(raw)["git_blob"]==blob,"FROZEN_SOURCE_BLOB"
        sources[role]=raw
    matlab=sources["matlab_source"].decode("utf-8")
    axis="\n".join(matlab.splitlines()[109:130])+"\n"
    runner=safe(W/"validators/multi_province/t31_r9_op.m").read_text(encoding="utf-8")
    actual=runner[runner.index("function G=axis_operator"):]
    normalize=lambda text:re.sub(r"\s+","",text)
    positive=normalize(actual)==normalize(axis)
    mutated=axis.replace("vals(end+1)=-total;","vals(end+1)=-total+1;")
    negative_m=normalize(mutated)!=normalize(axis)
    py=sources["python_source"].decode("utf-8")
    mutated_py=py.replace("row - (1 if axis == 0 else i_count)","row - (2 if axis == 0 else i_count)")
    negative_py=ident(mutated_py.encode())["git_blob"]!=FROZEN["python_source"]
    funcs={n.name for n in ast.parse(py).body if isinstance(n,ast.FunctionDef)}
    assert positive and negative_m and negative_py and {"assemble_source_axis","assemble_source_operator"}<=funcs,"SOURCE_PAIR_OR_NEGATIVE_GATE"
    assert "row=i+(j-1)*I+(nz-1)*I*J" in axis and "col=row-I" in axis and "col=row+I" in axis
    dump(L/"source_pair_static_gate_raw.json",dict(status="PASS",source_positive=positive,mutated_M_negative_rejected=negative_m,mutated_Python_negative_rejected=negative_py,negative_side_effects=0,sources={k:ident(v) for k,v in sources.items()},axis_lines=[110,130],axis_text=axis,axis_identity=ident(axis.encode()),runner_identity=ident(runner.encode()),axis_mapping={"MATLAB1":"Python0","MATLAB2":"Python1"},index_rule="k0=i+I*(j+J*z); MATLAB_row=k0+1",outward_rule="skip out-of-domain neighbor, retain -(rb+rf) diagonal",provenance="current official fixed-ref authenticated snapshots; no original trajectory execution"))
    return sources
def dependencies():
    cfg=json.loads(safe(L/"dependency_configuration_raw.json").read_bytes())
    pure=safe(Path(cfg["purelib"]))
    if str(pure) not in sys.path:sys.path.append(str(pure))
    import numpy as np
    import scipy
    from scipy import sparse
    for mod,key in ((np,"numpy"),(scipy,"scipy")):
        p=safe(Path(mod.__file__))
        assert p.resolve().is_relative_to(pure) and ident(p.read_bytes())==cfg[key]["identity"] and mod.__version__==cfg[key]["version"],"DEPENDENCY_IDENTITY"
    return np,scipy,sparse,cfg
def load_exact_snapshot(role,name):
    p=safe(L/(role+"_fixed_utf8.txt"));raw=p.read_bytes()
    assert ident(raw)["git_blob"]==FROZEN[role],"SNAPSHOT_AUTHENTICATION"
    module=types.ModuleType(name);module.__file__=str(p);module.__package__=""
    sys.modules[name]=module
    exec(compile(raw,str(p),"exec"),module.__dict__)
    return module
def fixture_payload(q):
    shape=(2,2,2) if q==1 else (3,2,2);M=math.prod(shape)
    pool=(0.0,0.125,-0.25,0.5,-0.75,0.25,-0.125,0.75)
    data={field:[pool[(k*(2*f+1)+f+1)%8] for k in range(M)] for f,field in enumerate(FIELDS)}
    switch=[[-0.25,0.25],[0.125,-0.125]] if q==1 else [[-0.5,0.5],[0.25,-0.25]]
    return dict(fixture_id="fixture_"+str(q),shape=list(shape),flatten_order="F",dtype="float64",switch_matrix=switch,vector=[((k%7)-3)/8 for k in range(M)],**data)
def prepare_once():
    global _PREPARED
    assert not _PREPARED,"FIXTURE_BUILD_REPLAY";_PREPARED=True
    dump(L/"fixture_python_build_claim.json",dict(invocations=1,max_fixtures=2,max_states=12,max_operator_constructions=8,retries=0))
    source_pair_gate()
    np,scipy,sparse,cfg=dependencies()
    op=load_exact_snapshot("python_source","r9_exact_frozen_operator")
    ix=load_exact_snapshot("indexing_source","r9_exact_frozen_indexing")
    assert op.assemble_source_operator.__module__==op.__name__ and op.assemble_source_axis.__module__==op.__name__
    counts={"assemble_source_operator":0,"assemble_source_axis":0}
    codes={op.assemble_source_operator.__code__:"assemble_source_operator",op.assemble_source_axis.__code__:"assemble_source_axis"}
    def profile(frame,event,arg):
        if event=="call" and frame.f_code in codes:counts[codes[frame.f_code]]+=1
    prepared=[];records=[];outputs={};index_records=[]
    for q in (1,2):
        payload=fixture_payload(q);path=L/("fixture_"+str(q)+".json")
        raw=json.dumps(payload,sort_keys=True,separators=(",",":"),allow_nan=False).encode("ascii")
        with path.open("xb") as f:f.write(raw)
        common=safe(path).read_bytes();assert common==raw
        data=json.loads(common);shape=tuple(data["shape"]);M=math.prod(shape)
        assert shape==((2,2,2) if q==1 else (3,2,2)) and M in (8,12)
        numbers=[v for key in FIELDS for v in data[key]]+sum(data["switch_matrix"],[])+data["vector"]
        for x in numbers:
            assert type(x) in (int,float) and math.isfinite(x)
            numerator,denominator=float(x).as_integer_ratio()
            assert denominator<=8 and denominator&(denominator-1)==0,"NON_DYADIC_INPUT"
        arrays=[np.asarray(data[key],dtype=np.float64).reshape(shape,order="F") for key in FIELDS]
        roundtrips=[]
        for key,array in zip(FIELDS,arrays):
            flat=np.asarray(data[key],dtype=np.float64)
            assert np.array_equal(ix.flatten(array,shape),flat) and np.array_equal(ix.unflatten(flat,shape),array)
            roundtrips.append(key)
        mapping=[]
        for k in range(M):
            coord=ix.inverse_index(k,shape);assert ix.canonical_index(*coord,shape)==k
            mapping.append(dict(k0=k,coordinate0=list(coord),MATLAB_coordinate1=[x+1 for x in coord],MATLAB_row1=k+1))
        previous=sys.getprofile();assert previous is None,"UNEXPECTED_PROFILE"
        sys.setprofile(profile)
        try:built=op.assemble_source_operator(*arrays,np.asarray(data["switch_matrix"],dtype=np.float64))
        finally:sys.setprofile(previous)
        matrices=dict(zip(NAMES,(built.bb,built.aah,built.bswitch,built.full)))
        assert all(m.shape==(M,M) and m.dtype==np.float64 and np.isfinite(m.data).all() for m in matrices.values())
        output={}
        for name,m in matrices.items():
            coo=m.copy();coo.sum_duplicates();coo=coo.tocoo()
            output[name]=dict(shape=list(m.shape),native_format=m.format,native_stored_nnz=int(m.nnz),dense_F=m.toarray().ravel(order="F").tolist(),coalesced_triplets=[[int(i),int(j),float(v)] for i,j,v in zip(coo.row,coo.col,coo.data)])
        outputs[data["fixture_id"]]=output
        record=dict(fixture_id=data["fixture_id"],shape=list(shape),states=M,input_identity=ident(common),fields_F_roundtrip=roundtrips,mapping=mapping)
        records.append(record);index_records.append(record)
        prepared.append(dict(data=data,arrays=arrays,shape=shape,M=M,matrices=matrices,input_identity=ident(common)))
    assert counts=={"assemble_source_operator":2,"assemble_source_axis":4},"FROZEN_CALL_BUDGET"
    dump(L/"python_matrices_raw.json",outputs)
    dump(L/"fixture_input_indexing_raw.json",dict(fixtures=records,field_formula="pool[(k*(2*f+1)+f+1)%8]",pool=[0,.125,-.25,.5,-.75,.25,-.125,.75],vector_formula="((k%7)-3)/8",fixture_builder_invocations=1))
    dump(L/"python_operator_build_receipt_raw.json",dict(status="PASS",actual_frozen_function_calls=counts,operator_constructions=8,module_mode="exact authenticated snapshot compiled as real module; no function-body changes",operator_snapshot_identity=ident((L/"python_source_fixed_utf8.txt").read_bytes()),index_snapshot_identity=ident((L/"indexing_source_fixed_utf8.txt").read_bytes()),operator_module_file=op.__file__,index_module_file=ix.__file__,dependency_configuration=cfg,fixture_input_identities=[x["input_identity"] for x in prepared],matrices_raw_identity=ident((L/"python_matrices_raw.json").read_bytes()),no_MATLAB_outputs_read=True,linear_solves=0))
    return dict(items=prepared,np=np,sparse=sparse,indexing=ix,fixture_identities=[x["input_identity"] for x in prepared])
def compare_once(prepared):
    global _COMPARED
    assert not _COMPARED,"COMPARATOR_REPLAY";_COMPARED=True
    from scipy.io import loadmat
    np=prepared["np"];sparse=prepared["sparse"];ix=prepared["indexing"]
    dump(L/"comparator_claim.json",dict(invocations=1,atol=1e-12,rtol=1e-12,exact_nonzero_support=True,matrices_budget=8))
    results=[];spots=[];outputs=[];indexing=[];totals=dict(elements=0,support_difference=0,tolerance_failures=0)
    def metric(p,m):
        d=np.abs(p-m);scale=np.maximum(np.abs(p),np.abs(m));relative=np.divide(d,scale,out=np.zeros_like(d),where=scale!=0)
        bad=d>(1e-12+1e-12*scale);where=np.unravel_index(int(np.argmax(d)),d.shape)
        coords=np.argwhere(bad)
        return dict(max_abs_diff=float(np.max(d)),max_rel_diff=float(np.max(relative)),tolerance_failures=int(np.count_nonzero(bad)),maximum_coordinate0=[int(x) for x in where],maximum_python_value=float(p[where]),maximum_MATLAB_value=float(m[where]),first_bad_coordinates0=coords[:8].astype(int).tolist())
    for q,item in enumerate(prepared["items"],1):
        p=L/("matlab_fixture_"+str(q)+".mat");safe(p);raw=p.read_bytes()
        assert 0<len(raw)<=1048576,"MATLAB_OUTPUT_BOUND"
        mat=loadmat(p,mat_dtype=True)
        expected=set(NAMES)|{n+"_mv" for n in NAMES}|{"vector","shp","fixture_input_bytes","input_b_backward_F","input_b_forward_F","input_a_backward_F","input_a_forward_F","index_table"}
        assert {k for k in mat if not k.startswith("__")}==expected,"MATLAB_OUTPUT_FIELDS"
        common=(L/("fixture_"+str(q)+".json")).read_bytes()
        echo=np.asarray(mat["fixture_input_bytes"],dtype=np.uint8).ravel().tobytes()
        assert echo==common and ident(echo)==item["input_identity"],"MATLAB_ACTUAL_INPUT_BYTES"
        shape=item["shape"];M=item["M"]
        assert tuple(np.asarray(mat["shp"]).ravel().astype(int))==shape
        for key,array in zip(FIELDS,item["arrays"]):
            assert np.array_equal(np.asarray(mat["input_"+key+"_F"]).ravel(),ix.flatten(array,shape)),"MATLAB_FLATTEN_ECHO"
        table=np.asarray(mat["index_table"])
        expected_table=np.asarray([[*(x+1 for x in ix.inverse_index(k,shape)),k+1] for k in range(M)])
        assert np.array_equal(table,expected_table),"MATLAB_FORTRAN_INDEX_ORDER"
        indexing.append(dict(fixture=q,all_rows=M,MATLAB_index_table1=table.astype(int).tolist(),F_flat_echoes_match=True,input_byte_echo_identity=ident(echo)))
        arrays_mat={name:mat[name].toarray() if sparse.issparse(mat[name]) else np.asarray(mat[name]) for name in NAMES}
        arrays_py={name:item["matrices"][name].toarray() for name in NAMES}
        assert np.array_equal(arrays_mat["A"],arrays_mat["BB"]+arrays_mat["AAH"]+arrays_mat["Bswitch"]),"MATLAB_OWN_TOTAL"
        assert np.array_equal(arrays_py["A"],arrays_py["BB"]+arrays_py["AAH"]+arrays_py["Bswitch"]),"PYTHON_OWN_TOTAL"
        vector=np.asarray(item["data"]["vector"],dtype=np.float64)
        assert np.array_equal(np.asarray(mat["vector"]).ravel(),vector),"MATLAB_VECTOR_INPUT"
        for name in NAMES:
            pm=item["matrices"][name];mm=mat[name];pd=arrays_py[name];md=arrays_mat[name]
            assert sparse.issparse(mm) and pm.shape==mm.shape==(M,M) and pd.dtype==md.dtype==np.float64,"MATRIX_SHAPE_DTYPE"
            assert np.isfinite(pd).all() and np.isfinite(md).all(),"NONFINITE_MATRIX"
            ps={tuple(map(int,v)) for v in np.argwhere(pd!=0)};ms={tuple(map(int,v)) for v in np.argwhere(md!=0)}
            error=metric(pd,md)
            py_mv=np.asarray(pm@vector).ravel();mat_mv=np.asarray(mat[name+"_mv"]).ravel()
            assert np.isfinite(py_mv).all() and np.isfinite(mat_mv).all() and mat_mv.shape==(M,)
            mv=metric(py_mv,mat_mv)
            symmetric=len(ps^ms)
            result=dict(fixture_id=item["data"]["fixture_id"],matrix=name,shape=[M,M],entries_compared=M*M,python_native_format=pm.format,MATLAB_loaded_format=mm.format,python_native_stored_nnz=int(pm.nnz),MATLAB_native_stored_nnz=int(mm.nnz),python_exact_nonzero_nnz=len(ps),MATLAB_exact_nonzero_nnz=len(ms),python_support0=[list(v) for v in sorted(ps)],MATLAB_support0=[list(v) for v in sorted(ms)],MATLAB_support1=[[i+1,j+1] for i,j in sorted(ms)],support_symmetric_difference_count=symmetric,duplicate_policy="coalesced by source CSR/MATLAB sparse; exact data!=0 support, no tolerance pruning",all_finite=True,**error,python_row_sums=pd.sum(axis=1).tolist(),MATLAB_row_sums=md.sum(axis=1).tolist(),python_diagonal=np.diag(pd).tolist(),MATLAB_diagonal=np.diag(md).tolist(),matvec=dict(vector=vector.tolist(),python=py_mv.tolist(),MATLAB=mat_mv.tolist(),**mv),total_decomposition_both_languages=True)
            result["pass"]=symmetric==0 and error["tolerance_failures"]==0 and mv["tolerance_failures"]==0
            results.append(result);totals["elements"]+=M*M;totals["support_difference"]+=symmetric;totals["tolerance_failures"]+=error["tolerance_failures"]
            if name in ("BB","AAH"):
                axis=0 if name=="BB" else 1;stride=1 if axis==0 else shape[0]
                rb=item["arrays"][0 if axis==0 else 2];rf=item["arrays"][1 if axis==0 else 3]
                for k in range(M):
                    coord=ix.inverse_index(k,shape);back_out=coord[axis]==0;forward_out=coord[axis]==shape[axis]-1
                    diagonal_expected=-(float(rb[coord])+float(rf[coord]))
                    assert float(pd[k,k])==float(md[k,k])==diagonal_expected
                    for sign,rate,outward in ((-1,float(rb[coord]),back_out),(1,float(rf[coord]),forward_out)):
                        col=k+sign*stride if not outward else None
                        record=dict(fixture=q,matrix=name,row0=k,coordinate0=list(coord),direction=sign,axis_python=axis,axis_MATLAB=axis+1,stride=stride,rate=rate,outward=outward,target_column0=col,diagonal_expected=diagonal_expected,python_diagonal=float(pd[k,k]),MATLAB_diagonal=float(md[k,k]),python_row_sum=float(pd[k,:].sum()),MATLAB_row_sum=float(md[k,:].sum()))
                        if col is not None:
                            record.update(python_neighbor=float(pd[k,col]),MATLAB_neighbor=float(md[k,col]))
                            assert float(pd[k,col])==float(md[k,col])==rate
                        spots.append(record)
            if not result["pass"]:
                dump(L/"elementwise_comparison_raw.json",dict(status="FAIL_SOURCE_OPERATOR_ELEMENTWISE_REVIEW_REQUIRED",results=results,totals=totals,remaining_not_compared=True,atol=1e-12,rtol=1e-12))
                raise ParityMismatch("ELEMENT_OR_SUPPORT_OR_MATVEC_MISMATCH")
        outputs.append(dict(fixture=q,output_identity=ident(raw),input_byte_echo_verified=True,matrices=list(NAMES),synthetic_only=True))
    assert len(results)==8 and totals["elements"]==832
    receipt=dict(status="PASS_SYNTHETIC_TWO_FIXTURES_EIGHT_MATRICES_SOURCE_ASSEMBLY_ELEMENTWISE",results=results,totals=totals,atol=1e-12,rtol=1e-12,relative_definition="abs(p-m)/max(abs(p),abs(m)); zero/zero=0",acceptance="abs(p-m)<=atol+rtol*max(abs(p),abs(m)) AND exact support",max_abs_diff=max(x["max_abs_diff"] for x in results),max_rel_diff=max(x["max_rel_diff"] for x in results),operator_count=8,fixtures=2,source_faithful_not_economic_model_equivalence=True)
    dump(L/"elementwise_comparison_raw.json",receipt)
    dump(L/"outward_boundary_stride_raw.json",dict(spots=spots,conservation_not_forced=True,raw_values_source="actual independently built Python and MATLAB matrices; fixture rates only used in separate spotcheck",axis2_strides=[2,3]))
    dump(L/"MATLAB_output_readback_raw.json",dict(outputs=outputs,indexing=indexing,actual_matvec_actions=8,shared_input_raw_bytes_verified=True))
    return receipt
if __name__=="__main__":raise SystemExit("EXPLICIT_R9_ENTRY_REQUIRED")
