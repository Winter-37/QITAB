The variational quantum eigensolver: a parametrized circuit, a measured energy, a classical optimizer.

## What this chapter is about

VQE applies the variational principle of Part 2, Chapter 7 with a quantum circuit as the trial function. A circuit $U(\boldsymbol\theta)$ prepares $|\psi(\boldsymbol\theta)\rangle$ on the device. The energy

$$
E(\boldsymbol\theta)=\langle\psi(\boldsymbol\theta)|\hat H|\psi(\boldsymbol\theta)\rangle=\sum_k c_k\langle P_k\rangle_{\boldsymbol\theta}
$$

is estimated by repeated measurement of the Pauli strings. A classical optimizer then updates $\boldsymbol\theta$. The result is an upper bound to the ground-state energy, up to statistical and hardware error. The quality of that bound depends on the *ansatz*, the form of the circuit.

## Why it matters

- **It was designed for near-term hardware.** Each circuit can be shallow, and the device only prepares and measures states. The optimization runs classically. This made VQE the first quantum-chemistry algorithm run on real devices, and the reference point for later ones.
- **Unitary coupled cluster becomes possible.** UCC is variational and keeps symmetries, but its energy expansion does not terminate, so it is impractical classically (Part 4, Chapter 12). On a quantum computer it is implemented directly as a circuit.
- **Its costs are now well understood (sections 3–5).** The number of shots needed for precision $\epsilon$ grows roughly as $(\sum_k|c_k|)^2/\epsilon^2$, which is very large for molecules at chemical accuracy. Random hardware-efficient circuits suffer from barren plateaus, gradients that vanish exponentially with qubit number. Noise biases the energy. These limitations motivated SQD (Chapter 5).

## Where it is used later

- [[dmet-with-quantum-solvers|VQE as a DMET fragment solver]] (Chapter 7).
- [[tilly-2022-vqe-review|Tilly et al. 2022]], the review this chapter draws on (Part 8).
- [[hao-2026-dmet-vqe-geometry|Hao et al. 2026]], which uses DMET-VQE for geometry optimization (Part 8).

## The main ideas, in order

1. **The algorithm.** The hybrid loop, and where the cost goes: shots, trainability and noise.
2. **Ansätze.** Hardware-efficient, unitary coupled cluster, symmetry-preserving and adaptive (ADAPT) circuits, compared on what they can represent and whether they can be trained.
3. **Measuring the energy.** Estimator variance and optimal shot allocation; grouping of qubit-wise and fully commuting terms; exact shot counts for H₂, LiH and H₂O.
4. **ADAPT-VQE.** Gradient-selected growth of the circuit, compared with single-step UCCSD and with CCSD and CCSD(T) on stretched hydrogen chains.
5. **Error mitigation.** A noisy gate-level H₂ circuit; symmetry verification, zero-noise extrapolation and readout correction, and their costs.

## How to read it

**Path.** [[variational-quantum-eigensolver]], then [[vqe-ansatze]], then [[pauli-measurement-and-grouping]], then [[adapt-vqe]], then [[error-mitigation-for-vqe]].

**Needs.**
- Chapter 2 (the qubit Hamiltonian; [[qubit-tapering]] for the symmetry projectors in error mitigation).
- Part 4, Chapter 11 for UCC.
- Part 5, Chapter 1 for measurements and density matrices.

**Leads to.**
- Chapter 5: SQD avoids the measurement cost.
- Chapter 7: VQE as a DMET solver.
- Chapter 8 (planned): excited-state VQE.

**Core (first pass).** [[variational-quantum-eigensolver]], [[vqe-ansatze]], [[pauli-measurement-and-grouping]].

**Checkpoint.**
1. Show that one-parameter UCCD is exact for minimal-basis H$_2$.
2. Derive the optimal shot allocation $N_G\propto\sigma_G$ and the resulting $N=(\sum_G\sigma_G)^2/\epsilon^2$.
3. Show that $e^{\theta\hat A}=1+\sin\theta\,\hat A+(1-\cos\theta)\hat A^2$ for a fermionic excitation generator.
4. Compute the variance amplification of quadratic Richardson extrapolation through $\lambda=1,2,3$.

**Planned sections:** Classical shadows; Factorized measurement in rotated orbital bases; Probabilistic error cancellation.
