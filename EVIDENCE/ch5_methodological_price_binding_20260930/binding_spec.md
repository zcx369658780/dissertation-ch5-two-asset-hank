# Methodological price binding extension specification

Date: 2026-09-30. Status: SPEC_REVIEW_PENDING__ZERO_SCIENCE.
Authority: owner_adoption.md and the limited accepted EVIDENCE/ch5_dual_consumer_integration_preparation_20260930/integration_packet.md.

## Exact implementation scope after spec acceptance

Only edit src/ch5_two_asset_hank/corrected_diagnostic/lagged_observed_gdp_wedge.py and create tests/test_ch5_methodological_price_binding.py. Preserve the existing old helper test file, all solver/validator/integration source, data/adapter, package imports, calibration, manuscripts, AGENTS and protected reports. Prechange helper bytes are saved as prior_helper.py.txt. No helper formula, amplitude, numerical validation or output axes changes.

Extend ProvenanceBinding with one backward-compatible optional field at the end: `price_attribution_sha256: str | None = None`. This identifies the separately reviewed attribution/authority document containing Owner adoption and official evidence identities. `source_sha256` identifies a combined source manifest binding GDP and population captures, audit, target/observation years and attribution document hash. The planned manifest is source_binding_manifest.json; its hash is computed from saved bytes, not reconstructed JSON. Hash syntax is structural validation, not authentication; a future source adapter must compare both hashes to separately pinned accepted identities before constructing observed bindings. No production activation or loader is provided by this extension.

The new observed route must use exactly `price_basis='current_price_methodologically_attributed'`, `price_verified=False`, `price_base_year=None`, and a built-in string attribution SHA256 of exactly 64 hexadecimal characters. It is an explicit Owner-adopted methodological attribution, never relabelled synthetic or directly verified.

Existing synthetic route continues to require synthetic_fixture / False / no base year and must have no attribution hash. Existing observed direct current_price and constant_price routes continue to require price_verified=True, their existing base-year rules, and no methodological attribution hash. Reject ambiguous combinations, method route with True, invalid hash types including bool/custom string subclasses, missing attribution, method route with base year, and attribution on unrelated routes. Existing enum/type and numerical failures remain intact. Immutable output binding carries the new field without losing metadata.

## Meaning of flags

`price_verified` in the helper continues to denote a directly verified price binding. Methodological acceptance is represented by the distinct price_basis plus reviewed attribution identity. No accepted old receipt/adapter is edited or silently set True. The new combined manifest reports evidence_use_adopted=True but direct_price_verified=False/model_activation=False. This task does not build an actual observed matrix; it only makes the accepted evidence category representable in inactive helper engineering.

## Exact verification surface and budget

Use only invented in-memory GDP/population fixtures, with conspicuously hypothetical observed metadata. Direct-load the exact standard-library helper without importing the HANK package or any scientific module. New test runner may direct-load the existing old test module and include its 14 tests as backward-compatibility verification because the helper has now changed; this is not an unchanged optional retest. Include new cases for method-route direction/immutability/metadata retention and the invalid combinations above; all data values and provenance hashes in formula tests are invented fixtures.

One initial invocation: bundled python -B tests/test_ch5_methodological_price_binding.py. Up to two repair invocations only after concrete scoped source/test fixes. No pytest collection, dependencies, observed panel reads, adapter readback repeat, preflight, wrapper, runner, scientific imports/calls or actual provincial coefficients. A failed initial test consumes one invocation. Historical two helper tests and one adapter test remain consumed and are not reset. Scientific budget exactly zero.

Independent code review is required after tests and hash readback. The change remains inactive and unreferenced by integration code. Then prepare a distinct annual two-consumer seam task under continuing Owner authority if no substantive choice is pending. Real binding and any future model execution remain separate, explicit gates.
