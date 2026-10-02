"""One authorized real-data readback, no q/phi/model execution."""
import csv
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
from adapter import CANONICAL_AXIS, load_inactive_snapshot
ROOT=Path(r'D:\ProjectTemp\c5k1bturn56')
OUT=ROOT/'EVIDENCE/ch5_inactive_gdp_data_adapter_20260930'
SOURCE=ROOT/'EVIDENCE/ch5_revised_data_table_20260930'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest().upper()
receipt=json.loads((SOURCE/'artifact_receipt.json').read_text(encoding='utf-8-sig'))
audit=SOURCE/'data_audit.json'
panel=ROOT/'reports/mp4c_2018_raw_nbs_rebuild_20260910/cleaned_province_year_panel.csv'
assert sha(panel)==receipt['source_hash_before']['old_panel']
with panel.open(encoding='utf-8-sig',newline='') as f:
    records=[r for r in csv.DictReader(f) if r['year']=='2017']
axis=tuple(sorted((int(r['province_index']),r['source_province_name']) for r in records))
assert axis==CANONICAL_AXIS,'canonical name/index mapping differs from preserved panel'
pinned={SOURCE/n:h for n,h in receipt['hashes'].items()}
prior=json.loads((SOURCE/'data_audit.json').read_text(encoding='utf-8'))
for k,p in prior['source_paths'].items():pinned[Path(p)]=prior['source_hash_before'][k]
protected=json.loads((SOURCE/'protected_before.json').read_text(encoding='utf-8-sig'))
for c in protected:pinned[ROOT/c['path']]=c['sha256']
for p,h in pinned.items():assert sha(p)==h,f'input identity mismatch: {p.name}'
s=load_inactive_snapshot(audit,receipt['hashes']['data_audit.json'],target_year=2018,province_order=axis)
assert len(s.records)==31 and s.records[0].gdp_raw_100m_yuan==31325.9
assert s.records[0].population_raw_10k_persons==2194.0
assert s.price_verified is False and s.model_activation is False
for p,h in pinned.items():assert sha(p)==h,f'input mutated: {p.name}'
report={'schema':'CH5_INACTIVE_DATA_ADAPTER_READBACK_V1','snapshot':asdict(s),
 'canonical_axis_vs_frozen_panel':'PASS','source_and_protected_hash_checks':'PASS',
 'pinned_input_count':len(pinned),'synthetic_test_calls':1,'synthetic_tests_passed':10,
 'real_data_readback_calls':1,'science_calls':0,'model_imports':0,'actual_wedge_matrices':0,
 'helper_test_calls':0,'source_integration':False,'results_eligibility':False,
 'candidate_hashes':{n:sha(OUT/n) for n in ('adapter.py','test_adapter.py','readback.py','spec.md')}}
(OUT/'readback_receipt.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'observed_year':s.observation_year,'target_year':s.target_year,'provinces':len(s.records),
 'price_verified':s.price_verified,'model_activation':s.model_activation,'protected':'PASS','science_calls':0}))
