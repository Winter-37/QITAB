Infinite series and the expansions built from them: when a series converges, how power and Taylor series represent functions, how periodic and non-periodic functions are written in sines, cosines and plane waves, how divergent asymptotic series are still useful, and how geometric and exponential series carry over to matrices and operators. The reference is Chapters 5, 14, 15 and 16 of Arfken and Weber. The table at the end lists every expansion used anywhere in the notebook and where each one is explained.

## What this chapter is about

An expansion writes something complicated as a sum of simple pieces: powers, sines and cosines, plane waves, polynomials, eigenfunctions, or products of operators. Three questions decide whether it can be trusted:

- **Does it converge?** And where: an interval, a disc, the whole plane?
- **How fast?** That decides how many terms a calculation needs.
- **What does truncation cost?** A remainder formula, an error bound, or for asymptotic series an optimal stopping point.

This chapter answers them for the expansions that matter most. Expansions in special functions (Legendre series, the Laplace expansion of $1/r_{12}$, plane waves in spherical waves) need the Sturm–Liouville theory of Chapter 6 and are explained there. Laurent series need complex analysis and are in Chapter 5.

## Why it matters

- **Most of physics is a truncated expansion.** The harmonic approximation is a second-order Taylor series. The dipole approximation is the first term of a multipole series. Perturbation theory is a power series in the coupling.
- **Convergence is a physical statement.** A Taylor series stops converging at the nearest complex singularity. Perturbation series in quantum chemistry are often only asymptotic. Fourier coefficients decay as fast as the function is smooth, which is why cusps make basis sets converge slowly.
- **Operator series are the algebra of quantum mechanics.** $(E - H)^{-1}$ as a Dyson series, $e^{\hat T}$ in coupled cluster, $e^{-iHt}$ and its Trotter splitting on quantum computers are all series of operators.

## The main ideas, in order

1. **Convergence of series.** Partial sums, the geometric and harmonic series, comparison, ratio, root and integral tests, alternating series, absolute and conditional convergence, uniform convergence.
2. **Power series.** The radius of convergence, term-by-term differentiation and integration, uniqueness, and singularities in the complex plane.
3. **Taylor and Maclaurin series.** Taylor's theorem with remainder, the standard series, the binomial series, the translation operator, expansion about a minimum.
4. **Taylor series in several variables.** Gradient, Hessian, Newton steps, normal coordinates, $1/|\mathbf r - \mathbf a|$.
5. **Fourier series.** Orthogonality, coefficients, convergence at jumps, the Gibbs phenomenon, Parseval.
6. **Fourier transforms** and the Dirac delta, as the limit of Fourier series for infinite period.
7. **Asymptotic expansions.** Optimal truncation, Stirling's series, Laplace's method, Euler–Maclaurin, Padé.
8. **Neumann and operator series.** $(1 - A)^{-1}$, resolvents, the Dyson equation and Born series, the exponential series.

## How to read it

**Path.**

1. [[sequences-series-and-convergence]]
2. [[power-series-and-radius-of-convergence]]
3. [[taylor-and-maclaurin-expansions]]
4. [[multivariable-taylor-expansion]]
5. [[fourier-series]]
6. [[fourier-transforms-and-the-dirac-delta]]
7. [[asymptotic-expansions]]
8. [[neumann-series-and-operator-expansions]]

**Needs.** Chapter 1 (matrices, functions of matrices) and Chapter 2 (limits, derivatives, integrals). Chapter 3 for the gradient in note 4.

**Leads to.** Complex analysis (Chapter 5), differential equations and eigenfunction expansions (Chapter 6), perturbation theory and scattering (Part 2), and response theory (Part 4, Chapters 15–17).

**Planned sections:** Bernoulli numbers and the Riemann zeta function; Infinite products.

## Every expansion in the notebook

What is expanded, in what, and where it is explained. "Mathematics" entries are in Part 0; the others apply an expansion to a physical problem.

| expansion | expands | in terms of | note |
|---|---|---|---|
| **Mathematics** | | | |
| geometric series | $1/(1 - r)$ | powers $r^n$ | [[sequences-series-and-convergence]] |
| power series | analytic functions | $(x - x_0)^n$ | [[power-series-and-radius-of-convergence]] |
| Taylor, Maclaurin | a smooth function near a point | derivatives times $(x - a)^n$ | [[taylor-and-maclaurin-expansions]] |
| binomial series | $(1 + x)^\alpha$, any $\alpha$ | $\binom\alpha nx^n$ | [[taylor-and-maclaurin-expansions]] |
| translation operator | $f(x + h)$ | $e^{h\,d/dx}$ | [[taylor-and-maclaurin-expansions]] |
| multivariable Taylor | $f(\mathbf x + \mathbf a)$ | gradient, Hessian, … | [[multivariable-taylor-expansion]] |
| Fourier series | a periodic function | $e^{inx}$ (or $\cos$, $\sin$) | [[fourier-series]] |
| Fourier transform | a function on the line | plane waves $e^{ikx}$ | [[fourier-transforms-and-the-dirac-delta]] |
| Laplace transform | a function on $[0,\infty)$ | decaying exponentials $e^{-st}$ | [[laplace-transform]] |
| exponential sum | $1/x$ (energy denominators) | $\sum_kw_ke^{-\alpha_kx}$ | [[laplace-transform]] |
| Gaussian quadrature | an integral | values at the zeros of orthogonal polynomials | [[gaussian-quadrature]] |
| Laurent series | a function around a singularity | positive and negative powers | [[laurent-series-singularities-and-residues]] |
| asymptotic series | $n!$, $\mathrm{erfc}\,x$, Laplace integrals | inverse powers | [[asymptotic-expansions]] |
| Euler–Maclaurin | a sum | integral plus Bernoulli corrections | [[asymptotic-expansions]] |
| Padé approximant | a power series | ratio of polynomials | [[asymptotic-expansions]] |
| Neumann series | $(1 - A)^{-1}$, integral equations | powers of $A$ | [[neumann-series-and-operator-expansions]] |
| Dyson equation, Born series | a resolvent $(E - H)^{-1}$ | powers of $G_0V$ | [[neumann-series-and-operator-expansions]] |
| exponential series | $e^{A}$ | $A^k/k!$ | [[neumann-series-and-operator-expansions]] |
| Baker–Campbell–Hausdorff | $e^{-B}Ae^{B}$, $\log(e^Ae^B)$ | nested commutators | [[baker-campbell-hausdorff]] |
| spectral decomposition | a normal matrix | projectors on eigenvectors | [[spectral-decomposition-and-normal-operators]] |
| completeness relation | identity, delta function | orthonormal basis functions | [[orthonormal-functions-and-operators]] |
| Schmidt decomposition | a bipartite state | product states | [[schmidt-decomposition-and-purification]] |
| Frobenius series | solutions of an ODE | $x^{s+k}$ | [[series-solutions-and-the-frobenius-method]] |
| eigenfunction expansion | a function on an interval | Sturm–Liouville eigenfunctions | [[eigenfunction-expansions-and-generating-functions]] |
| generating functions | a polynomial family | powers of $t$ | [[eigenfunction-expansions-and-generating-functions]] |
| Laplace expansion | $1/|\mathbf r - \mathbf r'|$ | $r_<^l/r_>^{l+1}\,P_l(\cos\gamma)$ | [[eigenfunction-expansions-and-generating-functions]] |
| addition theorem | $P_l(\cos\gamma)$ | $Y_{lm}^*Y_{lm}$ | [[eigenfunction-expansions-and-generating-functions]] |
| Rayleigh expansion | a plane wave | $j_l(kr)P_l(\cos\theta)$ | [[eigenfunction-expansions-and-generating-functions]] |
| **Physics and chemistry** | | | |
| multipole expansion | potential of a charge distribution | $1/r^{l+1}$ times moments | [[electric-and-magnetic-multipole-moments]] |
| multipolar interaction series | coupling to a field | dipole, quadrupole, magnetic dipole, … | [[multipolar-gauge-and-the-electric-dipole-approximation]] |
| field expansion of the energy | $E(\mathbf F)$ | $\mu$, $\alpha$, $\beta$, $\gamma$ | [[polarizabilities-and-dispersion-coefficients]] |
| sum over states | response functions | excited states, poles | [[exact-state-response-functions]] |
| normal modes | a potential surface near a minimum | harmonic oscillators | [[harmonic-vibrational-analysis]] |
| Rayleigh–Schrödinger series | eigenvalues and eigenvectors | powers of a perturbation | [[rayleigh-schrodinger-perturbation-theory]] |
| Møller–Plesset (MBPT) | the correlation energy | orders in the fluctuation potential | [[moller-plesset-and-coupled-cluster-perturbation-theory]] |
| time-dependent Dyson series | the evolution operator | time-ordered powers of $V$ | [[interaction-picture-and-dyson-series]] |
| partial waves | a scattering wave function | angular momenta $l$ | [[partial-wave-analysis-and-phase-shifts]] |
| WKB | a wave function | powers of $\hbar$ | [[wkb-approximation]] |
| basis-set expansion | molecular orbitals | Gaussian or Slater functions | [[gaussian-basis-sets-and-convergence]] |
| configuration interaction | the many-electron wave function | determinants | [[full-ci]] |
| exponential cluster ansatz | the many-electron wave function | $e^{\hat T}$, excitation operators | [[coupled-cluster-hierarchy-and-size-extensivity]] |
| linked-cluster theorem | the energy of a perturbation series | connected diagrams | [[linked-cluster-theorem]] |
| Pauli strings | a qubit Hamiltonian | tensor products of Pauli matrices | [[jordan-wigner-mapping]] |
| Trotter–Suzuki | $e^{-i(A + B)t}$ | products of $e^{-iAt/n}$, $e^{-iBt/n}$ | [[trotter-error-in-qpe-energies]] |
