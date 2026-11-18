Nuclear motion on a potential energy surface: how a computed electronic curve becomes vibrational and rotational levels, spectra and dissociation energies. The chapter starts with the diatomic molecule, where the nuclear problem reduces to one radial equation that can be solved essentially exactly, and the polyatomic harmonic analysis is in Part 4, Chapter 16.

## What this chapter is about

- **Vibration.** The harmonic limit, anharmonicity, the Morse potential, IR selection rules, fundamentals and overtones, isotope effects, and the difference between $D_e$ and $D_0$.
- **Rotation.** The rigid rotor, rotational constants and bond lengths from microwave lines, vibration–rotation coupling and centrifugal distortion.
- **Numerics.** The Numerov method, which solves the radial equation for any computed curve.

## Why it matters

A geometry optimization gives $R_e$ and a Hessian; experiment measures band origins, rotational constants and $D_0$. This chapter is the bridge: it says which computed number corresponds to which measured one, and how large the corrections between them are (zero-point energy, anharmonicity, vibrational averaging of bond lengths).

**Path.**

1. [[diatomic-vibration-and-anharmonicity]] - from $U(R)$ to vibrational levels; includes the FCI/cc-pVQZ curve of H₂ solved for its levels.
2. [[rigid-rotor-and-rovibrational-levels]] - rotation, $B_v$, $\alpha_e$ and centrifugal distortion on the same curve.
3. [[numerov-method]] - the numerical method used in both, with its convergence checks.

**Needs.** Part 2: the harmonic oscillator (Ch. 2), angular momentum and central potentials (Ch. 4), two-particle systems (Ch. 5). Part 4, Ch. 1 (Born–Oppenheimer).

**Leads to.** [[harmonic-vibrational-analysis]] and [[zero-point-energy-and-thermochemistry]] (Part 4, Ch. 16) for polyatomic molecules; Chapter 9 (potential energy surfaces).

**Planned sections:** Normal coordinates and polyatomic vibration–rotation (Wilson–Decius–Cross level); Vibrational perturbation theory.
