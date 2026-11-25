---
id: spherical-bessel-functions
title: Spherical Bessel, Neumann and Hankel functions
summary: The radial functions of a free particle in three dimensions. Defines j_l, n_l and h_l^(1,2) through Rayleigh's formulas (Griffiths' sign convention), lists the first few, their behaviour at small and large argument, recursion and derivative relations, the Wronskian, the zeros that quantize the spherical well, orthogonality on a sphere, the integral representation, and the plane-wave (Rayleigh) expansion e^{ikz} = Σ i^l (2l+1) j_l(kr) P_l(cos θ), all checked numerically.
status: in-progress
kind: reference
level: intermediate
tags: [special-functions, spherical-bessel-functions, spherical-neumann-functions, spherical-hankel-functions, rayleigh-formula, plane-wave-expansion, bessel-zeros, griffiths, sakurai]
prerequisites: [classical-orthogonal-polynomials, fourier-transforms-and-the-dirac-delta]
related: [central-potentials-and-spherical-harmonics, partial-wave-analysis-and-phase-shifts, low-energy-scattering-and-resonances, schrodinger-equation-in-three-dimensions]
order: 70
date: 2026-11-17
---

## Where they come from

For $V = 0$ the radial equation for $u = rR$ at energy $E = \hbar^2k^2/2m$ is

$$
\frac{d^2u}{dr^2} = \Big[\frac{l(l+1)}{r^2} - k^2\Big]u .
$$

In terms of $R$ and $x = kr$ this is the **spherical Bessel equation**

$$
x^2R'' + 2xR' + \big[x^2 - l(l+1)\big]R = 0 ,
$$

whose two independent solutions are $j_l(x)$ and $n_l(x)$. They are related to the ordinary Bessel functions of half-integer order,

$$
j_l(x) = \sqrt{\frac{\pi}{2x}}\,J_{l+1/2}(x) ,\qquad n_l(x) = (-1)^{l+1}\sqrt{\frac{\pi}{2x}}\,J_{-l-1/2}(x) ,
$$

and, unlike ordinary Bessel functions, are elementary: trigonometric functions times powers of $1/x$.

## Rayleigh's formulas

$$
\boxed{\,j_l(x) = (-x)^l\Big(\frac1x\frac{d}{dx}\Big)^l\frac{\sin x}{x} ,\qquad n_l(x) = -(-x)^l\Big(\frac1x\frac{d}{dx}\Big)^l\frac{\cos x}{x}\,}
$$

$$
j_0 = \frac{\sin x}{x} ,\qquad j_1 = \frac{\sin x}{x^2} - \frac{\cos x}{x} ,\qquad j_2 = \Big(\frac{3}{x^3} - \frac1x\Big)\sin x - \frac{3}{x^2}\cos x ,
$$

$$
n_0 = -\frac{\cos x}{x} ,\qquad n_1 = -\frac{\cos x}{x^2} - \frac{\sin x}{x} ,\qquad n_2 = -\Big(\frac{3}{x^3} - \frac1x\Big)\cos x - \frac{3}{x^2}\sin x .
$$

This sign convention for $n_l$ (Griffiths, Sakurai and SciPy's `spherical_yn`) is the common one; some books call these $y_l$, and a few use the opposite sign. The **spherical Hankel functions**

$$
h_l^{(1)} = j_l + i\,n_l ,\qquad h_l^{(2)} = j_l - i\,n_l
$$

behave as $(\mp i)^{l+1}e^{\pm ix}/x$ at large $x$: outgoing and incoming spherical waves. For example $h_0^{(1)} = -ie^{ix}/x$.

## Limits

**Small $x$.**

$$
j_l(x)\approx\frac{x^l}{(2l+1)!!} ,\qquad n_l(x)\approx-\frac{(2l-1)!!}{x^{l+1}}\qquad(x\ll l+1) ,
$$

with $(-1)!! = 1$. The $j_l$ are regular at the origin and the $n_l$ diverge, so only $j_l$ is allowed in a region containing $r = 0$. The factor $x^l$ is the centrifugal suppression responsible for $\delta_l\propto k^{2l+1}$ in low-energy scattering ([[partial-wave-analysis-and-phase-shifts]]).

**Large $x$.**

$$
j_l(x)\to\frac{\sin(x - l\pi/2)}{x} ,\qquad n_l(x)\to-\frac{\cos(x - l\pi/2)}{x}\qquad(x\gg l(l+1)/2) .
$$

The crossover is near $x\approx l$: the classical turning point of the centrifugal barrier, $kr = \sqrt{l(l+1)}$. The leading correction is $\frac{l(l+1)}{2x}\cos(x - l\pi/2)/x$ for $j_l$, so the asymptotic form is good to a relative error of order $l(l+1)/2x$ (checked at $x = 50$ and 200 for $l = 1, 2$).

## Relations

With $f_l$ standing for any of $j_l$, $n_l$, $h_l^{(1,2)}$:

$$
f_{l-1} + f_{l+1} = \frac{2l+1}{x}f_l ,\qquad (2l+1)f_l' = l\,f_{l-1} - (l+1)f_{l+1} ,
$$

$$
j_l\,n_l' - j_l'\,n_l = \frac{1}{x^2}\qquad\text{(Wronskian)} .
$$

All three were checked numerically for $l\le5$ on $0.5\le x\le30$. As with the polynomials of [[classical-orthogonal-polynomials]], upward recursion is stable for $n_l$; for $j_l$ at $x<l$ it is unstable and library routines recur downward instead.

**Integral representation.**

$$
j_l(x) = \frac{1}{2i^l}\int_{-1}^1P_l(u)\,e^{ixu}\,du ,
$$

checked for $l\le4$. It says that $j_l$ is (up to a factor) the Fourier transform of a Legendre polynomial on $[-1,1]$.

## Zeros and the spherical well

For a particle in an impenetrable sphere of radius $a$, $R = j_l(kr)$ must vanish at $r = a$, so $ka = \beta_{Nl}$, the $N$-th zero of $j_l$, and $E_{Nl} = \hbar^2\beta_{Nl}^2/2ma^2$ ([[central-potentials-and-spherical-harmonics]]).

| $l$ | $\beta_{1l}$ | $\beta_{2l}$ | $\beta_{3l}$ |
|---|---|---|---|
| 0 | 3.1416 | 6.2832 | 9.4248 |
| 1 | 4.4934 | 7.7253 | 10.9041 |
| 2 | 5.7635 | 9.0950 | 12.3229 |
| 3 | 6.9879 | 10.4171 | 13.6980 |

For $l = 0$ the zeros are $N\pi$; for $l = 1$ they solve $\tan x = x$, the same equation that gave the Ramsauer-Townsend condition in [[low-energy-scattering-and-resonances]].

**Orthogonality on the sphere.** For fixed $l$,

$$
\int_0^aj_l\Big(\beta_{Nl}\frac ra\Big)j_l\Big(\beta_{N'l}\frac ra\Big)r^2\,dr = \frac{a^3}{2}\big[j_{l+1}(\beta_{Nl})\big]^2\,\delta_{NN'} ,
$$

checked for $l\le2$, $N,N'\le3$. These are the normalization integrals of the spherical-well eigenfunctions.

## The plane-wave expansion

A plane wave along $z$ is a superposition of all partial waves:

$$
\boxed{\,e^{ikr\cos\theta} = \sum_{l=0}^\infty i^l(2l+1)\,j_l(kr)\,P_l(\cos\theta)\,}
$$

This follows from the integral representation and the completeness of the Legendre polynomials. Summing 40 terms at $kr = 3.74$, $\theta = 0.9$ reproduces $e^{ikr\cos\theta}$ to ten digits. It is the starting point of partial-wave scattering theory, and combined with the addition theorem for spherical harmonics it gives the expansion of $e^{i\mathbf k\cdot\mathbf r}$ for any direction of $\mathbf k$.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 4.1.3, Eqs. (4.41)-(4.50): spherical Bessel and Neumann functions (4.45)-(4.46), Table 4.4 (first few and small-$x$ forms), Fig. 4.2, zeros and the infinite spherical well (4.48)-(4.50); Sec. 10.2, Eqs. (10.18)-(10.28) (Hankel functions and Rayleigh's formula for the plane wave). Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Appendix B, Sec. B.5, pp. 524-527 (relation to $J_{l+1/2}$, Hankel functions, asymptotic forms); Sec. 6.4, pp. 388-392 (partial-wave expansion of the plane wave).

The recursions, Wronskian, integral representation and sphere orthogonality are standard results not derived in either book; each was checked in `mathematics/part0_batch5.py` (sections E and E2).
