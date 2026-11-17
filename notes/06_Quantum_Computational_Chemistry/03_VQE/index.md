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
- **Its costs are now well understood.** The number of shots needed for precision $\epsilon$ grows roughly as $(\sum_k|c_k|)^2/\epsilon^2$, which is very large for molecules at chemical accuracy. Random hardware-efficient circuits suffer from barren plateaus, gradients that vanish exponentially with qubit number. Noise biases the energy. These limitations motivated SQD (Chapter 5).

## Where it is used later

- [[dmet-with-quantum-solvers|VQE as a DMET fragment solver]] (Chapter 7).
- [[tilly-2022-vqe-review|Tilly et al. 2022]], the review this chapter draws on (Part 8).
- [[hao-2026-dmet-vqe-geometry|Hao et al. 2026]], which uses DMET-VQE for geometry optimization (Part 8).

## The main ideas, in order

1. **The algorithm.** The hybrid loop, and where the cost goes: shots, trainability and noise.
2. **Ansätze.** Hardware-efficient, unitary coupled cluster, symmetry-preserving and adaptive (ADAPT) circuits, compared on what they can represent and whether they can be trained.

## How to read it

**Path.**

1. The algorithm and where its cost goes (shots, trainability, noise).
2. Ansätze: hardware-efficient, unitary coupled cluster, symmetry-preserving, adaptive.

**Needs.** Chapter 2; Part 4, Chapter 11 for UCC.

**Leads to.** Chapter 5 (SQD avoids the measurement cost) and Chapter 7 (VQE as a DMET solver).

**Core (first pass).** [[variational-quantum-eigensolver]], [[vqe-ansatze]].

**Checkpoint.** Show that one-parameter UCCD is exact for minimal-basis H$_2$. Estimate the shots needed for 1.6 m$E_h$ from $\sum_k|c_k|$.

**Planned sections:** Measurement grouping and classical shadows; Error mitigation; Excited-state VQE.
