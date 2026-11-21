---
id: choosing-an-unconstrained-optimizer
title: Choosing an unconstrained optimizer
summary: Synopsis of the chapter. Which method to use given what can be computed (f only, gradient, Hessian–vector products, full Hessian), the size of the problem and whether the Hessian may be indefinite; what each costs per iteration; how scipy.optimize's methods map onto the algorithms of N&W; measured comparisons on Rosenbrock and an RHF/STO-3G water geometry optimization with PySCF gradients; and what this chapter does not yet cover (RFO and saddle-point searches, internal coordinates, noisy objectives).
status: in-progress
kind: comparison
level: intermediate
tags: [optimization, scipy-optimize, bfgs, l-bfgs, newton-cg, trust-region, geometry-optimization, pyscf, synopsis]
prerequisites: [bfgs-method, trust-region-methods, limited-memory-bfgs, inexact-newton-and-newton-cg]
related: [geometry-optimization, nonlinear-conjugate-gradient, sr1-and-the-broyden-class, exact-trust-region-step-and-hessian-modification, variational-quantum-eigensolver, choosing-a-symmetric-eigensolver]
order: 110
date: 2026-11-21
---

## Overview

All the methods of this chapter look for $\mathbf g = 0$ and differ in what they assume can be computed. In electronic structure the energy and gradient are usually available analytically ([[analytic-gradients-and-force-constants]]). A Hessian costs roughly $n$ gradients, but Hessian–vector products can be cheap. A single evaluation often takes minutes, so the count of energy+gradient evaluations is the cost that matters, not the linear algebra of the optimizer.

## Decision table

| available | $n$ | method | per-iteration work beyond $f$, $\mathbf g$ | note |
|---|---|---|---|---|
| $f$, $\mathbf g$ | up to $\sim10^3$ | BFGS + Wolfe line search | $O(n^2)$ | default; superlinear ([[bfgs-method]]) |
| $f$, $\mathbf g$ | large | L-BFGS, $m = 3$–20 | $4mn$ | ([[limited-memory-bfgs]]) |
| $f$, $\mathbf g$, memory-starved | large | nonlinear CG (PR+) | $O(n)$ | needs $c_2\approx0.1$ ([[nonlinear-conjugate-gradient]]) |
| $f$, $\mathbf g$, $\nabla^2f\,\mathbf v$ | large | Newton–CG, line search or trust region | CG iterations | rate set by forcing ([[inexact-newton-and-newton-cg]]) |
| $f$, $\mathbf g$, $\nabla^2f$ | small/medium | trust region, exact subproblem | one or a few Cholesky | handles indefinite Hessians ([[exact-trust-region-step-and-hessian-modification]]) |
| $f$, $\mathbf g$, indefinite model wanted | small/medium | SR1 + trust region | $O(n^2)$ | can model negative curvature ([[sr1-and-the-broyden-class]]) |
| $f$ only | small | finite-difference gradients + the above | $n$ extra $f$ per gradient | (N&W Ch. 7) |

The table summarizes Chs. 3-9 of N&W; the choices in the rightmost columns are argued in the linked notes. Steepest descent appears nowhere. It is only a safe first step, or the fallback inside other methods ([[steepest-descent-newton-and-superlinear-convergence]]).

**Line search or trust region.** Both are globally convergent with the right safeguards. A trust region is more natural when the model Hessian can be indefinite (exact Hessian, SR1), or when a step must be bounded, as in geometry optimization, where very long steps are unphysical. A line search is more natural with a PD quasi-Newton matrix (BFGS).

## What scipy.optimize calls

| `scipy.optimize.minimize(method=...)` | algorithm | needs |
|---|---|---|
| `"CG"` | nonlinear CG, Polak–Ribière variant | `jac` |
| `"BFGS"` | BFGS with a Wolfe line search; returns `hess_inv` | `jac` (else finite differences) |
| `"L-BFGS-B"` | L-BFGS with simple bounds (Byrd, Lu, Nocedal, Zhu) | `jac`; `maxcor` = $m$ |
| `"Newton-CG"` | line-search Newton–CG (truncated Newton) | `jac`, `hess` or `hessp` |
| `"dogleg"` | trust region, dogleg step | `jac`, `hess` (must be PD) |
| `"trust-ncg"` | trust region, Steihaug CG | `jac`, `hess` or `hessp` |
| `"trust-krylov"` | trust region, GLTR (Lanczos-based) subproblem | `jac`, `hess` or `hessp` |
| `"trust-exact"` | trust region, nearly exact subproblem (Moré–Sorensen type) | `jac`, `hess` (may be indefinite) |

The descriptions are from the SciPy documentation (SciPy 1.18), which cites the second edition of Nocedal and Wright for most of these. Defaults to know:

- `gtol` (gradient-norm tolerance) is $10^{-5}$ for BFGS and CG;
- the convergence test uses the infinity norm unless `norm` is changed;
- convergence tests are always in the units of `x`. For geometry optimization, choose the coordinates (bohr or Å) and the tolerance together.

!!! example "Measured comparisons"
    **Rosenbrock from $(-1.2,1)$**, default tolerances, exact derivatives:

    | method | iterations | $f$ evaluations | $\|\mathbf x-\mathbf x^*\|$ |
    |---|---:|---:|---:|
    | CG | 36 | 78 | $6\times10^{-9}$ |
    | BFGS | 32 | 39 | $6\times10^{-8}$ |
    | L-BFGS-B | 36 | 44 | $2\times10^{-6}$ |
    | Newton-CG | 83 | 105 | $4\times10^{-5}$ |
    | dogleg | 23 | 24 | $4\times10^{-6}$ |
    | trust-ncg | 29 | 30 | $7\times10^{-7}$ |
    | trust-krylov | 36 | 37 | $2\times10^{-4}$ |
    | trust-exact | 25 | 26 | $1\times10^{-9}$ |

    The final errors reflect the different default stopping rules as much as the methods. Compare evaluation counts.

    **Water, RHF/STO-3G**, all nine Cartesian coordinates, PySCF energies and analytic gradients (`conv_tol` $10^{-11}$), from R(OH) = 0.99/1.00 Å with a distorted angle, `gtol` $= 10^{-6}$:

    | method | iterations | SCF+gradient calls | final $E$ ($E_h$) |
    |---|---:|---:|---:|
    | SciPy BFGS | 6 | 7 | $-74.9659011923$ |
    | SciPy L-BFGS-B | 6 | 8 | $-74.9659011923$ |
    | SciPy CG | 8 | 14 | $-74.9659011923$ |
    | own BFGS (Algorithm 8.1, strong Wolfe, $\mathbf H_0$ rescaled) | 6 | 7 | $-74.9659011923$ |
    | steepest descent, to $\|\mathbf g\|\le10^{-4}$ only | 18 | 35 | $-74.9659011841$ |

    All converge to R(OH) = 0.98941 Å and HOH = 100.03°, the RHF/STO-3G minimum of [[geometry-optimization]].

    - Translations and rotations need no special treatment here: the gradient has no component along them, so no step is taken in those directions.
    - Steepest descent is five times as expensive and still $8\times10^{-9}\,E_h$ above the minimum.

## Not covered by this chapter's source

The first edition of N&W, the source for the rest of this chapter, does not cover the following. They stay planned until a proper source is in the library:

- **Rational-function (RFO) and partitioned-RFO steps, eigenvector following, and saddle-point (transition-state) searches** with Bofill-type Hessian updates. These are the standard steps of quantum-chemistry optimizers, related to the level-shifted Newton step of [[exact-trust-region-step-and-hessian-modification]].
- **Coordinate systems for molecules:** the Wilson B matrix, redundant and delocalized internal coordinates, and translation–rotation internal coordinates. Levine (Sec. 15.10) cites Baker et al. (1996, 1999) and Bakken and Helgaker (2002) for these.
- **Derivative-free and noise-tolerant optimizers** (Nelder–Mead, COBYLA, SPSA), and convergence tests when the gradient carries statistical noise, as for sampled quantum energies ([[variational-quantum-eigensolver]]).

## Source

Nocedal and Wright, *Numerical Optimization* (Springer, New York, 1999), Chs. 2-9, in particular Sec. 2.2, pp. 19-30, and Ch. 6, pp. 134-162.

The SciPy mapping is from the docstrings of `scipy.optimize.minimize` and its method functions (SciPy 1.18.1). Numbers: `Claude outputs/part7_ch2_numerical_optimization.py`, section K.
