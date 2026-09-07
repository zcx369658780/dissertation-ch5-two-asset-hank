"""Finite raw-external / LF-repository manifest and independent readback."""
import hashlib
import sys
from pathlib import Path
from common import REPO, read, write, sha

root = Path(sys.argv[1])
out = REPO / 'reports/call725_boundary_generator_repair_spec_20260907'
excluded = {'manifest.json', 'manifest_readback.json', 'publication_receipt.json'}
report = REPO / 'docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_REPORT.md'
paths = list(root.iterdir()) + list(out.iterdir()) + list(Path(__file__).parent.glob('*.py')) + [
    report, REPO / 'tests/test_call725_boundary_generator_repair_spec.py']
entries = []
for p in sorted(paths):
    if not p.is_file() or p.name in excluded:
        continue
    external = not p.is_relative_to(REPO)
    data = p.read_bytes() if external else p.read_text(encoding='utf-8').replace('\r\n','\n').encode()
    entries.append({'path': str(p), 'repository_path': None if external else p.relative_to(REPO).as_posix(),
        'mode': 'raw_bytes' if external else 'utf8_LF', 'bytes': len(data),
        'sha256': hashlib.sha256(data).hexdigest().upper()})
manifest = {'base_main': '6de422f3125045ca23f0464de9013a22ac77e3fc',
    'evidence_root': str(root), 'entries': entries,
    'excludes': sorted(excluded), 'finite_scope': 'new artifacts only; predecessor inputs bound by consumed_inputs receipt'}
write(root / 'manifest.json', manifest)
(out / 'manifest.json').write_bytes((root / 'manifest.json').read_bytes())
verified = 0
for item in read(root / 'manifest.json')['entries']:
    p = Path(item['path'])
    data = p.read_bytes() if item['mode'] == 'raw_bytes' else p.read_text(encoding='utf-8').replace('\r\n','\n').encode()
    assert len(data) == item['bytes'] and hashlib.sha256(data).hexdigest().upper() == item['sha256'], str(p)
    verified += 1
receipt = {'passed': True, 'manifest_sha256': sha(root / 'manifest.json'), 'entries_verified': verified,
    'repository_manifest_bytes_equal': (out / 'manifest.json').read_bytes() == (root / 'manifest.json').read_bytes()}
write(root / 'manifest_readback.json', receipt); write(out / 'manifest_readback.json', receipt)
print(receipt)
