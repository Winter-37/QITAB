---
id: complex-numbers
title: Complex numbers - algebra, the complex plane, modulus and argument, Euler's formula, de Moivre's theorem, roots of unity, and the multivalued logarithm and powers
summary: A complex number z = x + iy with i² = −1 is a point in the plane. It has a conjugate z* = x − iy, a modulus |z| = (zz*)^{1/2} and an argument arg z. Euler's formula e^{iθ} = cos θ + i sin θ gives the polar form z = re^{iθ}, in which multiplication multiplies moduli and adds arguments. De Moivre's theorem turns powers into multiple-angle formulas, and the n-th roots of a number lie on a regular polygon. Because the argument is defined only up to 2π, the logarithm and non-integer powers are multivalued. A principal branch with a cut along the negative real axis makes them single-valued, at the price of identities like Log(z₁z₂) = Log z₁ + Log z₂ failing across the cut. Worked examples: polar form, roots of unity, iⁱ = e^{−π/2}, and what happens on either side of a branch cut.
status: in-progress
kind: theory
level: introductory
tags: [complex-number, complex-conjugate, modulus, argument, polar-form, euler-formula, de-moivre, roots-of-unity, complex-logarithm, branch-cut, principal-value, hyperbolic-functions]
prerequisites: [functions, taylor-and-maclaurin-expansions]
related: [analytic-functions-and-cauchy-theorem, laurent-series-singularities-and-residues, fourier-series, unitary-matrices-exponential-logarithm]
key: euler
order: 10
date: 2026-11-25
---

$z = x + iy$ with $x = \mathrm{Re}\,z$, $y = \mathrm{Im}\,z$ real. The conjugate is written $z^*$ (physics) rather than $\bar z$. $\mathrm{Arg}$ and $\mathrm{Log}$ denote principal values.

## Algebra

**Definition.** Complex numbers are pairs $(x, y)$ with the product $(x_1 + iy_1)(x_2 + iy_2) = (x_1x_2 - y_1y_2) + i(x_1y_2 + y_1x_2)$, so that $i^2 = -1$ (Arfken Sec. 6.1). They form a field that contains the reals ($y = 0$). Unlike the reals, it is algebraically closed: every polynomial of degree $n$ has $n$ complex roots ([[functions]]).

**Conjugate and modulus.**

$$
z^* = x - iy,\qquad |z| = \sqrt{zz^*} = \sqrt{x^2 + y^2},\qquad \frac1z = \frac{z^*}{|z|^2}.
$$

- **Real and imaginary parts.** $\mathrm{Re}\,z = (z + z^*)/2$ and $\mathrm{Im}\,z = (z - z^*)/2i$.
- **Conjugation.** It respects sums and products: $(z_1z_2)^* = z_1^*z_2^*$.
- **Modulus.** It is multiplicative, $|z_1z_2| = |z_1||z_2|$, and satisfies the triangle inequality $|z_1 + z_2|\le|z_1| + |z_2|$.

In quantum mechanics $|\psi|^2 = \psi^*\psi$ is a probability density; amplitudes are complex, probabilities real.

## The complex plane and polar form

**The plane.** The Argand diagram plots $z$ at $(x, y)$. Addition is vector addition. In polar coordinates, $x = r\cos\theta$ and $y = r\sin\theta$ with $r = |z|$ and $\theta = \arg z$.

**Euler's formula.** Compare the Maclaurin series of $e^{i\theta}$, $\cos\theta$ and $\sin\theta$ ([[taylor-and-maclaurin-expansions]]). The even powers of $i\theta$ give the cosine and the odd powers $i$ times the sine:

$$
e^{i\theta} = \cos\theta + i\sin\theta,\qquad z = re^{i\theta} .
\label{euler}
$$

At $\theta = \pi$ it gives $e^{i\pi} + 1 = 0$.

**Products and quotients.** In polar form, $z_1z_2 = r_1r_2e^{i(\theta_1 + \theta_2)}$ and $z_1/z_2 = (r_1/r_2)e^{i(\theta_1 - \theta_2)}$. Multiplying by $e^{i\alpha}$ is a rotation by $\alpha$, and $|e^{i\alpha}| = 1$. Phase factors therefore do not change probabilities, and a global phase of a quantum state is unobservable.

**The argument.** $\arg z$ is defined only up to multiples of $2\pi$. The principal value $\mathrm{Arg}\,z\in(-\pi,\pi]$ is computed with the two-argument arctangent, $\mathrm{atan2}(y, x)$, not $\arctan(y/x)$, which loses the quadrant.

**Trigonometric and hyperbolic functions.** From Eq. [[#euler]]: $\cos\theta = \frac12(e^{i\theta} + e^{-i\theta})$ and $\sin\theta = \frac1{2i}(e^{i\theta} - e^{-i\theta})$. These definitions extend to complex arguments, with $\cos(iy) = \cosh y$ and $\sin(iy) = i\sinh y$. So $\sin z$ and $\cos z$ are unbounded off the real axis: $|\sin(1 + 2i)| = 3.72$.

## Powers and roots

**De Moivre's theorem.** $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$ for integer $n$. Expanding the left side binomially and comparing real and imaginary parts gives multiple-angle formulas, for example $\cos3\theta = 4\cos^3\theta - 3\cos\theta$.

**Roots.** The equation $w^n = z = re^{i\theta}$ has exactly $n$ solutions:

$$
w_k = r^{1/n}e^{i(\theta + 2\pi k)/n},\qquad k = 0, 1,\dots,n - 1 .
$$

They are the vertices of a regular $n$-gon of radius $r^{1/n}$.

**Roots of unity.** $\omega_k = e^{2\pi ik/n}$. They sum to zero for $n > 1$ (a geometric series), and their product is $(-1)^{n+1}$. They are the eigenvalues of a cyclic shift. They are the kernel of the discrete Fourier transform ([[fourier-transforms-and-the-dirac-delta]]) and the Bloch phases of a ring of $n$ sites, as in Hückel theory of cyclic polyenes.

## Logarithm and general powers

**The logarithm is multivalued.** Solving $e^w = z$ with $z = re^{i\theta}$ gives $w = \ln r + i(\theta + 2\pi k)$ for every integer $k$. The **principal logarithm** takes $\mathrm{Arg}\,z\in(-\pi,\pi]$:

$$
\mathrm{Log}\,z = \ln|z| + i\,\mathrm{Arg}\,z .
$$

It is discontinuous across the negative real axis, the **branch cut**. Arfken Sec. 6.6 treats branch points and cuts with Riemann surfaces.

**General powers.** $z^a = e^{a\log z}$, multivalued unless $a$ is an integer. With the principal branch:

- $i^i = e^{i\,\mathrm{Log}\,i} = e^{i\cdot i\pi/2} = e^{-\pi/2} = 0.2079$, a real number;
- $\sqrt z$ jumps sign across the cut.

**Identities that fail.** Familiar identities can fail for principal values: $\mathrm{Log}(z_1z_2) = \mathrm{Log}\,z_1 + \mathrm{Log}\,z_2$ holds only up to a multiple of $2\pi i$. Numerical codes that take logarithms of complex determinants or overlaps (phases of wave functions, Berry phases, the logarithm of a unitary matrix in [[unitary-matrices-exponential-logarithm]]) must track the branch explicitly.

## Worked examples

!!! example "Polar form, roots and branches (computed for this note)"
    **Polar form.** $z = 3 - 4i$: $|z| = 5$, $\mathrm{Arg}\,z = -0.927295$ rad, $1/z = z^*/25 = 0.12 + 0.16i$, $zz^* = 25$.

    **De Moivre.** At $\theta = 0.3$: $(\cos\theta + i\sin\theta)^5 = 0.0707372 + 0.9974950i$, equal to $\cos1.5 + i\sin1.5$. sympy confirms $\mathrm{Re}(\cos t + i\sin t)^3 = 4\cos^3t - 3\cos t$.

    **Roots.**

    - The fifth roots of unity sum to 0 and multiply to 1, which is $(-1)^{5+1}$.
    - The cube roots of $-8 = 8e^{i\pi}$ are $2e^{i\pi/3}$, $2e^{i\pi}$ and $2e^{5i\pi/3}$, i.e. $1 + 1.732051i$, $-2$ and $1 - 1.732051i$.

    **Branches.**

    - $i^i = 0.20787958 = e^{-\pi/2}$.
    - $\mathrm{Log}(-1) = i\pi$ and $\mathrm{Log}(-e) = 1 + i\pi$.
    - For $z_1 = z_2 = -1 + 0.1i$: $\mathrm{Log}(z_1z_2) = 0.00995 - 0.19934i$ but $2\,\mathrm{Log}\,z_1 = 0.00995 + 6.08385i$. They differ by $2\pi i$, because $z_1^2$ lands on the other side of the cut.
    - Just above and below the cut, $\sqrt{-4 \pm 10^{-12}i} = \pm2i$.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 6.1 (complex algebra: polar form, Euler's formula, de Moivre's theorem, roots, the logarithm and complex powers, trigonometric and hyperbolic functions), Sec. 6.6 (branch points and cuts). The Hückel and numerical-branch remarks are general knowledge. Calculations in `Claude outputs/part0_math_batchE.py`, section D.
