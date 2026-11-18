---
id: matrix-and-tensor-identities
title: Matrix, Kronecker and tensor identities
summary: Trace and determinant rules, block inversion by the Schur complement, the Woodbury and matrix-determinant lemmas, Kronecker-product rules including vec(AXB) = (Bᵀ⊗A)vec X, and Levi-Civita contractions. Each identity is checked numerically on random matrices.
status: in-progress
kind: reference
level: introductory
tags: [linear-algebra, identities, trace, determinant, schur-complement, woodbury, kronecker, levi-civita]
prerequisites: []
related: [matrices-and-determinants, functions-of-matrices, tensor-products-and-partial-trace, matrix-differentiation-identities, operator-and-matrix-notation]
order: 10
date: 2026-11-17
---

All matrices are square and $n\times n$ unless dimensions are given; inverses are assumed to exist where they appear.

## Trace and determinant

$$
\operatorname{tr}(\mathbf{ABC}) = \operatorname{tr}(\mathbf{BCA}) = \operatorname{tr}(\mathbf{CAB}),\qquad
\operatorname{tr}(\mathbf A^{\mathsf T}) = \operatorname{tr}\mathbf A,\qquad
\operatorname{tr}(\mathbf A\mathbf B) = \sum_{ij}A_{ij}B_{ji} .
$$

Only cyclic permutations are allowed: $\operatorname{tr}(\mathbf{ABC})\ne\operatorname{tr}(\mathbf{ACB})$ in general.

$$
\det(\mathbf{AB}) = \det\mathbf A\det\mathbf B,\qquad
\det(c\mathbf A) = c^n\det\mathbf A,\qquad
\ln\det\mathbf A = \operatorname{tr}\ln\mathbf A\ \ (\mathbf A\ \text{positive definite}),
$$

$$
(\mathbf{AB})^{-1} = \mathbf B^{-1}\mathbf A^{-1},\qquad (\mathbf{AB})^{\mathsf T} = \mathbf B^{\mathsf T}\mathbf A^{\mathsf T},\qquad(\mathbf{AB})^\dagger = \mathbf B^\dagger\mathbf A^\dagger .
$$

The trace of a projector is its rank; the trace of a density matrix is the particle number ([[density-matrix-conventions]]).

## Block matrices

For $\mathbf M = \begin{pmatrix}\mathbf P & \mathbf Q\\ \mathbf R & \mathbf S\end{pmatrix}$ with $\mathbf P$ invertible, define the **Schur complement** $\mathbf\Sigma = \mathbf S - \mathbf R\mathbf P^{-1}\mathbf Q$. Then

$$
\det\mathbf M = \det\mathbf P\,\det\mathbf\Sigma,
\qquad
\mathbf M^{-1} = \begin{pmatrix}\mathbf P^{-1} + \mathbf P^{-1}\mathbf Q\mathbf\Sigma^{-1}\mathbf R\mathbf P^{-1} & -\mathbf P^{-1}\mathbf Q\mathbf\Sigma^{-1}\\ -\mathbf\Sigma^{-1}\mathbf R\mathbf P^{-1} & \mathbf\Sigma^{-1}\end{pmatrix}.
$$

This is the algebra behind partitioning (Löwdin) and behind eliminating one block of a linear-response or Hessian system in favour of another.

## Low-rank updates

**Woodbury identity** ($\mathbf U$: $n\times k$, $\mathbf C$: $k\times k$, $\mathbf V$: $k\times n$):

$$
(\mathbf A + \mathbf{UCV})^{-1} = \mathbf A^{-1} - \mathbf A^{-1}\mathbf U\big(\mathbf C^{-1} + \mathbf V\mathbf A^{-1}\mathbf U\big)^{-1}\mathbf V\mathbf A^{-1}.
$$

For $k = 1$ this is the Sherman–Morrison formula. The **matrix determinant lemma** is the matching result for determinants:

$$
\det(\mathbf A + \mathbf u\mathbf v^{\mathsf T}) = \det\mathbf A\,\big(1 + \mathbf v^{\mathsf T}\mathbf A^{-1}\mathbf u\big).
$$

Quasi-Newton (BFGS) Hessian updates in geometry optimization are rank-two updates of this kind.

## Kronecker products

With $\mathbf A$ ($n\times n$) and $\mathbf E$ ($m\times m$):

$$
(\mathbf A\otimes\mathbf E)(\mathbf B\otimes\mathbf F) = \mathbf{AB}\otimes\mathbf{EF},\qquad
(\mathbf A\otimes\mathbf E)^{\mathsf T} = \mathbf A^{\mathsf T}\otimes\mathbf E^{\mathsf T},
$$

$$
\operatorname{tr}(\mathbf A\otimes\mathbf E) = \operatorname{tr}\mathbf A\operatorname{tr}\mathbf E,\qquad
\det(\mathbf A\otimes\mathbf E) = (\det\mathbf A)^m(\det\mathbf E)^n,
$$

$$
\operatorname{vec}(\mathbf{AXB}) = (\mathbf B^{\mathsf T}\otimes\mathbf A)\operatorname{vec}\mathbf X\qquad(\operatorname{vec}\ \text{stacks columns}).
$$

The eigenvalues of $\mathbf A\otimes\mathbf E$ are all products $\lambda_i\mu_j$. The vec identity turns a Sylvester equation $\mathbf{AX} + \mathbf{XB} = \mathbf C$ into the linear system $(\mathbf 1\otimes\mathbf A + \mathbf B^{\mathsf T}\otimes\mathbf 1)\operatorname{vec}\mathbf X = \operatorname{vec}\mathbf C$. Qubit operators are Kronecker products; for the order of the factors see [[qubit-ordering-conventions]].

## Levi-Civita and Kronecker delta

$\varepsilon_{ijk}$ is $+1$ for even permutations of $(1,2,3)$, $-1$ for odd ones, and 0 otherwise. Contractions:

$$
\sum_i\varepsilon_{ijk}\varepsilon_{imn} = \delta_{jm}\delta_{kn} - \delta_{jn}\delta_{km},\qquad
\sum_{ij}\varepsilon_{ijk}\varepsilon_{ijn} = 2\delta_{kn},\qquad
\sum_{ijk}\varepsilon_{ijk}\varepsilon_{ijk} = 6,
$$

$$
(\mathbf a\times\mathbf b)_i = \sum_{jk}\varepsilon_{ijk}a_jb_k,\qquad
\mathbf a\times(\mathbf b\times\mathbf c) = \mathbf b(\mathbf a\cdot\mathbf c) - \mathbf c(\mathbf a\cdot\mathbf b),\qquad
\det\mathbf A = \sum_{ijk}\varepsilon_{ijk}A_{1i}A_{2j}A_{3k}.
$$

The angular-momentum algebra $[\hat L_i,\hat L_j] = i\hbar\sum_k\varepsilon_{ijk}\hat L_k$ and the Pauli product rule ([[pauli-matrix-identities]]) are written with this symbol.

## Checks

Every identity above was evaluated on random real matrices ($n = 5$, $m = 3$; a $7\times7$ block matrix split $3+4$) in `part9_reference.py`, section C. All agree to better than $10^{-8}$ (determinants) or $10^{-10}$ (everything else).

## Source

Standard linear algebra; the identities are stated here without derivation and verified numerically. Related derivations: [[matrices-and-determinants]] (Szabo Ch. 1), [[tensor-products-and-partial-trace]] (Nielsen–Chuang Sec. 2.1.7).
