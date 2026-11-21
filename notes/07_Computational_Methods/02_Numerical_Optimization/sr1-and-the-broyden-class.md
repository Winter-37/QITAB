---
id: sr1-and-the-broyden-class
title: Quasi-Newton methods II - the SR1 update and the Broyden class
summary: The symmetric rank-one (SR1) update is the unique rank-one symmetric solution of the secant equation. It need not stay positive definite, which makes it a good model of indefinite Hessians in trust-region methods, but its denominator can vanish, so updates are skipped by a simple test. On quadratics it recovers the exact Hessian after n independent steps, without a line search. BFGS, DFP and SR1 are all members of the one-parameter Broyden class; the range of φ that preserves positive definiteness, and where the class becomes singular.
status: in-progress
kind: derivation
level: advanced
tags: [quasi-newton, sr1, symmetric-rank-one, broyden-class, hessian-update, indefinite-hessian, skipping-rule, trust-region]
prerequisites: [bfgs-method, trust-region-methods]
related: [exact-trust-region-step-and-hessian-modification, stationary-points-and-reaction-paths, limited-memory-bfgs]
key: sr1
order: 70
date: 2026-11-21
---

## Overview

BFGS keeps $\mathbf B_k$ positive definite. That is what a line-search minimizer needs, but it means BFGS cannot represent negative curvature. Far from a minimum, or on the way to a saddle point, the true Hessian has negative eigenvalues. The SR1 update can reproduce them. This note uses $\mathbf s_k,\mathbf y_k$ and the secant equation $\mathbf B_{k+1}\mathbf s_k = \mathbf y_k$ of [[bfgs-method]].

## The SR1 formula

Look for a symmetric rank-one correction $\mathbf B_{k+1} = \mathbf B_k+\sigma\mathbf v\mathbf v^{\mathsf T}$, $\sigma = \pm1$. The secant equation gives

$$
\mathbf y_k-\mathbf B_k\mathbf s_k = \sigma(\mathbf v^{\mathsf T}\mathbf s_k)\,\mathbf v ,
$$

so $\mathbf v = \delta(\mathbf y_k-\mathbf B_k\mathbf s_k)$ for some scalar $\delta$. Substituting back requires $\sigma\delta^2\,\mathbf s_k^{\mathsf T}(\mathbf y_k-\mathbf B_k\mathbf s_k) = 1$, which fixes $\sigma = \operatorname{sign}[\mathbf s_k^{\mathsf T}(\mathbf y_k-\mathbf B_k\mathbf s_k)]$ and $\delta^2$. Hence (Eq. (8.24))

$$
\mathbf B_{k+1} = \mathbf B_k+\frac{(\mathbf y_k-\mathbf B_k\mathbf s_k)(\mathbf y_k-\mathbf B_k\mathbf s_k)^{\mathsf T}}{(\mathbf y_k-\mathbf B_k\mathbf s_k)^{\mathsf T}\mathbf s_k},
\label{sr1}
$$

and in inverse form (Eq. (8.25)) $\mathbf H_{k+1} = \mathbf H_k+\dfrac{(\mathbf s_k-\mathbf H_k\mathbf y_k)(\mathbf s_k-\mathbf H_k\mathbf y_k)^{\mathsf T}}{(\mathbf s_k-\mathbf H_k\mathbf y_k)^{\mathsf T}\mathbf y_k}$.

The derivation covers all cases, with $\mathbf r_k = \mathbf y_k-\mathbf B_k\mathbf s_k$:

1. If $\mathbf r_k^{\mathsf T}\mathbf s_k\ne0$, Eq. [[#sr1]] is the *unique* symmetric rank-one update.
2. If $\mathbf r_k = 0$, then $\mathbf B_{k+1} = \mathbf B_k$ already satisfies the secant equation.
3. If $\mathbf r_k\ne0$ but $\mathbf r_k^{\mathsf T}\mathbf s_k = 0$, no symmetric rank-one update exists.

**Skipping rule** (Eq. (8.26)). Apply Eq. [[#sr1]] only if

$$
|\mathbf s_k^{\mathsf T}(\mathbf y_k-\mathbf B_k\mathbf s_k)|\ge r\,\|\mathbf s_k\|\,\|\mathbf y_k-\mathbf B_k\mathbf s_k\|,\qquad r\approx10^{-8};
$$

otherwise set $\mathbf B_{k+1} = \mathbf B_k$. Skipping is harmless here, and rare. A small denominator means that $\mathbf B_k$ already has nearly the right curvature along $\mathbf s_k$. BFGS updates fail for a different reason, $\mathbf s_k^{\mathsf T}\mathbf y_k\le0$, and skipping those can lose important curvature information.

**Use with a trust region** (Algorithm 8.2). Since $\mathbf B_k$ may be indefinite, SR1 is paired with a trust-region step ([[trust-region-methods]], [[exact-trust-region-step-and-hessian-modification]]) rather than a line search. The update is applied even when the step is rejected: the pair $(\mathbf s_k,\mathbf y_k)$ still carries curvature information.

**Properties.**

- *Hereditary and exact on quadratics* (Thm. 8.1). Let $f$ be a strongly convex quadratic with Hessian $\mathbf A$. Take steps $\mathbf s_0,\dots,\mathbf s_{n-1}$ that are linearly independent and keep the denominators nonzero, with no line search required. Then the secant equation holds for every previous step, and after $n$ steps $\mathbf B_n = \mathbf A$.
- *Good Hessian approximations in practice.* N&W report that SR1 matrices are often better approximations of the true Hessian than BFGS matrices. The convergence theory for the trust-region SR1 method (Thm. 8.7) gives $(n+1)$-step superlinear convergence, $\|\mathbf x_{k+n+1}-\mathbf x^*\|/\|\mathbf x_k-\mathbf x^*\|\to0$. Its assumptions are: iterates in a bounded convex set with a unique stationary point, a PD Lipschitz Hessian there, bounded $\|\mathbf B_k\|$, and the skipping test holding at every iteration. Under the same assumptions $\mathbf B_k$ is PSD for almost all $k$, even from an indefinite start.

## The Broyden class

With $\mathbf v_k = \dfrac{\mathbf y_k}{\mathbf y_k^{\mathsf T}\mathbf s_k}-\dfrac{\mathbf B_k\mathbf s_k}{\mathbf s_k^{\mathsf T}\mathbf B_k\mathbf s_k}$, the family (Eq. (8.32)) is

$$
\mathbf B_{k+1} = \mathbf B_k-\frac{\mathbf B_k\mathbf s_k\mathbf s_k^{\mathsf T}\mathbf B_k}{\mathbf s_k^{\mathsf T}\mathbf B_k\mathbf s_k}+\frac{\mathbf y_k\mathbf y_k^{\mathsf T}}{\mathbf y_k^{\mathsf T}\mathbf s_k}+\phi_k(\mathbf s_k^{\mathsf T}\mathbf B_k\mathbf s_k)\,\mathbf v_k\mathbf v_k^{\mathsf T},
\label{broyden}
$$

equivalently $\mathbf B_{k+1} = (1-\phi_k)\mathbf B^{\text{BFGS}}_{k+1}+\phi_k\mathbf B^{\text{DFP}}_{k+1}$.

Every member satisfies the secant equation, because $\mathbf v_k^{\mathsf T}\mathbf s_k = 0$. The special cases are:

- $\phi_k = 0$ gives BFGS and $\phi_k = 1$ gives DFP;
- $\phi_k = \mathbf s_k^{\mathsf T}\mathbf y_k/(\mathbf s_k^{\mathsf T}\mathbf y_k-\mathbf s_k^{\mathsf T}\mathbf B_k\mathbf s_k)$ gives SR1 (checked numerically below). This value can lie outside $[0,1]$.

**Positive definiteness.** If $\mathbf B_k$ is PD, $\mathbf y_k^{\mathsf T}\mathbf s_k>0$ and $\phi_k\ge0$, then $\mathbf B_{k+1}$ is PD, since the last term in Eq. [[#broyden]] is then PSD. The **restricted Broyden class** is $\phi_k\in[0,1]$. Decreasing $\phi_k$ below 0 lowers the eigenvalues, by eigenvalue interlacing for the rank-one term. $\mathbf B_{k+1}$ becomes singular at (Eqs. (8.37)-(8.38))

$$
\phi_k^c = \frac1{1-\mu_k},\qquad \mu_k = \frac{(\mathbf y_k^{\mathsf T}\mathbf B_k^{-1}\mathbf y_k)(\mathbf s_k^{\mathsf T}\mathbf B_k\mathbf s_k)}{(\mathbf y_k^{\mathsf T}\mathbf s_k)^2}\ge1 ,
$$

where $\mu_k\ge1$ by Cauchy–Schwarz, so $\phi_k^c\le0$. Every member with $\phi_k>\phi_k^c$ stays PD.

**Theorem 8.3** (strongly convex quadratic, $\phi_k\in[0,1]$, unit steps $\mathbf x_{k+1} = \mathbf x_k-\mathbf B_k^{-1}\nabla f_k$). Each eigenvalue of $\mathbf A^{1/2}\mathbf B_k^{-1}\mathbf A^{1/2}$ moves monotonically toward 1. This does not hold outside $[0,1]$. With exact line searches, all members with $\phi_k\ge\phi_k^c$ generate the same iterates. That is the quadratic-termination result Thm. 8.4 quoted in [[bfgs-method]].

## In molecular optimization

Saddle-point searches need an indefinite model Hessian with the right number of negative eigenvalues ([[stationary-points-and-reaction-paths]]). Updates of the SR1 type, or mixtures of SR1 with other rank-two formulas (for example Bofill's), are therefore used there instead of BFGS. These mixed updates and the eigenvector-following step that uses them are not in N&W. They are planned for a note with a proper source.

!!! example "Worked examples"
    **Exact recovery** (Thm. 8.1): random SPD $4\times4$ $\mathbf A$, $\mathbf B_0 = \mathbf 1$, random independent steps, $\mathbf y_j = \mathbf A\mathbf s_j$.

    | after step | 1 | 2 | 3 | 4 |
    |---|---:|---:|---:|---:|
    | $\|\mathbf B-\mathbf A\|$ | 5.71 | 2.27 | 0.105 | $1.4\times10^{-15}$ |
    | $\max_{j<k}\|\mathbf B\mathbf s_j-\mathbf y_j\|$ | $1.3\times10^{-15}$ | $1.4\times10^{-15}$ | $2.7\times10^{-15}$ | $2.0\times10^{-15}$ |

    **Indefinite target** $\mathrm{diag}(3,1,-2)$ with steps $\mathbf e_1,\mathbf e_2,\mathbf e_3$ from $\mathbf B_0 = \mathbf 1$. The second update has $\mathbf r = 0$ and is not needed. The result has eigenvalues $\{-2,1,3\}$, exactly. BFGS cannot produce a negative eigenvalue.

    **Skip test:** for $\mathbf s = (1,0)$, $\mathbf y = (1,1)$, $\mathbf B = \mathbf 1$, we get $\mathbf r^{\mathsf T}\mathbf s = 0$ with $\mathbf r\ne0$. That is case 3, so the update is skipped.

    **Broyden class** for a random SPD $\mathbf B_k$ ($n = 4$, $\mathbf y^{\mathsf T}\mathbf s>0$): $\mu = 1.0159$ and $\phi^c = -62.71$.

    | $\phi$ | secant holds | $\lambda_{\min}(\mathbf B_{k+1})$ |
    |---:|:-:|---:|
    | 0 (BFGS) | yes | 0.983 |
    | 1 (DFP) | yes | 0.998 |
    | $\phi^c = -62.71$ | yes | $1.6\times10^{-16}$ (singular) |
    | $\phi^c-0.5$ | yes | $-8.1\times10^{-3}$ |
    | $59.92$ (SR1 value) | yes | (equals Eq. [[#sr1]] exactly) |

    $\phi = 1$ reproduces Eq. (8.13) of DFP.

    **Rosenbrock with SR1 and exact trust-region steps** ($\mathbf B_0 = \mathbf 1$, update even after rejected steps): 54 iterations and 55 evaluations to $\|\mathbf g\|\le10^{-8}$, final error $2.3\times10^{-13}$. BFGS with a Wolfe line search needed 51.

## Source

Nocedal and Wright, *Numerical Optimization* (Springer, New York, 1999), Ch. 8, Secs. 8.2-8.4, pp. 202-211, 218-219, Algorithm 8.2, Thms. 8.1, 8.3, 8.4, 8.7, Eqs. (8.22)-(8.38).

The SR1 value of $\phi$ and the remark on saddle-point updates are mine (the former checked numerically). Numbers: `Claude outputs/part7_ch2_numerical_optimization.py`, section G.
