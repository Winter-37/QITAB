---
id: jacobi-eigenvalue-method
title: Jacobi's method for the symmetric eigenproblem
summary: Diagonalize A directly by plane rotations, each chosen to zero one off-diagonal pair. Every rotation lowers off(A)² by exactly 2A_ij². Classical and cyclic orderings converge quadratically in about log n sweeps. Too slow for full matrices (a sweep costs about as much as the whole reduction-based solve, about 3n³ flop), but fast for nearly diagonal matrices, parallel, and potentially very accurate. Includes the rotation formula, a sign remark on Lang's text, and sweep-by-sweep numbers.
status: in-progress
kind: algorithm
level: intermediate
tags: [jacobi-method, plane-rotation, off-diagonal-norm, cyclic-jacobi, quadratic-convergence, diagonally-dominant, parallel]
prerequisites: [givens-rotations-and-householder-reflections, matrix-eigenvalue-problem]
related: [tridiagonal-qr-iteration, choosing-a-symmetric-eigensolver, floating-point-and-eigenvalue-perturbation, orbital-rotations]
key: jacobi-t
order: 70
date: 2026-11-21
---

## Overview

Jacobi's method (1846) needs no tridiagonal reduction. It applies plane rotations to $\mathbf A$ itself until the off-diagonal part is negligible. The eigenvalues are then the diagonal entries, and the eigenvectors are the columns of the accumulated product of rotations. The $2\times2$ step was derived in [[matrix-eigenvalue-problem]]. This note treats the $n\times n$ algorithm.

## Off-diagonal norm

$$
\operatorname{off}(\mathbf A)^2 = \sum_{i\ne j}A_{ij}^2 = \|\mathbf A\|_F^2 - \sum_iA_{ii}^2 .
$$

(Evaluate it as the direct sum. The difference form cancels badly once $\mathbf A$ is nearly diagonal.)

## The Jacobi rotation

Use the rotation $\mathbf G$ of Lang's Eq. (8) in the $(i,j)$ plane ($G_{ii} = G_{jj} = c$, $G_{ij} = s$, $G_{ji} = -s$; see [[givens-rotations-and-householder-reflections]]). Write $a = A_{ii}$, $b = A_{ij}$, $d = A_{jj}$. The new off-diagonal entry is

$$
(\mathbf G^{\mathsf T}\mathbf A\mathbf G)_{ij} = b\,(c^2-s^2) + cs\,(a-d).
$$

Setting it to zero and dividing by $c^2$, with $t = s/c = \tan\theta$:

$$
t^2 + 2\tau t - 1 = 0,\qquad \tau = \frac{A_{jj}-A_{ii}}{2A_{ij}} .
$$

Take the root of smaller modulus, which keeps $|\theta|\le\pi/4$ and avoids cancellation:

$$
t = \frac{\operatorname{sign}(\tau)}{|\tau| + \sqrt{1+\tau^2}},\qquad c = \frac1{\sqrt{1+t^2}},\qquad s = t\,c .
\label{jacobi-t}
$$

!!! warning "Sign of τ in Lang"
    Lang (p. 254) writes $\tau = (A_{ii}-A_{jj})/(2A_{ij})$ with the same formula for $t$. With his Eq. (8) rotation that choice does *not* zero the entry. It does with $\mathbf G^{\mathsf T}$ in place of $\mathbf G$, i.e. the opposite angle. Numerically, on a random matrix, $A_{12}$ becomes $7.9\times10^{-1}$ instead of $2\times10^{-17}$. The two conventions differ only in the sign of $\theta$; use $\tau$ as above with Eq. (8).

**The decrease of off(A) is exact.** Orthogonal similarity preserves $\|\mathbf A\|_F$, so only the diagonal and off-diagonal parts trade weight. The transformation changes only rows and columns $i,j$:

- for each $k\notin\{i,j\}$, the pair $(A_{ki},A_{kj})$ is rotated, so $A_{ki}^2+A_{kj}^2$ is unchanged;
- inside the $2\times2$ block, $a^2+d^2+2b^2$ is invariant (its Frobenius norm), and $b$ becomes 0.

Hence

$$
\operatorname{off}(\mathbf G^{\mathsf T}\mathbf A\mathbf G)^2 = \operatorname{off}(\mathbf A)^2 - 2A_{ij}^2 .
\label{off-drop}
$$

Lang states that "off(A) drops by $2A(i,j)^2$". It is the *square* of off(A) that drops by this amount.

Zeros are not permanent: later rotations in planes sharing $i$ or $j$ refill them. The method still converges, because off(A)² decreases monotonically.

## Orderings and convergence

- **Classical Jacobi** always zeroes the largest $|A_{ij}|$. There are $n(n-1)$ off-diagonal entries, so $2A_{ij}^2\ge2\operatorname{off}^2/(n(n-1))$. Every rotation therefore multiplies off² by at most $1-2/(n(n-1))$: at least linear convergence. A finer analysis gives quadratic convergence. Searching for the maximum costs about $n^2/2$ comparisons per rotation, against $6n$ arithmetic operations, so the overhead dominates.
- **Cyclic Jacobi** zeroes the entries in a fixed order, row by row: $(2,1),(3,1),(3,2),(4,1),\dots,(n,n-1)$. One pass over all $n(n-1)/2$ entries is a **sweep**. With suitable care for the rotation angles it is also quadratically convergent.

Experience gives about $\log n$ sweeps. One sweep is $n(n-1)/2$ rotations at about $6n$ flop each, i.e. $\approx3n^3$ flop, plus the same again if eigenvectors are accumulated. The reduction-based solvers cost about as much as two sweeps, so Jacobi is usually not competitive for a full matrix.

**Where it wins.**

- **Nearly diagonal matrices.** If $\mathbf A$ is strongly diagonally dominant, a few sweeps suffice, and Jacobi can beat the reduction-based methods. Typical examples are a matrix re-diagonalized after a small change, or a matrix expressed in a basis that already nearly diagonalizes it.
- **Accuracy.** A carefully implemented Jacobi method can, in some cases, deliver much more accurate eigensystems than the other methods ([[floating-point-and-eigenvalue-perturbation]]).
- **Parallelism.** Rotations in disjoint planes, e.g. $(1,2),(3,4),(5,6),\dots$, commute and can be applied simultaneously. Suitable cyclic orders exploit this.

Generalized-eigenproblem variants exist, but according to Lang their convergence properties are not well known.

!!! example "Worked example: cyclic Jacobi on 5×5 matrices"
    **A random symmetric $5\times5$ matrix**, $\operatorname{off}(\mathbf A) = 5.996$. The first rotation, in the $(1,2)$ plane, leaves $A_{12} = -2.5\times10^{-17}$ and $|\theta| = 0.440\le\pi/4$. It lowers off² by $0.772319245999$, which equals $2A_{12}^2$ to all 12 printed digits, as in Eq. [[#off-drop]].

    | after sweep | 1 | 2 | 3 | 4 | 5 |
    |---|---:|---:|---:|---:|---:|
    | off(A) | 2.524 | $2.17\times10^{-1}$ | $8.81\times10^{-4}$ | $2.60\times10^{-9}$ | $4.4\times10^{-16}$ |

    The convergence is quadratic: each value is roughly the square of the previous one, times a constant below 1. The sorted diagonal matches `eigvalsh` to $2.7\times10^{-15}$, and the accumulated $\mathbf V$ diagonalizes the original matrix.

    **A diagonally dominant start**, $\mathrm{diag}(1,\dots,5) + 10^{-3}\times$(the same random symmetric matrix): off(A) is $2.9\times10^{-6}$ after one sweep, $8.2\times10^{-13}$ after two and $9.8\times10^{-19}$ after three.

    With the difference formula $\|\mathbf A\|_F^2-\sum A_{ii}^2$, the computed off(A) stalls at about $10^{-7}$, the square root of rounding noise. That is a measurement artefact, not a property of the method.

## Source

Grotendorst, *Modern Methods and Algorithms of Quantum Chemistry* (NIC Series Vol. 3, 2nd ed., John von Neumann Institute for Computing, Jülich, 2000): chapter by B. Lang, "Direct Solvers for Symmetric Eigenvalue Problems", pp. 231-257, Sec. 6.1, pp. 254-255.

The derivations of Eqs. [[#jacobi-t]] and [[#off-drop]] and the two remarks on Lang's text are mine, checked symbolically (`sympy`) and numerically. Numbers: `Claude outputs/part7_ch1_numerical_linear_algebra.py`, section G.
