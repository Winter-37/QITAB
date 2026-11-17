---
id: hydrogen-fine-structure
title: The fine structure of hydrogen
summary: The order α⁴mc² corrections to the Bohr levels. The relativistic kinetic-energy correction and the spin-orbit coupling are each evaluated in first-order perturbation theory and add up to a formula that depends only on n and j, E_fs = (E_n²/2mc²)(3 − 4n/(j + ½)). Covers the choice of good states, the expectation values of 1/r, 1/r² and 1/r³, the Darwin term that rescues l = 0, a comparison with the exact Dirac levels, and the numbers for n = 1 and 2.
status: in-progress
kind: derivation
level: intermediate
tags: [fine-structure, hydrogen-atom, spin-orbit-coupling, relativistic-correction, darwin-term, fine-structure-constant, total-angular-momentum, dirac-equation, griffiths, sakurai]
prerequisites: [degenerate-perturbation-theory, hydrogen-atom, spin-one-half, addition-of-angular-momenta]
related: [zeeman-effect, hyperfine-splitting-hydrogen, stark-effect, periodic-table-and-term-symbols, hellmann-feynman-and-virial-theorems]
order: 15
date: 2026-11-14
---

## Hierarchy of corrections

The Bohr Hamiltonian $H^0 = p^2/2m - e^2/(4\pi\varepsilon_0 r)$ gives $E_n = -\tfrac12\alpha^2mc^2/n^2$, where

$$
\alpha = \frac{e^2}{4\pi\varepsilon_0\hbar c} \approx \frac{1}{137.036}
$$

is the fine-structure constant. Everything left out of $H^0$ is smaller by powers of $\alpha$ or of $m/m_p$.

| Effect | Order | Size for $n = 2$ |
|---|---|---|
| Bohr energies | $\alpha^2mc^2$ | 3.4 eV |
| Fine structure | $\alpha^4mc^2$ | $10^{-5}$ to $10^{-4}$ eV |
| Lamb shift | $\alpha^5mc^2$ | $10^{-6}$ eV |
| Hyperfine splitting | $(m/m_p)\,\alpha^4mc^2$ | $10^{-7}$ eV |

Fine structure has two parts of the same order: a relativistic correction to the kinetic energy and the spin-orbit coupling. SI units are used throughout, $a$ is the Bohr radius, and $E_n$ is the Bohr energy.

## The relativistic correction

The relativistic kinetic energy is

$$
T = \sqrt{p^2c^2 + m^2c^4} - mc^2 = \frac{p^2}{2m} - \frac{p^4}{8m^3c^2} + \dots ,
$$

so the lowest-order correction to the Hamiltonian is

$$
H'_r = -\frac{p^4}{8m^3c^2} .
$$

$H'_r$ is spherically symmetric. It commutes with $L^2$ and $L_z$, the states $\psi_{nlm}$ of a given $n$ have distinct $(l,m)$, and by the theorem of [[degenerate-perturbation-theory]] they are good states. First-order nondegenerate theory applies:

$$
E^1_r = -\frac{1}{8m^3c^2}\,\langle p^2\psi|p^2\psi\rangle .
$$

The unperturbed Schrödinger equation gives $p^2\psi = 2m(E_n - V)\psi$, hence

$$
E^1_r = -\frac{1}{2mc^2}\Big[E_n^2 + 2E_n\frac{e^2}{4\pi\varepsilon_0}\Big\langle\frac1r\Big\rangle + \Big(\frac{e^2}{4\pi\varepsilon_0}\Big)^2\Big\langle\frac1{r^2}\Big\rangle\Big] .
$$

The hydrogen expectation values are

$$
\Big\langle\frac1r\Big\rangle = \frac{1}{n^2a},\qquad
\Big\langle\frac1{r^2}\Big\rangle = \frac{1}{(l+\tfrac12)\,n^3a^2},\qquad
\Big\langle\frac1{r^3}\Big\rangle = \frac{1}{l(l+\tfrac12)(l+1)\,n^3a^3}\quad(l>0) .
$$

The first follows from the virial theorem and the second from the Hellmann-Feynman theorem applied to $l$ ([[hellmann-feynman-and-virial-theorems]]). With $e^2/(4\pi\varepsilon_0 a) = -2n^2E_n$,

$$
\boxed{\,E^1_r = -\frac{E_n^2}{2mc^2}\Big[\frac{4n}{l+\tfrac12} - 3\Big]\,}
$$

The bracket is positive for every allowed $l$, so the correction always lowers the energy. It depends on $l$: the accidental degeneracy of the Coulomb problem is broken.

## Spin-orbit coupling

In the electron's rest frame the proton circles around it and produces a magnetic field proportional to the electron's orbital angular momentum,

$$
\mathbf B = \frac{1}{4\pi\varepsilon_0}\,\frac{e}{mc^2r^3}\,\mathbf L .
$$

The electron's magnetic moment $\boldsymbol\mu_s = -(e/m)\mathbf S$ has energy $-\boldsymbol\mu_s\cdot\mathbf B$ in this field. The electron frame is not inertial, and the kinematic correction (Thomas precession) multiplies the result by $\tfrac12$:

$$
H'_{so} = \frac{e^2}{8\pi\varepsilon_0}\,\frac{1}{m^2c^2r^3}\;\mathbf S\cdot\mathbf L .
$$

The factor $\tfrac12$ comes out automatically from the Dirac equation; the classical argument is a mnemonic.

**Good states.** $H'_{so}$ does not commute with $\mathbf L$ or $\mathbf S$ separately, so $m_l$ and $m_s$ are not good quantum numbers. It does commute with $L^2$, $S^2$ and the total $\mathbf J = \mathbf L + \mathbf S$. The good states are therefore $|n\,l\,j\,m_j\rangle$ with $j = l\pm\tfrac12$ ([[addition-of-angular-momenta]]). From $J^2 = L^2 + S^2 + 2\mathbf L\cdot\mathbf S$,

$$
\mathbf L\cdot\mathbf S = \tfrac12(J^2 - L^2 - S^2)
\;\longrightarrow\;
\frac{\hbar^2}{2}\Big[j(j+1) - l(l+1) - \tfrac34\Big] ,
$$

which equals $\tfrac12 l\hbar^2$ for $j = l+\tfrac12$ and $-\tfrac12(l+1)\hbar^2$ for $j = l-\tfrac12$. With $\langle1/r^3\rangle$ from above,

$$
\boxed{\,E^1_{so} = \frac{E_n^2}{mc^2}\;\frac{n\,[\,j(j+1) - l(l+1) - \tfrac34\,]}{l(l+\tfrac12)(l+1)}\,}\qquad(l>0) .
$$

The relativistic correction is also diagonal in this basis, because it commutes with $\mathbf J$ and does not involve spin.

## The fine-structure formula

Add the two results. For $j = l+\tfrac12$ the spin-orbit bracket is $l$, and

$$
E^1_{fs} = \frac{E_n^2}{2mc^2}\Big[3 - \frac{4n}{l+\tfrac12} + \frac{2n}{(l+\tfrac12)(l+1)}\Big]
= \frac{E_n^2}{2mc^2}\Big[3 - \frac{4n}{l+1}\Big] .
$$

For $j = l-\tfrac12$ the bracket is $-(l+1)$ and the same algebra gives $3 - 4n/l$. Both cases are

$$
\boxed{\,E^1_{fs} = \frac{E_n^2}{2mc^2}\Big(3 - \frac{4n}{j+\tfrac12}\Big)\,}
\qquad
E_{nj} = -\frac{13.6\ \text{eV}}{n^2}\Big[1 + \frac{\alpha^2}{n^2}\Big(\frac{n}{j+\tfrac12} - \frac34\Big)\Big] .
$$

- The correction depends on $n$ and $j$ only. States of the same $j$ and different $l$, such as $2s_{1/2}$ and $2p_{1/2}$, remain degenerate. That degeneracy survives in the exact Dirac theory and is lifted only by the Lamb shift, a quantum-electrodynamic effect outside this treatment.
- Each $n$ splits into $n$ sublevels, $j = \tfrac12,\dots,n-\tfrac12$.
- The good quantum numbers are $n$, $l$, $s$, $j$, $m_j$.

**The case l = 0.** The spin-orbit formula is $0/0$ at $l = 0$, where $\mathbf L\cdot\mathbf S$ vanishes but $\langle1/r^3\rangle$ diverges. The Dirac equation supplies a third term of the same order, the Darwin term,

$$
H'_D = \frac{\pi\hbar^2}{2m^2c^2}\,\frac{e^2}{4\pi\varepsilon_0}\,\delta^3(\mathbf r) ,
\qquad
E^1_D = \frac{E_n^2}{mc^2}\,2n\quad(l = 0\ \text{only}),
$$

using $|\psi_{n00}(0)|^2 = 1/(\pi n^3a^3)$. Adding it to $E^1_r$ at $l = 0$ gives $(E_n^2/2mc^2)(3 - 4n)$, which is the boxed formula with $j = \tfrac12$. The fine-structure formula is therefore right for all $l$, although the spin-orbit derivation alone does not justify it at $l = 0$. The Darwin term is a standard result that neither book derives; Sakurai points to it and Griffiths notes that the formula happens to hold.

## Comparison with the Dirac levels

The Dirac equation for the Coulomb potential has the exact levels (standard result, used here as a check)

$$
E_{nj} = mc^2\Bigg\{\Bigg[1 + \Bigg(\frac{\alpha}{n - (j+\tfrac12) + \sqrt{(j+\tfrac12)^2 - \alpha^2}}\Bigg)^2\Bigg]^{-1/2} - 1\Bigg\} .
$$

Expanding to order $\alpha^4$ reproduces $E_n + E^1_{fs}$.

!!! example "Numbers for n = 1 and n = 2"

    With CODATA values, $E_1 = -13.605693$ eV (infinite nuclear mass) and $E_n^2/2mc^2 = \alpha^2|E_n|/(4n^2)$.

    | State | $E^1_r$ (eV) | $E^1_{so}$ or $E^1_D$ (eV) | $E^1_{fs}$ (eV) | Dirac minus Bohr (eV) |
    |---|---|---|---|---|
    | $1s_{1/2}$ | $-9.0565\times10^{-4}$ | $+7.2452\times10^{-4}$ (Darwin) | $-1.8113\times10^{-4}$ | $-1.8114\times10^{-4}$ |
    | $2s_{1/2}$ | $-1.4717\times10^{-4}$ | $+9.0565\times10^{-5}$ (Darwin) | $-5.6603\times10^{-5}$ | $-5.6605\times10^{-5}$ |
    | $2p_{1/2}$ | $-2.6415\times10^{-5}$ | $-3.0188\times10^{-5}$ | $-5.6603\times10^{-5}$ | $-5.6605\times10^{-5}$ |
    | $2p_{3/2}$ | $-2.6415\times10^{-5}$ | $+1.5094\times10^{-5}$ | $-1.1321\times10^{-5}$ | $-1.1321\times10^{-5}$ |

    The $n = 2$ splitting is

    $$
    E(2p_{3/2}) - E(2p_{1/2}) = \frac{\alpha^4mc^2}{32} = 4.528\times10^{-5}\ \text{eV} = 10.95\ \text{GHz} .
    $$

    First-order perturbation theory agrees with the Dirac levels to the digits shown; the difference is of order $\alpha^6mc^2$.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 7.3, Eqs. (7.43)-(7.69), Table 7.1, Fig. 7.8 (described); Problems 7.15-7.23, and 7.42-7.43 for the expectation values. Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 5.3, Eqs. (5.95)-(5.125), pp. 305-311, including the remark on the Darwin term.

The Darwin term and the Dirac energy formula are standard results quoted from memory, not from either book; both were checked numerically against the fine-structure formula. Expectation values (SymPy, $n\le3$), the table and the splitting are computed in `griffiths/ch07_perturbation.py` (section B) with SciPy CODATA constants.
