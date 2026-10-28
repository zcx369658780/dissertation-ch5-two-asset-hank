# Code diff and isolated callpath

Fixed source: 5e4ec0ae4c310b8071b6aef68642fd0ffd862478, tree e636e09a2542deb29f386a26f5456e2b517f7911. Actual candidate diff contains three new code files plus this R4 task's evidence. Existing code files have no diff.

## New code

- src/ch5_two_asset_hank/multi_province/temp31_worksite_tax.py: Temp31LaborInputs line 44; destination-tax kernel line 87; source-like function line 106; normalized function line 115; single-class wage contract line 143; net-wage adapter line 170; conditional fiscal diagnostic line 199.
- validators/multi_province/temp31_worksite_tax_isolated.py: explicit legacy/candidate selection, direct safe-file loading and standalone unittest execution. Does not import the package initializer, suite configuration or production runner.
- tests/test_temp31_worksite_tax_isolated.py: 12 explicit two-province contracts, including unchanged history, two independent axis permutations, unequal taxes/wages/wedges, elasticity, zero limits, conservation, invalid inputs, net-wage and double-tax injection.

The actual change in the isolated kernel is:

```python
base = (inputs.old_firm_wage_by_destination[destination]
        * (1 - inputs.tax_by_destination[destination]
           - inputs.migration_wedge_destination_origin[destination][origin])
        / inputs.phi_destination_origin[destination][origin])
```

Historical migration_labor.py lines 98-133 and 311-382 are retained exactly, including `tax_by_origin[origin]` at lines 112 and 332. Their old behavior remains reproducible; it is not designated the correct TEMP31 tax mechanism. The new module has no import of historical one_turn, household initialization, shared contracts or HJB/KFE.

Validator -> direct test file -> direct historical migration/wage algebra and new pure TEMP31 module. No production composition calls the new module. The complete historical one_turn/stationary/steady-state/annual files are byte-identical; publication diff checks additionally confine changes to three new code paths and this R4 task directory.

The wage adapter creates `single_class` once at line 186, then passes it as both initialization and HJB data at line 187. This proves equality of the isolated proposed data contract only. It does not prove that current production initialization/HouseholdInputs consume that data; those steps are deliberately unwired and NOT_EXECUTED.

Rollback for this unmerged candidate is simply not adopting the three new files. No cleanup/deletion/reset is performed by this task. Subsequent production wiring, real HA integration, unit reconciliation and fiscal adoption require new Owner authority.
