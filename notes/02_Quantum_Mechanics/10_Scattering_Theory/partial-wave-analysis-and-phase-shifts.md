---
id: partial-wave-analysis-and-phase-shifts
title: Partial wave analysis and phase shifts
summary: Exact treatment of scattering by a spherically symmetric potential. Each angular momentum component of the incident plane wave scatters independently and conservation of probability allows it only a phase shift δ_l. Gives f(θ) = (1/k) Σ (2l+1) exp(iδ_l) sin δ_l P_l(cos θ), σ = (4π/k²) Σ (2l+1) sin²δ_l, the unitarity bound, the optical theorem, how δ_l is found by matching at the edge of the potential, and the hard sphere from ka → 0 (σ = 4πa²) to ka → ∞ (σ = 2πa²).
status: in-progress
kind: derivation
level: intermediate
tags: [scattering, partial-waves, phase-shift, optical-theorem, unitarity, hard-sphere, spherical-bessel-functions, s-matrix, griffiths, sakurai]
prerequisites: [scattering-cross-sections-and-amplitude, central-potentials-and-spherical-harmonics, orbital-angular-momentum]
related: [born-approximation-and-lippmann-schwinger, low-energy-scattering-and-resonances, one-dimensional-scattering-and-transfer-matrix, symmetry-conservation-and-degeneracy]
order: 20
date: 2026-11-15
---

## Setting

For a spherically symmetric potential, angular momentum is conserved and the Schrödinger equation separates: $\psi = R_l(r)Y_l^m(\theta,\phi)$ with $u = rR_l$ obeying the radial equation ([[central-potentials-and-spherical-harmonics]]). A plane wave along $z$ has $m = 0$ only, so the scattering state is a sum over $l$ of terms $R_l(r)P_l(\cos\theta)$, called **partial waves**. Each scatters on its own.

Assume the potential vanishes (or is negligible) beyond some radius $a$. For $r>a$ the radial equation is the free one, whose solutions are the spherical Bessel and Neumann functions $j_l(kr)$ and $n_l(kr)$, or the spherical Hankel functions $h_l^{(1,2)} = j_l\pm in_l$. At large argument

$$
j_l(x)\to\frac{\sin(x - l\pi/2)}{x} ,\qquad n_l(x)\to-\frac{\cos(x - l\pi/2)}{x} ,\qquad h_l^{(1)}(x)\to(-i)^{l+1}\frac{e^{ix}}{x} ,
$$

so $h_l^{(1)}$ is an outgoing spherical wave and $h_l^{(2)}$ an incoming one.

## Partial wave amplitudes

Outside the potential the scattered part must be purely outgoing:

$$
\psi(r,\theta) = A\Big\{e^{ikz} + k\sum_{l=0}^\infty i^{\,l+1}(2l+1)\,a_l\,h_l^{(1)}(kr)\,P_l(\cos\theta)\Big\} ,\qquad r>a .
$$

The numbers $a_l$ are the **partial wave amplitudes**; the factors in front are conventional. Using the large-$r$ form of $h_l^{(1)}$ and comparing with $\psi\approx A[e^{ikz} + f(\theta)e^{ikr}/r]$,

$$
f(\theta) = \sum_{l=0}^\infty(2l+1)\,a_l\,P_l(\cos\theta) .
$$

Then, with the orthogonality $\int_{-1}^1P_lP_{l'}\,d(\cos\theta) = 2\delta_{ll'}/(2l+1)$,

$$
\frac{d\sigma}{d\Omega} = |f(\theta)|^2 ,\qquad \sigma = 4\pi\sum_{l=0}^\infty(2l+1)\,|a_l|^2 .
$$

The partial waves interfere in the angular distribution but add incoherently in the total cross section.

To find the $a_l$ one needs the incident wave in the same form. **Rayleigh's formula** is

$$
e^{ikz} = \sum_{l=0}^\infty i^{\,l}(2l+1)\,j_l(kr)\,P_l(\cos\theta) .
$$

## Phase shifts

Look at one partial wave far from the centre. In the free plane wave its radial factor is

$$
j_l(kr)\to\frac{1}{2ikr}\Big[e^{i(kr - l\pi/2)} - e^{-i(kr - l\pi/2)}\Big] ,
$$

an incoming spherical wave plus an outgoing one of equal magnitude. The potential cannot alter the incoming part, which has not yet reached it. Because probability and angular momentum are both conserved, the outgoing flux in each $l$ must equal the incoming flux, so the outgoing wave can change only by a phase factor, written $e^{2i\delta_l}$:

$$
R_l(r)\to\frac{1}{2ikr}\Big[e^{2i\delta_l}e^{i(kr - l\pi/2)} - e^{-i(kr - l\pi/2)}\Big] = e^{i\delta_l}\,\frac{\sin(kr - l\pi/2 + \delta_l)}{kr} .
$$

The real number $\delta_l(k)$ is the **phase shift**: the radial wave is displaced by $\delta_l$ relative to the free one. An attractive potential pulls the wave in ($\delta_l>0$) and a repulsive one pushes it out ($\delta_l<0$). Subtracting the free wave leaves the scattered part, and comparison with the definition of $a_l$ gives

$$
\boxed{\,a_l = \frac{e^{2i\delta_l} - 1}{2ik} = \frac1k\,e^{i\delta_l}\sin\delta_l\,}
$$

$$
\boxed{\,f(\theta) = \frac1k\sum_{l=0}^\infty(2l+1)\,e^{i\delta_l}\sin\delta_l\,P_l(\cos\theta) ,\qquad \sigma = \frac{4\pi}{k^2}\sum_{l=0}^\infty(2l+1)\sin^2\delta_l\,}
$$

One complex number per partial wave has become one real number.

**Unitarity.** The quantity $S_l = e^{2i\delta_l}$ is the $l$-th element of the scattering matrix, and $|S_l| = 1$ expresses conservation of probability. Each partial wave contributes at most

$$
\sigma_l\le\frac{4\pi}{k^2}(2l+1) ,
$$

reached when $\delta_l = \pi/2$ (mod $\pi$). In the complex plane $ka_l = \tfrac{i}{2} + \tfrac12e^{i(2\delta_l - \pi/2)}$ lies on a circle of radius $\tfrac12$ centred at $i/2$.

**Optical theorem.** Since $P_l(1) = 1$,

$$
\mathrm{Im}\,f(0) = \frac1k\sum_l(2l+1)\sin^2\delta_l \quad\Rightarrow\quad \boxed{\,\sigma = \frac{4\pi}{k}\,\mathrm{Im}\,f(0)\,}
$$

The total cross section is fixed by the forward amplitude: the flux removed from the beam appears as destructive interference between the incident wave and the forward scattered wave. The theorem holds in general, not only for central potentials (Sakurai proves it from the Lippmann-Schwinger equation).

## Finding the phase shifts

For $r>a$ the general real solution is

$$
R_l(r)\propto\cos\delta_l\,j_l(kr) - \sin\delta_l\,n_l(kr) ,
$$

which has the asymptotic form $\sin(kr - l\pi/2 + \delta_l)/(kr)$ required above. Let $\beta_l = (R_l'/R_l)_{r=a}$ be the logarithmic derivative of the interior solution, which is regular at the origin. Continuity of $R_l'/R_l$ at $r = a$ gives

$$
\boxed{\,\tan\delta_l = \frac{k\,j_l'(ka) - \beta_l\,j_l(ka)}{k\,n_l'(ka) - \beta_l\,n_l(ka)}\,}
$$

where primes denote derivatives with respect to the argument. All of the physics of the potential enters through the numbers $\beta_l(E)$.

**Which partial waves matter.** Classically a particle with impact parameter $b$ has angular momentum $\hbar kb$ and misses the potential if $b>a$. So only $l\lesssim ka$ contribute appreciably. More precisely, for $ka\ll1$ the small-argument forms $j_l(x)\approx x^l/(2l+1)!!$ and $n_l(x)\approx-(2l-1)!!/x^{l+1}$ give $\delta_l\propto k^{2l+1}$: at low energy only the s wave survives and the scattering is isotropic ([[low-energy-scattering-and-resonances]]).

## Hard sphere

For $V = \infty$ inside $r = a$ the wave function vanishes at $r = a$, i.e. $\beta_l = \infty$:

$$
\tan\delta_l = \frac{j_l(ka)}{n_l(ka)} ,\qquad a_l = \frac{i\,j_l(ka)}{k\,h_l^{(1)}(ka)} .
$$

For $l = 0$, $\tan\delta_0 = -\tan ka$, so $\delta_0 = -ka$ exactly: the wave is simply pushed out by $a$.

!!! example "Hard sphere from low to high energy"

    Sum over partial waves with $a = 1$; the last column is the optical theorem evaluated independently from $\mathrm{Im}f(0)$.

    | $ka$ | $\sigma/\pi a^2$ | s-wave share | $(4\pi/k)\,\mathrm{Im}f(0)/\pi a^2$ |
    |---|---|---|---|
    | 0.01 | 3.9999 | 1.000 | 3.9999 |
    | 0.1 | 3.9868 | 1.000 | 3.9868 |
    | 0.5 | 3.7410 | 0.983 | 3.7410 |
    | 1 | 3.3824 | 0.837 | 3.3824 |
    | 2 | 2.9991 | 0.276 | 2.9991 |
    | 5 | 2.6024 | 0.057 | 2.6024 |
    | 20 | 2.2575 | 0.004 | 2.2575 |
    | 100 | 2.0909 | 0.000 | 2.0909 |

    **Low energy.** $\sigma\to4\pi a^2$, four times the classical value and equal to the full surface area of the sphere: a long wave feels the whole sphere. The scattering is isotropic with $d\sigma/d\Omega\to a^2$. At $ka = 0.5$ the p wave already tilts it forward: $d\sigma/d\Omega = 1.355,\ 1.117,\ 0.743,\ 0.601\ a^2$ at $0^\circ, 60^\circ, 120^\circ, 180^\circ$.

    **High energy.** $\sigma\to2\pi a^2$, twice the classical value, and the approach is slow. One $\pi a^2$ is the classical reflection, spread over all angles. The other is **shadow scattering**: to produce the shadow behind the sphere, the scattered wave must cancel the incident wave over an area $\pi a^2$, and this diffracted wave is confined to a forward cone of angle of order $1/(ka)$.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 10.2, Eqs. (10.15)-(10.36), Example 10.3 (quantum hard sphere); Sec. 10.3, Eqs. (10.37)-(10.48); Problems 10.3, 10.6 (hard-sphere phase shifts) and 10.19 (optical theorem). Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 6.4, pp. 388-400: partial-wave amplitude (6.114), unitarity (6.121)-(6.122), determination of phase shifts by matching, and the hard sphere including the high-energy limit and shadow scattering (Sec. 6.4.5, pp. 398-400); Sec. 6.2.2, pp. 381-384, for the general proof of the optical theorem.

Note on conventions: Sakurai defines $\beta_l$ as the dimensionless $(r/R_l)\,dR_l/dr$ at $r = a$; here $\beta_l$ is $R_l'/R_l$, so the two differ by a factor $a$. The table is computed in `griffiths/ch10_scattering.py` (section A).
