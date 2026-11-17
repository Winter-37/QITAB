---
id: error-mitigation-for-vqe
title: Error mitigation for VQE - zero-noise extrapolation, symmetry verification and readout correction on a noisy H₂ circuit
summary: A density-matrix simulation of the minimal-basis H₂ UCCD circuit at gate level (8 Pauli exponentials, 48 CNOTs) with two-qubit depolarizing noise p after every CNOT. At p = 10⁻³ the raw energy is 44.9 mEh above FCI; at 10⁻² it is 369 mEh above. Symmetry verification (keeping the N_α, N_β-parity sector) cuts the error by about 5×. Zero-noise extrapolation removes it almost completely when the extrapolation model fits the noise: exponential fit 0.001 mEh at p = 10⁻³ and 1.5 mEh at 10⁻²; linear and quadratic fits are much worse. Unitary folding (1×, 3×, 5×) works less well than ideal noise scaling. Readout flips of 2% add 55 mEh and are removed exactly by dividing each term by (1 − 2ε)^w. The mitigated estimates are no longer variational: symmetry verification combined with quadratic ZNE lands 7.2 mEh below FCI at p = 10⁻². Extrapolation also multiplies the shot noise, by a variance factor of 5 to 19.
status: in-progress
kind: algorithm
level: advanced
tags: [VQE, error-mitigation, zero-noise-extrapolation, symmetry-verification, readout-error, depolarizing-noise, density-matrix]
prerequisites: [variational-quantum-eigensolver, pauli-measurement-and-grouping, qubit-tapering]
related: [adapt-vqe, vqe-ansatze, ensembles-and-unitary-freedom, controlled-operations]
order: 50
date: 2026-11-17
---

## Overview

Without error correction, every gate on today's hardware has an error rate of roughly $10^{-3}$–$10^{-2}$ per two-qubit gate, and readout misreports bits at a similar rate. In VQE these errors bias the estimated energy far more than chemical accuracy allows, even for the smallest molecule. **Error mitigation** does not correct the state. It post-processes many noisy measurements into a less biased estimate of an expectation value, paying in extra shots. This note simulates the effect of noise on a real circuit and tests three standard techniques on it.

**Model.**
- Minimal-basis H₂ at 0.735 Å, 4 qubits, Jordan–Wigner, start $|1100\rangle$.
- One-parameter UCCD $e^{\theta\hat A}$ with $\hat A=\hat\tau-\hat\tau^\dagger$ and $\hat\tau=a_2^\dagger a_3^\dagger a_1a_0$. $\hat A$ is a sum of **8 mutually commuting Pauli strings**, each with coefficient $\pm i/8$, so $e^{\theta\hat A}$ is exactly a product of 8 Pauli exponentials.
- Each exponential $e^{-i\phi P}$ is a basis change ($H$ for $X$, $HS^\dagger$ for $Y$), a CNOT ladder over the 4 qubits, $R_z$, and the inverse. That makes 6 CNOTs per string, **48 CNOTs** in total.
- The circuit reproduces $e^{\theta\hat A}|1100\rangle$ exactly, and at $\theta^*=-0.1117685$ gives the FCI energy $-1.1373060358\,E_h$ ([[variational-quantum-eigensolver]]).
- **Noise:** after every CNOT, a two-qubit depolarizing channel $\rho\mapsto(1-p)\rho+\frac{p}{15}\sum_{P\ne II}P\rho P$ on its two qubits. Single-qubit gates are noiseless. The state is a density matrix throughout ([[ensembles-and-unitary-freedom]]).

## The raw damage

| $p$ per CNOT | $E-E_{\text{FCI}}$ (m$E_h$) | probability of staying in the right symmetry sector |
|---|---:|---:|
| $10^{-3}$ | 44.85 | 0.967 |
| $5\times10^{-3}$ | 205.3 | 0.847 |
| $10^{-2}$ | 369.3 | 0.726 |

Even at $p=10^{-3}$ the error is 28 times chemical accuracy. A rough estimate shows why. With 48 CNOTs, an error occurs somewhere with probability $\approx48p\approx5\%$. An error scrambles the state toward the maximally mixed state, whose energy $\operatorname{tr}\hat H/16=c_I$ lies about 1 $E_h$ above the ground state. So the bias is $\approx0.05\,E_h$.

Depolarizing noise raises the energy, so the raw values stay **above** FCI. Re-optimizing $\theta$ under noise ($p=10^{-2}$) moves it only from $-0.1118$ to $-0.1076$ and recovers 0.02 m$E_h$. The optimizer cannot fix a bias that a better circuit parameter cannot remove.

## Symmetry verification

The exact state has $N_\alpha=N_\beta=1$. The projector onto odd $N_\alpha$ and odd $N_\beta$ parity is

$$
\hat\Pi=\tfrac14(1-Z_0Z_2)(1-Z_1Z_3)
$$

(the $\mathbb Z_2$ symmetries of [[qubit-tapering]]; for 2 spatial orbitals odd parity means exactly one electron per spin). The verified energy is

$$
E_{\text{SV}}=\frac{\operatorname{tr}(\hat H\hat\Pi\rho)}{\operatorname{tr}(\hat\Pi\rho)} ,
$$

which is the energy of the state post-selected on the right symmetry. Diagonal terms can be post-selected shot by shot. For the off-diagonal terms ($XXYY$ type) the symmetry cannot be read off the same shots. Instead $\hat H\hat\Pi$ is expanded into Pauli strings and measured (Bonet-Monroig et al. 2018), or the symmetry is checked with an ancilla.

| $p$ | raw | SV | fraction kept |
|---|---:|---:|---:|
| $10^{-3}$ | 44.85 | 7.17 | 0.967 |
| $5\times10^{-3}$ | 205.3 | 37.65 | 0.847 |
| $10^{-2}$ | 369.3 | 79.61 | 0.726 |

The error falls by 4.6–6.3×, but what remains is errors that kept the state inside the symmetry sector. Their effect cannot be detected by symmetry alone. Post-selection discards $1-\operatorname{tr}(\hat\Pi\rho)$ of the shots, so the shot cost rises by $1/\operatorname{tr}(\hat\Pi\rho)$.

## Zero-noise extrapolation

**Idea** (Temme, Bravyi and Gambetta 2017). Measure $E(\lambda)$ at amplified noise levels $\lambda=1,2,3,\ldots$ and extrapolate to $\lambda=0$. Two ways to amplify:

- **Noise scaling** $p\to\lambda p$. This is the ideal version, achievable on hardware by stretching gate pulses.
- **Unitary folding** $G\to G(G^\dagger G)^k$, which needs only gates. It gives $\lambda=1,3,5$, and each fold adds the CNOTs of $G^\dagger G$ (Giurgica-Tiron et al. 2020).

Three extrapolation models are fitted through the points:
- linear through the first two;
- quadratic (Richardson) through three;
- exponential $E(\lambda)=a+b\,r^{\lambda}$ through three equally spaced points, solved exactly.

Errors in m$E_h$ relative to FCI:

| $p$ | raw | scaling: linear | quadratic | exponential | folding: linear | quadratic | exponential | SV + quadratic scaling |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| $10^{-3}$ | 44.85 | 1.977 | 0.088 | 0.001 | 2.984 | 0.227 | 0.008 | −0.001 |
| $5\times10^{-3}$ | 205.3 | 41.35 | 8.431 | 0.166 | 58.72 | 18.80 | 0.996 | −0.513 |
| $10^{-2}$ | 369.3 | 133.4 | 48.78 | 1.493 | 177.6 | 93.52 | 7.595 | −7.212 |

- **The model matters more than the method.** Depolarizing noise makes each Pauli expectation decay roughly exponentially with the number of errors, so the exponential fit nearly removes the bias. Polynomials fit badly once $48p$ is no longer small. On hardware the noise is not purely depolarizing, and no model is exact.
- **Folding is worse than ideal scaling.** Its points are further from $\lambda=0$ (3 and 5 rather than 2 and 3), so the extrapolation reaches further.
- **Extrapolation amplifies shot noise.** The estimate is $\sum_j\gamma_jE(\lambda_j)$ with Lagrange weights $\gamma_j$. With independent shot noise of equal variance at each point, the variance grows by $\sum_j\gamma_j^2$:
    - linear through $\lambda=1,2$: $\gamma=(2,-1)$, factor 5;
    - quadratic through $1,2,3$: $\gamma=(3,-3,1)$, factor 19;
    - quadratic through $1,3,5$: $\gamma=(\tfrac{15}{8},-\tfrac54,\tfrac38)$, factor 5.2.

    For the same final error bar, the quadratic scaled estimate needs about 19 times as many shots per point.

## The variational bound is lost

Mitigated estimates are no longer expectation values of a physical state, so they need not lie above FCI. Combining symmetry verification with quadratic extrapolation gives **−7.2 m$E_h$** at $p=10^{-2}$, *below* the exact energy. Two consequences:
- a lower mitigated energy does not mean a better circuit;
- mitigated energies should not be fed to an optimizer that assumes variationality without care.

## Readout errors

**Model:** each qubit's outcome flips independently with probability $\varepsilon$. For a Pauli string of weight $w$, measured as a product of $w$ bits,

$$
\langle P\rangle_{\text{meas}}=(1-2\varepsilon)^w\langle P\rangle ,
$$

checked by sampling $\langle ZZZZ\rangle$ (400,000 shots): 0.8500 sampled against 0.8493 predicted. With $\varepsilon=0.02$ and noiseless gates, this alone puts the energy 55.2 m$E_h$ above FCI. Dividing each measured term by $(1-2\varepsilon)^w$ removes the bias exactly, to $10^{-11}$ m$E_h$. Real readout errors are asymmetric and correlated; then the full confusion matrix is measured and inverted, or tensored approximations are used.

## What to take from this

1. **Mitigation is needed at chemical accuracy even for H₂.** Its cost grows with circuit size: the raw bias scales with the expected number of errors, (number of gates) × $p$. That is a strong argument for short circuits such as ADAPT ([[adapt-vqe]]) and for sampling-based methods that use the device less.
2. **Cheap fixes first.** Readout correction and symmetry verification are cheap and safe; they remove errors that are detectable or well characterized.
3. **Extrapolation is powerful but model-dependent** and expensive in shots. Its result should be reported with the model used and an error bar that includes the amplification.
4. **Not covered here:** probabilistic error cancellation (Temme et al. 2017), which needs a characterized noise model and has an exponential sampling overhead; virtual distillation; and N-representability-based purification of measured RDMs.

## Source

- K. Temme, S. Bravyi and J. M. Gambetta, "Error mitigation for short-depth quantum circuits", *Phys. Rev. Lett.* **119**, 180509 (2017), arXiv:1612.02058 (zero-noise extrapolation, probabilistic error cancellation).
- T. Giurgica-Tiron, Y. Hindy, R. LaRose, A. Mari and W. J. Zeng, "Digital zero noise extrapolation for quantum error mitigation", *2020 IEEE International Conference on Quantum Computing and Engineering (QCE)*, doi:10.1109/QCE49297.2020.00045 (unitary folding).
- X. Bonet-Monroig, R. Sagastizabal, M. Singh and T. E. O'Brien, "Low-cost error mitigation by symmetry verification", *Phys. Rev. A* **98**, 062339 (2018).
- R. Sagastizabal et al., "Experimental error mitigation via symmetry verification in a variational quantum eigensolver", *Phys. Rev. A* **100**, 010302 (2019).
- J. Tilly et al., *Phys. Rep.* **986**, 1 (2022), Sec. 8 (review).
- All numbers are computed in `qcchem/part6_ch3_vqe.py` (section C).
