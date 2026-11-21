---
id: hydrogen-molecule-ion-variational
title: The hydrogen molecule ion by the variational method
summary: The one-electron chemical bond. With the protons clamped a distance R apart, the trial function is a sum of two hydrogen 1s functions (LCAO). The overlap, direct and exchange integrals are evaluated in closed form, and the energy curve has a minimum at R = 2.49 a0 with a binding energy of 1.76 eV, against 2.00 a0 and 2.79 eV. Letting the 1s exponent vary improves this to 2.00 a0 and 2.35 eV and restores the virial theorem. The odd combination is repulsive at every R.
status: in-progress
kind: derivation
level: intermediate
tags: [hydrogen-molecule-ion, variational-principle, lcao, chemical-bond, overlap-integral, exchange-integral, bonding-antibonding, born-oppenheimer, scaling, griffiths]
prerequisites: [variational-principle, linear-variation-method, hydrogen-atom]
related: [born-oppenheimer-approximation, hydrogen-molecule-heitler-london, minimal-basis-h2-model, helium-ground-state-variational, hellmann-feynman-and-virial-theorems, parity-and-parity-selection-rules, hydrogen-molecule-ion-exact]
order: 60
date: 2026-11-14
---

## Setup

H₂⁺ is one electron in the field of two protons. Clamp the protons at separation $R$ ([[born-oppenheimer-approximation]]) and work in atomic units. With $r_a$ and $r_b$ the distances of the electron from the two protons,

$$
H = -\tfrac12\nabla^2 - \frac1{r_a} - \frac1{r_b} + \frac1R .
$$

The question is whether the energy can be made lower than $-\tfrac12\ E_h$, the energy of a hydrogen atom plus a distant proton. If a trial function achieves that for some $R$, the variational principle proves that the system binds.

## Trial function

Near either proton the electron should look like a hydrogen ground state. Let $\phi_a = e^{-r_a}/\sqrt\pi$ and $\phi_b = e^{-r_b}/\sqrt\pi$ and take the linear combinations

$$
\psi_\pm = A_\pm\,(\phi_a \pm \phi_b) .
$$

This is a linear variation in a two-function basis ([[linear-variation-method]]). The coefficients are fixed by symmetry: inversion through the midpoint commutes with $H$ and exchanges $\phi_a$ and $\phi_b$, so the eigenfunctions are the even and odd combinations ([[parity-and-parity-selection-rules]]). In chemistry these are the bonding $1\sigma_g$ and antibonding $1\sigma_u$ orbitals, built as a linear combination of atomic orbitals (LCAO).

## The three integrals

**Overlap.** $\phi_a$ and $\phi_b$ are not orthogonal:

$$
I(R) = \langle\phi_a|\phi_b\rangle = e^{-R}\Big(1 + R + \frac{R^2}{3}\Big) ,
\qquad |A_\pm|^2 = \frac{1}{2(1\pm I)} .
$$

$I\to1$ as $R\to0$ and $I\to0$ as $R\to\infty$.

**Direct and exchange integrals.** Since $\phi_a$ is the ground state of the atom at $a$,

$$
H\phi_a = \Big(-\tfrac12 - \frac1{r_b} + \frac1R\Big)\phi_a ,
$$

and the same with $a$ and $b$ exchanged. Two integrals remain,

$$
D(R) = \Big\langle\phi_a\Big|\frac1{r_b}\Big|\phi_a\Big\rangle = \frac1R - \Big(1 + \frac1R\Big)e^{-2R} ,
\qquad
X(R) = \Big\langle\phi_a\Big|\frac1{r_a}\Big|\phi_b\Big\rangle = (1 + R)\,e^{-R} .
$$

$D$ is the attraction between the electron cloud on $a$ and proton $b$; it is the potential $\Phi(r)$ of a 1s charge cloud met in [[helium-ground-state-variational]], evaluated at $r = R$. $X$ has no classical analogue: it is the attraction of the overlap density $\phi_a\phi_b$ to a proton. Griffiths calls $X$ the exchange integral; it is a one-electron resonance integral and should not be confused with the two-electron exchange integral of Hartree-Fock theory.

## Energy curves

Collecting terms,

$$
\boxed{\,E_\pm(R) = -\frac12 - \frac{D \pm X}{1 \pm I} + \frac1R\,}
$$

In Griffiths' notation, with $x = R/a$ and $F(x) = E_+/|E_1|$,

$$
F(x) = -1 + \frac2x\;\frac{(1 - \tfrac23x^2)\,e^{-x} + (1 + x)\,e^{-2x}}{1 + (1 + x + \tfrac13x^2)\,e^{-x}} ,
$$

which is the same function. The system binds wherever $F < -1$.

- **Even combination.** $E_+$ drops below $-\tfrac12$ for $R$ greater than about $1.5\,a_0$ and has a minimum at $R = 2.49\,a_0$ (1.32 Å) with $E_+ = -0.5648\ E_h$, a binding energy of 1.76 eV. A bond exists.
- **Odd combination.** $E_-$ lies above $-\tfrac12$ at every $R$ and decreases monotonically: the state is repulsive. The node at the midplane removes electron density from the region between the protons.

The measured equilibrium separation is 1.06 Å ($2.00\,a_0$) and the binding energy 2.79 eV, so the simple function gives the bond but underestimates its strength by a third. As always, the upper bound is above the true energy.

## Scaling the exponent

The 1s function with unit exponent is right for $R\to\infty$ but wrong for $R\to0$, where the united atom is He⁺ with exponent 2. Use $\phi = (\zeta^3/\pi)^{1/2}e^{-\zeta r}$ and treat $\zeta$ as a second variational parameter. With $\rho = \zeta R$, the Hamiltonian matrix elements become

$$
H_{aa} = \frac{\zeta^2}{2} - \zeta - \zeta D(\rho) ,\qquad
H_{ab} = -\frac{\zeta^2}{2}I(\rho) + \zeta^2X(\rho) - 2\zeta X(\rho) ,
\qquad
E_+ = \frac{H_{aa} + H_{ab}}{1 + I(\rho)} + \frac1R .
$$

Minimizing over $\zeta$ and $R$ gives $\zeta = 1.238$, $R = 2.003\,a_0$ and $E_+ = -0.5865\ E_h$: the bond length is now right and the binding energy rises to 2.35 eV. At this point $\langle T\rangle = -E$ to eight digits, the virial theorem for a molecule at its equilibrium geometry ([[hellmann-feynman-and-virial-theorems]]). The orbital contracts ($\zeta>1$): the bond lowers the potential energy by more than it raises the kinetic energy.

!!! example "Energy curves"

    Total energies in $E_h$. "Basis" is the one-electron problem solved in the aug-cc-pV5Z Gaussian basis, which is converged to about $10^{-5}\ E_h$ and stands in for the exact curve.

    | $R/a_0$ | $E_+$, $\zeta = 1$ | optimal $\zeta$ | $E_+$, optimal $\zeta$ | Basis | $E_-$, $\zeta = 1$ |
    |---|---|---|---|---|---|
    | 1.0 | $-0.28837$ | 1.538 | $-0.44100$ | $-0.45176$ | $+0.54540$ |
    | 1.5 | $-0.49501$ | 1.361 | $-0.56712$ | $-0.58231$ | $+0.07256$ |
    | 2.0 | $-0.55377$ | 1.239 | $-0.58651$ | $-0.60262$ | $-0.16085$ |
    | 2.5 | $-0.56483$ | 1.154 | $-0.57876$ | $-0.59381$ | $-0.29064$ |
    | 3.0 | $-0.55908$ | 1.095 | $-0.56445$ | $-0.57755$ | $-0.36756$ |
    | 4.0 | $-0.53687$ | 1.028 | $-0.53733$ | $-0.54606$ | $-0.44489$ |
    | 6.0 | $-0.50907$ | 0.995 | $-0.50908$ | $-0.51194$ | $-0.49002$ |

    | Function | $R_e/a_0$ | $E(R_e)$ | $D_e$ (eV) |
    |---|---|---|---|
    | LCAO, $\zeta = 1$ | 2.493 | $-0.56483$ | 1.76 |
    | LCAO, $\zeta = 1.238$ | 2.003 | $-0.58651$ | 2.35 |
    | Basis-set limit | 2.00 | $-0.60262$ | 2.79 |

    Every variational energy lies above the basis-set curve at every $R$, as it must. The remaining error of the scaled function comes from polarization: near one proton the electron cloud is pulled toward the other, which a spherical function cannot describe. At $R = 6\,a_0$ the optimal exponent dips slightly below 1, and the LCAO curve is too shallow there because it lacks the same polarization.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 8.3, Eqs. (8.36)-(8.53), Figs. 8.5-8.7 (described); Problems 8.9-8.11. Page numbers are not given because the PDF used is an e-book rendering without print pagination. Griffiths reports an equilibrium separation of about 2.4 Bohr radii (1.3 Å) and a binding energy of 1.8 eV, and quotes 1.06 Å and 2.8 eV as the measured values.

Sakurai has no section on H₂⁺, so the note rests on Griffiths.

The scaled-exponent matrix elements, the tables, the virial check and the statement that $E_-$ exceeds $-\tfrac12$ on a grid of 400 separations between 0.3 and 20 $a_0$ are computed in `griffiths/ch08_variational.py`. The reference curve is a PySCF one-electron calculation in aug-cc-pV5Z.

Companion reading in Levine, *Quantum Chemistry* (7th ed., Pearson, 2014): Sec. 13.5, pp. 357-365 (approximate treatments of the H₂⁺ ground electronic state); the exact solution is in [[hydrogen-molecule-ion-exact]].
