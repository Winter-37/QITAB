---
id: eigenvalue-and-eigenvector-derivatives
title: Derivatives of eigenvalues and eigenvectors - the matrix Hellmann-Feynman theorem, second derivatives, eigenvector derivatives and their phase, near-degeneracy, degenerate levels, and the generalized problem H c = ε S c
summary: For a symmetric (Hermitian) matrix A(t) with a nondegenerate eigenpair, dλₖ = vₖᵀ A' vₖ: the matrix Hellmann–Feynman theorem. The eigenvector derivative is a sum over the other eigenvectors with denominators λₖ − λⱼ, once its component along vₖ is fixed to zero by normalization and phase. The second derivative of the lowest eigenvalue has a sum-over-states term that is never positive. Near-degeneracy makes the eigenvector derivative large: a first-order estimate holds only while the coupling is small compared with the splitting. At an exact degeneracy the slopes are the eigenvalues of A' projected onto the degenerate subspace, and the eigenvectors that vary smoothly are the combinations that diagonalize that projection. For H c = ε S c with S-normalized vectors the same formulas hold with A' replaced by H' − ε S′ plus a −½ c (cᵀS′c) term. That is the matrix origin of the energy-weighted density and of the U matrices of coupled-perturbed Hartree–Fock. Every formula is checked numerically.
status: in-progress
kind: derivation
level: intermediate
tags: [eigenvalue-derivative, eigenvector-derivative, hellmann-feynman, sum-over-states, degenerate-perturbation, generalized-eigenvalue-problem, energy-weighted-density, phase-convention, near-degeneracy, avoided-crossing]
prerequisites: [matrix-calculus, matrix-eigenvalue-problem]
related: [rayleigh-schrodinger-perturbation-theory, degenerate-perturbation-theory, derivative-integrals-and-u-matrices, rhf-analytic-gradient, floating-point-and-eigenvalue-perturbation, envelope-theorem-and-the-lagrangian-method, matrix-differentiation-identities]
key: dlam
order: 60
date: 2026-11-26
---

$\mathbf A(t)$ is real symmetric and smooth in a parameter $t$, with $\mathbf A' = d\mathbf A/dt$ and $\mathbf A'' = d^2\mathbf A/dt^2$ at the point of interest. Its eigenpairs are $(\lambda_k, \mathbf v_k)$ with $\mathbf v_j^{\rm T}\mathbf v_k = \delta_{jk}$, and $W_{jk} = \mathbf v_j^{\rm T}\mathbf A'\mathbf v_k$. Hermitian matrices work the same way with $\mathbf v^\dagger$ in place of $\mathbf v^{\rm T}$, apart from the phase remark below.

The formulas are collected as a lookup table in [[matrix-differentiation-identities]] (Part 9).

## Nondegenerate eigenvalues

**First derivative.** Differentiate $\mathbf A\mathbf v_k = \lambda_k\mathbf v_k$:

$$
\mathbf A'\mathbf v_k + \mathbf A\mathbf v_k' = \lambda_k'\mathbf v_k + \lambda_k\mathbf v_k' .
$$

Multiply from the left by $\mathbf v_k^{\rm T}$. The terms in $\mathbf v_k'$ cancel because $\mathbf v_k^{\rm T}\mathbf A = \lambda_k\mathbf v_k^{\rm T}$, leaving

$$
\lambda_k' = \mathbf v_k^{\rm T}\mathbf A'\mathbf v_k = W_{kk} .
\label{dlam}
$$

This is the Hellmann–Feynman theorem in matrix form. The eigenvector response drops out because the eigenvalue is stationary with respect to the eigenvector: $\lambda_k$ is a stationary value of the Rayleigh quotient. The same stationarity argument is made general in [[envelope-theorem-and-the-lagrangian-method]].

**Eigenvector derivative.** Multiply instead by $\mathbf v_j^{\rm T}$ with $j\ne k$: $W_{jk} + \lambda_j\,\mathbf v_j^{\rm T}\mathbf v_k' = \lambda_k\,\mathbf v_j^{\rm T}\mathbf v_k'$. That fixes every component of $\mathbf v_k'$ except the one along $\mathbf v_k$ itself:

$$
\mathbf v_k' = \sum_{j\ne k}\mathbf v_j\,\frac{W_{jk}}{\lambda_k - \lambda_j} + c_k\mathbf v_k .
\label{dv}
$$

**The component along $\mathbf v_k$.** Normalization gives $\mathbf v_k^{\rm T}\mathbf v_k' = 0$ for real vectors, so $c_k = 0$. For complex vectors normalization fixes only $\mathrm{Re}\,c_k = 0$. $\mathrm{Im}\,c_k$ is a free phase change, and a convention must be chosen (for example the parallel-transport choice $c_k = 0$). Numerical eigensolvers return eigenvectors with arbitrary signs or phases at each $t$, so finite differences of eigenvectors need the phase aligned first.

**Second derivative.** Differentiate Eq. [[#dlam]] once more and use Eq. [[#dv]]:

$$
\lambda_k'' = \mathbf v_k^{\rm T}\mathbf A''\mathbf v_k + 2\sum_{j\ne k}\frac{W_{jk}^2}{\lambda_k - \lambda_j} .
\label{d2lam}
$$

For the lowest eigenvalue every denominator is negative, so the sum-over-states term is never positive: coupling to higher states always lowers the curvature. This is the matrix form of second-order Rayleigh–Schrödinger perturbation theory, with $\mathbf A = \mathbf H_0 + t\mathbf V$ giving $E^{(2)} = \tfrac12\lambda''$ ([[rayleigh-schrodinger-perturbation-theory]]). It is also why a static polarizability, $-\partial^2E/\partial F^2$, is positive for a ground state.

## Near-degeneracy

**Large derivatives.** The denominators $\lambda_k - \lambda_j$ in Eq. [[#dv]] make $\mathbf v_k'$ large when another eigenvalue is close. In a two-level model with splitting $\Delta$ and coupling $tg$, the exact mixing angle is $\theta = \tfrac12\arctan(2tg/\Delta)$. The first-order estimate $tg/\Delta$ is good only while $tg\ll\Delta$. Past that point the eigenvectors rotate by up to $\pi/4$, whatever the size of $t$.

**Consequences.**

- **Avoided crossings.** Molecular wave functions change character over a short range of geometry.
- **Large couplings.** Nonadiabatic couplings $\langle\Psi_j|\partial_x\Psi_k\rangle = \langle\Psi_j|\partial_xH|\Psi_k\rangle/(E_k - E_j)$ grow without bound at conical intersections.
- **Ill-conditioned responses.** CPHF and orbital-response equations become ill-conditioned when an occupied and a virtual level approach. The accuracy limits of computing such quantities are in [[floating-point-and-eigenvalue-perturbation]].

## Degenerate eigenvalues

**The adapted basis.** Let $\lambda$ be $m$-fold degenerate at $t = 0$, with eigenspace spanned by the columns of $\mathbf P$ ($n\times m$, orthonormal). Any orthonormal basis of the eigenspace is a valid set of eigenvectors at $t = 0$. But only one basis, up to order within the degeneracy, continues smoothly to $t\ne0$. Write $\mathbf v(t) = \mathbf P\mathbf r + O(t)$ and project the differentiated eigenvalue equation onto the eigenspace:

$$
(\mathbf P^{\rm T}\mathbf A'\mathbf P)\,\mathbf r = \lambda'\,\mathbf r .
\label{degen}
$$

**The slopes.** The $m$ branches leave the degenerate point with slopes equal to the eigenvalues of the projected perturbation $\mathbf P^{\rm T}\mathbf A'\mathbf P$. The adapted (zeroth-order) eigenvectors are $\mathbf P\mathbf r$. This is first-order degenerate perturbation theory ([[degenerate-perturbation-theory]]).

**Kinks.** If the slopes differ, the levels cross linearly at $t = 0$. A solver that sorts eigenvalues by size then produces kinks, and a central finite difference returns the average of the two slopes. Eq. [[#dv]] can then be used for the adapted vectors only, with the sums restricted to $j$ outside the degenerate set. The $O(t)$ components within the degenerate set need second-order information.

## The generalized eigenproblem

**The problem.** In a nonorthogonal basis, $\mathbf H\mathbf c_k = \varepsilon_k\mathbf S\mathbf c_k$ with $\mathbf c_j^{\rm T}\mathbf S\mathbf c_k = \delta_{jk}$, and both $\mathbf H$ and $\mathbf S$ depend on $t$. This is the Roothaan–Hall equation with geometry-dependent AOs, or a CI problem in a nonorthogonal basis.

**Derivatives.** Differentiating as above, with the $\mathbf S$-inner product:

$$
\varepsilon_k' = \mathbf c_k^{\rm T}(\mathbf H' - \varepsilon_k\mathbf S')\mathbf c_k,\qquad
\mathbf c_k' = \sum_{j\ne k}\mathbf c_j\,\frac{\mathbf c_j^{\rm T}(\mathbf H' - \varepsilon_k\mathbf S')\mathbf c_k}{\varepsilon_k - \varepsilon_j} - \tfrac12\,\mathbf c_k\,(\mathbf c_k^{\rm T}\mathbf S'\mathbf c_k) .
\label{gen}
$$

The last term comes from differentiating the normalization $\mathbf c_k^{\rm T}\mathbf S\mathbf c_k = 1$.

**What this is in quantum chemistry.** $-\varepsilon_k\mathbf c_k^{\rm T}\mathbf S'\mathbf c_k$, summed over occupied orbitals, is the energy-weighted density term $-\mathrm{tr}(\mathbf W\mathbf S^x)$ of the RHF gradient ([[rhf-analytic-gradient]]). The coefficients of $\mathbf c_k'$ on the $\mathbf c_j$ are the U matrices, and the $-\tfrac12$ term is the familiar $U_{kk}^x = -\tfrac12S_{kk}^x$ ([[derivative-integrals-and-u-matrices]]). In SCF, $\mathbf H$ is the Fock matrix, which itself depends on $\mathbf c$, so the occupied–virtual U matrices must be solved for (CPHF) rather than read off Eq. [[#gen]].

## Worked example

!!! example "Checks against finite differences (computed for this note)"
    Random symmetric $5\times5$ matrices, $\mathbf A(t) = \mathbf A_0 + t\mathbf A_1 + t^2\mathbf A_2$, eigenvalues of $\mathbf A_0$ $(-3.888, -1.002, 0.430, 1.515, 2.062)$, step $h = 10^{-5}$:

    - **Eq. [[#dlam]]:** largest error over the five slopes $1.6\times10^{-10}$.
    - **Eq. [[#d2lam]]:** largest error $3\times10^{-5}$ (the finite-difference second derivative limits this). For the lowest level the sum-over-states term is $-0.9438$.
    - **Eq. [[#dv]]** for $k = 0$ and $k = 2$, after aligning the solver's signs: errors $2.0\times10^{-11}$ and $1.2\times10^{-10}$, with $\mathbf v_k^{\rm T}\mathbf v_k' = 0$.

    **Near-degeneracy.** For the two-level model with unit coupling derivative:

    - splitting 0.1: first-order rotation after $t = 0.01$ is 0.100 rad, exact 0.0987;
    - splitting 0.001: the first-order estimate is 10 rad, which is meaningless; the exact angle is 0.760 rad, close to the limit $\pi/4$.

    **Degeneracy.** $\mathbf A_0$ with a doubly degenerate eigenvalue 0.5 and a random $\mathbf A'$. The projected matrix $\mathbf P^{\rm T}\mathbf A'\mathbf P$ has eigenvalues $-0.8170$ and $1.0621$. One-sided differences at $t = 0^+$ give slopes $-0.8170$ and $1.0621$, but the central difference gives 0.1226 for both, their average, because the sorted branches cross. At $t = 10^{-7}$ the solver's eigenvectors overlap the adapted combinations $\mathbf P\mathbf r$ with modulus 1.000.

    **Generalized problem.** Random $\mathbf H(t)$, positive definite $\mathbf S(t)$: Eq. [[#gen]] reproduces $\varepsilon'$ to $2\times10^{-11}$ and $\mathbf c'$ to $6\times10^{-11}$ for $k = 0$ and 3. Without the $-\tfrac12\mathbf c(\mathbf c^{\rm T}\mathbf S'\mathbf c)$ term, $\mathbf c'$ is wrong at first order.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000), Sec. 4.2.6 (the Hellmann–Feynman theorem). The matrix derivations are standard first- and second-order perturbation theory written for finite matrices, derived here and checked numerically. The connection to U matrices and the energy-weighted density follows the notebook's own analytic-gradient notes. Calculations in `Claude outputs/part0_math_batchF.py`, section B.
