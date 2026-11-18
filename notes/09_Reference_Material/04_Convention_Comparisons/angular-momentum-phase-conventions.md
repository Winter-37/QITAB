---
id: angular-momentum-phase-conventions
title: Angular-momentum phase conventions
summary: The phase choices that make angular-momentum formulas from different sources compatible - the Condon–Shortley sign in Y_ℓ^m (Griffiths puts it in P_ℓ^m, Sakurai in Y, both give the same functions as SciPy and SymPy), real solid harmonics and PySCF's ordering, positive J_± matrix elements and the Clebsch–Gordan sign rule, the symmetry under j₁↔j₂, the active rotation e^{-iJ_yβ} behind Wigner's d matrices, and the time-reversal phase.
status: in-progress
kind: comparison
level: intermediate
tags: [angular-momentum, spherical-harmonics, condon-shortley, clebsch-gordan, wigner-d, conventions, comparison]
prerequisites: [orbital-angular-momentum, addition-of-angular-momenta]
related: [central-potentials-and-spherical-harmonics, solid-harmonics-angular-basis, wigner-rotation-matrices, time-reversal-and-antiunitary-operators, spin-one-half]
order: 30
date: 2026-11-17
---

Angular-momentum eigenstates are defined only up to a phase for each $|j,m\rangle$. A convention fixes these phases once; every table of Clebsch–Gordan coefficients, every $Y_\ell^m$ and every $d^{(j)}$ matrix then follows. Mixing two conventions gives wrong relative signs, not wrong magnitudes, which is why the errors are easy to miss.

## The standard (Condon–Shortley) choices

1. **Ladder operators have real, non-negative matrix elements:**
$$
\hat J_\pm|j,m\rangle = \hbar\sqrt{(j\mp m)(j\pm m+1)}\,|j,m\pm1\rangle .
$$
2. **Spherical harmonics** carry the factor $(-1)^m$ for $m > 0$, so that, with $\hat L_\pm$ as in rule 1,
$$
Y_\ell^{-m} = (-1)^m\big(Y_\ell^m\big)^*,\qquad Y_\ell^0 = \sqrt{\tfrac{2\ell+1}{4\pi}}\,P_\ell(\cos\theta) .
$$
For example $Y_1^{1} = -\sqrt{3/8\pi}\,\sin\theta\,e^{i\phi}$ and $Y_1^0 = \sqrt{3/4\pi}\,\cos\theta$.
3. **Clebsch–Gordan coefficients** are real, and the overall sign of each coupled multiplet is fixed by
$$
\langle j_1\,j_1;\,j_2\,(j - j_1)\,|\,j\,j\rangle > 0 .
$$

## Where each source puts the sign

| Source | Where the $(-1)^m$ sits | Same $Y_\ell^m$ as SciPy/SymPy? |
|---|---|---|
| Griffiths (3rd ed.) | inside $P_\ell^m(x) = (-1)^m(1-x^2)^{m/2}(\mathrm d/\mathrm dx)^mP_\ell(x)$, Eq. (4.27); $Y_\ell^m$ in Eq. (4.32) | yes |
| Sakurai and Napolitano (3rd ed.) | in the prefactor $(-1)^\ell$ of $Y_\ell^\ell$ and the explicit formula (3.246) for $m\ge0$, with $Y_\ell^{-m} = (-1)^m[Y_\ell^m]^*$, Eq. (3.247) | yes |
| SciPy `special.sph_harm_y(l, m, θ, φ)` | Condon–Shortley phase included | reference |
| SymPy `Ynm(l, m, θ, φ)` | Condon–Shortley phase included | reference |

Both textbook formulas reproduce SciPy's and SymPy's $Y_\ell^m$ for all $\ell\le4$, $-\ell\le m\le\ell$ at three test points, to $4\times10^{-16}$. Sakurai's $(-1)^\ell$ in $Y_\ell^\ell$ is chosen so that lowering to $m = 0$ gives $Y_\ell^0$ with the sign of $P_\ell(\cos\theta)$ (his footnote to Eq. (3.244)). Some older chemistry and spectroscopy texts omit the $(-1)^m$; their $Y_\ell^m$ differ by $(-1)^m$ for $m>0$.

## Clebsch–Gordan coefficients

With rules 1 and 3 (Sakurai Sec. 3.8.3; Griffiths Table 4.8; SymPy `CG`):

| Coefficient | Value |
|---|---|
| $\langle\tfrac12\,\tfrac12;\tfrac12\,{-\tfrac12}\,|\,0\,0\rangle$ | $+1/\sqrt2$ |
| $\langle\tfrac12\,{-\tfrac12};\tfrac12\,\tfrac12\,|\,0\,0\rangle$ | $-1/\sqrt2$ |
| $\langle1\,1;\tfrac12\,{-\tfrac12}\,|\,\tfrac12\,\tfrac12\rangle$ | $+\sqrt{2/3}$ |
| $\langle1\,0;\tfrac12\,\tfrac12\,|\,\tfrac12\,\tfrac12\rangle$ | $-1/\sqrt3$ |

So the singlet is $(|{\uparrow\downarrow}\rangle - |{\downarrow\uparrow}\rangle)/\sqrt2$ with the first particle's $\uparrow$ term positive.

**Order of coupling matters.** Exchanging the two angular momenta changes the sign of some multiplets:

$$
\langle j_2\,m_2;\,j_1\,m_1\,|\,j\,m\rangle = (-1)^{j_1+j_2-j}\,\langle j_1\,m_1;\,j_2\,m_2\,|\,j\,m\rangle .
$$

Coupling $\ell$ to $s$ ($|\ell s;jm\rangle$, Sakurai Eq. (3.377)) and $s$ to $\ell$ give spin-orbitals that differ by $(-1)^{\ell+1/2-j}$. When combining a Clebsch–Gordan table with a formula from another source, check the order.

## Real spherical (solid) harmonics

Quantum-chemistry codes use real combinations ([[solid-harmonics-angular-basis]]):

$$
S_{\ell m}\propto(-1)^m\,\mathrm{Re}\,\mathcal Y_{\ell m},\qquad S_{\ell,-m}\propto(-1)^m\,\mathrm{Im}\,\mathcal Y_{\ell m}\quad(m > 0),
$$

where the $(-1)^m$ removes the Condon–Shortley sign, so that $S_{11}\propto x$ and $S_{1,-1}\propto y$ with positive coefficients. The **order** of the components is code-specific. PySCF lists $\ell = 1$ as $(p_x, p_y, p_z)$ and $\ell\ge2$ by $m = -\ell,\dots,\ell$: for $d$, $(d_{xy}, d_{yz}, d_{z^2}, d_{xz}, d_{x^2-y^2})$. A code that orders $p$ by $m = -1,0,1$ as well gets $(p_y,p_z,p_x)$; MO coefficient matrices from different codes cannot be exchanged without reordering.

## Rotations

Sakurai uses **active** rotations, $\mathcal D(R) = \exp(-i\hat{\mathbf J}\cdot\mathbf n\,\phi/\hbar)$, and Euler angles in the $z$-$y$-$z$ convention, $\mathcal D(\alpha,\beta,\gamma) = e^{-i\hat J_z\alpha/\hbar}e^{-i\hat J_y\beta/\hbar}e^{-i\hat J_z\gamma/\hbar}$, so that $\mathcal D^{(j)}_{m'm} = e^{-i(m'\alpha + m\gamma)}d^{(j)}_{m'm}(\beta)$ ([[wigner-rotation-matrices]]). For spin $\tfrac12$:

$$
d^{(1/2)}(\beta) = e^{-i\sigma_y\beta/2} = \begin{pmatrix}\cos\frac\beta2 & -\sin\frac\beta2\\ \sin\frac\beta2 & \cos\frac\beta2\end{pmatrix},
$$

which is what SymPy's `Rotation.d` returns. Passive (coordinate-frame) rotations replace $\beta$ by $-\beta$; for the real $d$ matrices this is the same as transposing, $d^{(j)}_{m'm}(-\beta) = d^{(j)}_{mm'}(\beta)$.

**Time reversal.** The phase of $\Theta|j,m\rangle$ is a further convention. With the Condon–Shortley $Y_\ell^m$, complex conjugation gives $Y_\ell^{m*} = (-1)^mY_\ell^{-m}$, and for spin $\tfrac12$ a common choice is $\Theta = -i\sigma_yK$; [[time-reversal-and-antiunitary-operators]] gives Sakurai's choice and the freedom in it.

## Checks

`part9_reference.py`, section J: Sakurai's Eqs. (3.246)-(3.247) and Griffiths' Eqs. (4.27), (4.32) implemented symbolically and compared with SymPy `Ynm` and SciPy `sph_harm_y` for $\ell\le4$; the Clebsch–Gordan sign rule for all couplings with $j_1\le2$, $j_2\le\tfrac32$; the table values; the $j_1\leftrightarrow j_2$ rule on four cases; $e^{-i\sigma_y\beta/2}$ against SymPy's `Rotation.d`; and PySCF's spherical AO labels for $p$ and $d$ shells.

## Source

- Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 3.6.2, p. 193, Eqs. (3.243)-(3.248) and footnote 8 ($Y_\ell^m$ phase); Sec. 3.8.3, pp. 214-215, Eqs. (3.377)-(3.378) (overall CG sign "fixed by convention", real and positive for the stretched state); Sec. 3.8 (CG coefficients real by convention).
- Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 4.1.2, Eqs. (4.27)-(4.32), as recorded in [[central-potentials-and-spherical-harmonics]]; Table 4.8 ([[addition-of-angular-momenta]]).
- SciPy 1.18 `scipy.special.sph_harm_y`, SymPy 1.14 `Ynm`, `CG`, `Rotation.d`; PySCF 2.15.1 AO labels. All compared in the script.
