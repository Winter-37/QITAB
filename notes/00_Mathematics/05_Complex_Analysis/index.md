Functions of a complex variable: complex numbers and their polar form, analytic functions and Cauchy's theorem, and the Laurent series and residues that turn real integrals and response functions into sums over poles. The reference is Chapters 6–7 of Arfken and Weber.

## What this chapter is about

Quantum mechanics is written in complex numbers, and many real problems are easier in the complex plane:

- **Complex numbers.** Phases $e^{i\theta}$, roots of unity, and the logarithm with its branch cut.
- **Analytic functions.** Requiring a derivative independent of direction (the Cauchy–Riemann equations) is so strong that an analytic function is fixed by its boundary values (Cauchy's formula). It is infinitely differentiable and equal to its Taylor series.
- **Laurent series and residues.** Around a singularity a function expands in positive and negative powers. The coefficient of $(z - z_0)^{-1}$, the residue, is all that a closed contour integral sees.

## Why it matters

- **Radii of convergence.** A Taylor series converges up to the nearest complex singularity, even when the function is smooth on the real line. This governs the convergence of perturbation series.
- **Real integrals.** Fourier-type integrals, rational integrals and principal values are evaluated by closing contours and summing residues.
- **Response functions.** Response functions are analytic in the upper half frequency plane because the response is causal. Their poles are excitation energies and their residues transition strengths. The Kramers–Kronig relations and $1/(x\mp i\eta)\to P(1/x)\pm i\pi\delta(x)$ follow from that analyticity.
- **Green's functions.** Their poles in the complex energy plane are the quasiparticle energies.

## The main ideas, in order

1. **Complex numbers.** Algebra, modulus and argument, Euler's formula, de Moivre's theorem, roots, the multivalued logarithm and principal branches.
2. **Analytic functions.** Cauchy–Riemann equations, harmonic functions, contour integrals, Cauchy's integral theorem and formula, Liouville's theorem, analytic continuation.
3. **Laurent series and residues.** The classification of singularities, the residue theorem, real integrals, Jordan's lemma, principal values, Sokhotski–Plemelj.
4. **The Laplace transform.** Transforms of derivatives and shifts, linear ODEs and rate equations, convolution, inversion by the Bromwich integral and residues, exponential sums for $1/x$ (Laplace-transformed MP2).

## How to read it

**Path.**

1. [[complex-numbers]]
2. [[analytic-functions-and-cauchy-theorem]]
3. [[laurent-series-singularities-and-residues]]
4. [[laplace-transform]]

**Needs.** Chapter 2 (calculus), Chapter 3 (Stokes's theorem in the plane, for the proof of Cauchy's theorem), Chapter 4 (power and Taylor series).

**Leads to.**

- Second-order ODEs with oscillatory solutions (Chapter 6).
- Kramers–Kronig relations and dispersion (Part 1, Chapter 2).
- Response functions and Green's functions (Part 4, Chapter 17).
- Scattering theory (Part 2, Chapter 10).
- Rate equations and their solution (Part 3); reduced-scaling MP2 (Part 4, Chapter 10).

**Planned sections:** Conformal mapping; The method of steepest descents; Analytic continuation and the Gamma function in the complex plane.
