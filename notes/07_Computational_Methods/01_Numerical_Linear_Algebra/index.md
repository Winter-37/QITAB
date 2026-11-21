How a dense symmetric eigenproblem is actually solved on a computer, and how accurate the answer can be.

## What this chapter is about

Part 0 established what a diagonalization is ([[matrix-eigenvalue-problem]]). This chapter is about how library routines such as `numpy.linalg.eigh` compute it. Every dense symmetric solver follows the same plan:

- a **finite reduction** by orthogonal transformations to tridiagonal form;
- an **iteration** on the tridiagonal matrix (QR, bisection with inverse iteration, or divide and conquer);
- a **back-transformation** of the eigenvectors.

The generalized problem $\mathbf A\mathbf q = \mathbf B\mathbf q\lambda$ is first reduced to this form by a Cholesky factorization. Jacobi's method is the one classical solver that skips the reduction.

## Why it matters

Every SCF iteration diagonalizes a Fock matrix in a non-orthogonal basis. Every CI or embedding calculation diagonalizes something in a subspace. The theory chapters take "diagonalize" as a single step, but three practical questions depend on how it is done:

- **Accuracy.** Small overlap eigenvalues, near-degenerate orbitals and eigenvector signs have limits set by floating point, not by the method.
- **Cost.** Which part of the $O(n^3)$ is spent where, and what is saved by asking for only some eigenpairs.
- **Choice of routine.** NumPy and SciPy call different LAPACK drivers by default.

## The main ideas, in order

1. **What accuracy means.** A backward-stable solver returns the exact eigensystem of $\mathbf A+\Delta\mathbf A$ with $\|\Delta\mathbf A\| = O(\varepsilon)\|\mathbf A\|$. Eigenvalues then carry an absolute error of $O(\varepsilon\|\mathbf A\|)$ and eigenvectors an error of $O(\varepsilon\|\mathbf A\|/\mathrm{gap})$.
2. **Tools.** Plane rotations zero one entry; Householder reflections zero a subvector. Both are orthogonal and stable, and blocking (the WY form) turns them into matrix–matrix products.
3. **Reduction.** $n-2$ reflections give $\mathbf T = \mathbf Q_1^{\mathsf T}\mathbf A\mathbf Q_1$ in $\tfrac43n^3$ flop.
4. **Tridiagonal solvers.** Each fits a different need:
    - QR with Wilkinson shifts (cubic convergence, all eigenvalues in $O(n^2)$);
    - bisection with Sturm counts plus inverse iteration (selected pairs);
    - divide and conquer (rank-one tearing, the secular equation, fastest in practice).
5. **Jacobi.** Direct rotations on $\mathbf A$, quadratically convergent, best for nearly diagonal matrices.
6. **Generalized problem.** Cholesky $\mathbf B = \mathbf L\mathbf L^{\mathsf T}$, then $\mathbf L^{-1}\mathbf A\mathbf L^{-\mathsf T}$. It is one of three equivalent orthogonalizers, which behave differently when $\mathbf B$ is nearly singular.
7. **In practice.** Which LAPACK driver does what, and what it costs.

## How to read it

**Path.**

1. [[floating-point-and-eigenvalue-perturbation]] (the standard everything is measured against)
2. [[givens-rotations-and-householder-reflections]]
3. [[householder-tridiagonalization]]
4. Three alternative Phase II solvers: [[tridiagonal-qr-iteration]], [[bisection-and-inverse-iteration]], [[divide-and-conquer-eigensolver]]
5. [[jacobi-eigenvalue-method]]
6. [[cholesky-and-generalized-eigenproblem]]
7. [[choosing-a-symmetric-eigensolver]] (the synopsis)

**Needs.** Part 0, Chapter 1 (Hermitian eigenproblem, spectral theorem, functions of matrices). For the generalized problem, the orthogonalization note of Part 4, Chapter 3 ([[basis-orthogonalization]]).

**Leads to.** Chapter 3 (iterative eigensolvers: Davidson and Lanczos need a dense solver for their subspace matrix). Chapter 5 (BLAS, memory hierarchy). Every SCF and CI code in Parts 4 and 6.

**Core (first pass).** [[floating-point-and-eigenvalue-perturbation]], [[householder-tridiagonalization]], [[tridiagonal-qr-iteration]], [[cholesky-and-generalized-eigenproblem]], [[choosing-a-symmetric-eigensolver]].

**Deep (second pass).** [[givens-rotations-and-householder-reflections]] (WY form), [[bisection-and-inverse-iteration]], [[divide-and-conquer-eigensolver]], [[jacobi-eigenvalue-method]].

**Checkpoint.** Reduce the $4\times4$ example of [[householder-tridiagonalization]] by hand, and count its eigenvalues below 2 with a Sturm sequence. Then explain why `numpy.linalg.eigh` and `scipy.linalg.eigh` may return eigenvectors that differ by more than rounding for a near-degenerate pair, and why that is not an error.

**Source.** The eigenvalue notes follow B. Lang's chapter in the NIC Winterschool proceedings *Modern Methods and Algorithms of Quantum Chemistry* (2000). Every number is checked by `Claude outputs/part7_ch1_numerical_linear_algebra.py`. Topics that chapter does not cover are planned until a proper numerical-analysis source is in the library: Golub and Van Loan, *Matrix Computations*; Trefethen and Bau, *Numerical Linear Algebra*; or Demmel, *Applied Numerical Linear Algebra* (Golub–Van Loan and Demmel are among Lang's references).

**Planned sections:** LU factorization and pivoting; Conditioning of linear systems; QR factorization and least squares; Computing the SVD (Golub–Kahan bidiagonalization); Randomized and pivoted-Cholesky low-rank approximation.
