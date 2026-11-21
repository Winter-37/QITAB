---
id: davidson-and-jacobi-davidson-methods
title: Davidson and Jacobi–Davidson methods - preconditioned subspace updates for a few eigenpairs
summary: Instead of Krylov directions, add to the subspace an approximate solution of the correction equation (A − θ)q = −r. Davidson's choice M = diag(A) − θ is very effective for diagonally dominant CI matrices. A better M can make things worse, since M = A − θ returns q = −x and adds nothing. Projecting the correction equation orthogonal to x (Jacobi–Davidson; the same step as HJO's quasi-Newton CI step) fixes this: q = −M⁻¹r + εM⁻¹x with ε = xᵀM⁻¹r/xᵀM⁻¹x. Block version, collapse, and a working code tested on model matrices and on a 245 025-determinant FCI of water (3 roots in 14 iterations against 38 without preconditioning).
status: in-progress
kind: algorithm
level: advanced
tags: [davidson, jacobi-davidson, quasi-newton-ci-step, preconditioner, correction-equation, block-davidson, subspace-collapse, fci, sigma-vector]
prerequisites: [rayleigh-ritz-and-harmonic-ritz, lanczos-and-krylov-subspaces]
related: [ci-optimization-newton-and-davidson, determinant-strings-and-direct-ci, ci-in-practice, preconditioned-conjugate-gradient, eom-ccsd-and-size-extensivity, inexact-newton-and-newton-cg]
key: jd
order: 30
date: 2026-11-21
---

## Overview

A Krylov method ([[lanczos-and-krylov-subspaces]]) adds $\mathbf A\mathbf q$ to the subspace and knows nothing about $\mathbf A$ beyond products. Many matrices of quantum chemistry are strongly diagonally dominant in a good basis: CI matrices in determinants built on Hartree–Fock orbitals, the response matrices of CPHF and EOM. Approximate-inverse updates exploit that structure (Steffen Sec. 3.2). For such matrices they are, in Steffen's words, the most interesting methods and give the best performance.

**Notation.** As in [[rayleigh-ritz-and-harmonic-ritz]]: current Ritz pair $(\theta,\mathbf x)$ with $\|\mathbf x\| = 1$, residual $\mathbf r = \mathbf A\mathbf x-\theta\mathbf x$. $\mathbf M$ is an easily inverted approximation to $\mathbf A-\theta\mathbf1$ (the preconditioner).

## The correction equation

We want a correction $\mathbf q$ with $\mathbf A(\mathbf x+\mathbf q) = \lambda(\mathbf x+\mathbf q)$. Write $\lambda = \theta+\delta$ and drop the second-order term $\delta\mathbf q$:

$$
(\mathbf A-\theta\mathbf1)\,\mathbf q = -\mathbf r+\delta\,\mathbf x .
\label{correction}
$$

The term $\delta\mathbf x$ lies along $\mathbf x$, which is already in the subspace. Dropping it and replacing $\mathbf A-\theta\mathbf1$ by $\mathbf M$ gives the generic update

$$
\mathbf q = -\mathbf M^{-1}\mathbf r ,\qquad \mathcal V\leftarrow\mathrm{span}(\mathcal V,\mathbf q).
\label{generic}
$$

- $\mathbf M = \mathbf1$ gives $\mathbf q\propto\mathbf r$. Since $\mathbf r\in\mathrm{span}(\mathcal V,\mathbf A\mathcal V)$, this is a Krylov method without its shortcuts.
- **Davidson's method** takes $\mathbf M = \mathrm{diag}(\mathbf A)-\theta\mathbf1$:

$$
q_p = -\frac{r_p}{A_{pp}-\theta} .
$$

For CI this is the familiar $-(H_{pp}-E)^{-1}r_p$ step with the diagonal of the CI matrix ([[ci-optimization-newton-and-davidson]]).

## The trap: a preconditioner that is too good

**Exact inverse.** If $\mathbf M = \mathbf A-\theta\mathbf1$ exactly, then

$$
\mathbf M^{-1}\mathbf r = (\mathbf A-\theta\mathbf1)^{-1}(\mathbf A-\theta\mathbf1)\mathbf x = \mathbf x ,
$$

which is already in $\mathcal V$. The subspace does not grow and the iteration stalls (Steffen Sec. 3.2). For a nearly exact $\mathbf M$ the new direction is nearly $\mathbf x$, and the useful part is lost in rounding. So improving the preconditioner can slow Davidson down, a puzzle that stood until the Jacobi–Davidson analysis.

## Jacobi–Davidson: project the correction

**Projected equation.** The correction is only needed orthogonal to $\mathbf x$. Restrict Eq. [[#correction]] to $\mathbf x^{\perp}$ with the projector $\mathbf P = \mathbf1-\mathbf x\mathbf x^{\mathsf T}$ (Sleijpen and van der Vorst, cited by Steffen):

$$
\mathbf P(\mathbf A-\theta\mathbf1)\mathbf P\,\mathbf q = -\mathbf r,\qquad \mathbf q\perp\mathbf x .
\label{jd}
$$

The right-hand side is already in $\mathbf x^\perp$, since $\mathbf x^{\mathsf T}\mathbf r = \mathbf x^{\mathsf T}\mathbf A\mathbf x-\theta = 0$.

**Solving it with $\mathbf M$.** Approximate $\mathbf A-\theta\mathbf1$ by $\mathbf M$ inside Eq. [[#jd]]. For $\mathbf q\perp\mathbf x$ we have $\mathbf P\mathbf q = \mathbf q$, and $\mathbf P\mathbf y = -\mathbf r$ means $\mathbf y = -\mathbf r+\varepsilon\mathbf x$ for some scalar $\varepsilon$. Hence $\mathbf M\mathbf q = -\mathbf r+\varepsilon\mathbf x$ and

$$
\mathbf q = -\mathbf M^{-1}\mathbf r+\varepsilon\,\mathbf M^{-1}\mathbf x,\qquad
\varepsilon = \frac{\mathbf x^{\mathsf T}\mathbf M^{-1}\mathbf r}{\mathbf x^{\mathsf T}\mathbf M^{-1}\mathbf x},
\label{olsen}
$$

where $\varepsilon$ is fixed by $\mathbf x^{\mathsf T}\mathbf q = 0$. This is Steffen's formula $\mathbf q = (\varepsilon+\theta)\mathbf M^{-1}\mathbf x-\mathbf M^{-1}\mathbf A\mathbf x$ up to an overall sign, since $\mathbf M^{-1}\mathbf A\mathbf x = \mathbf M^{-1}\mathbf r+\theta\mathbf M^{-1}\mathbf x$. It is exactly HJO's quasi-Newton step for CI, Eq. (11.5.24), with $\mathbf M = \mathbf H_0-E^{(0)}$ ([[ci-optimization-newton-and-davidson]]): HJO reach it from Newton's method, Steffen from the projected correction equation. (Steffen writes $\mathbf B$ both for the approximate inverse and, in this formula, for the approximation to $\mathbf A-\theta\mathbf1$; here $\mathbf M$ always means the latter.)

**What the projection buys.**

- With the exact $\mathbf M = \mathbf A-\theta\mathbf1$, Eq. [[#olsen]] gives $\mathbf q = -\mathbf x+\varepsilon(\mathbf A-\theta\mathbf1)^{-1}\mathbf x$. Modulo $\mathbf x$ the new direction is the Rayleigh-quotient-iteration vector, and the method converges cubically instead of stalling.
- With a diagonal $\mathbf M$ the extra term $\varepsilon\mathbf M^{-1}\mathbf x$ is a small change: Davidson and Jacobi–Davidson then behave almost the same.
- Steffen notes the preconditioner may change during the run: crude (diagonal) at the start, more accurate as $\mathbf x$ improves.

**Choosing $\mathbf M$.** Steffen's recommendations:

- extract a structurally simpler matrix from $\mathbf A$ and invert it (approximately): for most quantum-chemistry matrices a narrow, possibly tapered band, $\bar a_{pq} = a_{pq}$ for $|p-q|\le k_p$, $k_p\ll n$. Davidson's diagonal is the special case $k = 0$ and is often near optimal;
- if $\mathbf A$ is available only as a product, solve $(\mathbf A-\theta\mathbf1)\mathbf q = \mathbf r$ approximately by a few CG steps ([[linear-conjugate-gradient-method]]) instead. The projected form Eq. [[#jd]] is what makes such an inner solve safe.

## The algorithm (block form)

For the lowest $k$ roots:

1. Start from $k$ unit vectors on the lowest diagonal elements (for CI: the lowest determinants or CSFs). Form and store $\mathbf V$ and $\mathbf A\mathbf V$.
2. Rayleigh–Ritz: $\mathbf S = \mathbf V^{\mathsf T}(\mathbf A\mathbf V)$, eigenpairs $(\theta_j,\mathbf t_j)$, $j\le k$; Ritz vectors $\mathbf x_j = \mathbf V\mathbf t_j$ and residuals $\mathbf r_j = (\mathbf A\mathbf V)\mathbf t_j-\theta_j\mathbf x_j$.
3. Stop for root $j$ when $\|\mathbf r_j\|<\tau$. Some eigenvalue then lies within $\tau$ of $\theta_j$, and the energy error is $O(\tau^2)$.
4. For each unconverged root form $\mathbf q_j$ by Eq. [[#generic]] or [[#olsen]]. Guard denominators: $|A_{pp}-\theta|$ is clamped away from zero.
5. **Collapse.** If $\dim\mathcal V$ would exceed a limit, replace $\mathbf V$ by the current Ritz vectors (and $\mathbf A\mathbf V$ by $(\mathbf A\mathbf V)\mathbf T$, no new products).
6. Orthogonalize each $\mathbf q_j$ against $\mathbf V$ (twice, for safety), normalize, discard it if it is negligible, append it and its product $\mathbf A\mathbf q_j$. Return to step 2.

The cost per iteration is one product per unconverged root. All other work is $O(nm)$ vector operations and an $m\times m$ diagonalization.

## Numerical tests

!!! example "Model matrices (computed for this note)"

    $\mathbf A = \mathrm{diag}(1,2,\dots,1000)+c\,\mathbf E$, $\mathbf E$ symmetric with Gaussian entries; lowest root, residual tolerance $10^{-8}$, collapse at 40 vectors.

    | coupling $c$ | $\mathbf M = \mathbf1$ (residual) | Davidson (diagonal) | JD with diagonal $\mathbf M$ |
    |---|---|---|---|
    | 0.001 | 268 | 3 | 3 |
    | 0.1 | 334 | 8 | 8 |
    | 1 | 462 | 26 | 26 |

    Iteration counts; all final errors below $10^{-13}$. The unpreconditioned runs are slow partly because the collapse destroys the Krylov structure.

!!! example "The trap and its fix ($n = 300$, $c = 0.5$; computed for this note)"

    | update | iterations | residual norms |
    |---|---|---|
    | $\mathbf q = -(\mathbf A-\theta\mathbf1)^{-1}\mathbf r$ (exact, unprojected) | no progress in 40 | 5.6, 5.6, 5.6, … (error 0.64 at the end) |
    | Eq. [[#olsen]] with exact $\mathbf M$ | 4 | 5.6, 2.3, $4\times10^{-2}$, $8\times10^{-7}$, $4\times10^{-15}$ |
    | Davidson, diagonal $\mathbf M$ | 19 | 5.6, 2.2, 0.72, 0.35, 0.11, … |

    The exact-inverse update returns $\mathbf x$, which orthogonalization removes, so $\mathcal V$ never grows. The projected update converges cubically.

!!! example "FCI of water (computed for this note)"

    H₂O/6-31G at the HJO reference geometry, RHF orbitals, oxygen 1s frozen: 8 electrons in 12 orbitals, 495 α strings, FCI dimension 245 025. Products $\mathbf H\mathbf c$ from PySCF's string-driven $\sigma$ routine ([[determinant-strings-and-direct-ci]]); the driver is my own block Davidson, three lowest $M_S = 0$ roots, residual tolerance $10^{-6}$, collapse at 60 vectors.

    | update | iterations | $\sigma$ vectors | time |
    |---|---|---|---|
    | residual only | 38 | 114 | 23.8 s |
    | Davidson (diagonal of $\mathbf H$) | 14 | 44 | 8.3 s |
    | JD with diagonal $\mathbf M$ | 14 | 44 | 8.6 s |

    The roots are −76.121386 $E_h$ (singlet ground state), −75.844933 (a triplet, $\langle S^2\rangle = 2$) and −75.817487 (singlet). They agree with PySCF's own solver to $3\times10^{-13}$; PySCF took 10.8 s. A determinant-based $M_S = 0$ solver finds triplets too unless spin is enforced.

## Practical notes

- **Converged roots** are kept in $\mathcal V$ but get no new vectors (deflation by locking).
- **Root flipping.** If the target state is not the lowest in its symmetry, select the Ritz vector by overlap with the previous one or by its character, not by its position in the ordering.
- **Excited states of non-Hermitian matrices** (EOM-CC, [[eom-ccsd-and-size-extensivity]]) use the same scheme with left and right Ritz vectors.
- **Relation to Newton.** For a CI state, the Davidson step is HJO's quasi-Newton step with its second term dropped ([[ci-optimization-newton-and-davidson]], HJO Sec. 11.5.3); Eq. [[#olsen]] keeps it.

## Checks

`Claude outputs/part7_ch3_iterative_solvers.py`, section B (model matrices, the exact-preconditioner stall and its cure, the FCI run). Spin of the FCI roots checked with PySCF's `spin_square`.

## Source

Grotendorst, *Modern Methods and Algorithms of Quantum Chemistry* (NIC Series Vol. 3, 2nd ed., John von Neumann Institute for Computing, Jülich, 2000): chapter by B. Steffen, "Subspace Methods for Sparse Eigenvalue Problems", pp. 307-314, Sec. 3.2, pp. 311-312. Steffen cites G. L. G. Sleijpen and H. A. van der Vorst, "A Jacobi-Davidson iteration for linear eigenvalue problems" (title as Steffen gives it), *SIAM J. Matrix Anal. Appl.* **17**, 401 (1996) and E. R. Davidson, *J. Comput. Phys.* **17**, 87 (1975); neither was consulted (to verify). Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 11.5.3, Eq. (11.5.24), for the CI form of the step. The derivation of Eq. [[#olsen]] from Eq. [[#jd]] and all calculations are my own.
