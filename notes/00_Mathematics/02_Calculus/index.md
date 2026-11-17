Calculus beyond the first course: the integral transform and the generalized function that quantum mechanics uses everywhere.

## What this chapter is about

The Fourier transform writes a function as a superposition of plane waves $e^{ikx}$. The Dirac delta $\delta(x)$ is the idealized spike that picks out a single point under an integral. Neither is optional in quantum mechanics:

- plane waves are the momentum eigenstates, so the momentum-space wave function is the Fourier transform of the position-space one;
- the delta function is how completeness and continuum normalization are written.

## Why it matters

- **Position and momentum are Fourier partners.** With $p=\hbar k$, going from $\Psi(x)$ to $\Phi(p)$ is a Fourier transform. The norm is preserved (Plancherel's theorem), so it is a unitary change of representation.
- **The uncertainty principle starts here.** Any function and its transform satisfy $\sigma_x\sigma_k\ge\tfrac12$, with equality for Gaussians. This holds before any physics is added.
- **Continuum states need the delta function.** Plane waves cannot be normalized to one. They are normalized as $\langle k|k'\rangle=\delta(k-k')$, and completeness reads $\int |k\rangle\langle k|\,dk = 1$.
- **Convolution becomes multiplication.** Integrals of the form $\int f(x-y)g(y)\,dy$ become products of transforms. This is how Coulomb and Green's-function integrals are simplified.

## Where it is used later

- [[free-particle-and-wave-packets|Wave packets]], the [[delta-function-potential|delta-function potential]] and the [[position-momentum-and-energy-representations|momentum representation]] in Part 2.
- [[born-approximation-and-lippmann-schwinger|The Born approximation]]: the scattering amplitude is the Fourier transform of the potential.
- The discrete Fourier transform, the classical counterpart of the quantum Fourier transform in Part 5.

## The main ideas, in order

1. **The transform pair** in Griffiths' symmetric convention, $F(k)=(2\pi)^{-1/2}\int f(x)e^{-ikx}\,dx$, and Plancherel's theorem.
2. **Worked transforms.** A Gaussian transforms into a Gaussian and a box into a sinc. In both, a narrow function has a broad transform.
3. **The delta function** as the limit of nascent functions, with the rules for $\delta(cx)$ and $\delta(g(x))$ and its role in completeness.
4. **The convolution theorem.**
5. **The discrete Fourier transform** and its sign conventions. Nielsen–Chuang and NumPy use opposite signs.

## How to read it

**Path.** [[fourier-transforms-and-the-dirac-delta]].

**Needs.** Chapter 1 (Dirac notation, orthonormal functions).

**Leads to.** Free particles and wave packets, momentum space and the delta-function potential (Part 2, Chapters 2 and 3); the quantum Fourier transform (Part 5).

**Planned sections:** Multivariable calculus; Vector calculus.
