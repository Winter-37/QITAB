---
id: lanczos-and-krylov-subspaces
title: Krylov subspaces and the Lanczos method
summary: The Krylov subspace K_m(A, q) = span{q, Aq, …, A^{m−1}q} is built from matrix–vector products only. For symmetric A an orthonormal basis follows from a three-term recurrence, and the projected matrix is tridiagonal, so Rayleigh–Ritz on a Krylov space costs almost nothing beyond the products. Extremal eigenvalues converge first and fastest when well separated. In finite precision the Lanczos vectors lose orthogonality as soon as a Ritz pair converges, and converged eigenvalues reappear as copies ("ghosts"); full reorthogonalization removes them. Demonstrated on a 400-dimensional matrix.
status: in-progress
kind: algorithm
level: advanced
tags: [krylov-subspace, lanczos, three-term-recurrence, tridiagonal, ghost-eigenvalues, reorthogonalization, arnoldi]
prerequisites: [rayleigh-ritz-and-harmonic-ritz, tridiagonal-qr-iteration]
related: [davidson-and-jacobi-davidson-methods, linear-conjugate-gradient-method, householder-tridiagonalization, choosing-a-symmetric-eigensolver]
key: lanczos
order: 20
date: 2026-11-21
---

## Overview

The simplest sequence of subspaces adds $\mathbf A$ times the last vector (Steffen Sec. 3.1):

$$
\mathcal K_m(\mathbf A,\mathbf q_1) = \mathrm{span}\{\mathbf q_1,\mathbf A\mathbf q_1,\dots,\mathbf A^{m-1}\mathbf q_1\} .
$$

This is the **Krylov subspace**. Every vector in it has the form $p(\mathbf A)\mathbf q_1$ with $p$ a polynomial of degree less than $m$. Steffen calls the Lanczos (symmetric) and Arnoldi (nonsymmetric) methods built on it about the best possible black-box solvers for a few extreme eigenvalues. The same space underlies the conjugate gradient method for linear systems ([[linear-conjugate-gradient-method]]).

## The three-term recurrence

**Construction.** Let $\mathbf A$ be symmetric and $\mathbf q_1$ a unit vector. Orthonormalize $\mathbf A\mathbf q_j$ against the previous vectors:

$$
\beta_j\mathbf q_{j+1} = \mathbf A\mathbf q_j-\alpha_j\mathbf q_j-\beta_{j-1}\mathbf q_{j-1},\qquad \alpha_j = \mathbf q_j^{\mathsf T}\mathbf A\mathbf q_j,\quad \beta_j = \|\cdot\| ,
\label{lanczos}
$$

with $\beta_0\mathbf q_0 = 0$.

**Why only three terms.** By construction $\mathbf q_k\in\mathcal K_k$, so $\mathbf A\mathbf q_k\in\mathcal K_{k+1}$. For $k\le j-2$,

$$
\mathbf q_k^{\mathsf T}(\mathbf A\mathbf q_j) = \mathbf q_j^{\mathsf T}(\mathbf A\mathbf q_k) = 0,
$$

because $\mathbf A\mathbf q_k\in\mathcal K_{k+1}\subseteq\mathcal K_{j-1}\perp\mathbf q_j$. The first equality is the symmetry of $\mathbf A$; for a nonsymmetric matrix it fails and all earlier vectors are needed (the Arnoldi method, with a Hessenberg projected matrix). So $\mathbf A\mathbf q_j$ has components only along $\mathbf q_{j-1},\mathbf q_j,\mathbf q_{j+1}$, and the Gram–Schmidt step against all earlier vectors reduces to Eq. [[#lanczos]].

**Matrix form.** With $\mathbf Q_m = [\mathbf q_1,\dots,\mathbf q_m]$,

$$
\mathbf A\mathbf Q_m = \mathbf Q_m\mathbf T_m+\beta_m\mathbf q_{m+1}\mathbf e_m^{\mathsf T},\qquad
\mathbf T_m = \begin{pmatrix}\alpha_1&\beta_1&&\\ \beta_1&\alpha_2&\ddots&\\ &\ddots&\ddots&\beta_{m-1}\\ &&\beta_{m-1}&\alpha_m\end{pmatrix}
= \mathbf Q_m^{\mathsf T}\mathbf A\mathbf Q_m .
\label{lanczos-matrix}
$$

**Rayleigh–Ritz for free.** The projected matrix of [[rayleigh-ritz-and-harmonic-ritz]] is the tridiagonal $\mathbf T_m$. Its eigenvalues cost $O(m^2)$ with the tridiagonal eigensolvers of Chapter 1 ([[tridiagonal-qr-iteration]], [[bisection-and-inverse-iteration]]).

**Residuals without the vectors.** If $\mathbf T_m\mathbf t = \theta\mathbf t$ and $\mathbf x = \mathbf Q_m\mathbf t$, Eq. [[#lanczos-matrix]] gives

$$
\|\mathbf A\mathbf x-\theta\mathbf x\| = \beta_m\,|t_m| ,
$$

the last component of $\mathbf t$ times $\beta_m$. Convergence can be monitored without forming any Ritz vector.

**Cost and storage.** One product $\mathbf A\mathbf q_j$ and two vector updates per step. Eigenvalues alone need only the last two Lanczos vectors. Eigenvectors need all of $\mathbf Q_m$, or a second pass that regenerates it (Steffen).

**Lanczos is the Householder tridiagonalization done by products.** If run for $n$ steps in exact arithmetic, Eq. [[#lanczos-matrix]] is an orthogonal reduction $\mathbf Q^{\mathsf T}\mathbf A\mathbf Q = \mathbf T$, the same form as [[householder-tridiagonalization]], with $\mathbf Q\mathbf e_1 = \mathbf q_1$.

## Convergence

**Polynomial view.** The Ritz value $\theta_m^{\max}$ maximizes the Rayleigh quotient over $\mathcal K_m$, that is, over all $p(\mathbf A)\mathbf q_1$ with $\deg p<m$. A polynomial that is large at $\lambda_n$ and small on $[\lambda_1,\lambda_{n-1}]$ exists with modest degree when $\lambda_n$ is separated from the rest. Extremal, well-separated eigenvalues therefore converge first; interior and clustered ones last. The optimal polynomials are Chebyshev polynomials, as in the CG error bound ([[linear-conjugate-gradient-method]]).

!!! example "Convergence of the top Ritz values (computed for this note)"

    $n = 400$; 397 eigenvalues spread over $[0,1]$ plus $1.2$, $1.5$, $2.0$; random rotation; random $\mathbf q_1$; full reorthogonalization.

    | $m$ | error in 2.0 | error in 1.5 | error in 1.2 |
    |---|---|---|---|
    | 5 | $4.5\times10^{-2}$ | 0.56 | 0.54 |
    | 10 | $4.3\times10^{-7}$ | $9.6\times10^{-2}$ | $1.7\times10^{-2}$ |
    | 20 | 0 | 0 | $3.8\times10^{-10}$ |

    $\mathbf Q_{60}^{\mathsf T}\mathbf A\mathbf Q_{60}$ equals $\mathbf T_{60}$ to $10^{-10}$. The isolated largest eigenvalue converges first. After 20 products, three eigenvalues are exact to machine precision, out of 400.

## Loss of orthogonality and ghost eigenvalues

**What goes wrong.** In floating point the recurrence Eq. [[#lanczos]] does not keep $\mathbf q_{j+1}$ orthogonal to old vectors. The loss is not gradual: it grows quickly once a Ritz pair has converged, along the direction of that converged Ritz vector. The Krylov process then "rediscovers" the eigenvector and $\mathbf T_m$ acquires extra copies of the converged eigenvalue.

!!! example "Ghosts (computed for this note)"

    Same matrix, $m = 120$, plain recurrence without reorthogonalization. $\mathbf T_{120}$ has the Ritz values above 1.9:

    $$1.95017,\ 2.00000,\ 2.00000,\ 2.00000,\ 2.00000,\ 2.00000.$$

    The eigenvalue 2.0 (multiplicity one) appears five times, and $\max_{i\ne j}|\mathbf q_i^{\mathsf T}\mathbf q_j| = 0.67$. The value 1.95017 is not an eigenvalue of $\mathbf A$: it is the next copy forming. The number of copies grows with $m$: four at $m = 100$ (plus one at 1.999999), six at $m = 140$, seven at $m = 160$.

**Remedies.** Full reorthogonalization against all previous $\mathbf q_k$ (used in the example above, cost $O(nm)$ per step) removes the ghosts. Selective or partial reorthogonalization, or detecting and discarding the copies afterwards, are cheaper. Steffen notes that these stability problems "can be dealt with nicely" and points to Cullum and Willoughby and to ARPACK (implicitly restarted Arnoldi) for careful implementations; those are not treated here.

## Other Krylov-type updates

- **Block methods.** Starting from several vectors finds multiple or clustered eigenvalues more reliably.
- **Simultaneous iteration.** $\mathcal V^{(k+1)} = \mathrm{span}\{\mathbf A\mathbf w_1^{(k)},\dots,\mathbf A\mathbf w_m^{(k)}\}$ keeps the dimension fixed, which saves memory and helps stability, but converges only to the largest eigenvalues. Chebyshev acceleration replaces $\mathbf A$ by a polynomial $P(\mathbf A)$ (Steffen Sec. 3.1).
- **Shift-and-invert.** Krylov on $(\mathbf A-\sigma\mathbf1)^{-1}$ makes interior eigenvalues extremal, but needs a factorization or an accurate linear solve at each step, which is rarely affordable for CI matrices.
- **Preconditioned updates.** Adding approximate solutions of correction equations instead of $\mathbf A\mathbf q$ gives Davidson-type methods ([[davidson-and-jacobi-davidson-methods]]). They lose the three-term recurrence but converge in far fewer products for diagonally dominant matrices.

## Checks

`Claude outputs/part7_ch3_iterative_solvers.py`, section A: tridiagonality of $\mathbf Q^{\mathsf T}\mathbf A\mathbf Q$, the convergence table, and the ghost copies without reorthogonalization.

## Source

Grotendorst, *Modern Methods and Algorithms of Quantum Chemistry* (NIC Series Vol. 3, 2nd ed., John von Neumann Institute for Computing, Jülich, 2000): chapter by B. Steffen, "Subspace Methods for Sparse Eigenvalue Problems", pp. 307-314, Sec. 3.1, pp. 310-311. Steffen describes Lanczos only in outline; the derivation of the recurrence, the residual formula and the numerical examples were written and computed for this note. Detailed treatments (Cullum–Willoughby, Parlett) are cited by Steffen but were not consulted.
