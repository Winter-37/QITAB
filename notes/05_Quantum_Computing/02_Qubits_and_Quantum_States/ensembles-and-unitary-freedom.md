---
id: ensembles-and-unitary-freedom
title: Ensembles of states and the unitary freedom of the density operator
summary: Different ensembles {p_i, |ψ_i⟩} can give the same density operator, and then no measurement can tell them apart. Theorem 2.6 of Nielsen and Chuang characterizes the freedom exactly. Two sets of unnormalized vectors generate the same ρ if and only if √p_i|ψ_i⟩ = Σ_j u_ij √q_j|φ_j⟩ for a unitary u, after padding the shorter set with zero vectors. Worked for ρ = ¾|0⟩⟨0| + ¼|1⟩⟨1|, where u = H relates the eigen-ensemble to an equal mixture of two non-orthogonal states. Also covers the intrinsic characterization of density operators (positive, trace one), the purity test tr ρ² ≤ 1, the qubit Bloch ball with tr ρ² = (1 + |r|²)/2, and the weight 1/⟨ψ|ρ⁻¹|ψ⟩ of a state in a minimal ensemble.
status: in-progress
kind: theory
level: intermediate
tags: [density-operator, ensembles, unitary-freedom, mixed-state, bloch-ball, purity, minimal-ensemble, purification, nielsen-chuang]
prerequisites: [density-operators-and-mixed-states, quantum-postulates-for-information]
related: [schmidt-decomposition-and-purification, qubits-and-the-bloch-sphere, spectral-decomposition-and-normal-operators, one-particle-rdm]
order: 30
date: 2026-11-17
---

## Overview

A density operator $\rho=\sum_ip_i|\psi_i\rangle\langle\psi_i|$ ([[density-operators-and-mixed-states]]) describes a system known only statistically. It is tempting to read its eigen-decomposition as *the* ensemble: "the system is in eigenstate $|j\rangle$ with probability $\lambda_j$." That reading is wrong. Many different ensembles give the same $\rho$. Since all measurement statistics depend only on $\rho$ ([[quantum-postulates-for-information]]), no experiment can tell such ensembles apart. This note states exactly which ensembles are equivalent. The result is used later for quantum noise, error correction and purification.

## What makes an operator a density operator

**Theorem 2.5.** $\rho$ is the density operator of some ensemble if and only if $\operatorname{tr}\rho=1$ and $\rho\ge0$.

- *Only if:* $\operatorname{tr}\rho=\sum_ip_i=1$, and $\langle\varphi|\rho|\varphi\rangle=\sum_ip_i|\langle\varphi|\psi_i\rangle|^2\ge0$.
- *If:* a positive operator has a spectral decomposition $\rho=\sum_j\lambda_j|j\rangle\langle j|$ with $\lambda_j\ge0$, and the trace condition makes $\{\lambda_j,|j\rangle\}$ an ensemble.

**Purity.** $\operatorname{tr}\rho^2=\sum_j\lambda_j^2\le1$, with equality if and only if one $\lambda_j=1$, that is, the state is pure (Exercise 2.71).

**Qubits: the Bloch ball.** Every qubit density operator is $\rho=(I+\mathbf r\cdot\boldsymbol\sigma)/2$ with $\mathbf r$ real. The eigenvalues are $(1\pm|\mathbf r|)/2$, so positivity requires $|\mathbf r|\le1$; for example $|\mathbf r|=1.2$ gives an eigenvalue $-0.1$. Also

$$
\operatorname{tr}\rho^2=\tfrac12\big(1+|\mathbf r|^2\big),
$$

so pure states are the surface $|\mathbf r|=1$ and $I/2$ is the centre (Exercise 2.72). Mixing states mixes their Bloch vectors linearly, so the ball is convex.

## Same ρ, different ensembles

Take

$$
\rho=\tfrac34|0\rangle\langle0|+\tfrac14|1\rangle\langle1| ,
\qquad
|a\rangle=\sqrt{\tfrac34}\,|0\rangle+\sqrt{\tfrac14}\,|1\rangle ,\quad
|b\rangle=\sqrt{\tfrac34}\,|0\rangle-\sqrt{\tfrac14}\,|1\rangle .
$$

Then $\tfrac12|a\rangle\langle a|+\tfrac12|b\rangle\langle b|=\rho$. A source producing $|0\rangle$ three times in four and $|1\rangle$ otherwise cannot be told apart from one producing the non-orthogonal states $|a\rangle,|b\rangle$ with equal probability.

## Theorem 2.6: unitary freedom in the ensemble

Work with unnormalized vectors $|\tilde\psi_i\rangle=\sqrt{p_i}\,|\psi_i\rangle$, which **generate** $\rho=\sum_i|\tilde\psi_i\rangle\langle\tilde\psi_i|$.

**Theorem.** The sets $\{|\tilde\psi_i\rangle\}$ and $\{|\tilde\varphi_j\rangle\}$ generate the same operator if and only if

$$
|\tilde\psi_i\rangle=\sum_ju_{ij}\,|\tilde\varphi_j\rangle
$$

for some unitary matrix $u$, after padding the shorter set with zero vectors so that $u$ is square.

**Proof, "if".**

$$
\sum_i|\tilde\psi_i\rangle\langle\tilde\psi_i|=\sum_{jk}\Big(\sum_iu_{ki}^\dagger u_{ij}\Big)|\tilde\varphi_j\rangle\langle\tilde\varphi_k|=\sum_j|\tilde\varphi_j\rangle\langle\tilde\varphi_j| .
$$

**Proof, "only if".** Diagonalize $\rho=\sum_k\lambda_k|k\rangle\langle k|$ with $\lambda_k>0$ and set $|\tilde k\rangle=\sqrt{\lambda_k}|k\rangle$.

1. Any $|\psi\rangle$ orthogonal to all $|\tilde k\rangle$ has $0=\langle\psi|\rho|\psi\rangle=\sum_i|\langle\psi|\tilde\psi_i\rangle|^2$. So every $|\tilde\psi_i\rangle$ lies in the support of $\rho$ and can be written $|\tilde\psi_i\rangle=\sum_kc_{ik}|\tilde k\rangle$.
2. Equating $\sum_i|\tilde\psi_i\rangle\langle\tilde\psi_i|$ with $\sum_k|\tilde k\rangle\langle\tilde k|$, and using that the operators $|\tilde k\rangle\langle\tilde l|$ are linearly independent, gives $\sum_ic_{ik}c_{il}^*=\delta_{kl}$. The columns of $c$ are orthonormal, so $c$ extends to a unitary $v$.
3. Likewise $|\tilde\varphi_j\rangle=\sum_kw_{jk}|\tilde k\rangle$ with $w$ unitary. Then $u=vw^\dagger$ relates the two sets.

!!! example "Checks"
    - **The example above.** The two ensembles are related by $u=H$, the Hadamard matrix: $\sqrt{\tfrac12}|a\rangle=\tfrac{1}{\sqrt2}\big(\sqrt{\tfrac34}|0\rangle+\sqrt{\tfrac14}|1\rangle\big)$, and similarly for $|b\rangle$.
    - **"If" direction.** Three random vectors in $\mathbb C^3$ (weights 0.5, 0.3, 0.2), padded with two zero vectors and mixed by a random $5\times5$ unitary, generate the same $\rho$.
    - **"Only if" direction.** The coefficient matrices onto $\sqrt{\lambda_k}|k\rangle$ satisfy $c^\dagger c=I$ for both sets, and $u=c_Bc_A^\dagger$ reproduces the second set from the first.

## Consequences

- **Which states can appear in an ensemble.** Any state in the support of $\rho$ can be a member of some ensemble for $\rho$. In a **minimal** ensemble, with as many members as the rank of $\rho$, a member $|\psi\rangle$ must have weight

$$
p=\frac{1}{\langle\psi|\rho^{-1}|\psi\rangle},
$$

with $\rho^{-1}$ taken on the support (Exercise 2.73). Checked for a random rank-3 $\rho$: subtracting $p|\psi\rangle\langle\psi|$ leaves a positive operator of rank 2.
- **Purifications.** If $|\tilde\psi_i\rangle$ generate $\rho_A$, then $\sum_i|\tilde\psi_i\rangle|i_R\rangle$ purifies it. Theorem 2.6 is the reason two purifications differ only by a unitary on the reference system ([[schmidt-decomposition-and-purification]]).
- **Noise.** The operator-sum description of a quantum channel has the same freedom: its Kraus operators are fixed only up to a unitary mixing (Nielsen and Chuang, Chapter 8).
- **Chemistry analogue.** The one-particle density matrix of a correlated state ([[one-particle-rdm]]) is likewise not "a mixture of natural orbitals" in any physical sense. Its eigen-decomposition is only the most convenient of many representations.

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010):

- Sec. 2.4.1, pp. 99–101: ensembles, Eqs. (2.138)–(2.152).
- Sec. 2.4.2, pp. 101–105:
  - Theorem 2.5 and Eqs. (2.153)–(2.157);
  - the example (2.162)–(2.165);
  - Theorem 2.6, Eqs. (2.166)–(2.174);
  - Exercises 2.71–2.73.

Page numbers are those printed in the book. All checks are in `nielsen_chuang/part5_batch6.py` (section F).
