"""V0.0.1: synthetic engineering only; never a real household/GE run."""

from dataclasses import FrozenInstanceError, replace
import json
import math
import os
from pathlib import Path
import sys

import numpy as np
import pytest

from ch5_two_asset_hank.multi_province import corrected_household_adapter as adapter
from ch5_two_asset_hank.multi_province import one_turn
from ch5_two_asset_hank.multi_province import synthetic_household_bridge as bridge
from ch5_two_asset_hank.multi_province.household_adapter import FrozenHouseholdOutputs


def fixture(n=2, *, labor_scale=1.0, consumption_scale=1.0):
    order = tuple(f"SYNTH_{i}" for i in range(n))
    records, states, originals = [], [], []
    shape = (20, 20, 2)
    indices = np.column_stack(np.unravel_index(np.arange(800), shape, order="F"))
    b, a, z = np.linspace(-2, 5, 20), np.linspace(0, 10, 20), np.array([.8, 1.3])
    for i, name in enumerate(order):
        coordinates = np.indices(shape)
        c = consumption_scale * (1.4 + .03*coordinates[0] + .07*coordinates[1] + .2*coordinates[2] + .1*i)
        labor = labor_scale * (.4 + .01*coordinates[0] + .02*coordinates[1] + .08*coordinates[2] + .05*i)
        p = np.zeros(shape)
        for index, weight in zip(((0, 1, 0), (3, 8, 1), (17, 13, 0), (19, 19, 1)), (.125, .25, .125, .5)):
            p[index] = weight
        rah = .06 + .005*i
        effective = np.broadcast_to(rah*(1-.1*(a[None, :, None]/10)**9), shape)
        inputs = adapter.CorrectedHouseholdAggregateInputs(c, labor, b, a, z, effective, p, p/(70/361), 70/361, rah)
        records.append(bridge.SyntheticHouseholdRecord(name, 1, f"fixture-{i}", inputs, indices))
        originals.append(inputs)
        states.append(dict(name=name, source_kind=bridge.SOURCE_KIND, synthetic_iteration=1,
                           synthetic_source_id=f"fixture-{i}", N=10.0+3*i, wjt=1.0+.15*i,
                           tau=.1+.01*i, inter_prv_ratio=.3+.05*i, ra=.05+.01*i,
                           GovInv=1., alpha=.3, Zt=1.2, pit=0., Kt_prev=5., Lt_prev=999.,
                           Zt_1=1.2, pit_1=0., rk=.04, corptau=.2, AtTax=999., Tt=.1,
                           ramin=.02, ramax=.09, wjtmin=.01, wjtmax=10.))
    params = dict(ga=2., phi_l=2., alphal=1., epsilon=6., theta=2., delta=.05,
                  istar=.03, rho_pi=1.5, totalpit=0., epsilon_pi=0.)
    phi = np.array([[1.+.2*j+.1*i for i in range(n)] for j in range(n)])
    wedge = np.array([[.01*(1+j+2*i) for i in range(n)] for j in range(n)])
    return records, dict(province_order=order, entering_states=tuple(states), iteration=1,
                         params=params, phi_destination_origin=phi, migration_wedge_destination_origin=wedge), originals


def oracle(inputs):
    """Separate scalar loops: no production reduction or frozen factory used."""
    ct, lt, at, bt, flow = [], [], [], [], []
    for iz, z in enumerate(inputs.z_grid):
        for ia, a in enumerate(inputs.a_grid):
            for ib, b in enumerate(inputs.b_grid):
                index = (ib, ia, iz)
                p = float(inputs.probability_mass[index])
                ct.append(float(inputs.consumption[index])*p)
                lt.append(float(z)*float(inputs.labor[index])*p)
                at.append(float(a)*p)
                bt.append(float(b)*p)
                flow.append(float(a)*float(inputs.effective_r_a[index])*p)
    a_total = math.fsum(at)
    return dict(ct=math.fsum(ct), household_lt=math.fsum(lt), at=a_total,
                bt=math.fsum(bt), at_tax=a_total*inputs.source_r_a-math.fsum(flow))


def migration_oracle(kwargs, ct):
    n = len(ct)
    matrix = np.zeros((n, n))
    for destination in range(n):
        for origin in range(n):
            s = kwargs["entering_states"][origin]
            w = kwargs["entering_states"][destination]["wjt"]
            base = w*(1-s["tau"]-kwargs["migration_wedge_destination_origin"][destination, origin])/kwargs["phi_destination_origin"][destination, origin]
            matrix[destination, origin] = ct[origin]**(-kwargs["params"]["ga"]/kwargs["params"]["phi_l"])*base**(1/kwargs["params"]["phi_l"])*s["N"]
    return matrix


@pytest.mark.parametrize("n", [2, 3])
def test_same_call_chain_real_aggregates_callback_one_turn_and_firm(monkeypatch, n):
    records, kwargs, _ = fixture(n)
    events, frozen, captured = [], [], []
    real_aggregate = adapter.evaluate_corrected_household_aggregates
    real_frozen = adapter.CorrectedHouseholdAggregates.frozen_output
    real_factory = bridge.make_synthetic_household_callback
    real_firm = one_turn.evaluate_firm
    def aggregate(inputs):
        events.append("aggregate")
        return real_aggregate(inputs)
    def freeze(self, **flags):
        output = real_frozen(self, **flags)
        frozen.append(output)
        return output
    def factory(*args, **kw):
        callback = real_factory(*args, **kw)
        def observe(states, iteration):
            events.append("callback")
            assert states == kwargs["entering_states"] and iteration == 1
            return callback(states, iteration)
        return observe
    def firm(source, kt, lt, params):
        captured.append((dict(source), float(lt)))
        events.append("firm")
        return real_firm(source, kt, lt, params)
    monkeypatch.setattr(adapter, "evaluate_corrected_household_aggregates", aggregate)
    monkeypatch.setattr(adapter.CorrectedHouseholdAggregates, "frozen_output", freeze)
    monkeypatch.setattr(bridge, "make_synthetic_household_callback", factory)
    monkeypatch.setattr(one_turn, "evaluate_firm", firm)
    old_states = tuple(dict(s) for s in kwargs["entering_states"])
    result = bridge.run_synthetic_bridge_once(records, **kwargs)
    expected = [oracle(r.aggregate_inputs) for r in records]
    for field in ("ct", "household_lt", "at", "bt", "at_tax"):
        np.testing.assert_allclose(getattr(result.household_outputs, field), [o[field] for o in expected], rtol=2e-14, atol=2e-14)
        assert not getattr(result.household_outputs, field).flags.writeable
    for i, output in enumerate(frozen):
        assert output.Lt == result.household_outputs.household_lt[i]
        assert output.Ct == result.household_outputs.ct[i]
        assert output.converged is False
    matrix = migration_oracle(kwargs, [o["ct"] for o in expected])
    np.testing.assert_allclose(result.migration.lt_mat, matrix)
    np.testing.assert_allclose([s["Lt_prev"] for s, _ in captured], [o["household_lt"] for o in expected])
    np.testing.assert_allclose([s["AtTax"] for s, _ in captured], [o["at_tax"] for o in expected])
    np.testing.assert_allclose([lt for _, lt in captured], matrix.sum(axis=1))
    np.testing.assert_allclose([f.Lt for f in result.firms], matrix.sum(axis=1))
    assert not np.allclose(result.household_outputs.household_lt, result.migration.lt_supply)
    assert events == ["callback"] + ["aggregate"]*n + ["firm"]*n
    assert tuple(dict(s) for s in kwargs["entering_states"]) == old_states
    for d in result.household_outputs.diagnostics:
        assert d["source_kind"] == bridge.SOURCE_KIND
        assert d["evidence_level"] == "SYNTHETIC_ENGINEERING"
        assert d["convergence_evidence"] == "SYNTHETIC_FLAG_NOT_HJB_B_D"
    receipt = dict(source_kind=bridge.SOURCE_KIND, synthetic_province_order=list(kwargs["province_order"]),
                   callback_calls=events.count("callback"), aggregate_calls=events.count("aggregate"),
                   delegated_original_firm_calls=len(captured), independent_oracle=True,
                   household_lt=result.household_outputs.household_lt.tolist(),
                   captured_lt_prev=[s["Lt_prev"] for s, _ in captured],
                   migration_lt_supply=result.migration.lt_supply.tolist(),
                   captured_current_lt=[lt for _, lt in captured],
                   real_solver_calls=0, real_data_calls=0, science_acceptance=False, results=False)
    print("SYNTHETIC_CHAIN_RECEIPT="+json.dumps(receipt, sort_keys=True))


def test_distinct_labor_paths_and_consumption_effect(monkeypatch):
    captured = []
    real_firm = one_turn.evaluate_firm
    def observe(source, kt, lt, params):
        captured.append((source["Lt_prev"], lt))
        return real_firm(source, kt, lt, params)
    monkeypatch.setattr(one_turn, "evaluate_firm", observe)
    records, kwargs, _ = fixture()
    baseline = bridge.run_synthetic_bridge_once(records, **kwargs)
    altered, altered_kwargs, _ = fixture(labor_scale=2.)
    labor = bridge.run_synthetic_bridge_once(altered, **altered_kwargs)
    np.testing.assert_allclose(labor.household_outputs.household_lt, 2*baseline.household_outputs.household_lt)
    np.testing.assert_array_equal(labor.migration.lt_supply, baseline.migration.lt_supply)
    np.testing.assert_allclose([v[0] for v in captured[2:4]], 2*np.array([v[0] for v in captured[:2]]))
    np.testing.assert_array_equal([v[1] for v in captured[2:4]], [v[1] for v in captured[:2]])
    # At pit=0 the existing mt formula cancels the Lt_prev term. Input
    # propagation does not imply unconditional economic-output sensitivity.
    assert labor.firms[0].mt == baseline.firms[0].mt
    altered, altered_kwargs, _ = fixture(consumption_scale=2.)
    consumption = bridge.run_synthetic_bridge_once(altered, **altered_kwargs)
    np.testing.assert_array_equal(consumption.household_outputs.household_lt, baseline.household_outputs.household_lt)
    np.testing.assert_allclose(consumption.migration.lt_supply, baseline.migration.lt_supply/2)


def test_original_firm_reference_labor_sensitivity_has_independent_oracle():
    records, kwargs, _ = fixture()
    changed, other_kwargs, _ = fixture(labor_scale=2.)
    # Explicit synthetic branch probe, not a production calibration change.
    for payload in (kwargs, other_kwargs):
        for state in payload["entering_states"]:
            state["pit"] = .01
            state["pit_1"] = .01
    baseline = bridge.run_synthetic_bridge_once(records, **kwargs)
    altered = bridge.run_synthetic_bridge_once(changed, **other_kwargs)
    for i, (old, new) in enumerate(zip(baseline.firms, altered.firms)):
        state = kwargs["entering_states"][i]
        reference_change = altered.household_outputs.household_lt[i]-baseline.household_outputs.household_lt[i]
        delta = -(1-state["alpha"])*reference_change/old.Lt*state["pit"]*kwargs["params"]["theta"]/kwargs["params"]["epsilon"]
        assert new.mt-old.mt == pytest.approx(delta, rel=1e-10, abs=1e-15)


def test_record_and_output_snapshots_are_detached_and_readonly():
    records, kwargs, originals = fixture()
    baseline = bridge.build_synthetic_household_batch(records, province_order=kwargs["province_order"], iteration=1)
    originals[0].consumption.flags.writeable = True
    originals[0].consumption[:] = 999
    assert not np.shares_memory(records[0].aggregate_inputs.consumption, originals[0].consumption)
    again = bridge.build_synthetic_household_batch(records, province_order=kwargs["province_order"], iteration=1)
    np.testing.assert_array_equal(again.ct, baseline.ct)
    assert not np.shares_memory(again.ct, baseline.ct)
    with pytest.raises(ValueError):
        baseline.ct[0] = 99
    with pytest.raises(FrozenInstanceError):
        records[0].source_id = "changed"
    with pytest.raises(TypeError):
        baseline.diagnostics[0]["source_kind"] = "REAL"


@pytest.mark.parametrize("change", [dict(source_kind="REAL"), dict(source_kind=""), dict(province="RealProvince"),
    dict(axis_order=("a", "b", "z")), dict(flatten_order="C"), dict(iteration=True), dict(iteration=0),
    dict(synthetic_converged=1), dict(synthetic_convergence_statistic=-1.), dict(source_id="")])
def test_record_rejects_source_axis_stage_and_flags(change):
    records, _, _ = fixture()
    with pytest.raises(ValueError):
        replace(records[0], **change)


def test_f_order_indices_reject_c_order_and_noninteger_mapping():
    records, _, _ = fixture()
    indices = np.column_stack(np.unravel_index(np.arange(800), (20, 20, 2), order="C"))
    for invalid in (indices, records[0].flat_indices_b_a_z.astype(float)):
        with pytest.raises(ValueError, match="F-order"):
            replace(records[0], flat_indices_b_a_z=invalid)


def test_same_shape_transpose_is_detected_by_oracle_not_magic_guard():
    records, _, _ = fixture()
    original = records[0].aggregate_inputs
    transposed = replace(original, consumption=original.consumption.transpose(1, 0, 2))
    result = adapter.evaluate_corrected_household_aggregates(transposed)
    assert result.Ct.mass_form != pytest.approx(oracle(original)["ct"])
    assert result.Ct.mass_form == pytest.approx(oracle(transposed)["ct"])


@pytest.mark.parametrize("field,value", [("consumption", np.ones((20, 20, 1))),
    ("probability_mass", np.full((20, 20, 2), np.nan)), ("density", np.full((20, 20, 2), np.inf)),
    ("density", np.zeros((20, 20, 2)))])
def test_existing_adapter_rejects_shape_nonfinite_and_pg_mismatch(field, value):
    records, _, _ = fixture()
    with pytest.raises(ValueError):
        replace(records[0].aggregate_inputs, **{field: value})


def test_synthetic_mass_and_grid_domains_are_not_silently_repaired():
    records, _, _ = fixture()
    inputs = records[0].aggregate_inputs
    for mass in (-inputs.probability_mass, 2*inputs.probability_mass):
        altered = replace(inputs, probability_mass=mass, density=mass/inputs.omega)
        with pytest.raises(ValueError, match="synthetic mass"):
            replace(records[0], aggregate_inputs=altered)
    with pytest.raises(ValueError, match="grid"):
        replace(records[0], aggregate_inputs=replace(inputs, z_grid=np.array([.8, 1.4])))


@pytest.mark.parametrize("case", ["duplicate", "missing", "reordered", "wrong_stage", "duplicate_source"])
def test_batch_rejects_province_completeness_order_stage_and_source_identity(case):
    records, kwargs, _ = fixture()
    if case == "duplicate": records = [records[0], records[0]]
    if case == "missing": records = records[:1]
    if case == "reordered": records.reverse()
    if case == "wrong_stage": records[1] = replace(records[1], iteration=2)
    if case == "duplicate_source": records[1] = replace(records[1], source_id=records[0].source_id)
    with pytest.raises(ValueError):
        bridge.build_synthetic_household_batch(records, province_order=kwargs["province_order"], iteration=1)


@pytest.mark.parametrize("case", ["missing", "order", "source", "iteration", "source_id"])
def test_callback_rejects_inconsistent_entering_identity(case):
    records, kwargs, _ = fixture()
    states = [dict(s) for s in kwargs["entering_states"]]
    if case == "missing": states.pop()
    if case == "order": states.reverse()
    if case == "source": states[0]["source_kind"] = "REAL"
    if case == "iteration": states[0]["synthetic_iteration"] = 2
    if case == "source_id": states[0]["synthetic_source_id"] = "other"
    callback = bridge.make_synthetic_household_callback(records, province_order=kwargs["province_order"], iteration=1)
    with pytest.raises(ValueError):
        callback(tuple(states), 1)


def test_callback_is_one_use_and_rejects_request_stage():
    records, kwargs, _ = fixture()
    callback = bridge.make_synthetic_household_callback(records, province_order=kwargs["province_order"], iteration=1)
    with pytest.raises(ValueError): callback(kwargs["entering_states"], 2)
    callback(kwargs["entering_states"], 1)
    with pytest.raises(ValueError, match="already"):
        callback(kwargs["entering_states"], 1)


@pytest.mark.parametrize("field,value", [("household_lt", [-1., 1.]), ("ct", [0., 1.]),
    ("at", [-1., 1.]), ("bt", [1.]), ("converged", (1, 1))])
def test_existing_batch_rejects_invalid_vectors_and_flags(field, value):
    records, kwargs, _ = fixture()
    batch = bridge.build_synthetic_household_batch(records, province_order=kwargs["province_order"], iteration=1)
    with pytest.raises(ValueError): replace(batch, **{field: value})


def test_existing_frozen_rejects_invalid_flag_and_statistic():
    for kw in (dict(converged=1), dict(convergence_statistic=float("nan"))):
        data = dict(Ct=1., Lt=.5, At=1., Bt=0., AtTax=0., converged=False, convergence_statistic=0.)
        data.update(kw)
        with pytest.raises(ValueError): FrozenHouseholdOutputs(**data)


def test_migration_and_firm_reject_errors_without_guard_changes():
    records, kwargs, _ = fixture()
    bad = dict(kwargs, migration_wedge_destination_origin=np.full((2, 2), 2.))
    with pytest.raises(ValueError, match="power base"):
        bridge.run_synthetic_bridge_once(records, **bad)
    states = [dict(s) for s in kwargs["entering_states"]]
    states[0]["alpha"] = 2.
    with pytest.raises(ValueError, match="alpha"):
        bridge.run_synthetic_bridge_once(records, **dict(kwargs, entering_states=tuple(states)))
    with pytest.raises(ValueError, match="shape"):
        bridge.run_synthetic_bridge_once(records, **dict(kwargs, phi_destination_origin=np.ones((3, 3))))


def test_no_science_or_data_entry_during_synthetic_chain(monkeypatch):
    import ch5_two_asset_hank.hjb as hjb
    import ch5_two_asset_hank.kfe as kfe
    from ch5_two_asset_hank.multi_province import annual, stationary_runtime, steady_state
    blocked_calls = []
    def forbidden(*args, **kwargs):
        blocked_calls.append("blocked science/data/controller/normalized entry")
        raise AssertionError("forbidden science/data/controller/normalized entry")
    for module, name in ((hjb, "solve_hjb"), (kfe, "solve_stationary_kfe"),
                         (stationary_runtime, "run_online_stationary"), (steady_state, "run_manual_steady_state"),
                         (one_turn, "run_origin_preserving_normalized_one_turn"),
                         (one_turn, "reconstruct_origin_preserving_normalized_migration_labor"),
                         (annual, "load_primary_annual_input"), (np, "load")):
        monkeypatch.setattr(module, name, forbidden)
    records, kwargs, _ = fixture()
    previous_profile = sys.getprofile()
    def guard(frame, event, arg):
        if event == "call":
            module = frame.f_globals.get("__name__", "")
            name = frame.f_code.co_name
            if module.startswith("ch5_two_asset_hank") and (name.startswith("solve_") or module.startswith("ch5_two_asset_hank.corrected_diagnostic")):
                blocked_calls.append(f"{module}.{name}")
                raise AssertionError(f"forbidden scientific call: {module}.{name}")
    sys.setprofile(guard)
    try:
        bridge.run_synthetic_bridge_once(records, **kwargs)
    finally:
        sys.setprofile(previous_profile)
    assert blocked_calls == []
    print("PROTECTED_ENTRY_GUARD_RECEIPT="+json.dumps(dict(observed_protected_entry_calls=len(blocked_calls),
        scope="one synthetic chain with profile and entry sentinels; not a global security boundary")))


def test_module_origins_belong_to_exact_candidate_view():
    import importlib.metadata
    root = Path(os.environ["CH5_V001_CANDIDATE_VIEW"]).resolve()
    origins = {}
    for name, module in sorted(sys.modules.items()):
        if name.startswith("ch5_two_asset_hank") and getattr(module, "__file__", None):
            path = Path(module.__file__).resolve()
            assert path.is_relative_to(root), (name, str(path))
            origins[name] = str(path)
    assert Path(__file__).resolve().is_relative_to(root)
    print("CANDIDATE_MODULE_ORIGINS="+json.dumps(origins, sort_keys=True))
    print("RUNTIME_DEPENDENCIES="+json.dumps(dict(python=sys.version, executable=sys.executable,
        numpy=np.__version__, scipy=importlib.metadata.version("scipy"), pytest=pytest.__version__), sort_keys=True))
