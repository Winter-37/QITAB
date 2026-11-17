The semiclassical (WKB) approximation: solutions of the one-dimensional Schrödinger equation when the potential varies slowly on the scale of the de Broglie wavelength.

## What this chapter is about

When $V(x)$ changes little over one wavelength, the wave function locally looks like a plane wave whose wavelength follows the classical momentum $p(x)=\sqrt{2m(E-V(x))}$:

$$
\psi(x)\approx\frac{C}{\sqrt{p(x)}}\exp\!\Big(\pm\frac{i}{\hbar}\int p(x)\,dx\Big).
$$

In classically forbidden regions the exponentials become real. The approximation fails at turning points, where $p\to 0$. The chapter shows how to join the two sides there using Airy functions, and draws out the two main results:

- **a quantization rule**, $\oint p\,dx=(n+\tfrac12)h$, for bound states;
- **a tunnelling probability**, $T\approx e^{-2\gamma}$, for barriers.

## Why it matters

- **No small parameter and no trial function are needed.** WKB complements perturbation theory and the variational principle. It is accurate when the quantum numbers are large or the motion is nearly classical, which is where the other methods are least convenient.
- **It explains where quantization comes from.** Bound states exist where an integer number of half-wavelengths, plus a phase from each turning point, fits between the turning points. The $\tfrac12$ in the oscillator's $(n+\tfrac12)\hbar\omega$ is that turning-point phase.
- **Tunnelling rates are exponential in the barrier action.** This one formula explains why α-decay half-lives range over many orders of magnitude (Gamow), and why proton and hydrogen-atom transfer reactions can have large tunnelling contributions.
- **It connects quantum and classical mechanics.** The phase is the classical action divided by $\hbar$, which is the same structure as the stationary-phase limit of the path integral (Chapter 6).

## Where it is used later

- Resonance widths and quasi-bound states in [[low-energy-scattering-and-resonances|low-energy scattering]] (Chapter 10).
- [[sudden-and-adiabatic-approximations|The adiabatic approximation]] (Chapter 11), the time-domain counterpart of a slowly varying potential.
- [[feynman-path-integral|The path integral]] (Chapter 6), whose classical limit is the WKB phase.

## The main ideas, in order

1. **The WKB wave function.** Write $\psi$ as amplitude times phase and drop the term in $\hbar^2$. The result is valid when the wavelength changes slowly, $|d\lambda/dx|\ll 1$.
2. **Turning points.** Linearize the potential, solve the Airy equation exactly, and match its asymptotic forms. This gives the connection formulas and the quantization rules for one and two smooth walls and for vertical walls.
3. **Tunnelling.** $T\approx e^{-2\gamma}$ with $\gamma=\hbar^{-1}\int|p|\,dx$ across the forbidden region, compared with exact barrier results, and applied to Gamow's theory of α decay.

## How to read it

**Path.** [[wkb-approximation]] derives the wave function and the validity condition. [[wkb-connection-formulas-and-quantization]] joins the solutions across turning points with Airy functions and obtains the quantization rules. [[wkb-tunneling-and-alpha-decay]] treats barrier penetration and Gamow's theory of alpha decay.

**Needs.** Stationary states and the one-dimensional model problems of Chapter 2 (square well, oscillator, scattering from a barrier); the radial equation of Chapter 4 for the hydrogen example.

**Leads to.** Resonance widths in Chapter 10 (Scattering Theory) use the same tunnelling argument. The adiabatic approximation of Chapter 11 ([[sudden-and-adiabatic-approximations]]) is the time-domain counterpart of the slowly varying assumption.

**Planned sections:** none at present.
