---
id: time-dependent-perturbation-theory
title: Time-dependent perturbation theory
summary: Transition amplitudes to first and second order in a time-dependent perturbation, from the Dyson series. The first-order amplitude is the Fourier component of the perturbation at the transition frequency. Worked for a constant perturbation switched on at t = 0 and for a sinusoidal one (absorption and stimulated emission), with the conditions of validity, and tested on the forced harmonic oscillator, where the exact answer is a Poisson distribution.
status: in-progress
kind: derivation
level: intermediate
tags: [time-dependent-perturbation-theory, transition-probability, transition-amplitude, harmonic-perturbation, absorption, stimulated-emission, forced-oscillator, detailed-balance, griffiths, sakurai]
prerequisites: [interaction-picture-and-dyson-series, two-level-systems-and-rabi-oscillations, rayleigh-schrodinger-perturbation-theory]
related: [fermi-golden-rule-and-decay-width, emission-absorption-and-spontaneous-emission, harmonic-oscillator-coherent-states, energy-time-uncertainty-principle, sudden-and-adiabatic-approximations]
order: 30
date: 2026-11-15
---

## The expansion

Let $H = H_0 + V(t)$ with $H_0|n\rangle = E_n|n\rangle$, and let the system be in $|i\rangle$ at time $t_0$. The amplitude to be found in $|n\rangle$ at time $t$ is $c_n(t) = \langle n|U_I(t,t_0)|i\rangle$, and the Dyson series of [[interaction-picture-and-dyson-series]] gives $c_n = c_n^{(0)} + c_n^{(1)} + c_n^{(2)} + \cdots$ with

$$
c_n^{(0)} = \delta_{ni} ,
$$

$$
\boxed{\,c_n^{(1)}(t) = -\frac{i}{\hbar}\int_{t_0}^tV_{ni}(t')\,e^{i\omega_{ni}t'}\,dt'\,}\qquad \omega_{ni} = \frac{E_n - E_i}{\hbar} ,\quad V_{ni}(t) = \langle n|V(t)|i\rangle ,
$$

$$
c_n^{(2)}(t) = \Big(\!-\frac{i}{\hbar}\Big)^2\sum_m\int_{t_0}^tdt'\int_{t_0}^{t'}dt''\,e^{i\omega_{nm}t'}V_{nm}(t')\,e^{i\omega_{mi}t''}V_{mi}(t'') .
$$

The transition probability for $n\ne i$ is $P_{i\to n} = |c_n^{(1)} + c_n^{(2)} + \cdots|^2$.

**First order.** $c_n^{(1)}$ is, up to a factor, the Fourier component of the perturbation at the transition frequency $\omega_{ni}$. A perturbation causes a transition $i\to n$ only if (a) it connects the two states, $V_{ni}\ne0$, and (b) it contains the frequency $\omega_{ni}$. Condition (a) gives selection rules; condition (b) is energy conservation in the sense appropriate to a classical driving field.

**Second order.** The system goes from $i$ to $n$ through an intermediate state $m$, at times $t''<t'$. It matters when the direct matrix element $V_{ni}$ vanishes.

**Validity.** The expansion assumes the initial state is hardly depleted: $\sum_{n\ne i}|c_n^{(1)}|^2\ll1$.

## Constant perturbation

Let $V$ be switched on at $t = 0$ and constant afterwards. Then

$$
c_n^{(1)} = \frac{V_{ni}}{E_n - E_i}\big(1 - e^{i\omega_{ni}t}\big) ,\qquad P_{i\to n}(t) = \frac{4|V_{ni}|^2}{(E_n - E_i)^2}\,\sin^2\!\Big[\frac{(E_n - E_i)\,t}{2\hbar}\Big] .
$$

- For a given final state the probability oscillates in time and never grows beyond $4|V_{ni}|^2/(E_n - E_i)^2$, which is the square of twice the first-order mixing coefficient of time-independent perturbation theory ([[rayleigh-schrodinger-perturbation-theory]]): the state sloshes between $|i\rangle$ and the perturbed eigenstate.
- As a function of the final energy, $P$ is a peak of height $|V_{ni}|^2t^2/\hbar^2$ at $E_n = E_i$ and width $\Delta E\approx2\pi\hbar/t$. After a time $t$, energy is conserved only to within about $\hbar/t$ ([[energy-time-uncertainty-principle]]).
- The area under the peak grows linearly with $t$. For a continuum of final states this gives a constant transition **rate** ([[fermi-golden-rule-and-decay-width]]).

## Sinusoidal perturbation

Write a general harmonic perturbation, switched on at $t = 0$, as

$$
V(t) = \mathcal V\,e^{i\omega t} + \mathcal V^\dagger e^{-i\omega t} .
$$

Then

$$
c_n^{(1)}(t) = \frac1\hbar\Big[\frac{1 - e^{i(\omega_{ni} + \omega)t}}{\omega_{ni} + \omega}\,\mathcal V_{ni} + \frac{1 - e^{i(\omega_{ni} - \omega)t}}{\omega_{ni} - \omega}\,\mathcal V^\dagger_{ni}\Big] .
$$

This is the constant-perturbation result with $\omega_{ni}\to\omega_{ni}\pm\omega$. After a long time only one of the two terms can be large:

| condition | process | dominant term |
|---|---|---|
| $E_n\approx E_i + \hbar\omega$ | absorption of a quantum $\hbar\omega$ | $\mathcal V^\dagger_{ni}$ |
| $E_n\approx E_i - \hbar\omega$ | stimulated emission | $\mathcal V_{ni}$ |

Near either resonance, keeping the dominant term,

$$
P_{i\to n}(t)\approx\frac{4|\mathcal V_{ni}|^2}{\hbar^2}\,\frac{\sin^2[(\omega_{ni}\mp\omega)t/2]}{(\omega_{ni}\mp\omega)^2} .
$$

For a real perturbation $V\cos\omega t$, $\mathcal V = V/2$ and this is Griffiths' $P = |V_{ab}|^2\sin^2[(\omega_0 - \omega)t/2]/[\hbar^2(\omega_0 - \omega)^2]$.

Since $|\mathcal V_{ni}|^2 = |\mathcal V^\dagger_{in}|^2$, the probability of $i\to n$ by emission equals that of $n\to i$ by absorption: **detailed balance**.

On resonance the first-order probability grows as $(|\mathcal V_{ni}|t/\hbar)^2$ without limit, so the result holds only for $t\ll\hbar/|\mathcal V_{ni}|$. The exact two-level treatment shows what really happens: Rabi oscillations ([[two-level-systems-and-rabi-oscillations]]).

## A test with an exact answer

!!! example "Harmonic oscillator pushed by a pulse"

    $H = \hbar\omega(a^\dagger a + \tfrac12) - F(t)\,x$ with $F(t) = F_0\,e^{-t^2/\tau^2}$, starting in the ground state at $t = -\infty$.

    **First order.** Since $\langle n|x|0\rangle = \sqrt{\hbar/2m\omega}\;\delta_{n1}$, only $0\to1$ is possible:

    $$
    c_1^{(1)} = \frac{i}{\hbar}\sqrt{\frac{\hbar}{2m\omega}}\int_{-\infty}^\infty F_0\,e^{-t^2/\tau^2}e^{i\omega t}\,dt ,\qquad P_{0\to1}^{(1)} = \mu\equiv\frac{\pi F_0^2\tau^2}{2m\hbar\omega}\,e^{-\omega^2\tau^2/2} .
    $$

    **Second order.** $0\to1\to2$ gives $P_{0\to2}^{(2)} = \mu^2/2$.

    **Exact.** A forced oscillator that starts in the ground state ends in a coherent state ([[harmonic-oscillator-coherent-states]]), so the final distribution is Poisson with mean $\mu$: $P_{0\to n} = e^{-\mu}\mu^n/n!$.

    Numerical integration in a basis of 60 oscillator states ($\hbar = m = \omega = 1$) reproduces the Poisson values to all digits shown:

    | $F_0$ | $\tau$ | $\mu$ | $P_{0\to1}$ first order | $P_{0\to1}$ exact | $P_{0\to2}$ second order | $P_{0\to2}$ exact |
    |---|---|---|---|---|---|---|
    | 0.1 | 1.0 | 0.00953 | 0.00953 | 0.00944 | 0.00005 | 0.00004 |
    | 0.5 | 1.0 | 0.2382 | 0.2382 | 0.1877 | 0.0284 | 0.0224 |
    | 1.5 | 1.0 | 2.144 | 2.144 | 0.2513 | 2.298 | 0.2693 |
    | 1.5 | 0.2 | 0.1386 | 0.1386 | 0.1206 | 0.0096 | 0.0084 |
    | 1.5 | 5.0 | 0.00033 | 0.00033 | 0.00033 | 0.00000 | 0.00000 |

    Perturbation theory gives the leading term of $e^{-\mu}\mu^n/n!$ in each channel, and is accurate when $\mu\ll1$. Two limits are instructive. A pulse much shorter than the period ($\omega\tau\ll1$) is an impulse, and $\mu\propto(F_0\tau)^2$ depends only on the momentum delivered. A pulse much longer than the period ($\omega\tau\gg1$) is adiabatic: the oscillator follows the slowly moving equilibrium position and returns to its ground state, with $\mu$ exponentially small, however strong the force ([[sudden-and-adiabatic-approximations]]).

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 11.1.2, Eqs. (11.19)-(11.28); Sec. 11.1.3, Eqs. (11.29)-(11.36); Problems 11.6 and 11.7 (second order), 11.24 (multi-level systems), 11.36 (driven oscillator). Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 5.7.2, pp. 339-340 (amplitudes (5.276), probability (5.278)); Sec. 5.7.3, pp. 341-345 (constant perturbation, Eqs. (5.279)-(5.284), second order (5.295)); Sec. 5.7.4, pp. 345-346 (harmonic perturbation, Eqs. (5.298)-(5.306), detailed balancing).

The Gaussian-pulse example and its numbers are my own (the exactness of the Poisson distribution is the content of Griffiths' Problem 11.36), computed in `griffiths/ch11_dynamics.py` (section B).
