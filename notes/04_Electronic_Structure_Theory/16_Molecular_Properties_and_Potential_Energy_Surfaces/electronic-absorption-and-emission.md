---
id: electronic-absorption-and-emission
title: Electronic absorption and emission - UV/vis spectra from poles and residues, selection rules, vertical, adiabatic and 0-0 energies, line shapes, fluorescence and Kasha's rule, and phosphorescence from spin-orbit coupling as a quadratic-response residue
summary: A UV/vis spectrum follows from excitation energies (poles of the linear response function) and oscillator strengths (residues), broadened by a line shape. In the nonrelativistic electric-dipole picture, transitions keep the spin and obey symmetry selection rules (Laporte for centrosymmetric molecules); dark states can be reached by multiphoton absorption. Computed vertical energies are not observable. The band maximum, the 0-0 line and the adiabatic energy differ through Franck-Condon structure and zero-point energy. Lorentzian (homogeneous), Gaussian (inhomogeneous) and Voigt line shapes are normalized as used in practice. Emission obeys Kasha's rule and is red-shifted (Stokes shift), with radiative lifetime from the Einstein A coefficient. Phosphorescence borrows intensity through spin-orbit coupling, a first-order perturbation that makes the transition moment a single residue of a quadratic response function; the averaged lifetime is 1/τ = (1/3)Σ1/τ_k. Checked: line-shape normalizations, and NRS's formaldehyde triplet lifetime of 24.7 ms, which follows from one bright sublevel with f = 7.3 × 10⁻⁷.
status: in-progress
kind: theory
level: intermediate
tags: [uv-vis, absorption, fluorescence, phosphorescence, kasha-rule, stokes-shift, line-shape, voigt, spin-orbit-coupling, radiative-lifetime, oscillator-strength]
prerequisites: [residue-analysis-of-response-functions, damped-response-and-absorption-cross-sections, dispersion-oscillator-strengths-and-sum-rules]
related: [emission-absorption-and-spontaneous-emission, tddft-linear-response, linear-response-for-variational-wave-functions, raman-scattering, born-oppenheimer-approximation, parity-and-parity-selection-rules, zero-point-energy-and-thermochemistry]
conventions: [atomic-units, si-units]
key: tau
order: 80
date: 2026-11-24
---

Atomic units unless SI is stated ($c\approx137.036$). $f_{n0}$ is the oscillator strength ([[dispersion-oscillator-strengths-and-sum-rules]]); $S_n$ and $T_n$ denote singlet and triplet states.

## Absorption spectra from response functions

**Ingredients.** Excitation energies are the poles of the linear response function, and squared transition moments its residues ([[residue-analysis-of-response-functions]]). The cross section is $\sigma(\omega) = (2\pi^2/c)\sum_nf_{n0}L(\omega-\omega_{n0})$ for normalized line shapes $L$. Alternatively the damped response gives $\sigma = (4\pi\omega/c)\,\mathrm{Im}\,\bar\alpha(\omega)$ directly ([[damped-response-and-absorption-cross-sections]]). Absorbance follows from the Beer-Lambert law. Detectors usually stop near 180 nm, about 7 eV.

**Selection rules (nonrelativistic, electric dipole).**

- **Spin.** The dipole operator has no spin part, so transitions keep the spin multiplicity. Singlet-triplet transitions need spin-orbit coupling, which grows with nuclear charge.
- **Space.** From a totally symmetric ground state, only states transforming like $x$, $y$ or $z$ are reachable. With an inversion centre, the parity must change ($g\leftrightarrow u$, Laporte; [[parity-and-parity-selection-rules]]).
- **Dark states.** States that are forbidden, or allowed but with tiny $f$, are dark. Magnetic dipole and electric quadrupole transitions are 2-3 orders weaker; multiphoton absorption reaches dark states more effectively.

**Which energy to compare.** The quantities are defined in this figure-free way:

- **Vertical** $\Delta E_{\rm ve}$: the response-theory excitation energy at the ground-state geometry. It is not directly observable.
- **Adiabatic** $\Delta E_{\rm ad}$: the difference of the two electronic energies, each at its own minimum. It requires an excited-state geometry optimization.
- **0-0** $\Delta E_{00} = \Delta E_{\rm ad} + \Delta E_{\rm zpv}$, with $\Delta E_{\rm zpv}$ the difference of the two zero-point energies. It is the lowest line of a resolved gas-phase spectrum and the only line shared by absorption and fluorescence. In solution it is approximated by the crossing of the two spectra.
- **Band maximum.** It is the vibronic level with the largest Franck-Condon factor, generally above the 0-0 line. NRS's ethylene model has its maximum at 7.165 eV against a vertical 7.372 eV and a 0-0 line at 6.822 eV ([[raman-scattering]]).

**Method dependence.** Errors of a method vary with the character of the state, so even the ordering of states can be method dependent. TDDFT with standard functionals underestimates charge-transfer states by up to 1-2 eV and describes Rydberg states poorly ([[tddft-linear-response]]). Such states usually have small oscillator strengths, which limits their visible impact.

## Line shapes

**Normalization.** Each line is spread by a function with $\int L\,d\omega = 1$.

- **Lorentzian** $L = \gamma/\{\pi[(\omega-\omega_{n0})^2+\gamma^2]\}$, HWHM $\gamma$: homogeneous broadening, the same for every molecule (lifetime, collisions). It is what damped response produces.
- **Gaussian** in NRS's parametrization $g = \frac{\sqrt2}{\sigma\sqrt\pi}\exp[-2(\omega-\omega_{n0})^2/\sigma^2]$, HWHM $\sigma\sqrt{\ln2}/\sqrt2$: inhomogeneous broadening from a distribution of environments (solvent configurations, solids).
- **Voigt** $V = \int g(\omega')L(\omega-\omega')\,d\omega'$: both at once, usual in solution.

**Practice.** Calculations usually convolute vertical stick spectra with an empirical width (NRS's dipeptide example uses $\gamma = 0.2$ eV Lorentzians or $0.4$ eV Gaussians). This does not capture vibronic asymmetry: absorption bands tail to the blue, emission bands to the red.

## Emission

**Kasha's rule.** After absorption, vibrational relaxation, internal conversion (IC, same spin) and intersystem crossing (ISC, spin change) are fast between closely spaced excited states. The large gap to the ground state makes the last step slow. Emission therefore comes almost only from the lowest excited state of each multiplicity ($S_1$, $T_1$), and its yield does not depend on the excitation wavelength (Vavilov). An isolated higher state can break the rule: azulene emits from $S_2$.

**Fluorescence** ($S_1\to S_0$).

- **Stokes shift.** The molecule relaxes to the $S_1$ minimum first, so emission is red-shifted relative to absorption. The vibronic profile is roughly mirrored.
- **Quantum yield.** $\Phi$ = photons emitted/absorbed, the competition between radiative and nonradiative decay.
- **Radiative rate.** Spontaneous emission (Einstein $A$, [[emission-absorption-and-spontaneous-emission]]) gives, for equal degeneracies,

$$
\frac1{\tau_{\rm rad}} = A = \frac{2\omega^2}{c^3}f\quad\text{(a.u.)},\qquad \text{SI: }\ A = \frac{\omega^2e^2}{2\pi\varepsilon_0m_ec^3}f.
\label{tau}
$$

  An allowed transition with $f = 0.1$ at 3 eV lives 25.6 ns.

**Phosphorescence** ($T_1\to S_0$). With the Breit-Pauli spin-orbit operator $\hat H_{\rm SO}$ (one-electron term $\propto Z_A\hat{\mathbf l}_A\cdot\hat{\mathbf s}/r^3$ plus two-electron screening terms; mean-field and atomic mean-field (AMFI) approximations exist), the transition moment of triplet sublevel $k$ appears at first order:

$$
M^k_\alpha = \sum_n\frac{\langle S_0|\hat\mu_\alpha|S_n\rangle\langle S_n|\hat H_{\rm SO}|T^k_1\rangle}{E(S_n)-E(T_1)} + \sum_n\frac{\langle S_0|\hat H_{\rm SO}|T_n\rangle\langle T_n|\hat\mu_\alpha|T^k_1\rangle}{E(T_n)-E(S_0)}.
$$

This has the structure of a single residue of a quadratic response function with $\hat\mu$ and $\hat H^k_{\rm SO}$ as operators:

$$
M^k_\alpha = \lim_{\omega\to\omega_{f0}}(\omega_{f0}-\omega)\,\frac{\langle\langle\hat\mu_\alpha;\hat H^k_{\rm SO},\hat\Omega\rangle\rangle_{0,\omega}}{\langle f|\hat\Omega|0\rangle},
$$

where $\hat\Omega$ is any operator connecting to $f$; it cancels. So spin-forbidden intensities come from a ground-state calculation. In a relativistic (four-component) calculation the moment is an ordinary linear-response residue instead.

**Sublevel averaging.** Each sublevel has its own rate, $1/\tau_k = (4\omega^3/3c^3)\sum_\alpha|M^k_\alpha|^2$. At temperatures high compared with the zero-field splitting they are equally populated, so

$$
\frac1\tau = \frac13\sum_{k=1}^3\frac1{\tau_k}.
$$

## Worked example

!!! example "Formaldehyde phosphorescence and line shapes (NRS Fig. 8.18; arithmetic checked for this note)"
    **NRS's calculation.** Four-component HF/t-aug-cc-pVTZ at B3LYP/cc-pVTZ structures. The $n\to\pi^*$ triplet is at 3.46 eV vertical in absorption ($C_{2v}$). Emission from the relaxed, pyramidalized $T_1$ minimum is at 1.96 eV. The oscillator strengths are $5.1\times10^{-7}$ and $7.3\times10^{-7}$, and the predicted lifetime is 24.7 ms.

    **Arithmetic check.** With Eq. [[#tau]], one sublevel with $f = 7.3\times10^{-7}$ at 1.96 eV has $\tau_k = 8.22$ ms. If the other two sublevels are dark, the high-temperature average gives $\tau = 3\tau_k = 24.7$ ms, NRS's number. ($f = 5.1\times10^{-7}$ would give $\tau_k = 11.8$ ms.)

    **Line shapes.** Numerical integration confirms that NRS's Gaussian with HWHM $\sigma\sqrt{\ln2}/\sqrt2$ and the Lorentzian both integrate to 1 and reach half height at their HWHM. The Voigt convolution agrees with `scipy.special.voigt_profile` (peak 2.2456 for HWHM 0.1 each).

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 8.5 (introduction, Jablonski processes, Kasha's rule), pp. 335–338; Sec. 8.5.1, Eqs. (8.163)–(8.165), Figs. 8.14–8.17 (described); Sec. 8.5.2; Sec. 8.5.3, Eqs. (8.166)–(8.171), Fig. 8.18. NRS cite B. A. Hess, C. M. Marian, U. Wahlgren and O. Gropen, Chem. Phys. Lett. 251, 365 (1996) for AMFI (to verify). The interpretation of the 24.7 ms as one bright sublevel is an inference from the arithmetic, not stated by NRS. The calculations are in `Claude outputs/part4_response_batchB1.py`, section D.
