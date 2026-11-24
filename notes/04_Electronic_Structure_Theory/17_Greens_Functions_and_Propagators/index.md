Ionization energies, excitation spectra and frequency-dependent molecular properties directly from propagators and response functions, without computing each state separately.

## What this chapter is about

Methods so far compute one state at a time: the ground state, then each excited or ionized state as a separate calculation. Spectroscopy measures *differences* between states and the *response* of a molecule to light. Propagators, or many-body Green's functions, target those differences directly. A propagator $\langle\langle\hat A;\hat B\rangle\rangle_E$ is a function of energy with:

- **poles** at the energy differences between the reference state and other states;
- **residues** equal to products of transition matrix elements.

Two cases matter most:

- the **one-particle Green's function** (electron propagator), with $\hat A,\hat B$ creation and annihilation operators. Its poles are ionization energies and electron affinities.
- the **polarization propagator**, with $\hat A,\hat B$ one-body excitation operators. Its poles are excitation energies and its residues give oscillator strengths.

The second half of the chapter takes the time-domain view of the polarization propagator, response theory. A molecule in a weak oscillating field has an induced dipole that expands in the field. The coefficients are the linear, quadratic and cubic response functions: the frequency-dependent polarizability $\alpha(-\omega;\omega)$ and the hyperpolarizabilities $\beta$ and $\gamma$ of nonlinear optics. They are derived first for exact states, then reformulated as derivatives of a variational time-averaged quasienergy. That reformulation carries over to SCF, CI, MCSCF and coupled-cluster references, and, with damping, to absorption spectra.

## Why it matters

- **Corrections to Koopmans' theorem.** The electron propagator, with the self-energy $\Sigma(E)$ in the Dyson equation $G^{-1}=G_0^{-1}-\Sigma$, adds orbital relaxation and correlation to frozen-orbital ionization energies. Second order is already a large improvement.
- **RPA and TDHF.** The polarization propagator at the Hartree–Fock level is the random-phase approximation. It gives excitation energies, dynamic polarizabilities and the stability conditions of Chapter 7 in one framework. TDDFT has the same structure.
- **Most spectroscopies are response functions.** UV-vis absorption is the imaginary part of the damped polarizability. Two-photon absorption is a residue of $\beta$. Refractive indices, Kerr and Pockels effects, and second- and third-harmonic generation are $\alpha$, $\beta$ and $\gamma$ at specific frequencies. Excited-state dipoles and polarizabilities are double residues. One ground-state calculation per frequency replaces a calculation per excited state.
- **The same mathematics as analytic derivatives.** Response equations are the time-dependent version of CPHF. The quasienergy Lagrangian is the time-dependent version of the gradient Lagrangian of Chapter 15. The $2n+1$ and $2n+2$ rules hold in both.
- **It is the language of response theory and of $GW$.** Linear-response CC, ADC and the $GW$ method used in materials science are propagator methods. The superoperator formalism here is a common starting point for all of them.
- **It connects to the single-particle Green's function of Part 2.** It is the same resolvent idea, $(E-\hat H)^{-1}$, applied to a many-electron system.

## Where it is used later

- [[tddft-linear-response|TDDFT]] and the rest of the excited-states chapter (Chapter 18).
- [[eom-ccsd-and-size-extensivity|EOM-CC]] (Chapter 12), whose excitation energies are the poles of the coupled-cluster response function.
- Molecular properties and spectroscopies (planned sections of Chapter 16).

## The main ideas, in order

1. **The superoperator formalism.** Propagators, their spectral representation, and the moment expansion.
2. **The electron propagator.** The Dyson equation, the self-energy, and second-order ionization energies with orbital relaxation and pair correlation.
3. **The polarization propagator.** TDHF/RPA, its stability, coupled Hartree–Fock, and length and velocity forms of transition moments.
4. **Exact-state response functions.** The Kubo expansion, sum-over-states $\alpha$, $\beta$, $\gamma$, secular divergences and the phase-isolated wave function.
5. **The quasienergy.** Phase isolation, the time-dependent Hellmann-Feynman theorem, $\delta Q_T = 0$, response functions as $Q_T$ derivatives, and the $2n+1$ rule in time.
6. **Dispersion and sum rules.** Nonlinear optical processes, Cauchy moments, the universal dispersion of $\beta$ and $\gamma$, oscillator strengths and the TRK rule.
7. **Residues.** Poles and residues give excitation energies, multiphoton matrix elements and excited-state properties.
8. **Damping.** Relaxation in the Liouville equation, complex polarizabilities, line shapes and absorption cross sections.
9. **Approximate references.** $\mathbf E^{[2]}$ and $\mathbf S^{[2]}$ for SCF, CI and MCSCF, paired eigenvalues and stability. Coupled-cluster response from a time-averaged Lagrangian, with the CC Jacobian setting the poles.

## How to read it

**Path.**

1. [[propagators-and-superoperators|The superoperator formalism]].
2. [[one-particle-greens-function|The one-particle Green's function]] and [[ionization-potentials-second-order-self-energy|second-order self-energy]] for ionization potentials.
3. [[polarization-propagator-rpa|The polarization propagator and RPA]].
4. [[exact-state-response-functions|Exact-state response functions]].
5. [[quasienergy-and-time-dependent-variational-principle|The quasienergy and the time-dependent variational principle]].
6. [[dispersion-oscillator-strengths-and-sum-rules|Dispersion, oscillator strengths and sum rules]].
7. [[residue-analysis-of-response-functions|Residue analysis]].
8. [[damped-response-and-absorption-cross-sections|Damped response and absorption]].
9. [[linear-response-for-variational-wave-functions|Linear response for SCF, CI and MCSCF]].
10. [[coupled-cluster-response-functions|Coupled-cluster response functions]].

**Needs.** Chapters 3, 10 and 15. The response sections also need time-dependent perturbation theory and the density operator (Part 2, Chapters 3 and 11), and the variational perturbation theory note at the end of Chapter 15.

**Leads to.** Chapter 18 (excited states, starting with TDDFT) and the planned property sections of Chapter 16.

**Core (first pass).** [[polarization-propagator-rpa]], [[exact-state-response-functions]], [[linear-response-for-variational-wave-functions]].

**Deep (second pass).** [[quasienergy-and-time-dependent-variational-principle]], [[residue-analysis-of-response-functions]], [[damped-response-and-absorption-cross-sections]], [[coupled-cluster-response-functions]]; [[dispersion-oscillator-strengths-and-sum-rules]] as reference.

**Checkpoint.** Show that the static limit of the TDHF linear response function is the CPHF polarizability, and that its poles are the paired eigenvalues of $\mathbf E^{[2]}\mathbf X = \lambda\mathbf S^{[2]}\mathbf X$.

**Reading.** Second-pass chapter: skip it on a first reading and come back after the core chapters (Chapter 5 first; it is the prerequisite for almost every deep note).

**Planned sections:** Algebraic diagrammatic construction (ADC); the $GW$ approximation; magnetic and mixed electric-magnetic response (magnetizabilities, optical rotation).
