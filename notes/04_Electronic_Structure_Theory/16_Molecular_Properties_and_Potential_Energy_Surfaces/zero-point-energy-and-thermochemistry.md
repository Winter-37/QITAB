---
id: zero-point-energy-and-thermochemistry
title: Zero-point energy, dissociation energies and gas-phase thermochemistry
summary: From an electronic energy U_e, an optimized geometry and harmonic frequencies to measurable quantities. D₀ = D_e − E_ZPE with E_ZPE ≈ ½Σhν_k; atomization energies and enthalpies of formation; ideal-gas rigid-rotor harmonic-oscillator contributions to U, H, S and G at 298 K. Worked example: H₂O at HF/6-31G* reproduces Levine's D_e = 6.27 eV, D₀ = 5.71 eV (experiment 9.51 eV) and ΔH_f,0 = +30.6 kcal/mol (experiment −57), and gives S°₂₉₈ = 188.2 J mol⁻¹ K⁻¹ with each term checked.
status: in-progress
kind: theory
level: intermediate
tags: [zero-point-energy, thermochemistry, dissociation-energy, atomization-energy, partition-function, entropy, enthalpy]
prerequisites: [harmonic-vibrational-analysis, diatomic-vibration-and-anharmonicity]
related: [rigid-rotor-and-rovibrational-levels, energy-and-unit-conversions, physical-constants, standard-models-h2-and-water, hjo-calibration-energies-atomization-reactions-barriers]
order: 40
date: 2026-11-17
---

## Zero-point energy and dissociation energies

In the harmonic approximation the vibrational ground state of an $N$-atom molecule has energy

$$
E_{\text{ZPE}} = \tfrac12\sum_{k=1}^{3N-6}h\nu_k\qquad(3N-5\ \text{for linear molecules}),
$$

so the molecule never sits at the bottom of its well. The **equilibrium dissociation energy** $D_e$ is measured from the minimum of $U$; the **ground-state dissociation energy** $D_0$, which experiment measures, from the $v = 0$ level:

$$
D_0 = D_e - E_{\text{ZPE}} .
$$

Each mode contributes little, but there are many: Levine notes that 1,3-butadiene (24 modes) has $E_{\text{ZPE}} = 2.2$ eV, about 50 kcal/mol. Levine recommends fundamental rather than harmonic frequencies in $E_{\text{ZPE}}$ because they include part of the anharmonicity; scaled harmonic frequencies are the usual stand-in.

**From a calculation.** $D_e$ for total atomization is the sum of atomic energies minus $U_e$ of the molecule, with the same method and basis for all. Atoms are usually open shell; Levine uses UHF for them. At 0 K, $N_AD_0 = \Delta U^\circ_{\text{at},0} = \Delta H^\circ_{\text{at},0}$.

**Enthalpies of formation.** Route the formation reaction through atoms: elements → atoms (experimental atomization energies) → product (computed atomization energy reversed). The error in $\Delta H_f$ is then exactly the error in the computed atomization energy.

**Energy differences between isomers or conformers** at 0 K are $N_A[(U_{e,B} + E_{\text{ZPE},B}) - (U_{e,C} + E_{\text{ZPE},C})]$; for conformers the ZPE terms nearly cancel. Levine cites the gauche–anti energy difference of butane as 0.59 kcal/mol without ZPE, 0.70 with ZPE at 0 K and 0.64 at 298 K, against an experimental 0.67 (Smith and Jaffe, *J. Phys. Chem.* **100**, 18718 (1996)).

## Finite temperature: the RRHO model

For an ideal gas of molecules treated as rigid rotors and harmonic oscillators (RRHO), with the electronic ground state only, the molar internal energy above $U_e + E_{\text{ZPE}}$ (per mole) is

$$
U_T - U_0 = \underbrace{\tfrac32RT}_{\text{trans}} + \underbrace{RT\ \text{(linear)}\ \text{or}\ \tfrac32RT\ \text{(nonlinear)}}_{\text{rot}} + \underbrace{RT\sum_k\frac{x_k}{e^{x_k} - 1}}_{\text{vib, thermal}},\qquad x_k = \frac{h\nu_k}{k_BT},
$$

and $H = U + RT$ for one mole of ideal gas. The vibrational term matters only for modes below about 900 cm$^{-1}$ at room temperature (Levine), since $k_BT/hc = 207$ cm$^{-1}$.

The entropy is a sum of translational (depends only on the molar mass and on $T$, $P$), rotational (moments of inertia and the **symmetry number** $\sigma$, 2 for H₂O), vibrational and electronic contributions. The harmonic vibrational entropy is

$$
S_{\text{vib}} = R\sum_k\Big[\frac{x_k}{e^{x_k} - 1} - \ln\big(1 - e^{-x_k}\big)\Big],
$$

and $G = H - TS$. The RRHO model fails for low-frequency torsions, which should be treated as hindered rotors; Levine cites the East–Radom E1/E2 procedures, which handle them and reach entropies within about 1 J mol$^{-1}$ K$^{-1}$.

**Converting a 0 K enthalpy to 298 K.** For H₂(g) + ½O₂(g) → H₂O(g) the product gains $3RT$ (translation + nonlinear rotation), the reactants $\tfrac32RT + RT$ for H₂ and $\tfrac12(\tfrac32RT + RT)$ for O₂, i.e. $3.75RT$; with $\Delta n_{\text{gas}} = -\tfrac12$,

$$
\Delta H^\circ_{f,298} = \Delta H^\circ_{f,0} - 0.75RT - \tfrac12RT = \Delta H^\circ_{f,0} - \tfrac54RT ,
$$

a shift of $-0.74$ kcal/mol at 298 K (vibrations of H₂, O₂ and H₂O are not excited).

## Worked example

!!! example "Water at HF/6-31G* (Levine Sec. 15.13), recomputed"
    Same optimized geometry and Hessian as in [[harmonic-vibrational-analysis]]. Atoms by UHF/6-31G*: $E(\text{H}) = -0.498\,233$, $E(\text{O}) = -74.783\,934\,E_h$ (Levine $-74.783\,931$).

    | Step | Value |
    |---|---|
    | $D_e = 2E(\text{H}) + E(\text{O}) - U_e$ | $0.230\,35\,E_h$ = 6.268 eV |
    | $E_{\text{ZPE}}$, harmonic | 0.6252 eV |
    | $E_{\text{ZPE}}$, scaled frequencies (× 0.895) | 0.5595 eV |
    | $D_0 = D_e - E_{\text{ZPE}}$ (scaled) | 5.709 eV = 551 kJ/mol |
    | experiment (Levine, from Chase et al.) | $D_0 = 9.51$ eV = 917.79 kJ/mol |
    | $\Delta H^\circ_{f,0}$(H₂O, g) from $2(216.04) + 246.79 - 551$ kJ/mol | +128 kJ/mol = +30.6 kcal/mol |
    | experiment | −238.92 kJ/mol = −57.1 kcal/mol |
    | $\Delta H^\circ_{f,298} = \Delta H^\circ_{f,0} - \tfrac54RT$ | +29.9 kcal/mol |

    Hartree–Fock misses 40% of the atomization energy because the correlation energy of the molecule is much larger than that of the separated atoms; [[hjo-calibration-energies-atomization-reactions-barriers]] shows how correlated methods close the gap.

    **RRHO functions at 298.15 K and 1 atm** (PySCF `thermo`, unscaled frequencies, $\sigma = 2$):

    | Quantity | Value |
    |---|---|
    | $E_{\text{trans}} = E_{\text{rot}} = \tfrac32RT$ | $0.001\,416\,E_h$ each (checked to $5\times10^{-10}$) |
    | thermal vibrational energy above ZPE | 3.25 J/mol (negligible: lowest mode 1826 cm$^{-1}$) |
    | $H - U_e = E_{\text{ZPE}} + 3RT + E_{\text{vib,th}} + RT$ | $0.026\,753\,E_h$ = 70.24 kJ/mol |
    | $S_{\text{trans}}$, $S_{\text{rot}}$, $S_{\text{vib}}$ | 144.80, 43.42, 0.01 J mol$^{-1}$ K$^{-1}$ |
    | $S^\circ_{298}$ | 188.23 J mol$^{-1}$ K$^{-1}$ |
    | $G - U_e$ | 14.12 kJ/mol |

    The $S_{\text{vib}}$ formula above and the rigid-rotor $S_{\text{rot}}$ with $\sigma = 2$, coded independently, match PySCF to $4\times10^{-8}$ and $10^{-3}$ J mol$^{-1}$ K$^{-1}$. Note the standard pressure: PySCF and Gaussian use 1 atm here, while the recommended standard state is 1 bar; the difference shifts $S_{\text{trans}}$ by $R\ln(1.01325) = 0.11$ J mol$^{-1}$ K$^{-1}$.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 15.13, pp. 498-500, Eq. (15.78), the H₂O HF/6-31G* example (atomic UHF energies, $D_e$, $D_0$, atomization and formation enthalpies, the $\tfrac54RT$ conversion, experimental data from Chase et al.), the butadiene ZPE, the butane conformer energies and the East–Radom entropy procedures; Sec. 15.12, p. 498 (scale factor). The RRHO formulas are standard statistical mechanics (Levine refers to physical chemistry texts and gives the vibrational energy in Prob. 15.39). Calculations in `part3_batchA.py`, section D.
