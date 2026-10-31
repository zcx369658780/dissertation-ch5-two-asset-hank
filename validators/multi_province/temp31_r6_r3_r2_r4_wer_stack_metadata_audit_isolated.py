"""One bounded read-only Event/WER metadata audit; no crash-file contents.

Imports perform no environment, filesystem or registry observations. Main uses
five fixed standard roots, two registry keys and one exact latest prefdir.
Only the single fixed PowerShell Application-log query child is permitted.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import time
import winreg
from datetime import datetime, timezone

TASK = 'CH5_TEMP31_R6_R3_R2_R4_WER_STACK_METADATA_AUDIT_20261031'
GOV = '83e17a51b3d4ff41280a4b8ed684867fe34cfac2'
START = '2026-10-31T00:26:00Z'
END = '2026-10-31T01:01:00Z'
ANCHOR = '2026-10-31T00:31:35.050422Z'
LATEST = 'tasks/CH5_TEMP31_R6_R3_R2_R3_EXPLICIT_NATIVE_120S_20261031/LOCAL_ONLY/R3_NATIVE_RUNTIME/matlab_prefdir_fresh'
REG_BASE = r'SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps'
BLOCKED = {'NO_PERMISSION', 'REPARSE_BLOCKED', 'NOT_AVAILABLE', 'QUERY_FAILED', 'ENV_NOT_AVAILABLE'}
POWERSHELL_QUERY = r"""
$ErrorActionPreference='Stop'
[Console]::OutputEncoding=New-Object System.Text.UTF8Encoding($false)
$start=[DateTimeOffset]::Parse('2026-10-31T00:26:00Z').UtcDateTime
$end=[DateTimeOffset]::Parse('2026-10-31T01:01:00Z').UtcDateTime
$records=New-Object System.Collections.Generic.List[object]
$candidateCount=0; $matchedSeen=0
try {
  $events=@(Get-WinEvent -FilterHashtable @{LogName='Application';Id=@(1000,1001);StartTime=$start;EndTime=$end} -MaxEvents 100 -ErrorAction Stop)
  $candidateCount=$events.Count
  foreach($event in $events) {
    if($event.ProviderName -notin @('Application Error','Windows Error Reporting')) { continue }
    [xml]$xml=$event.ToXml()
    $fields=[ordered]@{}
    foreach($item in @($xml.Event.EventData.Data)) {
      if($null -ne $item -and $item.Name) { $fields[[string]$item.Name]=[string]$item.'#text' }
    }
    $matchedBy=$null
    foreach($name in @('AppName','ApplicationName','FaultingApplicationName','AppPath','ApplicationPath','P1')) {
      if($fields.Contains($name) -and $fields[$name]) {
        if([System.IO.Path]::GetFileName([string]$fields[$name]) -ieq 'MATLAB.exe') { $matchedBy=$name;break }
      }
    }
    if($null -eq $matchedBy) { continue }
    $matchedSeen++
    if($records.Count -ge 12) { continue }
    $records.Add([ordered]@{event_id=[int]$event.Id;provider=[string]$event.ProviderName;utc=$event.TimeCreated.ToUniversalTime().ToString('o');level=[int]$event.Level;matched_application_field=$matchedBy;named_event_data=$fields})
  }
  $result=[ordered]@{status='QUERY_COMPLETED';query_calls=1;candidate_count=$candidateCount;candidate_cap=100;candidate_cap_reached=($candidateCount -eq 100);matched_seen=$matchedSeen;matched_saved=$records.Count;matched_cap=12;matched_cap_exceeded=($matchedSeen -gt 12);matlab_records=@($records.ToArray());error=$null}
} catch {
  $kind='QUERY_FAILED'
  if($_.FullyQualifiedErrorId -like 'NoMatchingEventsFound*') { $kind='NO_MATCH' }
  elseif($_.Exception -is [System.UnauthorizedAccessException] -or $_.Exception.Message -match 'Access is denied|access.*denied|拒绝访问') { $kind='NO_PERMISSION' }
  $result=[ordered]@{status=$kind;query_calls=1;candidate_count=$candidateCount;candidate_cap=100;candidate_cap_reached=$false;matched_seen=$matchedSeen;matched_saved=$records.Count;matched_cap=12;matched_cap_exceeded=$false;matlab_records=@($records.ToArray());error=[ordered]@{exception_type=$_.Exception.GetType().FullName;fully_qualified_error_id=$_.FullyQualifiedErrorId;hresult=$_.Exception.HResult;message=$_.Exception.Message}}
}
$result | ConvertTo-Json -Depth 12 -Compress
"""


class ReparseBlocked(ValueError):
    pass


def stamp():
    return {'utc': datetime.now(timezone.utc).isoformat(), 'monotonic_ns': time.monotonic_ns()}


def hash_name(name):
    return hashlib.sha256(name.encode('utf-8')).hexdigest()


def safe_ancestry(path):
    """lstat ancestors first, so a descendant of a reparse is never followed."""
    for item in reversed([path, *path.parents]):
        info = os.lstat(item)
        if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 0x400:
            raise ReparseBlocked('Reparse metadata target rejected')
    return info


def status(error):
    if isinstance(error, FileNotFoundError):
        return 'NOT_FOUND'
    if isinstance(error, PermissionError):
        return 'NO_PERMISSION'
    if isinstance(error, ReparseBlocked):
        return 'REPARSE_BLOCKED'
    return 'NOT_AVAILABLE'


def utc_timestamp(value):
    return datetime.fromtimestamp(value, timezone.utc).isoformat()


def filesystem_metadata(path, role, info=None):
    """Never open, hash or copy original file content."""
    info = info if info is not None else os.lstat(path)
    creation = getattr(info, 'st_birthtime', info.st_ctime)
    return {'source_role': role, 'private_path': str(path), 'private_basename': path.name,
            'basename_sha256': hash_name(path.name), 'bytes': info.st_size,
            'mtime_utc': utc_timestamp(info.st_mtime), 'ctime_utc': utc_timestamp(info.st_ctime),
            'creation_utc': utc_timestamp(creation), 'mtime_ns': info.st_mtime_ns,
            'ctime_ns': info.st_ctime_ns, 'extension': path.suffix.lower(),
            'file_type': 'DIRECTORY' if stat.S_ISDIR(info.st_mode) else 'REGULAR_FILE' if stat.S_ISREG(info.st_mode) else 'OTHER',
            'reparse': bool(getattr(info, 'st_file_attributes', 0) & 0x400) or stat.S_ISLNK(info.st_mode),
            'content_read': False, 'content_sha256': 'NOT_COMPUTED_UNAUTHORIZED'}


def in_window(info):
    lo = datetime.fromisoformat(START.replace('Z', '+00:00')).timestamp()
    hi = datetime.fromisoformat(END.replace('Z', '+00:00')).timestamp()
    return any(lo <= value <= hi for value in (getattr(info, 'st_birthtime', info.st_ctime), info.st_mtime))


def matches_matlab_name(name):
    name = name.casefold()
    return name.startswith('appcrash_matlab') or name == 'matlab.exe' or name.startswith('matlab.exe.') or name.startswith('matlab.exe_')


def shallow_children(path, role, limit=16):
    children = []
    truncated = False
    safe_ancestry(path)
    with os.scandir(path) as entries:
        for entry in entries:
            if len(children) == limit:
                truncated = True
                break
            info = entry.stat(follow_symlinks=False)
            child = filesystem_metadata(path / entry.name, role + '_DIRECT_CHILD', info)
            child['status'] = 'REPARSE_BLOCKED' if child['reparse'] else 'METADATA_ONLY'
            children.append(child)
    return {'status': 'METADATA_ONLY', 'children': children, 'recorded_children': len(children),
            'child_cap': limit, 'truncated': truncated, 'recursive': False}


def roots_metadata(roots):
    results = []
    used = 0
    for role, path in roots.items():
        row = {'source_role': role, 'private_root': str(path) if path is not None else None,
               'root_status': 'ENV_NOT_AVAILABLE', 'candidates': [], 'candidate_cap_reached': False}
        if path is None:
            results.append(row)
            continue
        try:
            info = safe_ancestry(path)
            if not stat.S_ISDIR(info.st_mode):
                raise ValueError('Standard root not a directory')
            row.update(root_status='PRESENT', root_metadata=filesystem_metadata(path, role, info))
            with os.scandir(path) as entries:
                for entry in entries:
                    if not matches_matlab_name(entry.name):
                        continue
                    if used >= 12:
                        row['candidate_cap_reached'] = True
                        continue
                    used += 1
                    item = {'private_name': entry.name, 'status': 'NOT_AVAILABLE'}
                    try:
                        child_info = entry.stat(follow_symlinks=False)
                        meta = filesystem_metadata(path / entry.name, role + '_MATLAB_CANDIDATE', child_info)
                        item['metadata'] = meta
                        if meta['reparse']:
                            item['status'] = 'REPARSE_BLOCKED'
                        elif not in_window(child_info):
                            item['status'] = 'OUTSIDE_WINDOW_NOT_DESCENDED'
                        else:
                            item['status'] = 'NAME_AND_TIME_MATCH_METADATA_ONLY'
                            if stat.S_ISDIR(child_info.st_mode):
                                item['direct_children'] = shallow_children(path / entry.name, role)
                    except (OSError, ValueError) as error:
                        item.update(status=status(error), error_class=type(error).__name__)
                    row['candidates'].append(item)
        except (OSError, ValueError) as error:
            row.update(root_status=status(error), error_class=type(error).__name__)
        results.append(row)
    return {'roots': results, 'standard_roots': 5, 'candidate_metadata_slots_used': used,
            'candidate_slot_cap': 12, 'selection': 'Direct MATLAB/AppCrash_MATLAB basename and creation_or_mtime in exact UTC window',
            'file_contents_read_or_hashed': 0, 'custom_dumpfolder_traversals': 0}


def localdumps_registry(standard_dump_root):
    rows = []
    for role, suffix in [('HKLM_LOCALDUMPS_GLOBAL_64', ''), ('HKLM_LOCALDUMPS_MATLAB_EXE_64', r'\MATLAB.exe')]:
        row = {'source_role': role, 'hive': 'HKEY_LOCAL_MACHINE', 'view': '64_BIT',
               'access': 'KEY_READ', 'private_registry_key': REG_BASE + suffix, 'status': 'NOT_FOUND', 'values': {}}
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_BASE + suffix, 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as key:
                row['status'] = 'PRESENT'
                for name in ('DumpType', 'DumpCount', 'DumpFolder'):
                    try:
                        value, kind = winreg.QueryValueEx(key, name)
                        result = {'status': 'CONFIGURED', 'registry_type': kind}
                        if name == 'DumpFolder':
                            raw = str(value)
                            standard = raw.casefold() == r'%localappdata%\crashdumps'.casefold()
                            standard = standard or (standard_dump_root is not None and raw.casefold() == str(standard_dump_root).casefold())
                            result.update(private_value=raw, path_string_sha256=hash_name(raw),
                                          classification='CONFIGURED_STANDARD_ALLOWED_ROOT' if standard else 'CUSTOM_LOCATION_CONFIGURED', followed=False)
                        elif isinstance(value, int):
                            result['value'] = value
                        else:
                            result.update(classification='UNEXPECTED_VALUE_TYPE', value_string_sha256=hash_name(str(value)))
                        row['values'][name] = result
                    except FileNotFoundError:
                        row['values'][name] = {'status': 'NOT_SET'}
                    except OSError as error:
                        row['values'][name] = {'status': status(error), 'error_class': type(error).__name__}
        except OSError as error:
            row.update(status=status(error), error_class=type(error).__name__)
        rows.append(row)
    return {'keys': rows, 'hive': 'HKEY_LOCAL_MACHINE', 'writes': 0,
            'custom_folder_followed': False, 'note': 'Missing configuration does not prove no WER dump exists'}


def event_query():
    system_root = os.environ.get('SystemRoot')
    if not system_root:
        return {'status': 'ENV_NOT_AVAILABLE', 'query_calls': 0, 'child_processes': 0}
    powershell = Path(system_root) / 'System32/WindowsPowerShell/v1.0/powershell.exe'
    safe_ancestry(powershell)
    argv = [str(powershell), '-NoProfile', '-NonInteractive', '-Command', POWERSHELL_QUERY]
    before = stamp()
    try:
        child = subprocess.run(argv, capture_output=True, timeout=30, shell=False)
        result = {'status': 'QUERY_FAILED', 'query_calls': 1, 'child_processes': 1,
                  'exit_code': child.returncode, 'private_argv': argv,
                  'private_stdout_utf8': child.stdout.decode('utf-8-sig', errors='strict'),
                  'private_stderr_utf8': child.stderr.decode('utf-8-sig', errors='replace'),
                  'before': before, 'after': stamp(), 'retries': 0}
        if child.returncode == 0:
            body = json.loads(result['private_stdout_utf8'])
            result.update(status=body['status'], query_result=body)
        return result
    except (OSError, subprocess.TimeoutExpired, UnicodeError, ValueError) as error:
        return {'status': status(error), 'query_calls': 1, 'child_processes': 1,
                'error_class': type(error).__name__, 'private_error': str(error),
                'before': before, 'after': stamp(), 'retries': 0}


def main():
    assert os.name == 'nt'
    work = Path(__file__).resolve().parents[2]
    local = work / 'tasks' / TASK / 'LOCAL_ONLY'
    safe_ancestry(local)

    def dump(name, obj):
        assert '/' not in name and chr(92) not in name
        path = local / name
        with path.open('x', encoding='utf-8', newline='\n') as stream:
            json.dump(obj, stream, indent=2)
            stream.write('\n')

    gate = json.loads((local / 'source_gates_checked.json').read_bytes().decode('utf-8'))
    assert gate['all_passed'] is True and gate['governance_head'] == GOV
    dump('auditor_invocation_claim.json', {'task_id': TASK, 'invocation_index': 1, 'maximum': 1, 'retries': 0, 'start': stamp()})
    event = event_query()
    dump('event_query_raw.json', event)
    program_data = os.environ.get('ProgramData')
    local_app_data = os.environ.get('LOCALAPPDATA')
    roots = {
        'A_PROGRAMDATA_REPORTARCHIVE': Path(program_data) / 'Microsoft/Windows/WER/ReportArchive' if program_data else None,
        'B_PROGRAMDATA_REPORTQUEUE': Path(program_data) / 'Microsoft/Windows/WER/ReportQueue' if program_data else None,
        'C_LOCALAPPDATA_REPORTARCHIVE': Path(local_app_data) / 'Microsoft/Windows/WER/ReportArchive' if local_app_data else None,
        'D_LOCALAPPDATA_REPORTQUEUE': Path(local_app_data) / 'Microsoft/Windows/WER/ReportQueue' if local_app_data else None,
        'E_LOCALAPPDATA_CRASHDUMPS': Path(local_app_data) / 'CrashDumps' if local_app_data else None,
    }
    for path in roots.values():
        if path is not None and (not path.is_absolute() or str(path).startswith(chr(92) * 2)):
            raise ValueError('Standard root not local absolute path')
    wer = roots_metadata(roots)
    dump('wer_roots_metadata_raw.json', wer)
    registry = localdumps_registry(roots['E_LOCALAPPDATA_CRASHDUMPS'])
    dump('localdumps_registry_raw.json', registry)
    prefdir = work / LATEST
    try:
        info = safe_ancestry(prefdir)
        pref = {'status': 'METADATA_ONLY', 'directory': filesystem_metadata(prefdir, 'LATEST_R3_PREFDIR', info),
                'direct_children': shallow_children(prefdir, 'LATEST_R3_PREFDIR'),
                'file_content_reads': 0, 'earlier_prefdir_accesses': 0}
    except (OSError, ValueError) as error:
        pref = {'status': 'LATEST_PREFDIR_PENDING_IO', 'detail_status': status(error), 'error_class': type(error).__name__, 'file_content_reads': 0}
    dump('latest_prefdir_metadata_raw.json', pref)
    observed = [event['status']] + [r['root_status'] for r in wer['roots']] + [r['status'] for r in registry['keys']]
    for row in wer['roots']:
        observed += [r['status'] for r in row['candidates']]
        for candidate in row['candidates']:
            observed += [r['status'] for r in candidate.get('direct_children', {}).get('children', [])]
    if pref.get('status') == 'LATEST_PREFDIR_PENDING_IO':
        observed.append(pref.get('detail_status'))
    else:
        observed += [r['status'] for r in pref['direct_children']['children']]
    blocked = any(s in BLOCKED for s in observed)
    final = {'task_id': TASK, 'actual_terminal': 'STOP__R6_R3_R2_R4_WER_PERMISSION_OR_SCOPE_BLOCKED' if blocked else 'STOP__AWAITING_GPT_INDEPENDENT_ABC',
             'auditor_invocations': 1, 'event_query_calls': event.get('query_calls', 0),
             'event_query_child_processes': event.get('child_processes', 0),
             'event_query_status': event['status'], 'wer_standard_roots': 5,
             'candidate_metadata_slots_used': wer['candidate_metadata_slots_used'],
             'new_matlab_processes': 0, 'job_experiments': 0, 'new_dump_creations': 0,
             'dump_or_report_content_reads_hashes_copies': 0, 'prefdir_content_reads': 0,
             'new_prefdirs': 0, 'registry_writes': 0, 'event_log_writes': 0,
             'scientific_and_npz_calls': 0, 'retries': 0, 'stack_trace': 'NOT_OBSERVED',
             'scope_statuses': observed, 'finish': stamp()}
    dump('audit_execution_receipt_raw.json', final)
    print(json.dumps(final, indent=2))
    return 1 if blocked else 0


if __name__ == '__main__':
    raise SystemExit(main())
