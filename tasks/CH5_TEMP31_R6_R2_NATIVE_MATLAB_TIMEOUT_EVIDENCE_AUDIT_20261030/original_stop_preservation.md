# Original stop and byte protection

R6 STOP__R6_MATLAB_RUNTIME_UNAVAILABLE and R6-R1 STOP__R6_R1_NATIVE_MATLAB_GATE_FAILED remain unchanged. The current auditor independently recomputed actual bytes, SHA256 and Git Blob; it did not reuse old PASS declarations.

R6: declared20; VERIFIED19; OUT_OF_SCOPE1; missing/inaccessible0; mismatch0.
R6-R1: declared26; VERIFIED25; OUT_OF_SCOPE1; missing/inaccessible0; mismatch0.
The excluded external paths are the original R6 .m recipe and R6-R1 Python comparator. Neither is among the two external R6-R1 source files explicitly permitted by the R2 contract. They were not opened, treated as missing, or given a fabricated hash. Full scope authentication remains REVIEW_PENDING_IO.

Inside the exact old task directories, manifest-selected files were hash-only unless content reading was separately permitted. Controller/recipe, native and Job receipts, old results and exact raw logs provided the necessary timeout evidence. Forty-six unique permitted originals were rechecked unchanged at the end. No old write, move, rename, delete, cleanup or full unrelated historical audit occurred.
