# Chapter 5 MP4C-2018 D123 checkpoint 6 to checkpoint 10 bounded nonlinear continuation report

Date: 2026-09-20

Task: `CH5_MP4C_2018_KFE_D123_CHECKPOINT6_TO_CHECKPOINT10_BOUNDED_NONLINEAR_CONTINUATION_20260919`

## Terminal verdict

`COMPLETE_CHECKPOINT10_NONCONVERGED__TERMINAL_GATE_NOT_RUN`

The bounded trajectory reached a complete checkpoint 10. The frozen primary
convergence law failed at checkpoints 7, 8, 9 and 10. No exact recurrence and
no authorized approximate period-2/3 recurrence was detected. Execution
stopped at the checkpoint-10 ceiling. Terminal topology and KFE were not run.
Results eligibility is `FALSE`.

## Git and execution binding

- fresh live-main baseline: `c852473a3123513e26493db1fef75a65a8680b0d`
- task branch: `codex/ch5-mp4c-2018-kfe-d123-checkpoint6-to-checkpoint10-bounded-nonlinear-continuation-20260919`
- accepted checkpoint-6 identity: `B26177C216DA6902226BD93E802A2B1FE0E794B29BE14EA1A1BCBFFD8F8691A1`
- implementation commit before runtime: `b97f9b4`
- focused engineering gate: `83 passed`
- focused JUnit SHA-256: `674A88AC413AA34F51FC6232F75BBEC8A5CE6DFB8D6844E3B7939361C6822A73`
- `py_compile`: PASS
- `git diff --check`: PASS
- scientific code hash before/after execution: exact match

The execution bound the accepted checkpoint history from V0 through V6 and
verified the accepted 1,633-entry checkpoint-6 evidence manifest before the
first update. V6/P6/u6/Q6 were reused exactly. The V6 policy map and Q6 were
not rerun or regenerated.

## Direct-solve receipts

All solves used the frozen `scipy.sparse.linalg.spsolve` equation with
`Delta=1000`; all normwise backward errors are below `1e-12`.

| update | residual infinity norm | normwise backward error | status |
|---|---:|---:|---|
| V6 to V7 | `1.2004286453759505e-14` | `2.0086287473344903e-16` | PASS |
| V7 to V8 | `1.124100812432971e-14` | `2.474008165761441e-16` | PASS |
| V8 to V9 | `1.0005885009434223e-14` | `2.1980596450830867e-16` | PASS |
| V9 to V10 | `9.811595980124821e-15` | `2.1551480423314607e-16` | PASS |

## Complete checkpoint metrics

| checkpoint | B_n | D_n | primary | exact cycle | approximate cycle | disposition |
|---|---:|---:|---|---|---|---|
| 7 | `0.000983868092531745` | `0.0027865782347942236` | FAIL | none | none | continue |
| 8 | `0.00016252618227152738` | `0.0006617669262674042` | FAIL | none | none | continue |
| 9 | `8.986962138773924e-06` | `0.00011033293848816683` | FAIL | none | none | continue |
| 10 | `3.874510913493001e-08` | `5.8692895192891115e-06` | FAIL | none | none | bounded stop |

Primary convergence was evaluated first at every checkpoint using the
inclusive thresholds `B_n<=1e-8` and `D_n<=1e-7`. Exact-cycle evaluation came
next. Approximate period-2 and period-3 checks then used the full accepted
history and the adopted norm `||vec_F(V_j-V_(j-k))||inf`. Neither approximate
rule passed at tolerance `1e-8`. No trend-based or longer-period rule was
introduced.

### Identities

| checkpoint | V SHA-256 | P identity | u SHA-256 | Q artifact SHA-256 | checkpoint identity |
|---|---|---|---|---|---|
| 7 | `2D15DBC6839F3653D3497946758735BD4D8C8F4ED8DF8B487C5BDB3B211F9A48` | `D889536CAC650233121B5131E6863C88DF0F09152846157796DD780762A7CB2C` | `98FC4D8AA45E14C1CA1327E18C97A65441BFF180F0EC483D651CFBE817A9DBAD` | `0E7546D526A9327779B0CB1C4B3A92EE97E3D1D1C134C9005BB6CBF474B255B5` | `D8C18DFF8EFB21D16F01B7A51E0B2EEAD81976B0221097C800E86C8820C718B2` |
| 8 | `9D0C136B68269C305C64C4CAE82B8548DB4B0D224611B666C1AF6D4C54841A7A` | `6A7309DA1A27A78A8D229B3E8A45A407FECA004E1557EC20AAB69BC090B844E3` | `9994F568F7732D856C92ED8D82AA4EA6B1F6BCF34CDE124841D78512FDC8CF6E` | `341A725A9D027626893B68811BF6E901E9722DBA0D28B23D25CFB4F8997C1CA5` | `692BB36DE8B44FD0994AA8B933E4B0FC11930860CE84F0F6FDC9BBFD49CE23F2` |
| 9 | `EC5B3BA1BA65559FE468A3B9821D4D13356D8966631AC338BE08E37863F6732D` | `89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3` | `670E0130C7E2123CF6F0FEFC20252FE5910BFB5BB3FCD53E37889098E089AC0C` | `070D8FAE3FBC24ACF29AB339B24AAFBEEF4A2A05CFE2F3CEAE5282A98827DD60` | `C36F00DF696D4C16B8FCE581D47B2AC396413996911F264543E3325FFFA63653` |
| 10 | `AE1610BA320F57AF73EE3C5411C298BF00610606B13B5185F2CD65BF1736FB24` | `89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3` | `215BEC4AABBC337147D73A227751CD6A89CC483E3CA056470A2AEF161AA41F38` | `917479763C4690FEAB358098D7F1CE2EBB4DD7C4939A7060156E7A4FCDEE59BD` | `4FC2855AB4102AEAE8B173D0EBBBF40FCD334583A039BE4AE65C8DE2B1145C8D` |

All four D2 receipts are PASS. Relative to the immediately preceding
checkpoint, selected-policy identity changes were 800, 15, 2 and 0. Q
infinity-norm differences were `9.917810526065546`, `3.3272775154040026`,
`0.6135230787837366` and `0.035433358627171924`. Selected interior-a
switching-policy counts were 32, 30, 29 and 29. Selected liquid-Z and joint
switching counts were zero at every checkpoint. These are diagnostics only.

## Exact scientific ledger

| item | count |
|---|---:|
| accepted V0 through V6 loads | `1` each |
| accepted P2/P3/P6 loads | `1` each |
| accepted u2/u3/u6 loads | `1` each |
| accepted Q1/Q2/Q3/Q6 loads | `1` each |
| direct HJB solves / HJB updates | `4 / 4` |
| fresh corrected policy maps | `4` |
| selector evaluations | `3200` |
| scalar roots, total | `1078` |
| liquid-Z roots | `54` |
| interior-a switching roots | `4` |
| joint-switching roots | `0` |
| D2/Q assemblies | `4` |
| complete checkpoint evaluations | `4` |
| V6 policy-map reruns / Q6 reruns | `0 / 0` |
| scientific retries | `0` |
| solver substitutions | `0` |
| damping/relaxation/adaptive-Delta/continuation | `0` |
| parameter continuation/clipping/artificial diffusion | `0` |
| graph/SCC and terminal topology gates | `0` |
| KFE/SVD/eigen/nullspace/Q.T@p | `0` |
| MATLAB/production/outer/firm/GE/annual/shock/IRF/Results | `0` |

The four-map, 3,200-selector, four-Q, four-evaluation and four-update ceilings
were reached but not exceeded.

## Evidence closure

The fresh no-overwrite evidence root is:

`reports/ch5_mp4c_2018_kfe_d123_checkpoint6_to_checkpoint10_bounded_nonlinear_continuation_20260919_run001/`

Its sealed manifest has SHA-256
`1959B54DB2EC27BA1F12493F71E9E8AAD5F5442D20099D77EC84C0C2AE902EAC`,
3,249 entries and 52,183,186 bytes. Independent readback found zero missing or
mismatched entries.

No scientific code changed after the execution freeze. No newly exposed
scientific issue was repaired. No terminal KFE or downstream computation was
attempted. CURRENT files and main were not modified, and no successor task was
published. This candidate requires independent Reviewer inspection before any
further continuation or terminal gate.
