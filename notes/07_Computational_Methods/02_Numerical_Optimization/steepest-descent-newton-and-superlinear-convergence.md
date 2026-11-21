---
id: steepest-descent-newton-and-superlinear-convergence
title: Local rates of line-search methods - steepest descent, Newton, and the Dennis–Moré condition
summary: Steepest descent with exact line searches contracts the error in f by ((κ−1)/(κ+1))² per step, which is attained for the worst starting vector, so ill-conditioning makes it hopeless (6272 iterations on Rosenbrock). Newton's method converges quadratically once close, with unit steps accepted by the Wolfe conditions. A quasi-Newton method converges superlinearly exactly when its model Hessian is right along the steps taken (Dennis–Moré), not everywhere. Includes a correction to a numerical remark in the book.
status: in-progress
kind: theory
level: intermediate
tags: [steepest-descent, condition-number, newton-method, quadratic-convergence, superlinear-convergence, dennis-more, quasi-newton, rate-of-convergence]
prerequisites: [line-searches-and-wolfe-conditions]
related: [geometry-optimization, bfgs-method, inexact-newton-and-newton-cg, scf-convergence-diis-and-newton]
key: sd-rate
order: 30
date: 2026-11-21
---

## Overview

Zoutendijk's theorem ([[line-searches-and-wolfe-conditions]]) says when an iteration reaches $\mathbf g = 0$. This note says how fast, near a minimizer $\mathbf x^*$ with $\nabla^2f(\mathbf x^*)$ positive definite, with eigenvalues $0<\lambda_1\le\dots\le\lambda_n$ and condition number $\kappa = \lambda_n/\lambda_1$. Rates are as defined in [[optimality-conditions-and-convergence-rates]].

## Steepest descent

**Quadratic model problem.** $f(\mathbf x) = \tfrac12\mathbf x^{\mathsf T}\mathbf Q\mathbf x-\mathbf b^{\mathsf T}\mathbf x$ with $\mathbf Q$ symmetric positive definite. Then $\mathbf g = \mathbf Q\mathbf x-\mathbf b$, and the exact minimizer along $-\mathbf g_k$ is

$$
\alpha_k = \frac{\mathbf g_k^{\mathsf T}\mathbf g_k}{\mathbf g_k^{\mathsf T}\mathbf Q\mathbf g_k}.
$$

With $\|\mathbf z\|_{\mathbf Q}^2 = \mathbf z^{\mathsf T}\mathbf Q\mathbf z$ one has $\tfrac12\|\mathbf x-\mathbf x^*\|_{\mathbf Q}^2 = f(\mathbf x)-f(\mathbf x^*)$. One step gives exactly (N&W Eq. (3.28))

$$
\|\mathbf x_{k+1}-\mathbf x^*\|_{\mathbf Q}^2 = \Big\{1-\frac{(\mathbf g_k^{\mathsf T}\mathbf g_k)^2}{(\mathbf g_k^{\mathsf T}\mathbf Q\mathbf g_k)(\mathbf g_k^{\mathsf T}\mathbf Q^{-1}\mathbf g_k)}\Big\}\|\mathbf x_k-\mathbf x^*\|_{\mathbf Q}^2 .
$$

The Kantorovich inequality bounds the braces (Thm. 3.3, proof in Luenberger):

$$
\|\mathbf x_{k+1}-\mathbf x^*\|_{\mathbf Q}^2\le\Big(\frac{\lambda_n-\lambda_1}{\lambda_n+\lambda_1}\Big)^2\|\mathbf x_k-\mathbf x^*\|_{\mathbf Q}^2
= \Big(\frac{\kappa-1}{\kappa+1}\Big)^2\|\mathbf x_k-\mathbf x^*\|_{\mathbf Q}^2 .
\label{sd-rate}
$$

**General smooth f** (Thm. 3.4). If steepest descent with exact line searches converges to $\mathbf x^*$, then $f_{k+1}-f^*\le\big(\frac{\kappa-1}{\kappa+1}\big)^2(f_k-f^*)$ asymptotically, with $\kappa$ that of $\nabla^2f(\mathbf x^*)$. Inexact line searches do not improve this.

**Interpretation.** For $\kappa = 1$ the method converges in one step. For large $\kappa$ the factor is $\approx1-4/\kappa$: the iterates zigzag across a narrow valley. Steepest descent is the physical picture of "following the force downhill" in a geometry optimization. It is reliable far from a minimum but slow near one, which is why codes switch to (quasi-)Newton steps ([[geometry-optimization]]).

!!! warning "A numerical slip in the book"
    N&W (p. 49) say that for $\kappa = 800$, $f_0 = 1$ and $f^* = 0$, Thm. 3.4 leaves $f\approx0.08$ after 1000 iterations. With the bound as stated, $(799/801)^{2000} = 0.0067$. The value 0.08 is $(799/801)^{1000}$, i.e. the factor without the square. The conclusion (steepest descent is very slow) is unaffected.

## Newton's method

The direction is $\mathbf p_k^N = -(\nabla^2f_k)^{-1}\mathbf g_k$.

**Theorem 3.7.** Let $\nabla^2f$ be Lipschitz near $\mathbf x^*$ (constant $L$), with the second-order sufficient conditions holding at $\mathbf x^*$, and iterate $\mathbf x_{k+1} = \mathbf x_k+\mathbf p_k^N$ from a starting point close enough to $\mathbf x^*$. Then the iterates and the gradient norms converge quadratically.

*Key step.* Using $\mathbf g^* = 0$,

$$
\mathbf x_k+\mathbf p_k^N-\mathbf x^* = (\nabla^2f_k)^{-1}\big[\nabla^2f_k(\mathbf x_k-\mathbf x^*)-(\mathbf g_k-\mathbf g^*)\big].
$$

Taylor's theorem bounds the bracket by $\tfrac12L\|\mathbf x_k-\mathbf x^*\|^2$, so

$$
\|\mathbf x_{k+1}-\mathbf x^*\|\le L\,\|(\nabla^2f^*)^{-1}\|\,\|\mathbf x_k-\mathbf x^*\|^2 .
\label{newton}
$$

Far from $\mathbf x^*$ the Hessian may be indefinite and the unit step too long. Line-search Newton methods modify the Hessian to make it positive definite ([[exact-trust-region-step-and-hessian-modification]]) and use the Wolfe conditions. Those accept $\alpha = 1$ once the iterates are close (Thm. 3.5 below), so the quadratic rate is not lost.

## Quasi-Newton methods: the Dennis–Moré condition

Let $\mathbf p_k = -\mathbf B_k^{-1}\mathbf g_k$ with $\mathbf B_k$ positive definite.

**Theorem 3.5.** Let the step satisfy the Wolfe conditions with $c_1\le\tfrac12$, and let $\mathbf x_k\to\mathbf x^*$ with $\nabla^2f^*$ PD. If

$$
\lim_{k\to\infty}\frac{\|(\mathbf B_k-\nabla^2f^*)\mathbf p_k\|}{\|\mathbf p_k\|} = 0 ,
\label{dennis-more}
$$

then (i) $\alpha_k = 1$ is admissible for all large $k$, and (ii) with unit steps the convergence is superlinear.

**Theorem 3.6.** For quasi-Newton iterations with unit steps converging to such an $\mathbf x^*$, Eq. [[#dennis-more]] is necessary as well as sufficient for superlinear convergence. It is equivalent to $\|\mathbf p_k-\mathbf p_k^N\| = o(\|\mathbf p_k\|)$: the quasi-Newton step must approach the Newton step in direction and length.

**Interpretation.** $\mathbf B_k$ need not converge to the Hessian. It only needs to be right along the directions actually taken. That is what the secant equation $\mathbf B_{k+1}\mathbf s_k = \mathbf y_k$ enforces, one direction per iteration ([[bfgs-method]]).

!!! example "Worked examples"
    **Steepest descent on quadratics** (exact line search, $n = 10$, random eigenvectors, eigenvalues evenly spaced in $[1,\kappa]$):

    | $\kappa$ | bound $((\kappa-1)/(\kappa+1))^2$ | observed $\|\mathbf e_{k+1}\|_{\mathbf Q}^2/\|\mathbf e_k\|_{\mathbf Q}^2$ |
    |---:|---:|---:|
    | 10 | 0.6694 | 0.6677 (all steps) |
    | 100 | 0.9608 | 0.9608 |

    For $\mathbf Q = \mathrm{diag}(1,100)$ and the worst start $\mathbf x_0-\mathbf x^*\propto(1/\lambda_1,1/\lambda_2)$, every step has ratio $0.960788$, equal to the bound. Eq. [[#sd-rate]] is sharp.

    **Rosenbrock from $(-1.2,1)$** (Wolfe line search, $c_2 = 0.9$, initial step from the previous decrease):

    - Steepest descent needs 6272 iterations (6455 evaluations) to reach $\|\mathbf g\|\le10^{-4}$, and is still $2.4\times10^{-4}$ from $\mathbf x^*$ ($\kappa^* = 2508$).
    - Newton (Hessian shifted when not PD) needs 22 iterations. $\alpha<1$ is taken five times, all before iteration 15. The last gradient norms are

      $$1.3\times10^{-2}\to1.3\times10^{-3}\to5.5\times10^{-8}\to4.9\times10^{-14},$$

      quadratic, with $\alpha = 1$ throughout the final phase.
    - BFGS needs 37 iterations to $\|\mathbf g\|\le10^{-10}$. The error ratios $e_{k+1}/e_k$ over the last seven steps are $0.31, 0.058, 0.035, 0.15, 0.029, 0.0019, 0.0012$. They tend to zero but not monotonically: superlinear, as Thm. 3.6 requires.

## Source

Nocedal and Wright, *Numerical Optimization* (Springer, New York, 1999), Ch. 3, Sec. 3.3, pp. 46-53, Thms. 3.3-3.7, Eqs. (3.24)-(3.37).

The remark on p. 49 was checked numerically. Numbers: `Claude outputs/part7_ch2_numerical_optimization.py`, section C.
