# MP4C Owner-A intended-calendar capital provenance audit

## Terminal

`MP4C_OWNER_A_CAPITAL_PROVENANCE_UNRESOLVED__RERUN_NOT_AUTHORIZED`

The Owner-A calendar semantic is accepted for this audit: annual year `Y` intends
rolling entry `Y-2008`, PLM vintage and calendar level row `Y-1999`.  The legacy
MATLAB `data_year=ii` route is historical rather than final calendar authority.
However, the intended all-year capital series is not source-proven, so no input
adapter correction or 8-worker rerun is authorized.

## Evidence

`load_GDPdata.m` actively reads `总资本存量`, then assigns it to
`mydata.CAP{4}`.  The alternative `R语言计算资本存量` read is commented out;
its comment says it originates in an R package, but it does not establish that it
is the scientifically intended annual HANK `Kt0/Kt/GovInv` initializer or provide
an active, reproducible construction chain.  `multi_prov_HANK_12sts.m` comments
that the model uses provincial annual capital from R `CHNCapitalStock`, yet the
active loader still selects `总资本存量`.  This discrepancy is precisely the
unresolved scientific choice; positive later values cannot authorize substitution.

Selecting calendar rows 10--24 from the active cache produces inadmissible complex
`log_pcap` in 2022/2023.  Neither `abs`, clipping, interpolation, manual repair,
nor mixing the two sheets is authorized.

## Boundaries

The prior batch is
`LEGACY_CONFLATED_WINDOW_AND_LEVEL_ROW_BATCH__ENGINEERING_CONVERGENCE_ONLY__NOT_FINAL_CALENDAR_YEAR_AUTHORITY`.
The corrected-2009 same-input parity anchor remains unchanged. No MATLAB, R,
Python stationary/household/HJB/KFE, comparator, shock, IRF, R5, or Results call
occurred. MP4D numerical work remains blocked.

## Required Owner decision

Provide a source-backed designation of the unique 2000--2023, 31-province capital
series (including units, scaling, year/province order, construction code and its
relation to the two workbook sheets), or a deterministic documented reconstruction
contract. Only then may a new bounded task authorize Owner-A input materialization
and the exactly-eight-worker first batch attempt.
