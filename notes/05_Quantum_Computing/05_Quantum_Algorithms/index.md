The algorithms that show where quantum computers can outperform classical ones, and the two subroutines that matter most for chemistry: the quantum Fourier transform and phase estimation, together with the Hamiltonian simulation that feeds them (Nielsen and Chuang, Chs. 1, 4 and 5).

## What this chapter is about

Every quantum algorithm in this chapter follows one pattern:

1. prepare a superposition;
2. let a function or a unitary write its answer into **phases**;
3. **interfere** the branches with a Hadamard or Fourier transform so the wanted answer has large amplitude;
4. measure.

The chapter develops this from the simplest case (Deutsch–Jozsa) to the general tool (phase estimation). It then shows how to supply the unitary $e^{-iHt}$ that phase estimation needs for a physical Hamiltonian (Trotter simulation).

## Why it matters

- **Interference, not parallelism, is the source of speed-ups.** Evaluating $f$ on all inputs at once is useless if only one value can be read out. Deutsch–Jozsa shows how cancellation extracts a global property from one query.
- **The QFT turns phases into bits** using $O(n^2)$ gates. It is the step that makes phase estimation, order finding and Shor's algorithm work.
- **Phase estimation is an energy measurement.** With $U=e^{iH\tau}$ it projects onto eigenstates of a molecular Hamiltonian and returns their energies, with probability equal to the squared overlap with the input state. This is the long-term route to full-CI-quality energies.
- **Simulation makes it concrete.** Trotter formulas and Pauli-string exponentials turn a Jordan–Wigner Hamiltonian into a circuit, with errors that can be controlled.

## Where it is used later

- The planned phase-estimation chapter of Part 6 (Chapter 4), which applies QPE to molecular Hamiltonians.
- [[vqe-ansatze|UCC ansätze]] (Part 6), built from the same Pauli-string exponentials.
- [[sample-based-quantum-diagonalization|SQD]] and [[variational-quantum-eigensolver|VQE]], the near-term alternatives to QPE, which are judged against what QPE would deliver.

## The main ideas, in order

1. **Parallelism and Deutsch–Jozsa.** Reversible oracles, phase kickback, and the one-query separation for exact answers.
2. **Quantum Fourier transform.** The product representation, the $\Theta(n^2)$ circuit, the approximate QFT, and the sign convention against NumPy.
3. **Phase estimation.** Controlled powers, the inverse QFT, the success analysis ($4/\pi^2$, the tail bound, and $t=n+\lceil\log_2(2+1/2\epsilon)\rceil$), and non-eigenstate inputs.
4. **Simulation.** Trotter and Strang errors, and CNOT-ladder circuits for Pauli strings.

## How to read it

**Path.** [[deutsch-jozsa-and-quantum-parallelism]], [[quantum-fourier-transform]], [[quantum-phase-estimation]], [[simulation-of-quantum-systems]].

**Needs.** Chapters 3 and 4 ([[controlled-operations]], [[measurement-in-quantum-circuits]]). Fourier transforms (Part 0, Chapter 4). The Baker–Campbell–Hausdorff expansion (Part 0, Chapter 1).

**Leads to.** Part 6, Chapter 4 (phase estimation for chemistry) and the variational algorithms of Chapter 9.

**Checkpoint.** Derive the product form of $\mathrm{QFT}|j\rangle$. Then show that phase estimation with an exact $t$-bit phase returns it with certainty. Finally, write the circuit for $e^{-i\Delta t\,X_1Y_2Z_3}$.

**Planned sections:** Order finding and Shor's algorithm; Grover search and amplitude amplification; Hidden subgroup problems.
