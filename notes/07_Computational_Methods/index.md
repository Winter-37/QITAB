The numerical and programming techniques behind the methods of Parts 4 and 6.

## What this part is about

Every method in this notebook ends in a computation:

- diagonalizing large matrices;
- solving linear and nonlinear equations iteratively;
- optimizing many parameters;
- organizing code that runs on many cores.

This part collects those algorithms and practices in one place.

## Why it is here

The method chapters state *what* is computed. Whether the computation is feasible depends on *how*:

- **Davidson and Krylov solvers** make large CI and response calculations possible.
- **DIIS and quasi-Newton methods** make SCF and coupled-cluster iterations converge.
- **Low-rank decompositions** reduce memory and cost.

Keeping these in their own part avoids repeating them in every method note.

## How to read it

As a reference, when a method note points here. Chapter 1 (dense symmetric eigensolvers: accuracy, Householder reduction, QR, bisection, divide and conquer, Jacobi, the generalized problem, and which LAPACK driver to use) has notes. Chapter 2 (unconstrained optimization: line searches, trust regions, Newton, BFGS, SR1, L-BFGS, nonlinear CG, Newton–CG) has notes. Chapter 3 (iterative solvers: Rayleigh–Ritz and harmonic Ritz, Lanczos, Davidson and Jacobi–Davidson, linear and preconditioned CG, Newton and Broyden for nonlinear equations, DIIS) has notes. The other chapters are planned.
