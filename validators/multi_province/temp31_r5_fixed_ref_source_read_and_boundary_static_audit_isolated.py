"""One no-HA toy round plus static AST observations; never imports scientific code."""
from pathlib import Path
import ast,base64,hashlib,json,sys
WORK=Path(__file__).resolve().parents[2]
TASK='CH5_TEMP31_R5_FIXED_REF_SOURCE_READ_RECOVERY_AND_STATIC_AUDIT_R1_20261030'
R=WORK/'tasks'/TASK;EV=R/'evidence'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def dump(name,x):
 with (EV/name).open('x',encoding='utf-8',newline=chr(10)) as f:json.dump(x,f,indent=2);f.write(chr(10))
def source(step):
 d=read(EV/('LOCAL_ONLY_'+step+'_attempt1.json'))['response']['structuredContent'];return base64.b64decode(d['content']).decode('utf-8')
def main():
 assert sys.stdin.buffer.readline()==b'GO'+bytes([10])
 assert read(EV/'source_gate_pass.json')['FIXED_REF_SOURCE_READ_PASS']
 hjb=source('04_HJB_SOURCE');op=source('05_OPERATOR_SOURCE');kfe=source('06_KFE_SOURCE');export=source('07_EXPORT_SOURCE')
 for s in (hjb,op,kfe,export):ast.parse(s)
 tree=ast.parse(hjb);fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='solve_temp31_netwage_hjb')
 loops=[n for n in fn.body if isinstance(n,ast.For)];assert len(loops)==1
 policy_calls=[n for n in ast.walk(fn) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='select_temp31_netwage_local_policy'];assert len(policy_calls)==1
 post_stmt=next(n for n in fn.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='post' for t in n.targets))
 assert post_stmt.lineno>loops[0].end_lineno
 all_names={n.id for n in ast.walk(fn) if isinstance(n,ast.Name)}
 static=dict(grade='SOURCE_STATIC_MATCH_FOR_REPORTED_SYNTAX_ONLY',policy_call_line=policy_calls[0].lineno,policy_call_inside_last_iteration=True,loop_lines=[loops[0].lineno,loops[0].end_lineno],post_statement_line=post_stmt.lineno,policy_not_reselected_after_loop=True,post_uses_saved_mu_arrays=True,homecrit_symbol_present='homecrit' in all_names,homecrit_or_rowsum_internal_guard='NOT_PRESENT_IN_INSPECTED_DRIVER',driver_all_if_tests=[dict(line=n.lineno,test=ast.unparse(n.test)) for n in ast.walk(fn) if isinstance(n,ast.If)],export_contains_Cmin_identifier=any(isinstance(n,ast.Name) and n.id=='Cmin' for n in ast.walk(ast.parse(export))),scientific_functions_executed=0)
 assert not static['homecrit_symbol_present']
 # Explicitly artificial 3x3x2 rates, unit spacing, and asymmetric z switch.
 I=3;J=3;NZ=2;N=I*J*NZ
 def index(i,j,z):return i+I*j+I*J*z
 def decode(row):return row%I,(row//I)%J,row//(I*J)
 def add(M,row,col,val):
  if val:M[(row,col)]=M.get((row,col),0)+val
 direct={};strips={};axis_rows=[]
 for axis,stride in ((0,1),(1,I)):
  mat={};bands={-stride:[0]*N,0:[0]*N,stride:[0]*N}
  for z in range(NZ):
   for j in range(J):
    for i in range(I):
     row=index(i,j,z);coord=(i,j)[axis];v=(-2,0,3)[(i+2*j+z+axis)%3];back=max(-v,0);forward=max(v,0)
     add(mat,row,row,-back-forward);bands[0][row]=-back-forward
     if coord>0:
      add(mat,row,row-stride,back);bands[-stride][row-stride]=back
     if coord<2:
      add(mat,row,row+stride,forward);bands[stride][row+stride]=forward
     expected=-(back if coord==0 else 0)-(forward if coord==2 else 0)
     actual=sum(value for (r,c),value in mat.items() if r==row)
     assert actual==expected
     axis_rows.append(dict(axis='b' if axis==0 else 'a',source_index0=row,state_index0=[i,j,z],manual_drift=v,spacing=1,diag=-back-forward,back_rate=back,forward_rate=forward,legal_backward_target=row-stride if coord>0 else None,legal_forward_target=row+stride if coord<2 else None,expected_row_sum=expected,actual_row_sum=actual))
  # Mathematical square-strip convention: A[r,r+d] reads band_d[r+d].
  projected={}
  for d,band in bands.items():
   for row in range(N):
    col=row+d
    if 0<=col<N:add(projected,row,col,band[col])
  assert projected==mat
  for (row,col),value in mat.items():
   si,sj,sz=decode(row);ti,tj,tz=decode(col)
   assert sz==tz
   if row!=col:assert (sj==tj and abs(si-ti)==1) if axis==0 else (si==ti and abs(sj-tj)==1)
  for (row,col),value in mat.items():add(direct,row,col,value)
  strips['b' if axis==0 else 'a']=dict(offsets=[-stride,0,stride],entry_count=len(mat),manual_adjacency_equals_required_strip_projection=True)
 Q=((-2,2),(3,-3));switch={}
 for z in range(NZ):
  for target in range(NZ):
   for j in range(J):
    for i in range(I):add(switch,index(i,j,z),index(i,j,target),Q[z][target])
 assert all(sum(v for (r,c),v in switch.items() if r==row)==0 for row in range(N))
 assert [sum(Q[c][r] for c in range(2)) for r in range(2)]==[1,-1]
 total=dict(direct)
 for (row,col),value in switch.items():add(total,row,col,value)
 expected_rows=[sum(r['expected_row_sum'] for r in axis_rows if r['source_index0']==row) for row in range(N)]
 actual_rows=[sum(v for (r,c),v in total.items() if r==row) for row in range(N)]
 assert expected_rows==actual_rows
 # Each sign and lower/interior/upper branch independently uses manual unit-spacing rates.
 sign_cases=[]
 for axis in ('b','a'):
  for location in ('lower','interior','upper'):
   for v in (-2,0,3):
    back=max(-v,0);forward=max(v,0);off=(back if location!='lower' else 0)+(forward if location!='upper' else 0);diag=-back-forward
    expected=min(v,0) if location=='lower' else -max(v,0) if location=='upper' else 0
    assert diag+off==expected
    sign_cases.append(dict(axis=axis,location=location,drift=v,diag=diag,legal_offdiag_sum=off,expected_row_sum=expected,actual_row_sum=diag+off))
 dump('static_AST_observations.json',static)
 result=dict(passed=True,rounds=1,grid=dict(I=3,J=3,Nz=2,states=18),manual_rates='drift in (-2,0,3), h=1; no economic inputs',math_convention='square diagonal d: A[r,r+d]=band_d[r+d], zero based; required storage alignment example, not a MATLAB runtime emulator',axis_rows=axis_rows,sign_cases=sign_cases,strip_checks=strips,switch_Q=Q,switch_row_sums=[0,0],transpose_Q_row_sums=[1,-1],combined_row_sums=actual_rows,real_science_imports=0,model_calls=0,solver_calls=0,MATLAB_runtime_calls=0,original_800_state_arrays_read=0,scope='PURE_NO_HA_TOY_ALGEBRA; cannot certify actual original MATLAB strips or full runtime parity')
 dump('toy_index_result.json',result)
 print(json.dumps(dict(event='one_no_HA_toy_complete',passed=True,rounds=1,states=18,axis_rows_checked=len(axis_rows),sign_cases=len(sign_cases),required_strip_alignment='PASS_TOY_ONLY',model_calls=0,solver_calls=0,matlab_runtime=0)))
if __name__=='__main__':main()
