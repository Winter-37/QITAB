What comes after CCSD: triples, alternative cluster ansätze, and excited states.

## What this chapter is about

CCSD alone is usually not accurate enough for thermochemistry, and full CCSDT is expensive, at $O(N^8)$. This chapter covers how to do better at affordable cost, and how to extend coupled cluster beyond ground-state energies:

- **Perturbation analysis.** Count orders in the fluctuation potential to see which triples terms matter most. This gives (T), [T], CC2, CC3 and the CCSDT-$n$ family.
- **The MP series.** When it converges and when it does not.
- **Alternative ansätze.** Variational, unitary and extended CC, and why their energy functionals do not terminate. Brueckner and orbital-optimized CC, quadratic CI, and open-shell variants.
- **Excited states.** Equation-of-motion CC treats excited states as a biorthogonal eigenvalue problem of the similarity-transformed Hamiltonian.

## Why it matters

- **CCSD(T) is the workhorse of high-accuracy chemistry.** Its non-iterative triples correction costs $O(N^7)$ once. It brings CCSD close to CCSDT for single-reference systems. Knowing its perturbative origin explains both its success and its failure for stretched bonds, where the perturbative triples correction becomes unreliable.
- **Convergence of perturbation series.** The analysis in terms of a two-state model and singularities in the complex plane explains intruder states and the erratic behaviour of MP$n$ with diffuse basis sets.
- **Unitary CC matters for quantum computing.** It is variational and unitary, so it can be implemented as a circuit. Its energy expansion does not terminate, which is why it is impractical classically and natural on quantum hardware.
- **Excited states with CC accuracy.** EOM-CCSD gives size-intensive excitation energies for singly excited states. It is a standard benchmark for TDDFT and for quantum excited-state algorithms.

## Where it is used later

- [[variational-quantum-eigensolver|VQE]] and [[vqe-ansatze|VQE ansätze]] (Part 6), which use unitary CC.
- [[hjo-calibration-energies-atomization-reactions-barriers|Calibration of CCSD(T)]] (Chapter 14).
- The planned excited-states chapter (Chapter 18), which starts from EOM-CC.

## How to read it

**Path.**

1. Coupled-cluster perturbation theory and the convergence of the MP series.
2. Perturbative triples: (T), [T], CC3 and the CCSDT-$n$ family.
3. Variational and unitary CC.
4. Brueckner, QCISD and open-shell variants.
5. EOM-CC for excited states.

**Reading.** Second-pass chapter: skip it on a first reading and come back after the core chapters (Chapter 5 first; it is the prerequisite for almost every deep note).

**Planned sections:** Full CCSDT; EOM-IP, EOM-EA and spin-flip.
