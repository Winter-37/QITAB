---
id: line-searches-and-wolfe-conditions
title: Line searches and the Wolfe conditions
summary: How far to move along a descent direction. Sufficient decrease (Armijo) plus a curvature condition give the (strong) Wolfe conditions; acceptable steps always exist, and Zoutendijk's theorem turns them into global convergence whenever the direction stays away from orthogonal to the gradient. Goldstein conditions and backtracking as alternatives, quadratic and cubic interpolation, the choice of the first trial step, and the bracketing-plus-zoom algorithm that finds a strong-Wolfe point, with a traced example on Rosenbrock.
status: in-progress
kind: algorithm
level: intermediate
tags: [line-search, wolfe-conditions, armijo, sufficient-decrease, curvature-condition, goldstein, backtracking, zoutendijk, cubic-interpolation]
prerequisites: [optimality-conditions-and-convergence-rates]
related: [bfgs-method, nonlinear-conjugate-gradient, steepest-descent-newton-and-superlinear-convergence, geometry-optimization]
key: wolfe
order: 20
date: 2026-11-21
---

## Overview

A line-search method iterates

$$
\mathbf x_{k+1} = \mathbf x_k + \alpha_k\mathbf p_k,\qquad \mathbf g_k^{\mathsf T}\mathbf p_k<0
\label{ls}
$$

($\mathbf p_k$ a descent direction). Minimizing $\phi(\alpha) = f(\mathbf x_k+\alpha\mathbf p_k)$ exactly is expensive and unnecessary. Each trial $\alpha$ costs one evaluation of $f$ (and usually $\mathbf g$), which in quantum chemistry is a full electronic-structure calculation. What global convergence needs is only an $\alpha$ that gives enough decrease and is not too short. Note that $\phi'(\alpha) = \mathbf g(\mathbf x_k+\alpha\mathbf p_k)^{\mathsf T}\mathbf p_k$.

## The Wolfe conditions

**Sufficient decrease (Armijo):**

$$
f(\mathbf x_k+\alpha\mathbf p_k)\le f_k + c_1\alpha\,\mathbf g_k^{\mathsf T}\mathbf p_k,\qquad c_1\in(0,1).
\label{armijo}
$$

The right side is a line through $\phi(0)$ with slope $c_1\phi'(0)$, flatter than $\phi$ at 0. Every small enough $\alpha$ satisfies Eq. [[#armijo]], so on its own it does not exclude uselessly short steps. In practice $c_1$ is small, e.g. $10^{-4}$.

**Curvature condition:**

$$
\mathbf g(\mathbf x_k+\alpha\mathbf p_k)^{\mathsf T}\mathbf p_k\ge c_2\,\mathbf g_k^{\mathsf T}\mathbf p_k,\qquad c_2\in(c_1,1).
\label{curv}
$$

The slope at $\alpha$ must be less negative than $c_2$ times the initial slope. If $\phi$ is still falling steeply, a longer step would pay. Together, Eqs. [[#armijo]] and [[#curv]] with $0<c_1<c_2<1$ are the **Wolfe conditions** (N&W Eq. (3.6)).

The **strong Wolfe conditions** (Eq. (3.7)) replace Eq. [[#curv]] by

$$
|\mathbf g(\mathbf x_k+\alpha\mathbf p_k)^{\mathsf T}\mathbf p_k|\le c_2\,|\mathbf g_k^{\mathsf T}\mathbf p_k| ,
\label{wolfe}
$$

which also excludes points where $\phi'$ is large and positive, far beyond a minimizer of $\phi$.

Typical values for $c_2$:

- 0.9 for Newton and quasi-Newton directions;
- 0.1 for nonlinear conjugate gradients, which need a more accurate search ([[nonlinear-conjugate-gradient]]).

**Existence** (Lemma 3.1). Let $\phi$ be smooth and bounded below on $\alpha>0$, with $\mathbf p_k$ a descent direction. Then intervals of $\alpha$ satisfying the Wolfe and strong Wolfe conditions exist.

*Proof.* The Armijo line $l(\alpha) = \phi(0)+c_1\alpha\phi'(0)$ decreases without bound while $\phi$ is bounded below, so they intersect. Let $\alpha'$ be the smallest positive intersection; all $\alpha<\alpha'$ satisfy Eq. [[#armijo]]. By the mean value theorem there is $\alpha''\in(0,\alpha')$ with

$$
\phi'(\alpha'') = \frac{\phi(\alpha')-\phi(0)}{\alpha'} = c_1\phi'(0) > c_2\phi'(0) .
$$

So $\alpha''$ satisfies both conditions strictly. Since $\phi'(\alpha'')<0$, it also satisfies Eq. [[#wolfe]], and by continuity so does a neighbourhood of it. $\square$

**Scale invariance.** Multiplying $f$ by a constant, or making an affine change of variables, does not change which $\alpha$ satisfy the Wolfe conditions.

**Goldstein conditions** (Eq. (3.11)):

$$
f_k+(1-c)\alpha\,\mathbf g_k^{\mathsf T}\mathbf p_k\le f(\mathbf x_k+\alpha\mathbf p_k)\le f_k+c\,\alpha\,\mathbf g_k^{\mathsf T}\mathbf p_k,\qquad 0<c<\tfrac12 .
$$

These need only function values to bound the step from below. But the lower bound can exclude every minimizer of $\phi$, so they suit Newton methods better than quasi-Newton methods, which need a positive-definite update.

**Backtracking** (Procedure 3.1). Start from $\bar\alpha$ (= 1 for Newton-type directions) and multiply by $\rho\in(0,1)$ until Eq. [[#armijo]] holds. Because the trial steps shrink geometrically from a reasonable start, the accepted step is not too short. This is adequate for Newton's method, but not for quasi-Newton methods, which need $\mathbf y_k^{\mathsf T}\mathbf s_k>0$ ([[bfgs-method]]). The curvature condition guarantees that: from Eq. [[#curv]], $\mathbf y_k^{\mathsf T}\mathbf s_k\ge(c_2-1)\alpha_k\mathbf g_k^{\mathsf T}\mathbf p_k>0$.

## Global convergence: Zoutendijk's theorem

Let $\theta_k$ be the angle between $\mathbf p_k$ and $-\mathbf g_k$:

$$
\cos\theta_k = \frac{-\mathbf g_k^{\mathsf T}\mathbf p_k}{\|\mathbf g_k\|\,\|\mathbf p_k\|}.
$$

**Theorem 3.2 (Zoutendijk).** Assume:

- $f$ is bounded below and $C^1$ on a neighbourhood of the level set $\{f\le f(\mathbf x_0)\}$;
- $\mathbf g$ is Lipschitz there, with constant $L$;
- every $\mathbf p_k$ is a descent direction and every $\alpha_k$ satisfies the Wolfe conditions.

Then

$$
\sum_{k\ge0}\cos^2\theta_k\,\|\mathbf g_k\|^2<\infty .
\label{zoutendijk}
$$

*Proof.* Eq. [[#curv]] gives $(\mathbf g_{k+1}-\mathbf g_k)^{\mathsf T}\mathbf p_k\ge(c_2-1)\mathbf g_k^{\mathsf T}\mathbf p_k$. The Lipschitz bound gives $(\mathbf g_{k+1}-\mathbf g_k)^{\mathsf T}\mathbf p_k\le\alpha_kL\|\mathbf p_k\|^2$. Together,

$$
\alpha_k\ge\frac{c_2-1}{L}\frac{\mathbf g_k^{\mathsf T}\mathbf p_k}{\|\mathbf p_k\|^2}.
$$

Inserting this into Eq. [[#armijo]] gives $f_{k+1}\le f_k-c\cos^2\theta_k\|\mathbf g_k\|^2$ with $c = c_1(1-c_2)/L$. Summing, and using that $f$ is bounded below, gives the result. $\square$

**Consequence.** If the directions satisfy $\cos\theta_k\ge\delta>0$, then $\|\mathbf g_k\|\to0$.

- Steepest descent has $\cos\theta_k = 1$.
- Newton-like directions $\mathbf p_k = -\mathbf B_k^{-1}\mathbf g_k$ with $\mathbf B_k$ PD and $\kappa(\mathbf B_k)\le M$ have $\cos\theta_k\ge1/M$.

The line search alone does not guarantee a good rate. It guarantees that the iteration cannot stall away from a stationary point.

## Choosing α: interpolation and the first trial

**Interpolation** (Sec. 3.4). From $\phi(0)$, $\phi'(0)$ and a rejected $\phi(\alpha_0)$, take the minimizer of the interpolating quadratic,

$$
\alpha_1 = -\frac{\phi'(0)\,\alpha_0^2}{2[\phi(\alpha_0)-\phi(0)-\phi'(0)\alpha_0]} .
$$

From values and slopes at two points $\alpha_{i-1},\alpha_i$, the cubic interpolant has its minimizer at (N&W Eq. (3.43))

$$
\alpha_{i+1} = \alpha_i-(\alpha_i-\alpha_{i-1})\frac{\phi'(\alpha_i)+d_2-d_1}{\phi'(\alpha_i)-\phi'(\alpha_{i-1})+2d_2},
$$

where $d_1 = \phi'(\alpha_{i-1})+\phi'(\alpha_i)-3\dfrac{\phi(\alpha_{i-1})-\phi(\alpha_i)}{\alpha_{i-1}-\alpha_i}$ and $d_2 = \operatorname{sign}(\alpha_i-\alpha_{i-1})\sqrt{d_1^2-\phi'(\alpha_{i-1})\phi'(\alpha_i)}$.

Trial values too close to an endpoint are replaced by a bisection (safeguarding). Levine's description of the line search in molecular geometry optimization, which fits a cubic or quartic to the energies and gradients at two geometries, is this step ([[geometry-optimization]]).

**First trial step.**

- For Newton and quasi-Newton directions, always try $\alpha = 1$ first. Otherwise the fast local rate never appears.
- For steepest descent and CG, the direction carries no scale. Take $\alpha_0 = \alpha_{k-1}\mathbf g_{k-1}^{\mathsf T}\mathbf p_{k-1}/\mathbf g_k^{\mathsf T}\mathbf p_k$ (same first-order decrease as last time), or $\alpha_0 = 2(f_k-f_{k-1})/\phi'(0)$.

## An algorithm for the strong Wolfe conditions (Algorithms 3.2 and 3.3)

1. **Bracketing.** Increase trial steps $\alpha_1<\alpha_2<\dots$ (e.g. by doubling, up to $\alpha_{\max}$). Stop and accept $\alpha_i$ if it satisfies Eq. [[#wolfe]]. The interval between $\alpha_{i-1}$ and $\alpha_i$ contains acceptable points as soon as any of these holds: $\alpha_i$ violates Eq. [[#armijo]]; $\phi(\alpha_i)\ge\phi(\alpha_{i-1})$; or $\phi'(\alpha_i)\ge0$. Then call **zoom**.
2. **zoom($\alpha_{lo}$, $\alpha_{hi}$).** $\alpha_{lo}$ is the best point so far that satisfies Eq. [[#armijo]], and $\phi'(\alpha_{lo})(\alpha_{hi}-\alpha_{lo})<0$. Repeat:
    - interpolate $\alpha_j$ between them and evaluate it;
    - if it violates Eq. [[#armijo]] or $\phi(\alpha_j)\ge\phi(\alpha_{lo})$, set $\alpha_{hi} = \alpha_j$;
    - otherwise accept $\alpha_j$ if Eq. [[#wolfe]] holds; if $\phi'(\alpha_j)(\alpha_{hi}-\alpha_{lo})\ge0$ set $\alpha_{hi} = \alpha_{lo}$; then set $\alpha_{lo} = \alpha_j$.

Near convergence, $f_k$ and $f_{k-1}$ may agree to machine precision. Practical codes therefore stop after about ten trials, or when the relative change in $\mathbf x$ reaches machine accuracy. N&W recommend established implementations (Moré–Thuente) over one's own. For a loose search ($c_1 = 10^{-4}$, $c_2 = 0.9$) they find the strong and ordinary Wolfe conditions about equally expensive.

!!! example "Worked example: the first steepest-descent step on Rosenbrock"
    At $\mathbf x_0 = (-1.2,1)$, $\mathbf p = -\mathbf g_0 = (215.6, 88.0)$, $\phi(0) = 24.2$, $\phi'(0) = -54227.36$. The exact minimizer along $\mathbf p$ is $\alpha^* = 7.880\times10^{-4}$, with $\phi = 4.1281$.

    | $\alpha$ | $\phi(\alpha)$ | Armijo ($c_1 = 10^{-4}$) | curvature ($c_2 = 0.9$) | strong Wolfe | Goldstein ($c = \tfrac14$) |
    |---:|---:|:-:|:-:|:-:|:-:|
    | $1\times10^{-4}$ | 19.18 | yes | yes | yes | no (too short) |
    | $5\times10^{-4}$ | 6.594 | yes | yes | yes | yes |
    | $1\times10^{-3}$ | 5.353 | yes | yes | yes | yes |
    | $2\times10^{-3}$ | 37.34 | no | yes | no | no |
    | $1\times10^{-2}$ | 93.33 | no | no | no | no |

    The ordinary curvature condition still holds at $\alpha = 2\times10^{-3}$, far past the minimizer, where $\phi'>0$. The strong form excludes such points.

    **Algorithms 3.2/3.3 from $\alpha_1 = 1$** ($\phi(1) = 2.1\times10^{11}$):

    - the bracket is immediate;
    - zoom tries $0.338$, $0.117$, $0.0432$, $0.0186$, $0.0101$, $1.78\times10^{-3}$;
    - it accepts $\alpha = 7.892\times10^{-4}$ with $\phi = 4.12814$ after 8 evaluations in all;
    - tightening to $c_2 = 0.1$ gives the same point here.

    For comparison:

    - backtracking with $\rho = \tfrac12$ needs 11 trials and stops at $\alpha = 2^{-10} = 9.77\times10^{-4}$ ($\phi = 5.101$);
    - `scipy.optimize.line_search` returns $\alpha = 9.38\times10^{-4}$ ($\phi = 4.751$) after 10 function evaluations.

    At the Wolfe point, $\mathbf y^{\mathsf T}\mathbf s = 42.85$, well above the guaranteed bound $(c_2-1)\alpha\,\mathbf g^{\mathsf T}\mathbf p = 4.28$. The Newton direction at $\mathbf x_0$, $\mathbf p_N = (0.0247, 0.3807)$, is accepted with $\alpha = 1$ ($f = 4.732$).

## Source

Nocedal and Wright, *Numerical Optimization* (Springer, New York, 1999), Ch. 3, Secs. 3.1-3.2, 3.4, pp. 36-46, 55-61, Lemma 3.1, Thm. 3.2, Procedure 3.1, Algorithms 3.2-3.3, Eqs. (3.4)-(3.18), (3.40)-(3.44). Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 15.10, pp. 486-488 (line search in molecular geometry optimization).

Numbers: `Claude outputs/part7_ch2_numerical_optimization.py`, section B.
