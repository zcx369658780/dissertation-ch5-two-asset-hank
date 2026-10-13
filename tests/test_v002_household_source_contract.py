"""V0.0.2 synthetic source-contract tests; no solver, file loader or outer turn."""
from dataclasses import FrozenInstanceError, replace
from pathlib import Path
import os
import sys

import numpy as np
import pytest

from ch5_two_asset_hank.multi_province import household_source_contract as boundary
from ch5_two_asset_hank.multi_province import synthetic_household_bridge as bridge
from ch5_two_asset_hank.multi_province import corrected_household_adapter as adapter


def fixture(province="SYNTH_A", source="SIM_SOURCE_A"):
    identity = boundary.HouseholdSourceIdentity(province, source, 1, "SIM_CP1", "SIM_GRID1")
    shape = (20, 20, 2)
    p = np.zeros(shape, order="F")
    c = np.ones(shape, order="F")
    labor = np.zeros(shape, order="F")
    effective = np.full(shape, .04, order="F")
    for cell, mass, consumption, ell, rah in [((0, 0, 0), .2, 2., .5, .04),
                                            ((7, 4, 1), .3, 4., 1.5, .05),
                                            ((19, 19, 0), .5, 8., 2., .06)]:
        p[cell], c[cell], labor[cell], effective[cell] = mass, consumption, ell, rah
    payload = dict(consumption=c, labor=labor, b_grid=np.linspace(-2, 5, 20),
                   a_grid=np.linspace(0, 10, 20), z_grid=np.array([.8, 1.3]),
                   effective_r_a=effective, probability_mass=p, density=p/(70/361),
                   omega=70/361, source_r_a=.1,
                   flat_indices_b_a_z=np.column_stack(np.unravel_index(np.arange(800), shape, order="F")))
    return identity, payload, metadata(identity, payload)


def metadata(identity, payload):
    refs = tuple(boundary.SimulatedFieldReference(name, identity, boundary.FIELD_ROLES[name],
                  boundary.simulated_field_digest(name, value)) for name, value in payload.items())
    value = boundary.HouseholdSourceMetadata(identity=identity, field_references=refs,
              simulated_seal_sha256="0"*64)
    return replace(value, simulated_seal_sha256=boundary.simulated_manifest_digest(value))


def reseal(meta):
    return replace(meta, simulated_seal_sha256=boundary.simulated_manifest_digest(meta))


def admit(identity, payload, meta):
    return boundary.admit_synthetic_household_record(meta, payload, requested_identity=identity)


def test_real_aggregate_frozen_batch_and_independent_scalar_oracle():
    ia, pa, ma = fixture()
    ib, pb, mb = fixture("SYNTH_B", "SIM_SOURCE_B")
    snapshots = {k: np.array(v, copy=True) for k, v in pa.items()}
    assessment = boundary.assess_source_contract(ma, pa, requested_identity=ia)
    assert assessment.admitted
    assert assessment.evidence_level == "SYNTHETIC_ENGINEERING"
    assert assessment.real_source_authentication == "NOT_VERIFIED"
    a, b = admit(ia, pa, ma), admit(ib, pb, mb)
    # Exercise unchanged implementations, not a substitute reduction.
    aggregate = adapter.evaluate_corrected_household_aggregates(a.aggregate_inputs)
    frozen = aggregate.frozen_output(converged=False, convergence_statistic=0.)
    batch = bridge.build_synthetic_household_batch([a, b], province_order=("SYNTH_A", "SYNTH_B"), iteration=1)
    # Three occupied cells only: explicit fractions and scalars, no vectorized oracle.
    expected = dict(Ct=.2*2+.3*4+.5*8,
                    Lt=.2*.8*.5+.3*1.3*1.5+.5*.8*2,
                    At=.3*(40/19)+.5*10,
                    Bt=.2*(-2)+.3*(11/19)+.5*5,
                    AtTax=(.3*(40/19)+.5*10)*.1-(.3*(40/19)*.05+.5*10*.06))
    for name, wanted in expected.items():
        assert getattr(aggregate, name).mass_form == pytest.approx(wanted, abs=2e-14, rel=0)
        assert getattr(frozen, name) == pytest.approx(wanted, abs=2e-14, rel=0)
    for field, name in [("ct", "Ct"), ("household_lt", "Lt"), ("at", "At"), ("bt", "Bt"), ("at_tax", "AtTax")]:
        assert getattr(batch, field) == pytest.approx([expected[name]]*2, abs=2e-14, rel=0)
    assert batch.converged == (False, False)
    assert all(d["source_kind"] == "SYNTHETIC/NOT_REAL_SOURCE" and d["evidence_level"] == "SYNTHETIC_ENGINEERING" for d in batch.diagnostics)
    for key, original in snapshots.items():
        assert np.array_equal(pa[key], original)
    pa["consumption"][0, 0, 0] = 99
    pa["flat_indices_b_a_z"][0] = 99
    assert a.aggregate_inputs.consumption[0, 0, 0] == 2
    assert np.array_equal(a.flat_indices_b_a_z[0], [0, 0, 0])
    assert not a.aggregate_inputs.consumption.flags.writeable
    with pytest.raises(FrozenInstanceError):
        a.source_kind = "REAL"


@pytest.mark.parametrize("kind", ["REAL", "UNKNOWN", "SOURCE_ONLY", "HISTORICAL_ACCEPTED", "SYNTHETIC", "", None])
def test_non_synthetic_never_admitted_even_with_recomputed_seal(kind):
    identity, payload, meta = fixture()
    meta = reseal(replace(meta, source_kind=kind))
    assert not boundary.assess_source_contract(meta, payload, requested_identity=identity).admitted
    with pytest.raises(ValueError, match="source_kind"):
        admit(identity, payload, meta)


@pytest.mark.parametrize("attribute,value", [("province", "SYNTH_B"), ("source_id", "SIM_OTHER"),
    ("iteration", 2), ("checkpoint_id", "SIM_CP2"), ("grid_id", "SIM_GRID2")])
def test_joint_identity_conflicts(attribute, value):
    identity, payload, meta = fixture()
    wrong = replace(identity, **{attribute: value})
    # Whole declaration and field seals agree with each other but not the request.
    meta = metadata(wrong, payload)
    with pytest.raises(ValueError, match="requested identity"):
        admit(identity, payload, meta)
    # Only one field references another producer/stage/checkpoint/grid.
    meta = metadata(identity, payload)
    refs = list(meta.field_references)
    refs[0] = replace(refs[0], identity=wrong)
    with pytest.raises(ValueError, match="field identity"):
        admit(identity, payload, reseal(replace(meta, field_references=tuple(refs))))


@pytest.mark.parametrize("field", list(boundary.FIELD_ROLES))
def test_missing_field_rejected(field):
    identity, payload, meta = fixture()
    del payload[field]
    with pytest.raises(ValueError, match="payload fields"):
        admit(identity, payload, meta)


@pytest.mark.parametrize("case", ["missing_seal", "bad_seal", "missing_ref", "duplicate_ref", "bad_digest", "false_boolean", "role_swap", "axes", "flatten"])
def test_manifest_and_declaration_rejections(case):
    identity, payload, meta = fixture()
    if case == "missing_seal": meta = replace(meta, simulated_seal_sha256="")
    if case == "bad_seal": meta = replace(meta, simulated_seal_sha256="a"*64)
    if case == "missing_ref": meta = reseal(replace(meta, field_references=meta.field_references[:-1]))
    if case == "duplicate_ref": meta = reseal(replace(meta, field_references=meta.field_references+(meta.field_references[0],)))
    if case == "bad_digest":
        refs = list(meta.field_references); refs[0] = replace(refs[0], digest_sha256="a"*64)
        meta = reseal(replace(meta, field_references=tuple(refs)))
    if case == "false_boolean": payload["REAL_AUTHENTICATED"] = True
    if case == "role_swap":
        refs = tuple(replace(r, role="STATE_DEPENDENT_EFFECTIVE_RETURN") if r.field == "source_r_a" else r for r in meta.field_references)
        meta = reseal(replace(meta, field_references=refs))
    if case == "axes": meta = reseal(replace(meta, axis_order=("a", "b", "z")))
    if case == "flatten": meta = reseal(replace(meta, flatten_order="C"))
    with pytest.raises(ValueError): admit(identity, payload, meta)


@pytest.mark.parametrize("case", ["omega", "p_g", "negative", "nonunit", "nan", "inf", "indices", "float_indices", "grid", "shape", "effective_scalar", "uniform_array", "complex", "string"])
def test_numeric_rejections_even_when_payload_resealed(case):
    identity, payload, meta = fixture()
    if case == "omega": payload["omega"] = 1.
    if case == "p_g": payload["density"][0, 0, 0] += 1
    if case == "negative":
        payload["probability_mass"][0, 0, 0] = -.2
        payload["probability_mass"][1, 0, 0] = .4
        payload["density"] = payload["probability_mass"] / payload["omega"]
    if case == "nonunit":
        payload["probability_mass"] *= .9; payload["density"] *= .9
    if case == "nan": payload["probability_mass"][0, 0, 0] = np.nan
    if case == "inf": payload["probability_mass"][0, 0, 0] = np.inf
    if case == "indices": payload["flat_indices_b_a_z"] = payload["flat_indices_b_a_z"][:, [1, 0, 2]]
    if case == "float_indices": payload["flat_indices_b_a_z"] = payload["flat_indices_b_a_z"].astype(float)
    if case == "grid": payload["a_grid"][1] += .01
    if case == "shape": payload["consumption"] = np.ones((2, 20, 2))
    if case == "effective_scalar": payload["effective_r_a"] = .1
    if case == "uniform_array": payload["source_r_a"] = np.full((20, 20, 2), .1)
    if case == "complex": payload["consumption"] = payload["consumption"].astype(complex)
    if case == "string": payload["source_r_a"] = "0.1"
    # Digest construction allows describing invalid numeric inputs; admission rejects.
    try:
        meta = metadata(identity, payload)
    except (ValueError, TypeError):
        pass
    with pytest.raises((ValueError, TypeError)): admit(identity, payload, meta)


def test_post_seal_mutation_is_rejected():
    identity, payload, meta = fixture()
    payload["labor"][7, 4, 1] += .25
    with pytest.raises(ValueError, match="digest"):
        admit(identity, payload, meta)


@pytest.mark.parametrize("case", ["duplicate", "missing", "reordered"])
def test_original_batch_rejects_duplicate_missing_or_reordered_provinces(case):
    ia, pa, ma = fixture(); ib, pb, mb = fixture("SYNTH_B", "SIM_SOURCE_B")
    a, b = admit(ia, pa, ma), admit(ib, pb, mb)
    records = {"duplicate": [a, a], "missing": [a], "reordered": [b, a]}[case]
    with pytest.raises(ValueError):
        bridge.build_synthetic_household_batch(records, province_order=("SYNTH_A", "SYNTH_B"), iteration=1)


def test_self_consistent_transpose_cannot_be_authenticated_by_digest():
    identity, payload, meta = fixture()
    original = admit(identity, payload, meta)
    payload["consumption"] = payload["consumption"].swapaxes(0, 1)
    transposed = admit(identity, payload, metadata(identity, payload))
    before = adapter.evaluate_corrected_household_aggregates(original.aggregate_inputs).Ct.mass_form
    after = adapter.evaluate_corrected_household_aggregates(transposed.aggregate_inputs).Ct.mass_form
    assert before == pytest.approx(5.6)
    assert after == pytest.approx(4.7)
    assert transposed.source_kind == "SYNTHETIC/NOT_REAL_SOURCE"


def test_no_real_authenticated_switch_and_metadata_snapshot():
    identity, payload, meta = fixture()
    with pytest.raises(TypeError):
        boundary.HouseholdSourceMetadata(identity=identity, field_references=meta.field_references,
            simulated_seal_sha256=meta.simulated_seal_sha256, REAL_AUTHENTICATED=True)
    refs = list(meta.field_references)
    copy = replace(meta, field_references=refs)
    refs.clear()
    assert len(copy.field_references) == 11
    with pytest.raises(FrozenInstanceError): copy.source_kind = "REAL"


@pytest.mark.parametrize("attribute,value", [("iteration", True), ("iteration", 0),
    ("province", "REAL_A"), ("source_id", ""), ("checkpoint_id", ""), ("grid_id", "")])
def test_invalid_identity_cannot_be_a_request(attribute, value):
    identity, payload, meta = fixture()
    with pytest.raises(ValueError): replace(identity, **{attribute: value})


def test_assessment_does_not_authorize_later_changed_payload():
    identity, payload, meta = fixture()
    assert boundary.assess_source_contract(meta, payload, requested_identity=identity).admitted
    payload["source_r_a"] = .2
    with pytest.raises(ValueError, match="digest"):
        admit(identity, payload, meta)


def test_effective_return_role_cannot_be_uniform():
    identity, payload, meta = fixture()
    refs = tuple(replace(r, role="UNIFORM_SOURCE_RETURN") if r.field == "effective_r_a" else r for r in meta.field_references)
    with pytest.raises(ValueError, match="role"):
        admit(identity, payload, reseal(replace(meta, field_references=refs)))


def test_candidate_sources_and_prohibited_calls_are_absent():
    view = Path(os.environ["CH5_CANDIDATE_VIEW"]).resolve()
    for name, module in tuple(sys.modules.items()):
        if name.startswith("ch5_two_asset_hank") and getattr(module, "__file__", None):
            assert Path(module.__file__).resolve().is_relative_to(view)
    # Import definitions is distinct from invoking science; use a profile guard
    # around real admission/batch to observe no prohibited runtime entry.
    forbidden = {"solve_hjb", "solve_stationary_kfe", "solve_household_steady_state",
                 "run_source_faithful_one_turn", "evaluate_firm", "run_synthetic_bridge_once"}
    called = []
    def profile(frame, event, arg):
        if event == "call" and frame.f_code.co_name in forbidden: called.append(frame.f_code.co_name)
    ia, pa, ma = fixture(); ib, pb, mb = fixture("SYNTH_B", "SIM_SOURCE_B")
    sys.setprofile(profile)
    try:
        bridge.build_synthetic_household_batch([admit(ia, pa, ma), admit(ib, pb, mb)],
             province_order=("SYNTH_A", "SYNTH_B"), iteration=1)
    finally:
        sys.setprofile(None)
    assert called == []
