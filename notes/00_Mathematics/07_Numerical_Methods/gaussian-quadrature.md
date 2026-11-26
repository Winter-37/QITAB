---
id: gaussian-quadrature
title: Numerical integration - Newton-Cotes rules, Gaussian quadrature from orthogonal polynomials, the Golub-Welsch algorithm, Gauss-Hermite and Gauss-Laguerre rules, Lebedev angular grids, and product grids in three dimensions
summary: An n-point Newton–Cotes rule on equally spaced points integrates polynomials of degree n − 1 (n for odd n) exactly. Choosing the points as well as the weights doubles that: Gaussian quadrature with the n zeros of the orthogonal polynomial for a weight W(x) integrates every polynomial of degree up to 2n − 1 against W exactly. The proof divides the integrand by Pₙ and uses orthogonality. Nodes and weights follow from the three-term recurrence as the eigenvalues and first eigenvector components of a tridiagonal Jacobi matrix (Golub–Welsch). Gauss–Legendre, Gauss–Hermite and Gauss–Laguerre are the cases used most, and the art is putting the hard part of the integrand into W. Smooth integrands converge exponentially, kinks and cusps only algebraically. On the sphere, Lebedev grids integrate spherical harmonics up to a given degree exactly. Worked examples: exactness tests, convergence for three integrands, oscillator and hydrogen moments, Lebedev exactness, and a radial × angular grid for a two-centre overlap.
status: in-progress
kind: theory
level: intermediate
tags: [numerical-integration, quadrature, newton-cotes, simpson-rule, gaussian-quadrature, gauss-legendre, gauss-hermite, gauss-laguerre, golub-welsch, jacobi-matrix, lebedev-grid, product-grid, molecular-grids]
prerequisites: [classical-orthogonal-polynomials, floating-point-and-numerical-error]
related: [electron-repulsion-integrals-md-os-rys, gaussian-integral-identities, integral-calculus, asymptotic-expansions, kohn-sham-dft, sturm-liouville-theory]
key: gauss
order: 20
date: 2026-11-26
---

$\int_a^bf(x)W(x)\,dx\approx\sum_{i=1}^nw_if(x_i)$, with nodes (abscissae) $x_i$ and weights $w_i$. $W(x) > 0$ is a weight function. $P_n$ is the degree-$n$ polynomial orthogonal with respect to $W$ on $[a, b]$ ([[classical-orthogonal-polynomials]]). "Exact to degree $d$" means exact for every polynomial of degree $\le d$.

## Newton–Cotes rules

**Equally spaced points.** Interpolate $f$ by a polynomial through $n$ equally spaced points and integrate the polynomial:

| rule | points | exact to degree | error on one panel of width $h$ |
|---|---|---|---|
| trapezoid | 2 | 1 | $-\frac{h^3}{12}f''$ |
| Simpson | 3 | 3 | $-\frac{h^5}{90}f^{(4)}$ (for $h$ the half-width) |

Simpson gains an extra degree by symmetry. Composite rules repeat a low-order rule over many panels. Their errors fall as a fixed power of the panel width, $h^2$ for the trapezoid and $h^4$ for Simpson, and Richardson extrapolation removes the leading term ([[floating-point-and-numerical-error]]).

**When equal spacing is right.** For periodic analytic functions over a full period the plain trapezoid rule converges exponentially. This is why equally spaced grids are right for Fourier series and plane waves.

## Gaussian quadrature

**The theorem.** Let $x_1,\dots,x_n$ be the zeros of $P_n$. They are real, distinct, inside $(a, b)$, and interlace those of $P_{n-1}$. With weights

$$
w_i = \int_a^bW(x)\prod_{j\ne i}\frac{x - x_j}{x_i - x_j}\,dx ,
$$

the rule $\sum_iw_if(x_i)$ integrates every polynomial of degree $\le2n - 1$ exactly (HJO Eqs. 9.6.14–9.6.15):

$$
\int_a^bf(x)\,W(x)\,dx = \sum_{i=1}^nw_i\,f(x_i)\qquad(\deg f\le2n - 1).
\label{gauss}
$$

**Proof** (HJO Sec. 9.6.3). Divide: $f = QP_n + R$ with $\deg Q$, $\deg R < n$.

- $\int QP_nW = 0$ by orthogonality.
- $\int RW$ is reproduced exactly because $R$ equals its Lagrange interpolant through the $n$ nodes.
- At the nodes, $f(x_i) = R(x_i)$ because $P_n(x_i) = 0$.

The $2n$ free parameters ($n$ nodes and $n$ weights) buy exactness for $2n$ monomials, twice what $n$ fixed nodes give. The weights are all positive, which keeps the rule numerically stable.

**Error.** For smooth $f$ the error is proportional to $f^{(2n)}(\xi)/(2n)!$. For analytic integrands it falls exponentially with $n$, at a rate set by the distance of the nearest complex singularity from the interval, as for power series ([[power-series-and-radius-of-convergence]]). Kinks, cusps and endpoint singularities give only algebraic convergence. That is why molecular integration grids split space around each nucleus, so that each cusp sits at a grid origin rather than inside a cell.

**Golub–Welsch.** Monic orthogonal polynomials satisfy $p_{k+1} = (x - \alpha_k)p_k - \beta_kp_{k-1}$ (HJO Eqs. 9.6.6–9.6.9 give the classical cases). Build the symmetric tridiagonal Jacobi matrix

$$
\mathbf J_n = \begin{pmatrix}\alpha_0&\sqrt{\beta_1}\\\sqrt{\beta_1}&\alpha_1&\ddots\\&\ddots&\ddots&\sqrt{\beta_{n-1}}\\&&\sqrt{\beta_{n-1}}&\alpha_{n-1}\end{pmatrix}.
$$

Its eigenvalues are the nodes. The weights are $w_i = \mu_0v_{1i}^2$, where $v_{1i}$ is the first component of the $i$-th normalized eigenvector and $\mu_0 = \int W$. Nodes therefore come from a well-conditioned symmetric eigenproblem rather than from root-finding. For a nonclassical weight, $\alpha_k$ and $\beta_k$ come from a Lanczos (Stieltjes) process on a discretization of $W$, or from the moments of $W$.

## The standard rules

| rule | interval | weight $W$ | typical use |
|---|---|---|---|
| Gauss–Legendre | $[-1, 1]$ (map to $[a, b]$) | 1 | smooth integrands on a finite interval |
| Gauss–Chebyshev | $[-1, 1]$ | $(1 - x^2)^{-1/2}$ | endpoint singularities; the basis of several radial grids |
| Gauss–Hermite | $(-\infty,\infty)$ | $e^{-x^2}$ | oscillator matrix elements, Gaussian-weighted averages |
| (generalized) Gauss–Laguerre | $[0,\infty)$ | $x^\alpha e^{-x}$ | radial integrals with exponential decay |

**Putting the hard part into $W$.** Factor the difficult part of the integrand into the weight, so that what remains is close to a low-degree polynomial. For a hydrogenic density times $r^2$, generalized Laguerre with $\alpha = 2$ makes $\langle r^p\rangle$ exact for $p\ge0$. But $\langle1/r\rangle$ leaves $1/r$, which is not a polynomial, in the integrand. Choosing $\alpha = 1$ instead absorbs it.

## Gaussian quadrature for Coulomb integrals: Rys quadrature

**The idea.** A Coulomb integral over Gaussians with total angular momentum $L$ is a combination of Boys functions $F_n(x) = \int_0^1t^{2n}e^{-xt^2}dt$ with $n\le L$. It is therefore the integral of a polynomial of degree $L$ in $u = t^2$ against the weight $e^{-xt^2}$ (HJO Sec. 9.11).

**The rule.** Gaussian quadrature for that weight, the Rys polynomials, is exact with $N = \lfloor L/2\rfloor + 1$ points, and it bypasses the Boys function. The details are in [[electron-repulsion-integrals-md-os-rys]]: the Boys function's series, asymptotic and recursive evaluation, and the Rys roots from the Boys moments, with an implementation checked against libcint.

**A check.** With $x = 1$ and $N = 3$, weights built by a Lanczos process on a discretized weight in $u$ reproduce $F_0,\dots,F_5$ to $4\times10^{-15}$. They fail first at $F_6$ (error $2\times10^{-4}$), the first moment beyond degree $2N - 1 = 5$.

## Integration over the sphere and over space

**Lebedev grids.** Points on the unit sphere with octahedral symmetry and weights chosen so that every spherical harmonic of degree $\le L$ is integrated exactly. Equivalently, products $Y_{l_1m_1}Y_{l_2m_2}$ are integrated exactly for $l_1 + l_2\le L$. They need roughly $(L + 1)^2/3$ points, against about $(L + 1)^2/2$ for a product of Gauss rules in $\theta$ and $\phi$.

**Product grids for molecules.** A radial rule times an angular rule around one centre integrates functions centred there well. Products of functions on different centres have cusps at every nucleus. DFT and other numerical integrations therefore use one radial × Lebedev grid per atom, combined with smooth partition-of-unity weights that assign each point mostly to its nearest atom (Becke-type partitioning). The radial rules are mapped Gauss–Chebyshev or similar rules. These choices are described in the DFT literature, to be added with the DFT chapter ([[kohn-sham-dft]]).

## Worked examples

!!! example "Exactness, convergence and grids (computed for this note)"
    **Exactness.** Four-point Gauss–Legendre integrates $x^0,\dots,x^7$ to $3\times10^{-16}$ and fails first at $x^8$ (error 0.01), as Eq. [[#gauss]] says. Three-point Simpson is exact to $x^3$ and fails at $x^4$ (error 0.3).

    **Convergence** on $[-1, 1]$ (absolute error), Gauss–Legendre / composite Simpson with the same number of points:

    | integrand | $N = 5$ | $N = 9$ | $N = 17$ | $N = 33$ |
    |---|---|---|---|---|
    | $e^x$ (entire) | $8\times10^{-10}$ / $8\times10^{-4}$ | $<10^{-15}$ / $5\times10^{-5}$ | $4\times10^{-16}$ / $3\times10^{-6}$ | $4\times10^{-16}$ / $2\times10^{-7}$ |
    | $1/(1 + 25x^2)$ (poles at $\pm i/5$) | 0.16 / 0.019 | 0.029 / 0.026 | $1.2\times10^{-3}$ / $2.7\times10^{-3}$ | $2.1\times10^{-6}$ / $1.8\times10^{-5}$ |
    | $|x|$ (kink at 0) | 0.055 / 0 | 0.018 / 0 | $5.4\times10^{-3}$ / 0 | $1.5\times10^{-3}$ / 0 |

    - For the entire function Gauss reaches machine precision with 9 points.
    - For the function with nearby poles it converges exponentially but slowly at first.
    - For $|x|$ Gauss is only algebraic, while Simpson is exact because the kink sits on a node and the function is linear between nodes. Placing grid points at singularities matters more than the order of the rule.

    **Golub–Welsch.** The Jacobi matrices with $\beta_k = k^2/(4k^2 - 1)$ (Legendre) and $\beta_k = k/2$ (Hermite) reproduce numpy's 6-point nodes and weights to $10^{-15}$.

    **Moments.**

    - Oscillator ground state ($W = e^{-x^2}$), 3-point Gauss–Hermite: $\langle x^2\rangle = 0.5$ and $\langle x^4\rangle = 0.75$ exactly; $\langle x^6\rangle$ comes out 1.125 against 1.875, since degree 6 exceeds $2n - 1 = 5$.
    - Hydrogen 1s, 4-point Laguerre with $\alpha = 2$: $\langle r\rangle = 1.5$ and $\langle r^2\rangle = 3$ exactly, but $\langle1/r\rangle = 0.9333$ against 1. With $\alpha = 1$, $\langle1/r\rangle = 1.000000000000$.

    **Lebedev.** The rules of degree 5, 11 and 17 (14, 50 and 110 points) integrate $|Y_{L0}|^2$ to $10^{-15}$ for $2L$ up to the degree. They fail at the next $L$, with errors 0.56, 0.16 and 0.086.

    **A two-centre integral on a one-centre grid.** The overlap of two hydrogen 1s functions 1 bohr apart, on a 40-point Laguerre × 302-point Lebedev grid centred on one atom, is 0.85816. The exact value is $e^{-R}(1 + R + R^2/3) = 0.85839$. The error, $2\times10^{-4}$, comes from the cusp of the second function, which the grid treats as an interior kink. This is why molecular grids are built atom by atom.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000), Sec. 9.6 (orthogonal polynomials and their recurrences, Eqs. 9.6.1–9.6.11; Gaussian quadrature, Eqs. 9.6.12–9.6.15; proof, Sec. 9.6.3), Sec. 9.11 (Rys quadrature for Coulomb integrals). The Newton–Cotes error terms, the Golub–Welsch algorithm and the Lebedev point counts are standard numerical analysis, not from HJO. Lebedev rules are taken from `scipy.integrate.lebedev_rule`. Molecular grid partitioning is described only qualitatively here (to be sourced with the DFT chapter). Calculations in `Claude outputs/part0_math_batchG.py`, sections A and B.
