---
id: wkb-approximation
title: The WKB approximation
summary: The semiclassical solution of the one-dimensional Schrödinger equation for a slowly varying potential. Writing ψ as amplitude times phase gives ψ ≈ C p^(-1/2) exp(± i ∫p dx/ħ) in the classical region and real exponentials where E < V. Covers the derivation in Griffiths' and Sakurai's forms, the validity condition and its failure at turning points, the link to the classical probability 1/v, and the quantization condition ∫p dx = nπħ for a well with two vertical walls, tested on a tilted well.
status: in-progress
kind: derivation
level: intermediate
tags: [wkb, semiclassical-approximation, classical-limit, quantization-condition, turning-points, de-broglie-wavelength, hamilton-jacobi, griffiths, sakurai]
prerequisites: [stationary-states, infinite-square-well, free-particle-and-wave-packets]
related: [wkb-connection-formulas-and-quantization, wkb-tunneling-and-alpha-decay, one-dimensional-scattering-and-transfer-matrix, rayleigh-schrodinger-perturbation-theory]
order: 10
date: 2026-11-15
---

## The idea

For constant $V$ and $E>V$ the solutions of the Schrödinger equation are $\psi = Ae^{\pm ikx}$ with $k = \sqrt{2m(E-V)}/\hbar$: fixed amplitude, fixed wavelength $\lambda = 2\pi/k$. If $V(x)$ varies slowly compared with $\lambda$, the solution should still look like a sinusoid whose wavelength and amplitude drift with $x$. For $E<V$ the same holds with exponentials in place of sinusoids. The method is named after Wentzel, Kramers and Brillouin. It gives approximate bound-state energies and tunnelling rates, and it shows how classical mechanics emerges at short wavelength.

Write the Schrödinger equation as

$$
\frac{d^2\psi}{dx^2} = -\frac{p^2}{\hbar^2}\,\psi ,\qquad p(x) = \sqrt{2m\,[E - V(x)]} ,
$$

where $p(x)$ is the classical momentum of a particle with energy $E$ at position $x$. It is real in the **classical region** $E>V$ and imaginary in the nonclassical region $E<V$.

## Derivation in the classical region

Put $\psi(x) = A(x)\,e^{i\phi(x)}$ with $A$ and $\phi$ real. Substituting and separating real and imaginary parts gives two exact equations,

$$
A'' = A\Big[(\phi')^2 - \frac{p^2}{\hbar^2}\Big] ,\qquad \big(A^2\phi'\big)' = 0 .
$$

The second integrates at once:

$$
A = \frac{C}{\sqrt{|\phi'|}} .
$$

The first cannot be solved in general. The approximation is to drop $A''$, assuming the amplitude varies slowly: $|A''/A|\ll(\phi')^2$ and $p^2/\hbar^2$. Then $\phi' = \pm p/\hbar$ and

$$
\boxed{\,\psi(x) \approx \frac{C}{\sqrt{p(x)}}\,\exp\Big[\pm\frac{i}{\hbar}\int p(x)\,dx\Big]\,}
$$

The general solution is a combination of the two signs, with complex constants.

**Reading the result.** The phase advances at the local rate $p/\hbar$, the de Broglie relation applied point by point. The amplitude gives

$$
|\psi|^2 \approx \frac{|C|^2}{p(x)} ,
$$

the classical probability density: a particle spends a time $dx/v$ in the interval $dx$, so it is most likely found where it moves slowest.

## Sakurai's form: an expansion in ħ

Sakurai writes $\psi = \exp[iW(x)/\hbar]$ with $W$ complex, which turns the Schrödinger equation into

$$
i\hbar\,W'' - (W')^2 + p^2 = 0 .
$$

Treating the first term as small gives $W_0' = \pm p$, the Hamilton-Jacobi equation of classical mechanics for the abbreviated action. Inserting $W_0''$ back gives the next order, $W' = \pm p + i\hbar\,p'/(2p)$, which integrates to

$$
W = \pm\int p\,dx + \frac{i\hbar}{2}\ln p ,
$$

and the logarithm reproduces the prefactor $1/\sqrt p$. WKB is thus the first two terms of an expansion of the phase in powers of $\hbar$, which is why it is called semiclassical.

## Validity

The condition $\hbar|W''|\ll(W')^2$ reads

$$
\Big|\frac{\hbar\,p'}{p^2}\Big| = \Big|\frac{1}{2\pi}\frac{d\lambda}{dx}\Big| \ll 1 ,\qquad\text{equivalently}\qquad \frac{m\hbar\,|V'|}{|p|^3}\ll1 .
$$

The local wavelength must change by a small fraction of itself over one wavelength. Two consequences follow.

- The approximation improves at high energy and for smooth potentials.
- It fails at a **classical turning point**, where $E = V$ and $p = 0$: the wavelength diverges and the amplitude $1/\sqrt p$ blows up. The true wave function is finite there. Joining the solutions across a turning point is the subject of [[wkb-connection-formulas-and-quantization]].

## The nonclassical region

For $E<V$ the same steps go through with $p$ imaginary:

$$
\psi(x) \approx \frac{C}{\sqrt{|p(x)|}}\,\exp\Big[\pm\frac{1}{\hbar}\int|p(x)|\,dx\Big] .
$$

These growing and decaying exponentials describe tunnelling ([[wkb-tunneling-and-alpha-decay]]).

## A well with two vertical walls

Let $V(x)$ be arbitrary for $0<x<a$ and infinite outside, with $E>V$ throughout. In real form

$$
\psi(x) \approx \frac{1}{\sqrt{p(x)}}\,\big[C_1\sin\phi(x) + C_2\cos\phi(x)\big] ,\qquad \phi(x) = \frac1\hbar\int_0^xp(x')\,dx' .
$$

$\psi(0) = 0$ requires $C_2 = 0$, and $\psi(a) = 0$ requires $\phi(a) = n\pi$:

$$
\boxed{\,\int_0^ap(x)\,dx = n\pi\hbar ,\qquad n = 1,2,3,\dots\,}
$$

There are no turning points, so no connection formulas are needed. For a flat bottom $p$ is constant and the condition gives $E_n = n^2\pi^2\hbar^2/(2ma^2)$, the exact result ([[infinite-square-well]]); the WKB wave function is exact as well, because $A$ is constant.

!!! example "Tilted well"

    Take $V(x) = Fx$ for $0<x<1$ with walls at 0 and 1, in units $\hbar = m = 1$. If $E>F$ the whole well is classically allowed and

    $$
    \int_0^1\sqrt{2(E - Fx)}\,dx = \frac{2\sqrt2}{3F}\Big[E^{3/2} - (E - F)^{3/2}\Big] = n\pi .
    $$

    If $E<F$ the particle turns around at $x = E/F$ before reaching the right wall. Then the rule for one wall and one turning point applies, with $n - \tfrac14$ in place of $n$ ([[wkb-connection-formulas-and-quantization]]). The exact levels come from diagonalizing $H$ in 120 square-well functions; first-order perturbation theory is $E_n^0 + F/2$.

    | $n$ | exact, $F = 5$ | WKB | first-order PT | exact, $F = 40$ | WKB | first-order PT |
    |---|---|---|---|---|---|---|
    | 1 | 7.380 | 7.543 | 7.435 | 21.775 | 21.539 | 24.935 |
    | 2 | 22.255 | 22.266 | 22.239 | 40.451 | 41.637 | 39.739 |
    | 3 | 46.923 | 46.925 | 46.913 | 65.021 | 65.177 | 64.413 |
    | 4 | 81.463 | 81.463 | 81.457 | 99.338 | 99.381 | 98.957 |
    | 5 | 125.874 | 125.874 | 125.870 | 143.624 | 143.641 | 143.370 |
    | 6 | 180.156 | 180.156 | 180.153 | 197.833 | 197.841 | 197.653 |

    Three things to note. WKB improves rapidly with $n$, as the wavelength shrinks. For the weak tilt, perturbation theory is better at $n = 1$ and WKB better from $n = 2$ on. For the strong tilt the lowest level has its turning point inside the well and the $n - \tfrac14$ rule gets it to 1 percent, while $n = 2$, whose energy is just above $F$ so that $p\to0$ at the right wall, is the worst case for either WKB rule.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Ch. 9 introduction and Sec. 9.1, Eqs. (9.1)-(9.17), Example 9.1; Problems 9.1 and 9.2. Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 2.5.4, Eqs. (2.241)-(2.250), pp. 104-105, for the expansion of the phase and the validity condition.

The tilted-well example is my own; it is computed in `griffiths/ch09_wkb.py` (section E).
