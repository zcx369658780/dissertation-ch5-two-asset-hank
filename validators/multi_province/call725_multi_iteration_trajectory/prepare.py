"""Generate capture-only trajectory wrappers from the accepted one-step sources."""
import ast
import difflib
import hashlib
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
PRE = Path(r"D:\ProjectTemp\ch5-mp4c-2018-call725-postcall-residual-vectorization-repair-20260904-001")
EVIDENCE = Path(r"D:\ProjectTemp\ch5-call725-multi-iteration-trajectory-20260907-001")
BINDING = Path(r"D:\ProjectTemp\ch5-mp4c-2018-call725-first-iteration-scalar-binding-repair-20260904-001\call725_first_iteration_scalar_binding.json")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def generate_python(original):
    text = original.replace("import hashlib,json,sys", "import hashlib,json,sys,time")
    text = text.replace("REPO=Path(r'D:\\ProjectTemp\\ch5-pre-p5-controlled-household-exec-repo-20260829')", f"REPO=Path({str(REPO)!r})")
    text = text.replace("def main(out,binding_path,certification_only=False):", "def main(output_dir,binding_path,initialization_path,max_updates):\n output_dir.mkdir(parents=True,exist_ok=False)\n if not 1 <= max_updates <= 500: raise ValueError('update budget')\n ledger={'invocations_entered':0,'iterations_entered':0,'solves_entered':0,'completed_updates':0,'converged':False,'status':'INITIALIZING'}\n def persist(): (output_dir/'ledger.json').write_text(json.dumps(ledger,indent=2),encoding='utf-8')\n persist(); started=time.monotonic()")
    text = text.replace("m=loadmat(MAT,squeeze_me=False)", "m=loadmat(initialization_path,squeeze_me=False)")
    text = text.replace(" if certification_only: np.savez_compressed(out,old=old,l0=l0,b=b,a=a,z=z); return\n", "")
    start = text.index(" shape=old.shape")
    end = text.index("if __name__")
    body = text[start:end]
    # Preserve every scientific expression byte-for-byte, changing indentation only.
    body = body.replace("; v1=linalg.spsolve", "; ledger['solves_entered']+=1; persist(); v1=linalg.spsolve")
    prefix = text[:start]
    loop = " ledger['invocations_entered']=1; ledger['status']='RUNNING'; persist()\n try:\n  for iteration in range(1,max_updates+1):\n   if time.monotonic()-started>2650: raise TimeoutError('trajectory wall budget')\n   out=output_dir/f'step_{iteration:04d}.npz'\n   ledger['iterations_entered']+=1; persist()\n"
    body = "".join("  " + line if line.strip() else line for line in body.splitlines(keepends=True))
    tail = """   ledger['completed_updates']+=1
   finite=all(np.isfinite(x).all() for x in [old,v1,rhs,bb,bf,ab,af,*arrays.values(),op.full.data,M.data])
   statistic=float(np.max(abs(v1-old))); ledger['statistic']=statistic if np.isfinite(statistic) else None
   ledger['converged']=bool(finite and statistic<n.convergence_tolerance)
   trace={'iteration':iteration,'statistic':ledger['statistic'],'finite':bool(finite),'converged':ledger['converged'],'diagnostic_continuation':iteration>100,'value_min':float(np.min(v1)) if finite else None,'value_max':float(np.max(v1)) if finite else None}
   with (output_dir/'trace.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps(trace,allow_nan=False)+'\\n'); f.flush()
   persist()
   print(json.dumps(trace),flush=True)
   if not finite: ledger['status']='NONFINITE'; break
   if ledger['converged']: ledger['status']='CONVERGED'; break
   old=v1.copy()
  else: ledger['status']='MAX_UPDATES'
 except BaseException as exc:
  ledger['status']='FAILED'; ledger['error']=repr(exc); raise
 finally:
  persist()
if __name__=='__main__': main(Path(sys.argv[1]),Path(sys.argv[2]),Path(sys.argv[3]),int(sys.argv[4]))
"""
    return prefix + loop + body + tail


def generate_matlab(original):
    # Remove unreachable post-loop distribution/operator work; retain axis helper.
    helper = original[original.index("function G=axis_operator"):]
    body = original[:original.index("\ndh=Idh_B.*dh_B+Idh_F.*dh_F;")]
    body = body.replace("matlab_postcall_vectorized_stagewise_wrapper(manifest_path, initialization_path, output_path, designated_root, certification_only)", "matlab_trajectory(manifest_path, initialization_path, output_dir, designated_root, max_updates)")
    body = body.replace("if nargin < 5; certification_only=false; end", "if max_updates<1 || max_updates>500; error('update budget'); end\nif exist(output_dir,'dir'); error('output directory exists'); end\nmkdir(output_dir);\nledger=struct('invocations_entered',0,'iterations_entered',0,'solves_entered',0,'completed_updates',0,'converged',false,'status','INITIALIZING');\nwrite_ledger(output_dir,ledger); started=tic;")
    body = body.replace("if certification_only; save(output_path,'initial_value','l0','b','ah','z','p','n','switch_matrix','-v7'); return; end\n", "")
    body = body.replace("for iter=1:1\n    V=v;", "ledger.invocations_entered=1; ledger.status='RUNNING'; write_ledger(output_dir,ledger);\ntry\nfor iter=1:max_updates\n    if toc(started)>2650; error('trajectory wall budget'); end\n    output_path=fullfile(output_dir,sprintf('step_%04d.mat',iter));\n    ledger.iterations_entered=ledger.iterations_entered+1; write_ledger(output_dir,ledger);\n    V=v; initial_value=V;")
    body = body.replace("updated=reshape(matrix\\rhs", "ledger.solves_entered=ledger.solves_entered+1; write_ledger(output_dir,ledger); updated=reshape(matrix\\rhs")
    body = body.replace("    return\nend", """    ledger.completed_updates=ledger.completed_updates+1;
    finite=all(isfinite([V(:);updated(:);rhs(:);C(:);l(:);dh(:);adjustment_cost(:);Rah(:);mu_a(:);mu_b(:);u(:);bbB(:);bbF(:);aaB(:);aaF(:);nonzeros(A);nonzeros(matrix)]));
    ledger.statistic=dist; ledger.converged=finite && dist<n.convergence_tolerance;
    trace=struct('iteration',iter,'statistic',dist,'finite',finite,'converged',ledger.converged,'diagnostic_continuation',iter>100,'value_min',min(updated(:)),'value_max',max(updated(:)));
    f=fopen(fullfile(output_dir,'trace.jsonl'),'a'); fprintf(f,'%s\\n',jsonencode(trace)); fclose(f);
    write_ledger(output_dir,ledger); fprintf('STEP %d statistic %.17g\\n',iter,dist);
    if ~finite; ledger.status='NONFINITE'; break; end
    if ledger.converged; ledger.status='CONVERGED'; break; end
end
if strcmp(ledger.status,'RUNNING'); ledger.status='MAX_UPDATES'; end
catch ME
    ledger.status='FAILED'; ledger.error=ME.message; write_ledger(output_dir,ledger); rethrow(ME);
end
write_ledger(output_dir,ledger);
end

function write_ledger(output_dir,ledger)
f=fopen(fullfile(output_dir,'ledger.json'),'w'); fprintf(f,'%s',jsonencode(ledger)); fclose(f);
end""")
    return body + "\n\n" + helper


def main():
    EVIDENCE.mkdir(parents=True, exist_ok=False)
    names = {"python_postcall_vectorized_stagewise_wrapper.py": "FFD218B50BCAE20E2525F5DB806A21200E9DBD0C7E27ABC4CFBA827053CF87E0", "matlab_postcall_vectorized_stagewise_wrapper.m": "43EC8323529DBA9A7638732DC97C22ECB3120966AF65C693E73BDA003A94C9B6"}
    identities=[]
    for name, expected in names.items():
        path=PRE/name
        if sha(path)!=expected: raise ValueError(name)
        original=path.read_text(encoding='utf-8')
        target=HERE/('python_trajectory.py' if name.endswith('.py') else 'matlab_trajectory.m')
        generated=generate_python(original) if name.endswith('.py') else generate_matlab(original)
        if name.endswith('.py'): ast.parse(generated)
        target.write_text(generated,encoding='utf-8')
        (EVIDENCE/(target.stem+'.diff')).write_text(''.join(difflib.unified_diff(original.splitlines(True),generated.splitlines(True),fromfile=name,tofile=target.name)),encoding='utf-8')
        identities.append({'path':str(path),'sha256':expected})
    schema={'mutable_loop_state':{'V':'previous completed updated/v1 tensor; exact (20,20,2), F-order linear mapping'},'immutable_state':['b','ah/a','z','l0','scalar_binding','switch_matrix'], 'recomputed_each_step':['derivatives','policy labels/controls','coefficients','operators','M','RHS'],'stop':'statistic < frozen convergence_tolerance (strict <); nonfinite/fatal; maximum 500; production ceiling 100 unchanged','source_attribution':{'python':'exports/matlab_faithful_two_asset_ha.py:528-559; labor0 assigned once at 524 and never updated','matlab':'protected HJB lines 113-260; V=v, v=V, l0 unchanged; uses accepted one-step source-extracted operator/evaluator semantics'},'replay':'MATLAB pre-step initial_value relabeled v0, plus exact l0/b/ah/z; load same MAT into both evaluators','predecessor_wrappers':identities}
    (EVIDENCE/'state_schema.json').write_text(json.dumps(schema,indent=2)+'\n',encoding='utf-8')
    print('Generated wrappers without importing or calling science')


if __name__=='__main__': main()
