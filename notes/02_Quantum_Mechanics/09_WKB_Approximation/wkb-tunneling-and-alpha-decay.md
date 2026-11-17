---
id: wkb-tunneling-and-alpha-decay
title: WKB tunnelling and Gamow's theory of alpha decay
summary: The WKB transmission probability through a barrier, T ≈ exp(-2γ) with γ = (1/ħ)∫|p| dx across the forbidden region. Compared with exact results for the rectangular barrier (prefactor 16E(V0-E)/V0²), the Eckart barrier (prefactor tends to 1) and the parabolic barrier, where T = 1/(1+exp(2γ)) is exact. Applied to Gamow's model of alpha decay, with lifetimes for five nuclides computed and compared with measurement.
status: in-progress
kind: derivation
level: intermediate
tags: [wkb, tunnelling, transmission-probability, gamow-factor, alpha-decay, geiger-nuttall, eckart-barrier, parabolic-barrier, griffiths]
prerequisites: [wkb-approximation, one-dimensional-scattering-and-transfer-matrix]
related: [wkb-connection-formulas-and-quantization, finite-square-well, low-energy-scattering-and-resonances, energy-time-uncertainty-principle]
order: 30
date: 2026-11-15
---

## Transmission through a barrier

A particle of energy $E$ meets a barrier that is classically forbidden between $x_1$ and $x_2$ ($V>E$ there). To the left $\psi = Ae^{ikx} + Be^{-ikx}$, to the right $\psi = Fe^{ikx}$, and the transmission probability is $T = |F|^2/|A|^2$ ([[one-dimensional-scattering-and-transfer-matrix]]). Inside the barrier the WKB solution of [[wkb-approximation]] is

$$
\psi(x) \approx \frac{C}{\sqrt{|p(x)|}}\,e^{\frac1\hbar\int_{x_1}^x|p|\,dx'} + \frac{D}{\sqrt{|p(x)|}}\,e^{-\frac1\hbar\int_{x_1}^x|p|\,dx'} ,\qquad |p| = \sqrt{2m\,[V(x) - E]} .
$$

If the barrier is high or wide, the growing term must be negligible, since otherwise the wave would be larger on the far side than on the near side. The amplitude then falls across the barrier by the factor $e^{-\gamma}$, and

$$
\boxed{\,T \approx e^{-2\gamma} ,\qquad \gamma = \frac1\hbar\int_{x_1}^{x_2}|p(x)|\,dx\,}
$$

This fixes the exponent, which carries almost all of the energy dependence. It does not fix the prefactor, which is of order one and depends on how the barrier begins and ends. The estimate requires $\gamma\gg1$.

## How good is it?

!!! example "Rectangular barrier"

    Height $V_0$, width $2a$, so $\gamma = 2\kappa a$ with $\kappa = \sqrt{2m(V_0 - E)}/\hbar$. The exact result is

    $$
    T^{-1} = 1 + \frac{V_0^2}{4E(V_0 - E)}\sinh^2(2\kappa a) \ \longrightarrow\ T \approx \frac{16E(V_0 - E)}{V_0^2}\,e^{-2\gamma}\quad(\gamma\gg1) .
    $$

    With $\hbar = m = V_0 = 1$:

    | $E$ | $2a$ | $\gamma$ | exact $T$ | $e^{-2\gamma}$ | ratio | $16E(V_0 - E)/V_0^2$ |
    |---|---|---|---|---|---|---|
    | 0.5 | 2 | 2.000 | $7.065\times10^{-2}$ | $1.832\times10^{-2}$ | 3.857 | 4.000 |
    | 0.5 | 4 | 4.000 | $1.341\times10^{-3}$ | $3.355\times10^{-4}$ | 3.997 | 4.000 |
    | 0.5 | 8 | 8.000 | $4.501\times10^{-7}$ | $1.125\times10^{-7}$ | 4.000 | 4.000 |
    | 0.1 | 4 | 5.367 | $3.141\times10^{-5}$ | $2.181\times10^{-5}$ | 1.440 | 1.440 |
    | 0.9 | 4 | 1.789 | $4.084\times10^{-2}$ | $2.794\times10^{-2}$ | 1.462 | 1.440 |
    | 0.9 | 8 | 3.578 | $1.125\times10^{-3}$ | $7.806\times10^{-4}$ | 1.441 | 1.440 |

    The exponent is right and the prefactor, between 0 and 4, is missed. The vertical walls violate the WKB condition, and the prefactor is the price.

!!! example "Eckart barrier"

    For the smooth barrier $V = V_0/\cosh^2(x/a)$ the WKB integral is elementary,

    $$
    \gamma = \frac{\pi a}{\hbar}\Big(\sqrt{2mV_0} - \sqrt{2mE}\Big) ,
    $$

    and the exact transmission probability is known in closed form (for $8mV_0a^2/\hbar^2>1$):

    $$
    T = \frac{\sinh^2(\pi ka)}{\sinh^2(\pi ka) + \cosh^2\!\Big(\frac\pi2\sqrt{8mV_0a^2/\hbar^2 - 1}\Big)} ,\qquad k = \frac{\sqrt{2mE}}{\hbar} .
    $$

    For $\gamma\gg1$ this reduces to $T\approx e^{-2\gamma}\exp[\pi\hbar/(4a\sqrt{2mV_0})]$: the prefactor tends to 1 as the barrier becomes wide on the scale of the wavelength. With $\hbar = m = V_0 = 1$:

    | $E$ | $a$ | $\gamma$ | exact $T$ | $e^{-2\gamma}$ | ratio | $1/(1 + e^{2\gamma})$ |
    |---|---|---|---|---|---|---|
    | 0.2 | 3 | 7.368 | $4.797\times10^{-7}$ | $3.984\times10^{-7}$ | 1.204 | $3.984\times10^{-7}$ |
    | 0.5 | 3 | 3.904 | $4.893\times10^{-4}$ | $4.066\times10^{-4}$ | 1.204 | $4.064\times10^{-4}$ |
    | 0.8 | 3 | 1.407 | $6.733\times10^{-2}$ | $5.995\times10^{-2}$ | 1.123 | $5.656\times10^{-2}$ |
    | 0.95 | 3 | 0.337 | $0.3801$ | $0.5092$ | 0.746 | $0.3374$ |
    | 0.5 | 1 | 1.301 | $0.1158$ | $7.408\times10^{-2}$ | 1.563 | $6.897\times10^{-2}$ |
    | 0.5 | 6 | 7.808 | $1.814\times10^{-7}$ | $1.653\times10^{-7}$ | 1.097 | $1.653\times10^{-7}$ |

    The closed form was confirmed by integrating the Schrödinger equation numerically. For a wide smooth barrier (the rows with $a = 3$ and $a = 6$ and $\gamma>1$) $e^{-2\gamma}$ is right to within 10 to 20 percent across five orders of magnitude; the narrow barrier $a = 1$ is off by 56 percent.

**Near the top of the barrier.** As $E\to V_0$, $\gamma\to0$ and $e^{-2\gamma}\to1$, which is wrong: a particle at the barrier top is transmitted only about half the time. The connection formulas of [[wkb-connection-formulas-and-quantization]], applied at the two sloping walls separately, give $T\approx e^{-2\gamma}$ with unit prefactor for $\gamma\gg1$, but they too assume the turning points are far apart. A uniform treatment that handles both turning points together, by comparison with the parabolic barrier, gives

$$
T \approx \frac{1}{1 + e^{2\gamma}} .
$$

For a parabolic barrier $V = V_0 - \tfrac12m\omega^2x^2$, where $\gamma = \pi(V_0 - E)/(\hbar\omega)$, this expression is exact at every energy, including $E>V_0$ where $\gamma$ is continued to negative values. A numerical integration with $\hbar = m = \omega = 1$ gives $T = 0.2215,\ 0.0414,\ 0.0019$ for $V_0 - E = 0.2,\ 0.5,\ 1.0$ and $0.868$ for $V_0 - E = -0.3$, each matching $1/(1 + e^{2\gamma})$ to the accuracy of the integration.

## Gamow's theory of alpha decay

An alpha particle (charge $2e$, mass $m$) is pictured as moving inside the nucleus, held by the nuclear force out to a radius $r_1$. Beyond $r_1$ it feels only the Coulomb repulsion of the daughter nucleus of charge $Ze$:

$$
V(r) = \frac{1}{4\pi\epsilon_0}\frac{2Ze^2}{r}\quad(r>r_1) ,\qquad E = \frac{1}{4\pi\epsilon_0}\frac{2Ze^2}{r_2} ,
$$

where $r_2$ is the outer turning point. Since $E$ is far below the top of the Coulomb barrier, the particle must tunnel from $r_1$ to $r_2$. The exponent is

$$
\gamma = \frac1\hbar\int_{r_1}^{r_2}\sqrt{2m\Big(\frac{1}{4\pi\epsilon_0}\frac{2Ze^2}{r} - E\Big)}\,dr = \frac{\sqrt{2mE}}{\hbar}\Big[r_2\Big(\frac\pi2 - \arcsin\sqrt{\frac{r_1}{r_2}}\Big) - \sqrt{r_1(r_2 - r_1)}\Big] .
$$

For $r_1\ll r_2$ (thick barrier), using $\arcsin\epsilon\approx\epsilon$,

$$
\gamma \approx \frac{\sqrt{2mE}}{\hbar}\Big[\frac\pi2r_2 - 2\sqrt{r_1r_2}\Big] = K_1\frac{Z}{\sqrt E} - K_2\sqrt{Zr_1} ,
$$

$$
K_1 = \frac{e^2}{4\pi\epsilon_0}\frac{\pi\sqrt{2m}}{\hbar} = 1.980\ \text{MeV}^{1/2} ,\qquad K_2 = \Big(\frac{e^2}{4\pi\epsilon_0}\Big)^{1/2}\frac{4\sqrt m}{\hbar} = 1.485\ \text{fm}^{-1/2} .
$$

**Lifetime.** Inside the nucleus the particle moves with speed $v$ and hits the barrier once every $2r_1/v$. Each hit has escape probability $e^{-2\gamma}$, so the mean lifetime is

$$
\tau = \frac{2r_1}{v}\,e^{2\gamma} .
$$

Because $\gamma$ is large, $\ln\tau$ is dominated by $2K_1Z/\sqrt E$: the logarithm of the lifetime is linear in $Z/\sqrt E$. This is the Geiger-Nuttall law, and it explains how roughly a factor of two in $E$ changes $\tau$ by more than twenty orders of magnitude.

!!! example "Five alpha emitters"

    Take $r_1 = (1.07\ \text{fm})A^{1/3}$ (Griffiths' value), $v$ from $E = \tfrac12mv^2$, and the approximate $\gamma$ above. $Z$ is the daughter's charge.

    | parent | $E$ (MeV) | $Z$ | $r_1$ (fm) | $r_2$ (fm) | $\gamma$ | $\tau$ model (s) | $\tau$ measured (s) | $\log_{10}$ ratio |
    |---|---|---|---|---|---|---|---|---|
    | $^{238}$U | 4.27 | 90 | 6.63 | 60.7 | 49.93 | $2.2\times10^{22}$ | $2.03\times10^{17}$ | $+5.0$ |
    | $^{232}$Th | 4.08 | 88 | 6.57 | 62.1 | 50.51 | $7.0\times10^{22}$ | $6.40\times10^{17}$ | $+5.0$ |
    | $^{226}$Ra | 4.87 | 86 | 6.52 | 50.9 | 41.98 | $2.5\times10^{15}$ | $7.28\times10^{10}$ | $+4.5$ |
    | $^{210}$Po | 5.41 | 82 | 6.36 | 43.7 | 35.87 | $1.1\times10^{10}$ | $1.73\times10^{7}$ | $+2.8$ |
    | $^{212}$Po | 8.95 | 82 | 6.38 | 26.4 | 20.29 | $2.6\times10^{-4}$ | $4.31\times10^{-7}$ | $+2.8$ |

    The measured lifetimes span 24 orders of magnitude and the model follows them, staying a factor $10^3$ to $10^5$ too long. That residual is small on the scale of the effect and easy to account for:

    - $\tau$ is exponentially sensitive to $r_1$: for $^{238}$U, $d\ln\tau/dr_1 = -5.0$ per fm, and $r_1 = 9.5$ fm in place of 6.6 fm reproduces the measured value. A larger effective radius is reasonable, since the alpha particle has its own size and the nuclear force a finite range.
    - The thick-barrier approximation underestimates $\gamma$ by 0.6 to 1.4 here (the exact integral is 50.60 for $^{238}$U and 21.71 for $^{212}$Po). Using the exact integral makes the model lifetimes longer still, so this is not the cause of the excess.
    - The prefactor (the "attempt frequency" and the probability that an alpha particle is preformed) is only a rough estimate.

    The measured half-lives ($4.468\times10^9$ yr, $1.405\times10^{10}$ yr, 1600 yr, 138.4 d, 0.299 μs, converted to mean lives by dividing by $\ln2$) and the decay energies were entered from memory and should be checked against a nuclear data table before being quoted.

## Other uses

The same exponent governs field emission of electrons from a metal surface, tunnelling in semiconductor junctions (Zener tunnelling), ionization of atoms by a static field, and the splitting of levels in a double well. The resonance widths in [[low-energy-scattering-and-resonances]] follow the same "attempt frequency times transmission probability" argument.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 9.2, Eqs. (9.18)-(9.31), Example 9.2 (Gamow's theory); Problems 9.3 (rectangular barrier), 9.4 (lifetimes of U-238 and Po-212), 9.5 (Zener tunnelling), 9.11 (barrier with sloping walls), 9.17 (double well), 9.18 (tunnelling in the Stark effect). Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Not from Griffiths or Sakurai: the Eckart transmission formula and the statement that $1/(1 + e^{2\gamma})$ is exact for the parabolic barrier. Both were checked here by numerical integration of the Schrödinger equation. Original references, quoted from memory and to verify: C. Eckart, Phys. Rev. 35, 1303 (1930); E. C. Kemble, Phys. Rev. 48, 549 (1935); G. Gamow, Z. Phys. 51, 204 (1928); R. W. Gurney and E. U. Condon, Nature 122, 439 (1928).

All numbers are computed in `griffiths/ch09_wkb.py` (sections C, D and F).
