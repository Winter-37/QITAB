---
id: newton-and-broyden-methods-for-nonlinear-equations
title: Newton and Broyden methods for systems of nonlinear equations
summary: Solve r(x) = 0 for r: ℝⁿ → ℝⁿ, the form of the coupled-cluster amplitude equations and of any stationarity condition. Newton linearizes with the Jacobian and converges quadratically at a nondegenerate root, only linearly at a degenerate one. Inexact Newton solves the linear step to a relative tolerance η_k. Broyden's method replaces J by a secant matrix updated by the smallest rank-one change and converges superlinearly. Globalization uses the merit function ½‖r‖², whose spurious minima sit where J is singular; Powell's example shows that the Newton direction can stall a line search unless the angle condition is enforced. N&W Tables 11.1-11.3 reproduced to the printed digits.
status: in-progress
kind: algorithm
level: advanced
tags: [nonlinear-equations, newton-method, broyden-method, secant-equation, jacobian, merit-function, inexact-newton, globalization, coupled-cluster-amplitudes]
prerequisites: [steepest-descent-newton-and-superlinear-convergence, line-searches-and-wolfe-conditions, sr1-and-the-broyden-class]
related: [inexact-newton-and-newton-cg, diis-extrapolation, coupled-cluster-optimization-and-lagrangian, bfgs-method, preconditioned-conjugate-gradient]
key: broyden
order: 60
date: 2026-11-21
---

## Overview

Many electronic-structure problems are not minimizations but systems of equations

$$
\mathbf r(\mathbf x) = \mathbf 0,\qquad \mathbf r:\mathbb R^n\to\mathbb R^n .
$$

The coupled-cluster amplitude equations $\Omega_\mu(\mathbf t) = 0$ are the main example ([[coupled-cluster-optimization-and-lagrangian]]): the CC energy is not variational, so there is no function to minimize. Others are the stationarity conditions of a Lagrangian and the fixed-point form of SCF.

**Notation (N&W Ch. 11).** Jacobian $\mathbf J(\mathbf x) = \nabla\mathbf r(\mathbf x)$, $J_{pq} = \partial r_p/\partial x_q$, generally nonsymmetric. A root $\mathbf x^*$ is **nondegenerate** if $\mathbf J(\mathbf x^*)$ is nonsingular. $\mathbf r_k = \mathbf r(\mathbf x_k)$, $\mathbf J_k = \mathbf J(\mathbf x_k)$.

**Differences from optimization (N&W p. 279).** Quadratic convergence needs only first derivatives of $\mathbf r$. There is no natural objective to judge progress, so a merit function must be chosen. All roots are equally good, whereas a minimization prefers lower minima.

## Newton's method

**Model.** Taylor's theorem gives $\mathbf r(\mathbf x_k+\mathbf p) = \mathbf r_k+\mathbf J_k\mathbf p+O(\|\mathbf p\|^2)$ when $\mathbf J$ is Lipschitz (Theorem 11.1). Setting the linear model to zero:

$$
\mathbf J_k\mathbf p_k = -\mathbf r_k,\qquad \mathbf x_{k+1} = \mathbf x_k+\mathbf p_k
\label{newton}
$$

(Algorithm 11.1, Eq. (11.9)). Newton's method for minimizing $f$ is Algorithm 11.1 applied to $\nabla f = 0$, with the Hessian as Jacobian.

**Theorem 11.2 (local rate).** Near a nondegenerate root the convergence is Q-superlinear, and Q-quadratic if $\mathbf J$ is Lipschitz near $\mathbf x^*$:

$$
\|\mathbf x_{k+1}-\mathbf x^*\| = O(\|\mathbf x_k-\mathbf x^*\|^2).
$$

*Sketch.* $\mathbf x_{k+1}-\mathbf x^* = \mathbf J_k^{-1}[\mathbf J_k(\mathbf x_k-\mathbf x^*)-(\mathbf r_k-\mathbf r(\mathbf x^*))]$, and the bracket is $O(\|\mathbf x_k-\mathbf x^*\|^2)$ by Taylor's theorem, while $\|\mathbf J_k^{-1}\|$ stays bounded near a nondegenerate root.

**Degenerate roots.** For $r(x) = x^2$ Newton gives $x_k = 2^{-k}x_0$: convergence, but only linear (N&W p. 283).

**Weaknesses (N&W pp. 282-283).** Far from a root the iterates can wander or diverge; $\mathbf J$ may be expensive or unavailable; the linear solve may be too costly for large $n$; the root may be degenerate.

**Inexact Newton (Theorem 11.3).** Solve Eq. [[#newton]] only to

$$
\|\mathbf r_k+\mathbf J_k\mathbf p_k\|\le\eta_k\|\mathbf r_k\|,\qquad \eta_k\in[0,\eta],\ \eta<1 .
$$

Near a nondegenerate root the convergence is then Q-linear if $\eta$ is small enough, Q-superlinear if $\eta_k\to0$, and Q-quadratic if also $\mathbf J$ is Lipschitz and $\eta_k = O(\|\mathbf r_k\|)$, as for optimization ([[inexact-newton-and-newton-cg]]). Since $\mathbf J$ is nonsymmetric, the inner solver is GMRES or another Krylov method for nonsymmetric systems, not CG (N&W p. 285).

## Broyden's method

**Secant equation.** With $\mathbf s_k = \mathbf x_{k+1}-\mathbf x_k$ and $\mathbf y_k = \mathbf r_{k+1}-\mathbf r_k$, Theorem 11.1 gives $\mathbf y_k = \int_0^1\mathbf J(\mathbf x_k+t\mathbf s_k)\mathbf s_k\,dt\approx\mathbf J_{k+1}\mathbf s_k$ (Eq. (11.25)). Ask the approximate Jacobian to reproduce this:

$$
\mathbf B_{k+1}\mathbf s_k = \mathbf y_k .
$$

For $n>1$ this is $n$ equations for $n^2$ unknowns. Unlike in optimization ([[bfgs-method]], [[sr1-and-the-broyden-class]]) there is no symmetry or positive definiteness to impose.

**Update (Eq. (11.27)).**

$$
\mathbf B_{k+1} = \mathbf B_k+\frac{(\mathbf y_k-\mathbf B_k\mathbf s_k)\,\mathbf s_k^{\mathsf T}}{\mathbf s_k^{\mathsf T}\mathbf s_k} .
\label{broyden}
$$

**Lemma 11.4 (least change).** Among all $\mathbf B$ with $\mathbf B\mathbf s_k = \mathbf y_k$, Eq. [[#broyden]] minimizes $\|\mathbf B-\mathbf B_k\|_2$. *Proof:* $\mathbf B_{k+1}-\mathbf B_k = (\mathbf B-\mathbf B_k)\mathbf s_k\mathbf s_k^{\mathsf T}/\mathbf s_k^{\mathsf T}\mathbf s_k$, and $\|\mathbf s\mathbf s^{\mathsf T}/\mathbf s^{\mathsf T}\mathbf s\|_2 = 1$. The update leaves $\mathbf B_k$ unchanged on every vector orthogonal to $\mathbf s_k$.

**Algorithm 11.3.** Solve $\mathbf B_k\mathbf p_k = -\mathbf r_k$, step, update by Eq. [[#broyden]]. Only one new evaluation of $\mathbf r$ per iteration and no derivatives. A rank-one update of an LU or QR factorization, or the Sherman–Morrison formula for $\mathbf B_k^{-1}$, keeps the cost of each solve at $O(n^2)$ (N&W p. 290).

**Theorem 11.5 (local rate).** If $\mathbf x_0$ is close to a nondegenerate $\mathbf x^*$ and $\mathbf B_0$ close to $\mathbf J(\mathbf x^*)$, Broyden's method converges Q-superlinearly. In practice $\mathbf B_0$ is a finite-difference Jacobian at $\mathbf x_0$ or a cheap approximation.

!!! example "N&W Tables 11.1-11.3 (recomputed)"

    $$
    \mathbf r(\mathbf x) = \begin{pmatrix}(x_1+3)(x_2^3-7)+18\\ \sin(x_2e^{x_1}-1)\end{pmatrix},\qquad \mathbf x^* = (0,1),\qquad \mathbf x_0 = (-0.5,1.4),\qquad \mathbf B_0 = \mathbf J(\mathbf x_0)
    $$

    (Eq. (11.30)). Errors $\|\mathbf x_k-\mathbf x^*\|$, my run with N&W's values in brackets:

    | $k$ | Broyden | Newton | Broyden ratio $e_{k+1}/e_k$ |
    |---|---|---|---|
    | 0 | 0.640 [0.64] | 0.640 [0.64] | 0.097 [0.097] |
    | 1 | $6.20\times10^{-2}$ [0.62e−1] | $6.20\times10^{-2}$ [0.62e−1] | 0.0085 [0.0085] |
    | 2 | $5.25\times10^{-4}$ [0.52e−3] | $2.11\times10^{-4}$ [0.21e−3] | 0.47 [0.47] |
    | 3 | $2.46\times10^{-4}$ [0.25e−3] | $1.86\times10^{-8}$ [0.18e−7] | 0.17 [0.17] |
    | 4 | $4.30\times10^{-5}$ [0.43e−4] | $4.9\times10^{-17}$ [0.12e−15] | 0.0033 [0.0033] |
    | 5 | $1.40\times10^{-7}$ [0.14e−6] | | 0.0041 [0.0041] |
    | 6 | $5.69\times10^{-10}$ [0.57e−9] | | 0.0031 [0.0030] |
    | 7 | $1.76\times10^{-12}$ [0.18e−11] | | 0.00057 [0.00049] |
    | 8 | $1.0\times10^{-15}$ [0.87e−15] | | |

    The residual norms match Table 11.3 equally (0.74e1, 0.59, 0.20e−2/0.23e−2, …). Differences appear only at the $10^{-15}$–$10^{-16}$ level and in the last ratios, which are dominated by rounding. Newton doubles the exponent each step; Broyden takes twice as many iterations, with ratios that tend to zero (superlinear) after dithering at steps 2-3.

    Lemma 11.4 checked numerically: none of 2000 random other matrices satisfying the secant equation is closer to $\mathbf B_k$, in either the 2-norm or the Frobenius norm.

## Global convergence

**Failure modes (N&W p. 292).** Components can blow up, or the iterates can cycle. For $r(x) = -x^5+x^3+4x$ (real roots $0,\pm1.60049$, plus a complex pair) Newton from $x_0 = 1$ gives $1,-1,1,-1,\dots$ forever. For $r(x) = \sin5x-x$ (Eq. (11.3); roots 0 and $\pm0.519148$) the root reached depends erratically on $x_0$: from $-0.60$ Newton finds $-0.519148$, from $+0.50$ and $+0.80$ it finds $+0.519148$, from $-1.0$, $0.1$, $0.25$ and $1.2$ it finds 0, and from $-0.30$ it falls into cycles and is at $x = -3.2539$ ($r = 3.79$) after 50 steps.

**Merit function (Eq. (11.34)).**

$$
f(\mathbf x) = \tfrac12\|\mathbf r(\mathbf x)\|^2,\qquad \nabla f = \mathbf J^{\mathsf T}\mathbf r .
$$

Every root is a global minimizer of $f$. The converse fails: a local minimizer with $\mathbf r\ne0$ needs $\mathbf J^{\mathsf T}\mathbf r = 0$, so $\mathbf J$ is singular there (Eq. (11.35)). For $\sin5x-x$, $f$ has many such minima, e.g. near $\pm1.53053$.

**The Newton direction is a descent direction for $f$:** $\mathbf p_k^{\mathsf T}\nabla f_k = -\mathbf p_k^{\mathsf T}\mathbf J_k^{\mathsf T}\mathbf r_k = -\|\mathbf r_k\|^2<0$. But its angle to $-\nabla f$ obeys only (Eq. (11.40))

$$
\cos\theta_k\ \ge\ \frac1{\kappa(\mathbf J_k)},
$$

so it can be nearly orthogonal to the gradient where $\mathbf J$ is ill-conditioned. Theorem 11.6 (Zoutendijk, via Theorem 3.2) guarantees $\mathbf J_k^{\mathsf T}\mathbf r_k\to0$ only if $\cos\theta_k\ge\delta>0$ (Eq. (11.39)).

!!! example "Powell's example (Eq. (11.41); recomputed)"

    $\mathbf r(\mathbf x) = \big(x_1,\ 10x_1/(x_1+0.1)+2x_2^2\big)$, unique root $\mathbf x^* = 0$, $\mathbf J$ singular wherever $x_2 = 0$. Newton directions with exact line searches on $f$ (searched up to the pole at $x_1 = -0.1$), from $(3,1)$:

    | iteration | $\mathbf x$ | step length | $\cos\theta$ |
    |---|---|---|---|
    | 1 | (1.81494, −0.12237) | 0.395 | 0.75 |
    | 2 | (1.80175, 0.01150) | $7.3\times10^{-3}$ | 0.79 |
    | 3 | (1.80163, −0.00108) | $6.4\times10^{-5}$ | 0.11 |
    | 4 | (1.80163, 0.00010) | $5.7\times10^{-7}$ | 0.010 |
    | 6 | (1.80163, 0.00000) | $4.4\times10^{-11}$ | $8.9\times10^{-5}$ |

    The iterates stall at $(1.8016,0)$ in four iterations, as Powell found: not a root and not even a stationary point of $f$, since a step in $-x_1$ lowers both components of $\mathbf r$. The Newton direction there is almost parallel to the $x_2$ axis.

**Fix (Eq. (11.42)).** When the angle condition fails, use

$$
\mathbf p_k = -(\mathbf J_k^{\mathsf T}\mathbf J_k+\tau_k\mathbf1)^{-1}\mathbf J_k^{\mathsf T}\mathbf r_k ,
$$

with $\tau_k$ large enough that $\cos\theta_k\ge\delta$ (as $\tau\to\infty$ the step turns into steepest descent on $f$). This is a Levenberg–Marquardt step. The Cholesky factor of $\mathbf J^{\mathsf T}\mathbf J+\tau\mathbf1$ comes from a QR factorization of $\binom{\mathbf J}{\tau^{1/2}\mathbf1}$ without forming $\mathbf J^{\mathsf T}\mathbf J$. Algorithm 11.4 combines this test, the Newton step when acceptable, and a Wolfe line search with $\alpha = 1$ tried first. On Powell's problem with $\delta = 0.1$ and backtracking it leaves the false point: after 60 iterations $\mathbf x = (-0.0005,-0.159)$ with $\|\mathbf r\| = 5\times10^{-4}$, creeping along the curved valley $10x_1/(x_1+0.1)\approx-2x_2^2$ toward the root. Progress is slow because the root itself is degenerate.

An inexact Newton step satisfies $\cos\theta_k\ge(1-\eta)/(2\kappa(\mathbf J))$, so inexactness does not spoil global convergence (N&W p. 297). Trust-region versions (Algorithm 11.5) are often preferred for nonlinear equations; they are not treated here.

## In electronic structure

The CC amplitude equations are solved by a quasi-Newton iteration in which $\mathbf J$ is replaced by its orbital-energy diagonal, accelerated by DIIS rather than by Broyden updates ([[coupled-cluster-optimization-and-lagrangian]], [[diis-extrapolation]]). Full Newton (with GMRES-type inner solves on $\mathbf J$) is kept for difficult cases. The structure is that of Algorithm 11.1 with a cheap, fixed approximate Jacobian.

## Checks

`Claude outputs/part7_ch3_iterative_solvers.py`, section E: Tables 11.1-11.3, Lemma 11.4, the two scalar examples, Powell's example with exact line searches, and the modified direction (11.42).

## Source

Nocedal and Wright, *Numerical Optimization* (Springer, New York, 1999), Ch. 11, pp. 277-301: Newton's method, Theorems 11.1-11.3 and Algorithm 11.1 (pp. 280-286), Broyden's method, Lemma 11.4, Algorithm 11.3, Theorem 11.5 and Tables 11.1-11.3 (pp. 286-291), merit functions, Theorem 11.6, Powell's example and Algorithm 11.4 (pp. 292-298). All numbers recomputed for this note.
