---
id: gaussian-integral-identities
title: Gaussian integrals and the Boys function
summary: Moments of one- and three-dimensional Gaussians, the Gaussian product theorem, the overlap of two normalized s Gaussians, the Fourier transform of a Gaussian, the Gaussian representation of 1/r, and the Boys function F_n(T) - its erf and incomplete-gamma forms, downward recursion, values at T = 0 and large-T asymptotics - with the Coulomb energy of two Gaussian charges, erf(√α R)/R, checked against PySCF.
status: in-progress
kind: reference
level: intermediate
tags: [gaussian-integrals, boys-function, gaussian-product-theorem, molecular-integrals, erf, identities]
prerequisites: []
related: [gaussian-basis-functions, gaussian-overlap-distributions-and-one-electron-integrals, electron-repulsion-integrals-md-os-rys, fourier-transforms-and-the-dirac-delta]
order: 40
date: 2026-11-17
---

$a, b > 0$ are Gaussian exponents; $(2n-1)!! = 1\cdot3\cdots(2n-1)$ with $(-1)!! = 1$.

## One-dimensional moments

$$
\int_{-\infty}^{\infty}e^{-ax^2}\,\mathrm dx = \sqrt{\frac{\pi}{a}},\qquad
\int_{-\infty}^{\infty}x^{2n}e^{-ax^2}\,\mathrm dx = \frac{(2n-1)!!}{(2a)^n}\sqrt{\frac{\pi}{a}},
$$

and odd moments vanish. The half-line moments of any power are

$$
\int_0^\infty r^ne^{-ar^2}\,\mathrm dr = \frac{\Gamma\!\big(\tfrac{n+1}{2}\big)}{2a^{(n+1)/2}}
\qquad(n > -1),
$$

for example $\tfrac12\sqrt{\pi/a}$, $\tfrac1{2a}$, $\tfrac14\sqrt{\pi/a^3}$ and $\tfrac1{2a^2}$ for $n = 0,1,2,3$.

## Three dimensions

$$
\int e^{-ar^2}\,\mathrm d^3r = \Big(\frac{\pi}{a}\Big)^{3/2},
\qquad
\phi_a(\mathbf r) = \Big(\frac{2a}{\pi}\Big)^{3/4}e^{-ar^2}\ \ \text{is normalized}.
$$

**Gaussian product theorem.** With $p = a + b$, $\mu = ab/p$ and $\mathbf P = (a\mathbf A + b\mathbf B)/p$,

$$
e^{-a|\mathbf r - \mathbf A|^2}\,e^{-b|\mathbf r - \mathbf B|^2} = e^{-\mu|\mathbf A - \mathbf B|^2}\,e^{-p|\mathbf r - \mathbf P|^2} .
$$

So the overlap of two normalized s Gaussians is

$$
S_{ab} = \Big(\frac{4ab}{\pi^2}\Big)^{3/4}\Big(\frac{\pi}{p}\Big)^{3/2}e^{-\mu|\mathbf A - \mathbf B|^2}.
$$

Derivations and the Hermite-Gaussian machinery built on this are in [[gaussian-overlap-distributions-and-one-electron-integrals]].

**Fourier transform** (symmetric convention of [[fourier-transforms-and-the-dirac-delta]]):

$$
\frac{1}{\sqrt{2\pi}}\int e^{-ax^2}e^{-ikx}\,\mathrm dx = \frac{1}{\sqrt{2a}}\,e^{-k^2/4a} .
$$

**Gaussian representation of the Coulomb kernel.**

$$
\frac1r = \frac{2}{\sqrt\pi}\int_0^\infty e^{-r^2t^2}\,\mathrm dt .
$$

Inserting this into a Coulomb integral turns it into a Gaussian integral over $\mathbf r$ followed by a one-dimensional integral over $t$, which is the Boys function.

## The Boys function

$$
F_n(T) = \int_0^1 t^{2n}e^{-Tt^2}\,\mathrm dt,\qquad T\ge0 .
$$

| Property | Formula |
|---|---|
| order zero | $F_0(T) = \dfrac12\sqrt{\dfrac{\pi}{T}}\operatorname{erf}\sqrt T$ |
| incomplete gamma form | $F_n(T) = \dfrac{\Gamma(n+\tfrac12)\,P(n+\tfrac12,T)}{2T^{n+1/2}}$, $P$ = regularized lower incomplete gamma (`scipy.special.gammainc`) |
| at $T = 0$ | $F_n(0) = \dfrac1{2n+1}$ |
| downward recursion | $F_n(T) = \dfrac{2TF_{n+1}(T) + e^{-T}}{2n+1}$ |
| derivative | $F_n'(T) = -F_{n+1}(T)$ |
| large $T$ | $F_n(T)\to\dfrac{(2n-1)!!}{2^{n+1}}\sqrt{\dfrac{\pi}{T^{2n+1}}}$ |

The downward recursion is stable and is how integral codes fill all orders from the highest one. The asymptotic form is already exact to $10^{-12}$ at $T = 40$ for $n\le2$.

**Coulomb energy of two Gaussian charges.** Two unit charges with normalized densities $(a_i/\pi)^{3/2}e^{-a_ir^2}$ centred a distance $R$ apart repel with

$$
E(R) = \frac{\operatorname{erf}(\sqrt\alpha\,R)}{R} = 2\sqrt{\frac{\alpha}{\pi}}\,F_0(\alpha R^2),\qquad \alpha = \frac{a_1a_2}{a_1 + a_2},
$$

which tends to $1/R$ for large $R$ (point charges) and to the finite value $2\sqrt{\alpha/\pi}$ at $R = 0$. A point nucleus attracting a normalized Gaussian density is the limit $a_2\to\infty$, $\alpha\to a_1$.

!!! example "Two Gaussian charges"
    For $a_1 = 0.9$, $a_2 = 0.4$, $R = 1.7\,a_0$: $\alpha = 0.276\,92$ and $E = 0.467\,167\,045\,E_h$, against $1/R = 0.588\,235\,E_h$ for point charges. PySCF's two-electron integral $(ss|ss)$ over primitive s functions with exponents $a_1/2$ and $a_2/2$ (so that each density $|\phi|^2$ has exponent $a_i$) gives the same number to $10^{-14}$.

## Checks

`part9_reference.py`, section F: moments ($n\le4$ and $n\le5$) against adaptive quadrature; the product theorem at 20 random points; the s-s overlap against PySCF `int1e_ovlp`; $F_n$ for $n\le3$ and $T\in\{0,10^{-3},0.7,5,30\}$ against direct quadrature, with all rows of the table; the Coulomb formula against PySCF `int2e`; the Fourier transform and the $1/r$ integral. Agreement $10^{-10}$ or better.

## Source

Standard results; the Boys function and its recursion as used in [[electron-repulsion-integrals-md-os-rys]] (Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory*, Wiley, 2000, Sec. 9.8, pp. 365-368). Verified numerically here.
