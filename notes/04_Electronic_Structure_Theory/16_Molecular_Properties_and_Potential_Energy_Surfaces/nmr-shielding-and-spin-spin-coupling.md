---
id: nmr-shielding-and-spin-spin-coupling
title: NMR parameters - the spin Hamiltonian, nuclear shielding (Ramsey's dia and para terms, GIAO) and indirect spin-spin coupling (DSO, PSO, FC, SD)
summary: NMR spectra are described by an effective spin Hamiltonian with two electronic parameters, the shielding tensor σ_K and the reduced indirect coupling tensor K_KL, both mixed second derivatives of the electronic energy. Shielding couples the external field to a nuclear moment through an orbital Zeeman–paramagnetic spin–orbit response plus a diamagnetic expectation value, and inherits the gauge-origin problem of the magnetizability. Spin–spin coupling has four Ramsey terms, of which the Fermi contact term is usually dominant and needs tight s functions. The Bloch equations and the rotating frame describe the experiment itself. Recomputed: He (Lamb formula), water shieldings with and without GIAO, and J(H,D) with its four parts.
status: in-progress
kind: theory
level: intermediate
tags: [nmr, nuclear-shielding, chemical-shift, spin-spin-coupling, fermi-contact, paramagnetic-spin-orbit, giao, ramsey, bloch-equations, karplus]
prerequisites: [magnetizability-and-gauge-origin, exact-state-response-functions]
related: [hyperfine-coupling-and-epr, cphf-closed-shell, spin-operators, hyperfine-splitting-hydrogen, linear-response-for-variational-wave-functions]
conventions: [atomic-units]
key: sigma
order: 100
date: 2026-11-24
---

Atomic units: $\hbar = e = m_e = 1$, electron charge $-1$, $\mu_0/4\pi = \alpha^2$. $\mathbf m_K = \gamma_K\hat{\mathbf I}_K$ is the magnetic moment of nucleus $K$ with gyromagnetic ratio $\gamma_K = g_K\mu_N/\hbar$. $\mathbf r_{iK} = \mathbf r_i - \mathbf R_K$, $\mathbf r_{iO}$ is relative to the gauge origin, $\hat{\mathbf l}_{iK} = \mathbf r_{iK}\times\hat{\mathbf p}_i$. Response functions as in [[exact-state-response-functions]].

## The NMR experiment in brief

**One spin in a static field.** For a bare nucleus in a field $\mathbf B_0 = B_0\mathbf e_z$, $\hat H_0 = -\gamma\hat{\mathbf I}\cdot\mathbf B_0$. The levels are $E = -\gamma\hbar m_IB_0$, and the spin precesses about the field at the Larmor frequency $\omega_0 = -\gamma B_0$: $d\langle\hat{\mathbf I}\rangle/dt = \gamma\langle\hat{\mathbf I}\rangle\times\mathbf B_0$ (NRS Eqs. 8.267–8.273).

**Radio-frequency pulses.** A pulse $B_1\cos\omega_{\rm ref}t$ along $x$ is split into two counter-rotating circular components; only the co-rotating one matters (rotating-wave approximation). In the frame rotating at $\omega_{\rm ref}$, the spin Hamiltonian becomes time independent, $\hat H_R = (\omega_0 - \omega_{\rm ref})\hat I_z + \omega_{\rm nut}\hat I_x$ (NRS Eq. 8.286). At resonance the spin nutates about $x$, and a pulse of duration $\tau_p$ rotates it by the flip angle $\beta_p = \omega_{\rm nut}\tau_p$: $\pi/2$ for a free-induction decay, $\pi$ for inversion.

**The macroscopic picture.** Replacing $\hat{\mathbf I}$ by the magnetization $\mathbf M$ and adding phenomenological relaxation gives the Bloch equations:

- longitudinal relaxation $M_z(t) = M_{\rm eq}(1 - e^{-t/T_1})$ toward equilibrium;
- transverse dephasing $M_\perp\propto e^{-t/T_2}$ (NRS Eqs. 8.295–8.296).

The detected signal is the Fourier transform of the decaying transverse magnetization. Its line positions are what electronic-structure theory predicts.

## The NMR spin Hamiltonian

The electrons modify the field each nucleus feels and couple the nuclear moments to each other (NRS Eq. 8.297):

$$
\hat H_{\rm NMR} = -\sum_K\hat{\mathbf m}_K\cdot(\mathbf 1 - \boldsymbol\sigma_K)\cdot\mathbf B_0 + \tfrac12\sum_{K\neq L}\hat{\mathbf m}_K\cdot(\mathbf D_{KL} + \mathbf K_{KL})\cdot\hat{\mathbf m}_L.
\label{hnmr}
$$

- **Shielding.** $\boldsymbol\sigma_K$ is the shielding tensor, of order $10^{-6}$–$10^{-3}$, quoted in ppm.
- **Direct coupling.** $\mathbf D_{KL}$ is the classical dipole–dipole coupling, which averages to zero in isotropic liquids.
- **Indirect coupling.** $\mathbf K_{KL}$ is the reduced indirect coupling, transmitted by the electrons. Experiment reports $J_{KL}$ in Hz, with $2\pi J_{KL} = \gamma_K\gamma_LK_{KL}$ (NRS Eq. 8.301), so that $hJ_{KL}\hat{\mathbf I}_K\cdot\hat{\mathbf I}_L$ is the coupling energy.

**In liquids.** Only the isotropic parts $\sigma^{\rm iso} = \tfrac13\mathrm{tr}\,\boldsymbol\sigma$ and $J^{\rm iso}$ survive. The resonance of $K$ is at $\nu_K = \gamma_K(1-\sigma^{\rm iso}_K)B_0/2\pi$, and the chemical shift relative to a reference is

$$
\delta_K = \frac{\nu_K - \nu_{\rm ref}}{\nu_{\rm ref}} = \frac{\sigma_{\rm ref} - \sigma_K}{1 - \sigma_{\rm ref}}\approx\sigma_{\rm ref} - \sigma_K .
$$

**Mapping onto electronic structure.** Comparing with the energy expansion $E(\mathbf B_0,\{\mathbf m_K\})$ identifies $\sigma_{K,\alpha\beta} = \partial^2E/\partial m_{K,\alpha}\partial B_{0,\beta}$ and $K_{KL,\alpha\beta} = \partial^2E/\partial m_{K,\alpha}\partial m_{L,\beta}$ at zero field and moments.

## Electronic operators

The vector potential of a point nuclear dipole is $\mathbf A_K(\mathbf r) = \alpha^2\,\mathbf m_K\times\mathbf r_K/r_K^3$ (NRS Eq. 8.39). Inserting $\mathbf A_O + \sum_K\mathbf A_K$ into minimal coupling, and adding the interaction of the electron spin magnetization with the field of $\mathbf m_K$, gives the hyperfine operators of NRS Eqs. (8.41)–(8.45). With $g_e\approx2.0023$:

$$
\begin{aligned}
\hat h^{\rm pso}_K &= \alpha^2\sum_i\frac{\mathbf m_K\cdot\hat{\mathbf l}_{iK}}{r_{iK}^3}, &
\hat h^{\rm fc}_K &= \frac{4\pi g_e\alpha^2}{3}\sum_i\delta(\mathbf r_{iK})\,\hat{\mathbf s}_i\cdot\mathbf m_K,\\
\hat h^{\rm sd}_K &= \frac{g_e\alpha^2}{2}\sum_i\frac{3(\hat{\mathbf s}_i\cdot\mathbf r_{iK})(\mathbf r_{iK}\cdot\mathbf m_K) - r_{iK}^2\,\hat{\mathbf s}_i\cdot\mathbf m_K}{r_{iK}^5}, &
\hat h^{\rm dso}_{KL} &= \frac{\alpha^4}{2}\sum_i\frac{(\mathbf m_K\cdot\mathbf m_L)(\mathbf r_{iK}\cdot\mathbf r_{iL}) - (\mathbf m_K\cdot\mathbf r_{iL})(\mathbf r_{iK}\cdot\mathbf m_L)}{r_{iK}^3r_{iL}^3}.
\end{aligned}
\label{hfs}
$$

**Origin of each term.**

- **PSO** (paramagnetic spin–orbit) comes from $\mathbf A_K\cdot\hat{\mathbf p}$: the nuclear moment couples to the electronic orbital motion about the nucleus.
- **DSO** (diamagnetic spin–orbit) comes from the $\mathbf A_K\cdot\mathbf A_L$ part of $\tfrac12A^2$.
- **FC and SD** are the contact and dipolar parts of the field of $\mathbf m_K$ acting on the electron spin moment $-\tfrac{g_e}{2}\hat{\mathbf s}$.

PSO and DSO are spin-free (singlet) operators. FC and SD are triplet operators: for a closed-shell reference they connect only to triplet excited states.

**Diamagnetic shielding operator.** The term bilinear in $\mathbf B_0$ and $\mathbf m_K$ is the cross term $\mathbf A_O\cdot\mathbf A_K$:

$$
\hat h^{\rm dia}_{BK} = \frac{\alpha^2}{2}\sum_i\frac{(\mathbf B_0\cdot\mathbf m_K)(\mathbf r_{iO}\cdot\mathbf r_{iK}) - (\mathbf B_0\cdot\mathbf r_{iK})(\mathbf r_{iO}\cdot\mathbf m_K)}{r_{iK}^3}\qquad\text{(NRS Eq. 8.308)}.
$$

## Shielding

For a closed-shell molecule (NRS Eq. 8.307), the shielding is the sum of an expectation value and a linear response:

$$
\sigma_{K,\alpha\beta} = \underbrace{\frac{\alpha^2}{2}\Big\langle0\Big|\sum_i\frac{\mathbf r_{iO}\cdot\mathbf r_{iK}\,\delta_{\alpha\beta} - r_{iO,\alpha}r_{iK,\beta}}{r_{iK}^3}\Big|0\Big\rangle}_{\sigma^{\rm dia}}
\;\underbrace{-\;\alpha^2\sum_n{}'\frac{\mathrm{Re}\,\langle0|\hat L_{O,\beta}|n\rangle\langle n|\sum_i\hat l_{iK,\alpha}/r_{iK}^3|0\rangle}{\omega_{n0}}}_{\sigma^{\rm para}}.
\label{sigma}
$$

The paramagnetic term is the response of the PSO operator to the orbital Zeeman operator $\tfrac12\mathbf B\cdot\hat{\mathbf L}_O$. It is the second-order energy $-2\sum'\mathrm{Re}\,V_{0n}W_{n0}/\omega_{n0}$ for the two perturbations. (The tensor index order, $\alpha$ for the nuclear moment and $\beta$ for the field, matters only for the antisymmetric part, which does not enter $\sigma^{\rm iso}$.)

**Ramsey's picture.**

- **Diamagnetic part.** $\sigma^{\rm dia}$ is positive (shielding): induced Larmor currents of the ground-state density oppose the field at the nucleus.
- **Paramagnetic part.** $\sigma^{\rm para}$ is usually negative (deshielding). It mixes in excited states that carry orbital angular momentum about both the origin and the nucleus. Low-lying excitations with large $\hat L$ matrix elements (n → π* in carbonyls, transition metals) give large negative values.
- **Shift ranges.** This is why ¹H shifts span ~10 ppm while ¹⁷O and heavy-nucleus shifts span hundreds to thousands.

**Atoms: the Lamb formula.** With the origin at the nucleus of a $^1S$ atom, $\sigma^{\rm para} = 0$ and $\sigma = \tfrac{\alpha^2}{3}\langle0|\sum_i r_{iK}^{-1}|0\rangle$. The shielding is fixed by the electrostatic potential the electrons create at the nucleus.

**Gauge origin.** The split in Eq. [[#sigma]] depends on $\mathbf O$, and so does the total in a finite basis, as for the magnetizability ([[magnetizability-and-gauge-origin]]). GIAO (London) orbitals remove the dependence and are standard in every program. Shieldings converge faster than magnetizabilities because $\hat h^{\rm pso}_K$ is local to the nucleus, but they need core flexibility for the same reason.

**Relativity.** In the four-component theory there is a single response function, $\langle\langle\hat h^{\rm hfs}_{K,\rm rel};\hat h^{\rm Z}_{\rm rel}\rangle\rangle$, and the diamagnetic term emerges from negative-energy (positronic) states (NRS Eq. 8.309). Heavy-atom effects on light neighbours (the HALA effect, through spin–orbit coupling) shift ¹H and ¹³C resonances near iodine or mercury by many ppm.

## Indirect spin–spin coupling

For closed-shell molecules (NRS Eq. 8.310):

$$
K_{KL,\alpha\beta} = \frac{\partial^2}{\partial m_{K,\alpha}\partial m_{L,\beta}}\Big[\langle0|\hat h^{\rm dso}_{KL}|0\rangle + \langle\langle\hat h^{\rm pso}_K;\hat h^{\rm pso}_L\rangle\rangle_0 + \langle\langle\hat h^{\rm fc}_K + \hat h^{\rm sd}_K;\hat h^{\rm fc}_L + \hat h^{\rm sd}_L\rangle\rangle_0\Big].
\label{kkl}
$$

**Properties of the four terms.**

- **Ramsey's four contributions.** DSO, PSO, FC and SD, plus the FC/SD cross term, which is traceless and does not enter $J^{\rm iso}$.
- **FC dominates.** The Fermi contact term usually dominates $J^{\rm iso}$, especially for couplings through bonds to hydrogen and carbon.
- **Spin polarization.** FC transmits the coupling by spin polarization: the nuclear moment polarizes the electron spin density at its own nucleus, the polarization propagates through the bonds, and the spin density at the other nucleus feels it. Hence signs alternate with the number of bonds, and the dihedral dependence of vicinal $^3J_{\rm HH}$ follows the Karplus curve (NRS Fig. 8.52).

**Computational requirements.**

- **Tight s functions.** The FC operator samples the response density at a point, so the basis needs tight s functions (as for the hyperfine coupling of [[hyperfine-coupling-and-epr]]). Contracted valence basis sets give erratic results (worked example).
- **Triplet stability.** The FC and SD responses use the triplet response matrix. A closed-shell HF reference close to a triplet instability (the triplet orbital Hessian nearly singular, see [[rhf-instabilities-and-multiple-solutions]]) gives grossly overestimated FC terms. N₂ and CO are notorious cases at the HF level. Correlated methods are needed; DFT is less affected, the more so the less exact exchange the functional contains.
- **Response approach.** With the nuclear moments as perturbations, each of the $N_{\rm nuc}$ nuclei needs 3 (PSO) + 3 (FC/SD triplet) + … response equations, independent of the number of couplings wanted.

## Worked example

!!! example "Shieldings and the H–D coupling (recomputed for this note)"
    PySCF 2.15 `pyscf.prop.nmr` (GIAO unless a common origin is set) and `pyscf.prop.ssc`.

    **He, HF/aug-cc-pVTZ.** The Lamb formula gives $\tfrac{\alpha^2}{3}\langle\sum_ir_i^{-1}\rangle = 59.88$ ppm, identical to the GIAO shielding (59.88 ppm). Only the diamagnetic term survives for an atom.

    **Water, HF/aug-cc-pVTZ.** Geometry $r_{\rm OH} = 0.9572$ Å, $\angle$HOH $= 104.5^\circ$; $\sigma^{\rm iso}$ in ppm:

    | | O | H |
    |---|---:|---:|
    | GIAO | 328.51 | 30.73 |
    | common origin at O | 328.37 | 30.86 |
    | common origin 3 bohr along the $C_2$ axis | 343.71 | 20.97 |

    - **Origin at O.** A common origin at the oxygen is nearly as good as GIAO for O, because the PSO operator at O is small away from O.
    - **Distant origin.** An origin 1.6 Å away makes the proton shielding 10 ppm wrong, larger than the whole ¹H shift range.
    - **GIAO split.** O: $\sigma^{\rm dia} = 377.2$, $\sigma^{\rm para} = -48.7$; H: $29.9 + 0.9$ ppm. With GIAO the split itself has no unique meaning, but the paramagnetic O term is clearly the smaller one in water.

    **J(H,D) in HD**, $R = 0.7414$ Å, from the computed $K_{\rm HH}$ with $g_{\rm H} = 5.585695$ and $g_{\rm D} = 0.857438$. In Hz:

    | method/basis | DSO | PSO | FC | SD | total |
    |---|---:|---:|---:|---:|---:|
    | RHF/cc-pVTZ | −0.31 | 0.77 | 46.43 | 0.58 | 47.47 |
    | B3LYP/cc-pVTZ | −0.30 | 0.76 | 42.79 | 0.52 | 43.76 |
    | RHF/aug-cc-pVQZ | −0.32 | 0.82 | 55.36 | 0.41 | 56.27 |
    | B3LYP/aug-cc-pVQZ | −0.32 | 0.81 | 51.55 | 0.32 | 52.36 |

    - **FC dominance.** FC is 97–98% of the total.
    - **Contracted sets are not monotonic.** Contracted aug-cc-pVQZ gives a larger FC (55.4 Hz, RHF) than its own uncontracted primitives (46.9 Hz), although the uncontracted set spans the contracted one. The contraction coefficients are optimized for energies, not for the density at the nucleus.
    - **Uncontracted plus tight s.** Adding tight s functions (exponents $4^k$ times the largest, $k = 1$–$6$) to uncontracted aug-cc-pVQZ converges the FC term: RHF 46.9 → 51.7 → 52.9 → 53.2 Hz for 0, 2, 4, 6 extra functions; B3LYP 42.5 → 47.0 → 48.1 → 48.4 Hz.
    - **Against experiment.** The experimental coupling is about 43 Hz (to verify; it includes vibrational averaging). Both converged values are too large, HF by more. The good agreement in the small cc-pVTZ basis is a cancellation of basis and method errors.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 8.8.1, Eqs. (8.267)–(8.296); Sec. 8.8.2, Eqs. (8.297)–(8.311), Fig. 8.52 (described); Sec. 8.1.2.1, Eqs. (8.37)–(8.45) for the hyperfine operators. The Karplus relation and the N₂/CO triplet-instability examples are general knowledge, not taken from NRS. The calculations are in `Claude outputs/part4_response_batchB2.py`, section B.
