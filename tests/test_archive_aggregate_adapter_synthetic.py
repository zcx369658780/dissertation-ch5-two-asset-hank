"""Invented-memory adapter tests only; no archive bytes or scientific imports.

Nine methods: two positive/boundary methods and 68 explicit input-rejection
subcases (14 + 15 + 14 + 7 + 5 + 6 + 7). Three output mutation attempts in the
boundary method are additional assertions, not input-rejection subcases.
"""
import copy
from dataclasses import FrozenInstanceError, replace
import importlib.util
from pathlib import Path
import struct
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
ADAPTER_PATH = ROOT / 'validators/multi_province/annual_observed_labor_diagnostic/archive_aggregate_adapter.py'
spec = importlib.util.spec_from_file_location('_archive_aggregate_adapter_test', ADAPTER_PATH)
adapter = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = adapter
spec.loader.exec_module(adapter)


# Independent writer/_batch contract: never derived from the implementation.
WRITER_VECTOR_CONTRACT = (('ct', 'Ct'), ('household_lt', 'Lt'), ('at', 'At'),
                          ('bt', 'Bt'), ('at_tax', 'AtTax'))


class FloatSubclass(float):
    pass


class AdapterTests(unittest.TestCase):
    def setUp(self):
        self.declaration = adapter.ArchiveDeclaration('invented_terminal_bundle', 'A' * 64,
            ((0, 'Invented North'), (1, 'Invented South')), adapter.HOUSEHOLD_STAGE,
            tuple((name, 'invented_unit') for name, _ in WRITER_VECTOR_CONTRACT))
        # Signed and mixed int/float values are intentional: no sign inference,
        # clipping, float conversion or scientific validity is being tested.
        values = ((7, -2.5, 3.0, -0.0, -4), (1.25, 2, 0.0, -6.0, 0))
        self.receipts = tuple({'province_index': index, 'province': name,
            'checkpoint': 2 + index, 'B': .01, 'D': .02,
            'aggregates': {writer: {'mass_form': value, 'ignored': ['not copied']}
                for (_, writer), value in zip(WRITER_VECTOR_CONTRACT, values[index])},
            'ignored_metadata': {'mutable': []}}
            for index, name in self.declaration.province_axis)

    def wrap(self, receipts=None, declarations=None):
        receipts = self.receipts if receipts is None else receipts
        declarations = (self.declaration,) * len(receipts) if declarations is None else declarations
        return tuple(adapter.DeclaredTerminal(receipt, declaration)
                     for receipt, declaration in zip(receipts, declarations))

    def adapt(self, terminals=None, declaration=None):
        return adapter.adapt_terminal_receipts(self.wrap() if terminals is None else terminals,
            expected_declaration=self.declaration if declaration is None else declaration)

    def reject(self, terminals=None, declaration=None):
        with self.assertRaises(ValueError):
            self.adapt(terminals, declaration)

    def test_correct_mapping_preserves_values_types_and_negative_zero(self):
        before = copy.deepcopy(self.receipts)
        carrier = self.adapt()
        self.assertEqual(adapter.FIELD_MAPPING, WRITER_VECTOR_CONTRACT)
        # Literal vector expectations are independent of both fixture building
        # and implementation FIELD_MAPPING; Lt/At swaps cannot self-validate.
        expected_vectors = {'ct': (7, 1.25), 'household_lt': (-2.5, 2),
                            'at': (3.0, 0.0), 'bt': (-0.0, -6.0), 'at_tax': (-4, 0)}
        for name, expected in expected_vectors.items():
            self.assertEqual(getattr(carrier, name), expected)
        for output_name, writer_name in WRITER_VECTOR_CONTRACT:
            vector = getattr(carrier, output_name)
            self.assertIs(type(vector), tuple)
            for index, value in enumerate(vector):
                original = self.receipts[index]['aggregates'][writer_name]['mass_form']
                self.assertIs(type(value), type(original))
                self.assertEqual(value, original)
                if type(value) is float:
                    self.assertEqual(struct.pack('!d', value), struct.pack('!d', original))
        self.assertEqual(self.receipts, before)
        self.assertEqual(carrier.classification, 'ARCHIVE_DERIVED')
        self.assertFalse(carrier.source_authenticated)
        self.assertFalse(carrier.original_live_identity_restored)
        self.assertFalse(carrier.scientific_validity_established)
        self.assertFalse(carrier.model_activation)
        self.assertFalse(hasattr(carrier, 'converged'))
        self.assertEqual(tuple((d.province_index, d.province) for d in carrier.diagnostics),
                         self.declaration.province_axis)

    def test_output_detaches_mutable_inputs_and_has_frozen_assignment_boundaries(self):
        carrier = self.adapt()
        self.receipts[0]['aggregates']['Ct']['mass_form'] = 999
        self.receipts[0]['aggregates']['Ct']['ignored'].append('changed')
        self.receipts[0]['B'] = 999
        self.receipts[0]['province'] = 'Changed'
        self.assertEqual(carrier.ct, (7, 1.25))
        self.assertEqual(carrier.diagnostics[0].B, .01)
        self.assertEqual(carrier.diagnostics[0].province, 'Invented North')
        self.assertIs(carrier.declaration, self.declaration)  # deeply immutable declared primitives
        with self.assertRaises(FrozenInstanceError):
            carrier.ct = (0, 0)
        with self.assertRaises(TypeError):
            carrier.ct[0] = 0
        with self.assertRaises(FrozenInstanceError):
            carrier.declaration.stage = 'changed'
        # These are Python assignment/alias boundaries, not a tamper seal or
        # protection against concurrent input mutation, object.__setattr__ or OS writes.

    def test_missing_fields_14_rejection_subcases(self):
        cases = [('writer', writer) for _, writer in WRITER_VECTOR_CONTRACT]
        cases += [('mass', writer) for _, writer in WRITER_VECTOR_CONTRACT]
        cases += [('root', name) for name in ('aggregates', 'checkpoint', 'B', 'D')]
        self.assertEqual(len(cases), 14)
        for kind, name in cases:
            with self.subTest(kind=kind, name=name):
                receipts = copy.deepcopy(self.receipts)
                if kind == 'writer':
                    del receipts[0]['aggregates'][name]
                elif kind == 'mass':
                    del receipts[0]['aggregates'][name]['mass_form']
                else:
                    del receipts[0][name]
                self.reject(self.wrap(receipts))

    def test_nonfinite_values_15_rejection_subcases(self):
        cases = [(writer, value) for _, writer in WRITER_VECTOR_CONTRACT
                 for value in (float('nan'), float('inf'), float('-inf'))]
        self.assertEqual(len(cases), 15)
        for writer, value in cases:
            with self.subTest(writer=writer, value=value):
                receipts = copy.deepcopy(self.receipts)
                receipts[0]['aggregates'][writer]['mass_form'] = value
                self.reject(self.wrap(receipts))

    def test_bool_values_14_rejection_subcases(self):
        cases = [('mass', writer, value) for _, writer in WRITER_VECTOR_CONTRACT for value in (True, False)]
        cases += [('root', key, True) for key in ('B', 'D', 'province_index', 'checkpoint')]
        self.assertEqual(len(cases), 14)
        for kind, key, value in cases:
            with self.subTest(kind=kind, key=key, value=value):
                receipts = copy.deepcopy(self.receipts)
                if kind == 'mass':
                    receipts[0]['aggregates'][key]['mass_form'] = value
                else:
                    receipts[0][key] = value
                self.reject(self.wrap(receipts))

    def test_duplicate_wrong_order_missing_identity_7_rejection_subcases(self):
        for case in ('duplicate', 'reverse', 'missing_row', 'missing_index', 'missing_name', 'wrong_index', 'wrong_name'):
            with self.subTest(case=case):
                receipts = copy.deepcopy(self.receipts)
                if case == 'duplicate':
                    receipts = (receipts[0], receipts[0])
                elif case == 'reverse':
                    receipts = tuple(reversed(receipts))
                elif case == 'missing_row':
                    receipts = receipts[:1]
                elif case == 'missing_index':
                    del receipts[0]['province_index']
                elif case == 'missing_name':
                    del receipts[0]['province']
                elif case == 'wrong_index':
                    receipts[0]['province_index'] = 9
                else:
                    receipts[0]['province'] = 'Other'
                self.reject(self.wrap(receipts))

    def test_declaration_conflicts_5_rejection_subcases(self):
        conflicts = (
            replace(self.declaration, source_identifier='different_source'),
            replace(self.declaration, source_sha256='B' * 64),
            replace(self.declaration, stage='entering_c8'),
            replace(self.declaration, unit_contract=tuple((name, 'different_unit')
                                                        for name, _ in WRITER_VECTOR_CONTRACT)),
            replace(self.declaration, province_axis=((0, 'Other'), (1, 'Invented South'))),
        )
        self.assertEqual(len(conflicts), 5)
        for declaration in conflicts:
            with self.subTest(declaration=declaration):
                self.reject(self.wrap(declarations=(declaration, self.declaration)))

    def test_invalid_declarations_6_rejection_subcases(self):
        invalid = (
            replace(self.declaration, province_axis=((0.0, 'Invented North'), (1, 'Invented South'))),
            replace(self.declaration, province_axis=((False, 'Invented North'), (1, 'Invented South'))),
            replace(self.declaration, province_axis=((0, 'Same'), (1, 'Same'))),
            replace(self.declaration, unit_contract=self.declaration.unit_contract[:-1]),
            replace(self.declaration, unit_contract=(('ct', 'UNKNOWN'),) + self.declaration.unit_contract[1:]),
            replace(self.declaration, source_sha256='not-a-digest'),
        )
        self.assertEqual(len(invalid), 6)
        for declaration in invalid:
            with self.subTest(declaration=declaration):
                self.reject(self.wrap(declarations=(declaration, self.declaration)))

    def test_invalid_input_types_7_rejection_subcases(self):
        for case in ('terminal_list', 'receipt_list', 'aggregate_list', 'string_mass', 'null_mass', 'float_subclass', 'declaration_dict'):
            with self.subTest(case=case):
                receipts = copy.deepcopy(self.receipts)
                terminals = self.wrap(receipts)
                if case == 'terminal_list':
                    terminals = list(terminals)
                elif case == 'receipt_list':
                    terminals = (adapter.DeclaredTerminal([], self.declaration), terminals[1])
                elif case == 'aggregate_list':
                    receipts[0]['aggregates'] = []
                elif case == 'string_mass':
                    receipts[0]['aggregates']['Ct']['mass_form'] = '7'
                elif case == 'null_mass':
                    receipts[0]['aggregates']['Ct']['mass_form'] = None
                elif case == 'float_subclass':
                    receipts[0]['aggregates']['Ct']['mass_form'] = FloatSubclass(7.0)
                else:
                    terminals = (adapter.DeclaredTerminal(receipts[0], {}), terminals[1])
                self.reject(terminals)


if __name__ == '__main__':
    if len(sys.argv) != 1:
        raise SystemExit('Invented-memory tests accept no arguments or input files.')
    unittest.main(verbosity=2)
