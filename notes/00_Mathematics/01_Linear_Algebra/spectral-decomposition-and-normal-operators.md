---
id: spectral-decomposition-and-normal-operators
title: The spectral decomposition and normal operators
summary: Which operators can be diagonalized by a unitary change of basis? Exactly the normal ones, AA† = A†A, which include Hermitian, unitary and positive operators. Covers projectors, the spectral theorem in projector form A = Σ λ P_λ, its failure for non-normal matrices (with a test via the Frobenius norm), positive operators, functions of normal operators f(A) = Σ f(λ) P_λ, and the simultaneous diagonalization theorem for commuting Hermitian operators, including how to handle degeneracy in practice.
status: in-progress
kind: theory
level: intermediate
tags: [spectral-theorem, normal-operator, projector, positive-operator, simultaneous-diagonalization, commuting-observables, schur-decomposition, operator-functions, nielsen-chuang]
prerequisites: [matrix-eigenvalue-problem, functions-of-matrices, change-of-basis]
related: [polar-and-singular-value-decompositions, unitary-matrices-exponential-logarithm, tensor-products-and-partial-trace, eigenfunctions-of-hermitian-operators, symmetry-conservation-and-degeneracy]
order: 45
date: 2026-11-17
---

## Projectors

Let $W$ be a $k$-dimensional subspace of a $d$-dimensional inner-product space $V$, and $|1\rangle,\dots,|k\rangle$ an orthonormal basis of $W$ (extendable by Gram-Schmidt to a basis of $V$). The **projector** onto $W$ is

$$
P = \sum_{i=1}^k|i\rangle\langle i| ,
$$

independent of which orthonormal basis of $W$ is used. It is Hermitian and idempotent, $P^\dagger = P$, $P^2 = P$, and conversely every Hermitian idempotent operator is a projector, onto its range. $Q = 1 - P$ projects onto the orthogonal complement. Eigenvalues of a projector are 0 and 1, and $\mathrm{tr}P = k$.

## Normal operators and the spectral theorem

An operator $A$ is **normal** if

$$
AA^\dagger = A^\dagger A .
$$

Hermitian ($A^\dagger = A$), anti-Hermitian, unitary ($A^\dagger A = 1$) and positive operators are all normal; a general matrix is not.

**Theorem (spectral decomposition).** An operator on a finite-dimensional space is normal if and only if it is diagonal in some orthonormal basis. Equivalently, with $\lambda$ running over its distinct eigenvalues and $P_\lambda$ the projector onto the eigenspace of $\lambda$,

$$
\boxed{\,A = \sum_\lambda\lambda\,P_\lambda ,\qquad P_\lambda P_\mu = \delta_{\lambda\mu}P_\lambda ,\qquad \sum_\lambda P_\lambda = 1\,}
$$

The eigenvalues may be complex. They are real if and only if $A$ is Hermitian, of modulus one if and only if $A$ is unitary.

**Proof sketch** (by induction on the dimension). Let $\lambda$ be an eigenvalue, $P$ the projector onto its eigenspace and $Q = 1 - P$. Then $A = (P+Q)A(P+Q) = PAP + QAP + PAQ + QAQ$. Clearly $PAP = \lambda P$ and $QAP = 0$, since $A$ maps the eigenspace into itself. Normality gives $PAQ = 0$ as well: $A^\dagger$ also maps the eigenspace into itself (for $|v\rangle$ in it, $A(A^\dagger|v\rangle) = A^\dagger A|v\rangle = \lambda A^\dagger|v\rangle$), so $QA^\dagger P = 0$, whose adjoint is $PAQ = 0$. Finally $QAQ$ is normal on the smaller space, and the induction hypothesis diagonalizes it. The converse, that a unitarily diagonalizable matrix is normal, is a one-line check.

The Hermitian case, with real eigenvalues, is [[matrix-eigenvalue-problem]]; this theorem says that Hermiticity is more than is needed for an orthonormal eigenbasis.

**When it fails.** Every square matrix can be brought to upper-triangular form by a unitary (Schur decomposition, $A = UTU^\dagger$), with the eigenvalues on the diagonal of $T$. $A$ is normal exactly when $T$ is diagonal, which gives a practical test:

$$
\|A\|_F^2 = \sum_{ij}|A_{ij}|^2 = \sum_i|\lambda_i|^2\quad\Longleftrightarrow\quad A\ \text{normal} ,
$$

since the left side equals $\sum|T_{ij}|^2$ and the right side counts only its diagonal.

| matrix | normal? | eigenvectors | $\lVert A\rVert_F^2$ vs $\sum\lvert\lambda\rvert^2$ |
|---|---|---|---|
| random $4\times4$ with complex eigenvalues $1+2i$ (twice), $-0.5i$, $3$, built as $U\Lambda U^\dagger$ | yes | orthonormal | equal |
| $\begin{pmatrix}1&2\\0&3\end{pmatrix}$ | no | two, at $45^\circ$ to each other | 14 vs 10 |
| $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ | no | only one (defective) | 3 vs 2 |

Non-normal matrices do occur in physics: the coupled-cluster similarity-transformed Hamiltonian, the Jacobian of a nonsymmetric iteration, and the shift matrix above. For them eigenvalues still exist, but there is no orthonormal eigenbasis and left and right eigenvectors differ.

## Positive operators

$A$ is **positive** (positive semidefinite) if $\langle v|A|v\rangle$ is real and non-negative for every $|v\rangle$, and positive definite if it is strictly positive for $|v\rangle\neq0$. Over a complex space a positive operator is automatically Hermitian, so it has a spectral decomposition with eigenvalues $\lambda\ge0$. For any operator $B$, $B^\dagger B$ is positive, since $\langle v|B^\dagger B|v\rangle = \|B|v\rangle\|^2$. Overlap matrices and density operators ([[density-operators-and-mixed-states]]) are positive.

## Functions of normal operators

If $A = \sum\lambda P_\lambda$ is normal and $f$ is a function on the complex numbers, define

$$
f(A) = \sum_\lambda f(\lambda)\,P_\lambda .
$$

This agrees with the power series wherever the series converges, and it extends the construction of [[functions-of-matrices]] from Hermitian to normal operators. It defines the square root of a positive operator, the logarithm of a positive-definite one, and the exponential of any normal operator. For the normal matrix in the table, $\sum e^\lambda P_\lambda$ equals the numerically exponentiated matrix, and for a positive $B^\dagger B$ the spectral square root equals the general matrix square root.

## Commuting operators

**Theorem (simultaneous diagonalization).** Hermitian operators $A$ and $B$ commute if and only if there is an orthonormal basis in which both are diagonal.

If they share an eigenbasis they clearly commute. Conversely, let $[A,B] = 0$ and let $V_a$ be the eigenspace of $A$ with eigenvalue $a$. For $|v\rangle\in V_a$, $A(B|v\rangle) = BA|v\rangle = a\,B|v\rangle$, so $B$ maps $V_a$ into itself. Its restriction to $V_a$ is Hermitian and can be diagonalized within $V_a$. Doing this for every eigenvalue of $A$ produces a basis $|a,b\rangle$ of common eigenvectors.

The proof is also the algorithm. Diagonalizing $A$ alone fixes the eigenspaces but not a basis inside a degenerate one, and a numerical eigensolver returns an arbitrary basis there, in which $B$ is in general not diagonal.

!!! example "Two commuting operators with a degeneracy"

    $A$ and $B$ were built in a common random basis with eigenvalues $(1,1,2,5)$ and $(7,-3,4,4)$. They commute. After diagonalizing $A$, the $2\times2$ block of $B$ in the eigenspace $a = 1$ has off-diagonal elements of magnitude 0.598. Diagonalizing that block gives a basis in which both are diagonal, with labels $(a,b) = (1,-3),(1,7),(2,4),(5,4)$. Each pair of labels is unique, so $\{A,B\}$ is a complete set of commuting operators for this space, although neither operator alone is.

This is the mathematical content of compatible observables ([[generalized-uncertainty-principle]]) and of labelling states by symmetry quantum numbers ([[symmetry-conservation-and-degeneracy]]): diagonalize the Hamiltonian inside each block of a conserved quantity.

Related identities: the commutator $[A,B] = AB - BA$ and anticommutator $\{A,B\} = AB + BA$ satisfy $AB = \tfrac12([A,B] + \{A,B\})$. For the Pauli matrices $\{\sigma_j,\sigma_k\} = 2\delta_{jk}$ and $[\sigma_j,\sigma_k] = 2i\epsilon_{jkl}\sigma_l$, so distinct Pauli matrices anticommute.

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010), Sec. 2.1.4 (projectors, Eq. (2.35)), Sec. 2.1.6 (normal, unitary and positive operators; Box 2.2, Theorem 2.1, the spectral decomposition, p. 72; Exercises 2.13-2.25), Sec. 2.1.8 (operator functions, Eq. (2.56)), Sec. 2.1.9 (commutator and anticommutator; Theorem 2.2, simultaneous diagonalization, p. 77; Exercises 2.40-2.47), pp. 69-77. Page numbers are those printed in the book.

The Schur form, the Frobenius-norm test and the degenerate example are my additions, computed in `mathematics/part0_batch5.py` (section A).
