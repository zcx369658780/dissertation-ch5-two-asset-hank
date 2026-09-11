"""Separately named C1 one-turn composition with contemporaneous public assets."""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

from . import one_turn as source
from .government_assets import ResidualGovernmentAssetBatch, residual_government_asset_levels
from .one_turn import OneTurnInputs, PreFrozenHouseholdOutputBatch


C1_UPDATE_ORDER: tuple[str, ...] = (
    "pre_frozen_household_outputs",
    "source_faithful_migration_labor",
    "at_only_private_productive_capital",
    "c1_residual_public_asset_level",
    "firm",
    "household_composite_wage",
    "taylor_rb",
    "fiscal_diagnostics",
)


@dataclass(frozen=True)
class C1ResidualPublicAssetOneTurnResult:
    """Auditable C1 composition; no outer convergence action is included."""

    province_order: tuple[str, ...]
    household_outputs: PreFrozenHouseholdOutputBatch
    migration: object
    capital: object
    c1_accounting: ResidualGovernmentAssetBatch
    firms: tuple[object, ...]
    household_composite_wage: tuple[float, ...]
    monetary: object
    fiscal: object
    source_update_order: tuple[str, ...] = C1_UPDATE_ORDER

    def __post_init__(self) -> None:
        n = len(self.province_order)
        if (
            len(self.firms) != n
            or len(self.household_composite_wage) != n
            or self.migration.lt_supply.shape != (n,)
            or self.capital.kt_supply.shape != (n,)
            or self.c1_accounting.province_order != self.province_order
            or len(self.fiscal.Govinc) != n
        ):
            raise ValueError("C1 one-turn components do not share one province axis")
        if self.source_update_order != C1_UPDATE_ORDER:
            raise ValueError("C1 update order is immutable")
        if not all(isfinite(float(value)) for value in self.household_composite_wage):
            raise ValueError("household composite wages must be finite")


def run_c1_residual_public_asset_one_turn(
    inputs: OneTurnInputs,
) -> C1ResidualPublicAssetOneTurnResult:
    """Compose one source-faithful turn with C1 inserted before firm evaluation."""

    household = inputs.household_outputs
    provinces = inputs.old_provinces
    migration = source.reconstruct_migration_labor(source.MigrationLaborInputs(
        consumption_by_origin=household.ct,
        population_by_origin=[province["N"] for province in provinces],
        old_firm_wage_by_destination=[province["wjt"] for province in provinces],
        tax_by_origin=[province["tau"] for province in provinces],
        phi_destination_origin=inputs.phi_destination_origin,
        migration_wedge_destination_origin=inputs.migration_wedge_destination_origin,
        gamma_c=inputs.params["ga"],
        phi_l=inputs.params["phi_l"],
    ))
    capital = source.allocate_productive_capital(source.CapitalAllocationInputs(
        illiquid_assets_at=household.at,
        population=[province["N"] for province in provinces],
        inter_province_ratio=[province["inter_prv_ratio"] for province in provinces],
        old_firm_return_ra=[province["ra"] for province in provinces],
    ))
    accounting = residual_government_asset_levels(
        Ktarget_MU=[province["Kt0"] for province in provinces],
        Kprivate_current_MU=capital.kt_supply,
        province_order=inputs.province_order,
    )
    firms = []
    for index, province in enumerate(provinces):
        firm_source = dict(province)
        firm_source["GovInv"] = float(accounting.GovInv_residual_MU[index])
        firm_source["AtTax"] = float(household.at_tax[index])
        firm_source["Lt_prev"] = float(household.household_lt[index])
        firm = source.evaluate_firm(
            firm_source,
            float(capital.kt_supply[index]),
            float(migration.lt_supply[index]),
            inputs.params,
        )
        expected = float(accounting.firm_K_accounting_MU[index])
        if abs(float(firm.Kt) - expected) > 1e-12 * max(1.0, abs(expected)):
            raise RuntimeError(f"{inputs.province_order[index]}: C1 firm-capital assertion failed")
        firms.append(firm)
    composite_wage = source.composite_household_wages(
        provinces,
        [firm.wjt for firm in firms],
        inputs.phi_destination_origin,
        inputs.migration_wedge_destination_origin,
        phi_l=inputs.params["phi_l"],
        alphal=inputs.params["alphal"],
    )
    monetary = source.taylor_assignment(
        istar=inputs.params["istar"], rho_pi=inputs.params["rho_pi"],
        totalpit=inputs.params["totalpit"], epsilon_pi=inputs.params["epsilon_pi"],
    )
    fiscal = source.national_fiscal_diagnostics(
        [firm.Govinc for firm in firms], household.bt, monetary.rb,
        [province["N"] for province in provinces],
    )
    return C1ResidualPublicAssetOneTurnResult(
        province_order=inputs.province_order,
        household_outputs=household,
        migration=migration,
        capital=capital,
        c1_accounting=accounting,
        firms=tuple(firms),
        household_composite_wage=tuple(composite_wage),
        monetary=monetary,
        fiscal=fiscal,
    )
