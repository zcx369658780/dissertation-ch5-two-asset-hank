# Immutable post-operator handoff

All Python references are at fixed SOURCE_COMMIT 56447829ce0e6c3c85552c53c351b26a2452a4bd and source_identity.json Blobs. No referenced scientific file was changed or executed except the standalone KFE core.

| stage | fixed Python location | mapping and limit |
|---|---|---|
| local net resources | temp31_netwage_policy.py137–158 | w_net*z*l+T+Rb*b; no extra tau/sigma |
| final transfer and asset drift | policy234–244; economics121–141 | consumption argument C-T yields mu_b=Rb*b+w_net*z*l-dh-cost-C+T; mu_a=Rah(a)*a+dh |
| iteration rates | policy261–270; HJB108–110 | separate signed iteration components; not handed to KFE |
| implicit HJB matrix | HJB111–115 | (1/delta+rho)I-G_iteration; never passed as KFE input |
| post rebuild | HJB117 | max(-mu_b,0)/db, max(mu_b,0)/db, max(-mu_a,0)/da, max(mu_a,0)/da from final selected policy |
| BB / AAH | operator19–45,55–56 | axis0 +/-1 and axis1 +/-I with F index; outward offdiagonal omitted, diagonal retains full rate |
| Bswitch and G | operator57–59 | kron(switch,I); G=BB+AAH+Bswitch |
| returned post | HJB118 | post separated from iteration operator |
| replay handoff | validator | authenticated actual archived post_G CSR; exact immutable hash; direct KFE input |

Frozen MATLAB262–264 gives s=(1-tau)*w*z*l+Rb*b+T-Cmin-dh-cost-C and mh=dh+Rah*a. TEMP31 uses previously approved net wage, so tax/sigma are already upstream; Cmin is not an explicit term in this fixed economics function. No unconditional full economic-equation equivalence is asserted without resolving the original parameter/value meaning. The excerpt alone cannot certify all original boundary/spdiags placements, switch construction and local policy choices. These remain BOUNDED/BLOCKED; modifying them is outside this task.

The current post axis code maps X=-min(s,0)/db, Z=max(s,0)/db and diagonal -(X+Z), with analogous mh coefficients. At an outward boundary it can retain diagonal loss while omitting outward neighbor. This mathematical observation does not authorize a correction or prove every historical cell's causal origin. No historical HJB/policy recomputation was performed.

Four real archived post matrices have nonzero absolute row-sum maxima and near-zero maximum signed row sums. Their residual is concentrated at the removed equation; observed diagnostics are not a complete cellwise provenance of row loss. MATLAB's iteration homecrit .01 is a different historical guard; no equivalent post-KFE hard gate was found in supplied excerpts/Owner decision. Do not infer violation of that iteration threshold from these post diagnostics.
