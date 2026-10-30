# Signed source-density reallocation

All indices are zero based. Grid is (b,a,z)=(20,20,2), Fortran state index=b_index+20*a_index+400*z_index; db=7/19, da=10/19. No scientific source or production entry changed.

PURE_ARCHIVE_ALGEBRA using original signed g*db*da; no clipping or normalization changes.

| partition | mass change | contribution delta At | contribution delta Bt |
|---|---|---|---|
| b_lower | -0.0524208709802174 | -0.159351171182865 | 0.104841741960435 |
| b_interior | -0.386880128576719 | -1.49559391475474 | 0.586553735908614 |
| b_upper | 0.439300999556936 | 3.83901771564755 | 2.19650499778468 |
| a_lower | -0.0536648086557923 | 0 | -0.126719145238245 |
| a_interior | 0.0536648086557922 | 2.18407262970994 | 3.01461962089197 |
| a_upper | 1.90751273159572e-18 | 1.90751273159572e-17 | 7.0322278332913e-18 |
| z0 | -0.0366801044344759 | 0.814032160994735 | 2.22855679936592 |
| z1 | 0.0366801044344758 | 1.37004046871521 | 0.659343676287811 |
| high_b_last4 | 0.588533361318097 | 5.0472592661919 | 2.82899297052175 |

The b partition adds to near-zero signed total mass change. b upper contributes +3.839017715647547 to delta At, offset by lower/interior b contributions; its delta Bt contribution is +2.196504997784682. High-b and a/b/z masks overlap and must not be added across partition schemes.

20-bin a/b marginals, two-bin z marginals and their differences are public in numeric_crosschecks.json and evidence/density_reallocation_metrics.json. Top three positive/negative state contributions are reported for signed mass, At and Bt; full800 vectors remain LOCAL_ONLY.

SIGNED_SOURCE_OUTPUT_DISTANCE full800 half-L1=0.857277748681568; a marginal=0.550728916180609; b marginal=0.642386623404764. E04 contains15 tiny negative density cells and negative mass5.206431699190674e-21; E03 negative mass0. Strict stationarity is false for both, so these are not certified economic distribution TV distances.

STRICT_ECONOMIC_STATIONARITY_CERTIFIED=FALSE at both points. These are conditional original-source outputs, not certified economic steady states. Full MATLAB-Python parity NOT_CERTIFIED; full nonlinear Bellman residual NOT_EVALUATED.
