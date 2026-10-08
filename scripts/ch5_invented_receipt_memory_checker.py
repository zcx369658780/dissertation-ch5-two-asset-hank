"""SOURCE_ONLY artificial receipt protocol; no I/O or execution adapter."""


class _Stop(Exception):
    def __init__(self, outcome, code):
        self.outcome = outcome
        self.code = code


class _Number:
    def __init__(self, token):
        self.token = token


def _reject(code):
    raise _Stop("REJECT", code)


def _incomplete():
    raise _Stop("UNKNOWN", "UNKNOWN__INVENTED_INPUT_INCOMPLETE")


class _Scanner:
    """All budgets are checked before consuming their counted item."""

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.tokens = 0

    def _token(self):
        if self.tokens >= 512:
            _reject("REJECT__INVENTED_TOKEN_CAP")
        self.tokens += 1

    def _space(self):
        while self.pos < len(self.text) and self.text[self.pos] in " \t\r\n":
            self.pos += 1

    def _peek(self):
        if self.pos == len(self.text):
            _incomplete()
        return self.text[self.pos]

    def _expect(self, char):
        if self._peek() != char:
            _reject("REJECT__INVENTED_JSON_SYNTAX")
        self.pos += 1

    def _append(self, chars, char):
        if len(chars) >= 256:
            _reject("REJECT__INVENTED_STRING_CAP")
        chars.append(char)

    def _hex4(self):
        digits = []
        for _ in range(4):
            char = self._peek()
            if char not in "0123456789abcdefABCDEF":
                _reject("REJECT__INVENTED_JSON_SYNTAX")
            digits.append(char)
            self.pos += 1
        return int("".join(digits), 16)

    def _string(self):
        self._expect('"')
        chars = []
        escapes = {'"': '"', "\\": "\\", "/": "/", "b": "\b",
                   "f": "\f", "n": "\n", "r": "\r", "t": "\t"}
        while True:
            char = self._peek()
            self.pos += 1
            if char == '"':
                return "".join(chars)
            if ord(char) < 32:
                _reject("REJECT__INVENTED_JSON_SYNTAX")
            if char == "\\":
                char = self._peek()
                self.pos += 1
                if char == "u":
                    value = self._hex4()
                    if 0xD800 <= value <= 0xDBFF:
                        # EOF in an unfinished escape is incomplete; a present
                        # non-pair or isolated surrogate is invalid syntax.
                        self._expect("\\")
                        self._expect("u")
                        low = self._hex4()
                        if not 0xDC00 <= low <= 0xDFFF:
                            _reject("REJECT__INVENTED_JSON_SYNTAX")
                        value = 0x10000 + ((value - 0xD800) << 10) + low - 0xDC00
                    elif 0xDC00 <= value <= 0xDFFF:
                        _reject("REJECT__INVENTED_JSON_SYNTAX")
                    char = chr(value)
                elif char in escapes:
                    char = escapes[char]
                else:
                    _reject("REJECT__INVENTED_JSON_SYNTAX")
            self._append(chars, char)

    def _literal(self, spelling, value):
        for char in spelling:
            self._expect(char)
        return value

    def _digits(self):
        start = self.pos
        while self.pos < len(self.text) and "0" <= self.text[self.pos] <= "9":
            self.pos += 1
        if self.pos == start:
            self._peek()  # distinguishes EOF from a present invalid character
            _reject("REJECT__INVENTED_JSON_SYNTAX")

    def _number(self):
        start = self.pos
        if self._peek() == "-":
            self.pos += 1
        first = self._peek()
        if first == "0":
            self.pos += 1
        elif "1" <= first <= "9":
            self._digits()
        else:
            _reject("REJECT__INVENTED_JSON_SYNTAX")
        if self.pos < len(self.text) and self.text[self.pos] == ".":
            self.pos += 1
            self._digits()
        if self.pos < len(self.text) and self.text[self.pos] in "eE":
            self.pos += 1
            if self.pos < len(self.text) and self.text[self.pos] in "+-":
                self.pos += 1
            self._digits()
        return _Number(self.text[start:self.pos])

    def _value(self, depth):
        self._space()
        char = self._peek()
        if char in "[{":
            if depth >= 8:
                _reject("REJECT__INVENTED_DEPTH_CAP")
            self._token()  # container start, before entering it
            self.pos += 1
            self._space()
            if char == "{":
                result = {}
                if self._peek() == "}":
                    self._token()
                    self.pos += 1
                    return result
                while True:
                    if self._peek() != '"':
                        _reject("REJECT__INVENTED_JSON_SYNTAX")
                    self._token()  # object key, not also a scalar
                    key = self._string()
                    if key in result:
                        _reject("REJECT__INVENTED_DUPLICATE_KEY")
                    self._space()
                    self._expect(":")
                    result[key] = self._value(depth + 1)
                    self._space()
                    next_char = self._peek()
                    if next_char == "}":
                        self._token()
                        self.pos += 1
                        return result
                    self._expect(",")
                    self._space()
            else:
                result = []
                if self._peek() == "]":
                    self._token()
                    self.pos += 1
                    return result
                while True:
                    result.append(self._value(depth + 1))
                    self._space()
                    next_char = self._peek()
                    if next_char == "]":
                        self._token()
                        self.pos += 1
                        return result
                    self._expect(",")
                    self._space()
        self._token()  # scalar, before consuming its value
        if char == '"':
            return self._string()
        if char == "t":
            return self._literal("true", True)
        if char == "f":
            return self._literal("false", False)
        if char == "n":
            return self._literal("null", None)
        if char == "-" or "0" <= char <= "9":
            return self._number()
        _reject("REJECT__INVENTED_JSON_SYNTAX")

    def parse(self):
        value = self._value(0)
        self._space()
        if self.pos != len(self.text):
            _reject("REJECT__INVENTED_JSON_SYNTAX")
        return value


def _keys(value, expected):
    # Each known object: type, then extra before missing.
    if type(value) is not dict:
        _reject("REJECT__INVENTED_SCHEMA_TYPE")
    if any(key not in expected for key in value):
        _reject("REJECT__INVENTED_SCHEMA_EXTRA_OR_LAYER_CONFLICT")
    if any(key not in value for key in expected):
        _reject("REJECT__INVENTED_SCHEMA_MISSING")


def _schema(value):
    # Fixed order independent of incoming key order:
    # root type/kind; outer extra/missing; nested type/extra/missing;
    # capture type; tool exit type/range then output type, or It then it
    # type/label; marker; capture value; finite result.
    if type(value) is not dict:
        _reject("REJECT__INVENTED_SCHEMA_TYPE")
    kind = value.get("kind")
    if type(kind) is not str or kind not in (
        "INVENTED_TOOL_RESULT_V1", "INVENTED_RECEIPT_V1"
    ):
        _reject("REJECT__INVENTED_SCHEMA_KIND")
    if kind == "INVENTED_TOOL_RESULT_V1":
        _keys(value, ("kind", "result", "capture_complete"))
        nested = value["result"]
        _keys(nested, ("exit_code", "output"))
    else:
        _keys(value, ("kind", "capture_complete", "known_state_key_types"))
        nested = value["known_state_key_types"]
        _keys(nested, ("It", "it"))
    if type(value["capture_complete"]) is not bool:
        _reject("REJECT__INVENTED_SCHEMA_TYPE")
    if kind == "INVENTED_TOOL_RESULT_V1":
        number = nested["exit_code"]
        if type(number) is not _Number:
            _reject("REJECT__INVENTED_EXIT_TOKEN_TYPE")
        token = number.token
        if "." in token or "e" in token or "E" in token or token == "-0":
            _reject("REJECT__INVENTED_EXIT_TOKEN_TYPE")
        if token.startswith("-") or len(token) > 3 or (
            len(token) == 3 and token > "255"
        ):
            _reject("REJECT__INVENTED_EXIT_RANGE")
        # Only a validated integer token of at most three digits is converted.
        exit_code = int(token)
        if type(nested["output"]) is not str:
            _reject("REJECT__INVENTED_SCHEMA_TYPE")
        if "[TRUNCATED]" in nested["output"]:
            return "UNKNOWN", "UNKNOWN__INVENTED_OUTPUT_TRUNCATED"
    else:
        for key, label in (("It", "NUMBER_INTEGER"), ("it", "BOOLEAN")):
            if type(nested[key]) is not str:
                _reject("REJECT__INVENTED_SCHEMA_TYPE")
            if nested[key] != label:
                _reject("REJECT__INVENTED_RECEIPT_LABEL")
    if not value["capture_complete"]:
        return "UNKNOWN", "UNKNOWN__INVENTED_CAPTURE_INCOMPLETE"
    if kind == "INVENTED_RECEIPT_V1":
        return "PASS", "PASS__INVENTED_RECEIPT"
    if exit_code == 0:
        return "PASS", "PASS__INVENTED_TOOL_RESULT"
    return "OBSERVED_FAILURE", "OBSERVED_FAILURE__INVENTED_TOOL_EXIT"


def _result(outcome, code):
    return {
        "outcome": outcome,
        "code": code,
        "source_authenticated": False,
        "original_live_identity_restored": False,
        "scientific_validity_established": False,
        "model_activation": False,
        "execution_admitted": False,
        "stdout_capture": "NOT_SEPARATELY_CAPTURED",
        "stderr_capture": "NOT_SEPARATELY_CAPTURED",
    }


def inspect_invented_receipt(payload):
    """Inspect exact immutable bytes under the fixed artificial contract."""
    try:
        if type(payload) is not bytes:
            _reject("REJECT__INVENTED_INPUT_TYPE")
        if len(payload) > 8192:
            _reject("REJECT__INVENTED_BYTE_CAP")
        try:
            text = payload.decode("utf-8", "strict")
        except UnicodeDecodeError:
            _reject("REJECT__INVENTED_UTF8")
        if text.startswith("\ufeff"):
            _reject("REJECT__INVENTED_BOM")
        outcome, code = _schema(_Scanner(text).parse())
    except _Stop as stopped:
        outcome, code = stopped.outcome, stopped.code
    except Exception:
        outcome, code = "REJECT", "REJECT__INVENTED_INTERNAL_FAILURE"
    return _result(outcome, code)
