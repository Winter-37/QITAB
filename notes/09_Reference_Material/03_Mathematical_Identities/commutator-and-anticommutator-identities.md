---
id: commutator-and-anticommutator-identities
title: Commutator and anticommutator identities
summary: Product rules for commutators and their anticommutator forms, the Jacobi identity, the nested-commutator expansion of e^X A e^-X, the fermion anticommutation relations, commutators of a†_p a_q with single operators and with each other, and the commutator of the singlet excitation operators E_pq. All verified with explicit Jordan–Wigner matrices.
status: in-progress
kind: reference
level: intermediate
tags: [commutators, anticommutators, second-quantization, fermions, excitation-operators, identities]
prerequisites: [second-quantization-and-density-matrix-notation]
related: [baker-campbell-hausdorff, creation-and-annihilation-operators, second-quantized-operators, normal-ordering-and-wicks-theorem, pauli-matrix-identities]
order: 20
date: 2026-11-17
---

Notation: $[\hat A,\hat B] = \hat A\hat B - \hat B\hat A$, $\{\hat A,\hat B\} = \hat A\hat B + \hat B\hat A$.

## General operators

**Product rules.**

$$
[\hat A,\hat B\hat C] = [\hat A,\hat B]\hat C + \hat B[\hat A,\hat C],\qquad
[\hat A\hat B,\hat C] = \hat A[\hat B,\hat C] + [\hat A,\hat C]\hat B .
$$

**Anticommutator forms.** These are the ones to use with fermion operators, whose elementary relations are anticommutators:

$$
[\hat A,\hat B\hat C] = \{\hat A,\hat B\}\hat C - \hat B\{\hat A,\hat C\},\qquad
[\hat A\hat B,\hat C] = \hat A\{\hat B,\hat C\} - \{\hat A,\hat C\}\hat B .
$$

**Jacobi identity.**

$$
[\hat A,[\hat B,\hat C]] + [\hat B,[\hat C,\hat A]] + [\hat C,[\hat A,\hat B]] = 0 .
$$

**Similarity transformation** (Hadamard lemma; see [[baker-campbell-hausdorff]]):

$$
e^{\hat X}\hat Ae^{-\hat X} = \hat A + [\hat X,\hat A] + \tfrac1{2!}[\hat X,[\hat X,\hat A]] + \tfrac1{3!}[\hat X,[\hat X,[\hat X,\hat A]]] + \cdots
$$

This series terminates after four nested commutators for $e^{-\hat T}\hat He^{\hat T}$ in coupled-cluster theory, and is the starting point of every orbital-rotation expansion ($\hat X = \hat\kappa$).

**Hermiticity.** $[\hat A,\hat B]^\dagger = [\hat B^\dagger,\hat A^\dagger]$. If $\hat A$ and $\hat B$ are Hermitian, $[\hat A,\hat B]$ is anti-Hermitian and $i[\hat A,\hat B]$ is Hermitian.

## Fermion operators

For an orthonormal spin-orbital basis:

$$
\{a_P, a_Q^\dagger\} = \delta_{PQ},\qquad \{a_P, a_Q\} = \{a_P^\dagger, a_Q^\dagger\} = 0 .
$$

Consequences: $(a_P^\dagger)^2 = 0$ (Pauli), $\hat n_P^2 = \hat n_P$, and $a_P^\dagger a_Q^\dagger = -a_Q^\dagger a_P^\dagger$.

**Commutators with $a_P^\dagger a_Q$.** Applying the anticommutator forms above:

$$
[a_P^\dagger a_Q, a_R^\dagger] = \delta_{QR}\,a_P^\dagger,\qquad
[a_P^\dagger a_Q, a_R] = -\delta_{PR}\,a_Q,
$$

$$
[a_P^\dagger a_Q, a_R^\dagger a_S] = \delta_{QR}\,a_P^\dagger a_S - \delta_{PS}\,a_R^\dagger a_Q .
$$

So the operators $a_P^\dagger a_Q$ close under commutation (they generate the unitary group $U(M)$), and

$$
[\hat N, a_P^\dagger] = a_P^\dagger,\qquad [\hat N, a_P] = -a_P,\qquad [\hat N, a_P^\dagger a_Q] = 0 .
$$

Every operator with equal numbers of creators and annihilators conserves particle number.

## Singlet excitation operators

With $\hat E_{pq} = \sum_\sigma a_{p\sigma}^\dagger a_{q\sigma}$ over orthonormal spatial orbitals:

$$
[\hat E_{pq},\hat E_{rs}] = \delta_{qr}\hat E_{ps} - \delta_{ps}\hat E_{rq},\qquad
\hat E_{pq}^\dagger = \hat E_{qp},
$$

$$
[\hat E_{pq},\hat S^2] = [\hat E_{pq},\hat S_z] = [\hat E_{pq},\hat S_\pm] = 0,
$$

$$
\hat e_{pqrs} \equiv \hat E_{pq}\hat E_{rs} - \delta_{qr}\hat E_{ps} = \sum_{\sigma\tau}a_{p\sigma}^\dagger a_{r\tau}^\dagger a_{s\tau}a_{q\sigma}.
$$

The $\hat E_{pq}$ obey the same algebra as the spin-orbital $a_P^\dagger a_Q$ (they generate $U(n)$ on the orbital space) and commute with all total-spin operators, so they preserve $S$ and $M_S$. This is why spin-adapted methods are written in them ([[second-quantized-operators]], [[spin-tensor-operators]]).

## Checks

`part9_reference.py`, section D:

- general identities on random $6\times6$ matrices, and the Hadamard series summed to 25 terms for $\|\hat X\|\approx0.3$ (error $<10^{-12}$);
- fermion relations with Jordan–Wigner matrices for 4 spin orbitals (all index combinations);
- $\hat E_{pq}$ relations for 3 spatial orbitals (6 spin orbitals, $64\times64$ matrices), including the spin operators and the definition of $\hat e_{pqrs}$.

All hold to machine precision.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000), Sec. 1.5.2, p. 17 (canonical commutators), Sec. 1.8, p. 25 (commutator and anticommutator identities), Secs. 2.2-2.3, pp. 35-41 ($\hat E_{pq}$ and spin); Shavitt and Bartlett, *Many-Body Methods in Chemistry and Physics* (Cambridge University Press, 2009), Sec. 3.2, p. 55 (anticommutation relations). Derivations of the fermion relations are in [[creation-and-annihilation-operators]] and [[second-quantized-operators]]; this note collects the results and checks them numerically.
