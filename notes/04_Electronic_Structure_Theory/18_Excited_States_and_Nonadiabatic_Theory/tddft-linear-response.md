---
id: tddft-linear-response
title: TDDFT linear response - the Kohn-Sham quasienergy, the adiabatic approximation, the exchange-correlation kernel in the A and B matrices, and why beryllium's triplet is stable in B3LYP but not in Hartree-Fock
summary: Time-dependent Kohn-Sham response has the same structure as TDHF. The linear response function is −Ω[1]†(E[2] − ωS[2])⁻¹V[1], but the Hessian comes from a Kohn-Sham quasienergy functional. Exact exchange is scaled by the hybrid fraction c_x, and an exchange-correlation kernel f_xc = δ²E_xc/δρδρ is added. In the adiabatic approximation f_xc is the second derivative of the ground-state functional, local in time. For closed shells and LDA the singlet A and B matrices get 2∫f_xc φ_iφ_aφ_jφ_b in addition to 2(ia|jb), and the triplet ones ∫(f↑↑ − f↑↓)φ_iφ_aφ_jφ_b; both verified against PySCF to 10⁻¹⁵. For beryllium/6-31G the kernel removes the HF triplet instability: B3LYP puts the 2p ³P state at 2.08 eV and 2p ¹P at 5.30 eV (NRS: 2.05 and 5.30; experiment 2.32 and 5.28).
status: in-progress
kind: theory
level: advanced
tags: [tddft, linear-response, exchange-correlation-kernel, adiabatic-approximation, casida, triplet-instability, b3lyp, excitation-energies]
prerequisites: [linear-response-for-variational-wave-functions, kohn-sham-dft, exchange-correlation-functionals]
related: [quasienergy-and-time-dependent-variational-principle, polarization-propagator-rpa, dft-versus-hartree-fock, residue-analysis-of-response-functions, damped-response-and-absorption-cross-sections]
conventions: [ia-letters, spatial-orbitals, chemists-integrals, atomic-units]
key: tddftab
order: 10
date: 2026-11-24
---

Atomic units; closed-shell Kohn-Sham reference with real spatial orbitals $\phi_p$, $i,j$ occupied, $a,b$ virtual, orbital energies $\varepsilon_p$. $(pq|rs)$ are chemists' integrals. $c_x$ is the fraction of exact exchange ($c_x = 0$ for LDA/GGA, $0.2$ for B3LYP, $1$ for HF). Matrices use unit-normalized singlet and triplet excitation operators (NRS's are larger by 2).

## From TDHF to TDDFT

**Quasienergy functional.** In the Kohn-Sham reference system the time-averaged quasienergy ([[quasienergy-and-time-dependent-variational-principle]]) is written as a functional of the time-dependent density,

$$
Q_T[\rho] = T_s[\rho] + V[\rho] + J[\rho] + Q_{xc}[\rho] - S_s[\rho],
$$

with $T_s$ the noninteracting kinetic energy, $V$ the external and field terms, $J$ the Hartree energy, $Q_{xc}$ the exchange-correlation quasienergy and $S_s$ the $i\partial_t$ term. Without $Q_{xc}$ this is TDHF without exchange.

**Recipe.** The parametrization is the same orbital rotation $e^{-i\hat\kappa}$ as for TDHF ([[linear-response-for-variational-wave-functions]]), so all formulas carry over. Only the Hessian changes:

1. switch off exact exchange, or scale it by $c_x$ for hybrids;
2. add the second derivative of $Q_{xc}$ with respect to the rotation parameters.

**Adiabatic approximation.** $Q_{xc}$ is replaced by the ground-state functional evaluated with the instantaneous density, $Q_{xc}[\rho]\to E_{xc}[\rho(t)] = \int e_{xc}(\rho(\mathbf r,t),\ldots)\,d\mathbf r$. The kernel is then local in time, i.e. frequency independent. (This is unrelated to the adiabatic, Born-Oppenheimer, approximation.)

## The A and B matrices with a kernel

**Derivation (LDA).** The density in the rotated state is $\rho(\mathbf r) = \sum_{pq}\phi_p\phi_q\langle0|e^{i\hat\kappa}\hat a^\dagger_p\hat a_qe^{-i\hat\kappa}|0\rangle$. Its first derivative with respect to a singlet rotation $ai$ is $\propto\phi_i\phi_a$. Its second derivatives give orbital-energy-like terms that combine with the $\partial E_{xc}/\partial\rho = v_{xc}$ parts into the KS orbital energies. By the chain rule, $\partial^2E_{xc}/\partial\kappa\partial\kappa'$ adds the term $\int(\partial^2e_{xc}/\partial\rho^2)(\partial\rho/\partial\kappa)(\partial\rho/\partial\kappa')\,d\mathbf r$. With spin, the second derivative splits into $f_{\uparrow\uparrow}$ and $f_{\uparrow\downarrow}$. Singlet rotations move both spins together, and triplet rotations move them oppositely, so the closed-shell kernels are $\tfrac12(f_{\uparrow\uparrow}+f_{\uparrow\downarrow})$ and $\tfrac12(f_{\uparrow\uparrow}-f_{\uparrow\downarrow})$ per spin pair. For an unpolarized density $f_{\uparrow\uparrow}+f_{\uparrow\downarrow} = 2f_{xc}$, with $f_{xc} = d^2(\rho\epsilon_{xc})/d\rho^2$ evaluated at the total density.

**Result.**

$$
\begin{aligned}
A^{\rm S}_{ia,jb} &= (\varepsilon_a-\varepsilon_i)\delta_{ij}\delta_{ab} + 2(ia|jb) - c_x(ij|ab) + 2\!\int\! f_{xc}\,\phi_i\phi_a\phi_j\phi_b\,d\mathbf r,\\
B^{\rm S}_{ia,jb} &= 2(ia|jb) - c_x(ib|ja) + 2\!\int\! f_{xc}\,\phi_i\phi_a\phi_j\phi_b\,d\mathbf r,\\
A^{\rm T}_{ia,jb} &= (\varepsilon_a-\varepsilon_i)\delta_{ij}\delta_{ab} - c_x(ij|ab) + \int(f_{\uparrow\uparrow}-f_{\uparrow\downarrow})\,\phi_i\phi_a\phi_j\phi_b\,d\mathbf r,\\
B^{\rm T}_{ia,jb} &= -c_x(ib|ja) + \int(f_{\uparrow\uparrow}-f_{\uparrow\downarrow})\,\phi_i\phi_a\phi_j\phi_b\,d\mathbf r.
\end{aligned}
\label{tddftab}
$$

This is the modern sign of $\mathbf B$, as in [[polarization-propagator-rpa]]; NRS's $\mathbf B$ has the opposite sign. Their Eq. (7.120) for the kernel term carries the sign of their $e^{-i\hat\kappa}$ phase convention. GGA and meta-GGA kernels add terms with gradients of $\phi_i\phi_a$ (not derived here).

**Structure.**

- **Same as TDHF otherwise.** Excitation energies are the paired eigenvalues of $\mathbf E^{[2]}\mathbf X = \lambda\mathbf S^{[2]}\mathbf X$, and the response function is the RPA expression.
- **Real orbitals.** $(\mathbf A-\mathbf B)$ contains neither the Coulomb nor the kernel term, and for $c_x = 0$ it is diagonal, $\varepsilon_a-\varepsilon_i$. This reduces the problem to the Hermitian form $(\mathbf A-\mathbf B)^{1/2}(\mathbf A+\mathbf B)(\mathbf A-\mathbf B)^{1/2}\mathbf Z = \omega^2\mathbf Z$ (Casida's equation; general knowledge).
- **Spin independence of $\mathbf A - \mathbf B$.** It is the same for singlets and triplets, so it is the singlet-triplet difference in $\mathbf A+\mathbf B$ that decides triplet stability.

## Why the kernel cures the beryllium triplet

**HF.** The triplet $\mathbf A$ contains $-c_x(ij|ab)$, with $c_x = 1$. For beryllium the Coulomb coupling between $2s$ and the two $p_z$ virtuals is large, $-2(2p\,3p|2s\,2s) = 0.158$ in NRS units. This drives an eigenvalue of the triplet (NRS) $\mathbf A-\mathbf B$ negative: the RHF triplet instability of [[linear-response-for-variational-wave-functions]].

**B3LYP.** Only 20% of this coupling is left, and the kernel term replaces the rest. The triplet Hessian becomes positive definite, and the lowest triplet excitation energy becomes real and close to experiment.

## Worked example

!!! example "Beryllium, 6-31G, B3LYP (NRS Tables 7.3-7.4; recomputed for this note with PySCF 2.15.1)"
    KS orbital energies: −4.0645 (1s), −0.2238 (2s), −0.0361 (2p), 0.2882 (3p), 0.3156 (3s). NRS list −4.0608, −0.2206, −0.0330, 0.2911 and 0.3186. The 3 mEh shift was not traced; it is presumably a difference in the B3LYP definition or grid. Blocks for $2s\to2p_z,3p_z$ in NRS's normalization and sign (NRS in parentheses; off-diagonal signs depend on orbital phases):

    | | $\mathbf A$ | $\mathbf B$ |
    |---|---|---|
    | singlet | 0.4192 (0.4193), 0.0249 (0.0249), 0.9100 (0.9099) | −0.1479 (−0.1481), −0.0488 (0.0488), −0.0072 (−0.0075) |
    | triplet | 0.1851 (0.1842), 0.0605 (0.0608), 0.8482 (0.8471) | 0.0862 (0.0869), 0.0366 (−0.0369), 0.0546 (0.0553) |

    - **Stability.** The triplet $\mathbf A-\mathbf B$ (NRS sign) has eigenvalues 0.0856 and 0.8069, both positive: stable, unlike HF ($-0.0274$).
    - **$\mathbf A+\mathbf B$.** It has eigenvalues 0.2704 and 0.9037 in both spin cases, as the structure above requires.

    | State | TDDFT/B3LYP (this note) | NRS 6-31G | NRS t-aug-cc-pVTZ | TDHF 6-31G | Experiment |
    |---|---:|---:|---:|---:|---:|
    | $2p\ {}^3P^o$ | 2.077 eV | 2.05 | 2.08 | imaginary | 2.32 |
    | $2p\ {}^1P^o$ | 5.300 eV | 5.30 | 4.89 | 5.158 | 5.28 |

!!! example "LDA kernel formula checked (computed for this note)"
    Water/6-31G, SVWN. $f_{xc}$ is taken from libxc on the PySCF integration grid and the kernel integrals are built on the grid.

    - **Singlet.** Eq. [[#tddftab]] reproduces PySCF's singlet $\mathbf A$ and $\mathbf B$ to $1\times10^{-15}$ with the factor 2 in front of $\int f_{xc}$. Factors 1 or 4 miss by 0.04-0.08.
    - **Triplet.** The triplet $\mathbf A$ matches to $10^{-16}$ with $\int(f_{\uparrow\uparrow}-f_{\uparrow\downarrow})$.
    - **Identity.** $f_{\uparrow\uparrow}+f_{\uparrow\downarrow} = 2f_{xc}$ holds to $10^{-15}$ relative wherever $\rho > 10^{-6}$.

## Limitations

These are general knowledge, not covered by NRS's section; mark for verification against a TDDFT text.

- **Adiabatic kernel.** A frequency-independent kernel cannot describe states of dominant double-excitation character.
- **Charge transfer.** With semilocal functionals, long-range charge-transfer excitations are strongly underestimated, because the kernel decays too fast and $\varepsilon_a-\varepsilon_i$ is too small. Range-separated hybrids are the usual remedy.
- **Instabilities remain possible.** Triplet instabilities can survive in hybrids with large $c_x$. The Tamm-Dancoff approximation ($\mathbf B = 0$) is often used then.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 7.3.1, Eqs. (7.114)–(7.120); Sec. 7.3.4, Tables 7.3–7.4 and Fig. 7.8. The closed-shell singlet and triplet kernel expressions of Eq. [[#tddftab]] are derived here and checked numerically; Casida's form is general knowledge. The calculations are in `Claude outputs/part4_response_batchA.py`, section H.
