---
id: cholesky-and-generalized-eigenproblem
title: Cholesky factorization and the generalized eigenproblem Aq = Bqλ
summary: For symmetric A and positive definite B (the Roothaan problem FC = SCε), factor B = LLᵀ (n³/3 flop, blocked BLAS-3) and solve the standard problem for L⁻¹AL⁻ᵀ with triangular solves, about 12n³ flop in all (LAPACK sygvd, scipy.linalg.eigh(a, b)). Cholesky, Löwdin and canonical orthogonalization are three choices of X with XᵀBX = 1. How accuracy degrades with cond(B), a test of Lang's preference for the orthogonal route on near-dependent Gaussian bases, and what PySCF does.
status: in-progress
kind: algorithm
level: intermediate
tags: [cholesky, generalized-eigenvalue-problem, overlap-matrix, roothaan-equations, linear-dependence, canonical-orthogonalization, sygvd, pyscf]
prerequisites: [basis-orthogonalization, householder-tridiagonalization]
related: [floating-point-and-eigenvalue-perturbation, choosing-a-symmetric-eigensolver, scf-procedure, rhf, polar-and-singular-value-decompositions]
key: gen-red
order: 80
date: 2026-11-21
---

## Overview

The symmetric-definite generalized problem is

$$
\mathbf A\mathbf q_i = \mathbf B\mathbf q_i\lambda_i,\qquad \mathbf A = \mathbf A^{\mathsf T},\quad \mathbf B = \mathbf B^{\mathsf T}\ \text{positive definite}.
$$

The eigenvalues are real, and the eigenvectors can be chosen $\mathbf B$-orthonormal, $\mathbf q_i^{\mathsf T}\mathbf B\mathbf q_j = \delta_{ij}$. In general they are not orthogonal in the ordinary sense. In quantum chemistry this is the Roothaan problem $\mathbf F\mathbf C = \mathbf S\mathbf C\boldsymbol\varepsilon$ in a non-orthogonal AO basis ([[rhf]]), solved in every SCF iteration.

All practical methods reduce it to a standard symmetric problem with some $\mathbf X$ satisfying $\mathbf X^{\mathsf T}\mathbf B\mathbf X = \mathbf 1$. Substituting $\mathbf q = \mathbf X\tilde{\mathbf q}$ and multiplying by $\mathbf X^{\mathsf T}$ gives

$$
(\mathbf X^{\mathsf T}\mathbf A\mathbf X)\,\tilde{\mathbf q}_i = \tilde{\mathbf q}_i\lambda_i .
\label{gen-red}
$$

[[basis-orthogonalization]] gives two choices for $\mathbf X$: Löwdin, $\mathbf S^{-1/2}$, and canonical, $\mathbf U\mathbf s^{-1/2}$. The cheapest choice is a triangular one.

## Cholesky factorization

Every symmetric positive definite $\mathbf B$ has a unique factorization

$$
\mathbf B = \mathbf L\mathbf L^{\mathsf T},\qquad \mathbf L\ \text{lower triangular with positive diagonal}.
\label{chol}
$$

*Derivation (Lang Sec. 4.5).* Partition off the first row and column:

$$
\begin{pmatrix}b_{11}&\mathbf b^{\mathsf T}\\\mathbf b&\mathbf B_{22}\end{pmatrix}
= \begin{pmatrix}\ell_{11}&\\\boldsymbol\ell&\mathbf L_{22}\end{pmatrix}\begin{pmatrix}\ell_{11}&\boldsymbol\ell^{\mathsf T}\\&\mathbf L_{22}^{\mathsf T}\end{pmatrix}
\ \Rightarrow\
\ell_{11} = \sqrt{b_{11}},\quad \boldsymbol\ell = \mathbf b/\ell_{11},\quad \mathbf L_{22}\mathbf L_{22}^{\mathsf T} = \mathbf B_{22}-\boldsymbol\ell\boldsymbol\ell^{\mathsf T}.
$$

The trailing update $\mathbf B_{22}-\mathbf b\mathbf b^{\mathsf T}/b_{11}$ is again positive definite (it is a Schur complement), so the recursion continues to the end. Unrolled, this is Lang's Algorithm 6, which overwrites the lower triangle of $\mathbf B$ by $\mathbf L$:

1. for $k = 1,\dots,n$:
2. $\quad B_{kk}\leftarrow\sqrt{B_{kk}}$
3. $\quad \mathbf B(k{+}1{:}n,k)\leftarrow\mathbf B(k{+}1{:}n,k)/B_{kk}$
4. $\quad \mathbf B(k{+}1{:}n,k{+}1{:}n)\leftarrow\mathbf B(k{+}1{:}n,k{+}1{:}n)-\mathbf B(k{+}1{:}n,k)\,\mathbf B(k{+}1{:}n,k)^{\mathsf T}$

It costs about $\tfrac13n^3$ flop. In the blocked form (Algorithm 7), the entries become $n_b\times n_b$ blocks: factor a diagonal block, solve a triangular system for the block column, and update the trailing blocks. That runs almost entirely in BLAS-3.

## Reduction of the generalized problem (Lang Algorithm 5)

1. Factor $\mathbf B = \mathbf L\mathbf L^{\mathsf T}$.
2. Form $\mathbf M = \mathbf L^{-1}\mathbf A\mathbf L^{-\mathsf T}$, i.e. Eq. [[#gen-red]] with $\mathbf X = \mathbf L^{-\mathsf T}$, by two triangular solves with multiple right-hand sides: first $\mathbf Y\mathbf L^{\mathsf T} = \mathbf A$, then $\mathbf L\mathbf M = \mathbf Y$. These are BLAS-3 `dtrsm` calls; $\mathbf L^{-1}$ is never formed.
3. Solve $\mathbf M = \tilde{\mathbf Q}\boldsymbol\Lambda\tilde{\mathbf Q}^{\mathsf T}$ with a standard solver: [[householder-tridiagonalization]], then QR or divide and conquer.
4. Back-substitute $\mathbf L^{\mathsf T}\mathbf Q = \tilde{\mathbf Q}$.

The total is about $12n^3$ flop. The eigenvectors come out $\mathbf B$-orthonormal: $\mathbf Q^{\mathsf T}\mathbf B\mathbf Q = \tilde{\mathbf Q}^{\mathsf T}\mathbf L^{-1}\mathbf L\mathbf L^{\mathsf T}\mathbf L^{-\mathsf T}\tilde{\mathbf Q} = \mathbf 1$. This is LAPACK `dsygvd`, which `scipy.linalg.eigh(a, b)` uses for the full spectrum (SciPy documentation). Even if $\mathbf A$ and $\mathbf B$ are banded, $\mathbf M$ is generally full. Crawford's algorithm avoids forming $\mathbf M$ for banded problems by interleaving it with the band reduction.

**Three choices of X, one spectrum.**

| $\mathbf X$ | cost | properties |
|---|---|---|
| $\mathbf L^{-\mathsf T}$ (Cholesky) | $\tfrac13n^3$ + triangular solves | cheapest; triangular; depends on basis order |
| $\mathbf U\mathbf s^{-1/2}$ (canonical) | eigendecomposition of $\mathbf B$ | orthogonal $\mathbf U$; can drop small $s_p$ |
| $\mathbf U\mathbf s^{-1/2}\mathbf U^{\mathsf T}$ (Löwdin) | the same plus one product | closest to the original basis ([[polar-and-singular-value-decompositions]]) |

With all functions kept, all three give the same $\lambda_i$ and the same $\mathbf q_i$. They differ only in rounding behaviour and in what happens when $\mathbf B$ is nearly singular.

## Accuracy when B is ill conditioned

Lang warns that the backward error of Algorithm 5 grows with $\|\mathbf B^{-1}\|_2$. When the eigenvalues of $\mathbf B$ span many orders of magnitude, he recommends replacing the Cholesky factor by the eigendecomposition $\mathbf B = \mathbf S\boldsymbol\Delta^2\mathbf S^{\mathsf T}$, i.e. $\mathbf M = \boldsymbol\Delta^{-1}\mathbf S^{\mathsf T}\mathbf A\mathbf S\boldsymbol\Delta^{-1}$. This is canonical orthogonalization. In his words, "the use of orthogonal matrices gives better results, albeit at higher cost". If $\mathbf B$ is not positive definite at all, entirely different techniques are needed.

In Gaussian basis sets, near-linear dependence makes $\operatorname{cond}(\mathbf S)$ large. What one really wants is usually not an accurate solution in the full, nearly redundant space. It is to remove the redundant combinations: canonical orthogonalization keeping only eigenvalues $s_p$ above a threshold ([[basis-orthogonalization]]). That changes the variational space and so the answer, by an amount that can exceed the rounding errors it avoids (worked example).

**What PySCF does** (checked in the source of PySCF 2.15.1; other versions may differ):

- The SCF driver calls `check_linear_dependency`. That routine diagonalizes $\mathbf S$ and builds the canonical $\mathbf X = \mathbf U\mathbf s^{-1/2}$, dropping $s_p\le10^{-6}$ by default (`scf.hf.overlap_zero_eigenvalue_threshold`). It warns if $\operatorname{cond}(\mathbf S)>10^{10}$.
- Every Fock diagonalization then uses Eq. [[#gen-red]] with this $\mathbf X$.
- Only a bare `mf.eig(h, s)` without `x` goes through `scipy.linalg.eigh(h, s)`, i.e. the Cholesky route `dsygvd`.
- For even worse conditioning, `scf.addons.remove_linear_dep_` offers a partial (pivoted) Cholesky orthogonalization. It is marked deprecated in 2.15.1, and it switches to the pivoted Cholesky only when $\operatorname{cond}(\mathbf S)>1/\varepsilon$ or when forced.
- Before returning, PySCF makes the largest component of each eigenvector positive (`_adjust_phase_`), so its MO coefficients have a reproducible sign.

!!! example "Worked examples"
    **Algorithm 6** reproduces `numpy.linalg.cholesky` on a random $5\times5$ positive definite matrix.

    **H₂O/STO-3G core Hamiltonian** ($K = 7$, $\operatorname{cond}(\mathbf S) = 5.63$). The Cholesky route gives the one-electron levels
    $$
    -32.72125,\ -8.300539,\ -7.735413,\ -7.465584,\ -7.457170,\ -4.232036,\ -4.208218\ E_h .
    $$
    Löwdin, canonical and `scipy.linalg.eigh(h, S)` agree with these to $7\times10^{-15}$, $1.2\times10^{-14}$ and $5\times10^{-15}$. The vectors satisfy $\mathbf C^{\mathsf T}\mathbf S\mathbf C = \mathbf 1$.

    **A nearly dependent basis: He with even-tempered s functions** $\zeta_k = 0.05\,r^k$, $k = 0,\dots,N-1$, problem $\mathbf h\mathbf c = \mathbf S\mathbf c\varepsilon$ (the He⁺ 1s level, limit $-2\,E_h$). The reference is the exact generalized spectrum of the *float64* matrices $\mathbf h,\mathbf S$, computed with `mpmath` at 60 digits. The table therefore measures only the solver's rounding error.

    | $N$, $r$ | $\operatorname{cond}(\mathbf S)$ | $\lvert\Delta E_1\rvert$ Cholesky (`sygvd`) | canonical, all kept | canonical, $s_p>10^{-6}$ (kept/total) | max rel. error, lowest 5: Cholesky / canonical |
    |---|---:|---:|---:|---:|---:|
    | 20, 1.6 | $2.5\times10^{7}$ | $8.6\times10^{-14}$ | $6.5\times10^{-14}$ | $2.0\times10^{-7}$ (19/20) | $6.6\times10^{-11}$ / $1.5\times10^{-10}$ |
    | 24, 1.35 | $1.0\times10^{12}$ | $3.8\times10^{-11}$ | $5.8\times10^{-11}$ | $2.1\times10^{-4}$ (16/24) | $2.9\times10^{-8}$ / $1.4\times10^{-7}$ |
    | 28, 1.25 | $2.6\times10^{16}$ | $6.2\times10^{-8}$ | $2.4\times10^{-6}$ | $1.5\times10^{-3}$ (14/28) | $5.6\times10^{-4}$ / $7.4\times10^{-3}$ |

    Reading the table:

    1. Both full-space routes lose accuracy roughly in proportion to $\operatorname{cond}(\mathbf S)$, as the backward-error argument predicts.
    2. In this test the Cholesky route was *not* worse than the orthogonal route with all functions kept. It was usually better. So Lang's general preference is not confirmed for these unit-diagonal overlap matrices; one example does not settle the general case.
    3. The canonical column with a threshold is a different, smaller basis. Its "error" is the variational effect of removing functions. Here, for this deliberately over-dense basis, that effect is far larger than the rounding error of either full-space solve. With a threshold the computation is stable, but the threshold is itself an approximation.

## Source

Grotendorst, *Modern Methods and Algorithms of Quantum Chemistry* (NIC Series Vol. 3, 2nd ed., John von Neumann Institute for Computing, Jülich, 2000): chapter by B. Lang, "Direct Solvers for Symmetric Eigenvalue Problems", pp. 231-257, Secs. 1.2, 4.5, pp. 232, 245-247, Eq. (20), Algorithms 5-7.

The Schur-complement remark, the table of three choices of X, the He test and the PySCF description are mine. The PySCF behaviour was read from `pyscf/scf/hf.py` (`check_linear_dependency`, `eig`, `_eigh`, `_adjust_phase_`) and `pyscf/scf/addons.py` of version 2.15.1. Numbers: `Claude outputs/part7_ch1_numerical_linear_algebra.py`, section H.
