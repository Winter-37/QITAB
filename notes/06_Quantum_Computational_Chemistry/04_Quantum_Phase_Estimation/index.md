Phase estimation applied to molecular Hamiltonians: measuring electronic energies to a chosen precision on a fault-tolerant quantum computer.

## What this chapter is about

[[quantum-phase-estimation|Phase estimation]] measures the eigenphase of a unitary. Applied to $U=e^{-iH\tau}$ with $H$ the qubit form of a molecular Hamiltonian, it becomes a projective **energy measurement**. Each run returns an eigenvalue $E_u$ of $H$ with probability $|\langle u|\Phi\rangle|^2$ for input state $|\Phi\rangle$, and leaves the system close to $|u\rangle$. This chapter turns that statement into a working method:

- how to set the energy window and read the result;
- how to do it with one ancilla;
- what the Trotter approximation of $e^{-iH\tau}$ does to the energy;
- how the input state's overlap limits success;
- what the whole thing costs.

## Why it matters

- **It gives FCI-quality energies with controlled precision.** Unlike VQE and SQD, which give upper bounds whose quality depends on an ansatz or a sample, QPE returns the exact eigenvalue in the chosen orbital space. Its error is set by the number of readout bits and the simulation error, and its cost scales as $1/\epsilon$ rather than $1/\epsilon^2$.
- **It is the reference point for quantum chemistry on future hardware.** Resource estimates for FeMoco and similar systems are QPE estimates. Near-term methods are judged by how close they come to what QPE would deliver.
- **Its limits are chemical, not only technical.** The required overlap with the ground state decays exponentially with system size for any fixed-form input (the orthogonality catastrophe). Whether a quantum advantage exists therefore depends on state preparation as much as on circuits.

## Where it is used later

- The planned chapters on quantum excited states (Chapter 8) and gradients (Chapter 9), where QPE-prepared eigenstates are the input.
- Comparisons with [[variational-quantum-eigensolver|VQE]], [[sample-based-quantum-diagonalization|SQD]] and [[dmet-with-quantum-solvers|embedding with quantum solvers]].

## The main ideas, in order

1. **Energies from phases.** $\varphi=(E_{\text{ref}}-E)\tau/2\pi$. A safe window comes from the 1-norm $\lambda$; the grid is $2\lambda/2^t$; the success probability is $|c_0|^2$. Worked for H₂.
2. **One ancilla.** Iterative phase estimation reproduces the textbook statistics with semiclassical feedback.
3. **Trotter error.** QPE measures an effective Hamiltonian. For real molecular Hamiltonians the energy error is $O(\Delta t^2)$ even at first order, which fixes the step sizes for chemical accuracy.
4. **Overlap.** HF overlap falls with bond stretching and geometrically with system size. Better inputs are needed for large systems.
5. **Cost.** $(1/|c_0|^2)\times(\lambda/\epsilon)\times(\text{oracle cost})$, with qubitization and factorized Hamiltonians, and published FeMoco estimates.

## How to read it

**Path.** [[qpe-for-molecular-energies]], [[iterative-phase-estimation]], [[trotter-error-in-qpe-energies]], [[qpe-state-preparation-and-overlap]], [[qpe-cost-and-resource-estimates]].

**Needs.**
- Part 5, Chapter 5: [[quantum-fourier-transform]], [[quantum-phase-estimation]], [[simulation-of-quantum-systems]].
- Chapter 2 of this part: [[jordan-wigner-mapping]].
- Part 4, Chapter 9: [[full-ci]], [[electron-correlation]].
- Chapter 1 of this part, for how the Hamiltonian is built: [[molecular-hamiltonian-in-the-mo-basis]].

**Leads to.** Excited states and gradients (Chapters 8–9, planned) and hardware implementations (Chapter 10, planned).

**Checkpoint.** For H₂/STO-3G with $\lambda=1.894\,E_h$, compute the number of readout bits for a 1 m$E_h$ grid with the 1-norm window. Then explain why first-order Trotter gives an $O(\Delta t^2)$ energy error for a real Hamiltonian, and why the H₂ HF overlap tends to ½ on dissociation.

**Planned sections:** Qubitization and block encodings in detail; Double factorization and tensor hypercontraction; Early fault-tolerant phase estimation (statistical and robust methods); Excited states by phase estimation.
