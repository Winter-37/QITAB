---
id: householder-tridiagonalization
title: Householder reduction to tridiagonal form
summary: Phase I of a direct symmetric eigensolver. n − 2 Householder reflections reduce a full symmetric matrix to tridiagonal T = Q₁ᵀAQ₁ at (4/3)n³ flop. The blocked variant moves half of that into BLAS-3, eigenvectors are recovered by back-transformation q = Q₁v at 2n²m flop (all BLAS-3), and banded matrices are reduced by rotation bulge-chasing instead. Exact worked example on a 4×4 matrix.
status: in-progress
kind: algorithm
level: intermediate
tags: [tridiagonalization, householder, dsytrd, back-transformation, blocked-algorithm, band-reduction, bulge-chasing, flop-count]
prerequisites: [givens-rotations-and-householder-reflections]
related: [tridiagonal-qr-iteration, bisection-and-inverse-iteration, divide-and-conquer-eigensolver, choosing-a-symmetric-eigensolver]
key: tri
order: 30
date: 2026-11-21
---

## Overview

No finite sequence of arithmetic operations and root extractions can produce the eigenvalues of every matrix: that would contradict Galois theory, since the eigenvalues are the roots of a polynomial of degree $n$. So every eigensolver has an iterative part. *Direct* solvers split the work into two phases:

- **Phase I** is a finite reduction to a matrix that is cheap to iterate on.
- **Phase II** is the iteration on that matrix.

For symmetric matrices the reduced form is **tridiagonal**:

$$
\mathbf Q_1^{\mathsf T}\mathbf A\mathbf Q_1 = \mathbf T,\qquad
T_{ii} = \alpha_i,\quad T_{i,i-1} = T_{i-1,i} = \beta_i,\quad T_{ij} = 0\ \ (|i-j|>1).
\label{tri}
$$

The eigenvalues of $\mathbf T$ and $\mathbf A$ coincide. If $\mathbf T\mathbf v = \mathbf v\lambda$, then $\mathbf A(\mathbf Q_1\mathbf v) = (\mathbf Q_1\mathbf v)\lambda$: eigenvalues are invariant under similarity, and eigenvectors transform with $\mathbf Q_1$ (Lang Sec. 2.4).

## The reduction (Lang Algorithm 1)

Step $k = 1,\dots,n-2$ treats column (and, by symmetry, row) $k$. Take the reflection $\mathbf H_k = \mathbf 1 - \tau_k\mathbf y_k\mathbf y_k^{\mathsf T}$ that maps the subcolumn $\mathbf A(k{+}1{:}n, k)$ onto a multiple of its first unit vector ([[givens-rotations-and-householder-reflections]]):

$$
\mathbf y_k = (0,\dots,0,\ \mathbf x + \sigma\|\mathbf x\|\mathbf e_1),\qquad \mathbf x = \mathbf A(k{+}1{:}n,\,k),\qquad \sigma = \operatorname{sign}x_1 .
$$

Then apply it from both sides with the symmetric rank-2 update:

$$
\mathbf z_k = \tau_k\mathbf A\mathbf y_k,\qquad
\mathbf v_k = \mathbf z_k - \tfrac12\tau_k(\mathbf y_k^{\mathsf T}\mathbf z_k)\,\mathbf y_k,\qquad
\mathbf A\leftarrow\mathbf A - \mathbf y_k\mathbf v_k^{\mathsf T} - \mathbf v_k\mathbf y_k^{\mathsf T}.
\label{step}
$$

After $n-2$ steps, $\mathbf A = \mathbf T$ and $\mathbf Q_1 = \mathbf H_1\mathbf H_2\cdots\mathbf H_{n-2}$.

**Why the zeros survive.** $\mathbf y_k$ vanishes in positions $1,\dots,k$, so $\mathbf H_k = \operatorname{diag}(\mathbf 1_k,\hat{\mathbf H}_k)$. Multiplying by it from the left recombines only rows $k{+}1,\dots,n$. Multiplying from the right recombines only the same columns. The first $k-1$ rows and columns, already tridiagonal, are untouched. In column $k$, entries $k{+}2,\dots,n$ become zero and entry $k{+}1$ becomes $\beta_{k+1} = -\sigma\|\mathbf x\|$.

The reflection is deliberately chosen *not* to act on row $k$. A reflection that zeroed $\mathbf A(k{:}n,k)$ completely would refill column $k$ when applied from the right. One cannot reach diagonal form in finitely many steps.

**Cost.** Step $k$ updates the trailing $(n-k)\times(n-k)$ block at about $4(n-k)^2$ flop, using one triangle. Summing over $k$ gives

$$
\sum_{k=1}^{n-2}4(n-k)^2 \approx \tfrac43n^3\ \text{flop}.
$$

Nearly all of it is the symmetric matrix–vector product $\mathbf A\mathbf y_k$ and the rank-2 update: BLAS-2 operations, limited by memory bandwidth.

**Householder versus Givens.** Givens' older rotation-based tridiagonalization does more operations on a full matrix, but it can exploit sparsity better.

## Blocking

The intermediate matrices need not be formed at every step. After $s$ steps (Lang Eq. (19)),

$$
\mathbf A_s = \mathbf A_0 - \mathbf Y_s\mathbf V_s^{\mathsf T} - \mathbf V_s\mathbf Y_s^{\mathsf T},\qquad
\mathbf Y_s = (\mathbf y_1|\cdots|\mathbf y_s),\ \ \mathbf V_s = (\mathbf v_1|\cdots|\mathbf v_s).
\label{factored}
$$

The blocked algorithm (Lang Algorithm 2) therefore updates $\mathbf A$ only every $n_b$ steps. In between it reconstructs the one column it needs from Eq. [[#factored]], and corrects $\mathbf z_k$ by $-\mathbf Y(\mathbf V^{\mathsf T}\mathbf y_k\tau_k) - \mathbf V(\mathbf Y^{\mathsf T}\mathbf y_k\tau_k)$. The rank-2 updates become one rank-$2n_b$ matrix–matrix product (BLAS-3). The products $\mathbf A\mathbf y_k$ remain BLAS-2, so about half of the $\tfrac43n^3$ flop run at matrix–matrix speed. This is LAPACK's `dsytrd`.

A further step is to reduce first to a band (almost entirely BLAS-3), then reduce the band to tridiagonal form. According to Lang this typically wins when no eigenvectors are wanted.

## Back-transformation of eigenvectors

Phase II returns eigenvectors $\mathbf v_1,\dots,\mathbf v_m$ of $\mathbf T$. The eigenvectors of $\mathbf A$ are

$$
(\mathbf q_1|\cdots|\mathbf q_m) = \mathbf H_1\mathbf H_2\cdots\mathbf H_{n-2}\,(\mathbf v_1|\cdots|\mathbf v_m),
$$

which costs about $2n^2m$ flop. Grouping $n_b$ reflections into the compact WY form $\mathbf 1-\mathbf Y\mathbf T\mathbf Y^{\mathsf T}$ makes this almost entirely BLAS-3 (Lang Algorithm 3). It parallelizes well. Only the $m$ wanted vectors are back-transformed, which is where computing a subset of eigenpairs saves time.

## Banded matrices

If $A_{ij} = 0$ for $|i-j|>b$ with $b\ll n$, Algorithm 1 would destroy the band. Schwarz's algorithm instead zeroes the outermost band entry of column $j$ with a rotation in the plane of the two rows next to it. That rotation creates one fill-in entry $b$ positions further down, just outside the band. The next rotation removes the fill-in and creates another $b$ rows lower, and so on: the bulge is chased off the end of the matrix. Repeating this for every band entry, column by column, costs about $6bn^2$ flop.

If eigenvectors are needed, each rotation must also be applied to an explicit $n\times n$ matrix $\mathbf Q_1$, which costs $\approx3n^3$ flop and dominates. Householder-based band reductions (Murata–Horikoshi, Lang) allow coarser parallelism and blocked accumulation of $\mathbf Q_1$. The same bulge-chasing idea drives the tridiagonal QR iteration ([[tridiagonal-qr-iteration]]).

!!! example "Worked example: an exact 4×4 reduction"
    $$
    \mathbf A = \begin{pmatrix}4&1&-2&2\\1&2&0&1\\-2&0&3&-2\\2&1&-2&-1\end{pmatrix}.
    $$
    **Step 1.** $\mathbf x = (1,-2,2)$, $\|\mathbf x\| = 3$, $\sigma = +1$: $\mathbf y_1 = (0,4,-2,2)$, $\tau_1 = 2/24 = 1/12$. The update gives
    $$
    \mathbf A_1 = \mathbf H_1\mathbf A\mathbf H_1 = \begin{pmatrix}4&-3&0&0\\-3&\tfrac{10}3&1&\tfrac43\\0&1&\tfrac53&-\tfrac43\\0&\tfrac43&-\tfrac43&-1\end{pmatrix},
    \qquad \beta_2 = -\sigma\|\mathbf x\| = -3 .
    $$
    **Step 2.** $\mathbf x = \mathbf A_1(3{:}4,2) = (1,\tfrac43)$, $\|\mathbf x\| = \tfrac53$, $\sigma = +1$: $\mathbf y_2 = (0,0,\tfrac83,\tfrac43)$, $\tau_2 = 2/(\tfrac{80}{9}) = \tfrac{9}{40}$, $\beta_3 = -\tfrac53$.

    Exact arithmetic (`sympy`) gives
    $$
    \mathbf T = \begin{pmatrix}4&-3&0&0\\-3&\tfrac{10}{3}&-\tfrac53&0\\0&-\tfrac53&-\tfrac{33}{25}&\tfrac{68}{75}\\0&0&\tfrac{68}{75}&\tfrac{149}{75}\end{pmatrix}.
    $$
    The floating-point Algorithm 1 reproduces these to $10^{-15}$.

    Checks:

    - $\mathbf Q_1$ is orthogonal with first row and column $\mathbf e_1$;
    - $\operatorname{tr}\mathbf T = 4+\tfrac{10}3-\tfrac{33}{25}+\tfrac{149}{75} = 8 = \operatorname{tr}\mathbf A$;
    - $\operatorname{eig}\mathbf T = \operatorname{eig}\mathbf A = \{-2.197517,\ 1.084364,\ 2.268531,\ 6.844621\}$;
    - back-transformed vectors $\mathbf Q_1\mathbf v$ satisfy $\max|\mathbf A\mathbf q-\mathbf q\lambda| = 2.6\times10^{-15}$.

    The factored form Eq. [[#factored]] after two steps on a random $6\times6$ matrix agrees with the explicitly updated matrix to $1.2\times10^{-15}$.

    **Blocking pays.** For a random symmetric $1500\times1500$ matrix (single-threaded OpenBLAS, this container), LAPACK `dsytrd` took

    - 0.45 s with workspace $n$ (unblocked, BLAS-2);
    - 0.25 s with its optimal workspace of $48\,000$ (blocked).

    The flop count is the same, $\tfrac43n^3$. Only the memory traffic differs.

## Source

Grotendorst, *Modern Methods and Algorithms of Quantum Chemistry* (NIC Series Vol. 3, 2nd ed., John von Neumann Institute for Computing, Jülich, 2000): chapter by B. Lang, "Direct Solvers for Symmetric Eigenvalue Problems", pp. 231-257, Secs. 1.3, 2.4, 4.1-4.4, pp. 233, 237, 241-245, Eqs. (18)-(19), Algorithms 1-4.

The argument for why the zeros survive and the cost sum are mine. Numbers: `Claude outputs/part7_ch1_numerical_linear_algebra.py`, sections C and I.
