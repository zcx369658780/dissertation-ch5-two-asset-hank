"""In-memory terminal-receipt adapter; no file I/O, loader or science imports.

Writer contract: optionb_turn2_household_integration.py:809-831; vector mapping:
k1b_turn5_turn6_bounded_continuation/run.py:215-224. Only selected scalar fields
are copied into immutable tuples. Source, stage and units remain caller
assertions, not authenticated bytes, scientific validity or a live-object seal.
"""
from dataclasses import dataclass, field
import math


FIELD_MAPPING = (('ct', 'Ct'), ('household_lt', 'Lt'), ('at', 'At'),
                 ('bt', 'Bt'), ('at_tax', 'AtTax'))
HOUSEHOLD_STAGE = 'completed_c8_household_pre_outer'


def _label(value):
    return (type(value) is str and bool(value.strip())
            and value.strip().upper() not in {'UNKNOWN', 'UNRESOLVED', 'NONE', 'NULL'})


def _number(value):
    # Preserve the exact built-in scalar and its sign, including negative zero.
    # Integers are mathematically finite; no cast to float or range inference.
    if type(value) not in (int, float) or (type(value) is float and not math.isfinite(value)):
        raise ValueError('finite built-in int/float scalar excluding bool required')
    return value


@dataclass(frozen=True)
class ArchiveDeclaration:
    source_identifier: str
    source_sha256: str  # Declared source identity, not computed/authenticated here.
    province_axis: tuple  # Explicit writer axis: (zero-based index, model short name).
    stage: str
    unit_contract: tuple  # Exactly the five output vector names and declared units.

    def validate(self):
        if type(self) is not ArchiveDeclaration:
            raise ValueError('exact archive declaration required')
        if (not _label(self.source_identifier) or type(self.source_sha256) is not str
                or len(self.source_sha256) != 64
                or any(c not in '0123456789abcdefABCDEF' for c in self.source_sha256)):
            raise ValueError('explicit source identifier and SHA256 declaration required')
        axis = self.province_axis
        if type(axis) is not tuple or not axis:
            raise ValueError('explicit immutable writer province axis required')
        for index, row in enumerate(axis):
            if (type(row) is not tuple or len(row) != 2 or type(row[0]) is not int
                    or row[0] != index or not _label(row[1])):
                raise ValueError('exact zero-based writer index/name order required')
        if len({row[1] for row in axis}) != len(axis):
            raise ValueError('duplicate declared province name')
        if type(self.stage) is not str or self.stage != HOUSEHOLD_STAGE:
            raise ValueError('explicit completed-C8 household/pre-outer stage required')
        units = self.unit_contract
        if (type(units) is not tuple or any(type(row) is not tuple or len(row) != 2
                or not _label(row[0]) or not _label(row[1]) for row in units)):
            raise ValueError('immutable known unit declarations required')
        names = tuple(row[0] for row in units)
        if len(names) != len(FIELD_MAPPING) or set(names) != {name for name, _ in FIELD_MAPPING}:
            raise ValueError('exactly one unit for each of five aggregate vectors required')


@dataclass(frozen=True)
class DeclaredTerminal:
    receipt: dict
    declaration: ArchiveDeclaration


@dataclass(frozen=True)
class ArchiveDiagnostic:
    province_index: int
    province: str
    checkpoint: int
    B: int | float
    D: int | float


@dataclass(frozen=True)
class ArchiveDerivedAggregateCarrier:
    ct: tuple
    household_lt: tuple
    at: tuple
    bt: tuple
    at_tax: tuple
    diagnostics: tuple
    declaration: ArchiveDeclaration
    classification: str = field(default='ARCHIVE_DERIVED', init=False)
    source_authenticated: bool = field(default=False, init=False)
    original_live_identity_restored: bool = field(default=False, init=False)
    scientific_validity_established: bool = field(default=False, init=False)
    model_activation: bool = field(default=False, init=False)


def adapt_terminal_receipts(terminals, *, expected_declaration):
    """Adapt already-parsed declared dicts; never reads or hashes archive files.

    Every terminal separately repeats the caller's source/axis/stage/unit contract.
    Values are selected verbatim; no summing, conversion, clipping or missing-value
    fallback. Output retains no mutable receipt/dict/list references. No converged
    flag is invented from finite diagnostics; this is not a production batch type.
    """
    if type(expected_declaration) is not ArchiveDeclaration:
        raise ValueError('exact expected archive declaration required')
    ArchiveDeclaration.validate(expected_declaration)
    axis = expected_declaration.province_axis
    if type(terminals) is not tuple or len(terminals) != len(axis):
        raise ValueError('complete explicit terminal tuple on declared axis required')
    vectors = {name: [] for name, _ in FIELD_MAPPING}
    diagnostics = []
    for terminal, (index, province) in zip(terminals, axis):
        if type(terminal) is not DeclaredTerminal or type(terminal.receipt) is not dict:
            raise ValueError('exact declared already-parsed terminal dict required')
        if type(terminal.declaration) is not ArchiveDeclaration:
            raise ValueError('each terminal requires an exact archive declaration')
        ArchiveDeclaration.validate(terminal.declaration)
        if terminal.declaration != expected_declaration:
            raise ValueError('terminal source/axis/stage/unit declaration conflict')
        receipt = terminal.receipt
        if (type(receipt.get('province_index')) is not int or receipt['province_index'] != index
                or type(receipt.get('province')) is not str or receipt['province'] != province):
            raise ValueError('terminal province identity duplicate/missing/out of order')
        checkpoint = receipt.get('checkpoint')
        if type(checkpoint) is not int or checkpoint < 0:
            raise ValueError('explicit nonnegative integer checkpoint required')
        if 'B' not in receipt or 'D' not in receipt:
            raise ValueError('explicit terminal B/D diagnostics required')
        B, D = _number(receipt['B']), _number(receipt['D'])
        aggregates = receipt.get('aggregates')
        if type(aggregates) is not dict:
            raise ValueError('explicit aggregate mapping required')
        for output_name, writer_name in FIELD_MAPPING:
            aggregate = aggregates.get(writer_name)
            if type(aggregate) is not dict or 'mass_form' not in aggregate:
                raise ValueError('missing terminal aggregate mass_form: ' + writer_name)
            vectors[output_name].append(_number(aggregate['mass_form']))
        diagnostics.append(ArchiveDiagnostic(index, province, checkpoint, B, D))
    return ArchiveDerivedAggregateCarrier(
        *(tuple(vectors[name]) for name, _ in FIELD_MAPPING),
        tuple(diagnostics), expected_declaration)
