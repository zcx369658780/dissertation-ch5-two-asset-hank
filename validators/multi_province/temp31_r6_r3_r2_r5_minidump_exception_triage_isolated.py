"""One original dump, one unbuffered read-only open, bounded metadata reads.

No import-time IO/environment lookup, memory mapping, memory-stream reads,
dump hashing/copying, debugger spawning, network or native/model execution.
Only allowlisted parsed metadata is returned publicly; private values stay local.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import struct
import time
from datetime import datetime, timezone

TASK = 'CH5_TEMP31_R6_R3_R2_R5_LOCAL_DUMP_MINIMAL_EXCEPTION_TRIAGE_20261031'
GOV = '2aaa1b4bbfafeeffb9d985de7ad1433dde1406a9'
R4 = 'CH5_TEMP31_R6_R3_R2_R4_WER_STACK_METADATA_AUDIT_20261031'
R3 = 'CH5_TEMP31_R6_R3_R2_R3_EXPLICIT_NATIVE_120S_20261031'
NAME_SHA = 'fef366b31732a6d889909d0525bdc1ac014444f1297c147a035116a983119677'
FILE_SIZE = 23219990
CREATED = '2026-10-31T00:31:33.828285+00:00'
MTIME = '2026-10-31T00:31:35.037390+00:00'
STREAM_NAMES = {3: 'ThreadList', 4: 'ModuleList', 5: 'MemoryList', 6: 'Exception',
                7: 'SystemInfo', 9: 'Memory64List', 12: 'HandleData', 15: 'MiscInfo',
                16: 'MemoryInfoList', 17: 'ThreadInfo', 19: 'Token', 21: 'SystemMemoryInfo', 22: 'ProcessVmCounters'}
READ_ROLES = {'HEADER', 'DIRECTORY', 'SYSTEM_ARCHITECTURE', 'EXCEPTION_HEADER',
              'EXCEPTION_CONTEXT_DESCRIPTOR', 'MODULE_COUNT', 'MODULE_TABLE',
              'MODULE_NAME_LENGTH', 'MODULE_NAME_UTF16', 'MISC_PROCESS_ID_PREFIX'}


class IdentityBlocked(ValueError):
    pass


class ParseUncertain(ValueError):
    pass


def stamp():
    return {'utc': datetime.now(timezone.utc).isoformat(), 'monotonic_ns': time.monotonic_ns()}


def receipt_identity(raw):
    """Only new/authorized JSON metadata receipts or basename strings, never dump chunks."""
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()}


def safe(path):
    for component in reversed([path, *path.parents]):
        info = os.lstat(component)
        if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 0x400:
            raise IdentityBlocked('Reparse path rejected')
    return info


def metadata_json(path, cap=65536):
    """Caller paths are fixed JSON receipt roles, not paths taken from the dump."""
    if path.suffix.casefold() != '.json':
        raise IdentityBlocked('Not an authorized metadata receipt type')
    info = safe(path)
    if not stat.S_ISREG(info.st_mode) or info.st_size > cap:
        raise IdentityBlocked('Metadata receipt bounds')
    raw = path.read_bytes()
    return json.loads(raw.decode('utf-8', errors='strict')), receipt_identity(raw)


def stat_record(info):
    return {'bytes': info.st_size, 'mtime_ns': info.st_mtime_ns,
            'ctime_ns': info.st_ctime_ns,
            'creation_utc': datetime.fromtimestamp(getattr(info, 'st_birthtime', info.st_ctime), timezone.utc).isoformat(),
            'mtime_utc': datetime.fromtimestamp(info.st_mtime, timezone.utc).isoformat(),
            'regular_file': stat.S_ISREG(info.st_mode),
            'reparse': bool(getattr(info, 'st_file_attributes', 0) & 0x400) or stat.S_ISLNK(info.st_mode),
            'private_file_identity': [info.st_dev, info.st_ino]}


def unchanged(before, after):
    return all(before[k] == after[k] for k in ('bytes', 'mtime_ns', 'ctime_ns', 'private_file_identity'))


def target_identity(work):
    local = work / 'tasks' / TASK / 'LOCAL_ONLY'
    reply, _ = metadata_json(local / 'r4_dump_metadata_raw.json')
    body = reply['result']['structuredContent']
    body_bytes = body['content'].encode('utf-8')
    if receipt_identity(body_bytes)['git_blob'] != 'b81191aeb86c4c9ca7b6688d7e5ca8611c5a5d28' or body['sha'] != 'b81191aeb86c4c9ca7b6688d7e5ca8611c5a5d28':
        raise IdentityBlocked('Frozen R4 metadata mismatch')
    frozen = json.loads(body['content'])
    expected_receipt = frozen['raw_metadata_receipt_identity']
    raw_r4_path = work / 'tasks' / R4 / 'LOCAL_ONLY/wer_roots_metadata_raw.json'
    r4, actual_receipt = metadata_json(raw_r4_path)
    if actual_receipt != expected_receipt:
        raise IdentityBlocked('Original R4 LOCAL_ONLY receipt identity mismatch')
    candidates = [item for root in r4['roots'] if root['source_role'] == 'E_LOCALAPPDATA_CRASHDUMPS'
                  for item in root['candidates']
                  if item.get('metadata', {}).get('basename_sha256') == NAME_SHA]
    if len(candidates) != 1:
        raise IdentityBlocked('Unique prior target not established')
    previous = candidates[0]['metadata']
    target = Path(previous['private_path'])
    env_root = os.environ.get('LOCALAPPDATA')
    if not env_root:
        raise IdentityBlocked('Standard local root unavailable')
    standard = Path(os.path.abspath(Path(env_root) / 'CrashDumps'))
    if not target.is_absolute() or str(target).startswith(chr(92) * 2):
        raise IdentityBlocked('Target must be local absolute file')
    if os.path.normcase(os.path.abspath(target.parent)) != os.path.normcase(str(standard)):
        raise IdentityBlocked('Target is outside exact standard root')
    if hashlib.sha256(target.name.encode('utf-8')).hexdigest() != NAME_SHA:
        raise IdentityBlocked('Target basename identity mismatch')
    before = stat_record(safe(target))
    if before['bytes'] != FILE_SIZE or not before['regular_file'] or before['reparse']:
        raise IdentityBlocked('Target type/size mismatch')
    for field, expected in [('creation_utc', CREATED), ('mtime_utc', MTIME)]:
        actual = datetime.fromisoformat(before[field])
        if abs((actual - datetime.fromisoformat(expected)).total_seconds()) > 0.1:
            raise IdentityBlocked('Target timestamp mismatch')
        if abs((actual - datetime.fromisoformat(previous[field])).total_seconds()) > 0.1:
            raise IdentityBlocked('Target changed since R4')
    return target, before, actual_receipt


def prior_pid_correlation(work, target):
    path = work / 'tasks' / R3 / 'LOCAL_ONLY/owned_process_private_identity.json'
    result = {'filename_vs_owned_pid': 'NOT_AVAILABLE', 'dump_misc_pid_vs_owned_pid': 'NOT_AVAILABLE',
              'source_role': 'EXACT_PRIOR_OWNED_PROCESS_RECEIPT_ONLY'}
    owned = None
    try:
        data, rid = metadata_json(path, 4096)
        if set(data) != {'pid', 'tid'} or any(type(data[k]) is not int or not 0 < data[k] <= 0xffffffff for k in data):
            result['receipt_status'] = 'STRUCTURE_UNCERTAIN'
            return result, owned
        owned = data['pid']
        result.update(receipt_status='STRUCTURALLY_VALID_EXACT_PRIOR_PATH', private_owned_pid=owned,
                      owned_receipt_identity=rid,
                      receipt_authenticity_scope='Prior controller-created exact path; no independent fresh process inspection')
        match = re.fullmatch(r'matlab[.]exe[._]([0-9]+)[.]dmp', target.name, re.IGNORECASE)
        if match:
            candidate_pid = int(match.group(1))
            result.update(private_filename_pid=candidate_pid,
                          filename_vs_owned_pid='PID_MATCH' if candidate_pid == owned else 'PID_MISMATCH')
    except (OSError, ValueError) as error:
        result.update(receipt_status='NOT_AVAILABLE', error_class=type(error).__name__)
    return result, owned


class Reader:
    def __init__(self, stream, size):
        self.stream = stream
        self.size = size
        self.bytes_read = 0
        self.reads = []

    def bounds(self, offset, count):
        if type(offset) is not int or type(count) is not int or offset < 0 or count < 0 or count > self.size or offset > self.size - count:
            raise ParseUncertain('File range outside authenticated target')

    def at(self, offset, count, role):
        if role not in READ_ROLES or len(self.reads) >= 32 or count > 65536 - self.bytes_read:
            raise ParseUncertain('Read role/count/byte budget blocked')
        self.bounds(offset, count)
        self.stream.seek(offset, os.SEEK_SET)
        raw = self.stream.read(count)
        self.bytes_read += len(raw)
        self.reads.append({'index': len(self.reads) + 1, 'private_file_offset': offset,
                           'requested_bytes': count, 'actual_bytes': len(raw), 'role': role})
        if len(raw) != count:
            raise ParseUncertain('Short structural read; no retry')
        return raw


def public_module_name(name):
    if name is None:
        return {'module_role': 'MODULE_NAME_UNRESOLVED'}
    base = name.replace(chr(92), '/').rsplit('/', 1)[-1]
    low = base.casefold()
    known = {'matlab.exe', 'ntdll.dll', 'kernel32.dll', 'kernelbase.dll', 'jvm.dll', 'ucrtbase.dll', 'msvcrt.dll'}
    if low in known:
        return {'module_basename': base, 'module_role': 'KNOWN_PLATFORM_OR_MATLAB_BASENAME'}
    return {'module_role': 'OTHER_MODULE_BASENAME_LOCAL_ONLY',
            'module_basename_sha256': hashlib.sha256(base.encode('utf-8')).hexdigest()}


def parse_dump(reader, result, owned):
    header = reader.at(0, 32, 'HEADER')
    sig, version, count, directory, checksum, timestamp, flags = struct.unpack('<IIIIIIQ', header)
    if sig != 0x504d444d or version & 0xffff != 0xa793:
        raise ParseUncertain('Unsupported or non-Minidump format')
    result['header'] = {'recognized_format': 'MINIDUMP_MDMP', 'format_version_low16': hex(version & 0xffff),
                        'stream_count': count, 'private_directory_rva': directory,
                        'private_header_timestamp': timestamp, 'private_dump_type_flags': flags}
    if not 0 < count <= 128:
        raise ParseUncertain('Stream-directory count exceeds permitted format bounds')
    raw_directory = reader.at(directory, count * 12, 'DIRECTORY')
    streams = {}
    inventory = []
    for index in range(count):
        kind, size, rva = struct.unpack_from('<III', raw_directory, index * 12)
        reader.bounds(rva, size)
        inventory.append({'stream_type': kind, 'stream_role': STREAM_NAMES.get(kind, 'UNKNOWN_NOT_OPENED'),
                          'declared_bytes': size, 'content_read': False})
        if kind in (4, 6, 7, 15):
            if kind in streams:
                raise ParseUncertain('Duplicate needed stream')
            streams[kind] = (rva, size)
    result['stream_inventory'] = inventory
    result['exception'] = {'stream_present': 6 in streams, 'exception_code': 'NOT_PRESENT',
                           'new_code_vs_prior_exit': 'NOT_COMPARABLE', 'context_data_read': False}
    result['process'] = {'misc_pid_field_present': False, 'dump_misc_pid_vs_owned_pid': 'NOT_AVAILABLE'}
    result['module_mapping'] = {'status': 'EXCEPTION_ADDRESS_UNAVAILABLE', 'address_in_module': 'UNRESOLVED'}

    def read_prefix(kind, count_bytes, role):
        rva, declared = streams[kind]
        if declared < count_bytes:
            raise ParseUncertain('Needed stream too short')
        raw = reader.at(rva, count_bytes, role)
        next(item for item in inventory if item['stream_type'] == kind)['content_read'] = True
        return raw

    if 7 in streams:
        architecture = struct.unpack('<H', read_prefix(7, 2, 'SYSTEM_ARCHITECTURE'))[0]
        result['architecture'] = {9: 'AMD64', 12: 'ARM64', 0: 'X86'}.get(architecture, 'OTHER_UNINTERPRETED')
    if 15 in streams:
        prefix = read_prefix(15, 12, 'MISC_PROCESS_ID_PREFIX')
        size_info, valid_flags, pid = struct.unpack('<III', prefix)
        if size_info < 12 or size_info > streams[15][1]:
            raise ParseUncertain('MiscInfo size invalid')
        if valid_flags & 1:
            result['process'].update(misc_pid_field_present=True, private_dump_pid=pid,
                                     dump_misc_pid_vs_owned_pid='PID_MATCH' if owned is not None and pid == owned else 'PID_MISMATCH' if owned is not None else 'NOT_AVAILABLE')
    if 6 not in streams:
        return
    exception_rva, exception_size = streams[6]
    if exception_size < 168:
        raise ParseUncertain('ExceptionStream layout too short')
    thread, alignment, code, exception_flags, record, address = struct.unpack('<IIIIQQ', read_prefix(6, 32, 'EXCEPTION_HEADER'))
    context_size, context_rva = struct.unpack('<II', reader.at(exception_rva + 160, 8, 'EXCEPTION_CONTEXT_DESCRIPTOR'))
    reader.bounds(context_rva, context_size)
    result['exception'] = {'stream_present': True, 'exception_code': '0x' + format(code, '08X'),
                           'exception_flags': '0x' + format(exception_flags, '08X'),
                           'new_code_vs_prior_exit': 'EXCEPTION_STREAM_CODE_MATCH' if code == 0xc00000fd else 'EXCEPTION_STREAM_CODE_MISMATCH',
                           'context_descriptor_present': context_size > 0 and context_rva > 0,
                           'context_descriptor_in_file_bounds': True, 'context_data_read': False,
                           'context_register_values_read_or_published': 0, 'exception_parameters_read_or_published': 0,
                           'private_thread_id': thread, 'private_exception_record_address': record,
                           'private_exception_address': address, 'private_context_rva': context_rva,
                           'private_context_size': context_size}
    if 4 not in streams:
        result['module_mapping'] = {'status': 'MODULE_LIST_NOT_PRESENT', 'address_in_module': 'UNRESOLVED'}
        return
    module_rva, module_size = streams[4]
    total_modules = struct.unpack('<I', read_prefix(4, 4, 'MODULE_COUNT'))[0]
    if total_modules > (module_size - 4) // 108:
        raise ParseUncertain('Module count exceeds declared table')
    inspected = min(total_modules, (16384 - 4) // 108)
    table = reader.at(module_rva + 4, inspected * 108, 'MODULE_TABLE')
    modules = []
    for index in range(inspected):
        base, image_size, checksum, image_time, name_rva = struct.unpack_from('<QIIII', table, index * 108)
        if base + image_size > 1 << 64:
            raise ParseUncertain('Module range overflow')
        modules.append({'index': index, 'base': base, 'size': image_size, 'name_rva': name_rva})
    matched = [m for m in modules if m['base'] <= address < m['base'] + m['size']]
    name_cache = {}

    def module_name(module):
        if module['index'] in name_cache:
            return name_cache[module['index']]
        if len(name_cache) >= 8:
            raise ParseUncertain('Module-name count limit')
        name_length = struct.unpack('<I', reader.at(module['name_rva'], 4, 'MODULE_NAME_LENGTH'))[0]
        if name_length > 256:
            name_cache[module['index']] = None
            return None
        if name_length % 2:
            raise ParseUncertain('Module UTF16 size invalid')
        value = reader.at(module['name_rva'] + 4, name_length, 'MODULE_NAME_UTF16').decode('utf-16-le', errors='strict')
        if chr(0) in value:
            raise ParseUncertain('Unexpected embedded null in module name')
        name_cache[module['index']] = value
        return value

    common = {'total_modules_declared': total_modules, 'module_entries_inspected': inspected,
              'module_table_bytes_read': 4 + len(table), 'module_table_complete': inspected == total_modules}
    if len(matched) == 1:
        match = matched[0]
        name = module_name(match)
        result['module_mapping'] = dict(common, status='UNIQUE_MODULE_RANGE_MATCH', address_in_module=True,
                                        relative_offset='0x' + format(address - match['base'], 'X'),
                                        private_module_path=name, **public_module_name(name))
    else:
        result['module_mapping'] = dict(common, status='NO_UNIQUE_MATCH_IN_INSPECTED_MODULE_PREFIX',
                                        address_in_module=False if not matched and inspected == total_modules else 'UNRESOLVED')
    if modules:
        first_name = module_name(modules[0])
        result['process']['first_module_identity'] = public_module_name(first_name)
        result['process']['first_module_is_matlab'] = first_name is not None and first_name.replace(chr(92), '/').rsplit('/', 1)[-1].casefold() == 'matlab.exe'
    result['module_name_records_read'] = len(name_cache)


def cdb_availability_only():
    """No debugger preparation/execution. No PATH scan or fallback location."""
    base = os.environ.get('ProgramFiles(x86)')
    if not base:
        return {'status': 'SKIP_WITH_REASON', 'reason': 'KNOWN_KITS_ROOT_ENV_NOT_AVAILABLE', 'invocations': 0}
    candidate = Path(base) / 'Windows Kits/10/Debuggers/x64/cdb.exe'
    try:
        info = safe(candidate)
        return {'status': 'SKIP_WITH_REASON', 'reason': 'SIGNATURE_TRUST_AND_ZERO_NETWORK_EXECUTION_NOT_ESTABLISHED_NO_PREPARATION_OR_SPAWN',
                'candidate_role': 'EXACT_WINDOWS_KITS10_X64_CDB_PATH', 'candidate_exists': stat.S_ISREG(info.st_mode),
                'private_candidate_path': str(candidate), 'invocations': 0, 'symbols_directory_created': False}
    except FileNotFoundError:
        return {'status': 'SKIP_WITH_REASON', 'reason': 'DEBUGGER_NOT_AVAILABLE_AT_EXACT_KNOWN_KITS_PATH',
                'candidate_role': 'EXACT_WINDOWS_KITS10_X64_CDB_PATH', 'invocations': 0, 'system_search': False}
    except (OSError, ValueError) as error:
        return {'status': 'SKIP_WITH_REASON', 'reason': 'DEBUGGER_AVAILABILITY_SECURITY_UNVERIFIED',
                'error_class': type(error).__name__, 'invocations': 0}


def public_projection(result):
    """Strict structural field projection; never raw bytes, paths, IDs or pointers."""
    allowed = {'recognized_format', 'format_version_low16', 'stream_count', 'stream_type', 'stream_role',
               'declared_bytes', 'content_read', 'stream_present', 'exception_code', 'exception_flags',
               'new_code_vs_prior_exit', 'context_descriptor_present', 'context_descriptor_in_file_bounds',
               'context_data_read', 'context_register_values_read_or_published', 'exception_parameters_read_or_published',
               'status', 'address_in_module', 'relative_offset', 'module_basename', 'module_role',
               'module_basename_sha256', 'total_modules_declared', 'module_entries_inspected', 'module_table_bytes_read',
               'module_table_complete', 'misc_pid_field_present', 'dump_misc_pid_vs_owned_pid',
               'first_module_is_matlab', 'first_module_identity'}

    def project(obj):
        if isinstance(obj, list):
            return [project(x) for x in obj]
        if isinstance(obj, dict):
            return {k: project(v) for k, v in obj.items() if k in allowed}
        return obj

    return {k: project(result[k]) for k in ('header', 'stream_inventory', 'exception', 'module_mapping', 'process') if k in result}


def main():
    work = Path(__file__).resolve().parents[2]
    local = work / 'tasks' / TASK / 'LOCAL_ONLY'
    safe(local)

    def dump(name, data):
        if '/' in name or chr(92) in name:
            raise IdentityBlocked('Invalid output receipt role')
        with (local / name).open('x', encoding='utf-8', newline='\n') as stream:
            json.dump(data, stream, indent=2)
            stream.write('\n')

    gate, _ = metadata_json(local / 'source_gates_checked.json')
    if gate.get('all_passed') is not True or gate.get('governance_commit') != GOV:
        raise IdentityBlocked('Frozen authority gate missing')
    dump('parser_invocation_claim.json', {'task_id': TASK, 'invocation_index': 1, 'maximum': 1, 'retries': 0, 'start': stamp()})
    result = {'task_id': TASK, 'actual_terminal': 'STOP__R6_R3_R2_R5_DUMP_IDENTITY_OR_PERMISSION_BLOCKED',
              'dump_content_sha256': 'NOT_COMPUTED', 'open_attempts': 0, 'dump_bytes_read': 0,
              'read_records': [], 'parse_status': 'NOT_STARTED', 'error': None,
              'new_matlab_job_or_science_calls': 0, 'original_dump_copies_or_writes': 0,
              'wer_archive_retries': 0, 'original_metadata_unchanged': 'NOT_TESTED'}
    target = None
    before = None
    reader = None
    owned = None
    try:
        target, before, r4_identity = target_identity(work)
        result.update(private_target_path=str(target), before_stat=before,
                      target_identity='DUMP_FILE_STAT_MATCH', basename_sha256=NAME_SHA,
                      source_r4_raw_receipt_identity=r4_identity)
        pid, owned = prior_pid_correlation(work, target)
        result['pid_correlation'] = pid
        if pid['filename_vs_owned_pid'] == 'PID_MISMATCH':
            raise IdentityBlocked('Known owned process differs from filename PID')
        dump('target_identity_preopen_raw.json', {'status': 'PASS_BEFORE_DUMP_OPEN',
                                                'private_target_path': str(target), 'before_stat': before,
                                                'basename_sha256': NAME_SHA, 'pid_correlation': pid})
        result['open_attempts'] = 1
        with open(target, 'rb', buffering=0) as original:
            opened = stat_record(os.fstat(original.fileno()))
            if not unchanged(before, opened):
                raise IdentityBlocked('Opened file identity differs from lstat')
            reader = Reader(original, FILE_SIZE)
            result['parse_status'] = 'PARSING_BOUNDED_METADATA'
            parse_dump(reader, result, owned)
            result['parse_status'] = 'BOUNDED_STRUCTURE_PARSED'
        if result.get('exception', {}).get('stream_present') and result['exception'].get('exception_code') != 'NOT_PRESENT':
            result['actual_terminal'] = 'STOP__AWAITING_GPT_INDEPENDENT_ABC'
        else:
            result['actual_terminal'] = 'STOP__R6_R3_R2_R5_DUMP_FORMAT_OR_EXCEPTION_UNRESOLVED'
    except IdentityBlocked as error:
        result.update(actual_terminal='STOP__R6_R3_R2_R5_DUMP_IDENTITY_OR_PERMISSION_BLOCKED', error={'class': type(error).__name__, 'private_message': str(error)})
    except (ParseUncertain, UnicodeError, struct.error, ValueError) as error:
        result.update(actual_terminal='STOP__R6_R3_R2_R5_DUMP_FORMAT_OR_EXCEPTION_UNRESOLVED', parse_status='PARSE_UNCERTAIN', error={'class': type(error).__name__, 'private_message': str(error)})
    except OSError as error:
        result.update(actual_terminal='STOP__R6_R3_R2_R5_DUMP_IDENTITY_OR_PERMISSION_BLOCKED', error={'class': type(error).__name__, 'private_message': str(error)})
    finally:
        if reader:
            result.update(dump_bytes_read=reader.bytes_read, read_records=reader.reads)
        if target is not None and before is not None:
            try:
                after = stat_record(safe(target))
                result['after_stat'] = after
                result['original_metadata_unchanged'] = unchanged(before, after)
                if not result['original_metadata_unchanged']:
                    result['actual_terminal'] = 'STOP__R6_R3_R2_R5_UNEXPECTED_DUMP_WRITE_OR_EXFIL_ATTEMPT'
            except (OSError, ValueError) as error:
                result.update(actual_terminal='STOP__R6_R3_R2_R5_DUMP_IDENTITY_OR_PERMISSION_BLOCKED', post_stat_error_class=type(error).__name__)
        if result['dump_bytes_read'] > 65536 or len(result['read_records']) > 32:
            result['actual_terminal'] = 'STOP__R6_R3_R2_R5_UNEXPECTED_DUMP_WRITE_OR_EXFIL_ATTEMPT'
        if reader is not None:
            result['debugger'] = cdb_availability_only()
        else:
            result['debugger'] = {'status': 'SKIP_WITH_REASON', 'reason': 'DUMP_PREOPEN_GATE_NOT_PASSED', 'invocations': 0}
        result['public_parsed_metadata'] = public_projection(result)
        result['finish'] = stamp()
        dump('minimal_exception_triage_raw.json', result)
        public = {'task_id': TASK, 'actual_terminal': result['actual_terminal'],
                  'target_identity': result.get('target_identity', 'NOT_ESTABLISHED'),
                  'dump_bytes_read': result['dump_bytes_read'], 'read_calls': len(result['read_records']),
                  'open_attempts': result['open_attempts'], 'parse_status': result['parse_status'],
                  'filename_pid_match': result.get('pid_correlation', {}).get('filename_vs_owned_pid', 'NOT_AVAILABLE'),
                  'original_metadata_unchanged': result['original_metadata_unchanged'],
                  'parsed_metadata': result['public_parsed_metadata'],
                  'debugger_status': result['debugger']['status'], 'debugger_skip_reason': result['debugger']['reason'],
                  'debugger_invocations': 0, 'stack_frames': [], 'stack_status': 'NOT_OBSERVED_DEBUGGER_SKIPPED',
                  'dump_content_sha256': 'NOT_COMPUTED', 'error_class': (result.get('error') or {}).get('class')}
        dump('minimal_exception_triage_public_projection.json', public)
        print(json.dumps(public, indent=2))
    return 0 if result['actual_terminal'] == 'STOP__AWAITING_GPT_INDEPENDENT_ABC' else 1


if __name__ == '__main__':
    raise SystemExit(main())
