---
id: sequences-series-and-convergence
title: Infinite series and convergence - partial sums, the geometric and p-series, comparison, ratio, root and integral tests, alternating series, absolute and conditional convergence, and uniform convergence of series of functions
summary: An infinite series converges when its partial sums tend to a limit. Terms tending to zero are necessary but not sufficient, as the harmonic series shows. The standard tests compare a series with the geometric series (ratio and root tests) or with an integral (integral test, p-series). An alternating series with decreasing terms converges, and its error is smaller than the first term omitted. Absolutely convergent series can be rearranged freely; conditionally convergent ones cannot, and Riemann showed they can be rearranged to any sum. For series of functions, uniform convergence is what allows term-by-term integration and differentiation. Worked examples: harmonic growth ln N + γ, ζ(2) = π²/6, the alternating harmonic series and a rearrangement that halves its sum.
status: in-progress
kind: theory
level: introductory
tags: [infinite-series, convergence, partial-sums, geometric-series, harmonic-series, ratio-test, root-test, integral-test, alternating-series, absolute-convergence, conditional-convergence, uniform-convergence, riemann-rearrangement]
prerequisites: [limits-and-continuity, integral-calculus]
related: [power-series-and-radius-of-convergence, taylor-and-maclaurin-expansions, asymptotic-expansions, fourier-series]
key: geom
order: 10
date: 2026-11-25
---

$\sum a_n$ means $\sum_{n=1}^\infty a_n$ unless limits are written. $s_N = \sum_{n=1}^Na_n$ is the $N$-th partial sum.

## Convergence

**Definition.** The series $\sum a_n$ **converges** to $S$ if the partial sums converge, $s_N\to S$ ([[limits-and-continuity]]). Otherwise it diverges, either to infinity or by oscillation, like $1 - 1 + 1 - \cdots$ (Arfken Sec. 5.1).

**Necessary condition.** If $\sum a_n$ converges, then $a_n = s_n - s_{n-1}\to0$. The converse is false.

**The geometric series.** For $|r| < 1$,

$$
\sum_{n=0}^\infty r^n = \frac1{1 - r},\qquad s_N = \frac{1 - r^{N+1}}{1 - r},
\label{geom}
$$

and it diverges for $|r|\ge1$. This is the reference series for the ratio and root tests, and the model for every expansion of $(1 - A)^{-1}$ ([[neumann-series-and-operator-expansions]]).

**The harmonic series diverges.** Group the terms: $1 + \tfrac12 + (\tfrac13 + \tfrac14) + (\tfrac15 + \cdots + \tfrac18) + \cdots$, each group $\ge\tfrac12$. More precisely $s_N = \ln N + \gamma + O(1/N)$, with Euler's constant $\gamma = 0.5772\ldots$ The terms go to zero, but too slowly.

## Tests for series of positive terms

Arfken Sec. 5.2 gives these:

- **Comparison.** If $0\le a_n\le b_n$ and $\sum b_n$ converges, so does $\sum a_n$. If $a_n\ge b_n\ge0$ and $\sum b_n$ diverges, so does $\sum a_n$. Limit form: if $a_n/b_n\to c$ with $0 < c < \infty$, both converge or both diverge.
- **Ratio test (d'Alembert).** If $a_{n+1}/a_n\to\rho$: convergence for $\rho < 1$, divergence for $\rho > 1$, no conclusion for $\rho = 1$.
- **Root test (Cauchy).** Same conclusions with $\rho = \lim a_n^{1/n}$. It is at least as strong as the ratio test.
- **Integral test (Maclaurin).** If $a_n = f(n)$ with $f$ positive and decreasing, $\sum a_n$ and $\int_1^\infty f(x)\,dx$ converge or diverge together. Moreover $\int_{N+1}^\infty f\le S - s_N\le\int_N^\infty f$, a bound on the truncation error.
- **The $p$-series.** By the integral test, $\zeta(p) = \sum n^{-p}$ converges for $p > 1$ and diverges for $p\le1$. With the comparison test, this settles most series that arise in practice.
- **Kummer and Gauss tests.** Sharper tests for the case $\rho = 1$. Gauss's test decides hypergeometric-type series, such as the Legendre series at $x = \pm1$ (Arfken Sec. 5.2, Exercise 5.2.15).

## Alternating series

**Leibniz criterion.** If $a_n > 0$ decreases monotonically to 0, then $\sum(-1)^{n+1}a_n$ converges (Arfken Sec. 5.3). The partial sums bracket the limit alternately, so

$$
|S - s_N|\le a_{N+1} .
$$

The alternating harmonic series $1 - \tfrac12 + \tfrac13 - \cdots = \ln2$ converges, although the series of absolute values does not.

## Absolute and conditional convergence

**Definitions.** $\sum a_n$ converges **absolutely** if $\sum|a_n|$ converges. Absolute convergence implies convergence. A series that converges but not absolutely converges **conditionally**.

**Rearrangement.** An absolutely convergent series can be reordered, grouped and multiplied term by term (the Cauchy product) without changing its sum. A conditionally convergent series cannot. Riemann's theorem (Arfken Sec. 5.4): it can be rearranged to converge to any value, or to diverge. Positive and negative parts each diverge, and the order decides how they cancel.

**Practical consequence.** Lattice sums of Coulomb interactions in a crystal are conditionally convergent. Their value depends on the summation order (the shape of the summed region), which is why Ewald summation exists.

## Series of functions

**Pointwise and uniform convergence.** $\sum u_n(x)$ converges **uniformly** on an interval if the tail can be made small for all $x$ at once:

$$
\sup_x\Big|S(x) - \sum_{n\le N}u_n(x)\Big|\to0 .
$$

Pointwise convergence lets $N$ depend on $x$.

**What uniform convergence buys** (Arfken Sec. 5.5):

- the sum of continuous functions is continuous;
- the series may be integrated term by term;
- it may be differentiated term by term if the differentiated series also converges uniformly.

**Weierstrass M-test.** If $|u_n(x)|\le M_n$ for all $x$ and $\sum M_n$ converges, the series converges uniformly and absolutely.

**A counterexample.** The Fourier series of a square wave converges at every point but not uniformly near the jump, which is the Gibbs phenomenon ([[fourier-series]]).

## Worked example

!!! example "Harmonic, ζ(2), alternating and rearranged sums (computed for this note)"
    | $N$ | $s_N$ (harmonic) | $\ln N + \gamma$ | $\sum_1^Nn^{-2}$ | alternating harmonic |
    |---:|---:|---:|---:|---:|
    | 10 | 2.928968 | 2.879801 | 1.54976773 | 0.64563492 |
    | 1000 | 7.485471 | 7.484971 | 1.64393457 | 0.69264743 |
    | $10^6$ | 14.392727 | 14.392726 | 1.64493307 | 0.69314668 |

    - **Limits.** $\pi^2/6 = 1.64493407$ and $\ln2 = 0.69314718$. The difference $s_N - \ln N - \gamma\approx1/(2N)$.
    - **Integral-test bound.** The $p = 2$ tail after $N$ terms lies between $1/(N + 1)$ and $1/N$. At $N = 1000$ the actual tail is $1.0\times10^{-3}$.
    - **Leibniz bound.** After 100 terms of the alternating harmonic series, $|s_{100} - \ln2| = 4.98\times10^{-3}\le1/101 = 9.90\times10^{-3}$.
    - **Ratio test.** For $a_n = n!/n^n$, $a_{n+1}/a_n = (1 + 1/n)^{-n}\to1/e < 1$, so the series converges.

    **Rearrangement.** Taking one positive term then two negative ones, $1 - \tfrac12 - \tfrac14 + \tfrac13 - \tfrac16 - \tfrac18 + \cdots$, over $2\times10^5$ groups gives 0.346573. That is $\tfrac12\ln2 = 0.346574$, half the original sum, from the same terms.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 5.1 (fundamental concepts, geometric and harmonic series), Sec. 5.2 (convergence tests), Sec. 5.3 (alternating series), Sec. 5.4 (algebra of series, Riemann's theorem), Sec. 5.5 (series of functions, uniform convergence, Weierstrass M-test). The Ewald remark is general knowledge. Calculations in `Claude outputs/part0_math_batchE.py`, section C.
