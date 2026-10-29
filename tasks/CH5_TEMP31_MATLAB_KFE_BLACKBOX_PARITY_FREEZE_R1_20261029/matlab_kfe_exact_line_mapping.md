# Frozen MATLAB excerpt to fixed Python mapping

MATLAB provenance is SOURCE_EXCERPT_ONLY. The supplied HJB file identity is 12227 bytes / SHA256 049136b769560040bc678f828f5d3ec5338ddcaa2090d6bed4e40732f56c3eae; ZIP SHA256 ceb94ccf34d2d218722b81e5111a8f4c530571a9f886bd4afe0610a00321f755. No local original-byte authentication or MATLAB runtime execution is claimed.

Only frozen line ranges are available; individual MATLAB line numbers inside them are not inferred.

| MATLAB frozen range / step | core Python lines | export Python lines | conclusion |
|---|---|---|---|
| 262–264, final dh, s, mh | external to KFE | external to KFE | fixed handoff examined; full original parity BOUNDED |
| 265–333, rebuild post BB/AAH/Bswitch/A | external to KFE | external to KFE | post source preserved; full spdiags parity BLOCKED |
| 334–344, M=I*J*Nz | 32–36 | 654–658 | shape product and input checks; valid M800 proven |
| 334–344, AT=A' | 37 | 659 | transpose exact in all four actual archives |
| 334–344, floor(.37*M), one-based | 25–28,38 | 647–650,660 | 296 in MATLAB / 295 Python |
| 334–344, replace row by unit row | 39 | 661 | dense independent construction exact |
| 334–344, vec(iFix)=.007 | 40 | 662 | complete rhs exact |
| 334–344, AT\vec | 41–42 | 663–664 | one sparse solve per point; finite; no alternate solver |
| 334–344, sum(g)*db*dah | 43–44 | 665–666 | same weight and normalization factor |
| 334–344, divide by sum and reshape | 45,47 | 667,669 | density vector / F reshape exact |
| diagnostic only, pinned raw residual | 46 | 668 | observable; no added hard stationarity gate inside source |
| 345–354, integrals Ct/Lt/Bt/Aht | external to KFE | external to KFE | new validator checks At/Bt and 20-bin marginals, not full Ct/Lt source parity |

For shape (I,J,Nz), F flatten index i+I*j+I*J*nz puts b fastest, then a, then z. For Nz2 this corresponds to the excerpt's first/second I*J blocks. Density integration is db*da. Row replacement acts after transposition, not on the input G. Original G remains exact by CSR hash.

Class core10–23/export632–645, index helper core25–28/export647–650, solve core30–47/export652–669 have identical ASTs ignoring locations; AST hashes are in evidence/core_export_static_AST_parity.json. The export module was not imported or solved again. KFE result diagnostics and input validity checks are Python additions, not a claim of byte-identical MATLAB language implementation. Source-step equivalence is PROVEN for the valid archived800-state inputs against the frozen excerpt; all-model equivalence is not established.
