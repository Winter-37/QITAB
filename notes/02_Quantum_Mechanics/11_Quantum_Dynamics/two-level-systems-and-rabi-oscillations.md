---
id: two-level-systems-and-rabi-oscillations
title: Two-level systems and Rabi oscillations
summary: The simplest time-dependent problem. Two stationary states coupled by a perturbation obey a pair of exact first-order equations for their amplitudes. For a sinusoidal coupling near resonance the rotating-wave approximation gives Rabi's formula, a complete periodic exchange of population at the flopping frequency. Compared with the exact numerical solution and with first-order perturbation theory, and applied to spin magnetic resonance, where a rotating field makes the formula exact.
status: in-progress
kind: derivation
level: intermediate
tags: [two-level-system, rabi-oscillations, rotating-wave-approximation, magnetic-resonance, time-dependent-hamiltonian, pi-pulse, resonance, griffiths, sakurai]
prerequisites: [stationary-states, spin-one-half]
related: [interaction-picture-and-dyson-series, time-dependent-perturbation-theory, emission-absorption-and-spontaneous-emission, sudden-and-adiabatic-approximations]
order: 10
date: 2026-11-15
---

## Why time dependence is different

If the Hamiltonian does not depend on time, a system in a stationary state stays there forever: probabilities are constant and only phases evolve ([[stationary-states]]). **Transitions** between energy levels require a time-dependent Hamiltonian. The cleanest setting is a system with just two states that matter.

## The exact two-level equations

Let $H^0$ have orthonormal eigenstates $\psi_a$, $\psi_b$ with energies $E_a<E_b$ and transition frequency

$$
\omega_0 = \frac{E_b - E_a}{\hbar} .
$$

With a perturbation $H'(t)$ switched on, the state is still a combination of the two, but with time-dependent coefficients:

$$
\Psi(t) = c_a(t)\,\psi_a\,e^{-iE_at/\hbar} + c_b(t)\,\psi_b\,e^{-iE_bt/\hbar} ,\qquad |c_a|^2 + |c_b|^2 = 1 .
$$

The stationary-state phases have been factored out, so that $c_a$ and $c_b$ are constant when $H' = 0$. Substituting into $i\hbar\,\partial\Psi/\partial t = (H^0 + H')\Psi$ and taking inner products with $\psi_a$ and $\psi_b$ gives, for the usual case in which the diagonal elements $H'_{aa}$, $H'_{bb}$ vanish,

$$
\boxed{\,\dot c_a = -\frac{i}{\hbar}H'_{ab}\,e^{-i\omega_0t}\,c_b ,\qquad \dot c_b = -\frac{i}{\hbar}H'_{ba}\,e^{i\omega_0t}\,c_a\,}\qquad H'_{ij} = \langle\psi_i|H'|\psi_j\rangle .
$$

These equations are exact. (Nonzero diagonal elements only add phases to the amplitudes and shift the effective $\omega_0$.) They are the two-state case of the interaction-picture equations in [[interaction-picture-and-dyson-series]].

## Sinusoidal coupling and the rotating-wave approximation

Take $H'_{ab} = V_{ab}\cos\omega t$ and start in the lower state, $c_a(0) = 1$, $c_b(0) = 0$. Writing $\cos\omega t = \tfrac12(e^{i\omega t} + e^{-i\omega t})$, the equation for $c_b$ contains

$$
e^{i\omega_0t}\cos\omega t = \tfrac12\Big[e^{i(\omega_0 - \omega)t} + e^{i(\omega_0 + \omega)t}\Big] .
$$

Near resonance, $\omega\approx\omega_0$, the first term varies slowly and the second oscillates at about $2\omega_0$, averaging to nearly zero over the time in which $c_a$ and $c_b$ change. Dropping it (and the corresponding term in the other equation) is the **rotating-wave approximation**:

$$
\dot c_a = -\frac{i}{2\hbar}V_{ab}\,e^{-i(\omega_0 - \omega)t}\,c_b ,\qquad \dot c_b = -\frac{i}{2\hbar}V_{ba}\,e^{i(\omega_0 - \omega)t}\,c_a .
$$

Differentiating the second and eliminating $c_a$,

$$
\ddot c_b - i(\omega_0 - \omega)\,\dot c_b + \frac{|V_{ab}|^2}{4\hbar^2}\,c_b = 0 ,
$$

a linear equation with constant coefficients. With the initial conditions,

$$
c_b(t) = -\frac{iV_{ba}}{2\hbar\omega_r}\,e^{i(\omega_0 - \omega)t/2}\sin\omega_rt ,\qquad \omega_r = \tfrac12\sqrt{(\omega - \omega_0)^2 + \big(|V_{ab}|/\hbar\big)^2} ,
$$

and the transition probability is **Rabi's formula**:

$$
\boxed{\,P_{a\to b}(t) = \frac{(|V_{ab}|/\hbar)^2}{(\omega - \omega_0)^2 + (|V_{ab}|/\hbar)^2}\,\sin^2\omega_rt\,}
$$

$\omega_r$ is the **Rabi flopping frequency**.

**Reading the formula.**

- On resonance the population oscillates completely between the two states, $P = \sin^2(|V_{ab}|t/2\hbar)$, however weak the coupling. A pulse of duration $t_\pi = \pi\hbar/|V_{ab}|$ (a "$\pi$ pulse") inverts the population; half that duration leaves an equal superposition.
- Off resonance the oscillation is faster and incomplete. The maximum probability, as a function of $\omega$, is a Lorentzian of full width $2|V_{ab}|/\hbar$ at half maximum: a stronger field broadens the resonance.
- The probability never exceeds 1, and the same result holds starting from the upper state: absorption and stimulated emission are equally probable.
- For $|V_{ab}|/\hbar\ll|\omega - \omega_0|$ it reduces to the first-order result of [[time-dependent-perturbation-theory]], $P\approx|V_{ab}|^2\sin^2[(\omega_0 - \omega)t/2]/[\hbar^2(\omega_0 - \omega)^2]$.

**An exactly solvable variant.** If the coupling is $H'_{ab} = \gamma e^{i\omega t}$, $H'_{ba} = \gamma e^{-i\omega t}$ (a rotating rather than oscillating perturbation), no term has to be dropped and the same steps give the result exactly. This is the form treated by Sakurai; it corresponds to $\gamma = V_{ab}/2$ above.

!!! example "How good is the rotating-wave approximation?"

    Numerical integration of the exact two-level equations with $H'_{ab} = V\cos\omega t$, in units $\hbar = \omega_0 = 1$, over one Rabi period:

    | $V$ | $\omega$ | $\omega_r$ | max $P$, exact | max $P$, Rabi | max $|P_{\rm exact} - P_{\rm Rabi}|$ | max $P$, first order |
    |---|---|---|---|---|---|---|
    | 0.05 | 1.0 | 0.0250 | 0.9998 | 1 | 0.013 | 39.5 |
    | 0.05 | 1.1 | 0.0559 | 0.2017 | 0.2000 | 0.018 | 0.250 |
    | 0.2 | 1.0 | 0.1000 | 0.9975 | 1 | 0.058 | 39.5 |
    | 0.2 | 1.2 | 0.1414 | 0.5206 | 0.5000 | 0.097 | 1.000 |
    | 0.5 | 1.0 | 0.2500 | 0.9826 | 1 | 0.145 | 39.5 |

    The dropped counter-rotating term produces a small fast ripple on the Rabi curve, of relative size about $V/(4\hbar\omega_0)$ on resonance. First-order perturbation theory, by contrast, grows as $(Vt/2\hbar)^2$ on resonance and is meaningless once it approaches 1 (the 39.5 is its value after one Rabi period).

## Spin magnetic resonance

A spin-$\tfrac12$ particle with gyromagnetic ratio $\gamma_g$ has $H = -\gamma_g\,\mathbf B\cdot\mathbf S$ ([[spin-one-half]]). In a static field $B_0\hat{\mathbf z}$ the two levels are split by $\hbar\omega_0$ with $\omega_0 = \gamma_gB_0$, the Larmor frequency, and for $\gamma_g>0$ spin up is the lower state. Add a weak field of magnitude $B_1$ rotating in the $xy$ plane:

$$
\mathbf B = B_0\,\hat{\mathbf z} + B_1\big(\cos\omega t\,\hat{\mathbf x} - \sin\omega t\,\hat{\mathbf y}\big) .
$$

Then $\langle\uparrow|H|\downarrow\rangle = -\tfrac12\hbar\gamma_gB_1\,e^{i\omega t}$, which is exactly the rotating coupling above. The spin-flip probability is therefore exactly

$$
P_{\uparrow\to\downarrow}(t) = \frac{\Omega^2}{\Omega^2 + (\omega - \omega_0)^2}\,\sin^2\!\Big(\tfrac12\sqrt{\Omega^2 + (\omega - \omega_0)^2}\;t\Big) ,\qquad \Omega = \gamma_gB_1 .
$$

A numerical integration with $\gamma_g = B_0 = 1$, $B_1 = 0.1$ agrees with this to $10^{-9}$ at $\omega = 1$ and $\omega = 1.15$ (maximum 0.3077). The sense of rotation matters: the field above rotates clockwise seen from $+z$, the same way the spin precesses. A field rotating the other way gives a maximum flip probability of only 0.0025.

In practice the transverse field oscillates along a fixed axis, $2B_1\cos\omega t\,\hat{\mathbf x}$. That is the sum of two counter-rotating fields, of which only the one rotating with the spin is resonant. Neglecting the other is the rotating-wave approximation again.

This is the principle of nuclear magnetic resonance and electron spin resonance: the absorption peak at $\omega = \gamma_gB_0$ measures the local field or the magnetic moment, and $\pi$ and $\pi/2$ pulses prepare chosen spin states. The same two-level dynamics drives the ammonia maser and optical transitions in atoms ([[emission-absorption-and-spontaneous-emission]]).

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 11.1.1, Eqs. (11.5)-(11.18); Sec. 11.1.3, Eqs. (11.29)-(11.37); Problem 11.9 (Rabi flopping in the rotating-wave approximation, flopping frequency (11.37)) and Problem 11.29 (magnetic resonance). Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 5.5.3, pp. 323-325 (exact two-state problem, Rabi's formula (5.193), resonance condition (5.196)); Sec. 5.5.4, pp. 325-326 (spin magnetic resonance); Sec. 5.5.5, pp. 326-327 (maser).

The numerical comparison and the check of the sense of rotation are my own, computed in `griffiths/ch11_dynamics.py` (section A).
