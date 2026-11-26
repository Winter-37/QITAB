---
id: projection-operators-and-symmetry-adapted-functions
title: Projection operators and symmetry-adapted functions - transfer operators, character projectors, partner functions, and block-diagonal Hamiltonians
summary: Given a group acting on a space of functions, the transfer operators P^Γ_kl = (d_Γ/|G|) Σ_g ρ^Γ(g)*_kl Ô_g multiply like matrix units, P^Γ_kl P^Γ'_mn = δ_ΓΓ' δ_lm P^Γ_kn, by the orthogonality theorem. The character projector P^Γ = (d_Γ/|G|) Σ_g χ^Γ(g)* Ô_g needs only the character table. It is the orthogonal projector onto everything that transforms as Γ, and the P^Γ add up to 1. Starting from any function, P^Γ_11 gives a first basis function of Γ and P^Γ_k1 gives its partners. A symmetric Hamiltonian commutes with every P^Γ_kl, so in a symmetry-adapted basis it splits into one block of size n_Γ per irrep, shared by all d_Γ partners. Worked on NH₃/STO-3G in C₃ᵥ: 8 AOs = 4a₁ + 2e, projectors idempotent and complete to 10⁻¹⁶, a Fock coupling of 5 × 10⁻¹⁶ between the a₁ and e blocks, and the occupied MOs 1a₁ 2a₁ 1e 3a₁.
status: in-progress
kind: theory
level: intermediate
tags: [group-theory, projection-operator, transfer-operator, symmetry-adapted-linear-combination, salc, character-projector, partner-functions, block-diagonalization, c3v, ammonia, point-groups]
prerequisites: [groups-representations-and-characters, molecular-symmetry-and-point-groups]
related: [direct-products-and-selection-rules, molecular-orbitals-of-polyatomic-molecules, symmetry-conservation-and-degeneracy, qubit-tapering, spherical-tensor-operators]
key: transfer
order: 20
date: 2026-11-26
---

$G$ is a finite group of order $|G|$. It acts on a space $V$ of functions through linear operators $\hat O_g$ with $\hat O_g\hat O_h=\hat O_{gh}$. For a point-group operation with $3\times3$ matrix $R_g$, $(\hat O_gf)(\mathbf r)=f(R_g^{-1}\mathbf r)$ ([[molecular-symmetry-and-point-groups]]). These operators are unitary for the ordinary inner product.

$\rho^\Gamma(g)$ are the matrices of a unitary irrep $\Gamma$ of dimension $d_\Gamma$, and $\chi^\Gamma(g)=\operatorname{tr}\rho^\Gamma(g)$ its character. A set $\phi_1,\dots,\phi_{d_\Gamma}$ **transforms as** $\Gamma$ (is a set of partners) if

$$
\hat O_g\phi_k=\sum_m\phi_m\,\rho^\Gamma(g)_{mk}\qquad\text{for all }g .
\label{partners}
$$

The orthogonality theorem of [[groups-representations-and-characters]], with $\rho(g^{-1})=\rho(g)^\dagger$ for unitary irreps, reads $\sum_g\rho^\Gamma(g)^*_{kl}\,\rho^{\Gamma'}(g)_{mn}=\frac{|G|}{d_\Gamma}\delta_{\Gamma\Gamma'}\delta_{km}\delta_{ln}$.

## Transfer operators

Define

$$
\hat P^\Gamma_{kl}=\frac{d_\Gamma}{|G|}\sum_{g\in G}\rho^\Gamma(g)^*_{kl}\,\hat O_g .
\label{transfer}
$$

They have three properties.

**They multiply like matrix units.**

$$
\hat P^\Gamma_{kl}\hat P^{\Gamma'}_{mn}=\delta_{\Gamma\Gamma'}\,\delta_{lm}\,\hat P^\Gamma_{kn}.
\label{units}
$$

*Proof.* The product is $\frac{d_\Gamma d_{\Gamma'}}{|G|^2}\sum_{g,h}\rho^\Gamma(g)^*_{kl}\rho^{\Gamma'}(h)^*_{mn}\hat O_{gh}$. Put $u=gh$ and expand $\rho^{\Gamma'}(g^{-1}u)=\sum_j\rho^{\Gamma'}(g^{-1})_{mj}\rho^{\Gamma'}(u)_{jn}$. The sum over $g$ is then $\sum_g\rho^\Gamma(g)^*_{kl}\,\rho^{\Gamma'}(g)_{jm}$, which equals $\frac{|G|}{d_\Gamma}\delta_{\Gamma\Gamma'}\delta_{kj}\delta_{lm}$ by the orthogonality theorem. What remains is $\delta_{\Gamma\Gamma'}\delta_{lm}\hat P^\Gamma_{kn}$. ∎

**They generate partners.** The same manipulation gives $\hat O_h\hat P^\Gamma_{kl}=\sum_m\hat P^\Gamma_{ml}\,\rho^\Gamma(h)_{mk}$. So for any $f$ and fixed $l$, the functions $\phi_k=\hat P^\Gamma_{kl}f$, $k=1\ldots d_\Gamma$, transform as Eq. [[#partners]].

**Their adjoints swap indices.** $\hat P^{\Gamma\dagger}_{kl}=\hat P^\Gamma_{lk}$, because $\hat O_g^\dagger=\hat O_{g^{-1}}$. With Eq. [[#units]] this makes the $\phi_k$ mutually orthogonal and of equal norm.

## The character projector

Summing the diagonal transfer operators removes all dependence on the irrep matrices:

$$
\hat P^\Gamma=\sum_k\hat P^\Gamma_{kk}=\frac{d_\Gamma}{|G|}\sum_{g\in G}\chi^\Gamma(g)^*\,\hat O_g .
\label{projector}
$$

Its properties:

- **Idempotent and Hermitian.** By Eq. [[#units]], $\hat P^\Gamma\hat P^{\Gamma'}=\delta_{\Gamma\Gamma'}\hat P^\Gamma$, and $\hat P^{\Gamma\dagger}=\hat P^\Gamma$. So it is an orthogonal projector.
- **Complete.** $\sum_\Gamma\hat P^\Gamma=\frac1{|G|}\sum_g\big(\sum_\Gamma d_\Gamma\chi^\Gamma(g)^*\big)\hat O_g=\hat 1$. The inner sum is the character of the regular representation, $|G|$ at $g=e$ and 0 otherwise.
- **Its range.** It projects onto the **isotypic subspace** $V^\Gamma$: all of $V$ that transforms as $\Gamma$, which may contain several copies of $\Gamma$. Its rank is $n_\Gamma d_\Gamma$, where $n_\Gamma=\frac1{|G|}\sum_g\chi^\Gamma(g)^*\chi^V(g)$ is the multiplicity.

The character projector needs only the character table. It is enough for one-dimensional irreps, which are all the irreps of an Abelian group. For a degenerate irrep it gives the whole $d_\Gamma n_\Gamma$-dimensional space. Choosing partner functions inside it requires the transfer operators, or another symmetry such as a subgroup chain.

**Recipe for symmetry-adapted linear combinations.**

1. Take one function from a set of equivalent functions, for example the $1s$ of one hydrogen.
2. Apply $\hat P^\Gamma$ for every $\Gamma$. A zero result means that $\Gamma$ does not occur there.
3. For a degenerate $\Gamma$, take the result as $\phi_1=\hat P^\Gamma_{11}f$ and generate partners with $\hat P^\Gamma_{k1}$.
4. Normalize.

## Why the Hamiltonian blocks

If $[\hat H,\hat O_g]=0$ for all $g$, then $\hat H$ commutes with every $\hat P^\Gamma_{kl}$. For partner sets $\phi^{(a)}_k=\hat P^\Gamma_{k1}f_a$ and $\psi^{(b)}_m=\hat P^{\Gamma'}_{m1}f'_b$, moving $\hat P^\dagger=\hat P_{1k}$ across $\hat H$ and using Eq. [[#units]] gives

$$
\langle\phi^{(a)}_k|\hat H|\psi^{(b)}_m\rangle=\delta_{\Gamma\Gamma'}\,\delta_{km}\,h^\Gamma_{ab},\qquad h^\Gamma_{ab}=\langle\phi^{(a)}_1|\hat H|\psi^{(b)}_1\rangle .
\label{blocks}
$$

Two consequences:

- **One block per irrep.** Different irreps do not couple. Within an irrep, different partner rows do not couple.
- **The same block for every row.** The block $h^\Gamma$ (size $n_\Gamma$) is identical for all $d_\Gamma$ rows. Each eigenvalue of $h^\Gamma$ is therefore $d_\Gamma$-fold degenerate.

This is the symmetry-adapted form of Schur's lemma and the finite-group analogue of the Wigner–Eckart theorem ([[spherical-tensor-operators]]). An $n\times n$ problem with $n=\sum_\Gamma n_\Gamma d_\Gamma$ reduces to one $n_\Gamma\times n_\Gamma$ problem per irrep.

**Nonorthogonal bases.** In an AO basis, write $\hat O_g\chi_j=\sum_i\chi_iD_{ij}(g)$. The projectors become matrices $\mathbf P^\Gamma=\frac{d_\Gamma}{|G|}\sum_g\chi^\Gamma(g)^*\mathbf D(g)$ that act on MO coefficient vectors.

- **Not symmetric.** They are idempotent but not symmetric matrices, because $\mathbf D(g)$ is orthogonal only in the metric $\mathbf S$: invariance of the overlap reads $\mathbf D^{\mathsf T}\mathbf S\mathbf D=\mathbf S$.
- **Blocking.** The Fock matrix satisfies $\mathbf D^{\mathsf T}\mathbf F\mathbf D=\mathbf F$, and $\mathbf P^{\Gamma\mathsf T}\mathbf F\mathbf P^{\Gamma'}=0$ for $\Gamma\ne\Gamma'$.

!!! example "NH₃/STO-3G in C₃ᵥ"
    **Setup.** $r_{\text{NH}}=1.012$ Å, HNH angle 106.7°. $C_3$ lies along $z$ and H₁ in the $xz$ plane (one $\sigma_v$). The 8 AOs are N $1s$, $2s$, $2p_x$, $2p_y$, $2p_z$ and three H $1s$.

    **The AO representation.** In $\mathbf D(g)$, the N $s$ functions are invariant, the $2p$ functions rotate with $R_g$ ($\hat O_gp_j=\sum_ip_i(R_g)_{ij}$), and the H $1s$ functions are permuted with their atoms.

    - **Invariance.** $\mathbf D^{\mathsf T}\mathbf S\mathbf D=\mathbf S$ to $3\times10^{-16}$, and $\mathbf D^{\mathsf T}\mathbf F\mathbf D=\mathbf F$ to $3\times10^{-15}$ for the converged Fock matrix.
    - **Characters.** For $(E, 2C_3, 3\sigma_v)$ they are $(8, 2, 4)$. The $2p$ set contributes $1+2\cos120°=0$ under $C_3$ and 1 under $\sigma_v$. The hydrogens contribute the number of atoms left in place.
    - **Decomposition.** With the $C_3v$ table, $n_{A_1}=(8+2\cdot2+3\cdot4)/6=4$, $n_{A_2}=(8+4-12)/6=0$ and $n_E=(16-4)/6=2$. So $\Gamma_{\text{AO}}=4A_1\oplus2E$.

    **Projectors.**

    - **Ranks.** They are 4, 0 and 4, with $|\mathbf P^2-\mathbf P|\le1.1\times10^{-16}$, $\sum_\Gamma\mathbf P^\Gamma=\mathbf 1$ and $\mathbf P^{A_1}\mathbf P^E=0$.
    - **No coupling.** The Fock coupling $\max|\mathbf P^{A_1\mathsf T}\mathbf F\mathbf P^E|$ is $5\times10^{-16}$.
    - **Blocks.** The problem is one $4\times4$ $a_1$ block and one $2\times2$ $e$ block, the latter used twice.

    **Hydrogen SALCs.** Projecting $s_{\text{H}_1}$ gives (H-part coefficients):

    - $\mathbf P^{A_1}s_1=\tfrac13(s_1+s_2+s_3)$;
    - $\hat P^E_{11}s_1=\tfrac23s_1-\tfrac13s_2-\tfrac13s_3$;
    - its partner $\hat P^E_{21}\hat P^E_{11}s_1=0.5774\,(s_2-s_3)$.

    The partners are orthogonal ($2\times10^{-16}$). They transform together, $\mathbf D(C_3)[\phi_1\ \phi_2]=[\phi_1\ \phi_2]\,\rho^E(C_3)$, with $\rho^E$ the $xy$ block of the rotation matrices. They pair with N $2p_x$ and $2p_y$.

    **MOs.** Labelled by projection (largest $\mathbf S$-norm fraction), the RHF MOs are, in $E_h$:

    | occupied | $1a_1$ | $2a_1$ | $1e$ | $3a_1$ |
    |---|---:|---:|---:|---:|
    | $\varepsilon$ | $-15.305$ | $-1.091$ | $-0.573$ (×2) | $-0.353$ |

    | virtual | $4a_1$ | $2e$ |
    |---|---:|---:|
    | $\varepsilon$ | $+0.641$ | $+0.731$ (×2) |

    This is the familiar $1a_1^22a_1^21e^43a_1^2$ configuration, with the lone pair in $3a_1$. The $e$ levels are degenerate as Eq. [[#blocks]] requires.

## In practice

- **Abelian subgroups.** Most programs, PySCF included, symmetry-adapt only within $D_{2h}$ and its subgroups. All their irreps are one-dimensional, so only character projectors are needed and every MO gets a single label. For NH₃ such a program works in $C_s$. The two components of each $e$ pair then fall into different $C_s$ irreps ($a'$ and $a''$), and their degeneracy is not enforced.
- **Symmetry breaking.** Projecting MO coefficients after every SCF step prevents drift into lower symmetry. Whether that is wanted is the question of symmetry-broken solutions ([[rhf-instabilities-and-multiple-solutions]]).
- **Qubit Hamiltonians.** Point-group symmetries show up as $Z$-strings only when every orbital belongs to one irrep of an Abelian group. Tapering needs exactly that ([[qubit-tapering]]).

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010), Appendix 2, Theorem A2.4 (the orthogonality theorem used throughout).

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 4.7, pp. 291-301: classes, characters and the dimensionality theorem for the dihedral group $D_3\cong C_{3v}$.

Neither book treats projection operators. The transfer-operator algebra, its proof from the orthogonality theorem, Eq. [[#blocks]] and the nonorthogonal-basis form are derived here. The statement about PySCF's symmetry handling is general knowledge, not checked in its documentation. Every number is computed in `Claude outputs/part0_math_batchH.py`, section C.
