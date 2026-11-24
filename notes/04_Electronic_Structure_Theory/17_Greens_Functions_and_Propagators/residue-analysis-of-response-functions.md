---
id: residue-analysis-of-response-functions
title: Residue analysis of response functions - excitation energies and one-, two- and three-photon matrix elements from single residues, excited-state dipoles and polarizabilities from double residues
summary: A ground-state response function holds information on all excited states. Its poles are excitation energies, and its residues are products of matrix elements. The linear polarizability's residue is a squared transition moment. A single residue of β gives the two-photon matrix element, and a double residue of β gives excited-to-excited transition moments, or, for f = g, the change of dipole on excitation. A single residue of γ gives the three-photon matrix element, and its f = g double residue gives the excited-state polarizability minus the ground-state one. In approximate theories the poles and residues come from the response matrices, which deliver energies and transition properties but no excited-state wave function. The linear and quadratic residues and the f = g double residue of γ are checked numerically on a model.
status: in-progress
kind: theory
level: advanced
tags: [residues, poles, excitation-energies, transition-moments, two-photon-absorption, excited-state-properties, response-functions]
prerequisites: [exact-state-response-functions]
related: [linear-response-for-variational-wave-functions, polarization-propagator-rpa, propagators-and-superoperators, eom-ccsd-and-size-extensivity, dispersion-oscillator-strengths-and-sum-rules]
conventions: [atomic-units]
key: linres
order: 80
date: 2026-11-24
---

Atomic units; notation of [[exact-state-response-functions]], with $\mu^\alpha_{mn} = \langle m|\hat\mu_\alpha|n\rangle$ and $\bar\mu = \hat\mu - \mu_{00}$. $|f\rangle$, $|g\rangle$ are selected excited states.

## Poles and residues

**Definitions.** If $f(z) = g(z)/(z-a)^n$ with $g(a)\ne0$, then $a$ is a pole of order $n$, and

$$
\mathrm{Res}(f,a) = \frac1{(n-1)!}\lim_{z\to a}\frac{d^{n-1}}{dz^{n-1}}\big[(z-a)^nf(z)\big].
$$

For a simple pole the residue is $\lim(z-a)f(z)$.

**Why residues.** Response functions are *ground-state* properties, yet every excitation energy appears in their denominators. Finding the poles gives excitation energies without computing an excited state. Taking residues gives the matrix elements that set intensities. A higher-order response function contains more matrix elements in its numerators, so its residues reach further: excited-to-excited transitions and excited-state properties.

## Linear response

From the polarizability formula of [[exact-state-response-functions]],

$$
\lim_{\omega\to\omega_{f0}}(\omega_{f0}-\omega)\,\alpha_{\alpha\beta}(-\omega;\omega) = \mu^\alpha_{0f}\mu^\beta_{f0}.
\label{linres}
$$

The poles are the excitation energies; the residues are the one-photon transition moments that enter the oscillator strength.

## Quadratic response

**Single residue: two-photon absorption.** In $\beta$ (the full-sum form with all states), the factor $(\omega_{p0}-\omega_2)^{-1}$ with $p = f$ has a pole at $\omega_2 = \omega_{f0}$. Only the two permutations that keep the pair $(\gamma,\omega_2)$ in the last position contribute:

$$
\lim_{\omega_2\to\omega_{f0}}(\omega_{f0}-\omega_2)\,\beta_{\alpha\beta\gamma}(-\omega_\sigma;\omega_1,\omega_2) = \sum_n\left[\frac{\mu^\alpha_{0n}\mu^\beta_{nf}}{\omega_{nf}-\omega_1} + \frac{\mu^\beta_{0n}\mu^\alpha_{nf}}{\omega_{n0}+\omega_1}\right]\mu^\gamma_{f0}.
$$

At $\omega_1 = -\omega_{f0}/2$ (so $\omega_\sigma = \omega_{f0}/2$) the bracket becomes the two-photon matrix element for absorbing two photons of energy $\omega_{f0}/2$,

$$
M^{(2)}_{0f} = \sum_n\left[\frac{\mu^\alpha_{0n}\mu^\beta_{nf}}{\omega_{n0}-\omega_{f0}/2} + \frac{\mu^\beta_{0n}\mu^\alpha_{nf}}{\omega_{n0}-\omega_{f0}/2}\right],
$$

the same object that second-order time-dependent perturbation theory gives for the transition amplitude $d^{(2)}_f$. The sum runs over all states, including $n = 0$ and $n = f$, which bring in the permanent dipoles.

**Double residue: excited-state transition moments and dipoles.** Take $\omega_1\to-\omega_{f0}$ and $\omega_2\to\omega_{g0}$ in the fluctuation form of $\beta$:

$$
\lim_{\omega_1\to-\omega_{f0}}(\omega_{f0}+\omega_1)\Big[\lim_{\omega_2\to\omega_{g0}}(\omega_{g0}-\omega_2)\,\beta_{\alpha\beta\gamma}\Big] = \mu^\beta_{0f}\,\bar\mu^\alpha_{fg}\,\mu^\gamma_{g0}.
\label{dres}
$$

- **$f\ne g$.** The middle factor is the transition moment between two excited states, the quantity behind excited-state absorption.
- **$f = g$.** It is $\mu^\alpha_{ff} - \mu^\alpha_{00}$, the change of the permanent dipole on excitation. This is the first example of a *property of an excited state* obtained from a ground-state response function.

## Cubic response

**Single residue: three-photon absorption.** With $\omega_3\to\omega_{f0}$,

$$
\lim_{\omega_3\to\omega_{f0}}(\omega_{f0}-\omega_3)\,\gamma = \sum_{-\sigma,1,2}\sum_{nm}\frac{\mu^\alpha_{0n}\mu^\beta_{nm}\mu^\gamma_{mf}}{(\omega_{nf}-\omega_1-\omega_2)(\omega_{mf}-\omega_2)}\,\mu^\delta_{f0}.
$$

At $\omega_1 = \omega_2 = -\omega_{f0}/3$ this is the three-photon matrix element.

**Double residue, $f\ne g$: two-photon absorption between excited states.** With $\omega_2\to-\omega_{g0}$ and $\omega_3\to\omega_{f0}$, only the permutations that exchange $(\alpha,-\omega_\sigma)$ and $(\gamma,\omega_2)$ survive. The result is

$$
\sum_m\left[\frac{\mu^\alpha_{gm}\mu^\beta_{mf}}{\omega_{mf}-\omega_1} + \frac{\mu^\beta_{gm}\mu^\alpha_{mf}}{\omega_{mg}+\omega_1}\right]\mu^\gamma_{0g}\mu^\delta_{f0},
$$

the two-photon element between $|g\rangle$ and $|f\rangle$, evaluated at $\omega_1 = -\omega_{fg}/2$.

**Double residue, $f = g$: excited-state polarizability.** Here a secular term of $\gamma$ is involved, so the form with the secular terms already removed must be used. The term that would diverge at $\omega_1 = 0$ cancels against its permutation partner, leaving

$$
\lim_{\omega_2\to-\omega_{f0}}(\omega_{f0}+\omega_2)\Big[\lim_{\omega_3\to\omega_{f0}}(\omega_{f0}-\omega_3)\,\gamma_{\alpha\beta\gamma\delta}\Big] = \big[\alpha^{(f)}_{\alpha\beta}(-\omega_1;\omega_1) - \alpha^{(0)}_{\alpha\beta}(-\omega_1;\omega_1)\big]\mu^\gamma_{0f}\mu^\delta_{f0},
\label{gres}
$$

where $\alpha^{(f)}$ is the sum-over-states polarizability of state $f$ (sum over $m\ne f$ with $\omega_{mf}$, which may be negative).

## Summary of what the residues give

| Response function | Residue | Property |
|---|---|---|
| $\alpha(-\omega;\omega)$ | $\omega = \omega_{f0}$ | one-photon $\langle0|\mu|f\rangle$ |
| $\beta(-\omega_\sigma;\omega_1,\omega_2)$ | $\omega_2 = \omega_{f0}$ | two-photon $0\to f$ |
| | $\omega_1 = -\omega_{f0}$, $\omega_2 = \omega_{g0}$ | one-photon $f\to g$; for $f = g$, $\mu_{ff}-\mu_{00}$ |
| $\gamma(-\omega_\sigma;\omega_1,\omega_2,\omega_3)$ | $\omega_3 = \omega_{f0}$ | three-photon $0\to f$ |
| | $\omega_2 = -\omega_{g0}$, $\omega_3 = \omega_{f0}$ | two-photon $g\to f$; for $f = g$, $\alpha_f - \alpha_0$ |

A triple residue of $\gamma$ gives nothing beyond these.

## Approximate theories

**Matrix form.** In an approximate theory the sums over states become a response matrix, and poles become the values of $\omega$ where $\mathbf E^{[2]} - \omega\mathbf S^{[2]}$ is singular ([[linear-response-for-variational-wave-functions]]). With eigenvectors $\mathbf X_n$ normalized as $\mathbf X_n^\dagger\mathbf S^{[2]}\mathbf X_n = 1$, the linear response function has exactly the sum-over-states form, and

$$
E_n - E_0 \to \lambda_n,\qquad \langle0|\hat\Omega|n\rangle\to[\boldsymbol\Omega^{[1]}]^\dagger\mathbf X_n,\qquad \langle n|\hat V^\omega|0\rangle\to\mathbf X_n^\dagger\mathbf V^{\omega,[1]}.
$$

**What is not obtained.** Except for CI (whose response eigenvectors are CI vectors), the residue analysis gives energies, transition moments and, from quadratic and cubic response, excited-state densities and moments. It does not give an excited-state wave function; why, is shown in [[linear-response-for-variational-wave-functions]].

**Coupled cluster.** The poles are the eigenvalues of the non-symmetric Jacobian, the EOM-CC excitation energies of [[eom-ccsd-and-size-extensivity]]. Left and right eigenvectors then both enter the residues.

## Worked example

!!! example "Residues of a five-state model (computed for this note)"
    Model of [[exact-state-response-functions]] ($E$ and $\mu_z$ printed there), $f = 1$ ($\omega_{f0} = 0.541426$), $g = 3$. Limits evaluated at a distance $d = 10^{-8}$ from the poles.

    | Residue | numerical limit | formula |
    |---|---:|---:|
    | $\alpha$ at $\omega_{f0}$, Eq. [[#linres]] | 0.23390420 | $\mu_{0f}^2$ = 0.23390420 |
    | $\beta$ single, $\omega_1 = -\omega_{f0}/2$ | 0.94628348 | $M^{(2)}_{0f}\mu_{f0}$ = 0.94628349 |
    | $\beta$ double, $f\ne g$, Eq. [[#dres]] | 0.00383007 | $\mu_{0f}\mu_{fg}\mu_{g0}$ = 0.00383007 |
    | $\beta$ double, $f = g$ | 0.13255532 | $\mu_{0f}^2(\mu_{ff}-\mu_{00})$ = 0.13255531 |
    | $\gamma$ double, $f = g$, $\omega_1 = 0.07$, Eq. [[#gres]] | 0.09862622 | $(\alpha_f-\alpha_0)\mu_{0f}^2$ = 0.09862653 |

    At $\omega_1 = 0.07$: $\alpha_0 = 0.897652$ and $\alpha_f = 1.319305$. The two-photon matrix element is $M^{(2)}_{0f} = -1.95660090$. The small differences come from the finite distance to the pole.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 5.8, Eqs. (5.247)–(5.252) (multiphoton matrix elements); Sec. 5.9, Eqs. (5.253)–(5.262) and Table 5.3; Sec. 7.4, Eqs. (7.153)–(7.158). The calculations are in `Claude outputs/part4_response_batchA.py`, section D.
