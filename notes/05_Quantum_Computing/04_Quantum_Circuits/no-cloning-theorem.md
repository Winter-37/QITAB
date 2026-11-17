---
id: no-cloning-theorem
title: The no-cloning theorem
summary: No unitary maps |ψ⟩|s⟩ to |ψ⟩|ψ⟩ for every state: taking the inner product of two cloning equations gives ⟨ψ|φ⟩ = ⟨ψ|φ⟩², so only identical or orthogonal states can be copied. A CNOT copies |0⟩ and |1⟩ but turns |+⟩|0⟩ into a Bell state, whose overlap² with |+⟩|+⟩ is ½. Imperfect copying is allowed: the Bužek–Hillery universal cloner gives two copies, each with fidelity 5/6 for every input (my addition, verified). Consequences: unknown states cannot be read out from one copy, quantum states cannot be backed up, and intermediate data cannot be inspected without disturbing it.
status: in-progress
kind: theory
level: introductory
tags: [no-cloning, unitarity, linearity, quantum-copying, cloning-fidelity, nielsen-chuang]
prerequisites: [quantum-postulates-for-information, controlled-operations]
related: [projective-and-povm-measurements, quantum-teleportation, multi-qubit-states-and-bell-states]
order: 10
date: 2026-11-17
---

## Overview

Copying is the most basic operation on classical data. It underlies memory, backups, error correction by repetition, and debugging by inspection. For quantum states it is impossible. This note gives the one-line proof, shows where the naive copying circuit fails, and lists what follows. The theorem is behind several design constraints on quantum algorithms:

- results must be extracted by measurement statistics, not by reading out the state;
- error correction must work without copying;
- teleportation must destroy the original.

## The naive copy

A classical bit $x$ is copied by XOR-ing it onto a blank bit. The quantum analogue is a CNOT onto $|0\rangle$:

$$
\mathrm{CNOT}\,(a|0\rangle+b|1\rangle)|0\rangle=a|00\rangle+b|11\rangle ,
$$

whereas a copy would be

$$
(a|0\rangle+b|1\rangle)(a|0\rangle+b|1\rangle)=a^2|00\rangle+ab|01\rangle+ab|10\rangle+b^2|11\rangle .
$$

These agree only if $ab=0$. The circuit copies the basis states $|0\rangle$ and $|1\rangle$, that is, classical information, but turns $|+\rangle|0\rangle$ into the Bell state $|\beta_{00}\rangle$. Its overlap with $|+\rangle|+\rangle$ is $|\langle{+}{+}|\beta_{00}\rangle|^2=\tfrac12$.

There is also an information argument. After the circuit, measuring either qubit fixes the other completely, so no further information about $a,b$ can be gained. A true copy would leave a second, independent sample.

## The theorem

**Theorem (no-cloning).** No unitary $U$ and fixed blank state $|s\rangle$ satisfy $U(|\psi\rangle\otimes|s\rangle)=|\psi\rangle\otimes|\psi\rangle$ for all $|\psi\rangle$.

**Proof.** Suppose $U$ clones two states $|\psi\rangle$ and $|\varphi\rangle$:

$$
U|\psi\rangle|s\rangle=|\psi\rangle|\psi\rangle ,\qquad U|\varphi\rangle|s\rangle=|\varphi\rangle|\varphi\rangle .
$$

Take the inner product of the two equations. Unitarity preserves the left side, so

$$
\langle\psi|\varphi\rangle\langle s|s\rangle=\langle\psi|\varphi\rangle^2
\quad\Longrightarrow\quad x=x^2,\ \ x=\langle\psi|\varphi\rangle .
$$

So $x=0$ or $x=1$: a cloner can copy only states that are identical or orthogonal. A cloner for $|0\rangle$ and $|+\rangle$, with overlap $1/\sqrt2$, cannot exist.

**Remarks.**
- The proof uses only linearity and inner-product preservation. Allowing an ancilla in the machine ($U|\psi\rangle|s\rangle|m\rangle=|\psi\rangle|\psi\rangle|m_\psi\rangle$) gives $x=x^2\langle m_\psi|m_\varphi\rangle$. For $0<|x|<1$ this needs $|\langle m_\psi|m_\varphi\rangle|=1/|x|>1$, which is impossible.
- Non-unitary devices do no better. A device that clones non-orthogonal states perfectly would let two non-orthogonal states be distinguished with certainty, by cloning many times and measuring, which [[projective-and-povm-measurements]] forbids.
- Mixed-state versions exist ("no-broadcasting") and need more care in their definitions (N&C Box 12.1, discussion).

## Imperfect cloning

The theorem forbids perfect copies, not approximate ones. A standard example, not in Nielsen and Chuang, is the **Bužek–Hillery universal cloner**. It uses one input qubit, a blank and an ancilla:

$$
|0\rangle\mapsto\sqrt{\tfrac23}\,|00\rangle|0\rangle+\sqrt{\tfrac16}\,\big(|01\rangle+|10\rangle\big)|1\rangle ,\qquad
|1\rangle\mapsto\sqrt{\tfrac23}\,|11\rangle|1\rangle+\sqrt{\tfrac16}\,\big(|01\rangle+|10\rangle\big)|0\rangle .
$$

This map is an isometry, so it is physically realizable. Each of the two output copies has fidelity $\langle\psi|\rho_{\text{copy}}|\psi\rangle=5/6$ for every input state; checked for 200 random states, all equal to $0.833333$. The value $5/6$ is known to be optimal for symmetric universal $1\to2$ qubit cloning. That optimality is quoted, not proved here.

## Consequences

- **States cannot be read out from one copy.** Determining $|\psi\rangle$ needs many prepared copies, and the statistical cost is the shot cost of [[concentration-inequalities-and-sampling]].
- **Teleportation destroys the original.** In [[quantum-teleportation]] Alice's qubit ends in a computational basis state, so the protocol moves the state rather than copying it.
- **Error correction cannot use repetition codes on unknown states.** Quantum codes instead spread a state's information across entangled qubits and measure only syndromes (planned chapter).
- **Security.** An eavesdropper cannot copy qubits in transit to measure later. This underlies quantum key distribution.
- **No faster-than-light signalling.** Perfect cloning combined with entanglement would allow signalling, which relativity forbids.

## Source

- Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010), Sec. 1.3.5, pp. 24–25, Eqs. (1.21)–(1.22) and Figure 1.11; Box 12.1, p. 532, Eqs. (12.1)–(12.5). Page numbers are those printed in the book.
- The Bužek–Hillery cloner is my addition: V. Bužek and M. Hillery, *Phys. Rev. A* **54**, 1844 (1996). The reference is from memory and marked to verify.

Checks are in `nielsen_chuang/part5_batch7.py` (section A).
