---
id: sudden-and-adiabatic-approximations
title: The sudden and adiabatic approximations
summary: The two extreme ways a Hamiltonian can change. If it changes much faster than the system can respond, the state is unchanged and must be re-expanded in the new eigenstates (sudden approximation). If it changes much more slowly, a system that starts in the nth eigenstate stays in the nth instantaneous eigenstate (adiabatic theorem). Covers the derivation and the condition ħ|⟨m|dH/dt|n⟩| ≪ (E_n − E_m)², with worked examples: an expanding well, tritium beta decay, a spin in a rotating field and the Landau-Zener avoided crossing.
status: in-progress
kind: derivation
level: intermediate
tags: [adiabatic-theorem, adiabatic-approximation, sudden-approximation, landau-zener, avoided-crossing, instantaneous-eigenstates, dynamic-phase, griffiths, sakurai]
prerequisites: [time-dependent-perturbation-theory, infinite-square-well, spin-one-half]
related: [berry-phase, two-level-systems-and-rabi-oscillations, born-oppenheimer-approximation, nonadiabatic-couplings, hellmann-feynman-and-virial-theorems]
order: 60
date: 2026-11-15
---

## Two time scales

Let the Hamiltonian change from $H_i$ to $H_f$ over a time $T$. The system has its own internal times, $\hbar/|E_n - E_m|$, set by the level spacings. Everything depends on the comparison:

| regime | condition | result |
|---|---|---|
| sudden | $T\ll\hbar/|E_n - E_m|$ | the state does not change; its expansion in eigenstates does |
| adiabatic | $T\gg\hbar/|E_n - E_m|$ | the state follows the instantaneous eigenstate |

The classical picture is a pendulum whose support is moved. Jerk it and the bob is left behind; move it gradually and the pendulum keeps swinging in the same way relative to the support.

## The sudden approximation

Over a vanishing interval the evolution operator tends to the identity (a finite Hamiltonian acting for zero time does nothing), so the wave function just after the change equals the one just before. If the system was in the eigenstate $\psi_i$ of the old Hamiltonian, then in terms of the eigenstates $\phi_n$ of the new one

$$
\boxed{\,P_n = \big|\langle\phi_n|\psi_i\rangle\big|^2\,}
$$

The expectation value of any operator that did not itself change is continuous. The energy generally is not conserved; whoever changed the Hamiltonian did work.

!!! example "Three sudden changes"

    **A well that doubles.** A particle in the ground state of an infinite well of width $a$; the right wall jumps to $2a$. The overlaps with the new states $\sqrt{1/a}\sin(n\pi x/2a)$ are $c_2 = 1/\sqrt2$ and, for odd $n$, $c_n = \pm4\sqrt2/[\pi(4 - n^2)]$, zero for other even $n$:

    | new $n$ | 1 | 2 | 3 | 4 | 5 |
    |---|---|---|---|---|---|
    | $P_n$ | 0.3603 | 0.5000 | 0.1297 | 0 | 0.0074 |

    The most likely result of an energy measurement is the new $n = 2$ level, which has the same energy as the old ground state, and $\langle H\rangle = \pi^2\hbar^2/2ma^2$ is unchanged: the wall moved away without doing work, as in the free expansion of a gas.

    **A spring that stiffens.** An oscillator in its ground state, $\omega\to\omega'$. The probability of remaining in the ground state is $2\sqrt{\omega\omega'}/(\omega + \omega')$, which is $2\sqrt2/3 = 0.943$ for $\omega' = 2\omega$.

    **Beta decay of tritium.** The nuclear charge changes from $Z = 1$ to $Z = 2$ in a time far shorter than the orbital period of the atomic electron. The electron, initially in the hydrogen-like $1s$ state, is found in the $1s$ state of He$^+$ with probability

    $$
    \big|\langle1s,Z{=}2\,|\,1s,Z{=}1\rangle\big|^2 = \Big(\frac{2\sqrt{Z_1Z_2}}{Z_1 + Z_2}\Big)^6 = \frac{512}{729} = 0.702 ,
    $$

    in $2s$ with probability 0.250, and otherwise in higher states or the continuum. The same reasoning gives "shake-up" and "shake-off" satellites in photoelectron spectra.

## The adiabatic theorem

Let $H(t)$ have instantaneous eigenstates and eigenvalues,

$$
H(t)\,\psi_n(t) = E_n(t)\,\psi_n(t) ,
$$

assumed discrete and nondegenerate throughout. The **adiabatic theorem** states that if the system starts in $\psi_n(0)$ and $H$ changes slowly enough, it is found at time $t$ in $\psi_n(t)$, up to a phase:

$$
\Psi_n(t) = e^{i\theta_n(t)}\,e^{i\gamma_n(t)}\,\psi_n(t) ,\qquad \theta_n(t) = -\frac1\hbar\int_0^tE_n(t')\,dt' .
$$

$\theta_n$ is the **dynamic phase**, the generalization of $-E_nt/\hbar$. The second phase, $\gamma_n$, is the geometric phase, treated in [[berry-phase]].

**Derivation.** Expand the exact solution in the instantaneous eigenstates,

$$
\Psi(t) = \sum_nc_n(t)\,e^{i\theta_n(t)}\,\psi_n(t) .
$$

Substituting into the Schrödinger equation, the terms with $E_n$ cancel against the derivative of the dynamic phase, leaving $\sum_n e^{i\theta_n}[\dot c_n\psi_n + c_n\dot\psi_n] = 0$. The inner product with $\psi_m$ gives

$$
\dot c_m = -\sum_nc_n\,e^{i(\theta_n - \theta_m)}\,\langle\psi_m|\dot\psi_n\rangle .
$$

To evaluate $\langle\psi_m|\dot\psi_n\rangle$ for $m\ne n$, differentiate the eigenvalue equation with respect to time and project on $\psi_m$:

$$
\langle\psi_m|\dot H|\psi_n\rangle = (E_n - E_m)\,\langle\psi_m|\dot\psi_n\rangle\qquad(m\ne n) .
$$

Therefore, exactly,

$$
\boxed{\,\dot c_m = -c_m\langle\psi_m|\dot\psi_m\rangle - \sum_{n\ne m}c_n\,\frac{\langle\psi_m|\dot H|\psi_n\rangle}{E_n - E_m}\,e^{i(\theta_n - \theta_m)}\,}
$$

The adiabatic approximation drops the sum. Then $c_m(t) = c_m(0)\,e^{i\gamma_m(t)}$ with

$$
\gamma_m(t) = i\int_0^t\langle\psi_m(t')|\dot\psi_m(t')\rangle\,dt' ,
$$

which is real because $\langle\psi_m|\dot\psi_m\rangle$ is purely imaginary (differentiate $\langle\psi_m|\psi_m\rangle = 1$). Only the phase of each coefficient changes, so the populations of the instantaneous eigenstates are constant.

**Condition.** The dropped terms are small if $H$ changes little during the internal period $\hbar/|E_n - E_m|$:

$$
\hbar\,\big|\langle\psi_m|\dot H|\psi_n\rangle\big|\ll(E_n - E_m)^2\qquad\text{for all }m\ne n .
$$

The phase factor $e^{i(\theta_n - \theta_m)}$ helps: it oscillates at the transition frequency, so a slowly varying coupling averages out. The condition fails wherever two levels approach each other. At an exact crossing the theorem says nothing.

**Energy.** In an adiabatic process the system stays in the level $E_n(t)$, so its energy changes by the work done on it. If the well of the first example expands slowly instead, the particle remains in the ground state and its energy falls from $\pi^2\hbar^2/2ma^2$ to $\pi^2\hbar^2/8ma^2$: it does work on the receding wall, like a gas in a slowly expanding cylinder. The rate of change is $dE_n/dt = \langle\psi_n|\dot H|\psi_n\rangle$ ([[hellmann-feynman-and-virial-theorems]]).

## Two exactly solvable tests

!!! example "Spin in a field that sweeps a cone"

    An electron at rest in a magnetic field of fixed magnitude whose direction rotates about the $z$ axis at angular velocity $\omega$, at a fixed angle $\alpha$ from the axis. The Hamiltonian is $H = \tfrac12\hbar\omega_1\,\hat{\mathbf n}(t)\cdot\boldsymbol\sigma$ with $\omega_1 = eB_0/m$, and its instantaneous eigenstates are spin up and spin down along $\hat{\mathbf n}(t)$, with energies $\pm\tfrac12\hbar\omega_1$. The time-dependent Schrödinger equation can be solved exactly. Starting spin up along the field, the probability of being found spin down along the current field direction is

    $$
    P_{\rm flip}(t) = \Big[\frac{\omega}{\lambda}\sin\alpha\,\sin\frac{\lambda t}{2}\Big]^2 ,\qquad \lambda = \sqrt{\omega^2 + \omega_1^2 - 2\omega\omega_1\cos\alpha} .
    $$

    Numerical integration for $\alpha = 60^\circ$ reproduces this to $10^{-11}$:

    | $\omega/\omega_1$ | 0.02 | 0.1 | 0.5 | 2 |
    |---|---|---|---|---|
    | max $P_{\rm flip}$ | 0.00031 | 0.0082 | 0.250 | 1.000 |

    In the adiabatic regime $\omega\ll\omega_1$ the spin follows the field and $P_{\rm flip}\approx(\omega\sin\alpha/\omega_1)^2\to0$. The internal frequency is the Larmor frequency $\omega_1$, and the condition is that the field turns slowly compared with the precession.

!!! example "Landau-Zener avoided crossing"

    Two states whose unperturbed energies cross linearly in time, coupled by a constant $\Delta$:

    $$
    H(t) = \begin{pmatrix}\tfrac12\alpha t & \Delta\\ \Delta & -\tfrac12\alpha t\end{pmatrix} ,\qquad E_\pm(t) = \pm\sqrt{(\alpha t/2)^2 + \Delta^2} .
    $$

    The instantaneous levels do not cross; they approach to a minimum gap $2\Delta$ at $t = 0$ and exchange character there. Starting in the lower level at $t\to-\infty$, the probability of ending in the upper level is

    $$
    P_{\rm jump} = \exp\Big(-\frac{2\pi\Delta^2}{\hbar\alpha}\Big) .
    $$

    Numerical integration from $t = -200/\sqrt\alpha$ to $+200/\sqrt\alpha$ ($\hbar = 1$), projecting on the instantaneous eigenstates:

    | gap $2\Delta$ | sweep rate $\alpha$ | $P_{\rm jump}$ numerical | formula |
    |---|---|---|---|
    | 0.2 | 1 | 0.93910 | 0.93910 |
    | 0.5 | 1 | 0.67523 | 0.67523 |
    | 1.0 | 1 | 0.20788 | 0.20788 |
    | 1.0 | 0.25 | 0.00187 | 0.00187 |
    | 2.0 | 1 | 0.00187 | 0.00187 |

    A slow sweep or a large gap keeps the system on its adiabatic level. A fast sweep or a small gap carries it straight through, as if the levels crossed. The exponent is the adiabatic condition in quantitative form: the gap squared against $\hbar$ times the rate at which the unperturbed levels separate.

## Where it matters

The Born-Oppenheimer separation is an adiabatic approximation: the electrons, with their large level spacings, follow the slow nuclei and stay on one potential energy surface ([[born-oppenheimer-approximation]]). It breaks down where surfaces approach each other, which is the Landau-Zener situation, and the transitions there are governed by [[nonadiabatic-couplings]], the matrix elements $\langle\psi_m|\dot\psi_n\rangle$ of this note with nuclear coordinates as the slow parameters.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 11.5, Eqs. (11.89)-(11.107), Example 11.3 (expanding well), Example 11.4 (electron in a rotating field; exact solution (11.103)-(11.106)); Problems 11.18 (well suddenly doubled), 11.19 (spring constant suddenly quadrupled), 11.20. Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 5.6.1, pp. 327-328 (sudden approximation, Eq. (5.213), tritium decay mentioned); Problem 5.42, p. 368 (tritium); Sec. 5.6.2, pp. 328-331, Eqs. (5.214)-(5.229) (adiabatic approximation, the exact equation (5.221) and the condition (5.222)).

The Landau-Zener formula is not in either book; it was verified here by numerical integration. Original papers, quoted from memory and to verify: L. D. Landau, Phys. Z. Sowjetunion 2, 46 (1932); C. Zener, Proc. R. Soc. London A 137, 696 (1932). All numbers are computed in `griffiths/ch11_dynamics.py` (section E).
