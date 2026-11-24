---
id: damped-response-and-absorption-cross-sections
title: Damped response theory - relaxation in the Liouville equation, complex polarizabilities, Lorentzian line shapes, the absorption cross section σ(ω) ∝ ω Im α(ω), and damped nonlinear response
summary: At resonance, undamped response functions diverge and perturbation theory fails after about one Rabi period. Adding phenomenological relaxation to the Liouville equation (decay rates Γ_n, coherence damping γ_mn = (Γ_m + Γ_n)/2) keeps populations small, so perturbation theory holds at resonance. The response functions become complex: the real part is dispersive and the imaginary part absorptive, with a Lorentzian of half-width γ. For a common damping this is the response function at complex frequency ω + iγ. The linear absorption cross section is σ(ω) = 4πω Im ᾱ(ω)/c, and it integrates to the oscillator strength. For pure states the same results follow from damping in the Ehrenfest equation. The density-matrix quadratic response has eight terms against six, and they agree only if the observable enters as a fluctuation operator (found and checked here). Two-level Liouville propagation recomputed.
status: in-progress
kind: theory
level: advanced
tags: [damped-response, complex-polarization-propagator, relaxation, liouville-equation, absorption-cross-section, lorentzian, einstein-coefficients, kramers-kronig]
prerequisites: [exact-state-response-functions, density-operators-and-mixed-states, fermi-golden-rule-and-decay-width]
related: [two-level-systems-and-rabi-oscillations, emission-absorption-and-spontaneous-emission, dispersion-oscillator-strengths-and-sum-rules, linear-response-for-variational-wave-functions, residue-analysis-of-response-functions]
conventions: [atomic-units]
key: damped
order: 90
date: 2026-11-24
---

Atomic units ($c\approx137.036$, $4\pi\varepsilon_0 = 1$). $\Gamma_n$ is the total decay rate (inverse lifetime) of excited state $n$, $\Gamma_0 = 0$. Response functions as in [[exact-state-response-functions]].

## Why damping

**Resonance breaks perturbation theory.** A field tuned to $\omega_{f0}$ makes the first-order amplitude grow linearly in time. The excited population of a two-level atom then grows as $t^2$ until, at times of order of the inverse Rabi frequency $\Omega = \mu_{ab}F/\hbar$, the population oscillates back ([[two-level-systems-and-rabi-oscillations]]). Fermi's golden rule ([[fermi-golden-rule-and-decay-width]]) gives a rate only for transitions into a continuum. For discrete-to-discrete transitions it needs a line width put in by hand.

**Relaxation fixes both.** Real excited states decay: spontaneous emission (natural width), collisions, internal conversion, intersystem crossing. When the decay rates exceed the stimulated rates, the excited populations stay small and a perturbative treatment remains valid even at resonance. The line width then appears by itself.

## Relaxation in the density-matrix equation

**Liouville equation.** The density operator $\hat\rho = \sum_sp_s|\psi_s\rangle\langle\psi_s|$ ([[density-operators-and-mixed-states]]) obeys $\partial_t\hat\rho = -i[\hat H,\hat\rho]$, equivalent to the Schrödinger equation. Relaxation toward equilibrium is added per element:

$$
\partial_t\rho_{mn} = -i[\hat H,\hat\rho]_{mn} - \gamma_{mn}\big(\rho_{mn}-\rho^{\rm eq}_{mn}\big),\qquad \rho^{\rm eq}_{mn} = \delta_{m0}\delta_{n0}.
\label{liouville}
$$

- **Populations.** $\gamma_{nn} = \Gamma_n$; the lifetime is $\tau_n = 1/\Gamma_n$. Population lost from $n$ returns to the ground state, so $\mathrm{tr}\,\hat\rho = 1$ is kept. For that reason the ground-state population is not governed by a simple rate of its own.
- **Coherences in a pure state.** $|c_m(t)c_n^*(t)|$ decays as $e^{-(\Gamma_m+\Gamma_n)t/2}$, so $\gamma_{mn} = (\Gamma_m+\Gamma_n)/2$. In particular $\gamma_{n0} = \Gamma_n/2$.
- **Dephasing.** Collisions that only scramble phases add a further term to $\gamma_{mn}$ ($m\ne n$). That makes the ensemble incoherent and has no wave-function counterpart.

**First order.** With $\hat\rho^{(0)} = |0\rangle\langle0|$ and $[\hat H_0,\hat\rho]_{mn} = \omega_{mn}\rho_{mn}$, each order follows by integrating Eq. [[#liouville]]:

$$
\rho^{(N)}_{mn} = e^{-(i\omega_{mn}+\gamma_{mn})t}\int_{-\infty}^t(-i)[\hat V,\hat\rho^{(N-1)}]_{mn}\,e^{(i\omega_{mn}+\gamma_{mn})t'}dt'.
$$

$\hat\rho^{(1)}$ has only $0n$ and $n0$ elements, so populations do not change at first order. With $\langle\hat\Omega\rangle^{(1)} = \mathrm{tr}(\hat\rho^{(1)}\hat\Omega)$,

$$
\langle\langle\hat\Omega;\hat V^\omega_\beta\rangle\rangle = -\sum_n\left[\frac{\Omega_{0n}V^\omega_{n0}}{\omega_{n0}-\omega-i\gamma_{n0}} + \frac{V^\omega_{0n}\Omega_{n0}}{\omega_{n0}+\omega+i\gamma_{n0}}\right].
\label{damped}
$$

## Complex polarizability

**Common damping.** With $\gamma_{n0} = \gamma$ for all $n$, Eq. [[#damped]] is the undamped function at the complex frequency $z = \omega + i\gamma$:

$$
\alpha_{\alpha\beta}(-\omega;\omega) = \sum_n{}'\left[\frac{\mu^\alpha_{0n}\mu^\beta_{n0}}{\omega_{n0}-\omega-i\gamma} + \frac{\mu^\beta_{0n}\mu^\alpha_{n0}}{\omega_{n0}+\omega+i\gamma}\right].
\label{complexalpha}
$$

**Real and imaginary parts (real wave functions).**

$$
\mathrm{Re}\,\alpha = \sum_n{}'\mu_{0n}\mu_{n0}\left[\frac{\omega_{n0}-\omega}{(\omega_{n0}-\omega)^2+\gamma^2} + \frac{\omega_{n0}+\omega}{(\omega_{n0}+\omega)^2+\gamma^2}\right],\qquad
\mathrm{Im}\,\alpha = \gamma\sum_n{}'\mu_{0n}\mu_{n0}\left[\frac1{(\omega_{n0}-\omega)^2+\gamma^2} - \frac1{(\omega_{n0}+\omega)^2+\gamma^2}\right].
$$

- **Real part.** Positive below the first resonance and crosses zero at it: dispersion, the refractive index.
- **Imaginary part.** Zero at $\omega = 0$, peaked at each $\omega_{n0}$: absorption. Near a resonance it is $\pi\mu_{0n}\mu_{n0}L(\omega)$, with the Lorentzian $L = \gamma/\{\pi[(\omega_{n0}-\omega)^2+\gamma^2]\}$ of half width at half maximum $\gamma$ (full width $\Gamma$).
- **Frequency inversion.** $\mathrm{Re}\,\alpha$ is even and $\mathrm{Im}\,\alpha$ odd under $\omega\to-\omega$.
- **Kramers–Kronig.** The two parts are linked by the Kramers–Kronig relations, since $\alpha(z)$ is analytic in the upper half plane.

**Oscillator strengths.** As $\gamma\to0$, $L\to\delta(\omega-\omega_{n0})$, and the isotropic average $\bar\alpha$ satisfies

$$
\frac{2\omega}{\pi}\,\mathrm{Im}\,\bar\alpha(-\omega;\omega)\ \xrightarrow{\ \gamma\to0\ }\ \sum_n{}'f_{n0}\,\delta(\omega-\omega_{n0}),
$$

so $\tfrac2\pi\int_0^\infty\omega\,\mathrm{Im}\,\bar\alpha\,d\omega = \sum f_{n0} = N$ ([[dispersion-oscillator-strengths-and-sum-rules]]).

**Phase lag.** In polar form $\alpha = |\alpha|e^{i\phi}$, a field $2F\cos\omega t$ induces $2|\alpha|F\cos(\omega t-\phi)$. At resonance $\alpha$ is nearly imaginary, and the induced dipole lags the field by $\pi/2$.

## Absorption cross section

**From the work done by the field.** The time-averaged power absorbed per molecule is $\langle dW/dt\rangle_T = \int\mathbf E\cdot\mathbf j^{(1)}d\mathbf r$, with $\mathbf j^{(1)}$ the first-order current density. Expressed as a response function this is $-2\omega\,\mathrm{Im}\langle\langle\hat V^{-\omega};\hat V^\omega\rangle\rangle$, with $\hat V$ the velocity-gauge coupling $\propto\hat{\mathbf p}\cdot\mathbf F$. A dipole-equivalence relation for damped response converts $\mathrm{Im}\langle\langle\hat p;\hat p\rangle\rangle$ into $\omega^2\,\mathrm{Im}\langle\langle\hat r;\hat r\rangle\rangle$ for $\gamma\ll\omega$. Dividing by the intensity $I = cF^2/(8\pi)$ of the wave (with $4\pi\varepsilon_0 = 1$) leaves

$$
\sigma(\omega) = \frac{4\pi\omega}{c}\,\mathrm{Im}\,\bar\alpha(-\omega;\omega)\qquad\Big(\text{SI: }\ \sigma = \frac{\omega}{\varepsilon_0c}\,\mathrm{Im}\,\bar\alpha\Big).
\label{sigma}
$$

**Per transition.** Equivalently, $\sigma(\omega) = \frac{2\pi^2}{c}f_{n0}L(\omega)$ for an isolated line (SI: $\pi e^2f_{n0}L/(2\varepsilon_0cm_e)$). The same result follows from the golden-rule rate $w = 2\pi|V_{f0}|^2L(\omega)$ with the Lorentzian from the damped amplitudes, averaged over orientations and divided by the photon flux.

**Einstein coefficient.** Ignoring the line shape, the absorption rate per unit intensity is $B_{f\leftarrow i} = \frac{\pi}{3\varepsilon_0c\hbar^2}\sum_\alpha|\mu^\alpha_{fi}|^2$ (SI), matching [[emission-absorption-and-spontaneous-emission]].

**Higher orders.** Two-photon absorption is proportional to $\mathrm{Im}\,\gamma(-\omega;\omega,-\omega,\omega)$, the damped intensity-dependent refractive index.

## Damping in wave-function theory

**Ehrenfest with relaxation.** A pure state has no density-matrix freedom beyond its coherences with $|0\rangle$. Writing the Liouville equation for $|\psi\rangle\langle\psi|$ as an Ehrenfest equation for the state-transfer operators $|n\rangle\langle0|$ and adding $-\gamma_{n0}(\langle\cdot\rangle - \langle\cdot\rangle_{\rm eq})$ gives damped rotation amplitudes, e.g. $P^{(1)}_n\propto\langle n|\hat V^\omega|0\rangle/(\omega_{n0}-\omega-i\gamma_{n0})$. Norm conservation is automatic, which a non-Hermitian $H_0$ with $E_n + i\Gamma_n/2$ would violate. The linear response function is identical to Eq. [[#damped]].

**Quadratic response: six against eight terms.** The wave-function route gives a damped $\beta$ with six terms. The density-matrix route gives eight, because term 2 of the undamped function splits into two with denominators $(\omega_{nm}\mp\omega_\sigma\mp i\gamma_{nm})$. Their sum minus the wave-function term is proportional to $\gamma_{nm} - \gamma_{n0} - \gamma_{m0}$. That factor vanishes for pure states ($\Gamma_0 = 0$) and is nonzero only with pure dephasing, which adds resonances at differences between excited states.

**A detail found while checking.** Written with plain operators and $\gamma_{00} = 0$, the eight-term formula is *not* invariant under $\hat\mu\to\hat\mu + c\,\hat 1$ once $\Gamma_n\ne0$. A constant shift of the operator must not change an oscillating response. The fix is trace conservation of the second-order density matrix: $\rho^{(2)}_{00} = -\sum_{n>0}\rho^{(2)}_{nn}$. In $\mathrm{tr}(\hat\rho^{(2)}\hat\Omega)$ this puts the fluctuation operator $\bar\Omega$ in place of $\hat\Omega$. With that, the eight-term and six-term forms agree to machine precision for any $\Gamma_n$ (table below).

## Approximate-state damped response

For SCF, CI or MCSCF references the damped linear response function is

$$
\langle\langle\hat\Omega;\hat V^\omega\rangle\rangle = -[\boldsymbol\Omega^{[1]}]^\dagger\big(\mathbf E^{[2]} - (\omega+i\gamma)\mathbf S^{[2]}\big)^{-1}\mathbf V^{\omega,[1]},
$$

the complex polarization propagator. It is solved frequency by frequency as one complex linear system ([[linear-response-for-variational-wave-functions]]), without any eigenvectors. This makes it the method of choice where the density of states is high or the states of interest lie far up the spectrum (core excitations, X-ray absorption, the continuum).

**Basis-set resolution.** NRS's TDHF helium spectra illustrate a practical point. In t-aug-cc-pVTZ a single peak at 23.7 eV collects the intensity that q-aug-cc-pV5Z splits into two peaks (23.5 and 24.2 eV). The oscillator strength summed below and above the ionization potential is nearly the same in both, 1.999 and 2.001 in total.

## Worked examples

!!! example "Resonant two-level atom with relaxation (computed for this note)"
    $\omega_{ba} = 0.5$, $\mu_{ab} = 1$, $\Gamma = 0.025$ ($\gamma_{ab} = 0.0125$), field $5\times10^{-5}\sin(0.5t)$ switched on smoothly. Eq. [[#liouville]] is integrated to $t = 1500$ and $\mu(t)$ fitted in the steady state.

    - **Polarizability.** From propagation: $1.000 + 79.987i$. From Eq. [[#complexalpha]]: $1.000 + 79.988i$. The resonant term gives $\mu_{ab}^2/(-i\gamma) = 80i$, the antiresonant term $\mu_{ab}^2/(2\omega_{ba}) = 1$.
    - **Population.** The excited population settles at $4.0\times10^{-6}$ (NRS: "about $4\times10^{-6}$"), so perturbation theory holds at resonance.

!!! example "f-sum and damped β in the five-state model (computed for this note)"
    - **f-sum.** With $\gamma = 0.002$, $\tfrac2\pi\int_0^3\omega\,\mathrm{Im}\,\alpha\,d\omega = 0.27620$, against $\sum f_{n0} = 0.27644$. The difference is the Lorentzian tails beyond $\omega = 3$.
    - **Damped $\beta(-0.3;0.17,0.13)$** with $\Gamma_n = 0.01n$:

    | Form | value |
    |---|---|
    | six-term (wave function) | 3.92101815 + 0.08684702i |
    | eight-term, fluctuation observable | 3.92101815 + 0.08684702i |
    | eight-term + pure dephasing 0.02 | 3.92240930 + 0.08389988i |
    | eight-term, plain operators | 3.92092656 + 0.10326416i |
    | same, $\mu\to\mu + 0.5$ | 3.92109443 + 0.07317437i |

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 5.8, Eqs. (5.237)–(5.246); Sec. 5.10, Eqs. (5.263)–(5.339) (density operator, Liouville equation with damping, damped linear and quadratic response, relaxation in wave-function theory, absorption cross section, Einstein coefficients); Sec. 7.5, Eqs. (7.159)–(7.165), Figs. 7.9–7.10 (described). NRS cite P. Norman, D. M. Bishop, H. J. A. Jensen and J. Oddershede, J. Chem. Phys. 123, 194103 (2005) for nonlinear response with relaxation (to verify). The fluctuation-operator remark on the eight-term formula is a finding of this note, not a statement in NRS. The calculations are in `Claude outputs/part4_response_batchA.py`, section E.
