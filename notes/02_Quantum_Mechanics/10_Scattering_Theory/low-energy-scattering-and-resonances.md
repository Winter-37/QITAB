---
id: low-energy-scattering-and-resonances
title: Low-energy scattering, bound states and resonances
summary: Scattering when the wavelength exceeds the range of the potential. Only the s wave matters and one number, the scattering length a_s, fixes the cross section 4πa_s². Worked for the spherical well: a_s changes sign and diverges whenever a new bound state appears, a large positive a_s signals a shallow bound state with E = -ħ²/(2m a_s²), and a_s = 0 gives the Ramsauer-Townsend effect. Resonances are quasi-bound states with a Breit-Wigner cross section; the delta-shell potential gives positions and widths explicitly.
status: in-progress
kind: theory
level: advanced
tags: [scattering, scattering-length, s-wave, effective-range, bound-states, ramsauer-townsend, resonance, breit-wigner, delta-shell, s-matrix-poles, sakurai, griffiths]
prerequisites: [partial-wave-analysis-and-phase-shifts, finite-square-well]
related: [born-approximation-and-lippmann-schwinger, wkb-tunneling-and-alpha-decay, delta-function-potential, energy-time-uncertainty-principle]
order: 40
date: 2026-11-15
---

## Why low energy is simple

For a potential of range $a$ and $ka\ll1$, the phase shifts fall off as $\delta_l\propto k^{2l+1}$ ([[partial-wave-analysis-and-phase-shifts]]): the centrifugal barrier keeps every wave except $l = 0$ away from the potential. The scattering is then isotropic and described by $\delta_0(k)$ alone,

$$
f\approx\frac1k\,e^{i\delta_0}\sin\delta_0 = \frac{1}{k\cot\delta_0 - ik} ,\qquad \sigma\approx\frac{4\pi}{k^2}\sin^2\delta_0 .
$$

## The scattering length

For $l = 0$ the radial function $u = rR$ outside the potential is $u\propto\sin(kr + \delta_0)$. As $k\to0$ this becomes a straight line, and the **scattering length** $a_s$ is defined as its intercept with the axis:

$$
u(r)\ \xrightarrow{\ k\to0\ }\ \text{const}\times(r - a_s) ,\qquad \lim_{k\to0}k\cot\delta_0 = -\frac{1}{a_s} .
$$

Then

$$
\boxed{\,f\to-a_s ,\qquad \sigma\to4\pi a_s^2\quad(k\to0)\,}
$$

At zero energy any short-range potential scatters like a hard sphere of radius $|a_s|$. The sign carries extra information: $a_s<0$ for a weak attraction, $a_s>0$ for a repulsion or for an attraction strong enough to bind. The next term in the expansion defines the **effective range** $r_0$:

$$
k\cot\delta_0 = -\frac{1}{a_s} + \tfrac12r_0k^2 + \cdots .
$$

## The spherical well

Take $V = -V_0$ for $r<a$ and define $K_0 = \sqrt{2mV_0}/\hbar$, $K = \sqrt{k^2 + K_0^2}$. Inside, $u = \sin Kr$; matching $u'/u$ at $r = a$ gives $K\cot Ka = k\cot(ka + \delta_0)$, so

$$
\delta_0 = \arctan\Big[\frac kK\tan Ka\Big] - ka ,\qquad \boxed{\,a_s = a\Big[1 - \frac{\tan K_0a}{K_0a}\Big]\,}
$$

For a repulsive barrier of height $V_0$, $\tan\to\tanh$ and $a_s$ rises from 0 to $a$, the hard-sphere value.

!!! example "Scattering length against well depth"

    With $a = 1$; the Born value is $-K_0^2a^3/3$ ([[born-approximation-and-lippmann-schwinger]]).

    | $K_0a$ | $a_s/a$ | Born | $\sigma(k\to0)/\pi a^2$ | comment |
    |---|---|---|---|---|
    | 0.2 | $-0.0136$ | $-0.0133$ | 0.0007 | weak: Born is good |
    | 0.5 | $-0.0926$ | $-0.0833$ | 0.034 | |
    | 1.0 | $-0.557$ | $-0.333$ | 1.24 | |
    | 1.5 | $-8.40$ | $-0.750$ | 282 | almost bound |
    | 1.6 | $+22.4$ | $-0.853$ | 2006 | just bound |
    | 2.0 | $+2.09$ | $-1.33$ | 17.5 | |
    | 3.0 | $+1.05$ | $-3.00$ | 4.39 | |
    | 4.4934 | $0$ | $-6.73$ | 0 | Ramsauer-Townsend |
    | 4.6 | $-0.926$ | $-7.05$ | 3.43 | second state almost bound |
    | 4.8 | $+3.37$ | $-7.68$ | 45.5 | two bound states |

Three things happen as the well deepens.

**1. Divergence at threshold.** $a_s\to\mp\infty$ at $K_0a = \pi/2, 3\pi/2,\dots$, exactly the depths at which the well acquires a new s-wave bound state ([[finite-square-well]]). There the zero-energy interior wave arrives at $r = a$ with zero slope, the exterior line is horizontal, and $\sigma = 4\pi/k^2$ reaches the unitarity limit instead of a constant.

**2. Shallow bound state.** Just past threshold $a_s$ is large and positive. A bound state with $E = -\hbar^2\kappa^2/2m$ has exterior function $e^{-\kappa r}$, which for small $\kappa$ looks like the zero-energy line $1 - \kappa r$ with intercept $1/\kappa$. Hence

$$
\kappa\approx\frac{1}{a_s} ,\qquad E_b\approx-\frac{\hbar^2}{2ma_s^2} ,
$$

a relation between a scattering measurement and a binding energy that makes no reference to the shape of the potential. For the well, with $\hbar = m = a = 1$:

| $K_0a$ | $a_s$ | $1/a_s$ | exact $\kappa$ | $1/(2a_s^2)$ | exact $|E_b|$ |
|---|---|---|---|---|---|
| 1.6 | 22.40 | 0.0447 | 0.0457 | 0.00100 | 0.00104 |
| 1.7 | 5.527 | 0.1809 | 0.1993 | 0.0164 | 0.0199 |
| 2.0 | 2.093 | 0.4779 | 0.6381 | 0.114 | 0.204 |

The estimate is good only while $a_s\gg a$. The effective range repairs it: at $K_0a = 1.6$, $r_0 = 0.982$ and $\kappa = 1/a_s + \tfrac12r_0\kappa^2$ gives $0.0457$. Sakurai's example is the deuteron: the measured triplet neutron-proton scattering length, 5.4 fm, predicts a binding energy of 1.4 MeV against the measured 2.22 MeV, the difference being the effective-range correction.

**3. Ramsauer-Townsend effect.** When $\tan K_0a = K_0a$ ($K_0a = 4.4934, 7.7253,\dots$) the scattering length vanishes: the interior wave completes just enough extra oscillation that the exterior wave is undisplaced ($\delta_0 = \pi$), and the s wave does not scatter. Since the higher partial waves are still negligible, the target is nearly transparent. For $K_0a = 4.4934$ the full cross section is $\sigma/\pi a^2 = 0.0002,\ 0.013,\ 0.73$ at $ka = 0.1,\ 0.3,\ 1$. This is observed for slow electrons in argon, krypton and xenon.

**Bound states as poles.** In terms of $S_0 = e^{2i\delta_0}$, $f = (S_0 - 1)/(2ik)$. Continued to complex $k$, a bound state appears as a pole of $S_l(k)$ on the positive imaginary axis, $k = i\kappa$: there the "incoming" wave $e^{-ikr} = e^{\kappa r}$ must be absent, so the ratio of outgoing to incoming amplitude is infinite. Near threshold, $f\approx1/(-1/a_s - ik)$ has its pole at $k = i/a_s$, which is result 2 again.

## Resonances

A potential that would hold a bound state if it were slightly different (a well behind a barrier, or the centrifugal barrier for $l>0$) can trap the particle for a long but finite time. Such a **quasi-bound state** shows up as a pole of $S_l$ just below the real axis, at $E = E_r - i\Gamma/2$. For real energies near $E_r$ the phase shift rises rapidly by $\pi$,

$$
\delta_l(E)\approx\delta_{\rm bg} + \arctan\frac{\Gamma/2}{E_r - E} ,
$$

on top of a slowly varying background $\delta_{\rm bg}$. If the background is negligible the partial cross section has the **Breit-Wigner** form

$$
\boxed{\,\sigma_l(E) = \frac{4\pi}{k^2}(2l+1)\,\frac{(\Gamma/2)^2}{(E - E_r)^2 + (\Gamma/2)^2}\,}
$$

which touches the unitarity limit at $E = E_r$ and has full width $\Gamma$ at half maximum. The trapped state decays with lifetime $\hbar/\Gamma$ ([[energy-time-uncertainty-principle]]). With a background phase the line shape is asymmetric, but the width is still read from the slope: $\Gamma = 2/(d\delta_{\rm res}/dE)$ at $E_r$.

!!! example "Delta-shell potential"

    Let $V(r) = (\hbar^2\gamma/2m)\,\delta(r - R)$. For $l = 0$, $u = A\sin kr$ inside and $\sin(kr + \delta_0)$ outside; $u$ is continuous and $u'$ jumps by $\gamma u(R)$, so

    $$
    k\cot(kR + \delta_0) = k\cot kR + \gamma .
    $$

    For $\gamma\to\infty$ the inside and outside decouple: outside, a hard sphere with $\delta_0 = -kR$; inside, a box with bound states at $kR = n\pi$. For large finite $\gamma$ those states become resonances. The poles of $S_0$ satisfy $\cot kR + \gamma/k = i$, and to leading order in $1/\gamma R$

    $$
    k_rR\approx n\pi\Big(1 - \frac{1}{\gamma R}\Big) ,\qquad \Gamma\approx\frac{4n\pi}{(\gamma R)^2}\,E_n ,\qquad E_n = \frac{\hbar^2(n\pi)^2}{2mR^2} .
    $$

    The width has a simple meaning. A particle in the box hits the wall $v/2R$ times per unit time, and a delta barrier transmits with probability $T\approx4k^2/\gamma^2$, so $\Gamma/\hbar = (v/2R)\,T$, which is the expression above. This is the argument used for alpha decay in [[wkb-tunneling-and-alpha-decay]].

    Numerically, with $\hbar = m = R = 1$, solving the pole equation exactly and, independently, locating the maximum of $d\delta_0/dE$ after removing the background:

    | $\gamma R$ | $n$ | $k_rR$ | $n\pi(1 - 1/\gamma R)$ | $E_r$ | $\Gamma$ | $4n\pi E_n/(\gamma R)^2$ |
    |---|---|---|---|---|---|---|
    | 20 | 1 | 2.9958 | 2.9845 | 4.487 | 0.1231 | 0.1550 |
    | 40 | 1 | 3.0655 | 3.0631 | 4.699 | 0.0347 | 0.0388 |
    | 40 | 2 | 6.1342 | 6.1261 | 18.81 | 0.2696 | 0.3101 |

    The two numerical methods agree to four figures in $\Gamma$. The leading-order width is 12 to 26 percent high at these strengths and converges as $\gamma R$ grows. Higher resonances are broader because the barrier is more transparent at higher energy. The zero-energy limit gives the scattering length $a_s = R\,\gamma R/(1 + \gamma R)$, which tends to the hard-sphere value $R$.

## Source

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 6.6, pp. 405-412 (rectangular well and barrier, zero-energy scattering and the scattering length, the Ramsauer-Townsend effect on p. 407, the deuteron estimate (6.203)-(6.205), the effective range (6.206), bound states as poles of $S_l(k)$); Sec. 6.7, pp. 412-416 (resonance scattering, Breit-Wigner formula, the delta-shell potential (6.216)-(6.219) and Problem 6.10).

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Problems 10.4 and 10.7 (delta-function shell at low energy and its s-wave phase shift) and Sec. 10.3. Griffiths' text does not develop the scattering length or resonances. Page numbers are not given because the PDF used is an e-book rendering without print pagination.

The leading-order pole position and width of the delta-shell resonances, and the comparison with the attempt-frequency argument, are worked out here and are not quoted from either book. All numbers are computed in `griffiths/ch10_scattering.py` (sections B, D and E).
