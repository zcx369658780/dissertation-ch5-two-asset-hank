"""Capture actual focused unittest bytes; failure stops the caller."""
import base64
import hashlib
import re
import subprocess
import sys
from pathlib import Path
from common import REPO, write

root = Path(sys.argv[1])
command = [sys.executable, '-B', str(REPO / 'tests/test_call725_boundary_generator_repair_spec.py')]
run = subprocess.run(command, cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
raw = run.stdout
attempt = len(list(root.glob('tests_attempt_*.raw.json'))) + 1
prefix = root / f'tests_attempt_{attempt:02d}'
write(prefix.with_suffix('.raw.json'), {'command': command, 'returncode': run.returncode,
    'raw_sha256': hashlib.sha256(raw).hexdigest().upper(), 'base64': base64.b64encode(raw).decode()})
text = raw.decode('utf-8').replace('\r\n', '\n')
prefix.with_suffix('.txt').write_text(text, encoding='utf-8', newline='\n')
count = re.search(r'Ran (\d+) tests?', text)
receipt = {'attempt': attempt, 'returncode': run.returncode,
    'ran': int(count.group(1)) if count else None,
    'individual_ok': len(re.findall(r' \.\.\. ok$', text, re.M)),
    'passed': run.returncode == 0 and bool(re.search(r'^OK$', text, re.M)),
    'raw_sha256': hashlib.sha256(raw).hexdigest().upper(),
    'lf_text_sha256': hashlib.sha256(text.encode()).hexdigest().upper()}
write(prefix.with_suffix('.receipt.json'), receipt)
print(text)
print(receipt)
if not receipt['passed'] or receipt['ran'] != receipt['individual_ok']:
    raise SystemExit(1)
