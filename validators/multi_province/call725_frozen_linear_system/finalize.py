"""Publish compact diagnostics and a finite evidence receipt without circular hashes."""
from datetime import datetime,timezone
import base64
import re
import shutil
import sys
from pathlib import Path
from common import HERE,REPO,read,write,identity,sha

def main(root):
    out=REPO/'reports/call725_frozen_linear_system_20260907';out.mkdir(exist_ok=True)
    test=read(root/'checks.json');log=Path(test['log']['path'])
    assert sha(log)==test['log']['sha256']
    text=log.read_bytes().decode('utf-8');count=int(re.findall(r'Ran (\d+) tests? in',text)[-1])
    assert test['tests_run']==count and test['tests_passed']==count and test['passed'] and test['exit_code']==0
    warnings={}
    for p in sorted(root.glob('*_process.json')):
        process=read(p);key=process['language']+'_'+process['case'];raw=root/f'{key}.log'
        # Keep original bytes. MATLAB console is GB18030 on this Windows runtime.
        decoded=raw.read_bytes().decode('gb18030' if process['language']=='matlab' else 'utf-8')
        warnings[key]={'runtime_warning_receipt':read(root/key/'warnings.json'),'raw_log':identity(raw),
            'decoded_console':decoded,'decoding':'GB18030' if process['language']=='matlab' else 'UTF-8',
            'note':'Original JSON warning text may contain replacement characters; raw console bytes and decoded text are retained.'}
    write(root/'warnings_summary.json',warnings)
    write(root/'engineering_notes.json',{'scientific_failures':read(root/'execution_failures.json'),'ineligible':read(root/'ineligible.json'),
        'encoding_recovery':'MATLAB JSON warning message contains replacement characters. Preserved it and decoded original process log bytes with GB18030; no solve rerun.',
        'tests':'Initial binding-only run and subsequent expanded diagnostic runs retained; final counts parsed from latest raw log.',
        'python_timer':'Worker time.monotonic solve durations rounded to 0 on this host; process wall times retained. Do not interpret 0 as no solve.',
        'publication_check_failure':'Raw focused_tests.log bytes differed after Git CRLF normalization. The shell continued to commit/push 30438ea despite the assertion exit. Follow-up non-force commit adds exact-byte base64 log, retaining initial publication history. No science rerun.',
        'evidence_directory_created_utc':datetime.fromtimestamp(root.stat().st_ctime,timezone.utc).isoformat(),
        'finalized_utc':datetime.now(timezone.utc).isoformat(),
        'evidence_window_seconds':datetime.now(timezone.utc).timestamp()-root.stat().st_ctime})
    prior=read(root/'predecessor_comparisons.json')
    write(out/'predecessor_comparisons.json',{'provenance':prior['provenance'],'P32':prior['P32'],
        'origin_fidelity':{k:{'passed':v['passed'],'fields':len(v['rows']),'fields_passed':sum(r['passed'] for r in v['rows'])} for k,v in prior['origin_fidelity'].items()},
        'prior_tests':prior['prior_tests']})
    for name in ('result.json','systems.json','consumed_inputs.json','comparisons.json','attribution.json','residuals.json','representation.json',
                 'loaded_input_checks.json','call_ledger.json','checks.json','warnings_summary.json','engineering_notes.json'):
        shutil.copyfile(root/name,out/name)
    shutil.copyfile(log,out/'focused_tests.log')
    raw=log.read_bytes()
    raw_payload={'encoding':'base64','raw_sha256':sha(log),'raw_bytes':len(raw),'content':base64.b64encode(raw).decode('ascii'),
        'readable_log':'focused_tests.log may be newline-normalized by Git; decode this payload for byte-identical original unittest output'}
    assert base64.b64decode(raw_payload['content'])==raw
    write(out/'focused_tests_raw.json',raw_payload)
    # Original stage rows, actual warnings, exact input receipts and all equation-unit
    # residual summaries are small JSON. Residual vectors and sparse payloads stay local.
    excluded={'manifest.json','manifest_readback.json','publication_receipt.json'}
    artifacts=[identity(p) for p in sorted(root.rglob('*')) if p.is_file() and p.name not in excluded]
    files=list(HERE.glob('*.py'))+list(HERE.glob('*.m'))+[REPO/'tests/test_call725_frozen_linear_system.py',REPO/'docs/CH5_MP4C_CALL725_FROZEN_LINEAR_SYSTEM_ATTRIBUTION_REPORT.md']
    files+=list(p for p in out.iterdir() if p.is_file() and p.name!='evidence_manifest_receipt.json')
    files+=[REPO/'tasks/CH5_MP4C_CALL725_FROZEN_LINEAR_SYSTEM_ATTRIBUTION.md',REPO/'docs/CH5_MP4C_CALL725_POLICY_OPERATOR_STABILITY_ACCEPTANCE.md']
    manifest={'baseline':'80ce3f25ecc4455df15206d6ecab3909552f1b61','protocol':'finite artifacts/sources; self and terminal receipts excluded',
        'artifacts':artifacts,'sources_and_reports':[identity(p) for p in sorted(files)],'consumed_inputs_receipt':identity(root/'consumed_inputs.json')}
    write(root/'manifest.json',manifest)
    for r in manifest['artifacts']+manifest['sources_and_reports']:assert sha(r['path'])==r['sha256']
    receipt={'passed':True,'manifest':identity(root/'manifest.json'),'artifact_count':len(artifacts),'source_report_count':len(files),
        'test_log':identity(log),'tests_run_parsed':count,'tests_passed_parsed':test['tests_passed'],'receipt_excluded_from_manifest':True}
    write(root/'manifest_readback.json',receipt);write(out/'evidence_manifest_receipt.json',receipt)
    print(receipt)
if __name__=='__main__':main(Path(sys.argv[1]))
