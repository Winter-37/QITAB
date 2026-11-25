---
id: zero-point-vibrational-corrections-to-properties
title: Zero-point vibrational corrections to properties - vibrational perturbation theory, the harmonic [P]1,0 and anharmonic [P]0,1 terms, vibrationally averaged geometries, isotope effects and temperature
summary: The zero-point vibrationally averaged value of a property is ⟨0|P(Q)|0⟩ over the anharmonic vibrational ground state. To leading order it is a harmonic term (ħ/4)Σ P_aa/ω_a from the curvature of the property, plus an anharmonic term from the first derivative of P and the semidiagonal cubic force constants. The latter is equivalent to −Σ P_a ω_a⁻² ∂E_zpv/∂Q_a, so it needs only first derivatives of the property and gradients of the zero-point energy. Because cubic force constants of bonds are negative, averaged bonds are longer than equilibrium bonds. The corrections are typically 2–5% but carry isotope effects that purely electronic calculations cannot give. Recomputed: exact versus perturbative ZPVA for HF and DF, and ZPVA dipoles and bond lengths of H₂O, D₂O and HDO.
status: in-progress
kind: theory
level: advanced
tags: [zero-point-vibrational-averaging, zpva, vibrational-perturbation-theory, anharmonicity, cubic-force-constants, vibrationally-averaged-geometry, isotope-effects, morse-potential, temperature-effects]
prerequisites: [electronic-and-nuclear-contributions-to-response, harmonic-vibrational-analysis, rayleigh-schrodinger-perturbation-theory, zero-point-energy-and-thermochemistry]
related: [pure-vibrational-contributions-and-nuclear-relaxation, diatomic-vibration-and-anharmonicity, nmr-shielding-and-spin-spin-coupling, molecular-symmetry-and-point-groups]
conventions: [atomic-units]
key: zpva
order: 170
date: 2026-11-25
---

Atomic units ($\hbar = 1$ kept explicit where it helps). $Q_a$ are mass-weighted normal coordinates of the electronic ground state with harmonic frequencies $\omega_a = (V^{(2)}_{aa})^{1/2}$. $\xi_a = (\omega_a/\hbar)^{1/2}Q_a$ are reduced dimensionless coordinates. Force constants in $Q$ are $V^{(3)}_{abc} = \partial^3V/\partial Q_a\partial Q_b\partial Q_c$, and property derivatives are $P^{(1)}_a = \partial P/\partial Q_a$, $P^{(2)}_{ab} = \partial^2P/\partial Q_a\partial Q_b$ at the equilibrium geometry. The harmonic machinery (mass weighting, projection of translations and rotations, $\omega_a$, $L$) is in [[harmonic-vibrational-analysis]].

## Vibrational perturbation theory

**The zeroth order.** In normal coordinates the harmonic Hamiltonian separates, $\hat H^{(0)} = \sum_a\tfrac12(\hat P_a^2 + \omega_a^2Q_a^2)$, with product eigenfunctions of Hermite functions in $\xi_a$ and energies $\sum_a(n_a + \tfrac12)\hbar\omega_a$ (NRS Eqs. 6.27–6.36).

**Matrix elements.** They follow from the ladder relation $\langle m|\xi^k|n\rangle = \sqrt{n/2}\,\langle m|\xi^{k-1}|n-1\rangle + \sqrt{(n+1)/2}\,\langle m|\xi^{k-1}|n+1\rangle$, together with $\langle m|Q^k|n\rangle = (\hbar/\omega)^{k/2}\langle m|\xi^k|n\rangle$ (NRS Eqs. 6.37–6.39).

**The perturbations.** In dimensionless coordinates (NRS Eqs. 6.46–6.47; the coefficients there carry the energy units):

$$
\hat H^{(1)} = \tfrac16\sum_{abc}V^{(3)}_{abc}\xi_a\xi_b\xi_c,\qquad \hat H^{(2)} = \tfrac1{24}\sum_{abcd}V^{(4)}_{abcd}\xi_a\xi_b\xi_c\xi_d .
$$

$E^{(1)} = 0$ because $\hat H^{(1)}$ is odd. The leading energy correction is second order (NRS Eqs. 6.48–6.50), the standard VPT2 of anharmonic frequencies.

**First-order wave function.** For the vibrational ground state it contains at most three-mode excitations (NRS Eqs. 6.51–6.56):

$$
\Phi^{(1)} = \sum_ac^1_a|1_a\rangle + \sum_ac^3_a|3_a\rangle + \sum_{a\neq b}c^{21}_{ab}|2_a1_b\rangle + \sum_{a<b<c}c^{111}_{abc}|1_a1_b1_c\rangle,\qquad
c^1_a = -\frac{1}{4\sqrt2\,\hbar\omega_a}\sum_bV^{(3)}_{abb}.
\label{c1}
$$

Only $c^1_a$ matters for the leading ZPVA, and it contains only the **semidiagonal** cubic constants $V^{(3)}_{abb}$. The other three coefficients ($c^3_a$, $c^{21}_{ab}$, $c^{111}_{abc}$) enter properties only at higher order.

## Zero-point vibrational averaging

**Expansion of the property.** Expand the property, an expectation value or an electronic response function evaluated at geometry $Q$ (NRS Eq. 6.57):

$$
P(Q) = P^{(0)} + \sum_aP^{(1)}_aQ_a + \tfrac12\sum_{ab}P^{(2)}_{ab}Q_aQ_b + \cdots
$$

Averaging over $\Phi^{(0)} + \Phi^{(1)}$ and keeping the two leading terms gives (NRS Eqs. 6.60–6.63)

$$
\Delta P^{\rm zpva} = \underbrace{\frac{\hbar}{4}\sum_a\frac{P^{(2)}_{aa}}{\omega_a}}_{[P]^{1,0}}\;\underbrace{-\;\frac{\hbar}{4}\sum_{a,b}\frac{P^{(1)}_aV^{(3)}_{abb}}{\omega_a^2\,\omega_b}}_{[P]^{0,1}} .
\label{zpva}
$$

$[P]^{n,m}$ labels the order $n$ in the property (beyond its first derivative) and $m$ in the anharmonicity of the potential (beyond the harmonic one).

- **The harmonic term.** $[P]^{1,0}$ averages the property's curvature over the harmonic zero-point spread $\langle Q_a^2\rangle = \hbar/2\omega_a$.
- **The anharmonic term.** $[P]^{0,1}$ comes from the shift of the vibrational centre: $\langle Q_a\rangle = -\frac{\hbar}{4\omega_a^2}\sum_bV^{(3)}_{abb}/\omega_b$, multiplied by the slope of $P$.

**ZPE-gradient form.** The semidiagonal sum is the gradient of the harmonic zero-point energy $E_{\rm zpv}(Q) = \tfrac{\hbar}{2}\sum_a\omega_a(Q)$ (NRS Eqs. 6.64–6.65):

$$
\frac{\partial E_{\rm zpv}}{\partial Q_a}\Big|_0 = \frac{\hbar}{4}\sum_b\frac{V^{(3)}_{abb}}{\omega_b}
\quad\Rightarrow\quad
[P]^{0,1} = -\sum_a\frac{P^{(1)}_a}{\omega_a^2}\frac{\partial E_{\rm zpv}}{\partial Q_a}.
\label{zpe-grad}
$$

This is the practical route. Harmonic frequencies at a few displaced geometries (one Hessian per displacement) replace the cubic force field. The equation also has a picture: the zero-point energy pushes the molecule along $-\partial E_{\rm zpv}/\partial Q_a$, the harmonic spring $\omega_a^2$ resists, and the property follows the resulting shift. This is the effective geometry obtained by minimizing $V + E_{\rm zpv}$.

**Symmetry.** In Abelian groups (NRS Table 6.2), $P(Q_a)$ is odd in $Q_a$ when $\Gamma(\hat P) = \Gamma(Q_a)$ and $P^{(0)} = 0$. It is even when the symmetries differ and $P^{(0)}\neq0$. So $P^{(1)}_a\neq0$ only for modes of the property's symmetry: for a symmetric property such as $\alpha_{xx}$ or $\mu$ in a nondegenerate group, only totally symmetric modes enter $[P]^{0,1}$. Nontotally symmetric modes still contribute to $[P]^{1,0}$ through $P^{(2)}_{aa}$.

## Averaged geometries

**Bonds lengthen.** Take $P = Q$ itself: then $P^{(2)} = 0$ and

$$
\Delta Q^{\rm zpva}_a = -\frac{\hbar}{4}\sum_b\frac{V^{(3)}_{abb}}{\omega_a^2\omega_b}
$$

(NRS Eq. 6.68). For a Morse oscillator $V = D_e(1 - e^{-a(r-r_e)})^2$, with $a = \sqrt{k/2D_e}$, the cubic constant is $V''' = -2a^3D_e$, which is negative (NRS Eqs. 6.66–6.67). Bond stretches therefore lengthen on vibrational averaging: $r_0 > r_e$.

**Large-amplitude motion.** The perturbative treatment assumes the potential is near harmonic. Internal rotations, ring puckering, inversion and hydrogen-bond motions need the full one-dimensional potential along the large-amplitude coordinate. NRS's example is the H₂O₂ torsion (Fig. 6.6). The barrier between the two equivalent minima is crossed at room temperature, and the trans ($C_{2h}$) geometry makes the second excited state parity-forbidden. Vibrational averaging over the torsion gives that band nonzero intensity.

## How large, and where it matters

**Size.** ZPVA corrections are typically 2–5% of the electronic value. They are often smaller than the remaining electronic-structure error, which is why they are often skipped (NRS Sec. 6.5.2).

**Exceptions.**

- **Spin–spin couplings.** ZPVA can reach 10–20% for indirect spin–spin couplings ([[nmr-shielding-and-spin-spin-coupling]]), whose Fermi-contact term is very sensitive to bond length.
- **Isotope effects.** For properties that do not depend on the nuclear moments, the electronic surface is identical for all isotopologues, so every isotope effect is vibrational:
  - **Frequencies.** Diatomic frequencies scale as $\mu_{\rm red}^{-1/2}$: $\omega_{\rm HF}/\omega_{\rm DF} = [m_{\rm D}(m_{\rm H} + m_{\rm F})/m_{\rm H}(m_{\rm D} + m_{\rm F})]^{1/2} = 1.379$, against 4138/2998 = 1.380 measured (NRS Eq. 6.69).
  - **Symmetry lowering.** HDO has $C_{2v}$ electronic surfaces but a $C_s$ vibrational problem. Its averaged geometry has $r_0({\rm OH})\neq r_0({\rm OD})$ and an averaged dipole that tilts off the bisector.
  - **Induced dipoles.** CH₂=CD₂ acquires a vibrationally induced dipole moment, measured as 0.0091 ± 0.0004 D. CFHDT is chiral only through isotopic substitution (NRS Fig. 6.7).
  - **Secondary isotope shifts.** The ¹⁷O shielding differs by about 1.5 ppm between H₂O and HDO (NRS Sec. 6.5.2).
- **Local proton properties.** For local properties at a proton (its shielding, its field gradient), the light proton's motion couples weakly to the rest. A local-mode treatment of the X–H stretch and bends often suffices.

## Temperature

**Excited vibrational states.** Averaging over a Boltzmann distribution of vibrational states generalizes Eq. [[#zpva]]. For one harmonic mode the populations are

$$
p_n(T) = \frac{e^{-(n+\frac12)\hbar\omega/kT}}{Z},\quad Z = \frac{e^{-\hbar\omega/2kT}}{1 - e^{-\hbar\omega/kT}}\quad\Rightarrow\quad p_n(T) = \big(1 - e^{-\hbar\omega/kT}\big)e^{-n\hbar\omega/kT}.
$$

NRS Eq. 6.73 keeps an extra factor $1/e^{-\hbar\omega/2kT}$, which does not belong there: the $\tfrac12$ cancels between numerator and $Z$. At 298.15 K ($kT = 207.2$ cm⁻¹) the ground-state population is 0.910 for a 500 cm⁻¹ mode and 0.992 for a 1000 cm⁻¹ mode, the values plotted in NRS Fig. 6.8. Only low-frequency modes are thermally excited.

**Centrifugal distortion.** The larger temperature effect usually comes from rotation. Rotational levels are populated up to $J\sim\sqrt{kT/B}$, and the centrifugal force stretches the bonds, shifting the effective geometry further (NRS Sec. 6.5.3).

## Worked example

!!! example "Exact against perturbative ZPVA, and isotopologues of water (recomputed for this note)"
    **HF and DF, one coordinate.** HF/aug-cc-pVTZ curves from [[electronic-and-nuclear-contributions-to-response]]; exact averages from the sinc-DVR ground state. Taylor coefficients come from a degree-7 polynomial fit within ±0.35 bohr of $r_e = 0.89912$ Å. In au (bond length in bohr):

    | | HF exact | HF, Eq. [[#zpva]] ($[P]^{1,0}$ + $[P]^{0,1}$) | DF exact | DF, Eq. [[#zpva]] |
    |---|---:|---:|---:|---:|
    | $\langle r\rangle - r_e$ | 0.02701 | 0 + 0.02679 = 0.02679 | 0.01954 | 0.01942 |
    | $\Delta\mu$ ($\mu_e = 0.74383$) | 0.011725 | 0.000814 + 0.010786 = 0.011600 | 0.008474 | 0.008409 |
    | $\Delta\alpha_{zz}$ ($\alpha_e = 5.5329$) | 0.1912 | 0.0452 + 0.1398 = 0.1850 | 0.1373 | 0.1341 |

    **What the table shows.**

    - **Accuracy.** The two-term formula is within 1% (geometry, dipole) and 3% (polarizability) of the exact anharmonic average.
    - **The anharmonic term dominates.** The averaged bond is 0.0143 Å longer, and $\mu$ and $\alpha$ simply follow the longer bond.
    - **Isotope scaling.** The corrections scale roughly as $\mu_{\rm red}^{-1/2}$ (HF/DF ratio ≈ 1.38).
    - **ZPE-gradient form.** The anharmonic dipole term from Eq. [[#zpe-grad]] equals the cubic-constant form (0.010786 both).
    - **Frequencies.** Harmonic $\omega = 4465.8$ cm⁻¹; exact fundamental 4301.6 cm⁻¹ (HF theory, not experiment).

    **Water, HF/aug-cc-pVDZ, Eq. [[#zpe-grad]].** The setup:

    - analytic Hessians at displacements $\xi_a = \pm0.3$ along each normal mode of each isotopologue;
    - $\partial E_{\rm zpv}/\partial Q_a$ and $P^{(1)}_a$ from central differences, $P^{(2)}_{aa}$ from the three-point second difference;
    - $r_e({\rm OH}) = 0.94363$ Å, $\mu_e = 0.7729$ au.

    | | harmonic ω (cm⁻¹) | $\Delta r_{\rm OH}$ / bohr ($[P]^{1,0}$ + $[P]^{0,1}$) | $\Delta\mu$ along $C_2$ / au |
    |---|---|---|---:|
    | H₂O | 1744, 4130, 4238 | 0.00519 + 0.02495 = 0.03014 | +0.00150 |
    | D₂O | 1276, 2978, 3107 | 0.00382 + 0.01815 = 0.02196 | +0.00124 |
    | HDO, O–H | 1529, 3040, 4186 | 0.00770 + 0.02245 = 0.03015 | +0.00111 |
    | HDO, O–D | | 0.00223 + 0.01969 = 0.02192 | |

    Signs are relative to the equilibrium dipole direction (an increase of $|\mu|$).

    **What the water results show.**

    - **Isotopic asymmetry.** In HDO the two bonds average differently: $r_0({\rm OH}) - r_0({\rm OD}) = 0.0082$ bohr = 0.0044 Å. Each bond keeps very nearly the value it has in the symmetric isotopologue, so the stretches are close to local modes. The averaged dipole acquires a component of 0.00056 au perpendicular to the bisector.
    - **The harmonic bond term.** The $[P]^{1,0}$ part of $\Delta r_{\rm OH}$ is the curvilinear effect: bending and the perpendicular zero-point motion lengthen a bond even in a harmonic potential.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 6.3, Eqs. (6.27)–(6.45), Figs. 6.2–6.4 (described); Sec. 6.4, Eqs. (6.46)–(6.56); Sec. 6.5.1, Eqs. (6.57)–(6.68), Tables 6.2–6.3, Figs. 6.5–6.6 (described); Sec. 6.5.2, Eq. (6.69), Fig. 6.7 (described); Sec. 6.5.3, Eqs. (6.70)–(6.73), Fig. 6.8. The calculations are in `Claude outputs/part4_response_batchC.py`, sections A and B.
