---
id: born-approximation-and-lippmann-schwinger
title: The Born approximation and the Lippmann-Schwinger equation
summary: The Schrödinger equation for scattering rewritten as an integral equation with the outgoing Green's function of the Helmholtz operator, in position space (Griffiths) and as the Lippmann-Schwinger equation (Sakurai). Replacing the unknown wave function by the incident wave gives the first Born amplitude, the Fourier transform of the potential at the momentum transfer. Worked for the soft sphere, Yukawa and Coulomb potentials, with the Born series, the range of validity tested against exact partial-wave results, and the Born phase shifts.
status: in-progress
kind: derivation
level: intermediate
tags: [scattering, born-approximation, lippmann-schwinger, greens-function, momentum-transfer, yukawa-potential, rutherford-scattering, born-series, t-matrix, griffiths, sakurai]
prerequisites: [scattering-cross-sections-and-amplitude, greens-functions-single-particle, rayleigh-schrodinger-perturbation-theory]
related: [partial-wave-analysis-and-phase-shifts, low-energy-scattering-and-resonances, position-momentum-and-energy-representations]
order: 30
date: 2026-11-15
---

## Integral form of the Schrödinger equation

Write the time-independent Schrödinger equation as an inhomogeneous Helmholtz equation,

$$
(\nabla^2 + k^2)\,\psi = Q ,\qquad k = \frac{\sqrt{2mE}}{\hbar} ,\qquad Q = \frac{2m}{\hbar^2}V\psi .
$$

The "source" $Q$ contains $\psi$ itself, so this is only a rewriting. If $G(\mathbf r)$ solves the equation for a point source,

$$
(\nabla^2 + k^2)\,G(\mathbf r) = \delta^3(\mathbf r) ,
$$

then $\psi(\mathbf r) = \psi_0(\mathbf r) + \int G(\mathbf r - \mathbf r_0)\,Q(\mathbf r_0)\,d^3r_0$, where $\psi_0$ is any solution of the free equation.

**The Green's function.** Fourier transforming gives $G(\mathbf r) = (2\pi)^{-3}\int e^{i\mathbf s\cdot\mathbf r}/(k^2 - s^2)\,d^3s$. The angular integrals are elementary; the radial one has poles at $s = \pm k$ on the integration path, and the way they are avoided is a choice of boundary condition. Closing the contour so that only the pole at $s = +k$ contributes gives

$$
G(\mathbf r) = -\frac{e^{ikr}}{4\pi r} ,
$$

an outgoing spherical wave. The other choice gives the incoming wave $e^{-ikr}/r$, and the two differ by a solution of the free equation. For scattering the outgoing form is the right one. Hence

$$
\boxed{\,\psi(\mathbf r) = \psi_0(\mathbf r) - \frac{m}{2\pi\hbar^2}\int\frac{e^{ik|\mathbf r - \mathbf r_0|}}{|\mathbf r - \mathbf r_0|}\,V(\mathbf r_0)\,\psi(\mathbf r_0)\,d^3r_0\,}
$$

This is exactly equivalent to the Schrödinger equation together with the boundary condition (incident wave $\psi_0$ plus outgoing waves).

**Lippmann-Schwinger form.** In Dirac notation, with $H = H_0 + V$ and $|\phi\rangle$ a free state of the same energy,

$$
|\psi^{(\pm)}\rangle = |\phi\rangle + \frac{1}{E - H_0\pm i\varepsilon}\,V\,|\psi^{(\pm)}\rangle ,\qquad \varepsilon\to0^+ .
$$

The $\pm i\varepsilon$ makes the inverse of $E - H_0$ well defined and is the operator form of the contour choice: $+$ gives outgoing and $-$ incoming scattered waves. In the position representation the resolvent $(E - H_0 + i\varepsilon)^{-1}$ is $(2m/\hbar^2)G$, the free-particle Green's function of [[greens-functions-single-particle]], and the equation above is recovered.

## The scattering amplitude

Far from the scattering region, $|\mathbf r|\gg|\mathbf r_0|$, so $|\mathbf r - \mathbf r_0|\approx r - \hat{\mathbf r}\cdot\mathbf r_0$ in the exponent and $\approx r$ in the denominator. With $\psi_0 = Ae^{ikz}$ and $\mathbf k' = k\hat{\mathbf r}$ (the wave vector of the scattered particle),

$$
\psi(\mathbf r)\approx Ae^{ikz} - \frac{m}{2\pi\hbar^2}\frac{e^{ikr}}{r}\int e^{-i\mathbf k'\cdot\mathbf r_0}\,V(\mathbf r_0)\,\psi(\mathbf r_0)\,d^3r_0 ,
$$

so that, exactly,

$$
f(\theta,\phi) = -\frac{m}{2\pi\hbar^2A}\int e^{-i\mathbf k'\cdot\mathbf r_0}\,V(\mathbf r_0)\,\psi(\mathbf r_0)\,d^3r_0 .
$$

The amplitude needs $\psi$ only inside the potential.

## First Born approximation

If the potential is weak, the wave inside it is not much changed: put $\psi(\mathbf r_0)\approx\psi_0(\mathbf r_0) = Ae^{i\mathbf k\cdot\mathbf r_0}$ with $\mathbf k = k\hat{\mathbf z}$. Then

$$
\boxed{\,f(\theta,\phi)\approx-\frac{m}{2\pi\hbar^2}\int e^{i(\mathbf k - \mathbf k')\cdot\mathbf r_0}\,V(\mathbf r_0)\,d^3r_0\,}
$$

The amplitude is the Fourier transform of the potential at the **momentum transfer** $\hbar\boldsymbol\kappa = \hbar(\mathbf k' - \mathbf k)$, of magnitude

$$
\kappa = 2k\sin(\theta/2) .
$$

Special cases:

- **Low energy** ($ka\ll1$ over the range $a$ of the potential): the exponential is 1 and $f\approx-(m/2\pi\hbar^2)\int V\,d^3r$, isotropic.
- **Spherical symmetry:** doing the angular integral with the polar axis along $\boldsymbol\kappa$,

$$
f(\theta)\approx-\frac{2m}{\hbar^2\kappa}\int_0^\infty r\,V(r)\,\sin(\kappa r)\,dr .
$$

Two general features follow. The first Born amplitude is linear in $V$, so the cross section is the same for attraction and repulsion. And it is real for a real symmetric potential, so it violates the optical theorem $\sigma = (4\pi/k)\,\mathrm{Im}f(0)$: the imaginary part of $f$ first appears in second order, where it matches the first-order cross section.

## Examples

!!! example "Soft sphere"

    $V = V_0$ for $r<a$, zero outside:

    $$
    f(\theta)\approx-\frac{2mV_0}{\hbar^2\kappa^3}\big[\sin\kappa a - \kappa a\cos\kappa a\big]\ \xrightarrow{\ \kappa a\ll1\ }\ -\frac{2mV_0a^3}{3\hbar^2} ,\qquad \sigma\approx4\pi\Big(\frac{2mV_0a^3}{3\hbar^2}\Big)^2 .
    $$

!!! example "Yukawa potential"

    $V = \beta\,e^{-\mu r}/r$:

    $$
    f(\theta)\approx-\frac{2m\beta}{\hbar^2(\mu^2 + \kappa^2)} ,\qquad \sigma\approx\frac{16\pi m^2\beta^2}{\hbar^4\mu^2(\mu^2 + 4k^2)} .
    $$

    Both were checked by numerical quadrature (with $\hbar = m = \beta = \mu = 1$: $\sigma = 25.1327$ at $k = 0.5$ and $2.9568$ at $k = 2$, from the closed form and from integrating $|f|^2$ over angles).

!!! example "Rutherford scattering"

    Setting $\beta = q_1q_2/4\pi\epsilon_0$ and $\mu\to0$ in the Yukawa result,

    $$
    f(\theta)\approx-\frac{2mq_1q_2}{4\pi\epsilon_0\hbar^2\kappa^2} ,\qquad \frac{d\sigma}{d\Omega} = \Big[\frac{q_1q_2}{16\pi\epsilon_0E\sin^2(\theta/2)}\Big]^2 ,
    $$

    which is the classical Rutherford formula of [[scattering-cross-sections-and-amplitude]], with no $\hbar$ in it. It is also the exact quantum result. This triple agreement is a special property of the Coulomb potential, and the derivation is not really legitimate: the Coulomb potential does not fall off fast enough for the asymptotic form $e^{ikz} + fe^{ikr}/r$ to hold, which is why it is reached here as a limit.

## The Born series

Writing the integral equation schematically as $\psi = \psi_0 + \int gV\psi$ with $g = (2m/\hbar^2)G$, and substituting it into itself repeatedly,

$$
\psi = \psi_0 + \int gV\psi_0 + \iint gVgV\psi_0 + \iiint gVgVgV\psi_0 + \cdots .
$$

The $n$-th term describes a wave that propagates freely, is scattered $n$ times by the potential, and propagates out. The first Born approximation keeps the single-scattering term. In operator form the series sums to the transition operator $T = V + V(E - H_0 + i\varepsilon)^{-1}T$, defined so that $V|\psi^{(+)}\rangle = T|\phi\rangle$; the exact amplitude is the matrix element of $T$ between plane waves, and the Born approximation is $T\approx V$. This is the scattering analogue of the perturbation series of [[rayleigh-schrodinger-perturbation-theory]].

## When is it valid?

The approximation requires the scattered wave to be small compared with the incident wave inside the potential. For a potential of strength $V_0$ and range $a$ this gives, as order-of-magnitude conditions,

$$
\frac{m|V_0|a^2}{\hbar^2}\ll1\quad\text{(any energy)} ,\qquad\text{or}\qquad \frac{|V_0|a}{\hbar v}\ll1\quad\text{(high energy, } ka\gg1) .
$$

The first says the potential is too weak to come near binding a state. The second says a fast particle spends too little time in the potential to be much affected, however strong it is. (For the Yukawa potential Sakurai's high-energy condition carries an extra factor $\ln ka$, from the slowly decaying tail.)

!!! example "Attractive well: Born against exact"

    $V = -V_0$ for $r<a$, with $\hbar = m = a = 1$. The exact total cross section is the partial-wave sum of [[partial-wave-analysis-and-phase-shifts]] and the Born value is the angular integral of $|f|^2$. Here $mV_0a^2/\hbar^2 = V_0$ and $V_0a/\hbar v = V_0/k$.

    | $V_0$ | $k$ | $V_0/k$ | exact $\sigma/\pi a^2$ | Born $\sigma/\pi a^2$ | Born / exact |
    |---|---|---|---|---|---|
    | 0.1 | 0.1 | 1.0 | 0.02091 | 0.01771 | 0.85 |
    | 0.1 | 1 | 0.1 | 0.01335 | 0.01207 | 0.90 |
    | 0.1 | 5 | 0.02 | 0.00079 | 0.00079 | 1.00 |
    | 1 | 0.1 | 10 | 41.72 | 1.771 | 0.04 |
    | 1 | 1 | 1.0 | 2.270 | 1.207 | 0.53 |
    | 1 | 5 | 0.2 | 0.07928 | 0.07927 | 1.00 |
    | 5 | 1 | 5.0 | 6.855 | 30.19 | 4.4 |
    | 5 | 5 | 1.0 | 1.658 | 1.982 | 1.20 |
    | 5 | 20 | 0.25 | 0.1234 | 0.1249 | 1.01 |

    A weak well is described well at all energies, and any well at high enough energy. For $V_0 = 1$ at low energy the Born value is wrong by a factor 24: this well ($\sqrt{2V_0} = 1.41$) is close to the depth $\pi^2/8$ at which it first binds a state, and the true cross section is resonantly large ([[low-energy-scattering-and-resonances]]). No finite order of perturbation theory can produce a bound state.

**Born phase shifts.** Expanding the first Born amplitude in Legendre polynomials and comparing with the partial-wave series for small $\delta_l$ gives

$$
\delta_l\approx-\frac{2mk}{\hbar^2}\int_0^\infty V(r)\,\big[j_l(kr)\big]^2\,r^2\,dr .
$$

For the same well with $V_0 = 0.1$, $k = 1$ the exact phase shifts are $\delta_0 = 0.0574$, $\delta_1 = 0.00394$, $\delta_2 = 0.00011$, and the formula gives $0.0545$, $0.00385$, $0.00011$. The sign rule (attraction gives positive $\delta_l$) is explicit, and the formula is most accurate for the higher partial waves, which the centrifugal barrier keeps away from the potential.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 10.4: integral form and Green's function, Eqs. (10.49)-(10.67); first Born approximation, Eqs. (10.68)-(10.94), Examples 10.4 (soft sphere), 10.5 (Yukawa), 10.6 (Rutherford); Born series, Eqs. (10.97)-(10.101); Problems 10.8 and 10.10-10.15. Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 6.1, pp. 371-376 (transition operator and the Lippmann-Schwinger equation (6.29)); Sec. 6.2, pp. 376-381 (Green's function of the Helmholtz equation (6.48)); Sec. 6.3, pp. 384-388 (Born approximation, Yukawa amplitude (6.78), validity conditions (6.84)-(6.85), second order (6.86)).

Naming: Griffiths calls the incident wave vector $\mathbf k'$ and the scattered one $\mathbf k$, the reverse of the naming used here (which follows Sakurai); the expressions are otherwise the same, and for spherically symmetric potentials only $|\mathbf k' - \mathbf k|$ matters. The Born phase-shift formula is a standard result that is not derived in either book; it is verified numerically here. Tables are computed in `griffiths/ch10_scattering.py` (sections B, C and E).
