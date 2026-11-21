---
id: zeeman-effect
title: The Zeeman effect in hydrogen
summary: Splitting of the hydrogen levels in a uniform magnetic field, in three regimes set by the ratio of the Zeeman energy to the fine structure. Weak field, where j and m_j are good and the shift is the Landé factor times μ_B B m_j. Strong field (Paschen-Back), where m_l and m_s are good and fine structure is the perturbation. Intermediate field, where the two are diagonalized together; for n = 2 the eight levels have closed forms, checked here against a direct diagonalization.
status: in-progress
kind: derivation
level: intermediate
tags: [zeeman-effect, magnetic-field, lande-g-factor, paschen-back, fine-structure, degenerate-perturbation-theory, bohr-magneton, hydrogen-atom, griffiths, sakurai]
prerequisites: [hydrogen-fine-structure, degenerate-perturbation-theory, addition-of-angular-momenta]
related: [spin-one-half, rotational-selection-rules-and-wigner-eckart, stark-effect, hyperfine-splitting-hydrogen, minimal-coupling-and-aharonov-bohm]
order: 16
date: 2026-11-14
---

## The perturbation and the three regimes

An electron in a uniform external field $\mathbf B_{ext}$ has orbital and spin magnetic moments $\boldsymbol\mu_l = -(e/2m)\mathbf L$ and $\boldsymbol\mu_s = -(e/m)\mathbf S$, so

$$
H'_Z = -(\boldsymbol\mu_l + \boldsymbol\mu_s)\cdot\mathbf B_{ext} = \frac{e}{2m}\,(\mathbf L + 2\mathbf S)\cdot\mathbf B_{ext} .
$$

The factor 2 on the spin is the electron $g$-factor. The term quadratic in the field (diamagnetism, from $\mathbf A^2$ in [[minimal-coupling-and-aharonov-bohm]]) is neglected. Take $\mathbf B_{ext} = B\hat{\mathbf z}$ and write $\beta = \mu_BB$ with the Bohr magneton

$$
\mu_B = \frac{e\hbar}{2m} = 5.788\times10^{-5}\ \text{eV/T} .
$$

$H'_Z$ competes with the fine structure $H'_{fs}$ of [[hydrogen-fine-structure]]. The two do not commute, because $H'_{fs}$ conserves $\mathbf J$ while $H'_Z$ picks out $L_z + 2S_z$. Which one sets the good states depends on their relative size.

| Regime | Condition | Unperturbed problem | Good quantum numbers |
|---|---|---|---|
| Weak field | $\beta\ll$ fine structure | Bohr + fine structure | $n, l, j, m_j$ |
| Strong field | $\beta\gg$ fine structure | Bohr + Zeeman | $n, l, m_l, m_s$ |
| Intermediate | comparable | Bohr only | $n$, and $m_j = m_l + m_s$ |

For $n = 2$ the fine-structure splitting equals $\mu_BB$ at $B = 0.78$ T. $J_z$ commutes with both perturbations, so $m_j$ is good in every regime.

## Weak field

The good states are $|n\,l\,j\,m_j\rangle$ and first-order theory gives

$$
E^1_Z = \frac{e}{2m}\,B\,\langle L_z + 2S_z\rangle = \frac{e}{2m}\,B\,\langle J_z + S_z\rangle .
$$

$\langle J_z\rangle = \hbar m_j$, but $S_z$ is not diagonal in this basis. Its expectation value follows from the projection theorem, a consequence of the Wigner-Eckart theorem ([[rotational-selection-rules-and-wigner-eckart]]): within a level of fixed $j$, every vector operator is proportional to $\mathbf J$,

$$
\langle\mathbf S\rangle = \frac{\langle\mathbf S\cdot\mathbf J\rangle}{\hbar^2j(j+1)}\,\langle\mathbf J\rangle .
$$

The classical picture is that $\mathbf L$ and $\mathbf S$ precess rapidly about $\mathbf J$, so only the component of $\mathbf S$ along $\mathbf J$ survives the average. From $\mathbf L = \mathbf J - \mathbf S$,

$$
\mathbf S\cdot\mathbf J = \tfrac12(J^2 + S^2 - L^2) \;\longrightarrow\; \frac{\hbar^2}{2}\Big[j(j+1) + \tfrac34 - l(l+1)\Big] .
$$

Therefore

$$
\boxed{\,E^1_Z = \mu_B\,g_J\,B\,m_j ,\qquad g_J = 1 + \frac{j(j+1) - l(l+1) + \tfrac34}{2j(j+1)}\,}
$$

$g_J$ is the Landé factor. For one electron it reduces to $g_J = 1\pm1/(2l+1)$ for $j = l\pm\tfrac12$, the form Sakurai gives.

| Level | $s_{1/2}$ | $p_{1/2}$ | $p_{3/2}$ | $d_{3/2}$ | $d_{5/2}$ |
|---|---|---|---|---|---|
| $g_J$ | 2 | 2/3 | 4/3 | 4/5 | 6/5 |

Each level of given $j$ splits into $2j+1$ equally spaced lines. The ground state becomes

$$
E = -13.6\ \text{eV}\,\Big(1 + \frac{\alpha^2}{4}\Big) \pm \mu_BB .
$$

## Strong field: the Paschen-Back effect

Now $H^0 + H'_Z$ is the unperturbed problem. It is diagonal in $|n\,l\,m_l\,m_s\rangle$:

$$
E_{nm_lm_s} = -\frac{13.6\ \text{eV}}{n^2} + \mu_BB\,(m_l + 2m_s) .
$$

Fine structure is treated in first order. In these states $\langle\mathbf S\cdot\mathbf L\rangle = \langle S_xL_x\rangle + \langle S_yL_y\rangle + \langle S_zL_z\rangle = \hbar^2m_lm_s$, because the $x$ and $y$ terms average to zero. The relativistic correction is unchanged. The sum is

$$
E^1_{fs} = \frac{13.6\ \text{eV}}{n^3}\,\alpha^2\,\Big\{\frac{3}{4n} - \Big[\frac{l(l+1) - m_lm_s}{l(l+\tfrac12)(l+1)}\Big]\Big\} ,
$$

with the square bracket replaced by 1 for $l = 0$. States with the same $m_l + 2m_s$ stay degenerate under $H'_Z$ alone, but $H'_{fs}$ has no matrix elements between them within a given $n$ and $l$ (they differ in $m_j$ or the element vanishes), so nondegenerate theory is enough.

## Intermediate field: n = 2

Neither perturbation dominates, so $H' = H'_Z + H'_{fs}$ is diagonalized in the eight-dimensional $n = 2$ level. In the coupled basis $H'_{fs}$ is diagonal and $H'_Z$ connects only states of equal $m_j$ and equal $l$. The matrix falls into four $1\times1$ blocks and two $2\times2$ blocks (the pairs $p_{3/2}$, $p_{1/2}$ with $m_j = \pm\tfrac12$). With

$$
\gamma = \Big(\frac{\alpha}{8}\Big)^2\,13.6\ \text{eV} = 1.132\times10^{-5}\ \text{eV},\qquad \beta = \mu_BB ,
$$

the levels relative to $E_2$ are

| | Energy $-\,E_2$ | Weak-field state | Strong-field state $(l, m_l, m_s)$ |
|---|---|---|---|
| $\epsilon_1$ | $-5\gamma + \beta$ | $2s_{1/2}$, $m_j = \tfrac12$ | $(0, 0, \tfrac12)$ |
| $\epsilon_2$ | $-5\gamma - \beta$ | $2s_{1/2}$, $m_j = -\tfrac12$ | $(0, 0, -\tfrac12)$ |
| $\epsilon_3$ | $-\gamma + 2\beta$ | $2p_{3/2}$, $m_j = \tfrac32$ | $(1, 1, \tfrac12)$ |
| $\epsilon_4$ | $-\gamma - 2\beta$ | $2p_{3/2}$, $m_j = -\tfrac32$ | $(1, -1, -\tfrac12)$ |
| $\epsilon_5$ | $-3\gamma + \tfrac12\beta + \sqrt{4\gamma^2 + \tfrac23\gamma\beta + \tfrac14\beta^2}$ | $2p_{3/2}$, $m_j = \tfrac12$ | $(1, 0, \tfrac12)$ |
| $\epsilon_6$ | $-3\gamma + \tfrac12\beta - \sqrt{4\gamma^2 + \tfrac23\gamma\beta + \tfrac14\beta^2}$ | $2p_{1/2}$, $m_j = \tfrac12$ | $(1, 1, -\tfrac12)$ |
| $\epsilon_7$ | $-3\gamma - \tfrac12\beta + \sqrt{4\gamma^2 - \tfrac23\gamma\beta + \tfrac14\beta^2}$ | $2p_{3/2}$, $m_j = -\tfrac12$ | $(1, -1, \tfrac12)$ |
| $\epsilon_8$ | $-3\gamma - \tfrac12\beta - \sqrt{4\gamma^2 - \tfrac23\gamma\beta + \tfrac14\beta^2}$ | $2p_{1/2}$, $m_j = -\tfrac12$ | $(1, 0, -\tfrac12)$ |

**Limits.** For $\beta\ll\gamma$ the square root in $\epsilon_5$ is $2\gamma + \tfrac16\beta$, so $\epsilon_5\to-\gamma + \tfrac23\beta$ and $\epsilon_6\to-5\gamma + \tfrac13\beta$: the Landé results with $g_J = \tfrac43$ and $\tfrac23$. For $\beta\gg\gamma$ the root is $\tfrac12\beta + \tfrac23\gamma$, so $\epsilon_5\to\beta - \tfrac73\gamma$ and $\epsilon_6\to-\tfrac{11}3\gamma$, the Paschen-Back values for $(1,0,\tfrac12)$ and $(1,1,-\tfrac12)$. The first four levels are linear in $B$ and exact in all regimes, because each is alone in its $(l, m_j)$ block.

!!! example "Exact levels against the two limiting formulas"

    The $8\times8$ problem was built independently in the uncoupled basis, with $H'_{fs}$ written as a linear function of $\mathbf L\cdot\mathbf S$ for $l = 1$, and diagonalized numerically. It reproduces the closed forms above to machine precision at every field tried. The largest error of each limiting formula over the eight levels, in units of $\gamma$:

    | $B$ (T) | $\beta/\gamma$ | weak-field formula | strong-field formula |
    |---|---|---|---|
    | 0.02 | 0.10 | 0.0006 | 1.30 |
    | 0.1 | 0.51 | 0.015 | 1.18 |
    | 1 | 5.1 | 1.52 | 0.78 |
    | 5 | 25.6 | 10.0 | 0.15 |
    | 20 | 102 | 35.5 | 0.035 |

    At 1 T neither limit is usable for the four mixed levels. In units of $\gamma$ the exact values are $-8.226$, $-4.178$, $-2.887$, $3.291$; the weak-field formula gives $-6.704$, $-4.409$, $-3.296$, $2.409$ and the strong-field formula $-7.446$, $-3.667$, $-3.667$, $2.780$.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 7.4, Eqs. (7.70)-(7.88), Table 7.2, Figs. 7.9-7.11 (described); Problems 7.24-7.30. Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 5.3.3, Eqs. (5.126)-(5.146), pp. 311-314, for the weak-field result in the form $1\pm1/(2l+1)$ and the strong-field limit.

The numerical diagonalization, the comparison table and the field at which $\mu_BB$ equals the $n = 2$ splitting are computed in `griffiths/ch07_perturbation.py` (sections C and C2) with SciPy CODATA constants. The assignment of strong-field labels to $\epsilon_5$-$\epsilon_8$ follows from the limits worked out above.

Companion reading in Levine, *Quantum Chemistry* (7th ed., Pearson, 2014): Sec. 6.8, pp. 147-149 (the Zeeman effect).
