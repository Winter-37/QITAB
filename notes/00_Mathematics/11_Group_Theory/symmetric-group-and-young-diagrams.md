---
id: symmetric-group-and-young-diagrams
title: The symmetric group and Young diagrams - classes as cycle types, irreps as partitions, the hook-length and hook-content formulas, Schur–Weyl duality, and counting spin states and CSFs
summary: The permutations of N objects form S_N, whose conjugacy classes are the cycle types, so both classes and irreps are labelled by the partitions of N (Young diagrams). The dimension of an irrep is the number of standard Young tableaux, given by the hook-length formula N!/Π hooks. Characters follow from the Murnaghan–Nakayama rule, and transposing a diagram multiplies the character by the sign. Permutations of N particles and unitary changes of the one-particle basis commute, and the N-fold tensor product splits into pairs of matching irreps of S_N and U(n) (Schur–Weyl duality); the U(n) dimension is the hook-content formula. For N spins this reproduces the branching-diagram count of spin-S states. For N electrons the Pauli principle ties the spatial diagram to the transpose of the spin diagram, which gives the number of CSFs in n orbitals (the Weyl–Paldus formula). All checked: Σ(f^λ)² = N! up to N = 8, character orthogonality for S₅–S₇, permutation characters on the spin-S subspaces of six spins, and CSF counts against FCI S² spectra (175 singlets for 6 electrons in 6 orbitals).
status: in-progress
kind: theory
level: intermediate
tags: [group-theory, symmetric-group, permutation-group, young-diagram, young-tableau, hook-length-formula, hook-content-formula, murnaghan-nakayama, schur-weyl-duality, spin-eigenfunctions, branching-diagram, csf, weyl-paldus, unitary-group, guga, pauli-principle]
prerequisites: [groups-representations-and-characters, exchange-symmetry-spin-and-symmetrization-principle, tensor-products-and-partial-trace]
related: [genealogical-coupling, spin-adapted-configurations, lie-groups-and-lie-algebras, direct-products-and-selection-rules, addition-of-angular-momenta, determinant-strings-and-direct-ci, sample-based-quantum-diagonalization]
key: hook
order: 40
date: 2026-11-26
---

$S_N$ is the group of all $N!$ permutations of $N$ objects. A **partition** $\lambda\vdash N$ is a non-increasing list of positive integers $\lambda_1\ge\lambda_2\ge\dots$ summing to $N$. Its **Young diagram** has $\lambda_i$ boxes in row $i$, left-aligned. The **conjugate** (transposed) diagram $\tilde\lambda$ has the column lengths of $\lambda$ as its row lengths. Box $(i,j)$ sits in row $i$ and column $j$, counted from 1.

## Classes and irreps

**Classes are cycle types.** Every permutation is a product of disjoint cycles, and conjugation, $\tau\sigma\tau^{-1}$, relabels the objects inside the cycles without changing their lengths. Two permutations are therefore conjugate exactly when they have the same cycle lengths. The classes of $S_N$ are labelled by partitions $\mu\vdash N$. The class with $m_k$ cycles of length $k$ has

$$
|C_\mu|=\frac{N!}{\prod_kk^{m_k}\,m_k!}
$$

elements. By the counting theorem of [[groups-representations-and-characters]], the number of irreps equals the number of partitions of $N$, $p(N)$: 2, 3, 5, 7, 11, 15, 22 for $N=2\ldots8$.

**Irreps are Young diagrams.** For $S_N$ there is a natural one-to-one labelling of irreps by diagrams $\lambda\vdash N$. Among them:

- $[N]$, one row, is the trivial representation;
- $[1^N]$, one column, is the sign $\operatorname{sgn}\sigma=\pm1$;
- $[N-1,1]$ is the $(N-1)$-dimensional representation on vectors whose components sum to zero.

A **standard Young tableau** fills the diagram with $1\ldots N$, increasing along every row and down every column. The dimension $f^\lambda$ of the irrep is the number of standard tableaux.

**The hook-length formula.** The **hook** of a box is the box itself, the boxes to its right and the boxes below it, and $h(b)$ is the number of boxes in it. Then (Frame, Robinson and Thrall)

$$
f^\lambda=\frac{N!}{\prod_{b\in\lambda}h(b)} .
\label{hook}
$$

*Example.* For $[2,2]$ the hooks are 3, 2, 2, 1, so $f=24/12=2$. Since every irrep appears $f^\lambda$ times in the regular representation, $\sum_\lambda(f^\lambda)^2=N!$. This holds for every $N$ from 2 to 8 by direct computation, ending with $40\,320=8!$ from 22 diagrams.

**Characters.** The Murnaghan–Nakayama rule gives every character. Remove a connected border strip of $\mu_1$ boxes from $\lambda$ in every possible way, weighting each removal by $(-1)^{\text{rows spanned}-1}$, and recurse on the remaining cycles. The character table of $S_4$ (columns are cycle types; each column's class size is shown in parentheses):

| $\lambda$ | $(4)$ (6) | $(3,1)$ (8) | $(2,2)$ (3) | $(2,1,1)$ (6) | $(1^4)$ (1) |
|---|---:|---:|---:|---:|---:|
| $[4]$ | 1 | 1 | 1 | 1 | 1 |
| $[3,1]$ | $-1$ | 0 | $-1$ | 1 | 3 |
| $[2,2]$ | 0 | $-1$ | 2 | 0 | 2 |
| $[2,1,1]$ | 1 | 0 | $-1$ | $-1$ | 3 |
| $[1^4]$ | $-1$ | 1 | 1 | $-1$ | 1 |

The identity column $(1^4)$ gives the dimensions 1, 3, 2, 3, 1 of Eq. [[#hook]]. For $S_5$, $S_6$ and $S_7$ the rows computed this way are orthonormal with the class weights, which confirms the rule.

**Transposition multiplies by the sign.** $\chi^{\tilde\lambda}(\sigma)=\operatorname{sgn}(\sigma)\,\chi^\lambda(\sigma)$, as $[3,1]$ and $[2,1,1]$ show in the table. Rows of a diagram carry symmetric behaviour and columns antisymmetric behaviour. This fact links spin and space below.

## Schur–Weyl duality

Let $N$ particles each have the same $n$-dimensional one-particle space, spanned for example by $n$ orbitals or the two spin states. On $(\mathbb C^n)^{\otimes N}$ two groups act:

- $S_N$, by permuting the particles;
- $U(n)$, by the same one-particle unitary $u$ on every factor, $u\otimes u\otimes\cdots\otimes u$.

The two actions commute: changing the one-particle basis identically for everyone does not care who is who. The theorem states that the space splits into matched pairs,

$$
(\mathbb C^n)^{\otimes N}=\bigoplus_{\lambda\vdash N,\ \ell(\lambda)\le n}V^{U(n)}_\lambda\otimes S^\lambda ,
\label{schur-weyl}
$$

where $S^\lambda$ is the $S_N$ irrep $\lambda$ and $V^{U(n)}_\lambda$ is an irrep of $U(n)$ labelled by the same diagram. Diagrams with more than $n$ rows do not occur. A column longer than $n$ would require antisymmetry in more than $n$ states.

The $U(n)$ dimension is the **hook-content formula** (Arfken and Weber, Eq. (4.125)). Write $n+j-i$ in box $(i,j)$ (that is, $n$ on the diagonal, $n+1$ above it and $n-1$ below it), multiply these numbers and divide by the product of hooks:

$$
\dim V^{U(n)}_\lambda=\prod_{(i,j)\in\lambda}\frac{n+j-i}{h(i,j)} .
\label{hook-content}
$$

Two cases:

- **One row.** $\lambda=[N]$ is the totally symmetric space, with dimension $\binom{n+N-1}{N}$.
- **One column.** $\lambda=[1^N]$ is the totally antisymmetric space, with dimension $\binom nN$, the number of Slater determinants of $N$ spin-less fermions in $n$ orbitals.

## Spin: the branching diagram

**Spin diagrams have two rows.** For $N$ spin-½ particles ($n=2$), only diagrams with at most two rows occur, $\lambda=[N/2+S,\,N/2-S]$. For $U(2)$, Eq. [[#hook-content]] gives dimension $2S+1$, so $\lambda$ labels total spin $S$. By Eq. [[#schur-weyl]], spin $S$ occurs with multiplicity $f^\lambda$. Equivalently, the space of states with given $S$ and $M_S$ carries the $S_N$ irrep $\lambda$. From Eq. [[#hook]] for a two-row diagram,

$$
f^{[N/2+S,\,N/2-S]}=\binom N{N/2-S}-\binom N{N/2-S-1},
$$

which is the number of paths in the branching diagram and the number of genealogical spin functions ([[genealogical-coupling]]).

!!! example "Six spins"
    **Setup.** $\hat S^2$ is built on the $2^6=64$-dimensional space. A permutation operator moves the spin of particle $i$ to particle $\sigma(i)$. All permutations commute with $\hat S^2$ (exactly, error 0).

    **Characters.** On the $M_S=S$ subspace of each spin, the traces of the permutation operators by cycle type $(6),(5,1),\dots,(1^6)$ are as follows. They agree with the Murnaghan–Nakayama characters to every digit.

    | $S$ | multiplicity | diagram | characters on the $M_S=S$ block |
    |---:|---:|---|---|
    | 3 | 1 | $[6]$ | all 1 |
    | 2 | 5 | $[5,1]$ | $-1,0,-1,1,-1,0,2,-1,1,3,5$ |
    | 1 | 9 | $[4,2]$ | $0,-1,1,-1,0,0,0,3,1,3,9$ |
    | 0 | 5 | $[3,3]$ | $0,0,-1,-1,2,1,-1,-3,1,1,5$ |

    **Checks.** The multiplicities $1,5,9,5$ are the dimensions $f^\lambda$ of the four diagrams from Eq. [[#hook]], and the dimension count is $7\cdot1+5\cdot5+3\cdot9+1\cdot5=64$.

## Electrons: space is the transpose of spin

**The spatial diagram.** An $N$-electron wave function must transform as the sign, $[1^N]$, under simultaneous permutation of space and spin coordinates. If its spin part transforms as $\lambda$, its spatial part must transform as a $\lambda'$ such that $\lambda\otimes\lambda'$ contains $[1^N]$. This happens only for $\lambda'=\tilde\lambda$, because $\chi^{\tilde\lambda}=\operatorname{sgn}\cdot\chi^\lambda$. So for spin $S$ the spatial part has the two-column diagram

$$
\tilde\lambda_S=\text{columns of lengths }N/2+S\text{ and }N/2-S .
$$

**The Pauli principle.** In the $U(n)$ irrep with this diagram, a basis is given by the semistandard tableaux. These fill the diagram with orbital labels $1\ldots n$, non-decreasing along rows and strictly increasing down columns. With only two columns, an orbital label can occur at most twice. This is the Pauli principle in diagram form: no orbital holds more than two electrons. This basis is the Gelfand–Tsetlin or Paldus basis of the unitary group approach.

**Counting CSFs.** The number of spin-adapted functions (CSFs) of $N$ electrons in $n$ orbitals with spin $S$, per $M_S$, is $\dim V^{U(n)}_{\tilde\lambda_S}$ from Eq. [[#hook-content]]. In closed form,

$$
N_{\text{CSF}}(n,N,S)=\frac{2S+1}{n+1}\binom{n+1}{N/2-S}\binom{n+1}{N/2+S+1} ,
\label{weyl}
$$

the Weyl–Paldus formula.

!!! example "CSF counts against the S² spectrum of the FCI space"
    For each case, $\hat S^2$ is built in the determinant space of one $M_S$ value with PySCF's `contract_ss`. Its eigenvalues $S(S+1)$ are counted and compared with Eq. [[#hook-content]] for $\tilde\lambda_S$ and with Eq. [[#weyl]].

    | $n$ orbitals, $N$ electrons | determinants ($M_S$) | $S$: count from $\hat S^2$ = hook-content = Weyl–Paldus |
    |---|---:|---|
    | 4, 4 | 36 ($M_S=0$) | 0: 20; 1: 15; 2: 1 |
    | 5, 4 | 100 ($M_S=0$) | 0: 50; 1: 45; 2: 5 |
    | 6, 5 | 300 ($M_S=\tfrac12$) | ½: 210; 3/2: 84; 5/2: 6 |
    | 6, 6 | 400 ($M_S=0$) | 0: 175; 1: 189; 2: 35; 3: 1 |

    - **Agreement.** All three numbers agree in every entry.
    - **Total count.** For $(6,6)$, $\sum_S(2S+1)N_{\text{CSF}}=175+3\cdot189+5\cdot35+7\cdot1=924=\binom{12}{6}$, the full Fock-space sector with six electrons.
    - **Cost of using determinants.** A singlet calculation in a determinant basis carries 400 functions for 175 singlets, which is the price of working with determinants. CI and SQD codes accept it because determinant strings are much easier to handle ([[determinant-strings-and-direct-ci]], [[sample-based-quantum-diagonalization]]).

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 4.4, pp. 274-276, Eqs. (4.123)-(4.125): Young tableaux for SU(n), the link between $S_N$ and SU(n) multiplets, rows symmetric and columns antisymmetric, products with a single box, and the hook-content dimension formula.

Frame, Robinson and Thrall, "The hook graphs of the symmetric group", *Can. J. Math.* **6**, 316-324 (1954), doi:10.4153/CJM-1954-030-1.

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000), Sec. 2.6, Fig. 2.1: the branching diagram up to 12 electrons.

Which parts are from where:

- **General knowledge, not from these sources.** The Murnaghan–Nakayama rule, the statement of Schur–Weyl duality, the semistandard-tableau basis and the names Gelfand–Tsetlin, Paldus and Weyl–Paldus. Each formula is checked numerically instead.
- **Derived here.** The two-row form of the hook-length formula and the transposition argument for the spatial diagram.

Every number is computed in `Claude outputs/part0_math_batchH.py`, section E.
