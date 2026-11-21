What electronic-structure theory sets out to solve, and the approximation that makes it a well-defined problem.

## What this chapter is about

A molecule is a set of electrons and nuclei interacting through Coulomb forces. Its nonrelativistic Hamiltonian has five terms: kinetic energies of electrons and of nuclei, electron–nuclear attraction, electron–electron repulsion, and nuclear–nuclear repulsion. Nuclei are thousands of times heavier than electrons, so the Born–Oppenheimer approximation solves for the electrons with the nuclei clamped at positions $\mathbf R$:

$$
\hat H_\text{el}(\mathbf R)\,\Psi_\text{el}(\mathbf r;\mathbf R) = E_\text{el}(\mathbf R)\,\Psi_\text{el}(\mathbf r;\mathbf R),
\qquad
\hat H_\text{el} = \sum_i \hat h(i) + \sum_{i<j}\frac{1}{r_{ij}} .
$$

$E_\text{el}(\mathbf R)$ plus the nuclear repulsion is the potential energy surface on which the nuclei move. Every method in Part 4 is an approximate way of solving this equation, or of extracting properties from its solution.

## Why it matters

- **It defines the target.** Hartree–Fock, CI, coupled cluster, DFT, DMET and the quantum algorithms of Part 6 all approximate the same $\hat H_\text{el}$. Knowing its exact form (one-electron part, two-electron part, no spin dependence) explains what every method has to compute: one- and two-electron integrals.
- **Potential energy surfaces are chemistry.** Equilibrium structures, vibrational frequencies, reaction barriers and dissociation energies are all features of $E(\mathbf R)$. Geometry optimization and ab initio molecular dynamics need its gradient.
- **The approximation has limits.** Near degeneracies and conical intersections, electronic and nuclear motion couple. Nonadiabatic effects then matter, as in photochemistry.
- **Forces from expectation values.** The Hellmann–Feynman theorem expresses $dE/d\mathbf R$ as an expectation value for exact and fully variational wave functions. Atom-centred basis functions move with the nuclei, which adds Pulay terms. Both facts are the starting point of the analytic-gradient theory of Chapter 15.

## Where it is used later

- [[analytic-gradients-and-force-constants|Analytic gradients]] and [[geometry-optimization|geometry optimization]] (Chapters 15–16).
- [[dmet-analytic-nuclear-gradient|The DMET nuclear gradient]] (Chapter 19).
- Every chapter that writes $\hat H_\text{el}$ in a basis, starting with Chapter 2.

## The main ideas, in order

1. **Atomic units.** Setting $\hbar=m_e=e=4\pi\varepsilon_0=1$ makes the Bohr radius the unit of length and the hartree the unit of energy, and removes constants from every equation.
2. **The molecular Hamiltonian.** Its five terms, and the clamped-nucleus electronic Hamiltonian written as a sum of one- and two-electron operators.
3. **Born–Oppenheimer.** Separate electronic and nuclear motion, obtain the potential energy surface, and state where the separation fails.
4. **Hellmann–Feynman and virial theorems.** Both follow from stationarity of the energy, and they link energies to forces and to kinetic and potential energy.

## How to read it

**Path.** Atomic units first. Then the molecular Hamiltonian, and the Born-Oppenheimer separation that turns it into an electronic problem on a potential-energy surface. H₂⁺, the one molecule whose clamped-nuclei problem can be solved exactly, gives a first potential curve to test approximations against ([[hydrogen-molecule-ion-exact]]). The Hellmann-Feynman and virial theorems link energies to forces and properties; they return in Chapter 15.

**Needs.** Part 2, Chapters 5 and 7.

**Core (first pass).** [[atomic-units]], [[molecular-hamiltonian]], [[born-oppenheimer-approximation]].

**Deep (second pass).** [[hydrogen-molecule-ion-exact]], [[hellmann-feynman-and-virial-theorems]].
