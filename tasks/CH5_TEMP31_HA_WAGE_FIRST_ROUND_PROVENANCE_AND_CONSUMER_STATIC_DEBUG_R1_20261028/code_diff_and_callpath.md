# New-only diff and callpath

Fixed parent: 92ec73bc4fabfdf92a9f34c3715ebbdd4fb51f27. Candidate changes only add these paths and this task's evidence:

- src/ch5_two_asset_hank/multi_province/temp31_ha_wage_debug.py: complete synthetic witness class line 56; independent wage recomputation line 92; round record line 123; diagnostic blocking exception line 140; provenance gate line 161; resource identity probe line 198.
- validators/multi_province/temp31_ha_wage_debug_isolated.py: two explicitly selected standalone test groups, no production initialization/runner import.
- tests/test_temp31_ha_wage_debug_isolated.py: 8 provenance tests and 9 algebra/preservation tests.

New-only source is directly reviewable in the fixed candidate; no summary substitutes for the actual three code files. No existing function or file is edited. In particular, R4 temp31_worksite_tax.py retains Blob 90667ddc00c72b9290e91481af4835c808ecfccb, its tests/validator and all historical source files retain baseline bytes, and R3/R4 branch tips/receipts stay intact.

Callpath: synthetic calculation inputs -> independent wage formula -> explicit round record -> provenance/timing/context/order/observed-value guard -> unchanged R4 pure-data adapter -> common proposed wage views -> illustrative resource probe. The guard precedes R4 adaptation, so a default cannot become net solely by supplying R4's existing semantic label. The resource probe revalidates those pure data; it never calls an actual initializer, HJB boundary or policy function.

The new module's only project import is the unchanged R4 data module. There is no production import of the new module; production/annual/Owner-A/runtime_cache/HA source is unchanged. The formal initialization/HJB/policy bridge remains a design with explicit gaps, not deployed behavior. Rollback means not adopting these new files; no deletion/reset/cleanup is performed.
