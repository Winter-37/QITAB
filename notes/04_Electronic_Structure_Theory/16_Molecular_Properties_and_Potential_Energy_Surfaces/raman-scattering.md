---
id: raman-scattering
title: Raman scattering - the modulated polarizability, the Kramers-Heisenberg-Dirac transition polarizability, Placzek's approximation and polarizability derivatives, and resonance Raman (Franck-Condon, IMDHO, short-time and time-dependent forms)
summary: Classically, a vibrating molecule in a light field has a polarizability that oscillates with the nuclei. The induced dipole then contains sidebands at ω ± ω_vib (Stokes and anti-Stokes), incoherent because vibrational phases are random. Quantum mechanically, the scattering amplitude is the transition polarizability of Kramers, Heisenberg and Dirac, a two-photon object like the two-photon absorption amplitude. The difference is that Raman scattering is linear in the intensity. Far from electronic resonance, Placzek's approximations reduce it to ⟨f|α_e(ω;Q)|0⟩, and with harmonic states to [α]₁₀ = (ħ/2ω_a)^{1/2}∂α/∂Q_a: Raman activity needs a polarizability that changes along the mode. Near resonance one electronic state dominates. Franck-Condon, independent-mode displaced-oscillator (IMDHO), short-time (complex polarizability derivative) and time-dependent wave-packet forms then make the sum over vibronic states tractable, with overtones as strong as fundamentals. Recomputed: N₂ at B3LYP, including the anharmonic overtone.
status: in-progress
kind: theory
level: intermediate
tags: [raman, transition-polarizability, kramers-heisenberg-dirac, placzek, polarizability-derivative, resonance-raman, franck-condon, imdho, stokes, anti-stokes]
prerequisites: [polarizabilities-and-dispersion-coefficients, infrared-intensities, residue-analysis-of-response-functions]
related: [harmonic-vibrational-analysis, damped-response-and-absorption-cross-sections, numerov-method, diatomic-vibration-and-anharmonicity, electronic-absorption-and-emission, tddft-linear-response]
conventions: [atomic-units]
key: khd
order: 70
date: 2026-11-24
---

Atomic units ($\hbar = 1$ unless shown). $Q_a$ are mass-weighted normal coordinates with frequencies $\omega_a$. $\alpha^{\rm e}(\omega;\mathbf Q)$ is the electronic polarizability at a nuclear configuration $\mathbf Q$. $|0\rangle$ and $|f\rangle$ are initial and final vibrational (vibronic) states; $\omega$ and $\omega'$ are incident and scattered photon frequencies.

## The classical picture

**Modulated polarizability.** A molecule in a field $F\cos\omega t$ has $\mu(t) = \alpha^{\rm e}[\omega;Q(t)]\,F\cos\omega t$. If the nuclei vibrate, $Q(t) = Q_0\cos(\omega_vt+\phi)$, then to first order

$$
\mu(t) = \alpha^{\rm e}(\omega;0)F\cos\omega t + \tfrac12\frac{\partial\alpha^{\rm e}}{\partial Q}Q_0F\big[\cos((\omega-\omega_v)t-\phi) + \cos((\omega+\omega_v)t+\phi)\big].
$$

The carrier at $\omega$ radiates Rayleigh light. The sidebands at $\omega\mp\omega_v$ radiate Stokes (photon loses energy) and anti-Stokes (photon gains energy) Raman light. The phase $\phi$ differs randomly between molecules, so Raman light is incoherent.

**NRS's N₂ demonstration.** NRS run a constant-energy trajectory of N₂ on a B3LYP potential. They compute the TDDFT polarizability at 1 PHz along it, subtract the carrier, and Fourier-transform the autocorrelation function of the remainder. This reveals exactly the two sidebands at $\omega\pm\omega_v$. The trajectory period is 14.5 fs (anharmonic), against 13.6 fs harmonic. This route includes all anharmonicity automatically, but it is rarely used.

## Quantum theory: the transition polarizability

**Kramers-Heisenberg-Dirac (KHD).** Raman scattering is a second-order process: one photon annihilated, one created, through intermediate states $|n\rangle$. Its amplitude is

$$
[\alpha_{\alpha\beta}]_{f0} = \sum_n\left[\frac{\langle f|\hat\mu_\alpha|n\rangle\langle n|\hat\mu_\beta|0\rangle}{\omega_{n0}-\omega-i\gamma_n} + \frac{\langle f|\hat\mu_\beta|n\rangle\langle n|\hat\mu_\alpha|0\rangle}{\omega_{n0}+\omega'+i\gamma_n}\right],\qquad \omega' = \omega - \omega_{f0}.
\label{khd}
$$

**Relation to two-photon absorption.** Without damping this has the same form as the two-photon matrix element of [[residue-analysis-of-response-functions]], i.e. a single residue of a quadratic response function. There are two differences:

- **Frequencies.** In Raman $\omega\gg\omega_{f0}$, while in two-photon absorption $\omega = \omega_{f0}/2$.
- **Intensity dependence.** In Raman one photon is created, so the scattered intensity $\propto|[\alpha]_{f0}\cdot\mathbf F|^2$ is *linear* in the incident intensity. Two-photon absorption is quadratic.

Standard electronic response theory is ill suited to vibrational Raman directly, because $|f\rangle$ is a vibronic state.

## Normal (nonresonant) Raman: Placzek's theory

**Three approximations.** For $\omega$ well between vibrational and electronic frequencies:

1. **Drop the damping.** Lifetimes (ps) are long compared with optical periods.
2. **Electronic intermediates only.** The intermediate states $|n\rangle$ in the electronic ground state contribute little, since the vibrational polarizability is small at optical frequencies.
3. **Vertical denominators.** In the electronically excited intermediates, $\omega_{n0}$ is replaced by the vertical electronic excitation energy, independent of the vibrational level.

**Result.** The sum over intermediate vibrational levels then closes by completeness:

$$
[\alpha_{\alpha\beta}]_{f0} = \langle f|\alpha^{\rm e}_{\alpha\beta}(\omega;\mathbf Q)|0\rangle.
\label{placzek}
$$

**Harmonic form.** Expanding $\alpha^{\rm e}$ to first order in $\mathbf Q$ and using harmonic states, only fundamentals survive:

$$
[\alpha_{\alpha\beta}]_{1_a0} = \sqrt{\frac{\hbar}{2\omega_a}}\left(\frac{\partial\alpha^{\rm e}_{\alpha\beta}}{\partial Q_a}\right)_0.
\label{deriv}
$$

**Consequences.**

- A mode is **Raman active** if the polarizability changes along it, i.e. $Q_a$ transforms like a quadratic function ($x^2$, $xy$, …). This holds for the stretch of any homonuclear diatomic, which is IR inactive.
- In centrosymmetric molecules no mode is both IR and Raman active (mutual exclusion; [[infrared-intensities]]).
- The polarizability derivative is again a mixed derivative, $-\partial^3E/\partial F\partial F\partial Q$. By the $2n+1$ rule it needs only the field response for SCF.
- Electron correlation affects polarizabilities much less than hyperpolarizabilities, so normal Raman spectra are comparatively easy to compute.
- **Measured intensities.** For freely rotating molecules they combine the rotational invariants of $\partial\boldsymbol\alpha/\partial Q_a$: the mean $\bar\alpha'$ and the anisotropy $\gamma'$. The commonly printed "Raman activity" is $45\bar\alpha'^2 + 7\gamma'^2$ (general knowledge; NRS do not give it).

**Limitations.** Low-frequency torsions and environment effects are poorly described by an expansion about one minimum; configurational averaging is then used.

## Resonance Raman

**What changes.** When $\omega$ approaches an electronic absorption band $K$, one electronic state dominates and Placzek's third approximation fails. The vibrational levels $|k\rangle$ of state $K$ appear explicitly. Scattering becomes orders of magnitude stronger, and overtones become as strong as fundamentals.

**Approximations in order.** Keep only the resonant term of Eq. [[#khd]] and only band $K$, which is accurate.

- **Franck-Condon (FC).** Take the transition dipole $\mu_{0K}(\mathbf Q)$ as constant:

$$
[\alpha_{\alpha\beta}]_{f0} = (\mu^{0K}_\alpha)_0(\mu^{K0}_\beta)_0\sum_k\frac{\langle f|k\rangle\langle k|0\rangle}{\omega_{Kk,00}-\omega-i\gamma}.
\label{fc}
$$

- **Herzberg-Teller (HT).** Take $\mu_{0K}$ linear in $\mathbf Q$.
- **IMDHO.** In the independent-mode displaced harmonic oscillator model, the excited surface is the ground-state one shifted along each mode. The shift is set by the excited-state gradient at the ground-state geometry, and the Franck-Condon overlaps factorize mode by mode.
- **Short-time approximation.** If the damping $\gamma$ exceeds the vibrational spacing (lifetimes of ~10 fs), the vibrational structure in the denominator can be replaced by the vertical energy. Completeness then gives Eq. [[#placzek]] again, but with the **complex, damped** polarizability ([[damped-response-and-absorption-cross-sections]]). Its derivative along $Q_a$ gives the resonance Raman amplitude without any excited-state calculation, implicitly including all electronic states.
- **Time-dependent form.** Writing the FC denominator as a time integral turns the sum over $k$ into the overlap of $\langle f|$ with a wave packet propagated on the excited surface: $[\alpha]_{f0}\propto i\int_0^\infty\langle f|0(t)\rangle e^{-i(\Delta E_{\rm ad}-E_0-\omega)t-\gamma t}dt$.

**NRS's ethylene model (C-C stretch only, B3LYP/t-aug-cc-pVTZ; described, not recomputed).** The π→π* band has its maximum in the $k = 3$ vibronic level (7.165 eV) against a vertical 7.372 eV. With 0.1 ps lifetimes, the full KHD fundamental is $|[\alpha_{zz}]_{01}| = 154.9$ a.u., about two orders above nonresonant values. Dropping the nonresonant term changes it to 155.3, and keeping only $k = 2,3,4$ gives 137.1. Herzberg-Teller overestimates (184.1), Franck-Condon underestimates (125.9), and IMDHO gives 166.9. With 10 fs lifetimes, the complex-polarizability (short-time) profile peaks at 33.3 a.u. at the vertical energy, against 35.1 a.u. for KHD.

## Worked example

!!! example "N₂, B3LYP: polarizability derivative and transition polarizabilities (NRS Table 8.12; recomputed for this note)"
    Potential from B3LYP/cc-pVTZ. Isotropic $\bar\alpha(\omega)$ at $\omega = 2\pi\times10^{15}$ s⁻¹ ($0.15198\,E_h$, 4.136 eV) from full TDDFT B3LYP/aug-cc-pVTZ diagonalization. NRS used t-aug-cc-pVTZ, which is not in PySCF's basis library.

    - **Harmonic.** $R_e = 1.0914$ Å, $\omega_e = 2450.1$ cm⁻¹ (NRS 2450). $\bar\alpha(\omega) = 12.693$, $\partial\bar\alpha/\partial R = 7.057$ a.u. per bohr, $\partial\bar\alpha/\partial Q = 62.5\times10^{-3}$ a.u. (NRS $64.8\times10^{-3}$). Hence $[\bar\alpha]_{10} = 0.4180$ by Eq. [[#deriv]] (NRS 0.4338).
    - **Anharmonic 1D.** The potential and $\bar\alpha(R)$ on 17 points, splined, with vibrational states from a 3000-point finite-difference grid (the Numerov idea of [[numerov-method]]). Levels from the potential minimum: 1222.1, 3647.5, 6051.1, 8441.5 cm⁻¹ (NRS 3649.2, 6049.6, 8425.6 for $f = 1$-$3$); fundamental 2425.4 cm⁻¹.

    | $f$ | $[\bar\alpha]_{f0}$ this note | NRS |
    |---:|---:|---:|
    | 1 | +0.4212 | 0.4335 |
    | 2 | −0.0129 | −0.0128 |
    | 3 | +0.0007 | 0.0005 |
    | 4 | −0.0002 | 0.0000 |

    - **Overtone.** The overtone is nonzero only through anharmonicity and is 3% of the fundamental, matching NRS. In the harmonic approximation it vanishes.
    - **Remaining difference.** The 3-4% difference in the fundamental tracks the different $\partial\bar\alpha/\partial Q$ (basis set).

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 8.7.3.1, Eqs. (8.248)–(8.249), Figs. 8.39–8.41 (described); Sec. 8.7.3.2, Eqs. (8.250)–(8.258), Tables 8.12–8.13, Figs. 8.42–8.46 (described). The Raman-activity combination $45\bar\alpha'^2+7\gamma'^2$ is general knowledge and not from NRS (to verify against a Raman text before relying on its normalization). The calculations are in `Claude outputs/part4_response_batchB1.py`, section C.
