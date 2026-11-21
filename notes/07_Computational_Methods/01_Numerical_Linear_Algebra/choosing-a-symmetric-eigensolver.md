---
id: choosing-a-symmetric-eigensolver
title: Choosing a dense symmetric eigensolver
summary: Synopsis of the chapter. Which computational path to take (full or banded, standard or generalized, all or some eigenpairs), what each step costs in flop, why BLAS-3 blocking decides the speed, and which LAPACK driver numpy.linalg.eigh and scipy.linalg.eigh actually call (syevd, syevr, syevx, syev, sygvd). Measured timings and accuracies for a 1500×1500 matrix, and when to leave dense solvers for iterative ones.
status: in-progress
kind: comparison
level: intermediate
tags: [eigensolver, lapack, dsyev, dsyevd, dsyevr, dsyevx, dsygvd, numpy, scipy, blas, flop-count, synopsis]
prerequisites: [householder-tridiagonalization, tridiagonal-qr-iteration, divide-and-conquer-eigensolver, bisection-and-inverse-iteration]
related: [jacobi-eigenvalue-method, cholesky-and-generalized-eigenproblem, floating-point-and-eigenvalue-perturbation, matrix-eigenvalue-problem, ci-optimization-newton-and-davidson, determinant-strings-and-direct-ci, davidson-and-jacobi-davidson-methods, choosing-an-iterative-solver]
order: 90
date: 2026-11-21
---

## Overview

The previous notes give the pieces. This one puts them together the way Lang's synopsis does, adds operation counts, and maps the pieces onto the library calls actually used in Python.

## Computational paths

| Problem | Phase I | Phase II | Eigenvectors |
|---|---|---|---|
| full $\mathbf A$, all pairs | blocked Householder ([[householder-tridiagonalization]]) | divide and conquer ([[divide-and-conquer-eigensolver]]), or QR ([[tridiagonal-qr-iteration]]) | back-transformation $\mathbf Q_1\mathbf V$ |
| full $\mathbf A$, selected pairs | blocked Householder | bisection ([[bisection-and-inverse-iteration]]) | inverse iteration, then back-transformation of the $m$ vectors |
| eigenvalues only | blocked (or two-stage band) reduction | QR-type root-free variants, or bisection | none |
| banded $\mathbf A$ | Schwarz rotations or Householder band reduction | as above | accumulate $\mathbf Q_1$ ($3n^3$) |
| generalized $\mathbf A\mathbf q = \mathbf B\mathbf q\lambda$ | Cholesky of $\mathbf B$ ([[cholesky-and-generalized-eigenproblem]]), then any path above | | $\mathbf q = \mathbf L^{-\mathsf T}\tilde{\mathbf q}$ |
| nearly diagonal $\mathbf A$ | none | Jacobi ([[jacobi-eigenvalue-method]]) | accumulated rotations |

Points from Lang's discussion that decide between paths:

- **Clustered spectra** make inverse iteration need explicit orthogonalization; QR and divide and conquer do not.
- **Very accurate small eigenvalues** of special matrix classes can favour a carefully implemented Jacobi method.
- **Parallel machines.** Divide and conquer was designed for parallelism, and the two-stage band reduction allows coarser-grained parallelism than direct tridiagonalization.

## Operation counts (leading terms)

| Step | flop | BLAS level |
|---|---|---|
| Householder tridiagonalization | $\tfrac43n^3$ | half 2, half 3 when blocked |
| back-transformation of $m$ vectors | $2n^2m$ | 3 (compact WY) |
| QR iteration, eigenvalues only | $O(n^2)$ | scalar |
| QR iteration, accumulating vectors | $\approx6n^3$ | rotations |
| bisection, one eigenvalue | $O(n)$ per bit | scalar |
| inverse iteration, one vector | $O(n)$ per step (+ up to $O(n^3)$ orthogonalization in clusters) | scalar |
| divide and conquer | dominated by the merge products $\mathbf X\mathbf Y$ | 3 |
| Jacobi | $\approx3n^3$ per sweep, about $\log n$ sweeps | rotations |
| Cholesky | $\tfrac13n^3$ | 3 when blocked |
| generalized problem, Algorithm 5 | $\approx12n^3$ | mostly 3 |

## Why the BLAS level matters

On cache-based machines the speed is set by the **re-use factor** $r$, the flop performed per number moved between main memory and cache. Lang's examples:

| BLAS routine | operation | $r$ | Mflop/s on a 266 MHz Pentium II ($n = 1000$) |
|---|---|---:|---:|
| `DDOT` (level 1) | $\mathbf x^{\mathsf T}\mathbf y$ | $\approx1$ | 36 |
| `DGEMV` (level 2) | $\mathbf y\leftarrow\alpha\mathbf A\mathbf x+\beta\mathbf y$ | $\approx2$ | 61 |
| `DGEMM` (level 3) | $\mathbf C\leftarrow\alpha\mathbf A\mathbf B+\beta\mathbf C$ | $\approx n/2$ | 195 (peak 266) |

The hardware is from 2000, but the ordering still holds. Algorithms are therefore restructured ("blocked") so that most of their work is matrix–matrix products, even at the cost of a few more operations. Level-3 work also gives coarse-grained parallelism. The measurement in the worked example below (blocked against unblocked `dsytrd`) shows the effect directly.

## What NumPy and SciPy call

| Python call | LAPACK driver (real case) | Phase II algorithm |
|---|---|---|
| `numpy.linalg.eigh(A)` | `dsyevd` | divide and conquer |
| `scipy.linalg.eigh(A)` (default `driver="evr"`) | `dsyevr` | MRRR (see [[bisection-and-inverse-iteration]], *to verify*) |
| `scipy.linalg.eigh(A, driver="evd")` | `dsyevd` | divide and conquer |
| `scipy.linalg.eigh(A, driver="ev")` | `dsyev` | implicit QL/QR |
| `scipy.linalg.eigh(A, driver="evx")` | `dsyevx` | bisection + inverse iteration |
| `scipy.linalg.eigh(A, B)` | `dsygvd` (full set), `dsygvx` (subset) | Cholesky reduction, then D&C / bisection |
| `scipy.linalg.eigh(A, subset_by_index=[i, j])` | `dsyevr` (default) or `dsyevx` | only the requested pairs |
| `scipy.linalg.eigh_tridiagonal(d, e)` | tridiagonal drivers | Phase II only |

The driver names, the defaults and the summary "`ev` slowest and most robust, `evr` the best general choice, `evd` sometimes faster at the cost of memory" are from the SciPy and NumPy docstrings (SciPy 1.18, NumPy 2.5). Complex Hermitian matrices use the corresponding `zheevd`/`zheevr`/… routines.

Two practical points from the same documentation. First, the eigenvalues can differ at the level of $\varepsilon\|\mathbf A\|$ depending on whether eigenvectors are requested (`eigvals_only`), because different LAPACK paths run. Second, neither function checks symmetry: only one triangle is read, so a non-symmetric input silently gives a wrong answer.

## When not to use a dense solver

Direct solvers are the method of choice when a significant part of the eigensystem of a small to medium matrix is wanted. Lang's numbers are $n\lesssim5000$; with today's memory the practical limit is much higher. When only a few eigenpairs (Lang: up to about 100) of a very large, typically sparse, matrix are wanted, use iterative subspace methods that need only products $\mathbf A\mathbf x$, such as CI $\sigma$-vectors ([[determinant-strings-and-direct-ci]]). This is the Davidson approach of [[ci-optimization-newton-and-davidson]], treated as an algorithm in [[davidson-and-jacobi-davidson-methods]] (Lanczos: [[lanczos-and-krylov-subspaces]]).

Lang's advice on software still holds. Use established libraries rather than one's own implementation: they handle scaling, balancing and the many pitfalls that await the inexperienced programmer. Link them to an optimized BLAS, since modern dense solvers are only as fast as their BLAS. For distributed memory, ScaLAPACK is the analogue of LAPACK.

!!! example "Measured: random symmetric 1500×1500, single-threaded OpenBLAS (this container; timings are machine dependent)"
    | call | time (s) | $\|\mathbf A\mathbf V-\mathbf V\boldsymbol\Lambda\|_F/\|\mathbf A\|_F$ | $\|\mathbf V^{\mathsf T}\mathbf V-\mathbf 1\|_F$ |
    |---|---:|---:|---:|
    | `numpy.linalg.eigh` (`syevd`) | 0.58 | $2.8\times10^{-15}$ | |
    | `scipy eigh(driver="evd")` | 0.56 | $2.7\times10^{-15}$ | $1.4\times10^{-13}$ |
    | `scipy eigh(driver="evr")` (default) | 0.80 | $3.2\times10^{-15}$ | $1.5\times10^{-12}$ |
    | `scipy eigh(driver="ev")` | 3.97 | $1.0\times10^{-14}$ | $3.5\times10^{-13}$ |
    | `scipy eigh(driver="evx")`, all pairs | 4.01 | $1.0\times10^{-14}$ | $3.5\times10^{-13}$ |
    | eigenvalues only (`evr`) | 0.31 | | |
    | 10 lowest pairs, `evr` / `evx` | 0.27 / 0.28 | | |
    | `dsytrd` alone, blocked (optimal workspace) | 0.25 | | |
    | `dsytrd` alone, unblocked (workspace $n$) | 0.45 | | |

    Reading the table:

    - The Phase I reduction costs 0.25 s and is common to all paths. Eigenvalues only (0.31 s) and ten eigenpairs (0.27 s) cost little more than that.
    - The full eigenvector set roughly doubles the time with divide and conquer. QR accumulation ($6n^3$) makes `ev` seven times slower.
    - All drivers are backward stable to a few $\varepsilon$. Orthogonality is at the $10^{-13}$–$10^{-12}$ level in the Frobenius norm for $n = 1500$, about $n\varepsilon$.

## Source

Grotendorst, *Modern Methods and Algorithms of Quantum Chemistry* (NIC Series Vol. 3, 2nd ed., John von Neumann Institute for Computing, Jülich, 2000): chapter by B. Lang, "Direct Solvers for Symmetric Eigenvalue Problems", pp. 231-257, Secs. 1.3, 2.3, 7, 8, pp. 233, 236-237, 256-257, Table 1, Fig. 4.

The library mapping is from the docstrings of `numpy.linalg.eigh` and `scipy.linalg.eigh` (NumPy 2.5.3, SciPy 1.18.1); the identification of `dsyevr` with MRRR is marked "to verify". Timings: `Claude outputs/part7_ch1_numerical_linear_algebra.py`, section I.
