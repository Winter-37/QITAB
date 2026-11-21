---
id: divide-and-conquer-eigensolver
title: Divide and conquer for the symmetric tridiagonal eigenproblem
summary: Tear T into two tridiagonal halves plus a rank-one term, solve the halves recursively, and merge by diagonalizing Δ + ρzzᵀ. Its eigenvalues are the roots of the secular equation 1 + ρΣζᵢ²/(δᵢ − λ) = 0, which interlace the δᵢ, and its eigenvectors are (Δ − λ)⁻¹z. Deflation shrinks the merges; computing the eigenvectors stably needs accurate differences δᵢ − λ (Gu–Eisenstat). This is the algorithm behind numpy.linalg.eigh (LAPACK syevd).
status: in-progress
kind: algorithm
level: advanced
tags: [divide-and-conquer, secular-equation, rank-one-update, matrix-determinant-lemma, interlacing, deflation, gu-eisenstat, dstedc, dsyevd]
prerequisites: [householder-tridiagonalization, tridiagonal-qr-iteration]
related: [bisection-and-inverse-iteration, choosing-a-symmetric-eigensolver, floating-point-and-eigenvalue-perturbation, upper-bounds-and-interlacing]
key: secular
order: 60
date: 2026-11-21
---

## Overview

Divide and conquer (Cuppen 1981; Dongarra and Sorensen 1987) was designed to expose parallelism. It turned out to beat QR iteration and bisection/inverse iteration even on serial machines, although it needs more memory than QR. It works on the symmetric tridiagonal $\mathbf T$ (diagonal $\alpha_i$, off-diagonal $\beta_i$) of [[householder-tridiagonalization]].

## Tearing

Pick $m\approx n/2$ and set $\rho = \beta_{m+1}$, $\mathbf w = \mathbf e_m+\mathbf e_{m+1}$. Then

$$
\mathbf T = \begin{pmatrix}\mathbf T_1&\\&\mathbf T_2\end{pmatrix} + \rho\,\mathbf w\mathbf w^{\mathsf T}.
\label{tear}
$$

Here $\mathbf T_1$ is the leading $m\times m$ block of $\mathbf T$ with $\alpha_m$ replaced by $\alpha_m-\rho$, and $\mathbf T_2$ is the trailing block with $\alpha_{m+1}$ replaced by $\alpha_{m+1}-\rho$. The term $\rho\mathbf w\mathbf w^{\mathsf T}$ puts $\rho$ back on both diagonal entries and on the two coupling entries. Both $\mathbf T_i$ are again tridiagonal.

Diagonalize them recursively, $\mathbf T_i = \mathbf X_i\boldsymbol\Delta_i\mathbf X_i^{\mathsf T}$; small blocks are handled by QR. With $\mathbf X = \operatorname{diag}(\mathbf X_1,\mathbf X_2)$ and $\boldsymbol\Delta = \operatorname{diag}(\boldsymbol\Delta_1,\boldsymbol\Delta_2)$:

$$
\mathbf T = \mathbf X\big(\boldsymbol\Delta + \rho\,\mathbf z\mathbf z^{\mathsf T}\big)\mathbf X^{\mathsf T},\qquad
\mathbf z = \mathbf X^{\mathsf T}\mathbf w = \begin{pmatrix}\text{last row of }\mathbf X_1\\\text{first row of }\mathbf X_2\end{pmatrix}.
$$

So the merge step is the eigenproblem of a **diagonal matrix plus a rank-one term**:

$$
\boldsymbol\Delta+\rho\,\mathbf z\mathbf z^{\mathsf T} = \mathbf Y\boldsymbol\Lambda\mathbf Y^{\mathsf T}
\quad\Longrightarrow\quad
\mathbf T = (\mathbf X\mathbf Y)\boldsymbol\Lambda(\mathbf X\mathbf Y)^{\mathsf T}.
$$

## The secular equation

Assume for now that every $\zeta_i\ne0$ and the $\delta_i$ are distinct and sorted, $\delta_1<\dots<\delta_n$.

**Eigenvalues.** For $\lambda\notin\{\delta_i\}$, the matrix determinant lemma $\det(\mathbf M+\mathbf u\mathbf v^{\mathsf T}) = \det\mathbf M\,(1+\mathbf v^{\mathsf T}\mathbf M^{-1}\mathbf u)$ gives

$$
\det(\boldsymbol\Delta+\rho\mathbf z\mathbf z^{\mathsf T}-\lambda\mathbf 1)
= \prod_i(\delta_i-\lambda)\cdot f(\lambda),\qquad
f(\lambda) = 1+\rho\sum_{i=1}^n\frac{\zeta_i^2}{\delta_i-\lambda}.
\label{secular}
$$

With all $\zeta_i\ne0$, no $\delta_i$ is an eigenvalue, so the eigenvalues are exactly the roots of $f$, the **secular equation** (Lang Eq. (23)).

**Eigenvectors.** From $(\boldsymbol\Delta+\rho\mathbf z\mathbf z^{\mathsf T})\mathbf y = \lambda\mathbf y$ we get $(\boldsymbol\Delta-\lambda)\mathbf y = -\rho\,\mathbf z(\mathbf z^{\mathsf T}\mathbf y)$, hence

$$
\mathbf y_i \propto (\boldsymbol\Delta-\lambda_i\mathbf 1)^{-1}\mathbf z,\qquad (\mathbf y_i)_k = \frac{\zeta_k}{\delta_k-\lambda_i}.
\label{dc-vec}
$$

This is a cheap entry-wise scaling of $\mathbf z$ (Lang Eq. (24)). Substituting back reproduces $f(\lambda_i) = 0$.

**Interlacing.** Take $\rho>0$. Then $f'(\lambda) = \rho\sum_i\zeta_i^2/(\delta_i-\lambda)^2>0$, so $f$ increases between its poles.

- On $(\delta_i,\delta_{i+1})$, $f$ runs from $-\infty$ (just above $\delta_i$) to $+\infty$ (just below $\delta_{i+1}$), so it has exactly one root there.
- On $(\delta_n,\infty)$ it rises from $-\infty$ to 1. At $\lambda = \delta_n+\rho\,\mathbf z^{\mathsf T}\mathbf z$ every term satisfies $|\rho\zeta_i^2/(\delta_i-\lambda)|\le\zeta_i^2/\mathbf z^{\mathsf T}\mathbf z$, so $f\ge0$ there.

Hence

$$
\delta_1<\lambda_1<\delta_2<\lambda_2<\dots<\delta_n<\lambda_n\le\delta_n+\rho\,\mathbf z^{\mathsf T}\mathbf z .
$$

For $\rho<0$ the order is reversed, with $\lambda_i<\delta_i$. Each root is bracketed, and on each interval $f$ is well approximated by simple rational functions. That gives a globally and quadratically convergent root finder that computes all $n$ roots in $O(n^2)$.

## Deflation

The assumptions above are often violated, and that helps. If $\zeta_i = 0$, then $\delta_i$ is already an eigenvalue of $\mathbf T$, with eigenvector column $i$ of $\mathbf X$. If two $\delta_i$ (nearly) coincide, a rotation in their plane zeroes one of the corresponding $\zeta$'s, so all but one of them are (very good approximations to) eigenvalues. In both cases the secular problem and the product $\mathbf X\mathbf Y$ shrink. Lang notes that such deflation is frequent in practice.

## Computing orthogonal eigenvectors

Eq. [[#dc-vec]] is unstable as it stands. If $\lambda_i$ lies very close to some $\delta_k$, the difference $\delta_k-\lambda_i$ is computed with a large *relative* error unless it is formed carefully, and the computed $\mathbf y_i$ lose orthogonality. Early implementations fell back on extended precision. More than ten years after the method was invented, Gu and Eisenstat found the cure without it. The idea is to compute each root as an offset from its nearest pole, so that the differences $\delta_k-\lambda_i$ are accurate. Then apply Eq. [[#dc-vec]] to a slightly modified $\hat{\mathbf z}$, the vector for which the computed $\lambda_i$ are the *exact* eigenvalues of $\boldsymbol\Delta+\rho\hat{\mathbf z}\hat{\mathbf z}^{\mathsf T}$:

$$
\hat\zeta_k^2 = \frac{\prod_{j=1}^n(\lambda_j-\delta_k)}{\rho\prod_{j\ne k}(\delta_j-\delta_k)} ,
\qquad \operatorname{sign}\hat\zeta_k = \operatorname{sign}\zeta_k .
\label{zhat}
$$

Lang describes the idea only in words ("formula (24) applied to a slightly modified vector $\mathbf z$"). Eq. [[#zhat]] is the standard Löwner-type formula, checked numerically in the worked example.

## Cost, parallelism, software

At every level, the root finding and Eq. [[#dc-vec]] cost $O(n^2)$, and the merge product $\mathbf X\mathbf Y$ is a dense matrix–matrix product. The latter dominates and runs as BLAS-3, which is why the method is fast even serially. All roots and their vectors are independent, and $\mathbf X\mathbf Y$ parallelizes coarsely.

LAPACK's tridiagonal divide and conquer is `dstedc`. Combined with the reduction `dsytrd`, it makes the driver `dsyevd`, which is what `numpy.linalg.eigh` calls (NumPy documentation) and SciPy's `eigh(driver="evd")`.

!!! example "Worked example: a 6×6 tear"
    $\mathbf T$ has $\alpha = (1,2,3,4,5,6)$ and all $\beta_i = 1$. Tear at $m = 3$ with $\rho = \beta_4 = 1$. Then $\mathbf T_1$ has diagonal $(1,2,2)$ and $\mathbf T_2$ has diagonal $(3,5,6)$. Eq. [[#tear]] holds exactly, and $\mathbf z^{\mathsf T}\mathbf z = 2$ (one unit row from each orthogonal $\mathbf X_i$).

    | | 1 | 2 | 3 | 4 | 5 | 6 |
    |---|---:|---:|---:|---:|---:|---:|
    | $\delta_i$ | 0.198062 | 1.554958 | 2.539495 | 3.246980 | 4.760877 | 6.699628 |
    | $\zeta_i$ | 0.327985 | 0.736976 | 0.901753 | 0.591009 | $-0.404222$ | 0.153123 |
    | $\lambda_i$ (roots of $f$) | 0.253807 | 1.789472 | 2.964906 | 4.035094 | 5.210528 | 6.746193 |

    The roots agree with `eigvalsh(T)` to $1.8\times10^{-15}$ and interlace the $\delta_i$ as proved. The eigenvectors $\mathbf X\mathbf y_i$ from Eq. [[#dc-vec]] have residual $1.1\times10^{-15}$ and $\|\mathbf Q^{\mathsf T}\mathbf Q-\mathbf 1\| = 2.1\times10^{-15}$. The determinant identity Eq. [[#secular]] at $\lambda = 0.37$ gives $-48.413727883291$ on both sides.

    **Close poles.** $\boldsymbol\Delta = \mathrm{diag}(1, 1+g, 2, 3)$, $\mathbf z = (\tfrac12,\tfrac12,\tfrac12,\tfrac12)$, $\rho = 1$, roots computed as offsets from their left pole. They are accurate to $\le1.6\times10^{-16}$ (checked with `mpmath`).

    | $g$ | Eq. [[#dc-vec]] with $\lambda$ stored absolutely | with accurate $\delta_k-\lambda_i$ | with accurate differences and $\hat{\mathbf z}$ |
    |---:|---:|---:|---:|
    | $10^{-8}$ | $\|\mathbf Y^{\mathsf T}\mathbf Y-\mathbf 1\| = 1.9\times10^{-8}$ | $1.9\times10^{-16}$ | $2.1\times10^{-16}$ |
    | $10^{-11}$ | $1.9\times10^{-11}$ | $5.2\times10^{-16}$ | $5.0\times10^{-16}$ |

    With absolute $\lambda$, orthogonality degrades like $\varepsilon/g$. In this example the decisive ingredient is the accurate differences. $\hat{\mathbf z}$ differs from $\mathbf z$ by only $6\times10^{-17}$, because the roots are already accurate. The correction Eq. [[#zhat]] matters when the roots carry errors of their own.

## Source

Grotendorst, *Modern Methods and Algorithms of Quantum Chemistry* (NIC Series Vol. 3, 2nd ed., John von Neumann Institute for Computing, Jülich, 2000): chapter by B. Lang, "Direct Solvers for Symmetric Eigenvalue Problems", pp. 231-257, Sec. 5.4, pp. 251-253, Eqs. (22)-(24).

- Papers cited by Lang, not read for this note: J. J. M. Cuppen, *Numer. Math.* **36**, 177 (1981); J. J. Dongarra and D. C. Sorensen, *SIAM J. Sci. Stat. Comput.* **8**, s139 (1987); M. Gu and S. C. Eisenstat, *SIAM J. Matrix Anal. Appl.* **15**, 1266 (1994).

The determinant-lemma derivation, the interlacing proof and Eq. [[#zhat]] are mine (standard results; Lang states the conclusions). The routine `dstedc` is named from LAPACK, not from Lang. Numbers: `Claude outputs/part7_ch1_numerical_linear_algebra.py`, section F.
