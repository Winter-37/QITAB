Scattering in three dimensions: how a beam of particles is deflected by a localized potential, and how the measured cross sections follow from the Schrödinger equation.

## What this chapter is about

In a bound-state problem the energy is the unknown and comes out discrete. In scattering the experiment fixes the energy: a particle arrives from far away with momentum $\hbar k$, interacts with a potential of finite range, and leaves in some direction. The unknown is *where it goes*. All of that information sits in one function, the scattering amplitude $f(\theta)$. It is the coefficient of the outgoing spherical wave far from the target,

$$
\psi(\mathbf r) \;\xrightarrow{\;r\to\infty\;}\; A\left[e^{ikz} + f(\theta)\,\frac{e^{ikr}}{r}\right],
\qquad
\frac{d\sigma}{d\Omega} = |f(\theta)|^2 .
$$

The chapter is about computing $f$ from $V$. There are two routes: an exact one for central potentials (partial waves), and an approximate one valid for any potential when the interaction is weak (the Born approximation).

## Why it matters

- **Scattering is how interactions are measured.** The nucleus was discovered through the angular distribution of scattered α particles. Much of what is known about interatomic and nuclear forces comes from cross sections, not spectra.
- **It is the other half of the spectrum.** A Hamiltonian with bound states usually also has a continuum above them. Molecules have one above the ionization threshold. Resonances are states that sit in that continuum for a finite time, and their widths are lifetimes.
- **Its tools reappear in many-body theory.** Scattering is first rewritten with the outgoing Green's function $(E-\hat H_0+i\epsilon)^{-1}$. The result is an integral equation, the Lippmann–Schwinger equation $|\psi\rangle = |\phi\rangle + \hat G_0^{(+)}\hat V|\psi\rangle$. It has the same structure as the Dyson equation for the many-electron Green's function (Part 4, Chapter 17), and iterating it (the Born series) is perturbation theory in $\hat V$.

## Where it shows up for a chemist

- **Diffraction.** In the first Born approximation the amplitude is the Fourier transform of the potential at the momentum transfer $\mathbf q = \mathbf k' - \mathbf k$. This is the reason electron and X-ray diffraction patterns encode the spatial distribution of the scatterer.
- **Low-energy collisions.** When the wavelength is much longer than the range of the potential, a single number, the scattering length, fixes the cross section. Its sign and size reveal whether a shallow bound state exists.
- **Resonances and decay.** The Breit–Wigner line shape, the golden-rule width of Chapter 11 and the WKB tunnelling rate of Chapter 9 are three descriptions of the same physics: a quasi-bound state leaking into a continuum.

## The main ideas, in order

1. **Boundary conditions define the problem.** Choose an incident plane wave plus an outgoing spherical wave. Then $|f|^2$ is the measured cross section.
2. **Partial waves.** For a central potential each angular momentum $l$ scatters independently. Conservation of probability lets each one change only by a phase, $\delta_l$. This gives exact formulas for $f$ and $\sigma$, the unitarity bound, and the optical theorem.
3. **Integral equation and Born approximation.** Replacing the unknown $\psi$ inside the integral by the incident wave gives the first Born amplitude. This works when the potential is weak compared with the kinetic energy, and is tested here against exact phase shifts.
4. **Low energy and resonances.** As $k\to 0$ only the $s$ wave survives. Near a quasi-bound state, a phase shift rises rapidly through $\pi/2$, giving a peak of width $\Gamma$ and lifetime $\hbar/\Gamma$.

## How to read it

**Path.** [[scattering-cross-sections-and-amplitude]] sets up cross sections and the scattering amplitude. [[partial-wave-analysis-and-phase-shifts]] gives the exact solution for central potentials in terms of phase shifts, with unitarity and the optical theorem. [[born-approximation-and-lippmann-schwinger]] gives the integral equation, the Born approximation and its range of validity. [[low-energy-scattering-and-resonances]] treats the scattering length, the link to bound states, and resonances.

**Needs.** Chapter 4 (central potentials, spherical harmonics, angular momentum). One-dimensional scattering and the finite well from Chapter 2. The single-particle Green's function from Chapter 8. Spherical Bessel functions (Part 0, Chapter 3: [[spherical-bessel-functions|spherical Bessel functions]]). Chapter 9 (WKB) supplies the tunnelling picture of resonance widths.

**Leads to.** The golden rule of Chapter 11 ([[fermi-golden-rule-and-decay-width|golden rule]]) gives the Born cross section by another route. Green's functions and propagators return in Part 4, Chapter 17.

**Planned sections:** identical-particle scattering; the eikonal approximation; Coulomb scattering treated exactly.
