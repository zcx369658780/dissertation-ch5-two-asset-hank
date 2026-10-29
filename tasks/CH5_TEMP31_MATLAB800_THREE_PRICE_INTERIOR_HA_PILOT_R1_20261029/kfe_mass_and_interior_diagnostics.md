# KFE credibility first, interior assets second

| Point | total probability | negative mass | original post G stationarity residual | contaminated raw-system residual | At diagnostic | Bt diagnostic | a internal | b internal | KFE certified |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 | 0.99999999999999978 | 7.2768608767739868e-17 | 4.686593832556138 | 2.8456122435781354e-17 | 7.2740978684863942 | 4.6982774669466716 | 1 | 0.32115115866345523 | False |
| P2 | 1.0000000000000002 | 0 | 0.32557163336740258 | 1.3064636178450328e-17 | 5.0722995536457365 | 1.8147088284647883 | 0.94610432781602316 | 0.70104645099053653 | False |
| P4 | 1 | 1.6893356816383517e-16 | 3.7634433046985296 | 1.4619788669609224e-17 | 7.2688448772635486 | 4.7097431300129102 | 1 | 0.30704855218476157 | False |
| P5 | 1 | 9.6177918267864433e-17 | 3.4077708099368875 | 1.9827347229328662e-17 | 7.3037783353426775 | 4.6887577964605072 | 0.99999999999999989 | 0.32754863914089327 | False |


These At/Bt values and marginal probabilities are outputs of failed KFE certification and are not reported as successful equilibria. All four pass the finite/mass/negative-mass/contaminated-system criteria and the preregistered interior diagnostics, but fail maxabs(postG.T@g)<=1e-7. Normalization or an interior-looking distribution cannot repair the original stationarity residual. P1/P3/P6 have no KFE density,marginals or moments: HJB did not converge,so KFE was NOT_EXECUTED.

The unchanged source contaminated row is floor(.37*800)-1=295 in zero-based indexing; rhs there is.007. Source raw signed solution and normalization by sum(raw)*db*da are retained. No clip,abs,density correction,alternative matrix or replacement solve is used. The actual source post operator is supplied directly and its identity/hash checked unchanged. Certification evaluates original postG.T@g and independently the actual contaminated raw system M@raw-rhs,not a different normalized right-hand side.

Integration weight is db*da=70/361. At=sum(a*g*db*da),Bt=sum(b*g*db*da),Lt=sum(z*l*g*db*da),Ct=sum(c*g*db*da). No extra dz,population or N/household multiplier is inserted. Signed negative mass uses sum(max(-g,0))*db*da only as a diagnostic; density itself is never modified. All full20-bin a and b signed marginals,endpoint/internal masses,modal indices/asset locations,negative density cell counts,At distances,Lt and Ct are in each actual point result and report.

The source iteration operators stayed below the original .01 homecrit during this run,whereas returned post operators can have much larger row-loss norms. These are separate matrices and separately recorded. No claim is made that a small iteration row norm certifies the post matrix or full MATLAB equivalence. No source guard/algorithm was added or altered; the failed KFE residuals remain the decisive certification failures here.
