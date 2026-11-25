---
id: eigenfunction-expansions-and-generating-functions
title: Eigenfunction expansions and generating functions - generalized Fourier series, completeness, least-squares truncation, Legendre series, the Laplace expansion of 1/|r − r'|, the addition theorem, the Rayleigh plane-wave expansion, and Green's functions as eigenfunction sums
summary: The eigenfunctions of a Sturm–Liouville problem are a complete orthogonal basis. Any reasonable function expands in them with coefficients found by projection, generalizing Fourier series. Truncating after N terms gives the best least-squares approximation of that size, and the error falls faster the smoother the function. Generating functions package a whole family into one function of two variables. The Legendre one, (1 − 2xt + t²)^{−1/2}, gives the Laplace expansion 1/|r − r'| = Σ r<^l/r>^{l+1} P_l(cos γ). The addition theorem writes P_l(cos γ) through spherical harmonics, which separates the two electrons' coordinates in Coulomb integrals. The Rayleigh expansion writes a plane wave in spherical waves, the basis of partial-wave scattering. A Green's function is a sum over eigenfunctions divided by eigenvalue differences. Worked examples: |x| in Legendre polynomials, and numerical checks of the Laplace, addition-theorem and Rayleigh expansions.
status: in-progress
kind: theory
level: intermediate
tags: [eigenfunction-expansion, generalized-fourier-series, completeness-relation, bessel-inequality, legendre-series, generating-function, laplace-expansion, multipole-expansion, addition-theorem, spherical-harmonics, rayleigh-expansion, partial-waves, green-function, basis-set]
prerequisites: [sturm-liouville-theory, classical-orthogonal-polynomials, spherical-bessel-functions]
related: [fourier-series, multivariable-taylor-expansion, electric-and-magnetic-multipole-moments, born-approximation-and-lippmann-schwinger, orthonormal-functions-and-operators, neumann-series-and-operator-expansions]
key: laplace
order: 80
date: 2026-11-25
---

$\{y_n\}$ are the eigenfunctions of a self-adjoint Sturm–Liouville problem with weight $w$ ([[sturm-liouville-theory]]), $N_n = \langle y_n|y_n\rangle_w$. $r_< = \min(r, r')$, $r_> = \max(r, r')$, and $\gamma$ is the angle between $\mathbf r$ and $\mathbf r'$. Spherical harmonics are orthonormal on the sphere with the Condon–Shortley phase.

## Expansion in eigenfunctions

**The generalized Fourier series.** For square-integrable $f$ (Arfken Sec. 10.4):

$$
f(x) = \sum_nc_ny_n(x),\qquad c_n = \frac{\langle y_n|f\rangle_w}{N_n} = \frac1{N_n}\int_a^bw\,y_n^*f\,dx .
\label{expand}
$$

The coefficients come from projection, exactly as for Fourier series ([[fourier-series]]) and for components of a vector in an orthogonal basis ([[orthonormal-functions-and-operators]]).

**Completeness relation.** Substituting the coefficients back into the series,

$$
\sum_n\frac{y_n(x)\,y_n^*(x')}{N_n}\,w(x') = \delta(x - x') .
$$

This is the function-space form of $\sum_n|n\rangle\langle n| = 1$.

**Least squares and Bessel's inequality.** Among all combinations of $y_1,\dots,y_N$, the truncated series with the coefficients of Eq. [[#expand]] minimizes $\int w|f - f_N|^2$. Adding a term never changes the earlier coefficients. Bessel's inequality $\sum_n N_n|c_n|^2\le\int w|f|^2$ becomes Parseval's equality exactly when the set is complete.

**Convergence rate.** As for Fourier series, the smoother $f$ is, the faster $c_n$ decays. A kink gives algebraic decay. An analytic function gives exponential decay (for polynomial families, when it is analytic in an ellipse around the interval).

**Basis sets.** A basis-set calculation in quantum chemistry expands the wave function in a truncated set of functions. When the functions are not eigenfunctions of a simple operator, one solves the projected (Galerkin) problem, $\mathbf{Hc} = E\mathbf{Sc}$, instead of projecting $f$. The variational principle then plays the role of the least-squares property. The slow convergence of correlation energies with angular momentum is the eigenfunction-expansion symptom of the electron–electron cusp, a kink.

## Generating functions

**Definition.** A generating function $g(x, t) = \sum_nf_n(x)t^n$ packages a whole family into one function. Expanding $g$ in $t$ ([[taylor-and-maclaurin-expansions]]) gives the members. Differentiating $g$ in $t$ or $x$ gives the recurrence relations.

**The two most used** (Arfken Secs. 12.1 and 13.1):

$$
\frac1{\sqrt{1 - 2xt + t^2}} = \sum_{l=0}^\infty P_l(x)\,t^l\quad(|t| < 1),\qquad
e^{2xt - t^2} = \sum_{n=0}^\infty H_n(x)\frac{t^n}{n!} .
\label{genfun}
$$

The Legendre generating function is the binomial series of $(1 - u)^{-1/2}$ with $u = 2xt - t^2$, regrouped in powers of $t$.

## The Laplace expansion of 1/|r − r'|

**The expansion.** Write $|\mathbf r - \mathbf r'| = r_>\sqrt{1 - 2t\cos\gamma + t^2}$ with $t = r_</r_>$. Eq. [[#genfun]] then gives (Arfken Sec. 12.1)

$$
\frac1{|\mathbf r - \mathbf r'|} = \sum_{l=0}^\infty\frac{r_<^l}{r_>^{l+1}}P_l(\cos\gamma) .
\label{laplace}
$$

**Where it is used.**

- **Multipole expansions.** For $r > r'$ and a charge distribution at $\mathbf r'$, the $l$-th term is the $2^l$-pole potential. The first three terms are the Taylor expansion of [[multivariable-taylor-expansion]], and the full series is the multipole expansion of [[electric-and-magnetic-multipole-moments]].
- **Two-electron integrals over atoms.** With $r_<$ and $r_>$ the two electron distances, the radial factor does not separate, but the angular one does, after the addition theorem.

**The addition theorem.** For the angle $\gamma$ between directions $(\theta,\phi)$ and $(\theta',\phi')$ (Arfken Sec. 12.8):

$$
P_l(\cos\gamma) = \frac{4\pi}{2l + 1}\sum_{m=-l}^lY_{lm}^*(\theta',\phi')\,Y_{lm}(\theta,\phi) .
\label{addition}
$$

Inserted in Eq. [[#laplace]], it splits $1/r_{12}$ into products of functions of electron 1 and electron 2:

$$
\frac1{r_{12}} = \sum_{lm}\frac{4\pi}{2l + 1}\frac{r_<^l}{r_>^{l+1}}Y_{lm}^*(\hat{\mathbf r}_2)Y_{lm}(\hat{\mathbf r}_1).
$$

The angular integrals then reduce to Gaunt coefficients, integrals of three spherical harmonics (Arfken Sec. 12.9). These give the Slater–Condon parameters $F^k$, $G^k$ of atomic structure and the selection rules for which $l$ contribute.

## The Rayleigh plane-wave expansion

**The expansion.** A plane wave is a sum of spherical waves (Arfken Exercise 12.4.7):

$$
e^{ikr\cos\theta} = \sum_{l=0}^\infty(2l + 1)\,i^l\,j_l(kr)\,P_l(\cos\theta)
= 4\pi\sum_{lm}i^lj_l(kr)\,Y_{lm}^*(\hat{\mathbf k})Y_{lm}(\hat{\mathbf r}),
\label{rayleigh}
$$

with the spherical Bessel functions $j_l$ of [[spherical-bessel-functions]]. The second form uses the addition theorem.

**Partial waves.** In scattering from a central potential, each $l$ scatters independently. The cross section becomes a sum over phase shifts $\delta_l$. Because $j_l(kr)$ is small for $kr < l$, only $l\lesssim ka$ matter for a potential of range $a$ ([[born-approximation-and-lippmann-schwinger]]). In solid-state and molecular codes the same expansion turns plane-wave and Gaussian integrals into radial integrals.

## Green's functions as eigenfunction sums

**The expansion.** To solve $(\mathcal L + \lambda w)u = -wf$ with self-adjoint boundary conditions, expand both $u$ and $f$ in the $y_n$. Then each coefficient satisfies $(\lambda - \lambda_n)u_n = -f_n$, and (Arfken Sec. 10.5)

$$
u(x) = \int G(x, x')f(x')w(x')\,dx',\qquad G(x, x') = \sum_n\frac{y_n(x)\,y_n^*(x')}{N_n(\lambda_n - \lambda)} .
$$

**Meaning.** $G$ has poles at the eigenvalues. Near $\lambda = \lambda_n$ the response is dominated by one mode, which is resonance. With $\lambda\to E$ and $\mathcal L\to-\hat H$ this is the spectral representation of the resolvent, $(E - \hat H)^{-1} = \sum_n|n\rangle\langle n|/(E - E_n)$, and of every sum-over-states response function ([[neumann-series-and-operator-expansions]]).

## Worked examples

!!! example "Legendre series of |x|, and the three expansions checked (computed for this note)"
    **$|x|$ on $[-1, 1]$.** It is even, so only even $l$ appear. From Eq. [[#expand]] with $N_l = 2/(2l + 1)$: $c_0 = \tfrac12$, $c_2 = \tfrac58$, $c_4 = -\tfrac3{16}$, $c_6 = \tfrac{13}{128}$, $c_8 = -\tfrac{17}{256}$ (sympy, exact).

    | truncation $l_{\max}$ | max error | $\int(f - f_N)^2$ |
    |---:|---:|---:|
    | 2 | 0.1875 | $1.0\times10^{-2}$ |
    | 8 | 0.0673 | $5.0\times10^{-4}$ |
    | 40 | 0.0153 | $6.0\times10^{-6}$ |

    The largest error sits at the kink $x = 0$ and decays slowly, about as $1/l_{\max}$. The mean-square error falls much faster, as the least-squares property promises.

    **Laplace expansion, Eq. [[#laplace]].** For $r_< = 0.7$, $r_> = 1.9$, $\gamma = 1.1$ rad the exact value is 0.5878860921. Summing to $l = 2$, 5 and 20 gives 0.6005990, 0.5874439 and 0.5878860921. The error falls as $(r_</r_>)^l = 0.368^l$.

    **Addition theorem, Eq. [[#addition]].** For $l = 3$ and directions $(0.4, 1.0)$ and $(1.3, -0.6)$: $P_3(\cos\gamma) = -0.3205178534$, and $\frac{4\pi}7\sum_mY^*Y = -0.3205178534$.

    **Rayleigh expansion, Eq. [[#rayleigh]].** For $kr = 3.7$, $\cos\theta = 0.35$: $e^{ikr\cos\theta} = 0.2723132557 + 0.9622086524i$, and the sum over $l < 40$ gives the same digits. Terms beyond $l\approx kr + 10$ are negligible.

    **Generating functions, Eq. [[#genfun]].** The $t$-coefficients of $(1 - 2xt + t^2)^{-1/2}$ are $1$, $x$, $\tfrac32x^2 - \tfrac12$, $\tfrac52x^3 - \tfrac32x$, i.e. $P_0$ to $P_3$. Those of $e^{2xt - t^2}$ times $n!$ are $1$, $2x$, $4x^2 - 2$, $8x^3 - 12x$, i.e. $H_0$ to $H_3$.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 10.4 (completeness, Bessel's inequality), Sec. 10.5 (Green's function by eigenfunction expansion), Sec. 11.7 (spherical Bessel functions), Exercise 12.4.7 (the Rayleigh plane-wave expansion), Sec. 12.1 (Legendre generating function and the potential of a displaced charge), Sec. 12.8 (addition theorem), Sec. 12.9 (integrals of three $Y$'s), Sec. 13.1 (Hermite generating function). The basis-set and partial-wave remarks are general knowledge. Calculations in `Claude outputs/part0_math_batchE.py`, sections C and E.
