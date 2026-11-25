---
id: optical-activity-ecd-and-mcd
title: Chiroptical properties - optical rotation, electronic circular dichroism, rotatory strengths, gauge origin, and magnetic circular dichroism (Faraday A, B, C terms)
summary: A chiral molecule refracts and absorbs left and right circularly polarized light differently. Both effects come from the mixed electric dipole–magnetic dipole polarizability G′(ω): its real (dispersive) part gives optical rotation, the rotatory strengths at its poles give ECD. In a finite basis the length-gauge G′ depends on the gauge origin and the velocity gauge has an unphysical static limit; London orbitals or the modified velocity gauge cure this. In a magnetic field every molecule shows circular dichroism (MCD), described by the Faraday A, B and C terms, which are residues of a quadratic response function. Recomputed: full-RPA rotatory strengths and [α]_D of (S)-methyloxirane in length, velocity and modified velocity gauges; the conversion β → [α]_D against NRS Table 8.8.
status: in-progress
kind: theory
level: advanced
tags: [optical-rotation, ord, ecd, circular-dichroism, rotatory-strength, rosenfeld, gauge-origin, modified-velocity-gauge, london-orbitals, mcd, faraday-terms, birefringence, chirality]
prerequisites: [magnetizability-and-gauge-origin, residue-analysis-of-response-functions, electronic-absorption-and-emission]
related: [damped-response-and-absorption-cross-sections, vibrational-optical-activity, polarization-propagator-rpa, linear-response-for-variational-wave-functions, exact-state-response-functions]
conventions: [atomic-units]
key: rosenfeld
order: 140
date: 2026-11-24
---

Atomic units. The electron charge is $-1$, so $\hat{\boldsymbol\mu} = -\sum_i\mathbf r_i$ (plus nuclear terms) and $\hat{\mathbf m} = -\tfrac12\hat{\mathbf L}_O$ with $\hat{\mathbf L}_O$ about the gauge origin $\mathbf O$; $\hat{\mathbf P} = \sum_i\hat{\mathbf p}_i$. Exact states $|n\rangle$, $\omega_{n0} = E_n - E_0$. Repeated Cartesian indices are summed.

## Birefringence and dichroism

**Circular birefringence.** A medium with different refractive indices $n_\pm$ for the two circular components, $\Delta n = n_+ - n_-$ (NRS Eq. 8.198), rotates the plane of linearly polarized light. Writing linear light as a superposition of the two circular waves (NRS Eqs. 8.201–8.205):

$$
\Delta\theta = -\frac{\omega\,\Delta z\,\Delta n}{2c}.
$$

**Circular dichroism.** A difference in absorption, $\Delta\epsilon = \epsilon_+ - \epsilon_-$, makes the light elliptical. The two are the dispersive and absorptive faces of one complex response, linked by Kramers–Kronig relations.

**Natural and magnetic activity.**

- **Natural optical activity** (optical rotation, ORD, ECD) requires a chiral molecule: one not superimposable on its mirror image, which means no improper rotation axis $S_n$ (including $\sigma = S_1$ and $i = S_2$).
- **Magnetic optical activity** (Faraday rotation and MCD) appears in every molecule in a magnetic field parallel to the light (NRS Fig. 8.29).

## Optical rotation

**The tensor G′.** For an isotropic sample the relevant molecular quantity is the trace of the mixed electric dipole–magnetic dipole polarizability. In sum-over-states form (Barron's convention):

$$
G'_{\alpha\beta}(\omega) = -2\omega\sum_n{}'\frac{\mathrm{Im}\,\langle0|\hat\mu_\alpha|n\rangle\langle n|\hat m_\beta|0\rangle}{\omega_{n0}^2 - \omega^2},\qquad
\beta(\omega) = -\frac{1}{3\omega}G'_{\alpha\alpha}(\omega) = \frac23\sum_n{}'\frac{R_{n0}}{\omega_{n0}^2 - \omega^2},
\label{rosenfeld}
$$

with the rotatory strength

$$
R_{n0} = \mathrm{Im}\big[\langle0|\hat{\boldsymbol\mu}|n\rangle\cdot\langle n|\hat{\mathbf m}|0\rangle\big].
\label{rstrength}
$$

This is Rosenfeld's equation, NRS Eqs. (8.206)–(8.208). NRS write the dispersion denominator as $(\omega_{n0} - \omega)^2$, a misprint for $\omega_{n0}^2 - \omega^2$.

**Convention.** NRS also write $G' = -\mathrm{Im}\langle\langle\hat\mu_\alpha;\hat m_\beta\rangle\rangle_\omega$. With the response-function convention of [[exact-state-response-functions]] ($\langle\langle A;B\rangle\rangle_\omega = -\sum'_n[A_{0n}B_{n0}/(\omega_{n0}-\omega) + B_{0n}A_{n0}/(\omega_{n0}+\omega)]$), the sum-over-states form above equals $+\mathrm{Im}\langle\langle\hat\mu_\alpha;\hat m_\beta\rangle\rangle_\omega$. The sign in front of Im depends on the time-dependence convention, so here $G'$ is fixed by its sum-over-states form (my reading; to verify).

**Specific rotation.** The observable is the specific rotation, in deg dm⁻¹ (g mL⁻¹)⁻¹ at the sodium D line (589.29 nm):

$$
[\alpha]_D = \frac{28800\,\pi^2N_A\,a_0^4\,\tilde\nu^2}{M}\,\beta\;=\;38\,654\,\frac{\beta\ [\mathrm{au}]}{M\ [\mathrm{g\,mol^{-1}}]}\quad(\tilde\nu = 1/589.29\ \mathrm{nm}).
\label{alphaD}
$$

$\beta$ in cgs units (cm⁴) is $a_0^4$ times $\beta$ in atomic units, when $R$ is in $e a_0\cdot e\hbar/m_e$ ($1\ \mathrm{au} = 471.44\times10^{-40}$ esu² cm²). NRS Eq. 8.207 writes the same relation with a compressed prefactor.

**Properties.**

- **A small difference of large numbers.** Each $R_{n0}$ is positive or negative. Near a band the rotation is large and changes sign (the anomalous dispersion of a Cotton effect); at 589 nm it is a small difference of large contributions.
- **Sum rule.** For exact states $\sum'_nR_{n0} = \mathrm{Im}\langle0|\hat{\boldsymbol\mu}\cdot\hat{\mathbf m}|0\rangle = 0$ (NRS Eq. 8.217). Consequently $[\alpha]\to0$ for $\omega\gg\omega_{n0}$ (NRS Eq. 8.218).
- **Cancellation between components.** The diagonal components $\omega^{-1}G'_{\alpha\alpha}$ are typically ten to a hundred times larger than their trace (NRS Table 8.8: −0.820, −0.812, +1.587 for methyloxirane, summing to −0.045). Small errors in each component can flip the sign of $[\alpha]$.
- **Sensitivity.** The specific rotation depends strongly on conformation (NRS Figs. 8.31–8.32): even propane has a nonzero, dihedral-dependent $[\alpha]$ when frozen in a chiral conformation, and flexible molecules need Boltzmann averaging. It also depends on solvent, and needs diffuse basis functions.

**Damped response.** With damping, the real part of the complex $\beta(\omega)$ gives ORD through the resonance region and the imaginary part gives ECD (NRS Fig. 8.30). The anomalous dispersion is then regular at each band.

## The gauge-origin problem for G′

**Length gauge.** Under $\mathbf O\to\mathbf O + \mathbf D$, $\hat{\mathbf m}$ gains $\tfrac12\mathbf D\times\hat{\mathbf P}$ (NRS Eqs. 8.209–8.211):

$$
G'_{\alpha\beta}(\mathbf O + \mathbf D) = G'_{\alpha\beta}(\mathbf O) + \tfrac12\epsilon_{\beta\gamma\delta}D_\gamma\,\mathrm{Im}\langle\langle\hat\mu_\alpha;\hat P_\delta\rangle\rangle_\omega\;\overset{\rm exact}{=}\;G'_{\alpha\beta}(\mathbf O) + \tfrac{\omega}{2}\epsilon_{\beta\gamma\delta}D_\gamma\,\alpha_{\alpha\delta}.
$$

The trace of the correction is $\epsilon_{\alpha\gamma\delta}D_\gamma\alpha_{\alpha\delta} = 0$ because $\alpha$ is symmetric. So $\beta$ is origin independent for exact states, but only if $\langle\langle\hat\mu;\hat P\rangle\rangle = i\omega\alpha$-type relations hold, which they do not in a finite basis.

**Velocity gauge.** Replacing $\hat{\boldsymbol\mu}$ by the velocity form through $\langle0|\hat{\mathbf r}|n\rangle = i\langle0|\hat{\mathbf p}|n\rangle/\omega_{n0}$ (NRS Eq. 8.212) makes $G'$ origin independent in any basis, since the shift term involves $\langle\langle\hat P;\hat P\rangle\rangle$, which is symmetric. However, the velocity-gauge $G'$ does not vanish at $\omega = 0$ in a finite basis, although the exact static $G'$ does.

**Modified velocity gauge (MVG).** Subtract the static limit (NRS Eq. 8.213). In sum-over-states form:

$$
\beta^{\rm MVG}(\omega) = \frac23\sum_n{}'R^{\rm vel}_{n0}\Big[\frac{1}{\omega_{n0}^2 - \omega^2} - \frac{1}{\omega_{n0}^2}\Big],\qquad
R^{\rm vel}_{n0} = \mathrm{Im}\big[\boldsymbol\mu^{\rm vel}_{0n}\cdot\langle n|\hat{\mathbf m}|0\rangle\big],\qquad \boldsymbol\mu^{\rm vel}_{0n} = -\frac{i}{\omega_{n0}}\langle0|\hat{\mathbf P}|n\rangle,
$$

where the minus sign in $\boldsymbol\mu^{\rm vel}$ is the electron charge. Two remedies remain:

- **MVG** is origin independent and has the right static limit, but it is not exact for nonvariational methods.
- **London orbitals**, the other remedy, make length-gauge $\beta$ origin independent for variational methods and converge faster with basis set (NRS Sec. 8.6.1).

## Electronic circular dichroism

With a normalized line shape $f(\omega;\omega_{n0},\gamma)$, the decadic molar CD in SI units is (NRS Eq. 8.214)

$$
\Delta\epsilon(\omega) = \frac{16\pi^2N_A\,\omega}{3\times1000\,\ln10\,(4\pi\varepsilon_0)\hbar c^2}\sum_nf(\omega;\omega_{n0},\gamma)\,R_{n0}.
$$

The rotatory strength is the residue of $G'$ at $\omega_{n0}$, in the length form (NRS Eq. 8.215) or the velocity form (NRS Eq. 8.216).

**Properties.**

- **Enantiomers.** $R_{n0}$ changes sign between enantiomers, so ECD bands are signed and assign absolute configuration when theory and experiment are compared band by band. This is more robust than a single $[\alpha]_D$, because each band is a separate check.
- **Origin dependence.** In the length form $R_{n0}$ depends on the origin through $\tfrac12\mathbf D\cdot(\boldsymbol\mu_{0n}\times\mathbf P_{n0})$-type terms. These vanish when $\boldsymbol\mu$ and $\mathbf P$ matrix elements satisfy the hypervirial relation, approximately in a large basis. The velocity form is origin independent.
- **Emission.** Circularly polarized luminescence (CPL) is ECD in emission from the relaxed excited state. It can show chirality the ground state lacks, induced by excited-state distortion (NRS Fig. 8.33, pyramidalization at a ketone carbon).

## Magnetic circular dichroism

**Origin.** A field $\mathbf B$ along the light propagation lifts degeneracies and mixes states. The polarizability becomes $\alpha_{\alpha\beta}(\omega,\mathbf B) = \alpha_{\alpha\beta}(\omega) + (\partial\alpha_{\alpha\beta}/\partial B_\gamma)B_\gamma + \cdots$ (NRS Eq. 8.220), and its antisymmetric part gives Faraday rotation and MCD.

**Faraday terms.** The MCD of a band $0\to n$ is (NRS Eqs. 8.221–8.224)

$$
\Delta\epsilon(\omega)\propto-B\Big[\mathcal A_{0n}\Big(-\frac{\partial f}{\partial\omega}\Big) + \Big(\mathcal B_{0n} + \frac{\mathcal C_{0n}}{kT}\Big)f(\omega)\Big]
$$

(signs and prefactor as in NRS Eq. 8.221). The three terms:

- **A term.** Zeeman splitting of a degenerate excited (or ground) state. It is derivative shaped (bisignate) and needs degenerate irreducible representations. It is the double residue of the quadratic response function $\langle\langle\hat\mu;\hat m,\hat\mu\rangle\rangle$ (NRS Eq. 8.225).
- **B term.** Field-induced mixing of $|n\rangle$ (and $|0\rangle$) with other states $|k\rangle$ through $\hat{\mathbf m}$, weighted by $1/\omega_{kn}$ or $1/\omega_{k0}$. It has an absorptive shape of either sign and exists for every molecule. It is a single residue of the same quadratic response function (NRS Eq. 8.226).
- **C term.** Unequal Boltzmann populations of a Zeeman-split degenerate ground state. It has an absorptive shape and $1/T$ dependence, and it vanishes for closed-shell molecules with nondegenerate ground states.

**Closed shells.** For an orbitally nondegenerate ground state the whole MCD spectrum, including the overlap of bands, follows from the damped quadratic response function: $\Delta\epsilon\propto B\,\epsilon_{\alpha\beta\gamma}\mathrm{Re}\langle\langle\hat\mu_\alpha;\hat m_\beta,\hat\mu_\gamma\rangle\rangle_{0,\omega}$ (NRS Eq. 8.227).

**Example (described).** For planar Zn porphyrin ($D_{4h}$) the Q and B bands are degenerate ($E_u$) and give bisignate A-term features. Bending the macrocycle lowers the symmetry, splits the $E_u$ pairs, and turns the pattern into pairs of opposite-signed B terms (NRS Fig. 8.36).

**Other nonlinear birefringences.** Related effects are the Kerr effect (field-induced linear birefringence, through $\gamma$ and $\Delta\alpha^2/kT$) and the Cotton–Mouton effect (magnetic). The Buckingham effect (field-gradient-induced birefringence, Table 8.9) measures molecular quadrupole moments, from mixed quadratic response functions of $\hat\mu$, $\hat m$ and $\hat\Theta$ (NRS Eqs. 8.228–8.234).

## Worked example

!!! example "(S)-methyloxirane by full RPA (recomputed for this note)"
    **Setup.** Geometry: HF/6-31G* optimized. The $S$ configuration was checked from the sign of $(\mathbf v_{\rm O}\times\mathbf v_{\rm C_{ring}})\cdot\mathbf v_{\rm CH_3}$ at the stereocentre, which is positive for $S$. Full TDHF (RPA) by diagonalizing $(\mathbf A-\mathbf B)^{1/2}(\mathbf A+\mathbf B)(\mathbf A-\mathbf B)^{1/2}$. All 2080 (aug-cc-pVDZ) or 4896 (aug-cc-pVTZ) states were kept, so the sums over states are complete within RPA.

    - **Moments.** $\langle0|\hat{\boldsymbol\mu}|n\rangle = \sqrt2\,(-\mathbf r)_{ia}(X+Y)_{ia}$, $\langle0|\hat{\mathbf m}|n\rangle = \sqrt2\,\tfrac{i}{2}(\mathbf r\times\nabla)_{ia}(X-Y)_{ia}$. Velocity moments come from $\langle i|\nabla|a\rangle$.
    - **Sign check.** The length and velocity dipoles agree in sign for every bright state.
    - **TRK sums.** $\sum f$ is 26.0/25.4 (DZ, length/velocity) and 28.5/28.7 (TZ), against $N = 32$. The core region is not complete.

    **Lowest states**, aug-cc-pVTZ. $R$ in au (×471.44 for $10^{-40}$ cgs); origin at the centre of mass unless stated:

    | $\omega_{n0}$ / eV | $f$ | $R^{\rm len}$ | $R^{\rm len}$, origin +10 bohr | $R^{\rm vel}$ |
    |---:|---:|---:|---:|---:|
    | 8.872 | 0.0055 | +0.00762 | +0.00753 | +0.00758 |
    | 9.109 | 0.0064 | +0.00182 | +0.00182 | +0.00195 |
    | 9.307 | 0.0264 | −0.00854 | −0.00902 | −0.00867 |
    | 9.395 | 0.0469 | +0.00288 | +0.00312 | +0.00290 |
    | 9.425 | 0.0360 | +0.06799 | +0.06808 | +0.06806 |

    - **Origin dependence.** Single rotatory strengths are nearly origin independent at TZ.
    - **Energies.** The excitation energies are about 1.8 eV above the experimental first Rydberg band (7.1 eV, to verify), as expected for TDHF.
    - **Sum rule.** $\sum_nR^{\rm len}_{n0} = -2.5\times10^{-4}$ against $\sum|R_{n0}| = 14.9$ au, so the sum rule holds within RPA to $2\times10^{-5}$ relative. At DZ it is $-1.1\times10^{-3}$ against 14.0.

    **Specific rotation at 589.29 nm**, $\omega = 0.077319$ au, $M = 58.08$:

    | gauge | aug-cc-pVDZ $\beta$ | $[\alpha]_D$ | aug-cc-pVTZ $\beta$ | $[\alpha]_D$ |
    |---|---:|---:|---:|---:|
    | length, origin at COM | −0.01781 | −11.9 | −0.00854 | −5.7 |
    | length, origin COM + 10 bohr | −0.03376 | −22.5 | −0.00872 | −5.8 |
    | velocity | −0.02081 | −13.8 | −0.00961 | −6.4 |
    | modified velocity | +0.00219 | +1.5 | +0.00249 | +1.7 |

    **What the table shows.**

    - **The length gauge.** It is origin dependent at DZ: 10 bohr doubles $\beta$. At TZ the dependence nearly disappears.
    - **The velocity gauge.** Its spurious static part, $-\tfrac23\sum R^{\rm vel}/\omega_{n0}^2 = -0.0230$ (DZ) and $-0.0121$ (TZ), dominates the unmodified value.
    - **The modified velocity gauge.** It is stable between the bases (+1.5, +1.7). The length value moves toward it as the basis grows; the two must agree in the complete-basis limit.
    - **The sign is undetermined.** At the HF level in these bases even the sign of $[\alpha]_D$ cannot be fixed. This is the cancellation NRS emphasize: in the input axes at DZ, $\omega^{-1}G'_{\alpha\alpha} = (+1.476, -0.499, -0.924)$, with a trace of $-0.053$.

    **Conversion check.** Eq. [[#alphaD]] applied to NRS Table 8.8 reproduces their specific rotations: H₂O₂ $\beta = -0.049$ → −55.7 (NRS −55.3); methyloxirane $+0.015$ → +10.0 (+10.2); camphor $+0.239$ → +60.7 (+60.5). The residual differences come from rounding $\beta$ to three digits.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 8.6.1, Eqs. (8.198)–(8.213), Table 8.8, Figs. 8.29–8.32 (described); Sec. 8.6.2, Eqs. (8.214)–(8.218), Figs. 8.33–8.34 (described); Sec. 8.6.3, Eqs. (8.219)–(8.234), Table 8.9, Figs. 8.35–8.36 (described). The cgs form of Eq. [[#alphaD]] and the atomic-unit conversion of $R$ are standard and checked here numerically. The calculations are in `Claude outputs/part4_response_batchB2.py`, section F.
