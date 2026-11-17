Electronic-structure methods on quantum computers: the same molecular Hamiltonian as Part 4, solved with a quantum processor as part of the algorithm.

## What this part is about

A quantum computer with $n$ qubits works in a $2^n$-dimensional space. This is the same exponential growth that makes full CI impossible classically. This part asks how to exploit that:

1. **Map the problem.** Write the second-quantized Hamiltonian of Part 4 as a sum of Pauli strings acting on qubits (Chapters 1–2).
2. **Prepare and measure states.** VQE minimizes a measured energy over a parametrized circuit (Chapter 3). Phase estimation reads energies off a phase (Chapter 4, planned). SQD uses the device only to sample important determinants and diagonalizes classically (Chapter 5).
3. **Make it fit.** Embedding cuts a molecule into fragment problems small enough for current hardware (Chapter 7). Excited states, gradients and hardware-efficient implementations follow (Chapters 8–11, planned).

## Why it is here

Present devices are noisy and have limited numbers of qubits, so which algorithms are useful depends on understanding both sides:

- **Chemistry.** Which approximation a quantum algorithm replaces, and what classical method it must beat (Part 4, Chapters 9–13 and 20).
- **Quantum computing.** What circuits cost, how measurement noise scales, and what errors do (Part 5).

The chapters written so far take the shortest path from second quantization to the methods used most in recent work:

- map the Hamiltonian to qubits (Chapter 2);
- estimate energies variationally (Chapter 3);
- sample determinants instead (Chapter 5);
- embed either inside DMET (Chapter 7).

## How it connects to the rest

| Quantum method | Classical counterpart | Part 4 chapter |
|---|---|---|
| Jordan–Wigner Hamiltonian | Second-quantized $\hat H$ | 5 |
| VQE with UCC | Coupled cluster, made unitary and variational | 11, 12 |
| SQD | Selected CI with a quantum sampler | 9 |
| DMET with quantum solvers | DMET with an FCI solver | 19 |

## How to read it

**Needs.** Part 4, Chapters 5 (second quantization), 9 (CI) and 11 (coupled cluster); Chapter 19 (DMET) for Chapter 7. Qubits and gates from Part 5 help but are not required for the notes written so far.

**Order.** Chapters 2 → 3 → 5 → 7. Chapters 1, 4, 6 and 8–11 are planned.
