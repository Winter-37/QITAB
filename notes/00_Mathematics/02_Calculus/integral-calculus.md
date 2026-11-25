---
id: integral-calculus
title: Integral calculus - the Riemann integral, the fundamental theorem, substitution, integration by parts, partial fractions, improper integrals, the Gamma function, differentiating under the integral sign, and multiple integrals with Jacobians
summary: The definite integral is the limit of Riemann sums, and the fundamental theorem of calculus ties it to antiderivatives. The working techniques are substitution, integration by parts, partial fractions, and differentiation with respect to a parameter (the Leibniz rule). Improper integrals converge or diverge by comparison with powers and exponentials. The Gamma function Γ(z) = ∫ t^{z−1}e^{−t} dt generalizes the factorial and gives every Gaussian and Slater-type radial integral. Multiple integrals are done iteratively (Fubini) and transform with the absolute Jacobian determinant, r² sin θ in spherical coordinates. Worked examples cover each technique, the 3D Gaussian, and the error of the midpoint rule.
status: in-progress
kind: theory
level: introductory
tags: [integral, riemann-sum, fundamental-theorem-of-calculus, substitution, integration-by-parts, partial-fractions, improper-integral, gamma-function, beta-function, leibniz-integral-rule, multiple-integral, jacobian-determinant, gaussian-integral]
prerequisites: [differential-calculus]
related: [gaussian-integral-identities, curvilinear-coordinates, divergence-and-gauss-theorem, asymptotic-expansions, complex-numbers]
key: ftc
order: 40
date: 2026-11-25
---

Real functions. $d\tau = dx\,dy\,dz$ is the volume element, as in Arfken.

## The definite integral

**Riemann sums.** Divide $[a, b]$ into subintervals of widths $\Delta x_k$ and pick a point $\xi_k$ in each. If the sums $\sum_kf(\xi_k)\Delta x_k$ tend to the same limit as the largest width tends to zero, whatever the choice of points, that limit is $\int_a^bf(x)\,dx$. Every continuous function on a closed interval is integrable, and so is every bounded function with finitely many discontinuities.

**Properties.** Linearity; additivity $\int_a^b + \int_b^c = \int_a^c$; $\int_b^a = -\int_a^b$; monotonicity ($f\le g\Rightarrow\int f\le\int g$); and $|\int f|\le\int|f|$. The mean value theorem for integrals: for continuous $f$ there is a $\xi\in[a, b]$ with $\int_a^bf\,dx = f(\xi)(b - a)$ (Arfken Eq. 5.84).

**Fundamental theorem of calculus.** If $f$ is continuous, $F(x) = \int_a^xf(t)\,dt$ is differentiable with $F' = f$; and if $G' = f$, then

$$
\int_a^bf(x)\,dx = G(b) - G(a).
\label{ftc}
$$

Differentiation and integration are inverse operations; an antiderivative is fixed up to a constant.

## Techniques

**Substitution.** With $x = g(u)$, $\int f(x)\,dx = \int f(g(u))\,g'(u)\,du$, with the limits transformed too. Example: $\int_0^\infty xe^{-x^2}dx = \tfrac12\int_0^\infty e^{-u}du = \tfrac12$ with $u = x^2$.

**Integration by parts.** From the product rule,

$$
\int_a^bu\,v'\,dx = \big[uv\big]_a^b - \int_a^bu'\,v\,dx .
$$

It moves a derivative from one factor to the other. In quantum mechanics this is how $\langle\psi|\hat p|\phi\rangle$ is shown to be Hermitian: the boundary term vanishes for normalizable functions. Repeated parts give $\int_0^\infty x^ne^{-x}dx = n!$.

**Partial fractions.** A proper rational function $p/q$ is written as a sum over the factors of $q$. For distinct real roots, $\frac{1}{(x - a)(x - b)} = \frac{1}{a - b}\Big(\frac{1}{x - a} - \frac{1}{x - b}\Big)$. Repeated roots get terms up to the multiplicity, and irreducible quadratics give $\arctan$ terms. The coefficients are residues ([[laurent-series-singularities-and-residues]]).

**Trigonometric and hyperbolic substitutions.** $\sqrt{a^2 - x^2}$ with $x = a\sin\theta$; $\sqrt{a^2 + x^2}$ with $x = a\sinh u$; $\sqrt{x^2 - a^2}$ with $x = a\cosh u$.

**Differentiating under the integral sign (Leibniz rule).** If $f$ and $\partial f/\partial\alpha$ are continuous,

$$
\frac{d}{d\alpha}\int_{a(\alpha)}^{b(\alpha)}f(x,\alpha)\,dx = \int_a^b\frac{\partial f}{\partial\alpha}dx + f(b,\alpha)\,b'(\alpha) - f(a,\alpha)\,a'(\alpha).
$$

With fixed limits only the first term remains. Applied to $\int e^{-\alpha x^2}dx = \sqrt{\pi/\alpha}$ it generates all the moments $\int x^{2n}e^{-\alpha x^2}dx$, the workhorse of Gaussian basis-set integrals ([[gaussian-integral-identities]]).

## Improper integrals

**Definition.** An integral over an infinite range, or of a function unbounded at an endpoint, is defined as a limit: $\int_a^\infty f = \lim_{R\to\infty}\int_a^Rf$. It **converges** if the limit exists, and **converges absolutely** if $\int|f|$ converges.

**Comparison with powers.** $\int_1^\infty x^{-p}dx$ converges for $p > 1$; $\int_0^1x^{-p}dx$ converges for $p < 1$. Any $e^{-\alpha x}$ ($\alpha > 0$) beats any power at infinity. If $|f|\le g$ and $\int g$ converges, so does $\int f$.

**Conditional convergence.** $\int_0^\infty\frac{\sin x}{x}dx = \frac\pi2$ converges, but not absolutely ($\int|\sin x|/x$ diverges like $\ln R$). It is evaluated by contour integration in [[laurent-series-singularities-and-residues]]. Integrals with a singularity inside the range may exist only as a principal value, $P\int$, which is the symmetric limit around the singular point.

## The Gamma and Beta functions

**Definition.** For $\mathrm{Re}\,z > 0$ (Arfken Sec. 8.1),

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}\,dt,\qquad \Gamma(z + 1) = z\,\Gamma(z),\qquad \Gamma(n + 1) = n!,\qquad \Gamma(\tfrac12) = \sqrt\pi .
\label{gamma}
$$

The recurrence is integration by parts. $\Gamma(\tfrac12) = \sqrt\pi$ is the Gaussian integral after the substitution $t = x^2$. Half-integer values follow from the recurrence: $\Gamma(\tfrac72) = \tfrac{15}8\sqrt\pi$.

**Radial integrals.** Every radial integral of a Slater or Gaussian function reduces to Eq. [[#gamma]]:

$$
\int_0^\infty r^ne^{-\zeta r}dr = \frac{n!}{\zeta^{n+1}},\qquad \int_0^\infty r^ne^{-\alpha r^2}dr = \frac{\Gamma\big(\frac{n+1}2\big)}{2\alpha^{(n+1)/2}} .
$$

**Beta function.** $B(p, q) = \int_0^1t^{p-1}(1 - t)^{q-1}dt = \Gamma(p)\Gamma(q)/\Gamma(p + q)$ (Arfken Sec. 8.4). It gives the angular integrals $\int_0^{\pi/2}\sin^{2p-1}\theta\cos^{2q-1}\theta\,d\theta = \tfrac12B(p, q)$.

## Multiple integrals

**Iterated integration.** Over a rectangle, a continuous function's double integral equals either iterated integral (Fubini). Over other regions, the inner limits depend on the outer variable. Order can be exchanged, which often turns a hard integral into an easy one.

**Change of variables.** Under $\mathbf x = \mathbf x(\mathbf u)$,

$$
\int f(\mathbf x)\,d^n x = \int f(\mathbf x(\mathbf u))\,\Big|\det\frac{\partial\mathbf x}{\partial\mathbf u}\Big|\,d^n u ,
$$

with the Jacobian of [[differential-calculus]]. Standard cases:

- **Polar:** $dx\,dy = r\,dr\,d\phi$.
- **Cylindrical:** $d\tau = \rho\,d\rho\,d\phi\,dz$.
- **Spherical:** $d\tau = r^2\sin\theta\,dr\,d\theta\,d\phi$, and the full solid angle is $\int\sin\theta\,d\theta\,d\phi = 4\pi$.

[[curvilinear-coordinates]] derives these from scale factors.

**The Gaussian integral.** Squaring and going to polar coordinates, $\big(\int e^{-x^2}dx\big)^2 = \int_0^{2\pi}\int_0^\infty e^{-r^2}r\,dr\,d\phi = \pi$. So $\int_{-\infty}^\infty e^{-x^2}dx = \sqrt\pi$, and in three dimensions $\int e^{-r^2}d\tau = \pi^{3/2}$.

## Worked examples

!!! example "Each technique once (computed for this note)"
    **Parts.** $\int_0^\infty xe^{-x}dx = [-xe^{-x}]_0^\infty + \int_0^\infty e^{-x}dx = 1 = \Gamma(2)$.

    **Gamma values.** $\Gamma(\tfrac12) = \sqrt\pi$, $\Gamma(5) = 24$, $\Gamma(\tfrac72) = \tfrac52\cdot\tfrac32\cdot\tfrac12\sqrt\pi = \tfrac{15}8\sqrt\pi = 3.323351$.

    **Partial fractions.** $\frac1{x^2 - 1} = \frac12\Big(\frac1{x - 1} - \frac1{x + 1}\Big)$, so $\int_2^3\frac{dx}{x^2 - 1} = \tfrac12[\ln\tfrac{x - 1}{x + 1}]_2^3 = \tfrac12\ln\tfrac32 = 0.202733$.

    **Leibniz rule.** $-\frac{d}{d\alpha}\sqrt{\pi/\alpha} = \frac{\sqrt\pi}{2\alpha^{3/2}} = \int x^2e^{-\alpha x^2}dx$, confirmed by direct integration.

    **Jacobian.** $\det\partial(x, y, z)/\partial(r,\theta,\phi) = r^2\sin\theta$, and $4\pi\int_0^\infty r^2e^{-r^2}dr = \pi^{3/2}$.

    **A Riemann sum and its error.** The midpoint rule $M_N$ for $\int_0^1e^x\,dx = e - 1$ with $N$ intervals leaves $\int - M_N = 7.157\times10^{-4}$ at $N = 10$ and $7.159\times10^{-6}$ at $N = 100$. The error formula $\int - M_N = \frac{(b - a)h^2}{24}f''(\xi)$, with $h = 1/N$ and $f''$ averaged to $e - 1$, predicts $7.160\times10^{-4}$ and $7.160\times10^{-6}$. The sum converges as $O(N^{-2})$.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 1.10 (vector integration), Sec. 5.6 (mean value theorem of integral calculus), Secs. 8.1 and 8.4 (Gamma and Beta functions). The Riemann construction, the integration techniques and the Leibniz rule are standard calculus, written for this note. Calculations in `Claude outputs/part0_math_batchE.py`, section A.
