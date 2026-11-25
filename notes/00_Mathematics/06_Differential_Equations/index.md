Ordinary and partial differential equations, from first-order rate laws to the eigenvalue problems whose solutions are the special functions of quantum mechanics, and the expansions in those functions. The reference is Chapters 9–13 of Arfken and Weber, with Griffiths for the special functions.

## What this chapter is about

Every equation of motion and every eigenvalue equation in the notebook is a differential equation. The chapter goes from the general methods to the named solutions:

- **First-order equations:** separable, exact and linear equations, and integrating factors, with chemical rate laws as examples.
- **Second-order linear equations:** superposition, the Wronskian, constant coefficients and the damped, driven oscillator, particular solutions and Green's functions.
- **Partial differential equations:** the Laplace, Poisson, diffusion, wave and Schrödinger equations, and separation of variables, which reduces each of them to ODEs.
- **Series solutions:** the Frobenius method at regular singular points, and why a series must terminate.
- **Sturm–Liouville theory:** why the eigenfunctions of these ODEs are real, orthogonal and complete.
- **The special functions:**

  | problem | equation | solutions |
  |---|---|---|
  | harmonic oscillator | Hermite | $H_n(\xi)$ |
  | angular part of any central potential | Legendre | $P_l(x)$, $P_l^m(x)$ |
  | hydrogen radial equation | associated Laguerre | $L_{n-l-1}^{2l+1}(\rho)$ |
  | free particle in 3D, scattering | spherical Bessel | $j_l$, $n_l$, $h_l^{(1,2)}$ |

- **Eigenfunction expansions:** expansions in these functions, including the Laplace expansion of $1/r_{12}$ and the plane-wave expansion.

## Why it matters

- **Quantization comes from the mathematics.** A series solution stays normalizable only if it terminates as a polynomial, and the termination condition is the energy quantization. The quantum numbers $n$ and $l$ appear as polynomial degrees.
- **Hermitian operators come from boundary conditions.** Sturm–Liouville theory explains why Hamiltonians with the right boundary conditions have real eigenvalues and orthogonal, complete eigenfunctions.
- **Exact solutions are reference points.** Hydrogenic functions fix the shape of atomic orbitals and motivate Slater-type basis functions. Spherical harmonics underlie the angular part of every Gaussian basis set.
- **Two-electron integrals separate.** The Laplace expansion and the addition theorem split $1/r_{12}$ into products of one-electron functions.
- **Conventions differ between books.** Laguerre normalization changed between Griffiths' 2nd and 3rd editions, and spherical Neumann functions carry different signs in different texts. Getting these wrong gives wrong normalization constants without any obvious symptom.

## The main ideas, in order

1. **First-order ODEs** and existence and uniqueness.
2. **Second-order linear ODEs**, the oscillator, resonance and Green's functions.
3. **PDEs and separation of variables** in Cartesian, spherical and cylindrical coordinates.
4. **Frobenius series**, indicial equations, termination.
5. **Sturm–Liouville theory**: self-adjointness, real eigenvalues, orthogonality with weight, completeness, nodes.
6. **The classical orthogonal polynomials**: one structure for each family (differential equation, Rodrigues formula, generating function, recursion, orthogonality).
7. **Spherical Bessel functions**: regular and irregular solutions and their phase-shifted asymptotics.
8. **Eigenfunction expansions**, generating functions, the Laplace and Rayleigh expansions, Green's functions as eigenfunction sums.

## Where it is used later

- [[harmonic-oscillator-analytic-solution|The oscillator]], [[central-potentials-and-spherical-harmonics|spherical harmonics]] and [[hydrogen-atom|the hydrogen atom]] in Part 2.
- [[partial-wave-analysis-and-phase-shifts|Partial waves]] in scattering, through the plane-wave expansion $e^{ikz}=\sum_l i^l(2l+1)j_l(kr)P_l(\cos\theta)$.
- [[radial-basis-functions-slater-and-gaussian|Slater and Gaussian radial functions]] and [[solid-harmonics-angular-basis|solid harmonics]] in Part 4, Chapter 4.
- The Lorentz oscillator model of the permittivity in Part 1, Chapter 2.

## How to read it

**Path.**

1. [[first-order-differential-equations]]
2. [[second-order-linear-differential-equations]]
3. [[partial-differential-equations-and-separation-of-variables]]
4. [[series-solutions-and-the-frobenius-method]]
5. [[sturm-liouville-theory]]
6. [[classical-orthogonal-polynomials]] (Hermite, Legendre, Laguerre)
7. [[spherical-bessel-functions]]
8. [[eigenfunction-expansions-and-generating-functions]]

**Needs.**

- Chapter 1 (orthonormal functions, Hermitian operators);
- Chapter 2 (calculus);
- Chapter 3 (the Laplacian in curvilinear coordinates);
- Chapter 4 (power series, Fourier series and transforms);
- Chapter 5 (complex exponentials).

**Leads to.** The harmonic oscillator, spherical harmonics and the hydrogen atom (Part 2, Chapters 2 and 4); partial-wave scattering (Part 2, Chapter 10); Coulomb integrals and basis functions (Part 4, Chapter 4).

**Planned sections:** Hypergeometric and confluent hypergeometric functions; Bessel functions of integer order.
