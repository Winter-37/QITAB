---
id: exact-state-response-functions
title: Exact-state response functions - the Kubo expansion, sum-over-states linear, quadratic and cubic response, secular divergences and the phase-isolated wave function
summary: A molecule in a weak periodic field has an expectation value that expands in the field amplitudes; the coefficients are the linear, quadratic and cubic response functions ⟨⟨Ω;V⟩⟩, ⟨⟨Ω;V,V⟩⟩, ⟨⟨Ω;V,V,V⟩⟩. Time-dependent perturbation theory in the exact eigenstates gives them as sums over states. With Ω = μ and V = −μ they are the frequency-dependent polarizability α(−ω;ω) and hyperpolarizabilities β(−ωσ;ω1,ω2) and γ(−ωσ;ω1,ω2,ω3). Terms with the ground state as intermediate diverge at zero frequency; they cancel exactly and leave formulas with fluctuation operators μ̄ = μ − ⟨0|μ|0⟩. A rotation (exp(−iP)) parametrization of the phase-isolated wave function gives the same formulas with no divergent terms at all. Checked on a five-state model against exact field derivatives (static) and Floquet quasienergies (dynamic).
status: in-progress
kind: theory
level: advanced
tags: [response-functions, kubo-relation, polarizability, hyperpolarizability, sum-over-states, secular-divergence, nonlinear-optics, frequency-dependent]
prerequisites: [time-dependent-perturbation-theory, molecular-properties-and-response, propagators-and-superoperators]
related: [quasienergy-and-time-dependent-variational-principle, residue-analysis-of-response-functions, dispersion-oscillator-strengths-and-sum-rules, damped-response-and-absorption-cross-sections, polarization-propagator-rpa, stark-effect, interaction-picture-and-dyson-series]
conventions: [atomic-units]
key: kubo
order: 50
date: 2026-11-24
---

Atomic units ($\hbar = e = m_e = 1$). Greek subscripts $\alpha,\beta,\gamma,\delta$ are Cartesian axes in the molecular frame, summed when repeated. $|n\rangle$ are the exact eigenstates of the unperturbed Hamiltonian, $\hat H_0|n\rangle = E_n|n\rangle$, with $|0\rangle$ the reference (usually ground) state and $\omega_{n0} = E_n - E_0$. A primed sum $\sum'_n$ excludes $n = 0$.

## The setup and the definition

**Perturbation.** The molecule is in the state $|0\rangle$ before a field is switched on adiabatically in the remote past,

$$
\hat H(t) = \hat H_0 + \hat V(t),\qquad \hat V(t) = \sum_\omega \hat V^\omega_\beta F^\omega_\beta\,e^{-i\omega t}e^{\epsilon t}.
\label{vt}
$$

The sum runs over positive and negative frequencies, $\epsilon\to0^+$ switches the field on slowly, and a real field requires $F^{-\omega}_\beta = (F^\omega_\beta)^*$ and $\hat V^{-\omega}_\beta = (\hat V^\omega_\beta)^\dagger$. In the electric dipole approximation $\hat V^\omega_\beta = -\hat\mu_\beta$ for every $\omega$, but the formalism allows a different operator for each field.

**Response functions (Kubo relation).** At times when only the field frequencies and their combinations remain in the motion, the expectation value of an observable $\hat\Omega$ is expanded in the field amplitudes,

$$
\langle\Omega\rangle(t) = \langle0|\hat\Omega|0\rangle + \sum_{\omega_1}\langle\langle\hat\Omega;\hat V^{\omega_1}_\beta\rangle\rangle F^{\omega_1}_\beta e^{-i\omega_1t}
+ \tfrac12\sum_{\omega_1\omega_2}\langle\langle\hat\Omega;\hat V^{\omega_1}_\beta,\hat V^{\omega_2}_\gamma\rangle\rangle F^{\omega_1}_\beta F^{\omega_2}_\gamma e^{-i(\omega_1+\omega_2)t}
+ \tfrac16\sum_{\omega_1\omega_2\omega_3}\langle\langle\hat\Omega;\hat V^{\omega_1}_\beta,\hat V^{\omega_2}_\gamma,\hat V^{\omega_3}_\delta\rangle\rangle F^{\omega_1}_\beta F^{\omega_2}_\gamma F^{\omega_3}_\delta e^{-i(\omega_1+\omega_2+\omega_3)t} + \cdots
\label{kubo}
$$

(the factors $e^{n\epsilon t}$ are dropped). This *defines* the linear, quadratic and cubic response functions. The frequency of the induced oscillation is $\omega_\sigma = \sum_k\omega_k$.

**Electric properties.** For $\hat\Omega = \hat\mu_\alpha$ and $\hat V^\omega_\beta = -\hat\mu_\beta$, the dipole moment

$$
\mu_\alpha(t) = \mu^0_\alpha + \sum_\omega\alpha_{\alpha\beta}(-\omega;\omega)F^\omega_\beta e^{-i\omega t} + \tfrac12\sum_{\omega_1\omega_2}\beta_{\alpha\beta\gamma}(-\omega_\sigma;\omega_1,\omega_2)F^{\omega_1}_\beta F^{\omega_2}_\gamma e^{-i\omega_\sigma t} + \tfrac16\sum\gamma_{\alpha\beta\gamma\delta}(-\omega_\sigma;\omega_1,\omega_2,\omega_3)F^{\omega_1}_\beta F^{\omega_2}_\gamma F^{\omega_3}_\delta e^{-i\omega_\sigma t}+\cdots
$$

defines the polarizability and hyperpolarizabilities, with

$$
\alpha = \langle\langle\hat\mu;-\hat\mu\rangle\rangle,\qquad \beta = \langle\langle\hat\mu;-\hat\mu,-\hat\mu\rangle\rangle,\qquad \gamma = \langle\langle\hat\mu;-\hat\mu,-\hat\mu,-\hat\mu\rangle\rangle.
$$

The first argument, $-\omega_\sigma$, carries a minus sign so that all frequencies add to zero (energy conservation in the photon picture). Three bookkeeping facts:

- **Intrinsic symmetry.** Interchanging the pairs $(\beta,\omega_1)$, $(\gamma,\omega_2)$, … does not change $\mu(t)$, so the tensors are *chosen* symmetric under it.
- **Reality.** Real fields and real $\mu(t)$ give $\alpha(\omega;-\omega) = [\alpha(-\omega;\omega)]^*$ and the same for $\beta$, $\gamma$ with all frequencies reversed.
- **Static limit.** For a static field, $E(F) = E_0 - \mu^0F - \tfrac12\alpha F^2 - \tfrac16\beta F^3 - \tfrac1{24}\gamma F^4 - \cdots$, the energy-derivative definition of [[molecular-properties-and-response]].

## Perturbation theory in projection amplitudes

**Amplitude equations.** Write $|\psi(t)\rangle = \sum_n d_n(t)e^{-iE_nt}|n\rangle$ with $d_n(-\infty) = \delta_{n0}$. The Schrödinger equation projected on $\langle m|$ gives $i\dot d_m = \sum_n V_{mn}(t)d_n e^{i\omega_{mn}t}$, solved order by order:

$$
d_m^{(N)}(t) = -i\int_{-\infty}^t\sum_n V_{mn}(t')\,d_n^{(N-1)}(t')\,e^{i\omega_{mn}t'}\,dt'.
$$

With $\hat V(t)$ of Eq. [[#vt]] each time integral is elementary because of the $e^{\epsilon t}$ factor:

$$
d_m^{(1)} = -\sum_{\omega_1}\frac{\langle m|\hat V^{\omega_1}_\beta|0\rangle F^{\omega_1}_\beta}{\omega_{m0}-\omega_1-i\epsilon}e^{i(\omega_{m0}-\omega_1)t},\qquad
d_m^{(2)} = \sum_{\omega_1\omega_2}\sum_n\frac{\langle m|\hat V^{\omega_1}_\beta|n\rangle\langle n|\hat V^{\omega_2}_\gamma|0\rangle F^{\omega_1}_\beta F^{\omega_2}_\gamma}{(\omega_{m0}-\omega_1-\omega_2-2i\epsilon)(\omega_{n0}-\omega_2-i\epsilon)}e^{i(\omega_{m0}-\omega_1-\omega_2)t}.
$$

Each further order adds one matrix element and one denominator with the accumulated frequency. This is the Dyson series of [[time-dependent-perturbation-theory]] evaluated for periodic fields.

**Linear response.** Inserting $|\psi^{(0)}\rangle$ and $|\psi^{(1)}\rangle$ into $\langle\psi|\hat\Omega|\psi\rangle$, using $F^{-\omega} = (F^\omega)^*$ to bring both terms to the factor $e^{-i\omega_1t}$, and comparing with Eq. [[#kubo]]:

$$
\langle\langle\hat\Omega;\hat V^\omega_\beta\rangle\rangle = -\sum_n\left[\frac{\langle0|\hat\Omega|n\rangle\langle n|\hat V^\omega_\beta|0\rangle}{\omega_{n0}-\omega-i\epsilon} + \frac{\langle0|\hat V^\omega_\beta|n\rangle\langle n|\hat\Omega|0\rangle}{\omega_{n0}+\omega+i\epsilon}\right].
\label{linear}
$$

The two $n = 0$ terms have denominators $\mp\omega$ and opposite signs, so they cancel and the sum may be primed. Away from resonances $\epsilon$ can be set to zero:

$$
\alpha_{\alpha\beta}(-\omega;\omega) = \sum_n{}'\left[\frac{\langle0|\hat\mu_\alpha|n\rangle\langle n|\hat\mu_\beta|0\rangle}{\omega_{n0}-\omega} + \frac{\langle0|\hat\mu_\beta|n\rangle\langle n|\hat\mu_\alpha|0\rangle}{\omega_{n0}+\omega}\right].
\label{alpha}
$$

At $\omega = \omega_{n0}$ the formula diverges. These are **resonances**, physical and not removable; they are the subject of [[residue-analysis-of-response-functions]] and [[damped-response-and-absorption-cross-sections]].

**Quadratic response.** The second-order expectation value collects $\langle\psi^{(0)}|\hat\Omega|\psi^{(2)}\rangle + \langle\psi^{(1)}|\hat\Omega|\psi^{(1)}\rangle + \langle\psi^{(2)}|\hat\Omega|\psi^{(0)}\rangle$. Made intrinsically symmetric with $\tfrac12\sum_{1,2}$ (sum over the two orderings of the pairs $(\beta,\omega_1)$, $(\gamma,\omega_2)$), it gives

$$
\langle\langle\hat\Omega;\hat V^{\omega_1}_\beta,\hat V^{\omega_2}_\gamma\rangle\rangle = \sum_{1,2}\sum_{np}\left[\frac{\Omega_{0n}V^{\omega_1}_{np}V^{\omega_2}_{p0}}{(\omega_{n0}-\omega_\sigma)(\omega_{p0}-\omega_2)} + \frac{V^{\omega_1}_{0n}\Omega_{np}V^{\omega_2}_{p0}}{(\omega_{n0}+\omega_1)(\omega_{p0}-\omega_2)} + \frac{V^{\omega_2}_{0p}V^{\omega_1}_{pn}\Omega_{n0}}{(\omega_{n0}+\omega_\sigma)(\omega_{p0}+\omega_2)}\right]
$$

with $X_{mn} = \langle m|\hat X|n\rangle$ and $\epsilon\to0$ (valid when no one- or two-photon resonance is hit). For the dipole case the six terms are the six permutations of one term over the pairs $(\alpha,-\omega_\sigma)$, $(\beta,\omega_1)$, $(\gamma,\omega_2)$, written $\sum_{-\sigma,1,2}$:

$$
\beta_{\alpha\beta\gamma}(-\omega_\sigma;\omega_1,\omega_2) = \sum_{-\sigma,1,2}\sum_{np}\frac{\langle0|\hat\mu_\alpha|n\rangle\langle n|\hat\mu_\beta|p\rangle\langle p|\hat\mu_\gamma|0\rangle}{(\omega_{n0}-\omega_\sigma)(\omega_{p0}-\omega_2)}.
\label{betafull}
$$

So in the nonresonant region $\beta$ has **full permutation symmetry**, including the pair carrying $-\omega_\sigma$.

## Secular divergences and the fluctuation operator

**The problem.** In Eq. [[#betafull]] the terms with $n = 0$ or $p = 0$ have denominators $\omega_\sigma$ or $\omega_2$, which vanish for static fields although nothing physical diverges. These are **secular divergences**: an artefact of letting the ground state appear as an intermediate.

**Removing them.** Split off the $n = 0$ and $p = 0$ terms. The term with both equal to zero, $\mu_{00}^3/(\omega_\sigma\omega_2)$, cancels in the permutation sum because $1/(\omega_\sigma\omega_2) = 1/(\omega_1\omega_2) - 1/(\omega_\sigma\omega_1)$ and the six permutations then cancel pairwise. In the two single-zero terms, relabel the pairs inside the full permutation sum so that both carry the same numerator $\mu_{0n}\mu_{00}\mu_{n0}$. Their denominators then combine into $-1/[(\omega_{n0}-\omega_\sigma)(\omega_{n0}-\omega_2)]$, which is exactly the $p = n$ term generated by replacing the middle $\mu_{np}$ by $\mu_{np} - \mu_{00}\delta_{np}$. The result is

$$
\beta_{\alpha\beta\gamma}(-\omega_\sigma;\omega_1,\omega_2) = \sum_{-\sigma,1,2}\sum_{np}{}'\frac{\langle0|\hat\mu_\alpha|n\rangle\langle n|\bar\mu_\beta|p\rangle\langle p|\hat\mu_\gamma|0\rangle}{(\omega_{n0}-\omega_\sigma)(\omega_{p0}-\omega_2)},\qquad \bar\mu = \hat\mu - \langle0|\hat\mu|0\rangle.
\label{beta}
$$

The fluctuation operator $\bar\mu$ carries the permanent dipole into the formula. In the $p = n$ terms it gives $\mu_{nn} - \mu_{00}$, the change of dipole on excitation.

**Cubic response.** The same steps applied to third order give

$$
\gamma_{\alpha\beta\gamma\delta}(-\omega_\sigma;\omega_1,\omega_2,\omega_3) = \sum_{-\sigma,1,2,3}\left[\sum_{nmp}{}'\frac{\mu^\alpha_{0n}\bar\mu^\beta_{nm}\bar\mu^\gamma_{mp}\mu^\delta_{p0}}{(\omega_{n0}-\omega_\sigma)(\omega_{m0}-\omega_2-\omega_3)(\omega_{p0}-\omega_3)} - \sum_{nm}{}'\frac{\mu^\alpha_{0n}\mu^\beta_{n0}\mu^\gamma_{0m}\mu^\delta_{m0}}{(\omega_{n0}-\omega_\sigma)(\omega_{m0}-\omega_3)(\omega_{m0}+\omega_2)}\right],
\label{gamma}
$$

summed over the 24 permutations of the four pairs. The second term is what is left of the secular terms after cancellation. It is the only term for a two-level system without permanent dipoles, where it gives the negative $\gamma$ seen below. Eqs. [[#alpha]], [[#beta]] and [[#gamma]] hold whenever no one-, two- or three-photon combination of the field frequencies is resonant, and also for static fields.

**General order.** The pattern continues: the $n$th-order property is a sum over permutations of $\langle0|\mu|a_1\rangle\langle a_1|\mu|a_2\rangle\cdots\langle a_n|\mu|0\rangle$ divided by $n$ denominators $(\omega_{a_1}-\omega_\sigma)(\omega_{a_2}-\omega_\sigma+\omega_1)\cdots(\omega_{a_n}-\omega_n)$.

## The phase-isolated wave function

**Why the divergences appear.** In first order, the $n = 0$ part of $|\psi^{(1)}\rangle$ is a purely imaginary multiple of $|\psi^{(0)}\rangle$: a phase change, which keeps the norm to first order but contributes nothing to expectation values. Carried into higher orders, such phase terms generate the secular denominators.

**Rotation amplitudes.** Write instead $|\psi(t)\rangle = e^{-i\phi(t)}|\tilde\psi(t)\rangle$ with the overall phase $\phi$ separated out, and parametrize the phase-isolated part by a unitary rotation,

$$
|\tilde\psi(t)\rangle = e^{-i\hat P(t)}|0\rangle,\qquad \hat P(t) = \sum_n{}'\big[P_n(t)|n\rangle\langle0| + P_n^*(t)|0\rangle\langle n|\big].
\label{rotation}
$$

$e^{-i\hat P}|0\rangle = |0\rangle\cos a - i\sum'_nP_n|n\rangle\,(\sin a)/a$ with $a^2 = \sum'|P_n|^2$, so the norm is kept for any $P_n$ and the projection on $|0\rangle$ is real. The state-transfer amplitudes $P_n$ are found from the Ehrenfest equation $\partial_t\langle\tilde\psi|\hat\Omega|\tilde\psi\rangle = -i\langle\tilde\psi|[\hat\Omega,\hat H]|\tilde\psi\rangle$ with $\hat\Omega = |0\rangle\langle n|$, order by order:

$$
P^{(1)}_n = -i\sum_\omega\frac{\langle n|\hat V^\omega_\beta|0\rangle F^\omega_\beta}{\omega_{n0}-\omega}e^{-i\omega t},\qquad
P^{(2)}_n = i\sum_{\omega_1\omega_2}\sum_m{}'\frac{\langle n|\bar V^{\omega_1}_\beta|m\rangle\langle m|\hat V^{\omega_2}_\gamma|0\rangle F^{\omega_1}_\beta F^{\omega_2}_\gamma}{(\omega_{n0}-\omega_1-\omega_2)(\omega_{m0}-\omega_2)}e^{-i(\omega_1+\omega_2)t}.
$$

All sums are primed and the fluctuation operator appears by itself, so the expectation values give Eqs. [[#alpha]], [[#beta]] and [[#gamma]] directly. The price is that the higher-order rotation amplitudes are more tedious to derive than the projection amplitudes. The parametrization of Eq. [[#rotation]] is the one that carries over to approximate wave functions, where $\hat P$ is replaced by orbital and configuration rotations ([[linear-response-for-variational-wave-functions]]).

## Worked example

!!! example "Five-state model: sum-over-states vs exact (computed for this note)"
    $E = (0, 0.541426, 0.881331, 1.009333, 1.112632)$, a random real symmetric $\mu_z$ matrix with permanent dipoles ($\mu_{00} = -0.272802$), one Cartesian component.

    **Static.** Exact derivatives of the lowest eigenvalue of $H_0 - \mu F$, from a Cauchy contour integral in complex $F$, against Eqs. [[#alpha]], [[#beta]] and [[#gamma]] at zero frequency:

    | | exact $-k!\,c_k$ | sum over states |
    |---|---:|---:|
    | $\mu$ | −0.2728024711 | −0.2728024711 |
    | $\alpha$ | 0.8828879122 | 0.8828879122 |
    | $\beta$ | 2.4636294887 | 2.4636294887 |
    | $\gamma$ | 9.0632218238 | 9.0632218238 |

    **Dynamic.** The Floquet quasienergy of the state connected to $|0\rangle$ in $F_0\cos\omega t$ is $E_0 - \alpha F_0^2/4 - \gamma(-\omega;\omega,-\omega,\omega)F_0^4/64$ ([[quasienergy-and-time-dependent-variational-principle]]). At $\omega = 0.12$: $\alpha$ = 0.9277487519 (Floquet) and 0.9277487519 (Eq. [[#alpha]]); $\gamma$ = 12.26390443 and 12.26390441 (Eq. [[#gamma]]).

    **Processes.** At $\omega = 0.1$: $\beta(-2\omega;\omega,\omega)$ = 2.97338, $\beta(-\omega;\omega,0)$ = 2.61636 and $\beta(0;\omega,-\omega)$ = 2.61636. The last two are equal by full permutation symmetry (exchange $(\alpha,-\omega)$ with $(\gamma,0)$).

!!! example "Two-level atom (NRS Sec. 5.1)"
    $\Delta E = 0.5$, $\mu_{ab} = 1$, no permanent dipoles. The exact field-dependent ground energy $\tfrac12\Delta E - \sqrt{\Delta E^2/4 + \mu_{ab}^2F^2}$ (with $E_a = 0$) gives $\alpha = 2\mu_{ab}^2/\Delta E = 4$ and $\gamma = -24\mu_{ab}^4/\Delta E^3 = -192$. Only the second term of Eq. [[#gamma]] survives, hence the negative sign. At $\omega = 0.1$: $\alpha = 2\Delta E\mu_{ab}^2/(\Delta E^2-\omega^2) = 4.1667$, larger than the static value (normal dispersion).

## Limitations

- **Exact states.** The formulas need all excitation energies and transition moments, including the continuum. In practice the same functions are computed from an approximate reference by solving response equations, never by summing states ([[linear-response-for-variational-wave-functions]]).
- **Resonances.** With $\epsilon\to0$ the functions diverge at one- and multiphoton resonances. A finite lifetime must be added to describe absorption ([[damped-response-and-absorption-cross-sections]]).
- **Nuclear motion.** $|n\rangle$ are rovibronic states in principle. Restricting the sums to electronic states gives the electronic contribution only.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 5.1 (two-level atom, Eqs. (5.1)–(5.13)); Sec. 5.2, Eqs. (5.57)–(5.65); Sec. 5.3, Eqs. (5.78)–(5.88); Sec. 5.4, Eqs. (5.102)–(5.148); Sec. 5.5, Eqs. (5.149)–(5.205). The derivations are rewritten; the cancellation argument for the secular terms follows NRS Eqs. (5.185)–(5.187). The model calculations are in `Claude outputs/part4_response_batchA.py`, sections A and B.
