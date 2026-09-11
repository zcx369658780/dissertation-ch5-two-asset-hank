# Controller source and timing map

This is a read-only source reconstruction. It does not execute the controller.

1. A completed province batch reaches the firm before controller diagnostics. Firm accounting is `Kt=Kt_supply+GovInv`; the firm computes raw `ra0`, clips it to `[ramin,ramax]`, and stores only clipped `ra` in the shared state (`firm.py:61,110-125`; protected `HANK_firm.m:14,54-65`).
2. `_post_turn_states` copies those firm outputs into the post-turn state before `_diagnostics` and `_adapt` (`steady_state.py:146-168`). Consequently the controller sees the completed current-turn firm result.
3. The diagnostic is `nk_gap_i=abs(KNratio_i/tKNratio_i-1)`, and the gate is exactly `max(abs(KNratio/tKNratio-1))<0.1`. Adaptation opens only when that cross-province maximum condition holds and `steady_state` is true (`steady_state.py:172-201`; protected `HANK_mp_1eq.m:47`). This gate is separate from the final convergence tolerance.
4. Inside an open gate, the output discrepancy is checked first. If `abs(Yt/Yt0-1)>0.01`, `Zt` is recomputed before GovInv is inspected (`steady_state.py:209-218`; protected `HANK_mp_1eq.m:49-51`). Thus Zt and GovInv can both change in one adaptation pass.
5. The GovInv trigger uses clipped `state["ra"]`, not raw `ra0`: `ra < ramin+0.02` gives `GovInv*=0.9`; `ra > ramax-0.02` gives `GovInv*=1.1`; otherwise it holds (`steady_state.py:219-226`; protected `HANK_mp_1eq.m:52-57`). With current bounds this means thresholds `0.04` and `0.07`, using strict inequalities.
6. After every nonconverged turn, whether or not adaptation opened, `tKNratio_next=0.6*KNratio_current+0.4*tKNratio_old` (`steady_state.py:257-293`; protected `HANK_mp_1eq.m:60-62`). A converged turn returns without adaptation or damping update.

No C0 expression reads `Ktarget`, `Kt_supply`, `Kt-Ktarget`, or private-K residual. The protected source comments label GovInv/state-owned capital and includes it in firm productive K and government income. However no inspected source or accepted data contract identifies it as an observed province public-capital stock. In the current runtime it is therefore an operational numerical stock with a government-capital label; choosing a production economic interpretation remains an Owner decision.
