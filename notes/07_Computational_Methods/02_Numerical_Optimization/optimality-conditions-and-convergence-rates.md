---
id: optimality-conditions-and-convergence-rates
title: Optimality conditions, the two strategies, and rates of convergence
summary: When is x* a local minimizer of a smooth f? First-order necessary (∇f = 0), second-order necessary (Hessian positive semidefinite) and second-order sufficient (Hessian positive definite) conditions, with proofs from Taylor's theorem. The two algorithmic strategies (line search and trust region), the standard search directions (steepest descent, Newton, quasi-Newton), and the definitions of Q-linear, Q-superlinear and Q-quadratic convergence that every later note uses. Rosenbrock's function as the running example.
status: in-progress
kind: theory
level: intermediate
tags: [unconstrained-optimization, optimality-conditions, stationary-point, hessian, line-search, trust-region, rate-of-convergence, rosenbrock]
prerequisites: [matrix-eigenvalue-problem]
related: [stationary-points-and-reaction-paths, geometry-optimization, line-searches-and-wolfe-conditions, trust-region-methods, floating-point-and-eigenvalue-perturbation]
key: q-linear
order: 10
date: 2026-11-21
---

## Overview

Geometry optimization, orbital optimization and the classical outer loop of VQE all minimize a smooth function $f:\mathbb R^n\to\mathbb R$ without constraints. The rest of this chapter is about algorithms. This note fixes three things first:

- what counts as a solution;
- the two ways algorithms move toward one;
- how their speed is measured.

## Notation

- $\mathbf g(\mathbf x) = \nabla f(\mathbf x)$ is the gradient and $\nabla^2f(\mathbf x)$ the Hessian; along an iteration, $f_k = f(\mathbf x_k)$ and $\mathbf g_k = \mathbf g(\mathbf x_k)$.
- $\mathbf p_k$ is a step or search direction.
- $\mathbf B_k$ is a symmetric model Hessian and $\mathbf H_k = \mathbf B_k^{-1}$.
- A matrix is positive definite (PD) if $\mathbf p^{\mathsf T}\mathbf B\mathbf p>0$ for all $\mathbf p\ne0$, and positive semidefinite (PSD) if $\ge0$.

## What is a solution

A point $\mathbf x^*$ is a **local minimizer** if $f(\mathbf x^*)\le f(\mathbf x)$ for all $\mathbf x$ in a neighbourhood of $\mathbf x^*$. It is **strict** if the inequality is strict for $\mathbf x\ne\mathbf x^*$, and **global** if it holds for all $\mathbf x$. Algorithms in this chapter find local minimizers only. For a molecular potential energy surface there may be very many of them.

Everything rests on Taylor's theorem (N&W Thm. 2.1). For twice continuously differentiable $f$ and some $t\in(0,1)$:

$$
f(\mathbf x+\mathbf p) = f(\mathbf x) + \mathbf g(\mathbf x)^{\mathsf T}\mathbf p + \tfrac12\mathbf p^{\mathsf T}\nabla^2f(\mathbf x+t\mathbf p)\,\mathbf p .
\label{taylor}
$$

**First-order necessary condition** (Thm. 2.2). If $\mathbf x^*$ is a local minimizer and $f$ is $C^1$ near it, then $\mathbf g(\mathbf x^*) = 0$.

*Proof.* Suppose $\mathbf g^* = \mathbf g(\mathbf x^*)\ne0$ and take $\mathbf p = -\mathbf g^*$. Then $\mathbf p^{\mathsf T}\mathbf g^* = -\|\mathbf g^*\|^2<0$, and by continuity $\mathbf p^{\mathsf T}\mathbf g(\mathbf x^*+t\mathbf p)<0$ for all $t\in[0,T]$. By the first-order form of Eq. [[#taylor]], $f(\mathbf x^*+\bar t\mathbf p)<f(\mathbf x^*)$ for every $\bar t\in(0,T]$, a contradiction. $\square$

A point with $\mathbf g = 0$ is a **stationary point**.

**Second-order necessary condition** (Thm. 2.3). If $\mathbf x^*$ is a local minimizer and $\nabla^2f$ is continuous near it, then $\mathbf g^* = 0$ and $\nabla^2f(\mathbf x^*)$ is PSD. The proof is the same, along a direction with $\mathbf p^{\mathsf T}\nabla^2f\,\mathbf p<0$, using Eq. [[#taylor]].

**Second-order sufficient condition** (Thm. 2.4). If $\mathbf g^* = 0$ and $\nabla^2f(\mathbf x^*)$ is PD, then $\mathbf x^*$ is a strict local minimizer.

*Proof.* The Hessian stays PD on a small ball around $\mathbf x^*$. For any $\mathbf p\ne0$ in that ball, Eq. [[#taylor]] gives $f(\mathbf x^*+\mathbf p) = f(\mathbf x^*)+\tfrac12\mathbf p^{\mathsf T}\nabla^2f(\mathbf z)\mathbf p>f(\mathbf x^*)$. $\square$

The sufficient condition is not necessary: $f = x^4$ has a strict minimizer at 0, where $f'' = 0$.

**Convex functions** (Thm. 2.5): every local minimizer is global, and every stationary point is a global minimizer.

On a potential energy surface the same eigenvalue test classifies stationary points ([[stationary-points-and-reaction-paths]]). A PD Hessian (after removing translations and rotations) means a minimum; exactly one negative eigenvalue means a first-order saddle point. The algorithms here look for $\mathbf g = 0$. Whether they find a minimum depends on keeping the model Hessian PD or on checking curvature.

## Two strategies

**Line search.** Choose a direction $\mathbf p_k$, then a step length $\alpha_k>0$ that approximately minimizes $f(\mathbf x_k+\alpha\mathbf p_k)$, and set $\mathbf x_{k+1} = \mathbf x_k+\alpha_k\mathbf p_k$ ([[line-searches-and-wolfe-conditions]]).

**Trust region.** Build the quadratic model

$$
m_k(\mathbf p) = f_k + \mathbf g_k^{\mathsf T}\mathbf p + \tfrac12\mathbf p^{\mathsf T}\mathbf B_k\mathbf p ,
\label{model}
$$

and minimize it approximately inside a ball $\|\mathbf p\|\le\Delta_k$ where it is trusted. Then accept or reject the step and adjust $\Delta_k$ from the agreement between $f$ and $m_k$ ([[trust-region-methods]]).

The two differ in order: a line search fixes the direction first and then the distance, a trust region fixes the distance first and then the direction.

**Search directions.**

| Direction | formula | needs | local rate |
|---|---|---|---|
| steepest descent | $\mathbf p_k = -\mathbf g_k$ | gradient | linear, constant set by $\kappa(\nabla^2f^*)$ |
| Newton | $\mathbf p_k = -(\nabla^2f_k)^{-1}\mathbf g_k$ | Hessian (PD for descent) | quadratic |
| quasi-Newton | $\mathbf p_k = -\mathbf B_k^{-1}\mathbf g_k$, $\mathbf B_{k+1}\mathbf s_k = \mathbf y_k$ | gradients only | superlinear |
| nonlinear CG | $\mathbf p_k = -\mathbf g_k+\beta_k\mathbf p_{k-1}$ | gradients, $O(n)$ memory | linear to superlinear |

Here $\mathbf s_k = \mathbf x_{k+1}-\mathbf x_k$ and $\mathbf y_k = \mathbf g_{k+1}-\mathbf g_k$. The quasi-Newton condition $\mathbf B_{k+1}\mathbf s_k = \mathbf y_k$ (the secant equation) mimics $\nabla^2f_{k+1}\mathbf s_k\approx\mathbf y_k$, which follows from Eq. [[#taylor]] applied to $\mathbf g$ ([[bfgs-method]]).

**Scaling.** A problem is poorly scaled when changes of $\mathbf x$ in some directions change $f$ far more than in others, as with bond stretches against torsions. Steepest descent is sensitive to scaling. Newton's method is invariant under linear changes of variables, and quasi-Newton methods are nearly so.

## Rates of convergence

Let $\mathbf x_k\to\mathbf x^*$ and $e_k = \|\mathbf x_k-\mathbf x^*\|$. The convergence is

$$
\text{Q-linear:}\quad \frac{e_{k+1}}{e_k}\le r<1\ \ \text{for large }k;\qquad
\text{Q-superlinear:}\quad \frac{e_{k+1}}{e_k}\to0;\qquad
\text{Q-quadratic:}\quad e_{k+1}\le M e_k^2 .
\label{q-linear}
$$

Quadratic implies superlinear, and superlinear implies linear. Linear convergence gains a fixed number of digits per iteration ($-\log_{10}r$). Quadratic convergence roughly doubles the number of correct digits per iteration. N&W also define R-rates, which bound $e_k$ by a sequence that converges at the corresponding Q-rate. They are needed when $e_k$ itself is not monotone.

!!! example "Worked example: Rosenbrock's function and model sequences"
    $f(x_1,x_2) = 100(x_2-x_1^2)^2+(1-x_1)^2$, the standard test case, with a curved narrow valley.

    - $\mathbf x^* = (1,1)$, $f^* = 0$, $\mathbf g^* = 0$.
    - $\nabla^2f^* = \begin{pmatrix}802&-400\\-400&200\end{pmatrix}$, eigenvalues $0.39936$ and $1001.60$. Both are positive, so the sufficient condition holds and $\kappa = 2508$.
    - At the standard start $\mathbf x_0 = (-1.2,1)$: $f = 24.2$, $\mathbf g = (-215.6,-88.0)$, Hessian eigenvalues $23.63$ and $1506.37$.

    Model error sequences:

    | $k$ | linear, $r = 0.5$ | superlinear, $1/k!$ | quadratic, $e_{k+1} = e_k^2$, $e_0 = 0.5$ |
    |---:|---:|---:|---:|
    | 2 | $2.5\times10^{-1}$ | $5.0\times10^{-1}$ | $6.3\times10^{-2}$ |
    | 4 | $6.3\times10^{-2}$ | $4.2\times10^{-2}$ | $1.5\times10^{-5}$ |
    | 6 | $1.6\times10^{-2}$ | $1.4\times10^{-3}$ | $5.4\times10^{-20}$ |

## Source

Nocedal and Wright, *Numerical Optimization* (Springer, New York, 1999), Ch. 2, Secs. 2.1-2.2, pp. 13-30, Thms. 2.1-2.5, Eqs. (2.4)-(2.21).

Numbers: `Claude outputs/part7_ch2_numerical_optimization.py`, section A.
