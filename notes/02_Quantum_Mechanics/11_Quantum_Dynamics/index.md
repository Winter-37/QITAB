Hamiltonians that depend on time. Up to here every system was conservative and its stationary states carried all the physics. This chapter treats transitions between them, driven by an applied field or by a slow or sudden change of the Hamiltonian itself.

## What this chapter is about

When $\hat H=\hat H_0+\hat V(t)$, the stationary states of $\hat H_0$ are no longer stationary. Write the state as $\sum_n c_n(t)e^{-iE_nt/\hbar}|n\rangle$; the coefficients now change with time. The central question is the probability $|c_f(t)|^2$ of finding the system in state $f$ after it started in $i$.

- **Exact case.** A two-level system with an oscillating coupling can be solved exactly, giving Rabi oscillations.
- **General case.** The interaction picture and the Dyson series give $c_f$ order by order. To first order the amplitude is the Fourier component of $\hat V(t)$ at the transition frequency.
- **Continuum.** When the final states form a continuum, the probability grows linearly in time. This gives a constant rate, Fermi's golden rule $w=(2\pi/\hbar)|V_{fi}|^2\rho(E)$.
- **Slow and fast changes.** A Hamiltonian that changes very slowly keeps the system in its instantaneous eigenstate (adiabatic theorem), up to a dynamic phase and a geometric Berry phase. One that changes very fast leaves the state untouched (sudden approximation).

## Why it matters

- **Spectroscopy is time-dependent perturbation theory.** Absorption and stimulated emission rates, Einstein coefficients, line strengths and selection rules all come from the first-order amplitude in the dipole approximation.
- **Lifetimes and widths.** The golden rule gives decay rates, and a decaying state has an energy width $\Gamma=\hbar/\tau$. The same formula gives scattering cross sections in the Born approximation.
- **The Born–Oppenheimer picture is an adiabatic approximation.** Electrons follow the nuclei adiabatically. The Landau–Zener formula estimates when they do not, at avoided crossings. Berry phases appear around conical intersections. Nonadiabatic dynamics in photochemistry starts from these ideas.
- **Quantum computing is driven two-level dynamics.** On most hardware a single-qubit gate is a controlled Rabi rotation, and adiabatic state preparation is the adiabatic theorem applied deliberately.
- **Linear response is first-order time-dependent perturbation theory.** Frequency-dependent polarizabilities, excitation energies from response functions, and propagators all come from the amplitudes derived here.

## Where it is used later

- [[born-oppenheimer-approximation|The Born–Oppenheimer approximation]] and its breakdown (Part 4, Chapter 1).
- [[molecular-properties-and-response|Response properties]] and [[polarization-propagator-rpa|the polarization propagator]] (Part 4, Chapters 16–17).
- [[low-energy-scattering-and-resonances|Resonances]] (Chapter 10), whose widths the golden rule computes.
- Qubit rotations and gates (Part 5).

## The main ideas, in order

1. **The exact two-level problem.** Rabi oscillations, the rotating-wave approximation, and detuning.
2. **Formalism.** The interaction picture and the Dyson series.
3. **Perturbative amplitudes.** First and second order; constant and harmonic perturbations.
4. **Rates.** Fermi's golden rule, decay widths and level shifts.
5. **Radiation.** Absorption, stimulated and spontaneous emission, and Einstein coefficients in the dipole approximation.
6. **Limits of slow and fast change.** The sudden and adiabatic approximations, Landau–Zener transitions, and the Berry phase.

## How to read it

**Path.** [[two-level-systems-and-rabi-oscillations]] solves the simplest case exactly. [[interaction-picture-and-dyson-series]] sets up the general formalism, and [[time-dependent-perturbation-theory]] gives the first- and second-order transition amplitudes. [[fermi-golden-rule-and-decay-width]] treats transitions into a continuum, exponential decay and line widths, and [[emission-absorption-and-spontaneous-emission]] applies all of this to atoms in a radiation field. [[sudden-and-adiabatic-approximations]] covers the two limits of a changing Hamiltonian, and [[berry-phase]] the geometric phase that adiabatic evolution leaves behind.

**Needs.** Time-independent perturbation theory (Chapter 8), the Heisenberg picture and the selection rules (Chapter 6), spin one-half and the hydrogen atom (Chapter 4). The golden rule connects to scattering (Chapter 10), and the adiabatic limit to the WKB approximation (Chapter 9).

**Leads to.** The Born-Oppenheimer approximation and its breakdown (Part 4, Chapter 1), response theory and propagators (Part 4, Chapters 15 to 17), and the time evolution used throughout quantum computing (Part 5).

**Planned sections:** the photoelectric effect; quantization of the radiation field.
