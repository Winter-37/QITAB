---
id: classical-orthogonal-polynomials
title: "Hermite, Legendre and Laguerre polynomials"
summary: The three families of polynomials that solve the oscillator, the angular equation and the hydrogen radial equation. For each: the differential equation, the Rodrigues formula, the generating function, the three-term recursion, orthogonality with its weight and normalization, and the first few members, all verified symbolically. Includes associated Legendre functions with the (−1)^m phase inside, and the two incompatible conventions for associated Laguerre polynomials that make formulas from older books wrong by factorials.
status: in-progress
kind: reference
level: intermediate
tags: [special-functions, orthogonal-polynomials, hermite-polynomials, legendre-polynomials, associated-legendre-functions, laguerre-polynomials, rodrigues-formula, generating-function, recursion-relation, griffiths, sakurai]
prerequisites: [orthonormal-functions-and-operators]
related: [spherical-bessel-functions, harmonic-oscillator-analytic-solution, central-potentials-and-spherical-harmonics, hydrogen-atom, fourier-transforms-and-the-dirac-delta]
order: 10
date: 2026-11-17
---

## A common pattern

Each family arises from a second-order differential equation whose polynomial solutions exist only for integer "quantum numbers", which is exactly how the oscillator, angular momentum and hydrogen are quantized. Each family is orthogonal with respect to a weight $w(x)$ on an interval, so the polynomials are the eigenfunctions of a Hermitian (Sturm-Liouville) operator in the inner product $\int\bar f g\,w\,dx$ ([[orthonormal-functions-and-operators]]). And each has a Rodrigues formula $p_n\propto w^{-1}\,d^n(w\,s^n)/dx^n$, a generating function, and a three-term recursion. Normalizations are conventional, and this is where the trouble lies.

| family | interval | weight $w(x)$ | where it appears |
|---|---|---|---|
| Hermite $H_n$ | $(-\infty,\infty)$ | $e^{-x^2}$ | harmonic oscillator, $x = \sqrt{m\omega/\hbar}\,q$ |
| Legendre $P_l$ | $[-1,1]$ | 1 | angular equation, $x = \cos\theta$ |
| Laguerre $L_q^p$ | $[0,\infty)$ | $x^pe^{-x}$ | hydrogen radial equation, $x = 2r/na$ |

All identities below were verified symbolically with SymPy, and the numerical values against SciPy.

## Hermite polynomials

**Equation.** $H_n'' - 2xH_n' + 2nH_n = 0$, from the oscillator equation after the factor $e^{-x^2/2}$ is removed ([[harmonic-oscillator-analytic-solution]]).

**Rodrigues formula and generating function.**

$$
H_n(x) = (-1)^ne^{x^2}\frac{d^n}{dx^n}e^{-x^2} ,\qquad e^{2xt - t^2} = \sum_{n=0}^\infty H_n(x)\frac{t^n}{n!} .
$$

**Recursion and derivative.**

$$
H_{n+1} = 2xH_n - 2nH_{n-1} ,\qquad H_n' = 2nH_{n-1} .
$$

**Orthogonality.**

$$
\int_{-\infty}^\infty H_mH_n\,e^{-x^2}\,dx = \sqrt\pi\,2^nn!\,\delta_{mn} .
$$

**First few** ("physicists'" Hermite polynomials, leading coefficient $2^n$):

$$
H_0 = 1,\quad H_1 = 2x,\quad H_2 = 4x^2 - 2,\quad H_3 = 8x^3 - 12x,\quad H_4 = 16x^4 - 48x^2 + 12 .
$$

The oscillator eigenfunctions are then $\psi_n = (m\omega/\pi\hbar)^{1/4}(2^nn!)^{-1/2}H_n(\xi)e^{-\xi^2/2}$. Probabilists use $He_n(x) = 2^{-n/2}H_n(x/\sqrt2)$, with weight $e^{-x^2/2}$; NumPy's `hermite` module is the physicists' form and `hermite_e` the probabilists'.

## Legendre polynomials and associated Legendre functions

**Equation.** $(1 - x^2)P_l'' - 2xP_l' + l(l+1)P_l = 0$, the $m = 0$ angular equation with $x = \cos\theta$. The power-series solution terminates, and is finite at $x = \pm1$, only for integer $l\ge0$.

**Rodrigues formula and generating function.**

$$
P_l(x) = \frac{1}{2^ll!}\frac{d^l}{dx^l}(x^2 - 1)^l ,\qquad \frac{1}{\sqrt{1 - 2xt + t^2}} = \sum_{l=0}^\infty P_l(x)\,t^l .
$$

The generating function is the multipole expansion of $1/|\mathbf r - \mathbf r'|$ with $t = r_</r_>$ and $x = \cos\gamma$.

**Recursion (Bonnet).** $(l+1)P_{l+1} = (2l+1)xP_l - lP_{l-1}$.

**Orthogonality and normalization.**

$$
\int_{-1}^1P_lP_{l'}\,dx = \frac{2}{2l+1}\,\delta_{ll'} ,\qquad P_l(1) = 1 ,\qquad P_l(-x) = (-1)^lP_l(x) .
$$

**First few.**

$$
P_0 = 1,\quad P_1 = x,\quad P_2 = \tfrac12(3x^2 - 1),\quad P_3 = \tfrac12(5x^3 - 3x),\quad P_4 = \tfrac18(35x^4 - 30x^2 + 3) .
$$

**Associated Legendre functions** ($0\le m\le l$), in the convention of Griffiths' 3rd edition and of SciPy's `lpmv`:

$$
P_l^m(x) = (-1)^m(1 - x^2)^{m/2}\frac{d^m}{dx^m}P_l(x) ,\qquad \int_{-1}^1P_l^mP_{l'}^m\,dx = \frac{2}{2l+1}\frac{(l+m)!}{(l-m)!}\,\delta_{ll'} .
$$

The factor $(-1)^m$ is the Condon-Shortley phase. Some books leave it out of $P_l^m$ and put it into $Y_l^m$ instead, and some omit it altogether, so the sign of $Y_l^m$ for odd $m>0$ must be checked when combining sources. The spherical harmonics built from this $P_l^m$ are those of [[central-potentials-and-spherical-harmonics]]. Note that $P_l^m$ is a polynomial only for even $m$; for odd $m$ it carries a factor $\sqrt{1 - x^2} = \sin\theta$.

## Laguerre and associated Laguerre polynomials

**Equation.** $xL_q^{p\,\prime\prime} + (p + 1 - x)L_q^{p\,\prime} + qL_q^p = 0$, which is the hydrogen radial equation after the factors $x^le^{-x/2}$ are removed, with $p = 2l+1$ and $q = n - l - 1$.

**Convention of Griffiths' 3rd edition (and of SciPy's `genlaguerre`):**

$$
L_q(x) = \frac{e^x}{q!}\frac{d^q}{dx^q}\big(e^{-x}x^q\big) ,\qquad L_q^p(x) = (-1)^p\frac{d^p}{dx^p}L_{p+q}(x) .
$$

So $L_q(0) = 1$, and

$$
L_0 = 1,\quad L_1 = 1 - x,\quad L_2 = \tfrac12x^2 - 2x + 1,\quad L_3 = -\tfrac16x^3 + \tfrac32x^2 - 3x + 1 .
$$

**Orthogonality.**

$$
\int_0^\infty L_q^p\,L_{q'}^p\;x^pe^{-x}\,dx = \frac{(q+p)!}{q!}\,\delta_{qq'} .
$$

For the hydrogen radial functions the relevant integral has an extra power of $x$:

$$
\int_0^\infty\big[x^le^{-x/2}L_{n-l-1}^{2l+1}(x)\big]^2x^2\,dx = \frac{2n\,(n+l)!}{(n-l-1)!} ,
$$

which fixes the normalization quoted in [[hydrogen-atom]] (checked for $n\le3$, all $l$).

**The convention trap.** Older books, including Griffiths' 2nd edition, define $L_q = e^x\frac{d^q}{dx^q}(e^{-x}x^q)$, which is $q!$ times the polynomial above (for instance $L_2 = x^2 - 4x + 2$), and define the associated polynomials from those, with a different index placement. Normalization constants for hydrogen therefore differ between editions by factorials. A formula for $R_{nl}$ may only be combined with Laguerre polynomials from the same source. Sakurai's Appendix B makes the same warning.

## How to use them numerically

Use the recursions, not the explicit formulas: for large $n$ the alternating sums lose all precision, while the three-term recursions are stable when run upward from $n = 0,1$. Library routines (SciPy `eval_hermite`, `eval_legendre`, `lpmv`, `eval_genlaguerre`) do this, but check their conventions against the table above before relying on a sign.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018): Sec. 2.3.2 (Hermite polynomials, Table 2.1) and Problem 2.17 (Rodrigues formula (2.87), recursion, derivative (2.89), generating function); Sec. 4.1.2, Eqs. (4.27)-(4.28) (associated Legendre function and Rodrigues formula), Tables 4.1-4.2, Problem 4.8 (orthogonality (4.34)) and Problem 3.31 (Legendre polynomials by Gram-Schmidt); Sec. 4.2.2, Eqs. (4.86)-(4.88) (associated Laguerre polynomials), Tables 4.5-4.6, Problem 4.14. Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Appendix B, Secs. B.4 (oscillator and Hermite polynomials, pp. 523-524) and B.6 (hydrogen; remark that Laguerre conventions vary, p. 528).

The generating functions for Legendre polynomials and the orthogonality integrals are standard; every formula in this note was verified symbolically in `mathematics/part0_batch5.py` (section D).
