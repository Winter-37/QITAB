Groups and their representations: the mathematics of symmetry labels, degeneracies, selection rules, permutation symmetry and spin, and the continuous groups behind orbital rotations.

## What this chapter is about

A symmetry of a Hamiltonian is an operation that leaves it unchanged, such as a rotation, a reflection, a permutation or a Pauli operator. The symmetry operations form a group. Representation theory then answers three questions:

- in how many essentially different ways the group can act on a vector space (the irreducible representations);
- how to recognize them (by their characters);
- how to break a given space into them.

Most of the chapter treats finite groups: point groups and the symmetric group of particle permutations. The last section introduces Lie groups and algebras in general and the unitary group of orbital rotations. The rotation groups SU(2) and SO(3) themselves, with angular momentum, are in Part 2, Chapter 6.

## Why it matters

- **Labels and degeneracies.** If $[\hat H,\hat g]=0$ for every $g$ in a group, the eigenstates of $\hat H$ can be labelled by irreducible representations. Each level has the dimension of its irreducible representation, unless there is an accidental degeneracy.
- **Selection rules.** A matrix element $\langle a|\hat O|b\rangle$ vanishes unless the product of the three symmetry labels contains the totally symmetric representation. This one rule explains parity rules, dipole selection rules and why many integrals are zero.
- **Cheaper calculations.** In a symmetry-adapted basis the Hamiltonian is block-diagonal, one block per irreducible representation. Electronic-structure codes use point-group symmetry for this reason.
- **Spin and permutations.** Permutations of electrons and changes of orbital basis commute. As a result, spin states are labelled by Young diagrams, and the number of CSFs for any active space follows from one formula.
- **Orbital rotations.** The one-body excitation operators generate the unitary group. This is why exp(−κ̂) rotates orbitals, why one-body unitaries compile into Givens rotations, and why they never mix spin states.
- **Quantum information.** The Pauli group underlies stabilizer codes and Clifford circuits.

## Where it is used later

- [[symmetry-conservation-and-degeneracy|Symmetry and degeneracy]] and [[parity-and-parity-selection-rules|parity selection rules]] (Part 2, Chapter 6).
- [[rotational-selection-rules-and-wigner-eckart|The Wigner–Eckart theorem]], the continuous-group version of the same idea.
- [[hf-solution-classification|The classification of Hartree–Fock solutions]] by the symmetries they keep (Part 4, Chapter 3).
- [[molecular-orbitals-of-polyatomic-molecules|Symmetry orbitals]] (Part 3) and [[qubit-tapering|qubit tapering]] (Part 6).
- [[genealogical-coupling|Genealogical coupling]] and CSF counting (Part 4, Chapter 5); [[orbital-rotations|orbital rotations]] (Part 4, Chapter 7).
- The Pauli group, used in Part 5.

## The main ideas, in order

1. **Groups.** The axioms, subgroups, Lagrange's theorem, cosets and conjugacy classes.
2. **Representations.** Equivalence of representations and irreducibility.
3. **Schur's lemma and the orthogonality theorem.** Together they show that the matrix elements of different irreducible representations are orthogonal.
4. **Characters.** Characters are constant on conjugacy classes and obey orthogonality relations. As a consequence $\sum_i d_i^2=|G|$, and a reducible representation contains the $i$th irreducible representation $n_i=|G|^{-1}\sum_g\chi_i(g)^*\chi(g)$ times.
5. **Examples.** $S_3\cong C_{3v}$ (a molecular point group) and the one-qubit Pauli group.
6. **Projection operators.** Transfer operators multiply like matrix units. Character projectors split any space by irrep, and partner functions follow. A symmetric Hamiltonian is block-diagonal in the result.
7. **Direct products.** Product functions transform as $\Gamma\otimes\Gamma'$. An integral survives only if its integrand contains the totally symmetric irrep, which is the general selection rule. Symmetric and antisymmetric squares give the terms of degenerate configurations.
8. **The symmetric group.** Classes are cycle types and irreps are Young diagrams, with dimensions from the hook-length formula. Schur–Weyl duality links $S_N$ with $U(n)$. Spin states and CSF counts follow.
9. **Lie groups and algebras.** Generators, structure constants, the exponential map and its limits, Casimir operators. The $E_{pq}$ as generators of $U(n)$.

## How to read it

**Path.** [[groups-representations-and-characters]], [[projection-operators-and-symmetry-adapted-functions]], [[direct-products-and-selection-rules]], [[symmetric-group-and-young-diagrams]], [[lie-groups-and-lie-algebras]]. The last two can be read after the first alone.

**Needs.** Chapter 1 (matrices, the spectral theorem, matrix exponentials and the Baker–Campbell–Hausdorff formula), Chapter 10 (tensor products), and the molecular point groups of Part 3, Chapter 2 for the examples. The Lie-group section uses the rotation groups of Part 2, Chapter 6.

**Leads to.** Symmetry and degeneracy in Part 2, Chapter 6; molecular symmetry and spectroscopic selection rules in Parts 3 and 4; spin adaptation and CSFs in Part 4, Chapter 5; orbital rotations in Part 4, Chapter 7; the Pauli and Clifford groups in Part 5.

**Planned sections:** Space groups and Bloch's theorem; Double groups and spin–orbit coupling.
