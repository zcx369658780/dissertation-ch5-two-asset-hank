"""Persist raw focused-test output and derive counts from the actual unittest run."""
import re
import subprocess
import sys
from pathlib import Path
from common import REPO,write,identity
def main(root):
    n=1
    while (root/f'tests_{n:02d}.log').exists():n+=1
    command=[sys.executable,'-B','-m','unittest','discover','-s','tests','-p','test_call725_frozen_linear_system.py','-v']
    run=subprocess.run(command,cwd=REPO,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    log=root/f'tests_{n:02d}.log';log.write_bytes(run.stdout);text=run.stdout.decode('utf-8',errors='replace')
    matches=re.findall(r'Ran (\d+) tests? in',text);count=int(matches[-1]) if matches else None
    passed=run.returncode==0 and bool(re.search(r'^OK\s*$',text,re.MULTILINE))
    write(root/'checks.json',{'command':command,'exit_code':run.returncode,'tests_run':count,'tests_passed':count if passed else None,'passed':passed,'log':identity(log),
        'count_provenance':'parsed unittest raw log, not an independently executed Reviewer check'})
    print(text);assert passed
if __name__=='__main__':main(Path(sys.argv[1]))
