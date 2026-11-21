---
id: inexact-newton-and-newton-cg
title: Inexact Newton and Newton–CG (truncated Newton) methods
summary: Solve the Newton equations ∇²f p = −g only approximately, by conjugate gradients stopped when the residual falls below η_k‖g‖. The forcing sequence η_k decides the local rate (linear if η_k ≤ η < 1, superlinear if η_k → 0, quadratic if η_k = O(‖g‖)). Line-search Newton–CG stops at negative curvature; trust-region Newton–CG (Steihaug) follows it to the boundary. Only Hessian–vector products are needed, analytically or by one extra gradient. Forcing-sequence rates measured on a coupled n = 1000 problem.
status: in-progress
kind: algorithm
level: advanced
tags: [inexact-newton, newton-cg, truncated-newton, forcing-sequence, hessian-vector-product, steihaug, negative-curvature, large-scale-optimization]
prerequisites: [steepest-descent-newton-and-superlinear-convergence, nonlinear-conjugate-gradient, trust-region-methods]
related: [exact-trust-region-step-and-hessian-modification, limited-memory-bfgs, mcscf-second-order-optimization, ci-optimization-newton-and-davidson, cphf-closed-shell]
key: forcing
order: 100
date: 2026-11-21
---

## Overview

For large $n$, forming and factorizing $\nabla^2f_k$ to get the Newton step is too expensive. It is also wasteful far from $\mathbf x^*$, where the quadratic model is poor anyway. Inexact Newton methods solve

$$
\nabla^2f_k\,\mathbf p_k = -\mathbf g_k
\label{newton-eq}
$$

iteratively and stop early. With CG as the inner solver they need only products $\nabla^2f_k\mathbf v$. In electronic-structure programs this is the structure of second-order SCF and MCSCF: micro-iterations solve the Newton equations with Hessian-vector products (linear transformations), inside macro-iterations ([[mcscf-second-order-optimization]]). Levine calls it the truncated Newton (TN, TNCG) method and notes its use in molecular-mechanics optimizations.

## Forcing sequences and local rate

Stop the inner iteration when the residual satisfies (Eq. (6.3))

$$
\|\mathbf r_k\| = \|\nabla^2f_k\mathbf p_k+\mathbf g_k\|\le\eta_k\|\mathbf g_k\|,\qquad 0<\eta_k<1 .
\label{forcing}
$$

**Why it works.** Near $\mathbf x^*$, Taylor's theorem gives $\mathbf g(\mathbf x_k+\mathbf p_k) = \mathbf g_k+\nabla^2f_k\mathbf p_k+O(\|\mathbf p_k\|^2) = \mathbf r_k+O(\|\mathbf g_k\|^2)$. Hence (Eq. (6.5))

$$
\|\mathbf g_{k+1}\|\le\eta_k\|\mathbf g_k\|+O(\|\mathbf g_k\|^2).
$$

**Theorems 6.1-6.2.** Close enough to a minimizer with PD Hessian:

| forcing sequence | local rate |
|---|---|
| $\eta_k\le\eta<1$ | linear |
| $\eta_k\to0$, e.g. $\eta_k = \min(0.5,\sqrt{\|\mathbf g_k\|})$ | superlinear |
| $\eta_k = O(\|\mathbf g_k\|)$, e.g. $\min(0.5,\|\mathbf g_k\|)$ | quadratic |

The tolerance is loose far away, which saves inner iterations, and tight near the end, which keeps the rate.

## Line-search Newton–CG (Algorithm 6.1)

Run CG on Eq. [[#newton-eq]] from $\mathbf z_0 = 0$, with directions $\mathbf d_j$ and the tolerance $\epsilon_k = \eta_k\|\mathbf g_k\|$.

- If $\mathbf d_j^{\mathsf T}\nabla^2f_k\mathbf d_j\le0$ (negative curvature), stop. Return $\mathbf p_k = -\mathbf g_k$ if this happens at $j = 0$, and the current CG iterate $\mathbf z_j$ otherwise.
- Otherwise continue until $\|\mathbf r_j\|\le\epsilon_k$ and return $\mathbf z_j$.

Every CG iterate is a descent direction for $f$, so the result can go straight into a Wolfe line search with $\alpha = 1$ tried first. A practical code uses a small positive threshold instead of exactly zero in the curvature test.

The drawback is that a nearly singular Hessian can give very long steps. That is the motivation for the trust-region version.

**Trust-region Newton–CG (Steihaug).** Run the same CG inside a trust region ([[trust-region-methods]], Algorithm 4.3). On negative curvature, or on leaving the ball, go along the current direction to the boundary and stop. The step is never longer than $\Delta$, and directions of negative curvature are *used* rather than discarded. This is SciPy's `method="trust-ncg"`. With preconditioning, the trust region must be measured in the corresponding weighted norm.

## Hessian–vector products without the Hessian

If only $\mathbf g$ is available, one extra gradient gives (Eq. (6.7))

$$
\nabla^2f_k\,\mathbf v\approx\frac{\mathbf g(\mathbf x_k+h\mathbf v)-\mathbf g(\mathbf x_k)}{h},
$$

with $h\approx\sqrt{u}\,(1+\|\mathbf x_k\|)/\|\mathbf v\|$ ($u$ = unit roundoff). Automatic differentiation gives exact products at a small multiple of the cost of a gradient (N&W Ch. 7; planned for Chapter 6 of this part). Each CG iteration then costs one gradient. Newton–CG competes with L-BFGS when gradients are cheap relative to the curvature information they buy ([[limited-memory-bfgs]]).

!!! example "Worked example: chained Rosenbrock, n = 1000"
    Exact Hessian-vector products. Wolfe line search with unit step first. Stop at $\|\mathbf g\|\le10^{-8}$.

    **From $x_i = 1+0.5\sin i$:**

    | forcing | Newton iterations | CG iterations (= Hessian–vector products) |
    |---|---:|---:|
    | $\eta_k = 0.5$ | 33 | 105 |
    | $\eta_k = \min(0.5,\sqrt{\|\mathbf g_k\|})$ | 21 | 109 |
    | $\eta_k = \min(0.5,\|\mathbf g_k\|)$ | 20 | 128 |

    Replacing the exact products by the finite difference (6.7) changes nothing visible: 21 iterations, 109 CG steps, final error $6\times10^{-14}$. SciPy's Newton-CG needs 28 iterations and 181 Hessian products; its `trust-ncg` needs 27 and 167. L-BFGS ($m = 5$) to the same tolerance needs 111 gradient evaluations.

    **Local rates**, from $\mathbf x^*+0.05\times$(random), last iterations. ‖g‖ is shown with CG steps in parentheses; 0 means below $10^{-16}$.

    | forcing | last gradient norms (CG steps) |
    |---|---|
    | $\eta = 0.5$ | $1.6\times10^{-12}(2)$, $9.7\times10^{-13}(2)$, $5.5\times10^{-13}(1)$, $2.8\times10^{-13}(3)$, $1.4\times10^{-13}(12)$, $5.0\times10^{-14}(1)$ |
    | $\min(0.5,\sqrt{\|\mathbf g\|})$ | $8.0\times10^{-3}(3)$, $1.3\times10^{-3}(14)$, $4.8\times10^{-5}(5)$, $2.5\times10^{-7}(18)$, $1.2\times10^{-10}(12)$, 0 (27) |
    | $\min(0.5,\|\mathbf g\|)$ | $2.0\times10^{-1}(1)$, $2.5\times10^{-2}(3)$, $1.3\times10^{-3}(16)$, $1.5\times10^{-6}(10)$, $1.6\times10^{-10}(30)$, 0 (43) |

    The three rates of Thm. 6.2 are visible:

    - with $\eta = 0.5$, a factor of about 0.5 per iteration (44 iterations in all);
    - with the $\sqrt{\cdot}$ rule, ratios that keep shrinking (superlinear, 20 iterations);
    - with $\eta = O(\|\mathbf g\|)$, $1.3\times10^{-3}\to1.5\times10^{-6}\to1.6\times10^{-10}$, roughly squaring (17 iterations).

    The faster rates cost more CG steps per Newton iteration near the end.

## Source

Nocedal and Wright, *Numerical Optimization* (Springer, New York, 1999), Ch. 6, Secs. 6.1-6.2, 6.4, pp. 136-141, 154-160, Thms. 6.1-6.2, Algorithm 6.1, Eqs. (6.1)-(6.7); Ch. 4, Algorithm 4.3, pp. 74-76. Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 15.10, p. 490 (truncated Newton).

The step-size rule for $h$ is the usual choice, not a formula from N&W Ch. 6. Numbers: `Claude outputs/part7_ch2_numerical_optimization.py`, section J.
