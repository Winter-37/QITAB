---
id: fermi-golden-rule-and-decay-width
title: Fermi's golden rule, decay width and level shift
summary: When the final states form a continuum, first-order perturbation theory gives a transition rate that is constant in time, w = (2π/ħ)|V|²ρ(E). Covers the derivation and its window of validity, the density of states, the Born cross section as an application, and the fate of the initial state at longer times: exponential decay with width Γ = ħw, a level shift from second order, and a Lorentzian line shape. All of it is checked on a model of one level coupled to a dense band.
status: in-progress
kind: derivation
level: advanced
tags: [fermi-golden-rule, transition-rate, density-of-states, exponential-decay, decay-width, level-shift, lorentzian-line-shape, lifetime, quantum-zeno, griffiths, sakurai]
prerequisites: [time-dependent-perturbation-theory, free-particle-and-wave-packets]
related: [emission-absorption-and-spontaneous-emission, born-approximation-and-lippmann-schwinger, low-energy-scattering-and-resonances, energy-time-uncertainty-principle, rayleigh-schrodinger-perturbation-theory]
order: 40
date: 2026-11-15
---

## From probability to rate

For a constant perturbation switched on at $t = 0$, first-order theory gives ([[time-dependent-perturbation-theory]])

$$
P_{i\to n}(t) = \frac{4|V_{ni}|^2}{(E_n - E_i)^2}\sin^2\!\Big[\frac{(E_n - E_i)t}{2\hbar}\Big] .
$$

For a single final state this only oscillates. Suppose instead that the final states form a continuum (a free particle, a photon, a dense band of levels) with $\rho(E)\,dE$ states in the energy interval $dE$. The total probability of leaving $|i\rangle$ is

$$
P(t) = \int dE_n\,\rho(E_n)\,\frac{4|V_{ni}|^2}{(E_n - E_i)^2}\sin^2\!\Big[\frac{(E_n - E_i)t}{2\hbar}\Big] .
$$

As a function of $E_n$ the last factor is a peak at $E_n = E_i$ of width about $2\pi\hbar/t$. Once $t$ is large enough that $\rho|V_{ni}|^2$ hardly varies across the peak, it can be taken outside, and with $\int_{-\infty}^\infty\sin^2(xt/2)/x^2\,dx = \pi t/2$,

$$
P(t) = \frac{2\pi}{\hbar}\,|V_{ni}|^2\rho(E_i)\;t .
$$

The probability grows linearly, so there is a constant transition rate:

$$
\boxed{\,w_{i\to[n]} = \frac{2\pi}{\hbar}\,\big|V_{ni}\big|^2\,\rho(E_n)\Big|_{E_n = E_i}\,}
$$

This is **Fermi's golden rule**. It is often written per final state as $w_{i\to n} = (2\pi/\hbar)|V_{ni}|^2\delta(E_n - E_i)$, to be integrated over $\rho\,dE_n$.

**Harmonic perturbation.** For $V(t) = \mathcal Ve^{i\omega t} + \mathcal V^\dagger e^{-i\omega t}$ the same argument gives

$$
w_{i\to n} = \frac{2\pi}{\hbar}\,|\mathcal V^\dagger_{ni}|^2\,\delta(E_n - E_i - \hbar\omega)\ \ \text{(absorption)} ,\qquad \frac{2\pi}{\hbar}\,|\mathcal V_{ni}|^2\,\delta(E_n - E_i + \hbar\omega)\ \ \text{(emission)} .
$$

For a real perturbation $V\cos\omega t$ one has $\mathcal V = V/2$, which is the origin of the factor $|V_{if}/2|^2$ in Griffiths' statement of the rule.

**Window of validity.** Three time scales are involved.

- $t$ must be long enough for the peak to be narrow on the scale over which $\rho|V|^2$ varies, and (if the "continuum" is really a set of closely spaced levels) wide enough to cover many levels: $\hbar/\Delta E_{\rm band}\ll t\ll\hbar/\delta$.
- $t$ must be short enough that the initial state is not depleted: $wt\ll1$. The section on decay below removes this restriction.

## Density of states

For a free particle in a cube of side $L$ with periodic boundary conditions, the allowed wave vectors form a lattice of spacing $2\pi/L$. The number of states with $\mathbf k$ in $d^3k = k^2\,dk\,d\Omega$ is $(L/2\pi)^3k^2\,dk\,d\Omega$, and with $E = \hbar^2k^2/2m$,

$$
\rho(E)\,d\Omega = \Big(\frac{L}{2\pi}\Big)^3\frac{mk}{\hbar^2}\,d\Omega .
$$

The volume $L^3$ always cancels against the normalization of the states.

!!! example "The Born cross section from the golden rule"

    A particle in the plane wave $\psi_i = e^{i\mathbf k\cdot\mathbf r}/L^{3/2}$ scatters from $V(\mathbf r)$ into $\psi_f = e^{i\mathbf k'\cdot\mathbf r}/L^{3/2}$ with $|\mathbf k'| = |\mathbf k|$. The matrix element is $V_{fi} = L^{-3}\int e^{i(\mathbf k - \mathbf k')\cdot\mathbf r}V\,d^3r$, so the rate into $d\Omega$ is

    $$
    dw = \frac{2\pi}{\hbar}\,\frac{1}{L^6}\Big|\int e^{i(\mathbf k - \mathbf k')\cdot\mathbf r}V\,d^3r\Big|^2\Big(\frac{L}{2\pi}\Big)^3\frac{mk}{\hbar^2}\,d\Omega .
    $$

    The incident flux is the probability density times the speed, $(1/L^3)(\hbar k/m)$. Dividing,

    $$
    \frac{d\sigma}{d\Omega} = \Big|\frac{m}{2\pi\hbar^2}\int e^{i(\mathbf k - \mathbf k')\cdot\mathbf r}\,V(\mathbf r)\,d^3r\Big|^2 ,
    $$

    which is the first Born approximation of [[born-approximation-and-lippmann-schwinger]], obtained without solving any differential equation.

## What happens to the initial state

The golden rule says probability leaves $|i\rangle$ at the rate $w$. If that remains true as the state empties, $|c_i(t)|^2 = e^{-wt}$. A treatment that keeps the second-order amplitude confirms this and adds an energy shift. The result (Sakurai's derivation switches the perturbation on slowly as $e^{\eta t}$ and lets $\eta\to0$) is

$$
c_i(t) = e^{-i\Delta_it/\hbar} ,\qquad \Delta_i = V_{ii} + \sum_{m\ne i}\frac{|V_{mi}|^2}{E_i - E_m + i\hbar\eta} .
$$

Using $1/(x + i\epsilon) = \mathcal P(1/x) - i\pi\delta(x)$, where $\mathcal P$ denotes the principal value,

$$
\mathrm{Re}\,\Delta_i = V_{ii} + \mathcal P\sum_{m\ne i}\frac{|V_{mi}|^2}{E_i - E_m} ,\qquad \mathrm{Im}\,\Delta_i = -\pi\sum_{m\ne i}|V_{mi}|^2\,\delta(E_i - E_m) = -\frac{\Gamma_i}{2} .
$$

- The real part is the ordinary first- plus second-order energy shift of [[rayleigh-schrodinger-perturbation-theory]]: the level moves to $E_i + \mathrm{Re}\,\Delta_i$.
- The imaginary part defines the **decay width** $\Gamma_i = \hbar\sum_mw_{i\to m}$, the golden-rule rate times $\hbar$. Then

$$
\boxed{\,|c_i(t)|^2 = e^{-\Gamma_it/\hbar} ,\qquad \tau_i = \frac{\hbar}{\Gamma_i}\,}
$$

An unstable state behaves as if it had the complex energy $E_i + \mathrm{Re}\,\Delta_i - i\Gamma_i/2$.

**Line shape.** A state whose amplitude decays as $e^{-iE_0t/\hbar - \Gamma t/2\hbar}$ does not have a sharp energy. Its Fourier transform, which is also the distribution of final-state energies after the decay, is a Lorentzian:

$$
P(E)\propto\frac{1}{(E - E_0)^2 + \Gamma^2/4} ,
$$

with full width $\Gamma$ at half maximum, so that $\tau\,\Gamma = \hbar$. This is the Breit-Wigner shape met for scattering resonances ([[low-energy-scattering-and-resonances]]); a resonance and a decaying state are the same object seen in two ways.

!!! example "One level coupled to a dense band"

    A level at $E_i = 0$ is coupled with the same matrix element $v$ to each of a ladder of levels with spacing $\delta$, so $\rho = 1/\delta$ and the golden rule predicts $\Gamma = 2\pi v^2/\delta$. The model is diagonalized exactly ($\hbar = 1$, $\delta = 0.01$, about 2000 band levels).

    | $v$ | band | $\Gamma$ predicted | $|c_i|^2$ at $\Gamma t = 0.5,\,1,\,2,\,3$ | level shift | predicted shift | width of final distribution |
    |---|---|---|---|---|---|---|
    | 0.02 | $[-10,10]$ | 0.2513 | 0.614, 0.371, 0.135, 0.049 | 0.0000 | 0 | 0.26 |
    | 0.04 | $[-10,10]$ | 1.0053 | 0.626, 0.378, 0.136, 0.048 | 0.0000 | 0 | 1.08 |
    | 0.02 | $[-2,10]$ | 0.2513 | 0.627, 0.380, 0.136, 0.048 | $-0.0660$ | $-0.0644$ | 0.26 |
    | 0.02 | $[-10,1]$ | 0.2513 | 0.682, 0.382, 0.139, 0.045 | $+0.0963$ | $+0.0921$ | 0.27 |

    For comparison $e^{-\Gamma t} = 0.607,\ 0.368,\ 0.135,\ 0.050$. The predicted shift is the principal-value sum for a flat band, $(v^2/\delta)\ln[(E_i - E_{\rm lo})/(E_{\rm hi} - E_i)]$: a level is pushed away from the side on which more of the band lies. The final-state distribution is resolved only to the level spacing 0.01.

    Two departures from exponential decay are visible in the model and are general.

    - **Very short times.** $1 - |c_i|^2 = (\sum_kv^2)\,t^2$, quadratic and not linear: $8.0\times10^{-5}$ at $t = 0.01$, where $\Gamma t$ would give $2.5\times10^{-3}$. The rate is established only after $t\gtrsim\hbar/\Delta E_{\rm band}$. This is the origin of the quantum Zeno effect: observing the system very frequently keeps resetting it to the quadratic regime and inhibits the decay.
    - **Very long times.** A discrete band revives at $t = 2\pi\hbar/\delta$ (here 628, against a lifetime of 4). A true continuum has no revival.

## Uses

The golden rule is the working formula for almost every rate in atomic, molecular and nuclear physics: spontaneous and stimulated radiative transitions ([[emission-absorption-and-spontaneous-emission]]), photoionization, scattering, beta decay, and non-radiative transitions between electronic states of molecules.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 11.4, Eqs. (11.79)-(11.88), Example 11.2 (Born cross section from the golden rule); Problems 11.17 (photoelectric effect) and 11.37 (quantum Zeno paradox). Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 5.7.3, pp. 341-345 (golden rule (5.293)-(5.294), second-order rate (5.296)); Sec. 5.7.4, p. 346, Eqs. (5.302)-(5.303); Sec. 5.9, pp. 355-358, Eqs. (5.364)-(5.381) (slow switching on, level shift (5.370), decay width, lifetime (5.380), Lorentzian line shape).

The band model, the flat-band shift formula and the short-time and revival remarks are my own checks, computed in `griffiths/ch11_dynamics.py` (section C).
