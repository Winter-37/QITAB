---
id: kramers-kronig-debye-and-lorentz-models
title: Frequency dependence of the permittivity - causality and the Kramers-Kronig relations, Debye relaxation, Lorentz oscillators, the plasma limit, and the permittivity of water across the spectrum
summary: Because polarization cannot precede the field, the response function vanishes for t ≤ 0. Its even and odd parts are then tied by the sign function, which makes the real and imaginary parts of ε_r(ω) Hilbert transforms of each other (Kramers–Kronig). Two models cover the spectrum of a liquid like water. Debye relaxation (an overdamped response of rotating dipoles) gives ε₁ falling from ε_s to ε_∞ and a loss peak ε₂ = (ε_s − ε_∞)/2 at ωτ = 1. Lorentz damped oscillators (vibrations, electronic transitions) give dispersive ε₁ and Lorentzian ε₂ around each resonance and, far above all resonances, ε₁ → 1 − ω_p²/ω². Checked numerically: Kramers–Kronig reconstructs ε₁ of Lorentz and Debye models from ε₂, the Debye peak height for water (36.15 against NRS's 36.1), and the plasma sum rule.
status: in-progress
kind: theory
level: intermediate
tags: [kramers-kronig, causality, hilbert-transform, debye-relaxation, lorentz-oscillator, plasma-frequency, permittivity-of-water, dielectric-loss, lineshape, cauchy-distribution]
prerequisites: [electromagnetic-waves-in-linear-media]
related: [local-field-clausius-mossotti-and-reaction-field, damped-response-and-absorption-cross-sections, dispersion-oscillator-strengths-and-sum-rules, exact-state-response-functions]
conventions: [si-units]
key: kk
order: 100
date: 2026-11-25
---

SI units. Time dependence $e^{-i\omega t}$, so $\varepsilon_r(\omega) = \varepsilon_1 + i\varepsilon_2$ with $\varepsilon_2 > 0$ for loss. $P$ denotes the Cauchy principal value. Fourier conventions follow NRS Appendix D.

## Causality and Kramers–Kronig

**The response function.** For a linear medium $P(\omega) = \varepsilon_0[\varepsilon_r(\omega) - 1]E(\omega)$, so in time the polarization is a convolution of the field with a response function (NRS Eqs. 3.415–3.418):

$$
P(t) = \frac{\varepsilon_0}{2\pi}\int E(t')G(t - t')\,dt',\qquad G(t) = \int[\varepsilon_r(\omega) - 1]e^{-i\omega t}d\omega .
$$

**Causality.** The polarization cannot respond before the field, so $G(t) = 0$ for $t\le0$. Split $G$ into even and odd parts. Then $\varepsilon_1 - 1$ is the cosine transform of $G_{\rm even}$, and $\varepsilon_2$ the sine transform of $G_{\rm odd}$ (NRS Eqs. 3.419–3.422). Causality links the two parts: $G_{\rm odd}(t) = \mathrm{sgn}(t)G_{\rm even}(t)$ (NRS Eq. 3.423).

**The relations.** A product in time is a convolution in frequency, and the transform of $\mathrm{sgn}$ is a principal-value $1/\omega$. This gives the Kramers–Kronig relations (NRS Eqs. 3.424–3.426):

$$
\varepsilon_1(\omega) = 1 - \frac1\pi P\!\int_{-\infty}^{\infty}\frac{\varepsilon_2(\omega')}{\omega - \omega'}d\omega',\qquad
\varepsilon_2(\omega) = \frac1\pi P\!\int_{-\infty}^{\infty}\frac{\varepsilon_1(\omega') - 1}{\omega - \omega'}d\omega' .
\label{kk}
$$

**Uses.** The relations check measured data. They also give refractive indices from absorption spectra and vice versa. Their molecular counterpart is that the real and imaginary parts of a damped response function are not independent ([[damped-response-and-absorption-cross-sections]]).

**What water looks like.** Measured $\varepsilon_r$ of liquid water at 25 °C over 15 decades (NRS Fig. 3.22): $\varepsilon_1$ falls from about 80 through the microwave region, wiggles from the infrared to the UV, and tends to 1 in the X-ray region. $\varepsilon_2$ has a large microwave maximum at the inflection point of $\varepsilon_1$, plus structure at higher frequencies.

## Debye relaxation

**The relaxation function.** A static field switched on at $t_0$ builds the polarization with a delay, $P(t) = a(t - t_0)E_0$ with $a(t) = a_0(1 - e^{-t/\tau})$ (NRS Eqs. 3.427–3.430). An arbitrary field is a superposition of steps, so $P(t) = a(0)E(t) - \int E(u)\,\frac{da(t-u)}{du}\,du$ (NRS Eqs. 3.431–3.433).

**The Debye permittivity.** The electronic and vibrational polarization follows the field instantly on this time scale and is collected in $\varepsilon_\infty$ (NRS Eq. 3.434). The rotational part, in steady state, then gives (NRS Eqs. 3.435–3.439)

$$
\varepsilon_r(\omega) = \varepsilon_\infty + \frac{\varepsilon_s - \varepsilon_\infty}{1 - i\omega\tau},\qquad
\varepsilon_1 = \varepsilon_\infty + \frac{\varepsilon_s - \varepsilon_\infty}{1 + \omega^2\tau^2},\qquad
\varepsilon_2 = \frac{\omega\tau(\varepsilon_s - \varepsilon_\infty)}{1 + \omega^2\tau^2}.
\label{debye}
$$

**Properties.**

- **The loss peak.** $\varepsilon_2$ peaks at $\omega\tau = 1$ with height $(\varepsilon_s - \varepsilon_\infty)/2$.
- **Water.** $\varepsilon_s = 78.3$, and the peak is near $10^{10.3}$ Hz ≈ 20 GHz, so $\tau\approx8$ ps: rotational relaxation in the hydrogen-bond network. The measured peak height 36.1 implies $\varepsilon_\infty = 6.0$.
- **The fit.** It is remarkable from MHz to the low THz, where it falls off too quickly (NRS Fig. 3.24).
- **As a differential equation.** The Debye polarization obeys $dP/dt + P/\tau = a_0E/\tau$ (NRS Eq. 3.447), an overdamped oscillator that never oscillates.

## Lorentz oscillators

**One oscillator.** A bound electron on a spring of eigenfrequency $\omega_0$, driven by the field, has polarizability $\alpha(\omega) = \frac{e^2}{m_e}\frac{1}{\omega_0^2 - \omega^2}$ (NRS Eqs. 3.440–3.442). Adding damping $2\gamma\,\dot r$ and summing over oscillators of strengths $f_i$ (ignoring the local field) gives (NRS Eqs. 3.443–3.450)

$$
\varepsilon_r(\omega) = 1 + \frac{e^2}{m_e\varepsilon_0}\sum_i\frac{f_i}{\omega_i^2 - \omega^2 - 2i\gamma_i\omega}.
\label{lorentz}
$$

This is the classical form of the sum-over-states polarizability of [[dispersion-oscillator-strengths-and-sum-rules]], with $f_i$ the oscillator strengths. Here $f_i$ is per unit volume, i.e. multiplied by $\mathcal N$.

**The plasma limit.** Far above all resonances (NRS Eq. 3.451),

$$
\varepsilon_1\to1 - \frac{\omega_p^2}{\omega^2},\qquad \varepsilon_2\to\frac{2e^2}{m_e\varepsilon_0\omega^3}\sum_if_i\gamma_i,\qquad \omega_p^2 = \frac{e^2}{m_e\varepsilon_0}\sum_if_i\approx\frac{e^2\mathcal N_e}{m_e\varepsilon_0}.
$$

The last step is the Thomas–Reiche–Kuhn sum rule: the total oscillator strength equals the number of electrons. For water NRS find $1 - \varepsilon_1\propto\omega^{-2}$ in the measured data with coefficient $0.95\times10^{33}$ rad² s⁻², close to $\omega_p^2 = 1.06\times10^{33}$.

**Near one isolated resonance.** With $\omega_k^2 - \omega^2\approx2\omega(\omega_k - \omega)$ and $A_k = e^2f_k/2m_e\varepsilon_0\omega_k$ (NRS Eqs. 3.452–3.459):

$$
\varepsilon_1 = 1 + A_k\frac{\omega_k - \omega}{(\omega_k - \omega)^2 + \gamma_k^2},\qquad \varepsilon_2 = A_k\frac{\gamma_k}{(\omega_k - \omega)^2 + \gamma_k^2} = \pi A_kf(\omega;\omega_k,\gamma_k).
$$

- **Line shape.** $\varepsilon_2$ is a Lorentzian (Cauchy distribution), with FWHM $2\gamma_k$. The Cauchy distribution integrates to 1 and tends to $\delta(\omega - \omega_k)$ as $\gamma\to0$.
- **Dispersion.** $\varepsilon_1$ has its extremes at $\omega_k\pm\gamma_k$.
- **Water.** For the first electronic band of liquid water (about 1.97 PHz, blue-shifted from 1.80 PHz in the gas), the fit gives $\gamma\approx10^{14}$ s⁻¹, a 5 fs relaxation time. For the $\nu_3$ stretch near 101 THz, $\gamma\approx7\times10^{12}$ s⁻¹ (70 fs) (NRS Fig. 3.26).

**Refraction.** The refractive index of water falls from a static value of 8.85 to 1.33 in the visible, and goes below 1 in the far UV and X-ray range, where phase velocities exceed $c$ (NRS Fig. 3.28). The connection of $n(\omega)$ to molecular $\alpha(\omega)$ is the Lorentz–Lorenz relation of [[local-field-clausius-mossotti-and-reaction-field]].

## Worked example

!!! example "Kramers–Kronig by numerical Hilbert transform (computed for this note)"
    **Lorentz model.** Three oscillators in dimensionless units, $(f, \omega_0, \gamma) = (1.0, 2, 0.1), (0.6, 5, 0.3), (2.0, 11, 0.8)$. $\varepsilon_2$ is taken on a grid $|\omega|\le400$ with step 0.001, and $\varepsilon_1$ reconstructed by the first relation of Eq. [[#kk]] (principal value by excluding the singular point):

    | $\omega$ | $\varepsilon_1$ exact | from Kramers–Kronig |
    |---:|---:|---:|
    | 1 | 1.373506 | 1.373490 |
    | 2 (on resonance) | 1.045560 | 1.045957 |
    | 4 | 0.998253 | 0.998245 |
    | 8 | 1.001593 | 1.001592 |

    - **Accuracy.** The reconstruction is good to $10^{-5}$ away from resonances. On the sharp resonance it is good to $4\times10^{-4}$, the grid error.
    - **Plasma sum rule.** At $\omega = 300$, $(1 - \varepsilon_1)\omega^2 = 3.6028$ against $\sum f = 3.6$.

    **Debye model, water parameters.** Applied to Eq. [[#debye]] with $\omega\tau$ = 0.3, 1, 3, the relation reproduces $\varepsilon_1$ = 72.33, 42.15, 13.23 as 72.20, 42.03, 13.12. The 0.2–0.9% shortfall is the truncated tail: Debye $\varepsilon_2$ decays only as $1/\omega$.

    **Peak height.** $(\varepsilon_s - \varepsilon_\infty)/2 = (78.3 - 6.0)/2 = 36.15$, against NRS's 36.1.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 3.5.4, Eq. (3.415), Fig. 3.22 (described); Sec. 3.5.4.1, Eqs. (3.416)–(3.426); Sec. 3.5.4.2, Eqs. (3.427)–(3.439), Figs. 3.23–3.25 (described); Sec. 3.5.4.3, Eqs. (3.440)–(3.459), Fig. 3.26 (described); Sec. 3.5.4.4, Fig. 3.28 (described). The Thomas–Reiche–Kuhn identification is general knowledge. The checks are in `Claude outputs/part1_fields_batchD.py`, section G.
