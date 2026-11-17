The mathematics the rest of the notebook uses, collected in one place so that physics chapters can cite a result instead of re-deriving it. The content comes from Griffiths, Sakurai and Nielsen–Chuang, with additions labelled where they go beyond those books.

## What this part is about

Quantum mechanics is linear algebra in a complex vector space plus the analysis needed for infinite-dimensional spaces of functions. This part covers both:

- **Finite-dimensional linear algebra** (Chapter 1): vectors and operators, the eigenvalue problem, functions of matrices, the spectral theorem, polar and singular value decompositions, and the exponential parametrization of unitary matrices.
- **Analysis** (Chapters 2 and 3): Fourier transforms and the Dirac delta, and the special functions (Hermite, Legendre, Laguerre, spherical Bessel) that solve the exactly soluble problems.
- **Probability** (Chapter 5): what an expectation value is, and how many samples it takes to estimate one.
- **Composite systems** (Chapter 7): tensor products, the partial trace and the Schmidt decomposition.
- **Symmetry** (Chapter 8): finite groups, representations and characters.

## Why it is here

The physics chapters are easier to read when the mathematics is already familiar. Their key steps are often a single theorem used without comment:

- Hartree–Fock is a generalized eigenvalue problem, and the orthogonalizer is $\mathbf S^{-1/2}$.
- Orbital rotations are exponentials of anti-Hermitian matrices.
- The coupled-cluster equations rest on a Baker–Campbell–Hausdorff expansion.
- The DMET bath is a singular value decomposition.
- The Born amplitude is a Fourier transform.
- The cost of VQE is set by sampling statistics.

Collecting these results here also makes conventions explicit: Fourier sign and normalization, Laguerre polynomial normalization, and Kronecker-product index ordering. Different books disagree on all three.

## The storyline

| Chapter | Topic | Used most in |
|---|---|---|
| 1 | Linear algebra | Everything; above all Part 4, Chapters 3, 5, 7 and 9 |
| 2 | Fourier transforms, delta function | Part 2, Chapters 2, 3 and 10 |
| 3 | Special functions | Part 2, Chapters 2, 4 and 10; basis functions in Part 4, Chapter 4 |
| 4 | Numerical methods (planned) | Part 7 |
| 5 | Probability and sampling | Part 2, Chapter 1; measurement cost in Parts 5 and 6 |
| 6 | Optimization (planned) | Orbital optimization and geometry optimization in Part 4 |
| 7 | Tensor products | Many-particle states, RDMs, qubits, embedding |
| 8 | Group theory | Symmetry labels and selection rules in Parts 2–4; the Pauli group in Part 5 |

## How to read it

Not front to back. Read the core notes of Chapter 1 before Part 2. Treat the rest as a reference to open when a physics note points to it; the **Needs** line of every chapter introduction says which mathematics it uses.
