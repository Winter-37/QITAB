Using energy derivatives and response functions: geometry optimization, how the error of an approximate surface turns into a geometry error, harmonic vibrational analysis, zero-point and thermal corrections, and the properties that spectroscopy measures: polarizabilities and dispersion coefficients, IR intensities, Raman scattering, electronic absorption and emission, magnetic properties (magnetizability, NMR, hyperfine and EPR parameters), multiphoton and X-ray absorption, chiroptical spectroscopies (optical rotation, ECD, MCD, VCD, ROA), and the vibrational contributions to all of these (zero-point averaging and pure vibrational terms).

## What this chapter is about

Chapter 15 showed how to compute gradients and Hessians. This chapter uses them on the potential energy surface $E(\mathbf R)$:

- **Finding stationary points.** Minima and transition states satisfy $\mathbf g(\mathbf R)=0$. Newton–Raphson steps, $\Delta\mathbf R=-\mathbf H^{-1}\mathbf g$, and their quasi-Newton and trust-region variants find these points efficiently.
- **Predicting geometry errors.** An approximate method gives an approximate surface. The shift of its minimum from the reference minimum is set by the force the approximate method predicts at the reference geometry, not by the energy error itself.
- **Vibrations.** The mass-weighted Hessian at a stationary point gives harmonic frequencies and normal modes, and decides whether the point is a minimum or a saddle.
- **Thermochemistry.** Zero-point energy turns $D_e$ into $D_0$; rigid-rotor harmonic-oscillator partition functions give $H$, $S$ and $G$ at finite temperature.
- **Properties and spectra.** The response functions of Chapter 17 turned into observables: polarizabilities and $C_6$ dispersion coefficients from polarizabilities at imaginary frequencies, IR band intensities from dipole derivatives, Raman intensities from polarizability derivatives (and resonance Raman from the excited state), and UV/vis absorption, fluorescence and phosphorescence from poles and residues. Magnetic properties add the gauge-origin problem and London orbitals; core and multiphoton spectroscopies add relaxation, core-valence separation and higher-order residues; chiroptical properties add the mixed electric–magnetic polarizability $G'$.

## Why it matters

- **Structures are the most common output of a calculation.** Bond lengths, angles and conformations come from geometry optimization, and nearly every other property is evaluated at an optimized geometry.
- **Optimizers need curvature.** Plain gradient steps zigzag. Newton steps use the Hessian, either exact, approximate or built up from gradients (BFGS), together with coordinate choice and step control. This is why optimizations converge in tens of steps, not thousands.
- **Spectra are how calculations meet experiment.** Vibrational spectra need the Hessian plus a property derivative, computed with the same response machinery (Chapter 15). Electronic spectra need excitation energies, oscillator strengths and a line shape. Dispersion coefficients, the $C_6$ behind every empirical dispersion correction, come from frequency-dependent polarizabilities.
- **A constant energy error does not move a minimum.** Only the slope of the error at the reference minimum does. This explains why methods with large total-energy errors can still give good geometries, and why errors in an embedding or quantum solver show up in forces before they show up in energies.

## Where it is used later

- [[dmet-analytic-nuclear-gradient|The DMET gradient]] (Chapter 19) and [[hao-2026-dmet-vqe-geometry|DMET-VQE geometry optimization]] (paper note, Part 8).
- [[hjo-calibration-structures-and-dipoles|Calibration of structures]] (Chapter 14), whose trends this analysis explains.

## The main ideas, in order

1. **Newton–Raphson optimization.** A second-order expansion of $E(\mathbf u)$, the Newton step, quasi-Newton Hessian updates, step control, and characterizing a stationary point by its Hessian eigenvalues.
2. **Geometry error.** To first order the error is $\delta\mathbf R=-\mathbf H^{-1}\mathbf g$, where $\mathbf g$ is the approximate force at the reference minimum. The energy relaxation is second order in $\mathbf g$.
3. **Harmonic analysis.** Diagonalize $H_{ij}/\sqrt{m_im_j}$ after projecting out translations and rotations; $\tilde\nu = 5140.487\sqrt\lambda$ cm$^{-1}$.
4. **ZPE and thermochemistry.** $D_0 = D_e - \tfrac12\sum h\nu_k$; RRHO $U$, $H$, $S$, $G$.
5. **Polarizabilities and dispersion.** Unsöld picture, two-state model, induction and dispersion energies, Casimir–Polder $C_6 = (3/\pi)\int\alpha_A(iu)\alpha_B(iu)du$.
6. **IR intensities.** Double-harmonic transition moments $\sqrt{\hbar/2\omega}\,\partial\mu/\partial Q$, km/mol intensities, selection rules, anharmonicity.
7. **Raman.** The Kramers–Heisenberg–Dirac transition polarizability, Placzek's $\partial\alpha/\partial Q$, resonance Raman.
8. **Electronic spectra.** Vertical, adiabatic and 0–0 energies, line shapes, Kasha's rule, radiative lifetimes, phosphorescence through spin–orbit coupling.
9. **Magnetizability.** $\xi = \xi^{\rm dia} + \xi^{\rm para}$, origin dependence in a finite basis, London orbitals, Pascal's rule.
10. **NMR.** The spin Hamiltonian, Ramsey's shielding ($\sigma^{\rm dia} + \sigma^{\rm para}$, GIAO) and the DSO, PSO, FC, SD parts of $J_{KL}$; Bloch equations.
11. **Nucleus–electron interactions and EPR.** Finite nuclei and the Mössbauer shift, hyperfine $\mathbf A$, quadrupole coupling and field gradients (234.9647 MHz per b·au), Landé $g_J$, the $g$-matrix and zero-field splitting.
12. **Multiphoton absorption.** $j$-photon moments as single residues, rotational averages, two- and three-state models, parity rules.
13. **X-ray absorption.** Core-hole relaxation, ΔSCF and static exchange, core-valence separation and damped response, linear dichroism and the magic angle.
14. **Optical activity, ECD, MCD.** Rosenfeld's $\beta$ and rotatory strengths, gauge origin and the modified velocity gauge, Faraday A, B, C terms.
15. **Vibrational optical activity.** VCD from atomic polar and axial tensors; ROA invariants and scattering geometries.
16. **Electronic and nuclear contributions.** The vibronic sum over states splits into pure vibrational terms $[\mu^2]$, $[\mu\alpha]$, $[\mu^3]$ and the zero-point average $\langle0|\alpha^{\rm e}(\mathbf R)|0\rangle$: $\alpha = \alpha^{\rm e} + \Delta\alpha^{\rm zpva} + \alpha^{\rm v}$.
17. **Zero-point vibrational averaging.** $\Delta P = \tfrac{\hbar}{4}\sum_aP_{aa}/\omega_a - \sum_aP_a\omega_a^{-2}\partial E_{\rm zpv}/\partial Q_a$; longer averaged bonds, isotope effects, temperature.
18. **Pure vibrational terms and nuclear relaxation.** Double-harmonic $\sum_a\mu_a^2/(\omega_a^2-\omega^2)$, anharmonic corrections, and the static field-relaxed-geometry picture (nuclear relaxation plus curvature).

## How to read it

**Path.** [[geometry-optimization]], [[geometry-error-of-an-approximate-surface]], [[harmonic-vibrational-analysis]], [[zero-point-energy-and-thermochemistry]], [[polarizabilities-and-dispersion-coefficients]], [[infrared-intensities]], [[raman-scattering]], [[electronic-absorption-and-emission]], [[magnetizability-and-gauge-origin]], [[nmr-shielding-and-spin-spin-coupling]], [[hyperfine-coupling-and-epr]], [[multiphoton-absorption]], [[x-ray-absorption]], [[optical-activity-ecd-and-mcd]], [[vibrational-optical-activity]], [[electronic-and-nuclear-contributions-to-response]], [[zero-point-vibrational-corrections-to-properties]], [[pure-vibrational-contributions-and-nuclear-relaxation]].

**Needs.** Chapter 15 (analytic gradients and Hessians) and Chapter 1 (the Born–Oppenheimer surface). The property sections also need Chapter 17 (response functions, residues, damped response).

**Leads to.** Embedding gradients (Chapter 19), the excited-states chapter (Chapter 18, where vibronic band shapes continue the absorption section), and Part 3, Chapters 6 and 9 (vibrational spectra and potential energy surfaces as chemical objects).

**Core (first pass).** [[geometry-optimization]], [[harmonic-vibrational-analysis]], [[zero-point-energy-and-thermochemistry]], [[infrared-intensities]]. **Deep.** [[geometry-error-of-an-approximate-surface]], [[polarizabilities-and-dispersion-coefficients]], [[raman-scattering]], [[electronic-absorption-and-emission]], and the magnetic, X-ray, chiroptical and vibrational-correction sections from [[magnetizability-and-gauge-origin]] on.

**Checkpoint.** From a second-order expansion, show that the geometry error is $-\mathbf H^{-1}g$ with $g$ the force at the reference minimum, and that the relaxation energy is second order in $g$.

**Planned sections:** electric-field-gradient and Kerr birefringences in detail; relativistic NMR and EPR (four-component response).
