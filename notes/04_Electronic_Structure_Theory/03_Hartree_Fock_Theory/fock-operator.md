---
id: fock-operator
title: Coulomb, exchange, and Fock operators
summary: The spin-orbital Fock operator f = h + Σ_j (J_j − K_j), the local Coulomb and nonlocal exchange operators, their matrix elements, Hermiticity of f, cancellation of self-interaction, and orbital energies.
status: in-progress
kind: theory
level: intermediate
tags: [hartree-fock, fock-operator, coulomb-operator, exchange-operator, mean-field]
prerequisites: [slater-condon-rules, integral-notation]
related: [hartree-fock-equations, rhf, uhf, koopmans-theorem]
order: 10
date: 2026-11-03
conventions: [ia-letters, chemists-integrals, physicists-integrals, antisymmetrized-integrals]
---

## The Hartree-Fock eigenvalue equation

The Hartree-Fock spin orbitals solve a one-electron eigenvalue equation (derived in [[hartree-fock-equations]]):

$$
f(1)\,\chi_i(1) = \varepsilon_i\,\chi_i(1),
\qquad
f(1) = h(1) + v^{\text{HF}}(1).
$$

Here $h(1) = -\tfrac12\nabla_1^2 - \sum_A Z_A/r_{1A}$ is the core Hamiltonian, and the **Hartree-Fock potential** $v^{\text{HF}}$ is the average field that electron 1 feels from the other electrons. Because $v^{\text{HF}}$ depends on the occupied spin orbitals $\{\chi_j\}$, the equation is nonlinear and is solved iteratively: the self-consistent field.

Index letters as in the rest of Part 4: $i, j, k$ occupied, $a, b, c$ virtual, $p, q, r$ any. Szabo writes $a, b, c$ for occupied and $r, s, t$ for virtual orbitals ([[index-and-orbital-notation]]). Electron "1" stands for coordinate $\mathbf x_1$.

## Coulomb operator

$$
\mathcal J_j(1)\,\chi_i(1) = \Big[\int\mathrm d\mathbf x_2\ |\chi_j(2)|^2\,r_{12}^{-1}\Big]\chi_i(1).
$$

This is the electrostatic potential of the charge cloud $|\chi_j|^2$, evaluated at $\mathbf x_1$. It is **local**: the result at $\mathbf x_1$ needs only $\chi_i(\mathbf x_1)$. Its expectation value is the Coulomb integral,

$$
\langle\chi_i|\mathcal J_j|\chi_i\rangle = [ii|jj] = \langle ij|ij\rangle .
$$

## Exchange operator

$\mathcal K_j$ is defined by its action:

$$
\mathcal K_j(1)\,\chi_i(1) = \Big[\int\mathrm d\mathbf x_2\ \chi_j^*(2)\,r_{12}^{-1}\,\chi_i(2)\Big]\chi_j(1).
$$

It swaps the labels of the two electrons: $\chi_i$ ends up under the integral and $\chi_j$ outside. Finding $\mathcal K_j\chi_i$ at $\mathbf x_1$ needs $\chi_i$ everywhere, so it is **nonlocal**, an integral operator with kernel $\chi_j(1)\chi_j^*(2)/r_{12}$ ([[orthonormal-functions-and-operators]]). It has no classical analogue; it comes from antisymmetry. Its expectation value is the exchange integral,

$$
\langle\chi_i|\mathcal K_j|\chi_i\rangle = [ij|ji] = \langle ij|ji\rangle .
$$

## The Fock operator

$$
f(1) = h(1) + \sum_{j}^{N}\big[\mathcal J_j(1) - \mathcal K_j(1)\big].
$$

The sum is over all $N$ **occupied** spin orbitals, including $j = i$ when acting on $\chi_i$. This is harmless because

$$
\big[\mathcal J_i(1) - \mathcal K_i(1)\big]\chi_i(1) = 0 .
$$

The spurious repulsion of an electron with itself cancels exactly. Hartree theory, which lacks $\mathcal K$, and approximate density functionals do not have this cancellation (self-interaction error).

**Matrix elements (Szabo Ex. 3.1).**

$$
\langle\chi_p|f|\chi_q\rangle = \langle p|h|q\rangle + \sum_j^N\big([pq|jj] - [pj|jq]\big) = \langle p|h|q\rangle + \sum_j^N\langle pj||qj\rangle .
$$

**Hermiticity (Szabo Ex. 3.4).** $\langle p|h|q\rangle^* = \langle q|h|p\rangle$ and $\langle pj||qj\rangle^* = \langle qj||pj\rangle$, so $f_{pq}^* = f_{qp}$. The Fock operator is Hermitian, its eigenvalues are real, and its eigenfunctions can be chosen orthonormal.

## Orbital energies

Taking diagonal elements, with $\langle pj||pj\rangle = \langle pj|pj\rangle - \langle pj|jp\rangle$:

$$
\varepsilon_i = \langle i|h|i\rangle + \sum_{j}^{N}\langle ij||ij\rangle,
\qquad
\varepsilon_a = \langle a|h|a\rangle + \sum_{j}^{N}\langle aj||aj\rangle .
$$

**Occupied.** $\varepsilon_i$ is the core energy of $\chi_i$ plus Coulomb and exchange with the other $N-1$ electrons ($j=i$ cancels).

**Virtual.** $\varepsilon_a$ includes interaction with all $N$ occupied electrons, as if $\chi_a$ held an $(N+1)$th electron. This asymmetry is why virtual orbitals are poor descriptions of excited states and why Koopmans electron affinities are unreliable ([[koopmans-theorem]]).

**Sum of orbital energies is not the energy.** Summing $\varepsilon_i$ counts each pair interaction twice:

$$
\sum_i^N\varepsilon_i = \sum_i\langle i|h|i\rangle + \sum_{ij}\langle ij||ij\rangle,
\qquad
E_0 = \sum_i\langle i|h|i\rangle + \tfrac12\sum_{ij}\langle ij||ij\rangle = \sum_i\varepsilon_i - \tfrac12\sum_{ij}\langle ij||ij\rangle .
$$

## Fock operator as a nonlocal one-electron potential

The exact problem has $r_{12}^{-1}$ coupling all electrons. Hartree-Fock replaces it by $v^{\text{HF}}$:

- The **Coulomb part** is a local average potential.
- The **exchange part** is a nonlocal correction that keeps same-spin electrons apart (the Fermi hole, [[slater-determinants]]).

What is missing, instantaneous correlation of electron positions beyond exchange, is the correlation energy.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 3.1, pp. 111-115, Eqs. (3.1)-(3.23), Ex. 3.1, 3.4; orbital energies from Sec. 3.3.1, pp. 123-126.
