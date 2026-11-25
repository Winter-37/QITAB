---
id: vibronic-band-shapes-franck-condon-and-herzberg-teller
title: Vibronic band shapes - Franck-Condon factors, Duschinsky rotation, the generating-function method, the linear coupling model and Herzberg-Teller intensity borrowing
summary: An electronic band is a progression of vibronic lines whose intensities are Franck–Condon factors, squared overlaps of ground- and excited-state vibrational wave functions. With the excited-state normal coordinates related to the ground-state ones by Q₀ = JQ_K + K (Duschinsky rotation J, displacement K), all overlaps follow from a generating function. For equal frequencies and a pure displacement they form a Poisson distribution with Huang–Rhys factor S = Δ²/2. The linear coupling (vertical gradient) model gets the displacements from the excited-state gradient at the ground-state geometry. Symmetry-forbidden bands borrow intensity through the geometry dependence of the transition moment (Herzberg–Teller). Recomputed: the generating function against quadrature (two misprints in NRS Eq. 6.123), the Poisson limit, and for formaldehyde S₁ the Huang–Rhys factors and the Herzberg–Teller oscillator strength.
status: in-progress
kind: theory
level: advanced
tags: [franck-condon, vibronic, huang-rhys, duschinsky, linear-coupling-model, vertical-gradient, herzberg-teller, intensity-borrowing, laporte, generating-function, band-shape]
prerequisites: [electronic-absorption-and-emission, harmonic-vibrational-analysis, electronic-and-nuclear-contributions-to-response, tddft-linear-response]
related: [raman-scattering, parity-and-parity-selection-rules, diatomic-vibration-and-anharmonicity, emission-absorption-and-spontaneous-emission, molecular-symmetry-and-point-groups]
conventions: [atomic-units]
key: poisson
order: 20
date: 2026-11-25
---

Atomic units with $\hbar = 1$, so energies and frequencies are interchangeable. Vibronic states $|K,k\rangle$ as in [[electronic-and-nuclear-contributions-to-response]]. $Q^0$ and $Q^K$ are the mass-weighted normal coordinates of the ground and excited state, each measured from its own minimum, with frequencies $\omega_0$ and $\omega_K$ (diagonal matrices $\boldsymbol\Gamma_0$, $\boldsymbol\Gamma_K$). $\xi = \sqrt\omega\,Q$ are reduced dimensionless coordinates. The overlap of vibrational state $k$ of $K$ with state $n$ of the ground state is $S(k,n) = \langle k|n\rangle$.

## Franck–Condon and Herzberg–Teller

**The Franck–Condon principle.** The electronic transition is fast compared with nuclear motion, so the nuclei start on the excited surface where they were on the ground surface. They then find themselves away from the new minimum, with vibrational wave functions that are not eigenstates there.

**Expansion of the vibronic moment.** Integrating the electronic coordinates and expanding the electronic transition moment about the ground-state minimum (NRS Eqs. 6.106–6.107):

$$
\langle k,K|\hat\mu_\alpha|0,0\rangle = \langle k|\mu^{K0}_\alpha(Q)|0\rangle = \mu^{K0}_\alpha(0)\,S(k,0) + \sum_a\frac{\partial\mu^{K0}_\alpha}{\partial Q_a}\Big|_0\langle k|Q_a|0\rangle + \cdots
\label{ht}
$$

- **The Franck–Condon term.** The first term gives line intensities $|\mu^{K0}(0)|^2|S(k,0)|^2$. The Franck–Condon factors $|S(k,0)|^2$ sum to one over $k$, so the band's total intensity is that of the vertical transition, redistributed over the progression.
- **The Herzberg–Teller term.** The second term is the only route by which a transition with $\mu^{K0}(0) = 0$ by symmetry gains intensity.

## Relating the two sets of normal coordinates

**The linear relation.** Both sets are linear in the Cartesian displacements, so (NRS Eqs. 6.108–6.111)

$$
Q^0 = \mathbf JQ^K + \mathbf K,\qquad \mathbf K = \mathbf L_0\Delta\mathbf q,\qquad \mathbf J = \mathbf L_0(\mathbf L_K)^{-1}.
$$

Here $\Delta q_i = \sqrt{m_i}(x^K_{{\rm eq},i} - x^0_{{\rm eq},i})$ is the mass-weighted shift of the minimum and $\mathbf L$ are the normal-mode matrices. $\mathbf J$ is the Duschinsky rotation: excited-state modes are mixtures of ground-state modes. Translations drop out exactly. Rotations do not in general, which contaminates the transformation slightly.

**A hierarchy of approximations** (NRS Sec. 6.7), from expensive to cheap:

1. **Adiabatic Franck–Condon.** Full $\mathbf J$, frequency changes and displacement. It needs the excited-state minimum and Hessian.
2. **No rotation.** Diagonal $\mathbf J$ with frequency scaling; few savings.
3. **Displacement only.** Displaced oscillators with the ground-state force field ($\mathbf L_K = \mathbf L_0$). It needs the excited-state minimum.
4. **Linear coupling model** (vertical gradient). Common force field, with the displacement estimated from the excited-state gradient at the ground-state geometry. It needs one excited-state gradient and the ground-state Hessian.

**Cost.** The number of integrals grows combinatorially with the number of modes and quanta. For a 12-atom molecule with up to five quanta per mode, NRS estimate $5^{30}\approx9\times10^{20}$ Franck–Condon integrals, so practical codes select classes of transitions and check them with sum rules.

## The generating function (one mode)

**Construction.** With $\xi_0 = \sqrt{\omega_0/\omega_K}\,(\xi_K + \Delta_K)$, where $\Delta_K = \sqrt{\omega_K}\,d$ is the dimensionless shift of the excited minimum by $d$ in $Q$, the Hermite generating function $\sum_kT^kH_k(x)/k! = e^{2xT - T^2}$ turns all overlaps into one Gaussian integral (NRS Eqs. 6.114–6.122):

$$
\sum_{k,n}T^kU^n\sqrt{\frac{2^k2^n}{k!\,n!}}\,S(k,n) = I_0\exp\big(AT^2 + BT + CU^2 + DU + ETU\big).
\label{genfun}
$$

**Coefficients.** Doing the integral, with $s = \omega_0 + \omega_K$ and keeping the normalization of the oscillators in the physical coordinate $Q$, gives

$$
\begin{gathered}
I_0 = \sqrt{\frac{2\sqrt{\omega_0\omega_K}}{s}}\exp\Big[-\frac{\omega_0}{2\omega_K}\Delta_K^2\Big(1 - \frac{\omega_0}{s}\Big)\Big],\qquad
A = \frac{2\omega_K}{s} - 1,\qquad C = \frac{2\omega_0}{s} - 1,\\
B = -\frac{2\omega_0}{s}\Delta_K,\qquad D = 2\sqrt{\frac{\omega_0}{\omega_K}}\Big(1 - \frac{\omega_0}{s}\Big)\Delta_K,\qquad E = \frac{4\sqrt{\omega_0\omega_K}}{s}.
\end{gathered}
\label{coeffs}
$$

**Two misprints in NRS Eq. 6.123.** $A$, $B$, $C$ and $D$ agree with NRS. Two coefficients do not:

- **$E$.** NRS print $4\sqrt{\omega_0/\omega_K}/s$, which is not dimensionless.
- **$I_0$.** NRS's prefactor $\sqrt{2\omega_K/s}$ lacks the factor $(\omega_0/\omega_K)^{1/4}$ from normalizing the oscillators in $Q$. It matters whenever $\omega_0\neq\omega_K$; for $\Delta_K = 0$ the correct $I_0$ is the familiar $\langle0|0'\rangle = [2\sqrt{\omega_0\omega_K}/(\omega_0 + \omega_K)]^{1/2}$.

Both corrections are confirmed by quadrature in the worked example. Exchanging $T\leftrightarrow U$ together with the two frequencies gives emission instead of absorption.

**Equal frequencies: the Poisson progression.** With $\omega_0 = \omega_K$ and only $n = 0$ populated (see the population argument in [[zero-point-vibrational-corrections-to-properties]]), $A = C = 0$, $B = -\Delta$, $D = \Delta$, $E = 2$, $I_0 = e^{-\Delta^2/4}$, and

$$
|S(k,0)|^2 = e^{-S}\frac{S^k}{k!},\qquad S = \frac{\Delta^2}{2}
\label{poisson}
$$

(NRS Eqs. 6.124–6.128; there the factors $\omega_0$ in $I_0$ and $E$ amount to setting $\omega_0 = 1$). $S$ is the Huang–Rhys factor. Its consequences:

- **Weak coupling** ($S\ll1$). The 0–0 line dominates.
- **Strong coupling** ($S\gg1$). The progression peaks near $k\approx S$, and the 0–0 line, $e^{-S}$, can be invisible.
- **Band centre.** The intensity-weighted mean lies $S\hbar\omega = \lambda$ above the 0–0 line, where $\lambda$ is the reorganization energy.
- **Vertical against adiabatic.** In the displaced-oscillator model the vertical excitation energy is the adiabatic one plus $\lambda$. Absorption maxima typically lie 0.2–0.3 eV above computed adiabatic (0–0) energies, which should be compared with the band onset (NRS Sec. 6.7.2).
- **Mirror symmetry.** Emission from the relaxed excited state is the mirror image of absorption about the 0–0 line (NRS Fig. 6.12). Deviations from mirror symmetry signal frequency changes, Duschinsky mixing or a change of mechanism.
- **Line shape and broadening.** Homogeneous (lifetime) broadening can wash out the structure. An asymmetric envelope suggests an unresolved vibronic progression rather than separate electronic states.

## The linear coupling model

**The two assumptions** (NRS Eqs. 6.129–6.130):

- **A common force field** ($\mathbf J = \mathbf 1$, $\boldsymbol\Gamma_K = \boldsymbol\Gamma_0$).
- **Displacements from the vertical gradient.** On the excited surface $E_K(Q)\approx E_K(0) + \sum_ag_aQ_a + \tfrac12\sum_a\omega_a^2Q_a^2$ with $g_a = \partial E_K/\partial Q_a$, so the minimum is at $Q_a = -g_a/\omega_a^2$. In dimensionless units:

$$
\Delta_a = -\frac{g_a}{\omega_a^{3/2}},\qquad S_a = \frac{g_a^2}{2\omega_a^3},\qquad \lambda = \sum_aS_a\omega_a = \sum_a\frac{g_a^2}{2\omega_a^2}.
\label{lcm}
$$

**What it needs.** The vibronic structure then requires only the ground-state Hessian and one excited-state gradient. The latter is the gradient of a response-theory excitation energy, from a residue of the quadratic response function or from a TDDFT gradient Lagrangian ([[tddft-linear-response]]).

**Which modes appear.** Only modes along which the gradient is nonzero form progressions. At a symmetric ground-state geometry these are the totally symmetric modes. The modes with the largest $g_a^2/\omega_a^3$ dominate, and they follow from what the excitation does to the bonding.

**Limits.** The model misses frequency changes, Duschinsky mixing and symmetry-breaking distortions of the excited state. A pyramidal or twisted excited-state minimum cannot be reached along a gradient that vanishes by symmetry.

## Herzberg–Teller intensity borrowing

**The selection rule.** The second term of Eq. [[#ht]] reaches $|k\rangle = |1_a\rangle$ (one quantum in mode $a$), with moment $\sqrt{\hbar/2\omega_a}\,\partial\mu^{K0}/\partial Q_a$. It is nonzero when $\Gamma(K)\otimes\Gamma(Q_a)\otimes\Gamma(\mu_\alpha)\ni A_1$.

**Properties of HT bands.**

- **False origins.** HT bands are built on false origins displaced by one quantum of the inducing (nontotally symmetric) mode, carrying the totally symmetric progressions on top.
- **Weakness.** They are weak, because $\partial\mu^{K0}/\partial Q_a$ comes from mixing with distant allowed states.
- **Temperature dependence.** Their intensity grows with temperature as hot bands $\langle1_a|\to\langle0_a|$ of the inducing mode are added.

**The d–d example (NRS Sec. 6.7.4).** In an octahedral complex all $d$ orbitals are $g$ ($E_g$, $T_{2g}$) and $\hat{\boldsymbol\mu}$ is $T_{1u}$, so $d\to d$ transitions are parity (Laporte) forbidden ([[parity-and-parity-selection-rules]]). Of the 15 modes of an ML₆ unit ($A_{1g} + E_g + T_{2g} + 2T_{1u} + T_{2u}$), the $u$ modes give

$$
T_{1u}\otimes T_{1u} = A_{1g}\oplus E_g\oplus T_{1g}\oplus T_{2g},\qquad T_{2u}\otimes T_{1u} = A_{2g}\oplus E_g\oplus T_{1g}\oplus T_{2g}.
$$

These products contain every $g$ symmetry reached by $d\to d$ transitions, so all of them become vibronically allowed. This is why such bands are weak (ε ~ 1–100 M⁻¹ cm⁻¹) rather than absent.

## Worked example

!!! example "Generating function, Poisson limit and formaldehyde S₁ (recomputed for this note)"
    **Generating function.** For $\omega_0 = 1$, $\omega_K = 0.7$ and a displacement $d = 1.3$ ($\Delta_K = 1.0877$), $S(k,n)$ for $k,n\le3$ was computed by direct quadrature of the normalized oscillator functions in $Q$ (40 001 points on ±12). It was also extracted from the power series of Eq. [[#genfun]].

    - **Eq. [[#coeffs]].** It reproduces all sixteen overlaps to $4\times10^{-13}$ (e.g. $S(0,0) = 0.700577$, $S(1,0) = -0.633891$, $S(1,1) = 0.209714$).
    - **NRS's printed coefficients.** They give $S(0,0) = 0.6408$ (missing $(\omega_0/\omega_K)^{1/4}$) and errors up to 0.74 in the $n,k\ge1$ block (from $E$).

    **Poisson limit.** For equal frequencies and $\Delta = 1.6$ ($S = 1.28$), quadrature gives $|S(k,0)|^2 = 0.27804, 0.35589, 0.22777, 0.09718, 0.03110, \dots$. These are identical to $e^{-S}S^k/k!$ in Eq. [[#poisson]], and the first moment is $\sum_kk|S(k,0)|^2 = 1.28 = S$.

    **Formaldehyde, $S_1$ ($1^1A_2$, $n\to\pi^*$), TDA-B3LYP/aug-cc-pVDZ.** The vertical excitation energy at the optimized ground-state geometry is 3.930 eV, with oscillator strength $2\times10^{-16}$: symmetry forbidden. Linear coupling model, Eq. [[#lcm]], with B3LYP harmonic frequencies:

    | mode | ω (cm⁻¹) | symmetry | $\Delta_a$ | $S_a$ |
    |---|---:|---|---:|---:|
    | ν₄ out-of-plane wag | 1194 | $b_1$ | 0 | 0 |
    | ν₆ CH₂ rock | 1246 | $b_2$ | 0 | 0 |
    | ν₃ CH₂ scissor | 1513 | $a_1$ | 0.289 | 0.042 |
    | ν₂ C=O stretch | 1802 | $a_1$ | 1.326 | 0.879 |
    | ν₁ C–H stretch | 2891 | $a_1$ | 0.214 | 0.023 |
    | ν₅ C–H stretch | 2959 | $b_2$ | 0 | 0 |

    - **The progression.** The model predicts a band dominated by a C=O stretch progression with $S\approx0.9$: the $n\to\pi^*$ excitation weakens the C=O bond. The reorganization energy is $\lambda = 1714$ cm⁻¹ = 0.21 eV.
    - **What it misses.** The experimental $S_1$ minimum is pyramidal (the ν₄ coordinate becomes a double well), and the C=O frequency drops strongly. The model can show neither, since the gradient along the $b_1$ mode vanishes at the planar geometry.

    **Herzberg–Teller along ν₄.** TDA transition dipoles at $\xi_4 = \pm0.2$ give $|\partial\mu^{K0}/\partial Q_4| = 4.82\times10^{-3}$ au, polarized along $y$ (in plane, perpendicular to C=O). This is as symmetry requires: $A_2\otimes B_1 = B_2$, the symmetry of $y$.

    - **The false origin.** The moment to $|1_4\rangle$ is $\sqrt{1/2\omega_4}\,|\partial\mu/\partial Q_4| = 0.0462$ au, giving $f(0\to1_4) = \tfrac23(\omega_{K0} + \omega_4)|\mu|^2 = 2.1\times10^{-4}$. Summed over the $a_1$ progressions built on this origin, this is the band's total HT intensity.
    - **Against experiment.** The measured oscillator strength of the formaldehyde $n\to\pi^*$ band is of order $2\times10^{-4}$ (to verify).

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 6.7, Eqs. (6.106)–(6.111), Figs. 6.10–6.11 (described); Sec. 6.7.1, Eqs. (6.112)–(6.123); Sec. 6.7.2, Eqs. (6.124)–(6.128), Fig. 6.12 (described); Sec. 6.7.3, Eqs. (6.129)–(6.130); Sec. 6.7.4. T. E. Sharp and H. M. Rosenstock, "Franck–Condon factors for polyatomic molecules", *J. Chem. Phys.* **41**, 3453 (1964), cited by NRS for the polyatomic generating function (not read). The false-origin and hot-band remarks and the formaldehyde excited-state geometry are general knowledge, not from NRS. The calculations are in `Claude outputs/part4_response_batchC.py`, sections C and D.
