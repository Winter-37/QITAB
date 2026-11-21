How the minimizations behind geometry optimization, orbital optimization and variational algorithms are actually carried out, and how fast they converge.

## What this chapter is about

Many tasks in this notebook are unconstrained minimizations of a smooth function $f(\mathbf x)$: a Born–Oppenheimer energy over nuclear coordinates, an SCF or MCSCF energy over orbital rotations, a VQE energy over circuit parameters. The method chapters write down $f$, its gradient and sometimes its Hessian. This chapter covers the general algorithms that turn those into a converged answer:

- line searches;
- trust regions;
- Newton, quasi-Newton (BFGS, SR1, L-BFGS), nonlinear conjugate-gradient and Newton–CG methods.

It also covers the theory that says when they converge and how fast.

## Why it matters

The cost of an optimization is the number of energy and gradient evaluations, and in quantum chemistry each one is an expensive calculation. Several practical questions are settled by the results of this chapter:

- why codes use BFGS with a Wolfe line search rather than steepest descent;
- why the first trial step must be $\alpha = 1$;
- why updates must keep $\mathbf s^{\mathsf T}\mathbf y>0$;
- why a model Hessian with negative curvature needs a trust region;
- how loosely the Newton equations may be solved without losing the quadratic rate.

## The main ideas, in order

1. **Solutions and rates.** $\mathbf g = 0$ with a positive definite Hessian; line search versus trust region; Q-linear, superlinear and quadratic convergence.
2. **Line searches.** The Wolfe conditions, Zoutendijk's theorem, interpolation and the bracketing–zoom algorithm.
3. **Local rates.** Steepest descent is linear with factor $((\kappa-1)/(\kappa+1))^2$, Newton is quadratic, and quasi-Newton methods are superlinear exactly under the Dennis–Moré condition.
4. **Trust regions.** The ratio test, the Cauchy point, the dogleg and Steihaug steps.
5. **Indefinite Hessians.** The exact trust-region step $(\mathbf B+\lambda\mathbf 1)\mathbf p = -\mathbf g$, the hard case, and Hessian modification for line searches.
6. **Quasi-Newton updates.** The secant equation and curvature condition; DFP and BFGS as closest updates; SR1 and the Broyden class.
7. **Large problems.** L-BFGS (two-loop recursion), nonlinear CG, and Newton–CG with forcing sequences.
8. **Choosing a method**, and what SciPy calls.

## How to read it

**Path.**

1. [[optimality-conditions-and-convergence-rates]]
2. [[line-searches-and-wolfe-conditions]]
3. [[steepest-descent-newton-and-superlinear-convergence]]
4. [[trust-region-methods]]
5. [[exact-trust-region-step-and-hessian-modification]]
6. [[bfgs-method]]
7. [[sr1-and-the-broyden-class]]
8. [[limited-memory-bfgs]]
9. [[nonlinear-conjugate-gradient]]
10. [[inexact-newton-and-newton-cg]]
11. [[choosing-an-unconstrained-optimizer]] (the synopsis)

**Needs.** Part 0, Chapter 1 (eigenvalues, positive definiteness) and Chapter 1 of this part (Cholesky factorization, for the exact trust-region step). Gradients and Hessians of molecular energies are in Part 4, Chapter 15.

**Leads to.** Chapter 3 (iterative solvers: linear CG, Krylov methods, DIIS, Broyden's method for nonlinear equations). Molecular geometry optimization in Part 4, Chapter 16 ([[geometry-optimization]]). Second-order SCF and MCSCF in Part 4, Chapters 7 and 13. The classical optimizer of VQE in Part 6.

**Core (first pass).** [[optimality-conditions-and-convergence-rates]], [[line-searches-and-wolfe-conditions]], [[trust-region-methods]], [[bfgs-method]], [[choosing-an-unconstrained-optimizer]].

**Deep (second pass).** [[steepest-descent-newton-and-superlinear-convergence]], [[exact-trust-region-step-and-hessian-modification]], [[sr1-and-the-broyden-class]], [[limited-memory-bfgs]], [[nonlinear-conjugate-gradient]], [[inexact-newton-and-newton-cg]].

**Checkpoint.** Show that a Wolfe step guarantees $\mathbf y^{\mathsf T}\mathbf s>0$, and that the BFGS update then stays positive definite. Then explain why a transition-state search cannot use BFGS as it stands.

**Source.** Nocedal and Wright, *Numerical Optimization* (first edition, 1999), Chapters 2-9, with Levine Sec. 15.10 for the molecular context. Every number is checked by `Claude outputs/part7_ch2_numerical_optimization.py`. Constrained optimization and Lagrange multipliers (N&W Chs. 12-18) belong to Part 0, Chapter 6. Finite-difference and automatic differentiation (N&W Ch. 7) belong to Chapter 6 of this part.

**Planned sections:** Rational-function (RFO, P-RFO) and eigenvector-following steps; Saddle-point searches and Bofill-type updates; Internal coordinates for molecules (Wilson B matrix, redundant and translation–rotation internals); Derivative-free and noise-tolerant optimizers; Nonlinear least squares (Gauss–Newton, Levenberg–Marquardt).
