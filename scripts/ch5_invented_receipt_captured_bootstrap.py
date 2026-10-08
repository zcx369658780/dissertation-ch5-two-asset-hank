"""SOURCE_ONLY captured-code bootstrap. NOT_RUN; no pathname code loading."""
import sys
import json
import base64
import hashlib
import runpy


CHECKER_PATH = r"D:\ProjectTemp\c5k1bturn56\scripts\ch5_invented_receipt_memory_checker.py"
TESTS_PATH = r"D:\ProjectTemp\c5k1bturn56\tests\test_ch5_invented_receipt_memory_checker.py"


def _fixed_unhandled_exception(_exception_type, _exception_value, _traceback):
    # Remain installed through interpreter termination, even after linecache
    # restoration. No traceback formatting, source lookup or exception content.
    try:
        sys.stderr.write("BOOTSTRAP_UNHANDLED_EXCEPTION\n")
    except Exception:
        pass  # No fallback to Python's pathname-reading default diagnostic.


sys.excepthook = _fixed_unhandled_exception


def _binding_failed():
    # Fixed administrative diagnostic, never exception text or captured code.
    sys.stderr.write("BOOTSTRAP_BINDING_FAILED\n")
    raise SystemExit(2)


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError
        result[key] = value
    return result


def _constant(_):
    raise ValueError


def _decode_code(encoded, pin):
    if (type(encoded) is not str or len(encoded) > 87384
            or type(pin) is not str or len(pin) != 64
            or any(char not in "0123456789ABCDEF" for char in pin)):
        raise ValueError
    code = base64.b64decode(encoded, validate=True)
    if len(code) > 65536:
        raise ValueError
    if hashlib.sha256(code).hexdigest().upper() != pin:
        raise ValueError
    return code


def _main():
    try:
        raw = sys.stdin.buffer.read(262145)  # one bounded administrative read
        if len(raw) > 262144:
            raise ValueError
        envelope = json.loads(raw.decode("utf-8", "strict"),
                              object_pairs_hook=_pairs,
                              parse_constant=_constant)
        if type(envelope) is not dict or set(envelope) != {
            "kind", "checker_b64", "checker_sha256", "tests_b64", "tests_sha256"
        }:
            raise ValueError
        if (type(envelope["kind"]) is not str
                or envelope["kind"] != "INVENTED_MEMORY_CODE_CAPTURE_V1"):
            raise ValueError
        checker = _decode_code(envelope["checker_b64"], envelope["checker_sha256"])
        tests = _decode_code(envelope["tests_b64"], envelope["tests_sha256"])
    except Exception:
        _binding_failed()

    loader_state = {"calls": 0, "failed": False}
    diagnostic_cache = {}

    def captured_run_path(path_name, init_globals=None, run_name=None):
        loader_state["calls"] += 1
        if (loader_state["calls"] != 1 or type(path_name) is not str
                or path_name != CHECKER_PATH
                or init_globals is not None or run_name is not None):
            loader_state["failed"] = True
            raise ValueError("BOOTSTRAP_BINDING_FAILED")
        # unittest imports traceback/linecache before setUpClass. Disable
        # pathname diagnostic lookups too: never reread code for tracebacks
        # and never place captured source lines in the captured raw streams.
        if not diagnostic_cache:
            cache = sys.modules.get("linecache")
            if cache is None:
                loader_state["failed"] = True
                raise ValueError("BOOTSTRAP_BINDING_FAILED")
            for name in ("checkcache", "getline", "getlines"):
                diagnostic_cache[name] = getattr(cache, name)
            diagnostic_cache["module"] = cache
            cache.checkcache = lambda filename=None: None
            cache.getline = lambda filename, lineno, module_globals=None: ""
            cache.getlines = lambda filename, module_globals=None: []
        namespace = {"__name__": "<captured_checker>", "__file__": CHECKER_PATH,
                     "__package__": None, "__spec__": None}
        exec(compile(checker, CHECKER_PATH, "exec"), namespace)
        return namespace

    original_run_path = runpy.run_path
    runpy.run_path = captured_run_path
    try:
        sys.argv = [TESTS_PATH, "-f", "-v"]
        namespace = sys.modules["__main__"].__dict__
        namespace["__file__"] = TESTS_PATH
        try:
            exec(compile(tests, TESTS_PATH, "exec"), namespace)
        except SystemExit as stopped:
            # Preserve unittest's 0/1, but a claimed success requires the
            # one exact captured loader call, including no rejected call.
            if type(stopped.code) is int and stopped.code in (0, 1):
                if stopped.code == 0 and (
                    loader_state["calls"] != 1 or loader_state["failed"]
                ):
                    _binding_failed()
                raise
            _binding_failed()
        except Exception:
            _binding_failed()
        # unittest.main is required to terminate with its own SystemExit.
        _binding_failed()
    finally:
        runpy.run_path = original_run_path
        if diagnostic_cache:
            cache = diagnostic_cache["module"]
            for name in ("checkcache", "getline", "getlines"):
                setattr(cache, name, diagnostic_cache[name])


if __name__ == "__main__":
    _main()
