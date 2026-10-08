"""Single-use synthetic memory pipeline with explicitly injected dependencies.

No discovery, carrier/package import, file, environment, network or model access.
Dependencies are trusted single-threaded engineering callbacks, not a sandbox.
Input must remain stable during preparation; expected declarations are snapshotted
at construction. Provider returns a memory payload accepted by carrier_factory.
"""

from dataclasses import dataclass


class PipelineContractError(ValueError):
    """Invalid dependency, expectation or prepared metadata."""


class PipelineStateError(RuntimeError):
    """Illegal acquisition or reuse of a single-use pipeline."""


class CleanupError(RuntimeError):
    """Cleanup failed without an earlier operational exception."""

    def __init__(self, errors):
        self.errors = tuple(errors)
        super().__init__('pipeline cleanup failed; see errors')


@dataclass(frozen=True, slots=True)
class _Expectation:
    axes: tuple
    fields: tuple
    units: tuple
    calendar: tuple
    source: tuple


def _dict(value, keys, label):
    if (type(value) is not dict or any(type(k) is not str for k in value)
            or set(value) != set(keys)):
        raise PipelineContractError(f'{label}: exact dict and declared keys required')
    return value


def _seq(value, label):
    if type(value) not in (list, tuple):
        raise PipelineContractError(f'{label}: exact list or tuple required')
    return value


def _text(value, label):
    if type(value) is not str or not value.strip():
        raise PipelineContractError(f'{label}: nonblank exact str required')
    return value


def _expectation(raw):
    raw = _dict(raw, ('axes', 'field_names', 'units', 'calendar', 'source'), 'expected')
    axes = _seq(raw['axes'], 'expected.axes')
    if len(axes) != 31:
        raise PipelineContractError('expected.axes: exactly 31 required')
    result, identifiers, names = [], set(), set()
    id_type = None
    for index, axis in enumerate(axes):
        axis = _dict(axis, ('source_id', 'name', 'order'), 'expected.axis')
        identifier = axis['source_id']
        if type(identifier) not in (int, str):
            raise PipelineContractError('expected.axis.source_id: exact int or str required')
        if type(identifier) is str:
            _text(identifier, 'expected.axis.source_id')
        if id_type is None:
            id_type = type(identifier)
        if type(identifier) is not id_type:
            raise PipelineContractError('expected.axes: mixed ID types')
        name = _text(axis['name'], 'expected.axis.name')
        if identifier in identifiers or name in names:
            raise PipelineContractError('expected.axes: duplicate ID or name')
        if type(axis['order']) is not int or axis['order'] != index:
            raise PipelineContractError('expected.axis.order: must match input position')
        identifiers.add(identifier)
        names.add(name)
        result.append((identifier, name, index))
    field_names = tuple(_text(f, 'expected.field_names')
                        for f in _seq(raw['field_names'], 'expected.field_names'))
    if not field_names or len(set(field_names)) != len(field_names):
        raise PipelineContractError('expected.field_names: nonempty unique fields required')
    units = _dict(raw['units'], field_names, 'expected.units')
    frozen_units = tuple(_text(units[f], 'expected.unit') for f in field_names)
    calendar = _dict(raw['calendar'], ('target_year', 'observation_year', 'label'),
                     'expected.calendar')
    if any(type(calendar[k]) is not int for k in ('target_year', 'observation_year')):
        raise PipelineContractError('expected.calendar: exact int years required')
    frozen_calendar = (calendar['target_year'], calendar['observation_year'],
                       _text(calendar['label'], 'expected.calendar.label'))
    source = _dict(raw['source'], ('source_id', 'label'), 'expected.source')
    frozen_source = (_text(source['source_id'], 'expected.source.source_id'),
                     _text(source['label'], 'expected.source.label'))
    return _Expectation(tuple(result), field_names, frozen_units,
                        frozen_calendar, frozen_source)


def _typed_equal(actual, expected):
    """Do not let bool/int or float/int equality disguise metadata mismatch."""
    if type(actual) is not type(expected):
        return False
    if type(expected) is tuple:
        return (len(actual) == len(expected)
                and all(_typed_equal(a, b) for a, b in zip(actual, expected)))
    return actual == expected


def _check_metadata(carrier, expected):
    try:
        actual = _Expectation(
            tuple((a.source_id, a.name, a.order) for a in carrier.axes),
            tuple(v.field for v in carrier.vectors),
            tuple(v.unit for v in carrier.vectors),
            (carrier.calendar.target_year, carrier.calendar.observation_year,
             carrier.calendar.label),
            (carrier.source.source_id, carrier.source.label),
        )
    except (AttributeError, TypeError) as error:
        raise PipelineContractError('factory result: missing carrier metadata') from error
    for name in ('axes', 'fields', 'units', 'calendar', 'source'):
        if not _typed_equal(getattr(actual, name), getattr(expected, name)):
            raise PipelineContractError(f'factory result: expected {name} mismatch')


class SharedInputPipeline:
    """Explicit callback contract and resource ownership.

    provider() -> exact payload dict; provider_close() is registered before that
    call and must safely release even a partially acquired provider resource.
    carrier_factory(**payload) -> validated immutable carrier; it owns cleanup
    of any private partial allocations if it raises before returning.
    handle_factory(carrier) -> handle; its private partial allocations likewise
    remain its responsibility until a handle is returned.
    handle_acquire(handle) -> the identical carrier; handle_close(handle) releases
    the returned handle and must be safe for exactly one cleanup attempt.
    All six callbacks must be supplied and callable, with these signatures.

    prepare returns self; acquire requires prepared/running state. run requires
    two ordered callbacks consumer(carrier), and always closes on success/failure.
    No retries. close is idempotent, attempts handle then provider cleanup, and
    records errors. With a primary error, cleanup never replaces it. Without a
    primary, cleanup failures raise CleanupError. Failed cleanup is not retried.
    Same-thread callbacks may close to cancel. Every callback return is followed
    by a state check; cancellation raises PipelineStateError and cannot reopen.
    A handle returned after cancellation still transfers cleanup ownership here.
    Previously delivered references cannot be revoked. No concurrency guarantee.
    """

    def __init__(self, *, provider, provider_close, carrier_factory, handle_factory,
                 handle_acquire, handle_close, expected):
        dependencies = {
            'provider': provider, 'provider_close': provider_close,
            'carrier_factory': carrier_factory, 'handle_factory': handle_factory,
            'handle_acquire': handle_acquire, 'handle_close': handle_close,
        }
        for name, dependency in dependencies.items():
            if not callable(dependency):
                raise PipelineContractError(f'{name}: explicit callable required')
        self._expected = _expectation(expected)
        self._provider = provider
        self._provider_close = provider_close
        self._carrier_factory = carrier_factory
        self._handle_factory = handle_factory
        self._handle_acquire = handle_acquire
        self._handle_close = handle_close
        self._state = 'new'
        self._provider_attempted = False
        self._handle_returned = False
        self._carrier = None
        self._handle = None
        self._cleanup_errors = ()

    @property
    def state(self):
        return self._state

    @property
    def cleanup_errors(self):
        return self._cleanup_errors

    def _close(self, primary=None):
        self._state = 'closed'
        errors = []
        # Consume each ownership token BEFORE calling cleanup, so reentrant close
        # cannot repeat it. A late returned handle can add a new token even when
        # closed; that token must still be drained without repeating the provider.
        handle = self._handle
        handle_owned = self._handle_returned
        self._handle_returned = False
        self._handle = None
        try:
            if handle_owned:
                try:
                    self._handle_close(handle)
                except BaseException as error:
                    errors.append(error)
            if self._provider_attempted:
                self._provider_attempted = False
                try:
                    self._provider_close()
                except BaseException as error:
                    errors.append(error)
        finally:
            self._carrier = None
            self._handle = None
            self._cleanup_errors += tuple(errors)
        if self._cleanup_errors and primary is not None:
            primary.add_note('pipeline cleanup also failed; see pipeline.cleanup_errors')
        if errors and primary is None:
            raise CleanupError(errors)

    def _require_state(self, state, callback):
        if self._state != state:
            raise PipelineStateError(f'pipeline cancelled during {callback}; remains closed')

    def close(self):
        self._close()

    def prepare(self):
        if self._state != 'new':
            raise PipelineStateError('prepare requires new single-use pipeline')
        self._state = 'preparing'
        try:
            self._provider_attempted = True
            payload = self._provider()
            self._require_state('preparing', 'provider')
            if type(payload) is not dict:
                raise PipelineContractError('provider: exact payload dict required')
            carrier = self._carrier_factory(**payload)
            self._require_state('preparing', 'carrier_factory')
            self._carrier = carrier
            _check_metadata(self._carrier, self._expected)
            self._require_state('preparing', 'metadata validation')
            handle = self._handle_factory(self._carrier)
            # Register the returned resource before checking cancellation: even
            # a close inside its factory cannot leave this new handle unowned.
            self._handle = handle
            self._handle_returned = True
            self._require_state('preparing', 'handle_factory')
            acquired = self._handle_acquire(self._handle)
            self._require_state('preparing', 'handle_acquire')
            if acquired is not self._carrier:
                raise PipelineContractError('handle: must return identical carrier')
            self._state = 'prepared'
            return self
        except BaseException as primary:
            self._close(primary)
            raise

    def acquire(self):
        if self._state not in ('prepared', 'running'):
            raise PipelineStateError('acquire requires prepared/open pipeline')
        try:
            state = self._state
            carrier = self._handle_acquire(self._handle)
            self._require_state(state, 'handle_acquire')
            if carrier is not self._carrier:
                raise PipelineContractError('handle: carrier identity changed')
            return carrier
        except BaseException as primary:
            self._close(primary)
            raise

    def run(self, consumers):
        if self._state not in ('new', 'prepared'):
            raise PipelineStateError('run requires new/prepared single-use pipeline')
        try:
            consumers = _seq(consumers, 'consumers')
            if len(consumers) != 2 or not all(callable(c) for c in consumers):
                raise PipelineContractError('consumers: exactly two explicit callables required')
            # Snapshot the callback list before executing user code.
            first, second = consumers
            if self._state == 'new':
                self.prepare()
            self._require_state('prepared', 'prepare')
            self._state = 'running'
            first_result = first(self.acquire())
            self._require_state('running', 'first consumer')
            second_result = second(self.acquire())
            self._require_state('running', 'second consumer')
        except BaseException as primary:
            self._close(primary)
            raise
        self._close()
        return first_result, second_result

    def __enter__(self):
        return self.prepare()

    def __exit__(self, exc_type, exc_value, traceback):
        self._close(exc_value)
        return False
