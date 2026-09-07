"""Complete trace extrema, loop-state checks and attribution from saved operands."""
import json
import hashlib
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.io import loadmat

from analyze import ROOT, load, sparse_compare, c, write


def derivative_key(left_label,right_label):
    if left_label!=right_label or left_label not in (-1,1):
        raise ValueError('derivative attribution not established for zero/different liquid branches')
    return 'post_boundary_vb_b' if left_label==-1 else 'post_boundary_vb_f'


def main():
    summary={}
    for language,suffix in [('matlab','mat'),('python','npz')]:
        files=sorted(p for p in (ROOT/f'{language}_trajectory').glob(f'step_*.{suffix}') if len(p.stem)==9)
        previous=None; invariant=None; rows=[]
        with (ROOT/f'{language}_stage_extrema.jsonl').open('w',encoding='utf-8') as stream:
            for iteration,path in enumerate(files,1):
                data=load(language,path)
                if invariant is None:invariant={name:data[name].copy() for name in ('l0','b','a','z')}
                carry_pass=previous is None or np.array_equal(data['old/V0'],previous)
                invariant_pass=all(np.array_equal(data[name],value) for name,value in invariant.items())
                matrix_check=sparse_compare(data['M'],(.001+.05)*sparse.eye(800)-data['A'])
                rhs_check=c.compare_dense(data['RHS'],data['utility'].ravel(order='F')+data['old/V0'].ravel(order='F')/1000,(800,))
                statistic_check=c.compare_dense(data['first_iteration_statistic'],np.array([np.max(abs(data['V1']-data['old/V0']))]),(1,),exact=True)
                extrema={}
                for name,value in data.items():
                    # Sparse extrema include implicit zeros, never dense expansion.
                    values=value.data if sparse.issparse(value) else np.asarray(value)
                    finite=bool(np.isfinite(values).all())
                    minimum=float(values.min()) if values.size and finite else 0.
                    maximum=float(values.max()) if values.size and finite else 0.
                    if sparse.issparse(value):minimum=min(0.,minimum);maximum=max(0.,maximum)
                    extrema[name]={'finite':finite,'min':minimum if finite else None,'max':maximum if finite else None}
                residual=c.residual(data['M'],data['RHS'],data['V1'])
                row={'iteration':iteration,'carry_exact':carry_pass,'immutable_inputs_exact':invariant_pass,'M_identity':matrix_check['passed'],'RHS_identity':rhs_check['passed'],'statistic_identity':statistic_check['passed'],'all_stage_values_finite':all(v['finite'] for v in extrema.values()),'residual':residual}
                stream.write(json.dumps(dict(**row,stage_extrema=extrema),allow_nan=False)+'\n');rows.append(row);previous=data['V1']
        summary[language]={'updates_checked':len(rows),'all_loop_carry_exact':all(r['carry_exact'] for r in rows),'immutable_inputs_exact':all(r['immutable_inputs_exact'] for r in rows),'all_M_RHS_statistic_identities_pass':all(r['M_identity'] and r['RHS_identity'] and r['statistic_identity'] for r in rows),'all_stage_values_finite':all(r['all_stage_values_finite'] for r in rows),'all_residuals_finite':all(r['residual']['finite'] for r in rows),'max_residual_inf':max(r['residual']['residual_inf'] for r in rows),'max_backward_error':max(r['residual']['normwise_backward_error'] for r in rows)}
    write(ROOT/'trajectory_integrity.json',summary)
    left=load('matlab',ROOT/'matlab_trajectory/step_0002.mat');right=load('python',ROOT/'python_trajectory/step_0002.npz')
    delta=np.abs(left['consumption']-right['consumption']);idx=tuple(np.unravel_index(np.argmax(delta),delta.shape))
    replay=json.loads((ROOT/'common_state_comparison.json').read_text())
    state_identity=json.loads((ROOT/'replay_state_identity.json').read_text())
    if not replay['passed'] or state_identity['iteration']!=2 or not state_identity['all_fields_exact_readback']:raise ValueError('common-state attribution prerequisite failed')
    if hashlib.sha256(Path(state_identity['path']).read_bytes()).hexdigest().upper()!=state_identity['sha256']:raise ValueError('common-state identity drift')
    label=int(left['liquid_label'][idx]);derivative=derivative_key(label,int(right['liquid_label'][idx]))
    a,b=float(left[derivative][idx]),float(right[derivative][idx])
    attribution={'iteration':2,'maximum_consumption_difference_coordinate':list(map(int,idx)),'physical_coordinate':{'b':float(left['b'][idx[0]]),'a':float(left['a'][idx[1]]),'z':float(left['z'][idx[2]])},'same_consumed_label':bool(left['liquid_label'][idx]==right['liquid_label'][idx]),'label':label,'derivative_field':derivative,'matlab_derivative':a,'python_derivative':b,'derivative_absolute_difference':abs(a-b),'matlab_consumption':float(left['consumption'][idx]),'python_consumption':float(right['consumption'][idx]),'consumption_absolute_difference':float(delta[idx]),'source_expression':'max(vb,1e-6)**(-1/gamma), gamma=2; no evaluator invoked','arithmetic_replay_on_persisted_derivatives':[max(a,1e-6)**(-.5),max(b,1e-6)**(-.5)],'local_absolute_slope':.5*max(a,1e-6)**(-1.5),'interpretation':'Accepted tiny incoming V differences amplify in derivative/consumption arithmetic; same-state replay separately tests local cross-language agreement.'}
    write(ROOT/'earliest_difference_attribution.json',attribution)
    print(json.dumps({'integrity':summary,'attribution':attribution},indent=2))


if __name__=='__main__':main()
