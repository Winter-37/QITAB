---
id: bfgs-method
title: Quasi-Newton methods I - the secant equation, DFP and BFGS
summary: Build a Hessian approximation from gradient differences alone. The secant equation B_{k+1}s_k = y_k with the curvature condition s_kᵀy_k > 0 (which the Wolfe conditions guarantee) admits many symmetric solutions; the one closest to the previous matrix in a weighted Frobenius norm is DFP for B and BFGS for H = B⁻¹. Derivation of the properties (secant, rank two, positive definite), the initial scaling H₀ = (yᵀs/yᵀy)1, self-correction, termination on quadratics, and superlinear convergence; Rosenbrock and an inverse-Hessian check.
status: in-progress
kind: derivation
level: intermediate
tags: [quasi-newton, bfgs, dfp, secant-equation, curvature-condition, hessian-update, superlinear-convergence, geometry-optimization]
prerequisites: [line-searches-and-wolfe-conditions, steepest-descent-newton-and-superlinear-convergence]
related: [sr1-and-the-broyden-class, limited-memory-bfgs, geometry-optimization, trust-region-methods]
key: bfgs-h
order: 60
date: 2026-11-21
---

## Overview

Newton's method needs the Hessian, which in electronic-structure work costs far more than the gradient ([[analytic-gradients-and-force-constants]]). Quasi-Newton methods replace it by a matrix $\mathbf B_k$ (or its inverse $\mathbf H_k$) that is updated after every step, using only the change in the gradient. They converge superlinearly ([[steepest-descent-newton-and-superlinear-convergence]]). BFGS is the standard choice for molecular geometry optimization; Levine names it as "one widely used recipe" for the Hessian update.

## The secant equation and the curvature condition

With $\mathbf s_k = \mathbf x_{k+1}-\mathbf x_k = \alpha_k\mathbf p_k$ and $\mathbf y_k = \mathbf g_{k+1}-\mathbf g_k$, require the new model's gradient to match $\mathbf g$ at both $\mathbf x_k$ and $\mathbf x_{k+1}$:

$$
\mathbf B_{k+1}\mathbf s_k = \mathbf y_k\qquad\text{(secant equation)}.
\label{secant}
$$

A positive definite $\mathbf B_{k+1}$ can satisfy this only if

$$
\mathbf s_k^{\mathsf T}\mathbf y_k>0\qquad\text{(curvature condition)},
\label{curvature}
$$

as follows on multiplying Eq. [[#secant]] by $\mathbf s_k^{\mathsf T}$. For strongly convex $f$ it always holds. In general it is guaranteed by the Wolfe curvature condition: $\mathbf y_k^{\mathsf T}\mathbf s_k\ge(c_2-1)\alpha_k\mathbf g_k^{\mathsf T}\mathbf p_k>0$ ([[line-searches-and-wolfe-conditions]]). This is why quasi-Newton line searches enforce Wolfe and not just Armijo.

For $n>1$, Eq. [[#secant]] is $n$ equations for $n(n+1)/2$ unknowns. Levine's two-variable example makes the point: two equations, three Hessian elements. The update is fixed by asking for the symmetric solution closest to the previous matrix.

## DFP and BFGS as closest updates

**DFP.** Solve $\min\|\mathbf B-\mathbf B_k\|_{\mathbf W}$ subject to $\mathbf B = \mathbf B^{\mathsf T}$ and $\mathbf B\mathbf s_k = \mathbf y_k$, in the weighted Frobenius norm $\|\mathbf A\|_{\mathbf W} = \|\mathbf W^{1/2}\mathbf A\mathbf W^{1/2}\|_F$. Any weight with $\mathbf W\mathbf y_k = \mathbf s_k$ will do, for example the inverse of the average Hessian $\bar{\mathbf G}_k = \int_0^1\nabla^2f(\mathbf x_k+\tau\alpha_k\mathbf p_k)\,d\tau$, which makes the norm dimensionless. The solution is (Eq. (8.13))

$$
\mathbf B_{k+1} = (\mathbf 1-\gamma_k\mathbf y_k\mathbf s_k^{\mathsf T})\,\mathbf B_k\,(\mathbf 1-\gamma_k\mathbf s_k\mathbf y_k^{\mathsf T})+\gamma_k\mathbf y_k\mathbf y_k^{\mathsf T},\qquad \gamma_k = \frac1{\mathbf y_k^{\mathsf T}\mathbf s_k}.
\label{dfp}
$$

**BFGS.** Impose the analogous conditions on the inverse, $\min\|\mathbf H-\mathbf H_k\|_{\mathbf W}$ with $\mathbf H = \mathbf H^{\mathsf T}$, $\mathbf H\mathbf y_k = \mathbf s_k$, and now $\mathbf W\mathbf s_k = \mathbf y_k$. With $\rho_k = 1/(\mathbf y_k^{\mathsf T}\mathbf s_k)$, the unique solution is

$$
\mathbf H_{k+1} = (\mathbf 1-\rho_k\mathbf s_k\mathbf y_k^{\mathsf T})\,\mathbf H_k\,(\mathbf 1-\rho_k\mathbf y_k\mathbf s_k^{\mathsf T})+\rho_k\mathbf s_k\mathbf s_k^{\mathsf T}.
\label{bfgs-h}
$$

By the Sherman–Morrison–Woodbury formula, the corresponding update of $\mathbf B$ is

$$
\mathbf B_{k+1} = \mathbf B_k-\frac{\mathbf B_k\mathbf s_k\mathbf s_k^{\mathsf T}\mathbf B_k}{\mathbf s_k^{\mathsf T}\mathbf B_k\mathbf s_k}+\frac{\mathbf y_k\mathbf y_k^{\mathsf T}}{\mathbf y_k^{\mathsf T}\mathbf s_k}.
\label{bfgs-b}
$$

Eqs. [[#dfp]] and [[#bfgs-h]] have the same form, with $\mathbf s\leftrightarrow\mathbf y$ and $\mathbf B\leftrightarrow\mathbf H$ interchanged.

**Properties** (each line checked directly from Eq. [[#bfgs-h]]):

1. **Secant.** $(\mathbf 1-\rho_k\mathbf y_k\mathbf s_k^{\mathsf T})\mathbf y_k = \mathbf y_k-\rho_k\mathbf y_k(\mathbf s_k^{\mathsf T}\mathbf y_k) = 0$, so $\mathbf H_{k+1}\mathbf y_k = \rho_k\mathbf s_k(\mathbf s_k^{\mathsf T}\mathbf y_k) = \mathbf s_k$.
2. **Rank two.** $\mathbf H_{k+1}-\mathbf H_k$ has rank at most two.
3. **Positive definite**, if $\mathbf H_k$ is and $\mathbf y_k^{\mathsf T}\mathbf s_k>0$. For $\mathbf z\ne0$ put $\mathbf w = \mathbf z-\rho_k(\mathbf s_k^{\mathsf T}\mathbf z)\mathbf y_k$. Then
   $$\mathbf z^{\mathsf T}\mathbf H_{k+1}\mathbf z = \mathbf w^{\mathsf T}\mathbf H_k\mathbf w+\rho_k(\mathbf s_k^{\mathsf T}\mathbf z)^2\ge0 .$$
   Equality needs $\mathbf s_k^{\mathsf T}\mathbf z = 0$, hence $\mathbf w = \mathbf z$ and $\mathbf w^{\mathsf T}\mathbf H_k\mathbf w>0$, a contradiction.
4. **Cost.** $O(n^2)$ per update, and the direction $\mathbf p_k = -\mathbf H_k\mathbf g_k$ is a matrix–vector product with no linear solve. Updating a Cholesky factor of $\mathbf B_k$ is an equivalent $O(n^2)$ alternative.

## The algorithm (Algorithm 8.1)

1. Choose $\mathbf x_0$, a tolerance, and $\mathbf H_0$ (often $\mathbf 1$).
2. Repeat until $\|\mathbf g_k\|$ is small:
    - $\mathbf p_k = -\mathbf H_k\mathbf g_k$;
    - choose $\alpha_k$ by a line search satisfying the Wolfe conditions, always trying $\alpha = 1$ first;
    - set $\mathbf s_k = \alpha_k\mathbf p_k$, $\mathbf x_{k+1} = \mathbf x_k+\mathbf s_k$, $\mathbf y_k = \mathbf g_{k+1}-\mathbf g_k$;
    - update $\mathbf H$ by Eq. [[#bfgs-h]].

**Initial matrix.** There is no good general $\mathbf H_0$. A common heuristic is to take $\mathbf H_0 = \mathbf 1$ for the first step and then, before the first update, rescale (Eq. (8.20)):

$$
\mathbf H_0\leftarrow\frac{\mathbf y_0^{\mathsf T}\mathbf s_0}{\mathbf y_0^{\mathsf T}\mathbf y_0}\mathbf 1 .
$$

The quotient approximates an eigenvalue of the inverse average Hessian, so the scale of the first steps is right. In geometry optimization, $\mathbf H_0$ (or $\mathbf B_0$) is built instead from typical force constants or a cheap calculation. Levine recommends this, and it is usually much better than a multiple of $\mathbf 1$.

**Robustness.** If $\mathbf y_k^{\mathsf T}\mathbf s_k$ is tiny but positive, Eq. [[#bfgs-h]] makes $\mathbf H_{k+1}$ huge. In practice BFGS has strong **self-correcting** properties: a poor curvature estimate is repaired within a few steps, provided the Wolfe line search is used. DFP corrects bad estimates much less well, which is why BFGS replaced it. Without a Wolfe line search (in a trust-region method, or with a nonconvex $f$), Eq. [[#curvature]] can fail. Implementations then skip the update, or use the damped BFGS update (N&W Ch. 18).

## Convergence

- **Quadratic termination** (Thm. 8.4, for the whole Broyden class). On a strongly convex quadratic with exact line searches, the iterates reach the minimizer in at most $n$ steps. The secant equation then holds for all previous steps, and the final matrix is the exact Hessian (or its inverse). With $\mathbf B_0 = \mathbf 1$ the iterates coincide with those of linear conjugate gradients. N&W note that this is mainly of theoretical interest, since practical line searches are inexact.
- **Global convergence for convex f** (Thm. 8.5): with any SPD $\mathbf B_0$ and a Wolfe line search, BFGS converges to the minimizer when $f$ is twice differentiable with a convex level set and a Hessian bounded and PD on it. No such result is known for general nonconvex $f$. In practice BFGS is very robust anyway.
- **Superlinear rate** (Thm. 8.6). If the iterates converge to a minimizer with Lipschitz Hessian fast enough that $\sum_k\|\mathbf x_k-\mathbf x^*\|<\infty$, then the convergence is superlinear. The proof establishes the Dennis–Moré condition.

!!! example "Worked examples"
    **Algebra checks** on a random SPD $5\times5$ $\mathbf H$ with $\mathbf y^{\mathsf T}\mathbf s = 4.774$:

    - Eq. [[#bfgs-h]] gives a symmetric PD $\mathbf H_1$ with $\mathbf H_1\mathbf y = \mathbf s$;
    - $\operatorname{rank}(\mathbf H_1-\mathbf H) = 2$;
    - Eq. [[#bfgs-b]] gives $\mathbf B_1\mathbf s = \mathbf y$ and $\mathbf B_1^{-1} = \mathbf H_1$;
    - DFP satisfies the secant equation as well.

    **Quadratic termination:** with exact line searches on a random SPD $5\times5$ quadratic, after five steps $\|\mathbf g_5\| = 7\times10^{-16}$ and $\|\mathbf H_5-\mathbf A^{-1}\| = 5\times10^{-16}$.

    **Rosenbrock from $(-1.2,1)$**, strong Wolfe ($c_1 = 10^{-4}$, $c_2 = 0.9$), to $\|\mathbf g\|\le10^{-8}$:

    | $\mathbf H_0$ | iterations | $f$ / $\mathbf g$ evaluations |
    |---|---:|---:|
    | $\mathbf 1$, rescaled by Eq. (8.20) | 36 | 51 / 51 |
    | $\mathbf 1$, no rescaling | 33 | 53 / 53 |
    | $10^{-4}\mathbf 1$ | 36 | 50 |
    | $10^{4}\mathbf 1$ | 19 | 56 |
    | SciPy `minimize(method="BFGS")` | 34 | 41 |

    The poorly scaled starts cost only a few extra evaluations, which shows the self-correction at work. In the rescaled run:

    - $f$ falls from 24.2 to $7.5\times10^{-22}$;
    - the first step is the short steepest-descent-like $\alpha = 7.9\times10^{-4}$;
    - all of the last ten iterations take the unit step, as the Dennis–Moré theorem predicts;
    - the final error is $2.7\times10^{-11}$.

    **Water, RHF/STO-3G** in Cartesian coordinates with PySCF analytic gradients, from R(OH) = 0.99 Å / 1.00 Å and a distorted angle. This BFGS converges in 6 iterations and 7 SCF+gradient calls to $E = -74.9659011923\,E_h$, R(OH) = 0.98941 Å and HOH = 100.03°, the geometry of the Newton calculation in [[geometry-optimization]]. Steepest descent needs 35 calls to reach only $\|\mathbf g\|\le10^{-4}$.

## Source

Nocedal and Wright, *Numerical Optimization* (Springer, New York, 1999), Ch. 2, Sec. 2.2, pp. 23-25; Ch. 8, Secs. 8.1, 8.4, pp. 194-202, 209-218, Algorithm 8.1, Thms. 8.4-8.6, Eqs. (8.4)-(8.21). Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 15.10, pp. 486-488 (quasi-Newton geometry optimization, initial Hessian from force constants).

The proofs of the three properties are written out here from the update formulas; N&W state them more briefly. Numbers: `Claude outputs/part7_ch2_numerical_optimization.py`, sections F and K.
