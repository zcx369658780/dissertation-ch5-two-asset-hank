"""Package existing diagnostic outputs; no model arithmetic or execution."""
import csv
import hashlib
import shutil
import sys
from pathlib import Path
from common import REPO, read, write, identity

root = Path(sys.argv[1])
out = REPO / 'reports/call725_boundary_generator_repair_spec_20260907'
out.mkdir(exist_ok=True)
assert read(root / 'result.json')['snapshots'] == 14
assert not read(root / 'failures.json')
receipts = sorted(root.glob('tests_attempt_*.receipt.json'))
assert read(receipts[-1])['passed']
witnesses = read(root / 'witnesses.json')
checks = [c for group in witnesses.values() for w in group
          for c in w['legacy_reconstruction']['reconstructed_persisted_checks'].values()]
assert all(c['passed'] for c in checks)
count = sum(len(group) for group in witnesses.values())
write(root / 'ledger.json', {'science_calls': {key: 0 for key in (
    'HJB', 'policy_evaluator', 'direct_solve', 'root_solve', 'optimization',
    'condition_estimator', 'MATLAB_process', 'trajectory', 'KFE', 'GE',
    'annual', 'dynamics', 'IRF', 'Results', 'scientific_retry')},
    'saved_snapshots': 14, 'local_legacy_reconstruction_cells': count,
    'reconstructed_scalar_comparisons': len(checks),
    'all_reconstructed_scalar_comparisons_passed': True,
    'postprocessing_scope': 'stored arrays and selected local old expressions only; no complete policy map',
    'test_attempt_receipts': [read(p) for p in receipts]})
source = 'exports/matlab_faithful_two_asset_ha.py'
write(root / 'source_map.json', {'reference_git_blob': '9e7dc9556a2b76811e78f89999abecc045886106',
    'sources': [
        {'path': source, 'lines': '77-110', 'meaning': 'regularized cost versus raw-vb bare-a transfer candidate'},
        {'path': source, 'lines': '159-167,378-399', 'meaning': 'consumed budget drifts and captured fields'},
        {'path': source, 'lines': '306-319', 'meaning': 'consumed boundary-filtered transfer'},
        {'path': source, 'lines': '348-376', 'meaning': 'forced upper-b label, shadow selection, upper-a replacement'},
        {'path': source, 'lines': '403-413', 'meaning': 'split source rates versus net budget rates'},
        {'path': source, 'lines': '427-448', 'meaning': 'omitted exterior edges, retained diagonal'},
        {'path': 'validators/multi_province/call725_policy_operator_stability/diagnose.py', 'symbol': 'branch',
         'meaning': 'accepted local expression reconstruction; AST-equivalent except binding parameter'},
        {'path': 'src/ch5_two_asset_hank/contracts.py', 'symbol': 'GridSpec', 'meaning': 'economic lower-bound identity'}],
    'provenance': 'read-only source references; local reconstruction is not independent runtime capture'})
for name in ('binding_identity.json', 'consumed_inputs.json', 'snapshots.json',
             'result.json', 'ledger.json', 'source_map.json', 'corners.csv',
             'face_feasibility.csv', 'generator_summary.json', 'tail_switch_coordinates.json'):
    # Published text is LF; original external bytes are separately bound by the manifest.
    (out / name).write_text((root / name).read_text(encoding='utf-8'), encoding='utf-8', newline='\n')
for p in root.glob('tests_attempt_*'):
    (out / p.name).write_text(p.read_text(encoding='utf-8'), encoding='utf-8', newline='\n')
with (root / 'anomalous_rows.csv').open(newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))
fields = ['snapshot','row','i_b','i_a','i_z','face','negative_row','leak',
          'outward_budget_violation','budget_b','budget_a','captured_b','captured_a',
          'operator_b','operator_a','row_sum','neighbors_and_signed_A']
with (out / 'anomaly_index.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
    writer.writeheader(); writer.writerows({k:r[k] for k in fields} for r in rows)
selected = []
for key, group in witnesses.items():
    for witness in group:
        row = witness['row']['row']
        if (key == 'matlab_M143_FINAL' and witness['row']['corner'] or
            key == 'matlab_P32' and row == 704 or
            key == 'matlab_trajectory_52' and row == 799 or
            key == 'matlab_trajectory_57' and row == 379 or
            key == 'python_trajectory_146' and row == 399 or
            key in ('python_trajectory_401','python_trajectory_424','python_trajectory_500') and row in (398,790)):
            selected.append(witness)
write(out / 'representative_witnesses.json', selected)
assert len(selected) == 18
print({'output': str(out), 'anomaly_rows': len(rows), 'local_cells': count,
       'scalar_checks': len(checks), 'representative_witnesses': len(selected)})
