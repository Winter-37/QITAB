---
id: limits-and-continuity
title: Limits and continuity - the epsilon-delta definition, limits of sequences, one-sided and infinite limits, standard limits, continuity, and order notation
summary: The limit lim_{x→a} f(x) = L means f(x) can be made as close to L as wanted by taking x close enough to a (but not equal to it). The ε–δ definition makes this precise and is the basis for derivatives, integrals and series. This note covers limits of sequences, one-sided and infinite limits, the algebra of limits and the squeeze theorem, the standard limits sin x/x → 1 and (1 + 1/n)ⁿ → e, continuity with the intermediate- and extreme-value theorems, and the O and o notation used for error estimates. Worked example: an explicit δ for x² at 3, and the convergence rate of (1 + 1/n)ⁿ.
status: in-progress
kind: theory
level: introductory
tags: [limit, epsilon-delta, continuity, sequence, squeeze-theorem, intermediate-value-theorem, big-o-notation, euler-number]
prerequisites: [functions]
related: [differential-calculus, sequences-series-and-convergence, asymptotic-expansions]
key: limit
order: 20
date: 2026-11-25
---

Real-valued functions of a real variable. The same definitions hold for complex functions with $|\cdot|$ the modulus ([[analytic-functions-and-cauchy-theorem]]) and for vectors with $|\cdot|$ the length.

## Limits of sequences

**Definition.** A sequence $a_1, a_2,\dots$ **converges** to $L$, written $a_n\to L$, if for every $\varepsilon > 0$ there is an $N$ such that $|a_n - L| < \varepsilon$ for all $n > N$. The limit, if it exists, is unique. A sequence that does not converge **diverges**: to $\pm\infty$ (for every $M$, eventually $a_n > M$), or by oscillating, like $(-1)^n$.

**Two useful criteria.**

- **Monotone convergence.** A bounded monotonic sequence converges.
- **Cauchy criterion.** $a_n$ converges if and only if for every $\varepsilon > 0$ there is an $N$ with $|a_n - a_m| < \varepsilon$ for all $n, m > N$. This tests convergence without knowing the limit, which is how series are tested ([[sequences-series-and-convergence]]).

**The number $e$.** $a_n = (1 + 1/n)^n$ is increasing and bounded by 3, so it converges; its limit defines $e = 2.718281828\ldots$ The approach is slow: $e - a_n\approx e/(2n)$.

## Limits of functions

**Definition.** $\lim_{x\to a}f(x) = L$ if for every $\varepsilon > 0$ there is a $\delta > 0$ such that

$$
0 < |x - a| < \delta\ \Rightarrow\ |f(x) - L| < \varepsilon .
\label{limit}
$$

The condition $0 < |x - a|$ means the value $f(a)$, or whether $f$ is even defined at $a$, plays no role. Equivalently, $f(x_n)\to L$ for every sequence $x_n\to a$ with $x_n\ne a$. If two sequences give different limits, the limit does not exist: $\sin(1/x)$ at 0.

**Variants.**

- **One-sided limits** $\lim_{x\to a^\pm}$ restrict to $x > a$ or $x < a$. The two-sided limit exists if and only if both one-sided limits exist and agree. For the step function $\theta(x)$ at 0 they are 1 and 0.
- **Limits at infinity**, $\lim_{x\to\infty}f(x) = L$: for every $\varepsilon$ there is an $M$ with $|f(x) - L| < \varepsilon$ for $x > M$.
- **Infinite limits**, $\lim_{x\to a}f(x) = \infty$: $f$ exceeds every bound near $a$. Example: $1/x^2$ at 0. These signal vertical asymptotes.

**Algebra of limits.** If $f\to L$ and $g\to M$, then $f\pm g\to L\pm M$, $fg\to LM$, and $f/g\to L/M$ if $M\ne0$. These rules fail for the **indeterminate forms** $0/0$, $\infty/\infty$, $0\cdot\infty$, $\infty - \infty$, $1^\infty$, $0^0$, $\infty^0$, which need more work: algebra, Taylor expansion ([[taylor-and-maclaurin-expansions]]) or L'Hôpital's rule ([[differential-calculus]]).

**Squeeze theorem.** If $g(x)\le f(x)\le h(x)$ near $a$ and $g, h\to L$, then $f\to L$. Applied to $\cos x\le\frac{\sin x}{x}\le1$ (from comparing areas in the unit circle) it gives the standard limit

$$
\lim_{x\to0}\frac{\sin x}{x} = 1,
$$

which is the limit behind $\frac{d}{dx}\sin x = \cos x$.

**Standard limits.** $\lim_{x\to0}\frac{1 - \cos x}{x^2} = \tfrac12$; $\lim_{x\to0}\frac{e^x - 1}{x} = 1$; $\lim_{x\to0}\frac{\ln(1 + x)}{x} = 1$; $\lim_{x\to0^+}x\ln x = 0$; $\lim_{x\to\infty}x^ne^{-x} = 0$ for every $n$. The last two say that exponentials beat powers and powers beat logarithms, which is why $r^ne^{-\zeta r}$ basis functions are integrable and normalizable.

## Continuity

**Definition.** $f$ is **continuous at $a$** if $f(a)$ is defined and $\lim_{x\to a}f(x) = f(a)$. It is continuous on an interval if it is continuous at every point.

**Types of discontinuity.**

- **Removable**: the limit exists but differs from $f(a)$, or $f(a)$ is undefined. $\sin x/x$ at 0 becomes continuous by setting the value 1.
- **Jump**: the one-sided limits differ, as for the step function.
- **Infinite or essential**: $1/x$ or $\sin(1/x)$ at 0.

Sums, products, quotients (where the denominator is nonzero) and compositions of continuous functions are continuous. So are all elementary functions on their domains.

**Two theorems for continuous $f$ on a closed interval $[a, b]$.**

- **Intermediate value theorem.** $f$ takes every value between $f(a)$ and $f(b)$. In particular, if $f(a)$ and $f(b)$ have opposite signs, $f$ has a root in $(a, b)$. This is the guarantee behind bisection.
- **Extreme value theorem.** $f$ attains a maximum and a minimum on $[a, b]$. On an open interval this can fail: $1/x$ on $(0, 1)$ is unbounded.

## Order notation

**Definitions.** As $x\to a$:

- $f = O(g)$ if $|f/g|$ stays bounded;
- $f = o(g)$ if $f/g\to0$;
- $f\sim g$ if $f/g\to1$.

So $\sin x = x + O(x^3)$ as $x\to0$, $n! \sim\sqrt{2\pi n}\,(n/e)^n$ as $n\to\infty$ ([[asymptotic-expansions]]), and a central-difference derivative has error $O(h^2)$. In complexity statements ("CCSD scales as $O(N^6)$") the variable tends to infinity and $O$ gives the growth rate.

## Worked example

!!! example "An explicit δ, and how fast (1 + 1/n)ⁿ converges (computed for this note)"
    **ε–δ for $x^2$ at 3.** $|x^2 - 9| = |x - 3|\,|x + 3|$. If $|x - 3| < 1$ then $|x + 3| < 7$, so $|x^2 - 9| < 7|x - 3|$. Hence $\delta = \min(1, \varepsilon/7)$ works in Eq. [[#limit]]. For $\varepsilon = 10^{-3}$, $\delta = 1.43\times10^{-4}$, and on a fine grid of $|x - 3|\le\delta$ the largest $|x^2 - 9|$ is $8.57\times10^{-4} < \varepsilon$.

    **Convergence of $(1 + 1/n)^n$.**

    | $n$ | $(1 + 1/n)^n$ | $e - a_n$ | $e/(2n)$ |
    |---:|---:|---:|---:|
    | 10 | 2.5937424601 | $1.245\times10^{-1}$ | $1.359\times10^{-1}$ |
    | 1000 | 2.7169239322 | $1.358\times10^{-3}$ | $1.359\times10^{-3}$ |
    | $10^6$ | 2.7182804691 | $1.359\times10^{-6}$ | $1.359\times10^{-6}$ |

    The error is $O(1/n)$ with coefficient $e/2$. This follows from $n\ln(1 + 1/n) = 1 - \frac1{2n} + O(n^{-2})$, a Taylor expansion of the logarithm.

    **Standard limits** (sympy): $\lim\frac{\sin x}{x} = 1$, $\lim\frac{1 - \cos x}{x^2} = \frac12$, $\lim_{0^+}x\ln x = 0$.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 5.1 (convergence of sequences and partial sums, Cauchy criterion). The ε–δ definitions, continuity theorems and order notation are standard calculus, written for this note. Calculations in `Claude outputs/part0_math_batchE.py`, section A.
