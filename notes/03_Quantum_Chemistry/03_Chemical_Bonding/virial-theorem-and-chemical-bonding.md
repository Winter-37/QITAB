---
id: virial-theorem-and-chemical-bonding
title: The virial theorem and the energetics of bond formation
summary: From the molecular virial theorem, ⟨T⟩ = −U − R dU/dR and ⟨V⟩ = 2U + R dU/dR along a diatomic potential curve. At R_e the kinetic energy is higher and the potential energy lower than in the separated atoms, by D_e and 2D_e. At large R the order reverses - ⟨T⟩ first falls and ⟨V⟩ first rises - so ⟨T⟩ has a minimum and ⟨V⟩ a maximum outside R_e. Shown for H₂ from an FCI/cc-pVQZ curve (⟨T⟩ minimum 0.869 E_h at 2.91 bohr, ⟨V⟩ maximum at 3.29 bohr) and for H₂⁺. The LCAO with exponent 1 lowers ⟨T⟩ at its minimum, while the exponent-optimized LCAO raises it and obeys the virial theorem exactly.
status: in-progress
kind: theory
level: intermediate
tags: [virial-theorem, chemical-bond, kinetic-energy, potential-energy, h2, h2-plus, bonding-mechanism]
prerequisites: [hellmann-feynman-and-virial-theorems, hydrogen-molecule-ion-variational]
related: [h2-minimal-basis-correlation-analysis, mo-and-valence-bond-theories, diatomic-vibration-and-anharmonicity]
order: 20
date: 2026-11-18
---

Atomic units. $U(R)$ is the Born–Oppenheimer potential energy (electronic energy plus $1/R$), $\langle T\rangle$ the electronic kinetic energy and $\langle V\rangle$ the total potential energy including nuclear repulsion.

## Kinetic and potential energy along the curve

For the exact electronic wave function of a diatomic molecule the virial theorem ([[hellmann-feynman-and-virial-theorems]]) reads

$$
2\langle T\rangle + \langle V\rangle = -R\,\frac{\mathrm dU}{\mathrm dR},\qquad \langle T\rangle + \langle V\rangle = U ,
$$

so the curve $U(R)$ alone fixes both parts:

$$
\langle T\rangle = -U - R\,\frac{\mathrm dU}{\mathrm dR},\qquad \langle V\rangle = 2U + R\,\frac{\mathrm dU}{\mathrm dR} .
$$

**At the extremes.** At $R_e$ and at $R = \infty$ the derivative vanishes, so $\langle T\rangle = -U$ and $\langle V\rangle = 2U$ there, just as for an atom. Subtracting,

$$
\langle T\rangle_{R_e} - \langle T\rangle_\infty = U(\infty) - U(R_e) = D_e,\qquad
\langle V\rangle_{R_e} - \langle V\rangle_\infty = -2D_e .
$$

A stable bond has **more** kinetic energy than the separated atoms and twice as much less potential energy. Equivalently, $D_e = \tfrac12(\langle V\rangle_\infty - \langle V\rangle_{R_e})$.

**At large R.** The dispersion tail $U \approx U(\infty) - A/R^6$ (with $A > 0$) gives

$$
\langle V\rangle \approx \langle V\rangle_\infty + \frac{4A}{R^6},\qquad \langle T\rangle \approx \langle T\rangle_\infty - \frac{5A}{R^6} .
$$

As the atoms approach, the potential energy **rises** and the kinetic energy **falls**. Combined with the values at $R_e$, $\langle V\rangle$ must pass through a maximum and $\langle T\rangle$ through a minimum somewhere outside $R_e$.

**At small R.** United-atom perturbation theory gives $U \approx 1/R + E_{\text{UA}} + aR^2$, so $\langle T\rangle \approx -E_{\text{UA}} - 3aR^2$ and $\langle V\rangle \approx 1/R + 2E_{\text{UA}} + 4aR^2$.

## The physical picture (Levine)

Take H₂⁺.

- **At large $R$.** The region midway between the protons is a high-potential-energy region, so moving density there raises $\langle V\rangle$. The density also becomes less compact than in a single atom, which lowers $\langle T\rangle$ (by the uncertainty principle, $\langle p_x^2\rangle \ge \hbar^2/4(\Delta x)^2$).
- **At intermediate $R$.** The two potential wells merge and the midpoint becomes a low-potential-energy region. The density now contracts toward the nuclei, raising $\langle T\rangle$ above its atomic value and lowering $\langle V\rangle$.
- **Inside $R_e$.** The rise of $U(R)$ is driven by the further increase of $\langle T\rangle$ from squeezing the density; $\langle V\rangle$ is still falling steeply there. The internuclear repulsion matters only at smaller $R$.

!!! example "H₂: ⟨T⟩ and ⟨V⟩ from the FCI/cc-pVQZ curve"
    **Method.** The FCI/cc-pVQZ curve (71 points, 0.6-10 bohr, the curve of [[diatomic-vibration-and-anharmonicity]]) is splined and differentiated.

    | | $R$ (bohr) | $U$ ($E_h$) | $\langle T\rangle$ ($E_h$) | $\langle V\rangle$ ($E_h$) |
    |---|---:|---:|---:|---:|
    | equilibrium | 1.4018 | −1.17380 | 1.17385 | −2.34764 |
    | minimum of $\langle T\rangle$ | 2.91 | | 0.8690 | |
    | maximum of $\langle V\rangle$ | 3.29 | | | −1.9196 |
    | 10 bohr | 10.0 | −0.99990 | 0.99986 | −1.99976 |

    - **Equilibrium values.** $\langle T\rangle_{R_e} - \langle T\rangle_{10} = 0.17399\,E_h$ equals $U(10) - U(R_e)$ to $1\times10^{-4}\,E_h$, the spline accuracy.
    - **The dip.** Near 3 bohr the kinetic energy is 0.13 $E_h$ below the atoms' value; by $R_e$ it has risen to 0.17 $E_h$ above it.
    - **Direct check.** $\langle T\rangle$ from the FCI/cc-pVQZ density matrix at $R_e$ is 1.17317 $E_h$, 0.7 m$E_h$ below the virial value. A finite basis does not satisfy the virial theorem exactly.

!!! example "H₂⁺: fixed and optimized exponent"
    **Method.** LCAO $\sigma_g = N(a + b)$ with Slater 1s orbitals of exponent $\zeta$, using the 22-Gaussian fit. The H atom has $\langle T\rangle = 0.5$.

    | | $R_e$ (bohr) | $\zeta$ | $E$ ($E_h$) | $\langle T\rangle$ ($E_h$) | $-E/\langle T\rangle$ |
    |---|---:|---:|---:|---:|---:|
    | $\zeta = 1$ fixed | 2.493 | 1 | −0.56483 | 0.38271 | 1.476 |
    | $\zeta$ optimized | 2.003 | 1.2380 | −0.58651 | 0.58651 | 1.00000 |

    - **Fixed exponent.** The function cannot contract, so it lowers the kinetic energy at its minimum, and the virial theorem fails badly.
    - **Optimized exponent.** Scaling $\zeta$ is equivalent to scaling all coordinates, so the optimized function satisfies $\langle T\rangle = -E$ to $5\times10^{-8}$. Its kinetic energy exceeds the atom's, as for the exact wave function. (Levine's Finkelstein–Horowitz values are $\zeta = 1.24$ and $R_e = 2.00$ bohr.)
    - **Reconciling the two pictures.** The energy decomposition of [[h2-minimal-basis-correlation-analysis]], with exponent 1, likewise finds a lowered kinetic energy. Whether "the bond lowers the kinetic energy" depends on whether the orbitals are allowed to contract.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 14.5, pp. 422-426: Eqs. (14.94)-(14.108), the changes in ⟨T⟩ and ⟨V⟩ between $R_e$ and $\infty$, the large-$R$ and small-$R$ behaviour, Fig. 14.1, and the H₂⁺ explanation (Figs. 14.2-14.3). The Finkelstein–Horowitz exponent is from Sec. 13.5. Calculations in `part3_batchC.py`, section G (spline of the FCI/cc-pVQZ curve from `part3_batchA.py`; PySCF).
