---
id: rayleigh-ritz-and-harmonic-ritz
title: Extracting eigenpairs from a subspace - Rayleigh–Ritz, harmonic Ritz and residual minimization
summary: A subspace method for a few eigenpairs of a large symmetric A alternates two steps, extraction (best approximations inside a subspace V) and update (enlarging V). Rayleigh–Ritz diagonalizes WᵀAW and is near optimal for extremal eigenpairs, with eigenvalue bounds from the min–max principle and the residual. For interior eigenpairs it can fail even when V contains a good vector. Harmonic Ritz (Petrov–Galerkin with test space (A − σ1)V) and linearized residual minimization fix this. Steffen's Examples 1 and 2 and his residual-minimization vector reproduced; his harmonic-Ritz numbers could not be, and a 200-dimensional test shows what harmonic Ritz does.
status: in-progress
kind: theory
level: advanced
tags: [subspace-methods, rayleigh-ritz, ritz-values, harmonic-ritz, interior-eigenvalues, residual-minimization, petrov-galerkin, eigenvalue-bounds]
prerequisites: [matrix-eigenvalue-problem, floating-point-and-eigenvalue-perturbation, variational-principle]
related: [lanczos-and-krylov-subspaces, davidson-and-jacobi-davidson-methods, ci-optimization-newton-and-davidson, cholesky-and-generalized-eigenproblem]
key: ritz
order: 10
date: 2026-11-21
---

## Overview

Large CI, EOM and response problems need a few eigenpairs of a symmetric matrix $\mathbf A\in\mathbb R^{n\times n}$ with $n$ in the millions or more. $\mathbf A$ is never stored. A program can only form products $\mathbf A\mathbf v$ (for CI: the $\sigma$ vector, [[determinant-strings-and-direct-ci]]).

A **subspace method** (Steffen Sec. 1) keeps a low-dimensional subspace $\mathcal V\subset\mathbb R^n$ and repeats two steps.

1. **Extraction.** Find the best approximations to the wanted eigenpairs *inside* $\mathcal V$, using only $\mathbf A\mathbf V$.
2. **Update.** Add new directions to $\mathcal V$, and sometimes remove old ones (a *restart* or *collapse*).

The methods of this chapter differ mainly in the update: Krylov directions $\mathbf A\mathbf v$ ([[lanczos-and-krylov-subspaces]]) or preconditioned residuals ([[davidson-and-jacobi-davidson-methods]]). This note is about extraction, which is common to all of them.

**Notation.** $\mathbf A$ is symmetric with eigenpairs $(\lambda_k,\mathbf u_k)$, $\lambda_1\le\dots\le\lambda_n$. $\mathbf W\in\mathbb R^{n\times m}$ has orthonormal columns spanning $\mathcal V$, $m\ll n$. For a unit vector $\mathbf x$, $\rho(\mathbf x) = \mathbf x^{\mathsf T}\mathbf A\mathbf x$ is its Rayleigh quotient and $\mathbf r = \mathbf A\mathbf x-\rho\mathbf x$ its residual.

## Rayleigh–Ritz

**Definition.** Form the projected matrix and diagonalize it:

$$
\mathbf S = \mathbf W^{\mathsf T}\mathbf A\mathbf W\in\mathbb R^{m\times m},\qquad \mathbf S\mathbf t_j = \theta_j\mathbf t_j,\qquad \mathbf x_j = \mathbf W\mathbf t_j .
\label{ritz}
$$

The $\theta_j$ are the **Ritz values** and the $\mathbf x_j$ the **Ritz vectors**. Each $\mathbf x_j$ is a unit vector with $\rho(\mathbf x_j) = \theta_j$.

**Galerkin condition.** Eq. [[#ritz]] is equivalent to

$$
\mathbf A\mathbf x_j-\theta_j\mathbf x_j\;\perp\;\mathcal V,\qquad \mathbf x_j\in\mathcal V,
$$

since $\mathbf W^{\mathsf T}(\mathbf A\mathbf W\mathbf t_j-\theta_j\mathbf W\mathbf t_j) = (\mathbf S-\theta_j)\mathbf t_j = 0$. The residual is orthogonal to the whole subspace. Any eigenvector of $\mathbf A$ that lies in $\mathcal V$ is reproduced exactly.

**Extremal eigenvalues: bounds.** The min–max (Courant–Fischer) characterization of the eigenvalues of $\mathbf A$ and of $\mathbf S$ gives

$$
\lambda_j\le\theta_j\le\lambda_{n-m+j},\qquad j = 1,\dots,m .
\label{interlace}
$$

In particular $\theta_1\ge\lambda_1$: the lowest Ritz value is an upper bound to the lowest eigenvalue. This is the matrix form of the variational principle ([[variational-principle]]), and it is why the lowest Ritz values decrease monotonically when $\mathcal V$ is enlarged.

**Residual bound.** For any unit $\mathbf x$ and any number $\theta$, expand $\mathbf x = \sum_kc_k\mathbf u_k$. Then

$$
\|\mathbf A\mathbf x-\theta\mathbf x\|^2 = \sum_k(\lambda_k-\theta)^2c_k^2\ \ge\ \min_k(\lambda_k-\theta)^2,
$$

so some eigenvalue lies within $\|\mathbf r\|$ of $\theta$. The residual norm is therefore the natural convergence test. It costs nothing extra, since $\mathbf A\mathbf x_j = (\mathbf A\mathbf W)\mathbf t_j$ is a combination of stored vectors.

**Accuracy.** If the Ritz vector has angle $\phi$ to the eigenvector $\mathbf u_k$, the Ritz value error is $O(\sin^2\phi)$. This is the usual variational doubling: eigenvalues converge twice as fast (in digits) as eigenvectors.

## When Rayleigh–Ritz fails: interior eigenpairs

For hermitian $\mathbf A$ the Ritz vectors are forced to be mutually orthogonal, but the projections of the eigenvectors of $\mathbf A$ onto $\mathcal V$ are not. The Ritz vector of an extremal Ritz value can be a mixture of several eigenvectors, and every other Ritz vector must be orthogonal to it. An interior eigenvector can therefore be badly represented by its Ritz vector even when $\mathcal V$ contains a very good approximation to it (Steffen Sec. 2.1).

!!! example "Steffen's Examples 1 and 2 (recomputed)"

    $\mathbf A = \mathrm{diag}(-1000,4,5,6)$.

    **Example 1.** $\mathcal V = \mathrm{span}\{(0.001,0.1,0,1),\ (-0.005,-1,1,0.001)\}$ contains a good approximation to $\mathbf e_4$ (eigenvalue 6, the largest). The Ritz values are 4.486435 and 5.992931. The Ritz vector of the larger one is $(0.00066,0.03205,0.06767,0.99719)$, as Steffen states. The best approximation to $\mathbf e_4$ in $\mathcal V$ (its orthogonal projection) is $(0.00075,0.04987,0.04988,0.99751)$. Rayleigh–Ritz is near optimal here.

    **Example 2.** Exchange the last two components of both basis vectors. Now $\mathcal V$ contains a good approximation to the *interior* eigenvector $\mathbf e_3$: its projection onto $\mathcal V$ is $(0.0007,0.0499,0.9975,0.0499)$, only $4.0°$ away. The Ritz values are 4.919947 and 5.066825. The Ritz vector of the value near 5 is $(-0.0018,-0.4423,0.7338,0.5156)$, $42.8°$ from $\mathbf e_3$ ("almost 43°", Steffen), even though its Ritz value 4.92 is good. The large component $-1000$ pulls the Ritz pair of the lowest value into a mixture, and the other Ritz vector must be orthogonal to it.

## Harmonic Ritz

**Idea (Steffen Sec. 2.2).** Eigenvalues of $\mathbf A$ near a target $\sigma$ become the extremal eigenvalues of $(\mathbf A-\sigma\mathbf1)^{-1}$. Apply Rayleigh–Ritz to $(\mathbf A-\sigma\mathbf1)^{-1}$ on the space $\mathcal W = (\mathbf A-\sigma\mathbf1)\mathcal V$. No inverse is needed: $(\mathbf A-\sigma\mathbf1)^{-1}$ maps $\mathcal W$ back onto $\mathcal V$, whose image under $\mathbf A$ is already known.

**Equations.** Write a trial vector as $\mathbf x = \mathbf V\mathbf y$ and set $\mathbf Z = (\mathbf A-\sigma\mathbf1)\mathbf V$. The Galerkin condition for $(\mathbf A-\sigma\mathbf1)^{-1}$ on $\mathcal W$, with eigenvalue $\mu = 1/(\theta-\sigma)$, reads $\mathbf Z^{\mathsf T}(\mathbf V\mathbf y-\mu\mathbf Z\mathbf y) = 0$:

$$
\mathbf Z^{\mathsf T}\mathbf V\,\mathbf y = \mu\,\mathbf Z^{\mathsf T}\mathbf Z\,\mathbf y,\qquad \theta = \sigma+1/\mu .
\label{harmonic}
$$

Equivalently $\mathbf A\mathbf x-\theta\mathbf x\perp(\mathbf A-\sigma\mathbf1)\mathcal V$: a Petrov–Galerkin condition, with test space different from the trial space. The $\theta$ are the **harmonic Ritz values**. The wanted pair is the one with the largest $|\mu|$, that is, $\theta$ closest to $\sigma$. Both matrices in Eq. [[#harmonic]] are $m\times m$ and need only $\mathbf A\mathbf V$, so the extra cost is marginal.

**Why it helps.** A harmonic Ritz value cannot sit close to $\sigma$ by accident. Since $1/(\theta-\sigma)$ is a Ritz value of $(\mathbf A-\sigma\mathbf1)^{-1}$, it is bounded by the extreme eigenvalues of that matrix, which come from the eigenvalues of $\mathbf A$ nearest $\sigma$. Ordinary Ritz values near $\sigma$ can be spurious mixtures of eigenvalues on both sides of $\sigma$, as in Example 2.

!!! example "Harmonic Ritz on an interior eigenvector (computed for this note)"

    $\mathbf A$ is a random orthogonal rotation of $\mathrm{diag}(1,2,\dots,200)$. The target is $\mathbf u_{100}$ (eigenvalue 100), with $\sigma = 100.3$. $\mathcal V$ holds $\mathbf u_{100}$ plus noise of relative size 0.05, and 9 random vectors. Over 200 random trials:

    | method | median angle to $\mathbf u_{100}$ | worst angle |
    |---|---|---|
    | best vector in $\mathcal V$ (projection) | 2.79° | |
    | Rayleigh–Ritz, pair nearest $\sigma$ | 8.98° | 84.2° |
    | harmonic Ritz, largest $\lvert\mu\rvert$ | 2.86° | 3.2° |

    The Ritz vector is worse than 10° in 46% of the trials; harmonic Ritz is never worse than 3.2° and nearly matches the best possible vector.

**Steffen's numbers.** For Example 2, Steffen reports $(0.0017,0.2390,0.9605,-0.1429)$ at $\sigma = 4.9$ and $(0.0013,0.1630,0.9845,-0.0646)$ at $\sigma = 4.995$. Solving Eq. [[#harmonic]] gives harmonic Ritz values 5.374 and 6.396 (closest to $\sigma$) with vectors 11.9° and 12.2° from $\mathbf e_3$, not his vectors. The second root at $\sigma = 4.995$, $(0.0016,0.2323,0.9631,-0.1360)$, is close to his $\sigma = 4.9$ vector. In this tiny example the $0.001$ component along the eigenvalue $-1000$ is amplified about 1000 times in $(\mathbf A-\sigma\mathbf1)\mathbf V$ and dominates $\mathcal W$, so the result is very sensitive to the exact variant used. **To verify:** which variant Steffen computed.

## Residual minimization

**When to use it.** Sometimes a good approximate eigenvector $\bar{\mathbf v}\in\mathcal V$ is known (from a cheaper calculation, or the previous iteration), but its eigenvalue is not known well enough to choose $\sigma$.

**Definition (Steffen Sec. 2.2).** Choose the $\mathbf x\in\mathcal V$ closest to $\bar{\mathbf v}$ that locally minimizes $\|(\mathbf A-\rho(\mathbf x)\mathbf1)\mathbf x\|$, among vectors with $\cos\angle(\mathbf x,\bar{\mathbf v})>\alpha$. Steffen recommends $\alpha>0.9$, with $1/\sqrt2$ the theoretical lower limit. This is a small nonlinear problem in $m$ variables.

**Linearization.** Freeze the Rayleigh quotient at $\bar\rho = \bar{\mathbf v}^{\mathsf T}\mathbf A\bar{\mathbf v}$ and minimize over corrections orthogonal to $\bar{\mathbf v}$:

$$
\min_{\mathbf x\in\mathcal V,\ \mathbf x\perp\bar{\mathbf v}}\ \|(\mathbf A-\bar\rho\mathbf1)(\bar{\mathbf v}+\mathbf x)\| .
$$

This is a linear least-squares problem of dimension $m-1$.

**Example 2 again.** With $\bar{\mathbf v}$ the first basis vector ($\bar\rho = 4.9891$), the linearized problem gives $(0.00006,-0.08685,0.97894,0.18473)$. Steffen gives $(0.00006,-0.0861,0.9791,0.1840)$, which agrees to about $10^{-3}$. Steffen's assessment: residual minimization is more robust than harmonic Ritz and good for starting steps, while harmonic Ritz is usually better in final convergence.

## Implementation: no explicit orthonormalization

Eq. [[#ritz]] needs an orthonormal basis, but the basis need not be formed (Steffen Sec. 4). Let $\mathbf V$ be any basis of $\mathcal V$, $\mathbf F = \mathbf V^{\mathsf T}\mathbf V = \mathbf C\mathbf C^{\mathsf T}$ its Cholesky factorization ([[cholesky-and-generalized-eigenproblem]]), and $\mathbf R = \mathbf C^{-\mathsf T}$. Then $\mathbf W = \mathbf V\mathbf R$ is orthonormal and

$$
\mathbf S = \mathbf R^{\mathsf T}\,(\mathbf A\mathbf V)^{\mathsf T}\mathbf V\,\mathbf R .
$$

Only $\mathbf V^{\mathsf T}\mathbf V$ and $\mathbf V^{\mathsf T}\mathbf A\mathbf V$ are formed in $n$ dimensions; the Ritz vectors are $\mathbf V(\mathbf R\mathbf T)$. This saves about half the work of Gram–Schmidt (checked: the eigenvalues equal those of $\mathbf Q^{\mathsf T}\mathbf A\mathbf Q$ for a random $50\times5$ case).

**The catch.** Rayleigh–Ritz is sensitive to loss of orthogonality, and the Cholesky route is numerically like classical Gram–Schmidt. A nearly dependent new vector must be removed or replaced; at a restart, explicit orthogonalization may pay.

## Checks

All numbers above are produced by `Claude outputs/part7_ch3_iterative_solvers.py`, section A.

- Examples 1 and 2: Ritz values and vectors as printed by Steffen; the 42.8° angle.
- Residual minimization: agreement with Steffen to about $10^{-3}$.
- Harmonic Ritz: the 200-trial test; Steffen's own numbers not reproduced (see above).

## Source

Grotendorst, *Modern Methods and Algorithms of Quantum Chemistry* (NIC Series Vol. 3, 2nd ed., John von Neumann Institute for Computing, Jülich, 2000): chapter by B. Steffen, "Subspace Methods for Sparse Eigenvalue Problems", pp. 307-314, Secs. 1, 2.1, 2.2 and 4 (Examples 1 and 2, p. 309). The bounds Eq. [[#interlace]], the residual bound and the 200-dimensional harmonic Ritz test are standard results derived or computed for this note.
