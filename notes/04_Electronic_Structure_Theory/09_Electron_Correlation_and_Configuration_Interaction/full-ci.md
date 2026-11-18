---
id: full-ci
title: Full configuration interaction
summary: The full CI wave function as an expansion in all excited determinants, the block structure of the full CI matrix, intermediate normalization, the exact result that the correlation energy depends only on double-excitation coefficients, the coupled hierarchy of CI equations, and the closed-form full CI of minimal-basis H2 including its dissociation limit.
status: in-progress
kind: derivation
level: intermediate
tags: [ci, full-ci, correlation-energy, intermediate-normalization, determinant-space]
prerequisites: [excited-determinants, slater-condon-rules, brillouin-theorem, linear-variation-method]
related: [electron-correlation, cisd, size-consistency, minimal-basis-h2-model, natural-orbitals, ci-in-practice]
conventions: [ia-letters, antisymmetrized-integrals]
order: 30
date: 2026-11-03
---

## The full CI expansion

Start from a closed-shell RHF determinant $|\Psi_0\rangle$ in a basis of $2K$ spin orbitals. The full CI ground state is

$$
|\Phi_0\rangle = c_0|\Psi_0\rangle + \sum_{ia}c_i^a|\Psi_i^a\rangle + \sum_{\substack{i<j\\ a<b}}c_{ij}^{ab}|\Psi_{ij}^{ab}\rangle + \sum_{\substack{i<j<k\\ a<b<c}}c_{ijk}^{abc}|\Psi_{ijk}^{abc}\rangle + \cdots
$$

up to $N$-fold excitations ([[excited-determinants]]).

**Unrestricted sums.** With unrestricted sums the $n$-fold term carries a factor $(1/n!)^2$. The coefficients are then taken antisymmetric in their upper and in their lower indices, so that each determinant is counted once. For example, $\tfrac14\sum_{ijab}c_{ij}^{ab}|\Psi_{ij}^{ab}\rangle$ has four equal terms per distinct double.

**Variational status.** Diagonalizing $\hat H$ in this basis is the [[linear-variation-method]]. The lowest eigenvalue $\mathcal E_0$ is exact within the basis and defines the basis-set correlation energy $\mathcal E_0 - E_0$ ([[electron-correlation]]). Higher roots bound excited states.

**Size of the space.** There are $\binom{N}{n}\binom{2K-N}{n}$ $n$-fold excitations. Restricting to $M_S = 0$, to spin-adapted configurations, and to the right spatial symmetry shrinks the space, but it still grows combinatorially.

## Structure of the full CI matrix

Write $|\Phi_0\rangle = c_0|\Psi_0\rangle + c_S|S\rangle + c_D|D\rangle + c_T|T\rangle + c_Q|Q\rangle + \cdots$ (singles, doubles, ...). The Hamiltonian matrix has the block form (upper triangle shown):

$$
\begin{pmatrix}
\langle\Psi_0|\hat H|\Psi_0\rangle & 0 & \langle\Psi_0|\hat H|D\rangle & 0 & 0 & \cdots\\
& \langle S|\hat H|S\rangle & \langle S|\hat H|D\rangle & \langle S|\hat H|T\rangle & 0 & \cdots\\
& & \langle D|\hat H|D\rangle & \langle D|\hat H|T\rangle & \langle D|\hat H|Q\rangle & \cdots\\
& & & \langle T|\hat H|T\rangle & \langle T|\hat H|Q\rangle & \cdots\\
& & & & \langle Q|\hat H|Q\rangle & \cdots
\end{pmatrix}
$$

**Zeros, and why.**

- $\langle\Psi_0|\hat H|S\rangle = 0$ by [[brillouin-theorem]].
- Blocks between configurations that differ by more than two excitation levels vanish by the [[slater-condon-rules]]: $\langle\Psi_0|\hat H|T\rangle$, $\langle\Psi_0|\hat H|Q\rangle$, $\langle S|\hat H|Q\rangle$, and so on.
- Even the nonzero off-diagonal blocks are sparse. $\langle\Psi_{ij}^{ab}|\hat H|\Psi_{cdef}^{tuvw}\rangle\neq0$ only if $\{i,j\}\subset\{k,l,e,f\}$ and $\{a,b\}\subset\{c,d,v,w\}$.

**Consequences for the ground state.**

- **Doubles dominate.** Only doubles couple directly to $|\Psi_0\rangle$, so for small molecules they give most of the correlation energy.
- **Singles enter indirectly.** They couple through the doubles, so their energy effect is small, but they matter for one-electron properties.
- **Quadruples matter more than triples** for the ground-state energy.
- **Excited states are different.** Singles dominate electronic spectra.

Szabo Table 4.1 collects matrix elements between singlet spin-adapted single and double configurations, all derivable with the Slater-Condon rules and [[spin-orbital-to-spatial-orbital]].

## Intermediate normalization and the correlation energy

When $|\Psi_0\rangle$ is a good zeroth-order description, scale $|\Phi_0\rangle$ so that $c_0 = 1$:

$$
\langle\Psi_0|\Phi_0\rangle = 1 \qquad(\text{intermediate normalization}).
$$

The wave function is then not normalized, but it can be at the end. Write the Schrödinger equation as

$$
(\hat H - E_0)|\Phi_0\rangle = (\mathcal E_0 - E_0)|\Phi_0\rangle = E_{\text{corr}}|\Phi_0\rangle ,
$$

with $E_0 = \langle\Psi_0|\hat H|\Psi_0\rangle$, and project onto $\langle\Psi_0|$. Brillouin's theorem removes the singles, and triples and higher do not couple, so

$$
E_{\text{corr}} = \sum_{\substack{i<j\\ a<b}}c_{ij}^{ab}\,\langle\Psi_0|\hat H|\Psi_{ij}^{ab}\rangle = \sum_{\substack{i<j\\ a<b}}c_{ij}^{ab}\,\langle ij||ab\rangle .
$$

**The exact correlation energy is determined by the double-excitation coefficients alone.** This holds only in intermediate normalization, and with Hartree-Fock orbitals for the reference.

**The equations are still coupled.** Projecting onto $\langle\Psi_i^a|$ (Szabo Ex. 4.1) couples singles, doubles and triples:

$$
\sum_{k,c}c_k^c\langle\Psi_i^a|\hat H - E_0|\Psi_k^c\rangle
+ \sum_{\substack{k<l\\ c<d}}c_{kl}^{cd}\langle\Psi_i^a|\hat H|\Psi_{kl}^{cd}\rangle
+ \sum_{\substack{k<l<e\\ c<d<v}}c_{cde}^{tuv}\langle\Psi_i^a|\hat H|\Psi_{cde}^{tuv}\rangle
= E_{\text{corr}}\,c_i^a .
$$

Projections onto doubles, triples, and so on form a hierarchy that must be solved simultaneously. Truncating it is the subject of [[cisd]].

## Exact solution for minimal-basis H₂

In [[minimal-basis-h2-model]] the symmetry- and spin-adapted expansion is

$$
|\Phi_0\rangle = |\Psi_0\rangle + c\,|\Psi_{1\bar1}^{2\bar2}\rangle .
$$

The singlet single excitation is ungerade and cannot mix. The matrix elements (real orbitals) are

$$
\langle\Psi_0|\hat H|\Psi_0\rangle = 2h_{11} + J_{11} = 2\varepsilon_1 - J_{11},
\qquad
\langle\Psi_0|\hat H|\Psi_{1\bar1}^{2\bar2}\rangle = K_{12},
$$

$$
\langle\Psi_{1\bar1}^{2\bar2}|\hat H|\Psi_{1\bar1}^{2\bar2}\rangle = 2h_{22} + J_{22} = 2\varepsilon_2 - 4J_{12} + J_{22} + 2K_{12}.
$$

**Equations.** Define the excitation energy

$$
2\Delta = \langle\Psi_{1\bar1}^{2\bar2}|\hat H - E_0|\Psi_{1\bar1}^{2\bar2}\rangle = 2(\varepsilon_2 - \varepsilon_1) + J_{11} + J_{22} - 4J_{12} + 2K_{12}.
$$

Projecting onto $\langle\Psi_0|$ and $\langle\Psi_{1\bar1}^{2\bar2}|$ gives

$$
E_{\text{corr}} = cK_{12},
\qquad
K_{12} + 2\Delta\,c = c\,E_{\text{corr}},
\qquad\text{i.e.}\qquad
\begin{pmatrix}0 & K_{12}\\ K_{12} & 2\Delta\end{pmatrix}\begin{pmatrix}1\\ c\end{pmatrix} = E_{\text{corr}}\begin{pmatrix}1\\ c\end{pmatrix}.
$$

**Solution.** Eliminate $c = K_{12}/(E_{\text{corr}} - 2\Delta)$ and take the lower root (Szabo Ex. 4.2):

$$
E_{\text{corr}} = \Delta - \sqrt{\Delta^2 + K_{12}^2}.
$$

!!! example "Numbers (STO-3G, R = 1.4 bohr) and the dissociation limit (Szabo Ex. 4.3)"
    With the integrals of [[minimal-basis-h2-model]]: $\Delta = 0.788645$ and $K_{12} = 0.181258$ hartree, so
    $$
    E_{\text{corr}} = -0.020562\ \text{hartree},
    \qquad
    c = \frac{K_{12}}{E_{\text{corr}} - 2\Delta} = -0.11344 .
    $$
    Normalizing $(1, c)$ gives $(0.99363, -0.11272)$, the full CI vector found before.

    **As $R$ grows,** $\Delta$ shrinks and $c\to-1$:

    | $R$ (bohr) | 1.4 | 2.0 | 3.0 | 5.0 | 10.0 |
    |---|---:|---:|---:|---:|---:|
    | $\Delta$ (hartree) | 0.7886 | 0.4916 | 0.2268 | 0.0424 | 0.0001 |
    | $c$ | −0.113 | −0.196 | −0.425 | −0.864 | −0.9997 |

    **Limit.** At $R\to\infty$, $|\Psi_0\rangle$ and $|\Psi_{1\bar1}^{2\bar2}\rangle$ have equal weight. The normalized full CI wave function becomes $2^{-1/2}(|\phi_1\bar\phi_2\rangle + |\phi_2\bar\phi_1\rangle)$, the Heitler-London singlet. In the limit $\Delta\to0$ and every MO two-electron integral tends to $\tfrac12(\phi_1\phi_1|\phi_1\phi_1)$. So $E_{\text{corr}}\to-K_{12}$, which cancels the spurious ionic repulsion in the RHF energy, and the full CI energy goes to $2E_{\text{H}}$ ([[h2-dissociation-rhf-uhf]]). Computed for this note.

**Perturbative limit (Szabo Ex. 4.13).** If $K_{12}^2\ll\Delta^2$, then $E_{\text{corr}}\approx-K_{12}^2/(2\Delta) = -0.020830$ hartree. This is the second-order perturbation estimate, within 1.3% of the exact value here.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 4.1, pp. 233-242, Eqs. (4.2)-(4.24), Fig. 4.1, Table 4.1, Ex. 4.1-4.3, 4.13. Numbers computed for this note.
