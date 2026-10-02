"""Read-only source/processed-data reconciliation; no model imports or matrices."""
import csv
import hashlib
import json
import math
from pathlib import Path
import sys

sys.path.insert(0, r'C:\Users\zcxve\AppData\Local\Temp\ch5-xls-readonly-20260930-deps')
import xlrd

ROOT = Path(r'D:\ProjectTemp\c5k1bturn56')
SOURCE = Path(r'D:\MatlabProgram\2023年12月2日 多省份神经网络HANK')
OUT = ROOT / 'EVIDENCE/ch5_lagged_observed_gdp_wedge_helper_20260930/raw_2017_readonly_audit.json'
FILES = {
    'gdp': (SOURCE / '地区生产总值 亿元.xls', '0EA17C78F60054ACCA26D0B56402977E560EE3FF4B220D666A5D0E98178F83E7'),
    'population': (SOURCE / '年末常住人口 万人.xls', '565B83873D56B8F9770F46BF897452B08A8850A3A954519643C1370188C09CAA'),
    'panel': (ROOT / 'reports/mp4c_2018_raw_nbs_rebuild_20260910/cleaned_province_year_panel.csv', '774C357E9762A3DFD76373F3440EA8E1D32F2C23FB1F9CDC31A4D77FC9960A5F'),
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()

before = {key: sha(path) for key, (path, expected) in FILES.items()}
for key, (path, expected) in FILES.items():
    if before[key] != expected:
        raise ValueError(f'{key} identity mismatch')

def read_year(path):
    book = xlrd.open_workbook(str(path), on_demand=True)
    try:
        if book.sheet_names() != ['分省年度数据']:
            raise ValueError('unexpected worksheet identity')
        sheet = book.sheet_by_name('分省年度数据')
        headers = sheet.row_values(3)
        columns = [i for i, v in enumerate(headers) if str(v).strip() == '2017年']
        if len(columns) != 1:
            raise ValueError('missing or duplicate 2017 column')
        col = columns[0]
        records = []
        for row in range(4, 35):
            name = sheet.cell_value(row, 0).strip()
            cell = sheet.cell(row, col)
            if cell.ctype != xlrd.XL_CELL_NUMBER or not math.isfinite(cell.value) or cell.value <= 0:
                raise ValueError(f'invalid source value at row {row+1}')
            records.append({'source_province_name': name, 'raw_value': cell.value,
                            'cell': f'{xlrd.formula.colname(col)}{row+1}'})
        if len({r['source_province_name'] for r in records}) != 31:
            raise ValueError('duplicate/missing source provinces')
        return {'sheet': sheet.name, 'shape': [sheet.nrows, sheet.ncols],
                'header_first_four_rows': [sheet.row_values(i) for i in range(4)],
                'footer_rows': [sheet.row_values(i) for i in range(35, sheet.nrows)],
                'year_column_1based': col+1, 'records': records}
    finally:
        book.release_resources()

gdp = read_year(FILES['gdp'][0])
population = read_year(FILES['population'][0])
with FILES['panel'][0].open(encoding='utf-8-sig', newline='') as handle:
    panel = [r for r in csv.DictReader(handle) if r['year'] == '2017']
if len(panel) != 31 or len({r['source_province_name'] for r in panel}) != 31:
    raise ValueError('panel year/province coverage invalid')
g = {r['source_province_name']: r for r in gdp['records']}
p = {r['source_province_name']: r for r in population['records']}
if set(g) != set(p) or set(g) != {r['source_province_name'] for r in panel}:
    raise ValueError('source/panel province sets differ')
checks = []
for record in sorted(panel, key=lambda r: int(r['province_index'])):
    name = record['source_province_name']
    a, b = g[name], p[name]
    checks.append({'province_index': int(record['province_index']), 'province_name': name,
                   'gdp_cell': a['cell'], 'population_cell': b['cell'],
                   'gdp_raw_100m_yuan': a['raw_value'], 'population_raw_10k_persons': b['raw_value'],
                   'gdp_raw_matches_panel': a['raw_value'] == float(record['gdp_raw_100m_yuan']),
                   'population_raw_matches_panel': b['raw_value'] == float(record['population_raw_10k_persons']),
                   'gdp_legacy_scale_x1000_matches_panel': a['raw_value']*1000 == float(record['gdp_model_units_x1000']),
                   'population_legacy_scale_x100_matches_panel': b['raw_value']*100 == float(record['population_model_units_x100'])})
after = {key: sha(path) for key, (path, expected) in FILES.items()}
if before != after:
    raise ValueError('source mutated during read-only check')
data = {'schema': 'CH5_RAW_2017_READONLY_AUDIT_V1', 'date': '2026-09-30',
        'scope': '2017 source cells versus preserved processed panel; no actual wedge matrix',
        'source_hash_before': before, 'source_hash_after': after,
        'source_identity_and_preservation': 'PASS', 'year': 2017,
        'gdp_sheet_readback': gdp, 'population_sheet_readback': population,
        'gdp_population_same_row_order': [r['source_province_name'] for r in gdp['records']] == [r['source_province_name'] for r in population['records']],
        'panel_province_indices': [r['province_index'] for r in checks],
        'checks': checks, 'mismatches': [r for r in checks if not all(r[k] for k in r if k.endswith('matches_panel'))],
        'owner_source_statement': 'direct NBS provincial annual database download, confirmed 2026-09-30',
        'price_basis': 'UNVERIFIED', 'release_vintage': 'UNVERIFIED',
        'model_imports': 0, 'science_calls': 0, 'wedge_matrices': 0, 'original_workbook_writes': 0}
if OUT.exists():
    raise FileExistsError('audit receipt already exists')
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'provinces': len(checks), 'mismatches': len(data['mismatches']),
                  'same_raw_row_order': data['gdp_population_same_row_order'],
                  'gdp_year_column': gdp['year_column_1based'], 'population_year_column': population['year_column_1based'],
                  'unchanged_source_hashes': before == after,
                  'gdp_footer': gdp['footer_rows'], 'population_footer': population['footer_rows']}, ensure_ascii=False))
