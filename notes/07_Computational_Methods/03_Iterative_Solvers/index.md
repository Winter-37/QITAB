Iterative methods for eigenvalue problems, linear systems and nonlinear equations whose matrices are too large to store or factorize, and are known only through matrix–vector products.

## What this chapter is about

Large electronic-structure calculations end in three kinds of problem:

- **a few eigenpairs** of a huge symmetric matrix: CI, CIS, response and EOM excitation energies;
- **linear systems**: CPHF, CPCI, Z-vector equations, Newton steps of second-order SCF;
- **nonlinear systems and fixed points**: coupled-cluster amplitude equations, the SCF iteration.

The matrix is never formed. A program supplies products $\mathbf A\mathbf v$ (a $\sigma$ vector, a Fock-like build, a CC residual), and the solver must use as few of them as possible. This chapter covers the subspace methods for eigenpairs (Rayleigh–Ritz, Lanczos, Davidson, Jacobi–Davidson), conjugate gradients with and without preconditioning, Newton and Broyden methods for nonlinear equations, and DIIS.

## Why it matters

Each product costs as much as a whole small calculation, so the solver decides what is feasible. Several practical facts are settled here:

- why the residual norm, not the change in energy, is the convergence test;
- why a Davidson preconditioner that is *too good* stalls, and how the projected (Jacobi–Davidson) correction cures it;
- why CG needs about $\sqrt\kappa$ iterations, why clustered spectra help, and why the orbital-energy diagonal is such a good preconditioner;
- why a Newton line search on $\tfrac12\lVert\mathbf r\rVert^2$ can stall away from any root;
- why DIIS is cheap, why it needs the affine constraint, and why it cannot invent directions the underlying iteration does not supply.

## The main ideas, in order

1. **Extraction.** Rayleigh–Ritz in a subspace; eigenvalue bounds; failure for interior eigenpairs; harmonic Ritz and residual minimization.
2. **Krylov spaces.** The Lanczos three-term recurrence, tridiagonal projection, convergence of extreme eigenvalues, and ghost copies when orthogonality is lost.
3. **Preconditioned updates.** The correction equation; Davidson's diagonal step; the trap of an exact inverse; Jacobi–Davidson, identical to HJO's quasi-Newton CI step.
4. **Linear CG.** Conjugate directions, the two-term recurrence, Krylov optimality, termination for few distinct eigenvalues, the $2((\sqrt\kappa-1)/(\sqrt\kappa+1))^k$ bound.
5. **Preconditioned CG.** Algorithm 5.3, preconditioner choices, CPHF for the polarizability of water.
6. **Nonlinear equations.** Newton, inexact Newton, Broyden's secant update, merit functions and Powell's example.
7. **DIIS.** The bordered least-squares system, error vectors for SCF, CC and linear response, history length and conditioning.
8. **Choosing a solver**, and what SciPy and PySCF call.

## How to read it

**Path.**

1. [[rayleigh-ritz-and-harmonic-ritz]]
2. [[lanczos-and-krylov-subspaces]]
3. [[davidson-and-jacobi-davidson-methods]]
4. [[linear-conjugate-gradient-method]]
5. [[preconditioned-conjugate-gradient]]
6. [[newton-and-broyden-methods-for-nonlinear-equations]]
7. [[diis-extrapolation]]
8. [[choosing-an-iterative-solver]] (the synopsis)

**Needs.** Chapter 1 of this part (perturbation bounds, tridiagonal eigensolvers, Cholesky) and Chapter 2 (convergence rates, line searches, steepest descent, quasi-Newton updates, Newton–CG). For the examples: CI in determinants (Part 4, Chapter 9), CPHF (Part 4, Chapter 15), the SCF iteration (Part 4, Chapters 3 and 7) and coupled-cluster theory (Part 4, Chapter 11).

**Leads to.** Large CI and excited-state calculations ([[ci-optimization-newton-and-davidson]], [[ci-in-practice]]); response properties and analytic derivatives ([[cphf-closed-shell]], [[z-vector-method]]); SCF and CC convergence ([[scf-convergence-diis-and-newton]], [[coupled-cluster-optimization-and-lagrangian]]). Chapters 4 and 5 of this part (parallel and high-performance computing) take the products as given and make them fast.

**Core (first pass).** [[rayleigh-ritz-and-harmonic-ritz]], [[davidson-and-jacobi-davidson-methods]], [[linear-conjugate-gradient-method]], [[diis-extrapolation]], [[choosing-an-iterative-solver]].

**Deep (second pass).** [[lanczos-and-krylov-subspaces]], [[preconditioned-conjugate-gradient]], [[newton-and-broyden-methods-for-nonlinear-equations]].

**Checkpoint.** Show that Davidson's update with the exact inverse of $\mathbf A-\theta\mathbf1$ returns the current Ritz vector, and derive the projected correction $\mathbf q = -\mathbf M^{-1}\mathbf r+\varepsilon\mathbf M^{-1}\mathbf x$. Then explain why CG on a matrix with five large outliers and a tight cluster converges in a few more than five iterations.

**Source.** B. Steffen, "Subspace Methods for Sparse Eigenvalue Problems", in Grotendorst (ed.), *Modern Methods and Algorithms of Quantum Chemistry* (NIC, 2000); Nocedal and Wright, *Numerical Optimization* (first edition, 1999), Ch. 5.1 and Ch. 11; Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (2000), Secs. 10.6.2, 11.5.3 and 13.4. Every number is checked by `Claude outputs/part7_ch3_iterative_solvers.py`. Book slips found on the way: N&W's CG bound (5.35) is printed with exponent $2k$ and without the factor 2; N&W's Algorithm 5.3 starts with $\mathbf p_0 = -\mathbf r_0$ instead of $-\mathbf y_0$; Steffen's harmonic-Ritz example vectors could not be reproduced (to verify).

**Planned sections:** GMRES and MINRES (minimal residual methods, restarts); Arnoldi and implicitly restarted Lanczos (ARPACK); Nonsymmetric Davidson for EOM-CC; Anderson acceleration and the relation of DIIS to Krylov methods; Block CG for many right-hand sides.
