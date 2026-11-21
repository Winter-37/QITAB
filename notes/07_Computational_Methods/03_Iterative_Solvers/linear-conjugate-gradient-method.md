---
id: linear-conjugate-gradient-method
title: Linear conjugate gradient method
summary: For symmetric positive definite A, solving Ax = b is minimizing φ(x) = ½xᵀAx − bᵀx. Conjugate directions give exact minimization over growing subspaces; CG generates them with a two-term recurrence from the residuals, so each step costs one product Ap and the k-th iterate minimizes the A-norm error over the Krylov space x₀ + K_k(r₀). This makes the error a polynomial problem: r distinct eigenvalues give termination in r steps, clusters cost one step each, and the condition-number bound is 2((√κ−1)/(√κ+1))^k. N&W's (5.35) as printed (exponent 2k, no factor 2) is violated by a Chebyshev-spaced spectrum; the standard bound holds. The residuals are the Lanczos vectors.
status: in-progress
kind: algorithm
level: advanced
tags: [conjugate-gradient, krylov-subspace, spd, linear-systems, conjugate-directions, chebyshev-bound, condition-number, eigenvalue-clustering]
prerequisites: [optimality-conditions-and-convergence-rates, steepest-descent-newton-and-superlinear-convergence, lanczos-and-krylov-subspaces]
related: [preconditioned-conjugate-gradient, nonlinear-conjugate-gradient, inexact-newton-and-newton-cg, cphf-closed-shell, z-vector-method]
key: kappa
order: 40
date: 2026-11-21
---

## Overview

Response calculations end in large symmetric positive definite (SPD) linear systems: CPHF ([[cphf-closed-shell]]), the Z-vector equations ([[z-vector-method]]), the Newton equations of second-order SCF. The matrix is available only through products $\mathbf A\mathbf p$, so direct factorization is out. The conjugate gradient (CG) method of Hestenes and Stiefel is the standard solver. It needs one product per step and four vectors of storage.

**Notation (N&W Ch. 5).** $\mathbf A\in\mathbb R^{n\times n}$ SPD with eigenvalues $0<\lambda_1\le\dots\le\lambda_n$ and orthonormal eigenvectors $\mathbf v_i$. The solution is $\mathbf x^*$. Define

$$
\phi(\mathbf x) = \tfrac12\mathbf x^{\mathsf T}\mathbf A\mathbf x-\mathbf b^{\mathsf T}\mathbf x,\qquad
\mathbf r(\mathbf x) = \nabla\phi = \mathbf A\mathbf x-\mathbf b,\qquad
\|\mathbf z\|_{\mathbf A}^2 = \mathbf z^{\mathsf T}\mathbf A\mathbf z .
$$

$\phi$ is strictly convex with unique minimizer $\mathbf x^*$, and $\phi(\mathbf x)-\phi(\mathbf x^*) = \frac12\|\mathbf x-\mathbf x^*\|_{\mathbf A}^2$. N&W's sign convention $\mathbf r = \mathbf A\mathbf x-\mathbf b$ is kept.

## Conjugate directions

**Definition.** Nonzero vectors $\mathbf p_0,\dots,\mathbf p_{n-1}$ are conjugate with respect to $\mathbf A$ if $\mathbf p_i^{\mathsf T}\mathbf A\mathbf p_j = 0$ for $i\ne j$. They are then linearly independent.

**Conjugate direction method.** Minimize $\phi$ exactly along each direction in turn:

$$
\mathbf x_{k+1} = \mathbf x_k+\alpha_k\mathbf p_k,\qquad \alpha_k = -\frac{\mathbf r_k^{\mathsf T}\mathbf p_k}{\mathbf p_k^{\mathsf T}\mathbf A\mathbf p_k} .
$$

**Theorem 5.1 (finite termination).** For any $\mathbf x_0$ the sequence reaches $\mathbf x^*$ in at most $n$ steps. *Reason:* expand $\mathbf x^*-\mathbf x_0 = \sum_j\sigma_j\mathbf p_j$; multiplying by $\mathbf p_k^{\mathsf T}\mathbf A$ isolates $\sigma_k = \mathbf p_k^{\mathsf T}\mathbf A(\mathbf x^*-\mathbf x_0)/\mathbf p_k^{\mathsf T}\mathbf A\mathbf p_k$. Conjugacy gives $\mathbf p_k^{\mathsf T}\mathbf A(\mathbf x_k-\mathbf x_0) = 0$, so $\sigma_k = -\mathbf p_k^{\mathsf T}\mathbf r_k/\mathbf p_k^{\mathsf T}\mathbf A\mathbf p_k = \alpha_k$.

In the eigenvector basis, conjugate directions turn $\phi$ into a sum of independent one-dimensional problems. That is why one exact line search per direction suffices.

**Theorem 5.2 (expanding subspace minimization).** For a conjugate direction sequence,

$$
\mathbf r_k^{\mathsf T}\mathbf p_i = 0\quad(i<k),
$$

and $\mathbf x_k$ minimizes $\phi$ over the whole affine set $\mathbf x_0+\mathrm{span}\{\mathbf p_0,\dots,\mathbf p_{k-1}\}$, not only along the last direction.

## The CG recurrence

**Idea.** Generate each new direction from the current residual (steepest-descent direction) and only the previous direction:

$$
\mathbf p_k = -\mathbf r_k+\beta_k\mathbf p_{k-1},\qquad
\beta_k = \frac{\mathbf r_k^{\mathsf T}\mathbf A\mathbf p_{k-1}}{\mathbf p_{k-1}^{\mathsf T}\mathbf A\mathbf p_{k-1}},
$$

which makes $\mathbf p_k$ conjugate to $\mathbf p_{k-1}$. The surprise is that it is then conjugate to *all* earlier directions.

**Theorem 5.3.** If $\mathbf x_k\ne\mathbf x^*$, then

$$
\mathbf r_k^{\mathsf T}\mathbf r_i = 0,\qquad \mathbf p_k^{\mathsf T}\mathbf A\mathbf p_i = 0\quad(i<k),
$$

$$
\mathrm{span}\{\mathbf r_0,\dots,\mathbf r_k\} = \mathrm{span}\{\mathbf p_0,\dots,\mathbf p_k\} = \mathcal K_{k+1}(\mathbf A,\mathbf r_0) = \mathrm{span}\{\mathbf r_0,\mathbf A\mathbf r_0,\dots,\mathbf A^k\mathbf r_0\} .
$$

The key step of the induction: $\mathbf A\mathbf p_i\in\mathcal K_{i+2}\subseteq\mathrm{span}\{\mathbf p_0,\dots,\mathbf p_{i+1}\}$, and $\mathbf r_{k+1}$ is orthogonal to all those $\mathbf p$'s by Theorem 5.2, so $\mathbf r_{k+1}^{\mathsf T}\mathbf A\mathbf p_i = 0$ for $i<k$ and only $\beta$ is needed to remove the last component.

**Algorithm 5.2 (CG).** Using the orthogonality relations, $\alpha_k$ and $\beta_{k+1}$ simplify:

$$
\begin{aligned}
&\mathbf r_0 = \mathbf A\mathbf x_0-\mathbf b,\quad \mathbf p_0 = -\mathbf r_0;\qquad\text{while } \mathbf r_k\ne0:\\
&\alpha_k = \frac{\mathbf r_k^{\mathsf T}\mathbf r_k}{\mathbf p_k^{\mathsf T}\mathbf A\mathbf p_k},\quad
\mathbf x_{k+1} = \mathbf x_k+\alpha_k\mathbf p_k,\quad
\mathbf r_{k+1} = \mathbf r_k+\alpha_k\mathbf A\mathbf p_k,\\
&\beta_{k+1} = \frac{\mathbf r_{k+1}^{\mathsf T}\mathbf r_{k+1}}{\mathbf r_k^{\mathsf T}\mathbf r_k},\quad
\mathbf p_{k+1} = -\mathbf r_{k+1}+\beta_{k+1}\mathbf p_k .
\end{aligned}
\label{cg}
$$

**Cost.** One product $\mathbf A\mathbf p_k$, two inner products, three vector updates per step; only the current $\mathbf x,\mathbf r,\mathbf p,\mathbf A\mathbf p$ are stored. The residual is updated by recursion; in floating point it slowly drifts from the true $\mathbf A\mathbf x_k-\mathbf b$, so a final check of the true residual is prudent.

**Relation to Lanczos.** By Theorem 5.3 the residuals are mutually orthogonal and $\mathbf r_k\in\mathcal K_{k+1}(\mathbf A,\mathbf r_0)$. So $\mathbf r_k/\|\mathbf r_k\|$ are, up to sign, the Lanczos vectors started from $\mathbf r_0/\|\mathbf r_0\|$ ([[lanczos-and-krylov-subspaces]]), and the CG coefficients determine the Lanczos tridiagonal matrix. CG is Lanczos applied to a linear system; it inherits the same loss of orthogonality in floating point, which delays convergence rather than preventing it.

## Optimality and the polynomial view

**Krylov optimality.** By Theorems 5.2 and 5.3, $\mathbf x_k$ minimizes $\|\mathbf x-\mathbf x^*\|_{\mathbf A}$ over $\mathbf x_0+\mathcal K_k(\mathbf A,\mathbf r_0)$. Every such $\mathbf x$ has $\mathbf x-\mathbf x^* = Q_k(\mathbf A)(\mathbf x_0-\mathbf x^*)$ for a polynomial $Q_k$ of degree $\le k$ with $Q_k(0) = 1$. With $\mathbf x_0-\mathbf x^* = \sum_i\xi_i\mathbf v_i$ (N&W Eqs. (5.32)-(5.33)),

$$
\|\mathbf x_k-\mathbf x^*\|_{\mathbf A}^2 = \min_{Q_k(0)=1}\ \sum_i\lambda_iQ_k(\lambda_i)^2\xi_i^2
\ \le\ \min_{Q_k(0)=1}\ \max_i Q_k(\lambda_i)^2\ \|\mathbf x_0-\mathbf x^*\|_{\mathbf A}^2 .
\label{poly}
$$

CG picks the best polynomial automatically, adapted to the actual spectrum and right-hand side. Three consequences follow by choosing good polynomials.

**Theorem 5.4 (distinct eigenvalues).** If $\mathbf A$ has only $r$ distinct eigenvalues $\tau_1,\dots,\tau_r$, CG terminates in at most $r$ steps. Take $Q_r(\lambda) = \prod_j(1-\lambda/\tau_j)$, which vanishes on the spectrum.

**Theorem 5.5 (large outliers; Luenberger).**

$$
\|\mathbf x_{k+1}-\mathbf x^*\|_{\mathbf A}\le\frac{\lambda_{n-k}-\lambda_1}{\lambda_{n-k}+\lambda_1}\,\|\mathbf x_0-\mathbf x^*\|_{\mathbf A} .
$$

The polynomial has roots at the $k$ largest eigenvalues and at the midpoint of $[\lambda_1,\lambda_{n-k}]$. After $m+1$ steps, $m$ large outlying eigenvalues no longer matter; what is left is the condition number of the cluster.

**Condition-number bound.** Use only $\lambda\in[\lambda_1,\lambda_n]$ and $\kappa = \lambda_n/\lambda_1$. The best polynomial on an interval is a shifted Chebyshev polynomial,

$$
Q_k(\lambda) = \frac{T_k\!\big((\lambda_n+\lambda_1-2\lambda)/(\lambda_n-\lambda_1)\big)}{T_k\!\big((\kappa+1)/(\kappa-1)\big)},\qquad
\max_{[\lambda_1,\lambda_n]}|Q_k| = \frac1{T_k\!\big(\frac{\kappa+1}{\kappa-1}\big)} .
$$

With $T_k(z) = \frac12[(z+\sqrt{z^2-1})^k+(z-\sqrt{z^2-1})^k]\ge\frac12(z+\sqrt{z^2-1})^k$ and $z+\sqrt{z^2-1} = (\sqrt\kappa+1)/(\sqrt\kappa-1)$ for $z = (\kappa+1)/(\kappa-1)$:

$$
\|\mathbf x_k-\mathbf x^*\|_{\mathbf A}\le2\left(\frac{\sqrt\kappa-1}{\sqrt\kappa+1}\right)^{k}\|\mathbf x_0-\mathbf x^*\|_{\mathbf A} .
\label{kappa}
$$

The number of iterations for a fixed reduction grows like $\sqrt\kappa$; for steepest descent it grows like $\kappa$, since its factor per step in the $\mathbf A$-norm is $(\kappa-1)/(\kappa+1)$ ([[steepest-descent-newton-and-superlinear-convergence]]).

**The printed (5.35).** N&W (1st ed., p. 117) print $\|\mathbf x_k-\mathbf x^*\|_{\mathbf A}\le\big((\sqrt\kappa-1)/(\sqrt\kappa+1)\big)^{2k}\|\mathbf x_0-\mathbf x^*\|_{\mathbf A}$: exponent $2k$ and no factor 2. That is too strong. A spectrum placed at the Chebyshev points of $[1,\kappa]$, for which Eq. [[#kappa]] is nearly attained, violates it at every $k$ (table below). It is violated even if both norms are read as squared. Eq. [[#kappa]], the standard form, holds throughout.

## Numerical tests

!!! example "Spectrum shapes ($n = 1000$; computed for this note)"

    $\|\mathbf e_k\|_{\mathbf A}/\|\mathbf e_0\|_{\mathbf A}$, random rotation, random $\mathbf b$, $\mathbf x_0 = 0$:

    | spectrum | iterations to $\|\mathbf r\|/\|\mathbf b\|<10^{-12}$ | error after 4, 5, 6, 7, 8, 9 steps |
    |---|---|---|
    | 995 eigenvalues in $1\pm0.05$, plus 10, 20, 40, 60, 80 | 18 | 0.039, 0.028, 0.023, $5.8\times10^{-4}$, $1.4\times10^{-5}$, $3.6\times10^{-7}$ |
    | 1000 eigenvalues uniform in $[1,80]$ | 113 | 0.32, 0.25, 0.20, 0.16, 0.13, 0.10 |

    Both have $\kappa\approx80$; the clustered one converges six times faster. Theorem 5.5 predicts $\le(\lambda_{n-5}-\lambda_1)/(\lambda_{n-5}+\lambda_1)\approx0.05$ after six steps; observed 0.023.

    Four distinct eigenvalues (1, 3, 7, 15, each 250 times): $\|\mathbf r_4\|/\|\mathbf b\| = 3.9\times10^{-14}$, i.e. termination after 4 steps (Theorem 5.4). Krylov optimality ($n = 30$, $k = 5$): $\mathbf x_5$ agrees with the explicit minimizer of $\|\mathbf x-\mathbf x^*\|_{\mathbf A}$ over $\mathcal K_5$ to $4\times10^{-15}$.

!!! example "The $\kappa$ bound ($n = 2000$, eigenvalues at Chebyshev points of $[1,\kappa]$; computed for this note)"

    $q = (\sqrt\kappa-1)/(\sqrt\kappa+1)$.

    | $\kappa$ | $k$ | measured | $2q^k$ (Eq. [[#kappa]]) | $q^{2k}$ (printed (5.35)) |
    |---|---|---|---|---|
    | 100 | 10 | 0.188 | 0.269 | 0.018 |
    | 100 | 40 | $4.62\times10^{-4}$ | $6.53\times10^{-4}$ | $1.1\times10^{-7}$ |
    | $10^4$ | 100 | 0.190 | 0.271 | 0.018 |
    | $10^4$ | 200 | $2.59\times10^{-2}$ | $3.66\times10^{-2}$ | $3.4\times10^{-4}$ |

    The measured ratio stays at about 0.7 of $2q^k$, so Eq. [[#kappa]] is close to sharp for this spectrum. For $\kappa = 100$, a $10^{-6}$ reduction needs about 691 steepest-descent steps by its rate and 72 CG steps by Eq. [[#kappa]].

## Checks

`Claude outputs/part7_ch3_iterative_solvers.py`, section C.

## Source

Nocedal and Wright, *Numerical Optimization* (Springer, New York, 1999), Ch. 5, Sec. 5.1, pp. 102-117: conjugate directions and Theorem 5.1 (pp. 102-104), Theorem 5.2 (p. 106), Theorem 5.3 and Algorithm 5.2 (pp. 108-111), Eqs. (5.32)-(5.35) and Theorems 5.4-5.5 (pp. 113-117). The Chebyshev derivation of Eq. [[#kappa]], the Lanczos connection and all numerical tests were written and computed for this note.
