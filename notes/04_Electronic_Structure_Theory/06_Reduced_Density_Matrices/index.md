One- and two-particle density matrices: everything an energy or a one- or two-electron property needs from a wave function.

## What this chapter is about

The exact wave function depends on $3N$ spatial and $N$ spin coordinates, but the Hamiltonian contains only one- and two-electron operators. Every expectation value therefore needs only two much smaller objects:

- the **one-particle reduced density matrix** (1-RDM), $D_{pq}=\langle\Psi|a_p^\dagger a_q|\Psi\rangle$;
- the **two-particle reduced density matrix** (2-RDM), $d_{pqrs}=\langle\Psi|a_p^\dagger a_r^\dagger a_s a_q|\Psi\rangle$.

They are obtained by integrating out all but one or two electrons. The energy is then exactly

$$
E=\sum_{pq}h_{pq}D_{pq}+\tfrac12\sum_{pqrs}g_{pqrs}\,d_{pqrs}.
$$

This chapter defines them in coordinate space and in second quantization, and lists their basic properties: Hermiticity, trace, positivity and occupation-number bounds.

## Why it matters

- **They are what methods actually compute.** Energies, dipole moments, spin densities, populations and forces all come from contracting integrals with RDMs. A wave-function method can be judged by the RDMs it produces.
- **Natural orbitals and occupations.** Diagonalizing the 1-RDM gives natural orbitals and occupations between 0 and 1 (spin orbitals). Occupations far from 0 or 1 are the standard diagnostic of strong (static) correlation and guide active-space selection.
- **Gradients need relaxed densities.** For non-variational methods the effective densities that enter analytic gradients include orbital-response contributions (Chapter 15).
- **Embedding and quantum algorithms work with RDMs.** DMET matches fragment and mean-field 1-RDMs. On a quantum computer one measures RDM elements rather than the wave function, and SQD and VQE energies are assembled from them.

## Where it is used later

- [[natural-orbitals|Natural orbitals]] (Chapter 9).
- [[generalized-fock-matrix-and-orbital-hessian|The generalized Fock matrix]] (Chapter 7), built from the 1- and 2-RDM.
- [[z-vector-method|Relaxed densities and the Z-vector method]] (Chapter 15).
- [[dmet-self-consistency-and-correlation-potential|DMET self-consistency]] (Chapter 19), which fits 1-RDMs.

## The main ideas, in order

1. **The 1-RDM.** Its definition by integrating out $N-1$ electrons, its matrix in a spin-orbital basis, and its properties (Hermitian, trace $N$, eigenvalues in $[0,1]$).
2. **Second quantization.** $D_{pq}$ and $d_{pqrs}$ as expectation values of operator strings, with occupation and pair-occupation interpretations and the energy formula above.

## How to read it

**Path.** [[one-particle-rdm]], then [[density-matrices-second-quantization]].

**Needs.** Chapter 2 (determinants), and Chapter 5 for the second note. Reduced density matrices are partial traces: Part 0, Chapter 10 ([[tensor-products-and-partial-trace|tensor products and partial trace]]) and the density operators of Part 2, Chapter 3.

**Leads to.** The generalized Fock matrix (Chapter 7), natural orbitals (Chapter 9), relaxed densities (Chapter 15) and DMET (Chapter 19).

**Reading.** Second-pass chapter, needed by the deep notes of Chapters 7, 13 and 15.

**Planned sections:** Spin-resolved and transition RDMs; Cumulants; N-representability.
