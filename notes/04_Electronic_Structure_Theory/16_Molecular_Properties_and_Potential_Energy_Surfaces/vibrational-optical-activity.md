---
id: vibrational-optical-activity
title: Vibrational optical activity - VCD rotational strengths from atomic polar and axial tensors, and Raman optical activity invariants and scattering geometries
summary: Vibrational circular dichroism is ECD of infrared transitions. Its rotational strength needs the vibrational magnetic transition moment, which vanishes in the Born–Oppenheimer approximation and must be obtained from the first nonadiabatic correction (Stephens' atomic axial tensor), the frequency derivative of a magnetic-field/nuclear-displacement response function. Raman optical activity is the small difference in Raman scattering of right and left circularly polarized light. It is governed by three invariants built from normal-coordinate derivatives of α, G′ and the dipole–quadrupole polarizability A, whose weights depend on the scattering angle. Checked here: the angular formula against the forward, backward and right-angle expressions of NRS Table 8.14.
status: in-progress
kind: theory
level: advanced
tags: [vcd, vibrational-circular-dichroism, roa, raman-optical-activity, atomic-axial-tensor, atomic-polar-tensor, stephens, rotational-strength, absolute-configuration, circular-intensity-difference]
prerequisites: [optical-activity-ecd-and-mcd, infrared-intensities, raman-scattering]
related: [magnetizability-and-gauge-origin, harmonic-vibrational-analysis, born-oppenheimer-approximation, linear-response-for-variational-wave-functions]
conventions: [atomic-units]
key: vcd-r
order: 150
date: 2026-11-24
---

Atomic units unless stated. $Q_a$ is a mass-weighted normal coordinate with harmonic frequency $\omega_a$, $\dot Q_a$ its velocity (conjugate momentum). $|0\rangle$ and $|1_a\rangle$ are the vibrational ground and first excited states of mode $a$, $L_{N\beta,a} = \partial R_{N\beta}/\partial Q_a$ the normal-mode vectors. $\hat{\boldsymbol\mu}$ and $\hat{\mathbf m}$ are the full (electronic plus nuclear) electric and magnetic dipole operators. Notation for $\alpha$, $G'$ and the rotatory strength follows [[optical-activity-ecd-and-mcd]].

## Why vibrational optical activity

**Advantages over ECD.** ECD needs a chromophore, and a few broad bands carry its information. Infrared and Raman spectra have one band per normal mode, all localized in the molecule, so vibrational optical activity gives many independent signed checks of absolute configuration and conformation. VCD and ROA of the same molecule carry similar information (NRS Figs. 8.38 and 8.48 for (S)-methyloxirane).

**The price is small signals.**

- **VCD.** $\Delta\epsilon/\epsilon\sim10^{-4}$–$10^{-5}$.
- **ROA.** The circular intensity difference $\Delta_{\rm CID} = (I_R - I_L)/(I_R + I_L)\sim10^{-3}$–$10^{-4}$ (NRS Eq. 8.266). Its size is the ratio of the magnetic and quadrupolar couplings of the light wave to its electric coupling, of order $\alpha\times$ (molecular size / wavelength).

## VCD rotational strength

**Rotational strength.** For a fundamental $0\to1_a$ (NRS Eq. 8.239):

$$
R_a = \mathrm{Im}\big[\langle0|\hat{\boldsymbol\mu}|1_a\rangle\cdot\langle1_a|\hat{\mathbf m}|0\rangle\big].
$$

**Electric moment.** In the double-harmonic approximation (linear dipole, harmonic oscillator), $\langle0|\hat{\boldsymbol\mu}|1_a\rangle = (\hbar/2\omega_a)^{1/2}\,\partial\boldsymbol\mu/\partial Q_a$, with the atomic polar tensor of [[infrared-intensities]] (NRS Eq. 8.241):

$$
P_{N,\alpha\beta} = \frac{\partial\mu_\alpha}{\partial R_{N\beta}} = Z_N\delta_{\alpha\beta} + \langle\langle\hat\mu^e_\alpha;\partial\hat H/\partial R_{N\beta}\rangle\rangle_0 .
$$

**Magnetic moment.** The magnetic moment of a molecule in a real, nondegenerate electronic ground state is zero for every fixed nuclear geometry: the electronic contribution $\langle\psi_0|\hat{\mathbf L}|\psi_0\rangle$ vanishes for a real wave function. The magnetic moment is nonzero only because the nuclei move:

- **Nuclear part.** The nuclei themselves carry a current. For nucleus $N$ moving with velocity $\dot{\mathbf R}_N$ the moment is $\tfrac12Z_N\mathbf R_N\times\dot{\mathbf R}_N$, linear in velocity.
- **Electronic part.** The electrons, dragged along non-adiabatically, acquire a current. This appears only in the first-order correction to the Born–Oppenheimer wave function from the nuclear kinetic-energy coupling (NRS Eq. 8.242).

**Stephens' form.** Both contributions are linear in the nuclear velocities, $\mathbf m = \sum_{N}\mathbf M_N\cdot\dot{\mathbf R}_N$, with the atomic axial tensor (AAT)

$$
M_{N,\alpha\beta} = \underbrace{\tfrac{i}{4}\epsilon_{\alpha\beta\gamma}Z_NR_{N\gamma}}_{\text{nuclear}}\;\underbrace{-\;\sum_K{}'\frac{\langle0|\partial\hat H_{\rm OZ}/\partial B_\alpha|K\rangle\langle K|\partial\hat H/\partial R_{N\beta}|0\rangle}{\omega_{K0}^2}}_{\text{electronic}}
= \tfrac{i}{4}\epsilon_{\alpha\beta\gamma}Z_NR_{N\gamma} - \tfrac12\frac{d}{d\omega}\Big\langle\Big\langle\frac{\partial\hat H}{\partial B_\beta};\frac{\partial\hat H}{\partial R_{N\alpha}}\Big\rangle\Big\rangle_\omega\Big|_{\omega=0}
\label{aat}
$$

(NRS Eqs. 8.243–8.245; index placement and the factor $i$ as printed there). The factor $1/\omega_{K0}^2$, rather than $1/\omega_{K0}$, is the signature of the nonadiabatic origin. It is also why the AAT is a frequency derivative of a linear response function at zero frequency, equivalently Stephens' overlap $\langle\partial\psi_0/\partial R_{N\beta}|\partial\psi_0/\partial B_\alpha\rangle$ of two perturbed wave functions.

**Combining the moments.** With $\langle1_a|\dot Q_a|0\rangle = i(\hbar\omega_a/2)^{1/2}$:

$$
R_a = \frac{\hbar}{2}\Big(\sum_{N\beta}P_{N,\alpha\beta}L_{N\beta,a}\Big)\Big(\sum_{N'\gamma}\mathrm{Im}M_{N',\alpha\gamma}L_{N'\gamma,a}\Big)
\;\equiv\;\frac{\hbar}{2\omega_a}\,\mathrm{Im}\Big[\frac{\partial\mu_\alpha}{\partial Q_a}\frac{\partial m_\alpha}{\partial Q_a}\Big],
\label{vcd-r}
$$

where the second form is NRS Eq. (8.240), with $\partial m/\partial Q_a$ standing for $i\omega_a$ times the velocity derivative. The two forms are the same quantity (my reconciliation of the notations).

**Origin dependence.** Both the nuclear and electronic AATs depend on the origin. Their sum gives origin-independent $R_a$ for exact states and, with London orbitals or distributed origins, for approximate ones.

**Geometric picture.** $R_a = |\boldsymbol\mu^a_{01}||\mathbf m^a_{10}|\cos\theta_a$ (NRS Eq. 8.246).

- **Achiral molecules.** $\cos\theta_a = 0$ for every mode.
- **Enantiomers.** They have $\theta^R_a = 180^\circ - \theta^S_a$ (NRS Eq. 8.247).
- **Robust signs.** A mode whose $\theta_a$ lies near $90^\circ$ has a sign that is not robust: small errors in either moment can flip it. Robustness analyses discard such modes before assigning a configuration.
- **Frequencies.** Harmonic frequencies are typically a few percent too high and can reorder close modes (NRS Table 8.11 for water). Assignments compare band patterns, often after scaling.

## Raman optical activity

**The ROA difference intensity.** Raman scattering (KHD, Placzek; see [[raman-scattering]]) involves $\partial\alpha/\partial Q_a$. ROA adds interference with the magnetic dipole and electric quadrupole parts of the scattering, through $\partial G'/\partial Q_a$ and $\partial A/\partial Q_a$ with $A_{\alpha,\beta\gamma} = \langle\langle\hat\mu_\alpha;\hat\Theta_{\beta\gamma}\rangle\rangle_\omega$ (NRS Eq. 8.265). For scattered circular polarization (SCP) at scattering angle $\phi$ (NRS Eq. 8.259):

$$
I^{\rm SCP}_R - I^{\rm SCP}_L\;\propto\;\big[90aG'_a + 26\beta^2_{G,a} - 2\beta^2_{A,a}\big] + \cos\phi\,\big[180aG'_a - 20\beta^2_{G,a} - 12\beta^2_{A,a}\big] + \cos^2\phi\,\big[90aG'_a + 2\beta^2_{G,a} + 6\beta^2_{A,a}\big],
\label{roa}
$$

with prefactor $\frac{1}{90c}\big(\frac{\omega_s^2\mu_0}{4\pi}\big)^2\frac{\hbar}{2\omega_a}$, where $\omega_s$ is the scattered frequency.

**Invariants** (sums over repeated indices; derivatives with respect to $Q_a$, written $'$; NRS Eqs. 8.260–8.264):

$$
\begin{aligned}
a^2_a &= \tfrac19\,\alpha'_{\alpha\alpha}\alpha'_{\beta\beta}, &
\beta^2_a &= \tfrac12\big(3\alpha'_{\alpha\beta}\alpha'_{\alpha\beta} - \alpha'_{\alpha\alpha}\alpha'_{\beta\beta}\big),\\
aG'_a &= \tfrac19\,\alpha'_{\alpha\alpha}G'^{\,\prime}_{\beta\beta}, &
\beta^2_{G,a} &= \tfrac12\big(3\alpha'_{\alpha\beta}G'^{\,\prime}_{\alpha\beta} - \alpha'_{\alpha\alpha}G'^{\,\prime}_{\beta\beta}\big),\qquad
\beta^2_{A,a} = \tfrac{\omega}{2}\,\alpha'_{\alpha\beta}\,\epsilon_{\alpha\gamma\delta}A'_{\gamma,\delta\beta}.
\end{aligned}
$$

**Features of the formula.**

- **Origin independence.** Each invariant is origin independent for exact states. The origin dependence of $G'$ cancels against that of $A$ within the combinations that appear (NRS Sec. 8.7.4).
- **Backscattering is the workhorse.** At $\phi = 180^\circ$ the isotropic invariant $aG'$ drops out and only the anisotropic invariants remain, $\propto24\beta^2_G + 8\beta^2_A$ (Table 8.14). These are usually large, which maximizes the signal against the polarized background.
- **The quadrupole invariant.** In (S)-methyloxirane backscattering the $\beta^2_A$ invariant contributes up to about 17% of individual bands, with either sign (NRS Table 8.15). It cannot be dropped.
- **The CID.** Comparison with experiment usually uses $\Delta_{\rm CID}$, or band shapes of the difference spectrum, because absolute Raman cross sections are hard to measure.
- **Away from resonance.** Far from electronic resonance, $\alpha$, $G'$ and $A$ are evaluated at the laser frequency $\omega$ by linear response. Their geometric derivatives come from finite differences or analytic geometric derivatives of the response functions.

## Worked example

!!! example "Scattering geometries (checked for this note)"
    Eq. [[#roa]] is linear in $(aG', \beta^2_G, \beta^2_A)$. Its coefficient vectors at the three standard angles, compared with the brackets of NRS Table 8.14 (all with prefactor $2/c$ there):

    | geometry | Eq. (8.259) | Table 8.14 |
    |---|---|---|
    | forward, $\phi = 0$ | $(360, 8, -8)$ | $(180, 4, -4)$ |
    | backward, $\phi = \pi$ | $(0, 48, 16)$ | $(0, 24, 8)$ |
    | right angle, $\phi = \pi/2$ | $(90, 26, -2)$ | polarized $(90, 14, 2)$ + depolarized $(0, 12, -4)$ = $(90, 26, -2)$ |

    **The relation.** The angular formula reproduces the forward and backward brackets up to a common factor 2. At right angles it gives the sum of the polarized and depolarized brackets once.

    **A factor 2 to verify.** Within NRS, the forward/backward rows and the right-angle rows therefore carry a relative factor 2 that the angular formula does not. I have not checked which convention matches Barron's original expressions (to verify). The ratios within each geometry, which determine band signs and relative intensities, are unaffected.

    **Raman analogue.** The same structure appears in the Raman column of Table 8.14: $90a^2 + 14\beta^2$ for the forward, backward and polarized right-angle geometries, and $12\beta^2$ for the depolarized one.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 8.7.2, Eqs. (8.239)–(8.247), Table 8.11, Fig. 8.38 (described); Sec. 8.7.4, Eqs. (8.259)–(8.266), Tables 8.14–8.15, Figs. 8.47–8.48 (described). Stephens' magnetic-field-perturbation formulation, the overlap form of the AAT and the robustness argument are general knowledge, not taken from NRS. The check is in `Claude outputs/part4_response_batchB2.py`, section G.
