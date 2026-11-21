---
id: trust-region-methods
title: Trust-region methods - the ratio test, the Cauchy point and the dogleg step
summary: Minimize a quadratic model inside a ball of radius Δ, then accept or reject the step and resize the ball from the ratio ρ of actual to predicted reduction (Algorithm 4.1). Any step that does at least a fixed fraction as well as the Cauchy point (the model minimizer along −g) gives global convergence. The dogleg path for positive definite models, two-dimensional subspace minimization for indefinite ones, and Steihaug's truncated CG for large problems. Traced on Rosenbrock.
status: in-progress
kind: algorithm
level: intermediate
tags: [trust-region, cauchy-point, dogleg, ratio-test, steihaug, global-convergence, level-shift]
prerequisites: [optimality-conditions-and-convergence-rates]
related: [exact-trust-region-step-and-hessian-modification, mcscf-trust-region-and-augmented-hessian, scf-convergence-diis-and-newton, inexact-newton-and-newton-cg, sr1-and-the-broyden-class]
key: rho
order: 40
date: 2026-11-21
---

## Overview

A line search fixes a direction and then chooses a distance. A trust-region method fixes a distance and then chooses the best step within it. This is the natural framework when the model Hessian may be indefinite, as for exact Hessians far from a minimum or SR1 updates. The same framework appears in electronic-structure theory as the trust-region and level-shifted Newton methods for MCSCF and SCF ([[mcscf-trust-region-and-augmented-hessian]], [[scf-convergence-diis-and-newton]]). Levine describes the cruder geometry-optimization version: scale a step down when it exceeds a "trust radius".

## The subproblem and the ratio test

At $\mathbf x_k$ use the model $m_k(\mathbf p) = f_k+\mathbf g_k^{\mathsf T}\mathbf p+\tfrac12\mathbf p^{\mathsf T}\mathbf B_k\mathbf p$. Here $\mathbf B_k$ is the exact Hessian or an approximation, and need not be positive definite. Solve, exactly or approximately,

$$
\min_{\mathbf p}\ m_k(\mathbf p)\quad\text{subject to}\quad\|\mathbf p\|\le\Delta_k .
\label{trs}
$$

Then compare what the model promised with what $f$ delivered:

$$
\rho_k = \frac{f(\mathbf x_k)-f(\mathbf x_k+\mathbf p_k)}{m_k(\mathbf 0)-m_k(\mathbf p_k)}\qquad\Big(\frac{\text{actual reduction}}{\text{predicted reduction}}\Big).
\label{rho}
$$

The denominator is never negative, because $\mathbf p = 0$ is feasible.

**Algorithm 4.1** (with $\bar\Delta$ the maximum radius and $\eta\in[0,\tfrac14)$):

1. If $\rho_k<\tfrac14$, shrink: $\Delta_{k+1} = \tfrac14\|\mathbf p_k\|$.
2. Else, if $\rho_k>\tfrac34$ and $\|\mathbf p_k\| = \Delta_k$, expand: $\Delta_{k+1} = \min(2\Delta_k,\bar\Delta)$.
3. Otherwise keep $\Delta_{k+1} = \Delta_k$.
4. Accept $\mathbf x_{k+1} = \mathbf x_k+\mathbf p_k$ if $\rho_k>\eta$; otherwise stay at $\mathbf x_k$ and re-solve with the smaller radius.

The radius grows only when the step actually hits the boundary. A step strictly inside the region is not being limited by $\Delta_k$.

## The Cauchy point

The Cauchy point is the minimizer of $m_k$ along $-\mathbf g_k$ within the trust region (Algorithm 4.2):

$$
\mathbf p_k^C = -\tau_k\frac{\Delta_k}{\|\mathbf g_k\|}\mathbf g_k,\qquad
\tau_k = \begin{cases}1, & \mathbf g_k^{\mathsf T}\mathbf B_k\mathbf g_k\le0,\\[2pt]
\min\big(\|\mathbf g_k\|^3/(\Delta_k\,\mathbf g_k^{\mathsf T}\mathbf B_k\mathbf g_k),\ 1\big), & \text{otherwise}.\end{cases}
\label{cauchy}
$$

It is cheap and it guarantees a decrease (Lemma 4.5):

$$
m_k(\mathbf 0)-m_k(\mathbf p_k^C)\ge\tfrac12\|\mathbf g_k\|\min\Big(\Delta_k,\frac{\|\mathbf g_k\|}{\|\mathbf B_k\|}\Big).
\label{cauchy-decrease}
$$

The proof considers the three cases of Eq. [[#cauchy]] in turn: $\tau = 1$ with $\mathbf g^{\mathsf T}\mathbf B\mathbf g\le0$, the interior minimizer, and $\tau = 1$ with $\mathbf g^{\mathsf T}\mathbf B\mathbf g>0$.

**Global convergence.** Suppose every step achieves a fixed fraction of the Cauchy decrease, $m_k(\mathbf 0)-m_k(\mathbf p_k)\ge c_1\|\mathbf g_k\|\min(\Delta_k,\|\mathbf g_k\|/\|\mathbf B_k\|)$, with $\|\mathbf B_k\|$ bounded and $\|\mathbf p_k\|\le\gamma\Delta_k$. Then:

- $\liminf\|\mathbf g_k\| = 0$ for $\eta = 0$ (Thm. 4.7);
- $\lim\|\mathbf g_k\| = 0$ for $\eta\in(0,\tfrac14)$ when $\mathbf g$ is Lipschitz (Thm. 4.8).

The exact solution of Eq. [[#trs]] achieves $c_1 = \tfrac12$ (Thm. 4.6), and so do all the methods below, since each does at least as well as $\mathbf p^C$. Using the Cauchy point alone is steepest descent with a step-length rule, and just as slow (worked example). The point of the better methods is the fast local rate.

## The dogleg method (B positive definite)

The exact solution $\mathbf p^*(\Delta)$ traces a curve:

- for $\Delta\ge\|\mathbf p^B\|$ it is the full step $\mathbf p^B = -\mathbf B^{-1}\mathbf g$;
- for small $\Delta$ it is approximately $-\Delta\,\mathbf g/\|\mathbf g\|$.

The dogleg replaces the curve by two line segments. The first runs from 0 to the unconstrained minimizer along $-\mathbf g$, $\mathbf p^U = -\dfrac{\mathbf g^{\mathsf T}\mathbf g}{\mathbf g^{\mathsf T}\mathbf B\mathbf g}\mathbf g$; the second from $\mathbf p^U$ to $\mathbf p^B$:

$$
\tilde{\mathbf p}(\tau) = \begin{cases}\tau\,\mathbf p^U, & 0\le\tau\le1,\\ \mathbf p^U+(\tau-1)(\mathbf p^B-\mathbf p^U), & 1\le\tau\le2.\end{cases}
\label{dogleg}
$$

By Lemma 4.1, along this path $\|\tilde{\mathbf p}(\tau)\|$ increases and $m(\tilde{\mathbf p}(\tau))$ decreases. So the best point on the path within the ball is either:

- $\mathbf p^B$, if it lies inside;
- or the unique crossing of the boundary, found from the scalar quadratic $\|\mathbf p^U+(\tau-1)(\mathbf p^B-\mathbf p^U)\|^2 = \Delta^2$;
- or, if even $\mathbf p^U$ lies outside, the scaled gradient step $-\Delta\mathbf g/\|\mathbf g\|$.

## Indefinite and large problems

**Two-dimensional subspace minimization.** Minimize $m$ exactly over the ball intersected with $\operatorname{span}\{\mathbf g,\mathbf B^{-1}\mathbf g\}$ (Eq. (4.14)). This is at least as good as the dogleg. If $\mathbf B$ is indefinite, replace $\mathbf B^{-1}\mathbf g$ by $(\mathbf B+\alpha\mathbf 1)^{-1}\mathbf g$ with $\alpha\in(-\lambda_1,-2\lambda_1]$, where $\lambda_1<0$ is the most negative eigenvalue. If necessary, add a component along a direction of negative curvature (Eqs. (4.15)-(4.16)).

**Steihaug's truncated CG** (Algorithm 4.3). Run linear conjugate gradients on $\mathbf B\mathbf p = -\mathbf g$ from $\mathbf p = 0$, using only products $\mathbf B\mathbf v$. Stop when:

- the residual is small;
- a direction of negative curvature appears (then go along it to the boundary);
- or an iterate leaves the ball (then stop on the boundary).

The first iterate is the Cauchy point, and $\|\mathbf p_j\|$ increases monotonically (Thm. 4.2). This makes trust-region Newton practical without forming or factorizing $\mathbf B$ ([[inexact-newton-and-newton-cg]]).

**Nearly exact solutions** of Eq. [[#trs]], with their characterization $(\mathbf B+\lambda\mathbf 1)\mathbf p = -\mathbf g$, are in [[exact-trust-region-step-and-hessian-modification]].

!!! example "Worked example: Rosenbrock with the exact Hessian"
    **One subproblem at $\mathbf x_0 = (-1.2,1)$.** $\mathbf B = \nabla^2f$ has eigenvalues 23.6 and 1506, so it is PD. The full Newton step $\mathbf p^B = (0.0247, 0.3807)$ has length 0.3815 and $m(\mathbf p^B)-f_0 = -19.414$.

    | $\Delta$ | $\|\mathbf p^C\|$ | $m(\mathbf p^C)-f_0$ | dogleg case | $m(\mathbf p^{\text{dog}})-f_0$ | exact $m(\mathbf p^*)-f_0$ | bound (Eq. [[#cauchy-decrease]]) |
    |---:|---:|---:|---|---:|---:|---:|
    | 0.05 | 0.0500 | $-9.763$ | gradient step on boundary | $-9.763$ | $-9.764$ | 5.82 |
    | 0.20 | 0.1548 | $-18.022$ | dogleg crossing | $-18.832$ | $-18.846$ | 18.00 |
    | 0.50 | 0.1548 | $-18.022$ | full step | $-19.414$ | $-19.414$ | 18.00 |

    The dogleg is within 0.1 % of the exact subproblem value at $\Delta = 0.2$. Along the path, $\|\tilde{\mathbf p}\|$ increases and $m$ decreases, as Lemma 4.1 states.

    **Algorithm 4.1 with dogleg steps** ($\Delta_0 = 1$, $\bar\Delta = 10$, $\eta = 0.15$) converges in 25 iterations and 26 function evaluations to $\|\mathbf g\|<10^{-8}$. The start of the trace:

    | it | $f$ | $\Delta$ | $\|\mathbf p\|$ | $\rho$ | action |
    |---:|---:|---:|---:|---:|---|
    | 0 | 24.20 | 1.00 | 0.382 | 1.003 | full step, accept, keep $\Delta$ |
    | 1 | 4.732 | 1.00 | 1.000 | $-0.414$ | reject, $\Delta\to0.25$ |
    | 2 | 4.732 | 0.25 | 0.250 | 1.020 | accept, $\Delta\to0.5$ |
    | 3 | 4.302 | 0.50 | 0.500 | 0.850 | accept, $\Delta\to1$ |
    | 4 | 3.602 | 1.00 | 0.398 | 1.250 | full step |

    Near the end $\rho\to1$ and all steps are full Newton steps: $f = 2.3\times10^{-8}\to6.6\times10^{-14}$ with $\|\mathbf g\| = 2.7\times10^{-3}\to8.0\times10^{-6}$.

    Using only the Cauchy point instead needs **14110 iterations** to reach $\|\mathbf g\|\le10^{-6}$.

## Source

Nocedal and Wright, *Numerical Optimization* (Springer, New York, 1999), Ch. 4, pp. 64-77, 87-93, Algorithms 4.1-4.3, Lemmas 4.1, 4.5, Thms. 4.2, 4.6-4.8, Eqs. (4.1)-(4.16), (4.34)-(4.47). Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 15.10, p. 488 (trust radius in geometry optimization).

Numbers: `Claude outputs/part7_ch2_numerical_optimization.py`, section D.
