The differential equations of quantum mechanics and the special functions that solve them.

## What this chapter is about

In Part 2, the Schrödinger equation for the oscillator, for the angular motion in a central potential, for the hydrogen atom and for a free particle in three dimensions each reduces to an ordinary differential equation with a named solution:

| Problem | Equation | Solutions |
|---|---|---|
| Harmonic oscillator | Hermite | $H_n(\xi)$ |
| Angular part of any central potential | Legendre | $P_l(x)$, $P_l^m(x)$ |
| Hydrogen radial equation | associated Laguerre | $L_{n-l-1}^{2l+1}(\rho)$ |
| Free particle in 3D, scattering | spherical Bessel | $j_l$, $n_l$, $h_l^{(1,2)}$ |

This chapter collects their properties in one place: Rodrigues formulas, generating functions, recursions, orthogonality relations and asymptotic forms. The physics notes can then use them without stopping.

## Why it matters

- **Quantization comes from the mathematics.** A series solution stays normalizable only if it terminates as a polynomial, and the termination condition is the energy quantization. Here the quantum numbers $n$ and $l$ appear as polynomial degrees.
- **Exact solutions are reference points.** Hydrogenic functions fix the shape of atomic orbitals and motivate Slater-type basis functions. Spherical harmonics underlie the angular part of every Gaussian basis set.
- **Conventions differ between books.** Laguerre normalization changed between Griffiths' 2nd and 3rd editions, and spherical Neumann functions carry different signs in different texts. Getting these wrong gives wrong normalization constants without any obvious symptom.

## Where it is used later

- [[harmonic-oscillator-analytic-solution|The oscillator]], [[central-potentials-and-spherical-harmonics|spherical harmonics]] and [[hydrogen-atom|the hydrogen atom]] in Part 2.
- [[partial-wave-analysis-and-phase-shifts|Partial waves]] in scattering, through the plane-wave expansion $e^{ikz}=\sum_l i^l(2l+1)j_l(kr)P_l(\cos\theta)$.
- [[radial-basis-functions-slater-and-gaussian|Slater and Gaussian radial functions]] and [[solid-harmonics-angular-basis|solid harmonics]] in Part 4, Chapter 4.

## The main ideas, in order

1. **One structure for each polynomial family.** Each family has a differential equation, a Rodrigues formula, a generating function, a three-term recursion, and orthogonality with a weight on an interval. Any one of these determines the others.
2. **Spherical Bessel functions.** Two kinds of solution, regular at the origin ($j_l$) and irregular ($n_l$). At large $r$ both become phase-shifted sinusoids divided by $r$. That phase shift is what scattering theory measures.

## How to read it

**Path.** [[classical-orthogonal-polynomials]] (Hermite, Legendre, Laguerre), then [[spherical-bessel-functions]].

**Needs.** Chapter 1 (orthonormal functions) and Chapter 2 (Fourier transforms).

**Leads to.** The harmonic oscillator, spherical harmonics and the hydrogen atom (Part 2, Chapters 2 and 4), and partial-wave scattering (Part 2, Chapter 10).

**Planned sections:** Ordinary differential equations (series solutions, Sturm-Liouville theory); Airy and hypergeometric functions; Partial differential equations.
