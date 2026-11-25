---
id: taylor-and-maclaurin-expansions
title: Taylor and Maclaurin expansions - Taylor's theorem with remainder, the standard series, the binomial series, the translation operator, and expansions about a minimum
summary: Taylor's theorem writes a smooth function as a polynomial in (x − a) plus a remainder R_n = f^{(n)}(ξ)(x − a)ⁿ/n!. The remainder both decides whether the infinite series converges to f and bounds the error of truncating it. Expanding about a = 0 gives the Maclaurin series of eˣ, sin, cos, ln(1 + x), arctan and the binomial series (1 + x)^α with generalized binomial coefficients, valid for |x| < 1 for any real α. Formally, the whole Taylor series is the translation operator e^{h d/dx}. Expanding a potential about its minimum gives the harmonic approximation with anharmonic corrections. Worked examples: the Lagrange bound for e, relativistic kinetic energy, the large-amplitude pendulum, and a Morse potential expanded at r_e.
status: in-progress
kind: theory
level: introductory
tags: [taylor-series, maclaurin-series, taylor-remainder, lagrange-remainder, binomial-series, binomial-coefficient, translation-operator, harmonic-approximation, anharmonicity, small-angle-approximation]
prerequisites: [power-series-and-radius-of-convergence, differential-calculus]
related: [multivariable-taylor-expansion, asymptotic-expansions, baker-campbell-hausdorff, unitary-matrices-exponential-logarithm, harmonic-oscillator-ladder-operators]
key: taylor
order: 30
date: 2026-11-25
---

Real functions with as many continuous derivatives as each statement needs. $f^{(n)}$ is the $n$-th derivative, $f^{(0)} = f$.

## Taylor's theorem

**Statement.** If $f$ has $n$ continuous derivatives on an interval containing $a$ and $x$ (Arfken Eqs. 5.82–5.85),

$$
f(x) = \sum_{k=0}^{n-1}\frac{f^{(k)}(a)}{k!}(x - a)^k + R_n,\qquad R_n = \frac{f^{(n)}(\xi)}{n!}(x - a)^n
\label{taylor}
$$

for some $\xi$ between $a$ and $x$.

**Proof idea.** Arfken obtains Eq. [[#taylor]] by integrating $f^{(n)}$ $n$ times from $a$ to $x$. That gives the remainder as an $n$-fold integral. The mean value theorem of integral calculus turns it into the Lagrange form.

**Integral form.** Equivalently, $R_n = \frac1{(n - 1)!}\int_a^x(x - t)^{n-1}f^{(n)}(t)\,dt$. This form is useful when $f^{(n)}$ is easier to integrate than to bound.

**From the theorem to the series.** If $R_n\to0$ as $n\to\infty$, the Taylor series converges to $f$:

$$
f(x) = \sum_{n=0}^\infty\frac{f^{(n)}(a)}{n!}(x - a)^n .
$$

For $a = 0$ this is the **Maclaurin series** (Arfken Eq. 5.88). A function can have a convergent Taylor series that converges to something else ($e^{-1/x^2}$ at 0, [[power-series-and-radius-of-convergence]]). Checking $R_n\to0$, or analyticity, is what rules this out.

**What the remainder is for.** For a truncated expansion, $|R_n|\le\max|f^{(n)}|\,|x - a|^n/n!$ is a rigorous error bound. It also shows that the error of an $n$-term expansion is $O((x - a)^n)$ as $x\to a$, which is how "first-order" and "second-order" approximations are compared.

## The standard Maclaurin series

| function | series | valid for |
|---|---|---|
| $e^x$ | $\sum x^n/n! = 1 + x + x^2/2 + x^3/6 + \cdots$ | all $x$ |
| $\sin x$ | $x - x^3/3! + x^5/5! - \cdots$ | all $x$ |
| $\cos x$ | $1 - x^2/2! + x^4/4! - \cdots$ | all $x$ |
| $\sinh x$, $\cosh x$ | as $\sin$, $\cos$ with all signs $+$ | all $x$ |
| $\ln(1 + x)$ | $x - x^2/2 + x^3/3 - \cdots$ | $-1 < x\le1$ |
| $\arctan x$ | $x - x^3/3 + x^5/5 - \cdots$ | $|x|\le1$ |
| $\tan x$ | $x + x^3/3 + 2x^5/15 + \cdots$ | $|x| < \pi/2$ |
| $(1 + x)^\alpha$ | $\sum\binom\alpha nx^n$ | $|x| < 1$ |

Arfken derives $e^x$ and $\ln(1 + x)$ with their remainders in Eqs. 5.90–5.96. For $e^x$, $|R_n|\le|x|^ne^{|x|}/n!\to0$ for every $x$.

**The binomial series.** For any real (or complex) $\alpha$ (Arfken Sec. 5.6),

$$
(1 + x)^\alpha = \sum_{n=0}^\infty\binom\alpha nx^n,\qquad \binom\alpha n = \frac{\alpha(\alpha - 1)\cdots(\alpha - n + 1)}{n!},\qquad |x| < 1 .
\label{binom}
$$

For a nonnegative integer $\alpha$ it terminates, giving the binomial theorem. Otherwise it is infinite. The cases used most:

- $\sqrt{1 + x} = 1 + \frac x2 - \frac{x^2}8 + \frac{x^3}{16} - \cdots$
- $\frac1{\sqrt{1 - x}} = 1 + \frac x2 + \frac{3x^2}8 + \frac{5x^3}{16} + \cdots$
- $(1 + x)^{-1} = 1 - x + x^2 - \cdots$, the geometric series.

The second, with $x = 2\mu t - t^2$, generates the Legendre polynomials ([[eigenfunction-expansions-and-generating-functions]]).

## The translation operator

**Formal statement.** Summing the Taylor series formally,

$$
f(x + h) = \sum_n\frac{h^n}{n!}\frac{d^nf}{dx^n} = e^{h\,d/dx}f(x).
$$

The exponential of the derivative shifts the argument. In quantum mechanics $\hat p = -i\hbar\,d/dx$, so $e^{-ih\hat p/\hbar}$ is the translation operator: momentum generates translations. Exponentials of operators and their products are the subject of [[baker-campbell-hausdorff]].

## Expanding about a minimum

**The harmonic approximation.** At a minimum $x_e$ of a potential, $V'(x_e) = 0$, so

$$
V(x_e + q) = V(x_e) + \tfrac12kq^2 + \tfrac16V'''q^3 + \tfrac1{24}V''''q^4 + \cdots,\qquad k = V''(x_e).
$$

Keeping the quadratic term gives the harmonic oscillator ([[harmonic-oscillator-ladder-operators]]). The cubic and quartic terms are the anharmonicity, which shifts and splits vibrational levels. In many dimensions the expansion is in the Hessian ([[multivariable-taylor-expansion]]).

**Small-quantity approximations.** These are all first-order Taylor expansions:

- $\sin\theta\approx\theta$ (pendulum, small-angle scattering);
- $\sqrt{1 + x}\approx1 + x/2$ (relativistic corrections, separations of nearly equal distances);
- $e^{-x}\approx1 - x$ (low-temperature Boltzmann factors, short times).

## Worked examples

!!! example "Remainder bound, relativity, the pendulum and a Morse well (computed for this note)"
    **The Lagrange bound for $e$.** Summing $1/k!$ for $k = 0..N$ approximates $e$ with $|R|\le e/(N + 1)!$:

    | $N$ | error | bound |
    |---:|---:|---:|
    | 5 | $1.615\times10^{-3}$ | $3.775\times10^{-3}$ |
    | 10 | $2.731\times10^{-8}$ | $6.810\times10^{-8}$ |
    | 12 | $1.729\times10^{-10}$ | $4.365\times10^{-10}$ |

    **Relativistic kinetic energy.** Expanding $mc^2[(1 - v^2/c^2)^{-1/2} - 1]$ with Eq. [[#binom]] ($\alpha = -\tfrac12$, $x = -v^2/c^2$) gives $\tfrac12mv^2 + \tfrac38mv^4/c^2 + \tfrac5{16}mv^6/c^4 + \cdots$. The $v^4$ term is the mass-velocity correction of relativistic quantum chemistry.

    **The pendulum.** The exact period is $T/T_0 = \frac2\pi K(\sin^2\frac{\theta_0}2)$, with $K$ the complete elliptic integral. Its series is $1 + \theta_0^2/16 + 11\theta_0^4/3072 + \cdots$. At $\theta_0 = 30°$ the exact value is 1.017409 and the two-term value 1.017135.

    **Morse potential at $r_e$.** $V = D_e(1 - e^{-a(r - r_e)})^2$ with $D_e = 0.1745$, $a = 1.0282$, $r_e = 1.4011$ (atomic units, H₂-like illustrative values).

    - **Coefficients.** $V''(r_e) = 2D_ea^2 = 0.36896$ and $V'''/6 = -D_ea^3 = -0.18968$.
    - **Accuracy.** At $\Delta r = 0.1$: exact 0.001666, harmonic 0.001845, through fourth order 0.001666. At $\Delta r = 0.3$: exact 0.012293, harmonic 0.016603, fourth order 0.012403.
    - **Reading.** The negative cubic term softens the well on the stretching side. The harmonic error grows as $\Delta r^3$.

    **Translation operator.** $\sum_{k<20}\frac{(1.2)^k}{k!}\frac{d^k}{dx^k}\sin x$ at $x = 0.3$ gives 0.9974949866, equal to $\sin1.5$ to all printed digits.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 5.6 (Taylor's expansion: Eqs. 5.79–5.88 for the theorem and remainder, Eqs. 5.89–5.96 for $e^x$ and $\ln(1 + x)$, the binomial theorem), Exercise 4.2.4 (operator form, referred to in Sec. 5.6). The Morse parameters are illustrative, not fitted. Calculations in `Claude outputs/part0_math_batchE.py`, section C.
