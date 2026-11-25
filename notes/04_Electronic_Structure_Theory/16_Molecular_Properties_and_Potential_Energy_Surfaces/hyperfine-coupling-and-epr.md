---
id: hyperfine-coupling-and-epr
title: Nuclear-electron interactions and EPR - finite nuclei and the Mössbauer isomer shift, hyperfine coupling, nuclear quadrupole coupling and electric field gradients, Zeeman splitting, the g-matrix and zero-field splitting
summary: Beyond the point-charge Coulomb attraction, nuclei interact with electrons through their finite size (the Mössbauer isomer shift measures the electron density at the nucleus), their magnetic dipole (hyperfine coupling, with Fermi-contact and spin-dipolar parts) and their electric quadrupole (coupling to the electric field gradient). An external field splits electronic levels (Zeeman effect, Landé g_J); in molecules these effects are collected in the EPR spin Hamiltonian μ_B B·g·S + I·A·S + S·D·S over a pseudo-spin. Recomputed: the H-atom hyperfine constant and its Gaussian-basis error, the Cs clock constant, the NQCC conversion factor, the field gradient at F in HF (NRS Table 8.3), Landé factors and Zeeman patterns of the Na D lines.
status: in-progress
kind: theory
level: intermediate
tags: [hyperfine-coupling, fermi-contact, epr, g-tensor, zero-field-splitting, nuclear-quadrupole, electric-field-gradient, nqcc, mossbauer, isomer-shift, finite-nucleus, zeeman, lande-g]
prerequisites: [nmr-shielding-and-spin-spin-coupling, hyperfine-splitting-hydrogen, zeeman-effect, addition-of-angular-momenta]
related: [magnetizability-and-gauge-origin, hydrogen-fine-structure, spherical-tensor-operators, spin-tensor-operators, rotational-selection-rules-and-wigner-eckart]
conventions: [atomic-units]
key: aiso
order: 110
date: 2026-11-24
---

Atomic units unless SI is shown ($\hbar = e = m_e = 1$, $\mu_0/4\pi = \alpha^2$). Nucleus $K$ has charge $Z_K$, spin $\hat{\mathbf I}_K$, moment $\mathbf m_K = \gamma_K\hat{\mathbf I}_K$ and, if $I_K\ge1$, quadrupole moment $Q_K$. $\rho_e(\mathbf r)$ is the electron number density; $\rho_s = \rho^\alpha - \rho^\beta$ the spin density.

## The nucleus as a finite charge

**Models.** A point nucleus is a convenient fiction. Real nuclei have rms charge radii of a few fm. Two finite models are common: a homogeneous sphere and a Gaussian, $\rho_n\propto e^{-r^2/R_G^2}$ with $\langle r_n^2\rangle = \tfrac32R_G^2$ (NRS Eqs. 8.1–8.17). The Gaussian model is popular because it fits Gaussian basis sets.

**Energy shift.** Split the electron–nucleus energy into the point-charge term and a correction from inside a small radius $r_c$. The electron density is nearly constant there, $\rho_e(\mathbf r)\approx\rho_e(0)$, and the correction becomes (NRS Eqs. 8.19–8.26)

$$
E_{eN} = \int\rho_e(\mathbf r)\phi^{\rm point}_n(\mathbf r)\,d^3r - \frac{Ze\rho_e}{6\varepsilon_0}\langle r_n^2\rangle\quad\text{(SI; }\rho_e\text{ the effective charge density at the nucleus)}.
\label{finite}
$$

The result depends on the model only through the mean-square radius. In relativistic calculations finite nuclei are essential: $s_{1/2}$ and $p_{1/2}$ Dirac spinors are weakly singular at a point nucleus.

**Mössbauer isomer shift.** A γ transition between nuclear states changes $\langle r_n^2\rangle$ by $\delta\langle r_n^2\rangle$, so its energy depends on the electron density at the nucleus. Absorber and source differ in chemical environment, and the Doppler velocity needed to bring them into resonance is the isomer shift (NRS Eqs. 8.27–8.30):

$$
\delta = \frac{c}{E_\gamma}(\Delta E^{\rm a}_\gamma - \Delta E^{\rm s}_\gamma) = \alpha_{\rm cal}\big(\rho^{\rm a}_e - \rho^{\rm s}_e\big),\qquad \alpha_{\rm cal} = -\frac{Zec}{6\varepsilon_0E_\gamma}\delta\langle r_n^2\rangle .
$$

**Computation.** Theory computes $\rho_e(0)$ for a series of compounds and fits $\alpha_{\rm cal}$ against measured shifts. ⁵⁷Fe is the standard case, where $\delta$ reports oxidation and spin state. The density at the nucleus is dominated by the core s shells, which feel valence changes only through screening. It therefore needs flexible core basis functions and, for iron and heavier elements, a relativistic Hamiltonian.

## Magnetic hyperfine interaction

**Origin.** A nuclear magnetic dipole produces the vector potential $\mathbf A_K = \alpha^2\mathbf m_K\times\mathbf r_K/r_K^3$ and the field (NRS Eq. 8.40)

$$
\mathbf B_K(\mathbf r) = \alpha^2\Big[\frac{8\pi}{3}\mathbf m_K\delta(\mathbf r_K) - \frac{\mathbf m_Kr_K^2 - 3\mathbf r_K(\mathbf r_K\cdot\mathbf m_K)}{r_K^5}\Big].
$$

Coupling to the electron orbital motion and spin gives the PSO, FC and SD operators, and the DSO term between two nuclei, listed in [[nmr-shielding-and-spin-spin-coupling]] (NRS Eqs. 8.41–8.45). In a closed-shell molecule they act only in second order (NMR). In an open-shell system the expectation values are first order: this is hyperfine coupling.

**Atoms.** Within a fine-structure level $J$, the Wigner–Eckart theorem reduces the interaction to $\hat H_K = A(J)\,\hat{\mathbf I}\cdot\hat{\mathbf J}$ (NRS Eq. 8.48). Coupling to $\mathbf F = \mathbf I + \mathbf J$ gives

$$
E_{\rm hfs}(F) = \tfrac12A(J)\big[F(F+1) - I(I+1) - J(J+1)\big],\qquad E(F) - E(F-1) = A(J)\,F,
\label{interval}
$$

Landé's interval rule (NRS Eqs. 8.50–8.53). Deviations from it were the first evidence of nuclear quadrupole moments (Schüler and Schmidt, 1935).

**Fermi contact for one s electron.** For an $S = \tfrac12$ state the isotropic constant comes from the FC operator alone:

$$
a_{\rm iso} = \frac{2\mu_0}{3h}\,g_e\mu_B\,g_K\mu_N\,\rho_s(\mathbf R_K)\quad\text{(SI, in Hz)},
\label{aiso}
$$

with $\rho_s$ normalized to one unpaired electron. For hydrogen $\rho_s(0) = |\psi_{1s}(0)|^2 = 1/\pi a_0^3$. This is the 21-cm line of [[hyperfine-splitting-hydrogen]].

**Molecules.** The effective Hamiltonian becomes $\hat H_K = \hat{\mathbf I}_K\cdot\mathbf A_K\cdot\hat{\mathbb S}$ with a $3\times3$ hyperfine matrix and a pseudo-spin $\hat{\mathbb S}$ (NRS Eq. 8.54). $\mathbf A_K$ has an isotropic FC part $a_{\rm iso}$ and a traceless dipolar part from SD; spin–orbit coupling adds an antisymmetric orbital (PSO) part, important for heavy elements.

**Spin polarization.** In UHF or UKS, the FC term includes spin polarization of the doubly occupied core and bonding orbitals. This produces negative spin density at the protons of π radicals, such as CH₃ and aromatic radical anions (McConnell relation), which ROHF cannot describe.

## Nuclear quadrupole coupling

**Interaction energy.** A nucleus with $I\ge1$ has a nonspherical charge distribution. Its traceless quadrupole $\Theta_{\alpha\beta} = \int\rho_n\tfrac12(3r_\alpha r_\beta - \delta_{\alpha\beta}r^2)\,d^3r$ interacts with the electric field gradient $V_{\alpha\beta} = \partial^2\phi/\partial r_\alpha\partial r_\beta$ produced at the nucleus by the electrons and the other nuclei. By Wigner–Eckart, $\Theta_{\alpha\beta}\propto\tfrac12(3\hat I_\alpha\hat I_\beta - \delta_{\alpha\beta}\hat I^2)$, with constant fixed by $eQ = 2\Theta_{zz}$ in the state $m_I = I$ (NRS Eqs. 8.55–8.58).

**Principal axes.** In principal axes with $|V_{zz}|\ge|V_{yy}|\ge|V_{xx}|$, using $V_{\alpha\alpha} = 0$ outside the nucleus, define the asymmetry and $q$ (NRS Eqs. 8.61–8.65):

$$
\eta = \frac{V_{xx} - V_{yy}}{V_{zz}},\qquad eq = V_{zz},\qquad
E_Q(I,m_I) = \frac{e^2qQ}{4I(2I-1)}\big[3m_I^2 - I(I+1)\big]\quad(\eta = 0).
\label{eq}
$$

**The measured quantity** is the nuclear quadrupole coupling constant (NQCC) $e^2qQ/h$, from microwave rotational hyperfine structure, NQR, or quadrupolar NMR line widths (NRS Eq. 8.68). In practical units

$$
\mathrm{NQCC}\,[\mathrm{MHz}] = 234.9647\times Q\,[\mathrm b]\times q\,[E_h\,e^{-1}a_0^{-2}].
$$

**Uses.** The electronic part $q$ is an expectation value. Measured NQCCs and computed $q$ are the main route to nuclear quadrupole moments $Q$ (the "molecular method").

**Townes–Dailey picture.** At the SCF level $q^e$ is a sum of orbital contributions (NRS Eqs. 8.69–8.79):

- **Selection rules.** With the nucleus at the origin, $(3z^2 - r^2)/r^5 = \sqrt{16\pi/5}\,Y_{20}/r^3$. Only $\ell\ge1$ orbitals contribute on-centre, and a filled shell contributes zero (Unsöld's theorem).
- **p shell.** For a p shell, $p_0$ gives $-\tfrac45\langle r^{-3}\rangle$ and each $p_{\pm1}$ gives $+\tfrac25\langle r^{-3}\rangle$ (sign as for the charge $-e$).
- **The gradient as a hole count.** The field gradient therefore measures the imbalance of p populations. In F⁻ it is zero. In HF the bonding σ orbital draws density out of $2p_z$ toward H, the two π pairs are left unbalanced, and $q_F\neq0$.

## Zeeman effect and EPR

**Atoms.** In an external field the orbital and spin Zeeman operators act together, $\hat H_{M1} = \mu_BB(\hat L_z + g_e\hat S_z)$ with $g_e = 2.002\,319\,304$ (NRS Eqs. 8.81–8.87).

- **Weak field.** For a field weak compared with the fine-structure splitting (anomalous Zeeman effect), projection onto $|LSJM_J\rangle$ gives $E = E(^{2S+1}L_J) + g_J\mu_BBM_J$ with

$$
g_J = \frac{J(J+1) + L(L+1) - S(S+1)}{2J(J+1)} + g_e\,\frac{J(J+1) + S(S+1) - L(L+1)}{2J(J+1)}
\label{gJ}
$$

(NRS Eqs. 8.89–8.96). Electric-dipole lines with $\Delta M_J = 0,\pm1$ then appear at $h\nu_0 + \mu_BB(g'_JM'_J - g_JM_J)$.

- **Singlets.** For singlets $g_J = 1$ and the normal Zeeman triplet results.
- **Strong field.** For fields large compared with the fine structure (Paschen–Back), $E = E(^{2S+1}L) + \mu_BB(M_L + g_eM_S)$ (NRS Eqs. 8.100–8.103).

**Molecules: the g-matrix.** Orbital angular momentum is quenched in a nondegenerate spatial state, $\langle\Phi_0|\hat{\mathbf L}|\Phi_0\rangle = 0$. To first order a doublet then has $g = g_e\mathbf 1$ (NRS Eqs. 8.108–8.112). Deviations come from spin–orbit coupling, which mixes orbital angular momentum back in.

- **The g-matrix.** The phenomenological Hamiltonian $\hat{\mathcal Z} = \mu_B\mathbf B\cdot\mathbf g\cdot\hat{\mathbb S}$ acts on the Kramers doublet as a pseudo-spin $\tfrac12$ (NRS Eqs. 8.104–8.107). Its splitting is $\Delta E = \mu_B(\mathbf B\cdot\mathbf G\cdot\mathbf B)^{1/2}$ with $\mathbf G = \mathbf g\mathbf g^{\rm T}$ (NRS Eqs. 8.117–8.121).
- **What experiment fixes.** Experiment determines $\mathbf G$, not $\mathbf g$. The absolute signs of the principal $g$ values are not observable from the splitting; only the sign of the triple product $g_{xx}g_{yy}g_{zz}$ (the sign of $\det\mathbf g$) is, in experiments sensitive to the sense of precession (NRS Sec. 8.8.1).
- **The g-shift.** $\Delta\mathbf g = \mathbf g - g_e\mathbf 1$ is, to leading order, a linear response of the spin–orbit operator to the orbital Zeeman operator, plus small kinetic-energy and gauge corrections. It is a mixed second-order property like the NMR shielding.

**The EPR spin Hamiltonian** collects everything for a pseudo-spin $\mathbb S$ whose multiplicity equals the number of states treated (NRS Eq. 8.122):

$$
\hat H_{\rm EPR} = \mu_B\mathbf B\cdot\mathbf g\cdot\hat{\mathbb S} + \sum_K\hat{\mathbf I}_K\cdot\mathbf A_K\cdot\hat{\mathbb S} + \hat{\mathbb S}\cdot\mathbf D\cdot\hat{\mathbb S}.
$$

The last term is the zero-field splitting (ZFS). It needs $\mathbb S\ge1$: a Kramers doublet cannot be split by a time-even interaction. It comes from the direct electron spin–spin dipolar interaction (first order) and from spin–orbit coupling (second order). It splits $^{2S+1}\Gamma$ terms without an external field, as in triplet O₂ and in high-spin transition-metal ions.

## Worked example

!!! example "Hyperfine, quadrupole and Zeeman numbers (recomputed for this note)"
    **H atom, Eq. [[#aiso]].**

    - Infinite nuclear mass (CODATA 2018 constants): $a_{\rm iso} = 1422.808$ MHz.
    - Reduced mass: scaling $|\psi(0)|^2$ by $(1 + m_e/m_p)^{-3}$ gives 1420.485 MHz. The measured 1420.406 MHz differs by $5.6\times10^{-5}$ relative, the size of the relativistic and QED corrections left out.
    - The same formula with the UHF spin density at the nucleus shows the Gaussian cusp problem:

    | basis | $E$ / $E_h$ | $\pi\rho_s(0)$ (exact 1) | $a_{\rm iso}$ / MHz |
    |---|---:|---:|---:|
    | cc-pVTZ | −0.499810 | 0.903 | 1283 |
    | aug-cc-pV5Z | −0.499995 | 0.972 | 1380 |
    | uncontracted aug-cc-pV5Z | −0.499995 | 0.972 | 1380 |

    A basis exact to 5 μ$E_h$ still misses 3% of the contact density. Hyperfine work needs tight s functions or specially designed sets.

    **Cs clock.** The ground state is $6s\ ^2S_{1/2}$ with $I = \tfrac72$, so $F = 4, 3$. By Eq. [[#interval]] the splitting is $4A$, and the defined 9.192 631 770 GHz gives $A = 2.298\,157\,9425$ GHz.

    **NQCC factor.** $e\cdot(1\ {\rm b})\cdot(1\ E_he^{-1}a_0^{-2})/h = 234.9648$ MHz from CODATA 2018 (NRS: 234.9647).

    **Field gradient at F in HF**, $R = 0.9168$ Å, PBE0. Orbital contributions to $V_{zz}$ ($E_h\,e^{-1}a_0^{-2}$, two electrons each); NRS Table 8.3 against PySCF (uncontracted aug-cc-pwCVQZ on F, uncontracted aug-cc-pVQZ on H):

    | | 1σ | 2σ | 3σ | 1π (each) | electronic | nuclear | total |
    |---|---:|---:|---:|---:|---:|---:|---:|
    | NRS | −0.010 | −0.403 | −8.680 | +5.768 | 2.444 | 0.385 | 2.828 |
    | this note | −0.067 | −0.391 | −8.649 | +5.709 | 2.311 | 0.385 | 2.696 |

    - **Nuclear part.** It is $2Z_{\rm H}/R^3 = 0.385$ in both.
    - **F⁻.** The total vanishes, as Unsöld's theorem requires.
    - **Townes–Dailey.** The π contribution is $\tfrac45\langle r^{-3}\rangle$: NRS's 5.768 means $\langle r^{-3}\rangle_{2p} = 7.21$, against 6.60 in F⁻: the 2p shell contracts in the molecule. Mine gives 7.14.
    - **The difference.** My total is 5% below NRS. The difference is spread over the π and core orbitals: my 1σ core polarization is larger in an uncontracted basis (−0.032 in contracted aug-cc-pwCVTZ). NRS do not state their basis, so I could not locate the cause (to verify).
    - **HF and PBE0.** The HF/aug-cc-pwCVTZ total is 2.764.

    **Na D lines, Eq. [[#gJ]]** with $g_e = 2.002319$: $g_J(3s\,^2S_{1/2}) = 2.00232$, $g_J(3p\,^2P_{1/2}) = 0.66589$, $g_J(3p\,^2P_{3/2}) = 1.33411$. Zeeman components in units of $\mu_BB$:

    - D₁: $\pm0.668$, $\pm1.334$ (four lines);
    - D₂: $\pm0.334$, $\pm1.000$, $\pm1.668$ (six lines).

    This is the anomalous pattern of NRS Fig. 8.5.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 8.1.1, Eqs. (8.1)–(8.30), Figs. 8.1–8.2 (described); Sec. 8.1.2.1, Eqs. (8.31)–(8.54); Sec. 8.1.2.2, Eqs. (8.55)–(8.79), Tables 8.2–8.3, Fig. 8.4 (described); Sec. 8.2, Eqs. (8.80)–(8.122), Figs. 8.5–8.6 (described). The McConnell relation and the remark on spin polarization in UHF are general knowledge, not from NRS. The calculations are in `Claude outputs/part4_response_batchB2.py`, section C.
