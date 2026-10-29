"""Two bounded groups: provenance guard, then proposed-consumer algebra."""
from __future__ import annotations

import dataclasses
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "src/ch5_two_asset_hank/multi_province"
NAMESPACE = "temp31_ha_debug_sandbox"


def load_source(name):
    full = NAMESPACE + "." + name
    if full in sys.modules:
        return sys.modules[full]
    if NAMESPACE not in sys.modules:
        package = types.ModuleType(NAMESPACE)
        package.__path__ = [str(SOURCE_DIR)]
        sys.modules[NAMESPACE] = package
    spec = importlib.util.spec_from_file_location(full, SOURCE_DIR / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    sys.modules[full] = module
    spec.loader.exec_module(module)
    return module


class Common(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r4 = load_source("temp31_worksite_tax")
        cls.debug = load_source("temp31_ha_wage_debug")

    def calculation(self, generated=1):
        return self.debug.SyntheticNetWageCalculation(
            firm_wages_by_destination=(5, 10), tax_by_destination=(0.2, 0.6),
            phi_destination_origin=((1, 1), (1, 1)),
            sigma_destination_origin=((0, 0.8), (0.1, 0)),
            phi_l=1, alphal=1, province_order=("A", "B"),
            context_id="SYNTHETIC_TWO_PROVINCE_A", generated_after_iteration=generated)

    def proposal(self):
        return self.debug.prepare_proposed_consumers(self.debug.calculated_round_record(self.calculation(), 2))

    def default_record(self, iteration=1):
        return self.debug.WageRoundRecord(iteration, self.debug.INITIAL_DEFAULT_UNPROVEN,
            (20, 20), ("A", "B"), "SYNTHETIC_TWO_PROVINCE_A")


class ProvenanceGuardTests(Common):
    def test_default_rejected_before_r4_adapter_and_diagnostic_retained(self):
        record = self.default_record()
        with patch.object(self.debug, "adapt_temp31_net_composite_wage", side_effect=AssertionError("must not reach adapter")) as adapter:
            with self.assertRaises(self.debug.WageProvenanceBlocked) as caught:
                self.debug.prepare_proposed_consumers(record)
            adapter.assert_not_called()
        self.assertEqual(caught.exception.diagnostics["observed_wage_by_origin"], (20, 20))
        self.assertFalse(caught.exception.diagnostics["source_reclassified"])
        self.assertEqual(record.provenance, self.debug.INITIAL_DEFAULT_UNPROVEN)

    def test_label_without_witness_is_not_evidence(self):
        forged = dataclasses.replace(self.default_record(2), provenance=self.debug.CALCULATED_NET_AFTER_DESTINATION_TAU_AND_SIGMA)
        with self.assertRaises(self.debug.WageProvenanceBlocked):
            self.debug.prepare_proposed_consumers(forged)

    def test_wrong_observed_wage_rejected_despite_valid_label(self):
        valid = self.debug.calculated_round_record(self.calculation(), 2)
        with self.assertRaises(self.debug.WageProvenanceBlocked):
            self.debug.prepare_proposed_consumers(dataclasses.replace(valid, wage_by_origin=(20, 20)))

    def test_context_and_province_order_cannot_be_substituted(self):
        record = self.debug.calculated_round_record(self.calculation(), 2)
        for change in ({"context_id": "ANOTHER_SYNTHETIC_RUN"}, {"province_order": ("B", "A")}):
            with self.assertRaises(self.debug.WageProvenanceBlocked):
                self.debug.prepare_proposed_consumers(dataclasses.replace(record, **change))

    def test_source_state_transitions_do_not_promote_defaults(self):
        for iteration in (1, 2, 4):
            with self.assertRaises(self.debug.WageProvenanceBlocked):
                self.debug.prepare_proposed_consumers(self.default_record(iteration))
        for entering in (2, 3):
            record = self.debug.calculated_round_record(self.calculation(entering-1), entering)
            result = self.debug.prepare_proposed_consumers(record)
            self.assertEqual(result.record.entering_iteration, entering)

    def test_stale_and_future_rounds_rejected(self):
        for generated, entering in ((1, 3), (2, 2)):
            with self.assertRaises(self.debug.WageProvenanceBlocked):
                self.debug.prepare_proposed_consumers(self.debug.calculated_round_record(self.calculation(generated), entering))

    def test_fixed_source_formula_and_synthetic_scope_required(self):
        for change in ({"source_commit": "0"*40}, {"formula_git_blob": "0"*40}, {"evidence_scope": "REAL_PRODUCTION_VERIFIED"}):
            with self.assertRaises(ValueError):
                self.debug.calculated_round_record(dataclasses.replace(self.calculation(), **change), 2)

    def test_first_round_calculation_is_not_owner_adoption(self):
        record = self.debug.calculated_round_record(self.calculation(), 1)
        with self.assertRaises(self.debug.WageProvenanceBlocked):
            self.debug.prepare_proposed_consumers(record)


class ConsumerAlgebraTests(Common):
    def test_witness_matches_pinned_wage_formula_and_hand_golden(self):
        witness = self.calculation()
        wages = self.debug.recompute_synthetic_net_wage(witness)
        self.assertAlmostEqual(wages[0], 5)
        self.assertAlmostEqual(wages[1], 4)
        old = load_source("wage").composite_household_wages(
            [{"tau": t} for t in witness.tax_by_destination], witness.firm_wages_by_destination,
            witness.phi_destination_origin, witness.sigma_destination_origin,
            phi_l=witness.phi_l, alphal=witness.alphal)
        for a, b in zip(wages, old):
            self.assertAlmostEqual(a, b)

    def test_initialization_and_hjb_share_net_data_and_keep_real_taxes(self):
        proposal = self.proposal()
        self.assertIs(proposal.views.initialization, proposal.views.hjb)
        self.assertEqual(proposal.views.tax_by_destination, (0.2, 0.6))
        self.assertEqual(proposal.views.migration_wedge_destination_origin, ((0, 0.8), (0.1, 0)))
        for item, expected in zip(proposal.views.initialization, (5, 4)):
            self.assertAlmostEqual(item.effective_wage, expected)
            self.assertEqual((item.tau_for_HA, item.sigma_for_HA), (0, 0))

    def test_wrong_second_tax_is_rejected_by_data_and_consumer_guard(self):
        p = self.proposal()
        with self.assertRaises(ValueError):
            dataclasses.replace(p.views.hjb[0], tau_for_HA=0.2)
        wrong = dataclasses.replace(p.views.hjb[0], w_for_HA=p.views.hjb[0].w_for_HA * 0.8)
        changed = dataclasses.replace(p.views, hjb=(wrong, p.views.hjb[1]))
        with self.assertRaises(ValueError):
            self.debug.probe_proposed_resource_identity(dataclasses.replace(p, views=changed), origin=0, z=1, labor=1)

    def test_wrong_second_migration_wedge_and_global_tax_zeroing_rejected(self):
        p = self.proposal()
        with self.assertRaises(ValueError):
            dataclasses.replace(p.views.hjb[0], sigma_for_HA=0.1)
        wrong = dataclasses.replace(p.views.hjb[0], w_for_HA=p.views.hjb[0].w_for_HA * 0.9)
        for views in (dataclasses.replace(p.views, initialization=(wrong, p.views.initialization[1]), hjb=(wrong, p.views.hjb[1])),
                      dataclasses.replace(p.views, tax_by_destination=(0, 0))):
            with self.assertRaises(ValueError):
                self.debug.probe_proposed_resource_identity(dataclasses.replace(p, views=views), origin=0, z=1, labor=1)

    def test_hand_resource_identity_all_three_proposed_consumers(self):
        probe = self.debug.probe_proposed_resource_identity(self.proposal(), origin=0,
            z=0.5, labor=2, transfer=2, rb=0.1, liquid_assets=10, other_asset_resources=3, saving_flow=4)
        for actual in (probe.initialization_wage_income, probe.hjb_boundary_wage_income, probe.policy_wage_income):
            self.assertAlmostEqual(actual, 5)
        self.assertAlmostEqual(probe.total_resources, 11)
        self.assertAlmostEqual(probe.illustrative_consumption_after_saving, 7)

    def test_distinct_z_labor_and_origin_do_not_duplicate_efficiency(self):
        for origin, z, labor, income, consumption in ((0, 1.5, 2, 15, 17), (1, 2, 0.5, 4, 6), (0, 3, 0, 0, 2)):
            probe = self.debug.probe_proposed_resource_identity(self.proposal(), origin=origin,
                z=z, labor=labor, transfer=2, rb=0.1, liquid_assets=10, other_asset_resources=3, saving_flow=4)
            self.assertAlmostEqual(probe.initialization_wage_income, income)
            self.assertAlmostEqual(probe.hjb_boundary_wage_income, income)
            self.assertAlmostEqual(probe.policy_wage_income, income)
            self.assertAlmostEqual(probe.illustrative_consumption_after_saving, consumption)

    def test_three_province_nonunit_elasticity_against_unchanged_wage(self):
        witness = self.debug.SyntheticNetWageCalculation((2, 3, 4), (0.1, 0.2, 0.3),
            ((1, 1, 1),)*3, ((0, 0.1, 0.2), (0.2, 0, 0.1), (0.1, 0.2, 0)),
            2, 2, ("A", "B", "C"), "SYNTHETIC_THREE_PROVINCE", 2)
        new = self.debug.recompute_synthetic_net_wage(witness)
        old = load_source("wage").composite_household_wages([{"tau": t} for t in witness.tax_by_destination],
            witness.firm_wages_by_destination, witness.phi_destination_origin,
            witness.sigma_destination_origin, phi_l=2, alphal=2)
        for a, b in zip(new, old):
            self.assertAlmostEqual(a, b)
        self.debug.prepare_proposed_consumers(self.debug.calculated_round_record(witness, 3))

    def test_invalid_algebra_and_immutable_witness_inputs(self):
        for change in ({"phi_destination_origin": ((0, 1), (1, 1))}, {"tax_by_destination": (2, 0.6)}, {"firm_wages_by_destination": (5,)}):
            with self.assertRaises(ValueError):
                self.debug.recompute_synthetic_net_wage(dataclasses.replace(self.calculation(), **change))
        for z, labor in ((0, 1), (1, -1), (float("nan"), 1)):
            with self.assertRaises(ValueError):
                self.debug.probe_proposed_resource_identity(self.proposal(), origin=0, z=z, labor=labor)
        with self.assertRaises(dataclasses.FrozenInstanceError):
            self.calculation().context_id = "changed"

    def test_history_and_r4_source_bytes_unchanged(self):
        identity = json.loads((ROOT / "tasks/CH5_TEMP31_HA_WAGE_FIRST_ROUND_PROVENANCE_AND_CONSUMER_STATIC_DEBUG_R1_20261028/source_identity.json").read_text())
        for record in identity["source_files"]:
            raw = (ROOT / record["path"]).read_bytes()
            self.assertEqual(len(raw), record["bytes"])
            self.assertEqual(hashlib.sha256(raw).hexdigest(), record["sha256"])
            self.assertEqual(hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest(), record["git_blob"])
        # R4's permissive pure label API remains unchanged; R5 guards it first.
        old = self.r4.adapt_temp31_net_composite_wage((20, 20), semantic=self.r4.NET_COMPOSITE,
            tax_by_destination=(0.2, 0.6), migration_wedge_destination_origin=((0, 0.8), (0.1, 0)))
        self.assertEqual(old.initialization[0].effective_wage, 20)

