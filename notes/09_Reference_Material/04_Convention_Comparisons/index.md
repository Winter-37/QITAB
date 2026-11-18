Side-by-side comparisons of conventions that differ between books and codes. Mixing two conventions is the most common source of a wrong factor of 2 or a wrong sign, and the error is usually silent: magnitudes come out right and relative signs or normalizations do not. Integral notation lives in Part 4, Chapter 2 ([[integral-notation|integral notation]]) and atomic units in Part 4, Chapter 1, where they are first needed.

**Path.**

1. [[density-matrix-conventions]] - index order and normalization of the one- and two-electron density matrices in Szabo, HJO, Shavitt–Bartlett, YOGS and PySCF, with the energy formula for each.
2. [[excitation-operator-conventions]] - excitation operators, the operator strings behind Szabo's excited determinants, and spin-orbital versus closed-shell coupled-cluster amplitudes.
3. [[angular-momentum-phase-conventions]] - Condon–Shortley phases, Clebsch–Gordan signs, real solid harmonics and PySCF's ordering, active rotations.
4. [[qubit-ordering-conventions]] - Nielsen–Chuang (big-endian) versus Qiskit (little-endian).

**Needs.** The notation chapter of this part; Part 4, Chapters 5-6 for the first two notes; Part 2, Chapter 4 for the third; Part 5, Chapter 2 for the fourth.

**Leads to.** Any calculation that combines formulas from one book with numbers from another or from a program.

**Planned sections:** Fourier-transform conventions (currently in [[fourier-transforms-and-the-dirac-delta]]); Fermion-to-qubit orbital orderings in common libraries.
