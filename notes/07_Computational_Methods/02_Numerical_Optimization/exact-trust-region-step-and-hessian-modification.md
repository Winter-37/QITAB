---
id: exact-trust-region-step-and-hessian-modification
title: Indefinite Hessians - the exact trust-region step, the hard case, and Hessian modification
summary: The global minimizer of a quadratic model in a ball satisfies (B + λ1)p = −g, λ(Δ − ‖p‖) = 0, B + λ1 positive semidefinite (Thm. 4.3). So the step is a level-shifted Newton step with λ ≥ max(0, −λ₁), found by a safeguarded Newton iteration on 1/Δ − 1/‖p(λ)‖ (Algorithm 4.4), with a separate formula in the hard case. Line-search Newton methods instead modify an indefinite Hessian before solving: eigenvalue replacement, adding τ1, or modified Cholesky. Worked on diag(−2, 1, 3) and on N&W's diag(10, 3, −1) example.
status: in-progress
kind: derivation
level: advanced
tags: [trust-region-subproblem, level-shift, more-sorensen, hard-case, hessian-modification, negative-curvature, modified-cholesky, levenberg-marquardt]
prerequisites: [trust-region-methods, cholesky-and-generalized-eigenproblem]
related: [mcscf-trust-region-and-augmented-hessian, scf-second-order-and-stability, inexact-newton-and-newton-cg, stationary-points-and-reaction-paths]
key: tr-kkt
order: 50
date: 2026-11-21
---

## Overview

Far from a minimizer the exact Hessian is often indefinite. On a potential energy surface this happens near a transition state; in MCSCF, for a poor starting guess. The pure Newton step is then useless: it may point uphill or toward a saddle. There are two remedies, and they lead to the same matrix $\mathbf B+\lambda\mathbf 1$:

- a trust region, which bounds the step and solves the bounded problem exactly;
- a modification of the Hessian before the line search.

## Characterization of the exact step

**Theorem 4.3.** $\mathbf p^*$ is a global solution of $\min m(\mathbf p) = f+\mathbf g^{\mathsf T}\mathbf p+\tfrac12\mathbf p^{\mathsf T}\mathbf B\mathbf p$ subject to $\|\mathbf p\|\le\Delta$ if and only if $\|\mathbf p^*\|\le\Delta$ and there is a scalar $\lambda\ge0$ with

$$
(\mathbf B+\lambda\mathbf 1)\,\mathbf p^* = -\mathbf g,\qquad
\lambda\,(\Delta-\|\mathbf p^*\|) = 0,\qquad
\mathbf B+\lambda\mathbf 1\ \text{positive semidefinite}.
\label{tr-kkt}
$$

So there are two possibilities:

- either $\lambda = 0$: $\mathbf B$ is PSD and the Newton step lies inside the ball;
- or the step lies on the boundary and is a **level-shifted Newton step** with $\lambda\ge\max(0,-\lambda_1)$, where $\lambda_1$ is the smallest eigenvalue of $\mathbf B$.

The global solution is found without any search over local minima. N&W prove this from Lemma 4.4, which shows that $m$ is minimized globally along any feasible direction under Eq. [[#tr-kkt]].

The $\lambda>0$ solutions for varying $\Delta$ trace the Levenberg–Marquardt trajectory. HJO's level-shifted Newton step for MCSCF, $(\mathbf E^{(2)}-\mu\mathbf 1)\mathbf P\boldsymbol\lambda = -\mathbf E^{(1)}$, is Eq. [[#tr-kkt]] with $\mu = -\lambda$ ([[mcscf-trust-region-and-augmented-hessian]]).

## Finding λ (Algorithm 4.4)

Write $\mathbf B = \mathbf Q\boldsymbol\Lambda\mathbf Q^{\mathsf T}$ with eigenpairs $(\lambda_j,\mathbf q_j)$. Then

$$
\mathbf p(\lambda) = -\sum_j\frac{\mathbf q_j^{\mathsf T}\mathbf g}{\lambda_j+\lambda}\mathbf q_j,\qquad
\|\mathbf p(\lambda)\|^2 = \sum_j\frac{(\mathbf q_j^{\mathsf T}\mathbf g)^2}{(\lambda_j+\lambda)^2}.
\label{plam}
$$

On $(-\lambda_1,\infty)$, $\|\mathbf p(\lambda)\|$ decreases from $+\infty$ (if $\mathbf q_1^{\mathsf T}\mathbf g\ne0$) to 0, so $\|\mathbf p(\lambda)\| = \Delta$ has exactly one root there.

Applying Newton's method to $\|\mathbf p(\lambda)\|-\Delta$ would be poor, because the function behaves like $C/(\lambda+\lambda_1)$ near the pole. The reciprocal form

$$
\phi_2(\lambda) = \frac1\Delta-\frac1{\|\mathbf p(\lambda)\|}
$$

is almost linear there, so Newton's method works well on it. With the Cholesky factor $\mathbf B+\lambda^{(\ell)}\mathbf 1 = \mathbf R^{\mathsf T}\mathbf R$, solve $\mathbf R^{\mathsf T}\mathbf R\,\mathbf p_\ell = -\mathbf g$ and $\mathbf R^{\mathsf T}\mathbf q_\ell = \mathbf p_\ell$. The Newton update is

$$
\lambda^{(\ell+1)} = \lambda^{(\ell)}+\Big(\frac{\|\mathbf p_\ell\|}{\|\mathbf q_\ell\|}\Big)^2\frac{\|\mathbf p_\ell\|-\Delta}{\Delta}.
\label{newton-lam}
$$

Each iteration costs one Cholesky factorization ([[cholesky-and-generalized-eigenproblem]]). The factorization failing signals $\lambda<-\lambda_1$, which practical codes use as a safeguard. Moré–Sorensen-type codes stop after two or three iterations with an approximate $\lambda$.

**The hard case.** If $\mathbf g$ is orthogonal to every eigenvector of $\lambda_1$, then $\|\mathbf p(\lambda)\|$ stays finite as $\lambda\to-\lambda_1$ and may never reach $\Delta$. Theorem 4.3 then forces $\lambda = -\lambda_1$. Take

$$
\mathbf p = -\sum_{j:\lambda_j\ne\lambda_1}\frac{\mathbf q_j^{\mathsf T}\mathbf g}{\lambda_j-\lambda_1}\mathbf q_j+\tau\mathbf z ,
\label{hard}
$$

with $\mathbf z$ a unit eigenvector of $\lambda_1$, and $\tau$ chosen so that $\|\mathbf p\| = \Delta$. The two parts are orthogonal, so $\tau^2 = \Delta^2-\|\cdot\|^2$.

## Modifying the Hessian in line-search Newton methods (Sec. 6.3)

A line-search method needs a positive definite $\mathbf B_k$, so that $\mathbf p_k = -\mathbf B_k^{-1}\mathbf g_k$ is a descent direction. The condition number must also stay bounded for Zoutendijk's theorem to apply ([[line-searches-and-wolfe-conditions]]). Write $\nabla^2f_k = \mathbf Q\boldsymbol\Lambda\mathbf Q^{\mathsf T}$ and require a minimum eigenvalue $\delta>0$:

- **Eigenvalue replacement.** The correction of minimum Frobenius norm that gives $\lambda_{\min}\ge\delta$ is $\Delta\mathbf A = \mathbf Q\operatorname{diag}(\tau_i)\mathbf Q^{\mathsf T}$, with $\tau_i = \max(0,\delta-\lambda_i)$.
- **Shift.** The correction of minimum 2-norm is $\tau\mathbf 1$ with $\tau = \max(0,\delta-\lambda_{\min})$: the same shifted matrix as in Eq. [[#tr-kkt]].
- **Without an eigendecomposition** (too costly in general):
    - Algorithm 6.3 tries Cholesky on $\mathbf A+\tau\mathbf 1$ with increasing $\tau$, starting from $\|\mathbf A\|_F/2$ when some diagonal entry is not positive;
    - modified Cholesky (Algorithm 6.5) increases diagonal entries during the factorization;
    - modified symmetric indefinite ($\mathbf L\mathbf B\mathbf L^{\mathsf T}$) factorizations do the same with $2\times2$ pivots.

N&W stress that there is no consensus on the best modification. Replacing a negative eigenvalue by a tiny $\delta$ gives an enormous step along that eigenvector. Flipping its sign gives a moderate one. Both are "valid". A trust region resolves the ambiguity by tying the shift to a step length.

!!! example "Worked examples"
    **Exact trust-region steps for $\mathbf B = \mathrm{diag}(-2,1,3)$, $\mathbf g = (1,1,1)$**, so $\lambda_1 = -2$. Newton's method on $\phi_2$ starts just above $-\lambda_1 = 2$:

    | $\Delta$ | $\lambda^*$ | iterates of Eq. [[#newton-lam]] | $\|(\mathbf B+\lambda^*\mathbf 1)\mathbf p+\mathbf g\|$ |
    |---:|---:|---|---:|
    | 0.5 | 4.2647093121 | 2.000002, 4.0, 4.26101, 4.264708634, 4.2647093121 | $5\times10^{-16}$ |
    | 1.0 | 3.0473589178 | 2.000002, 3.0, 3.04719, 3.0473589158, 3.0473589178 | $2\times10^{-16}$ |
    | 2.0 | 2.5072982105 | 2.000002, 2.5, 2.50729, 2.5072982105 | $7\times10^{-16}$ |

    The convergence is quadratic after the first step. For $\Delta = 1$, $m(\mathbf p^*)-f = -2.20729$. The best of $2\times10^5$ random points in the ball gives only $-2.19267$, consistent with $\mathbf p^*$ being the global minimizer.

    **Hard case:** $\mathbf g = (0,1,1)$ is orthogonal to $\mathbf q_1 = \mathbf e_1$. The non-$\lambda_1$ part of Eq. [[#hard]] is $(0,-\tfrac13,-\tfrac15)$, of length 0.3887. For $\Delta = 0.4$, $\tau = 0.0943$ gives $\mathbf p = (0.0943,-0.3333,-0.2)$ with $m-f = -0.4267$. For $\Delta = 2$, $\tau = 1.9619$ gives $m-f = -4.2667$, almost all of it from moving along the negative-curvature direction.

    **N&W's modification example.** $\nabla^2f_k = \mathrm{diag}(10,3,-1)$, $\mathbf g_k = (1,-3,2)$:

    | Hessian used | step $\mathbf p$ | $\|\mathbf p\|$ | $\mathbf g^{\mathsf T}\mathbf p$ |
    |---|---|---:|---:|
    | unmodified (pure Newton) | $(-0.1,1,2)$ | 2.24 | $+0.90$ (uphill) |
    | $-1\to\delta = 10^{-8}$ | $(-0.1,1,-2\times10^8)$ | $2\times10^8$ | $-4\times10^8$ |
    | $-1\to+1$ (sign flip) | $(-0.1,1,-2)$ | 2.24 | $-7.1$ |
    | $+\tau\mathbf 1$, $\tau = 2$ ($\lambda_{\min} = 1$) | $(-0.083,0.6,-2)$ | 2.09 | $-5.9$ |

    The minimum-Frobenius correction for $\delta = 10^{-8}$ has $\|\Delta\mathbf A\|_F = 1.00000001 = \delta-\lambda_{\min}$.

## Source

Nocedal and Wright, *Numerical Optimization* (Springer, New York, 1999):

- Ch. 4, Sec. 4.2, pp. 77-87, Thm. 4.3, Lemma 4.4, Algorithm 4.4, Eqs. (4.18)-(4.28);
- Ch. 6, Secs. 6.2-6.3, pp. 139-154, Algorithms 6.2-6.5, Eqs. (6.8)-(6.14).

The identification with HJO's level shift is mine, by comparison of the equations. Numbers: `Claude outputs/part7_ch2_numerical_optimization.py`, section E.
