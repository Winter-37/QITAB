How fermionic operators become qubit operators, and why a measured qubit register is a Slater determinant.

## What this chapter is about

Qubits are distinguishable two-level systems, and operators on different qubits commute. Electrons are fermions, and their creation and annihilation operators anticommute. A fermion-to-qubit mapping must reproduce the anticommutation relations with qubit operators. The Jordan–Wigner mapping does this with one qubit per spin orbital ($|1\rangle$ occupied, $|0\rangle$ empty). The fermionic sign is carried by a string of $Z$ operators on all lower-numbered qubits:

$$
a_j \;\mapsto\; \Big(\prod_{k<j} Z_k\Big)\,\sigma_j^{-}.
$$

Applied to the Hamiltonian of Part 4, Chapter 5, this gives a weighted sum of Pauli strings, $\hat H=\sum_k c_k P_k$, which a quantum computer can measure term by term.

## Why it matters

- **It is the input to every algorithm in this part.** VQE measures the Pauli strings. Phase estimation exponentiates them. SQD reads out computational basis states.
- **Bit strings are determinants.** Under Jordan–Wigner a computational basis state is an occupation-number vector, that is, a Slater determinant. Measuring a qubit register therefore samples determinants with probability $|c_I|^2$. This is the idea SQD is built on.
- **The cost of a mapping is locality.** A Jordan–Wigner string can be as long as the number of qubits, which affects circuit depth. Bravyi–Kitaev and parity mappings trade string length for other structure, and qubit tapering removes qubits using symmetries such as particle-number parity.

## Where it is used later

- [[variational-quantum-eigensolver|VQE]] (Chapter 3).
- [[sample-based-quantum-diagonalization|SQD]] (Chapter 5).

## How to read it

**Path.** The Jordan-Wigner mapping, its Pauli-string Hamiltonian, and the determinant-bitstring correspondence.

**Needs.** Part 4, Chapter 5.

**Leads to.** Chapter 3 (energies from Pauli measurements) and Chapter 5 (sampling determinants).

**Core (first pass).** [[jordan-wigner-mapping]].

**Checkpoint.** Show that $Z_0\sigma^-_1$ and $\sigma^+_0$ anticommute. Count the Pauli strings of the H$_2$/STO-3G Hamiltonian and explain why only four are off-diagonal.

**Planned sections:** Bravyi-Kitaev; Parity mapping and qubit tapering.
