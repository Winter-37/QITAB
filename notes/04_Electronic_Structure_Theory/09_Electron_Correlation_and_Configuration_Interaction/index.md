What Hartree–Fock misses, and the most direct way to recover it.

## What this chapter is about

In Hartree–Fock each electron feels only the average charge cloud of the others, so the instantaneous avoidance of two electrons is missing. The energy this costs is the correlation energy. In a given one-electron basis it is defined as

$$
E_\text{corr}=E_\text{FCI}-E_\text{HF}.
$$

Configuration interaction (CI) recovers it in the most direct way: write the wave function as a linear combination of the Hartree–Fock determinant and its excitations, then diagonalize $\hat H$ in that space,

$$
|\Psi\rangle = c_0|\Phi_0\rangle+\sum_{ia}c_i^a|\Phi_i^a\rangle+\sum_{i<j,\,a<b}c_{ij}^{ab}|\Phi_{ij}^{ab}\rangle+\cdots .
$$

Keeping every excitation (full CI) gives the exact answer in the basis. Truncating at doubles (CISD) is affordable but has a structural defect. The chapter treats both, together with the physics of correlation (the Coulomb hole and the cusp) and the algorithms that make large CI calculations possible.

## Why it matters

- **It names the problem the rest of Part 4 solves.** Correlation energies are small compared with total energies, but they are about the size of bond energies, barriers and excitation energies. Every method after Hartree–Fock is a way of approximating them.
- **Two kinds of correlation.** *Dynamic* correlation is the short-range avoidance of electrons; it needs many small contributions from high excitations. *Static* (nondynamic) correlation appears when several determinants are nearly degenerate, as in stretched bonds; it needs a few large coefficients. Different methods are good at different kinds, so this distinction guides every method choice.
- **Full CI is the benchmark.** It is exact in its basis and is the reference against which approximate methods are tested. It is also what SQD and other quantum algorithms approximate, by sampling or by preparing the important part of the full-CI space.
- **Size consistency.** Truncated CI does not give twice the energy for two noninteracting molecules. This one failure motivated perturbation theory and coupled cluster (Chapters 10–11).
- **Slow basis convergence.** Orbital expansions cannot reproduce the cusp in $\Psi$ at $r_{12}=0$, so correlation energies converge slowly with basis size. This sets the cost of high accuracy.

## Where it is used later

- [[mp2|Perturbation theory]] (Chapter 10) and [[coupled-cluster-doubles|coupled cluster]] (Chapter 11), which repair size extensivity.
- [[mcscf-and-gvb|MCSCF]] (Chapter 13), which treats static correlation.
- [[sample-based-quantum-diagonalization|SQD]] and [[dmet-with-quantum-solvers|quantum solvers in DMET]], which approximate full CI.
- [[ci-analytic-gradient|CI gradients]] and [[selected-ci-analytic-gradient|selected-CI gradients]] (Chapter 15).

## The main ideas, in order

1. **Correlation.** Definition, static versus dynamic, analysed on minimal-basis H₂.
2. **Full CI.** Block structure of the Hamiltonian matrix and intermediate normalization. Only doubles couple directly to the energy, $E_\text{corr}=\sum_{i<j,\,a<b}\langle\Phi_0|\hat H|\Phi_{ij}^{ab}\rangle c_{ij}^{ab}$.
3. **Natural orbitals.** They make CI expansions more compact, and their occupations diagnose correlation.
4. **Truncated CI.** CISD, its lack of size consistency, and the Davidson correction.
5. **The cusp.** The Coulomb hole, cusp conditions, and why partial-wave expansions converge slowly.
6. **Algorithms.** Alpha and beta strings, direct CI, and Davidson and Newton solvers.

## How to read it

**Path.**

1. Electron correlation, static versus dynamic, analysed for H$_2$.
2. Full CI, the exact answer in a basis, and natural orbitals as its diagnostic.
3. Truncated CI (CISD), and its central flaw: size consistency and extensivity.
4. The electron-electron cusp and why correlation energies converge slowly.
5. How CI is done in practice: determinant strings, direct CI, Davidson and Newton methods.

**Leads to.** Chapters 10 and 11 cure size extensivity; Chapter 13 handles static correlation.

**Core (first pass).** [[electron-correlation]], [[h2-minimal-basis-correlation-analysis]], [[full-ci]], [[natural-orbitals]], [[cisd]], [[size-consistency]], [[ci-in-practice]].

**Deep (second pass).** [[ci-size-extensivity-and-excitation-levels]], [[coulomb-cusp-and-helium-expansions]], [[determinant-strings-and-direct-ci]], [[ci-optimization-newton-and-davidson]].

**Checkpoint.** Show that CID for two noninteracting H₂ molecules is not twice the monomer value.

**Planned sections:** CIS; Selected CI.
