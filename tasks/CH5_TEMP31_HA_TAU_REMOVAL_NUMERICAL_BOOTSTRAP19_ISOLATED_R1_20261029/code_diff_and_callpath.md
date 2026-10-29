# Exact candidate scope and source derivation

Only six new code paths are added:

1. multi_province/temp31_ha_taxfree_bootstrap.py: numerical19/later-source records, explicit no-tax consumer type, context/order guards, source-derived root/initialization helpers.
2. temp31_netwage_hjb.py: authenticated HJB copy with boundary wage factor removed; corrected input/policy bindings and names only.
3. temp31_netwage_policy.py: authenticated local-policy copy with corrected economics, no-tax local input rebuild/provenance retention and net coefficient.
4. temp31_netwage_economics.py: authenticated economics copy with three wage factors removed and corrected input guards.
5. validators/multi_province/temp31_ha_taxfree_bootstrap_isolated.py.
6. tests/test_temp31_ha_taxfree_bootstrap_isolated.py.

All source paths above are relative to src/ch5_two_asset_hank except the explicit validator/tests. Exact code is present in the candidate; evidence/source_transformation_manifest.json records original Blobs, edits and final file hashes. source_identity.json records all twelve required original objects and successful bounded acquisition.

The new source callpath is net record -> new no-tax inputs -> source-derived initializer or corrected HJB -> corrected policy -> corrected labor/drift economics. The HJB operator import is unchanged. No production file imports or calls the new path; historical source, R4/R5 code/evidence and R3/R4/R5 branches remain intact.

The source sync requested exactly five initially missing fixed Blobs in one ordinary SSH git-upload-pack session:14,020 compressed bytes,47,172 source bytes,5 objects,about6 seconds; limits1MiB/60seconds, no retry. Native Git index-pack authenticated the received pack. No historical file was created/overwritten and no other source/history/data fetched. The initial generated receipt had an unused bytes_received counter left0; the public verified receipt explicitly corrects it to actual pack_bytes, records original receipt SHA and retains the original locally. No source/pack identity was changed by that metadata correction.

Rollback is not adopting these new files. No deletion, reset, cleanup, main/governance scientific update, model activation or integration occurs.
