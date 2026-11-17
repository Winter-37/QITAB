The mean-field approximation, derived and solved.

## What this chapter is about

The electronic Schrödinger equation of Chapter 1 cannot be solved exactly beyond a few electrons, because the repulsion $1/r_{ij}$ couples every electron to every other one. Hartree–Fock theory gives up on the exact wave function and asks a smaller question: *which single Slater determinant has the lowest energy?* The answer is a set of orbitals in which each electron moves in the averaged electrostatic field of all the others, plus a nonlocal exchange term that comes from antisymmetry alone. The orbitals obey an effective one-electron eigenvalue equation,

$$
\hat f\,\chi_a = \varepsilon_a\,\chi_a ,
$$

but the Fock operator $\hat f$ is built from the occupied orbitals themselves. The equation is therefore nonlinear and is solved by iteration until the orbitals reproduce the field that produced them. This is the self-consistent field (SCF).

## Why it matters

- **It is the reference for nearly every other method.** CI, Møller–Plesset theory and coupled cluster expand around the Hartree–Fock determinant and are written in its orbitals. The correlation energy is *defined* relative to it: in a given basis, $E_\text{corr} = E_\text{FCI} - E_\text{HF}$ ([[electron-correlation|electron correlation]]).
- **It is accurate in the wrong currency.** Near equilibrium, Hartree–Fock recovers most of the total energy, typically over 99 % for small molecules. The part it misses, though, is about as large as bond energies and reaction barriers. Chapter 14 measures where this matters ([[hjo-calibration-energies-atomization-reactions-barriers|energies]], [[hjo-calibration-structures-and-dipoles|structures and dipoles]]).
- **It supplies the vocabulary of chemistry.** Orbitals, orbital energies, occupied and virtual spaces, HOMO and LUMO, Koopmans ionization energies and atomic charges are all defined here.
- **Its failures are instructive.** Stretching H$_2$ forces a choice. Keeping spin symmetry (RHF) gives the wrong dissociation limit. Breaking it (UHF) gives the right energy with a spin-contaminated wave function. This dilemma is the clearest motivation for the multiconfigurational methods of Chapter 13.

## Where it is used later

- **Correlated methods.** The Hartree–Fock orbitals and orbital energies define the molecular-orbital basis of Chapters 9–12 ([[mp2|MP2]], [[cisd|CISD]], [[coupled-cluster-doubles|CCD]]). They also define the basis of the qubit Hamiltonians in Part 6 ([[jordan-wigner-mapping|Jordan–Wigner]], [[variational-quantum-eigensolver|VQE]], [[sample-based-quantum-diagonalization|SQD]]).
- **Embedding.** In DMET (Chapter 19), a mean-field calculation on the whole molecule gives the one-particle density matrix. Its Schmidt decomposition defines the bath orbitals ([[schmidt-decomposition-and-dmet-bath|DMET bath]]).
- **Gradients.** The analytic gradient chapter starts from the [[rhf-analytic-gradient|RHF gradient]] and the [[cphf-closed-shell|coupled-perturbed Hartree–Fock equations]].
- **Optimization.** Chapter 7 recasts Hartree–Fock as minimization over orbital rotations. That view explains convergence ([[scf-convergence-diis-and-newton|DIIS and Newton]]) and multiple solutions ([[rhf-instabilities-and-multiple-solutions|instabilities]]).
- **Density functional theory.** The Kohn–Sham equations of the planned Chapter 8 have the same matrix structure, with exchange partly or wholly replaced by an exchange–correlation potential ([[kohn-sham-dft|Kohn–Sham DFT]]).

## The main ideas, in order

1. **Variational principle in a restricted space.** Minimize $\langle\Phi|\hat H|\Phi\rangle$ over the spin orbitals of one determinant, keeping them orthonormal. The stationarity condition is the Hartree–Fock equation. A unitary rotation among the occupied orbitals leaves the determinant unchanged, so the matrix of Lagrange multipliers can be diagonalized; this gives the canonical orbitals.
2. **Coulomb and exchange.** The Coulomb operator $\hat J_b$ is local and acts like a classical charge cloud. The exchange operator $\hat K_b$ is nonlocal and acts only between electrons of parallel spin. For $b=a$, the two cancel exactly, so there is no self-interaction.
3. **Why it serves as a reference.** By Brillouin's theorem, singly excited determinants do not couple directly to the Hartree–Fock state. Koopmans' theorem makes $-\varepsilon_a$ a frozen-orbital ionization energy.
4. **From functions to matrices.** Expanding the orbitals in $K$ basis functions turns the integro-differential equations into $\mathbf{FC}=\mathbf{SC}\boldsymbol\varepsilon$ (Roothaan–Hall). Orthogonalizing the basis makes this an ordinary eigenvalue problem, and iteration converges it.
5. **Constraints define the variants.** RHF uses the same spatial orbitals for both spins. UHF uses separate ones, and GHF uses two-component spinors. Each larger space contains the smaller one, so its global minimum is lower or equal. The price is the loss of symmetries the exact state has.

## How to read it

**Path.**

1. The Fock operator, the Hartree–Fock equations from constrained minimization, and two consequences: Brillouin's theorem and Koopmans' theorem.
2. Restricted Hartree–Fock in a basis (the Roothaan equations), orthogonalization of the basis, and the SCF procedure, worked through for HeH$^+$.
3. Population analysis.
4. Unrestricted Hartree–Fock and the H$_2$ dissociation problem, which motivates everything in Chapters 9–13.
5. Generalized Hartree–Fock, and the classification of Hartree–Fock solutions by the symmetries they keep.

**Needs.** Chapter 1 (the molecular Hamiltonian, atomic units). Chapter 2 (Slater determinants and the Slater–Condon rules). The variational principle (Part 2, Chapter 7).

**Leads to.** Chapter 4 (basis sets), Chapter 7 (Hartree–Fock as an optimization problem), and every correlated method from Chapter 9 on.

**Core (first pass).** [[fock-operator]], [[hartree-fock-equations]], [[brillouin-theorem]], [[koopmans-theorem]], [[rhf]], [[basis-orthogonalization]], [[scf-procedure]], [[heh-plus-minimal-basis-model]], [[population-analysis]], [[uhf]], [[h2-dissociation-rhf-uhf]].

**Deep (second pass).** [[ghf]], [[hf-solution-classification]].

**Checkpoint.** Run the HeH⁺ SCF by hand for two iterations. Then explain why RHF H₂ dissociates to the wrong limit.

**Planned sections:** Restricted open-shell Hartree–Fock (ROHF); maximum-overlap method for excited-state SCF; initial guesses.
