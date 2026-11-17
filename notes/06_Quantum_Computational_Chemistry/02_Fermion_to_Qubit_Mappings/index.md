How fermionic operators become qubit operators, why a measured qubit register is a Slater determinant, and how symmetries remove qubits.

## What this chapter is about

Qubits are distinguishable two-level systems, and operators on different qubits commute. Electrons are fermions, and their creation and annihilation operators anticommute. A fermion-to-qubit mapping must reproduce the anticommutation relations with qubit operators. The Jordan–Wigner mapping does this with one qubit per spin orbital ($|1\rangle$ occupied, $|0\rangle$ empty). The fermionic sign is carried by a string of $Z$ operators on all lower-numbered qubits:

$$
a_j \;\mapsto\; \Big(\prod_{k<j} Z_k\Big)\,\sigma_j^{-}.
$$

Applied to the Hamiltonian of Chapter 1, this gives a weighted sum of Pauli strings, $\hat H=\sum_k c_k P_k$, which a quantum computer can measure term by term or exponentiate.

The chapter then generalizes in two directions:

- **Other encodings.** The qubits can store parities or Fenwick-tree partial sums of the occupations instead of the occupations themselves. These are the parity and Bravyi–Kitaev encodings, and every such encoding is a Clifford rotation of Jordan–Wigner.
- **Fewer qubits.** Symmetries of the Hamiltonian ($N_\alpha$ and $N_\beta$ parities, point-group operations) can be used to remove qubits exactly.

## Why it matters

- **It is the input to every algorithm in this part.** VQE measures the Pauli strings. Phase estimation exponentiates them. SQD reads out computational basis states.
- **Bit strings are determinants.** Under Jordan–Wigner a computational basis state is an occupation-number vector, that is, a Slater determinant. Measuring a qubit register therefore samples determinants with probability $|c_I|^2$. This is the idea SQD is built on. Other encodings need a cheap classical decoding step, $\mathbf n=B^{-1}\mathbf b$.
- **The choice of encoding changes locality and nothing else.** Because the encodings are Clifford rotations of one another, they share the term count, the 1-norm $\lambda$ and the spectrum. Only the Pauli weights differ: $O(M)$ for Jordan–Wigner and parity, $O(\log M)$ for Bravyi–Kitaev.
- **Tapering is free accuracy-wise.** Removing a qubit with a $\mathbb Z_2$ symmetry is exact, and saves 3–5 qubits for small molecules. It requires symmetry-adapted orbitals.

## Where it is used later

- [[variational-quantum-eigensolver|VQE]] (Chapter 3), which measures the Pauli strings, often on a tapered register.
- [[qpe-for-molecular-energies|Phase estimation]] (Chapter 4), where Pauli weights set the cost of each Trotter exponential.
- [[sample-based-quantum-diagonalization|SQD]] (Chapter 5), which relies on bit strings being determinants.

## The main ideas, in order

1. **Jordan–Wigner.** Occupations in qubits, signs in $Z$ strings; the Pauli Hamiltonian; determinants as bit strings.
2. **Parity and Bravyi–Kitaev.** Encodings as binary matrices $B$; update, parity and remainder sets; weights; the Clifford equivalence.
3. **Qubit tapering.** $\mathbb Z_2$ symmetries from a GF(2) kernel; the Clifford $U=(X_q+\tau)/\sqrt2$; choosing the sector; the parity-mapping two-qubit reduction.

## How to read it

**Path.** [[jordan-wigner-mapping]], then [[parity-and-bravyi-kitaev-mappings]], then [[qubit-tapering]].

**Needs.**
- Chapter 1 ([[molecular-hamiltonian-in-the-mo-basis]]).
- Part 4, Chapter 5 (second quantization).
- For tapering: point-group characters ([[groups-representations-and-characters]]).

**Leads to.** Chapter 3 (energies from Pauli measurements), Chapter 4 (Trotter circuits) and Chapter 5 (sampling determinants).

**Checkpoint.**
1. Show that $Z_0\sigma^-_1$ and $\sigma^+_0$ anticommute.
2. Write the Bravyi–Kitaev $a_5$ for $M=8$ from its update, parity and remainder sets.
3. Taper H₂/STO-3G to one qubit and recover the FCI energy from the $2\times2$ Hamiltonian.

**Planned sections:** Ternary-tree and superfast encodings; Fermionic swap networks and qubit connectivity.
