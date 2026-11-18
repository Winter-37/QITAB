The core of the notebook, arranged as a textbook: how to compute the electronic structure of molecules from first principles, and how good the answer is.

## What this part is about

Given the positions of the nuclei, find the energy and wave function of the electrons by solving the clamped-nucleus Schrödinger equation. It can be solved exactly only for the smallest systems, so this part is a sequence of approximations, each with its own logic:

- **Chapters 1–8: the mean-field picture.** The Hamiltonian, determinants, Hartree–Fock, basis sets and integrals, second quantization, density matrices, orbital optimization, and Kohn–Sham density functional theory.
- **Chapters 9–14: electron correlation.** CI, perturbation theory, coupled cluster, methods beyond CCSD, multiconfigurational methods, and how they compare.
- **Chapters 15–17: properties.** Analytic derivatives, geometries and potential energy surfaces, and propagators.
- **Chapter 19: quantum embedding.** DMET, up to its analytic gradient.
- **Planned:** excited states (Chapter 18), stochastic and tensor-network methods (20), software (21) and applications (22).

## Why it is organized this way

Each correlated method fixes a specific failure of the one before it:

| Failure | Where it shows up | Fixed by |
|---|---|---|
| No electron correlation | Hartree–Fock (Ch. 3) | CI (Ch. 9) |
| Truncated CI is not size-consistent | CISD (Ch. 9) | MP theory and coupled cluster (Ch. 10–11) |
| CCSD not accurate enough | thermochemistry | (T) and higher (Ch. 12) |
| One determinant qualitatively wrong | bond breaking (Ch. 3, Ch. 9) | MCSCF and CASPT2 (Ch. 13) |
| Accurate solvers cost too much for large systems | everything above | embedding (Ch. 19) |

Reading the chapters in order follows this chain of problems and fixes. Each method then makes sense as an answer to a specific question rather than as a recipe.

## How it connects to the rest

- **Built on:** Part 2 (above all Chapters 3, 5, 7 and 8) and Part 0, Chapter 1.
- **Leads to:** Part 6, where the same Hamiltonian is mapped to qubits and solved with VQE, SQD and DMET with quantum solvers. The paper notes of Part 8 summarize the literature behind Chapters 15, 16 and 19.

## How to read it

Read the chapters in order; the Previous/Next buttons follow the same order. Use two passes:

1. **First pass.** Only the notes marked *core* in each chapter introduction, at the level of Szabo–Ostlund or Jørgensen–Simons: first quantization, explicit determinants, small worked models.
2. **Second pass.** Add the *deep* notes, at the level of Helgaker–Jørgensen–Olsen: second quantization, exponential parametrizations, Lagrangians and production algorithms.

Chapters 5, 6, 7, 12, 15 and 17 are second-pass chapters. Chapter 5 is the prerequisite for almost every deep note.

Each chapter ends its reading list with a checkpoint: a derivation or number to reproduce before moving on. Most of the worked numbers already sit inside the notes, so the test is to rederive them before looking.
