---
id: stationary-points-and-reaction-paths
title: Stationary points, transition states and the intrinsic reaction coordinate
summary: The potential energy surface U(q) of an N-atom molecule has 3N−6 coordinates. Its stationary points are classified by the number of negative Hessian eigenvalues - minima (reactants, products, intermediates, conformers), first-order saddle points (transition states, one imaginary frequency) and higher-order saddles. The intrinsic reaction coordinate is the steepest-descent path from a transition state in mass-weighted Cartesians. Worked example: ammonia inversion at HF/6-31G* - planar saddle (974i cm⁻¹), pyramidal minimum, classical barrier 2276 cm⁻¹ (1856 cm⁻¹ with ZPE), and a computed IRC that ends in the two mirror-image minima.
status: in-progress
kind: theory
level: intermediate
tags: [potential-energy-surface, transition-state, saddle-point, hessian-index, intrinsic-reaction-coordinate, reaction-path, conformers]
prerequisites: [born-oppenheimer-approximation, geometry-optimization, harmonic-vibrational-analysis]
related: [zero-point-energy-and-thermochemistry, geometry-error-of-an-approximate-surface, diatomic-vibration-and-anharmonicity, sudden-and-adiabatic-approximations]
order: 10
date: 2026-11-17
---

## The surface

The electronic energy $U$ (including nuclear repulsion) of a nonlinear molecule with $N$ nuclei depends on $3N - 6$ internal coordinates $q_1,\dots,q_{3N-6}$; translations and rotations leave it unchanged ($3N - 5$ coordinates for a linear molecule, one, $R$, for a diatomic). $U(\mathbf q)$ is the **potential energy surface** (PES) for nuclear motion. One electronic-structure calculation gives one point (a single-point calculation). Mapping a full surface with ten points per coordinate needs $10^{3N-6}$ calculations, $10^3$ for a triatomic and $10^9$ for a five-atom system, so in practice one locates its important features instead.

## Stationary points and their character

A **stationary point** has zero gradient, $\partial U/\partial q_\alpha = 0$ for all $\alpha$. Its character is fixed by the eigenvalues of the Hessian $\partial^2U/\partial q_\alpha\partial q_\beta$ there, equivalently by the harmonic frequencies ([[harmonic-vibrational-analysis]]):

| Hessian eigenvalues | Frequencies | Stationary point | Chemical meaning |
|---|---|---|---|
| all positive | all real | local minimum | reactant, product, intermediate, conformer |
| exactly one negative | one imaginary | first-order saddle point | transition state |
| $n\ge2$ negative | $n$ imaginary | $n$th-order saddle point | not a transition state |

- **Minima.** The lowest minimum is the global minimum. Flexible molecules have many local minima (conformers); butane has the anti global minimum and two mirror-image gauche minima along the CCCC dihedral, and a polypeptide with $2n$ free dihedrals has of the order of $3^{2n}$ (the multiple-minima problem). A **reaction intermediate** is a minimum: a product of one elementary step and a reactant of the next.
- **Transition states.** A first-order saddle point is a maximum along one direction and a minimum along all others. The normal mode of the imaginary frequency, the **transition vector**, points (to first order) toward the reactant and product it connects.
- **Optimizers do not know the difference.** Newton-type methods converge to the nearest stationary point of whatever character ([[geometry-optimization]]). Starting planar NH₃ in a symmetry-preserving optimization returns the planar saddle point. A frequency calculation at every optimized structure is the only check. Levine notes that structures reported in the literature as minima are sometimes saddle points.

## Reaction paths

**Minimum-energy path and its coordinate dependence.** The location of a saddle point does not depend on the coordinates used, but the "steepest-descent path" does: steepest descent depends on the metric, and bond lengths, angles or Cartesians define different metrics.

**Intrinsic reaction coordinate (IRC).** The standard choice is the steepest-descent path from the transition state in **mass-weighted Cartesian coordinates** $\sqrt{m_a}\,x_a$, $\sqrt{m_a}\,y_a$, $\sqrt{m_a}\,z_a$. It is the path a classical particle would follow sliding downhill with infinitesimal velocity. Starting along the transition vector in either direction, the IRC is the solution of

$$
\frac{\mathrm d\mathbf q_{\text{mw}}}{\mathrm ds} = -\frac{\mathbf g_{\text{mw}}}{|\mathbf g_{\text{mw}}|},\qquad (\mathbf g_{\text{mw}})_i = \frac{1}{\sqrt{m_i}}\frac{\partial U}{\partial X_i},
$$

with $s$ the arc length in mass-weighted space. It is not a classical trajectory, since real molecules carry kinetic energy in all modes, but it is the reference path for reaction-path Hamiltonians and variational transition-state theory.

**Rates.** The barrier height and the frequencies at the minimum and the saddle point are what Eyring's transition-state theory needs for a rough rate constant; tunnelling and recrossing corrections need the shape of the surface along and around the IRC. The theory itself belongs to Chapter 8 (planned). The measured Arrhenius activation energy is not identical to the classical barrier.

**Practical search strategies** (Levine Sec. 16.14): start a saddle-point optimizer from a guessed structure with an accurately computed initial Hessian, so that the negative-curvature direction is known; if that fails, generate the guess by interpolating between reactant and product structures (synchronous transit). Then run an IRC in both directions to confirm which minima the saddle connects, and look for lower saddles between the same minima.

## Worked example

!!! example "Ammonia inversion at HF/6-31G*"
    All structures optimized with PySCF and geomeTRIC (Cartesian $d$), analytic Hessians.

    | Structure | $U$ ($E_h$) | $r$(NH) (Å) | geometry | wavenumbers (cm$^{-1}$) |
    |---|---:|---:|---|---|
    | planar ($D_{3h}$) | −56.173 985 | 0.9884 | HNH = 120° | **974 i**, 1733.5 (×2), 3835.1, 4049.2 (×2) |
    | pyramidal ($C_{3v}$) | −56.184 356 | 1.0025 | HNH = 107.18° | 1208.8, 1849.3 (×2), 3689.1, 3822.1 (×2) |

    - **Character.** The planar structure has exactly one imaginary frequency: a transition state. Levine reports the same planar stationary point (0.99 Å, 120°) from Gaussian 09 when the optimization starts planar. The pyramidal minimum agrees with Levine's HF/6-31G* values (107°, 1.00 Å).
    - **Barrier.** Classical barrier $U_{\text{TS}} - U_{\min} = 2276$ cm$^{-1}$ = 6.51 kcal/mol. Adding harmonic zero-point energies (real modes only at the TS: 7700 cm$^{-1}$; minimum 8120 cm$^{-1}$) lowers it to 1856 cm$^{-1}$. In a light-atom inversion like this one, tunnelling through the barrier is important, so neither number is the whole story.
    - **Transition vector.** The lowest eigenvalue of the mass-weighted Hessian is $-0.0359\,E_h\,a_0^{-2}\,\mathrm u^{-1}$; the eigenvector moves N and the three H atoms along the $C_3$ axis only, in opposite directions, with Cartesian displacements in the ratio 0.216 : 1 (N : each H), so that the centre of mass stays fixed ($14.007\times0.216\approx3\times1.008$). This is the umbrella motion.
    - **IRC.** Steepest descent in mass-weighted Cartesians, first step 0.05 $a_0\,\mathrm u^{1/2}$ along $\pm$ the transition vector, later steps halved whenever the energy would rise:

    | $s$ ($a_0\,\mathrm u^{1/2}$) | 0 | 0.15 | 0.40 | 0.65 | 0.90 | 1.14 |
    |---|---:|---:|---:|---:|---:|---:|
    | $U - U_{\text{TS}}$ (cm$^{-1}$) | −9.8 | −106.7 | −596.4 | −1345.6 | −2026.5 | −2276.0 |

    The first point lies $\tfrac12\lambda s^2 = -9.85$ cm$^{-1}$ below the saddle, as the quadratic model predicts. Both branches reach $U_{\min}$ to 0.1 cm$^{-1}$ with the H plane 0.370 Å on opposite sides of N: the saddle connects the two mirror-image pyramids, as it must.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 15.10, pp. 480-490 (PES dimensionality, conformers of butane, multiple minima, saddle points found by optimizers, the planar NH₃ example, HF/6-31G* NH₃ geometry); Sec. 16.14, pp. 591-594 (stationary-point classification, transition states, reaction intermediates, IRC in mass-weighted coordinates, coordinate dependence of the minimum-energy path, transition-state search strategies, activation energy versus barrier). Calculations in `part3_batchA.py`, section E.
