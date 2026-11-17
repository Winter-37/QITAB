From a Hartree–Fock calculation to the second-quantized Hamiltonian that a quantum computer acts on: integral transformation, spin orbitals, conventions, and the active-space reduction that makes problems fit on a device.

## What this chapter is about

Every quantum algorithm for chemistry takes the same input:

$$
\hat H=E_0+\sum_{pq}h_{pq}a_p^\dagger a_q+\tfrac12\sum_{pqrs}(pq|rs)\,a_p^\dagger a_r^\dagger a_sa_q
$$

in a finite set of orthonormal orbitals. This chapter builds that input:

- transform the AO integrals of an SCF calculation to molecular orbitals;
- expand spatial orbitals into spin orbitals in a fixed order;
- keep track of the notation and the constant term;
- reduce the problem to an active space by freezing core orbitals and discarding high virtuals.

The result is handed to a fermion-to-qubit mapping (Chapter 2) and then to VQE, phase estimation or SQD (Chapters 3–5).

## Why it matters

- **Convention errors are silent.** A mismatched integral ordering, a missing ½, or a dropped nuclear-repulsion constant gives a Hamiltonian that is wrong but still Hermitian. The HF-energy and FCI-energy checks catch almost all of these.
- **The orbital basis shapes the cost.** The spectrum does not depend on which orbitals are used, but the number of Pauli terms, the 1-norm $\lambda$ (which sets the QPE cost) and the overlap of simple input states all do.
- **Active spaces decide what is computed.** A quantum calculation in an active space returns a CASCI-quality energy. Freezing cores is nearly free in energy and saves qubits and a large part of $\lambda$. Small valence spaces lose dynamic correlation, which must be recovered by other means.

## Where it is used later

- [[jordan-wigner-mapping|The Jordan–Wigner mapping]] (Chapter 2), which takes this Hamiltonian as input.
- [[qpe-for-molecular-energies|Phase estimation]] and [[qpe-cost-and-resource-estimates|its cost]] (Chapter 4), where $\lambda$ and the active-space size set the resources.
- [[sample-based-quantum-diagonalization|SQD]] and [[dmet-with-quantum-solvers|embedding]] (Chapters 5 and 7), whose embedding Hamiltonian has the active-space form.

## The main ideas, in order

1. **MO-basis Hamiltonian.** Quarter transformations ($O(n^5)$); 8-fold permutational symmetry; chemists', physicists' and antisymmetrized notation; interleaved spin orbitals; the HF and FCI checks. Orbital rotations leave the spectrum unchanged but change the qubit Hamiltonian.
2. **Frozen core and active space.** The core energy and core Fock operator; CASCI equivalence; the energy and $\lambda$ trade-offs.

## How to read it

**Path.** [[molecular-hamiltonian-in-the-mo-basis]], then [[frozen-core-and-active-space-hamiltonians]].

**Needs.**
- Part 4, Chapters 2–3 and 5: [[integral-notation]], [[rhf]], [[second-quantized-operators]].
- For the active-space note: Part 4, Chapter 13 ([[mcscf-and-gvb]]).

**Leads to.** Chapter 2 (qubit mappings) and every algorithm chapter of this part.

**Checkpoint.** Rebuild the RHF energy of H₂O from MO integrals. Then derive $E_{\text{core}}$ and $h^{\text{eff}}_{tu}$ for one frozen doubly occupied orbital, and check them against a CASCI calculation.

**Planned sections:** Density fitting and Cholesky-factorized Hamiltonians; Orbital choice for low 1-norm; Symmetry sectors and the electron-number constraint.
