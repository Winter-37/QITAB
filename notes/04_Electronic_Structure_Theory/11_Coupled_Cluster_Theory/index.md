From pair theories to the exponential ansatz.

## What this chapter is about

Coupled cluster writes the wave function as an exponential of excitation operators acting on the Hartree–Fock determinant:

$$
|\Psi_\text{CC}\rangle=e^{\hat T}|\Phi_0\rangle,\qquad \hat T=\hat T_1+\hat T_2+\cdots .
$$

Even when $\hat T$ is truncated at doubles, $e^{\hat T}$ contains products such as $\tfrac12\hat T_2^2$. These describe two independent pairs of electrons correlating at the same time, and they generate quadruple and higher excitations at no extra parameter cost. The amplitudes are found by projecting the Schrödinger equation, not by minimizing the energy. The similarity-transformed Hamiltonian $e^{-\hat T}\hat He^{\hat T}$ has a commutator expansion that stops after four nested commutators, so the equations are finite. The chapter reaches this form in two ways:

- historically, from independent and coupled pair approximations derived from the CI hierarchy;
- formally, in second quantization.

It then gives the working CCSD equations, their diagrams, and how they are solved.

## Why it matters

- **It is the accuracy standard for single-reference molecules.** CCSD(T) (Chapter 12) is often called the "gold standard" of quantum chemistry for systems dominated by one determinant near equilibrium. CCSD is the foundation it rests on.
- **Size extensivity by construction.** The exponential makes the energy of noninteracting fragments additive at every truncation level, which repairs the central flaw of CISD.
- **A different kind of approximation.** Coupled cluster is not variational: its energy is not an upper bound. Properties and gradients therefore need the $\Lambda$ Lagrangian, which is set up at the end of this chapter.
- **It connects to quantum computing.** Unitary coupled cluster, $e^{\hat T-\hat T^\dagger}$, is the ansatz behind UCCSD-VQE. The LUCJ ansatz used with SQD is a local unitary cluster–Jastrow form of the same idea.

## Where it is used later

- [[perturbative-triples-cc2-cc3|Perturbative triples]] and [[eom-ccsd-and-size-extensivity|EOM-CC]] (Chapter 12).
- [[variational-and-unitary-coupled-cluster|Variational and unitary CC]] (Chapter 12), [[vqe-ansatze|VQE ansätze]] and [[lucj-ansatz|the LUCJ ansatz]] (Part 6).
- [[lagrangian-for-nonvariational-energies|Lagrangians for non-variational energies]] (Chapter 15).
- [[hjo-calibration-energies-atomization-reactions-barriers|Calibration of CC methods]] (Chapter 14).

## The main ideas, in order

1. **Pair theories.** IEPA, then DCI, linear CCD and CEPA as truncations of the full-CI hierarchy. CCD closes the hierarchy by writing quadruples as products of doubles.
2. **The exponential ansatz.** $e^{\hat T}$ in second quantization, and the terminating Baker–Campbell–Hausdorff series.
3. **The hierarchy and extensivity.** Connected and disconnected clusters; why a projected exponential is extensive.
4. **Working equations.** Spin-orbital CCSD with Stanton–Gauss intermediates, the diagram rules, and the closed-shell $T_1$-transformed form.
5. **Solving and making it variational.** Quasi-Newton iterations with DIIS, and the $\Lambda$ Lagrangian for properties.

## How to read it

**Path.**

1. Independent and coupled electron-pair approximations, and CCD derived from the CI hierarchy.
2. Coupled cluster in second quantization: $e^{\hat T}$ and the terminating commutator series.
3. The CC hierarchy and size extensivity.
4. The spin-orbital CCSD equations, coupled-cluster diagrams, and the closed-shell $T_1$-transformed form.
5. How the equations are solved, and the $\Lambda$ Lagrangian for properties.

**Needs.** Chapters 5, 9 and 10.

**Core (first pass).** [[iepa]], [[coupled-pair-approximations]], [[coupled-cluster-doubles]], [[coupled-cluster-second-quantization]].

**Deep (second pass).** [[coupled-cluster-hierarchy-and-size-extensivity]], [[ccsd-spin-orbital-equations]], [[coupled-cluster-diagrams]], [[closed-shell-ccsd-t1-transformation]], [[coupled-cluster-optimization-and-lagrangian]].

**Checkpoint.** Expand $e^{\hat T}$ to quadruples and identify each disconnected term. Explain why CCSD is exact for two electrons.
