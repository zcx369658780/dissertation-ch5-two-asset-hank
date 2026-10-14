"""Declared fixed-C8 contract, reusing the existing archive and three-axis schema.

This is synthetic engineering, not historical execution/source authentication.
V0.0.1/V0.0.2's SYNTHETIC/NOT_REAL_SOURCE restriction and V0.0.3's
separate producer/context/return/access evidence domains remain in force.
"""
from dataclasses import dataclass, field
import math
import re

SOURCE_KIND = 'SYNTHETIC/NOT_REAL_SOURCE'
FIELDS = ('ct', 'household_lt', 'at', 'bt', 'at_tax')
DOCUMENTED_PRODUCERS = (
    ('c8_caller', 'validators/multi_province/k1b_turn8_outer_r2/run.py', '_execute_after_gate'),
    ('terminal_writer', 'src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py', '_solve_province'),
    ('mass_selector', 'validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py', '_batch'),
)
BASELINE = 'cf74384f151427f0b7071ac0461cede6ad6cdf11'


def scalar(value):
    if type(value) not in (int, float):
        raise ValueError('finite built-in scalar excluding bool required')
    try:
        finite = math.isfinite(value)
    except OverflowError:
        finite = False
    if not finite:
        raise ValueError('nonfinite scalar')
    return value


def five_vectors(batch, n):
    """Select all existing mass_form carrier fields; never aggregate or convert."""
    result = []
    for name in FIELDS:
        values = getattr(batch, name, None)
        if type(values) is not tuple or len(values) != n:
            raise ValueError('complete immutable five-field vector required: ' + name)
        row = tuple(scalar(v) for v in values)
        if name == 'ct' and any(v <= 0 for v in row):
            raise ValueError('positive consumption required')
        if name in ('at', 'household_lt') and any(v < 0 for v in row):
            raise ValueError('nonnegative assets/labor required')
        result.append(row)
    return tuple(result)


@dataclass(frozen=True)
class FixedC8SourceContract:
    # Reuse ArchiveDeclaration and InputDeclaration; no alternate identity system.
    archive_declaration: object
    state_declaration: object
    share_declaration: object
    household_declaration: object
    terminal_checkpoints: tuple
    documented_producers: tuple = DOCUMENTED_PRODUCERS
    documented_code_commit: str = BASELINE
    source_kind: str = SOURCE_KIND
    target_year: int = 2018
    observation_year: int = 2017
    information_set: str = 'retrospective_revised'
    price_basis: str = 'current_price_methodologically_attributed'
    price_verified: bool = False
    direct_price_verified: bool = False
    release: str = 'UNKNOWN'
    baseyear: None = None
    population_basis: str = 'population_per_person_not_households'
    source_evidence: str = 'DECLARED'
    economic_units: str = 'ECONOMIC_UNIT_UNVERIFIED'
    share_orientation: str = 'destination_by_origin'
    share_field_encoding: str = 'little_endian_float64_F_uppercase_sha256'
    annual_layout: str = 'float64_C_order'
    payoff_timing: str = 'COMPLETED_PRIOR_TURN_RAW_RA0'
    source_authenticated: bool = field(default=False, init=False)
    runtime_authorized: bool = field(default=False, init=False)
    model_activation: bool = field(default=False, init=False)
    results: bool = field(default=False, init=False)

    def validate(self, *, archive_module, binding_module, mapping):
        if type(self) is not FixedC8SourceContract or self.source_kind != SOURCE_KIND:
            raise ValueError('only explicit V001/V002 synthetic source kind admitted')
        if (self.documented_producers != DOCUMENTED_PRODUCERS
                or self.documented_code_commit != BASELINE):
            raise ValueError('documented C8 producer conflict; not a runtime pin')
        if (type(self.target_year) is not int or type(self.observation_year) is not int
                or (self.target_year, self.observation_year, self.information_set) !=
                (2018, 2017, 'retrospective_revised')):
            raise ValueError('2017 observation/2018 retrospective target required')
        if (self.price_basis != 'current_price_methodologically_attributed'
                or self.price_verified is not False or self.direct_price_verified is not False
                or self.release != 'UNKNOWN' or self.baseyear is not None):
            raise ValueError('methodological attribution cannot become direct price verification')
        if (self.population_basis != 'population_per_person_not_households'
                or self.source_evidence != 'DECLARED'
                or self.economic_units != 'ECONOMIC_UNIT_UNVERIFIED'
                or any(getattr(self, k) is not False for k in
                       ('source_authenticated', 'runtime_authorized', 'model_activation', 'results'))):
            raise ValueError('declared synthetic evidence cannot grant economic/runtime authority')
        if (self.share_orientation != 'destination_by_origin'
                or self.share_field_encoding != 'little_endian_float64_F_uppercase_sha256'
                or self.annual_layout != 'float64_C_order'
                or self.payoff_timing != 'COMPLETED_PRIOR_TURN_RAW_RA0'):
            raise ValueError('S/annual-layout/raw-payoff timing role conflict')
        declaration = self.archive_declaration
        archive_module.ArchiveDeclaration.validate(declaration)
        if (not declaration.source_identifier.startswith('SIM_')
                or re.fullmatch('[0-9a-fA-F]{64}', declaration.source_sha256) is None):
            raise ValueError('explicit simulated source declaration required')
        if type(mapping) is not tuple or len(mapping) != 31:
            raise ValueError('joint contract requires complete explicit 31-axis mapping')
        model = tuple((r[0], r[1]) for r in mapping)
        annual = tuple((r[2], r[3]) for r in mapping)
        if declaration.province_axis != model:
            raise ValueError('archive/model axis conflict')
        if (type(self.terminal_checkpoints) is not tuple or len(self.terminal_checkpoints) != 31
                or any(type(v) is not int or v < 0 for v in self.terminal_checkpoints)):
            raise ValueError('explicit per-province synthetic terminal checkpoints required')
        declarations = (self.state_declaration, self.share_declaration, self.household_declaration)
        units = None
        for item, stage in zip(declarations, binding_module.STAGES):
            if type(item) is not binding_module.InputDeclaration:
                raise ValueError('reuse exact existing InputDeclaration')
            binding_module._axis(item.model_axis, 0)
            binding_module._axis(item.annual_axis, 1)
            current = binding_module._units(item.unit_contract)
            if (item.stage != stage or item.model_axis != model or item.annual_axis != annual
                    or (units is not None and current != units)):
                raise ValueError('three-input source stage/axis/unit conflict')
            units = current
        combined = dict(units)
        if dict(declaration.unit_contract) != {name: combined[name] for name in FIELDS}:
            raise ValueError('five-field archive/joint unit conflict')
        # These are explicit fixture units, never certifications of MU/NU/hour bridges.
        if any(value != 'synthetic_' + name for name, value in units if name != 'S'):
            raise ValueError('unchanged explicit synthetic unit roles required')
        return self
