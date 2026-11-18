---
id: exchange-correlation-functionals
title: Exchange–correlation functionals - LDA, GGA, meta-GGA, hybrids, double hybrids
summary: The approximations to E_xc used in Kohn–Sham calculations, rung by rung of Perdew's ladder - LDA/LSDA from the uniform electron gas (with X-alpha as a special case), gradient-corrected GGAs (B88, LYP, PW91, PBE), meta-GGAs (kinetic-energy density), hybrids with a fraction of exact exchange (B3LYP, B3PW91, PBE0, B1B95, Minnesota functionals) and MP2-based double hybrids - plus dispersion corrections. Checked numerically - the LDA exchange formula and potential, the LSDA spin scaling, Becke's exchange and correlation energies of Ar from the HF density, and the B3LYP decomposition, including the VWN3/VWN5 ambiguity that shifts B3LYP energies by 37 mE_h for water.
status: in-progress
kind: theory
level: intermediate
tags: [dft, exchange-correlation, lda, gga, meta-gga, hybrid-functionals, b3lyp, double-hybrid, dispersion-correction]
prerequisites: [kohn-sham-dft]
related: [dft-versus-hartree-fock, free-electron-gas, mp2, electronic-structure-methods-at-a-glance]
order: 20
date: 2026-11-17
---

Atomic units; $\rho = \rho^\alpha + \rho^\beta$. Every functional below is an approximation to the exact but unknown $E_{xc}[\rho]$ of [[kohn-sham-dft]]. It is customary to split $E_{xc} = E_x + E_c$ and model each part.

## Rung 1: local (spin-)density approximation

If $\rho$ varies slowly, each volume element can be treated as a **uniform electron gas** (jellium: electrons in a uniform neutralizing positive background, [[free-electron-gas]]) of the local density:

$$
E_{xc}^{\text{LDA}} = \int\rho(\mathbf r)\,\varepsilon_{xc}\big(\rho(\mathbf r)\big)\,\mathrm d\mathbf r,\qquad
v_{xc}^{\text{LDA}} = \varepsilon_{xc}(\rho) + \rho\frac{\partial\varepsilon_{xc}}{\partial\rho} .
$$

**Exchange** of the uniform gas is known exactly:

$$
\varepsilon_x(\rho) = -\frac34\Big(\frac3\pi\Big)^{1/3}\rho^{1/3},\qquad
E_x^{\text{LDA}} = -\frac34\Big(\frac3\pi\Big)^{1/3}\int\rho^{4/3}\,\mathrm d\mathbf r,\qquad
v_x^{\text{LDA}} = -\Big(\frac{3\rho}{\pi}\Big)^{1/3} .
$$

**Correlation** $\varepsilon_c(\rho)$ comes from accurate numerical solutions of the uniform-gas Schrödinger equation at many densities, fitted by Vosko, Wilk and Nusair (VWN). VWN gave two fits, called VWN3 (or VWN-RPA) and VWN5; which one a program calls "VWN" matters (see the B3LYP example below).

**Spin polarization (LSDA).** Exchange acts only between like spins, so

$$
E_x^{\text{LSDA}} = -\frac34\Big(\frac6\pi\Big)^{1/3}\int\Big[(\rho^\alpha)^{4/3} + (\rho^\beta)^{4/3}\Big]\mathrm d\mathbf r,
$$

which reduces to the LDA form when $\rho^\alpha = \rho^\beta = \rho/2$. LSDA is called SVWN (S for Slater exchange).

**X$\alpha$.** Slater's earlier exchange-only method, $E_x^{X\alpha} = -\tfrac98\alpha(3/\pi)^{1/3}\int\rho^{4/3}$, is LDA exchange when $\alpha = 2/3$ and is best viewed as a special case of DFT.

LSDA gives surprisingly good geometries, frequencies and dipole moments, but atomization energies that are far too large.

## Rung 2: generalized gradient approximations (GGA)

Semilocal functionals add the density gradient:

$$
E_{xc}^{\text{GGA}} = \int f\big(\rho^\alpha,\rho^\beta,\nabla\rho^\alpha,\nabla\rho^\beta\big)\,\mathrm d\mathbf r = E_x^{\text{GGA}} + E_c^{\text{GGA}} .
$$

**Becke 1988 exchange (B88)** corrects LSDA exchange with one parameter $\beta = 0.0042$, fitted to atomic HF exchange energies:

$$
E_x^{\text{B88}} = E_x^{\text{LSDA}} - \beta\sum_{\sigma}\int(\rho^\sigma)^{4/3}\frac{x_\sigma^2}{1 + 6\beta x_\sigma\sinh^{-1}x_\sigma}\,\mathrm d\mathbf r,\qquad x_\sigma = \frac{|\nabla\rho^\sigma|}{(\rho^\sigma)^{4/3}} .
$$

Other components: PW86 and PW91 exchange; LYP (Lee–Yang–Parr), P86 and PW91 correlation; PBE exchange and correlation (no empirical parameters, widely used for solids). Any exchange functional can be combined with any correlation functional (BLYP, BPW91, ...).

## Rung 3: meta-GGA

Meta-GGAs add the Laplacian $\nabla^2\rho^\sigma$ and/or the **kinetic-energy density**

$$
\tau_\sigma = \tfrac12\sum_i^{\text{occ}}|\nabla u_{i\sigma}^{\text{KS}}|^2 .
$$

Examples: B95 correlation, TPSS, oTPSS, M06-L. They cost little more than GGAs.

## Rung 4: hybrids

A **hybrid** mixes in a fraction of exact (Hartree–Fock-type) exchange computed with the KS orbitals, $E_x^{\text{exact}} = -\tfrac12\sum_{ij}^{\text{occ}}\langle u_iu_j|u_ju_i\rangle$ over spin orbitals of equal spin.

**B3LYP**, the most widely used functional of 1995-2010:

$$
E_{xc}^{\text{B3LYP}} = (1 - a_0 - a_x)E_x^{\text{LSDA}} + a_0E_x^{\text{exact}} + a_xE_x^{\text{B88}} + (1 - a_c)E_c^{\text{VWN}} + a_cE_c^{\text{LYP}},
$$

$a_0 = 0.20$, $a_x = 0.72$, $a_c = 0.81$, i.e. $0.08E_x^{\text{LSDA}} + 0.20E_x^{\text{exact}} + 0.72E_x^{\text{B88}} + 0.19E_c^{\text{VWN}} + 0.81E_c^{\text{LYP}}$. Becke actually proposed B3PW91 and fitted the three parameters with PW91 correlation; others then swapped in LYP without refitting, and this version became B3LYP.

| Hybrid | Exact exchange | Remark |
|---|---:|---|
| B3LYP, B3PW91 | 20% | three parameters fitted to atomization energies |
| PBE0 | 25% | hybrid of PBE |
| B1B95 | 28% | one-parameter hybrid meta-GGA |
| M06 / M06-2X / M06-HF | 27% / 54% / 100% | Minnesota meta-GGAs, about 35 parameters each |
| BMK | 42% | fitted for barrier heights (kinetics) |

Range-separated hybrids, which switch from semilocal to exact exchange with interelectronic distance, are not covered in Levine and are left as a planned section.

## Rung 5: double hybrids

Grimme's double hybrids add second-order perturbation theory on top of a hybrid solved self-consistently:

$$
E_{xc} = a_1E_x^{\text{GGA}} + (1 - a_1)E_x^{\text{exact}} + a_2E_c^{\text{GGA}} + (1 - a_2)E_c^{\text{KS-MP2}},
$$

where $E_c^{\text{KS-MP2}}$ is the MP2 formula ([[mp2]]) evaluated with KS orbitals and orbital energies, occupied and virtual. B2PLYP uses B88 and LYP with $a_1 = 0.47$, $a_2 = 0.73$, i.e. 53% exact exchange and 27% MP2 correlation. They need larger basis sets and MP2 cost, and are the most accurate rung.

## Dispersion

None of the functionals above contains the long-range correlation that produces London dispersion ($-C_6/R^6$). Two fixes:

- **DFT-D.** Add $E_{\text{disp}} = -\sum_{A<B}\frac{C_6^{AB}}{R_{AB}^6}f(R_{AB})$ with a damping function $f$. DFT-D3 computes the $C_6$ from first principles, adds an $R^{-8}$ term and has three parameters per functional.
- **Nonlocal correlation.** The VV10 functional can be added to any $E_{xc}$.

## How good is each rung

Weighted mean absolute errors on the GMTKN30 database (quadruple-zeta basis, D3 added to most functionals; Goerigk and Grimme 2011, as quoted by Levine), in kcal/mol:

| LDA | GGA | meta-GGA | hybrid | double hybrid | MP2/CBS |
|---:|---:|---:|---:|---:|---:|
| 12.0 | 5.3 | 4.4 | 3.3 | 1.8 | 3.6 |

B3LYP-D3 scored 3.8, worse than the average hybrid. No functional is best for everything: performance depends on the chemistry and the property.

## Worked examples

!!! example "LDA exchange and its potential"
    For the B3LYP/cc-pVTZ density of water, the quadrature of $-\tfrac34(3/\pi)^{1/3}\int\rho^{4/3}$ gives $E_x^{\text{LDA}} = -8.119\,811\,E_h$, identical to libxc's Slater functional to $10^{-14}$. libxc's potential equals $-(3\rho/\pi)^{1/3}$ point by point. A finite-difference derivative of $E_x[\rho + \epsilon f]$ for a test function $f$ equals $\int v_xf$ to $2\times10^{-11}$, which is the defining property of the functional derivative.

    For the triplet O atom (LSDA, cc-pVTZ), the spin-polarized formula gives $-7.341\,313\,E_h$ (libxc agrees). Treating the same density as unpolarized gives $-7.250\,892\,E_h$: spin polarization lowers the exchange energy by 0.090 $E_h$.

!!! example "Exchange and correlation energies of argon"
    Evaluated with the HF/aug-cc-pV5Z density ($E_{\text{HF}} = -526.817\,347\,E_h$), compared with Becke's values as quoted by Levine:

    | | $E_x^{\text{HF}}$ | $E_x^{\text{LSDA}}$ | $E_x^{\text{B88}}$ | $E_c^{\text{LSDA}}$ (PW92) | $E_c^{\text{PW91}}$ |
    |---|---:|---:|---:|---:|---:|
    | this work | −30.185 | −27.863 | −30.153 | −1.424 | −0.771 |
    | Becke (Levine) | −30.19 | −27.86 | −30.15 | −1.431 | −0.768 |

    - **Exchange.** LSDA underestimates $|E_x|$ by 8%; one gradient parameter brings B88 within 0.03 $E_h$.
    - **Correlation.** LSDA roughly doubles the correlation energy; the reference value is about $-0.72\,E_h$. With VWN5 instead of PW92, $E_c^{\text{LSDA}} = -1.431$.
    - **Sizes.** Exchange is 5.7% of the total energy, correlation 0.15%.

!!! example "What does 'B3LYP' mean in a program?"
    PySCF's `b3lyp` (as in Gaussian) uses the VWN-RPA (VWN3) correlation in the 19% local part; PySCF's `b3lyp5` uses VWN5. For water at the B3LYP/cc-pVTZ density the semilocal part of $E_{xc}$ is $-7.560\,073\,E_h$ with VWN-RPA and $-7.522\,969\,E_h$ with VWN5. It equals the five-term linear combination above to $10^{-14}$ in the first case, and also in Levine's second form $0.80E_x^{\text{LSDA}} + 0.72\Delta E_x^{\text{B88}} + \cdots$. The self-consistent total energies differ by **37.1 m$E_h$** (23 kcal/mol). Absolute B3LYP energies from different programs are therefore not comparable unless the VWN variant is stated.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 16.5, pp. 559-570: LDA and jellium, Eqs. (16.52)-(16.58); $E_x$ and $E_c$, Eqs. (16.59)-(16.60); X$\alpha$, Eq. (16.61); LSDA, Eq. (16.65); GGA and B88, Eqs. (16.63)-(16.64); Becke's Ar values; VWN3/VWN5; meta-GGA, Eq. (16.66); hybrids, Eq. (16.67), B3PW91 history, B97, PBE0, BMK; double hybrids, Eqs. (16.69)-(16.70); Jacob's ladder; dispersion corrections; Minnesota functionals; GMTKN30 errors. Calculations in `part4_dft.py`, sections B, C and D (PySCF 2.15.1 with libxc).
