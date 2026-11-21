---
id: degenerate-perturbation-theory
title: Degenerate perturbation theory
summary: Why the nondegenerate formulas fail when unperturbed levels coincide, and the cure. The first-order energies are the eigenvalues of the perturbation restricted to the degenerate subspace, and the eigenvectors are the "good" zeroth-order states. Covers the two-fold case in closed form, the n-fold secular equation, the commuting-operator theorem that finds the good states without diagonalizing, second order inside a split level, and near-degeneracy. Worked on the two-dimensional oscillator with an xy coupling, where the exact answer is known.
status: in-progress
kind: derivation
level: intermediate
tags: [perturbation-theory, degeneracy, secular-equation, good-states, symmetry, near-degeneracy, griffiths, sakurai]
prerequisites: [rayleigh-schrodinger-perturbation-theory, matrix-eigenvalue-problem]
related: [symmetry-conservation-and-degeneracy, stark-effect, hydrogen-fine-structure, zeeman-effect, linear-variation-method, helium-excited-states-perturbation]
order: 12
date: 2026-11-14
---

## The problem

Split the Hamiltonian as $H = H^0 + \lambda H'$ and let $H^0\psi^0_n = E^0_n\psi^0_n$. Nondegenerate Rayleigh-Schrödinger theory ([[rayleigh-schrodinger-perturbation-theory]]) gives

$$
E^1_n = \langle\psi^0_n|H'|\psi^0_n\rangle ,\qquad
E^2_n = \sum_{m\neq n}\frac{|\langle\psi^0_m|H'|\psi^0_n\rangle|^2}{E^0_n - E^0_m} .
$$

Suppose two orthonormal states $\psi^0_a$, $\psi^0_b$ share the energy $E^0$. Two things go wrong.

1. The denominator $E^0_a - E^0_b$ vanishes, so $E^2$ and the first-order wave function diverge unless $\langle\psi^0_a|H'|\psi^0_b\rangle = 0$.
2. $E^1$ is ambiguous. Any combination $\alpha\psi^0_a + \beta\psi^0_b$ is an equally valid unperturbed state, and $\langle H'\rangle$ depends on $\alpha$ and $\beta$.

Both have the same origin. As $\lambda\to0$ each exact eigenstate tends to one definite combination inside the degenerate subspace. Those limits are the **good states**. Perturbation theory is an expansion around them, and they are not known in advance.

## Two-fold degeneracy

Write the zeroth-order state as $\psi^0 = \alpha\psi^0_a + \beta\psi^0_b$ and expand $\psi = \psi^0 + \lambda\psi^1 + \dots$, $E = E^0 + \lambda E^1 + \dots$. The order-$\lambda$ equation is

$$
H^0\psi^1 + H'\psi^0 = E^0\psi^1 + E^1\psi^0 .
$$

Take the inner product with $\psi^0_a$. Because $H^0$ is Hermitian, $\langle\psi^0_a|H^0\psi^1\rangle = E^0\langle\psi^0_a|\psi^1\rangle$ and the terms in $\psi^1$ cancel. The same happens with $\psi^0_b$. What remains is a $2\times2$ eigenvalue problem,

$$
\begin{pmatrix} W_{aa} & W_{ab}\\ W_{ba} & W_{bb}\end{pmatrix}
\begin{pmatrix}\alpha\\ \beta\end{pmatrix}
= E^1\begin{pmatrix}\alpha\\ \beta\end{pmatrix},
\qquad W_{ij} = \langle\psi^0_i|H'|\psi^0_j\rangle ,
$$

with roots

$$
E^1_\pm = \tfrac12\Big[W_{aa} + W_{bb} \pm \sqrt{(W_{aa} - W_{bb})^2 + 4|W_{ab}|^2}\Big] .
$$

The first-order energies are the eigenvalues of $H'$ restricted to the degenerate subspace, and the eigenvectors $(\alpha,\beta)$ are the good states. If $W_{ab} = 0$ the starting states were already good and $E^1 = W_{aa}$, $W_{bb}$, the nondegenerate formula.

## n-fold degeneracy

Nothing changes for a level of degeneracy $g$. Collect any orthonormal basis $\{\psi^0_i\}$ of the level, build the $g\times g$ Hermitian matrix $W_{ij} = \langle\psi^0_i|H'|\psi^0_j\rangle$, and solve

$$
\det(\mathbf W - E^1\mathbf 1) = 0 .
$$

The $g$ roots are the first-order corrections, and the eigenvectors are the good states. This is the linear variation method ([[linear-variation-method]]) carried out in the degenerate subspace alone. The trace is invariant, so the mean shift of the level is $\mathrm{tr}\,\mathbf W/g$ in every basis.

Sakurai writes the same result with the projector $P_0$ onto the degenerate subspace: the zeroth-order kets diagonalize $P_0H'P_0$, and its eigenvalues are the first-order shifts.

## Finding the good states by symmetry

Diagonalizing $\mathbf W$ can often be avoided.

**Theorem.** Let $A$ be a Hermitian operator with $[A,H^0] = [A,H'] = 0$. If $\psi^0_a$ and $\psi^0_b$ are eigenfunctions of $A$ with different eigenvalues $\mu\neq\nu$, then $W_{ab} = 0$, so they are good states.

**Proof.** $[A,H'] = 0$ gives

$$
0 = \langle\psi^0_a|[A,H']|\psi^0_b\rangle = (\mu - \nu)\,W_{ab} ,
$$

and $\mu\neq\nu$ forces $W_{ab} = 0$.

In practice: find an operator that commutes with the full Hamiltonian, label the degenerate states by its eigenvalues, and use the nondegenerate first-order formula. The fine structure of hydrogen is the standard case. $H'$ commutes with $J^2$ and $J_z$ but not with $L_z$ and $S_z$, so the good states are $|n\,l\,j\,m_j\rangle$ ([[hydrogen-fine-structure]]). If $A$ does not separate all the states, diagonalize $\mathbf W$ inside each block of equal eigenvalue.

## Beyond first order

With the good states $\psi^0_k$ as the basis, the first-order wave function has two parts,

$$
\psi^1_k = \sum_{m\notin D}\frac{\langle\psi^0_m|H'|\psi^0_k\rangle}{E^0 - E^0_m}\,\psi^0_m
\;+\;\sum_{\substack{l\in D\\ l\neq k}} c_{lk}\,\psi^0_l ,
$$

where $D$ is the degenerate level. The second-order energy needs only the first part:

$$
E^2_k = \sum_{m\notin D}\frac{|\langle\psi^0_m|H'|\psi^0_k\rangle|^2}{E^0 - E^0_m} .
$$

The sum runs over states outside $D$, so no denominator vanishes. The coefficients $c_{lk}$ follow from the order-$\lambda^2$ equation and carry the denominator $E^1_k - E^1_l$. Two cases need care.

- **Degeneracy not lifted at first order.** If two roots of $\mathbf W$ coincide, the good states inside that pair are still undetermined. They diagonalize the second-order effective operator $\sum_{m\notin D} H'|\psi^0_m\rangle\langle\psi^0_m|H'/(E^0 - E^0_m)$ restricted to the pair.
- **Near-degeneracy.** If two levels are separated by $\Delta$ with $|W_{ab}|\gtrsim\Delta$, the series converges slowly or not at all. Treat the pair exactly: diagonalize $H^0 + H'$ in the two-state space and handle the remaining states perturbatively. The two-state formula is in [[rayleigh-schrodinger-perturbation-theory]]. The same situation appears in electronic-structure theory as an intruder state.

## Worked example: two-dimensional oscillator with an xy coupling

!!! example "Exact, first order and second order compared"

    Take $H^0 = \dfrac{p_x^2 + p_y^2}{2m} + \tfrac12 m\omega^2(x^2 + y^2)$ and $H' = \epsilon\,m\omega^2xy$.

    **Unperturbed level.** The first excited level $E^0 = 2\hbar\omega$ is doubly degenerate, with $\psi^0_a = \psi_1(x)\psi_0(y)$ and $\psi^0_b = \psi_0(x)\psi_1(y)$.

    **The matrix.** $\langle\psi_1|x|\psi_0\rangle = \sqrt{\hbar/2m\omega}$ and $\langle\psi_n|x|\psi_n\rangle = 0$ give $W_{aa} = W_{bb} = 0$ and $W_{ab} = \epsilon\hbar\omega/2$. Therefore

    $$
    E^1_\pm = \pm\tfrac12\epsilon\hbar\omega ,\qquad \psi^0_\pm = \tfrac{1}{\sqrt2}\,(\psi^0_a \pm \psi^0_b) .
    $$

    **By symmetry.** The exchange operator $x\leftrightarrow y$ commutes with $H^0$ and $H'$. Its eigenfunctions in the level are $\psi^0_\pm$ with eigenvalues $\pm1$, so the theorem gives the good states with no diagonalization.

    **Exact solution.** In the rotated coordinates $x_\pm = (x\pm y)/\sqrt2$ the Hamiltonian is two independent oscillators with frequencies $\omega\sqrt{1\pm\epsilon}$:

    $$
    E_{n_+n_-} = \hbar\omega\Big[\sqrt{1+\epsilon}\,(n_+ + \tfrac12) + \sqrt{1-\epsilon}\,(n_- + \tfrac12)\Big] .
    $$

    Expanding the pair $(n_+,n_-) = (1,0),(0,1)$ gives $E = \hbar\omega\,[\,2 \pm \tfrac12\epsilon - \tfrac14\epsilon^2 \pm \tfrac1{16}\epsilon^3 + \dots]$. The ground state is nondegenerate with $E = \hbar\omega\,[\,1 - \tfrac18\epsilon^2 + \dots]$.

    | $\epsilon$ | exact lower | exact upper | first order | through second order |
    |---|---|---|---|---|
    | 0.01 | 1.994975 | 2.004975 | 1.995000, 2.005000 | 1.994975, 2.004975 |
    | 0.1 | 1.947429 | 2.047555 | 1.950000, 2.050000 | 1.947500, 2.047500 |
    | 0.3 | 1.825078 | 2.128593 | 1.850000, 2.150000 | 1.827500, 2.127500 |

    Energies in units of $\hbar\omega$. The exact column was also obtained by diagonalizing $H$ in a product basis of 40 oscillator functions per coordinate; the two agree to all digits shown.

!!! example "A degeneracy that is only partly lifted"

    Put a delta-function bump $H' = a^3V_0\,\delta(x - \tfrac a4)\,\delta(y - \tfrac a2)\,\delta(z - \tfrac{3a}4)$ in the infinite cubical well of side $a$. The first excited level is triply degenerate, $(n_x,n_y,n_z) = (1,1,2),(1,2,1),(2,1,1)$. Since $W_{ij} = a^3V_0\,\psi_i(\mathbf r_0)\psi_j(\mathbf r_0)$ has rank one, its eigenvalues are $8V_0$, $0$, $0$: one state moves and a two-fold degeneracy survives. The ground state shifts by $2V_0$. Computed here; the setup is Griffiths' Problem 7.11.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 7.2, Eqs. (7.16)-(7.42), Examples 7.2-7.4, Problems 7.10 and 7.11. Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 5.2, pp. 300-305, for the projector formulation and the second-order statement.

The second- and third-order coefficients of the oscillator example, the table and the cubical-well eigenvalues are computed in `griffiths/ch07_perturbation.py` (sections A and A2), not quoted from either book.

Companion reading in Levine, *Quantum Chemistry* (7th ed., Pearson, 2014): Secs. 9.5-9.6, pp. 245-250 (perturbation theory for a degenerate level; simplification of the secular equation); worked case in [[helium-excited-states-perturbation]].
