---
id: magnetizability-and-gauge-origin
title: Magnetizability - diamagnetic and paramagnetic parts, the gauge-origin problem, London orbitals and Pascal's rule
summary: A static magnetic field enters the Hamiltonian through a vector potential whose origin is arbitrary. For a closed-shell molecule the energy is lowered by −½B·ξ·B, with ξ the sum of a diamagnetic expectation value (always negative) and a paramagnetic linear response of the orbital angular momentum (always positive). Each part depends on the gauge origin; for exact states the dependence cancels through the hypervirial relation, in a finite basis it does not. London orbitals give every basis function its own origin and make the result origin independent in any basis. Recomputed: He, and PF₃ with and without London orbitals (NRS Table 8.5).
status: in-progress
kind: theory
level: intermediate
tags: [magnetizability, magnetic-susceptibility, gauge-origin, london-orbitals, giao, diamagnetism, paramagnetism, pascal-rule, orbital-zeeman]
prerequisites: [exact-state-response-functions, cphf-closed-shell, orbital-angular-momentum]
related: [nmr-shielding-and-spin-spin-coupling, optical-activity-ecd-and-mcd, zeeman-effect, polarizabilities-and-dispersion-coefficients, linear-response-for-variational-wave-functions]
conventions: [atomic-units]
key: xi-split
order: 90
date: 2026-11-24
---

Atomic units: $\hbar = e = m_e = 1$, so the electron charge is $-1$ and $\mu_0/4\pi = \alpha^2$ with $\alpha = 1/c$. $\mathbf r_i$ is the position of electron $i$, $\mathbf r_{iO} = \mathbf r_i - \mathbf O$ relative to the gauge origin $\mathbf O$, $\hat{\mathbf L}_O = \sum_i\mathbf r_{iO}\times\hat{\mathbf p}_i$. Exact states $|n\rangle$ with $\omega_{n0} = E_n - E_0$; $\sum'_n$ excludes $n = 0$. Response functions follow [[exact-state-response-functions]]: $\langle\langle A;B\rangle\rangle_0 = -2\sum'_n\mathrm{Re}\,A_{0n}B_{n0}/\omega_{n0}$ for real-symmetric pairs.

## The Hamiltonian in a static field

A uniform field $\mathbf B$ has the vector potential $\mathbf A(\mathbf r) = \tfrac12\mathbf B\times(\mathbf r - \mathbf O)$, with $\nabla\cdot\mathbf A = 0$. The origin $\mathbf O$ is arbitrary: moving it adds a gradient, $\mathbf A\to\mathbf A + \nabla\chi$ with $\chi = -\tfrac12(\mathbf B\times\mathbf D)\cdot\mathbf r$, which is a gauge transformation. Minimal coupling for charge $-1$, $\hat{\mathbf p}\to\hat{\mathbf p} + \mathbf A$, gives

$$
\hat H(\mathbf B) = \hat H_0 + \tfrac12\mathbf B\cdot\hat{\mathbf L}_O + \tfrac18\sum_i\big[B^2r_{iO}^2 - (\mathbf B\cdot\mathbf r_{iO})^2\big] + \tfrac{g_e}{2}\mathbf B\cdot\hat{\mathbf S}.
\label{hb}
$$

The linear term uses $\hat{\mathbf p}\cdot\mathbf A = \mathbf A\cdot\hat{\mathbf p}$ (Coulomb gauge) and $(\mathbf B\times\mathbf r)\cdot\hat{\mathbf p} = \mathbf B\cdot(\mathbf r\times\hat{\mathbf p})$. It is the orbital Zeeman term $-\hat{\mathbf m}\cdot\mathbf B$ with $\hat{\mathbf m} = -\tfrac12\hat{\mathbf L}_O$, the Bohr magneton being $\tfrac12$ in these units. The quadratic term is the diamagnetic operator. For a closed-shell singlet the spin term does nothing.

## Magnetizability as a second derivative

For a closed-shell molecule the permanent moment vanishes and

$$
E(\mathbf B) = E_0 - \tfrac12\,\xi_{\alpha\beta}B_\alpha B_\beta + \mathcal O(B^4),\qquad \xi_{\alpha\beta} = -\frac{\partial^2E}{\partial B_\alpha\partial B_\beta}\bigg|_0 .
$$

Rayleigh–Schrödinger perturbation theory with Eq. [[#hb]] gives two terms. The first-order energy of the quadratic operator gives the diamagnetic part, the second-order energy of the linear operator the paramagnetic part:

$$
\xi_{\alpha\beta} = \underbrace{-\tfrac14\Big\langle0\Big|\sum_i(r_{iO}^2\delta_{\alpha\beta} - r_{iO,\alpha}r_{iO,\beta})\Big|0\Big\rangle}_{\xi^{\rm dia}}
\;\underbrace{+\;\tfrac12\sum_n{}'\frac{\mathrm{Re}\,\langle0|\hat L_{O,\alpha}|n\rangle\langle n|\hat L_{O,\beta}|0\rangle}{\omega_{n0}}}_{\xi^{\rm para} = -\langle\langle\hat m_\alpha;\hat m_\beta\rangle\rangle_0}.
\label{xi-split}
$$

The paramagnetic term is the magnetic analogue of $\alpha = \langle\langle\hat\mu;-\hat\mu\rangle\rangle$. Signs:

- $\xi^{\rm dia}$ is negative definite (a negative multiple of the second moment of the density); isotropically $\bar\xi^{\rm dia} = -\tfrac16\langle\sum_ir_{iO}^2\rangle$, Langevin's result.
- $\xi^{\rm para}$ is positive semidefinite for the ground state, since every $\omega_{n0} > 0$.
- Nearly all closed-shell molecules are diamagnetic, $\bar\xi < 0$. Closed-shell paramagnets exist (BH, CH⁺ have low-lying states coupled by $\hat L$).

**Atoms.** For a $^1S$ atom with the origin at the nucleus, $\hat{\mathbf L}|0\rangle = 0$, so $\xi^{\rm para} = 0$ and $\xi = \xi^{\rm dia}$ exactly (NRS Eq. 8.150). This is the only case where one part vanishes.

## The gauge-origin problem

Shift the origin, $\mathbf O\to\mathbf O + \mathbf D$. Then $\hat{\mathbf L}_{O+D} = \hat{\mathbf L}_O - \mathbf D\times\hat{\mathbf P}$ with $\hat{\mathbf P} = \sum_i\hat{\mathbf p}_i$, and each part changes (NRS Eqs. 8.153–8.154):

- **Diamagnetic.** $\xi^{\rm dia}$ acquires terms linear in $\mathbf D$ (through $\langle\mathbf r\rangle$) and quadratic in $\mathbf D$ (through $N_e$).
- **Paramagnetic.** $\xi^{\rm para}$ acquires cross terms $\langle\langle\hat L;\hat P\rangle\rangle_0$ and a term $\propto\langle\langle\hat P;\hat P\rangle\rangle_0$.

For exact states the two changes cancel because of two exact identities:

- **Momentum–position.** $\langle0|\hat P_\alpha|n\rangle = i\omega_{n0}\langle0|\hat R_\alpha|n\rangle$ (from $[\hat H,\hat R_\alpha] = -i\hat P_\alpha$), which turns $\langle\langle\hat P_\alpha;\hat P_\beta\rangle\rangle_0$ into $-N_e\delta_{\alpha\beta}$ (the Thomas–Reiche–Kuhn sum rule) and cancels the $D^2$ term.
- **Cross terms.** The same relation turns $\langle\langle\hat L;\hat P\rangle\rangle_0$ into expectation values of $\mathbf r$, which cancel the linear terms (NRS Eqs. 8.155–8.156).

Both identities hold for variational methods only in a complete basis. In a finite basis the dia and para changes no longer cancel. The error grows quadratically with the distance between the origin and the molecule, and it is not small at ordinary distances (worked example below).

**Choosing an origin is not a fix.** The centre of mass or of charge is a reasonable choice for a small molecule but not for a large one, where every atom is far from any single origin. Results also change when a molecule is translated, and properties of a dimer are not the sum of the monomers at infinite separation.

## London orbitals

London's remedy is to give each basis function its own gauge origin, at its own centre $\mathbf R_\mu$:

$$
\chi_\mu^{\rm L}(\mathbf r;\mathbf B) = \exp\big[-i\mathbf A_O(\mathbf R_\mu)\cdot\mathbf r\big]\chi_\mu(\mathbf r),\qquad \mathbf A_O(\mathbf R_\mu) = \tfrac12\mathbf B\times(\mathbf R_\mu - \mathbf O).
\label{lao}
$$

**Why it works.** The phase factor converts the mechanical momentum acting on $\chi_\mu$ into one with the vector potential referred to $\mathbf R_\mu$ (NRS Eq. 8.158):

$$
(\hat{\mathbf p} + \mathbf A_O)\chi^{\rm L}_\mu = e^{-i\mathbf A_O(\mathbf R_\mu)\cdot\mathbf r}\,(\hat{\mathbf p} + \mathbf A_{R_\mu})\chi_\mu.
$$

A shift of the global origin multiplies every London orbital by a common gauge phase, which a gauge-invariant (variational) energy absorbs exactly. The magnetizability is therefore origin independent in any basis, for HF, DFT, MCSCF and other variational methods.

**Further properties** (NRS Sec. 8.4.1):

- **Exact for a free atom.** A London atomic orbital is an exact first-order solution for a one-electron atom in a field along $z$ (NRS Eq. 8.159). The basis therefore already carries the leading response, and basis-set convergence is much faster. The gain in accuracy matters more than the origin independence itself.
- **Field-dependent integrals.** The integrals depend on $\mathbf B$, so their field derivatives (gradient-like integrals) enter. The response equations are the coupled-perturbed HF equations of [[cphf-closed-shell]] with imaginary perturbations and a modified right-hand side.
- **Also known as GIAO** (gauge-including atomic orbitals) in the NMR literature, where they are standard ([[nmr-shielding-and-spin-spin-coupling]]).

**Other routes.** Other distributed-origin schemes exist: IGLO (individual gauges for localized orbitals) and CSGT (continuous set of gauge transformations). A complementary picture writes $\xi$ through the magnetically induced current density, $\xi_{\alpha\beta} = \frac{d^2}{dB_\alpha dB_\beta}\int\mathbf A\cdot\mathbf j(\mathbf r;\mathbf B)\,d^3r$ (NRS Eq. 8.160), which is where ring-current analyses of aromaticity start.

## Pascal's rule

Experimental magnetizabilities are measured as bulk susceptibilities, for example from the apparent weight change of a sample in an inhomogeneous field (Gouy balance, NRS Eq. 8.161).

**Pascal's rule.** These are, to good approximation, additive: $\xi\approx\sum_Kc_K\xi_K$ over elements $K$ with $c_K$ atoms each (NRS Eq. 8.162). The "atomic" increments are fitted, not the magnetizabilities of free atoms. Additivity holds because the induced currents are dominated by near-atomic circulation. For alkanes, fitting HF data gives $\xi_{\rm C} = -81.4$ and $\xi_{\rm H} = -56.4\times10^{-30}$ J T⁻² (NRS Sec. 8.4.3).

**Deviations.** Large deviations flag delocalized currents. Aromatic rings give an exalted, strongly anisotropic diamagnetism perpendicular to the ring. The same argument explains why London orbitals converge fast: they put the gauge origin where the currents are.

**Units.** The atomic unit of magnetizability is $e^2a_0^2/m_e = 7.891\times10^{-29}$ J T⁻². The molar susceptibility in cgs-emu is $\chi_m = \mu_0N_A\xi/4\pi$ (cm³ mol⁻¹ when the SI product is converted).

## Worked example

!!! example "He and PF₃ at the Hartree–Fock level (recomputed for this note)"
    PySCF 2.15 `pyscf.prop.magnetizability`, which uses London orbitals by default; setting `gauge_orig` switches to a common origin.

    **He atom, HF/aug-cc-pVTZ.**

    - $\bar\xi = -0.39569$ au $= -31.22\times10^{-30}$ J T⁻². This is exactly $-\tfrac16\langle\sum_ir_i^2\rangle = -0.39569$, since the paramagnetic part vanishes for an atom.
    - Molar susceptibility $\chi_m = -1.880\times10^{-6}$ cm³ mol⁻¹ (cgs-emu).

    **PF₃, HF.** Experimental geometry $r_{\rm PF} = 1.561$ Å, $\angle$FPF $= 97.8^\circ$, $C_3$ axis along $z$. $\bar\xi$ and the anisotropy $\Delta\xi = \xi_\parallel - \xi_\perp$ in au:

    | basis | London | origin at COM | origin at P | origin COM + 4 bohr along $z$ |
    |---|---:|---:|---:|---:|
    | aug-cc-pVDZ: $\bar\xi$ | −6.780 | −16.240 | −17.156 | −52.936 |
    | aug-cc-pVDZ: $\Delta\xi$ | −0.248 | −3.771 | −2.396 | +51.274 |
    | aug-cc-pVTZ: $\bar\xi$ | −6.645 | −11.291 | −11.084 | −32.667 |
    | aug-cc-pVTZ: $\Delta\xi$ | −0.327 | −0.913 | −1.224 | +31.151 |

    - **London values.** They change by 2% from DZ to TZ. NRS Table 8.5 gives −6.80 (London) and −16.55 (no London) at aug-cc-pVDZ. The London value agrees; the common-origin value depends on where NRS put the origin.
    - **Common-origin values.** At the centre of mass they are off by a factor 2.4 at DZ and still by 70% at TZ. Moving the origin 4 bohr, less than the molecule's own size, makes $\bar\xi$ eight times too large and turns the anisotropy positive.
    - **The lesson** is NRS's: with a common origin, even a triple-zeta basis gives no reliable magnetizability for a molecule with heavy atoms.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 8.4, Eqs. (8.148)–(8.162), Table 8.5, Figs. 8.11–8.12 (described); Sec. 8.4.1, Eqs. (8.153)–(8.159); Sec. 8.4.2, Eq. (8.160); Sec. 8.4.3, Eqs. (8.161)–(8.162). The operators of Eq. [[#hb]] are NRS Eqs. (8.81)–(8.83). The calculations are in `Claude outputs/part4_response_batchB2.py`, section A.
