Finite groups and their representations: the mathematics of symmetry labels, degeneracies and selection rules.

## What this chapter is about

A symmetry of a Hamiltonian is an operation that leaves it unchanged, such as a rotation, a reflection, a permutation or a Pauli operator. The symmetry operations form a group. Representation theory then answers three questions:

- in how many essentially different ways the group can act on a vector space (the irreducible representations);
- how to recognize them (by their characters);
- how to break a given space into them.

This chapter treats finite groups. The continuous rotation groups SU(2) and SO(3) are in Part 2, Chapter 6.

## Why it matters

- **Labels and degeneracies.** If $[\hat H,\hat g]=0$ for every $g$ in a group, the eigenstates of $\hat H$ can be labelled by irreducible representations. Each level has the dimension of its irreducible representation, unless there is an accidental degeneracy.
- **Selection rules.** A matrix element $\langle a|\hat O|b\rangle$ vanishes unless the product of the three symmetry labels contains the totally symmetric representation. This one rule explains parity rules, dipole selection rules and why many integrals are zero.
- **Cheaper calculations.** In a symmetry-adapted basis the Hamiltonian is block-diagonal, one block per irreducible representation. Electronic-structure codes use point-group symmetry for this reason.
- **Quantum information.** The Pauli group underlies stabilizer codes and Clifford circuits.

## Where it is used later

- [[symmetry-conservation-and-degeneracy|Symmetry and degeneracy]] and [[parity-and-parity-selection-rules|parity selection rules]] (Part 2, Chapter 6).
- [[rotational-selection-rules-and-wigner-eckart|The Wigner–Eckart theorem]], the continuous-group version of the same idea.
- [[hf-solution-classification|The classification of Hartree–Fock solutions]] by the symmetries they keep (Part 4, Chapter 3).
- The Pauli group, used in Part 5.

## The main ideas, in order

1. **Groups.** The axioms, subgroups, Lagrange's theorem, cosets and conjugacy classes.
2. **Representations.** Equivalence of representations and irreducibility.
3. **Schur's lemma and the orthogonality theorem.** Together they show that the matrix elements of different irreducible representations are orthogonal.
4. **Characters.** Characters are constant on conjugacy classes and obey orthogonality relations. As a consequence $\sum_i d_i^2=|G|$, and a reducible representation contains the $i$th irreducible representation $n_i=|G|^{-1}\sum_g\chi_i(g)^*\chi(g)$ times.
5. **Examples.** $S_3\cong C_{3v}$ (a molecular point group) and the one-qubit Pauli group.

## How to read it

**Path.** [[groups-representations-and-characters]].

**Needs.** Chapter 1 (matrices, the spectral theorem).

**Leads to.** Symmetry and degeneracy in Part 2, Chapter 6; molecular symmetry in Parts 3 and 4; the Pauli and Clifford groups in Part 5.

**Planned sections:** Point groups and character tables; Projection operators and symmetry-adapted orbitals; Direct products and selection rules.
