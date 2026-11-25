---
id: power-series-and-radius-of-convergence
title: Power series - radius of convergence, behaviour at the endpoints, term-by-term differentiation and integration, uniqueness, algebra of power series, and why the radius is set by complex singularities
summary: A power series Σ aₙ(x − x₀)ⁿ converges absolutely inside a symmetric interval |x − x₀| < R and diverges outside. The radius R follows from the ratio or root test, 1/R = lim |aₙ|^{1/n}; the endpoints must be checked separately. Inside, the series converges uniformly on every smaller interval, so it can be differentiated and integrated term by term, and the expansion of a function is unique. Power series can be added, multiplied, divided and inverted like polynomials. The radius equals the distance from x₀ to the nearest singularity in the complex plane: 1/(1 + x²) is smooth on the whole real line, yet its Maclaurin series stops converging at |x| = 1 because of the poles at ±i. Worked examples: radii of four series, slow convergence near the edge, and arctan by term-by-term integration.
status: in-progress
kind: theory
level: introductory
tags: [power-series, radius-of-convergence, cauchy-hadamard, analytic-function, term-by-term-differentiation, uniqueness, series-inversion, complex-singularity]
prerequisites: [sequences-series-and-convergence]
related: [taylor-and-maclaurin-expansions, analytic-functions-and-cauchy-theorem, laurent-series-singularities-and-residues, series-solutions-and-the-frobenius-method]
key: radius
order: 20
date: 2026-11-25
---

$x_0$ is the expansion point; the series is written $\sum_{n\ge0}a_n(x - x_0)^n$. Everything holds unchanged for a complex variable $z$, where the interval becomes a disc.

## The radius of convergence

**Statement.** For every power series there is an $R\in[0,\infty]$ such that the series converges absolutely for $|x - x_0| < R$ and diverges for $|x - x_0| > R$ (Arfken Sec. 5.7). From the root test (Cauchy–Hadamard) and, when the limit exists, the ratio test:

$$
\frac1R = \limsup_{n\to\infty}|a_n|^{1/n} = \lim_{n\to\infty}\Big|\frac{a_{n+1}}{a_n}\Big| .
\label{radius}
$$

**Endpoints.** At $|x - x_0| = R$ the tests give no conclusion, and anything can happen:

- $\sum x^n$ diverges at both $x = \pm1$;
- $\ln(1 + x) = \sum(-1)^{n+1}x^n/n$ converges at $x = 1$ (to $\ln2$) and diverges at $x = -1$;
- $\sum x^n/n^2$ converges at both.

**Examples.**

| series | $a_n$ | $R$ |
|---|---|---|
| $e^x = \sum x^n/n!$ | $1/n!$ | $\infty$ |
| $(1 - x)^{-1} = \sum x^n$ | 1 | 1 |
| $\ln(1 + x)$ | $(-1)^{n+1}/n$ | 1 |
| $\sum n!\,x^n$ | $n!$ | 0 (converges only at $x = 0$) |
| Hermite series with $\nu\notin\mathbb N$ | $a_{k+2}/a_k\to2/k$ | $\infty$, but grows like $e^{x^2}$ |

## Working with power series

**Uniform convergence inside.** On any closed interval $|x - x_0|\le r < R$ the series converges uniformly, by the M-test with $M_n = |a_n|r^n$ ([[sequences-series-and-convergence]]). Hence the sum is continuous there and (Arfken Sec. 5.7):

- **Term-by-term differentiation.** $f'(x) = \sum na_n(x - x_0)^{n-1}$, with the same radius $R$;
- **Term-by-term integration.** $\int_{x_0}^xf = \sum a_n(x - x_0)^{n+1}/(n + 1)$, also with radius $R$.

Repeated differentiation gives $a_n = f^{(n)}(x_0)/n!$. So a convergent power series is the Taylor series of its sum ([[taylor-and-maclaurin-expansions]]).

**Uniqueness.** If $\sum a_n(x - x_0)^n = \sum b_n(x - x_0)^n$ on some interval around $x_0$, then $a_n = b_n$ for all $n$. This justifies equating coefficients, which is how the Frobenius method solves differential equations ([[series-solutions-and-the-frobenius-method]]) and how generating functions define polynomials.

**Algebra.**

- **Sum and product.** Two series add and multiply (Cauchy product $c_n = \sum_ka_kb_{n-k}$) within the smaller radius.
- **Division.** $1/f$ is found by solving $f\cdot g = 1$ order by order, provided $f(x_0)\ne0$.
- **Inversion (reversion).** If $y = \sum_{n\ge1}a_nx^n$ with $a_1\ne0$, the inverse $x = \sum b_ny^n$ starts $b_1 = 1/a_1$, $b_2 = -a_2/a_1^3$ (Arfken Sec. 5.7).

## Analytic functions and complex singularities

**Analyticity.** A function equal to a convergent power series in a neighbourhood of each point of an interval is **real analytic** there. Every analytic function is infinitely differentiable. The converse fails: $e^{-1/x^2}$ (set to 0 at 0) has all derivatives zero at the origin, so its Maclaurin series is identically 0 while the function is not.

**What sets $R$.** Extend $x$ to a complex $z$. A power series converges in a disc. The disc cannot contain a singularity of the function, and it extends to the nearest one ([[laurent-series-singularities-and-residues]]):

$$
R = \text{distance from }x_0\text{ to the nearest singularity of }f\text{ in the complex plane.}
$$

This explains radii that look strange on the real line:

- **$1/(1 + x^2)$** is smooth for all real $x$, but has poles at $z = \pm i$, so $R = 1$ about $x_0 = 0$. About $x_0 = 1$ it is $\sqrt2$.
- **$\arctan x$** has $R = 1$ for the same reason.
- **Perturbation series.** The radius of convergence of a perturbation series in a coupling $\lambda$ is set by singularities in the complex $\lambda$ plane. For Møller–Plesset series these can lie at small $|\lambda|$, even at negative real $\lambda$ from intruder states.

## Worked examples

!!! example "Radii, the edge of the disc, and arctan (computed for this note)"
    **Radius from the coefficients.** $|a_n|^{-1/n}$ at $n\approx40$ (sympy series):

    | series | estimate | exact $R$ |
    |---|---:|---:|
    | $\ln(1 + x)$ | 1.0966 | 1 |
    | $1/(1 + x^2)$ | 1.0000 | 1 |
    | $\arctan x$ | 1.0985 | 1 |
    | $e^x$ | 15.77 | $\infty$ |

    The root estimate converges slowly when $|a_n| = 1/n$, because $n^{1/n}\to1$ only logarithmically. The ratio form of Eq. [[#radius]] gives exactly 1 at once. For $e^x$ the estimate grows without bound.

    **Near the edge.** At $x = 0.9$ the partial sums of $\sum(-1)^kx^{2k}$ for $1/(1 + x^2) = 0.552486$ are 0.745126 (5 terms), 0.544320 (20 terms) and 0.552486 (80 terms). The terms shrink only as $0.81^k$. At $x = 1.1$ they grow as $1.21^k$.

    **arctan by integration.** Integrating $1/(1 + t^2) = \sum(-1)^kt^{2k}$ from 0 to $x$ term by term gives $\arctan x = x - x^3/3 + x^5/5 - \cdots$ (sympy agrees). At $x = 1$, the endpoint, the series still converges (alternating), giving Leibniz's $\pi/4$.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 5.7 (power series: convergence, uniform and absolute convergence, continuity, differentiation and integration, uniqueness, inversion). The link between $R$ and complex singularities is Arfken Sec. 6.5 (Laurent expansion). The Møller–Plesset remark is general knowledge. Calculations in `Claude outputs/part0_math_batchE.py`, section C.
