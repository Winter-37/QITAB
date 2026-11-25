---
id: pure-vibrational-contributions-and-nuclear-relaxation
title: Pure vibrational polarizabilities and hyperpolarizabilities - the double-harmonic term, anharmonic corrections, and the nuclear-relaxation and curvature picture of a molecule relaxing in a static field
summary: The pure vibrational polarizability is, to leading order, Σ_a (∂μ_α/∂Q_a)(∂μ_β/∂Q_a)/(ω_a² − ω²). It is large for static fields and small and negative at optical frequencies. Anharmonic terms of electrical and mechanical origin follow from vibrational perturbation theory (NRS Tables 6.3–6.4). For static fields there is a more intuitive route: let the geometry relax in the field. The energy at the field-relaxed geometry gives the nuclear-relaxation (hyper)polarizabilities, the double-harmonic terms plus some anharmonic ones. The field dependence of the zero-point energy gives the curvature contributions, which contain the ZPVA and the remaining anharmonic terms. Recomputed: for HF, finite-field nuclear relaxation against the formulas (α_nr to 10⁻⁴, β_nr to 0.05%), and a sign misprint in NRS Eq. 6.95.
status: in-progress
kind: theory
level: advanced
tags: [pure-vibrational, vibrational-polarizability, vibrational-hyperpolarizability, nuclear-relaxation, curvature-contribution, double-harmonic, finite-field, field-induced-geometry, bishop-kirtman]
prerequisites: [electronic-and-nuclear-contributions-to-response, zero-point-vibrational-corrections-to-properties, variational-perturbation-theory-and-the-2n-plus-1-rule, infrared-intensities]
related: [polarizabilities-and-dispersion-coefficients, raman-scattering, dispersion-oscillator-strengths-and-sum-rules, geometry-optimization]
conventions: [atomic-units]
key: alpha-nr
order: 180
date: 2026-11-25
---

Atomic units, notation as in [[zero-point-vibrational-corrections-to-properties]]: normal coordinates $Q_a$, harmonic $\omega_a$, cubic constants $V^{(3)}_{abc}$, and property derivatives at equilibrium written $\mu_{\alpha,a} = \partial\mu_\alpha/\partial Q_a$, $\mu_{\alpha,ab}$, $\alpha_{\alpha\beta,a}$, and so on. Static field $\mathbf F$; the energy expansion is $E(\mathbf F) = E_0 - \mu_\alpha F_\alpha - \tfrac12\alpha_{\alpha\beta}F_\alpha F_\beta - \tfrac16\beta_{\alpha\beta\gamma}F_\alpha F_\beta F_\gamma - \cdots$. The frequency factors of NRS Table 6.3 are $\lambda^{\pm i}_x = (\omega_x^2 - \omega_i^2)^{-1}$.

## Perturbation theory for the pure vibrational part

**The double-harmonic term.** Start from the pure vibrational polarizability $[\mu^2]$ of [[electronic-and-nuclear-contributions-to-response]]. With harmonic vibrational states and a dipole linear in $Q$, only the fundamentals $|1_a\rangle$ contribute, with $\langle0|\mu_\alpha|1_a\rangle = \sqrt{\hbar/2\omega_a}\,\mu_{\alpha,a}$ (NRS Eq. 6.74). The resulting double-harmonic term is

$$
[\mu^2]^{0,0}_{\alpha\beta}(-\omega;\omega) = \sum_a\mu_{\alpha,a}\mu_{\beta,a}\frac{1}{2\omega_a}\Big[\frac{1}{\omega_a - \omega} + \frac{1}{\omega_a + \omega}\Big] = \sum_a\frac{\mu_{\alpha,a}\mu_{\beta,a}}{\omega_a^2 - \omega^2}
\label{dh}
$$

(NRS Eq. 6.75).

**Where it is large and where it is small.**

- **Statically.** Each mode contributes its IR intensity divided by $\omega_a^2$, so low-frequency, IR-bright modes dominate.
- **At optical frequencies.** For $\omega\gg\omega_a$ the term tends to $-\sum_a\mu_{\alpha,a}\mu_{\beta,a}/\omega^2$: small, negative, and isotope dependent through $\mu_{\alpha,a}\propto m^{-1/2}$.

**Anharmonic corrections.** They are classified by their order $n$ in property derivatives beyond the first and $m$ in force constants beyond the harmonic (NRS Table 6.3).

- **$[\mu^2]^{1,0} = 0$.** Both transition moments must reach the same state, and a linear term reaches $|1_a\rangle$ while a quadratic term reaches $|2_a\rangle$ or $|1_a1_b\rangle$.
- **$[\mu^2]^{0,1} = 0$.** The first-order wave function of [[zero-point-vibrational-corrections-to-properties]] has no $|1_a1_b\rangle$ or $|2_a\rangle$ components, and the cross terms vanish (NRS Eqs. 6.79–6.80).
- **Electrical anharmonicity at second order.** It comes from the overtone and combination terms built from $\mu_{\alpha,ab}$, and from $\mu_{\alpha,a}\mu_{\beta,abb}$ (NRS Eq. 6.78):

$$
[\mu^2]^{2,0} = \frac{\hbar}{4}\sum_{a,b}\Big[\mu_{\alpha,ab}\,\mu_{\beta,ab}\Big(\frac1{\omega_a} + \frac1{\omega_b}\Big)\frac{1}{(\omega_a + \omega_b)^2 - \omega^2} + \big(\mu_{\alpha,a}\mu_{\beta,abb} + \mu_{\beta,a}\mu_{\alpha,abb}\big)\frac{1}{\omega_b(\omega_a^2 - \omega^2)}\Big].
$$

The matrix-element identity behind it (NRS Eq. 6.77) should read $\frac{\hbar^2}{4\omega_a\omega_b}(\delta_{ac}\delta_{bd} + \delta_{ad}\delta_{bc})$; the printed $\delta_{ad}\delta_{bd}$ is a typo.

- **The remaining second-order terms.** $[\mu^2]^{1,1}$ and $[\mu^2]^{0,2}$ need cubic and quartic constants (Table 6.3).
- **Hyperpolarizabilities.** Leading orders follow by the substitution rules of NRS Table 6.4. For $\beta$:

$$
[\mu\alpha]^{0,0} = \tfrac12\sum_{-\sigma,1,2}\sum_a\frac{\mu_{\alpha,a}\,\alpha_{\beta\gamma,a}}{\omega_a^2 - \omega_\sigma^2},\qquad [\mu^3]^{0,0} = 0
$$

(NRS Eqs. 6.81–6.82). $[\mu^3]$ first appears at first order in anharmonicity, $[\mu^3]^{1,0}$ and $[\mu^3]^{0,1}$.

**Cost.** The perturbation route works at any frequency, but the algebra grows quickly. Mixed cubic constants $V^{(3)}_{abc}$ and property derivatives up to third order are needed for a complete second-order treatment.

## The nuclear-relaxation picture (static fields)

**Physical picture.** A static field along the dipole of HF pulls charge toward F. The molecule gains more energy by lengthening the bond (larger dipole) than by shortening it, so the bond stretches. The repulsive wall makes the response asymmetric, and an opposing field shortens the bond less than a parallel one stretches it (NRS Fig. 6.9). The extra dipole from this geometry change is the vibrational polarizability, seen as a static, classical effect.

**Three contributions.** Separate (NRS Eqs. 6.83–6.85):

$$
\alpha^{\rm e} = -\frac{d^2E_e(\mathbf R_0,F)}{dF^2},\qquad
\alpha^{\rm nr} = -\frac{d^2[E_e(\mathbf R(F),F) - E_e(\mathbf R_0,F)]}{dF^2},\qquad
\alpha^{\rm curv} = -\frac{d^2E_{\rm zpv}(\mathbf R(F),F)}{dF^2}.
$$

Here $\mathbf R(F)$ minimizes $V(Q,F) = E^0_e(Q) - \mu_\alpha(Q)F_\alpha - \cdots$ at each field.

**Nuclear relaxation.** The geometry is variational, $\partial V/\partial Q_a = 0$ at every field (NRS Eq. 6.87), so the field derivatives follow the variational perturbation theory of [[variational-perturbation-theory-and-the-2n-plus-1-rule]]:

- **First-order response.** The geometry responds to first order as $\partial Q_a/\partial F_\beta = \mu_{\beta,a}/\omega_a^2$ (NRS Eqs. 6.91–6.93).
- **Polarizability.** The total second derivative is

$$
-\frac{d^2V}{dF_\alpha dF_\beta} = \alpha^{\rm e}_{\alpha\beta} + \sum_a\frac{\mu_{\alpha,a}\mu_{\beta,a}}{\omega_a^2} = \alpha^{\rm e}_{\alpha\beta} + [\mu^2]^{0,0}_{\alpha\beta}(0;0)\;\Rightarrow\;\alpha^{\rm nr} = [\mu^2]^{0,0}(0;0).
\label{alpha-nr}
$$

- **First hyperpolarizability.** By the $2n+1$ rule, the third derivative needs only $\partial Q/\partial F$. Writing it out for one mode makes the sign of the cubic term explicit:

$$
-\frac{d^3V}{dF^3} = \beta^{\rm e} + 3\alpha_{,a}\frac{\mu_{,a}}{\omega_a^2} + 3\mu_{,aa}\frac{\mu_{,a}^2}{\omega_a^4} - V^{(3)}_{aaa}\frac{\mu_{,a}^3}{\omega_a^6},
$$

and in general (NRS Eq. 6.95)

$$
\beta^{\rm nr} = [\mu\alpha]^{0,0} + [\mu^3]^{1,0} + [\mu^3]^{0,1}\quad(\text{static}).
\label{beta-nr}
$$

**A sign misprint in NRS Eq. 6.95.** The cubic-force-constant term enters $-d^3V/dF^3$ with a minus sign: $-\sum V^{(3)}_{abc}(\partial Q_a/\partial F)(\partial Q_b/\partial F)(\partial Q_c/\partial F)$, because $\partial^3V/\partial Q^3 = +V^{(3)}$. This agrees with the $[\mu^3]^{0,1}$ entry of NRS Table 6.3, which carries $-\tfrac16$. Eq. 6.95 prints the term with a plus sign. The finite-field calculation below settles it.

**Second hyperpolarizability.** $\gamma^{\rm nr} = [\alpha^2]^{0,0} + [\mu\beta]^{0,0} + [\mu^2\alpha]^{0,1} + [\mu^2\alpha]^{1,0} + [\mu^4]^{2,0} + [\mu^4]^{0,2} + [\mu^4]^{1,1}$ (NRS Eq. 6.96).

**Mass independence.** The nuclear-relaxation terms do not depend on the nuclear masses: they are properties of the potential surface. Isotope effects enter only through the curvature terms.

**Curvature terms.** The zero-point energy $E_{\rm zpv} = \tfrac{\hbar}{2}\sum_a\omega_a(\mathbf R(F),F)$ also depends on the field (NRS Eqs. 6.97–6.105):

$$
\mu^{\rm curv} = -\frac{dE_{\rm zpv}}{dF} = \Delta\mu^{\rm zpva},\qquad
\alpha^{\rm curv} = \Delta\alpha^{\rm zpva} + [\mu^2]^{2,0} + [\mu^2]^{1,1} + [\mu^2]^{0,2},
$$

$$
\beta^{\rm curv} = \Delta\beta^{\rm zpva} + [\mu\alpha]^{2,0} + [\mu\alpha]^{1,1} + [\mu\alpha]^{0,2} + [\mu^3]^{3,0} + [\mu^3]^{2,1} + [\mu^3]^{1,2} + [\mu^3]^{0,3}.
$$

$E_{\rm zpv}$ is not variational in $Q$, so its second field derivative needs the second-order geometry response $\partial^2Q/\partial F^2$ (NRS Eqs. 6.101–6.102). The nuclear-relaxation part plus the curvature part reproduce the static pure vibrational and ZPVA contributions through the orders listed.

**Which route.** The relaxation picture is intuitive and easy to compute by finite fields. It applies only to static fields. The perturbation route works for dynamic fields (dc-Kerr, EFISHG, intensity-dependent refractive index) but needs the long expressions of Tables 6.3–6.4.

## Worked example

!!! example "HF in a static field (recomputed for this note)"
    **Setup.** HF/aug-cc-pVTZ $E(r,F_z)$ as in [[electronic-and-nuclear-contributions-to-response]]. For each field a degree-8 polynomial in $r$ (within ±0.45 bohr of $r_e$) gives the relaxed bond length, the relaxed energy and the field-dependent harmonic frequency. Field derivatives come from five-point differences with $h = 0.0025$ au. Derivatives in mass-weighted $Q$ use the reduced mass of each isotopologue. All values in au, zz components.

    | | ¹H¹⁹F | ²H¹⁹F |
    |---|---:|---:|
    | $\alpha^{\rm e}$ | 5.5329 | 5.5329 |
    | $\alpha^{\rm nr}$, finite field | 0.22445 | 0.22445 |
    | $\mu_{,a}^2/\omega_a^2$, Eq. [[#alpha-nr]] | 0.22443 | 0.22443 |
    | $\alpha^{\rm curv}$, finite field | 0.2020 | 0.1465 |
    | $\alpha^{\rm e} + \alpha^{\rm nr} + \alpha^{\rm curv}$ | 5.9594 | 5.9038 |
    | exact vibronic $-\partial^2E_{\rm vib,0}/\partial F^2$ | 5.9661 | 5.9073 |
    | $\alpha^{\rm v}(0;0)$ exact sum over states / double harmonic | 0.2420 / 0.2244 | 0.2371 / 0.2244 |
    | $\alpha^{\rm v}$ at 589 nm, exact / double harmonic | −0.0169 / −0.0167 | −0.0085 / −0.0085 |
    | $\beta^{\rm e}$ | −8.711 | −8.711 |
    | $\beta^{\rm nr}$, finite field | 9.315 | 9.315 |
    | Eq. [[#beta-nr]] with $-V^{(3)}$ | 9.311 | 9.311 |
    | same with $+V^{(3)}$ (as printed in NRS Eq. 6.95) | 8.359 | 8.359 |
    | $\beta^{\rm curv}$, finite field | 0.060 | 0.043 |
    | $\beta^{\rm e} + \beta^{\rm nr} + \beta^{\rm curv}$ against exact vibronic | 0.663 / 0.673 | 0.647 / 0.652 |

    **What the table shows.**

    - **Nuclear relaxation.** It matches the double-harmonic formula to $10^{-4}$ and is the same for both isotopologues.
    - **Curvature.** It carries the isotope effect, and agrees with $\Delta\alpha^{\rm zpva}$ plus the anharmonic part of the exact $\alpha^{\rm v}$ ($0.185 + 0.018 = 0.203$ for HF).
    - **The cubic sign.** The finite-field $\beta^{\rm nr}$ agrees with the formula only with the minus sign on the cubic term.
    - **Near cancellation.** For $\beta$ the nuclear relaxation (+9.3 au) almost cancels the electronic value (−8.7 au), so the static $\beta_{zzz}$ of HF is dominated by vibrational effects even in sign.
    - **Field-induced bond stretch.** $dr_e/dF = \mu_{,a}/(\omega_a^2\sqrt{m_{\rm red}}) = 0.557$ bohr per au of field. A field of $10^{-3}$ au (5.1 × 10⁸ V m⁻¹) along the dipole lengthens the bond by about $5.6\times10^{-4}$ bohr.
    - **Optical frequencies.** At 589 nm the vibrational part is negative, isotope dependent and only 0.3% of $\alpha^{\rm e}$.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 6.6.1, Eqs. (6.74)–(6.82), Tables 6.3–6.4; Sec. 6.6.2, Eqs. (6.83)–(6.105), Fig. 6.9 (described). The calculations are in `Claude outputs/part4_response_batchC.py`, section A.
