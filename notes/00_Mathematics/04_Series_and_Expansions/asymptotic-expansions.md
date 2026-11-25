---
id: asymptotic-expansions
title: Asymptotic expansions - divergent series that work, optimal truncation, Stirling's series, Laplace's method, the Euler-Maclaurin formula, and Padé approximants
summary: An asymptotic series approximates f(x) ever better as x → ∞ (or a small parameter → 0) at fixed truncation order, even when, at fixed x, it diverges as more terms are added. The best accuracy comes from stopping near the smallest term. Stirling's series for n! and ln Γ(z), the large-x expansion of erfc, and Laplace's method for integrals of e^{N g(t)} are the standard examples. Euler–Maclaurin turns sums into integrals plus Bernoulli-number corrections. Padé approximants resum a power series into a rational function and often converge beyond its radius. Perturbation series in quantum mechanics are typically asymptotic, not convergent. Worked examples: Stirling's accuracy from n = 1, optimal truncation of erfc at x = 3, Laplace's method for a Bessel integral, and a Padé approximant for ln 2.
status: in-progress
kind: theory
level: intermediate
tags: [asymptotic-series, divergent-series, optimal-truncation, stirling-formula, gamma-function, laplace-method, steepest-descent, euler-maclaurin, bernoulli-numbers, pade-approximant, erfc]
prerequisites: [taylor-and-maclaurin-expansions, integral-calculus]
related: [sequences-series-and-convergence, power-series-and-radius-of-convergence, limits-and-continuity, laurent-series-singularities-and-residues]
key: stirling
order: 70
date: 2026-11-25
---

$x\to\infty$ along the real axis unless stated. $f\sim g$ means $f/g\to1$ ([[limits-and-continuity]]). $B_{2n}$ are the Bernoulli numbers, $B_2 = \tfrac16$, $B_4 = -\tfrac1{30}$, $B_6 = \tfrac1{42}$.

## Asymptotic series

**Definition (Poincaré).** $\sum_na_nx^{-n}$ is an asymptotic expansion of $f$, written $f(x)\sim\sum a_nx^{-n}$, if for every fixed $N$

$$
x^N\Big[f(x) - \sum_{n=0}^Na_nx^{-n}\Big]\to0\qquad(x\to\infty).
$$

The truncation error at fixed $N$ vanishes faster than the last term kept (Arfken Sec. 5.10).

**Two different limits.** For a convergent series, adding terms at fixed $x$ improves the result without limit. For an asymptotic series, increasing $x$ at fixed $N$ improves it; at fixed $x$ the terms first shrink and then grow, and the series usually diverges. The two notions are independent: many asymptotic series have zero radius of convergence.

**Optimal truncation.** At fixed $x$, the error is roughly the size of the first omitted term. The best result therefore comes from stopping just before the smallest term. The achievable error is typically exponentially small, of order $e^{-cx}$ for some $c$.

**Uniqueness.** A function has at most one asymptotic expansion in powers of $1/x$. Different functions can share one, since $e^{-x}\sim0$ to all orders. Asymptotic series therefore cannot see exponentially small terms. This is the origin of non-perturbative effects (tunnelling splittings, for example) that no order of perturbation theory reproduces.

## Standard examples

**Stirling's series.** From the Euler–Maclaurin formula (Arfken Sec. 8.3, Eqs. 8.45–8.47):

$$
\ln\Gamma(z + 1)\sim\big(z + \tfrac12\big)\ln z - z + \tfrac12\ln2\pi + \sum_{n=1}^\infty\frac{B_{2n}}{2n(2n - 1)z^{2n-1}},\qquad
n!\sim\sqrt{2\pi n}\Big(\frac ne\Big)^n\Big(1 + \frac1{12n} + \frac1{288n^2} - \cdots\Big).
\label{stirling}
$$

The series in $1/z$ diverges for every $z$, because $B_{2n}$ grows like $(2n)!$. Yet the leading term is already within 8% at $n = 1$. $\ln N!\approx N\ln N - N$ is the version used in statistical mechanics, where $N\sim10^{23}$.

**The complementary error function.** Repeated integration by parts of $\int_x^\infty e^{-t^2}dt$ gives

$$
\mathrm{erfc}\,x\sim\frac{e^{-x^2}}{\sqrt\pi\,x}\Big[1 - \frac1{2x^2} + \frac{1\cdot3}{(2x^2)^2} - \frac{1\cdot3\cdot5}{(2x^2)^3} + \cdots\Big].
$$

The $k$-th term grows like $(2k - 1)!!/(2x^2)^k$, so the series diverges; terms decrease only while $2k - 1 < 2x^2$.

**Laplace's method.** For large $N$ and a function $g(t)$ with a single interior maximum at $t_0$ ($g''(t_0) < 0$),

$$
\int e^{Ng(t)}h(t)\,dt\sim h(t_0)\,e^{Ng(t_0)}\sqrt{\frac{2\pi}{N|g''(t_0)|}} .
$$

The integrand is replaced by a Gaussian at its peak, using the second-order Taylor expansion of $g$. Corrections come in powers of $1/N$. With $\int_0^\infty t^ne^{-t}dt$ written as $\int e^{n\ln t - t}dt$, it gives the leading Stirling formula. Its extension to the complex plane is the method of steepest descents (Arfken Sec. 7.3). Saddle-point approximations in statistical mechanics, semiclassical propagators and the large-$N$ limits of path integrals all rest on it.

**Euler–Maclaurin.** A sum of a smooth function is an integral plus corrections at the ends (Arfken Sec. 5.9):

$$
\sum_{k=0}^nf(k) = \int_0^nf(x)\,dx + \tfrac12[f(0) + f(n)] + \sum_{p\ge1}\frac{B_{2p}}{(2p)!}\big[f^{(2p-1)}(n) - f^{(2p-1)}(0)\big] .
$$

The series is usually asymptotic. It gives the trapezoid rule and its error (the first correction is $\propto h^2$), the high-temperature expansion of rotational partition functions, and Stirling's formula.

## Resummation: Padé approximants

**Definition.** The $[L/M]$ Padé approximant of a power series is the rational function $P_L(x)/Q_M(x)$ whose own Taylor series agrees with the given one through order $L + M$.

**What it does.** A rational function can have poles, so it can mimic the singularity that limits a power series' radius of convergence ([[power-series-and-radius-of-convergence]]). Padé approximants often converge well beyond the radius, and sometimes for divergent asymptotic series. Borel summation is the other standard resummation, for factorially divergent series.

**Perturbation series.** Rayleigh–Schrödinger and Møller–Plesset series can converge, diverge or oscillate, depending on singularities in the complex coupling plane. Padé or quadratic approximants of the $E^{(n)}$ are a standard diagnostic (general knowledge; not in Arfken).

## Worked examples

!!! example "Stirling, erfc, Laplace and Padé in numbers (computed for this note)"
    **Stirling.** Ratio $n!/[\sqrt{2\pi n}(n/e)^n]$ against the first corrections of Eq. [[#stirling]]:

    | $n$ | ratio | $1 + \frac1{12n}$ | $+ \frac1{288n^2}$ |
    |---:|---:|---:|---:|
    | 1 | 1.084438 | 1.083333 | 1.086806 |
    | 5 | 1.016784 | 1.016667 | 1.016806 |
    | 10 | 1.008365 | 1.008333 | 1.008368 |
    | 50 | 1.001668 | 1.001667 | 1.001668 |

    Even at $n = 1$ the leading term is 8% off, and one correction brings it to 0.1%. At $n = 1$, adding the $1/288$ term overshoots slightly: the asymptotic character already shows.

    **erfc at $x = 3$.** The bracketed series, compared with $\sqrt\pi\,x\,e^{x^2}\mathrm{erfc}\,x$: the error is smallest after 8 terms ($8.7\times10^{-5}$) and grows again after that, to $5.7\times10^{-4}$ with 15 terms. With $2x^2 = 18$, terms decrease until $2k - 1\approx18$.

    **Laplace's method.** $\int_0^{2\pi}e^{N\cos t}dt = 2\pi I_0(N)$, with peak $g = \cos t$ at $t = 0$, $g'' = -1$. The method predicts $e^N\sqrt{2\pi/N}$. Ratio to $e^N$: exact 0.803201 against 0.792665 at $N = 10$, and 0.250978 against 0.250663 at $N = 100$. The relative error falls as $1/(8N)$.

    **Padé.** The Taylor series of $\ln(1 + x)$ at $x = 1$, its radius of convergence, gives 0.634524 after 8 terms. The $[4/4]$ Padé approximant built from the same 8 coefficients gives 0.69314642, against $\ln2 = 0.69314718$.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 5.9 (Bernoulli numbers, Euler–Maclaurin formula), Sec. 5.10 (asymptotic series, including the incomplete Gamma function and erfc-type integrals), Sec. 7.3 (method of steepest descents), Sec. 8.3 (Stirling's series, Eqs. 8.45–8.47). Padé approximants and the perturbation-theory remarks are general knowledge, not from Arfken. Calculations in `Claude outputs/part0_math_batchE.py`, section C.
