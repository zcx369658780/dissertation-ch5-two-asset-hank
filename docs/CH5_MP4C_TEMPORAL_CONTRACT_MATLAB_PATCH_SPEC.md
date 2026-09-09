# Chapter 5 MP4C temporal-contract MATLAB minimal patch specification

Date: 2026-09-09
Status: specification only; protected MATLAB sources remain unchanged.

## Frozen contract

For `ii=1..15`, define `steady_year=2008+ii`, `level_row=ii+9`, and retain `data_MAT{ii}` as the PLM/cache slot. The PLM workbook and estimator remain unchanged and represent a rolling ten-year sample ending in `steady_year`. `Zt` retains its current formula and alpha but uses GDP/CAP/POP from `level_row` for the same steady year.

Contract version: `CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`.

## Minimal future source patch

1. In protected `multi_prov_HANK_12sts.m`, the current line 133 passes `data_MAT{ii}` and `data_year=ii`:

   ```matlab
   st = mpHANK_equilibrium_2000(param,grids,num,CHI,inits,data_MAT{ii}, 4, ii);
   ```

   Keep `data_MAT{ii}` unchanged and pass the explicit same-year level row:

   ```matlab
   level_row = ii + 9;
   st = mpHANK_equilibrium_2000(param,grids,num,CHI,inits,data_MAT{ii}, 4, level_row);
   ```

   Add assertions that `steady_year==2008+ii`, `level_row==steady_year-1999`, and the rolling PLM window is `steady_year-9:steady_year` with length 10.

2. In protected `load_GDPdata.m`, lines 112–139 build each `mydata2{ii}` from PLM sheet vintage `ii+9`. Within that same `ii` loop, replace the hard-coded level index `21` in the active `Zt_new` expression at line 135 with `level_row=ii+9`. Apply the same index to the diagnostic `Zt_old` expression at line 133 if retained. Do not change the active formula:

   ```matlab
   Zt_new = mydata.GDP{j}(level_row,col) ...
       * mydata.CAP{j}(level_row,col)^(-reg_alpha{j}) ...
       * mydata.POP{j}(level_row,col)^(reg_alpha{j}-1);
   ```

   Calendar 2020 then uses row 21 only when `ii=12`; no fixed-2020 branch or special case is permitted.

3. In protected `mpHANK_equilibrium_2000.m`, lines 27–43 already consume `data_year` consistently for CAP/POP/GDP and their log ratios. No equation change is required after the caller passes `ii+9`. Keep `IND_alpha` and `IND_Zt` from the selected `data_MAT{ii}` slot.

4. Before accepting any corrected cache or annual output, save and validate metadata containing the contract version, steady/calendar year, analysis index, level row/year, `data_MAT` slot, PLM vintage and rolling-window bounds, Zt row/year, source workbook hashes, PLM workbook hash, and output identity/version. Reject missing, unversioned/legacy, internally inconsistent, or hash-mismatched metadata. Do not delete or overwrite the old cache.

5. The known `ii=15`, industry-4 mismatch (`old cache alpha=0.967775174774325`; current verified PLM workbook vintage24 `alpha=1.0219847778591`) remains provenance evidence. A corrected build must read the current hash-bound PLM workbook and must not allow the old cache value to override it.

## Protected identities at specification time

| File | SHA-256 |
|---|---|
| `multi_prov_HANK_12sts.m` | `3C44449CFD4047B5C9E17E540AFEA2F50B4251150F8F74AB8CCEED26E15DEC97` |
| `load_GDPdata.m` | `DECA8AF3F22097550B8957FE848989E6342619CB9929A1C00076E020549366C5` |
| `mpHANK_equilibrium_2000.m` | `26EA44552DA33919F8CCD777C084E15ECA0EA9575FEE80A07F9E0056F3F97DE5` |

This specification does not authorize editing MATLAB, rebuilding caches, or running a steady state.
