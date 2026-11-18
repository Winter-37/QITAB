---
id: numerov-method
title: The Numerov method for one-dimensional bound states
summary: Shooting solution of ψ'' = G(x)ψ with the three-point Numerov recursion (local error O(s⁶), eigenvalue error O(s⁴)), node counting to bracket each level, and dimensionless variables. Checked on the harmonic oscillator, the hydrogen radial equation, and Levine's Morse-potential model of H₂, whose six lowest levels (2169.96 … 20388.94 cm⁻¹) and ⟨R⟩ values it reproduces.
status: in-progress
kind: algorithm
level: intermediate
tags: [numerov, numerical-methods, shooting-method, vibrational-levels, morse-potential, radial-equation]
prerequisites: [stationary-states, harmonic-oscillator-analytic-solution]
related: [diatomic-vibration-and-anharmonicity, rigid-rotor-and-rovibrational-levels, hydrogen-atom, wkb-connection-formulas-and-quantization, energy-and-unit-conversions]
order: 30
date: 2026-11-17
---

## The problem

Most potentials of interest - a computed diatomic curve $U(R)$, a torsional profile, an anharmonic well - give a one-dimensional Schrödinger equation without a closed-form solution. The Numerov method turns it into a recursion on a grid and finds the bound-state energies by shooting. It is the standard tool for the nuclear-motion step of the diatomic problem ([[diatomic-vibration-and-anharmonicity]]).

## The recursion

Write the one-particle equation $-\frac{\hbar^2}{2m}\psi'' + V\psi = E\psi$ as

$$
\psi'' = G(x)\,\psi,\qquad G(x) = \frac{2m}{\hbar^2}\big[V(x) - E\big] .
$$

On a uniform grid $x_n = x_0 + ns$ write $\psi_n = \psi(x_n)$, $G_n = G(x_n)$. Adding the Taylor series of $\psi(x_n\pm s)$ cancels odd powers:

$$
\psi_{n+1} + \psi_{n-1} = 2\psi_n + s^2\psi_n'' + \frac{s^4}{12}\psi_n^{(4)} + O(s^6).
$$

The fourth derivative is eliminated with the differential equation itself, $\psi^{(4)} = (G\psi)''$, approximated by the central difference $[(G\psi)_{n+1} - 2(G\psi)_n + (G\psi)_{n-1}]/s^2$. Collecting terms gives the **Numerov formula**

$$
\psi_{n+1} = \frac{2\psi_n - \psi_{n-1} + \tfrac{5}{6}s^2G_n\psi_n + \tfrac{1}{12}s^2G_{n-1}\psi_{n-1}}{1 - \tfrac{1}{12}s^2G_{n+1}} ,
$$

which is exact through $s^5$ in each step (local error $O(s^6)$). Over the $\sim1/s$ steps of a calculation the eigenvalue error is $O(s^4)$: halving the step reduces it about sixteenfold (checked below). A plain three-point finite difference, by comparison, is $O(s^2)$.

## Shooting with node counting

1. Choose a range $[x_0, x_{\max}]$ that extends well into the classically forbidden region on both sides of the energies wanted.
2. Set $\psi_0 = 0$ and $\psi_1$ to a small number (its value only fixes the normalization).
3. For a trial energy $E$, run the recursion to $x_{\max}$.
4. If $E$ is not an eigenvalue, $\psi$ grows exponentially in the right-hand forbidden region and $\psi(x_{\max})$ is large. Its **sign changes as $E$ passes an eigenvalue**, and the number of interior nodes of the trial $\psi$ equals the number of eigenvalues below $E$. Bracket each level by the node count or the sign change, then refine by bisection or Brent's method.
5. Normalize $\psi$ numerically.

**Dimensionless variables.** Define $E_r = E/A$ and $x_r = x/B$ with $A$ and $B$ built from the constants of the problem so that $AB^2 = \hbar^2/m$. The equation becomes $\psi_r'' = 2(V_r - E_r)\psi_r$, and the size of the guesses and of the step is set by numbers of order one. For the oscillator $A = h\nu$ and $B = (\hbar/m\omega)^{1/2}$; for a Morse potential $U = D_e[1 - e^{-a(R-R_e)}]^2$ one takes $A = \hbar^2a^2/m = (h\nu_e)^2/2D_e$ and $B = 1/a$.

**Radial problems.** For $V(r)$ in three dimensions, write $\psi = r^{-1}F(r)Y_\ell^m$. Then $F$ obeys a one-dimensional equation with the effective potential $V + \ell(\ell+1)\hbar^2/2mr^2$ and the boundary condition $F(0) = 0$, so the same recursion applies on $(0, r_{\max}]$ ([[hydrogen-atom]]). With $\ell = J$ and $V = U(R)$ this is the rotating diatomic ([[rigid-rotor-and-rovibrational-levels]]).

## Worked examples

!!! example "Convergence on the harmonic oscillator"
    $V_r = x_r^2/2$ on $[-5, 5]$, exact $E_r = v + \tfrac12$.

    | $v$ | error, $s = 0.1$ | error, $s = 0.05$ | ratio |
    |---:|---:|---:|---:|
    | 0 | $3.9\times10^{-7}$ | $2.4\times10^{-8}$ | 16.1 |
    | 1 | $2.7\times10^{-6}$ | $1.7\times10^{-7}$ | 16.4 |
    | 2 | $9.7\times10^{-6}$ | $5.3\times10^{-7}$ | 18.4 |

    The ratio near 16 confirms the $O(s^4)$ eigenvalue error. For $v = 3$ the ratio is distorted (74) because the finite interval, not the step, starts to limit the accuracy.

!!! example "Morse model of H₂ (Levine Sec. 13.2)"
    With $D_e/hc = 38\,297$ cm$^{-1}$ and $\nu_e/c = 4403.2$ cm$^{-1}$: $A = 253.129\,hc$ cm$^{-1}$, $B = 0.514\,12$ Å, $D_{e,r} = 151.294$. The grid runs from $x_r = -1.44$ ($R = 0$) to $2.8$ with $s = 0.02$.

    | $v$ | Numerov $E_{\text{vib}}/hc$ (cm$^{-1}$) | exact Morse | harmonic | $\langle R\rangle$ (Å) |
    |---:|---:|---:|---:|---:|
    | 0 | 2169.96 | 2169.96 | 2201.6 | 0.764 |
    | 1 | 6320.02 | 6320.03 | 6604.8 | 0.811 |
    | 2 | 10216.96 | 10216.97 | 11008.0 | 0.862 |
    | 3 | 13860.75 | 13860.78 | 15411.2 | 0.918 |
    | 4 | 17251.41 | 17251.47 | 19814.4 | 0.978 |
    | 5 | 20388.94 | 20389.02 | 24217.6 | 1.043 |

    The reduced energies agree with Levine's spreadsheet values to $10^{-4}$ and the exact Morse levels to 0.1 cm$^{-1}$. A three-point finite-difference diagonalization on the same grid is off by up to 32 cm$^{-1}$. The growth of $\langle R\rangle$ with $v$ is the anharmonic lengthening of the bond.

!!! example "Hydrogen radial equation"
    $V_{\text{eff}} = \ell(\ell+1)/2r^2 - 1/r$ (atomic units) on $(0, 60]$, $s = 0.01$. For $\ell = 0$ the three lowest roots are $-0.499\,965$, $-0.124\,996$, $-0.055\,554$ against $-1/2n^2$; for $\ell = 1$ the error is $10^{-6}$. The $\ell = 0$ error is larger because $F\sim r$ and the Coulomb singularity make the first few steps less accurate.

## Limitations

- Only one dimension (or a separable radial coordinate). Coupled coordinates need basis-set or grid (DVR) methods.
- The interval must be wide enough: a too-short range raises the energies of the upper levels.
- Levels near a dissociation limit have long tails and need large $x_{\max}$; above the limit there are no bound states to find.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 4.4, pp. 74 ff., Eqs. (4.65)-(4.82) (Numerov formula, node counting, dimensionless variables); Sec. 6.9, pp. 149-154 (radial equation); Sec. 13.2, pp. 347-352, Example (Morse H₂: $A$, $B$, $D_{e,r}$, reduced energies, levels and $\langle R\rangle$). Numbers recomputed in `part3_batchA.py`, section A.
