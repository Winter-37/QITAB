---
id: choosing-an-iterative-solver
title: Choosing an iterative solver
summary: Synopsis of the chapter. Which method to use for a few eigenpairs, a linear system or a nonlinear system, given what the matrix offers (only products, a good diagonal, symmetry, definiteness); what each costs per iteration; what SciPy and PySCF call; a measured comparison of ARPACK Lanczos, LOBPCG and Davidson on a diagonally dominant matrix (about 310 products against 9-10); and what the chapter does not yet cover (GMRES and MINRES in detail, Anderson acceleration, restarted Arnoldi).
status: in-progress
kind: comparison
level: intermediate
tags: [iterative-solvers, davidson, lanczos, conjugate-gradient, diis, broyden, scipy-sparse-linalg, pyscf, synopsis]
prerequisites: [davidson-and-jacobi-davidson-methods, preconditioned-conjugate-gradient, diis-extrapolation, newton-and-broyden-methods-for-nonlinear-equations]
related: [rayleigh-ritz-and-harmonic-ritz, lanczos-and-krylov-subspaces, linear-conjugate-gradient-method, choosing-a-symmetric-eigensolver, choosing-an-unconstrained-optimizer]
order: 80
date: 2026-11-21
---

## Overview

The methods of this chapter apply when the matrix is too large to store or to factorize, and is known only through products $\mathbf A\mathbf v$. In electronic structure such a product is a $\sigma$ vector, a Fock-like build, or a CC residual. Its cost dominates, so methods are compared by the number of products (or residual evaluations) they need. When $\mathbf A$ is small enough to store and diagonalize, use the dense solvers of Chapter 1 instead ([[choosing-a-symmetric-eigensolver]]).

Almost every quantum-chemistry matrix has a dominant, cheaply known diagonal of orbital-energy differences (or diagonal CI energies). That one fact decides most choices below: preconditioned methods beat plain Krylov methods by large factors.

## Decision table

| problem | matrix | method | per iteration | note |
|---|---|---|---|---|
| few lowest eigenpairs | symmetric, good diagonal (CI, CIS, response) | Davidson, block form; Jacobi–Davidson correction if the preconditioner is accurate | one product per unconverged root | [[davidson-and-jacobi-davidson-methods]] |
| few extreme eigenpairs | symmetric, no useful diagonal | Lanczos with reorthogonalization (ARPACK) | one product | [[lanczos-and-krylov-subspaces]] |
| interior eigenpairs near $\sigma$ | symmetric | harmonic Ritz extraction in Davidson; shift-and-invert if a factorization is affordable | as above | [[rayleigh-ritz-and-harmonic-ritz]] |
| linear system | SPD (CPHF, Z-vector, Newton step at a minimum) | PCG with orbital-energy diagonal | one product, one diagonal solve | [[preconditioned-conjugate-gradient]] |
| linear system | symmetric indefinite | MINRES (not treated here) | one product | planned |
| linear system | nonsymmetric (CC response, Jacobian of CC) | GMRES or DIIS on the diagonal iteration | one product; GMRES stores all directions | planned; [[diis-extrapolation]] |
| nonlinear system | Jacobian available | Newton, solve inexactly, globalize with $\tfrac12\lVert\mathbf r\rVert^2$ | one Jacobian solve | [[newton-and-broyden-methods-for-nonlinear-equations]] |
| nonlinear system | no Jacobian; diagonal approximation known (CC amplitudes) | quasi-Newton (diagonal) step + DIIS | one residual | [[diis-extrapolation]] |
| nonlinear system | no Jacobian, small $n$ | Broyden | one residual, $O(n^2)$ | [[newton-and-broyden-methods-for-nonlinear-equations]] |
| fixed-point iteration (SCF) | — | DIIS on the Roothaan step; second-order methods when DIIS fails | one Fock build | [[diis-extrapolation]], [[scf-convergence-diis-and-newton]] |

**Convergence tests.** For eigenproblems test the residual norm, not the change in eigenvalue: an eigenvalue lies within $\|\mathbf r\|$ of the Ritz value, and the eigenvalue error is $O(\|\mathbf r\|^2)$ for symmetric matrices. For linear systems test $\|\mathbf r\|/\|\mathbf b\|$ with the *true* residual at the end. For DIIS, the multiplier $\lambda$ of the DIIS system is the predicted squared error.

## Measured comparison

!!! example "Lowest eigenpair of $\mathrm{diag}(1,\dots,1000)+0.1\,\mathbf E$ (computed for this note)"

    $\mathbf E$ symmetric Gaussian. Matrix–vector products to residual or tolerance $10^{-8}$-$10^{-10}$:

    | solver | products | error in $\lambda_1$ |
    |---|---|---|
    | `scipy.sparse.linalg.eigsh` (ARPACK, implicitly restarted Lanczos), `which="SA"` | about 310-320 (depends on the random start) | $10^{-14}$ |
    | `scipy.sparse.linalg.lobpcg`, fixed diagonal preconditioner $\mathrm{diag}(\mathbf A)-\min_p A_{pp}+0.5$ | 10 | $8\times10^{-16}$ |
    | own Davidson, diagonal preconditioner | 9 | $4\times10^{-16}$ |

    The same ranking appears for the 245 025-determinant FCI of water in [[davidson-and-jacobi-davidson-methods]] (114 products without a preconditioner, 44 with the diagonal).

## What SciPy and PySCF call

Checked against SciPy 1.18.1 and PySCF 2.15.1.

| routine | algorithm |
|---|---|
| `scipy.sparse.linalg.eigsh` | ARPACK: implicitly restarted Lanczos; shift-invert mode with `sigma` |
| `scipy.sparse.linalg.lobpcg` | locally optimal block preconditioned CG for eigenvalues |
| `scipy.sparse.linalg.cg`, `minres`, `gmres`, `bicgstab` | CG (SPD), MINRES (symmetric), GMRES and BiCGSTAB (nonsymmetric); preconditioner argument `M` |
| `scipy.optimize.root(method="hybr")` | MINPACK `hybrd`/`hybrj`, a modified Powell hybrid (trust-region-type) method |
| `scipy.optimize.root(method="broyden1")`, `"anderson"`, `"krylov"` | Broyden, Anderson mixing, Newton–Krylov |
| `pyscf.lib.davidson`, `davidson1` | Davidson; the default diagonal preconditioner `make_diag_precond` subtracts $\theta$ minus a level shift of $10^{-3}$, so that a diagonal matrix does not reproduce the stalling of the exact-inverse case |
| `pyscf.lib.krylov` | Krylov solver for $(\mathbf1+\mathbf a)\mathbf x = \mathbf b$ (Pople et al.), used by `pyscf.scf.cphf.solve` |
| `pyscf.scf` (`CDIIS`) | DIIS with commutator error vectors, 8 vectors, from cycle 1 by default |
| `pyscf.cc.CCSD` | diagonal quasi-Newton amplitude update with DIIS, 6 vectors |
| `pyscf.fci.direct_spin1` | Davidson on string-driven $\sigma$ vectors |

## What this chapter does not yet cover

- **GMRES and MINRES** in detail, with their minimal-residual property and restarts; N&W mention GMRES only in passing (as an inner solver for inexact Newton).
- **Arnoldi and implicit restarts** (ARPACK), and nonsymmetric Davidson for EOM-CC.
- **Anderson acceleration** and the relation of DIIS to Krylov methods on linear problems; the CPHF test in [[diis-extrapolation]] only shows the iteration counts are similar.
- **Block CG** for many right-hand sides, and the sparse-matrix preconditioners (incomplete Cholesky, SSOR) in practice.

## Source

Synopsis of the chapter: Steffen's chapter in Grotendorst, *Modern Methods and Algorithms of Quantum Chemistry* (NIC Series Vol. 3, 2nd ed., John von Neumann Institute for Computing, Jülich, 2000), pp. 307-314; Nocedal and Wright, *Numerical Optimization* (Springer, New York, 1999), Ch. 5, Sec. 5.1 and Ch. 11; Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Secs. 10.6.2 and 13.4. The library descriptions come from the SciPy and PySCF docstrings and source of the versions named; the comparison was computed for this note (`Claude outputs/part7_ch3_iterative_solvers.py`, section B).
