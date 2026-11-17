---
id: polar-and-singular-value-decompositions
title: Polar and singular value decompositions
summary: Every linear operator is a unitary times a positive operator (polar decomposition, A = UJ = KU with J = √(A†A), K = √(AA†)), and every matrix is U Σ V† with non-negative singular values (SVD). Covers the proofs from the spectral theorem, a worked 2×2 example whose singular values are the golden ratio and its inverse, the relation to eigenvalues of A†A, optimal low-rank approximation by truncating the SVD, and Löwdin symmetric orthogonalization as the polar decomposition of the basis matrix.
status: in-progress
kind: theory
level: intermediate
tags: [polar-decomposition, singular-value-decomposition, svd, low-rank-approximation, eckart-young, lowdin-orthogonalization, positive-operator, nielsen-chuang]
prerequisites: [spectral-decomposition-and-normal-operators, functions-of-matrices]
related: [schmidt-decomposition-and-purification, basis-orthogonalization, unitary-matrices-exponential-logarithm, natural-orbitals]
order: 55
date: 2026-11-17
---

## Why another decomposition

The spectral theorem ([[spectral-decomposition-and-normal-operators]]) covers normal operators only, and only square ones. The polar and singular value decompositions cover every operator, by splitting it into pieces that are well understood: unitary operators, which rotate, and positive operators, which stretch along orthogonal axes.

## The polar decomposition

**Theorem.** For any linear operator $A$ on $V$ there are a unitary $U$ and positive operators $J$, $K$ with

$$
\boxed{\,A = UJ = KU ,\qquad J = \sqrt{A^\dagger A} ,\qquad K = \sqrt{AA^\dagger}\,}
$$

$J$ and $K$ are unique; $U$ is unique if $A$ is invertible, and then $U = AJ^{-1}$. The two forms are called the left and right polar decompositions. They generalize $z = e^{i\theta}|z|$ for complex numbers.

**Proof.** $A^\dagger A$ is positive, so $J = \sqrt{A^\dagger A}$ exists, with spectral decomposition $J = \sum_i\lambda_i|i\rangle\langle i|$, $\lambda_i\ge0$. Put $|\psi_i\rangle = A|i\rangle$; then $\langle\psi_i|\psi_j\rangle = \langle i|J^2|j\rangle = \lambda_i^2\delta_{ij}$. For $\lambda_i\neq0$ the vectors $|e_i\rangle = |\psi_i\rangle/\lambda_i$ are orthonormal; extend them by Gram-Schmidt to an orthonormal basis $\{|e_i\rangle\}$ and set $U = \sum_i|e_i\rangle\langle i|$. Then $UJ|i\rangle = \lambda_i|e_i\rangle = A|i\rangle$ for every $i$ (both sides vanish when $\lambda_i = 0$), so $A = UJ$. Finally $A = UJU^\dagger U = KU$ with $K = UJU^\dagger$ positive, and $AA^\dagger = K^2$ identifies $K$.

!!! example "A 2×2 example"

    For $A = \begin{pmatrix}1&0\\1&1\end{pmatrix}$, $A^{\rm T}A = \begin{pmatrix}2&1\\1&1\end{pmatrix}$ and

    $$
    J = \frac{1}{\sqrt5}\begin{pmatrix}3&1\\1&2\end{pmatrix} ,\qquad K = \frac{1}{\sqrt5}\begin{pmatrix}2&1\\1&3\end{pmatrix} ,\qquad U = \frac{1}{\sqrt5}\begin{pmatrix}2&-1\\1&2\end{pmatrix} .
    $$

    $U$ is a rotation by $\arctan\tfrac12 = 26.6^\circ$, and $UJ = KU = A$ (checked numerically, and against SciPy's `polar`). The eigenvalues of $J$, which are the singular values below, are $\varphi = 1.618034$ and $1/\varphi = 0.618034$, with $\varphi$ the golden ratio, because $\det A^{\rm T}A = 1$ and $\mathrm{tr}A^{\rm T}A = 3$.

## The singular value decomposition

**Theorem.** Any $m\times n$ matrix $A$ can be written

$$
\boxed{\,A = U\Sigma V^\dagger = \sum_{i=1}^r\sigma_i\,|u_i\rangle\langle v_i|\,}
$$

with $U$ ($m\times m$) and $V$ ($n\times n$) unitary and $\Sigma$ ($m\times n$) zero except for the **singular values** $\sigma_1\ge\sigma_2\ge\dots\ge\sigma_r>0$ on its diagonal, $r$ being the rank of $A$.

For square $A$ it follows from the polar decomposition: write $A = SJ$ and $J = TDT^\dagger$ (spectral decomposition, $D$ diagonal, non-negative); then $A = (ST)D\,T^\dagger$. For rectangular $A$ the same reasoning works with the orthonormal sets padded to full bases.

**Relations.**

- $A^\dagger A = V\Sigma^\dagger\Sigma V^\dagger$ and $AA^\dagger = U\Sigma\Sigma^\dagger U^\dagger$: the $|v_i\rangle$ and $|u_i\rangle$ are eigenvectors of $A^\dagger A$ and $AA^\dagger$, and $\sigma_i^2$ their common nonzero eigenvalues. Numerically, computing the SVD directly is more accurate than diagonalizing $A^\dagger A$, which squares the condition number.
- For a normal matrix the singular values are the moduli of the eigenvalues; for a positive one they are the eigenvalues.
- $\|A\|_2 = \sigma_1$ (largest stretch), $\|A\|_F^2 = \sum\sigma_i^2$, and $|\det A| = \prod\sigma_i$ for square $A$.
- The polar factors are $U_{\rm polar} = UV^\dagger$, $J = V\Sigma V^\dagger$, $K = U\Sigma U^\dagger$ (square case).

## Low-rank approximation

Truncating the SVD after $k$ terms, $A_k = \sum_{i\le k}\sigma_i|u_i\rangle\langle v_i|$, gives the best rank-$k$ approximation to $A$ in both the Frobenius and the spectral norm:

$$
\|A - A_k\|_F = \Big(\sum_{i>k}\sigma_i^2\Big)^{1/2} ,\qquad \|A - A_k\|_2 = \sigma_{k+1} .
$$

This optimality result (associated with Eckart and Young) is not in the three books used for Part 0; it was checked numerically. For a random complex $6\times4$ matrix, the truncation errors equal the formulas to all digits for $k = 1,2,3$, and 3000 other rank-$k$ matrices close to $A_k$ all did worse (for $k = 2$: 2.6853 for the truncation against at best 2.6936).

Truncated SVDs, and their special case for positive matrices (truncated eigendecompositions, as in [[natural-orbitals]]), underlie the Schmidt decomposition and its truncation in tensor-network methods ([[schmidt-decomposition-and-purification]]), and density fitting and compression of integral tensors.

## Löwdin orthogonalization as a polar decomposition

Let the columns of $C$ ($m\times n$) be the expansion coefficients of $n$ linearly independent but nonorthogonal functions, with overlap matrix $S = C^\dagger C$. **Symmetric (Löwdin) orthogonalization** replaces $C$ by $CS^{-1/2}$. Since $S^{1/2} = \sqrt{C^\dagger C}$ is exactly the positive factor $J$ of the polar decomposition $C = UJ$,

$$
CS^{-1/2} = U ,
$$

the isometric factor of $C$. This explains its special property: of all orthonormal sets, it is the one closest to the original functions in the least-squares sense, $\|C - U\|_F$ minimal. For a random real $5\times3$ example, $\|C - CS^{-1/2}\|_F = 2.31587$, against 2.41436 for the Gram-Schmidt set and at least 2.31603 for 2000 nearby orthonormal sets. The procedure is the one used in [[basis-orthogonalization]].

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010), Sec. 2.1.10, pp. 78-79: Theorem 2.3 (polar decomposition) with proof, Corollary 2.4 (singular value decomposition), Exercises 2.48-2.50 (the last is the $2\times2$ example). Page numbers are those printed in the book.

The low-rank optimality and the polar interpretation of Löwdin orthogonalization are my additions (beyond the three books used for Part 0), checked in `mathematics/part0_batch5.py` (section B).
