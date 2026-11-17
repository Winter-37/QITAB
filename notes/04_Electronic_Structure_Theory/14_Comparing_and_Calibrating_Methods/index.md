A review chapter: every method of Chapters 3–13 side by side, and how accurate each actually is.

## What this chapter is about

By this point there are many methods: HF, MP2, MP3, CISD, CCSD, CCSD(T), MCSCF, CASPT2 and others. Each comes with an ansatz, an energy expression, a cost and a set of formal properties. This chapter compares them in two ways:

- **Against full CI in a fixed basis.** H₂ and water, at equilibrium and when stretched, isolate the error of the method from the error of the basis.
- **Against experiment.** HJO's calibration on 20 small molecules covers bond lengths, dipole moments, atomization energies, reaction enthalpies and barriers, across basis sets of increasing size. Here method and basis errors combine.

The chapter also shows what every many-electron method does with a Hamiltonian that has no two-electron part. It ends with basis-set superposition error, the most common basis artifact in weakly bound complexes.

## Why it matters

- **Formal properties are not accuracy.** Variationality, size extensivity, orbital invariance and scaling are listed for each method. The calibration shows how much each property matters in practice and when a cheaper method is good enough.
- **Errors can cancel.** Better correlation lengthens bonds, while a bigger basis shortens them. CISD and MP3 bond lengths therefore look good in cc-pVDZ only by cancellation, and get worse in larger bases. Distinguishing the apparent error from the intrinsic error (at the basis-set limit) is the main lesson of the calibration.
- **Method choice is the practical question.** A table of methods with their cost and typical errors is what one consults before starting a calculation.
- **Reference numbers for testing new methods.** The H₂ and water full-CI curves are standard tests for any approximate solver, including the embedding and quantum methods of Chapter 19 and Part 6.

## Where it is used later

- [[dmet-with-quantum-solvers|DMET with quantum solvers]] (Part 6), whose accuracy is judged against references of this kind.
- [[geometry-error-of-an-approximate-surface|Geometry error of an approximate surface]] (Chapter 16), which explains the structure errors seen here.

## How to read it

**Path.**

1. All methods side by side in one notation, then every model applied to H$_2$ and water against full CI.
2. Many-electron methods on one-particle Hamiltonians.
3. HJO's calibration of structures, dipoles, atomization energies and barriers.
4. Basis-set superposition error.

Read it after Chapters 3-13.

**Core (first pass).** [[electronic-structure-methods-at-a-glance]], [[standard-models-h2-and-water]].

**Deep (second pass).** [[one-particle-hamiltonian-models]], [[hjo-calibration-structures-and-dipoles]], [[hjo-calibration-energies-atomization-reactions-barriers]], [[basis-set-superposition-error]].

**Checkpoint.** Predict, before looking, the ordering of HF, MP2, CCSD and CCSD(T) bond lengths against experiment in a triple-zeta basis. Then check the calibration note.

**Planned sections:** Gradient and vibrational benchmarks; Convergence and error analysis.
