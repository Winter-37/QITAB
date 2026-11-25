---
id: schmidt-decomposition-and-purification
title: The Schmidt decomposition and purification
summary: Any pure state of two systems can be written as Σ λ_i |i_A⟩|i_B⟩ with orthonormal sets on each side and non-negative Schmidt coefficients; the decomposition is the singular value decomposition of the coefficient matrix. Consequences: the two reduced density operators have the same nonzero spectrum, the number of terms (Schmidt number) is at most the smaller dimension and measures entanglement, and every mixed state is the reduced state of a pure state on a larger space (purification), unique up to a unitary on the added system. Also shows why no such decomposition exists for three systems.
status: in-progress
kind: theory
level: intermediate
tags: [schmidt-decomposition, schmidt-number, purification, entanglement, entanglement-entropy, singular-value-decomposition, reduced-density-operator, bipartite-state, nielsen-chuang]
prerequisites: [tensor-products-and-partial-trace, polar-and-singular-value-decompositions]
related: [density-operators-and-mixed-states, natural-orbitals, one-particle-rdm]
order: 20
date: 2026-11-17
---

## The theorem

**Theorem (Schmidt decomposition).** For any pure state $|\psi\rangle$ of a composite system $AB$ there are orthonormal states $|i_A\rangle$ of $A$ and $|i_B\rangle$ of $B$ such that

$$
\boxed{\,|\psi\rangle = \sum_i\lambda_i\,|i_A\rangle|i_B\rangle ,\qquad \lambda_i\ge0 ,\qquad \sum_i\lambda_i^2 = 1\,}
$$

The $\lambda_i$ are the **Schmidt coefficients** and the number of nonzero ones is the **Schmidt number** (or Schmidt rank).

**Proof.** In fixed bases $|j\rangle$ of $A$ and $|k\rangle$ of $B$, $|\psi\rangle = \sum_{jk}a_{jk}|j\rangle|k\rangle$, with $a$ an $m\times n$ matrix. Its singular value decomposition ([[polar-and-singular-value-decompositions]]) is $a = u\,d\,v$, with $u$ and $v$ unitary and $d$ diagonal with non-negative entries $\lambda_i$. Then

$$
|\psi\rangle = \sum_{i,j,k}u_{ji}\,\lambda_i\,v_{ik}\,|j\rangle|k\rangle = \sum_i\lambda_i\Big(\sum_ju_{ji}|j\rangle\Big)\Big(\sum_kv_{ik}|k\rangle\Big) ,
$$

and the bracketed states are orthonormal because $u$ and $v$ are unitary. The same proof covers $m\neq n$, where at most $\min(m,n)$ coefficients are nonzero.

A general state $\sum_{jk}a_{jk}|j\rangle|k\rangle$ has $mn$ terms; the Schmidt form has at most $\min(m,n)$, with a single sum. The price is that the bases depend on the state.

## Consequences

**Equal spectra.** From the Schmidt form,

$$
\rho^A = \mathrm{tr}_B|\psi\rangle\langle\psi| = \sum_i\lambda_i^2|i_A\rangle\langle i_A| ,\qquad \rho^B = \sum_i\lambda_i^2|i_B\rangle\langle i_B| .
$$

The two reduced density operators ([[tensor-products-and-partial-trace]]) have the same nonzero eigenvalues $\lambda_i^2$, even when $A$ and $B$ have different dimensions, and the Schmidt vectors are their eigenvectors. Any function of the spectrum, such as purity or entropy, is the same for both halves. For a random state of a qutrit and a ququart, the decomposition reconstructs the state exactly, the spectra of $\rho^A$ and $\rho^B$ both equal $\lambda_i^2$, and $\rho^B$ has rank 3 in dimension 4.

**Entanglement.** The state is a product state if and only if its Schmidt number is 1. The **entanglement entropy** $S = -\sum_i\lambda_i^2\ln\lambda_i^2$, the von Neumann entropy of either reduced state ([[density-operators-and-mixed-states]]), measures how entangled a pure bipartite state is. Schmidt coefficients cannot be changed by unitaries acting on $A$ and $B$ separately, so these are properties of the state, not of a basis.

!!! example "Three two-qubit states (Nielsen and Chuang, Exercise 2.79)"

    | state | Schmidt coefficients | Schmidt number | entropy of $\rho^A$ |
    |---|---|---|---|
    | $(\lvert00\rangle + \lvert11\rangle)/\sqrt2$ | $1/\sqrt2,\ 1/\sqrt2$ | 2 | $\ln2 = 0.6931$ |
    | $(\lvert00\rangle + \lvert01\rangle + \lvert10\rangle + \lvert11\rangle)/2$ | $1,\ 0$ | 1 | 0 |
    | $(\lvert00\rangle + \lvert01\rangle + \lvert10\rangle)/\sqrt3$ | $0.934172,\ 0.356822$ | 2 | 0.3813 |

    The second state is $|{+}\rangle|{+}\rangle$, a product in disguise. For the third, the coefficient matrix $\frac{1}{\sqrt3}\begin{pmatrix}1&1\\1&0\end{pmatrix}$ has singular values $\sqrt{(3\pm\sqrt5)/6}$, which are the numbers in the table: the golden-ratio matrix of the polar-decomposition note appears again.

**Truncation.** Keeping the $k$ largest Schmidt terms and renormalizing gives the best approximation to $|\psi\rangle$ by a state of Schmidt number $k$ (by the low-rank property of the SVD); the discarded weight $\sum_{i>k}\lambda_i^2$ measures the error. This is the operation at the heart of the density-matrix renormalization group and other tensor-network methods. In electronic structure, the natural orbitals of a two-electron singlet are Schmidt vectors of the spatial wave function ([[natural-orbitals]]).

## Purification

Given a mixed state $\rho^A = \sum_ip_i|i_A\rangle\langle i_A|$ (spectral decomposition), introduce a **reference system** $R$ with the same dimension as $A$ and orthonormal basis $|i_R\rangle$, and define

$$
|AR\rangle = \sum_i\sqrt{p_i}\,|i_A\rangle|i_R\rangle .
$$

Then $\mathrm{tr}_R|AR\rangle\langle AR| = \sum_ip_i|i_A\rangle\langle i_A| = \rho^A$. Every mixed state is the reduced state of some pure state of a larger system; the construction is a Schmidt decomposition read backwards. $R$ need not have any physical meaning.

Purifications are not unique: $(1\otimes V_R)|AR\rangle$ for any unitary $V_R$ on $R$ gives the same $\rho^A$. Conversely, any two purifications of $\rho^A$ on the same reference space are related by such a unitary, since both must have Schmidt coefficients $\sqrt{p_i}$ and Schmidt vectors on $A$ that diagonalize $\rho^A$ (checked numerically for a random qutrit state). Purification lets statements about pure states be applied to mixed states, and the reverse.

## No Schmidt decomposition for three systems

One might hope to write any state of $ABC$ as $\sum_i\lambda_i|i_A\rangle|i_B\rangle|i_C\rangle$. This is impossible in general. In that form, $\rho^{AB} = \sum_i\lambda_i^2|i_Ai_B\rangle\langle i_Ai_B|$ would have product eigenvectors. For the W state

$$
|W\rangle = \frac{1}{\sqrt3}\big(|001\rangle + |010\rangle + |100\rangle\big) ,
$$

$\rho^{AB}$ has eigenvalues $\tfrac23$ and $\tfrac13$, and the eigenvector for $\tfrac23$, which is unique because the eigenvalue is nondegenerate, is $(|01\rangle + |10\rangle)/\sqrt2$, an entangled state of Schmidt number 2. So $|W\rangle$ has no three-party Schmidt form. Multipartite entanglement has no single canonical form, which is one reason it is harder to characterize than the bipartite case.

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010), Sec. 2.5, pp. 109-111: Theorem 2.7 (Schmidt decomposition) and its proof via the singular value decomposition, Eqs. (2.202)-(2.206); Schmidt number; purification, Eqs. (2.207)-(2.211); Exercises 2.76 (unequal dimensions), 2.77 (no tripartite form), 2.79 (the three states), 2.81 (freedom in purifications). Page numbers are those printed in the book.

The W-state argument for Exercise 2.77, the truncation remark and the connection to natural orbitals are my additions; all numbers are computed in `mathematics/part0_batch5.py` (section I).
