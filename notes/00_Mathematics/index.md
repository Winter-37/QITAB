The mathematics the rest of the notebook uses, collected in one place so that physics chapters can cite a result instead of re-deriving it. The chapters are ordered as the subject is learned: linear algebra and calculus first, then vector calculus, series and complex analysis, then differential equations, numerical error, probability, optimization, tensors and groups. The main references are Arfken and Weber's *Mathematical Methods for Physicists*, Griffiths, Sakurai and Nielsen–Chuang, with additions labelled where they go beyond those books.

## What this part is about

Quantum mechanics is linear algebra in a complex vector space plus the analysis needed for infinite-dimensional spaces of functions. This part covers both:

- **Finite-dimensional linear algebra** (Chapter 1): vectors and operators, determinants and matrices, the eigenvalue problem, functions of matrices, the spectral theorem, polar and singular value decompositions, and the exponential parametrization of unitary matrices.
- **Calculus** (Chapter 2): functions, limits and continuity, differential and integral calculus in one and several variables, matrix calculus and eigenvalue derivatives, the calculus of variations and functional derivatives.
- **Vector calculus** (Chapter 3): scalars and vectors, gradient, divergence and curl, the theorems of Gauss and Stokes, the Laplacian and vector identities, curvilinear coordinates.
- **Series and expansions** (Chapter 4): convergence, power series, Taylor and binomial expansions, Fourier series and transforms, asymptotic and operator series. Its introduction lists every expansion in the notebook.
- **Complex analysis** (Chapter 5): complex numbers, analytic functions and Cauchy's theorem, Laurent series and residues, and the Laplace transform.
- **Differential equations** (Chapter 6): first- and second-order ODEs, PDEs and separation of variables, the Frobenius method, Sturm–Liouville theory, the special functions (Hermite, Legendre, Laguerre, spherical Bessel), and eigenfunction expansions.
- **Numerical methods** (Chapter 7): floating point, cancellation, truncation and conditioning; Gaussian quadrature; ODE integrators and velocity Verlet.
- **Probability and statistics** (Chapter 8): expectation values, error analysis and propagation of uncertainty, and how many samples an estimate needs.
- **Optimization** (Chapter 9): constrained stationary points, Lagrange multipliers and the KKT conditions, the envelope theorem, and the Lagrangian (adjoint) method for derivatives of nonvariational energies.
- **Composite systems** (Chapter 10): tensor products, the partial trace, the Schmidt decomposition, and rotational averages of Cartesian tensors.
- **Symmetry** (Chapter 11): finite groups, representations and characters.

## Why it is here

The physics chapters are easier to read when the mathematics is already familiar. Their key steps are often a single theorem used without comment:

- Hartree–Fock is a generalized eigenvalue problem, and the orthogonalizer is $\mathbf S^{-1/2}$.
- Orbital rotations are exponentials of anti-Hermitian matrices.
- The coupled-cluster equations rest on a Baker–Campbell–Hausdorff expansion.
- Geometry optimization and vibrational analysis are a second-order Taylor expansion of the energy.
- Every Coulomb integral uses $\nabla^2(1/r) = -4\pi\delta(\mathbf r)$ and the Legendre expansion of $1/r_{12}$.
- Quantization is the termination of a power series.
- Kramers–Kronig relations and damped response functions are contour integration.
- The DMET bath is a singular value decomposition.
- The cost of VQE is set by sampling statistics.

Collecting these results here also makes conventions explicit: Fourier sign and normalization, Laguerre polynomial normalization, the physics convention for spherical angles, and Kronecker-product index ordering. Different books disagree on all of them.

## The storyline

| Chapter | Topic | Used most in |
|---|---|---|
| 1 | Linear algebra | Everything; above all Part 4, Chapters 3, 5, 7 and 9 |
| 2 | Calculus, matrix calculus, variational calculus | Everything; analytic gradients and DFT in Part 4 |
| 3 | Vector calculus | Electromagnetism (Part 1), kinetic energy and Coulomb operators, densities and currents |
| 4 | Series and expansions | Perturbation theory, Fourier methods, response functions, asymptotics; Part 2, Chapters 2, 3 and 10 |
| 5 | Complex analysis | Fourier and Green's-function methods, Kramers–Kronig, response theory (Part 4, Chapter 17) |
| 6 | Differential equations and special functions | Part 2, Chapters 2, 4 and 10; basis functions in Part 4, Chapter 4 |
| 7 | Numerical error, quadrature, ODE integrators | Every worked example; integral and DFT grids; molecular dynamics; Part 7 |
| 8 | Probability, statistics and error analysis | Part 2, Chapter 1; measurement cost in Parts 5 and 6 |
| 9 | Constrained optimization and the Lagrangian method | Hartree–Fock and Kohn–Sham equations, orbital optimization, analytic gradients (Part 4, Chapters 3, 7, 8 and 15) |
| 10 | Tensor products, tensors and tensor decompositions | Many-particle states, RDMs, qubits, embedding, isotropic averages; integral factorization and DMRG |
| 11 | Group theory: finite groups, the symmetric group, Lie groups | Symmetry labels, symmetry orbitals and selection rules in Parts 2–4; spin adaptation and CSF counts; orbital rotations; the Pauli group in Part 5 |

## How to read it

For a first pass, read Chapters 2–4 and the core of Chapter 1 before Part 2, and Chapter 3 before Part 1's electromagnetism. Treat the rest as a reference to open when a physics note points to it; the **Needs** line of every chapter introduction says which mathematics it uses.
