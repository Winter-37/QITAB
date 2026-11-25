---
id: sturm-liouville-theory
title: Sturm-Liouville theory - self-adjoint second-order operators, boundary conditions, real eigenvalues, orthogonality with a weight, completeness, the oscillation theorem, and the classical eigenvalue problems
summary: Any linear second-order eigenvalue equation can be written in Sturm–Liouville form (p y')' + q y = −λ w y with weight w > 0. With boundary conditions that make the boundary terms of integration by parts vanish, the operator is self-adjoint (Hermitian) with respect to ∫ w u* v dx. Its eigenvalues are then real and can be ordered, eigenfunctions of different eigenvalues are orthogonal with weight w, and the set is complete. The n-th eigenfunction has n − 1 interior nodes, and the lowest eigenvalue minimizes the Rayleigh quotient. The Fourier, Legendre, Hermite, Laguerre and Bessel problems are all of this type, which is why their solutions are orthogonal families. This is the differential-equation form of the spectral theorem behind quantum mechanics. Worked examples: −y'' = λy solved by finite differences, Legendre orthogonality, and the node count.
status: in-progress
kind: theory
level: intermediate
tags: [sturm-liouville, self-adjoint-operator, hermitian-operator, weight-function, orthogonality, completeness, oscillation-theorem, rayleigh-quotient, eigenvalue-problem, boundary-conditions, gram-schmidt]
prerequisites: [series-solutions-and-the-frobenius-method, partial-differential-equations-and-separation-of-variables]
related: [classical-orthogonal-polynomials, eigenfunction-expansions-and-generating-functions, spectral-decomposition-and-normal-operators, orthonormal-functions-and-operators, matrix-eigenvalue-problem, fourier-series]
key: sl
order: 50
date: 2026-11-25
---

$\langle u|v\rangle_w = \int_a^bw(x)\,u^*(x)v(x)\,dx$ is the inner product with weight $w > 0$ on $(a, b)$. $\mathcal L y = (py')' + qy$ with $p > 0$ on $(a, b)$ and $p$, $p'$, $q$, $w$ real and continuous.

## Self-adjoint form

**The Sturm–Liouville equation.** The eigenvalue problem (Arfken Sec. 10.1) is

$$
\frac{d}{dx}\Big(p(x)\frac{dy}{dx}\Big) + q(x)y + \lambda\,w(x)\,y = 0 .
\label{sl}
$$

**Any linear equation fits.** Every $a_2y'' + a_1y' + a_0y + \lambda by = 0$ can be put in this form. Multiply by $\mu = \frac1{a_2}\exp\int\frac{a_1}{a_2}dx$, which makes $p = a_2\mu$ satisfy $p' = a_1\mu$. The same integrating-factor idea appears for first-order equations ([[first-order-differential-equations]]). Example: Hermite's $y'' - 2xy' + 2ny = 0$ times $e^{-x^2}$ gives $(e^{-x^2}y')' + 2ne^{-x^2}y = 0$, so $p = w = e^{-x^2}$ and $\lambda = 2n$.

**Self-adjointness.** Integrating by parts twice (Green's identity in one dimension):

$$
\int_a^b(u^*\mathcal Lv - v\,\mathcal Lu^*)\,dx = \Big[p\,(u^*v' - u^{*\prime}v)\Big]_a^b .
\label{green}
$$

$\mathcal L$ is self-adjoint (Hermitian) when the right side vanishes for all functions in the domain (Arfken Sec. 10.2). That happens for:

- **Regular problems:** Dirichlet, Neumann or mixed conditions $\alpha y + \beta y' = 0$ at each end;
- **Periodic conditions:** $y(a) = y(b)$, $y'(a) = y'(b)$ with $p(a) = p(b)$;
- **Singular problems:** $p$ vanishes at an endpoint (Legendre at $\pm1$, Laguerre at 0), and one requires only boundedness there;
- **Infinite intervals:** the solutions decay fast enough (Hermite).

The boundary conditions are part of the operator. The same differential expression with the wrong conditions is not Hermitian. This is the one-dimensional case of why $-i\hbar\,d/dx$ needs its domain stated.

## The theorems

From Eq. [[#green]] with $\mathcal Ly_n = -\lambda_nwy_n$ (Arfken Secs. 10.2–10.4):

1. **Real eigenvalues.** Take $u = v = y_n$: $(\lambda_n - \lambda_n^*)\langle y_n|y_n\rangle_w = 0$.
2. **Orthogonality with weight.** For $\lambda_m\ne\lambda_n$, $(\lambda_n - \lambda_m)\langle y_m|y_n\rangle_w = 0$, so $\int w\,y_m^*y_n\,dx = 0$. Degenerate eigenfunctions (possible with periodic conditions: $\sin nx$ and $\cos nx$) can be orthogonalized by Gram–Schmidt (Arfken Sec. 10.3).
3. **Ordering.** For a regular problem the eigenvalues are simple and form an increasing sequence $\lambda_1 < \lambda_2 < \cdots\to\infty$.
4. **Oscillation theorem.** The eigenfunction $y_n$ has exactly $n - 1$ zeros inside $(a, b)$. The ground state has no node, the first excited state one, and so on, as for one-dimensional bound states.
5. **Completeness.** The eigenfunctions form a complete set: every square-integrable $f$ (with weight $w$) has a convergent-in-the-mean expansion $f = \sum c_ny_n$, with $c_n = \langle y_n|f\rangle_w/\langle y_n|y_n\rangle_w$ ([[eigenfunction-expansions-and-generating-functions]]).
6. **Variational characterization.** The lowest eigenvalue minimizes the Rayleigh quotient,

   $$\lambda_1 = \min_y\frac{\int(p|y'|^2 - q|y|^2)\,dx}{\int w|y|^2\,dx} ,$$

   which is the variational principle in its original form. The higher eigenvalues are minima over functions orthogonal to the lower eigenfunctions.

**Connection to linear algebra.** These are the statements of the spectral theorem for Hermitian matrices ([[spectral-decomposition-and-normal-operators]]), carried over to an infinite-dimensional function space. Discretizing $\mathcal L$ on a grid gives a real symmetric matrix (the weight becomes a metric, like an overlap matrix). Its eigenvectors approximate the eigenfunctions ([[matrix-eigenvalue-problem]]).

## The classical problems

| problem | $p$ | $q$ | $w$ | interval | $\lambda$ | eigenfunctions |
|---|---|---|---|---|---|---|
| Fourier | 1 | 0 | 1 | $(0, L)$, $y = 0$ at ends | $(n\pi/L)^2$ | $\sin(n\pi x/L)$ |
| Legendre | $1 - x^2$ | 0 | 1 | $(-1, 1)$, bounded | $l(l + 1)$ | $P_l(x)$ |
| associated Legendre | $1 - x^2$ | $-m^2/(1 - x^2)$ | 1 | $(-1, 1)$ | $l(l + 1)$ | $P_l^m(x)$ |
| Hermite | $e^{-x^2}$ | 0 | $e^{-x^2}$ | $(-\infty,\infty)$ | $2n$ | $H_n(x)$ |
| Laguerre | $xe^{-x}$ | 0 | $e^{-x}$ | $(0,\infty)$ | $n$ | $L_n(x)$ |
| Bessel, fixed $\nu$ | $x$ | $-\nu^2/x$ | $x$ | $(0, a)$, $y(a) = 0$ | $k^2$ | $J_\nu(kx)$ |

In the Bessel row the eigenvalue sits in the argument: the zeros of $J_\nu$ fix $k$. The orthogonality relations, norms and recurrences of the polynomials are in [[classical-orthogonal-polynomials]] and [[spherical-bessel-functions]].

## Worked examples

!!! example "A discretized Sturm–Liouville problem and Legendre orthogonality (computed for this note)"
    **$-y'' = \lambda y$ on $(0,\pi)$, $y(0) = y(\pi) = 0$.** The exact eigenvalues are $n^2$ with eigenfunctions $\sin nx$. A three-point finite-difference matrix on 400 interior points gives lowest eigenvalues 0.99999, 3.99992, 8.99959 and 15.99869. The error grows as $n^4h^2/12$, the truncation error of the second difference. The overlap of the first two eigenvectors is 0 to machine precision: a symmetric matrix has orthogonal eigenvectors, the discrete form of theorem 2.

    **Nodes.** The first five eigenvectors change sign 0, 1, 2, 3 and 4 times across the grid, the discrete oscillation theorem.

    **Legendre.** $\int_{-1}^1P_2P_4\,dx = 0$ and $\int_{-1}^1P_3^2\,dx = \tfrac27 = \tfrac2{2l + 1}$ (sympy).

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 10.1 (self-adjoint ODEs, the integrating factor, boundary conditions), Sec. 10.2 (Hermitian operators: real eigenvalues and orthogonality), Sec. 10.3 (Gram–Schmidt orthogonalization), Sec. 10.4 (completeness of eigenfunctions). The oscillation theorem and the Rayleigh-quotient statement are standard results quoted here without proof. Calculations in `Claude outputs/part0_math_batchE.py`, section E.
