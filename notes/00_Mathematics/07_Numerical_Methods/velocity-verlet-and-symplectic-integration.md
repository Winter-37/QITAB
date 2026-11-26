---
id: velocity-verlet-and-symplectic-integration
title: Velocity Verlet and symplectic integration - derivation, time reversibility, symplecticity and the shadow Hamiltonian, bounded energy error, the time-step limit, and why imperfect forces make ab initio MD drift
summary: Velocity Verlet advances positions and momenta with one force evaluation per step: a half kick, a drift, a new force, a second half kick. It is second order, explicit, and exactly time reversible. It is also symplectic: it preserves phase-space volume. Its numerical trajectory therefore conserves a slightly modified (shadow) Hamiltonian H + O(h²), so the true energy oscillates within a bounded band instead of drifting, over very long times. That is what makes it the integrator of molecular dynamics, where RK4 would bleed energy steadily. For a vibration of angular frequency ω the method is unstable for ωh ≥ 2, and accuracy needs ωh well below that: about 0.5–1 fs for X–H stretches. In Born–Oppenheimer ab initio MD the forces carry errors from incomplete SCF convergence and from non-reversible wave-function guesses. Those errors break the structure, and the conserved energy then drifts at a rate set by the convergence threshold (Marx and Hutter's Table 1). Worked examples: the O(h²) energy band, an exactly conserved shadow energy, reversibility, the stability limit, a Morse H₂ bond at several time steps, and the energy random walk caused by noisy forces.
status: in-progress
kind: theory
level: intermediate
tags: [velocity-verlet, verlet-algorithm, symplectic-integrator, time-reversibility, shadow-hamiltonian, energy-conservation, time-step, molecular-dynamics, born-oppenheimer-md, car-parrinello, energy-drift, hamiltonian-dynamics]
prerequisites: [numerical-integration-of-odes]
related: [born-oppenheimer-approximation, analytic-gradients-and-force-constants, harmonic-vibrational-analysis, calculus-of-variations-and-the-euler-lagrange-equation, multivariable-taylor-expansion]
key: vv
order: 50
date: 2026-11-26
---

Nuclear coordinates $\mathbf R$, momenta $\mathbf P$, masses $M$, forces $\mathbf F(\mathbf R) = -\nabla E(\mathbf R)$ on a potential energy surface $E$; time step $h$ (also written $\delta t$ or $\Delta t$). Hamiltonian $H = \sum P^2/2M + E(\mathbf R)$. Atomic units unless stated; 1 au of time is 0.024189 fs.

## The algorithm

**Störmer–Verlet.** Adding the Taylor expansions of $\mathbf R(t\pm h)$ cancels the odd terms ([[taylor-and-maclaurin-expansions]]):

$$
\mathbf R(t + h) = 2\mathbf R(t) - \mathbf R(t - h) + \frac{h^2}{M}\mathbf F(t) + O(h^4).
$$

This is the original Verlet algorithm. Its local error is $O(h^4)$ and its global error $O(h^2)$.

**Velocity Verlet.** The same trajectory in a self-starting form that carries the momenta explicitly (Marx and Hutter Eq. 231):

$$
\mathbf P\big(t + \tfrac h2\big) = \mathbf P(t) + \tfrac h2\mathbf F(t),\qquad
\mathbf R(t + h) = \mathbf R(t) + \frac hM\mathbf P\big(t + \tfrac h2\big),\qquad
\mathbf P(t + h) = \mathbf P\big(t + \tfrac h2\big) + \tfrac h2\mathbf F(t + h) .
\label{vv}
$$

The steps are a half kick, a drift, a force evaluation and a second half kick. The new force is reused for the first half kick of the next step, so the cost is one force evaluation per step. Marx and Hutter prefer this form to the original Verlet algorithm because velocities are available at every step (for thermostats and kinetic energies) and the step size can be changed trivially.

**As a splitting.** Velocity Verlet is the symmetric (Strang) composition of the exact flows of the kinetic part ("drift") and the potential part ("kick") of $H$, as $e^{\frac h2\hat V}e^{h\hat T}e^{\frac h2\hat V}$. The same construction gives the second-order Trotter–Suzuki formula of quantum simulation, and its error analysis is a Baker–Campbell–Hausdorff expansion ([[baker-campbell-hausdorff]]).

## Why it conserves energy over long times

**Time reversibility.** Run Eq. [[#vv]] for $N$ steps, reverse all momenta, and run $N$ more. The trajectory retraces itself exactly, up to round-off. The method inherits this symmetry of Newton's equations. RK4 does not have it.

**Symplecticity.** Each kick and each drift is the exact flow of a Hamiltonian, so it preserves phase-space volume (Liouville) and, more strongly, the symplectic two-form. Their composition does too. A general Runge–Kutta method does neither ([[numerical-integration-of-odes]]).

**The shadow Hamiltonian.** Backward error analysis shows that a symplectic method with step $h$ follows, to all orders in $h$, the exact flow of a modified Hamiltonian $\tilde H = H + h^2H_2 + h^4H_4 + \cdots$. Consequences:

- **Bounded energy error.** $\tilde H$ is conserved almost exactly, so the true energy $H$ oscillates around a fixed value with amplitude $O(h^2)$. It does not drift, over times exponentially long in $1/h$.
- **For a harmonic oscillator** the shadow Hamiltonian is known in closed form, and is conserved to machine precision:

  $$\tilde H = \frac{p^2}{2} + \frac{\omega^2}{2}\Big(1 - \frac{(\omega h)^2}{4}\Big)q^2 .$$

**Stability.** For an oscillator of angular frequency $\omega$, velocity Verlet is stable only for $\omega h < 2$. The fastest vibration of the system sets the time step.

**Choosing the time step.**

- **Accuracy.** About 10–20 steps per period of the fastest motion. X–H stretches at 3000–4000 cm⁻¹ have periods of 8–11 fs, so 0.5–1 fs is the usual choice. Marx and Hutter put the limit for systems with stiff covalent bonds at less than a femtosecond, and note that a 2.4 fs step is already at the edge for frequencies up to 3–4000 cm⁻¹.
- **Larger steps.** Constraining X–H bonds (SHAKE/RATTLE), multiple-time-step schemes and mass repartitioning are the standard ways around the limit.

## Ab initio molecular dynamics

**Born–Oppenheimer MD.** The force at each step comes from a converged electronic-structure calculation at the current geometry ([[born-oppenheimer-approximation]], [[analytic-gradients-and-force-constants]]). Verlet's guarantees assume exact forces that are gradients of one fixed function $E(\mathbf R)$. Two things break that assumption in practice:

- **Incomplete SCF convergence.** The force contains an error that is not the gradient of anything and changes from step to step. It acts as a small random or systematic non-conservative force, and the energy drifts. The analytic gradient of a non-stationary energy is also not the derivative of the energy actually computed, unless the Lagrangian terms are included ([[envelope-theorem-and-the-lagrangian-method]]).
- **Starting the SCF from the previous steps' wave functions.** This saves iterations, but makes the converged solution depend on the history. That breaks time reversibility, and the drift grows with the leftover convergence error.

**Marx and Hutter's comparison.** They ran 8-atom silicon with LDA, velocity Verlet and DIIS-converged BOMD, measuring drift in $E_h$ per ps:

| method | time step | gradient convergence | drift ($E_h$/ps) |
|---|---|---|---|
| Car–Parrinello | 5 au (0.12 fs) | (none) | $6\times10^{-8}$ |
| Car–Parrinello | 10 au (0.24 fs) | (none) | $3\times10^{-7}$ |
| BOMD | 10 au | $10^{-6}$ | $1\times10^{-6}$ |
| BOMD | 100 au (2.4 fs) | $10^{-6}$ | $6\times10^{-6}$ |
| BOMD | 100 au | $10^{-4}$ | $1\times10^{-3}$ |

The energy convergence varies roughly quadratically with the gradient threshold. A drift of $10^{-3}E_h$/ps is 0.63 kcal/mol per ps, which ruins a microcanonical run within picoseconds.

**Car–Parrinello and extended-Lagrangian methods.** Car–Parrinello MD avoids the problem differently. It propagates the orbitals as fictitious classical variables together with the nuclei, from an extended Lagrangian, using the same velocity Verlet (with RATTLE for orthonormality). The combined system is Hamiltonian, so a conserved quantity exists and Verlet's guarantees apply. The price is a smaller time step, set by the fictitious electron dynamics (Marx and Hutter Secs. 2.4 and 3.7). Time-reversible extended-Lagrangian Born–Oppenheimer schemes apply the same idea to the SCF guess (general knowledge, not from Marx and Hutter).

## Worked examples

!!! example "Bounded energy, reversibility, step limits and noisy forces (computed for this note)"
    **Harmonic oscillator, $\omega = 1$.** From $q = 1$, $p = 0$, integrated to $t = 1000$:

    | $h$ | max $|E - E_0|$ | $(\omega h)^2/8$ | mean drift over $t = 1000$ |
    |---:|---:|---:|---:|
    | 0.2 | $5.000\times10^{-3}$ | $5.000\times10^{-3}$ | $7\times10^{-7}$ |
    | 0.1 | $1.250\times10^{-3}$ | $1.250\times10^{-3}$ | $6\times10^{-6}$ |
    | 0.05 | $3.125\times10^{-4}$ | $3.125\times10^{-4}$ | $1\times10^{-6}$ |

    The energy band shrinks as $h^2$ and the drift is negligible. Compare RK4 at $h = 0.2$, which loses 4% of the energy by $t = 10\,000$ ([[numerical-integration-of-odes]]).

    **Shadow energy.** At $h = 0.2$, $p^2/2 + \tfrac12(1 - h^2/4)q^2$ varies by $5\times10^{-15}$ over 5000 steps.

    **Reversibility.** A pendulum ($F = -\sin q$, $h = 0.1$): 10 000 steps forward, momentum reversed, 10 000 steps back. It returns to the start within $1\times10^{-13}$ in $q$ and $3\times10^{-13}$ in $p$.

    **Stability limit.** For $\omega = 1$: with $h = 1.9$ the amplitude stays at 0.92 after 60 steps; with $h = 2.1$ it reaches $10^{16}$.

    **A Morse H₂ bond** ($D_e = 0.1745$, $a = 1.0282$, $r_e = 1.4011$ au, reduced mass 918 $m_e$). Harmonic frequency 4400 cm⁻¹, period 7.58 fs, harmonic stability limit $2/\omega = 2.41$ fs. Started at $r_e$ with 0.01 $E_h$ of kinetic energy and run for 2 ps:

    | $\delta t$ (fs) | energy fluctuation (max − min, $E_h$) | drift over 2 ps ($E_h$) |
    |---:|---:|---:|
    | 0.1 | $2.1\times10^{-5}$ | $-3\times10^{-7}$ |
    | 0.5 | $5.6\times10^{-4}$ | $-4\times10^{-6}$ |
    | 1.0 | $2.9\times10^{-3}$ | $-3\times10^{-6}$ |
    | 2.0 | 65 (trajectory destroyed) | |

    At 2 fs, below the harmonic limit, the anharmonic bond still blows up. The stretched bond reaches regions where the effective frequency is higher.

    **Noisy forces, as from loose SCF convergence.** Gaussian noise of standard deviation $s$ is added to every force, with $\delta t = 0.5$ fs, run for 20 ps, 60 runs each:

    - $s = 10^{-5}$ $E_h$/bohr: rms energy change $1.5\times10^{-4}E_h$;
    - $s = 10^{-4}$ $E_h$/bohr: rms energy change $1.6\times10^{-3}E_h$.

    Both match the random-walk estimate $s\,v_{\rm rms}h\sqrt N = 1.4\times10^{-4}$ and $1.4\times10^{-3}$: the energy diffuses, growing as $\sqrt t$. A systematic error of $10^{-5}$ $E_h$/bohr aligned with the velocity pumps in energy linearly instead: $+3.7\times10^{-2}E_h$ in 20 ps, 250 times more than random noise of the same size.

## Source

Marx and Hutter, "Ab initio molecular dynamics: theory and implementation", in J. Grotendorst (ed.), *Modern Methods and Algorithms of Quantum Chemistry* (NIC, Jülich, 2000), Sec. 2.4 (Car–Parrinello dynamics), Sec. 2.6 (choice of method, time steps, Table 1 energy conservation), Sec. 3.7.1 (velocity Verlet/RATTLE in CPMD, Eq. 231). The Störmer–Verlet derivation, symplecticity, backward error analysis and the harmonic shadow Hamiltonian are standard results of geometric numerical integration, stated here and checked numerically. Calculations in `Claude outputs/part0_math_batchG.py`, section D.
