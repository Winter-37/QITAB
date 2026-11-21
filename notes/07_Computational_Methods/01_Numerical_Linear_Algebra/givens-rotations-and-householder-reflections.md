---
id: givens-rotations-and-householder-reflections
title: Givens rotations and Householder reflections
summary: The two orthogonal building blocks of every direct symmetric eigensolver. A plane rotation zeroes one entry; a Householder reflection I − τyyᵀ zeroes a whole subvector. Choice of the parameters (with the sign that avoids cancellation), application without forming the matrix (4ℓm flop), the symmetric two-sided update, stability, and the (compact) WY form that turns k reflections into matrix–matrix products.
status: in-progress
kind: algorithm
level: intermediate
tags: [givens-rotation, jacobi-rotation, householder, reflection, orthogonal-transformation, wy-representation, blas-3, flop-count]
prerequisites: [floating-point-and-eigenvalue-perturbation, unitary-matrices-exponential-logarithm]
related: [householder-tridiagonalization, tridiagonal-qr-iteration, jacobi-eigenvalue-method, matrix-eigenvalue-problem, orbital-rotations]
key: house-y
order: 20
date: 2026-11-21
---

## Overview

Direct eigensolvers transform $\mathbf A\mapsto\mathbf Q^{\mathsf T}\mathbf A\mathbf Q$ by orthogonal matrices. Such transformations keep $\mathbf A$ symmetric, have the trivial inverse $\mathbf Q^{\mathsf T}$, and are backward stable ([[floating-point-and-eigenvalue-perturbation]]). In practice $\mathbf Q$ is always a product of two elementary kinds:

- **Rotations**, which introduce one zero at a time and touch two rows or columns.
- **Householder reflections**, which zero a whole subvector at once.

## Plane (Givens) rotations

The $(i,j)$ rotation is the identity except in rows and columns $i,j$ (Lang Eq. (8)):

$$
G_{ii} = G_{jj} = c,\qquad G_{ij} = s,\qquad G_{ji} = -s,\qquad c^2+s^2 = 1 .
\label{givens}
$$

It is orthogonal, and $c = \cos\theta$, $s = \sin\theta$ for some angle. The angle itself is never needed.

**Zeroing an entry.** To annihilate $x_j$ against $x_i$, choose (Lang Eq. (9))

$$
r = \sqrt{x_i^2+x_j^2},\qquad c = \frac{x_i}{r},\qquad s = -\frac{x_j}{r}
\quad\Longrightarrow\quad
(\mathbf G^{\mathsf T}\mathbf x)_i = r,\quad (\mathbf G^{\mathsf T}\mathbf x)_j = 0 .
\label{givens-cs}
$$

Check: $(\mathbf G^{\mathsf T}\mathbf x)_i = cx_i - sx_j = (x_i^2+x_j^2)/r$ and $(\mathbf G^{\mathsf T}\mathbf x)_j = sx_i + cx_j = 0$. Compute $r$ with `hypot` so that $x_i^2+x_j^2$ cannot overflow.

**Applying it.** $\mathbf A\mapsto\mathbf G^{\mathsf T}\mathbf A$ changes only rows $i$ and $j$:

$$
\mathbf a_i \leftarrow c\,\mathbf a_i - s\,\mathbf a_j,\qquad
\mathbf a_j \leftarrow s\,\mathbf a_i + c\,\mathbf a_j
\qquad(\text{both from the old rows}).
$$

This costs $4m$ multiplications and $2m$ additions for an $n\times m$ matrix. $\mathbf A\mapsto\mathbf A\mathbf G$ does the same to columns $i,j$.

!!! warning "A sign in Lang"
    Lang's text (p. 239) prints the row update as $c\,\mathbf a_i + s\,\mathbf a_j$, $-s\,\mathbf a_i + c\,\mathbf a_j$. With his own Eqs. (8)-(9) that combination is $\mathbf G\mathbf A$, not $\mathbf G^{\mathsf T}\mathbf A$. On $\mathbf x = (3,4)$ it gives $(-1.4, 4.8)$ instead of $(5,0)$. The formulas above are consistent with Eqs. [[#givens]]-[[#givens-cs]] (checked numerically).

**Symmetric two-sided use.** $\mathbf A\mapsto\mathbf G^{\mathsf T}\mathbf A\mathbf G$ keeps $\mathbf A$ symmetric, so only one triangle needs updating: about $6n$ flop. The backward error of one application is at most $6\varepsilon\|\mathbf A\|_F$. *Fast Givens* rotations scale $\mathbf G$ implicitly and halve the multiplications. Rotations in disjoint planes commute and can be applied in parallel.

Rotations are the tool when the zero pattern matters: chasing a bulge down a band ([[householder-tridiagonalization]], [[tridiagonal-qr-iteration]]), or zeroing one chosen entry ([[jacobi-eigenvalue-method]]). The $2\times2$ matrix that diagonalizes a symmetric $2\times2$ block in [[matrix-eigenvalue-problem]] has determinant $-1$, so it is a reflection. The rotation with the same angle does the same job. A rotation between two orbitals $p,q$ ([[orbital-rotations]]) is exactly Eq. [[#givens]] acting on the coefficient matrix.

## Householder reflections

For $\mathbf y\ne0$,

$$
\mathbf H = \mathbf 1 - \tau\,\mathbf y\mathbf y^{\mathsf T},\qquad \tau = \frac{2}{\mathbf y^{\mathsf T}\mathbf y}.
\label{house}
$$

$\mathbf H$ is symmetric and orthogonal ($\mathbf H^2 = \mathbf 1 - 2\tau\mathbf y\mathbf y^{\mathsf T} + \tau^2\mathbf y(\mathbf y^{\mathsf T}\mathbf y)\mathbf y^{\mathsf T} = \mathbf 1$). It reflects through the hyperplane orthogonal to $\mathbf y$: the component along $\mathbf y$ changes sign, everything orthogonal to $\mathbf y$ is unchanged.

**Mapping $\mathbf x$ onto a multiple of $\mathbf e_1$.** Let $\sigma = \operatorname{sign}(x_1)$ (with $\operatorname{sign}0 = 1$) and

$$
\mathbf y = \mathbf x + \sigma\|\mathbf x\|_2\,\mathbf e_1 .
\label{house-y}
$$

Then $\mathbf y^{\mathsf T}\mathbf x = \|\mathbf x\|^2 + \sigma\|\mathbf x\|x_1$ and $\mathbf y^{\mathsf T}\mathbf y = 2(\|\mathbf x\|^2+\sigma\|\mathbf x\|x_1)$, so $\tau\,\mathbf y^{\mathsf T}\mathbf x = 1$ and

$$
\mathbf H\mathbf x = \mathbf x - \mathbf y(\tau\mathbf y^{\mathsf T}\mathbf x) = \mathbf x - \mathbf y = -\sigma\|\mathbf x\|_2\,\mathbf e_1 .
\label{house-x}
$$

To zero entries $i+1,\dots,j$ only, apply this to the subvector $\mathbf x(i{:}j)$ and pad $\mathbf y$ with zeros (Lang Eq. (11)). Only entries $i$ to $j$ change.

**Why that sign.** The other sign, $y_1 = x_1-\sigma\|\mathbf x\|$, is just as valid algebraically. But when $\mathbf x$ is nearly parallel to $\mathbf e_1$ the subtraction cancels, $y_1$ loses all its digits, and $\mathbf H$ no longer maps $\mathbf x$ to $\mathbf e_1$. With the sign of Eq. [[#house-y]] the two terms add.

**Applying it without forming H.** For an $\ell\times m$ block ($\ell$ = active length of $\mathbf y$):

$$
\mathbf z^{\mathsf T} = \tau\,\mathbf y^{\mathsf T}\mathbf A,\qquad
\mathbf H\mathbf A = \mathbf A - \mathbf y\mathbf z^{\mathsf T}.
$$

This is one matrix–vector product and one rank-1 update, $4\ell m$ flop. Forming $\mathbf H$ and multiplying would cost $2\ell^2m$.

**Symmetric two-sided update.** Expanding $\mathbf H\mathbf A\mathbf H$ and setting $\mathbf z = \tau\mathbf A\mathbf y$ gives

$$
\mathbf H\mathbf A\mathbf H = \mathbf A - \mathbf y\mathbf z^{\mathsf T} - \mathbf z\mathbf y^{\mathsf T} + \tau(\mathbf y^{\mathsf T}\mathbf z)\,\mathbf y\mathbf y^{\mathsf T}.
$$

With $\mathbf v = \mathbf z - \tfrac12\tau(\mathbf y^{\mathsf T}\mathbf z)\,\mathbf y$ the last three terms combine into a symmetric rank-2 update (Lang Eqs. (14)-(15)):

$$
\mathbf H\mathbf A\mathbf H = \mathbf A - \mathbf y\mathbf v^{\mathsf T} - \mathbf v\mathbf y^{\mathsf T}.
\label{house-sym}
$$

Updating only one triangle, this costs $4n^2$ flop, the same as a one-sided update of a non-symmetric matrix. The backward error is at most $c\,n\varepsilon\|\mathbf A\|_F$ with a small constant $c$.

## Blocking: the WY representation

Single rotations and reflections are BLAS-2 operations: each matrix element is used $O(1)$ times per memory access. To reach matrix–matrix (BLAS-3) speed, accumulate $k$ reflections first and apply them together. Bischof and Van Loan showed that $\mathbf Q = \mathbf H_1\cdots\mathbf H_k$ has the form

$$
\mathbf Q = \mathbf 1 - \mathbf W\mathbf Y^{\mathsf T}\qquad(\mathbf W,\mathbf Y\in\mathbb R^{n\times k}).
\label{wy}
$$

*Construction.* For $k=1$: $\mathbf W = \tau_1\mathbf y_1$, $\mathbf Y = \mathbf y_1$. Appending $\mathbf H_{k+1}$:

$$
\mathbf Q\mathbf H_{k+1} = \mathbf 1 - \mathbf W\mathbf Y^{\mathsf T} - \tau_{k+1}\mathbf Q\mathbf y_{k+1}\mathbf y_{k+1}^{\mathsf T}
= \mathbf 1 - \big(\mathbf W\,|\,\tau_{k+1}\mathbf Q\mathbf y_{k+1}\big)\big(\mathbf Y\,|\,\mathbf y_{k+1}\big)^{\mathsf T}.
$$

The columns of $\mathbf Y$ are just the $\mathbf y_j$. Applying $\mathbf Q^{\mathsf T}\mathbf A = \mathbf A - \mathbf Y(\mathbf W^{\mathsf T}\mathbf A)$ is then two matrix–matrix products.

The **compact WY form** of Schreiber and Van Loan stores an upper-triangular $k\times k$ matrix $\mathbf T$ instead of $\mathbf W$:

$$
\mathbf Q = \mathbf 1 - \mathbf Y\mathbf T\mathbf Y^{\mathsf T},\qquad
\tilde{\mathbf T} = \begin{pmatrix}\mathbf T & -\tau_{k+1}\mathbf T\mathbf Y^{\mathsf T}\mathbf y_{k+1}\\ \mathbf 0^{\mathsf T} & \tau_{k+1}\end{pmatrix}.
\label{cwy}
$$

It needs less storage, but applying it takes a third matrix product. (Lang prints the new column as $-\tau_{k+1}\mathbf T\mathbf y_{k+1}$. The factor $\mathbf Y^{\mathsf T}$ is needed for the dimensions to match, and the form above is the one verified numerically.) LAPACK applies blocks of reflections this way.

!!! example "Worked example"
    **Rotation.** $\mathbf x = (3,4)$: $r = 5$, $c = 0.6$, $s = -0.8$, and $\mathbf G^{\mathsf T}\mathbf x = (5, 0)$ (computed: $(5, -4.4\times10^{-16})$).

    **Reflection.** $\mathbf x = (3,1,5,1)$: $\|\mathbf x\| = 6$, $\sigma = +1$, $\mathbf y = (9,1,5,1)$, $\mathbf y^{\mathsf T}\mathbf y = 108$, $\tau = 1/54$. Then $\mathbf H\mathbf x = (-6,0,0,0)$, as Eq. [[#house-x]] predicts. The computed zeros are of order $10^{-16}$.

    **Cancellation.** $\mathbf x = (1, 10^{-9}, 0)$, so $\|\mathbf x\| = \sqrt{1+10^{-18}}$, which rounds to exactly 1.

    | choice of $y_1$ | computed $y_1$ | computed $(\mathbf H\mathbf x)_2$ (should be 0) |
    |---|---:|---:|
    | $x_1 - \|\mathbf x\|$ | $0$ (true value $-5\times10^{-19}$) | $-1.0\times10^{-9}$ |
    | $x_1 + \|\mathbf x\|$ (Eq. [[#house-y]]) | $2$ | $0$ |

    Both reflections are orthogonal to machine precision. The wrong sign gives an exact reflection of the wrong vector.

    **Checks.** The rank-1 application equals $\mathbf H\mathbf A$; Eq. [[#house-sym]] equals $\mathbf H\mathbf S\mathbf H$ for a random symmetric $\mathbf S$. For three reflections of length 6, $\|\mathbf H_1\mathbf H_2\mathbf H_3 - (\mathbf 1-\mathbf W\mathbf Y^{\mathsf T})\| = \|\mathbf H_1\mathbf H_2\mathbf H_3-(\mathbf 1-\mathbf Y\mathbf T\mathbf Y^{\mathsf T})\| = 5\times10^{-16}$, with $\mathbf T$ upper triangular.

## Source

Grotendorst, *Modern Methods and Algorithms of Quantum Chemistry* (NIC Series Vol. 3, 2nd ed., John von Neumann Institute for Computing, Jülich, 2000): chapter by B. Lang, "Direct Solvers for Symmetric Eigenvalue Problems", pp. 231-257, Secs. 2.3, 2.4, 3, pp. 236-241, Eqs. (8)-(17).

The derivations of Eqs. [[#house-x]], [[#house-sym]] and of the WY recursion are mine. Numbers and the two sign checks: `Claude outputs/part7_ch1_numerical_linear_algebra.py`, section B.
