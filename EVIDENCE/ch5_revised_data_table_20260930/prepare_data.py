"""Standalone source-table audit only. No model imports or calculations."""
import csv, hashlib, json, math, sys
from pathlib import Path
sys.path.insert(0, r'C:\Users\zcxve\AppData\Local\Temp\ch5-xls-readonly-20260930-deps')
import xlrd
ROOT=Path(r'D:\ProjectTemp\c5k1bturn56')
OUT=ROOT/'EVIDENCE/ch5_revised_data_table_20260930'
SRC=Path(r'D:\MatlabProgram\2023年12月2日 多省份神经网络HANK')
FILES={
 'old_gdp':(SRC/'地区生产总值 亿元.xls','0EA17C78F60054ACCA26D0B56402977E560EE3FF4B220D666A5D0E98178F83E7'),
 'old_population':(SRC/'年末常住人口 万人.xls','565B83873D56B8F9770F46BF897452B08A8850A3A954519643C1370188C09CAA'),
 'old_panel':(ROOT/'reports/mp4c_2018_raw_nbs_rebuild_20260910/cleaned_province_year_panel.csv','774C357E9762A3DFD76373F3440EA8E1D32F2C23FB1F9CDC31A4D77FC9960A5F')}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest().upper()
before={k:sha(p) for k,(p,h) in FILES.items()}
assert all(before[k]==h for k,(p,h) in FILES.items()),'source identity mismatch'
def raw(p):
 b=xlrd.open_workbook(str(p),on_demand=True)
 try:
  assert b.sheet_names()==['分省年度数据']
  s=b.sheet_by_index(0); result={}
  for y in range(2015,2019):
   cols=[i for i,x in enumerate(s.row_values(3)) if str(x).strip()==f'{y}年']
   assert len(cols)==1
   c=cols[0]
   for r in range(4,35):
    name=s.cell_value(r,0).strip(); v=s.cell_value(r,c)
    assert isinstance(v,(int,float)) and math.isfinite(v) and v>0
    assert (name,y) not in result
    result[name,y]={'value':v,'cell':f'{xlrd.formula.colname(c)}{r+1}'}
  return result
 finally: b.release_resources()
def displayed(filename,indicator):
 d=json.loads((OUT/filename).read_text(encoding='utf-8'))
 assert d['indicator']==indicator
 t=d['tables']; assert len(t)==4 and len(t[1])==31 and len(t[3])==31
 years=[int(x[:-1]) for x in t[0][0][1:5]]
 assert years==[2018,2017,2016,2015]
 names=[r[0] for r in t[3]]; assert len(set(names))==31
 result={}
 for name,row in zip(names,t[1]):
  assert len(row)==5 and row[0]==''
  for y,txt in zip(years,row[1:]):
   v=float(txt); assert math.isfinite(v) and v>0
   result[name,y]=v
 return result,names,d['captured_at']
og=raw(FILES['old_gdp'][0]); op=raw(FILES['old_population'][0])
ng,names,gdate=displayed('nbs_gdp_display.json','地区生产总值 (亿元)')
np,pnames,pdate=displayed('nbs_population_display.json','年末常住人口 (万人)')
assert names==pnames and set(og)==set(op)==set(ng)==set(np) and len(ng)==124
with FILES['old_panel'][0].open(encoding='utf-8-sig',newline='') as f:
 panel={(r['source_province_name'],int(r['year'])):r for r in csv.DictReader(f) if 2015<=int(r['year'])<=2018}
assert len(panel)==124 and set(panel)==set(og)
rows=[]; old_matches=0
for name in names:
 for y in range(2015,2019):
  k=(name,y); pg=panel[k]
  assert float(pg['gdp_raw_100m_yuan'])==og[k]['value']
  assert float(pg['population_raw_10k_persons'])==op[k]['value']
  old_matches+=2
  rows.append({'province':name,'year':y,'old_gdp':og[k]['value'],'new_gdp':ng[k],
   'old_population':op[k]['value'],'new_population':np[k],
   'old_gdp_cell':og[k]['cell'],'old_population_cell':op[k]['cell']})
after={k:sha(p) for k,(p,h) in FILES.items()}; assert before==after
audit={'schema':'CH5_REVISED_DATA_CANDIDATE_V1','date':'2026-09-30','records':rows,
 'coverage':{'provinces':31,'years':[2015,2016,2017,2018],'province_year_rows':124,'new_numeric_values':248},
 'old_raw_panel_matching_values':old_matches,
 'gdp_changed':sum(r['new_gdp']!=r['old_gdp'] for r in rows),
 'population_changed':sum(r['new_population']!=r['old_population'] for r in rows),
 'gdp_price_basis':'Current-price interpretation supported by NBS Yearbook 2023 table 3-9 absolute-level note; current database page does not independently label price basis. Exact-release price binding remains pending.',
 'population_basis':'year_end_resident; persons, not households; no divide by three',
 'gdp_vintage':'NBS displayed current series after fifth economic census historical revision; exact release date not displayed',
 'population_vintage':'NBS current displayed series; exact release/revision date not displayed',
 'source_paths':{k:str(p) for k,(p,h) in FILES.items()},'source_hash_before':before,'source_hash_after':after,
 'display_capture_times':{'gdp':gdate,'population':pdate},
 'display_hashes':{n:sha(OUT/n) for n in ['nbs_gdp_dom.txt','nbs_gdp_display.json','nbs_population_dom.txt','nbs_population_display.json']},
 'science_calls':0,'model_imports':0,'wedge_matrices':0,'model_activation':False,'results_eligibility':False}
(OUT/'data_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:audit[k] for k in ['coverage','old_raw_panel_matching_values','gdp_changed','population_changed']},ensure_ascii=False))
