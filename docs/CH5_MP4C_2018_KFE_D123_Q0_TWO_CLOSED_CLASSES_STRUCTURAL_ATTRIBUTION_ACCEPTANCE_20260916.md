# CH5 MP4C 2018 KFE D1-D3 Q0 two-closed-class structural attribution acceptance

Date: 2026-09-16

## Reviewer verdict

`PASS__Q0_TWO_CLOSED_CLASSES_STRUCTURAL_ATTRIBUTION_ACCEPTED__EXACT_ZERO_ASSET_DRIFT_SINKS_CONFIRMED__V1_POLICY_REMAP_TOPOLOGY_DIAGNOSTIC_AUTHORIZED_NEXT`

Independent review accepts candidate `2723c475943f7e6a767a940a9a52bad7b9c25e6f` and the report `docs/CH5_MP4C_2018_KFE_D123_Q0_TWO_CLOSED_CLASSES_STRUCTURAL_ATTRIBUTION_REPORT.md` as bounded forensic evidence for the accepted Q0 only.

## Accepted structural facts

The two closed communicating classes are exactly the two productivity pairs at adjacent lower-a asset nodes:

- class A: flats `5,405`, asset node `(i_b,i_a)=(5,0)`, `(b,a)=(-0.1578947368421053,0.0)`;
- class B: flats `6,406`, asset node `(i_b,i_a)=(6,0)`, `(b,a)=(0.2105263157894739,0.0)`.

At all four recurrent states the selected corrected policy is the conjunction of:

- interior-liquid `Z` zero-drift switching;
- active `lower_a` state constraint;
- `zero_kink` transfer branch;
- accepted lower-a multiplier interval handling.

Persisted consumed drifts are exactly `g_b=0.0` and `g_a=0.0`; therefore there are no positive asset-transition rates from these states. The only positive outgoing rate is the two-way productivity transition `1/3`, which connects the two z states within each size-2 recurrent class.

The closure is therefore caused by exact zero consumed drift in both asset dimensions, not by a nonzero asset cycle, b-boundary behavior, graph tolerance, numerical pinning, or omitted exterior flow.

## Accepted basin topology

The reproduced exact-positive Q0 graph has 400 SCCs of size 2 and 759 condensation-DAG edges. Reachability partitions are accepted as:

- A-only: 6 SCC / 12 states;
- B-only: 280 SCC / 560 states;
- both-reachable: 114 SCC / 228 states;
- neither: 0.

The asset-grid reachability split is also accepted:

- at `a=0`, `i_b=0..5` are A-only and `i_b=6..19` are B-only;
- at `a>0`, `i_b=0..5` are both-reachable and `i_b=6..19` are B-only.

The first direct fork is SCC 21 at `(i_b,i_a)=(5,1)`.

These are deterministic graph-reachability facts for Q0, not absorption probabilities.

## Scientific interpretation boundary

This evidence establishes structural nonuniqueness of the invariant stationary space for the accepted Option-A V0 policy operator Q0. It does **not** establish economic multiple equilibria, corrected-HJB fixed-point multiplicity, nonlinear-HJB nonexistence, or a stationary economic equilibrium.

The recurrent sinks may be specific to the V0 policy map. The already accepted V1 is one direct HJB step and has not yet been remapped through the selector. Therefore the smallest scientifically informative next diagnostic is to construct exactly one V1 policy map and its conservative Q1, then compare recurrent-class topology with Q0 without performing another HJB solve or any stationary-mass solve.

## Next authorization

Reviewer authorizes a bounded **V1 policy-remap and Q1 topology diagnostic** only. No new economic law, selector law, grid, calibration, or KFE stationary solve is authorized.

Results eligibility remains `FALSE`; production remains unchanged.