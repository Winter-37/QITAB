---
id: density-fitting-and-cholesky-decomposition
title: Density fitting and Cholesky decomposition of the electron-repulsion integrals - the positive semidefinite ERI matrix, pivoted Cholesky with its error bound, Coulomb-metric fitting and its second-order error, and factorized Hamiltonians
summary: Read the AO integrals (μν|λσ) as a matrix over orbital pairs. It is the Gram matrix of the overlap densities in the Coulomb inner product, so it is positive semidefinite and numerically of low rank. A pivoted, incomplete Cholesky decomposition stops when the largest remaining diagonal is below τ, which bounds every integral error by τ; for H₂O/cc-pVDZ, τ = 10⁻⁴ needs 121 vectors (5n) and changes the RHF energy by 4.5 × 10⁻⁵ Eₕ. Density fitting expands each pair density in an atom-centred auxiliary basis and fits it in the Coulomb metric. The integral error is then the Coulomb interaction of the two fitting residuals, second order. The residual matrix is positive semidefinite, so the Coulomb and exchange energies of any density are both underestimated. Plain overlap-metric fitting has a first-order error several hundred times larger, which Dunlap's robust formula removes. The same factorization written in the MO basis gives the single- and double-factorized Hamiltonians used in quantum algorithms.
status: in-progress
kind: theory
level: intermediate
tags: [density-fitting, resolution-of-the-identity, ri, cholesky-decomposition, pivoted-cholesky, auxiliary-basis, coulomb-metric, robust-fitting, low-rank, electron-repulsion-integrals, double-factorization, rhf, mp2, pyscf]
prerequisites: [electron-repulsion-integrals-md-os-rys, multipole-methods-and-integral-screening, cholesky-and-generalized-eigenproblem, polar-and-singular-value-decompositions, rhf]
related: [tensor-decompositions, mp2, laplace-transform, molecular-hamiltonian-in-the-mo-basis, qpe-cost-and-resource-estimates, orbital-rotations, kohn-sham-dft]
conventions: [ia-letters, chemists-integrals]
key: df
order: 100
date: 2026-11-26
---

$\chi_\mu$ are the $n$ AO basis functions. $\Omega_{\mu\nu}=\chi_\mu\chi_\nu$ is an overlap distribution, and $a=(\mu\nu)$, $\mu\ge\nu$, labels the $n(n+1)/2$ pairs. Two functions interact through

$$
(f|g)=\iint\frac{f(\mathbf r_1)\,g(\mathbf r_2)}{r_{12}}\,d\mathbf r_1d\mathbf r_2 ,
$$

so $(\mu\nu|\lambda\sigma)=(\Omega_{\mu\nu}|\Omega_{\lambda\sigma})$. $\chi_P$ are auxiliary functions and $J_{PQ}=(\chi_P|\chi_Q)$. $D_{\mu\nu}=2\sum_iC_{\mu i}C_{\nu i}$ is the closed-shell AO density. The Coulomb and exchange energies are $E_J=\tfrac12\sum D_{\mu\nu}(\mu\nu|\lambda\sigma)D_{\lambda\sigma}$ and $E_K=\tfrac14\sum D_{\mu\nu}D_{\lambda\sigma}(\mu\lambda|\nu\sigma)$, and $E_{\text{RHF}}$ contains $E_J-E_K$. Indices $\mu\nu\lambda\sigma$ are AOs, $P,Q$ auxiliary functions, $L$ Cholesky vectors and $p,q,r,s$ MOs.

## The ERI matrix is positive semidefinite and nearly singular

**The Coulomb inner product is positive.** In Fourier space, with $\hat f(\mathbf k)=\int f(\mathbf r)e^{-i\mathbf k\cdot\mathbf r}d\mathbf r$,

$$
(f|f)=\int\frac{d\mathbf k}{(2\pi)^3}\,\frac{4\pi}{k^2}\,|\hat f(\mathbf k)|^2\ \ge\ 0 ,
$$

because the Fourier transform of $1/r$ is $4\pi/k^2>0$ ([[fourier-transforms-and-the-dirac-delta]]). So $V_{ab}=(\Omega_a|\Omega_b)$ is a Gram matrix and $\mathbf V\succeq0$. This is also what makes the Schwarz inequality $|(a|b)|\le\sqrt{(a|a)(b|b)}$ of [[multipole-methods-and-integral-screening]] hold.

**It is numerically rank deficient.** There are $n(n+1)/2$ products of $n$ functions, but they are far from linearly independent. Products of two functions on the same atom resemble a smaller set of functions with higher angular momentum. Products of distant functions are negligible.

For H₂O/cc-pVDZ ($n=24$, 300 pairs), the eigenvalues of $\mathbf V$ run from 19.8 down to $-5\times10^{-16}$:

| eigenvalue threshold | $10^{-6}$ | $10^{-8}$ | $10^{-10}$ |
|---|---:|---:|---:|
| eigenvalues above it | 183 | 241 | 273 |

Both methods below exploit this structure. Each writes

$$
(\mu\nu|\lambda\sigma)\approx\sum_{L=1}^{M}B^L_{\mu\nu}B^L_{\lambda\sigma},\qquad M\approx3n\text{-}10n ,
\label{factor}
$$

that is, $\mathbf V\approx\mathbf B^{\mathsf T}\mathbf B$ with a tall three-index $\mathbf B$. Storage falls from about $n^4/8$ to $Mn^2/2$. For $n=100$ that is 100 MB against 12 MB, and the gap grows with $n$.

## Pivoted Cholesky decomposition

The full Cholesky factorization of [[cholesky-and-generalized-eigenproblem]] would be too expensive and is not needed. The incomplete version picks the largest remaining diagonal at each step (Beebe and Linderberg; Koch, Sánchez de Merás and Pedersen):

1. Set the residual diagonal $d_a=V_{aa}=(a|a)$.
2. Pick the pivot $p=\arg\max_ad_a$. Stop if $d_p\le\tau$.
3. Form the new vector $L_a=\big(V_{ap}-\sum_{L'}L'_aL'_p\big)/\sqrt{d_p}$. Only column $p$ of $\mathbf V$ is needed.
4. Update $d_a\leftarrow d_a-L_a^2$ and return to step 2.

**Error bound.** The residual $\mathbf R=\mathbf V-\mathbf L^{\mathsf T}\mathbf L$ is a Schur complement of a positive semidefinite matrix, hence itself positive semidefinite. Its diagonal is the final $d_a\le\tau$. A positive semidefinite matrix obeys $|R_{ab}|\le\sqrt{R_{aa}R_{bb}}$, so

$$
\big|(\mu\nu|\lambda\sigma)-(\mu\nu|\lambda\sigma)_{\text{CD}}\big|\le\tau\qquad\text{for every integral.}
\label{cd-bound}
$$

The threshold is a rigorous, uniform error bound on every integral, which no fitted auxiliary basis provides. Only the $M$ pivot columns of $\mathbf V$ are ever computed. The pivots define an auxiliary basis made from the molecule's own products, so no basis set has to be chosen.

!!! example "Cholesky vectors for H₂O/cc-pVDZ"
    Reference energy: conventional RHF $E=-76.0267720534$. The bound of Eq. [[#cd-bound]] holds in every row of the table.

    | $\tau$ | vectors $M$ | $M/n$ | max integral error | $\Delta E_{\text{RHF}}$ ($E_h$) |
    |---:|---:|---:|---:|---:|
    | $10^{-2}$ | 61 | 2.5 | $1.0\times10^{-2}$ | $+1.1\times10^{-2}$ |
    | $10^{-4}$ | 121 | 5.0 | $9.5\times10^{-5}$ | $+4.5\times10^{-5}$ |
    | $10^{-6}$ | 185 | 7.7 | $9.6\times10^{-7}$ | $+2.4\times10^{-7}$ |
    | $10^{-8}$ | 248 | 10.3 | $7.2\times10^{-9}$ | $+5.5\times10^{-9}$ |

    - **Close to optimal.** At $\tau=10^{-6}$ the 185 vectors are within two of the 183 eigenvalues above $10^{-6}$, the optimal truncation.
    - **Accuracy.** The RHF error falls roughly as $\tau$.

## Density fitting

**The fit.** Expand each pair density in the auxiliary basis, $\Omega_a\approx\tilde\Omega_a=\sum_Pc^P_a\chi_P$, with residual $\Delta_a=\Omega_a-\tilde\Omega_a$. Choose the coefficients to minimize the Coulomb self-repulsion of the residual, $(\Delta_a|\Delta_a)$ (Whitten; Dunlap, Connolly and Sabin; Vahtras, Almlöf and Feyereisen). Setting the derivative with respect to $c^P_a$ to zero gives

$$
(\chi_P|\Delta_a)=0\quad\Longrightarrow\quad\sum_QJ_{PQ}\,c^Q_a=(P|a) ,
$$

so

$$
(\mu\nu|\lambda\sigma)_{\text{DF}}=\sum_{PQ}(\mu\nu|P)\,[\mathbf J^{-1}]_{PQ}\,(Q|\lambda\sigma) .
\label{df}
$$

This has the form of Eq. [[#factor]] with $\mathbf B=\mathbf J^{-1/2}(Q|\mu\nu)$, or with the Cholesky factor of $\mathbf J$ in place of $\mathbf J^{1/2}$. It needs only three-index integrals $(P|\mu\nu)$ and two-index integrals $J_{PQ}$.

**The error is second order.** Expand the exact integral around the fit:

$$
(\Omega_a|\Omega_b)=(\tilde\Omega_a|\tilde\Omega_b)+(\tilde\Omega_a|\Delta_b)+(\Delta_a|\tilde\Omega_b)+(\Delta_a|\Delta_b).
$$

The two cross terms vanish, because $\tilde\Omega$ lies in the auxiliary space and every residual is Coulomb-orthogonal to that space. With $(\tilde\Omega_a|\tilde\Omega_b)=(\mu\nu|\lambda\sigma)_{\text{DF}}$, this leaves

$$
(\mu\nu|\lambda\sigma)-(\mu\nu|\lambda\sigma)_{\text{DF}}=(\Delta_{\mu\nu}|\Delta_{\lambda\sigma}) .
\label{df-error}
$$

The error is quadratic in the fitting residuals. A residual with 1 % of the Coulomb norm of the density gives integrals good to about $10^{-4}$ in relative terms. Dunlap called such a fit **robust**.

**Both energies are underestimated.** By Eq. [[#df-error]] the residual matrix $\mathbf R=\mathbf V-\mathbf V_{\text{DF}}$ is a Gram matrix, hence positive semidefinite.

- **Coulomb.** $E_J-E_J^{\text{DF}}=\tfrac12\mathbf d^{\mathsf T}\mathbf R\,\mathbf d\ge0$ for every density, where $\mathbf d$ is $D$ written as a pair vector.
- **Exchange.** $E_K-E_K^{\text{DF}}=\tfrac14\operatorname{tr}(\mathbf R\mathbf W)\ge0$, with $W_{(\mu\lambda),(\nu\sigma)}=D_{\mu\nu}D_{\lambda\sigma}$. This matrix $\mathbf W=\mathbf D\otimes\mathbf D$ is positive semidefinite, and the trace of a product of two positive semidefinite matrices is non-negative.

The total energy contains $E_J-E_K$, so its error has no fixed sign.

**Which auxiliary basis.** Auxiliary sets are optimized for a purpose. JK-fitting sets (for example cc-pVDZ-JKFIT, or Weigend's universal def2 set) are meant for Coulomb and exchange in SCF. RI (MP2-fitting) sets are smaller and are fitted to the occupied-virtual products that dominate correlation energies.

!!! example "Density fitting for H₂O/cc-pVDZ, same molecule"
    | auxiliary basis | $N_{\text{aux}}$ | max integral error | $E_J^{\text{DF}}-E_J$ | $E_K^{\text{DF}}-E_K$ | $\Delta E_{\text{RHF}}$ |
    |---|---:|---:|---:|---:|---:|
    | cc-pVDZ-JKFIT | 116 (4.8 $n$) | $2.4\times10^{-2}$ | $-2.9\times10^{-5}$ | $-5.0\times10^{-5}$ | $+2.1\times10^{-5}$ |
    | def2-universal-JKFIT | 113 (4.7 $n$) | $7.6\times10^{-3}$ | $-3.2\times10^{-5}$ | $-6.5\times10^{-5}$ | $+3.3\times10^{-5}$ |
    | cc-pVDZ-RI (MP2 set) | 84 (3.5 $n$) | $2.5\times10^{-2}$ | $-2.4\times10^{-3}$ | $-1.3\times10^{-3}$ | $-1.1\times10^{-3}$ |

    $E_J$ and $E_K$ are evaluated on the conventional RHF density ($E_J=46.90$, $E_K=8.98\ E_h$). Checks and comparisons:

    - **Signs.** Both differences are negative in every row, as proved above.
    - **First order.** Their difference equals $\Delta E_{\text{RHF}}$ to the digits shown, because SCF relaxation enters only at second order.
    - **Residual matrix.** The eigenvalues of $\mathbf V-\mathbf V_{\text{DF}}$ lie in $[-4\times10^{-17},\,5\times10^{-2}]$, positive semidefinite to rounding. The Schwarz bound $|R_{ab}|\le\sqrt{R_{aa}R_{bb}}$ is never violated (by more than $4\times10^{-18}$).
    - **Wrong purpose.** The MP2 set gives a 50 times larger SCF error. Used for what it was made for, RI-MP2 on the conventional orbitals, it changes $E_c^{(2)}=-0.2040036$ by $+1.5\times10^{-5}$ (0.007 %).
    - **Against Cholesky.** JK fitting with 116 functions is about as accurate as Cholesky with $\tau=10^{-4}$ (121 vectors). The largest individual integral error is much larger (0.024 against $10^{-4}$), but the energy errors are similar. A fitted basis targets energies; Cholesky bounds every element.

**Overlap metric.** Fitting with the overlap $\int\Delta_a\chi_P$ instead of the Coulomb metric loses the cancellation. The plain product $(\tilde\Omega_a|\tilde\Omega_b)$ is then wrong to first order: $E_J$ is off by $+1.6\times10^{-2}\ E_h$ with the JKFIT functions.

Dunlap's robust combination restores the second-order error for any fit:

$$
(\Omega_a|\Omega_b)\approx(\tilde\Omega_a|\Omega_b)+(\Omega_a|\tilde\Omega_b)-(\tilde\Omega_a|\tilde\Omega_b).
$$

It brings the $E_J$ error to $-4.9\times10^{-5}$, close to the Coulomb-metric value. Local fitting schemes use other metrics for the same reason.

## Cost, and when each is used

- **Coulomb matrix.** It costs $O(n^2N_{\text{aux}})$ through $\gamma_P=\sum_Q[\mathbf J^{-1}]_{PQ}\sum_{\lambda\sigma}(Q|\lambda\sigma)D_{\lambda\sigma}$. RI-J is nearly free in DFT without exact exchange ([[kohn-sham-dft]]).
- **Exchange.** It costs $O(n_{\text{occ}}n^2N_{\text{aux}})$: half-transform $B^L_{\mu i}$ first.
- **Correlation.** MP2 and coupled cluster need $(ia|jb)=\sum_LB^L_{ia}B^L_{jb}$. Only the three-index $B^L_{ia}$ is transformed, at $O(n^3N_{\text{aux}})$, instead of the $O(n^5)$ four-index transformation ([[molecular-hamiltonian-in-the-mo-basis]]). Combined with a Laplace-transformed denominator, this gives reduced-scaling MP2 ([[laplace-transform]]).
- **Gradients.** With DF the auxiliary functions are atom-centred and move with the atoms, so derivative integrals follow the usual rules. Cholesky pivots can change discontinuously with geometry, which makes analytic gradients of CD energies more delicate. That matters for geometry optimization.
- **Choosing.** DF is cheaper per vector and standard in production codes. CD is preferred when an error bound independent of the method is needed, or for benchmarks that must converge to the exact-integral result.

## Factorized Hamiltonians

**Single factorization.** In the MO basis, Eq. [[#factor]] reads $(pq|rs)=\sum_LL^L_{pq}L^L_{rs}$ with $\mathbf L^L$ symmetric $n\times n$ matrices. The spin-free two-electron operator of HJO Eq. (2.2.18) becomes

$$
\tfrac12\sum_{pqrs}(pq|rs)\big(E_{pq}E_{rs}-\delta_{qr}E_{ps}\big)=\tfrac12\sum_L\big(\hat L^L\big)^2-\tfrac12\sum_{ps}\Big(\sum_q(pq|qs)\Big)E_{ps},\qquad\hat L^L=\sum_{pq}L^L_{pq}E_{pq} .
$$

The Hamiltonian is a sum of squares of one-body operators plus a one-body correction.

**Double factorization.** Diagonalize each vector, $\mathbf L^L=\mathbf U^L\operatorname{diag}(\lambda^L_k)\mathbf U^{L\mathsf T}$. Then $\hat L^L=\sum_k\lambda^L_k\hat n_k^{(L)}$ is a sum of number operators of rotated orbitals. Each square is diagonal after one orbital rotation $e^{-\hat\kappa^L}$ ([[orbital-rotations]]), and small $|\lambda^L_k|$ can be dropped. This is the low-rank structure that block encodings for phase estimation use ([[qpe-cost-and-resource-estimates]]).

For H₂O/cc-pVDZ with $\tau=10^{-6}$ (185 vectors, MO-basis integrals reproduced to $1.9\times10^{-5}$), dropping eigenvalues gives:

| eigenvalues kept | per vector, of 24 | max ERI error |
|---|---:|---:|
| $\vert\lambda\vert>10^{-2}$ | 7.6 | $2.9\times10^{-3}$ |
| $\vert\lambda\vert>10^{-3}$ | 13.2 | $1.4\times10^{-4}$ |
| $\vert\lambda\vert>10^{-4}$ | 16.9 | $1.9\times10^{-5}$ |

## Source

HJO (Helgaker, Jørgensen and Olsen) does not treat density fitting or Cholesky decomposition. The second-quantized Hamiltonian used for the factorized form is their Eq. (2.2.18):

- Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000), Sec. 2.2.1, Eqs. (2.2.16) and (2.2.18).

The methods are from the papers:

- Beebe and Linderberg, "Simplifications in the generation and transformation of two-electron integrals in molecular calculations", *Int. J. Quantum Chem.* **12**, 683-705 (1977), doi:10.1002/qua.560120408.
- Koch, Sánchez de Merás and Pedersen, "Reduced scaling in electronic structure calculations using Cholesky decompositions", *J. Chem. Phys.* **118**, 9481-9484 (2003), doi:10.1063/1.1578621.
- Whitten, "Coulombic potential energy integrals and approximations", *J. Chem. Phys.* **58**, 4496-4501 (1973). The DOI is not checked.
- Dunlap, Connolly and Sabin, "On some approximations in applications of Xα theory", *J. Chem. Phys.* **71**, 3396-3402 (1979), doi:10.1063/1.438728.
- Vahtras, Almlöf and Feyereisen, "Integral approximations for LCAO-SCF calculations", *Chem. Phys. Lett.* **213**, 514-518 (1993), doi:10.1016/0009-2614(93)89151-7.
- Dunlap, "Robust and variational fitting", *Phys. Chem. Chem. Phys.* **2**, 2113-2116 (2000). Title and journal are taken from a reference list; the paper was not read and the DOI is not checked.
- Weigend, "A fully direct RI-HF algorithm: Implementation, optimised auxiliary basis sets, demonstration of accuracy and efficiency", *Phys. Chem. Chem. Phys.* **4**, 4285-4291 (2002), doi:10.1039/b204199p.

Which statement comes from which paper:

- **Error bound and sign.** The proofs that every integral error is at most τ and that $E_J$ and $E_K$ are underestimated are worked out here from positive semidefiniteness. The second-order error is Dunlap's "robust" observation, re-derived here.
- **Robust overlap-metric formula.** It is attributed to Dunlap (2000) from memory, to verify against the paper.
- **Gradients remark and factorized Hamiltonian.** These are general knowledge.

Every number is computed with PySCF 2.15 in `Claude outputs/part0_math_batchH.py`, section B.
