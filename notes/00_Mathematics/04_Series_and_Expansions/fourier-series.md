---
id: fourier-series
title: Fourier series - expansion of periodic functions in sines and cosines, the complex form, convergence at jumps, the Gibbs phenomenon, Parseval's identity, and the link to the Fourier transform
summary: A periodic function is expanded in the orthogonal set 1, cos nx, sin nx. Its coefficients are found by projection, because the sines and cosines are orthogonal over a period; in complex form f = Σ cₙ e^{inx} with cₙ = (1/2π)∫ f e^{−inx} dx. For piecewise smooth f the series converges to f where f is continuous and to the midpoint of a jump. Near a jump the partial sums overshoot by about 9% of the jump however many terms are taken (Gibbs phenomenon). Parseval's identity equates the mean square of f to the sum of |cₙ|². Smoothness controls how fast the coefficients decay. Letting the period grow turns the series into the Fourier transform. Worked examples: a square wave with its Gibbs overshoot and Parseval sum, and a sawtooth that reproduces Leibniz's series for π/4.
status: in-progress
kind: theory
level: introductory
tags: [fourier-series, periodic-function, orthogonality, fourier-coefficients, gibbs-phenomenon, parseval-identity, dirichlet-conditions, sine-series, cosine-series, square-wave]
prerequisites: [sequences-series-and-convergence, integral-calculus, functions]
related: [fourier-transforms-and-the-dirac-delta, eigenfunction-expansions-and-generating-functions, sturm-liouville-theory, partial-differential-equations-and-separation-of-variables, orthonormal-functions-and-operators]
key: fs
order: 50
date: 2026-11-25
---

Period $2\pi$ on the interval $(-\pi,\pi)$; for period $2L$ replace $nx$ by $n\pi x/L$ and $\frac1\pi\int_{-\pi}^\pi$ by $\frac1L\int_{-L}^L$. Arfken uses $(0, 2\pi)$, which gives the same coefficients for a $2\pi$-periodic $f$.

## The series

**Orthogonality.** Over one period, for integers $m, n\ge0$:

$$
\int_{-\pi}^\pi\cos mx\cos nx\,dx = \pi\delta_{mn}\ (m, n\ge1),\qquad
\int_{-\pi}^\pi\sin mx\sin nx\,dx = \pi\delta_{mn},\qquad
\int_{-\pi}^\pi\sin mx\cos nx\,dx = 0 ,
$$

and $\int\cos^20x = 2\pi$. The functions $1,\cos nx,\sin nx$ are an orthogonal basis of square-integrable functions on the interval: they are the eigenfunctions of $-d^2/dx^2$ with periodic boundary conditions ([[sturm-liouville-theory]]).

**The expansion.** If $f$ has period $2\pi$ (Arfken Eqs. 14.1–14.3),

$$
f(x) = \frac{a_0}2 + \sum_{n=1}^\infty(a_n\cos nx + b_n\sin nx),\qquad
a_n = \frac1\pi\int_{-\pi}^\pi f(x)\cos nx\,dx,\quad b_n = \frac1\pi\int_{-\pi}^\pi f(x)\sin nx\,dx .
\label{fs}
$$

The coefficients follow by multiplying both sides by $\cos mx$ or $\sin mx$ and integrating: orthogonality kills every term but one. This is projection onto a basis, as in [[orthonormal-functions-and-operators]]. The factor $\tfrac12$ on $a_0$ lets the same formula serve $n = 0$.

**Complex form.** With $\cos nx = \frac12(e^{inx} + e^{-inx})$ (Arfken Eq. 14.4):

$$
f(x) = \sum_{n=-\infty}^\infty c_ne^{inx},\qquad c_n = \frac1{2\pi}\int_{-\pi}^\pi f(x)\,e^{-inx}dx,\qquad c_{\pm n} = \tfrac12(a_n\mp ib_n).
$$

For real $f$, $c_{-n} = c_n^*$.

**Even and odd functions.** An even $f$ has $b_n = 0$, a pure cosine series; an odd $f$ has $a_n = 0$, a pure sine series. A function given only on $(0,\pi)$ can be extended either way, which is how boundary conditions are matched: a sine series vanishes at $0$ and $\pi$ ([[partial-differential-equations-and-separation-of-variables]]).

## Convergence

**Dirichlet's theorem.** If $f$ is piecewise smooth (finitely many jumps and extrema in a period), the series converges at every $x$ (Arfken Sec. 14.1):

- to $f(x)$ where $f$ is continuous;
- to $\tfrac12[f(x^+) + f(x^-)]$ at a jump.

**Convergence in the mean.** For any square-integrable $f$, the series converges in the mean: $\int|f - S_N|^2\to0$. This is completeness of the basis, and it is all that quantum mechanics needs.

**Coefficient decay and smoothness.** Integrating by parts in Eq. [[#fs]] shows that the coefficients decay faster the smoother the periodic function is:

| $f$ (periodic) | coefficients |
|---|---|
| has jumps | $\sim1/n$ |
| continuous, $f'$ has jumps | $\sim1/n^2$ |
| $k$ continuous derivatives | $o(n^{-k})$ |
| analytic | exponentially |

This is the reason plane-wave codes converge quickly for smooth pseudopotentials and slowly near nuclear cusps.

**Term-by-term operations.** The series can always be integrated term by term. It can be differentiated term by term only if the result still converges. The sawtooth below cannot be: the differentiated series $2\sum(-1)^{n+1}\cos nx$ diverges.

## The Gibbs phenomenon

**The overshoot.** Near a jump the partial sums $S_N$ overshoot (Arfken Sec. 14.5). As $N\to\infty$ the overshoot moves toward the jump but does not shrink. For a jump of height $J$ its limit is

$$
\frac{J}{2}\Big[\frac2\pi\mathrm{Si}(\pi) - 1\Big] = 0.0895\,J,\qquad \mathrm{Si}(\pi) = \int_0^\pi\frac{\sin t}tdt = 1.8519 .
$$

The convergence is pointwise but not uniform ([[sequences-series-and-convergence]]). Truncating any expansion of a discontinuous function produces the same ringing, including a truncated basis expansion of a cusp. Smoothing the coefficients ($\sigma$-factors) suppresses it.

## Parseval's identity

**Statement.** For square-integrable $f$:

$$
\frac1{2\pi}\int_{-\pi}^\pi|f(x)|^2dx = \sum_{n=-\infty}^\infty|c_n|^2 = \frac{a_0^2}4 + \frac12\sum_{n\ge1}(a_n^2 + b_n^2).
\label{parseval}
$$

This is the Pythagorean theorem in an orthonormal basis (Arfken Sec. 14.4, Exercise 14.4.2, a special case of the completeness relation). Applied to simple functions it sums series: the square wave below gives $\sum_{\rm odd}n^{-2} = \pi^2/8$, and from there $\zeta(2) = \pi^2/6$.

## From series to transform

**The limit $L\to\infty$.** For period $2L$ the frequencies are $k_n = n\pi/L$, spaced by $\Delta k = \pi/L$. As $L\to\infty$ the spacing goes to zero and $\sum_n c_ne^{ik_nx}$ becomes an integral over $k$. The coefficients become the Fourier transform $F(k)$, and Parseval becomes Plancherel ([[fourier-transforms-and-the-dirac-delta]]). A box with periodic boundary conditions, whose plane waves are a Fourier series, is the standard way to discretize this.

## Worked examples

!!! example "Square wave, Gibbs and Parseval; sawtooth and π/4 (computed for this note)"
    **Square wave.** $f = -1$ on $(-\pi, 0)$ and $+1$ on $(0, \pi)$. It is odd, and Eq. [[#fs]] gives $b_n = 4/(n\pi)$ for odd $n$ and 0 for even $n$: $f = \frac4\pi\big(\sin x + \frac13\sin3x + \frac15\sin5x + \cdots\big)$. At $x = 0$ the series gives 0, the midpoint of the jump.

    - **Gibbs.** The maximum of the partial sum, for jump $J = 2$:

      | highest harmonic $N$ | max $S_N$ | overshoot / $J$ |
      |---:|---:|---:|
      | 11 | 1.18130 | 9.065% |
      | 101 | 1.17901 | 8.951% |
      | 1001 | 1.17898 | 8.949% |

      The limit is $\frac2\pi\mathrm{Si}(\pi) = 1.178980$.
    - **Parseval.** $\frac1{2\pi}\int f^2 = 1$ and $\frac12\sum b_n^2 = \frac8{\pi^2}\sum_{\rm odd}n^{-2}$, so $\sum_{\rm odd}n^{-2} = \pi^2/8 = 1.233701$. The sum to $n = 2\times10^5$ is 1.233698.

    **Sawtooth.** $f = x$ on $(-\pi,\pi)$: $b_n = 2(-1)^{n+1}/n$, i.e. $2, -1, 0.6667, -0.5$ for $n = 1..4$. At $x = \pi/2$, $\sin(n\pi/2)$ picks out the odd $n$ with alternating signs, so $\pi/2 = 2(1 - \tfrac13 + \tfrac15 - \cdots)$. That is Leibniz's series $\pi/4$; the partial sum to $2\times10^5$ terms gives 0.785396.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 14.1 (general properties, Eqs. 14.1–14.4, Dirichlet conditions, convergence in the mean), Secs. 14.2–14.3 (uses and applications: square wave, sawtooth), Sec. 14.4 (properties, Parseval's identity, Exercise 14.4.2), Sec. 14.5 (Gibbs phenomenon). The remark on plane-wave codes is general knowledge. Calculations in `Claude outputs/part0_math_batchE.py`, section C.
