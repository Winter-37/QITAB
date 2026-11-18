---
id: reading-order-quantum-mechanics
title: Reading order - quantum mechanics, from the wave function to scattering and dynamics
summary: A staged path through Part 2 (Griffiths with Sakurai companions), with a core list for a first pass, deep notes for a second, the mathematics each stage needs, and a checkpoint per stage. Ends with what to read next in Parts 3, 4 and 5.
status: in-progress
kind: reference
level: introductory
tags: [reading-guide, study-plan, quantum-mechanics, curriculum, overview]
prerequisites: []
related: [reading-order-electronic-structure, reading-order-quantum-computing, operator-and-matrix-notation, angular-momentum-phase-conventions]
order: 20
date: 2026-11-17
---

## How to use this guide

**Relation to the chapters.** Part 2 is ordered like Griffiths, so Previous/Next already walks it front to back. This guide adds three things: a **core/deep** split (deep notes are mostly the Sakurai companions and the advanced-level notes), the **mathematics** to read first at each stage, and a slightly different order for the middle of the part (approximation methods before symmetry), which suits a chemist.

**Route.** Read the core lists of stages 1-7 in order. Return for the deep lists when a later note asks for them.

**Conventions.** Part 2 keeps $\hbar$ explicit. Spherical harmonics and Clebsch–Gordan coefficients follow Condon–Shortley ([[angular-momentum-phase-conventions]]).

## Stage 1 - The wave function and one-dimensional problems

**Mathematics first.** [[fourier-transforms-and-the-dirac-delta]], [[probability-and-random-variables]].

**Core.**

1. [[wave-function-and-statistical-interpretation]] and [[normalization-and-probability-current]] - what $\Psi$ means and why its norm is conserved.
2. [[momentum-operator-and-ehrenfest-theorem]] and [[de-broglie-and-heisenberg-uncertainty]] - operators as derivatives, and the classical limit of expectation values.
3. [[stationary-states]] - separation of time; everything after this is an eigenvalue problem.
4. [[infinite-square-well]], [[harmonic-oscillator-ladder-operators]], [[harmonic-oscillator-analytic-solution]] - the two exactly solvable bound problems. The ladder method returns in angular momentum and second quantization.
5. [[free-particle-and-wave-packets]], [[delta-function-potential]], [[finite-square-well]] - continuum states, bound states in a well, and tunnelling.

**Deep.** [[one-dimensional-scattering-and-transfer-matrix]].

**Checkpoint.** Derive the harmonic-oscillator spectrum from $[\hat a,\hat a^\dagger] = 1$ alone. Find the number of bound states of a finite well from its strength parameter.

## Stage 2 - Formalism

**Mathematics first.** [[dirac-notation]], [[orthonormal-functions-and-operators]], [[matrix-eigenvalue-problem]], [[spectral-decomposition-and-normal-operators]].

**Core.**

1. [[hilbert-space-and-hermitian-operators]] and [[eigenfunctions-of-hermitian-operators]] - real eigenvalues, orthogonal eigenfunctions, completeness.
2. [[generalized-statistical-interpretation]] - measurement in any basis.
3. [[position-momentum-and-energy-representations]] - the same state in different bases.
4. [[generalized-uncertainty-principle]] - uncertainty from commutators.

**Deep.** [[energy-time-uncertainty-principle]], [[harmonic-oscillator-coherent-states]], [[density-operators-and-mixed-states]] (needed before reduced density matrices and before Part 5).

**Checkpoint.** Show that $\sigma_A\sigma_B\ge\tfrac12|\langle[\hat A,\hat B]\rangle|$, and that the oscillator coherent state saturates the position-momentum bound.

## Stage 3 - Three dimensions, angular momentum and spin

**Mathematics first.** [[classical-orthogonal-polynomials]], [[spherical-bessel-functions]].

**Core.**

1. [[schrodinger-equation-in-three-dimensions]] and [[central-potentials-and-spherical-harmonics]] - separation in spherical coordinates.
2. [[hydrogen-atom]] - the spectrum and orbitals every atomic basis set imitates.
3. [[orbital-angular-momentum]] and [[spin-one-half]] - angular momentum algebraically; spin as the first purely algebraic angular momentum.
4. [[addition-of-angular-momenta]] - Clebsch–Gordan coefficients, singlets and triplets.

**Deep.** [[minimal-coupling-and-aharonov-bohm]]; [[pauli-matrix-identities]] (reference).

**Checkpoint.** Build the singlet and triplet states of two spins from $\hat S_-$, and compare signs with the Clebsch–Gordan table.

## Stage 4 - Identical particles

**Core.**

1. [[two-particle-systems-and-reduced-mass]] - separating the centre of mass.
2. [[bosons-fermions-and-exchange-forces]] and [[exchange-symmetry-spin-and-symmetrization-principle]] - symmetrization, the exchange "force", and how spin and space share the antisymmetry.
3. [[helium-atom-independent-particle-model]] and [[periodic-table-and-term-symbols]] - many-electron atoms at the independent-particle level.

**Deep.** [[free-electron-gas]], [[band-structure-and-the-dirac-comb]] (solids).

**Checkpoint.** Explain why the triplet of excited helium lies below the singlet, in terms of the exchange integral.

## Stage 5 - Approximation methods

**Core.**

1. [[variational-principle]], [[variation-method]] and [[linear-variation-method]] - the upper bound, and why diagonalization in a basis is variational.
2. [[helium-ground-state-variational]] - the classic one-parameter calculation.
3. [[hydrogen-molecule-ion-variational]] and [[hydrogen-molecule-heitler-london]] - the first molecules (LCAO and valence bond).
4. [[rayleigh-schrodinger-perturbation-theory]] and [[degenerate-perturbation-theory]] - the perturbation series.
5. [[stark-effect]], [[hydrogen-fine-structure]], [[zeeman-effect]] - perturbation theory at work on hydrogen.
6. [[wkb-approximation]] and [[wkb-connection-formulas-and-quantization]] - the semiclassical limit.

**Deep.** [[upper-bounds-and-interlacing]], [[hyperfine-splitting-hydrogen]], [[greens-functions-single-particle]], [[wkb-tunneling-and-alpha-decay]].

**Checkpoint.** Reproduce the optimal effective charge and energy of the one-parameter helium wave function, and show that at effective charge $Z = 2$ the variational energy equals the first-order perturbation result.

## Stage 6 - Symmetry

**Mathematics first.** [[groups-representations-and-characters]], [[unitary-matrices-exponential-logarithm]].

**Core.**

1. [[translation-operator-and-translational-symmetry]] and [[parity-and-parity-selection-rules]] - symmetry operators and their eigenvalues.
2. [[rotation-operator-and-rotational-symmetry]] and [[symmetry-conservation-and-degeneracy]] - conserved quantities and degeneracy.
3. [[rotational-selection-rules-and-wigner-eckart]] - selection rules from symmetry alone.
4. [[heisenberg-picture-and-time-translation]] - time evolution as a symmetry operation.

**Deep (Sakurai companions).** [[rotations-su2-so3-and-euler-angles]], [[wigner-rotation-matrices]], [[schwinger-oscillator-model]], [[time-reversal-and-antiunitary-operators]], [[spherical-tensor-operators]], [[feynman-path-integral]].

**Checkpoint.** Show that a $2\pi$ rotation multiplies a spin-$\tfrac12$ state by $-1$, and use the Wigner–Eckart theorem to list the allowed $\Delta\ell$, $\Delta m$ for a dipole transition.

## Stage 7 - Dynamics and scattering

**Core.**

1. [[two-level-systems-and-rabi-oscillations]] - the exactly solvable driven system (and the qubit of Part 5).
2. [[time-dependent-perturbation-theory]] and [[emission-absorption-and-spontaneous-emission]] - transition probabilities and selection rules in spectroscopy.
3. [[sudden-and-adiabatic-approximations]] - the limits behind Born–Oppenheimer and adiabatic state preparation.
4. [[scattering-cross-sections-and-amplitude]] and [[partial-wave-analysis-and-phase-shifts]] - scattering in a central potential.

**Deep.** [[interaction-picture-and-dyson-series]], [[fermi-golden-rule-and-decay-width]], [[berry-phase]], [[born-approximation-and-lippmann-schwinger]], [[low-energy-scattering-and-resonances]].

**Checkpoint.** Derive the Rabi formula and its resonance width; obtain the Born cross section of a Yukawa potential.

## Where to go next

- **Quantum chemistry and electronic structure:** Part 4 via [[reading-order-electronic-structure]] (Stage 2 lists the Part 2 notes it relies on). Part 3 (quantum chemistry proper) builds on stages 3-5 and 7.
- **Quantum computing:** [[reading-order-quantum-computing]]; it needs stages 2-3 and the two-level system of stage 7.

## Source

Organizes the notebook's own notes. Part 2 is built on Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018) and Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021); each note cites its exact sections.
