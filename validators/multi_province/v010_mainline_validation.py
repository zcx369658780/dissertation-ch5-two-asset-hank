"""Frozen synthetic driver. One process; persistent stage-specific call ledger.

Run only with a new output directory. A scientific failure stops every dependent
stage and is preserved, rather than being changed into a successful exit status.
"""
from __future__ import annotations
import argparse
from dataclasses import asdict, is_dataclass
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import time

REPO=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(REPO/'src'))
import numpy as np
from ch5_two_asset_hank.multi_province.mainline_household_runtime import (
    HAInputs, ScienceFailure, solve_conditioned_household, seal_json,
)
from ch5_two_asset_hank.multi_province.one_turn import PreFrozenHouseholdOutputBatch
from ch5_two_asset_hank.multi_province.stationary_runtime import (
    mainline_initial_states, run_mainline_stationary, verify_mainline_frozen,
)
from ch5_two_asset_hank.multi_province.mainline_response import run_mainline_response


def serial(value):
    if is_dataclass(value): return serial(asdict(value))
    if isinstance(value,np.ndarray): return value.tolist()
    if isinstance(value,np.generic): return value.item()
    if isinstance(value,dict): return {str(k):serial(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)): return [serial(v) for v in value]
    return value


def main():
    parser=argparse.ArgumentParser();parser.add_argument('output');args=parser.parse_args()
    output=Path(args.output);output.mkdir(parents=True,exist_ok=False)
    raw=(REPO/'tests/fixtures/v010_mainline_synthetic_v1.json').read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if blob != '40915658d93403cfc21b33a6b864b332b7857749':
        raise ScienceFailure('FROZEN_FIXTURE_BYTE_IDENTITY')
    fixture=json.loads(raw)
    ledger={'stage_attempts':{k:0 for k in ('binding','outer','verify','response_zero','response_tfp')},
            'HA_attempts':0,'roots':0,'cells':0,'completed_HA':0,'failures':[],
            'stages':{},'start_utc':datetime.now(timezone.utc).isoformat(),
            'fixture_blob':blob,'fixture_SHA256':hashlib.sha256(raw).hexdigest().upper()}
    limits={'binding':2,'outer':10,'verify':2,'response_zero':6,'response_tfp':6}
    started=time.monotonic()
    def persist():
        # Mutable operation ledger, independent of immutable attempt receipts.
        (output/'ledger.json').write_text(json.dumps(serial(ledger),indent=2,sort_keys=True,
               allow_nan=False)+'\n',encoding='utf-8',newline='\n')
    def attempt(state,stage):
        if ledger['stage_attempts'][stage] >= limits[stage] or ledger['HA_attempts'] >= 26:
            raise ScienceFailure('STAGE_HA_BUDGET')
        ledger['stage_attempts'][stage]+=1;ledger['HA_attempts']+=1;persist()
        inp=HAInputs(state['rb'],state['rah'],state['w_eff'],state['Tt'],state['rb_gap'],
                     fixture['parameters'],fixture['grid'])
        try:
            value,diagnostic=solve_conditioned_household(inp,output/f"HA_{ledger['HA_attempts']:02d}_{stage}",ledger)
            ledger['completed_HA']+=1
            return value,diagnostic
        finally:
            persist()
    def solve_batch(states,stage):
        rows=[attempt(state,stage) for state in states]
        results=[r[0] for r in rows]
        return PreFrozenHouseholdOutputBatch(
            [r.Ct for r in results],[r.Lt for r in results],[r.At for r in results],
            [r.Bt for r in results],[r.AtTax for r in results],tuple(r.converged for r in results),
            tuple(dict(r[1],strict_qualified=True) for r in rows))
    terminal='ENGINEERING_IMPLEMENTED__SCIENCE_FAIL_CLOSED'
    try:
        states=mainline_initial_states(fixture)
        first,proof1=attempt(states[0],'binding')
        second,proof2=attempt(states[0],'binding')
        if asdict(first) != asdict(second) or proof1['V0'] != proof2['V0']:
            raise ScienceFailure('SAME_INPUT_BINDING_MISMATCH')
        ledger['stages']['binding']='PASS';persist()
        outer=run_mainline_stationary(fixture,solve_batch)
        seal_json(output/'outer.json',serial(outer))
        ledger['stages']['outer']=outer['status'];persist()
        if outer['status'] != 'OUTER_ITERATION_CONVERGED':
            raise ScienceFailure(outer['status'])
        verified=verify_mainline_frozen(fixture,outer,solve_batch)
        seal_json(output/'frozen.json',serial(verified))
        ledger['stages']['verify']=verified['status'];persist()
        if verified['status'] != 'TARGET_CALIBRATION_VERIFIED':
            raise ScienceFailure(verified['status'])
        for zero in (True,False):
            response=run_mainline_response(fixture,verified,solve_batch,zero=zero)
            seal_json(output/('zero.json' if zero else 'TFP.json'),serial(response))
            if zero and any(abs(v)>1e-9 for h in response['history'] for row in h['relative_response']
                            for v in row.values() if v is not None):
                raise ScienceFailure('ZERO_SHOCK_DOES_NOT_RETURN_TO_BASELINE')
            ledger['stages']['response_zero' if zero else 'response_tfp']='DIAGNOSTIC_COMPLETED'
        terminal='SYNTHETIC_MAINLINE_GATES_COMPLETED__NOT_REAL_GE_OR_RESULTS'
    except Exception as exc:
        ledger['failures'].append({'type':type(exc).__name__,'reason':str(exc)})
    finally:
        ledger.update(terminal=terminal,wall_seconds=time.monotonic()-started,
                      end_utc=datetime.now(timezone.utc).isoformat(),
                      REAL_GE=False,Results=False,model_activation=False)
        persist()
        print(json.dumps(serial(ledger),sort_keys=True))
    return 0 if not ledger['failures'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
