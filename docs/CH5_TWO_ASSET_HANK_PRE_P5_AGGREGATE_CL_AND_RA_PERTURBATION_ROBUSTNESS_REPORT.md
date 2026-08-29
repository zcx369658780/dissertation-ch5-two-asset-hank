# CH5 Two-Asset HANK Pre-P5 Aggregate C/L and r_a Perturbation Robustness

## Supplementary classification

`PRE_P5_NATIVE_AGGREGATE_ROBUSTNESS_BLOCKED_SOURCE_OR_ENVIRONMENT`

Terminal authority blocker:

`BLOCKED_PRE_P5_AGGREGATE_ROBUSTNESS_MATLAB_NATIVE_INVOCATION_AUTHORITY`

The designated MATLAB tree does not contain one unique, auditable native invocation with an illiquid-return baseline of `0.040`. The source instead exposes multiple top-level entry routes, fifteen year/data configurations, a cache-versus-recompute branch, an explicit initial `rah=0.09`, and a subsequent endogenous cross-province update of `rah`. Under the task's pre-execution hard gate, all four scientific-run counts remain zero. No Python run was consumed merely to produce an incomplete cross-language table.

This report does not issue P5 acceptance.

## Live and source identity

- repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- fresh-fetched live/base `origin/main`: `08723b07b4f3e870c6619ad5c1f9fffacd1b1bb6`
- accepted Python baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`
- accepted P1-P4 evidence commit: `daa3e60ff97828ec80fb2e83bee863eb4aa632a4`
- isolated Git workspace: `D:\ProjectTemp\ch5-pre-p5-aggregate-robustness-repo-20260829`
- `git diff 7a2388a2ba89073e307f05a909570e8c40a4be13..08723b07b4f3e870c6619ad5c1f9fffacd1b1bb6 -- src tests`: empty

Python scientific/test continuity: PASS. No Python model, HJB, KFE, fixture or scientific harness was executed.

The required MATLAB production identities passed:

| File | Bytes | SHA-256 |
|---|---:|---|
| `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m` | 12227 | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` |
| `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK3_cost.m` | 691 | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` |
| `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK3_FOC.m` | 565 | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` |

## MATLAB caller audit

The only direct textual call to `HANK_2ASSETS_HJB` is:

`HANK_mp_1turn.m:15 -> HANK_2ASSETS_HJB(param, grids{i}, num, CHI, results_temp{i}, show_result)`.

That direct caller is not a unique native invocation configuration. Its observed caller graph is:

```text
main.m / main2.m / multi_prov_HANK.m
  -> multi_prov_HANK_12sts(ii, pp)
    -> mpHANK_equilibrium_2000(..., data_MAT{ii}, st_ind=4, data_year=ii)
      -> HANK_mp_1eq(...)
        -> HANK_mp_1turn(..., steady_state=1)
          -> HANK_2ASSETS_HJB(...)

mpHANK_shock_2000(...)
  -> HANK_mp_1turn(..., steady_state=1)
    -> HANK_2ASSETS_HJB(...)
```

Material caller identities:

| Caller/configuration file | Bytes | SHA-256 |
|---|---:|---|
| `main.m` | 21950 | `5C49CEAEDA9B43ED615E5DD376498D45F0E01D9A2F469C0FBB617C02110D5E12` |
| `main2.m` | 10342 | `E4B8E5BF748FB38616E70B7B1F931B99E3B59468A7A27D3ABB00D0573B7F83FB` |
| `multi_prov_HANK.m` | 1304 | `587FBA4ABA2DE88E2FD9B172379CEFA3E4AA144A32C8AD7FB26156618517E929` |
| `multi_prov_HANK_12sts.m` | 5531 | `3C44449CFD4047B5C9E17E540AFEA2F50B4251150F8F74AB8CCEED26E15DEC97` |
| `mpHANK_equilibrium_2000.m` | 4255 | `26EA44552DA33919F8CCD777C084E15ECA0EA9575FEE80A07F9E0056F3F97DE5` |
| `HANK_mp_1eq.m` | 3817 | `ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF` |
| `HANK_mp_1turn.m` | 3254 | `D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF` |

## Why native invocation authority is not unique

1. `main.m` and `main2.m` each call `multi_prov_HANK_12sts(i,0)` over `i=1..15`, corresponding to the 2009-2023 configurations. No year/index was designated by the task or a unique native caller.
2. `multi_prov_HANK.m` is another top-level entry using an externally supplied `nst`.
3. `multi_prov_HANK_12sts(ii,pp)` conditionally loads `Multi_Province_12sts_<year>.mat` if present; otherwise it reads external data and solves. Thus identical source invocation can select a cached state or a new solve, and neither exact cache artifact nor branch was frozen by the task.
4. The steady-state call depends on `data_MAT{ii}`, province data, `load_GDPdata`, `load_distdata`, 31 province states and iterative firm/government feedback. These inputs are not a single frozen household-call object.
5. `mpHANK_shock_2000` independently calls `HANK_mp_1turn`; it is a dynamic route and is forbidden for this task, but confirms that the direct caller is not uniquely steady-state-owned.

## Parameter and grid evidence

The explicit configuration in `multi_prov_HANK_12sts.m` is:

- `N_prov=31`;
- HJB controls: `num.maxit=100`, `num.crit=1e-7`, `num.Delta=1000`;
- adjustment costs: `CHI.chi0=0.1`, `CHI.chi1=2`, `CHI.a_bar=1e-6`;
- grid: liquid `I=20`, `b in [-2,5]`; illiquid `J=20`, `a in [0,10]`; productivity `Nz=2`, `z=[0.8,1.3]`;
- productivity generator: the configured `la_mat` constructed from the two-state `1/3` switching expression;
- preferences: `ga=2`, `phi_l=5`, `rho=0.05`;
- explicit initial returns: `init.rah=0.09`, `init.ra=0.09`, `init.rb=0.02`;
- other state inputs include province-specific wages, taxes, transfers, production data and migration costs.

### Illiquid-return mapping conflict

`HANK_2ASSETS_HJB.m:27` reads the household illiquid return as:

```matlab
rah = results.rah;
```

The only explicit native initialization found in the designated tree is:

```matlab
init.rah = 0.09;
```

No native `rah=0.040` assignment exists in the tree. Moreover, after the household call, `HANK_mp_1turn.m:40` updates the next-iteration value as a cross-province function of `results{i}.ra`, `inter_prv_ratio`, and the other provinces' `ra` values. Therefore `rah` is not a single exogenous scalar that can be changed from `0.040` to `0.041` while otherwise retaining the native invocation unchanged. Creating such a baseline would require an Owner-designated external configuration and a decision about whether the endogenous update is frozen, bypassed or retained. This task does not authorize that inference.

## Native MATLAB stationary and policy objects identified

Although no run was authorized, the household source defines the relevant objects audibly:

- backward generator `A`, forward stationary equation `A' * g = 0` with the native pin-row normalization;
- density-like stationary array `g`, normalized by `sum(g*dah*db)=1`;
- probability-cell weights `gg = g*db*dah`, stored as `results.g`;
- raw consumption policy `C` and raw labor policy `l` in the HJB scope;
- stored state contributions `results.C = C.*g*dah*db` and `results.l = zzz.*l.*g*dah*db`;
- native aggregates `Ct = sum(C.*g*dah*db,'all')` and `Lt = sum(zzz.*l.*g*dah*db,'all')`;
- assets `Aht = sum(aaah.*g*dah*db,'all')` and `Bt = sum(bbb.*g*dah*db,'all')`.

These formulas identify how a future authorized run should aggregate. They do not identify which of the multiple native configurations should be run.

## Python configuration status

The accepted R4 fixture/configuration and steady-state report were read. The authorized baseline/perturbed construction would have retained the accepted R4 grids, initialization, buffer protocol, HJB/KKT/generator/KFE tolerances and all inputs except `r_a: 0.040 -> 0.041`, with `C_hh=sum(g*c)` and `L_hh=sum(g*l)`.

No Python harness was created or executed because the cross-language task requires the MATLAB native-authority preflight to pass before the four-run budget is consumed.

## Scientific execution counts

| Run | Count | Status |
|---|---:|---|
| Python baseline `r_a=0.040` | 0 | not authorized after preflight blocker |
| Python perturbed `r_a=0.041` | 0 | not authorized after preflight blocker |
| MATLAB native baseline | 0 | blocked: no unique auditable `rah=0.040` invocation |
| MATLAB perturbed `rah=0.041` | 0 | blocked: baseline authority absent |

No HJB, KFE, stationary distribution, aggregate, MATLAB model, Python model or frozen fixture was evaluated.

## Requested compact table

| implementation | r_a | C_hh | L_hh |
|---|---:|---:|---:|
| MATLAB | 0.040 | `NOT_RUN_NATIVE_AUTHORITY_BLOCK` | `NOT_RUN_NATIVE_AUTHORITY_BLOCK` |
| Python | 0.040 | `NOT_RUN_PRECHECK_BLOCK` | `NOT_RUN_PRECHECK_BLOCK` |
| MATLAB | 0.041 | `NOT_RUN_NATIVE_AUTHORITY_BLOCK` | `NOT_RUN_NATIVE_AUTHORITY_BLOCK` |
| Python | 0.041 | `NOT_RUN_PRECHECK_BLOCK` | `NOT_RUN_PRECHECK_BLOCK` |

`Delta C_hh`, `Delta L_hh`, percentage changes, cross-language level differences and response differences are not defined because no scientific run was authorized. No value or tolerance is fabricated.

## Files read and written

Read: live task/rules; accepted P1-P4 and Owner parity reports; accepted Python R4 steady-state/configuration source; designated MATLAB HJB/helpers; all direct and top-level MATLAB caller/configuration files listed above.

Repository write: only this report. No external scientific harness or numerical output was created.

## Forbidden-operation check

- P1-P4 rerun: no
- Python baseline/perturbed run: no
- MATLAB baseline/perturbed run: no
- MATLAB or Python production source/test modified: no
- parameter, grid, productivity, initialization, equation, FOC, boundary/KKT, generator/KFE or tolerance changed: no
- missing native configuration inferred or fabricated: no
- P5 acceptance issued: no
- AR(1), transition, IRF, calibration extension or Results entered: no
- merge, rebase, reset or force-push: no

## Acceptance level and recommended next gate

P1-P4 numerical evidence remains complete and unchanged. The supplementary native robustness experiment is blocked before execution and therefore cannot support or oppose Owner acceptance numerically.

The next gate must be an Owner/reviewer task that designates one exact MATLAB native baseline package, including year/data index, cache-versus-recompute choice and file identity, all external data/state identities, province scope, the exact `rah=0.040` injection point, and whether the endogenous cross-province `rah` update remains active. Only after that authority exists may a new bounded four-run robustness task be issued. P5 remains pending.
