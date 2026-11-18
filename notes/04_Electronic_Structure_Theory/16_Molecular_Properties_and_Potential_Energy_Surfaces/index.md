Using energy derivatives: geometry optimization, how the error of an approximate surface turns into a geometry error, harmonic vibrational analysis, and zero-point and thermal corrections. Other properties are planned.

## What this chapter is about

Chapter 15 showed how to compute gradients and Hessians. This chapter uses them on the potential energy surface $E(\mathbf R)$:

- **Finding stationary points.** Minima and transition states satisfy $\mathbf g(\mathbf R)=0$. Newton–Raphson steps, $\Delta\mathbf R=-\mathbf H^{-1}\mathbf g$, and their quasi-Newton and trust-region variants find these points efficiently.
- **Predicting geometry errors.** An approximate method gives an approximate surface. The shift of its minimum from the reference minimum is set by the force the approximate method predicts at the reference geometry, not by the energy error itself.
- **Vibrations.** The mass-weighted Hessian at a stationary point gives harmonic frequencies and normal modes, and decides whether the point is a minimum or a saddle.
- **Thermochemistry.** Zero-point energy turns $D_e$ into $D_0$; rigid-rotor harmonic-oscillator partition functions give $H$, $S$ and $G$ at finite temperature.

## Why it matters

- **Structures are the most common output of a calculation.** Bond lengths, angles and conformations come from geometry optimization, and nearly every other property is evaluated at an optimized geometry.
- **Optimizers need curvature.** Plain gradient steps zigzag. Newton steps use the Hessian, either exact, approximate or built up from gradients (BFGS), together with coordinate choice and step control. This is why optimizations converge in tens of steps, not thousands.
- **A constant energy error does not move a minimum.** Only the slope of the error at the reference minimum does. This explains why methods with large total-energy errors can still give good geometries, and why errors in an embedding or quantum solver show up in forces before they show up in energies.

## Where it is used later

- [[dmet-analytic-nuclear-gradient|The DMET gradient]] (Chapter 19) and [[hao-2026-dmet-vqe-geometry|DMET-VQE geometry optimization]] (paper note, Part 8).
- [[hjo-calibration-structures-and-dipoles|Calibration of structures]] (Chapter 14), whose trends this analysis explains.

## The main ideas, in order

1. **Newton–Raphson optimization.** A second-order expansion of $E(\mathbf u)$, the Newton step, quasi-Newton Hessian updates, step control, and characterizing a stationary point by its Hessian eigenvalues.
2. **Geometry error.** To first order the error is $\delta\mathbf R=-\mathbf H^{-1}\mathbf g$, where $\mathbf g$ is the approximate force at the reference minimum. The energy relaxation is second order in $\mathbf g$.
3. **Harmonic analysis.** Diagonalize $H_{ij}/\sqrt{m_im_j}$ after projecting out translations and rotations; $\tilde\nu = 5140.487\sqrt\lambda$ cm$^{-1}$.
4. **ZPE and thermochemistry.** $D_0 = D_e - \tfrac12\sum h\nu_k$; RRHO $U$, $H$, $S$, $G$.

## How to read it

**Path.** [[geometry-optimization]], [[geometry-error-of-an-approximate-surface]], [[harmonic-vibrational-analysis]], [[zero-point-energy-and-thermochemistry]].

**Needs.** Chapter 15 (analytic gradients and Hessians) and Chapter 1 (the Born–Oppenheimer surface).

**Leads to.** Embedding gradients (Chapter 19), the planned excited-states chapter (Chapter 18), and Part 3, Chapters 6 and 9 (vibrational spectra and potential energy surfaces as chemical objects).

**Core (first pass).** [[geometry-optimization]], [[harmonic-vibrational-analysis]], [[zero-point-energy-and-thermochemistry]]. **Deep.** [[geometry-error-of-an-approximate-surface]].

**Checkpoint.** From a second-order expansion, show that the geometry error is $-\mathbf H^{-1}g$ with $g$ the force at the reference minimum, and that the relaxation energy is second order in $g$.

**Planned sections:** Dipole moments and polarizabilities; IR intensities; Excitation energies and transition properties.
