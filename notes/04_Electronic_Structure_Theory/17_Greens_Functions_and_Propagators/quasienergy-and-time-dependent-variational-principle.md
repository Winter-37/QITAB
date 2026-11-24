---
id: quasienergy-and-time-dependent-variational-principle
title: The quasienergy and the time-dependent variational principle - phase isolation, the time-dependent Hellmann-Feynman theorem, response functions as derivatives of the time-averaged quasienergy, and the 2n + 1 rule in time
summary: In a periodic field the energy is not conserved, but splitting off the phase of the wave function leaves a real quasienergy Q(t) = ⟨ψ̃|H − i∂t|ψ̃⟩. Its time average Q_T over one period is stationary in the phase-isolated wave function (δQ_T = 0), and its field derivatives are time-averaged expectation values (time-dependent Hellmann-Feynman). Expanded in the field amplitudes, Q_T has the response functions as coefficients, so they can be computed as derivatives of a variational function. The first-order response equations are (E[2] − ωS[2])P = −Q₁, and the quadratic response needs only first-order amplitudes (2n + 1). Checked with Floquet quasienergies of the NRS two-level atom and of a five-state model.
status: in-progress
kind: theory
level: advanced
tags: [quasienergy, time-dependent-variational-principle, hellmann-feynman, floquet, response-functions, 2n-plus-1-rule, two-level-atom]
prerequisites: [exact-state-response-functions, variational-perturbation-theory-and-the-2n-plus-1-rule, two-level-systems-and-rabi-oscillations]
related: [coupled-cluster-response-functions, linear-response-for-variational-wave-functions, hellmann-feynman-and-virial-theorems, lagrangian-for-nonvariational-energies, heisenberg-picture-and-time-translation]
conventions: [atomic-units]
key: qtexpansion
order: 60
date: 2026-11-24
---

Atomic units. $\hat H(t) = \hat H_0 + \hat V(t)$ with $\hat V(t) = \sum_\omega\hat V^\omega_\alpha F^\omega_\alpha e^{-i\omega t}$ as in [[exact-state-response-functions]]. $T$ is the period of the perturbation; for several frequencies, $T$ is a common period.

## Why a quasienergy

**The energy is gone.** For a static field the properties are derivatives of the energy. In an oscillating field energy flows between the molecule and the field, so $\langle\hat H\rangle$ is not conserved and its derivatives are not properties. One option is to expand the polarization instead ([[exact-state-response-functions]]). The other is to find a substitute for the energy that is variational and has the response functions as derivatives.

**Phase isolation.** Write

$$
\psi(t) = e^{-i\phi(t)}\tilde\psi(t),
$$

with $\phi$ real and the phase of $\langle0|\tilde\psi\rangle$ fixed to zero. Without a field $\tilde\psi = |0\rangle$ and $\phi = E_0t$. Inserting into the Schrödinger equation,

$$
\big(\hat H - i\partial_t\big)\tilde\psi(t) = Q(t)\,\tilde\psi(t),\qquad Q(t) = \dot\phi(t) = \langle\tilde\psi|\hat H - i\partial_t|\tilde\psi\rangle.
\label{qdef}
$$

$Q(t)$ is the **quasienergy**. It is real: from $\langle\tilde\psi_1|\hat H - i\partial_t|\tilde\psi_2\rangle = \langle\tilde\psi_2|\hat H - i\partial_t|\tilde\psi_1\rangle^* - i\partial_t\langle\tilde\psi_1|\tilde\psi_2\rangle$ with $\tilde\psi_1 = \tilde\psi_2$ and a constant norm. Without a field it is $E_0$.

## The variational principle

**Allowed variations.** A variation that keeps the norm is $\delta\tilde\psi = \delta\tilde\psi_\perp + i\varepsilon(t)\tilde\psi$ with $\varepsilon$ real. With the identity above and Eq. [[#qdef]],

$$
\delta Q(t) = -i\partial_t\langle\tilde\psi|\delta\tilde\psi\rangle.
$$

So $Q(t)$ is not stationary: its variation is a total time derivative.

**Time-dependent Hellmann-Feynman theorem.** Taking $\delta\tilde\psi = (d\tilde\psi/dF)\,dF$,

$$
\frac{dQ(t)}{dF} = \Big\langle\tilde\psi\Big|\frac{\partial\hat H}{\partial F}\Big|\tilde\psi\Big\rangle - i\,\partial_t\Big\langle\tilde\psi\Big|\frac{d\tilde\psi}{dF}\Big\rangle.
$$

The extra term, absent in the static theorem of [[hellmann-feynman-and-virial-theorems]], is the time derivative of a periodic function. It vanishes on averaging over a period.

**The time-averaged quasienergy.** In the steady state (only the field frequencies and their combinations remain),

$$
Q_T = \frac1T\int_t^{t+T}Q(t')\,dt',\qquad \delta Q_T = 0,\qquad \frac{dQ_T}{dF^\omega_\alpha} = \frac1T\int_t^{t+T}\langle\tilde\psi|\hat V^\omega_\alpha|\tilde\psi\rangle e^{-i\omega t'}dt'.
\label{tdhf}
$$

$Q_T$ is time-independent, a function of the field amplitudes only, and it is the zero-frequency Fourier component of $Q(t)$. It plays the role the energy plays for static fields.

**Response functions as derivatives.** The second relation in Eq. [[#tdhf]] makes the $F$-expansion of $Q_T$ reproduce the Kubo expansion term by term, with the frequency constraint made explicit:

$$
Q_T = E_0 + \sum_{\omega_1}\langle0|\hat V^{\omega_1}_\alpha|0\rangle\delta_{\omega_1}F^{\omega_1}_\alpha + \tfrac12\sum_{\omega_1\omega_2}\langle\langle\hat V^{\omega_1}_\alpha;\hat V^{\omega_2}_\beta\rangle\rangle\delta_{\omega_1+\omega_2}F^{\omega_1}_\alpha F^{\omega_2}_\beta + \tfrac16\sum\langle\langle\hat V^{\omega_1}_\alpha;\hat V^{\omega_2}_\beta,\hat V^{\omega_3}_\gamma\rangle\rangle\delta_{\omega_1+\omega_2+\omega_3}F^{\omega_1}_\alpha F^{\omega_2}_\beta F^{\omega_3}_\gamma + \cdots
\label{qtexpansion}
$$

Only combinations whose frequencies add to zero survive the averaging. In particular the first-order term is nonzero only for a static field.

**Monochromatic field.** For $F(t) = F_0\cos\omega t$ ($F^{\pm\omega} = F_0/2$) and $\hat V = -\hat\mu$, the third-order term cannot satisfy $\pm\omega\pm\omega\pm\omega = 0$, and

$$
Q_T = E_0 - \tfrac14\alpha(-\omega;\omega)F_0^2 - \tfrac1{64}\gamma(-\omega;\omega,-\omega,\omega)F_0^4 - \cdots
\label{qtmono}
$$

The fourth-order coefficient counts the six orderings of $\{\omega,\omega,-\omega,-\omega\}$, all equal to $-\gamma(-\omega;\omega,-\omega,\omega)$ by permutation symmetry, times $(F_0/2)^4/24$. As $\omega\to0$ this is the time average of $E(F_0\cos\omega t)$: $\langle\cos^2\rangle = \tfrac12$ and $\langle\cos^4\rangle = \tfrac38$ give the factors $\tfrac14$ and $\tfrac1{64}$.

**Connection with Floquet theory (standard result, checked below).** For a strictly periodic $\hat H(t)$ the solutions are Floquet states $e^{-i\varepsilon t}u(t)$ with $u$ periodic. The phase-isolated wave function differs from $u$ by a periodic phase, whose derivative averages to zero, so $Q_T$ equals the Floquet quasienergy $\varepsilon$ of the branch connected to $|0\rangle$. This gives an independent numerical check of response functions.

## Response equations from stationarity

**Parameters.** Use the rotation parametrization $\tilde\psi = e^{-i\hat P(t)}|0\rangle$ of [[exact-state-response-functions]], with $P_n(t) = \sum_{\omega_1}P^{(1)}_n(\omega_1)e^{-i\omega_1t} + \cdots$. $Q_T$ becomes a function of the Fourier amplitudes $P^{(k)}_n$, $[P^{(k)}_n]^*$ and the fields, stationary in every amplitude at every field strength.

**First-order equations.** Differentiating the stationarity conditions once with respect to the field (as for static fields in [[variational-perturbation-theory-and-the-2n-plus-1-rule]]):

$$
\mathbf Q_T^{[2;0]}\,\mathbf P^\beta + \mathbf Q_T^{[1;\beta]} = 0,\qquad \mathbf Q_T^{[2;0]} = \big(\mathbf E^{[2]} - \omega_2\mathbf S^{[2]}\big)\delta_{\omega_1+\omega_2},
\label{response}
$$

with $\mathbf P^\beta$ the vector of $\partial P_n/\partial F^{\omega_2}_\beta$ and $\partial P^*_n/\partial F^{\omega_2}_\beta$. The two matrices come from the two parts of the quasienergy operator:

- $\hat H_0$ gives the Hessian $\mathbf E^{[2]} = \mathrm{diag}(\omega_{n0},\omega_{n0})$, obtained by expanding $\langle0|e^{i\hat P}\hat H_0e^{-i\hat P}|0\rangle$ to second order;
- $-i\partial_t$ gives the metric $\mathbf S^{[2]} = \mathrm{diag}(\mathbf 1,-\mathbf 1)$, because each Fourier amplitude carries its own $e^{-i\omega t}$.

The field gradient is $\mathbf Q_T^{[1;\beta]} = i\big(\langle n|\hat V^{\omega_2}_\beta|0\rangle, -\langle0|\hat V^{\omega_2}_\beta|n\rangle\big)$.

**Linear response.** By the $2n+1$ rule, $d^2Q_T/dF^{\omega_1}_\alpha dF^{\omega_2}_\beta = [\mathbf Q_T^{[1;\alpha]}]^\dagger_-\mathbf P^\beta$, where the subscript $-$ means the frequency signs are reversed. Inserting the solution of Eq. [[#response]],

$$
\langle\langle\hat V^{\omega_1}_\alpha;\hat V^{\omega_2}_\beta\rangle\rangle = -[\mathbf Q_T^{[1;\alpha]}]^\dagger_-\big(\mathbf E^{[2]} - \omega_2\mathbf S^{[2]}\big)^{-1}\mathbf Q_T^{[1;\beta]} = -\sum_n{}'\left[\frac{V^{\omega_1}_{0n}V^{\omega_2}_{n0}}{\omega_{n0}-\omega_2} + \frac{V^{\omega_2}_{0n}V^{\omega_1}_{n0}}{\omega_{n0}-\omega_1}\right]_{\omega_1=-\omega_2}.
$$

This is the sum-over-states formula, because the exact Hessian is diagonal. For an approximate wave function the same equation holds with a non-diagonal $\mathbf E^{[2]}$; that is the whole of linear response theory for SCF, CI and MCSCF ([[linear-response-for-variational-wave-functions]]).

**Quadratic response from first-order amplitudes.** The third field derivative of $Q_T$ contains second-order amplitudes. They multiply either the first-order equations (zero) or terms that cancel pairwise, as in the static case. The term with three amplitudes multiplies $\langle0|[\hat P,[\hat P,[\hat P,\hat Q]]]|0\rangle$-type matrix elements, which vanish for exact states. What remains is

$$
\frac{d^3Q_T}{dF^{\omega_1}_\alpha dF^{\omega_2}_\beta dF^{\omega_3}_\gamma} = [\mathbf P^\alpha]^\dagger_-\mathbf Q_T^{[2;\beta]}\mathbf P^\gamma + [\mathbf P^\beta]^\dagger_-\mathbf Q_T^{[2;\gamma]}\mathbf P^\alpha + [\mathbf P^\gamma]^\dagger_-\mathbf Q_T^{[2;\alpha]}\mathbf P^\beta,\qquad \mathbf Q_T^{[2;\beta]} = \mathrm{diag}\big(\langle n|\hat V^{\omega_2}_\beta|m\rangle,\ \langle m|\hat V^{\omega_2}_\beta|n\rangle\big),
$$

which gives the overall-symmetric quadratic response function $\sum_{1,2,3}\sum'_{nm}V^{\omega_1}_{0n}V^{\omega_2}_{nm}V^{\omega_3}_{m0}/[(\omega_{n0}+\omega_1)(\omega_{m0}-\omega_3)]$, free of secular terms. This is Wigner's $2n+1$ rule in time: first-order amplitudes fix properties through third order.

**Why bother.** For exact states the quasienergy route adds nothing new. Its value is that it (i) makes the response function a derivative of a variational function, so the $2n+1$ and $2n+2$ rules apply, and (ii) extends to non-variational methods through a time-averaged Lagrangian ([[coupled-cluster-response-functions]]).

## Worked examples

!!! example "NRS two-level atom: Q(t), the polarizability and the time-dependent Hellmann-Feynman theorem (computed for this note)"
    $E_a = 0$, $E_b = 0.5$, $\mu_{ab} = 1$; field $F\sin\omega t$, with $F = 5\times10^{-5}$ in the propagations.

    - **Quasienergy (NRS Eq. 5.42, second order).** $Q(t) = E_a - \omega_{ba}\mu_{ab}^2F^2\sin^2\omega t/(\omega_{ba}^2-\omega^2)$ in the steady state. Its average $E_a - \alpha F^2/4$ has $\alpha = 2\omega_{ba}\mu_{ab}^2/(\omega_{ba}^2-\omega^2)$, i.e. Eq. [[#qtmono]].
    - **Direct propagation.** Propagating the Schrödinger equation with $\Delta t = 0.1$ and the NRS switch-on $\mathrm{erf}(0.01t)$ at $\omega = 0.1$ gives a steady-state ratio $\max\mu(t)/F = 4.171$. The formula gives 4.1667 (NRS quote "≈ 4.17").
    - **Floquet check.** NRS's $\omega = 0.1$ is exactly $\omega_{ba}/5$, a five-photon resonance where $|b,-5\omega\rangle$ is degenerate with $|a\rangle$ in Floquet space, so the check uses $\omega = 0.11$. Taylor coefficients of the Floquet quasienergy (contour in complex $F_0$, 61 Fourier blocks) give $\alpha = 4.2034468264$ (formula 4.2034468264) and $\gamma(-\omega;\omega,-\omega,\omega) = -226.40636227$ ([[exact-state-response-functions#gamma]]: −226.40636227).
    - **Hellmann-Feynman.** At $F_0 = 5\times10^{-5}$, $dQ_T/dF_0 = -1.050862\times10^{-4}$ by finite difference, and $-\alpha F_0/2 = -1.050862\times10^{-4}$.

!!! example "Five-state model with permanent dipoles (computed for this note)"
    Floquet quasienergies against Eq. [[#qtmono]] with the sum-over-states $\alpha$ and $\gamma$ (model of [[exact-state-response-functions]]):

    | $\omega$ | $\alpha$ Floquet | $\alpha$ SOS | $\gamma$ Floquet | $\gamma$ SOS |
    |---:|---:|---:|---:|---:|
    | 0.05 | 0.8903585825 | 0.8903585825 | 9.51817364 | 9.51817364 |
    | 0.12 | 0.9277487519 | 0.9277487519 | 12.26390443 | 12.26390441 |

    The odd Taylor coefficients of the quasienergy are below $10^{-11}$, as the frequency constraint in Eq. [[#qtexpansion]] requires.

## Limitations

- **Steady state only.** Time averaging assumes that all transients have died out. Pulsed or real-time problems need the time-dependent equations themselves.
- **Resonances.** $Q_T$ is defined only away from resonances; near them, damping must be added ([[damped-response-and-absorption-cross-sections]]).

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 5.1, Eqs. (5.25)–(5.55) (phase isolation, quasienergy, time-dependent Hellmann–Feynman theorem, time averaging); Sec. 5.5, Eqs. (5.151)–(5.178) and (5.190)–(5.193) (response functions as $Q_T$ derivatives); Sec. 7.2.2, Eqs. (7.83)–(7.85); Appendix I, Sec. I.3. NRS list O. Christiansen, P. Jørgensen and C. Hättig, Int. J. Quantum Chem. 68, 1 (1998) as the reference for the quasienergy formalism (to verify). The Floquet identification of $Q_T$ is added here and checked numerically; the computations are in `Claude outputs/part4_response_batchA.py`, sections A and B.
