---
id: series-solutions-and-the-frobenius-method
title: Series solutions and the Frobenius method - ordinary and singular points, the indicial equation, recurrence relations, termination and quantization, Fuchs's theorem, and the second solution
summary: A linear second-order ODE with analytic coefficients has power-series solutions about every ordinary point. About a regular singular point, Frobenius's ansatz y = Σ aₖ x^{k+s} works: the lowest power gives the indicial equation for s, and the rest gives a recurrence for the coefficients. Fuchs's theorem guarantees at least one such solution, converging up to the nearest other singularity. When the roots of the indicial equation differ by an integer, the second solution may contain a logarithm. Physical boundary conditions often allow only series that terminate. For the Hermite equation, a series that does not terminate grows like e^{x²}, so normalizable harmonic-oscillator states require ν = n: that is where quantization comes from. Worked examples: the Hermite series terminating to H₃, the e^{x²} growth when it does not, and the Bessel series for J₀.
status: in-progress
kind: derivation
level: intermediate
tags: [frobenius-method, power-series-solution, indicial-equation, regular-singular-point, recurrence-relation, fuchs-theorem, hermite-equation, bessel-equation, legendre-equation, termination, quantization]
prerequisites: [second-order-linear-differential-equations, power-series-and-radius-of-convergence]
related: [sturm-liouville-theory, classical-orthogonal-polynomials, spherical-bessel-functions, harmonic-oscillator-analytic-solution, partial-differential-equations-and-separation-of-variables]
key: recur
order: 40
date: 2026-11-25
---

$y'' + P(x)y' + Q(x)y = 0$ in standard form. Series are about $x_0 = 0$ unless stated (shift $x\to x - x_0$ otherwise).

## Ordinary and singular points

**Definitions** (Arfken Sec. 9.4):

- $x_0$ is an **ordinary point** if $P$ and $Q$ are analytic there.
- It is a **regular singular point** if $P$ or $Q$ is singular, but $(x - x_0)P$ and $(x - x_0)^2Q$ are analytic.
- It is an **irregular (essential) singular point** otherwise.

The point at infinity is classified by substituting $x = 1/z$.

**Examples.**

| equation | singular points |
|---|---|
| Hermite $y'' - 2xy' + 2\nu y = 0$ | none finite; irregular at $\infty$ |
| Legendre $(1 - x^2)y'' - 2xy' + l(l + 1)y = 0$ | regular at $x = \pm1$ and $\infty$ |
| Bessel $x^2y'' + xy' + (x^2 - \nu^2)y = 0$ | regular at 0, irregular at $\infty$ |
| hydrogen radial equation | regular at $r = 0$, irregular at $\infty$ |

The singular points are where the physics is: the nucleus, the poles of the sphere, infinity.

## Series about an ordinary point

**Ansatz.** Substitute $y = \sum_ka_kx^k$, collect each power of $x$, and set its coefficient to zero. That uniqueness argument is valid because power series are unique ([[power-series-and-radius-of-convergence]]). The result is a recurrence for $a_k$; $a_0$ and $a_1$ are the two free constants. The series converges at least up to the nearest singular point of $P$ or $Q$ in the complex plane.

**The Hermite equation.** $y'' - 2xy' + 2\nu y = 0$ gives

$$
a_{k+2} = \frac{2(k - \nu)}{(k + 1)(k + 2)}a_k .
\label{recur}
$$

The even and odd coefficients decouple, giving an even solution (from $a_0$) and an odd one (from $a_1$). Both converge for all $x$, since there is no finite singular point.

## The Frobenius method

**The ansatz at a regular singular point.** About a regular singular point, try (Arfken Sec. 9.5)

$$
y = x^s\sum_{k=0}^\infty a_kx^k,\qquad a_0\ne0 .
$$

Multiply the equation by $x^2$, so that $xP = p_0 + p_1x + \cdots$ and $x^2Q = q_0 + q_1x + \cdots$ are power series. The lowest power of $x$ gives the **indicial equation**

$$
s(s - 1) + p_0s + q_0 = 0 ,
$$

and higher powers give a recurrence for $a_k$.

**Bessel's equation.** $p_0 = 1$ and $q_0 = -\nu^2$, so $s^2 = \nu^2$ and $s = \pm\nu$. With $s = \nu$ the recurrence $a_{k+2} = -a_k/[(k + 2)(k + 2 + 2\nu)]$ gives $J_\nu$:

$$
J_\nu(x) = \sum_{m=0}^\infty\frac{(-1)^m}{m!\,\Gamma(m + \nu + 1)}\Big(\frac x2\Big)^{2m + \nu} .
$$

**Fuchs's theorem.** At an ordinary point, or a regular singular point, at least one Frobenius solution exists. It converges up to the nearest other singularity (Arfken Sec. 9.5). At an irregular singular point the ansatz can fail. There one first factors out the asymptotic behaviour, such as $e^{-x^2/2}$ for the oscillator or $e^{-\kappa r}$ for hydrogen.

**The second solution.** Let the indicial roots be $s_1\ge s_2$ (real parts):

- **$s_1 - s_2$ not an integer.** Both roots give independent Frobenius series.
- **$s_1 - s_2$ an integer, or zero.** The smaller root may fail, and the second solution has the form $y_2 = cy_1\ln x + x^{s_2}\sum b_kx^k$ (Arfken Sec. 9.6). It can also be obtained from the Wronskian ([[second-order-linear-differential-equations]]). The Neumann function $Y_0$ (Bessel), the Legendre function $Q_l$, and the irregular solutions at the nucleus are of this kind. All are singular at the regular singular point, and physical boundary conditions usually exclude them.

## Termination and quantization

**Why the series must stop.** For the harmonic oscillator, $\psi = h(\xi)e^{-\xi^2/2}$ turns the Schrödinger equation into the Hermite equation with $E = (\nu + \tfrac12)\hbar\omega$ ([[harmonic-oscillator-analytic-solution]]).

- **If $\nu$ is not an integer.** By Eq. [[#recur]], $a_{k+2}/a_k\to2/k$ for large $k$. That is the ratio of the series $e^{\xi^2} = \sum\xi^{2j}/j!$. The solution grows like $e^{\xi^2}$, and $\psi$ grows like $e^{\xi^2/2}$, which is not normalizable.
- **If $\nu = n$ is a nonnegative integer.** One of the two series terminates at $k = n$, giving the Hermite polynomial $H_n$, and the other is discarded.

So the boundary condition at infinity forces $E = (n + \tfrac12)\hbar\omega$.

**Elsewhere.**

- **Legendre's equation.** The series diverges at $x = \pm1$ (the poles of the sphere) unless it terminates. That happens for $l(l + 1)$ with integer $l$, giving $P_l$.
- **Hydrogen.** The radial series terminates for $E_n = -1/(2n^2)$ hartree and gives associated Laguerre polynomials ([[classical-orthogonal-polynomials]]).

## Worked examples

!!! example "Termination, growth, and J₀ (computed for this note)"
    **Hermite, $\nu = 3$.** Eq. [[#recur]] from $a_1 = 1$, $a_0 = 0$ gives $a_3 = 2(1 - 3)/(2\cdot3) = -\tfrac23$, then $a_5 = 0$ and every later odd coefficient 0. So $y = x - \tfrac23x^3 = -\tfrac1{12}(8x^3 - 12x) = -H_3/12$.

    **Hermite, $\nu = 2.5$.** The even series from $a_0 = 1$ does not terminate. At $k = 100$, $a_{k+2}/a_k = 0.01893$, approaching $2/k = 0.02000$ from below. These are the coefficients of an $e^{x^2}$ growth.

    **Bessel $J_0$.** Twenty terms of the series at $x = 2.4$ give $0.0025076833$, against scipy's $J_0(2.4) = 0.0025076833$. The point is close to the first zero, 2.40483, where the alternating terms nearly cancel.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 9.4 (singular points), Sec. 9.5 (series solutions, Frobenius's method, the indicial equation, Fuchs's theorem, with the oscillator and Bessel examples), Sec. 9.6 (a second solution, logarithmic terms), Sec. 13.1 (Hermite functions). Calculations in `Claude outputs/part0_math_batchE.py`, section E.
