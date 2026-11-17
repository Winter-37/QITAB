---
id: quantum-teleportation
title: Quantum teleportation
summary: Alice sends an unknown qubit |ψ⟩ = α|0⟩ + β|1⟩ to Bob using one shared Bell pair and two classical bits. She applies a CNOT from her qubit to her half of the pair, then H, then measures both qubits. Each outcome m₁m₂ occurs with probability ¼ and leaves Bob with X^{m₂}Z^{m₁}|ψ⟩ up to phase, which Z^{m₁}X^{m₂} undoes. Before Bob receives the bits his qubit is exactly I/2, so nothing travels faster than light. Alice's original is destroyed, consistent with no-cloning. In the deferred-measurement version the classical corrections become a CNOT and a CZ, and Bob's qubit is exactly |ψ⟩. All steps are verified for random states.
status: in-progress
kind: algorithm
level: introductory
tags: [teleportation, bell-states, entanglement, deferred-measurement, classical-communication, no-signalling, nielsen-chuang]
prerequisites: [multi-qubit-states-and-bell-states, controlled-operations]
related: [no-cloning-theorem, measurement-in-quantum-circuits, epr-and-bell-inequalities]
order: 20
date: 2026-11-17
---

## Overview

Alice holds a qubit in an unknown state $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$ and must deliver it to Bob, but she can send only classical bits. Measuring $|\psi\rangle$ would destroy it and reveal almost nothing. Describing it exactly would take infinitely many bits. Teleportation solves the problem with **one shared Bell pair and two classical bits**. It is superdense coding run in reverse ([[multi-qubit-states-and-bell-states]]), and the first example of entanglement used as a consumable resource.

## The protocol

Qubit 1 holds $|\psi\rangle$ and qubit 2 is Alice's half of $|\beta_{00}\rangle$; both belong to Alice. Qubit 3 is Bob's half. The input is

$$
|\psi_0\rangle=|\psi\rangle|\beta_{00}\rangle=\tfrac1{\sqrt2}\Big[\alpha|0\rangle\big(|00\rangle+|11\rangle\big)+\beta|1\rangle\big(|00\rangle+|11\rangle\big)\Big].
$$

1. **CNOT, qubit 1 → qubit 2.**
$$
|\psi_1\rangle=\tfrac1{\sqrt2}\Big[\alpha|0\rangle(|00\rangle+|11\rangle)+\beta|1\rangle(|10\rangle+|01\rangle)\Big].
$$
2. **Hadamard on qubit 1**, then regroup by Alice's two qubits:
$$
|\psi_2\rangle=\tfrac12\Big[|00\rangle(\alpha|0\rangle+\beta|1\rangle)+|01\rangle(\alpha|1\rangle+\beta|0\rangle)+|10\rangle(\alpha|0\rangle-\beta|1\rangle)+|11\rangle(\alpha|1\rangle-\beta|0\rangle)\Big].
$$
3. **Alice measures** qubits 1 and 2, obtaining $m_1m_2$ with probability $\tfrac14$ each. Bob's qubit is then

| $m_1m_2$ | Bob holds | correction |
|---|---|---|
| 00 | $\alpha\lvert0\rangle+\beta\lvert1\rangle$ | $I$ |
| 01 | $\alpha\lvert1\rangle+\beta\lvert0\rangle$ | $X$ |
| 10 | $\alpha\lvert0\rangle-\beta\lvert1\rangle$ | $Z$ |
| 11 | $\alpha\lvert1\rangle-\beta\lvert0\rangle$ | $ZX$ |

4. **Alice sends $m_1m_2$**, and Bob applies $Z^{m_1}X^{m_2}$, which returns exactly $|\psi\rangle$. In a circuit diagram $X$ is drawn first; in the matrix product the rightmost factor acts first.

Checked for a random $|\psi\rangle$: all four probabilities equal $\tfrac14$, Bob's four conditional states match the table, and each correction restores $|\psi\rangle$ exactly, with no phase left over.

Steps 1–2 followed by a computational-basis measurement are a **Bell measurement** on Alice's two qubits ([[measurement-in-quantum-circuits]]). Teleportation is therefore: measure $|\psi\rangle$ jointly with half a Bell pair in the Bell basis, then apply the Pauli correction indicated by the result.

## What is and is not transmitted

- **No faster-than-light signalling.** Before Bob learns $m_1m_2$, his qubit is an equal mixture of the four states in the table, which is $I/2$ for every $|\psi\rangle$ (verified). No local operation tells him anything until the classical bits arrive, and those travel no faster than light.
- **No cloning.** After the measurement Alice's qubits are in a computational basis state that carries no trace of $\alpha,\beta$. The state has moved, not been copied ([[no-cloning-theorem]]).
- **Accounting.** One ebit plus two classical bits transmit one qubit. Superdense coding uses one ebit plus one transmitted qubit to send two classical bits. Neither protocol can be improved, and together they show the exchange rate between entanglement, qubits and bits.
- **Information.** Each outcome is uniformly random, independent of $|\psi\rangle$. The measurement reveals nothing about the state, which is why it does not destroy it. Quantum error correction relies on the same idea.

## Deferred-measurement form

Classically controlled gates can be replaced by quantum-controlled ones, with all measurements moved to the end ([[measurement-in-quantum-circuits]]). Replacing "if $m_2$ then $X$" and "if $m_1$ then $Z$" by a CNOT from qubit 2 to 3 and a CZ from qubit 1 to 3 gives a purely unitary circuit (N&C Figure 4.15). The final state is

$$
|{+}\rangle|{+}\rangle|\psi\rangle ,
$$

so Bob's qubit is exactly $|\psi\rangle$, and Alice's qubits would give uniformly random results if measured (verified). The two-way physical interpretation is lost, but the overall operation is the same.

## Uses beyond communication

- **Gate teleportation.** Teleporting through a pre-prepared entangled resource applies a gate to the teleported state. This is how $T$ gates are supplied in fault-tolerant architectures (magic-state injection) and how measurement-based quantum computing works.
- **Entanglement swapping and repeaters.** Teleporting half of one Bell pair entangles qubits that never interacted. This is the basis of quantum networks.
- **Hardware benchmark.** Teleportation with mid-circuit measurement and feed-forward is a standard test of dynamic-circuit capability.

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010):

- Sec. 1.3.7, pp. 26–28: the protocol, Eqs. (1.28)–(1.36), Figure 1.13, the corrections $Z^{M_1}X^{M_2}$, and the discussion of signalling and cloning.
- Sec. 4.4, pp. 186–187: the deferred-measurement circuit, Figure 4.15.

Page numbers are those printed in the book. The applications in the last section are general knowledge, not from these pages. All checks are in `nielsen_chuang/part5_batch7.py` (section B).
