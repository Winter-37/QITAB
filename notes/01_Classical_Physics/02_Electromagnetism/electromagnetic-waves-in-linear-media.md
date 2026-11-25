---
id: electromagnetic-waves-in-linear-media
title: Electromagnetic waves in linear media - refractive index, phase and group velocity, complex permittivity and attenuation, the Beer-Lambert law and absorption cross sections
summary: In a linear medium with frequency-dependent ε and μ, plane waves obey k² = (ω²/c²)μ_rε_r. The refractive index n² = μ_rε_r gives the phase velocity c/n, and dispersion separates the group velocity from it. A complex permittivity ε₁ + iε₂ makes the wave vector complex, k + iκ, with k and κ given by ε₁ and |ε_r|. The intensity then decays as e^{−2κl}, which is the Beer–Lambert law, with absorption coefficient 2κ = 𝒩σ and molar decadic absorption coefficient ε = N_Aσ/ln 10. Energy flow generalizes to S = E × B/μ. Computed: microwave penetration depths of water from the Debye model (0.46 mm at the 20 GHz loss peak, 2 cm at the 2.45 GHz oven frequency), and the plasma frequency of water.
status: in-progress
kind: theory
level: intermediate
tags: [refractive-index, complex-permittivity, absorption-coefficient, beer-lambert, absorption-cross-section, molar-absorption-coefficient, penetration-depth, phase-velocity, group-velocity, attenuation]
prerequisites: [maxwell-equations-in-matter, electromagnetic-waves-and-polarization]
related: [kramers-kronig-debye-and-lorentz-models, local-field-clausius-mossotti-and-reaction-field, damped-response-and-absorption-cross-sections, electronic-absorption-and-emission, multiphoton-absorption]
conventions: [si-units]
key: kkappa
order: 90
date: 2026-11-25
---

SI units. The fields are Fourier components at angular frequency $\omega$, with the time factor $e^{-i\omega t}$, so absorption corresponds to $\varepsilon_2 > 0$. $\varepsilon_r = \varepsilon_1 + i\varepsilon_2$ and $\mu_r$ are relative to vacuum. $\mathcal N$ is the number density of absorbers and $c_{\rm mol}$ their molar concentration.

## Waves in a linear medium

**The wave equations.** With $\mathbf D(\omega) = \varepsilon(\omega)\mathbf E(\omega)$ and $\mathbf B(\omega) = \mu(\omega)\mathbf H(\omega)$, the macroscopic equations of [[maxwell-equations-in-matter]] give, without free sources (NRS Eqs. 3.390–3.394),

$$
\Big[\nabla^2 + \frac{\omega^2}{c^2}\mu_r(\omega)\varepsilon_r(\omega)\Big]\mathbf E(\mathbf r,\omega) = \mathbf 0\quad\Rightarrow\quad k^2(\omega) = \frac{\omega^2}{c^2}\mu_r\varepsilon_r,\qquad n^2(\omega) = \mu_r(\omega)\varepsilon_r(\omega).
$$

**Velocities.** Each frequency component travels at the phase velocity $v_p = c/n(\omega)$. A wave packet centred at $\bar\omega$ moves with the group velocity $v_g = (\partial k/\partial\omega)^{-1}_{\bar\omega}$ (NRS Eqs. 3.395–3.397). Information travels at the signal velocity, which is bounded by $c$. Phase velocities, and in special media group velocities, can exceed $c$ without violating relativity: in the X-ray region $n < 1$.

**Energy flow.** Poynting's theorem generalizes, and for simple linear media the energy density is $\tfrac12(\varepsilon E^2 + B^2/\mu)$ and the flux is (NRS Eqs. 3.398–3.402)

$$
\mathbf S = \frac1\mu\mathbf E\times\mathbf B .
$$

## Complex permittivity and attenuation

**Complex wave vector.** For a nonmagnetic medium with $\varepsilon_r = \varepsilon_1 + i\varepsilon_2$ the wave vector is complex, $\tilde k = k + i\kappa$. The wave oscillates as $e^{i\mathbf k\cdot\mathbf r}$ and decays as $e^{-\boldsymbol\kappa\cdot\mathbf r}$. From $\tilde k^2 = \omega^2\varepsilon_r/c^2$ (NRS Eqs. 3.403–3.405):

$$
k^2 - \kappa^2 = \frac{\omega^2}{c^2}\varepsilon_1,\quad 2k\kappa = \frac{\omega^2}{c^2}\varepsilon_2
\quad\Rightarrow\quad
k = \frac\omega c\sqrt{\tfrac12(|\varepsilon_r| + \varepsilon_1)},\qquad \kappa = \frac\omega c\sqrt{\tfrac12(|\varepsilon_r| - \varepsilon_1)}.
\label{kkappa}
$$

The real refractive index is $n = ck/\omega$, and $c\kappa/\omega$ is the extinction coefficient.

**The Beer–Lambert law.** The intensity $\langle S\rangle_T = \frac{1}{2\mu}\mathrm{Re}(\mathbf E\times\mathbf B^*)$ falls as $I(l) = I_0e^{-2\kappa l}$ (NRS Eqs. 3.406–3.412):

$$
-\ln\frac{I}{I_0} = \alpha l,\qquad \alpha = 2\kappa = \mathcal N\sigma,\qquad
A = -\log_{10}\frac{I}{I_0} = \epsilon\,c_{\rm mol}\,l,\qquad \epsilon = \frac{N_A\sigma}{\ln10} = \frac{\alpha}{c_{\rm mol}\ln10}.
$$

Here $\alpha$ is the absorption coefficient (not a polarizability), $A$ the absorbance and $\epsilon$ the molar decadic absorption coefficient. In practical units, $\epsilon\,[\mathrm{M^{-1}cm^{-1}}] = 2.615\times10^{20}\,\sigma\,[\mathrm{cm^2}]$.

**The cross section $\sigma$.** It is the molecular quantity that theory computes ([[electronic-absorption-and-emission]], [[damped-response-and-absorption-cross-sections]]). Two pictures:

- **Projectiles.** A slab of thickness $dl$ removes the fraction $\mathcal N\sigma\,dl$ of a photon flux, which integrates to the exponential law (NRS Fig. 3.21).
- **A tube.** The transmittance is the probability that no molecule lies in a tube of cross section $\sigma$ along the path, $(1 - \sigma l/V)^N\to e^{-\mathcal N\sigma l}$ (NRS Eqs. 3.413–3.414).

**Loss and absorption.** $\varepsilon_2$ measures energy loss, but it is not itself an absorption spectrum. The measured absorption coefficient $2\kappa$ depends on both $\varepsilon_1$ and $\varepsilon_2$ through Eq. [[#kkappa]]. For water it rises through the microwave region to $1.2\times10^6$ m⁻¹ near 100 THz (vibrations). It is nearly zero in the visible, which is why water is transparent, and largest near the plasma frequency in the UV (NRS Fig. 3.27).

## Worked example

!!! example "Water from microwaves to the far UV (computed for this note)"
    **Microwave penetration.** The Debye model of [[kramers-kronig-debye-and-lorentz-models]] with NRS's parameters for water at 25 °C: $\varepsilon_s = 78.3$, $\varepsilon_\infty = 6.0$, loss peak at $10^{10.3}$ Hz, so $\tau = 7.98$ ps. Through Eq. [[#kkappa]]:

    | frequency | $\varepsilon_r$ | $n$ | $\alpha = 2\kappa$ (m⁻¹) | penetration depth $1/\alpha$ |
    |---|---|---:|---:|---:|
    | 2.45 GHz (microwave oven) | 77.23 + 8.75 i | 8.80 | 51.0 | 19.6 mm |
    | 19.95 GHz (loss peak) | 42.15 + 36.15 i | 6.99 | 2163 | 0.46 mm |

    These match the values quoted by NRS (about 2 cm and 0.5 mm). An oven works below the loss peak deliberately, so that the energy is deposited throughout the food rather than in a thin surface layer.

    **Plasma frequency.** With 10 electrons per molecule and $\mathcal N = 3.334\times10^{28}$ m⁻³, $\omega_p^2 = e^2N_e/m_e\varepsilon_0 = 1.061\times10^{33}$ rad² s⁻², so $\nu_p = 5.18\times10^{15}$ Hz. This is in the extreme UV, as NRS state. Beyond it $1 - \varepsilon_1$ falls as $\omega_p^2/\omega^2$.

    **Unit conversion.** $N_A/(\ln10\times1000\ \mathrm{cm^3\,L^{-1}}) = 2.615\times10^{20}$, so a cross section of $10^{-17}$ cm² corresponds to $\epsilon = 2615$ M⁻¹ cm⁻¹.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 3.5.3, Eqs. (3.390)–(3.414), Fig. 3.21 (described); Sec. 3.5.4.4, Figs. 3.27–3.28 (described). The unit factor 2.615 × 10²⁰ and the remark on oven frequencies are general knowledge, not from NRS. The calculations are in `Claude outputs/part1_fields_batchD.py`, section G.
