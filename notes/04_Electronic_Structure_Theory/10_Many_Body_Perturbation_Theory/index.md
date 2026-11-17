Correlation as a perturbation of Hartree–Fock.

## What this chapter is about

Møller–Plesset (MP) perturbation theory takes the sum of Fock operators as the unperturbed Hamiltonian, $\hat H^{(0)}=\sum_i\hat f(i)$. The perturbation is then the difference between the true electron repulsion and its Hartree–Fock average. Every determinant is an eigenfunction of $\hat H^{(0)}$, so Rayleigh–Schrödinger theory (Part 2, Chapter 8) applies directly. The zeroth- plus first-order energy is the Hartree–Fock energy, and correlation starts at second order:

$$
E^{(2)}_\text{MP2}=\frac14\sum_{ijab}\frac{|\langle ij||ab\rangle|^2}{\varepsilon_i+\varepsilon_j-\varepsilon_a-\varepsilon_b}.
$$

The chapter derives MP2 and MP3 and recasts the theory in second quantization with diagrams. It then proves the linked-cluster theorem, which explains why MP theory is size-extensive at every order.

## Why it matters

- **MP2 is the cheapest correlated method.** It needs one transformation of the integrals to the MO basis and a single sum, at $O(N^5)$ cost. It recovers a large fraction of the dynamic correlation energy for well-behaved closed-shell molecules. It is often the first correlated step and is used in double-hybrid functionals and composite schemes.
- **It is size-extensive, unlike truncated CI.** The linked-cluster theorem shows that the unphysical terms growing as $N^2$ for $N$ noninteracting fragments cancel exactly at each order. This is the property CISD lacks.
- **It organizes coupled cluster.** Counting orders in the fluctuation potential explains why CCSD(T) works and what each coupled-cluster term contributes (Chapter 12).
- **Its limits are instructive.** The MP series can converge slowly, oscillate or diverge, especially with small denominators or diffuse functions. It fails badly when the reference is near-degenerate, which is where multiconfigurational methods are needed.

## Where it is used later

- [[coupled-cluster-doubles|Coupled cluster]] (Chapter 11), which sums MP-type terms to infinite order.
- [[moller-plesset-and-coupled-cluster-perturbation-theory|Coupled-cluster perturbation theory]] and [[mp-convergence-intruders-analytic-continuation|convergence of the MP series]] (Chapter 12).
- [[caspt2-and-caspt-series|CASPT2]] (Chapter 13), which applies the same idea to a multiconfigurational reference.
- [[ionization-potentials-second-order-self-energy|Second-order self-energy]] (Chapter 17).

## The main ideas, in order

1. **The Møller–Plesset partition.** MP2 in spin-orbital and closed-shell form; MP3 and its three diagram types.
2. **One-particle perturbations.** When both $\hat H^{(0)}$ and $\hat V$ are one-particle operators, the $N$-electron series reduces to orbital perturbation theory (the Hückel resonance-energy example).
3. **Second quantization.** Resolvent derivation, Brillouin–Wigner versus Rayleigh–Schrödinger, and why only the latter is size-extensive.
4. **The linked-cluster theorem.** Hugenholtz and Goldstone diagrams; disconnected terms cancel.
5. **Variational structure.** Wigner's $2n+1$ rule and the Hylleraas functional, which make $E^{(2)}$ stationary.

## How to read it

**Path.**

1. MP2 and MP3.
2. Orbital perturbation theory.
3. Perturbation theory in second quantization, with diagrams and the linked-cluster theorem (why MPn is size-extensive).
4. Wigner's 2n+1 rule and the Hylleraas functional.

**Leads to.** The MP series is examined again from the coupled-cluster side in Chapter 12.

**Core (first pass).** [[mp2]], [[mp3]], [[orbital-perturbation-theory]].

**Deep (second pass).** [[perturbation-theory-second-quantization]], [[linked-cluster-theorem]], [[rspt-wigner-rule-and-hylleraas-functional]].

**Checkpoint.** Derive the closed-shell MP2 formula from the spin-orbital one.
